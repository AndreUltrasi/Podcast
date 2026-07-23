# Análise dos pilotos — Áudio Sem Autoestima

> Baseado na transcrição integral dos dois arquivos (`transcricoes/`), feita localmente com
> Whisper large-v3. Toda afirmação aqui aponta para um timestamp. Onde eu não tenho certeza,
> está escrito que não tenho.
>
> Timestamps no formato `[P1 mm:ss]` e `[P2 mm:ss]`, em minutos corridos de cada arquivo.

---

## 1. O que são esses arquivos

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
| Densidade | 176 palavras/min | 144 palavras/min |
| Fala / silêncio | 87% fala | 78% fala |
| Tempo morto (pausas >3s) | 1min 02s no total | 1min 28s no total |

**Apresentadores:** Gabriel e André `[P1 00:09]`. Primeiro episódio, declarado no ar `[P1 00:17]`.

**Nome:** *"Áudio Sem Autoestima Podcast"* `[P1 00:04]`. Vale conferir a grafia — é transcrição
de áudio e eu posso ter recebido errado. Seja como for, o nome conversa bem com o eixo
editorial que vocês acharam sem perceber (seção 4).

**O filme:** *O Estranho Mundo de Zé do Caixão* (1968), de José Mojica Marins — três curtas
numa antologia. Vocês nunca acertam o título no ar (`[P1 00:56]` *"O Mundo de Zé do Castelo.
Eu acho que é esse o nome."*), então deduzi pelo conteúdo, não por metadado: *"são três
curtas"* `[P1 02:13]`, o fabricante de bonecas cujos olhos são reais demais `[P1 02:32]`,
`[P1 05:29]` (**O Fabricante de Bonecas**), e o corcunda dos balões com o par de sapatos
`[P1 14:11]`, `[P1 15:45]` (**Tara**). Confere antes de publicar — mas se estiver certo, isso
já é o primeiro "não vale porra nenhuma" do programa.

---

## 2. O número mais importante deste documento — e a faca de dois gumes

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
| Ritmo | 176 palavras/min | **143 palavras/min** |
| Proporção de fala | 87% | **78%** |
| Pausa longa por minuto (miolo) | 1,02s | **1,61s** |

**A Parte 2 é 19% mais lenta e tem ~60% mais pausa no miolo.** Este documento a trata como a
metade fraca porque ela abre mal, aos 92 ppm — e isso continua verdade. Mas o *ritmo* dela é o
mais próximo do tom que vocês querem. O modelo de como soar já está gravado; é o segundo
arquivo, não o primeiro.

*(Os 3,38 s/min brutos da Parte 2 incluem o teste de microfone e a despedida — o número
comparável é o do miolo, 1,61.)*

→ Alvo de ritmo e o que fazer com isso em [MODELO-PODCAST.md](MODELO-PODCAST.md), seção "O tom".

E as poucas pausas longas que existem quase todas têm causa externa, não constrangimento:

| Timestamp | Duração | O que era |
|---|---|---|
| `[P1 14:24]` | 25,8s | Alguém abordando vocês na calçada |
| `[P1 55:36]` | 6,3s | Falha de áudio — o que vem depois sai ininteligível (ver §8) |
| `[P1 47:14]` | 4,7s | Hesitação real ("mas..." / "sei lá") |
| `[P1 36:09]` | 4,2s | Pausa de argumento |

A de `[P1 55:36]` é a única que não é nem incidente nem hesitação: os 11 segmentos seguintes
`[P1 55:43–56:00]` vêm com confiança despencada (logprob −2,37) e saem como *"umca"*, *"fi"*,
*"um hp"*. Não é vocês travando — é a gravação falhando. É o mesmo trecho que interrompe a
melhor ideia da noite (seção 6).

**Conclusão:** o problema de vocês não é conteúdo nem química. É estrutura. Isso é uma
posição muito melhor de partida do que o contrário — dá para consertar estrutura, não dá
para fabricar química.

---

## 3. O ritmo da conversa — e o que não dá para medir

O celular aplicou controle automático de ganho, o que achatou o volume — todos os blocos de
5 min medem entre −11,4 e −12,1 dBFS. Então o volume não diz nada sobre energia.

**E o que eu queria medir aqui, não dá.** O ideal seria a densidade de turnos: quantas vezes
vocês trocam de voz por minuto. Só que a gravação é mono com microfone único (§8), então não
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
cobrado. O fim é cansaço, e vocês dizem isso no ar (§7.7).

> **Nota de método.** A curva que estava aqui antes contava segmentos do Whisper e os chamava
> de turnos. Não são: na Parte 1 o Whisper corta a ~6 palavras por segmento até o minuto 22,
> cai para ~2,9 até o minuto 56, e volta para ~4,9 no fim. O "pico de 134 aos 30 min" e a
> "queda para 51 aos 60 min" são essa mudança, mais a última janela ser parcial. Medindo:
> a contagem de segmentos correlaciona **−0,888** com palavras por segmento e só **0,324** com
> a taxa de fala. Ela media a transcrição. Saiu.

---

## 4. O eixo editorial que vocês acharam sem perceber

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

E o nome do podcast — *Sem Autoestima* — já aponta para lá. Vocês acertaram o nome antes de
saber qual era o programa.

---

## 5. Os papéis — e por que o par funciona

**Confiança:** os papéis estão claros e sustentados por várias evidências. A atribuição
linha a linha, não — é gravação mono, microfone único, com muita fala sobreposta. Onde eu
digo "Gabriel" ou "André" abaixo, é por cadeia de evidência, não por reconhecimento de voz.

### Gabriel — o cético do ofício
Julga a coisa em si. Quer saber se é bem feito.

> `[P1 01:55]` *"Mas vendo esse filme, eu achei uma bosta. Uma bosta imensa."*
> `[P1 24:55]` *"Eu não aprendo nada vendo esse curta. (...) Você não absorve nada substancial."*
> `[P1 24:30]` *"Quando você vai fazer arte (...) você tem que fazer de um jeito que as pessoas se interessem em assistir. Eu não vou assistir seu filme de graça."*

### André — o advogado do significado
Julga o que a coisa representa. Sobe para sociedade, essência, autenticidade.

> `[P1 09:21]` *"Ele virou uma identidade, uma persona que tá ligada muito ao terror. Eu acho que isso é muito saudável."*
> `[P1 35:29]` *"Apesar de não ter dinheiro, apesar de não ter meios, ele fez do jeito dele. E pra mim isso é foda pra caralho, é uma referência."*
> `[P1 34:51]` *"Vem de Sócrates, na verdade. Sócrates falava que o sapo sapeia, a girafa girafeia..."*

**Isso é um par de podcast legitimamente bom.** Não é "dois amigos concordando" — é uma
oposição estrutural real: *o que a coisa É* contra *o que a coisa SIGNIFICA*. Essa tensão
não se esgota, porque não tem resposta certa. Dá para rodar em cima dela por anos.

### E tem uma ironia de personagem pronta

André sugeriu o filme `[P1 00:59]` e não assistiu direito — viu uma análise no YouTube e leu o
roteiro depois `[P1 18:48]`. Gabriel assistiu e detestou. O programa inteiro começa com o cara
que indicou o filme defendendo um filme que ele não viu, contra o cara que viu.

> `[P1 01:04]` *"Eu assisti e o filho da puta não assistiu."*
> `[P1 01:11]` *"Não vale porra nenhuma, cara. Você não vai saber falar isso de nada, entendeu?"*
> `[P1 18:48]` *"Você tá repetindo o que você viu no vídeo de análise."*

Isso é ouro de personagem. Não conserta — **transforma em quadro** (ver `MODELO-PODCAST.md`).

---

## 6. Momentos de ouro

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

---

## 7. O que não funcionou

### 7.1 A abertura falhou, e vocês disseram isso no ar

O roteiro previa "conversa livre" primeiro, depois o filme `[P1 00:46]`. A conversa livre durou
**90 segundos** antes de vocês desistirem:

> `[P1 00:46]` *"Primeiro a gente vai tentar começar com uma conversa livre. Eu não sei se isso vai funcionar."*
> `[P1 01:24]` *"Não tenho ideia nenhuma do que falar, então vai ser sobre o filme."*

A dúvida do Gabriel em `[P1 00:46]` estava certa. Papo livre não é ponto de partida — é o que
acontece **depois** que um objeto concreto esquenta a conversa. Vocês provaram isso na
prática: o filme puxou 35 minutos, e desses 35 nasceu a melhor parte do episódio.

### 7.2 Nenhum dos dois tinha visto o filme direito

Isso limitou o bloco o tempo todo:

> `[P1 17:30]` *"Caralho, velho, eu não lembro também."*
> `[P1 29:01]` *"Porra, eu não lembro do final direito."*
> `[P1 36:23]` *"Não sei porra nenhuma da história do Zé do Caixão."* — *"Eu também não sei."*

E ainda assim rendeu 35 minutos. É o argumento mais forte a favor do formato: **com
preparação de verdade, esse bloco vira o melhor do programa.**

### 7.3 "Tá ligado" — 116 vezes em 87 minutos

Uma vez a cada 45 segundos. Somando "entendeu" (39×), "sei lá", "tipo" e "cara", boa parte
do texto é enchimento. No áudio passa. **Em vídeo, com o rosto de vocês na tela, vira a
única coisa que a pessoa escuta.**

Não é para eliminar — é vício de fala natural, e matar isso mata a naturalidade. É para
derrubar de 116 para uns 30. Só ter consciência já resolve metade.

### 7.4 O "é um dado" — o furo mais sério

O trecho sobre Japão e autismo `[P1 48:00–52:30]` circula por quatro minutos sem sair do lugar,
porque a discussão inteira se apoia num número que ninguém tem:

> `[P1 50:10]` *"Lá o nível de namoros no Japão é abaixo da média."*
> `[P1 50:16]` *"Isso é verdade? É um fato?"* — *"Deve ser."* — *"É um dado."* — *"Eu não sei. Mas é um dado."*
> `[P1 50:39]` *"É um dado aleatório."*

Vocês perceberam ao vivo e mesmo assim seguiram. Quatro minutos de trilho falso. Solução
proposta em `MODELO-PODCAST.md` — não é cortar, é virar quadro.

### 7.5 Quando vocês concordam, a conversa para de andar

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

### 7.6 As viradas de assunto são sem cerimônia

> `[P1 36:44]` *"Agora vamos falar. Qual que é o próximo tópico?"*
> `[P2 25:05]` *"Então o próximo assunto, então."*

Funciona, mas é plano. E o encerramento foi improvisado — vocês perguntaram no ar como se faz,
e só então improvisaram uma despedida:

> `[P2 25:28]` *"Como é que encerra o podcast?"*
> `[P2 25:32]` *"Galera, muito obrigado por participar dessa jornada que estamos tentando fazer funcionar."*

A despedida improvisada até é simpática. O problema é que ela nasce depois da pergunta ficar
gravada.

### 7.7 A madrugada cobrou

Os avisos estão todos gravados:

> `[P1 43:32]` *"Eu tô muito bêbado."*
> `[P1 47:23]` *"Tô bêbado."*
> `[P2 25:12]` *"Acho que eu tô bêbado, entendeu?"*
> `[P2 25:19]` *"Eu tô cansado. Melhor a gente parar esse podcast por aqui."*

A Parte 2 não acabou porque o assunto acabou — acabou porque vocês acabaram. O tema das
relações estava vivo, com discordância aberta, quando encerrou.

---

## 8. Diagnóstico técnico da gravação

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

1. **Faixa dinâmica de 8–12 dB.** O ruído do bar está quase no mesmo volume da voz de
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

## 9. Resumo

**O que vocês já têm, e é a parte difícil:**
- Química real, medida: 87% de fala e só 1 minuto de pausa longa, em um primeiro episódio
- Uma oposição de papéis que se sustenta sozinha e não se esgota
- Um eixo editorial coerente, que vocês encontraram sem procurar
- Reflexo bom para incidente ao vivo (a abordagem na calçada)
- Um nome que já combina com o programa

**O que falta, e é a parte fácil:**
- Começo e fim sempre iguais (hoje são improvisados, e falham)
- Preparação mínima do objeto — os dois consumirem de verdade
- Um jeito de não desabar em concordância — descer ao motivo, não fingir o lado contrário
- Ritmo: baixar dos 176 palavras/min e deixar o silêncio existir
- Parar aos 60 minutos, num bar só, começando mais cedo
- Dois microfones e desligar o ganho automático

Nada na lista de falta é sobre talento. É tudo processo.

→ Formato proposto em [MODELO-PODCAST.md](MODELO-PODCAST.md)
→ Pautas concretas em [BANCO-DE-PAUTAS.md](BANCO-DE-PAUTAS.md)
