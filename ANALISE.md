# Análise dos pilotos — Áudio de Baixa Autoestima

## Leitura de dois minutos

Este documento é a **fonte histórica e probatória** dos dois arquivos-piloto. Ele registra o
que foi ouvido, medido e inferido; quando uma conclusão é apenas editorial ou não pode ser
demonstrada pela gravação, isso está indicado. Para transformar os achados em prática, use o
[guia de campo](MODELO-PODCAST.md). Para escolher e preparar assuntos, consulte o
[banco de pautas](BANCO-DE-PAUTAS.md).

**Material analisado:** duas partes de uma mesma gravação, feitas em 18 e 19 de julho de
2026: `18-07-2026 22.22(2).m4a`, com 61min 09s, e `19-07-2026 01.03.m4a`, com 26min 01s.
A transcrição integral em `transcricoes/` foi produzida localmente com Whisper large-v3; as
métricas de captação foram medidas diretamente nos arquivos com `analise_audio.py`.

### Cinco achados principais

| O que aconteceu | Evidência | Implicação |
|---|---|---|
| A conversa se sustentou no primeiro piloto. | Na Parte 1, 87% do arquivo contém fala, com 176 palavras/min e só 1min 02s de pausas acima de 3s. | O problema demonstrado não é falta de conteúdo nem de química; é estrutura. |
| A segunda parte chegou mais perto do ritmo desejado. | A mediana das janelas de 2 min é 143 palavras/min; ela tem 78% de fala e 1,61s de pausa longa por minuto no miolo, ficando 19% mais lenta e com ~60% mais pausa que a Parte 1. | O exemplo de ritmo mais próximo do *low vibe* já está gravado, embora a troca de bar tenha prejudicado a abertura. |
| Assuntos diferentes convergiram para um mesmo eixo. | Zé do Caixão, régua alta, Whindersson Nunes, autismo, anime, cinema brasileiro e relações voltam à distância entre identidade e exigência social. | O nome *Baixa Autoestima* já conversa com um território editorial demonstrado pelo piloto. |
| Os apresentadores ocupam posições complementares. | Gabriel julga a realização; André procura significado, com discordância real sobre o mesmo objeto. | A tensão entre “o que a coisa é” e “o que ela significa” sustenta conversa sem exigir oposição artificial. |
| Processo e captação limitaram o material. | A abertura livre morreu em 90s; nenhum dos dois lembrava bem o filme; a madrugada trouxe cansaço; os arquivos têm mono duplicado, picos acima de 0 dBFS e 49.178/62.088 amostras clipadas. | Preparação mínima, um local-base, teto de duração e dois canais com ganho manual atacam falhas que já aparecem na gravação. |

### Como usar esta análise

- Leia **Método e material** para saber o que foi medido e o que não pode ser afirmado.
- Leia **O que os pilotos provaram** para entender ritmo e eixo editorial.
- Leia **Onde funciona** e **Onde perde força** para decidir o que repetir e o que mudar.
- Leia **Diagnóstico técnico** antes de escolher o equipamento e o lugar da próxima gravação.
- Volte a **Limitações metodológicas** antes de tratar qualquer inferência como fato.

> Baseado na transcrição integral dos dois arquivos (`transcricoes/`), feita localmente com
> Whisper large-v3. Toda afirmação aqui aponta para um timestamp. Onde eu não tenho certeza,
> está escrito que não tenho.
>
> Timestamps no formato `[P1 mm:ss]` e `[P2 mm:ss]`, em minutos corridos de cada arquivo.

---

## 1. Método e material

### 1.1 O que são esses arquivos

**Não são dois episódios. São um episódio só, em duas partes, com troca de bar no meio.**

A Parte 2 abre confirmando isso, sem margem para dúvida:

> `[P2 00:52]` *"Como é que a gente volta?"* — *"A gente parou pra mijar."*
> `[P2 00:58]` *"A gente tava num bar na Freicaneca... Agora a gente tá num karaokê da Augusta."*

E a Parte 1 termina exatamente onde a Parte 2 diz que terminou:

> `[P1 61:02]` *"Eu vou no banheiro, meu. Já volto aí."* — *"Quer dar pausa aí?"* — *"Melhor, melhor."*

| | Parte 1 | Parte 2 |
|---|---|---|
| Arquivo | `18-07-2026 22.22(2).m4a` | `19-07-2026 01.03.m4a` |
| Duração | 61min 09s | 26min 01s |
| Local | Bar Vila Coqueiros, calçada da Frei Caneca | Karaokê perto da Praça Rússia, transversal da Augusta |
| Início | 22:22 | 01:03 |
| Palavras | 10.739 | 3.755 |
| Densidade total (palavras ÷ duração) | 176 palavras/min | 144 palavras/min |
| Fala / silêncio | 87% fala | 78% fala |
| Tempo morto (pausas >3s) | 1min 02s no total | 1min 28s no total |

**Apresentadores:** Gabriel e André `[P1 00:09]`. Primeiro episódio, declarado no ar `[P1 00:17]`.

**Nome:** ***Áudio de Baixa Autoestima*** (confirmado pelos apresentadores). No piloto a
transcrição recebeu como *"Áudio Sem Autoestima Podcast"* `[P1 00:04]`, mas o nome certo é
*Baixa Autoestima*. Seja como for, ele conversa bem com o eixo editorial que vocês acharam sem
perceber (seção 2.3).

**O filme:** *O Estranho Mundo de Zé do Caixão* (1968), de José Mojica Marins — três curtas
numa antologia. Vocês nunca acertam o título no ar (`[P1 00:56]` *"O Mundo de Zé do Castelo.
Eu acho que é esse o nome."*), então deduzi pelo conteúdo, não por metadado: *"são três
curtas"* `[P1 02:13]`, o fabricante de bonecas cujos olhos são reais demais `[P1 02:32]`,
`[P1 05:29]` (**O Fabricante de Bonecas**), e o corcunda dos balões com o par de sapatos
`[P1 14:11]`, `[P1 15:45]` (**Tara**). Confere antes de publicar — mas se estiver certo, isso
já é o primeiro "não vale porra nenhuma" do programa.

### 1.2 Como a evidência foi tratada

- Os timestamps apontam para minutos corridos de cada arquivo, não para episódios distintos.
- Palavras por minuto, proporção de fala, pausas, pico, RMS, clipping e faixa dinâmica vêm da
  transcrição ou da medição direta do áudio; os métodos e as ressalvas aparecem junto de cada
  resultado.
- A gravação mono não permite diarização confiável. Toda atribuição individual é feita por
  cadeia de evidência e está marcada como tal.
- Segmentos do Whisper não são turnos de conversa. A curva que confundia essas duas coisas
  foi descartada, e a razão estatística está registrada na seção 2.2.
- A identificação do filme é uma dedução pelo conteúdo. A leitura do melhor trecho e dos
  papéis é juízo editorial, não resultado automático de uma métrica.

---

## 2. O que os pilotos provaram

### 2.1 O número mais importante deste documento — e a faca de dois gumes

**87% de fala — e só 1 minuto disso em pausas longas.**

Os dois números medem coisas diferentes, então vale separar: dos 61min09s da Parte 1, o
Whisper detecta fala em 52min57s. Os 8min12s restantes não são silêncio constrangido — são
respiração, sobreposição, ruído de bar e as beiradas de cada frase. **O que interessa é o
tempo morto de verdade: as pausas acima de 3 segundos somam 1min02s no arquivo inteiro.**

Isso não é normal em episódio piloto. O padrão de podcast estreante é o oposto: pausas
constrangidas, gente esperando o outro puxar assunto, blocos que morrem. Vocês gravaram uma
hora com 176 palavras por minuto e praticamente nenhum buraco.

**Agora o outro lado, que só apareceu depois.** Quando vocês nomearam a referência de tom —
Ben-Yur e os podcasts do Petry, o clima *low vibe* — esse número deixou de ser só boa notícia.
Não existe pausa constrangida, e isso continua ótimo. Mas também **não existe respiro nenhum**,
e é isso que um programa low vibe tem de sobra.

As duas metades não são iguais, e a diferença é grande:

| | Parte 1 (bar) | Parte 2 (karaokê) |
|---|---|---|
| Mediana por janela de 2 min | 176 palavras/min | **143 palavras/min** |
| Proporção de fala | 87% | **78%** |
| Pausa longa por minuto (miolo) | 1,02s | **1,61s** |

**A Parte 2 é 19% mais lenta e tem ~60% mais pausa no miolo.** Este documento a trata como a
metade fraca porque ela abre mal, aos 92 ppm — e isso continua verdade. Mas o *ritmo* dela é o
mais próximo do tom que vocês querem. O modelo de como soar já está gravado; é o segundo
arquivo, não o primeiro.

*(Os 3,38 s/min brutos da Parte 2 incluem o teste de microfone e a despedida — o número
comparável é o do miolo, 1,61.)*

→ Alvo de ritmo e o que fazer com isso em [MODELO-PODCAST.md](MODELO-PODCAST.md), seção "A energia".

E as poucas pausas longas que existem quase todas têm causa externa, não constrangimento:

| Timestamp | Duração | O que era |
|---|---|---|
| `[P1 14:24]` | 25,8s | Alguém abordando vocês na calçada |
| `[P1 55:36]` | 6,3s | Falha de áudio — o que vem depois sai ininteligível (ver §5) |
| `[P1 47:14]` | 4,7s | Hesitação real ("mas..." / "sei lá") |
| `[P1 36:09]` | 4,2s | Pausa de argumento |

A de `[P1 55:36]` é a única que não é nem incidente nem hesitação: os 11 segmentos seguintes
`[P1 55:43–56:00]` vêm com confiança despencada (logprob −2,37) e saem como *"umca"*, *"fi"*,
*"um hp"*. Não é vocês travando — é a gravação falhando. É o mesmo trecho que interrompe a
melhor ideia da noite (seção 3.2).

**Conclusão:** o problema de vocês não é conteúdo nem química. É estrutura. Isso é uma
posição muito melhor de partida do que o contrário — dá para consertar estrutura, não dá
para fabricar química.

---

### 2.2 O ritmo da conversa — e o que não dá para medir

O celular aplicou controle automático de ganho, o que achatou o volume — todos os blocos de
5 min medem entre −11,4 e −12,1 dBFS. Então o volume não diz nada sobre energia.

**E o que eu queria medir aqui, não dá.** O ideal seria a densidade de turnos: quantas vezes
vocês trocam de voz por minuto. Só que a gravação é mono com microfone único (§5), então não
existe diarização — não há como saber quem falou. Qualquer curva de "turnos" neste material é
inventada, e eu voltei atrás de uma que estava aqui: contar segmentos do Whisper parecia
funcionar, mas o Whisper muda a granularidade do corte sozinho no meio do arquivo, e a
contagem acaba medindo a transcrição, não a conversa. Detalhe no fim da seção.

O que sobra é medida honesta: **palavras por minuto.**

```
Parte 1 — palavras/min por janela de 2 min

10:00  ###################################  215   <<< mais denso
22:00  ##################################   205
38:00  #################################    202
42:00  #################################    202
08:00  #################################    199
50:00  #################################    198
30:00  ###############################      188
...
26:00  #######################              138
28:00  ######################               134
14:00  ##################                   112   <- abordagem na calçada

mediana: 176 ppm     (janela final, de 70s, descartada por ser parcial)
```

A leitura muda: **a Parte 1 não tem um pico, tem um platô.** Fora do buraco da abordagem na
calçada, a conversa fica entre 134 e 215 palavras/min do começo ao fim — a janela dos 58 min
marca 177, praticamente a mediana. Não há curva de aquecimento nem queda de energia para
explicar. Vocês entraram no ritmo no primeiro minuto e ficaram nele.

Dito isso, **o melhor trecho do episódio é entre 30 e 43 minutos** — e isso é juízo editorial
meu, não número. O que o número faz é não desmentir: `[P1 38:00]` e `[P1 42:00]` estão entre
as janelas mais densas do arquivo, 202 ppm contra mediana de 176. O que está acontecendo ali
não é o filme — é a discussão sobre régua alta, autenticidade e Whindersson Nunes. O filme foi
a rampa; o assunto de verdade veio depois.

Na Parte 2 a curva diz algo que a da Parte 1 não dizia: ela **abre com 92 palavras/min, o valor
mais baixo das duas gravações inteiras**, e fecha em 108 contra mediana de 143. A abertura é
pura reorientação — *"Tira agora"*, *"Começou?"*, *"Como é que a gente volta?"* — e a janela
ainda inclui os 26,7s de teste de microfone, o que é exatamente o custo da troca de bar sendo
cobrado. O fim é cansaço, e vocês dizem isso no ar (§4.7).

> **Nota de método.** A curva que estava aqui antes contava segmentos do Whisper e os chamava
> de turnos. Não são: na Parte 1 o Whisper corta a ~6 palavras por segmento até o minuto 22,
> cai para ~2,9 até o minuto 56, e volta para ~4,9 no fim. O "pico de 134 aos 30 min" e a
> "queda para 51 aos 60 min" são essa mudança, mais a última janela ser parcial. Medindo:
> a contagem de segmentos correlaciona **−0,888** com palavras por segmento e só **0,324** com
> a taxa de fala. Ela media a transcrição. Saiu.

---

### 2.3 O eixo editorial que vocês acharam sem perceber

Este é o achado principal da análise.

Vocês falaram de coisas aparentemente desconexas: um filme de terror dos anos 60, Whindersson
Nunes, autismo, anime japonês, cinema brasileiro, relações não-heteronormativas. **É tudo o
mesmo assunto.** Olha a sequência:

| Timestamp | Assunto aparente | O que estava sendo dito de verdade |
|---|---|---|
| `[P1 01:30–36:40]` | Zé do Caixão | Um cara assumiu ser o que era, e pagou o preço |
| `[P1 36:46–39:00]` | "A régua muito alta" | A gente se cobra um padrão que não alcança |
| `[P1 39:30–46:00]` | Whindersson Nunes | Chegou onde queria e está deprimido |
| `[P1 47:50–52:30]` | Autismo | Tem gente que biologicamente não consegue caber no padrão |
| `[P1 52:40–55:30]` | Anime e dorama | O japonês desenha o eu que não consegue ser |
| `[P1 56:27–59:30]` | Cinema brasileiro | "Povão" e "consciente" — dois padrões brigando |
| `[P2 01:19–20:45]` | Relações e geração Z | O padrão de família está deixando de ser obrigatório |

**O tema do podcast é: a distância entre quem você é e o que o mundo exige que você seja.**

Vocês voltam a isso sozinhos, de sete ângulos diferentes, ao longo de 87 minutos, sem nunca
nomear. Está tudo condensado numa frase do André sobre ele mesmo:

> `[P1 47:45]` *"Eu acho que eu sou menos André do que eu gostaria de ser."*

E o nome do podcast — *Baixa Autoestima* — já aponta para lá. Vocês acertaram o nome antes de
saber qual era o programa.

---

## 3. Onde funciona

| O que aconteceu | Evidência | Implicação |
|---|---|---|
| Os dois ocuparam papéis diferentes diante do mesmo objeto. | Gabriel cobrou execução; André defendeu significado e autenticidade. | A discordância nasce do modo de olhar, não de um papel inventado. |
| A rua entrou no programa sem quebrá-lo. | Na abordagem da vendedora, vocês atenderam, explicaram o incidente e voltaram à conversa. | O ambiente pode gerar conteúdo quando é reconhecido no ar. |
| Vulnerabilidade e deboche coexistiram. | André se assume autista e Gabriel responde com o teste do BuzzFeed. | Esse contraste já entrega o tom demonstrado pelo piloto. |

### 3.1 Os papéis — e por que o par funciona

**Confiança:** os papéis estão claros e sustentados por várias evidências. A atribuição
linha a linha, não — é gravação mono, microfone único, com muita fala sobreposta. Onde eu
digo "Gabriel" ou "André" abaixo, é por cadeia de evidência, não por reconhecimento de voz.

#### Gabriel — o cético do ofício
Julga a coisa em si. Quer saber se é bem feito.

> `[P1 01:55]` *"Mas vendo esse filme, eu achei uma bosta. Uma bosta imensa."*
> `[P1 24:55]` *"Eu não aprendo nada vendo esse curta. (...) Você não absorve nada substancial."*
> `[P1 24:30]` *"Quando você vai fazer arte (...) você tem que fazer de um jeito que as pessoas se interessem em assistir. Eu não vou assistir seu filme de graça."*

#### André — o advogado do significado
Julga o que a coisa representa. Sobe para sociedade, essência, autenticidade.

> `[P1 09:21]` *"Ele virou uma identidade, uma persona que tá ligada muito ao terror. Eu acho que isso é muito saudável."*
> `[P1 35:29]` *"Apesar de não ter dinheiro, apesar de não ter meios, ele fez do jeito dele. E pra mim isso é foda pra caralho, é uma referência."*
> `[P1 34:51]` *"Vem de Sócrates, na verdade. Sócrates falava que o sapo sapeia, a girafa girafeia..."*

**Isso é um par de podcast legitimamente bom.** Não é "dois amigos concordando" — é uma
oposição estrutural real: *o que a coisa É* contra *o que a coisa SIGNIFICA*. Essa tensão
não se esgota, porque não tem resposta certa. Dá para rodar em cima dela por anos.

#### E tem uma ironia de personagem pronta

André sugeriu o filme `[P1 00:59]` e não assistiu direito — viu uma análise no YouTube e leu o
roteiro depois `[P1 18:48]`. Gabriel assistiu e detestou. O programa inteiro começa com o cara
que indicou o filme defendendo um filme que ele não viu, contra o cara que viu.

> `[P1 01:04]` *"Eu assisti e o filho da puta não assistiu."*
> `[P1 01:11]` *"Não vale porra nenhuma, cara. Você não vai saber falar isso de nada, entendeu?"*
> `[P1 18:48]` *"Você tá repetindo o que você viu no vídeo de análise."*

Isso é ouro de personagem. Não conserta — **transforma em hábito natural** (ver
`MODELO-PODCAST.md`).

---

### 3.2 Momentos de ouro

Trechos que já são conteúdo publicável do jeito que estão.

| Timestamp | O quê | Por que funciona |
|---|---|---|
| `[P1 42:20–43:25]` | Vendedora aborda a mesa; vocês atendem, recusam com educação, e viram pro microfone: *"galera, pra quem só tão ouvindo, a gente tá na calçada, e sempre aparece alguém tentando vender alguma coisa"* | É papo de bar com o bar dentro. Vocês já souberam o que fazer com isso, no reflexo. |
| `[P1 43:51–44:02]` | Whindersson: *"cadê aquele Whindersson Nunes feliz que eu lembro há 10 anos atrás"* / *"nossa, a alma dele foi embora"* | Assunto popular, dor real, os dois com posições diferentes |
| `[P1 47:50–48:20]` | André se assume autista, Gabriel corta com *"você fez um teste no BuzzFeed"* | Vulnerabilidade + deboche imediato. É exatamente o tom do programa. |
| `[P1 52:40–53:30]` | Tese do anime: *"é o japonês criando imagem do que ele queria ser, mas não consegue"* | Ideia original, própria de vocês, não é opinião reciclada |
| `[P2 15:06]` | *"Amar gasta energia."* | Frase de corte. Brutal e curta. |
| `[P2 16:24]` | *"É muito mais difícil pro homem chorar na frente de um amigo. Isso é um fato que não tem como você negar."* | Assunto sério, atingido de raspão, deixado para trás em 45s |
| `[P2 23:33]` | *"A opinião da grande massa é fezes."* | Provocação real, com o outro discordando na hora |

### O que repetir

- Partir de um objeto concreto e deixar que ele abra assuntos maiores.
- Sustentar a diferença entre execução e significado sem atribuir papéis artificiais.
- Reconhecer no microfone o que acontece ao redor, como vocês fizeram com a abordagem na
  calçada.
- Deixar vulnerabilidade e deboche ocuparem o mesmo trecho, sem transformar um no antídoto
  do outro.
- Perseguir ideias próprias que surgem no desvio, como a tese do anime, e frases curtas que
  condensam uma posição, como *"Amar gasta energia."*

---

## 4. Onde perde força

| O que aconteceu | Evidência | Implicação |
|---|---|---|
| A conversa livre não encontrou partida. | Em 90 segundos, vocês abandonaram a abertura e recorreram ao filme. | O papo livre funciona depois que um ponto concreto aquece a conversa. |
| O objeto foi preparado pela metade. | Os dois esqueceram trechos do filme e declararam não saber sua história. | O bloco rendeu apesar da preparação; não por causa dela. |
| Concordância encerrou o raciocínio. | “Acho que sim” se repetiu cinco vezes em quatro segundos e mais três logo depois. | É preciso perguntar pelo motivo da concordância para continuar pensando junto. |
| A mudança de lugar e a madrugada cobraram ritmo. | A Parte 2 começa em 92 palavras/min e termina quando vocês dizem estar bêbados e cansados. | A gravação precisa proteger começo, duração e energia. |

### 4.1 A abertura falhou, e vocês disseram isso no ar

O roteiro previa "conversa livre" primeiro, depois o filme `[P1 00:46]`. A conversa livre durou
**90 segundos** antes de vocês desistirem:

> `[P1 00:46]` *"Primeiro a gente vai tentar começar com uma conversa livre. Eu não sei se isso vai funcionar."*
> `[P1 01:24]` *"Não tenho ideia nenhuma do que falar, então vai ser sobre o filme."*

A dúvida do Gabriel em `[P1 00:46]` estava certa. Papo livre não é ponto de partida — é o que
acontece **depois** que um objeto concreto esquenta a conversa. Vocês provaram isso na
prática: o filme puxou 35 minutos, e desses 35 nasceu a melhor parte do episódio.

### 4.2 Nenhum dos dois tinha visto o filme direito

Isso limitou o bloco o tempo todo:

> `[P1 17:30]` *"Caralho, velho, eu não lembro também."*
> `[P1 29:01]` *"Porra, eu não lembro do final direito."*
> `[P1 36:23]` *"Não sei porra nenhuma da história do Zé do Caixão."* — *"Eu também não sei."*

E ainda assim rendeu 35 minutos. É o argumento mais forte a favor do formato: **com
preparação de verdade, esse bloco vira o melhor do programa.**

### 4.3 "Tá ligado" — 116 vezes em 87 minutos

Uma vez a cada 45 segundos. Somando "entendeu" (39×), "sei lá", "tipo" e "cara", boa parte
do texto é enchimento. No áudio passa. **Em vídeo, com o rosto de vocês na tela, vira a
única coisa que a pessoa escuta.**

Não é para eliminar — é vício de fala natural, e matar isso mata a naturalidade. É para
derrubar de 116 para uns 30. Só ter consciência já resolve metade.

### 4.4 O "é um dado" — o furo mais sério

O trecho sobre Japão e autismo `[P1 48:00–52:30]` circula por quatro minutos sem sair do lugar,
porque a discussão inteira se apoia num número que ninguém tem:

> `[P1 50:10]` *"Lá o nível de namoros no Japão é abaixo da média."*
> `[P1 50:16]` *"Isso é verdade? É um fato?"* — *"Deve ser."* — *"É um dado."* — *"Eu não sei. Mas é um dado."*
> `[P1 50:39]` *"É um dado aleatório."*

Vocês perceberam ao vivo e mesmo assim seguiram. Quatro minutos de trilho falso. A solução
proposta em `MODELO-PODCAST.md` não é cortar nem criar um quadro: é admitir “não sei”, anotar e
seguir.

### 4.5 Quando vocês concordam, a conversa para de andar

Aqui não tenho número — tenho a transcrição, que é mais direta. Duas vezes, com um minuto de
distância, a discussão simplesmente trava em concordância:

> `[P1 42:16–42:20]` *"acho que sim"* — *"acho que sim"* — *"acho que sim"* — *"acho que sim"* — *"acho que sim"*
> `[P1 43:41–43:43]` *"acho que sim"* — *"acho que sim"* — *"não, acho que sim"*

Cinco vezes em quatro segundos, e mais três logo depois. O que separa os dois blocos é a
vendedora chegando na mesa `[P1 42:20]` — ou seja: **o que destravou a conversa não foi vocês,
foi a rua.** Sem a interrupção, não dá para saber quanto tempo o *"acho que sim"* ia durar.

E note onde isso acontece: no meio do trecho que eu chamo de melhor do episódio. Não é falta
de assunto nem cansaço — é o modo padrão de dois amigos conversando, que é justamente o que
não funciona em podcast.

**O problema não é concordar — é parar de pensar junto.** Vocês concordam na conclusão e
divergem no motivo quase sempre; o *"acho que sim"* é o que acontece quando ninguém desce até
o motivo. A saída é perguntar *por que você acha isso?*, não fingir o lado contrário. Tratado
em [MODELO-PODCAST.md](MODELO-PODCAST.md).

### 4.6 As viradas de assunto são sem cerimônia

> `[P1 36:44]` *"Agora vamos falar. Qual que é o próximo tópico?"*
> `[P2 25:05]` *"Então o próximo assunto, então."*

Funciona, mas é plano. E o encerramento foi improvisado — vocês perguntaram no ar como se faz,
e só então improvisaram uma despedida:

> `[P2 25:28]` *"Como é que encerra o podcast?"*
> `[P2 25:32]` *"Galera, muito obrigado por participar dessa jornada que estamos tentando fazer funcionar."*

A despedida improvisada até é simpática. O problema é que ela nasce depois da pergunta ficar
gravada.

### 4.7 A madrugada cobrou

Os avisos estão todos gravados:

> `[P1 43:32]` *"Eu tô muito bêbado."*
> `[P1 47:23]` *"Tô bêbado."*
> `[P2 25:12]` *"Acho que eu tô bêbado, entendeu?"*
> `[P2 25:19]` *"Eu tô cansado. Melhor a gente parar esse podcast por aqui."*

A Parte 2 não acabou porque o assunto acabou — acabou porque vocês acabaram. O tema das
relações estava vivo, com discordância aberta, quando encerrou.

### O que mudar

- Abrir com um ponto concreto, sem exigir que a conversa livre produza o próprio começo.
- Quando filme, livro ou outra obra for o objeto central, fazer os dois chegarem com o objeto
  consumido de verdade.
- Reduzir os vícios de fala por consciência, sem tentar esterilizar a conversa.
- Diante de um dado incerto, assumir a incerteza e não deixar uma afirmação sem base sustentar
  quatro minutos de raciocínio.
- Quando houver concordância, perguntar pelo motivo em vez de fingir discordância.
- Preparar uma despedida fixa e evitar que a madrugada decida o encerramento.

---

## 5. Diagnóstico técnico da gravação

| O que aconteceu | Evidência | Implicação |
|---|---|---|
| O gravador achatou voz e ambiente. | A faixa dinâmica ficou em 12,6 dB na Parte 1 e 8,5 dB na Parte 2, com controle automático de ganho. | O ruído ficou perto da voz; edição posterior não recupera a separação perdida. |
| Os dois arquivos cliparam. | Os picos chegaram a +0,7 e +1,0 dBFS, com 49.178 e 62.088 amostras clipadas. | A distorção já está impressa no arquivo. |
| As vozes não podem ser tratadas separadamente. | O áudio é mono duplicado e a correlação L/R é 1,000000. | É preciso captar cada pessoa em seu próprio canal. |

Medido direto no arquivo, com `analise_audio.py`.

| Métrica | Parte 1 | Parte 2 | Alvo |
|---|---|---|---|
| Canais | mono duplicado | mono duplicado | 2 canais separados |
| Pico | **+0,7 dBFS** | **+1,0 dBFS** | ≤ −3 dBFS |
| RMS | −11,8 dBFS | −10,2 dBFS | −20 a −16 dBFS |
| Amostras clipadas | **49.178** | **62.088** | 0 |
| Faixa dinâmica (p90−p10) | **12,6 dB** | **8,5 dB** | > 35 dB |

Sobre a última linha: ela é a distância entre os trechos altos e os trechos baixos, medida em
janelas de 100 ms. Costuma servir de aproximação de sinal/ruído, mas aqui **não é sinal/ruído
de verdade** — com o ganho automático ligado, o p10 não é o piso de ruído do bar, é o piso
*depois* de o celular ter subido o volume dele. O número real seria pior, não melhor. Serve
para comparar as duas partes entre si e para dizer que está ruim; não serve para especificar
equipamento.

**Três problemas, em ordem de gravidade:**

1. **Faixa dinâmica de 8,5–12,6 dB.** O ruído do bar está quase no mesmo volume da voz de
   vocês. Esse é o teto de qualidade de tudo — nenhuma edição conserta. Note que a Parte 2
   está pior (8,5 dB): à 1h da manhã o bar estava mais cheio.
2. **Está clipando.** Picos acima de 0 dBFS, ~50 a 62 mil amostras estouradas por arquivo.
   Distorção permanente, gravada no arquivo.
3. **Microfone único, em mono.** Correlação entre os canais L e R deu exatamente 1,000000 —
   os dois lados são idênticos. Não dá para equilibrar as vozes nem separar quem falou.

O ganho automático do celular ainda piora o quadro: ele sobe o volume no silêncio, o que
levanta o ruído do bar junto e achata a dinâmica (crest factor de 12,5 dB; fala normal fica
em 15–20 dB).

---

## 6. Limitações metodológicas

Esta análise não transforma inferência em certeza. Os limites que precisam acompanhar seus
achados são estes:

- **Transcrição:** o Whisper large-v3 pode errar nomes e palavras. A grafia do nome do
  programa e a identificação de *O Estranho Mundo de Zé do Caixão* precisam de confirmação.
- **Vozes:** o microfone único e o mono duplicado impedem diarização. As atribuições a Gabriel
  e André são sustentadas por contexto, não por reconhecimento de voz.
- **Energia:** o controle automático de ganho mantém os blocos de 5 min entre −11,4 e
  −12,1 dBFS. Volume, portanto, não serve como medida de energia neste material.
- **Turnos:** a segmentação do Whisper muda durante o arquivo. Contar segmentos mede a
  transcrição, não a alternância entre apresentadores; por isso essa curva foi retirada.
- **Faixa dinâmica:** p90−p10 funciona aqui para comparar as partes e demonstrar um problema,
  mas não é uma medição real de sinal/ruído e não especifica equipamento.
- **Juízo editorial:** chamar o trecho entre 30 e 43 minutos de melhor parte é uma leitura
  humana. As janelas de 202 ppm não a contradizem, mas também não a provam sozinhas.
- **Escopo:** há um único piloto, dividido em dois arquivos e gravado na mesma noite. Os
  resultados descrevem este material; não demonstram sozinhos como o programa se comportará
  em outras pautas, lugares ou estados de sobriedade.

### Fechamento probatório

**O que vocês já têm, e é a parte difícil:**

- Química real, medida: 87% de fala e só 1 minuto de pausa longa, em um primeiro episódio
- Uma oposição de papéis que se sustenta sozinha e não se esgota
- Um eixo editorial coerente, que vocês encontraram sem procurar
- Reflexo bom para incidente ao vivo (a abordagem na calçada)
- Um nome que já combina com o programa

**O que falta, e é a parte fácil:**

- Começo e fim sempre iguais (nos pilotos são improvisados, e falham)
- Quando houver objeto central, preparação mínima — os dois consumirem de verdade
- Um jeito de não desabar em concordância — descer ao motivo, não fingir o lado contrário
- Ritmo: baixar dos 176 palavras/min e deixar o silêncio existir
- Parar aos 60 minutos, num bar só, começando mais cedo
- Dois microfones e desligar o ganho automático

Nada na lista de falta é sobre talento. É tudo processo.

→ Formato proposto em [MODELO-PODCAST.md](MODELO-PODCAST.md)

→ Pautas concretas em [BANCO-DE-PAUTAS.md](BANCO-DE-PAUTAS.md)
