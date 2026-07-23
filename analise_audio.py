"""
Diagnostico tecnico objetivo das gravacoes: niveis, clipping, piso de ruido,
proporcao de silencio e teste de separacao de canais L/R.

Nao opina sobre conteudo -- so mede o que da para medir.
"""

import pathlib

import av
import numpy as np

RAIZ = pathlib.Path(__file__).parent


def carregar_estereo(caminho: pathlib.Path):
    """Decodifica preservando os dois canais separados, em float32 -1..1."""
    with av.open(str(caminho)) as container:
        stream = container.streams.audio[0]
        taxa = stream.rate
        blocos = []
        resampler = av.AudioResampler(format="fltp", layout="stereo", rate=taxa)
        for frame in container.decode(stream):
            for f in resampler.resample(frame):
                blocos.append(f.to_ndarray())
    dados = np.concatenate(blocos, axis=1)
    return dados, taxa


def db(x: float) -> float:
    return 20 * np.log10(max(x, 1e-10))


def analisar(caminho: pathlib.Path) -> None:
    print(f"\n{'=' * 62}\n{caminho.name}\n{'=' * 62}")
    dados, taxa = carregar_estereo(caminho)
    canais, amostras = dados.shape
    dur = amostras / taxa
    print(f"canais={canais}  taxa={taxa} Hz  duracao={dur / 60:.1f} min")

    # --- Teste de canais: os dois lados sao microfones diferentes ou mono duplicado?
    if canais == 2:
        L, R = dados[0], dados[1]
        dif = np.abs(L - R)
        corr = float(np.corrcoef(L, R)[0, 1])
        print(f"\n-- CANAIS --")
        print(f"correlacao L/R: {corr:.6f}")
        print(f"diferenca media |L-R|: {np.mean(dif):.8f}   maxima: {np.max(dif):.8f}")
        if corr > 0.9999 and np.max(dif) < 1e-4:
            print(">> MONO DUPLICADO: um microfone so. Nao da para separar por canal.")
        elif corr > 0.98:
            print(">> Quase identicos: microfone unico, talvez com leve diferenca estereo.")
        else:
            print(">> CANAIS DISTINTOS: possivel separar falantes por canal!")

    mono = dados.mean(axis=0)

    # --- Niveis
    pico = float(np.max(np.abs(mono)))
    rms = float(np.sqrt(np.mean(mono**2)))
    print(f"\n-- NIVEIS --")
    print(f"pico:  {db(pico):6.1f} dBFS")
    print(f"RMS:   {db(rms):6.1f} dBFS  (alvo de fala: -20 a -16)")
    print(f"crest factor: {db(pico) - db(rms):.1f} dB")

    # --- Clipping
    clip = int(np.sum(np.abs(mono) >= 0.999))
    print(f"amostras clipadas: {clip} ({100 * clip / len(mono):.4f}%)")

    # --- Janelas de 100 ms para silencio / piso de ruido
    jan = int(taxa * 0.1)
    n = len(mono) // jan
    janelas = mono[: n * jan].reshape(n, jan)
    rms_jan = np.sqrt(np.mean(janelas**2, axis=1))
    rms_db = 20 * np.log10(np.maximum(rms_jan, 1e-10))

    piso = float(np.percentile(rms_db, 10))
    mediana = float(np.percentile(rms_db, 50))
    alto = float(np.percentile(rms_db, 90))
    print(f"\n-- DINAMICA (janelas de 100 ms) --")
    print(f"piso de ruido (p10): {piso:6.1f} dBFS")
    print(f"mediana (p50):       {mediana:6.1f} dBFS")
    print(f"trechos altos (p90): {alto:6.1f} dBFS")
    print(f"relacao sinal/ruido aprox: {alto - piso:.1f} dB  (bom: >35 dB)")

    limiar = piso + 8
    silencio = float(np.mean(rms_db < limiar))
    print(f"proporcao de silencio/ruido baixo: {100 * silencio:.1f}%")

    # --- Distribuicao de energia ao longo do tempo (blocos de 5 min)
    print(f"\n-- ENERGIA POR BLOCO DE 5 MIN --")
    por_bloco = int(taxa * 300)
    for i in range(0, len(mono), por_bloco):
        bloco = mono[i : i + por_bloco]
        if len(bloco) < taxa * 10:
            continue
        r = float(np.sqrt(np.mean(bloco**2)))
        barra = "#" * int(max(0, (db(r) + 60) / 2))
        print(f"  {i // taxa // 60:3d}-{min(len(mono), i + por_bloco) // taxa // 60:3d} min: "
              f"{db(r):6.1f} dBFS {barra}")


if __name__ == "__main__":
    for f in sorted(RAIZ.glob("*.m4a")):
        analisar(f)
