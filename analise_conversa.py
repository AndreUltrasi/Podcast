"""
Analise quantitativa da conversa a partir dos JSON de transcricao.

O celular aplicou controle automatico de ganho, o que achatou a energia do audio
(todos os blocos de 5 min medem o mesmo dBFS). Entao a "curva de energia" da
conversa tem que ser derivada do ritmo da FALA, nao do volume:
densidade de palavras, tamanho dos segmentos e pausas.

CUIDADO: segmento do Whisper NAO e turno de fala. A gravacao e mono com
microfone unico, entao nao ha diarizacao -- nao da para saber quem falou nem
contar trocas de voz. A contagem de segmentos mede a granularidade com que o
Whisper cortou o audio, e essa granularidade muda sozinha ao longo do arquivo
(na Parte 1 cai de ~6 para ~2,9 palavras/segmento por volta do minuto 22 e
volta a ~4,9 por volta do minuto 56). Medido nesse material, a contagem de
segmentos correlaciona -0,888 com palavras/segmento e so 0,324 com a taxa de
fala. Use palavras/min como medida de ritmo; leia segmentos apenas como
diagnostico da propria transcricao.
"""

import json
import pathlib
import re
from collections import Counter

RAIZ = pathlib.Path(__file__).parent
TRANS = RAIZ / "transcricoes"

# Palavras vazias para o mapa de assuntos
VAZIAS = set("""
a o e que de do da em um uma os as para com nao na no se por mais como mas
foi ele ela eu voce tu nos eles isso isto essa esse aquele la ali aqui ja
ta tao entao ai né ne pra pro tem ter tinha vai vou ir e eh ah oh uh hum
muito bem so tudo todo toda todos todas ser sou sao era eram fica ficou
sabe acho achei acha cara mano tipo assim tambem tambm porque por que qual
quando onde quem cade meu minha seu sua dele dela nosso nossa
q vc pq de_novo ok tá tô né? sim nao? nada algo alguma algum coisa coisas
faz fazer fez feito dar deu dou da_pra pode podia posso quer quero queria
tava tavam estava estavam esta estao esse essa isso aquilo mesmo mesma
ver vi visto vendo falar falou fala falando disse dizer diz
""".split())


def carregar(caminho: pathlib.Path) -> dict:
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def mmss(s: float) -> str:
    return f"{int(s // 60):02d}:{int(s % 60):02d}"


def detectar_loops(segs: list) -> list:
    """Whisper as vezes trava repetindo a mesma frase. Sinaliza isso."""
    achados = []
    for i in range(len(segs) - 2):
        t = segs[i]["texto"].strip().lower()
        if len(t) > 8 and t == segs[i + 1]["texto"].strip().lower() == segs[i + 2]["texto"].strip().lower():
            achados.append((segs[i]["inicio"], t))
    return achados


def suspeitos(segs: list) -> list:
    """Segmentos com baixa confianca -- candidatos a alucinacao."""
    return [s for s in segs if s["avg_logprob"] < -1.0 or s["no_speech_prob"] > 0.6]


def curva_ritmo(segs: list, dur: float, janela: int = 120) -> list:
    """Palavras por minuto em janelas -- proxy de energia da conversa.

    A ultima janela quase sempre e parcial; normalizar por `janela` fixo
    subestimaria o ppm dela proporcionalmente ao quanto falta para fechar.
    """
    n = int(dur // janela) + 1
    palavras = [0] * n
    segmentos = [0] * n
    for s in segs:
        idx = min(int(s["inicio"] // janela), n - 1)
        palavras[idx] += len(s["texto"].split())
        segmentos[idx] += 1
    out = []
    for i in range(n):
        real = min(janela, dur - i * janela)
        if real <= 0:
            continue
        out.append({
            "inicio": i * janela,
            "dur": real,
            "parcial": real < janela,
            "ppm": palavras[i] / (real / 60),
            "segmentos": segmentos[i],
            "pps": palavras[i] / segmentos[i] if segmentos[i] else 0.0,
        })
    return out


def lacunas(segs: list, minimo: float = 3.0) -> list:
    """Silencios longos entre segmentos -- possiveis pontos mortos."""
    out = []
    for a, b in zip(segs, segs[1:]):
        g = b["inicio"] - a["fim"]
        if g >= minimo:
            out.append({"inicio": a["fim"], "dur": g, "antes": a["texto"][-60:], "depois": b["texto"][:60]})
    return out


def termos(segs: list, n: int = 40) -> list:
    txt = " ".join(s["texto"].lower() for s in segs)
    txt = re.sub(r"[^\wáàâãéêíóôõúüç\s]", " ", txt)
    palavras = [w for w in txt.split() if len(w) > 3 and w not in VAZIAS]
    return Counter(palavras).most_common(n)


def relatorio(dados: dict) -> None:
    segs = dados["segmentos"]
    dur = dados["duracao_audio_s"]
    total_palavras = sum(len(s["texto"].split()) for s in segs)

    print(f"\n{'=' * 68}\n{dados['arquivo']}\n{'=' * 68}")
    print(f"duracao: {mmss(dur)}  |  fala detectada: {mmss(dados['duracao_fala_s'])} "
          f"({100 * dados['duracao_fala_s'] / dur:.0f}%)")
    print(f"segmentos: {len(segs)}  |  palavras: {total_palavras}  "
          f"|  {total_palavras / (dur / 60):.0f} palavras/min")

    loops = detectar_loops(segs)
    print(f"\n-- QUALIDADE DA TRANSCRICAO --")
    print(f"loops de repeticao: {len(loops)}")
    for t, txt in loops[:5]:
        print(f"   [{mmss(t)}] {txt[:70]}")
    susp = suspeitos(segs)
    print(f"segmentos de baixa confianca: {len(susp)} ({100 * len(susp) / len(segs):.1f}%)")
    for s in susp[:8]:
        print(f"   [{mmss(s['inicio'])}] logprob={s['avg_logprob']:.2f} "
              f"nospeech={s['no_speech_prob']:.2f} | {s['texto'][:60]}")

    print(f"\n-- RITMO DA CONVERSA (janelas de 2 min) --")
    print("   ppm = medida de ritmo. segs/pps = granularidade do Whisper,")
    print("   NAO troca de voz: em mono com microfone unico nao ha diarizacao.")
    print("   tempo    ppm   segs   pps")
    cur = curva_ritmo(segs, dur)
    cheias = [c for c in cur if not c["parcial"] and c["ppm"] > 0]
    ppms = sorted(c["ppm"] for c in cheias)
    med = ppms[len(ppms) // 2] if ppms else 0
    for c in cur:
        barra = "#" * int(c["ppm"] / 6)
        if c["parcial"]:
            marca = f"  <<< PARCIAL ({c['dur']:.0f}s)"
        elif c["ppm"] > med * 1.25:
            marca = "  <<< ALTA"
        elif c["ppm"] < med * 0.7:
            marca = "  <<< baixa"
        else:
            marca = ""
        print(f"   {mmss(c['inicio'])}  {c['ppm']:5.0f}  {c['segmentos']:5d}  "
              f"{c['pps']:4.1f}  {barra}{marca}")
    print(f"   mediana: {med:.0f} ppm  (janelas parciais fora)")

    print(f"\n-- PAUSAS LONGAS (>3s) --")
    lac = lacunas(segs)
    print(f"total: {len(lac)}  |  tempo morto somado: {mmss(sum(l['dur'] for l in lac))}")
    for l in sorted(lac, key=lambda x: -x["dur"])[:10]:
        print(f"   [{mmss(l['inicio'])}] {l['dur']:4.1f}s  ...{l['antes']} || {l['depois']}...")

    print(f"\n-- TERMOS MAIS FREQUENTES --")
    linha = []
    for w, c in termos(segs):
        linha.append(f"{w}({c})")
    print("   " + ", ".join(linha))


if __name__ == "__main__":
    for j in sorted(TRANS.glob("*.json")):
        relatorio(carregar(j))
