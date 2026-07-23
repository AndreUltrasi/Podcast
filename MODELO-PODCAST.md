# Modelo do programa — Áudio Sem Autoestima

> Tudo aqui é derivado do que aconteceu nos pilotos, não de fórmula de podcast genérica.
> Os timestamps são a justificativa de cada decisão. Diagnóstico completo em [ANALISE.md](ANALISE.md).
>
> Timestamps no formato `[P1 mm:ss]` e `[P2 mm:ss]`, em minutos corridos de cada arquivo.
>
> As expansões de conteúdo e de rua acrescentadas ao modelo são **propostas de teste**.
> Quando uma orientação não tem timestamp, ela não é uma conclusão tirada dos pilotos.

---

## O eixo

**A distância entre quem você é e o que o mundo exige que você seja.**

Vocês chegaram nisso sozinhos, por sete caminhos diferentes, em 87 minutos — Zé do Caixão,
régua alta, Whindersson, autismo, anime, cinema brasileiro, relações da geração Z. Não
precisa inventar nicho: já está lá, é só assumir.

Isso dá uma frase de apresentação:

> *"Dois caras num bar em São Paulo discutindo se vale a pena ser você mesmo."*

E dá o critério de pauta, que é o mais útil: **serve pauta que tenha alguém tentando caber
em algum molde, ou se recusando a caber.** Filme, celebridade, relação, trabalho, diagnóstico,
país. Se não tiver essa tensão, não é pauta do programa.

---

## O tom

Se o eixo diz *do que* o programa trata, isto diz *como ele soa*. As referências que vocês
deram: **Ben-Yur** (Bento Ribeiro e Yuri Moraes) e **os podcasts do Arthur Petry** — À Deriva,
Saco Cheio, Tarja Preta. O que vocês querem de lá é o **clima low vibe**.

> **Aviso de fonte.** O que segue sobre as duas referências é pesquisa, não escuta — eu não
> ouvi nenhum episódio. Onde este documento fala de vocês, tem timestamp; onde fala delas,
> tem só isto. Trate como ponto de partida para vocês corrigirem, não como análise.

**Ben-Yur:** comédia, semanal, dupla fixa com amigos e convidados improváveis. Passou do
episódio #287 — é um formato repetível, rodando há anos.

**Arthur Petry:** comediante, e o método descrito é o mais útil dos dois — *prefere ouvir a
falar*, *faz a pergunta certa no momento certo e deixa a pessoa responder livremente*, com
*ponto de vista coerente, com contrapontos*. A persona pública dele é "hater número 1 de
podcasts do Brasil (incluindo os SEUS)", o que diz muito: a marca é **ser contra a formatação
de podcast**.

**Uma divergência consciente:** as duas referências são programas de convidado. O de vocês
não é, e não vai ser. O que se importa daqui é o tom, não a estrutura.

### O que "low vibe" quer dizer neste documento

Ouvir mais, correr menos, e parar de anunciar o programa. Nas quatro alavancas:

1. **Ritmo mais lento, com silêncio permitido**
2. **Deixar o outro terminar** — a frase, o raciocínio, e a pausa depois dele
3. **Menos quadro** — o que precisa de nome e regra já está formatado demais
4. **Mais bar, menos programa** — a calçada, o ruído, o vendedor, a bebida

E o que **não** quer dizer: menos assunto, menos opinião, menos discordância. As duas
referências são faladoras e opinativas. Elas só não são apressadas.

### O alvo, em número — porque dá para medir

Aqui está o problema: **os pilotos são rápidos e densos, que é o oposto do que vocês
descrevem.** E as duas metades não são iguais.

| | Parte 1 (bar) | Parte 2 (karaokê) |
|---|---|---|
| Ritmo | 176 palavras/min | **143 palavras/min** |
| Proporção de fala | 87% | **78%** |
| Pausa longa por minuto (miolo) | 1,02s | **1,61s** |

**O tom que vocês querem já está gravado — é a Parte 2, não a Parte 1.** Ela é 19% mais
lenta, tem 9 pontos a mais de não-fala e ~60% mais pausa no miolo. Este documento tratava a
Parte 2 como a metade fraca porque ela abre mal, aos 92 ppm `[P2 00:00–02:00]`. Sob a régua
nova, a lentidão dela deixa de ser defeito e vira o exemplo. O que era defeito continua
sendo: a abertura confusa e o fim por cansaço.

**Alvo prático:** descer dos 176 na direção de ~150 palavras/min e subir o tempo de pausa.
Dá para conferir depois de cada episódio com `analise_conversa.py`, que já mede as três
coisas.

*Duas ressalvas honestas. Os 3,38 s/min brutos da Parte 2 incluem o teste de microfone e a
despedida — o número comparável é o do miolo, 1,61. E eu não tenho medida nenhuma do Ben-Yur
nem do À Deriva: esse alvo é relativo ao baseline de vocês, não cópia do número de ninguém.*

---

## Concordar não é o problema — parar de pensar é

Duas vezes em um minuto, a conversa trava assim:

> `[P1 42:16–42:20]` *"acho que sim"* × 5, em quatro segundos
> `[P1 43:41–43:43]` *"acho que sim"* × 3

O que destrava é a vendedora chegando na mesa `[P1 42:20]` — ou seja, foi a rua, não vocês.
E acontece **dentro do melhor trecho do episódio**, não num momento fraco. Concordar é o modo
padrão de dois amigos conversando, e é o único jeito garantido de matar um assunto.

**Mas a saída não é discordar de mentira.** Uma versão anterior deste documento mandava, se
os dois concordassem por 2 minutos, um assumir o lado contrário de propósito. Retirei, por
três motivos:

- É a coisa mais formatada que tinha aqui, e é exatamente o que o registro da referência
  rejeita — o Petry construiu uma persona inteira sendo contra isso
- O método descrito lá é melhor e mais barato: **ponto de vista coerente, com contrapontos.**
  Não é fingir posição, é ter uma e cobrar a do outro
- **Briga com o eixo do próprio programa.** Um podcast sobre *a distância entre quem você é e
  o que o mundo exige que você seja* não pode exigir que os apresentadores finjam posição no
  ar. A regra antiga pedia, ao vivo, o comportamento que o programa critica

### O que fazer no lugar

Quando perceberem que concordaram, o próximo movimento não é inverter — **é perguntar
"por que você acha isso?" até achar onde vocês divergem de verdade.** Sempre tem. Vocês
concordam na conclusão e discordam no motivo quase toda vez; é só descer um andar.

O piloto mostra isso funcionando: os dois acham o Zé do Caixão relevante, mas Gabriel acha a
obra ruim `[P1 01:55]` e André acha que o que ela representa importa mais `[P1 09:21]`. Mesma
conclusão, motivos incompatíveis, 35 minutos de conversa. A oposição de papéis descrita na §5
do ANALISE (*o que a coisa É* contra *o que a coisa SIGNIFICA*) já dá o lado de cada um de
graça — não precisa inventar.

---

## Estrutura do episódio — ~55 min

A ordem não é arbitrária: é a que o piloto descobriu funcionando. O objeto concreto esquenta
a conversa, e o assunto abstrato nasce dele. O melhor trecho do episódio `[P1 30:00–43:00]` só
existiu porque 30 minutos de filme vieram antes.

> **Isto é ferramenta de preparação, não roteiro de locução.** Os minutos são faixa, não
> cronômetro, e **a divisão nunca é anunciada no ar.** O problema do piloto nunca foi falta de
> vinheta — era `[P1 36:44]` *"agora vamos falar, qual que é o próximo tópico?"*. A correção é
> só mudar de assunto. Ouvinte nenhum precisa saber que existe um Bloco 2.

### Começo · ~2 min

Hoje é o ponto mais fraco. A conversa livre de abertura durou 90 segundos antes de vocês
desistirem no ar `[P1 01:24]`. A correção não é um ritual — é um começo **curto e chato de
propósito**, sempre igual, que ninguém precisa performar:

Onde a gente tá, quem tá falando, e qual é a pergunta da noite — cada um responde em uma
frase, antes de qualquer discussão.

Essa última parte é a que faz diferença, e é a única coisa que precisa acontecer: as duas
frases mostram, sem anunciar, que vocês estão em lugares diferentes. Servem de abertura de
corte também, mas isso é consequência, não motivo.

Depois dessas duas frases, **a conversa continua livre dentro do episódio**; ela não ganha um
bloco separado. O começo só dá chão e não determina cada desvio. O objeto é a primeira âncora,
mas um caso da semana, uma coisa vista no caminho ou o próprio lugar podem atravessar a
discussão. Se vier o vazio que matou a abertura do piloto, sigam no objeto — sem anunciar a
troca.

### O Objeto · ~20 min

Um filme, disco, livro, série ou vídeo que **os dois consumiram de verdade.**

Quando o objeto for cinema, alternem a porta de entrada: **um filme específico, um diretor
discutido a partir de duas obras ou um gênero comparado por meio de dois filmes concretos.**
Gênero, direção e contexto não entram como ficha técnica; entram para descobrir qual molde a
obra reproduz, quem ela deixa de fora e onde o autor se recusa a caber.

Vocês já inventaram esse bloco ("o filme da semana", `[P1 00:50]`). A mudança é uma só, e é
inegociável: **os dois assistem.** O bloco do Zé do Caixão rendeu 35 minutos com nenhum dos
dois lembrando o final `[P1 29:01]` e ambos admitindo *"não sei porra nenhuma da história"*
`[P1 36:23]` — e sem nenhum dos dois saber o nome do filme (*O Estranho Mundo de Zé do
Caixão*, 1968, de José Mojica Marins; no ar sai como *"O Mundo de Zé do Castelo"*,
`[P1 00:56]`). Com preparação real, esse vira o melhor bloco do programa.

*Próximo objeto já está escolhido por vocês, no ar `[P1 60:08]`: o filme do Leandro Hassum
fazendo um personagem baixinho.*

### A Pergunta · ~20 min

Um dos dois traz uma pergunta que o outro **não conhece de antemão**. Alterna a cada episódio.

A pergunta pode nascer de uma **notícia ou assunto da semana**. Entra um caso concreto, com
fato, data e fontes conferidos, não um giro de manchetes. Alegação não verificada não entra
como fato. A notícia só vale quando revela a tensão do programa e deixa uma pergunta que
continue interessante depois que a semana acabar.

Esse é o formato da Parte 2, e não é coincidência que ela tenha sido a parte mais focada do
material. A pergunta do André abriu 20 minutos de discussão direta:

> `[P2 01:25]` *"Eu vejo uma tendência da geração Z pra relações não heteronormativas. O que você acha sobre isso?"*

Três critérios para a pergunta funcionar, todos observáveis no piloto:
- **Não tem resposta certa** — senão vira aula, não conversa
- **Os dois têm opinião** — senão vira entrevista
- **Nasce do objeto quando dá** — foi assim que o filme virou a discussão sobre régua alta

### A Régua · ~5 min, e acabou

Cada um conta **uma coisa da semana em que se mediu contra um padrão impossível.** Curto,
pessoal, sem resolver.

É aqui que entram **saúde mental e dramas pessoais**: como experiência vivida, não como
diagnóstico do outro nem conselho clínico. Falem em primeira pessoa e retirem detalhes que
identifiquem quem não consentiu em ser identificado.

É também o pedaço mais low vibe do programa por natureza: ninguém conta isso apressado, e é
o único momento em que o silêncio depois da fala do outro é obrigatório.

Sai direto do trecho em que o episódio encontra o próprio assunto `[P1 36:46–39:00]`:

> `[P1 36:51]` *"Será que a gente não tem uma régua muito alta sobre as coisas? A gente vê o mundo e tudo é foda (...) e a gente assume pra gente uma régua tão alta que a gente não consegue chegar nessa régua."*

É o eixo do programa aplicado a vocês mesmos, toda semana. E resolve o encerramento, que hoje
é improvisado a ponto de vocês perguntarem no ar *"como é que encerra o podcast?"* `[P2 25:28]`.

Fecha com uma despedida fixa, sempre a mesma.

---

## Duas coisas com nome — e o resto sem

Este documento já teve seis quadros. Seis quadros é um programa de auditório, não é o clima
que vocês querem. Ficaram dois, e ficaram porque **nasceram sozinhos no piloto e já são
piada de vocês** — não porque um formato precisa de quadros.

O resto virou hábito: coisa que vocês fazem, sem nome, sem regra e sem cronômetro. A
diferença importa. Quadro é anunciado; hábito só acontece.

### "Não vale porra nenhuma"
**Origem:** `[P1 01:11]` e `[P1 18:48]`

Qualquer um pode acusar o outro de estar defendendo algo que não consumiu ou não conhece de
verdade. O acusado tem que declarar sua fonte na hora: assisti inteiro, vi um vídeo de
análise, li a sinopse, ou tô inventando.

Já é engraçado de nascença por causa da ironia de origem — **André indicou o filme `[P1 00:59]`
e não assistiu direito**, e Gabriel não perdoou:

> `[P1 01:04]` *"Eu assisti e o filho da puta não assistiu."*

E tem uma segunda camada de graça disponível: **nenhum dos dois sabia o nome do filme**
`[P1 00:56]`. O quadro pode valer para o título também.

### "O bar entra"
**Origem:** `[P1 42:20–43:25]`

Interrupção de vendedor, garçom, gente na calçada — **não corta.** Atende, e depois comenta
para o microfone.

Vocês já acertaram isso no reflexo, sem combinar:

> `[P1 43:12]` *"Galera, pra quem só tão ouvindo — não é que a gente tá num bar, a gente tá na calçada, e aí sempre aparece alguém tentando vender alguma coisa."*

Às vezes vocês podem fazer o movimento inverso e ir até a rua: **uma pergunta curta para um
desconhecido, ligada ao assunto da noite**. Não é enquete nem busca por uma resposta que
confirme a tese. Se a conversa surgir naturalmente, acompanhem por alguns minutos; se não,
agradeçam e voltem para a mesa. Expliquem o projeto e peçam autorização para gravar e
publicar. Essas vozes são matéria breve para a dupla discutir, não convidados do episódio.

Isso é o que separa "papo de bar" de "dois caras num estúdio fingindo estar num bar". É a
sua vantagem competitiva, é impossível de imitar em estúdio, e é **a coisa mais low vibe que
existe no material de vocês** — a única em que o programa deixa o mundo entrar em vez de se
proteger dele. Em vídeo, vale ainda mais.

---

## Hábitos — sem nome, sem regra, sem cronômetro

Estes eram quadros e deixaram de ser. Continuam valendo; só não são anunciados nem têm
mecânica. Se virarem tique, tira.

**Os dois consomem o objeto.** `[P1 00:50]` — quem escolhe alterna, e quem escolhe é obrigado
a consumir. É a piada e a regra ao mesmo tempo, e é a única coisa inegociável da lista.

**Quando ninguém tem o dado, admite e segue.** `[P1 50:10–50:40]` foi o pior trecho do
piloto: quatro minutos rodando em falso porque ninguém tinha o número (*"É um dado." — "Eu
não sei. Mas é um dado."*). Não precisa de buzina nem de 10 segundos no relógio — precisa de
alguém dizer "não sei" e a conversa andar. Anota, checa depois, e menciona no episódio
seguinte se lembrar. Se não lembrar, tudo bem.

**Quando o assunto de agora já apareceu antes, aponta.** O terceiro curta do Zé do Caixão é
sobre provar que o amor não existe, que é instinto disfarçado `[P1 27:55]`. Cinco horas
depois, no karaokê, vocês chegaram sozinhos em *"ninguém tem a necessidade de amar outra
pessoa (...) porque amar gasta energia"* `[P2 14:56]`. **Vocês concordaram com o Zé do Caixão
sem citar o Zé do Caixão**, e ninguém percebeu no ar. Dito na hora, faz o episódio parecer
escrito — e ele não é.

**No fim de um assunto, o que quase te convenceu?** Vocês já perguntam isso quando o assunto
interessa (*"você concorda com essa ideia?"* `[P1 33:56]`), mas os assuntos do piloto nunca
fecham — são interrompidos por *"qual que é o próximo tópico"* `[P1 36:44]`. Uma frase de cada
um encerra sem exigir conclusão. "Nada" é resposta válida.

**O lugar também pauta.** Antes de gravar, cada um anota uma coisa que viu, uma frase que
ouviu e uma pergunta que o ambiente levantou. Uma delas pode entrar na conversa; as outras
vão para o [banco de pautas](BANCO-DE-PAUTAS.md). A rua não é só cenário: ela serve para
desmentir ou complicar a hipótese que vocês levaram.

---

## Como chegar no tom

**Deixar o outro terminar.** É a única coisa desta seção que não é experimento — é o método
inteiro da referência do Petry (*prefere ouvir a falar*) e é o que a gravação de vocês menos
tem: microfone único, muita fala sobreposta, 176 palavras por minuto. Não é falar menos, é
esperar mais. A pausa depois da frase do outro faz parte da frase dele.

O resto **não saiu do piloto** — são propostas, com motivo. Testem uma por episódio, não
empilhem:

**Deixar o silêncio existir.** Quando der vontade de preencher, conta até três antes. Motivo:
vocês gravaram 87% de fala e 1 minuto de pausa longa em 61 minutos — o problema não é buraco,
é o contrário. É a alavanca mais direta para sair dos 176 e chegar perto dos 150, e a única
que não depende de mais ninguém.

**A pergunta escrita antes de sair de casa.** Quem traz a pergunta escreve e não muda no bar.
Motivo: a pergunta do André `[P2 01:25]` funcionou porque estava formulada; a abertura livre
falhou em 90 segundos `[P1 01:24]` porque não estava. O bar é bom para responder, não para
formular.

**O outro escolhe o objeto.** Em vez de alternar quem escolhe o próprio, alterna quem escolhe
**para o outro** — de preferência algo que ele provavelmente vai detestar. Motivo: a melhor
tensão do piloto veio de Gabriel odiando um filme que André defendia `[P1 01:55]`. Cria a
situação de propósito, sem ninguém precisar fingir opinião.

**Começar admitindo o que errou.** O piloto já tem material: o nome do filme `[P1 00:56]`, o
número do Japão `[P1 50:10]`. Errar em público, toda semana, é barato, é engraçado e é o mais
coerente com um programa chamado *Sem Autoestima*.

---

## Duração, horário e local

Três decisões, todas tiradas dos dados:

**Um local-base só, sem mudança no meio.** A troca custou os minutos mais fracos das duas
gravações — a Parte 2 abre com 92 palavras/min, o valor mais baixo de todo o material, e a
janela ainda inclui 26,7s de teste de microfone. O tempo foi gasto em *"Tira agora"*,
*"Começou?"*, *"Como é que a gente volta?"*.

**Proposta de circulação, a testar:** o endereço pode mudar entre episódios. **República,
Augusta, Liberdade e Pinheiros** são os primeiros territórios. Em cada saída, levem uma
pergunta e, quando surgir naturalmente, conversem com pessoas que tenham relações diferentes
com o lugar. Um recorte e um local-base por episódio; andar e observar faz parte, trocar toda
a operação de lugar no meio não.

**Começar mais cedo — por volta das 20h.** Vocês começaram 22:22 e aos 43 minutos já havia
*"eu tô muito bêbado"* `[P1 43:32]`, repetido em `[P1 47:23]`. A Parte 2, à 1h da manhã,
terminou por cansaço com o assunto ainda vivo: *"eu tô cansado, melhor a gente parar esse
podcast por aqui"* `[P2 25:19]`.

**Teto rígido de 60 minutos.** A Parte 2 fecha em 108 palavras/min contra mediana de 143 — a
única vez, nas duas gravações, em que o ritmo cai *no fim* em vez de cair por interrupção — e
vocês anunciam o motivo no ar (`[P2 25:12]`, `[P2 25:19]`). A Parte 1, por comparação, mantém
o ritmo até o último minuto cheio: não foi o assunto que acabou, foi a noite. Encerrar no auge
é melhor do que encerrar no fim da bateria — e sobra material para o episódio seguinte.

---

## Destravamento

Quando o assunto morrer, em ordem:

1. **Pergunta direta ao outro.** Já é hábito de vocês e funciona: *"tem mais algo a comentar sobre esse?"* `[P1 13:58]`, *"você concorda com essa ideia?"* `[P1 33:56]`, *"faz sentido?"* `[P2 03:51]`
2. **Caso concreto.** As melhores viradas do piloto vieram de exemplo específico, não de teoria: a família da coxinha `[P1 11:32]`, Whindersson `[P1 39:30]`, o dorama da namorada do André `[P1 54:35]`
3. **Descer ao motivo.** Se vocês concordaram na conclusão, perguntem por quê até encontrar onde os motivos divergem de verdade
4. **Nova rodada = novo assunto.** Ritual físico marcando a virada, resolve o *"qual que é o próximo tópico"* `[P1 36:44]`

---

## A ponte para o vídeo

Vocês ainda não estão publicando, então isto é sobre **não criar retrabalho**, não sobre produção.

### Faça agora, muda tudo e é barato

**Dois microfones, um por pessoa, em canais separados.** É a mudança de maior impacto
disponível. Hoje é microfone único em mono — correlação L/R de exatamente 1,000000. Isso
resolve, de uma vez:

- A faixa dinâmica de 8–12 dB, que é o teto de qualidade de tudo hoje
- O equilíbrio entre as vozes, hoje impossível de ajustar
- A separação de quem falou, que hoje não existe — com canais separados, as transcrições
  futuras já vêm com falante identificado, e aí dá para medir de verdade quem fala quanto e
  quantas vezes vocês trocam de voz (hoje, não dá — ver §3 do ANALISE)

Microfone dinâmico cardioide, perto da boca. Dinâmico rejeita ruído de ambiente muito melhor
que o microfone do celular, que é omnidirecional e capta o bar inteiro.

**Desligue o ganho automático e trave o nível na mão.** Alvo: picos em −6 dBFS, média em −16.
Hoje está clipando em +0,7 e +1,0 dBFS, com ~50 a 62 mil amostras estouradas por arquivo —
distorção que já está gravada e não sai.

**Grave uma batida de palma no começo.** Trivial hoje, salva horas quando houver duas fontes
(áudio e vídeo) para sincronizar.

### Pense agora, executa depois

- **A calçada é cenário e fonte.** Movimento de rua atrás de vocês, mesa, copo, encontros e
  histórias que não existiriam no estúdio. Não troque isso por fundo neutro — é justamente o
  que ninguém consegue copiar
- **Vocês já sentam lado a lado**, o que dá um plano de dois naturalmente
- **O "tá ligado" vira o problema nº 1 em vídeo.** 116 vezes em 87 minutos. No áudio passa
  despercebido; com o rosto na tela, é a única coisa que a pessoa escuta. Não elimine — só
  ter consciência já derruba pela metade
- **A Régua é o corte vertical natural.** Curto, pessoal, autoconclusivo

---

## Resumo em uma tela

```
COMEÇO         ~2 min   onde estamos + a pergunta em 1 frase cada
O OBJETO      ~20 min   obra concreta; no cinema: filme, diretor ou gênero
A PERGUNTA    ~20 min   um traz; pode nascer do assunto da semana
A RÉGUA        ~5 min   drama pessoal: onde me cobrei um padrão impossível
E ACABOU       ~2 min   sempre igual
              -------
              ~55 min   um local-base · começar às 20h · teto de 60 min

              (isto é preparação. nada disso se anuncia no ar.)

TOM       low vibe: ouvir mais, correr menos, não anunciar o programa
ALVO      ~150 palavras/min e mais pausa   (piloto: 176 · P2 já foi 143)
FLUXO     conversa livre dentro e entre as âncoras, sem bloco separado
LOCAL     o bairro pode mudar entre episódios; um recorte por saída
COM NOME  "não vale porra nenhuma" · "o bar entra"
NA RUA    ambiente como fonte · desconhecidos só com autorização
NO LUGAR DE DISCORDAR DE MENTIRA
          "por que você acha isso?" até achar onde vocês divergem de verdade
```

→ Pautas concretas em [BANCO-DE-PAUTAS.md](BANCO-DE-PAUTAS.md)
