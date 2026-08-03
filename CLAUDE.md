# Instruções do projeto — Podcast (Áudio Sem Autoestima)

Projeto de análise dos episódios do podcast: transcrição local dos áudios e relatórios de
evolução. Documentos-chave: `ANALISE.md` (pilotos), `ANALISE-EP2.md` (ep. 2), `MODELO-PODCAST.md`
(guia de campo), `BANCO-DE-PAUTAS.md` (pautas). Scripts: `transcrever.py`, `analise_audio.py`,
`analise_conversa.py`.

## Transcrição — sempre na GPU

**Sempre transcrever na GPU** (`device="cuda"`): é muito mais rápido que a CPU.

- Nesta máquina (NVIDIA RTX 4050 Laptop, 6 GB) a GPU roda large-v3 em `float16` sem estourar VRAM.
- **Atenção:** a config padrão do `transcrever.py` (`word_timestamps=True` + `beam_size=5`) **trava
  a tela** no meio da transcrição — reset do driver de vídeo (TDR do Windows), porque a GPU desenha
  a tela e roda o Whisper ao mesmo tempo. Portanto, na GPU use a **config leve**: `beam_size=1` e
  `word_timestamps=False`. O alinhamento por palavra (DTW) é a operação pesada que estoura o
  watchdog; `analise_conversa.py` não usa dados por palavra, então dropá-los não afeta a análise.
- Só cair para CPU se a GPU estiver indisponível.
- O ambiente vive em `.venv` (fora do git). Reconstruir com `pip install -r requirements.txt`.

## Fluxo de trabalho git — após concluir cada tarefa

Ao terminar uma tarefa que alterou arquivos, **não commitar direto na `main`**. Em vez disso:

1. Criar uma branch a partir da `main` (se ainda não houver uma branch de trabalho para a tarefa).
2. Commitar as mudanças nessa branch.
3. `push` da branch para o `origin`.
4. Habilitar o auto-merge no repositório/PR.
5. Abrir um PR da branch para a `main`.
6. Concluir o merge (fechar o PR) via auto-merge.

Assim a `main` avança sempre por PR, nunca por commit direto.
