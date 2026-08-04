# Análise do episódio 2 — Áudio Sem Autoestima

> **Relatório de evolução.** Este documento mede o segundo episódio contra o que os pilotos
> provaram ([ANALISE.md](ANALISE.md)) e contra os alvos do guia de campo
> ([MODELO-PODCAST.md](MODELO-PODCAST.md)). A pergunta que ele responde não é "o episódio é
> bom?", e sim **"o que evoluiu desde os pilotos, e o que ainda falta?"**
>
> Baseado na transcrição integral de `podcast 2.m4a.mp4` (`transcricoes/podcast_2.m4a.*`), feita
> localmente com Whisper large-v3, e na medição direta do áudio com `analise_audio.py`. Toda
> afirmação aponta para um timestamp; onde não tenho certeza, está escrito que não tenho.
>
> Timestamps no formato `[E2 mm:ss]`, em minutos corridos do arquivo único. Timestamps dos
> pilotos aparecem como `[P1 mm:ss]` / `[P2 mm:ss]`, como no documento original.

---

## Leitura de dois minutos

**Material:** um episódio só, `podcast 2.m4a.mp4`, **76min 30s**, gravado numa pizzaria na
Augusta `[E2 00:26]`. Apresentadores Gabriel e André, os mesmos. O nome se confirma: abriram
como *"Baixa Autoestima"*, se corrigiram no ar — *"Áudio sem autoestima podcast. Eu errei."*
`[E2 00:23]`. O objeto foi o filme ***Amor Sem Medidas*** (Leandro Hassum como um homem
baixinho) — exatamente a semente que ficou escolhida no ar no fim do piloto `[P1 60:08]`.

### Cinco achados principais

| O que aconteceu | Evidência | Implicação |
|---|---|---|
| A captação deu um salto real. | Clipping foi de 49.178/62.088 amostras para **0**; o pico caiu de +0,7/+1,0 para **−2,4 dBFS**; a faixa dinâmica dobrou (8,5–12,6 → **19,8 dB**), sinal de que o ganho automático foi desligado. | Dos três problemas técnicos dos pilotos, dois foram resolvidos. Sobra um. |
| O eixo editorial deixou de ser acidente e virou motor. | A pergunta principal foi **preparada e escrita** — *"Como a pressão externa do mundo transforma a gente?"* `[E2 07:36]` — e o episódio inteiro gira em torno dela: Hassum, Superman, Batman, Kafka. | Nos pilotos vocês acharam o eixo sem perceber; agora vocês partiram dele de propósito. |
| Os vícios que dá para medir caíram. | *"Tá ligado"* foi de **116× em 87 min** (1,33/min) para **34× em 76 min** (0,45/min). O *"acho que sim"* aparece 17× mas **espalhado**, sem o estouro dos pilotos (5× em 4s), e vocês passaram a perguntar *"por quê / fale quais partes"* `[E2 52:37]`. | As notas do piloto sobre vício de fala e concordância pegaram. |
| O ritmo **não** desacelerou e o tempo estourou. | 171 palavras/min no total, mediana de **171 ppm** por janela — praticamente igual ao P1 (176) e longe do alvo (~150). Só **1min 22s** de pausa longa em 76 min. Duração **76min 30s**, acima do teto de 60, com um fim-falso aos `[E2 59:29]` ignorado. | O *low vibe* — desacelerar, deixar ar, parar aos 60 — é o que ainda não aconteceu. |
| A melhor parte foi uma história; a pior foi quando a pauta secou. | Pico de **228 ppm** na história do sofá do pai do André `[E2 35:16–40:51]`; vale de **116 ppm** quando o assunto *"não rendeu"* e viraram meta-conversa sobre o próprio podcast `[E2 48:00–54:00]`. | Seguir a história (como o guia manda) funcionou; depender da pauta travou. |

### Como ler o resto

- **§1** confirma o que foi medido e o que não posso afirmar (segue mono; sem diarização).
- **§2 — Placar do modelo** é o coração deste documento: item por item do guia, *aplicou ou não*.
- **§3** mostra onde funcionou; **§4**, onde perdeu força.
- **§5** é o diagnóstico técnico lado a lado com os pilotos.
- **§6** repete as limitações metodológicas — leia antes de tratar inferência como fato.

---

## 1. Método e material

**É um episódio só, num arquivo só.** Diferente dos pilotos (uma noite em dois arquivos, com
troca de bar no meio), aqui não há corte: 76min 30s contínuos.

| | Piloto (P1+P2) | **Episódio 2** |
|---|---|---|
| Arquivos | `18-07...m4a` + `19-07...m4a` | `podcast 2.m4a.mp4` |
| Duração | 61min + 26min | **76min 30s** |
| Local | bar na Frei Caneca → karaokê na Augusta | pizzaria na Augusta `[E2 00:26]` |
| Palavras | 10.739 + 3.755 | **13.095** |
| Fala / silêncio | 87% / 78% | **86%** |
| Densidade total | 176 / 144 ppm | **171 ppm** (mediana por janela: **171**) |
| Pausa longa (>3s) | 1min 02s / 1min 28s | **1min 22s** (14 pausas) |

**Objeto:** o filme *Amor Sem Medidas* (Leandro Hassum). Um dos dois **assistiu e anotou** —
*"Eu anotei aqui. Eu fiz o meu trabalho."* `[E2 06:36]`; o outro **não viu** — *"A gente
combina de ver um filme… e você não viu."* `[E2 05:58]`. A mesma dinâmica do piloto, com os
papéis provavelmente trocados. Como é gravação mono, não confirmo por voz quem é quem; atribuo
por cadeia de evidência e sinalizo quando o faço.

Ressalvas de transcrição estão em §6. A principal: o áudio segue **mono** (não há como saber
quem falou). A transcrição foi refeita com `beam_size=5`, o que limpou os artefatos da primeira
versão (a alucinação de *"É…"* no silêncio do fim sumiu; loops de repetição caíram de 33 para 2).
O trecho de menor confiança que resta é a discussão da grafia de *besouro* `[E2 61:32–61:52]`,
por causa da fala sobreposta — mas o conteúdo é inteligível.

---

## 2. Placar do modelo — o que o guia pediu e o que aconteceu

Cada linha é um item do [MODELO-PODCAST.md](MODELO-PODCAST.md), com o veredito e a evidência.

| Item do guia | Veredito | Evidência |
|---|---|---|
| **Abertura curta**, sem a "conversa livre" que morreu em 90s no piloto | ✅ **Melhorou** | Abriram direto no assunto (a "pizza do ator" → Hassum) `[E2 00:26–01:15]`. Não houve os 90s mortos do `[P1 01:24]`. Não é a fórmula exata "onde estamos / quem fala / pergunta da noite", mas cumpre a função. |
| **Pergunta principal preparada** | ✅ **Aplicado** | Escrita antes: *"Como a pressão externa do mundo transforma a gente?"* `[E2 07:36]`. É uma pergunta sem resposta certa e que toca o eixo — exatamente o pedido do guia. |
| **Objeto consumido de verdade pelos dois** | ⚠️ **Meio** | Um assistiu e anotou `[E2 06:36]`; o outro não viu `[E2 05:58]`. A preparação melhorou de um lado; a regra "os dois consomem" segue quebrada. |
| **Ritmo ~150 ppm e deixar o ar existir** | ❌ **Não aplicado** | 171 ppm de mediana (≈ P1), 86% de fala, só 1min 22s de pausa longa. Continua sem respiro — o número que o piloto já apontava como faca de dois gumes. |
| **Não desabar em "acho que sim"; descer ao motivo** | ✅ **Melhorou** | 17 ocorrências, mas **espalhadas** (as mais próximas a 24s), sem o estouro do `[P1 42:16]` (5× em 4s). E vocês perguntam o motivo: *"Cara, eu concordo em parte." — "Fale quais partes."* `[E2 52:37]`. |
| **Um local-base, sem refazer a operação em outro lugar** | ✅ **Melhorou** | Ficaram na pizzaria/bar; cogitaram descer para o Parlapatões `[E2 49:44]` mas o núcleo não migrou. Sem o recomeço a 92 ppm do `[P2 00:00]`. |
| **Teto de 60 minutos; encerrar com assunto vivo** | ❌ **Não aplicado** | 76min 30s. Houve um fim-falso — *"Vamos encerrar"* `[E2 59:29]` — e seguiram +17 min. O fim veio por sono, não por escolha: *"tá com sono, mano"* `[E2 76:00]`. |
| **Despedida fixa** *("Isso foi Áudio Sem Autoestima. Até a próxima.")* | ❌ **Não aplicado** | A frase não aparece. Encerraram improvisando: *"Vamos encerrar? — Vamos. — Fecha aí, velho."* `[E2 76:09]`. Menos constrangido que o *"como é que encerra o podcast?"* `[P2 25:28]`, mas ainda improvisado. |
| **"Não sei é resposta"; não sustentar quatro minutos em dado incerto** | ✅ **Melhorou** | Na dúvida da grafia de *besouro*, conferiram na hora em vez de especular `[E2 61:10]`. Não houve o trilho falso de quatro minutos do *"é um dado"* `[P1 50:16]`. |
| **Fazer a conexão em voz alta** | ⚠️ **Meio** | Acertaram um callback ao piloto — *"essa foi discutida no podcast passado, que a gente falou do Mojica"* `[E2 19:02]`. Mas **perderam** a conexão mais óbvia do episódio: a barata de Kafka `[E2 60:06]` é o eixo em estado puro e virou piada de pronúncia (§4). |
| **Captação: 2 microfones, canais separados, ganho manual, sem clipping** | ⚠️ **Meio** | Ganho manual e níveis: resolvidos (§5). Dois microfones/canais: **não** — segue mono duplicado, um microfone só. |

**Resumo do placar:** dos itens verificáveis, a maioria melhorou ou foi aplicada. Os três que
**não** foram — ritmo ~150, teto de 60 min e dois microfones — são os que sobram, e são todos de
disciplina/equipamento, não de conteúdo.

---

## 3. Onde funcionou

### 3.1 O eixo virou o motor do episódio

Nos pilotos, o tema — *a distância entre quem você é e o que o mundo exige que você seja* —
apareceu sem vocês perceberem. No episódio 2 ele é o ponto de partida declarado, e vocês o
atacam de vários ângulos, todos o mesmo assunto:

| Timestamp | Assunto aparente | O que estava sendo dito de verdade |
|---|---|---|
| `[E2 07:36–11:00]` | O filme do Hassum | A pressão do mundo (ser baixinho, ser julgado) transforma a pessoa |
| `[E2 13:11–16:28]` | Superman | O mundo tentou corrompê-lo e não conseguiu: *"a sociedade tinha tudo pra corrompê-lo e mesmo assim ele não foi corrompido"* |
| `[E2 14:22–17:00]` | Batman | Riqueza + trauma: o que a gente decide fazer com o molde que recebeu |
| `[E2 16:34–16:53]` | Hassum de novo | *"Se ele fosse mais Leandro e menos Leandrinho…"* — o nome vira a própria tese |
| `[E2 60:06]` | Kafka | Virar um inseto: a metamorfose de quem não cabe |
| `[E2 51:53–54:11]` | O próprio podcast | *"A gente começa a performar quando está gravando"* — não ser você diante da lente |

*"Se o mundo não te pune, não te instrui a ser o que você quer ser, você não vira ninguém"*
`[E2 10:00]` é a frase que condensa tudo — e é a mesma ideia do André sobre si mesmo no piloto
(*"sou menos André do que gostaria"* `[P1 47:45]`). **O programa agora sabe qual é o programa.**

### 3.2 Os papéis se mantiveram — e continuam se sustentando

A oposição do piloto seguiu de pé (atribuição por contexto, não por voz):

- **Gabriel — a execução:** julga se a coisa é bem-feita. Acha o Batman não-admirável *"é um
  bilionário que prefere descer na porrada"* `[E2 14:40]`; duvida que o filme do Hassum
  enriqueça a cultura `[E2 19:12]`.
- **André — o significado:** sobe para o que a coisa representa. Traz a pergunta do eixo
  `[E2 07:36]`, defende que o Hassum foi *"corrompido, talvez positivamente"* `[E2 16:34]`, lê o
  Superman como mito do imigrante `[E2 13:37]`.

A mesma tensão *o que a coisa É × o que ela SIGNIFICA* — que o piloto disse que dava para rodar
por anos — rodou o episódio 2 inteiro.

### 3.3 Momentos de ouro

| Timestamp | O quê | Por que funciona |
|---|---|---|
| `[E2 35:16–40:51]` | **A história do sofá do pai do André**: a intimação no correio, o funcionário estressado, o reencontro em que viram amigos porque as duas vidas se espelham | É o trecho mais denso do episódio (228 ppm) e o mais bem contado. Um causo com arco completo, exatamente o "desvio que ganhou força" que o guia manda deixar acontecer. |
| `[E2 13:11–17:00]` | Superman × Batman × Hassum | Ideia própria, na veia do eixo, com os dois em posições diferentes sem briga fabricada. |
| `[E2 16:47]` | *"Se ele fosse mais Leandro e menos Leandrinho"* | Uma frase que é a tese do programa inteiro, dita de passagem. Corte curto pronto. |
| `[E2 08:38]` | *"Olhei pro meu pênis e falei: você tem potencial"* (dos pequenos frascos, os grandes perfumes) | Humor de bar cru e curto. Vídeo vertical autossuficiente. |
| `[E2 51:53–54:11]` | A auto-análise: *"a gente começa a performar quando está gravando… as ideias não me alcançam quando a gente grava"* | Vulnerabilidade real sobre o próprio ofício. É *Sem Autoestima* aplicado a eles mesmos. |
| `[E2 19:02]` | Callback ao piloto: *"isso foi discutido no podcast passado, quando a gente falou do Mojica"* | Começa a costurar uma continuidade entre episódios. |

---

## 4. Onde perde força

### 4.1 O ritmo não baixou — e agora vocês sabem que era pra baixar

Este é o item mais importante que **não** mudou. A mediana ficou em 171 ppm — praticamente o P1
(176) —, a fala é 86% do arquivo e há só 1min 22s de pausa longa em 76 min. O piloto já dizia: não existe
pausa constrangida, o que é ótimo, **mas também não existe respiro nenhum**, e é disso que um
programa *low vibe* vive. O episódio 2 acelerou de novo. Não é falta de assunto; é hábito de
disputar cada fresta da conversa.

### 4.2 Estourou o tempo — e ignorou o próprio fim

Aos `[E2 59:29]` um de vocês disse *"Vamos encerrar"*. Vocês seguiram **mais 17 minutos**, e
esses minutos são os mais fracos: a discussão da grafia de *besouro* e, depois, o arrastar
cansado até o *"tá com sono, mano"* `[E2 76:00]`. O episódio passou dos 60 min do guia (76min
30s) e terminou por exaustão — o mesmo desfecho dos pilotos (*"tô cansado, melhor a gente
parar"* `[P2 25:19]`). O fim-falso aos 59 min era o lugar de parar.

### 4.3 A conexão de ouro foi enterrada numa piada

Logo depois de discutir como o mundo transforma a pessoa, um de vocês diz que está sem energia,
que *"o ar não vai sair do meu pulmão"* `[E2 60:03]`, e o outro responde: *"você vai virar uma
barata igual o Kafka"* `[E2 60:06]`. **A Metamorfose é o eixo do programa em estado puro** — um
homem que acorda virado inseto, que não cabe mais no próprio mundo. Era o momento de fazer a
conexão em voz alta (o guia pede isso explicitamente). Em vez disso, a conversa virou **quatro
minutos discutindo se se fala "besouro" ou "bizoro"** `[E2 60:14–62:27]`. A tangente é divertida
e natural — mas a ideia boa ficou no chão. É o mesmo padrão do *"amar gasta energia"* do piloto,
que também passou batido.

### 4.4 A pauta secou no meio, e o buraco virou meta-conversa

O vale de energia do episódio (116–117 ppm, `[E2 48:00–54:00]`) começou quando o assunto
acabou: *"Ah, eu achei que ia render mais esse assunto." — "Eu também."* `[E2 50:05]`. A saída
foi falar sobre o próprio podcast — que vocês *"performam quando gravam"*. Isso rendeu um dos
melhores trechos (§3.3), mas veio de um buraco, não de um plano; é exatamente o risco de depender
da pauta em vez de deixar uma história puxar a próxima. Note o contraste: o **pico** do episódio
(a história do sofá) não era pauta nenhuma — era um causo.

### 4.5 O objeto, de novo, só um consumiu

*"A gente combina de ver um filme… e você não viu."* `[E2 05:58]`. O bloco ainda rendeu — como
no piloto — mas a regra do guia (quando a obra é central, **os dois** consomem) segue quebrada.
A boa notícia é que o lado que preparou preparou de verdade: assistiu, anotou e trouxe a pergunta
principal `[E2 06:36]`.

---

## 5. Diagnóstico técnico — o salto real

Medido direto no arquivo com `analise_audio.py`.

| Métrica | Piloto P1 | Piloto P2 | **Episódio 2** | Alvo |
|---|---|---|---|---|
| Canais | mono dup. | mono dup. | **mono dup. (corr. L/R 1,000000)** | 2 canais separados |
| Pico | +0,7 dBFS | +1,0 dBFS | **−2,4 dBFS** | ≤ −3 dBFS |
| RMS | −11,8 | −10,2 | **−15,5 dBFS** | −20 a −16 |
| Amostras clipadas | 49.178 | 62.088 | **0** | 0 |
| Crest factor | 12,5 | — | **13,1 dB** | 15–20 (fala normal) |
| Faixa dinâmica (p90−p10) | 12,6 | 8,5 | **19,8 dB** | > 35 |

**Dois dos três problemas dos pilotos foram resolvidos:**

1. **Clipping zerou.** Era o problema #2 (distorção gravada no arquivo, irreversível). Não há
   mais nenhuma amostra estourada. O pico ficou em −2,4 dBFS, dentro da margem do guia.
2. **A faixa dinâmica quase dobrou** (8,5–12,6 → 19,8 dB) e o piso de ruído despencou para
   −31,5 dBFS. Nos pilotos, a energia por bloco de 5 min era achatada (−11,4 a −12,1) pelo ganho
   automático; aqui ela varia (−14,6 a −16,6) e o piso é muito mais baixo. **Isso é a assinatura
   do ganho automático desligado** — a recomendação central do §8 do guia.

**Sobra um, o mais caro:**

3. **Ainda é um microfone só.** A correlação entre os canais L e R deu exatamente 1,000000: os
   dois lados são idênticos. Continua impossível separar as vozes, equilibrar quem falou ou fazer
   diarização confiável. É o único item de captação do guia que não foi atacado — e é o que exige
   comprar/posicionar um segundo microfone, não só mudar um ajuste.

A relação sinal/ruído aproximada (19,8 dB) segue abaixo do alvo (>35), mas subiu muito. Como no
piloto, esse número serve para comparar e para dizer que ainda dá para melhorar, não para
especificar equipamento.

---

## 6. Limitações metodológicas

- **Transcrição:** Whisper large-v3 na GPU, com `beam_size=5` e sem timestamps por palavra (o
  alinhamento por palavra travava a tela). A qualidade do texto é alta (idioma pt, prob. 1,0; só
  0,3% de segmentos de baixa confiança; 2 loops de repetição). Ainda assim nomes e grafias podem
  sair errados — confira *Amor Sem Medidas* e os nomes próprios antes de citar em público.
- **Trecho de menor confiança:** a discussão da grafia de *besouro* `[E2 61:32–61:52]` sai com
  confiança mais baixa (fala sobreposta), mas é inteligível. Esta versão foi regravada com
  `beam_size=5`, o que eliminou a alucinação de *"É…"* que a primeira transcrição (beam 1) tinha
  no silêncio do fim.
- **Vozes:** áudio mono, um microfone. **Não há diarização.** Toda atribuição a "Gabriel" ou
  "André" neste documento é por cadeia de evidência (quem é chamado pelo nome, quem conta a
  história de qual familiar), não por reconhecimento de voz.
- **Ritmo:** palavras/min é medida honesta; contagem de segmentos, não (a granularidade do
  Whisper muda sozinha) — por isso a curva de "turnos" foi descartada, como nos pilotos.
- **Ganho automático desligado:** é a leitura mais provável para a dinâmica ter dobrado, mas é
  inferência a partir da medição, não confirmação de como vocês configuraram o gravador.
- **Juízo editorial:** chamar a história do sofá de melhor trecho, ou a barata de Kafka de
  conexão perdida, é leitura humana. As janelas de 228 e 116 ppm não contradizem essas leituras,
  mas também não as provam sozinhas.
- **Escopo:** é um episódio. Descreve este material; não prova sozinho como o programa se
  comportará nas próximas pautas.

---

## Fechamento

**O que evoluiu (e é a parte que costuma ser difícil):**

- A captação: clipping zerado, níveis no alvo, dinâmica dobrada, ganho automático desligado.
- O eixo deixou de ser sorte e virou intenção — com uma pergunta principal preparada.
- Os vícios mensuráveis caíram: *"tá ligado"* despencou, o *"acho que sim"* não desabou, e vocês
  passaram a descer ao motivo.
- Um local-base, sem a troca de bar que afundou o piloto.
- A melhor parte nasceu de uma história solta, não de uma pauta — que é como o guia diz que tem
  que ser.

**O que ainda falta (e é a parte fácil — é processo e equipamento):**

- Baixar o ritmo dos 171 ppm rumo aos ~150 e **deixar o silêncio existir**.
- Parar aos 60 minutos — e respeitar o próprio fim-falso quando ele aparecer.
- Uma despedida fixa, para o cansaço não decidir o encerramento.
- Fazer a conexão em voz alta quando ela aparecer (a barata de Kafka era de graça).
- Os dois consumirem o objeto, quando houver objeto.
- **Um segundo microfone, em canal separado** — o último problema técnico de pé.

Nada na lista de falta é sobre talento nem sobre química. As duas coisas difíceis — química e um
eixo editorial — vocês já provaram nos pilotos e confirmaram aqui. O que falta é disciplina de
gravação e um microfone.

→ Método e baseline dos pilotos em [ANALISE.md](ANALISE.md) · Guia de campo em
[MODELO-PODCAST.md](MODELO-PODCAST.md) · Pautas em [BANCO-DE-PAUTAS.md](BANCO-DE-PAUTAS.md)
