"""
Transcricao local dos episodios do podcast.

Roda 100% na maquina, nada e enviado para fora. Usa faster-whisper (large-v3)
na GPU quando disponivel, com fallback automatico para CPU.

Uso:
    .venv/Scripts/python.exe transcrever.py                 # transcreve todos os .m4a da pasta
    .venv/Scripts/python.exe transcrever.py --seconds 120   # so os primeiros 120s (teste rapido)
    .venv/Scripts/python.exe transcrever.py arquivo.m4a     # um arquivo especifico
"""

import argparse
import json
import os
import pathlib
import sys
import time

RAIZ = pathlib.Path(__file__).parent
SAIDA = RAIZ / "transcricoes"
TAXA = 16000  # o Whisper trabalha em 16 kHz


def registrar_dlls_cuda() -> None:
    """No Windows o CTranslate2 procura cuBLAS/cuDNN no PATH do processo."""
    base = pathlib.Path(sys.executable).parent.parent / "Lib" / "site-packages" / "nvidia"
    for sub in ("cublas", "cudnn", "cuda_nvrtc"):
        p = base / sub / "bin"
        if p.is_dir():
            os.add_dll_directory(str(p))
            os.environ["PATH"] = str(p) + os.pathsep + os.environ["PATH"]


registrar_dlls_cuda()

from faster_whisper import WhisperModel  # noqa: E402
from faster_whisper.audio import decode_audio  # noqa: E402

# Enviesa o modelo para portugues coloquial brasileiro com pontuacao.
# Sem isso o Whisper tende a "formalizar" a fala e comer as marcas de oralidade,
# que sao justamente o que interessa para analisar papo de bar.
PROMPT_INICIAL = (
    "Conversa informal entre amigos, em portugues brasileiro, gravada num papo de bar. "
    "Tem giria, palavrao, risada, gente falando por cima do outro e piada solta."
)


def formatar_tempo(segundos: float, virgula: bool = False) -> str:
    h = int(segundos // 3600)
    m = int((segundos % 3600) // 60)
    s = int(segundos % 60)
    ms = int((segundos - int(segundos)) * 1000)
    sep = "," if virgula else "."
    return f"{h:02d}:{m:02d}:{s:02d}{sep}{ms:03d}"


def carregar_modelo(tamanho: str = "large-v3"):
    """Tenta GPU primeiro; cai para CPU se a placa nao for suportada."""
    try:
        import ctranslate2

        if ctranslate2.get_cuda_device_count() > 0:
            modelo = WhisperModel(tamanho, device="cuda", compute_type="float16")
            print(f"[modelo] {tamanho} na GPU (float16)")
            return modelo
    except Exception as e:
        print(f"[modelo] GPU indisponivel ({type(e).__name__}: {e}) -- caindo para CPU")

    modelo = WhisperModel(tamanho, device="cpu", compute_type="int8", cpu_threads=16)
    print(f"[modelo] {tamanho} na CPU (int8, 16 threads) -- vai demorar bem mais")
    return modelo


def transcrever(modelo, caminho: pathlib.Path, segundos: int | None = None) -> dict:
    print(f"\n=== {caminho.name} ===")
    t0 = time.time()

    audio = decode_audio(str(caminho), sampling_rate=TAXA)
    duracao_total = len(audio) / TAXA
    if segundos:
        audio = audio[: segundos * TAXA]
        print(f"[teste] limitado a {segundos}s de {duracao_total:.0f}s")
    print(f"[audio] {len(audio) / TAXA:.1f}s decodificados em {time.time() - t0:.1f}s")

    segmentos_iter, info = modelo.transcribe(
        audio,
        language="pt",
        beam_size=5,
        vad_filter=True,  # gravacao de bar tem muito silencio; sem VAD o modelo alucina
        vad_parameters={"min_silence_duration_ms": 500},
        word_timestamps=True,
        initial_prompt=PROMPT_INICIAL,
        condition_on_previous_text=True,
    )

    segmentos = []
    for seg in segmentos_iter:
        segmentos.append(
            {
                "id": seg.id,
                "inicio": round(seg.start, 3),
                "fim": round(seg.end, 3),
                "texto": seg.text.strip(),
                "no_speech_prob": round(seg.no_speech_prob, 4),
                "avg_logprob": round(seg.avg_logprob, 4),
                "palavras": [
                    {"p": w.word.strip(), "i": round(w.start, 3), "f": round(w.end, 3),
                     "prob": round(w.probability, 3)}
                    for w in (seg.words or [])
                ],
            }
        )
        if len(segmentos) % 50 == 0:
            print(f"  ... {len(segmentos)} segmentos ({seg.end:.0f}s)", flush=True)

    decorrido = time.time() - t0
    fala = sum(s["fim"] - s["inicio"] for s in segmentos)
    print(
        f"[pronto] {len(segmentos)} segmentos | {fala:.0f}s de fala em "
        f"{duracao_total:.0f}s de audio | processado em {decorrido:.0f}s"
    )

    return {
        "arquivo": caminho.name,
        "duracao_audio_s": round(duracao_total, 2),
        "duracao_fala_s": round(fala, 2),
        "idioma": info.language,
        "idioma_prob": round(info.language_probability, 3),
        "segundos_processados": round(decorrido, 1),
        "segmentos": segmentos,
    }


def gravar_saidas(dados: dict, destino: pathlib.Path) -> None:
    destino.mkdir(parents=True, exist_ok=True)
    base = pathlib.Path(dados["arquivo"]).stem.replace(" ", "_").replace("(", "").replace(")", "")

    with open(destino / f"{base}.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=1)

    with open(destino / f"{base}.txt", "w", encoding="utf-8") as f:
        f.write(f"# {dados['arquivo']}\n")
        f.write(
            f"# duracao {formatar_tempo(dados['duracao_audio_s'])} | "
            f"fala {formatar_tempo(dados['duracao_fala_s'])} | "
            f"idioma {dados['idioma']} ({dados['idioma_prob']})\n\n"
        )
        for s in dados["segmentos"]:
            f.write(f"[{formatar_tempo(s['inicio'])}] {s['texto']}\n")

    with open(destino / f"{base}.srt", "w", encoding="utf-8") as f:
        for i, s in enumerate(dados["segmentos"], 1):
            f.write(f"{i}\n")
            f.write(
                f"{formatar_tempo(s['inicio'], True)} --> {formatar_tempo(s['fim'], True)}\n"
            )
            f.write(f"{s['texto']}\n\n")

    print(f"[saida] {base}.txt / .srt / .json em {destino}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("arquivos", nargs="*", help="arquivos de audio (padrao: todos os .m4a da pasta)")
    ap.add_argument("--seconds", type=int, default=None, help="limita aos primeiros N segundos")
    ap.add_argument("--model", default="large-v3")
    args = ap.parse_args()

    alvos = [pathlib.Path(a) for a in args.arquivos] or sorted(RAIZ.glob("*.m4a"))
    if not alvos:
        sys.exit("Nenhum arquivo de audio encontrado.")

    print(f"{len(alvos)} arquivo(s): {', '.join(a.name for a in alvos)}")
    modelo = carregar_modelo(args.model)

    for caminho in alvos:
        dados = transcrever(modelo, caminho, args.seconds)
        gravar_saidas(dados, SAIDA)


if __name__ == "__main__":
    main()
