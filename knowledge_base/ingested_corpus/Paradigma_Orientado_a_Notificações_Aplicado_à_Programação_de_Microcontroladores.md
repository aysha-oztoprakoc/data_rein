# Paradigma Orientado a Notificações Aplicado à Programação de Microcontroladores.pdf

Paradigma Orientado a Notiﬁcac¸˜oes
Aplicado `a Programac¸˜ao de Microcontroladores
Lucas V. S. de Mamann
CPGEI - UTFPR
Curitiba - PR, Brasil
lucasmamann@alunos.utfpr.edu.br
Jean Marcelo Sim˜ao
CPGEI - UTFPR
Curitiba - PR, Brasil
jeansimao@utfpr.edu.br
Myriam Regattieri Delgado
CPGEI - UTFPR
Curitiba - PR, Brasil
myriamdelg@utfpr.edu.br
Daniel F. Pigatto
PPGCA - UTFPR
Curitiba - PR, Brasil
pigatto@utfpr.edu.br
Resumo—Este
artigo
visa
`a
an´alise
de
desempenho
de
aplicac¸˜oes desenvolvidas em materializac¸˜oes do Paradigma Ori-
entado a Notiﬁcac¸˜oes (PON), no contexto de microcontroladores.
A aplicac¸˜ao envolve sensores e atuadores para Internet das Coisas
comunicando-se em rede. Os resultados apresentados mostram
que materializac¸˜oes do PON possuem diversas vantagens quanto
ao usual Paradigma Imperativo (PI), sendo mais eﬁciente do que
PI neste cen´ario. Este estudo expande os horizontes da aplicac¸˜ao
do PON para um novo conjunto de plataformas, particularmente
para aquelas com grande limitac¸˜ao de mem´oria e processamento.
I. INTRODUC¸ ˜AO
Os equipamentos com processamento embarcado e conec-
tividade `a Internet das Coisas (ou IoT do inglˆes Internet of
Things) possuem vasta aplicabilidade. Eles podem ser utili-
zados tanto em ambientes residenciais para prover conforto,
seguranc¸a ou assistˆencia m´edica [1], quanto em ambientes
industriais e corporativos para possibilitar o monitoramento
e controle do ambiente e de processos [2]. A acessibilidade `a
IoT por´em, muitas vezes ´e alcanc¸ada utilizando-se hardwares
com microprocessadores enxutos, devido ao seu baixo custo
monet´ario e devido ao pouco poder de processamento reque-
rido pelos equipamentos que estes controlam [1].
O Paradigma Orientado a Notiﬁcac¸˜oes (PON) surge como
uma alternativa aos demais paradigmas de programac¸˜ao, como
o Paradigma Imperativo (PI), mais usado na ind´ustria. O
PON busca melhorias como o aumento de desacoplamento
e reduc¸˜ao de redundˆancias entre entes computacionais [3],
melhorando a performance de processamento e viabilizando
aplicac¸˜oes distribu´ıdas [4]. Dado que aplicac¸˜oes IoT necessi-
tam de um c´odigo mais eﬁciente, ´e primordial buscar integrar
o PON a microcontroladores voltados a essas aplicac¸˜oes.
Este artigo tem por base dois trabalhos anteriores. O pri-
meiro, de Banaszewski [3], utiliza PON para controlar o
estado de aparelhos de ar condicionado, com base em sensores
de temperatura. O segundo trabalho, de Oliveira [4], desen-
volve uma aplicac¸˜ao IoT distribu´ıda em rede para o aux´ılio
m´edico domiciliar, por´em sem a limitac¸˜ao de recursos imposta
no presente trabalho. Neste artigo, busca-se desenvolver um
sistema gen´erico de sensores e atuadores distribu´ıdos em
rede, controlados via PON em um hardware microprocessado
enxuto, comparando-o a uma soluc¸˜ao PI.
Agradece-se `a UTFPR (CPGEI e PPGCA) e aos pesquisadores do grupo
do PON. Particularmente, J. M. Sim˜ao agradece `a Fundac¸˜ao Arauc´aria - bolsa
PQ - Edital 15/2017.
II. PARADIGMA ORIENTADO A NOTIFICAC¸ ˜OES
O PON surgiu de uma soluc¸˜ao de controle discreto para pro-
cessos industriais, proposta por Sim˜ao [5], a qual evoluiu, por
meio de diversos trabalhos, culminando neste novo paradigma
de programac¸˜ao [6]. Este novo paradigma oferece alternativas
para lidar com problemas do Paradigma Imperativo (PI) e do
Paradigma Declarativo (PD) no tocante `a computac¸˜ao l´ogico-
causal, como redundˆancias estruturais (repetic¸˜ao indevida de
c´odigo) e temporais (repetic¸˜ao indevida de processamento),
bem como o acoplamento entre partes do c´odigo [6].
O principal diferencial do PON, quando comparado ao PD
ou PI, ´e a utilizac¸˜ao de um mecanismo de notiﬁcac¸˜ao por
meio de entidades minimalistas, colaborativas e adaptadas ao
uso deste mecanismo. As notiﬁcac¸˜oes s˜ao geradas e recebidas
pelas entidades apenas nos momentos apropriados, em que de
fato h´a mudanc¸as de estado que demandem avaliac¸˜ao l´ogico-
causal, fazendo com que o sistema desenvolvido em PON seja
mais conciso quanto ao uso de recursos computacionais [6].
A estrutura do PON cont´em duas partes: (a) uma l´ogico-
causal, em que regras s˜ao avaliadas, sendo ou se mantendo
aprovadas ou desaprovadas; e (b) outra facto-execucional, em
que os elementos executam ac¸˜oes (processamentos usuais) que
alteram o estado do sistema, mantendo registro destes estados
[6]. A parte l´ogico-causal, via entidades Rules (Regras), e
a parte facto-execucional, via Fact Base Elements (FBE -
Elementos da Base de Fatos), s˜ao representadas na Figura 1.
Figura 1: Exemplo de Rule do PON (Neves, 2021 [6]).
A parte l´ogico-causal do sistema ´e implementada por Rules,
sendo estas entidades que deﬁnem as condicionantes analis´a-
veis a partir de notiﬁcac¸˜oes advindas dos FBEs. Conforme a
Figura 2, as Rules possuem Conditions a serem satisfeitas que,
por sua vez, s˜ao relacionadas a Premises a serem avaliadas.
Caso as Premises de uma Rule sejam todas aprovadas, a
Rule executa sua respectiva Action e esta suas Instigations,
que instigam execuc¸˜oes nos FBEs. Por outro lado, os FBEs


comp˜oem a parte facto-execucional, realizando ac¸˜oes quando
instigados. Mais precisamente, os FBEs possuem Attributes,
cujos estados s˜ao relacionados e avaliados pelas Premises,
bem como possuem Methods, que s˜ao instigados pelas Rules,
completando o quadro de entidades do PON [3][6].
Destaca-se a maneira inovadora de execuc¸˜ao colaborativa
das entidade do PON por meio de notiﬁcac¸˜oes, constituindo
uma cadeia de notiﬁcac¸˜oes (Figura 2). Cada Attribute de uma
instˆancia de um FBE que mudar de estado, notiﬁca apenas
as Premises pertinentes, que refazem seus c´alculos l´ogicos.
Cada Premise que mudar de estado l´ogico notiﬁca apenas as
Conditions pertinentes, as quais refazem seus c´alculos l´ogicos
pelos estados notiﬁcados contabilizados. Se a Condition ´e
aprovada, ela pode aprovar sua respectiva Rule. Esta, quando
aprovada, ativa sua Action, que notiﬁca suas Instigations, as
quais instigam os Methods. Estes ´ultimos geralmente alteram
os estados dos Attributes, reativando o ﬂuxo de notiﬁcac¸˜oes.
As conex˜oes entre as entidades para ﬁns de notiﬁcac¸˜ao ocor-
rem em tempo de construc¸˜ao dos sistemas [7] [8].
Figura 2: Representac¸˜ao das entidades da cadeia de
notiﬁcac¸˜ao do PON (Ronszcka, 2019 [8]).
O aparato para programac¸˜ao em PON est´a dispon´ıvel em
diversas formas. Para este trabalho ser˜ao utilizadas a Tecnolo-
gia LingPON 2.0, que implementa um sistema de compilac¸˜ao
e linguagem pr´oprios do PON, bem como a vers˜ao 4.0 do
Framework PON, que permite a criac¸˜ao de c´odigo em C++,
por´em utilizando os conceitos do PON. A Tecnologia Ling-
PON 2.0, ´e considerada o estado da arte em PON, enquanto o
Framework PON C++ 4.0 estabelece o estado da t´ecnica dele.
III. PROPOSTA: MICROPON EM IOT
O sistema em estudo no presente trabalho ´e descrito pelo
diagrama apresentado na Figura 3, no qual h´a N sensores,
M atuadores e uma central controladora, todos conectados
a uma rede local que possui acesso `a Internet. Ao detectar
alguma mudanc¸a de estado, podem enviar sinais `a central
controladora na forma de requisic¸˜oes a uma interface API,
por meio de uma conex˜ao qualquer (RF, WiFi ou Ethernet).
Por sua vez, os elementos atuadores s˜ao passivos, no sentido
que tˆem a necessidade de receber um comando para atuar,
ainda assim possuem capacidade de alterar o ambiente de
algum modo. Tais comandos s˜ao recebidos atrav´es de sinais
Figura 3: Representac¸˜ao do sistema em estudo
predeterminados, em seu enderec¸o na rede e em uma porta
dada. Assim como os sensores, os atuadores podem ser de
variados tipos e possuir diferentes tipos de conex˜ao `a rede.
A central controladora gera a interface API que permite
consulta e modiﬁcac¸˜ao dos estados atuais dos elementos, al´em
de poder enviar comandos aos atuadores. Tamb´em, a central
implementa a l´ogica de interac¸˜ao entre os diversos elementos
do sistema e possui mem´oria sobre os estados atuais.
No caso do sistema implementado em PON (MicroPon IoT)
os elementos sensores podem ser entendidos como FBEs com
Attributes, que notiﬁcam suas mudanc¸as de estado n˜ao por
chamadas de func¸˜oes e sim por meio de troca de mensagens
em uma rede, assim como estabelecido por Sim˜ao [5] para o
caso de uma aplicac¸˜ao industrial. Os elementos atuadores, por
outro lado, assumem o papel dos Methods de FBEs em PON,
sendo tamb´em instigados por mensagens em rede. Os demais
elementos constituintes do PON, por´em, continuam sendo
implementados em um c´odigo ´unico, na central controladora,
sempre `a luz de seus pr´oprios princ´ıpios.
Os sensores tˆem uma l´ogica simples, necessitando apenas
notiﬁcar uma mudanc¸a de estado `a central controladora. Dada
a simplicidade da natureza dos sensores, optou-se por n˜ao
implement´a-los utilizando PON, pois isto n˜ao acrescentaria
informac¸˜oes relevantes `as an´alises realizadas para este artigo.
Os sensores, portanto, foram simulados somente em compu-
tador, utilizando-se C++. Os sensores aqui implementados,
simulam a extrac¸˜ao de informac¸˜oes bin´arias do ambiente,
possuindo apenas dois estados: ativo e inativo. Estes estados
s˜ao alterados manualmente pelo usu´ario, por meio de coman-
dos disponibilizados pelo programa simulador dos sensores.
Inicialmente, todos os sensores est˜ao no estado inativo.
Quando h´a uma mudanc¸a no estado de um dos sensores, o
mesmo envia uma requisic¸˜ao `a API da central controladora,
para que o valor seja atualizado na central. A requisic¸˜ao ´e feita
utilizando-se a biblioteca CURL, que envia um pacote TCP a
um enderec¸o, porta e URL dados no c´odigo da central de
controle. Esta comunicac¸˜ao se d´a por meio de uma conex˜ao
WiFi, entre o computador e o roteador, e ethernet, entre o
roteador e a central.
Os atuadores s˜ao executados como threads concorrentes.
Cada um cria um socket em uma porta arbitr´aria do com-
putador, atrav´es do qual a central de controle pode escrever
um bit de comando, causando o respectivo atuador a mudar
para o estado indicado pelo bit. A implementac¸˜ao usou a


biblioteca padr˜ao de sockets da linguagem C, de modo que
esta comunicac¸˜ao tamb´em ocorre por meio de pacotes TCP
enviados a um enderec¸o e porta espec´ıﬁcos. Os atuadores
possuem as mesmas formas de conex˜ao que os sensores.
A central de controle foi implementada de diferentes
formas, al´em de ter sido testada tanto em uma plataforma
microprocessada quanto simulada em computador. Todas as
implementac¸˜oes, por´em, podem ser divididas em duas partes:
(i) uma desenvolvida em C++ que provˆe as funcionalidades
b´asicas de acesso ao hardware da rede, implementac¸˜ao do
protocolo de rede e da API; (ii) outra que realiza a func¸˜ao de
controle em si, desenvolvida tanto em PON (via Framework
PON C++ 4.0 e Tecnologia LingPON 2.0) quanto PI (via
linguagem de programac¸˜ao C++).
Para uma comparac¸˜ao justa entre as implementac¸˜oes, tanto a
estrutura do c´odigo quanto as funcionalidades foram replicadas
de maneira t˜ao similar quanto a linguagem ou plataforma
permite. No entanto, em se tratando da conex˜ao `a rede, h´a
uma diferenc¸a signiﬁcativa: para a simulac¸˜ao em computador,
foi utilizada a biblioteca padr˜ao de sockets da linguagem C,
tanto para o recebimento quanto para o envio de mensagens;
para a implementac¸˜ao em microcontrolador, por´em, foi feita
uma adaptac¸˜ao da biblioteca AVR-ENC28J60 [9], pois al´em
de implementar o protocolo para comunicac¸˜ao TCP/IP, o
microcontrolador necessitava da implementac¸˜ao do acesso ao
hardware de rede.
Por ﬁm, a l´ogica de decis˜ao foi implementada em C++
PI, LingPON Namespaces AVR, LingPON Namespaces e
PON Framework 4.0, sendo a segunda utilizada apenas no
microcontrolador e as duas ´ultimas apenas simuladas em
computador. Esta parte do c´odigo ´e a que de fato provˆe Rules,
relacionando os estados dos sensores e atuadores, enquanto
FBEs, com seus Attributes e Methods.
A aqui chamada LingPON Namespaces, diz respeito `a
Linguagem de Programac¸˜ao do PON (LingPON), associada a
um dos compiladores do sistema de compilac¸˜ao da Tecnologia
LingPON 2.0, considerado com melhor performance [7] [8].
Por sua vez, a LingPON Namespaces AVR diz respeito `a
LingPON com um compilador adaptado para o contexto de
AVR, elaborado no ˆambito deste presente trabalho.
A l´ogica de controle foi incorporada ao c´odigo da central
controladora. Esta l´ogica tem a responsabilidade de associar os
estados dos sensores aos estados desej´aveis para os atuadores.
Para simular algumas poss´ıveis situac¸˜oes de aplicac¸˜oes reais
e possibilitar o estudo de casos de interesse do sistema, foram
criados quatro conjuntos de regras, cada qual variando o
n´umero de sensores envolvidos na ativac¸˜ao dos atuadores. Nas
implementac¸˜oes em PON, estes conjuntos foram transcritos
utilizando-se de Rules, enquanto que para implementac¸˜oes em
C++, foram utilizadas estruturas usuais de se-ent˜ao (if-else
statements) equivalentes.
O primeiro conjunto de Rules (conjunto I) relaciona cada
atuador diretamente a um sensor. Isto ´e, quando um sensor com
ID J ´e ativado, o atuador com mesmo ID J tamb´em ´e ativado,
enquanto que o atuador ´e desativado quando seu respectivo
sensor ´e desativado.
Os trˆes demais conjuntos de Rules, relacionam K sensores
com os mesmos K atuadores, sendo K igual a 5 (conjunto II),
10 (conjunto III) e 20 (conjunto IV). Nestes casos, se os K
sensores estiverem ativos ao mesmo tempo, seus respectivos K
atuadores recebem o sinal de ativac¸˜ao (l´ogica E para ativac¸˜ao),
enquanto que se um ou mais dos K sensores for desativado,
todos os K atuadores respectivos s˜ao desativados (l´ogica OU
para desativac¸˜ao).
IV. MATERIAIS E M ´ETODOS
Para a simulac¸˜ao dos sensores e atuadores, utilizou-se o
sistema operacional Fedora 32, 64-bit, com kernel vers˜ao
5.6.6-300, executando em um processador AMD A8-4555M
Quad core, 1.6 GHz. Para reduzir as chances de preempc¸˜ao,
utilizaram-se apenas os terminais virtuais do sistema (TTYs),
de modo que a interface gr´aﬁca e servic¸os n˜ao essenciais
n˜ao estivessem rodando em paralelo com os testes. Para a
simulac¸˜ao da central de controle, utilizou-se um servidor com
processador AMD FX-4300 Quad Core, 3.8 GHz, rodando o
sistema operacional Ubuntu 20.04.2, 64-bits, com kernel 5.4.0-
65-generic. Este servidor tamb´em estava executando apenas
em modo terminal, sendo seu acesso realizado por meio de
uma conex˜ao SSH. A implementac¸˜ao f´ısica da central foi re-
alizada em um microprocessador ATMEGA328P-PU, AVR 8-
bit, 16 MHz. Em conjunto com este hardware, foi utilizado um
m´odulo ENC28J60 para prover acesso `a ethernet. Diferentes
m´etricas foram utilizadas para a extrac¸˜ao de resultados.
Tempo de requisic¸˜ao sem ativac¸˜ao de Rules ou equivalen-
te (se-ent˜ao) - diferenc¸a de tempo entre uma requisic¸˜ao, com
m´etodo GET, `a API da central controladora e o recebimento de
sua resposta. Este tipo de requisic¸˜ao n˜ao causa a veriﬁcac¸˜ao de
nenhuma Rule ou equivalente, servindo apenas como medida
do tempo de processamento das funcionalidades b´asicas de
rede e do tempo de tr´afego da mensagem na rede.
Tempo de requisic¸˜ao com ativac¸˜ao de Rules ou equiva-
lente - diferenc¸a de tempo entre uma requisic¸˜ao, com m´etodo
POST, `a API da central controladora e o recebimento de
sua resposta. Este tipo de requisic¸˜ao pode causar ativac¸˜ao de
Rules e a consequente ativac¸˜ao de atuadores, processamentos
adicionais que tamb´em est˜ao inclu´ıdos no tempo de resposta.
Desta forma, o caso m´edio desta m´etrica, representa o tempo
de processamento do mecanismo de inferˆencia das Rules.
Tr´afego de dados na rede - quantidade de bytes trocados
entre os elementos do sistema, enviados pela rede atrav´es de
mensagens. Esta m´etrica se torna relevante, pois um sistema
distribu´ıdo em rede ´e t˜ao mais r´apido quanto menos dados
forem transmitidos ou quanto mais r´apida for a transmiss˜ao.
Os experimentos foram executados com os sensores e atu-
adores executando em um computador em combinac¸˜ao com:
a central executando a l´ogica em C++, no microcontrolador;
a central executando a l´ogica em PON Namespaces AVR, no
microcontrolador; a central executando a l´ogica em C++, no
servidor; a central executando a l´ogica em PON Namespaces,
no servidor; e a central executando a l´ogica em PON Fra-
mework 4.0, no servidor. Para todos os experimentos, foram
simulados 20 sensores e 20 atuadores. Este n´umero reduzido


foi escolhido devido `a limitac¸˜ao de mem´oria do microcon-
trolador, como ser´a melhor discutido na sec¸˜ao de resultados.
Para manter os diferentes casos compar´aveis, o mesmo n´umero
de sensores foi adotado, inclusive para sistemas com maior
capacidade de mem´oria.
1) Requisic¸˜ao sem ativac¸˜ao de Rules ou equivalente: O
primeiro experimento consistiu em requisitar os estados de
todos os sensores, um por vez, em sequˆencia, e aguardar a
resposta da central. O ciclo de requisic¸˜oes foi repetido 20
vezes, gerando um total de 400 requisic¸˜oes. O tempo total
foi mensurado e sua m´edia foi calculada, gerando o tempo
m´edio de requisic¸˜ao sem ativac¸˜ao de Rules.
2) Requisic¸˜ao com ativac¸˜ao de Rules ou equivalente: Para
o segundo experimento, incialmente a central controladora
foi carregada com o c´odigo contendo o conjunto I de Rules
(descrito na sec¸˜ao III). Isto dito, 5% dos sensores, ou seja,
1 sensor, foi ativado e na sequˆencia desativado. Esta parte do
experimento foi repetida por 10 vezes, gerando 20 requisic¸˜oes.
O tempo total foi mensurado e sua m´edia foi calculada, ge-
rando o tempo m´edio de requisic¸˜ao com ativac¸˜ao de Rules. O
mesmo procedimento foi repetido com 50% dos sensores (10
sensores) sendo ativados e na sequˆencia desativados, gerando
200 requisic¸˜oes. Por ﬁm, os mesmos passos foram realizados
com 100% dos sensores (20 sensores) sendo ativados e ent˜ao
desativados, gerando 400 requisic¸˜oes.
Este experimento, composto de suas trˆes etapas (ativac¸˜ao
de 5, 50 e 100% dos sensores), foi ent˜ao repetido para a
central contendo os conjuntos de Rules II, III e IV, extraindo-se
sempre as mesmas m´etricas.
3) Tr´afego de dados: Como ´ultimo experimento, a central
foi carregada com o c´odigo contendo o conjunto de Rules
IV, devido ao seu potencial de ser um caso cr´ıtico quanto
ao tempo de processamento e volume de dados. Foram ati-
vados 100% dos sensores (20 sensores), sendo os mesmos
desativados na sequˆencia, este processo foi repetido por 10
vezes. Foram monitorados os pacotes de dados trocados entre
os sensores, atuadores e a central, obtendo-se o total de bytes
movimentados na rede por estes elementos. A m´edia de bytes
por requisic¸˜ao foi calculada, obtendo-se o volume m´edio de
bytes gerados por requisic¸˜ao.
V. RESULTADOS
Do C´odigo: A Tabela I apresenta uma an´alise quantitativa
do n´umero de linhas necess´arias para implementar a l´ogica
em cada linguagem utilizada, o tamanho do c´odigo execut´avel
compilado e da mem´oria RAM utilizada na execuc¸˜ao deles.
Dentre as variantes, nota-se que o c´odigo em C++ ´e o mais
simples de ser escrito, tanto em n´umero de linhas quanto
em facilidade de implementac¸˜ao dos c´odigos decisionais. A
simplicidade deste, no entanto, ´e em relac¸˜ao `a estrutura de
c´odigo necess´ario e n˜ao em relac¸˜ao `as Rules, dado que
estas s˜ao semelhantes em todos os casos, como abordado
na sec¸˜ao III. Esta estrutura notavelmente reduz os gastos de
mem´oria, tanto em disco quanto RAM, tornando-a atrativa
principalmente para a plataforma microprocessada, que possui
grande restric¸˜ao de mem´oria.
Tabela I: An´alise quantitativa dos c´odigos
No outro extremo, encontra-se o c´odigo que utiliza o
Framework PON C++ 4.0, implementac¸˜ao est´avel do PON - o
estado da t´ecnica. Tal c´odigo em Framework PON C++ 4.0 ´e o
mais custoso em termos de mem´oria. Isto claramente se deve
`a estrutura adicional necess´aria para implementar o PON em
si usando estruturas de dados sobre o C++. A codiﬁcac¸˜ao em
Framework PON C++ 4.0 se assemelha ao C++, em facilidade
e em n´umero de linhas. Por´em, h´a impedimentos para que
o c´odigo seja portado para a plataforma microprocessada,
uma vez que o Framework 4.0 utiliza diversas bibliotecas
e funcionalidades n˜ao suportadas pelo compilador AVR. E
mais, o execut´avel gerado precisaria ser otimizado, de modo
a reduzir seu tamanho em cerca de 10 vezes.
O c´odigo em PON Namespaces e sua vers˜ao adaptada
para o compilar AVR, por sua vez, s˜ao um meio termo em
quest˜ao de uso de mem´oria. Isto possibilita a sua aplicac¸˜ao na
plataforma microprocessada, apesar de ainda ser um limitante
da complexidade e n´umero de Rules. Entretanto, o menor
n´umero de funcionalidades desta implementac¸˜ao do PON
reduz a facilidade e escalabilidade de sua implementac¸˜ao.
Como se observa nos dados da Tabela I, s˜ao necess´arias de
5 a 10 vezes mais linhas para se programar a mesma l´ogica,
principalmente devido `a redundˆancia da linguagem.
A maior diferenc¸a entre o Namespaces e as demais
implementac¸˜oes, se d´a pela impossibilidade de se utilizar
vetores e loops para a criac¸˜ao dos objetos e das Rules. O
Namespaces possui a implementac¸˜ao de vetores e loops, por´em
estas se mostram limitadas para o desenvolvimento dos expe-
rimentos. Os vetores, por exemplo, n˜ao podem ser utilizados
em Instigations, forc¸ando o programador a declarar todas as
vari´aveis ali utilizadas. Tamb´em, os ´ındices dos vetores n˜ao
suportam express˜oes num´ericas, limitando as Formation Rules
(FR - i.e., modelo de Rules que as cria) a serem mais simples.
Por ﬁm, os loops podem ser utilizados somente em FRs,
n˜ao atendendo ao caso de atribuic¸˜ao de valores aos diversos
´ındices de um vetor, por exemplo. Por estas raz˜oes, a l´ogica
em Namespaces se tornou a menos facilitada quanto ao seu
desenvolvimento.
Dos Experimentos: Ao observar os gr´aﬁcos de 4 a 8, ´e
importante notar a relac¸˜ao entre as colunas e linhas de barras
nos gr´aﬁcos. As colunas (com valores de 5 a 100%) indicam
quantos sensores foram ativos durante a medic¸˜ao, enquanto as
linhas (com valores de 1 a 20) indicam o n´umero de sensores
que comp˜oem cada regra. Desta forma, para a linha 1, sempre


h´a regras sendo ativadas (para 5, 50 e 100%), pois cada regra
depende apenas de um sensor. Por´em, para a linha 20, por
exemplo, s´o h´a regras sendo ativadas para a coluna de 100%,
pois a ´unica regra presente depende dos 20 sensores.
Figura 4: Tempo m´edio de requisic¸˜ao para ativac¸˜ao de regras
com c´odigo em C++ em plataforma microprocessada
Figura 5: Tempo m´edio de requisic¸˜ao para ativac¸˜ao de regras
com c´odigo em C++ simulado em computador
Para as implementac¸˜oes das regras em C++, Figuras 4
e 5, notam-se comportamentos um tanto diferentes, por´em
ambos tendem a crescer com a complexidade da regra e/ou
n´umero de sensores ativados. Isto indica que um maior n´umero
de requisic¸˜oes causa um maior volume de processamento,
assim como estruturas se-ent˜ao mais complexas geram o
mesmo efeito principalmente para o ambiente microproces-
sado. Tamb´em, nota-se que o n´umero de estruturas se-ent˜ao
ativadas pouco inﬂuencia no tempo de processamento, pois os
valores para uma mesma linha do gr´aﬁco s˜ao muito pr´oximos.
Estes fatos demonstram que o c´odigo em C++ repete
desnecessariamente o processamento para objetos que n˜ao
sofreram mudanc¸a de estado. Claramente, para uma aplicac¸˜ao
real nesta linguagem, o c´odigo seria otimizado para evitar tais
redundˆancias, o que demandaria professional treinado, com
gasto de tempo e esforc¸o para tal. Assim, neste trabalho,
escolheu-se manter o mesmo n´ıvel de diﬁculdade entre as
implementac¸˜oes, para tornar mais justas as comparac¸˜oes.
Figura 6: Tempo m´edio de requisic¸˜ao para ativac¸˜ao de regras
com c´odigo PON Nspc AVR em plataforma microprocessada
Figura 7: Tempo m´edio de requisic¸˜ao para ativac¸˜ao de regras
com c´odigo em PON Namespaces simulado em computador
Considerando agora os resultados das implementac¸˜oes em
PON Namespaces, apresentados nas Figuras 6 e 7, ´e poss´ıvel
notar um comportamento bastante diferenciado do caso an-
terior. Para a plataforma microprocessada, ﬁca evidente que
com o aumento da complexidade das Rules, reduz-se o tempo
m´edio de processamento de uma requisic¸˜ao, o que pode
parecer contraintuitivo. No entanto, isto demonstra que as
notiﬁcac¸˜oes do PON reduzem drasticamente o processamento
redundante, que ocorre no caso do C++, de forma que o
processador ´e ocupado somente quando realmente h´a Rules
para serem aprovadas.
No caso do PON Namespaces simulado, os tempos de
processamento s˜ao mais pr´oximos entre si, devido `a maior
capacidade de processamento da plataforma. Ainda assim,
nota-se que o processador ´e mais exigido somente para os
casos em que de fato h´a aprovac¸˜ao de Rules; resultado
semelhante ao da implementac¸˜ao com PON Framework 4.0,
apresentado na Figura 8, n˜ao sendo poss´ıvel distinguir ambas
as implementac¸˜oes.
Figura 8: Tempo m´edio de requisic¸˜ao para ativac¸˜ao de regras
com c´odigo em PON Frw 4.0 simulado em computador
Nota-se nos resultados uma discrepˆancia, j´a esperada, entre
a plataforma microprocessada e a simulac¸˜ao em computador.
Devido ao maior processamento, o computador consegue res-
ponder mais rapidamente `as requisic¸˜oes, at´e mesmo nos piores
casos em C++, al´em de apresentar tempos semelhantes para
todas as implementac¸˜oes, cujos melhores casos s˜ao aproxima-
damente 40 milissegundos. Entretanto, a implementac¸˜ao em
PON para o microprocessador surge como uma boa alternativa,
pois esta foi capaz de responder cerca de duas vezes mais
r´apido `as requisic¸˜oes do que as simulac¸˜oes, em seus melhores
casos. Isto mostra que o PON, em sua implementac¸˜ao via
LingPON Namespaces, tem um grande potencial, at´e mesmo
para hardwares com pouco poder de processamento, chegando
a se igualar e a superar o c´odigo em programac¸˜ao imperativa.
Claramente, ainda s˜ao necess´arias melhorias quanto ao Name-
spaces, conforme j´a citado, para que possa ser considerado


estado da t´ecnica em PON. No entanto, tais melhorias s˜ao um
caminho natural no grupo de pesquisa.
Figura 9: Tempo m´edio de requisic¸˜oes sem ativac¸˜ao de regras
A Figura 9 apresenta os resultados relativos ao segundo
experimento. Enquanto os resultados anteriores analisavam
o tempo de processamento de poss´ıveis ativac¸˜oes de Ru-
les, causadas por mudanc¸as de estado, o presente resultado
trata apenas do tempo necess´ario para se retornar os estados
atuais. O objetivo deste teste ´e veriﬁcar se h´a diferenc¸as
consider´aveis quanto ao processamento b´asico das diferentes
implementac¸˜oes. Os resultados obtidos, por´em, mostram que
as diferenc¸as s˜ao m´ınimas e as ﬂutuac¸˜oes est˜ao dentro do
esperado. Isto mostra que, para esta aplicac¸˜ao em espec´ıﬁco,
todas as implementac¸˜oes s˜ao igualmente satisfat´orias no que
se trata do envio de mensagens em rede.
Figura 10: Resultados para tr´afego de dados por requisic¸˜ao
Finalmente, os resultados respectivos ao tr´afego de dados na
rede, causados pela comunicac¸˜ao entre sensores, atuadores e
central, est˜ao mostrados na Figura 10. A primeira observac¸˜ao
que deve ser feita ´e que este resultado est´a diretamente
relacionado com a redundˆancia do c´odigo em C++, j´a mencio-
nada anteriormente. Esta redundˆancia faz com que a central
notiﬁque seus atuadores, mesmo quando n˜ao h´a mudanc¸a de
estado, congestionando desnecessariamente a rede. Isto causa
um aumento de 70 a 80 vezes no tr´afego de dados. Outra
observac¸˜ao cab´ıvel, por´em de menor importˆancia, ´e a ligeira
vantagem dos c´odigos carregados no microprocessador, quanto
ao volume de dados gerado. Isto ocorre, pois a vers˜ao do
protocolo TCP/IP ali implementado foi refeita manualmente
e simpliﬁcada, devido `as limitac¸˜oes de mem´oria desta plata-
forma, gerando assim mensagens menores em n´umero de bits.
Em aplicac¸˜oes que dependem fortemente da comunicac¸˜ao
em rede, esta se tornar rapidamente congestionada em um caso
real, se a mudanc¸a de estado de um ´unico sensor causar a
movimentac¸˜ao de um volume t˜ao grande de dados. Os dados
da Figura 10 destacam a importˆancia de se gerar notiﬁcac¸˜oes
apenas quando realmente h´a mudanc¸as de estado.
VI. CONCLUS ˜OES
Este trabalho utilizou o PON em um hardware micro-
processado. Os resultados mostraram que ´e poss´ıvel desen-
volver c´odigos que possuem desempenho igual ou melhor
que a programac¸˜ao imperativa, al´em serem mais eﬁcientes,
dependendo da aplicac¸˜ao. O estudo serviu para demonstrar
que o PON n˜ao est´a restrito a hardwares multicore ou com
grande poder de processamento. Mostrou-se que o PON pode
ser aplicado a plataformas bastante limitadas, estendendo sua
aplicac¸˜ao tamb´em a qualquer tipo de dispositivo de IoT,
alinhando seu uso com a idealizac¸˜ao inicial, de um paradigma
pensado para um sistema distribu´ıdo em rede.
A implementac¸˜ao do PON no cen´ario deste trabalho,
tamb´em serviu para explicitar as vantagens da estrutura pro-
videnciada por este paradigma. Com esforc¸o equipar´avel `a
implementac¸˜ao de uma l´ogica simples em programac¸˜ao im-
perativa, o PON reduz as redundˆancias do c´odigo e pode ser
integrado a sistemas distribu´ıdos sem grande esforc¸o, uma vez
que esteja tecnologicamente est´avel. Contudo, neste ˆambito,
ﬁca a ressalva de que o LingPON Namespaces carece de certas
melhorias, bem como sua melhor adaptac¸˜ao para o compilador
AVR. O est´agio inicial destes, diﬁculta sua programac¸˜ao e
integrac¸˜ao, por´em de forma alguma as impossibilita, conforme
demonstrado neste trabalho.
Como trabalhos futuros, sugere-se estudar melhorias no
LingPON Namespaces AVR e em seu compilador, para
aplicac¸˜oes com microcontroladores. Isto pode propiciar um
c´odigo mais otimizado, em tamanho, al´em da gerac¸˜ao de
c´odigos j´a integrados ao c´odigo b´asico necess´ario para um
microcontrolador. Tamb´em ser˜ao buscadas aplicac¸˜oes mais
complexas e completas, no sentido de haver mais elementos
microprocessados, conectados em rede.
REFERˆENCIAS
[1] F. John Dian, R. Vahidnia, and A. Rahmati, “Wearables and the internet of
things (iot), applications, opportunities, and challenges: A survey,” IEEE
Access, vol. 8, pp. 69200–69211, 2020.
[2] S. Aheleroff, X. Xu, Y. Lu, M. Aristizabal, J. Pablo Vel´asquez, B. Joa,
and Y. Valencia, “Iot-enabled smart appliances under industry 4.0: A case
study,” Advanced Engineering Informatics, vol. 43, p. 101043, 2020.
[3] R. F. Banaszewski, “Paradigma orientado a notiﬁcac¸˜oes: avanc¸os e
comparac¸˜oes,” 2009. Dissertac¸˜ao de Mestrado, CPGEI/UTFPR, Curitiba
- PR.
[4] R. N. Oliveira, “Assistˆencia `a autonomia domiciliar empregando para-
digma orientado a notiﬁcac¸˜oes,” 2019. Dissertac¸˜ao de Mestrado, CP-
GEI/UTFPR, Curitiba - PR.
[5] J. M. Sim˜ao, “A contribution to the development of a hms simulation
tool and proposition of a meta-model for holonic control,” 2005. Doctoral
Thesis, CPGEI/UTFPR (Brazil) - UHP (France), Curitiba - PR.
[6] F. S. Neves, J. M. Sim˜ao, and R. R. Linhares, “Application of generic
programming for the development of a c++ framework for the notiﬁcation
oriented paradigm,” 11th International Conference on Information Society
and Technology, pp. 56–61, 2021.
[7] L. K. Oshiro, A. F. Ronszcka, J. A. Fabro, and J. M. Sim˜ao, “Linguagem
e compilador para o paradigma orientado a notiﬁcac¸˜oes: uma soluc¸˜ao
performante orientada a regras,” in Anais da XII Escola Regional de Alto
Desempenho de S˜ao Paulo, pp. 61–64, SBC, 2021.
[8] A. F. Ronszcka, “M´etodo para a criac¸˜ao de linguagens de programac¸˜ao e
compiladores para o paradigma orientado a notiﬁcac¸˜oes em plataformas
distintas,” . Tese de Doutorado - CPGEI, UTFPR, 2019.
[9] B.
Prayudha,
“Biblioteca
avr-enc28j60,”
2014.
Dispon´ıvel
em:
https://github.com/bprayudha/avr-enc28j60.
Acesso
em:
01
Ago.
2021.


