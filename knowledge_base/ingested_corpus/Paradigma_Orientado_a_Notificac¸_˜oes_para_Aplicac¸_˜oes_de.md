# Paradigma Orientado a Notificac¸ ˜oes para Aplicac¸ ˜oes de.pdf

Paradigma Orientado a Notificac¸˜oes para Aplicac¸˜oes de
Internet das Coisas em Cidades Inteligentes
Luis H. P. Figueiredo1, Jean M. Sim˜ao2, Ana Cristina B. Kochem Vendramin1
1Programa de P´os Graduac¸˜ao em Computac¸˜ao Aplicada (PPGCA)
Universidade Tecnol´ogica Federal do Paran´a (UTFPR) – Curitiba – PR – Brasil
2Programa de P´os Graduac¸˜ao em Engenharia El´etrica
e Inform´atica Industrial (CPGEI)
Universidade Tecnol´ogica Federal do Paran´a (UTFPR) – Curitiba – PR – Brasil
luisfigueiredo@alunos.utfpr.edu.br,{jeansimao,criskochem}@utfpr.edu.br
Abstract. The Internet of Things (IoT) for Smart Cities enables a better use of
resources and services. However, the technological challenges for the creation
of efficient computational systems increase due to the number and complexity of
interactions. This paper proposes a Distributed version of the Notification Ori-
ented Paradigm (NOP) via a publish/subscribe architecture with the Message
Queuing Telemetry Transport (MQTT) protocol. Performance of NOP and the
object-oriented programming paradigm are compared in a generic IoT applica-
tion. Results show that by distributing the NOP entities, it is possible to reduce
the execution, processing and response times of the application at the cost of
higher memory usage.
Resumo. A Internet das Coisas para Cidades Inteligentes possibilita um me-
lhor uso dos recursos e servic¸os.
Por´em, os desafios tecnol´ogicos para a
criac¸˜ao de sistemas computacionais eficientes aumentam devido ao n´umero
e complexidade das interac¸˜oes.
Este artigo prop˜oe distribuir as entidades
do Paradigma Orientado a Notificac¸˜oes (PON) por meio de uma arquite-
tura publicac¸˜ao/assinatura com o protocolo MQTT. O desempenho do PON e
do paradigma de programac¸˜ao orientado a objetos s˜ao comparados em uma
aplicac¸˜ao gen´erica de Internet das Coisas. Os resultados mostram que ao dis-
tribuir as entidades do PON ´e poss´ıvel reduzir o tempo de execuc¸˜ao, processa-
mento e resposta da aplicac¸˜ao ao custo de um maior uso de mem´oria.
1. INTRODUC¸ ˜AO
A Internet das Coisas (ou IoT do termo em inglˆes Internet of Things) contribui para a
construc¸˜ao das Cidades Inteligentes em diversos aspectos. O uso dos sistemas compu-
tacionais e dos dispositivos sensores e atuadores conectados por meio da IoT permite o
aprimoramento na forma de interac¸˜ao com o ambiente e um melhor uso dos recursos e
servic¸os, seja em uma pequena residˆencia ou em uma grande metr´opole. Como exem-
plos, pode-se considerar: um sistema de controle de tr´afego inteligente, fazendo uso de
sensores de contagem de ve´ıculos e atuando por meio dos sem´aforos com o objetivo de
melhorar o fluxo de ve´ıculos em uma determinada regi˜ao; e um sistema de iluminac¸˜ao
p´ublica inteligente, cujos sensores de luminosidade natural e do fluxo de passagem de
Anais Estendidos do XVIII Simpósio Brasileiro de Sistemas de Informação (SBSI 2022)
0326


pessoas e ve´ıculos podem permitir o controle da intensidade luminosa das lˆampadas, re-
duzindo o desperd´ıcio de energia el´etrica.
Por´
se por um lado a sociedade se beneficia dessa revoluc¸
em,
˜ao promovida pe-
las aplicac¸˜oes IoT nos diversos ˆambitos de uma cidade inteligente, por outro lado essa
crescente demanda por desenvolvimento de software agrava ainda mais a chamada ’Crise
de Software’ [Bautsch 2007]. Resumidamente, a ’Crise de Software’ indica a dificuldade
na produc¸˜ao de software frente ao r´apido crescimento da demanda aliada ao aumento da
complexidade dos problemas a serem resolvidos [Ronszcka 2019][Bautsch 2007].
´E necess´ario que as t´ecnicas, ferramentas de projeto, an´alise e implementac¸˜ao
de sistemas, em especial de sistemas distribu´ıdos voltados para IoT, tornem-se cada vez
mais f´aceis e acess´ıveis aos desenvolvedores de sistemas, ao mesmo tempo que condu-
zam a implementac¸˜oes mais eficientes e eficazes. Por´em, os paradigmas de programac¸˜ao
atualmente dominantes e usuais, derivados dos primordiais Paradigmas Imperativos (PI)
e dos Paradigmas Declarativos (PD), apresentam ineficiˆencias para o desenvolvimento
e execuc¸˜ao de programas, principalmente em ambientes concorrentes e/ou distribu´ıdos
[Ronszcka 2019] [Sim˜ao and Stadzisz 2008].
O Paradigma Orientado a Notificac¸˜oes (PON) surge justamente como uma alter-
nativa aos paradigmas de programac¸˜ao existentes [Sim˜ao and Stadzisz 2008]. Em sua
concepc¸˜ao, o PON agrega caracter´ısticas desejadas do PI (nomeadamente a orientac¸˜ao a
objetos) e PD (nomeadamente a programac¸˜ao l´ogica) ao mesmo tempo que resolve parte
dos seus problemas e limitac¸˜oes facilitando o desenvolvimento de aplicac¸˜oes mesmo em
ambientes concorrentes e/ou distribu´ıdos, ao mesmo tempo que as torna mais eficientes
no uso dos recursos computacionais [Sim˜ao and Stadzisz 2008] [Ronszcka 2019].
Para a programac¸˜ao de aplicac¸˜oes segundo o PON, existem diversos aparatos tec-
nol´ogicos j´a desenvolvidos. Enquanto estado da arte, o mais relevante ´e a linguagem de
programac¸˜ao e compilac¸˜ao pr´opria do paradigma, conhecida como tecnologia LingPON
[Oshiro et al. 2021]. Enquanto estado da t´ecnica, h´a um conjunto de fraweworks imple-
mentados em diversas linguagens de programac¸˜ao orientada a objetos, alterando assim
suas formas usuais de utilizac¸˜ao. Este trabalho prop˜oe um aprimoramento do Framework
PON C++ 4.0 [Neves et al. 2021] apresentando, de forma inovadora, o PON no contexto
de sistemas distribu´ıdos para IoT por meio de um protocolo de mensagens padronizado e
arquitetura publicac¸˜ao/assinatura.
2. PARADIGMA ORIENTADO A NOTIFICAC¸ ˜OES
Dentre os principais problemas encontrados em PI e PL, pode-se citar: a redundˆancia
temporal que ocorre principalmente nos ciclos impl´ıcitos de execuc¸˜ao do paradigma im-
perativo os quais frequentemente avaliam desnecessariamente vari´aveis que n˜ao tiveram
seus valores alterados desde o ´ultimo ciclo de verificac¸˜ao; e o forte acoplamento de c´odigo
entre express˜oes causais e estrutura de fatos/dados, a qual n˜ao permite ou dificulta a
execuc¸˜ao paralela e/ou distribu´ıda de instruc¸˜oes. O PON surge nesse cen´ario como uma
alternativa, possuindo mecanismos que eliminam (ou ao menos diminuem) os problemas
apresentados sem perder as caracter´ısticas desej´aveis dos paradigmas como a coes˜ao, a
abstrac¸˜ao e a clareza de c´odigo [Sim˜ao and Stadzisz 2008] [Banaszewski 2009].
O principal diferencial do PON, quando comparado ao PD ou PI, ´e a utilizac¸˜ao
de um mecanismo de notificac¸˜ao que ocorre por meio de entidades minimalistas, colabo-
Anais Estendidos do XVIII Simpósio Brasileiro de Sistemas de Informação (SBSI 2022)
0327


rativas e adaptadas para tal. Dessa forma, as notificac¸˜oes s˜ao geradas e recebidas pelas
entidades apenas nos momentos pertinentes, ou seja, quando de fato h´a mudanc¸as de es-
tado que demandem uma nova avaliac¸˜ao l´ogico-causal. Esse mecanismo faz com que os
sistemas desenvolvidos em PON sejam mais concisos quanto ao uso de recursos compu-
tacionais [Sim˜ao and Stadzisz 2008] [Neves et al. 2021].
Em linhas gerais, o PON prop˜oe a divis˜ao da computabilidade em dois grandes
grupos relacionados entre si por meio de notificac¸˜oes de seus constituintes, conforme
exemplificado na Figura 1 [Sim˜ao and Stadzisz 2008] [Banaszewski 2009]: (i) o grupo
que trata do processamento facto-execucional por meio de entidades chamadas Fact-Base-
Elements (FBEs). As FBEs s˜ao as entidades respons´aveis por representar entidades do
mundo real ou abstrato por meio de estados (Attributes) e servic¸os (Methods), de forma
an´aloga (mas, distinta) aos objetos do Paradigma Orientado a Objetos (POO); (ii) o grupo
que trata do processamento l´ogico-causal por meio de entidades chamadas de Rules, de
forma an´aloga (mas, distinta) aos Sistemas Baseados em Regras (SBR). Cada Attribute ´e
capaz de notificar as Rules por meio das Premises e Conditions, enquanto cada Method ´e
capaz de ser instigado pelas Rules por meio das Actions e Instigations.
(a) Interac¸˜ao entre entidades do PON.
(b) Ciclo de notificac¸˜oes.
Figura 1. Paradigma Orientado a Notificac¸ ˜oes.
[Oshiro et al. 2021]
A relac¸˜ao entre as entidades constituintes do PON ´e ilustrada na Figura 1a por
meio de um exemplo que utiliza como base um sistema simples de alarme. Como re-
quisito funcional, tem-se um ambiente (FBE Sector) no qual se o estado (atState) de um
sensor (FBE Sensor) for igual a um valor de referˆencia (atReference) e ainda n˜ao estiver
alarmado (atIntruderDetected), ent˜ao os usu´arios ser˜ao notificados (mtNotifyInvasion).
Destaca-se a maneira inovadora de colaborac¸˜ao das entidades do PON por meio
de notificac¸˜oes, conforme Figura 1b. Ao mudar de estado, cada Attribute de uma instˆancia
de um FBE notifica apenas as Premises pertinentes, que refazem seus c´alculos l´ogicos.
Por sua vez, cada Premise que mudar de estado l´ogico notifica apenas as Conditions per-
tinentes, as quais refazem seus c´alculos l´ogicos pelos estados notificados contabilizados.
Se a Condition ´e aprovada, ela pode aprovar sua respectiva Rule. Esta, quando apro-
vada, ativa sua Action, que notifica suas Instigations, as quais instigam os Methods. Estes
´ultimos geralmente alteram os estados dos Attributes, reativando o fluxo de notificac¸˜oes.
Por considerar as alterac¸˜oes dos Attributes para desencadear os ciclos de notificac¸˜oes, o
PON elimina a redundˆancia temporal, pois as avaliac¸˜oes l´ogicas passam a ser executadas
somente quando existe uma alterac¸˜ao pertinente. Ademais, as conex˜oes entre as entidades
ocorrem em tempo de construc¸˜ao dos sistemas [Oshiro et al. 2021] [Ronszcka 2019].
Anais Estendidos do XVIII Simpósio Brasileiro de Sistemas de Informação (SBSI 2022)
0328


3. PON DISTRIBU´IDO PARA IOT
O presente trabalho prop˜oe a distribuic¸˜ao, experimentac¸˜ao e a comparac¸˜ao do PON em
um ambiente de IoT por meio de um sistema de correlac¸˜ao de sensores e atuadores, uti-
lizando arquiteturas e protocolos t´ıpicos desse contexto. Esse tipo de aplicac¸˜ao ´e muito
comum em cidades inteligentes, estando presentes, por exemplo, nos sistemas de controle
de tr´afego inteligente, os quais fazem uso de sensores (contagem de ve´ıculos) e atuadores
(sem´aforos) ou em um contexto de iluminac¸˜ao p´ublica inteligente, cujos sensores de lumi-
nosidade natural e do fluxo de passagem de pessoas e ve´ıculos podem permitir o controle
da intensidade luminosa das lˆampadas.
Para permitir a distribuic¸˜ao do PON, alterac¸˜oes foram adicionadas no Framework
PON C++ 4.0 de modo a permitir que as interac¸˜oes entre todas as entidades do PON
acontec¸am por meio da publicac¸˜ao ou recebimento de mensagens via rede. Por exemplo,
um Attribute distribu´ıdo pode ter seu estado alterado via recebimento de mensagens de
rede e notificar a(s) Premise(s) interessada(s) conforme o mecanismo do PON. Como a
mensagem que desencadeia as alterac¸˜oes segue o protocolo padronizado, a alterac¸˜ao do
Attribute distribu´ıdo pode ocorrer via alterac¸˜ao de um outro Attribute distribu´ıdo ou de
outro elemento gen´erico como, por exemplo, um sensor ou aplicac¸˜ao IoT.
Para a comunicac¸˜ao, utiliza-se o protocolo MQTT (Message Queuing Teleme-
try Transport) padronizado pelo OASIS para IoT e um dos protocolos que apresentam
maior suporte em plataformas comerciais [Al-Masri et al. 2020]. O MQTT implementa
o padr˜ao publicac¸˜ao/assinatura, desacoplando o cliente editor (sensor) do(s) cliente(s) as-
sinante(s) por meio de uma estrutura de t´opicos inserida em um elemento intermedi´ario
conhecido como broker. Quando o cliente editor publica uma mensagem em determi-
nado t´opico, esta mensagem ´e repassada para os clientes assinantes que previamente te-
nham registrado interesse no respectivo t´opico. O broker ´e respons´avel pela criac¸˜ao e
gerenciamento de t´opicos os quais permitem a identificac¸˜ao e filtragem de mensagens de
acordo com um determinado dom´ınio [mqt ]. A correspondˆencia entre cada entidade do
PON e os t´opicos MQTT segue um padr˜ao de nomenclatura de t´opicos, nomeadamente
<dom´ınio>/<entidade PON>/<Identificac¸˜ao ´Unica>/<conte´udo>.
Como exemplo,
considera-se o Attribute distribu´ıdo atState da FBE Sensor apresentado na Figura 2a, in-
teragindo por meio do t´opico ”Sensor/at/atState/”. De forma similar, as demais entidades
do PON podem publicar mensagens em t´opicos, assinar/registrar em interesse em t´opicos
e consumir as mensagens em t´opicos que sejam de seus interesses.
(a) Interac¸˜oes com o MQTT.
(b) Exemplo de aplicac¸˜ao IoT.
Figura 2. PON distribu´ıdo.
Anais Estendidos do XVIII Simpósio Brasileiro de Sistemas de Informação (SBSI 2022)
0329


4. EXPERIMENTOS
No cen´ario proposto para an´alise, consideram-se N sensores e M atuadores os quais in-
teragem com uma central controladora exclusivamente por meio de mensagens MQTT
enviadas e recebidas ao/do broker, conforme ilustrado na Figura 2b. Ao detectar uma
mudanc¸a de estado, os sensores (clientes editores) podem publicar mensagens em t´opicos
espec´ıficos no broker, servindo como notificac¸˜ao `a central controladora. Por sua vez, os
elementos atuadores (clientes assinantes) recebem comandos da central controladora, via
broker, por meio de mensagens publicadas nos t´opicos pertinentes os quais foram previa-
mente subscritos pelos atuadores.
Como os sensores e atuadores possuem uma l´ogica relativamente simples, neces-
sitando apenas notificar uma mudanc¸a de estado e receber comandos da central controla-
dora, optou-se por n˜ao consider´a-los na an´alise. Dessa forma, utilizou-se duas aplicac¸˜oes
auxiliares sendo uma delas respons´avel por publicar mensagens de mudanc¸as de estados
em seus respectivos t´opicos no broker e a outra respons´avel por receber os comandos de
controle enviados pela central controladora para os atuadores.
Por sua vez, a central controladora, na qual a l´ogica de processamento dos eventos
acontece, foi implementada utilizando-se dois paradigmas: (i) o Paradigma Orientado
a Objetos (POO) distribu´ıdo por meio do protocolo MQTT; (ii) o PON via Framework
PON C++ 4.0 distribu´ıdo com MQTT. Para fins de an´alise, implementou-se tamb´em a
central controladora nas vers˜oes n˜ao distribu´ıdas do POO e do PON via Framework PON
C++ 4.0. Para uma comparac¸˜ao justa entre as implementac¸˜oes distribu´ıdas, utilizou-se o
mesmo broker de mensagens e bibliotecas de comunicac¸˜ao MQTT. O broker utilizado foi
o Mosquitto e suas respectivas bibliotecas de comunicac¸˜ao em C++ [Light 2017].
Para avaliar o desempenho desses paradigmas em diferentes condic¸˜oes e
configurac¸˜oes t´ıpicas em ambientes de IoT, foram criados cen´arios com diferentes percen-
tuais de ativac¸˜oes dos sensores. Para as implementac¸˜oes em PON, cada conjunto de regras
l´ogico-causais foi transcrito para o respectivo conjunto de Rules. Para as implementac¸˜oes
em POO utilizou-se estruturas decis´orias usuais de “se-ent˜ao“ avaliando por meio de cha-
madas de m´etodos os estados dos respectivos objetos e, quando pertinente, atuando por
meio dos m´etodos dos respectivos objetos.
Utilizou-se um processador Intel(R) Core(TM) i7-8665U, Quad Core, 2.11 GHz,
16GB de mem´oria RAM DDR4 e sistema operacional Windows 10 Enterprise. Para evitar
eventuais atrasos na rede de comunicac¸˜ao, avaliou-se todo o sistema na m´aquina local. As
seguintes m´etricas de desempenho s˜ao avaliadas:
• Tempo m´
de execuc¸
edio
˜ao da aplicac¸˜ao: tempo total de execuc¸˜ao incluindo
a inicializac¸˜ao das estruturas (por exemplo, os objetos do POO) e os ciclos de
avaliac¸˜oes l´ogicas dos estados e respectivas alterac¸˜oes;
• Tempo m´edio de processamento das mensagens: tempo de processamento ap´os
a alterac¸˜ao de estado de um sensor, sendo a diferenc¸a de tempo entre o recebi-
mento de uma mensagem e a finalizac¸˜ao da avaliac¸˜ao dessa mensagem. Optou-se
por avaliar o tempo m´edio de processamento das mensagens em duas situac¸˜oes:
(i) quando a mensagem recebida provoca alterac¸˜ao no estado de um atuador e; (ii)
quando a mensagem recebida n˜ao provoca alterac¸˜ao no estado de um atuador;
• Tempo m´edio de resposta do sistema: tempo m´edio para ativac¸˜ao de um atuador
ap´os alterac¸˜ao do respectivo sensor, representando a diferenc¸a de tempo entre o
Anais Estendidos do XVIII Simpósio Brasileiro de Sistemas de Informação (SBSI 2022)
0330


recebimento de uma mensagem MQTT indicando a troca do estado de um sensor
e a consequente mensagem MQTT de ativac¸˜ao de um atuador;
• Uso m´aximo de recursos de processamento e mem´oria: alocac¸˜ao de mem´oria
m´axima necess´aria para a execuc¸˜ao de uma aplicac¸˜ao e o uso m´aximo de recursos
de processamento.
Para avaliar o tempo m´edio da execuc¸˜ao da aplicac¸˜ao, utilizou-se o framework
do Google benchmark e o conjunto de testes propostos por [Neves et al. 2021]. Esse
conjunto consiste na inicializac¸˜ao de 100.000 sensores e posterior alterac¸˜ao do valor de
porcentagem de sensores (0,001, 0,01, 0,1, 1, 10 e 100) e suas respectivas avaliac¸˜oes
l´ogicas decorrentes. Para o PON distribu´ıdo e POO distribu´ıdo, considerou-se o uso de
sensores alter´aveis via mensagens MQTT e via c´odigo local.
Para a avaliac¸˜ao do tempo m´edio de processamento das mensagens utilizou-se
a biblioteca chrono para a medic¸˜ao da diferenc¸a de tempo entre o recebimento de uma
mensagem MQTT at´e a finalizac¸˜ao desse processamento e liberac¸˜ao para o processamento
de uma nova mensagem. Para a avaliac¸˜ao do tempo de resposta do sistema, utilizou-se
o software Wireshark para o registro dos pacotes recebidos e enviados e um script auxiliar
para processamento dos dados gerados pelo Wireshark, contabilizando o tempo entre uma
requisic¸˜ao e sua consequente resposta. Em ambos experimentos, utilizou-se um conjunto
de 1.000 sensores com correspondˆencia para 1.000 atuadores sendo que a ativac¸˜ao de
um sensor provoca a ativac¸˜ao de um correspondente atuador. A ativac¸˜ao do sensor ocorre
com base na comparac¸˜ao de um valor inteiro recebido na mensagem MQTT com um valor
interno, iniciado em zero e incrementado a cada ativac¸˜ao. As mensagens de alterac¸˜ao dos
sensores foram produzidas por uma aplicac¸˜ao externa respons´avel por publicar mensagens
de acordo com os campos e valores esperados a cada 0,01 segundo. Cada avaliac¸˜ao foi
feita com base na alterac¸˜ao dos 1.000 sensores, duas vezes cada, totalizando 2.000 ciclos.
Para avaliar o uso de processamento e mem´oria utilizou-se a ferramenta de di-
agn´ostico disponibilizada no ambiente de desenvolvimento Microsoft Visual Studio 2019,
considerando-se o cen´ario com 100.000 sensores e 100% de taxa de alterac¸˜ao.
5. RESULTADOS
O tempo m´edio de execuc¸˜ao de uma aplicac¸˜ao variando o percentual de sensores que tˆem
seu estado modificado pode ser visto na Figura 3. Observa-se que as implementac¸˜oes
em PON via Framework PON C++ 4.0 e sua vers˜ao distribu´ıda apresentaram um melhor
desempenho em relac¸˜ao ao POO quando o percentual de ativac¸˜oes foi baixo e um de-
sempenho inferior para taxas de ativac¸˜oes mais altas. Ademais, ´e poss´ıvel observar que
o tempo de execuc¸˜ao da vers˜ao distribu´ıda do Framework PON C++ 4.0 foi ligeiramente
superior ao da vers˜ao n˜ao distribu´ıda o que pode ser considerado dentro do esperado, visto
que foram adicionadas estruturas auxiliares para distribuic¸˜ao das entidades do PON.
Os resultados da avaliac¸˜ao do tempo m´edio de processamento das mensagens e do
tempo m´edio de resposta do sistema s˜ao apresentados na Figura 4. Os resultados mostram
que o PON em sua vers˜ao distribu´ıda apresentou tempos de processamento e resposta
menores que o POO nos dois cen´arios: o tempo de processamento foi 20% menor no
cen´ario com a ativac¸˜ao de atuadores e 69% menor no cen´ario sem a ativac¸˜ao de atuadores;
o tempo de resposta foi, em m´edia, 16% menor. Esses resultados demonstram que o
Anais Estendidos do XVIII Simpósio Brasileiro de Sistemas de Informação (SBSI 2022)
0331


Figura 3. Tempo m´edio de execuc¸ ˜ao.
mecanismo de notificac¸˜oes pontuais e concisas do PON reduz as redundˆancias fazendo
com que o processamento ocorra somente nas partes que tiveram seu estado alterado.
(a) Tempo m´edio de processamento.
(b) Tempo m´edio de resposta.
Figura 4. Tempo m´edio de processamento e de resposta.
O uso de mem´oria RAM da aplicac¸˜ao em POO e POO distribu´ıdo foi de 14,4
MB e 25,9 MB, respectivamente. Nas aplicac¸˜oes com PON e PON distribu´ıdo o uso
m´aximo de mem´oria RAM foi de 411,0 MB e 424,8 MB, respectivamente. O uso de
processador em todas as implementac¸˜oes foi de aproximadamente 13%. Observa-se que
as implementac¸˜oes em PON via Framework PON C++ 4.0 utilizaram cerca de 20 vezes
mais mem´oria RAM do que as aplicac¸˜oes em POO. Al´em disso, as implementac¸˜oes dis-
tribu´ıdas utilizaram mais mem´oria RAM que as implementac¸˜oes n˜ao distribu´ıdas. Nesse
contexto, o maior uso de mem´oria RAM pelas aplicac¸˜oes em PON via frameworks pode
ser considerado dentro do esperado por conta da estrutura adicional do pr´oprio framework.
O maior uso de mem´oria do PON distribu´ıdo se justifica pelas estruturas adicionais ne-
cess´arias para distribuic¸˜ao das entidades do PON.
6. CONCLUS ˜OES
Este trabalho apresentou, de forma inovadora, o PON em um ambiente distribu´ıdo por
meio de uma arquitetura Publicac¸˜ao/Assinatura com o protocolo MQTT, mostrando a
adaptabilidade e boa aderˆencia do paradigma em arquiteturas desse tipo.
Anais Estendidos do XVIII Simpósio Brasileiro de Sistemas de Informação (SBSI 2022)
0332


Os resultados mostraram que, em cen´arios com pouca variac¸˜ao dos estados
do sistema, a implementac¸˜ao em PON via Framework PON C++ 4.0 ´e superior `as
implementac¸˜oes desenvolvidas com POO em termos de tempos de execuc¸˜ao. Em relac¸˜ao
ao tempo de processamento, o PON distribu´ıdo foi mais eficiente que o POO distribu´ıdo
em ambos os cen´arios, apresentando um tempo de processamento 22% menor no cen´ario
com ativac¸˜ao de atuadores e 69% menor no cen´ario sem a ativac¸˜ao de atuadores. Em
relac¸˜ao ao tempo de resposta da aplicac¸˜ao, considerando a ativac¸˜ao dos atuadores, no
PON distribu´ıdo esse tempo foi, em m´edia, 16% melhor que o POO distribu´ıdo. Observa-
se, por´em, que nas aplicac¸˜oes em PON (distribu´ıdo e n˜ao distribu´ıdo), devido ao uso de
frameworks (nomeadamente do Framework PON C++ 4.0), o uso de mem´oria RAM ´e
cerca de 20 vezes maior que as aplicac¸˜oes em POO, o que pode dificultar o seu uso em
dispositivos com poucos recursos de mem´oria dispon´ıveis.
Como trabalhos futuros, sugere-se os aprimoramentos da tecnologia LingPON
com foco na gerac¸˜ao de c´odigo contemplando elementos distribu´ıdos via rede e do Fra-
mework PON C++ 4.0 em sua vers˜ao distribu´ıda apresentada neste artigo, com foco na
otimizac¸˜ao do uso dos recursos de mem´oria e processamento.
Referˆencias
MQTT Version 5.0.
OASIS Standard.
Dispon´ıvel em:
https://docs.oasis-
open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html. Acesso em 23 de marc¸o de 2022.
Al-Masri, E., Kalyanam, K. R., Batts, J., Kim, J., Singh, S., Vo, T., and Yan, C. (2020). In-
vestigating messaging protocols for the internet of things (iot). IEEE Access, 8:94880–
94911.
Banaszewski, R. F. (2009). Paradigma orientado a notificac¸˜oes: avanc¸os e comparac¸˜oes.
Master’s thesis. CPGEI / UTFPR. Curitiba, Brasil.
Bautsch, M. (2007). Cycles of software crises. ENISA Quarterly on Secure Software,
vol. 3, no. 4, p. 3-5.
Light, R. A. (2017). Mosquitto: server and client implementation of the mqtt protocol.
Journal of Open Source Software, 2(13):265.
Neves, F. d. S., R., L. R., and Sim˜ao, J. M. (2021). Application of generic programming
for the development of a c++ framework for the notification oriented paradigm. pages
44–49. 11th International Conference on Information Society and Technology.
Oshiro, L., Ronszcka, A., Fabro, J., and Sim˜ao, J. (2021). Linguagem e compilador para
o paradigma orientado a notificac¸˜oes: Uma soluc¸˜ao performante orientada a regras. In
Anais da XII Escola Regional de Alto Desempenho de S˜ao Paulo. p61–64, Brasil. SBC.
Ronszcka, A. F. (2019). M´etodo para a criac¸˜ao de linguagens de programac¸˜ao e com-
piladores para o paradigma orientado a notificac¸˜oes em plataformas distintas. PhD
thesis, CPGEI / UTFPR, Curitiba.
Sim˜ao, J. M. and Stadzisz, P. C. (2008). Paradigma orientado a notificac¸˜oes (pon)–uma
t´ecnica de composic¸˜ao e execuc¸˜ao de software orientado a notificac¸˜oes. PI08055181,
data de dep´osito: 26/11/2008. Universidade Tecnol´ogica Federal do Paran´a - UTFPR.
Anais Estendidos do XVIII Simpósio Brasileiro de Sistemas de Informação (SBSI 2022)
0333


