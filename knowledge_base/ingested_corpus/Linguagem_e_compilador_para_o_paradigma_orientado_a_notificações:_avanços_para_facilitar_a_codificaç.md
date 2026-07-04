# Linguagem e compilador para o paradigma orientado a notificações: avanços para facilitar a codificação e sua validação em uma aplicação de controle de futebol de robôs.pdf

UNIVERSIDADE TECNOL´OGICA FEDERAL DO PARAN´A
PROGRAMA DE P´OS-GRADUAC¸ ˜AO EM ENGENHARIA EL´ETRICA
E INFORM´ATICA INDUSTRIAL
LEONARDO ARAUJO SANTOS
LINGUAGEM E COMPILADOR PARA O PARADIGMA
ORIENTADO A NOTIFICAC¸ ˜OES: AVANC¸ OS PARA
FACILITAR A CODIFICAC¸ ˜AO E SUA VALIDAC¸ ˜AO EM
UMA APLICAC¸ ˜AO DE CONTROLE DE FUTEBOL DE
ROBˆOS
DISSERTAC¸ ˜AO
CURITIBA
2017


LEONARDO ARAUJO SANTOS
LINGUAGEM E COMPILADOR PARA O PARADIGMA
ORIENTADO A NOTIFICAC¸ ˜OES: AVANC¸ OS PARA
FACILITAR A CODIFICAC¸ ˜AO E SUA VALIDAC¸ ˜AO EM
UMA APLICAC¸ ˜AO DE CONTROLE DE FUTEBOL DE
ROBˆOS
Disserta¸c˜ao apresentada ao Programa de P´os-
gradua¸c˜ao em Engenharia El´etrica e Inform´atica
Industrial da Universidade Tecnol´ogica Federal do
Paran´a como requisito parcial para obten¸c˜ao do
grau de “Mestre em Ciˆencias” - ´Area de Concen-
tra¸c˜ao: Engenharia de Computa¸c˜ao.
Orientador:
Prof. Dr. Jean Marcelo Sim˜ao
Co-orientador: Prof. Dr. Jo˜ao Alberto Fabro
CURITIBA
2017


Dados Internacionais de Catalogação na Publicação 
 
 
Santos, Leonardo Araujo 
S237L           Linguagem e compilador para o paradigma orientado a notifi- 
2017        cações: avanços para facilitar a codificação e sua validação em 
uma aplicação de controle de futebol de robôs / Leonardo Araujo 
Santos.-- 2017. 
274 p. : il. ; 30 cm 
 
Texto em português, com resumo em inglês 
Disponível também via World Wide Web 
Dissertação (Mestrado) - Universidade Tecnológica Federal 
do Paraná. Programa de Pós-graduação em Engenharia Elétrica 
e Informática Industrial, Curitiba, 2017  
Bibliografia: p. 128-135 
 
1. Paradigma orientado a notificações. 2. Futebol – Simulação 
por computador. 3. Robótica. 4. Robôs. 5. Framework (Programa 
de computador). 6. C++ (Linguagem de programação de compu-
tador). 7. Engenharia elétrica – Dissertações. I. Simão, Jean Mar-
celo. II. Fabro, João Alberto. III. Universidade Tecnológica Fede-
ral do Paraná. Programa de Pós-Graduação em Engenharia Elé-
trica e Informática Industrial. IV. Título.  
 
CDD: Ed. 22 – 621.3 
Biblioteca Central da UTFPR, Câmpus Curitiba 


 
 
UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ 
Câmpus Curitiba 
                              
 
Programa de Pós-Graduação em Engenharia Elétrica e Informática Industrial 
 
 
Título da Dissertação Nº. ____ 
 
Linguagem e Compilador para o Paradigma 
orientado a Notificações: Avanços para 
Facilitar a codificação e sua Validação em 
uma Aplicação de Controle de Futebol de 
Robôs 
 
por 
Leonardo Araujo Santos  
Orientador: Prof. Dr. Jean Marcelo Simão (UTFPR) 
Coorientador: Prof. Dr. João Alberto Fabro (UTFPR) 
 
Esta dissertação foi apresentada como requisito parcial à obtenção do grau de 
MESTRE EM CIÊNCIAS – Área de Concentração: ENGENHARIA DE COMPUTAÇÃO do 
Programa de Pós-Graduação em Engenharia Elétrica e Informática Industrial – 
CPGEI – da Universidade Tecnológica Federal do Paraná – UTFPR, às 15:30h  do 
dia  31 de março 2017. O trabalho foi aprovado pela Banca Examinadora, composta 
pelos professores doutores: 
 
 
 
 
 
 
_____________________________________ 
Prof. Dr. Paulo Cézar Stadzisz 
(Presidente – UTFPR) 
 
 
 
 
 
___________________________________ 
Prof. Dr. André Murbach Maidl 
(PUC-PR) 
 
 
 
 
 
 
___________________________________ 
Prof. Dr. André Schneider de Oliveira 
(UTFPR) 
___________________________________ 
Prof. Dr. Robson Ribeiro Linhares 
(UTFPR)  
 
 
 
Visto da coordenação: 
 
 
 
 
 
    ________________________________ 
Prof. Jean Carlos Cardozo da Silva, Dr. 
 (Coordenador do CPGEI) 
 


AGRADECIMENTO 
 
Agradeço, primeiramente, a Deus, por ter me concedido vida e saúde para 
concluir este trabalho. 
Agradeço à minha esposa, Jaqueline Prudencio Santos, por todo o carinho e 
incentivo que tanto me ajudaram a alcançar este objetivo. 
Agradeço aos meus pais Henrique Guimarães dos Santos e Ione Araujo Santos 
e minha irmã Ingrid Santos Andor, por todo amor ao longo de toda a minha vida. 
Agradeço aos professores Jean Marcelo Simão e João Alberto Fabro pelos 
conselhos e orientação e co-orientação durante este período de mestrado.  
Agradeço aos professores Paulo Cézar Stadzisz, André Murbach Maidl, André 
Schneider de Oliveira e Robson Linhares, membros da banca, pela disponibilidade em 
avaliar este trabalho e apresentar sugestões e correções pertinentes. 
 
 


RESUMO
Araujo Santos, Leonardo. LINGUAGEM E COMPILADOR PARA O PARADIGMA
ORIENTADO A NOTIFICAC¸ ˜OES: AVANC¸OS PARA FACILITAR A CODIFICAC¸ ˜AO
E SUA VALIDAC¸ ˜AO EM UMA APLICAC¸ ˜AO DE CONTROLE DE FUTEBOL DE
ROBˆOS. 293 f. Disserta¸c˜ao – Programa de P´os-gradua¸c˜ao em Engenharia El´etrica e
Inform´atica Industrial, Universidade Tecnol´ogica Federal do Paran´a. Curitiba, 2017.
As t´ecnicas de programa¸c˜ao baseadas no Paradigma Imperativo (PI) e Paradigma Decla-
rativo (PD) apresentam limita¸c˜oes como redundˆancias e acoplamentos, os quais podem
prejudicar o desenvolvimento e execu¸c˜ao de softwares. Visando solucionar algumas das de-
ﬁciˆencias desses paradigmas de programa¸c˜ao surgiu o Paradigma Orientado a Notiﬁca¸c˜oes
(PON), o qual apresenta uma nova forma de realizar avalia¸c˜oes l´ogico-causais. Isto ´e
realizado atrav´es de entidades computacionais de pequeno porte, reativas e desacopladas
que colaboram por meio de notiﬁca¸c˜oes pontuais. O PON foi originalmente materializado
na forma de um Framework, implementado na linguagem de programa¸c˜ao C++. Este foi
projetado de forma a fornecer interfaces de alto n´ıvel que facilitassem o desenvolvimento
de aplica¸c˜oes PON. Entretanto, internamente, o Framework usa estruturas de dados
que induzem a uma sobrecarga de processamento computacional e consequente preju´ızo
ao desempenho das aplica¸c˜oes. Visando solucionar esse problema, uma linguagem de
programa¸c˜ao espec´ıﬁca para o PON, nomeada LingPON, e respectivo compilador, foram
criados recentemente. Entretanto, em um primeiro esfor¸co, apenas algumas poucas e
simples aplica¸c˜oes PON foram criadas utilizando a LingPON, fato este que n˜ao permite
sua consolida¸c˜ao mais efetiva. Isso se deve, principalmente, a algumas limita¸c˜oes que
existem na atual vers˜ao da linguagem, as quais diﬁcultam o desenvolvimento de aplica¸c˜oes
complexas que solucionem problemas real´ısticos. Neste sentido, este trabalho prop˜oe uma
nova vers˜ao da LingPON (vers˜ao 1.2), baseada em agrega¸c˜oes de entidades, na qual ´e
poss´ıvel criar aplica¸c˜oes complexas de forma mais f´acil e direta. Os avan¸cos s˜ao validados
por meio do desenvolvimento de um software, utilizando a LingPON (vers˜ao 1.0 e 1.2),
para algo reconhecidamente complexo. O software em quest˜ao trata do controle para
partidas de futebol de robˆos (Robocup). Ao ﬁnal, o software desenvolvido utilizando o
LingPON ´e comparado quantitativamente e qualitativamente com um software equivalente
desenvolvido o utilizando o Framework PON 2.0 e outro software equivalente desenvolvido
com o Paradigma Orientado a Objetos utilizando a linguagem de programa¸c˜ao C++
(este programado por outrem). Os resultados obtidos mostraram que ao utilizar a nova
vers˜ao da LingPON, apresentada neste trabalho, ´e poss´ıvel desenvolver aplica¸c˜oes PON
de forma mais simples e com menor esfor¸co. Ademais, as aplica¸c˜oes PON desenvolvidas
apresentaram maior facilidade de manuten¸c˜ao quando comparadas a aplica¸c˜ao PI. Esses
resultados obtidos, com o desenvolvimento de uma aplica¸c˜ao conhecidamente complexa
utilizando a nova vers˜ao da LingPON, vˆem ao encontro de colaborar na demonstra¸c˜ao de
propriedades previstas na pr´opria teoria do PON.
Palavras-chave: Paradigma Orientado a Notiﬁca¸c˜oes, LingPON, Futebol de Robˆos


ABSTRACT
Araujo Santos, Leonardo. LANGUAGE AND COMPILER FOR THE NOTIFICATION-
ORIENTED PARADIGM: ADVANCES TO FACILITATE CODING AND ITS VALI-
DATION IN A ROBOT CONTROL SOCCER APPLICATION. 293 f. Disserta¸c˜ao –
Programa de P´os-gradua¸c˜ao em Engenharia El´etrica e Inform´atica Industrial, Universidade
Tecnol´ogica Federal do Paran´a. Curitiba, 2017.
Programming techniques based on the Imperative Paradigm (PI) and Declarative Pa-
radigm (PD) have limitations such as redundancies and couplings, which may hamper
the development and execution of software. In order to solve some of the deﬁciencies of
these programming paradigms, the Notiﬁcation Oriented Paradigm (NOP) has emerged,
which presents a new way of performing logical/cause revisions. This is accomplished
through small, reactive and decoupled computational entities that collaborate through
timely notiﬁcations. The NOP was originally materialized in the form of a Framework,
implemented in the C++ programming language. It is designed to provide high-level
interfaces that facilitate the development of NOP applications. However, internally the
Framework has data structures that induce an overhead of computational processing
and consequent damage to the performance of the applications. In order to address this
problem, a speciﬁc programming language for the NOP, named LingPON, and its compiler
have been created recently. However, only a few, simple, NOP applications were created
using LingPON, which does not allow its more eﬀective consolidation. This is essentially
for some limitations that exist in the current language version, as well as diﬃculties in
developing complex applications that solve real problems. In this sense, this work proposes
a new version of LingPON (version 1.2), with new features such as aggregations of entities,
allowing an easier and more direct development of complex applications. The advances
are validated by developing a more complex software using LingPON (version 1.0 and
1.2). The software in question deals with the autonomous control for soccer playing robots
(Robocup). In the end, software developed using LingPON is compared quantitatively
and qualitatively with equivalent software developed using the NOP 2.0 Framework and
other equivalent software developed with the Object Oriented Paradigm using a C++
programming language (this one programmed by others). The results show that the use
of the new version of LingPON, presented here, allows an easier development of NOP
applications. Also, that the developed application was easier to maintain when compared
to the PI application. These results, with the development of a known complex application
using a new version of LingPON, allows the demonstration of the properties expected in
the NOP theory itself.
Keywords: Notiﬁcation Oriented Paradigm, LingPON, Robots Soccer, RoboCup


LISTA DE FIGURAS
Figura 1:
Exemplo de uma Rule. . . . . . . . . . . . . . . . . . . . . . . . . .
19
Figura 2:
Atividades do m´etodo de pesquisa. . . . . . . . . . . . . . . . . . .
29
Figura 3:
Taxonomia de paradigmas de programa¸c˜ao com o Paradigma Ori-
entado a Notiﬁca¸c˜oes em destaque. Extra´ıdo de [Xavier 2014]. . . .
32
Figura 4:
Evento, condi¸c˜ao detectada e notiﬁca¸c˜ao [Faison 2006]. . . . . . . .
36
Figura 5:
Paradigma Orientado a Eventos adaptado de [Hansen e Fossum
2010]. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
36
Figura 6:
Arquitetura de um Sistema Baseado em Regras (SBR).
. . . . . .
37
Figura 7:
Inferˆencia por notiﬁca¸c˜oes [Sim˜ao et al. 2014].
. . . . . . . . . . .
41
Figura 8:
Modelo Centralizado de Resolu¸c˜ao de Conﬂitos [Banaszewski 2009]. 43
Figura 9:
C´alculo assint´otico do mecanismo de notiﬁca¸c˜oes [Banaszewski 2009] 46
Figura 10:
Impacto nas altera¸c˜oes de estado de Attributes ativos (adaptado
de [Ronszcka 2012]). . . . . . . . . . . . . . . . . . . . . . . . . . .
47
Figura 11:
Impacto nas altera¸c˜oes es estado de Attributes impertinentes (ada-
patado de [Ronszcka 2012]) . . . . . . . . . . . . . . . . . . . . . .
48
Figura 12:
Exemplo de reativa¸c˜ao de uma entidade desativada (adapatado
de [Ronszcka 2012]) . . . . . . . . . . . . . . . . . . . . . . . . . .
48
Figura 13:
Estrutura do Framework PON [Linhares et al. 2011] . . . . . . . .
51
Figura 14:
Diagrama de Classes do pacote Core [Linhares et al. 2011] . . . . .
52
Figura 15:
Diagrama de Classes dos subpacotes Attributes e Conditions [Li-
nhares et al. 2011] . . . . . . . . . . . . . . . . . . . . . . . . . . .
53
Figura 16:
Diagrama de classes do procedimento inicial de uma aplica¸c˜ao
PON [Ronszcka 2012] . . . . . . . . . . . . . . . . . . . . . . . . .
54
Figura 17:
Diagrama de atividades UML do compilador PON. . . . . . . . . .
63
Figura 18:
Exemplo de an´alise semˆantica [Ferreira 2016] . . . . . . . . . . . .
64
Figura 19:
Diagrama de classes utilizada pelo compilador PON para representar
entidades PON [Ferreira 2016].
. . . . . . . . . . . . . . . . . . .
65
Figura 20:
Dimens˜oes do campo oﬁcial da categoria SSL, em mil´ımetros. . . .
68
Figura 21:
Sistema RoboCup SSL [Yoon 2015] . . . . . . . . . . . . . . . . . .
69
Figura 22:
Interface gr´aﬁca da aplica¸c˜ao grSim Simulator. . . . . . . . . . . .
70
Figura 23:
Interface gr´aﬁca da aplica¸c˜ao Referee Box. . . . . . . . . . . . . . .
71


Figura 24:
Diagrama representativo das aplica¸c˜oes que comp˜oem o ambiente
simulado Robocup SSL. . . . . . . . . . . . . . . . . . . . . . . . .
72
Figura 25:
Fluxo de compila¸c˜ao de c´odigo utilizando o pr´e-compilador PON. .
82
Figura 26:
Diagrama de atividades simpliﬁcado de uma partida de futebol de
robˆos. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
92
Figura 27:
Diagrama de atividades para escolha do batedor de penalidade
m´axima.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
94
Figura 28:
Diagrama de classes simpliﬁcado da solu¸c˜ao desenvolvida em PI.
.
95
Figura 29:
Diagrama de classes do software de controle para partida de futebol
de robˆos em PON. . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
Figura 30:
Gr´aﬁco linhas de c´odigo-fonte para cada uma das solu¸c˜oes apresen-
tadas. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
Figura 31:
Gr´aﬁco quantidade de tokens presentes no c´odigo-fonte de cada
uma das solu¸c˜oes apresentadas. . . . . . . . . . . . . . . . . . . . . 110
Figura 32:
Campo de jogo (dimens˜oes em mil´ımetros). . . . . . . . . . . . . . 146
Figura 33:
Dimens˜oes m´axima do robˆo (em mil´ımetros). . . . . . . . . . . . . 147
Figura 34:
Posi¸c˜ao do marcador central (azul ou amarelo), e dos 4 marcadores
laterais coloridos (magenta ou verde claro). . . . . . . . . . . . . . 147
Figura 35:
Marcadores coloridos utilizados para a identiﬁca¸c˜ao. . . . . . . . . 148
Figura 36:
Esquema geral de funcionamento do Futebol de Robˆos da categoria
SSL. Fonte: http://wiki.robcup.org/Small Size League . . . . . . . 148
Figura 37:
Interface do programa SSL Referee Box, para envio de comandos
do ´arbitro. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
Figura 38:
Elementos do diagrama de objetos PON [Kossoski et al. 2014]. . . 159
Figura 39:
Diagrama de objetos PON das Rules rlRobotMoveX, rlRobotMo-
veY, rlAngleMove e rlBallFar. . . . . . . . . . . . . . . . . . . . . . 161
Figura 40:
Diagrama de objetos PON da Rule rlStartTargetToBall. . . . . . . 161
Figura 41:
Diagrama de objetos PON das Rules rlStartFreePartner e rlStart-
FreePartnerPass. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
Figura 42:
Diagrama de objetos PON das Rules rlStartNoFreePartner e rlS-
tartNoFreePartnerKick. . . . . . . . . . . . . . . . . . . . . . . . . 162
Figura 43:
Diagrama de objetos PON das Rules rlStartEnemyPositionKick e
rlStartEnemyFieldKick
. . . . . . . . . . . . . . . . . . . . . . . . 163
Figura 44:
Diagrama de objetos PON das Rules rlGoalkeeperStopCloseGoal e
rlGoalKeeperStopFarGoal.
. . . . . . . . . . . . . . . . . . . . . . 163
Figura 45:
Diagrama de objetos PON das Rules rlGoalkeeperStartInsideArea-
ClosestBall e rlGoalkeeperStartInsideAreaClosestBallKick. . . . . . 164


Figura 46:
Diagrama de objetos PON das Rules rlGoalkeeperStartInsideArea
e rlGoalkeeperStartOutsideArea. . . . . . . . . . . . . . . . . . . . 164
Figura 47:
Diagrama de objetos PON das Rules rlGoalkeeperBluePenaltyYel-
low e rlGoalkeeperYellowPenaltyBlue. . . . . . . . . . . . . . . . . 165
Figura 48:
Diagrama de objetos PON das Rules rlDefenderLeftStopBallFar e
rlDefenderLeftStopBallClose. . . . . . . . . . . . . . . . . . . . . . 165
Figura 49:
Diagrama de objetos PON das Rules rlDefenderLeftBlueDirectKick-
Blue e rlDefenderLeftYellowDirectKickYellow. . . . . . . . . . . . . 166
Figura 50:
Diagrama de objetos PON das Rules rlDefenderLeftBlueIndirect-
KickBlue e rlDefenderLeftYellowIndirectKickYellow. . . . . . . . . 166
Figura 51:
Diagrama de objetos PON das Rules rlDefenderLeftBluePenaltyYel-
low e rlDefenderLeftYellowPenaltyBlue. . . . . . . . . . . . . . . . 166
Figura 52:
Diagrama de objetos PON da Rule rlDefenderLefStartBallNotClose.167
Figura 53:
Diagrama de objetos PON das Rules rlDefenderRightStopBallFar
e rlDefenderRightStopBallClose. . . . . . . . . . . . . . . . . . . . 167
Figura 54:
Diagrama de objetos PON das Rules rlDefenderRightBlueDirect-
KickBlue e rlDefenderRightYellowDirectKickYellow. . . . . . . . . 167
Figura 55:
Diagrama de objetos PON das Rules rlDefenderRightBlueIndirect-
KickBlue e rlDefenderRightYellowIndirectKickYellow.
. . . . . . . 168
Figura 56:
Diagrama de objetos PON das Rules rlDefenderRightBluePenaltyYel-
low e rlDefenderRightYellowPenaltyBlue.
. . . . . . . . . . . . . . 168
Figura 57:
Diagrama de objetos PON da Rule rlDefenderRightStartBallNotClose.168
Figura 58:
Diagrama de objetos PON da Rule rlMidﬁeldOnlyStop. . . . . . . 169
Figura 59:
Diagrama de objetos PON das Rules rlMidﬁeldOnlyBlueKickoﬀe
rlMidﬁeldOnlyYellowKickoﬀ. . . . . . . . . . . . . . . . . . . . . . 169
Figura 60:
Diagrama de objetos PON das Rules rlMidﬁeldOnlyBlueReadyKic-
koﬀBlue e rlMidﬁeldOnlyYellowReadyKickoﬀYellow. . . . . . . . . 169
Figura 61:
Diagrama de objetos PON das Rules rlMidﬁeldOnlyBlueDirectKick
e rlMidﬁeldOnlyYellowDirectKick. . . . . . . . . . . . . . . . . . . 170
Figura 62:
Diagrama de objetos PON das Rules rlMidﬁeldOnlyBlueIndirect-
Kick e rlMidﬁeldOnlyYellowIndirectKick.
. . . . . . . . . . . . . . 170
Figura 63:
Diagrama de objetos PON das Rules rlMidﬁeldOnlyBluePenalty-
Blue e rlMidﬁeldOnlyYellowPenaltyYellow.
. . . . . . . . . . . . . 170
Figura 64:
Diagrama de objetos PON das Rules rlMidﬁeldOnlyBluePenaltyYel-
low e rlMidﬁeldOnlyYellowPenaltyBlue. . . . . . . . . . . . . . . . 171
Figura 65:
Diagrama de objetos PON das Rules rlMidﬁeldOnlyBlueReadyPe-
naltyBlue e rlMidﬁeldOnlyYellowReadyPenaltyYellow. . . . . . . . 171


Figura 66:
Diagrama de objetos PON das Rules rlStrikerLeftStopTeamLeft e
rlStrikerLeftStopTeamRight.
. . . . . . . . . . . . . . . . . . . . . 172
Figura 67:
Diagrama de objetos PON das Rules rlStrikerLeftBlueDirectKick e
rlStrikerLeftYellowDirectKick.
. . . . . . . . . . . . . . . . . . . . 172
Figura 68:
Diagrama de objetos PON das Rules rlStrikerLeftBlueIndirectKick
e rlStrikerLeftYellowIndirectKick.
. . . . . . . . . . . . . . . . . . 173
Figura 69:
Diagrama de objetos PON das Rules rlStrikerLeftBluePenaltyBlue
e rlStrikerLeftYellowPenaltyYellow.
. . . . . . . . . . . . . . . . . 173
Figura 70:
Diagrama de objetos PON das Rules rlStrikerLeftBluePenaltyYellow
e rlStrikerLeftYellowPenaltyBlue. . . . . . . . . . . . . . . . . . . . 173
Figura 71:
Diagrama de objetos PON da Rule rlStrikerLeftStartBallNotClose. 174
Figura 72:
Diagrama de objetos PON das Rules rlStrikerRightStopTeamLeft
e rlStrikerRightStopTeamRight.
. . . . . . . . . . . . . . . . . . . 174
Figura 73:
Diagrama de objetos PON das Rules rlStrikerRightBlueDirectKick
e rlStrikerRightYellowDirectKick. . . . . . . . . . . . . . . . . . . . 174
Figura 74:
Diagrama de objetos PON das Rules rlStrikerRightBlueIndirectKick
e rlStrikerRightYellowIndirectKick. . . . . . . . . . . . . . . . . . . 175
Figura 75:
Diagrama de objetos PON das Rules rlStrikerRightBluePenaltyBlue
e rlStrikerRightYellowPenaltyYellow. . . . . . . . . . . . . . . . . . 175
Figura 76:
Diagrama de objetos PON das Rules rlStrikerRightBluePenaltyYel-
low e rlStrikerRightYellowPenaltyBlue.
. . . . . . . . . . . . . . . 175
Figura 77:
Diagrama de objetos PON das Rules rlStrikerRightStartBallNotClose.176
Figura 78:
Representa¸c˜ao da aplica¸c˜ao Mira ao Alvo [Banaszewski 2009] . . . 217
Figura 79:
Exemplo de uma Rule presente na aplica¸c˜ao Mira ao Alvo . . . . . 218
Figura 80:
Representa¸c˜ao do Sistema de Condicionamento de Ar [Banaszewski
2009]. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219
Figura 81:
Ambiente gerado pelo simulador [Ronszcka et al. 2011].
. . . . . . 221
Figura 82:
Figura conceitual de um exoesqueleto do projeto Hardiman I da
General Electric. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223
Figura 83:
Casos de uso do Sistema de Vendas. . . . . . . . . . . . . . . . . . 224
Figura 84:
Rule respons´avel por ﬁnalizar a venda [Ferreira et al. 2013]. . . . . 225
Figura 85:
Conﬁgura¸c˜ao Inicial da Torre de Han´oi [Krug 2016]. . . . . . . . . 229


LISTA DE TABELAS
Tabela 1:
Rules, Conditions e suas Premises e Actions instigadas do software
de controle PON para futebol de robˆos. . . . . . . . . . . . . . . . . 103
Tabela 2:
Resultados obtidos a partir dos experimentos de contabilidade de
linhas de c´odigo e quantidade de tokens presentes no c´odigo fonte e
n´ıvel de manutenibilidade. . . . . . . . . . . . . . . . . . . . . . . . 120
Tabela 3:
Deﬁni¸c˜ao das Premises utilizadas pelas Rules na aplica¸c˜ao de con-
trole de futebol de robˆos. . . . . . . . . . . . . . . . . . . . . . . . . 160


SUM´ARIO
1
INTRODUC¸ ˜AO
17
1.1
PARADIGMA ORIENTADO A NOTIFICAC¸ ˜OES (PON)
. . . . . . . . .
18
1.2
MOTIVAC¸ ˜AO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
1.3
JUSTIFICATIVA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
1.3.1
Quest˜ao da agrega¸c˜ao de Rules
. . . . . . . . . . . . . . . . . . . .
23
1.3.2
Quest˜ao de agrega¸c˜ao entre FBEs . . . . . . . . . . . . . . . . . . .
24
1.3.3
Reﬂex˜ao . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
1.4
OBJETIVOS
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
1.5
ATIVIDADES DO M´ETODO DE PESQUISA . . . . . . . . . . . . . . . .
27
1.5.1
Revis˜ao do Estado da Arte . . . . . . . . . . . . . . . . . . . . . . .
28
1.5.2
Reﬂex˜ao e Proposta . . . . . . . . . . . . . . . . . . . . . . . . . . .
28
1.5.3
Deﬁni¸c˜ao dos Objetivos
. . . . . . . . . . . . . . . . . . . . . . . .
28
1.5.4
Desenvolvimento Investigativo . . . . . . . . . . . . . . . . . . . . .
28
1.5.5
Compara¸c˜oes e Valida¸c˜oes . . . . . . . . . . . . . . . . . . . . . . .
30
1.5.6
Conclus˜ao . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
2
REVIS˜AO DO ESTADO DA ARTE
31
2.1
PARADIGMAS DE PROGRAMAC¸ ˜AO . . . . . . . . . . . . . . . . . . . .
31
2.1.1
Paradigma Imperativo . . . . . . . . . . . . . . . . . . . . . . . . .
33
2.1.2
Paradigma Orientado a Eventos . . . . . . . . . . . . . . . . . . . .
36
2.1.3
Paradigma Declarativo . . . . . . . . . . . . . . . . . . . . . . . . .
37
2.2
PARADIGMA ORIENTADO A NOTIFICAC¸ ˜OES
. . . . . . . . . . . . .
38
2.2.1
Rela¸c˜ao entre o PON e os Paradigmas Imperativo e Declarativo . .
39


2.2.2
Mecanismo de Notiﬁca¸c˜ao do PON . . . . . . . . . . . . . . . . . .
41
2.2.3
Resolu¸c˜ao de Conﬂitos no PON . . . . . . . . . . . . . . . . . . . .
42
2.2.4
Propriedades Inerentes ao PON . . . . . . . . . . . . . . . . . . . .
44
2.2.5
PON – Utiliza¸c˜ao x Compreens˜ao . . . . . . . . . . . . . . . . . . .
44
2.2.6
C´alculo Assint´otico da Inferˆencia do PON
. . . . . . . . . . . . . .
45
2.2.7
Attributes Impertinentes . . . . . . . . . . . . . . . . . . . . . . . .
46
2.2.8
Regras de Forma¸c˜ao
. . . . . . . . . . . . . . . . . . . . . . . . . .
48
2.3
MATERIALIZAC¸ ˜OES DO PON . . . . . . . . . . . . . . . . . . . . . . . .
49
2.3.1
Framework PON . . . . . . . . . . . . . . . . . . . . . . . . . . . .
50
2.3.2
Linguagem e Compilador para o PON - LingPON 1.0 . . . . . . . .
56
2.3.2.1
Linguagem de programa¸c˜ao PON . . . . . . . . . . . . . .
56
2.3.2.2
Compilador para o PON . . . . . . . . . . . . . . . . . . .
62
2.3.3
Outras Materializa¸c˜oes em Software do PON . . . . . . . . . . . . .
66
2.4
FUTEBOL DE ROBˆOS - ROBOCUP . . . . . . . . . . . . . . . . . . . . .
67
2.4.1
Ambiente Simulado RoboCup SSL . . . . . . . . . . . . . . . . . . .
69
2.5
REFLEX˜AO SOBRE A REVIS˜AO DO ESTADO DA ARTE . . . . . . . .
73
3
DESENVOLVIMENTO
75
3.1
CONTRIBUIC¸ ˜OES PARA A LINGPON . . . . . . . . . . . . . . . . . . .
75
3.1.1
Agrega¸c˜ao entre FBEs . . . . . . . . . . . . . . . . . . . . . . . . .
76
3.1.2
Agrega¸c˜ao de Rules em FBEs . . . . . . . . . . . . . . . . . . . . .
79
3.1.3
Corre¸c˜ao de erro: Gera¸c˜ao de c´odigo-alvo C++ com m´ultiplas
instˆancias de FBE
. . . . . . . . . . . . . . . . . . . . . . . . . . .
86
3.2
ESTUDO DE CASO - SOFTWARE DE CONTROLE PARA O FUTEBOL
DE ROBˆOS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
91
3.2.1
Especiﬁca¸c˜ao do Software de controle para uma partida de futebol
de robˆos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
91


3.2.2
Solu¸c˜ao desenvolvida sob o vi´es do Paradigma Imperativo - Pro-
grama¸c˜ao Orientada a Objetos . . . . . . . . . . . . . . . . . . . . .
94
3.2.3
Solu¸c˜oes desenvolvidas sob o vi´es do Paradigma Orientado a Noti-
ﬁca¸c˜oes
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
3.2.3.1
Solu¸c˜ao desenvolvida sob o vi´es do Framework PON 2.0
. 104
3.2.3.2
Solu¸c˜ao desenvolvida sob o vi´es do Paradigma Orientado a
Notiﬁca¸c˜oes - LingPON 1.0
. . . . . . . . . . . . . . . . . 105
3.2.3.3
Solu¸c˜ao desenvolvida sob o vi´es do Paradigma Orientado a
Notiﬁca¸c˜oes - LingPON 1.2
. . . . . . . . . . . . . . . . . 106
3.2.4
Compara¸c˜oes entre a aplica¸c˜ao de controle de futebol de robˆos
desenvolvida nos Paradigma Orientado a Objetos e no Paradigma
Orientado a Notiﬁca¸c˜oes . . . . . . . . . . . . . . . . . . . . . . . . 108
3.2.4.1
Compara¸c˜oes de complexidade de c´odigo-fonte entre a
aplica¸c˜ao de controle de futebol de robˆos desenvolvida em
PI/POO e PON
. . . . . . . . . . . . . . . . . . . . . . . 108
3.2.4.2
Compara¸c˜oes de manutenibilidade entre a aplica¸c˜ao de
controle de futebol de robˆos desenvolvida em PI/POO e
PON . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
3.2.5
Reﬂex˜ao sobre as compara¸c˜oes . . . . . . . . . . . . . . . . . . . . . 118
4
CONCLUS˜AO E TRABALHOS FUTUROS
121
4.1
CONCLUS˜AO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
4.2
TRABALHOS FUTUROS . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
4.2.1
Suporte a m´ultiplos arquivos de c´odigo-fonte . . . . . . . . . . . . . 124
4.2.2
Utiliza¸c˜ao de bibliotecas externas . . . . . . . . . . . . . . . . . . . 124
4.2.3
Simpliﬁca¸c˜ao da sintaxe da LingPON . . . . . . . . . . . . . . . . . 125
4.2.4
Teste de unidade para o compilador . . . . . . . . . . . . . . . . . . 125
4.2.5
Melhorar experimento de n´ıvel de manutenibilidade . . . . . . . . . 126
4.2.6
Estudo de Agentes aplicados ao PON . . . . . . . . . . . . . . . . . 126


REFERˆENCIAS
128
Apˆendice A -- DESCRIC¸ ˜AO DAS ALTERAC¸ ˜OES REALIZADAS NA
LINGPON
136
A.1 AGREGAC¸ ˜AO DE FBES . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
A.2 FBE RULES
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
A.3 CORREC¸ ˜AO DE ERRO: GERAC¸ ˜AO DE C´ODIGO-ALVO C++ COM
M´ULTIPLAS INSTˆANCIAS DE FBE
. . . . . . . . . . . . . . . . . . . . 142
Apˆendice B -- ESPECIFICAC¸ ˜AO T´ECNICA - ROBOCUP SMALL SIZE
LEAGUE
145
B.1 DESCRIC¸ ˜AO DO AMBIENTE DE JOGO . . . . . . . . . . . . . . . . . . 145
B.2 DESCRIC¸ ˜AO DOS ROBˆOS . . . . . . . . . . . . . . . . . . . . . . . . . . 146
B.2.1
Uniformes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
B.3 REQUISITOS FUNCIONAIS DA APLICAC¸ ˜AO DE CONTROLE . . . . . 151
Apˆendice C -- CONJUNTO DE RULES APLICADAS `A SOLUC¸ ˜AO
DESENVOLVIDA SOB O VI´ES DO PON
159
C.1 DIAGRAMA DE OBJETOS PON
. . . . . . . . . . . . . . . . . . . . . . 159
C.2 C´ODIGO-FONTE DAS RULES DESENVOLVIDAS PARA O SOFTWARE
PON . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177
Apˆendice D -- ANALISADOR L´EXICO DESENVOLVIDO PARA A CON-
TAGEM DO N ´UMERO DE TOKENS
210
Apˆendice E -- CENSO DAS APLICAC¸ ˜OES PON
212
E.1
MIRA AO ALVO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217
E.2
SISTEMA DE CONDICIONAMENTO DE AR
. . . . . . . . . . . . . . . 219
E.3
SIMULADOR DE JOGO (PACMAN )
. . . . . . . . . . . . . . . . . . . . 220
E.4
SIMULADOR DE TRANSPORTE INDIVIDUAL . . . . . . . . . . . . . . 222
E.5
SISTEMA DE VENDAS . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224


E.6
PORT˜AO ELETRˆONICO . . . . . . . . . . . . . . . . . . . . . . . . . . . 226
E.7
CONTROLE DA ILUMINAC¸ ˜AO EM UMA CIDADE VIRTUAL 3D
. . . 226
E.8
WARSHIPATTACK GAME . . . . . . . . . . . . . . . . . . . . . . . . . . 227
E.9
CTA SIMULATOR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228
E.10 TORRE DE HAN´OI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228
E.11 ALGORITMO TRIANGULAR MESH SLICING
. . . . . . . . . . . . . . 229
E.12 REFLEX˜AO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 230
Apˆendice F -- PROGRAMAC¸ ˜AO ORIENTADA A AGENTES
232
Anexo A -- BNF DA LINGPON 1.0
234
Anexo B -- BNF DA LINGPON 1.2
237
Anexo C -- RELAT´ORIOS AINDA N˜AO PUBLICADOS SOBRE APLICAC¸ ˜OES
PON
241
Anexo D -- RELAT´ORIO DA DISCIPLINA LINGUAGENS/COMPILA-
DORES - 2015
254
Anexo E -- RELAT´ORIO DA DISCIPLINA LINGUAGENS/COMPILA-
DORES - 2016
271


17
1
INTRODUC¸ ˜AO
Os principais paradigmas de programa¸c˜ao vigentes na ind´ustria de desenvolvi-
mento de software s˜ao o Paradigma Imperativo (PI) e o Paradigma Declarativo (PD).
Aplica¸c˜oes desenvolvidas sob esses paradigmas de programa¸c˜ao apresentam, em sua maioria,
processamento desnecess´ario. Isto ocorre, principalmente, por motivos como redundˆancias
em avalia¸c˜oes causais e/ou utiliza¸c˜ao de estruturas de dados computacionalmente custosas.
Visando solucionar algumas das deﬁciˆencias dos paradigmas usuais de programa¸c˜ao
em rela¸c˜ao a avalia¸c˜oes causais desnecess´arias e acopladas, o Paradigma Orientado a
Notiﬁca¸c˜oes (PON) foi inicialmente proposto por J. M. Sim˜ao na forma de uma solu¸c˜ao
de controle discreto e de inferˆencia para sistemas de manufatura inteligentes [Sim˜ao 2001],
evoluindo posteriormente para a forma de um paradigma de programa¸c˜ao [Sim˜ao e Stadzisz
2008,Ronszcka 2012,Banaszewski 2009].
O PON apresenta uma nova forma de realizar avalia¸c˜oes de express˜oes l´ogico-
causais. No PON, tais express˜oes s˜ao expressas na forma de regras (Rules) e o ﬂuxo de
execu¸c˜ao da aplica¸c˜ao ´e determinado por notiﬁca¸c˜oes pontuais e precisas entre entidades
computacionais de pequeno porte. Dessa forma, ´e poss´ıvel eliminar, ou ao menos amenizar,
as limita¸c˜oes presentes no PI e PD.
Os conceitos do PON foram inicialmente implementados ou materializados com-
putacionalmente na forma de um Framework. Este Framework foi constru´ıdo utilizando a
linguagem de programa¸c˜ao C++. Tal Framework encontra-se em sua terceira vers˜ao [Va-
len¸ca 2013,Ronszcka et al. 2011]. Tais materializa¸c˜oes possibilitaram a cria¸c˜ao de aplica¸c˜oes
PON e consequente demonstra¸c˜ao de seus principais conceitos. Entretanto, o desempenho
das aplica¸c˜oes desenvolvidas utilizando o Framework ﬁcaram aqu´em do que era esperado
pela teoria do PON [Ferreira et al. 2013,Sim˜ao et al. 2012].
Posteriormente, uma linguagem de programa¸c˜ao, nomeada LingPON, e respectivo
compilador, espec´ıﬁcos para o PON, foram desenvolvidos [Ferreira 2016]. Por utilizar
estruturas de dados mais enxutas quando comparada com o Framework, a linguagem de


18
programa¸c˜ao PON apresentou resultados, em termos de desempenho, mais pr´oximos ao
esperado pela teoria do PON [Ferreira 2016].
Apesar de trazer avan¸cos em quest˜ao de desempenho, a LingPON n˜ao representou
um grande avan¸co no tocante `a facilidade de programa¸c˜ao. Conforme apresentado nas
se¸c˜oes subsequentes, o desenvolvedor que deseja criar um software sob o vi´es do PON
utilizando a atual vers˜ao da LingPON necessita escrever muitas linhas de c´odigo, fato este
que n˜ao contribui para a consolida¸c˜ao do paradigma em quest˜ao.
Al´em disso, um n´umero n˜ao muito expressivo de aplica¸c˜oes foram desenvolvidas
utilizando a LingPON at´e o presente momento, fato este que n˜ao permite uma real
compreens˜ao das limita¸c˜oes da linguagem de programa¸c˜ao. Dessa forma, vislumbra-se
a possibilidade de desenvolver uma aplica¸c˜ao conhecidamente complexa, nomeadamente
uma aplica¸c˜ao de controle de futebol de robˆos, utilizando a LingPON para que a mesma
possa ser avaliada de forma mais efetiva. Ademais, essa aplica¸c˜ao enriquecer´a o rol de
aplica¸c˜oes PON e poder´a, at´e mesmo, ser de valor consider´avel para a consolida¸c˜ao do
PON entre os paradigmas de programa¸c˜ao vigentes.
Dessa forma, este trabalho pretende evoluir a especiﬁca¸c˜ao da LingPON e seu
respectivo compilador de forma a facilitar e agilizar o desenvolvimento de aplica¸c˜oes PON,
al´em de usar o PON em uma aplica¸c˜ao de complexidade reconhecida.
Neste cap´ıtulo introdut´orio, a Se¸c˜ao 1.1 apresenta uma contextualiza¸c˜ao sobre o
Paradigma Orientado a Notiﬁca¸c˜oes. A Se¸c˜ao 1.2 detalha a motiva¸c˜ao para este estudo.
A Se¸c˜ao 1.3, por sua vez, apresenta a justiﬁcativa para este estudo. Por ﬁm, a Se¸c˜ao 1.4
elenca os objetivos pretendidos com este trabalho 1.
1.1
PARADIGMA ORIENTADO A NOTIFICAC¸ ˜OES (PON)
O PON encontra alguma inspira¸c˜ao nos paradigmas usuais de programa¸c˜ao,
nomeadamente o Paradigma Declarativo (PD) e o Paradigma Imperativo (PI), aproveitando
a ﬂexibilidade algor´ıtmica e abstra¸c˜ao em forma de classes/objetos da Programa¸c˜ao-
Paradigma Orientado a Objetos (POO) do PI e a representa¸c˜ao do conhecimento em regras
dos Sistemas Baseados em Regras (SBR) do Paradigma L´ogico (PL) do PD. Sendo assim, o
PON usa inclusive parte de ambos os estilos de programa¸c˜ao em seu modelo, evoluindo-os
no que se refere ao processo de inferˆencia ou c´alculo l´ogico-causal [Xavier 2014,Sim˜ao e
1Pertinente registrar que parte destes esfor¸cos de pesquisa, aqui considerados, foram apresentados na
forma de Trabalho Individual (“Qualiﬁca¸c˜ao de Mestrado”) junto ao CPGEI/UTFPR em 03 de Junho de
2016


19
Stadzisz 2008,Sim˜ao et al. 2009,Banaszewski 2009,Linhares et al. 2011,Sim˜ao et al. 2012]
Visando solucionar, ou ao menos amenizar, algumas das deﬁciˆencias encontra-
das naqueles paradigmas, tais como a repeti¸c˜ao de express˜oes l´ogicas e reavalia¸c˜oes
desnecess´arias delas (i.e. redundˆancias estruturais e temporais) e, particularmente, o
acoplamento forte de entidades quanto `as avalia¸c˜oes ou c´alculo l´ogico-causal, o PON
apresenta outra forma de realizar tais avalia¸c˜oes ou inferˆencias. Isto ´e realizado via
entidades computacionais de pequeno porte, reativas e desacopladas que colaboram por
meio de notiﬁca¸c˜oes pontuais, sendo tais entidades criadas a partir do ‘conhecimento’ de
regras [Linhares et al. 2011,Sim˜ao et al. 2012,Sim˜ao et al. 2012,Sim˜ao et al. 2012].
No PON, as entidades computacionais que possuem atributos (Attribute) e m´etodos
(Methods) s˜ao genericamente chamadas de FBEs (Fact Base Elements). Por meio de seus
Attributes e Methods, as entidades de FBE s˜ao pass´ıveis de correla¸c˜ao l´ogico-causal por
meio de Rules, as quais constituem elementos fundamentais do PON [Xavier 2014,Sim˜ao e
Stadzisz 2008,Linhares et al. 2011,Sim˜ao et al. 2012,Sim˜ao et al. 2012,Sim˜ao et al. 2012].
A Figura 1 apresenta um exemplo de Rule, justamente na forma de uma regra
l´ogico-causal. A Rule ´e uma entidade computacional composta por outras duas entidades,
Condition e Action. A Condition trata da decis˜ao da Rule, enquanto a Action trata da
execu¸c˜ao das a¸c˜oes associadas `a Rule. Assim sendo, a Condition e a Action tratam o
conhecimento l´ogico e causal associado a Rule [Sim˜ao e Stadzisz 2008, Linhares et al.
2011,Sim˜ao et al. 2012,Sim˜ao et al. 2012,Sim˜ao et al. 2012].
Figura 1: Exemplo de uma Rule.
A Rule apresentada na Figura 1 faz parte de um sistema de controle de robˆos
em uma partida de futebol de robˆos. Essa Rule refere-se `a decis˜ao de movimento de
um determinado Robˆo (Robot) em uma partida de futebol, em fun¸c˜ao do estado de seus
Attributes.
Neste contexto, a Condition da Rule apresentada na Figura 1 ´e composta por trˆes


20
entidades Premises. Estas, realizam, respectivamente as seguinte veriﬁca¸c˜oes: a) o comando
recebido pelo Robˆo (Robot1.atRefereeCmd) representa a interrup¸c˜ao da partida (Stop)?
b) a distˆancia entre a o Robˆo e o gol que ele est´a defendendo (Robot1.atDistTeamGoal) ´e
menor que 1800 cm.? c) a fun¸c˜ao que o Robˆo est´a exercendo no time (Robot1.atRole) ´e a
de lateral-esquerdo (“DEFENDER LEFT”)?. Portanto, ´e poss´ıvel concluir que os estados
dos atributos dos FBEs comp˜oem os fatos a serem avaliados pelas Premises [Sim˜ao e
Stadzisz 2008,Sim˜ao et al. 2009,Banaszewski 2009].
Cada Premise avalia o estado de um ou dois Attributes de FBE. Em tempo,
para cada mudan¸ca de estado de um Attribute de um FBE, ocorrem automaticamente,
via notiﬁca¸c˜oes, avalia¸c˜oes (l´ogicas) somente nas Premises relacionadas com eventuais
mudan¸cas nos seus estados.
Semelhantemente, a partir da mudan¸ca de estado das
Premises, ocorrem automaticamente avalia¸c˜oes somente nas Conditions relacionadas com
eventuais mudan¸cas em seus estados [Sim˜ao e Stadzisz 2008,Sim˜ao et al. 2009,Banaszewski
2009,Sim˜ao et al. 2012].
Sucintamente, a cada mudan¸ca no estado de um Attribute, ele pr´oprio notiﬁca
imediatamente uma ou um conjunto de entidades Premises relacionadas para que estas
reavaliem os seus estados l´ogicos. Isto se d´a em cada Premise pela compara¸c˜ao, usando
um operador l´ogico, do valor notiﬁcado com outro valor, este uma constante ou um valor
notiﬁcado por outro Attribute. Se o valor l´ogico da entidade Premise se alterar, essa
notiﬁca um conjunto de entidades Conditions conectadas para que seus estados l´ogicos
sejam reavaliados [Banaszewski 2009].
Desse modo, cada entidade Condition notiﬁcada reavalia o seu estado l´ogico de
acordo com o valor rec´em notiﬁcado pela Premise em quest˜ao e os valores notiﬁcados
previamente pelas demais Premises conectadas. Assim, a entidade Condition ´e satisfeita
quando todas as entidades Premises que a comp˜oem apresentam estado l´ogico verdadeiro,
decorrendo na aprova¸c˜ao da sua respectiva Rule. Com isto, a entidade Action conectada
a esta Rule ´e executada, podendo invocar Methods de FBEs atrav´es das entidades
Instigations [Banaszewski 2009]. Usualmente, os Methods alteram os estados dos Attributes
do FBE, fazendo assim com que um novo ciclo de notiﬁca¸c˜oes se inicie. No exemplo
apresentado, a Action cont´em apenas uma Instigation, a qual instiga um Method que faz
movimentar o Robˆo para uma posi¸c˜ao espec´ıﬁca (Stop Position).
Isto posto, nota-se que a essˆencia da computa¸c˜ao no PON est´a na forma como
as responsabilidades de um programa est˜ao distribu´ıdas entre entidades computacionais
autˆonomas e reativas que colaboram entre si atrav´es de notiﬁca¸c˜oes pontuais.
Este


21
arranjo forma o mecanismo de notiﬁca¸c˜oes, o qual determina o ﬂuxo de execu¸c˜ao das
aplica¸c˜oes, permitindo execu¸c˜ao otimizada e minimamente acoplada de processamento
l´ogico-causal, ´util para o aproveitamento correto de mono-processamento, bem como para
o processamento distribu´ıdo [Sim˜ao e Stadzisz 2008,Sim˜ao et al. 2010,Belmonte et al.
2012,Sim˜ao et al. 2012,Sim˜ao et al. 2012,Sim˜ao et al. 2012,Linhares et al. 2015,Linhares
2015,Ferreira 2016].
Os conceitos do PON foram primeiramente materializados sobre a programa¸c˜ao
orientada a objetos (POO), atrav´es de um Framework desenvolvido utilizando a linguagem
de programa¸c˜ao C++ em uma vers˜ao prototipal concebida por Sim˜ao em 2007. Subsequen-
temente, a chamada vers˜ao 1.0 foi desenvolvida em 2009 por Banaszewski [Banaszewski
2009]. Em 2012, uma nova vers˜ao (vers˜ao 2.0) otimizada para ambientes monoprocessados
foi desenvolvida por Valen¸ca [Valen¸ca 2013] e Ronszcka [Ronszcka 2012]. Posteriormente,
foi desenvolvida uma linguagem de programa¸c˜ao espec´ıﬁca para o PON (LingPON, vers˜ao
1.0), acompanhada do respectivo compilador [Ferreira 2016], a qual j´a apresenta uma nova
vers˜ao prototipal [Pordeus et al. 2015]. Atualmente, o Framework PON (particularmente
a vers˜ao 2.0) e a LingPON (particularmente a vers˜ao 1.0) representam as principais
materializa¸c˜oes em software do PON.
1.2
MOTIVAC¸ ˜AO
Muitos assuntos relacionados ao PON foram estudados nos ´ultimos anos, entre
eles pode-se destacar: Desenvolvimento Orientado a Notiﬁca¸c˜oes (DON) [Wiecheteck
et al. 2011, Wiecheteck 2012, Medon¸ca et al. 2015], padr˜oes de projetos aplicados a
softwares PON [Ronszcka 2012], linguagem nativa de programa¸c˜ao PON (LingPON) e
respectivo compilador [Ferreira 2016], teste funcional em software PON [Kossoski et al.
2014], coprocessadores para acelera¸c˜ao de aplica¸c˜oes desenvolvidas utilizando o PON
(CoPON) [Peters 2012], PON em hardware digital (PON HD) [Kerschbaumer et al.
2015, Sim˜ao et al. 2012], processador nativo em PON (ARQPON) [Linhares 2015] e
compara¸c˜oes entre abordagens orientada a eventos e orientada a notiﬁca¸c˜oes [Xavier 2014].
Apesar destes avan¸cos, como ´e ainda um tanto natural academicamente no tocante
`a prova de conceito, um n´umero n˜ao verdadeiramente signiﬁcativo de aplica¸c˜oes, que
sejam complexas2 e que tenham sido comparados a vers˜oes equivalente em paradigmas
2Segundo [Russell e Norvig 2009], a complexidade de um sistema est´a relacionado `a certas caracter´ısticas
de seu ambiente de execu¸c˜ao. As caracter´ısticas consideradas para determinar a complexidade de uma
tarefa consideram se o ambiente ´e parcialmente ou completamente observ´avel, determin´ıstico ou estoc´astico,
est´atico ou dinˆamico e discreto ou cont´ınuo e se envolve um ´unico agente ou multi-agentes.


22
vigentes, foram desenvolvidos em PON. Isso se agrava quando se observa a materializa¸c˜ao
de linguagem e compilador para o PON, aqui nomeada apenas como LingPON. Isto
se deve, inclusive, ao fato desta ser uma materializa¸c˜ao recente, a qual ainda est´a em
desenvolvimento para se tornar uma linguagem de programa¸c˜ao mais completa. Como
relatado em [Ferreira 2016], ainda faz-se necess´ario, dentre outros, evolui-la no tocante a
certas facilidades de programa¸c˜ao, visando proporcionar maior agilidade no desenvolvimento
de aplica¸c˜oes PON.
Dessa forma, este trabalho vislumbra a possibilidade de evoluir a LingPON, de
forma a facilitar o desenvolvimento de aplica¸c˜oes PON por meio do aprimoramento de
agrega¸c˜ao de entidades no LingPON, a luz do pr´oprio PON, o que leva a redu¸c˜ao de
redundˆancias de linhas de c´odigo fonte em aplica¸c˜oes feitas neste paradigma nessa sua
materializa¸c˜ao. Ademais, este trabalho tamb´em visa a demonstra¸c˜ao da utiliza¸c˜ao da
LingPON no desenvolvimento de uma aplica¸c˜ao pertinente e de maior complexidade,
quando comparada com as aplica¸c˜oes previamente desenvolvidas.
A aplica¸c˜ao visada neste presente trabalho est´a no ˆambito de controle de futebol
de robˆos, um dom´ınio reconhecidamente com consider´avel complexidade, uma vez que se
trata de um ambiente estoc´asticos, dinˆamico, n˜ao determin´ıstico, cont´ınuo e com m´ultiplos
agentes [Visser e Burkhard 2007,Russell e Norvig 2009]. Ainda, este dom´ınio de aplica¸c˜ao
permitir´a tecer compara¸c˜oes entre a vers˜ao evolu´ıda da LingPON aqui proposta, a vers˜ao
at´e ent˜ao vigente da LingPON (vers˜ao 1.0), o Framework PON na sua vers˜ao 2.0 (´ultima
vers˜ao em C++) e mesmo compara¸c˜oes para com a Programa¸c˜ao/Paradigma Orientado
a Objetos (POO) em C++. Isto se dar´a por meio de vers˜oes equivalentes da mesma
aplica¸c˜ao nestes diferentes meios, sublinhando que a vers˜ao POO foi elaborada por outrem,
o que permitiria compara¸c˜ao um tanto mais isenta.
1.3
JUSTIFICATIVA
A oferta de facilidades na programa¸c˜ao ´e uma caracter´ıstica inerente `a teoria
do PON, principalmente devido ao fato de ele, neste ˆambito, ter sido inspirado em
conceitos do PD. De fato, um conjunto de autores consideram a programa¸c˜ao em PD
menos dif´ıcil que em PI [Kaisler 2005,Gabbrielli e Martini 2010]. Assim, a programa¸c˜ao
em PON ´e tida como menos dif´ıcil que programa¸c˜ao em PI porque aquela ´e considerada
intuitiva `a forma cognitiva humana, caracter´ıstica esta herdada do PD [Panescu et al.
2015,Banaszewski 2009]. Neste sentido, um dos objetivos fundamentais do PON, atrav´es de
suas materializa¸c˜oes, ´e proporcionar o desenvolvimento de software com alguma facilidade


23
de programa¸c˜ao [Banaszewski 2009].
Entretanto, at´e o presente momento, um n´umero n˜ao grande de aplica¸c˜oes em
PON (aproximadamente 35) foram desenvolvidas utilizando a LingPON 3. Ainda, as
aplica¸c˜oes PON desenvolvidas apresentavam escopo reduzido, pois visavam o estudo do
desempenho do PON em cen´arios espec´ıﬁcos de compara¸c˜ao. O fato de apenas algumas
aplica¸c˜oes PON terem sido desenvolvidas utilizando a LingPON est´a relacionado inclusive
a algumas limita¸c˜oes da linguagem, relativas a restri¸c˜oes de agrega¸c˜ao de entidades PON
na gram´atica da LingPON. Tais restri¸c˜oes fazem com que o desenvolvedor tenha que
reescrever, por diversas vezes, linhas de c´odigo muito semelhantes. Estas limita¸c˜oes s˜ao
apresentadas e explicadas a seguir, atrav´es da apresenta¸c˜ao de exemplos.
1.3.1
QUEST˜AO DA AGREGAC¸ ˜AO DE RULES
De forma an´aloga ao que existe em aplica¸c˜oes desenvolvidas segundo a POO, nas
quais objetos s˜ao criados como sendo instˆancias de classes, em aplica¸c˜oes PON ´e poss´ıvel (e
necess´ario) criar instˆancias de FBEs. Em aplica¸c˜oes desenvolvidas utilizando a LingPON,
cada uma das Rules relaciona-se com instˆancias de FBEs. Neste sentido, para cada nova
instˆancia de FBE criada, novas Rules e, consequentemente, novas linhas de c´odigo devem
ser adicionadas ao sistema, resultando assim em aumento no c´odigo fonte a ser escrito.
Isto ´e assaz normal, mas h´a situa¸c˜oes nas quais ocorre um aumento desnecess´ario de
complexidade na atual vers˜ao da LingPON (vers˜ao 1.0).
De forma a exempliﬁcar o problema em quest˜ao, pode-se imaginar uma aplica¸c˜ao
PON que controle o funcionamento de robˆos em uma partida de futebol de robˆos. O
comportamento do robˆo depende da posi¸c˜ao (goleiro, zagueiro e etc.) designada ao mesmo
na partida. Caso o robˆo seja um zagueiro, seu comportamento esperado ´e o de defender.
Entretanto, caso seja um atacante, um comportamento mais ofensivo ´e esperado. Sendo
assim, um robˆo poderia ser modelado como sendo um FBE que apresenta apenas um
Attribute (posi¸c˜ao) e dois Methods (defender e atacar). Desse modo, havendo apenas um
robˆo (R1) presente na partida, o sistema de controle poderia ser criado com as Rules:
• Rule 1: Se posi¸c˜ao de R1 ´e ‘zagueiro’ ent˜ao defender.
• Rule 2: Se posi¸c˜ao de R1 ´e ‘atacante’ ent˜ao atacar.
Entretanto, caso seja necess´ario expandir tal aplica¸c˜ao de forma a controlar
3As aplica¸c˜oes PON desenvolvidas at´e o presente momento s˜ao listadas no Apˆendice E deste trabalho.


24
dois robˆos (R1 e R2), ser´a imprescind´ıvel duplicar o n´umero de Rules que regem o
comportamento do sistema aﬁm de que ambos apresentem um funcionamento correto.
Nesse caso, o sistema apresentaria as seguintes Rules:
• Rule 1: Se posi¸c˜ao de R1 ´e ‘zagueiro’ ent˜ao defender.
• Rule 2: Se posi¸c˜ao de R1 ´e ‘atacante’ ent˜ao atacar.
• Rule 3: Se posi¸c˜ao de R2 ´e ‘zagueiro’ ent˜ao defender.
• Rule 4: Se posi¸c˜ao de R2 ´e ‘atacante’ ent˜ao atacar.
Nesse pequeno exemplo ´e poss´ıvel evidenciar um cen´ario no qual haver´a re-
dundˆancia de Rules no c´odigo fonte da aplica¸c˜ao PON desenvolvida utilizando a LingPON.
Portanto, vislumbra-se a possibilidade de evoluir a LingPON de forma a evitar a re-
dundˆancia na declara¸c˜ao de Rules em cen´arios similares ao exempliﬁcado, atrav´es da
inclus˜ao do conceito de “agrega¸c˜ao”de Rules em FBEs.
1.3.2
QUEST˜AO DE AGREGAC¸ ˜AO ENTRE FBES
Na LingPON, deﬁne-se que os Attributes de um FBE devem ser de tipos primitivos,
isto ´e, boolean, integer, ﬂoat, char ou string [Ferreira 2016]. Entretanto, existem casos nos
quais h´a a necessidade de se criar Attributes que fa¸cam referˆencia a outro FBE de forma a
aumentar o encapsulamento de Attributes e Methods.
Para exempliﬁcar tal cen´ario, pode-se imaginar uma aplica¸c˜ao PON na qual seja
necess´ario criar um FBE que simule o comportamento de um time de futebol. O time ´e
composto por dois jogadores, sendo que cada jogador possui um nome, um n´umero e uma
posi¸c˜ao de jogo.
Na atual vers˜ao do LingPON, o desenvolvedor dever´a construir um FBE Time o
qual apresentar´a dois Attributes nome (nome1 e nome2), dois Attributes n´umero (numero1,
numero2) e dois Attributes posi¸c˜ao (posicao1, posicao2). Em se tratando de um time de
dois jogadores, isso n˜ao ´e um grande problema. Entretanto, caso seja necess´ario expandir
o n´umero de jogadores no time, ser´a imprescind´ıvel criar novos Attributes para cada novo
jogador.
Dessa forma, visando aumentar o encapsulamento na LingPON, vislumbra-se a
possibilidade de evoluir a LingPON de forma a permitir que FBEs relacionem outros FBEs,
ou seja, possuam Attributes que sejam deﬁnidos por um FBE. No exemplo apresentado,


25
seria poss´ıvel criar um FBE Jogador e um FBE Time, o qual possuiria quantos Attributes
do tipo Jogador quanto necess´ario para compor um time.
1.3.3
REFLEX˜AO
Esses s˜ao exemplos que demonstram a necessidade de evolu¸c˜ao da LingPON.
Outros exemplos seriam a necessidade de mecanismos de heran¸ca, declara¸c˜ao de vetores
e aloca¸c˜ao dinˆamica de mem´oria. Portanto, refor¸ca-se a necessidade de valida¸c˜ao do
LingPON, inclusive com as novas caracter´ısticas.
Neste sentido, esta disserta¸c˜ao de mestrado se prop˜oe a evoluir a LingPON no
tocante a facilidade de programa¸c˜ao por meio de aprimoramento de rela¸c˜oes de agrega¸c˜ao
entre entidades PON na LingPON. Particularmente, a evolu¸c˜ao englobar´a as solu¸c˜oes
vislumbradas na subse¸c˜ao 1.3.1 (i.e. agrega¸c˜ao de Rules em FBEs) e na subse¸c˜ao 1.3.2 (i.e.
agrega¸c˜ao de FBEs em FBE), bem como a corre¸c˜ao de erros ou bugs existente na atual
vers˜ao do LingPON, tais como erros na gera¸c˜ao de c´odigo alvo quando o c´odigo LingPON
apresenta m´ultiplas instˆancias do mesmo FBE.
Esta evolu¸c˜ao da LingPON (i.e. linguagem e compilador do PON) se dar´a por
meio de mudan¸cas na gram´atica ou BNF (Backus normal form), no analisador l´exico, no
analisador sint´atico, no analisador semˆantico e no gerador de c´odigo relativos ao LingPON.
Isto inclusive por meio de ferramental de desenvolvimento de linguagens e compiladores,
como as ferramentas Flex e Bison.
Ainda, tanto esta evolu¸c˜ao da LingPON, como ela na ´ıntegra ser˜ao neste trabalho
validados por experimentos em uma aplica¸c˜ao com n´ıvel de complexidade que supera as
aplica¸c˜oes anteriores. Desse modo, faz-se necess´ario realizar um levantamento e an´alise,
em termos de quantidade de entidades PON, das aplica¸c˜oes previamente desenvolvidas
utilizando o PON.
Em suma, a aplica¸c˜ao utilizada para a valida¸c˜ao das evolu¸c˜oes da LingPON ser´a
o controle de futebol de robˆos que permite inclusive testes em um estudo de caso de
complexidade reconhecida em v´arios dom´ınios da ciˆencia da computa¸c˜ao e aﬁns [Visser e
Burkhard 2007] 4. Neste contexto, a pr´opria vers˜ao anterior do compilador ser´a testada,
bem como a ´ultima vers˜ao do Framework PON em C++ (Framework PON 2.0) via
vers˜oes da aplica¸c˜ao desenvolvidas nessas materializa¸c˜oes precedentes do PON. Portanto,
isso permitir´a compor compara¸c˜oes entre as principais materializa¸c˜oes correntes em
4Os requisitos funcionais da aplica¸c˜ao de controle de futebol de robˆos s˜ao apresentados no Apˆendice
deste trabalho.


26
software do PON. Por ﬁm, as aplica¸c˜oes nessas materializa¸c˜oes ser˜ao comparadas como
um vers˜ao da aplica¸c˜ao desenvolvida por outrem em POO. Neste, ˆambito as compara¸c˜oes
tratar˜ao inclusive do grau de diﬁculdade de lidar com nova demanda (i.e. mudan¸ca) em
funcionalidades de software no tocante ao POO e ao PON.
1.4
OBJETIVOS
Tendo em vista o apresentado at´e agora em termos de motiva¸c˜ao e justiﬁcativa, a
disserta¸c˜ao de mestrado desenvolvida com base neste trabalho apresenta como objetivos
principais 5:
• Evoluir a tecnologia LingPON (linguagem e seu respectivo compilador), no tocante
a tratar agrega¸c˜oes de entidades PON, nomeadamente FBEs que agregam Rules
e/ou FBEs. Isto com o intuito de evitar redundˆancia de c´odigo e, assim, facilitar a
programa¸c˜ao ou desenvolvimento de aplica¸c˜oes em PON.
• Desenvolver com a tecnologia LingPON at´e ent˜ao vigente, com a tecnologia Ling-
PON proposta neste trabalho e com o Framework PON 2.0, para cada uma dessas
materializa¸c˜oes, uma aplica¸c˜ao de complexidade reconhecida. Nomeadamente, esta
aplica¸c˜ao ´e a reconhecida aplica¸c˜ao de controle para partida de futebol de robˆos.
Tal desenvolvimento visa contribuir para demonstrar e consolidar a factibilidade do
PON em um contexto mais efetivo.
• Comparar entre si, por meio das aplica¸c˜oes em PON para controle futebol de robˆos,
as trˆes materializa¸c˜oes do PON consideradas, bem como a mesma aplica¸c˜ao feita em
POO/PI por outrem. Tais compara¸c˜oes se dar˜ao no tocante ao n´umero de linhas de
c´odigo e tokens6 presentes no c´odigo-fonte e diﬁculdade de manuten¸c˜ao de software
em fun¸c˜ao de nova demanda.
Para atingir estes objetivos principais, o presente trabalho de pesquisa tem os
seguintes objetivos espec´ıﬁcos:
• Evoluir a especiﬁca¸c˜ao da LingPON (linguagem e seu respectivo compilador) de
forma a evitar a redundˆancia na declara¸c˜ao de Rules quando as mesmas devem
5Os objetivos principais deste trabalho poderia ser apresentado de forma tradicional, em um ´unico
par´agrafo, com o mesmo valor semˆantico dos trˆes itens. Entretanto, os objetivos s˜ao apresentados
separadamente de forma a facilitar a compreens˜ao e avalia¸c˜ao dos mesmos.
6Um token ´e um par constitu´ıdo de um nome de token e um valor de atributo opcional identiﬁcado a
partir de um lexema (sequˆencia de caracteres que associa um padr˜ao a um token) [Aho et al. 1995].


27
ser aplicadas sobre todas as instˆancias de um determinado FBE. Isto se dar´a pela
possibilidade de FBE poder agregar Rules;
• Evoluir a especiﬁca¸c˜ao da LingPON (linguagem e seu respectivo compilador) para
suportar agrega¸c˜ao de FBEs atrav´es da declara¸c˜ao de Attributes de tipos n˜ao
primitivos. Isto se dar´a pela possibilidade de FBE poder agregar FBE;
• Realizar levantamento e an´alise das aplica¸c˜oes PON desenvolvidas at´e o presente
momento, em termos de entidades PON presentes no c´odigo-fonte e complexidade
de funcionamento, de forma a evidenciar a simplicidade destas aplica¸c˜oes. Isto
principalmente para as materializa¸c˜oes do PON, nomeadamente Framework PON
2.0 e LingPON 1.0;
• Desenvolver aplica¸c˜oes de controle para o futebol de robˆos utilizando as seguintes
materializa¸c˜oes do PON: Framework PON 2.0 (C++), atual vers˜ao da LingPON
(vers˜ao 1.0) e a nova vers˜ao da LingPON (chamada de vers˜ao 1.27), esta apresentada
neste trabalho;
• Comparar a aplica¸c˜ao desenvolvida utilizando a nova vers˜ao da LingPON com uma
solu¸c˜ao existente, constru´ıda sob o PI, e com solu¸c˜oes desenvolvidas utilizando o
Framework PON 2.0 e a atual vers˜ao da LingPON, utilizando n´umero de linhas e
n´umero de tokens como crit´erios de complexidade de c´odigo-fonte;
• Veriﬁcar propriedades do PON de facilidade de programa¸c˜ao, atrav´es da an´alise
de n´ıvel de manutenibilidade por meio de altera¸c˜ao de requisito, utilizando as
materializa¸c˜oes pertinentes a este trabalho (i.e. Framework PON 2.0, atual vers˜ao
da LingPON e a nova vers˜ao da LingPON) em uma situa¸c˜ao pr´atica a ser comparada
com aplica¸c˜ao equivalente (mesmo funcionamento) desenvolvida em C++ PI/POO
por outrem.
1.5
ATIVIDADES DO M´ETODO DE PESQUISA
A metodologia desta pesquisa envolveu tarefas te´oricas e pr´aticas, com compara¸c˜oes
qualitativas e quantitativas. Dessa forma, foram realizadas seis tarefas principais durante
a pesquisa e desenvolvimento deste trabalho, s˜ao elas: Revis˜ao do Estado da Arte e da
T´ecnica, Reﬂex˜ao e Proposta, Deﬁni¸c˜ao dos Objetivos, Desenvolvimento Investigativo,
7A vers˜ao da LingPON desenvolvida e apresentada neste trabalhado foi deﬁnida como sendo 1.2 por
suportar duas novas funcionalidades, a saber a agrega¸c˜ao de FBE em FBEs e Rule em FBE.


28
Compara¸c˜oes e Valida¸c˜oes e, por ﬁm, Conclus˜ao, conforme apresentado na Figura 2. A
seguir, cada uma destas fases ´e apresentada.
1.5.1
REVIS˜AO DO ESTADO DA ARTE
Primeiramente, com o objetivo de prover uma base s´olida para a argumenta¸c˜ao
e desenvolvimento deste trabalho, foram angariadas referˆencias bibliogr´aﬁcas sobre os
paradigmas de programa¸c˜ao apresentados neste trabalho, nomeadamente o Paradigma
Imperativo, Paradigma Declarativo e Paradigma Orientado a Notiﬁca¸c˜oes. Posteriormente
foi realizado um estudo sobre as materializa¸c˜oes do PON em software, a saber o Framework
PON C++ 2.0 e a LingPON. Por ﬁm, foi realizado um censo das aplica¸c˜oes PON
desenvolvidas at´e o presente momento, de forma a evidenciar a baixa complexidade
na maioria das aplica¸c˜oes PON desenvolvidas at´e o presente momento.
1.5.2
REFLEX˜AO E PROPOSTA
Esta etapa teve como objetivo identiﬁcar as limita¸c˜oes da atual vers˜ao da LingPON,
principalmente no tocante `a agrega¸c˜ao de entidades.
Ademais, com base nos dados
obtidos atrav´es do censo de aplica¸c˜oes PON, contatou-se a necessidade de desenvolver a
apresentar um estudo de caso mais complexo e apropriados aos anteriores para validar
as materializa¸c˜oes do PON em software: Framework PON C++ 2.0 e LingPON. Como
resultado desta reﬂex˜ao, surgiu a proposta de desenvolver uma aplica¸c˜ao de controle de
futebol de robˆos utilizando as materializa¸c˜oes PON software. Para isso, um estudo e
an´alise de uma aplica¸c˜ao j´a existente foram realizados. Por ﬁm, foi proposto a utiliza¸c˜ao
da aplica¸c˜ao de controle de futebol de robˆos para a valida¸c˜ao das materializa¸c˜oes PON em
software.
1.5.3
DEFINIC¸ ˜AO DOS OBJETIVOS
Utilizando os resultados obtidos a partir da etapa de reﬂex˜ao e propostas, foram
deﬁnidos os trˆes objetivos principais apresentados deste trabalho, os quais s˜ao apresentado
na Se¸c˜ao 1.4.
1.5.4
DESENVOLVIMENTO INVESTIGATIVO
A etapa de desenvolvimento iniciou-se pelo desenvolvimento de uma aplica¸c˜ao de
futebol de robˆos, funcionalmente equivalente a uma solu¸c˜ao j´a existente e desenvolvida em


29
Figura 2: Atividades do m´etodo de pesquisa.


30
PI/POO, utilizando o Framework PON C++ 2.0 e a LingPON. Na aplica¸c˜ao desenvolvida
em Framework PON C++ 2.0, foi poss´ıvel validar a rela¸c˜ao de agrega¸c˜oes de entidades
PON, conforme desenvolvido e apresentado em [Ronszcka 2012]. Na aplica¸c˜ao desenvolvida
em LingPON, por sua vez, contatou-se que limita¸c˜oes referentes `a agrega¸c˜ao de entidades
PON diﬁcultava o desenvolvimento de aplica¸c˜oes PON. Sendo assim, foi desenvolvida
uma nova vers˜ao da LingPON (vers˜ao 1.2) que solucionou as duas limita¸c˜oes observadas.
Utilizando esta nova vers˜ao da LingPON, uma nova aplica¸c˜ao de controle de futebol de
robˆos foi desenvolvida.
1.5.5
COMPARAC¸ ˜OES E VALIDAC¸ ˜OES
As aplica¸c˜oes PON de controle de futebol de robˆos desenvolvidas neste trabalho
foram comparadas em rela¸c˜ao `as entidades PON presentes em seu c´odigo-fonte. Posterior-
mente, as aplica¸c˜oes PON foram comparadas, em termos de linhas de c´odigo e quantidade
de tokens presentes no c´odigo-fonte, entre si e com a aplica¸c˜ao PI/POO que foi utilizada
como base na etapa de desenvolvimento investigativo. Por ﬁm, as aplica¸c˜oes PON e a
aplica¸c˜ao PI/POO foram comparadas em termos de facilidade de manuten¸c˜ao, atrav´es de
um experimento de adi¸c˜ao de um novo requisito funcional `a cada um dos sistemas.
1.5.6
CONCLUS˜AO
A ´ultima etapa realizada durante o desenvolvimento deste trabalho contou com a
compila¸c˜ao dos resultados obtidos atrav´es das compara¸c˜oes realizadas na etapa anterior.
Posteriormente realizou-se a etapa de avalia¸c˜ao dos resultados obtidos, a qual permitiu
avaliar os resultados obtidos durante o desenvolvimento deste trabalho.


31
2
REVIS˜AO DO ESTADO DA ARTE
Neste cap´ıtulo s˜ao apresentados os principais conceitos sobre os quais se desenvolve
este trabalho. Em primeiro lugar, a Se¸c˜ao 2.1 apresenta uma sucinta reﬂex˜ao sobre os
paradigmas de programa¸c˜ao usuais da computa¸c˜ao. Em seguida, a Se¸c˜ao 2.2 apresenta o
Paradigma Orientado a Notiﬁca¸c˜oes (PON) de forma mais aprofundada `aquela apresentada
na Subse¸c˜ao 1.1.2. A Se¸c˜ao 2.3 detalha as atuais materializa¸c˜oes do PON em software.
Ainda, a se¸c˜ao 2.4 apresenta o que ´e o futebol de robˆos. Findando o cap´ıtulo, a Se¸c˜ao 2.5
apresenta algumas reﬂex˜oes sobre o presente cap´ıtulo.
2.1
PARADIGMAS DE PROGRAMAC¸ ˜AO
Existem diversas deﬁni¸c˜oes para o signiﬁcado da palavra paradigma no contexto
da computa¸c˜ao.
Segundo David Watt, o termo paradigma de programa¸c˜ao consiste
na sele¸c˜ao de conceitos chaves da programa¸c˜ao (e.g tipos de dados, vari´aveis, escopo,
abstra¸c˜ao, concorrˆencia e controle) utilizados de maneira conjunta para formar um estilo
de programa¸c˜ao [Watt 2004]. Segundo Peter Van Roy, um paradigma de programa¸c˜ao ´e
um sistema formal que deﬁne como a programa¸c˜ao ´e realizada. Cada paradigma tem o
seu pr´oprio conjunto de t´ecnicas para estruturar o pensamento na concep¸c˜ao de solu¸c˜oes
em software [Van-Roy e Haridi 2004].
De forma sucinta, paradigma de programa¸c˜ao ´e o modelo utilizado para com-
preender um problema do mundo real, de forma que o mesmo possa ser solucionado
por sistemas computacionais, tradicionalmente software. Usualmente, o modelo do pa-
radigma de programa¸c˜ao est´a dispon´ıvel para o programador na forma de linguagem
de programa¸c˜ao pr´opria ou em framework sobre outra linguagem de outro paradigma.
Neste sentido, as linguagens de programa¸c˜ao s˜ao as ferramentas capazes de tornar o para-
digma aplic´avel e permitir que artefatos de software possam ser criados para solucionar
problemas [Banaszewski 2009].
Van Roy (2009) apresentou uma taxonomia de como os paradigmas de programa¸c˜ao


32
s˜ao relacionados e qual ´e o caminho das linguagens de programa¸c˜ao at´e os paradigmas e
conceito relacionados a eles. Esta taxonomia ´e apresentada na Figura 3.
Nesta taxonomia, cada paradigma de programa¸c˜ao ´e deﬁnido por um conjunto
de conceitos de programa¸c˜ao e organizado em uma linguagem b´asica simples, nomeada
kernel language [Roy et al. 2009]. Para classiﬁc´a-los, Van Roy utilizou caracter´ısticas
pertinente a cada um deles, tais como conceitos de registros (record), recipientes com
escopo l´exico (closure), independˆencia (concorrˆencia) e estado nomeado (named state),
al´em do n˜ao-determinismo observ´avel 1.
Figura 3: Taxonomia de paradigmas de programa¸c˜ao com o Paradigma Orientado a
Notiﬁca¸c˜oes em destaque. Extra´ıdo de [Xavier 2014].
Atualmente, h´a v´arios paradigmas de programa¸c˜ao. Entretanto, de maneira
resumida, uma forma de classiﬁc´a-los seria em Paradigma Imperativo (PI) e Paradigma
Declarativo (PD) [Van-Roy e Haridi 2004]. O PI ainda pode ser subdividido em Paradigma
Procedimental (PP) e Paradigma Orientado a Objetos (POO). Por sua vez, o PD pode
1N˜ao-determinismo ´e quando a execu¸c˜ao de um programa n˜ao pode ser completamente determinada
pela sua especiﬁca¸c˜ao, isto ´e, em algum momento durante a execu¸c˜ao a especiﬁca¸c˜ao permite ao programa
escolher o que fazer a seguir. Sendo assim, o n˜ao-determinismo observ´avel ocorre quando um usu´ario
pode ver resultados diferentes de execu¸c˜oes a partir da mesma conﬁgura¸c˜ao interna [Roy et al. 2009].


33
ser subdividido em Paradigma Funcional (PF) e Paradigma L´ogico (PL). Isto considerado,
conforme citado na introdu¸c˜ao deste trabalho, o PON encontra alguma inspira¸c˜ao no POO
e no PD. Neste sentido, de forma a compreender as caracter´ısticas do PON e suas vantagens,
faz-se necess´ario entender os conceitos relacionados ao POO e ao PL, particularmente do
Sistemas Baseados em Regras (SBR). Por esse motivo, as subse¸c˜oes sequentes apresentam
maiores detalhes sobre tais paradigmas de programa¸c˜ao.
A revis˜ao sobre paradigmas de programa¸c˜ao apresenta neste trabalho foi baseada
em trabalhos anteriores desenvolvidos pelo grupo de pesquisa da UTFPR sobre o PON,
sendo as principais referˆencias as seguintes [Banaszewski 2009,Xavier 2014].
2.1.1
PARADIGMA IMPERATIVO
O Paradigma Imperativo (PI) engloba dois dos subparadigmas mais utilizados
no desenvolvimento de software: Paradigma Procedimental (PP) e Paradigma Orientado
a Objetos (POO). A utiliza¸c˜ao de ambos os subparadigmas do PI tornou-se popular na
ind´ustria de software devido a quest˜oes como in´ercia cultural, riqueza de abstra¸c˜ao e
ﬂexibilidades algor´ıtmicas [Xavier 2014].
No caso do PP/PI, as vari´aveis e comandos s˜ao organizados em fun¸c˜oes e proce-
dimentos, os quais permitem alcan¸car um grau signiﬁcativo de modularidade no c´odigo
implementado [Watt 2004,Banaszewski 2009].
O POO/PI, por sua vez, apresenta um n´ıvel de abstra¸c˜ao considerado mais rico e
natural para o ser humano, quando comparado ao PP/PI. Os softwares baseados neste
subparadigma s˜ao compostos por entidades modulares denominadas objetos, as quais
representam objetos do mundo real, apresentando somente as caracter´ısticas pertinentes
para a implementa¸c˜ao do sistema computacional [Poo et al. 2007]. As entidades objetos,
em termos t´ecnicos, agrupam atributos (similares a vari´aveis do PP) e m´etodos (simi-
lares a procedimentos ou fun¸c˜oes do PP) relacionados de maneira a estimular coes˜ao e
desacoplamento [Pressman e Maxim 2016,Brookshear 2002,Watt 2004].
Independentemente do subparadigma utilizado, softwares baseados no PI s˜ao
concebidos como sequˆencias de instru¸c˜oes. Esse mecanismo de execu¸c˜ao sequencial consiste
em buscas sobre entidades passivas, as quais correspondem aos dados (e.g vari´aveis, vetores
e listas) e aos comandos de decis˜ao (e.g se-ent˜ao e escolha-de-casos) usualmente executados
dentro de la¸cos de repeti¸c˜ao (e.g for, while e do-while).
Devido `a forma de busca presente na execu¸c˜ao de softwares PI, as linhas de


34
c´odigo se tornam interdependentes, causando assim problemas de redundˆancia temporal e
estrutural em sua execu¸c˜ao. Estes problemas podem, inclusive, acarretar degrada¸c˜ao de
desempenho dos programas desenvolvidos.
A redundˆancia temporal ocorre na avalia¸c˜ao desnecess´aria e repetida de express˜oes
causais na presen¸ca de estados previamente avaliados e inalterados.
A redundˆancia
estrutural, por sua vez, ocorre quando o conhecimento sobre o valor Booleano de uma
express˜ao l´ogica n˜ao ´e compartilhado entre outras express˜oes causais pertinentes, causando
assim reavalia¸c˜oes desnecess´arias [Banaszewski 2009].
Ambas redundˆancias apresentadas s˜ao observadas no C´odigo 1.
Neste, trˆes
express˜oes causais veriﬁcam os estados de x e y dos objetos A e B a ﬁm de alterar o estado
y do objeto B.
C´odigo 1: Exemplo de redundˆancia temporal e estrutural em aplica¸c˜oes
PI [Banaszewski 2009].
1 ...
2 A->setX(false);
3 B->setX(false);
4 B->setY(true);
5
6 while (B->getY() == true) {
7
if (A->getX() == true)
8
{
9
B->setY(true);
10
}
11
if ((B->getX() == true) && (B->getY() == false))
12
{
13
B->setY(true);
14
}
15
if ((B->getX() == true) && (B->getY() == true))
16
{
17
B->setY(false);
18
}
19 }
20 ...


35
A redundˆancia temporal ´e observada na avalia¸c˜ao repetida da primeira express˜ao
causal (linha 7) a cada ciclo interativo, mesmo quando a mesma n˜ao apresenta varia¸c˜ao
em rela¸c˜ao `as avalia¸c˜oes anteriores. A redundˆancia estrutural ´e observada na avalia¸c˜ao da
primeira condi¸c˜ao das duas ´ultimas express˜oes causais (linhas 11 e 15). Esta condi¸c˜ao ´e
avaliada duas vezes em um mesmo ciclo, sem altera¸c˜oes em seu valor l´ogico.
Al´em de problemas de redundˆancia, o PI tamb´em apresenta problemas relacionados
a composi¸c˜ao de programas. Geralmente, nos programas criados com os conceitos do
PI, o c´odigo que envolve o conhecimento l´ogico-causal da aplica¸c˜ao encontra-se disperso
entre os comandos e express˜oes de controle da linguagem, tornando dif´ıcil a leitura e
entendimento do c´odigo, al´em de desviar a aten¸c˜ao do programador do que realmente ´e
importante [Banaszewski 2009].
Os programadores normalmente encontram diﬁculdades na manipula¸c˜ao das
linguagens de programa¸c˜ao imperativas, principalmente no que diz respeito ao controle de
ﬂuxo de execu¸c˜ao atrav´es de loops (e.g for, while e do-while) e por sintaxes pouco intuitivas,
como por exemplo a atribui¸c˜ao de valores por meio do s´ımbolo “=” e de igualdade por
meio do s´ımbolo “==”.
Ademais, a maior diﬁculdade na programa¸c˜ao imperativa se encontra na forma com
a qual o c´odigo ´e organizado. Apesar do POO oferecer avan¸cos em termos de abstra¸c˜oes
de maior compreens˜ao, o c´odigo OO normalmente ´e de dif´ıcil compreens˜ao, n˜ao s´o pela
sintaxe, mas tamb´em pela organiza¸c˜ao l´ogica do c´odigo-fonte [Banaszewski 2009].
Devido aos relacionamentos entre os objetos, torna-se dif´ıcil compreender uma
funcionalidade do sistema analisando apenas uma classe. Normalmente, ´e preciso considerar
as demais classes relacionadas. Essa diﬁculdade se deve `a dispers˜ao da l´ogica da aplica¸c˜ao
em diferente m´etodos de diferentes objetos coligados, o que leva a necessidade de analisar
o ﬂuxo de chamada de m´etodo para entender a l´ogica [Banaszewski 2009].
Esse problema continua mesmo na manuten¸c˜ao de programas. Devido aos relaci-
onamentos entre os objetos que comp˜oem o software OO, a altera¸c˜ao de uma pequena
parcela do conhecimento em algum ponto do c´odigo-fonte pode, muitas vezes, resultar na
necessidade de altera¸c˜ao em outros, criando assim uma rea¸c˜ao em cadeia em termos de
altera¸c˜oes a serem realizadas.
Sendo assim, a inclus˜ao de uma simples express˜ao causal (se-ent˜ao) pode se tornar
uma tarefa dif´ıcil e complexa com o POO. Primeiramente, deve-se encontrar a posi¸c˜ao


36
correta que a express˜ao deve ser inserida no c´odigo-fonte. Na sequˆencia, deve-se analisar o
ﬂuxo de execu¸c˜ao, uma vez que a mesma n˜ao pode afetar a avalia¸c˜ao das demais express˜oes
e deve apresentar oportunidade de ser avaliada [Banaszewski 2009].
2.1.2
PARADIGMA ORIENTADO A EVENTOS
Considerado por alguns como um paradigma de programa¸c˜ao atualmente associado
principalmente ao POO (ainda que haja tecnologias com PP/PI e mesmo PD) [Brookshear
2012,Ferg 2006], a programa¸c˜ao orientada a eventos (POE) busca amenizar a redundˆancia
temporal presente nas aplica¸c˜oes atrav´es do controle de ﬂuxo determinado por eventos.
Um evento, por sua vez, ´e uma condi¸c˜ao detectada que pode disparar uma notiﬁca¸c˜ao,
a qual ser´a enviada para um recebedor deﬁnido em tempo de execu¸c˜ao [Faison 2006]
(conforme Figura 4).
Figura 4: Evento, condi¸c˜ao detectada e notiﬁca¸c˜ao [Faison 2006].
Um evento ocorre de forma imprevis´ıvel e pode ser exempliﬁcado por um bot˜ao
pressionado, uma interrup¸c˜ao de hardware ou uma mensagem recebida, oriunda de uma
entidade externa `a aplica¸c˜ao [Xavier 2014]. Esse evento instiga uma determinada a¸c˜ao (i.e
m´etodo), conforme Figura 5. A a¸c˜ao normalmente est´a contida em um tipo determinado de
m´odulo, como um bloco, objeto, observador, consumidor ou, at´e mesmo, agente [Eugster
et al. 2003,Faison 2006,Hansen e Fossum 2010].
Figura 5: Paradigma Orientado a Eventos adaptado de [Hansen e Fossum 2010].
Em geral, um software baseado em eventos ´e mais simples sob o ponto de vista
estrito de c´odigo [Faison 2006]. Isto ocorre porque a POE propicia componentes menores,
razoavelmente coesos e desacoplados amenizando redundˆancias. Entretanto, ainda que
amenize quest˜oes de redundˆancias, POE n˜ao as resolve pois em cada procedimento ou


37
similar disparado por evento tal deﬁciˆencia n˜ao raro permanece. Ademais, aumenta-se a
dispers˜ao l´ogica e os relacionamentos do software, sendo necess´ario percorrer e compreender
todo o conjunto de unidades de uma aplica¸c˜ao [Pordeus 2016,Faison 2006,Brookshear
2012,Xavier 2014].
2.1.3
PARADIGMA DECLARATIVO
Diferentemente do PI, o Paradigma Declarativo (PD) possibilita uma programa¸c˜ao
de mais alto n´ıvel quando comparada ao PI, permitindo ao programador focar mais na
organiza¸c˜ao do conhecimento para a solu¸c˜ao do problema computacional do que na forma
de implementa¸c˜ao do mesmo. Neste sentido, o PD exige que o programador descreva as
regras que comp˜oem o conhecimento l´ogico-causal do sistema, ao inv´es de escrever C´odigos
na forma de sequˆencia de instru¸c˜oes que solucionem o problema, como ocorre no PI [Riley
e Giarratano 1993,Krug 2016].
No PD, enfatizando Sistemas Baseados em Regras (SBR), softwares s˜ao compostos
por elementos da Base de Fatos, os quais podem possuir atributos e m´etodos similares
a objetos da POO. Posteriormente, deﬁne-se uma Base de Regras com rela¸c˜oes causais
relativas `as entidades da Base de Fatos. Estas duas bases s˜ao processadas por meio de
uma M´aquina de Inferˆencia, a qual compara as regras e fatos (e.g estados dos atributos)
gerando assim novos fatos e, portanto, um novo ciclo de inferˆencia [Xavier 2014]. Estes
componentes formam a arquitetura dos SBR, como apresentado na Figura 6.
Figura 6: Arquitetura de um Sistema Baseado em Regras (SBR).
Um ciclo de inferˆencia do SBR consiste em trˆes fases distintas:
• Matching: essa fase compara os fatos em rela¸c˜ao as regras. As regras aprovadas s˜ao
ent˜ao colocadas, de forma desordenada, em um reposit´orio chamado conjunto de
conﬂito (i.e conﬂict set).


38
• Sele¸c˜ao: nessa fase as regras presente no conjunto de conﬂito s˜ao ordenadas segundo
uma estrat´egia de resolu¸c˜ao de conﬂitos, como a estrat´egia baseada na prioridade
das regras ou a estrat´egia relativa a recenticidade dos fatos que ativaram as regras,
para formar o conjunto ordenado de regras chamado Agenda.
• Execu¸c˜ao: nessa fase a primeira regra da Agenda ´e selecionada e a a¸c˜ao relacionada
a mesma ´e executada. Nesta execu¸c˜ao, a regra pode inserir novos elementos na Base
de Fatos ou, at´e mesmo, invocar algum servi¸co externo (e.g fun¸c˜oes de alguma outra
entidade de software).
Entre as fases de um ciclo de inferˆencia, a fase de matching ´e a que mais interfere
no desempenho dos SBR. Nos primeiros SBR, durante a fase de matching, cada regra era
avaliada contra os estados da cada um dos elementos da base de fatos. Com isso, essa fase
do ciclo de inferˆencia correspondia a aproximadamente 90% do tempo de execu¸c˜ao dos
SBR [Miranker e Lofaso 1991]. A ineﬁciˆencia destes sistemas ocorria principalmente devido
`a avalia¸c˜ao redundante entre fatos e regras, uma vez que muitos desses testes realizados
durante a fase de matching apresentavam o mesmo resultado dos ciclos anteriores, gerando
assim desperd´ıcio de processamento [Banaszewski 2009].
Para solucionar, ou ao menos amenizar, a ineﬁciˆencia da fase de matching, algumas
solu¸c˜oes foram propostas. Basicamente os novos C´odigos de inferˆencia buscam guardar os
estados j´a avaliados em ciclos anteriores. Dessa forma, as regras s˜ao comparadas apenas
com os estados dos elementos da base de fatos atualizados recentemente. Estas solu¸c˜oes
s˜ao chamadas de C´odigos de inferˆencia incrementais. Exemplos deste tipo de C´odigo s˜ao
o RETE [Forgy 1982], o TREAT [Miranker 1987], o LEAPS [Miranker et al. 1990] e o
HAL [Lee e Cheng 2002].
2.2
PARADIGMA ORIENTADO A NOTIFICAC¸ ˜OES
Esta se¸c˜ao detalha o Paradigma Orientado a Notiﬁca¸c˜oes (PON), o qual foi
brevemente introduzido na Subse¸c˜ao 1.1. Primeiramente, nesta presente se¸c˜ao, a Subse¸c˜ao
2.2.1 apresenta a rela¸c˜ao existente entre o PON e os paradigmas Imperativo e Declarativo. A
Subse¸c˜ao 2.2.2 apresenta o mecanismo de notiﬁca¸c˜ao do PON. Por sua vez, a Subse¸c˜ao 2.2.3
aborda o mecanismo de resolu¸c˜ao de conﬂitos e garantias de determinismo em aplica¸c˜oes
PON. A Subse¸c˜ao 2.2.4, particularmente, reﬂete e contextualiza sobre as propriedades
inerentes ao PON. A Subse¸c˜ao 2.2.5 deﬁne as caracter´ısticas de utiliza¸c˜ao e compreens˜ao do
PON. Ainda, a Subse¸c˜ao 2.2.6, detalha a fun¸c˜ao assint´otica do PON em rela¸c˜ao ao processo


39
de resolu¸c˜ao de c´alculo l´ogico-causal. Subsequentemente, a subse¸c˜ao 2.2.7 apresenta os
detalhes sobre a propriedade do PON denominada Attributes impertinentes. Por ﬁm, a
subse¸c˜ao 2.2.8 apresenta o conceito de Regras de Forma¸c˜ao do PON.
2.2.1
RELAC¸ ˜AO ENTRE O PON E OS PARADIGMAS IMPERATIVO E DECLARA-
TIVO
Conforme apresentado no C´odigo 2, escrito em linguagem de programa¸c˜ao PON
(a qual ser´a apresentado na Se¸c˜ao 2.3.2), o PON aproveita caracter´ısticas de ambos os
paradigmas previamente apresentados, a saber o PI e o PD. Similarmente ao que ocorre
no Paradigma Imperativo, mais especiﬁcamente na POO atrav´es de seus objetos, no PON
´e poss´ıvel declarar entidades computacionais que possuam atributos e m´etodos. Al´em
disso, a forma como o conhecimento l´ogico-causal da aplica¸c˜ao ´e representado no PON ´e
semelhante `a base de fatos e de regras dos SBR do Paradigma Declarativo [Banaszewski
2009].


40
C´odigo 2: Exemplo de c´odigo PON.
1 fbe Robot
2
attributes
3
boolean atGameStarted false
4
end attributes
5
methods
6
method mtRunToBall ( ... )
7
end methods
8 end fbe
9
10 inst
11
Robot robot1
12 end inst
13
14 rule rlRunToBallRobot1
15
condition
16
subcondition condition1
17
premise prRobot1Started robot1.atGameStarted == true
18
end subcondition
19
end condition
20
action
21
instigation inRobot1Started robot1.mtRunToBall();
22
end action
23 end rule
Embora aproveite conceitos dos dois paradigmas citados, o PON apresenta uma
nova forma de estruturar e executar a l´ogica de programas computacionais, fato este que
justiﬁcaria sua classiﬁca¸c˜ao como um paradigma [Linhares 2015]. O modelo do PON
imp˜oe a express˜ao da dinˆamica de funcionamento de um software e da sua l´ogica de causa
e efeito por meio de notiﬁca¸c˜oes potencialmente executadas em paralelo [Linhares 2015].
Essa caracter´ıstica o diferencia do comportamento de programas PI, nos quais a l´ogica
do programa ´e totalmente dependente da sequˆencia de execu¸c˜ao e dos SBR, nos quais a
sequˆencia de execu¸c˜ao ´e abstra´ıda e dependente do mecanismo de inferˆencia monol´ıtico
utilizado [Linhares 2015].


41
2.2.2
MECANISMO DE NOTIFICAC¸ ˜AO DO PON
Um novo conceito para a constru¸c˜ao e execu¸c˜ao de aplica¸c˜oes de software ´e
introduzido pelo Paradigma Orientado a Notiﬁca¸c˜oes (PON). No PON, as aplica¸c˜oes s˜ao
compostas por pequenas entidades reativas e desacopladas, as quais colaboram por meio
de notiﬁca¸c˜oes precisas e pontuais, ditando assim o ﬂuxo de execu¸c˜ao de tais aplica¸c˜oes.
Esse novo modo de estruturar e executar software tende a proporcionar uma melhora no
desempenho das aplica¸c˜oes e, potencialmente, facilitar o desenvolvimento de aplica¸c˜oes
distribu´ıdas [Sim˜ao e Stadzisz 2008,Sim˜ao e Stadzisz 2009,Sim˜ao et al. 2012].
Gra¸cas ao orquestramento da cadeia de notiﬁca¸c˜oes pontuais entre as entidades
PON, emergido do c´odigo PON em tempo de constru¸c˜ao, o ﬂuxo de execu¸c˜ao das aplica¸c˜oes
PON ´e realizado de modo transparente ao desenvolvedor. Isto diferencia-se do ﬂuxo de
execu¸c˜ao encontrado em aplica¸c˜oes do PI, incluindo o subparadigma OO, no qual o
desenvolvedor informa de maneira expl´ıcita o la¸co de itera¸c˜ao atrav´es de comandos como
while e for. No PON, a repeti¸c˜ao ocorre de forma natural na perspectiva de execu¸c˜ao
da aplica¸c˜ao a partir da mudan¸ca de estado de um Attribute, conforme exempliﬁcado na
Figura 7.
Figura 7: Inferˆencia por notiﬁca¸c˜oes [Sim˜ao et al. 2014].
O ﬂuxo de execu¸c˜ao inicia-se a partir da mudan¸ca de estado de um Attribute de
um determinado FBE. Ap´os sua mudan¸ca de estado, o Attribute notiﬁca todas as Premises
pertinentes, a ﬁm de que estas reavaliem seus estados l´ogicos. Caso o valor l´ogico de uma


42
Premise se altere, a Premise colabora com a avalia¸c˜ao l´ogica de uma ou de um conjunto de
Conditions conectadas, o que ocorre por meio da notiﬁca¸c˜ao sobre a mudan¸ca relacionada
ao seu estado l´ogico [Banaszewski 2009].
Consequentemente, cada Condition notiﬁcada avalia o seu valor l´ogico de acordo
com as notiﬁca¸c˜oes recebidas das Premises e com um dado operador l´ogico, sendo nor-
malmente tal operador de conjun¸c˜ao ou disjun¸c˜ao. Assim, no caso de uma conjun¸c˜ao
por exemplo, quando todas as Premises que integram uma Condition s˜ao satisfeitas, a
Condition tamb´em ´e satisfeita. Isto resulta na aprova¸c˜ao de sua respectiva Rule que pode
ent˜ao ser executada [Banaszewski 2009].
Sendo assim, quando uma dada Rule aprovada est´a pronta para ser executada
(i.e aprovada e com conﬂitos resolvidos conforme discutido na pr´oxima subse¸c˜ao), a sua
Action ´e ativada. Uma Action, por sua vez, ´e conectada a um ou v´arios Instigations. Os
Instigations colaboram com as atividades das Actions, acionando a execu¸c˜ao de algum
servi¸co de um objeto FBE por meio dos seus Methods. Usualmente, os Methods alteram
os estados dos Attributes, recome¸cando assim o ciclo de notiﬁca¸c˜oes. [Banaszewski 2009]
Oportunamente, as conex˜oes entre os objetos notiﬁcantes s˜ao estabelecidas em
tempo de cria¸c˜ao. Por exemplo, toda Premise quando criada deve possuir pelo menos um
Attribute associado. Uma vez que um Attribute ´e referenciado em uma Premise, o Attribute
considera automaticamente esta Premise como sendo interessada em receber notiﬁca¸c˜oes
sobre qualquer altera¸c˜ao em seu estado. Assim, o Attribute identiﬁca todas as Premises
interessadas e notiﬁca-as quando o seu estado ´e alterado. Ainda, mecanismo similar
ocorre em rela¸c˜ao `as Premises e as Conditions, bem como as rela¸c˜oes entre Conditions e
Rules [Banaszewski 2009].
2.2.3
RESOLUC¸ ˜AO DE CONFLITOS NO PON
Um conﬂito ocorre quando duas ou mais Rules referenciam um mesmo FBE e
demandam exclusividade de acesso ao mesmo. Isto posto, as Rules concorrem para adquirir
acesso exclusivo a este FBE, sendo que somente uma destas Rules deve ser executada por
vez aﬁm de garantir determinismo e consistˆencia. Neste ˆambito, visando solucionar conﬂitos
entre as Rules, o ﬂuxo de execu¸c˜ao das mesmas ´e determinado segundo uma estrat´egia
preestabelecida. Visando alcan¸car o ﬂuxo de execu¸c˜ao pretendido, o desenvolvedor pode
escolher qual estrat´egia ser´a utilizada para a resolu¸c˜ao de conﬂitos [Banaszewski 2009].
Em um ambiente monoprocessado, a resolu¸c˜ao de conﬂitos visa estabelecer uma


43
ordem de execu¸c˜ao para Rules, de forma que apenas uma Rule possa ser executada por vez.
Para isso, ´e empregado um escalonador de Rules formado por uma estrutura de dados do
tipo linear (e.g ﬁla, lista ou pilha) [Banaszewski 2009]. Tais estruturas recebem as Rules
na ordem em que s˜ao aprovadas e as organiza de acordo com os preceitos da estrat´egia de
resolu¸c˜ao de conﬂitos adotada [Banaszewski 2009], conforme ilustrado na Figura 8.
Figura 8: Modelo Centralizado de Resolu¸c˜ao de Conﬂitos [Banaszewski 2009].
Os modelos de resolu¸c˜ao de conﬂitos empregados para o PON em ambientes
monoprocessados s˜ao:
• BREADTH ou Largura: baseia-se no escalonamento First In, First Out (FIFO),
ou seja, refere-se `a execu¸c˜ao de Rules seguindo a estrutura de dados do tipo ﬁla;
• DEPTH ou Profundidade: baseia-se no escalonamento Last In, First Out (LIFO),
ou seja, refere-se `a execu¸c˜ao de Rules seguindo a estrutura de dados do tipo pilha; e
• PRIORITY ou Prioridade: organiza as Rules de acordo com as prioridades deﬁnidas
na cria¸c˜ao dass mesmas.
Quando nenhuma estrat´egia de resolu¸c˜ao de conﬂito for deﬁnida em uma aplica¸c˜ao
PON, utiliza-se a estrat´egia NO ONE por padr˜ao. Essa estrat´egia faz com que as entidades
Rules n˜ao sejam enviadas ao escalonador, sendo imediatamente executadas ap´os respectiva
aprova¸c˜ao.
As estrat´egias de resolu¸c˜ao de conﬂitos apresentadas s˜ao particularmente aplic´aveis
a aplica¸c˜oes PON monoprocessadas, ainda que possam ser ´uteis em solu¸c˜oes multiprocessa-
das e distribu´ıdas [Banaszewski 2009]. Entretanto, a resolu¸c˜ao de conﬂitos em aplica¸c˜oes
PON concorrentes e/ou distribu´ıdas deveriam ser realizadas a partir de solu¸c˜oes que lhe
sejam mais apropriadas (i.e. n˜ao centralizadoras). Ainda que este trabalho n˜ao seja
relativo `a aplica¸c˜oes PON em sistemas concorrentes ou distribu´ıdos, os trabalhos [Sim˜ao


44
2005,Banaszewski 2009,Sim˜ao et al. 2010] apresentam solu¸c˜oes ´uteis para a resolu¸c˜ao de
conﬂitos em ambientes distribu´ıdos, bem como solu¸c˜oes correlatas para certa garantia de
determinismo.
2.2.4
PROPRIEDADES INERENTES AO PON
´E not´avel que a essˆencia computacional no PON est´a organizada e distribu´ıda
entre entidades reativas que colaboram por meio de notiﬁca¸c˜oes pontuais. Este arranjo
forma o mecanismo de notiﬁca¸c˜oes apresentado na subse¸c˜ao 2.2.2 o qual determina o ﬂuxo
de execu¸c˜ao das aplica¸c˜oes PON.
Atrav´es desse mecanismo, as responsabilidades de um programa PON s˜ao divididas
entre as diferentes instˆancias do modelo.
Neste sentido, a colabora¸c˜ao por meio de
notiﬁca¸c˜oes pontuais e precisas representaria a solu¸c˜ao para parte das deﬁciˆencias dos
atuais paradigmas de programa¸c˜ao.
Neste ˆambito, ao evitar buscas sobre entidades passivas, o PON implicitamente
evita redundˆancias estruturais e temporais que tanto afetam o desempenho de aplica¸c˜oes
no PI e mesmo no PD [Banaszewski 2009]
Ademais, os objetos participantes da cadeia de notiﬁca¸c˜ao do PON apresentam-
se desacoplados, devido `a comunica¸c˜ao realizada por meio de notiﬁca¸c˜oes pontuais e
precisas. Dessa forma, pode-se considerar que o PON seja apropriado para a execu¸c˜ao
em ambientes multiprocessados, uma vez que cada objeto notiﬁcante precisa apenas
conhecer os endere¸cos dos objetos a serem notiﬁcados para que o ciclo de notiﬁca¸c˜oes
ocorra [Banaszewski 2009,Sim˜ao et al. 2012]. Isto tem sido demonstrado em trabalhos
sobre o PON [Peters et al. 2012,Linhares et al. 2015,Belmonte et al. 2016]
2.2.5
PON – UTILIZAC¸ ˜AO X COMPREENS˜AO
O PON permite uma nova maneira de estruturar, executar e pensar os artefatos
de software. Ainda que o PON permita compor software em alto n´ıvel na forma de regras
sem o conhecimento de sua essˆencia, conhecˆe-la ´e importante em certas situa¸c˜oes [Sim˜ao et
al. 2012]. A compreens˜ao dos princ´ıpios do PON ´e importante para aplica¸c˜oes complexas,
onde o ﬂuxo de notiﬁca¸c˜oes ´e intenso e precisa-se de maior formalismo e rastreabilidade,
como em aplica¸c˜oes de tempo real e controle discreto. Na verdade, esse tipo de aplica¸c˜ao
pode exigir apoio de ferramentas formais para elabora¸c˜ao do projeto [Sim˜ao et al. 2012].
Um exemplo particular de formalismo ´e o DON (Desenvolvimento Orientado a


45
Notiﬁca¸c˜oes, proposto prototipalmente no ano de 2011 em [Wiecheteck et al. 2011]. O
DON ´e um m´etodo para projeto de software PON. A solu¸c˜ao proposta ´e baseada em
um perﬁl UML que expressa os conceitos PON e viabiliza a sua aplica¸c˜ao na etapa de
modelagem de um processo de engenharia de software [Wiecheteck et al. 2011,Linhares
2015]. Atualmente, uma Metodologia de Projeto de Software Orientada a Notiﬁca¸c˜oes
(MON) est´a sendo desenvolvida como uma metodologia iterativa e incremental, na qual os
elementos fundamentais do PON s˜ao considerados desde os primeiros n´ıveis de modelagem
[Mendon¸ca 2016].
2.2.6
C´ALCULO ASSINT´OTICO DA INFERˆENCIA DO PON
Em seu pior cen´ario, a complexidade assint´otica polinomial do PON ´e representada
por O(n3) ou O(FactBaseSize * nPremises * nRules), onde FactBaseSize corresponde ao
tamanho m´aximo de objetos Attributes, nPremises corresponde ao tamanho m´aximo de
objetos Premises notiﬁcados por estes Attributes e nConditions corresponde ao tamanho
m´aximo de objetos Conditions notiﬁcados por estas Premises [Sim˜ao 2005,Banaszewski
2009]. A fun¸c˜ao assint´otica apresentada para o PON, no pior cen´ario, demonstra uma
fun¸c˜ao bastante similar, mas ainda assim mais eﬁciente, ao mecanismo de notiﬁca¸c˜oes do
C´odigo HAL e mais eﬁciente do que os C´odigos de inferˆencia RETE, TREAT e LEAPS,
sendo esses dois derivados do RETE [Banaszewski 2009].
Essa fun¸c˜ao assint´otica representa a ordem da quantidade de notiﬁca¸c˜oes que
ocorre entre objetos colaboradores, o que tamb´em corresponde `a ordem da quantidade de
avalia¸c˜oes l´ogicas. A constata¸c˜ao desta fun¸c˜ao assint´otica pode ser realizada pela an´alise
da Figura 9, a qual demonstra as rela¸c˜oes por notiﬁca¸c˜oes entre os objetos colaboradores.
Nesta, os Attributes, Premises, Conditions e Rules correspondem, respectivamente, aos
s´ımbolos Att, Pr, Cd e Rl [Banaszewski 2009].
Outra forma menos ortodoxa de analisar a complexidade assint´otica do PON ´e
considerar o caso m´edio, ao inv´es do pior caso, uma vez que o pior caso ´e irrealista dado
que seria improv´avel que todos os Attributes notiﬁcassem todas as Premisses e assim por
diante.
Neste sentido, a an´alise da complexidade do caso m´edio ´e iniciada analisando-se
o come¸co do processo de notiﬁca¸c˜ao do PON atrav´es da entidade Attribute. Assim, as
principais vari´aveis envolvidas em uma notiﬁca¸c˜ao de um Attribute s˜ao demonstradas pela
Equa¸c˜ao 1.
ppgcaFBat = NumPremises + NumRules
(8)


46
Figura 9: C´alculo assint´otico do mecanismo de notiﬁca¸c˜oes [Banaszewski 2009]
A vari´avel NumPremises representa a soma de entidades Premises relacionadas ao
respectivo Attribute e a vari´avel NumRules ´e a soma das entidades Rules relacionadas a cada
entidade Premise contada em NumPremises. Portanto, se for considerado simplesmente
cada ciclo de inferˆencia como a instiga¸c˜ao de um Attribute e w sendo o n´umero de todos
os Attributes existentes, uma m´edia poss´ıvel seria:
TMedium(x) = (FBAT.1() + ... + FBAT.w())/w
(9)
Assim, o resultado desta m´edia seria uma ordem de (n), o que implicaria uma
complexidade linear [Sim˜ao 2005].
2.2.7
ATTRIBUTES IMPERTINENTES
A reatividade presente nos Attributes proporciona, na maioria dos casos, uma
execu¸c˜ao livre de avalia¸c˜oes redundantes e desnecess´arias, comuns aos paradigmas de
programa¸c˜ao usuais. Entretanto, existem casos em que a varia¸c˜ao de um Attribute encadeia
uma sequˆencia de notiﬁca¸c˜oes indesej´aveis [Ronszcka 2012].
Isso ocorre em situa¸c˜oes nas quais um dado Attribute apresenta mudan¸cas frequen-
tes de estado, disparando o ﬂuxo de notiﬁca¸c˜oes a cada varia¸c˜ao, sem afetar efetivamente
a aprova¸c˜ao da Rule associada. Isto poderia ser grave em casos de muitas notiﬁca¸c˜oes


47
desnecess´arias, as quais impactariam negativamente o desempenho de uma aplica¸c˜ao
PON [Ronszcka 2012].
De modo a ilustrar o problema da impertinˆencia, considera-se o exemplo ilustrado
na Figura 10. Neste exemplo, s˜ao apresentado dois Attributes distintos de um FBE que
representa um robˆo SSL da RoboCup. O primeiro Attribute ´e atWithBall (Boolean), o
qual indica se o robˆo est´a com a posse da bola, e o outro ´e atDistanceGoal (Double),
o qual representa a distˆancia do robˆo ao gol advers´ario. Ambos participam de uma
Condition/Rule composta por duas Premises, sendo que a primeira Premise avalia se
o estado de atWithBall ´e verdadeiro, enquanto a outra Premise avalia se o valor de
atDistanceGoal ´e menor do que um dado valor preestabelecido.
Figura 10: Impacto nas altera¸c˜oes de estado de Attributes ativos (adaptado de [Ronszcka
2012]).
O Attribute atWithBall apresentaria poucas varia¸c˜oes em seu estado, permane-
cendo a maior parte do tempo com o estado false, disparando assim o ﬂuxo de notiﬁca¸c˜oes
esporadicamente. Por sua vez, o Attribute atDistanceGoal apresentaria altera¸c˜oes constan-
tes em seu estado, uma vez que o robˆo est´a em constante movimenta¸c˜ao pelo campo de
jogo, gerando assim constantes notiﬁca¸c˜oes a Rule associada.
Neste sentido, um Attribute como atDistanceGoal pode ser categorizado como
‘impertinente’. Neste dado contexto, o Attribute passa a ter suas fun¸c˜oes reativas desa-
bilitadas temporariamente, conforme ilustrado na Figura 11. Dessa forma, as varia¸c˜oes
de estado do Attribute atDistanceGoal n˜ao iniciariam o ﬂuxo de notiﬁca¸c˜oes para as
Conditions-Rules associados ao Attribute.
Neste ˆambito, quando o conjunto dos Attributes aprovar suas respectivas Premises
em uma dada Condition-Rule, essa deve solicitar a reativa¸c˜ao das notiﬁca¸c˜oes para a
Premise composta pelo Attribute impertinente. Assim, uma vez que o Attribute atWithBall


48
Figura 11: Impacto nas altera¸c˜oes es estado de Attributes impertinentes (adapatado
de [Ronszcka 2012])
.
apresentasse estado verdadeiro, a Conditiion ilustrada solicitaria a reativa¸c˜ao da Premise
correspondente ao Attribute atDistanceGoal, conforme ilustrado na Figura 12
Figura 12: Exemplo de reativa¸c˜ao de uma entidade desativada (adapatado de [Ronszcka
2012])
.
Dessa forma, o Attribute atWithBall, ao apresentar o estado verdadeiro, colocaria
tal Condition em “ponto de aprova¸c˜ao”, o que reativaria as fun¸c˜oes reativas da Premise
desconsiderada. Assim, a entidade Premise em quest˜ao permitiria ser notiﬁcada novamente
pelo Attribute atDistanceGoal. Por ﬁm, ap´os a devida aprova¸c˜ao e execu¸c˜ao da Rule em
quest˜ao, o Attribute impertinente voltaria a ignorar tal Premise at´e que seja requisitado
novamente por outra Condition [Ronszcka 2012].
2.2.8
REGRAS DE FORMAC¸ ˜AO
Deﬁnido por Sim˜ao em [Sim˜ao 2001], uma Regra de Forma¸c˜ao ou Formation Rules
´e uma entidade sob a forma de regra que explica como ser´a criada uma ou mais Rules.


49
Desse modo, uma Formation Rule n˜ao ´e uma Rule a ser executada, mas sim uma forma
gen´erica de constitui¸c˜ao de um conjunto de Rules [Sim˜ao 2001].
Neste sentido, a utiliza¸c˜ao de Formation Rule permite a cria¸c˜ao de Rules espec´ıﬁcas,
a partir da representa¸c˜ao gen´erica de uma Rule. Este conceito ´e bastante ´util quando o
conhecimento causal de uma Rule ´e comum para diferentes conjuntos de instˆancias de
FBEs, ou seja, um conjunto de Rules espec´ıﬁcas se diferencia apenas nas instˆancias de
FBEs referenciadas [Pordeus 2016].
2.3
MATERIALIZAC¸ ˜OES DO PON
Os conceitos do PON foram primeiramente materializados sobre o POO, atrav´es
de um arqu´etipo ou Framework desenvolvido com a linguagem de programa¸c˜ao C++. Tal
materializa¸c˜ao possibilitou a demonstra¸c˜ao dos principais conceitos do PON, permitindo
a cria¸c˜ao de aplica¸c˜oes sob o dom´ınio desse novo paradigma. Entretanto, as aplica¸c˜oes
desenvolvidas utilizando o Framework apresentaram desempenho n˜ao t˜ao satisfat´orio
quanto esperado a luz do c´alculo assint´otico do PON. Isto se d´a principalmente devido
ao uso de estruturas de dados computacionalmente caras, tais como listas duplamente
encadeadas da biblioteca Standard Template Library (STL), que foram utilizadas no seu
desenvolvimento. [Banaszewski 2009,Valen¸ca 2013].
Concluiu-se ent˜ao que existia a necessidade de melhorias no estado da t´ecnica
para que o PON atingisse o que fora vislumbrado em seu estado da arte. Neste ˆambito,
foi desenvolvida uma linguagem de programa¸c˜ao espec´ıﬁca, acompanhada do respectivo
compilador, que traduz o c´odigo PON para c´odigo-alvo mais puro, isto ´e, com menos
depˆendencia de conceitos de outros paradigmas, evitando assim o uso de estruturas de
dados complexas [Ferreira 2016].
Ademais, vislumbrou-se a possibilidade de materializar o PON atrav´es de im-
plementa¸c˜oes em hardware, de modo que aplica¸c˜oes pudessem ser concebidas seguindo
o modelo PON de maneira mais ﬁdedigna no tocante ao paralelismo [Pordeus 2016].
Alguns trabalhos foram realizados neste ˆambito, com destaque a [Witt et al. 2011,Jasinski
2012,Peters 2012,Kerschbaumer et al. 2015]. Recentemente, como outro avan¸co no ˆambito
de PON em hardware, Linhares (2015) propˆos uma nova abordagem para execu¸c˜ao de
software PON, na forma de uma arquitetura de computador denominada Notiﬁcation
Oriented Computer Paradigm (NOCA) [Linhares et al. 2015].
Entretanto, esse trabalho visa a evolu¸c˜ao do estado da t´ecnica do PON no ˆambito


50
de software. Dessa forma, as pr´oximas subse¸c˜oes apresentam maiores detalhes apenas sobre
as materializa¸c˜oes em software do PON que s˜ao consideradas assaz est´aveis e testadas.
Al´em de detalhar as materializa¸c˜oes em software do PON, este trabalho apresenta
tamb´em um censo das aplica¸c˜oes PON desenvolvidas at´e o presente momento. Maiores
informa¸c˜oes sobre estas aplica¸c˜oes s˜ao apresentadas no Apˆendice E.
2.3.1
FRAMEWORK PON
O Framework PON consiste em uma estrutura de elementos orientada a objetos,
constru´ıda com a utiliza¸c˜ao da linguagem de programa¸c˜ao C++, correspondentes `as
entidades que comp˜oem o modelo do PON e a luz do PON. O principal objetivo deste
Framework ´e oferecer uma interface de programa¸c˜ao para a implementa¸c˜ao de aplica¸c˜oes
sob o vi´es do PON, deﬁnindo as abstra¸c˜oes necess´arias para compor os FBEs e respectivas
Rules, tanto FBEs quanto Rules com seus respectivos constituintes [Linhares 2015,Valen¸ca
2013].
A vers˜ao 1.0 do Framework PON foi desenvolvida por Banaszewski [Banaszewski
2009] a partir de uma vers˜ao prototipal concebida por Sim˜ao em 2007 [Sim˜ao et al.
2012], sendo esta vers˜ao prototipal derivado de seus esfor¸cos de disserta¸c˜ao de mestrado e
tese de doutorado no ˆambito do atualmente chamado Controle Orientado a Notiﬁca¸c˜oes
(CON) [Sim˜ao 2001,Sim˜ao 2005]. Por ser um conjunto de classes materializados sobre
o PI, o Framework PON 1.0 tem sua implementa¸c˜ao baseada em percorrimentos sobre
estruturas de dados, fornecidas pela STL - Standard Template Library2, para avalia¸c˜ao de
rela¸c˜oes l´ogico-causais e envio de notiﬁca¸c˜oes [Linhares 2015]. A principal vantagem de
uma materializa¸c˜ao constru´ıda sobre o POO/PI ´e a possibilidade de r´apida prototipa¸c˜ao
de aplica¸c˜oes PON para teste sobre plataformas de computa¸c˜ao convencionais, o que
inicialmente permitiu a demonstra¸c˜ao da viabilidade do PON. Entretanto, esta forma de
implementa¸c˜ao ´e desvantajosa `a ﬁlosoﬁa do PON em si, pois fundamenta seu funcionamento
em estruturas de dados caras e percurso sequencial sobre estas estruturas, o que ´e natural
em PI [Linhares 2015].
Dadas algumas quest˜oes de implementa¸c˜ao do Framework PON em sua vers˜ao
1.0, em particular a degrada¸c˜ao de desempenho causada por sua implementa¸c˜ao baseada
em estruturas de dados baseadas em Standard Template Lists (STL) do C++, Ronszcka
e Valen¸ca (2012) efetuaram uma s´erie de otimiza¸c˜oes com o objetivo de melhorar o
desempenho de execu¸c˜ao de aplica¸c˜oes constru´ıdas utilizando o Framework. Um dos
2Biblioteca padr˜ao/standard de gabaritos/templates do C++.


51
resultados deste trabalho ´e uma nova vers˜ao do Framework PON (vers˜ao 2.0) baseada em
uma variedade de estruturas de dados mais otimizadas do que as equivalentes fornecidas
pela STL. Tais novas estruturas contemplam vetores (PONVECTOR), listas (PONLIST)
e tabelas hash (PONHASH) [Ronszcka 2012,Valen¸ca 2013] . Esta vers˜ao do Framework
apresentou ganhos signiﬁcativos de desempenho em diversas aplica¸c˜oes quando comparado
`a sua vers˜ao 1.0 [Valen¸ca 2013].
Conforme ilustrado na Figura 13, o Framework PON 2.0 ´e subdividido em trˆes
pacotes principais.
O pacote Application possui apenas a classe Application, a qual
relaciona uma aplica¸c˜ao PON `as demais classes que comp˜oem o Framework. O pacote
Scheduler, por sua vez, possui as classes que materializam as estrat´egias de resolu¸c˜ao de
conﬂitos, conforme descrito na Subse¸c˜ao 2.2.3. Por ﬁm, o pacote Core ´e formado pelas
classes que materializam as entidades colaborativas do PON, conforme apresentado na
Figura 14.
Figura 13: Estrutura do Framework PON [Linhares et al. 2011]
.
Conforme apresentado na Figura 14, as classes Rule e FBE se apresentam nas
extremidades opostas do diagrama de classes e se relacionam atrav´es de classes ditas
colaborativas, isto ´e Attribute, Premise, Condition, Action, Instigation e Method. Em


52
tempo, ´e a colabora¸c˜ao entre as instˆancias destas classes que determina o ﬂuxo de execu¸c˜ao
da aplica¸c˜ao PON.
Figura 14: Diagrama de Classes do pacote Core [Linhares et al. 2011]
.
Ainda, o pacote Core ´e composto pelo subpacotes Attributes e Conditions. Con-
forme apresentado na Figura 15, o subpacote Attributes ´e composto pelas classes que
encapsulam os tipos primitivos do POO (nomeadamente Boolean, Char, Double, Integer e
String), introduzindo aos tipos primitivos reatividades de forma a permitir que estes fa¸cam
parte da estrutura de notiﬁca¸c˜oes do PON. O subpacote Conditions, por sua vez, ´e com-
posto pelas diferentes opera¸c˜oes l´ogicas previstas (nomeadamente Conjuction, Disjunction
e Single) que comp˜oe a deﬁni¸c˜ao de uma Condition no PON.
Para desenvolver aplica¸c˜oes utilizando o Framework PON, inicialmente ´e necess´ario
a cria¸c˜ao de uma classe principal a qual estenda a classe NOPApplication. Conforme
apresentado na Figura 16, a classe NOPApplication apresenta m´etodos abstratos, os quais
constituem uma ponte entre a aplica¸c˜ao PON e o cerne do Framework.
A cria¸c˜ao de entidades PON via Framework ´e dada pelo uso de uma f´abrica de
entidades, a qual possui como responsabilidade principal instanciar tais entidades adaptadas


53
Figura 15: Diagrama de Classes dos subpacotes Attributes e Conditions [Linhares et al.
2011]
.
a uma estrutura de dados espec´ıﬁca [Ronszcka 2012]. O C´odigo 3 demonstra a inicializa¸c˜ao
dos componentes iniciais de uma aplica¸c˜ao PON, em especial a classe SingleFactory (linha
2), a qual ´e respons´avel pela instancia¸c˜ao das entidades PON. As poss´ıveis f´abricas a serem
utilizadas na cria¸c˜ao de entidades PON s˜ao NOP LIST, NOP VECTOR, NOP HASH e
STL LIST.
C´odigo 3: Inicializa¸c˜ao dos componentes iniciais de uma aplica¸c˜ao PON
1 void Main::initStartApplicationComponents() {
2
SingletonFactory::changeStructure(SingletonFactory::NOPVECTOR);
3
SingletonLog::changeStream(SingletonLog::CONSOLE);
4
SingletonScheduler::changeScheduler(SchedulerStrategy::NO ONE);
5
this->startApplication();
6 }


54
Figura 16: Diagrama de classes do procedimento inicial de uma aplica¸c˜ao PON [Ronszcka
2012]
.
Ademais, no C´odigo 3 ´e mostrado que o m´etodo initStartApplicationComponents
pode ser utilizado para inicializar o gerador de logs (linha 3), deﬁnir a estrat´egia de
resolu¸c˜ao de conﬂito de Rules (linha 4) e, por ﬁm, o m´etodo startApplication deve ser
invocado. Em tempo, o m´etodo startApplication ´e respons´avel por chamar ordenadamente
os m´etodos de cria¸c˜ao de uma aplica¸c˜ao PON, conforme apresentado pelo C´odigo 4.
C´odigo 4: Implementa¸c˜ao do m´etodo startApplication
1 void NOPApplication::startApplication() {
2
initFactBase();
3
initSharedEntities();
4
initRules();
5
codeApplication();
6 }
A composi¸c˜ao de entidades de FBEs no Framework PON se d´a por meio da
cria¸c˜ao e instancia¸c˜ao de classes de FBEs. As classes que representam os modelos para
cria¸c˜ao de entidades FBEs pertinentes `a aplica¸c˜ao podem conter Attributes e Methods.
De acordo com a sequˆencia de cria¸c˜ao de aplica¸c˜oes, o pr´oximo m´etodo herdado da
classe NOPApplication a ser implementado ´e o m´etodo initFactBase. Conforme apresetando
no C´odigo 5, nas linhas 2 e 3 s˜ao criadas duas instˆancias de FBEs do tipo Robot.


55
C´odigo 5: Implementa¸c˜ao do m´etodo initFactBase
1 void Main::initFactBase() {
2
robot1 = new Robot();
3
robot2 = new Robot();
4 }
A composi¸c˜ao de Rules, por sua vez, deﬁne o ﬂuxo de execu¸c˜ao de uma aplica¸c˜ao
PON, uma vez que s˜ao as Rules que deﬁnem o relacionamento entre as diferentes entidades
PON que comp˜oem a aplica¸c˜ao. Conforme apresentado no C´odigo 6, a conﬁgura¸c˜ao das
Rules se d´a atrav´es da implementa¸c˜ao do m´etodo initRules. A Rule descrita no C´odigo 6
foi apresentada na Subse¸c˜ao 1.1.2 e tem por objetivo controlar a movimenta¸c˜ao de um
robˆo em uma partida de futebol de robˆos.
C´odigo 6: Implementa¸c˜ao do m´etodo initFactBase
1 void Main::initRules() {
2
Scheduler * scheduler = SingletonScheduler::getInstance();
3
RULE (rlRule1,scheduler,Condition::CONJUNCTION);
4
rlRule1->addPremise(prIsOn);
5
rlRule1->addPremise(prBallNotMoving);
6
rlRule1->addPremise(prGameStop);
7
rlRule1->addInstigation(inMoveRobot);
8
rlRule1->end();
9 }
Conforme apresentado no C´odigo 6, uma Rule ´e criada a partir de trˆes argumentos:
o objeto do tipo RuleObject (rlRule1), o qual representa a Rule que est´a sendo criada, a
referˆencia ao Scheduler inicializado e conﬁgurado no m´etodo initStartApplicationCom-
ponents (scheduler) e o tipo de opera¸c˜ao l´ogica desejado (Condition::CONJUNCTION ).
Entre as linhas 4 e 6, observa-se a associa¸c˜ao de entidades Premises `a entidade Rule. Por
ﬁm, na linha 7 ´e poss´ıvel observar a adi¸c˜ao de uma Instigation a Rule.


56
2.3.2
LINGUAGEM E COMPILADOR PARA O PON - LINGPON 1.0
A Linguagem e Compilador para o PON surgiram como resultado de esfor¸cos da
disciplina “Linguagens e Compiladores” 3 ofertada pela UTFPR em 2013 e ministrada por
Prof. Dr. Jo˜ao Alberto Fabro e Prof. Dr. Jean Marcelo Sim˜ao.
Em suma, a vers˜ao prototipal desenvolvida na disciplina foi uma primeira demons-
tra¸c˜ao sobre a viabilidade de se desenvolver uma linguagem e compilador para o PON.
Neste contexto, a gram´atica que deﬁne a linguagem de programa¸c˜ao PON, doravante de-
nominada LingPON 1.0, foi especiﬁcada segundo a Backus-Naur Form (BNF) apresentada
no Anexo A deste trabalho. Em tempo, n˜ao raro e conforme o contexto, o termo LingPON
se refere n˜ao s´o a Linguagem mas tamb´em a tecnologia de compila¸c˜ao pertinente. Em
tempo, na disserta¸c˜ao de C. A. Ferreira esta vers˜ao prototipal de linguagem e compilador
foi evolu´ıda, atingindo a vers˜ao dita LingPON 1.0. Isto considerado, a subse¸c˜ao 2.3.2.1
apresenta a linguagem de programa¸c˜ao PON e a subse¸c˜ao 2.3.2.2 apresenta o compilador
PON.
2.3.2.1
LINGUAGEM DE PROGRAMAC¸ ˜AO PON
De modo geral, o c´odigo fonte de uma aplica¸c˜ao desenvolvida utilizando a LingPON
segue um padr˜ao de declara¸c˜oes, conforme apresentado pelo C´odigo 7.
3Disciplina: T´opicos Avan¸cados Em Engenharia De Software. Tema: LINGUAGENS E COMPILA-
DORES. C´odigo CAES101. Programa PPGCA/UTFPR - Prof Jo˜ao Alberto Fabro (em colabora¸c˜ao com
Prof. Jean Marcelo Sim˜ao - CPGEI/UTFPR). 2 Trimestre de 2013.


57
C´odigo 7: Padr˜ao de declara¸c˜oes da linguagem PON
1 fbe Robot
2
. . .
3 end fbe
4
5 fbe Ball
6
. . .
7 end fbe
8
9 inst
10
. . .
11 end inst
12
13 strategy
14
. . .
15 end strategy
16
17 rule rlKickBall
18
. . .
19 end rule
20
21 main {
22
. . .
23 }
Primeiramente, o desenvolvedor precisa deﬁnir os FBEs de seu programa. Em
seguida, o desenvolvedor precisa declarar as instˆancias de tais FBEs, bem como deﬁnir a
estrat´egia de escalonamento das Rules. Subsequentemente, as Rules devem ser deﬁnidas
para ﬁns de avalia¸c˜ao l´ogico causal dos estados das instˆancias de FBEs por meio de
notiﬁca¸c˜oes. Por ﬁm, ´e poss´ıvel adicionar c´odigo espec´ıﬁco da linguagem alvo escolhida no
processo de compila¸c˜ao (e.g C ou C++) com a utiliza¸c˜ao do bloco de c´odigo main [Ferreira
2016].
Na gram´atica do PON, a palavra reservada fbe anuncia o in´ıcio da estrutura de
um FBE. Por padr˜ao, todos os FBEs devem ser deﬁnidos no primeiro bloco de c´odigo.


58
Na sequˆencia, as instˆancias dos FBEs devem ser declaradas dentro do bloco de c´odigo
iniciado pela palavra reservada inst. Em seguida, a estrat´egia de escalonamento das Rules
deve ser declarada utilizando-se a palavra reservada strategy. Ainda, as Rules devem
ser deﬁnidas fazendo uso da palavra reservada rule. Finalmente, a ´ultima estrutura a
ser declarada ´e o bloco de c´odigo main, o qual possibilita a inser¸c˜ao de c´odigo nativo na
linguagem alvo escolhida durante o per´ıodo de compila¸c˜ao (i.e C ou C++).
O in´ıcio do c´odigo fonte em LingPON ´e caracterizado pela declara¸c˜ao dos FBEs.
Conforme apresentado no C´odigo 8, um FBE ´e composto por dois blocos de c´odigo. O
primeiro bloco representa a declara¸c˜ao dos Attributes, a qual ´e feita utilizando-se a palavra
reservada attributes. O segundo representa a declara¸c˜ao dos Methods, a qual faz uso da
palavra reservada methods.
C´odigo 8: Exemplo de declara¸c˜ao de FBEs no LingPON
1 fbe Robot
2
attributes
3
boolean atConnected false
4
boolean atSetKick false
5
ﬂoat atSpeed 0.0
6
integer atPosX 0
7
integer atPosY 0
8
end attributes
9
methods
10
method mtKickBall (atSetKick = true)
11
method mtMoveForward (atPositionX = atPositionX + 1)
12
method mtSendCommand begin method ... end method
13
end methods
14 end fbe
A declara¸c˜ao dos Attributes na LingPON segue uma estrutura comumente utilizada
pelas atuais linguagens de programa¸c˜ao (e.g. linguagem Java do PI ), formada pelo tipo
do Attribute, seguido do seu nome e seu respectivo valor inicial. Neste ˆambito, os tipos
de dados suportados pela atual vers˜ao da linguagem s˜ao boolean, integer, ﬂoat, char e
string [Ferreira 2016].


59
Por conven¸c˜ao, mas n˜ao obrigatoriamente, os nomes dos Attributes seguem um
padr˜ao de nomenclatura, conforme apresentado em outros trabalhos do PON [Ronszcka
2012,Valen¸ca 2013], fazendo usdo do preﬁxo at, seguido de um mnemˆonico que deﬁne o
prop´osito do Attribute em quest˜ao. Por ﬁm, o valor inicial deve estar de acordo com o
tipo de dados empregado na constru¸c˜ao de tal Attribute.
Os Methods, por sua vez, apresentam uma constru¸c˜ao particular em sua estrutura.
Esta se d´a pelo an´uncio da abertura de um Method atrav´es da palavra reservada method
seguida do nome e sua respectiva funcionalidade. Assim como os Attributes, os Methods
tamb´em devem, por boas pr´aticas, seguir um padr˜ao de nomenclaturas, utilizando-se
o preﬁxo mt. Neste ˆambito, o C´odigo 8, entre as linhas 9 e 11 apresenta as poss´ıveis
estruturas de constru¸c˜ao v´alidas para os Methods na linguagem PON.
Na linha 8 do C´odigo 8, a funcionalidade do Method mtKickBall est´a entre
parˆenteses. Basicamente tal funcionalidade altera o valor do Attribute atHasKicked para
true. Por sua vez, o m´etodo mtMoveForward, linha 9, apresenta a possibilidade de atribui¸c˜ao
de uma opera¸c˜ao (e.g soma) em um Attribute. Finalmente, o Method mtSendCommand,
na linha 10, possibilita o desenvolvedor adicionar c´odigo nativo da linguagem alvo do
compilador, tal como enviar um comando via socket, ao bloco de c´odigo do m´etodo entre
as palavras reservadas begin method e end method .
O segundo bloco de c´odigo em um programa PON consiste na instancia¸c˜ao dos
FBEs deﬁnidos no primeiro bloco. Para isso, o C´odigo 9 apresenta como tais instancia¸c˜oes
devem ser declaradas. No C´odigo 9 ´e poss´ıvel observar nas linhas 2 e 3 que duas instˆancias
do FBEs Robot s˜ao criadas.
C´odigo 9: Exemplo de instancia¸c˜oes de FBEs
1 inst
2
Robot robot1
3
Robot robot2
4 end inst
O terceiro bloco de c´odigo consiste na deﬁni¸c˜ao da estrat´egia de resolu¸c˜ao de
conﬂitos a ser utilizada. Conforme apresentado e explicado na Subse¸c˜ao 2.2.2, o PON
apresenta trˆes estrat´egias de resolu¸c˜ao de conﬂitos (NO ONE, BREATH e DEPTH ). O
C´odigo 10 apresenta o padr˜ao de implementa¸c˜ao sugerido para adicionar a estrat´egia de


60
resolu¸c˜ao de conﬂitos NO ONE no c´odigo fonte em LingPON.
C´odigo 10: Exemplo de deﬁni¸c˜ao de estrat´egia de escalonamento
1 strategy
2
no one
3 end strategy
O quarto bloco de c´odigo consiste na cria¸c˜ao do conhecimento l´ogico-causal da
aplica¸c˜ao atrav´es da deﬁni¸c˜ao das Rules. O C´odigo 11 apresenta o padr˜ao de implementa¸c˜ao
para a cria¸c˜ao de uma Rule.
C´odigo 11: Exemplo de cria¸c˜ao de Rules
1 rule rlKickBallRobot1
2
condition
3
subcondition A1
4
premise prIsRobotStop robot1.atSpeed == 0.0 and
5
premise prIsPositioned robot1.atSetKick == true
6
end subcondition
7
end condition
8
action
9
instigation inKickBall robot1.mtKickBall();
10
end action
11 end rule
A deﬁni¸c˜ao de uma Rule ´e anunciada pela palavra reservada rule seguida de um
identiﬁcador para a mesma. ´E importante ressaltar que o identiﬁcador da Rule nesse
ponto ´e obrigat´orio, n˜ao podendo ser omitido.
Basicamente, cada Rule ´e composta por trˆes blocos, que s˜ao as suas Properties, a
Condition (express˜ao l´ogica) e Action (execu¸c˜ao), sendo que o bloco Properties ´e opcional.
O C´odigo 12 apresenta um exemplo de c´odigo que pode ser utilizado no bloco Properties
de uma Rule. O bloco Properties de uma Rule pode ser composto por duas propriedades:
Priority e Keeper.


61
C´odigo 12: Propriedades das Rules
1 properties
2
priority 1
3
keeper true
4 end properties
A propriedade priority deﬁne uma ordem de prioridade e consequente execu¸c˜ao de
Rules quando duas ou mais Rules compartilham o mesmo Exclusive Attribute (cf. Subse¸c˜ao
2.2.3) em alguma de suas Premises. Portanto, a Rule que apresentar a maior prioridade
ter´a sua execu¸c˜ao priorizada frente as demais Rules.
Na atual vers˜ao da LingPON, ´e obrigat´oria a utiliza¸c˜ao de SubConditions, seguidas
de um identiﬁcador, mesmo quando se trata de express˜oes com apenas uma Premisse.
Como exemplo de tal constru¸c˜ao, tem-se a linha 3 do C´odigo 11. Seguindo o estado da arte
do PON, a constru¸c˜ao de uma SubCondition necessita de, ao menos, uma Premise. No caso
da utiliza¸c˜ao de mais de uma Premise, estas devem estar conectadas por conjun¸c˜oes (and).
Para utiliza¸c˜ao de disjun¸c˜oes (or), ´e necess´ario a cria¸c˜ao de duas ou mais SubConditions
na Rule.
Para a deﬁni¸c˜ao de Premises no LingPON, a palavra reservada premise deve ser
utilizada seguida de um identiﬁcador (opcional) e uma avalia¸c˜ao l´ogica. Ainda, `a uma
Premise pode ser aplicada uma propriedade inerente dos padr˜oes de execu¸c˜ao do PON,
conhecida como Attribute Impertinente (cf. Subse¸c˜ao 2.2.6). Para tal, basta adicionar a
palavra reservada imp ap´os o identiﬁcador da Premise, conforme apresentado no C´odigo
13.
C´odigo 13: Deﬁni¸c˜ao de uma Premise com Attribute impertinente
1
premise prIsConnected imp robot1.atIsConnected == true
A compara¸c˜ao em uma Premise ´e composta por trˆes elementos: o valor de um
Attribute vinculado a uma instˆancia de um FBE, o operador de compara¸c˜ao (e.g ==) e
o valor a ser comparado (e.g true). Este ´ultimo pode ser tanto uma constante quanto o
valor de um outro Attribute. Os operadores de compara¸c˜ao suportados pela atual vers˜ao


62
da LingPON s˜ao: “==”,“<”,“>”,“<=”,“>=”,“!=”.
O ´ultimo bloco de c´odigo deﬁnido em uma Rule representa sua execu¸c˜ao e ´e
anunciada a partir da palavra reservada action.
Este bloco consiste no v´ınculo de
instiga¸c˜oes a Methods deﬁnidos pelas FBEs. Conforme apresentado na linha 9 do C´odigo
11, a estrutura das Instigations ´e composta pela palavra reservada instigation seguida de
um identiﬁcador (opcional) e um Method de uma instˆancia particular de um FBE. Dessa
forma, cada Instigation est´a relacionada a execu¸c˜ao de um ´unico Method [Ferreira 2016].
Outrossim, o conjunto de padr˜oes de nomenclaturas prevˆe, mas n˜ao obriga, os
seguintes preﬁxos para as entidades PON apresentadas nessa etapa: rl para Rules, cd
para Conditions, sc para SubConditions pr para Premises, ac para Actions e in para
Instigations.
Finalmente, o ´ultimo bloco de c´odigo consiste na cria¸c˜ao do bloco de c´odigo
principal (main). Este bloco de c´odigo permite ao desenvolvedor adicionar c´odigo espec´ıﬁco
para a linguagem alvo deﬁnida, conforme ´e apresentado no C´odigo 14. ´E importante
ressaltar que o c´odigo inserido dentro do bloco main n˜ao ´e avaliado pelas regras de
compila¸c˜ao da LingPON 1.0 [Ferreira et al. 2013].
C´odigo 14: Exemplo de deﬁni¸c˜ao do bloco main
1 main {
2
// C´odigo espec´ıﬁco em C++
3
robot1->setatConnected(true);
4
robot2->setatConnected(true);
5 }
Aliado `a LingPON existe um compilador, o qual ´e objeto da pr´oxima subse¸c˜ao.
Em tempo, n˜ao raro a LingPON em si e seu compilador s˜ao chamados apenas de LingPON
ou de tecnologia LingPON. Assim, na pr´atica, o contexto que determinaria se est´a se
referindo apenas a linguagem de programa¸c˜ao em si ou se a ela e ao seu compilador.
2.3.2.2
COMPILADOR PARA O PON
Um compilador pode ser compreendido como um programa tradutor, o qual
transforma uma linguagem fonte escrita em uma linguagem objeto [Aho et al. 1995].
Para isso, um compilador ´e constitu´ıdo de fases que operam em sequˆencia, nomeadamente
an´alise l´exica, an´alise sint´atica, an´alise semˆantica, otimiza¸c˜ao de c´odigo e gera¸c˜ao de c´odigo.


63
O diagrama de atividades da Figura 17 apresenta as etapas existentes no compilador PON
desenvolvida na LingPON 1.0. Cada etapa possui um objetivo espec´ıﬁco e o resultado da
fase precedente ´e utilizado pela fase posterior.
Figura 17: Diagrama de atividades UML do compilador PON.
Por se tratar da primeira fase de um compilador, o principal objetivo de um
analisador l´exico ´e ler os caracteres do c´odigo fonte, agrup´a-los em tokens e produzir como
sa´ıda uma sequˆencia de tokens, sendo um para cada palavra ou s´ımbolo encontrado no
c´odigo fonte.
No caso do compilador PON, o analisar l´exico foi gerado utilizando a ferramenta
Flex/Lex [Grune et al. 2012]. A entrada do programa Flex/Lex ´e um arquivo contendo
express˜oes regulares que deﬁnem os poss´ıveis tokens de uma linguagem. Deste modo, a
ferramenta Flex/Lex produz um m´odulo de software que pode ser compilado e acoplado
ao m´odulo de an´alise sint´atica [Ferreira 2016].
A pr´oxima fase no processo de compila¸c˜ao ´e a an´alise sint´atica. Um analisador
sint´atico ´e compreendido como um programa computacional que determina se um c´odigo
fonte est´a sintaticamente correto. Esta an´alise veriﬁca se os tokens identiﬁcados pela
an´alise l´exica est˜ao encadeados corretamente de acordo com a especiﬁca¸c˜ao gramatical
da linguagem. Por ﬁm, o analisador sint´atico agrupa os tokens em frases gramaticais que


64
ser˜ao usadas para sintetizar a sa´ıda.
Por sua vez, a fase de an´alise semˆantica veriﬁca as frases gramaticas formadas pelo
analisador sint´atico a ﬁm de detectar poss´ıveis erros semˆanticos. Diferentemente da an´alise
sint´atica, a qual veriﬁca se a estrutura da frase gramatical est´a correta, a an´alise semˆantica
ir´a veriﬁcar sua signiﬁcˆancia. Como exemplo, o analisador semˆantico valida se um valor
do tipo inteiro est´a sendo atribu´ıdo `a uma vari´avel do tipo inteiro. Em contrapartida, a
an´alise sint´atica valida sua estrutura gramatical, ou seja, se os s´ımbolos est˜ao encadeados
na ordem correta, de acordo com a especiﬁca¸c˜ao sint´atica da linguagem [Ferreira 2016]. A
Figura 18 ilustra um fragmento de c´odigo no qual ´e poss´ıvel perceber a diferen¸ca entre
an´alise semˆantica e a an´alise sint´atica.
Figura 18: Exemplo de an´alise semˆantica [Ferreira 2016]
Os m´odulo de an´alise sint´atica e an´alise semˆantica foram gerados utilizando a
ferramenta Bison [Grune et al. 2012]. O Bison ´e uma ferramenta que, baseado em
uma gram´atica, constr´oi um programa em C/C++ que analisa uma sequˆencia de tokens
provenientes de um arquivo de c´odigo-fonte segundo as regras gramaticais.
A etapa de otimiza¸c˜ao de c´odigo ´e uma etapa usualmente presente no processo de
compila¸c˜ao. Esta etapa tenta melhorar o c´odigo intermedi´ario, de tal forma que venha
resultar um c´odigo de m´aquina mais r´apido em tempo de execu¸c˜ao [Aho et al. 1995].
Entretanto, o compilador PON ainda n˜ao possui a etapa de otimiza¸c˜ao durante o seu
processo de compila¸c˜ao.
Finalmente, a etapa de gera¸c˜ao de c´odigo utiliza as informa¸c˜oes interpretadas e
validadas pelas etapas precedentes com o intuito de gerar c´odigo alvo. Por n˜ao existir uma
ferramenta gen´erica para gera¸c˜ao de c´odigo, um gerador de c´odigo espec´ıﬁco para o PON
foi desenvolvido em [Ferreira 2016]. O m´odulo de gera¸c˜ao de c´odigo desenvolvido ´e capaz
de gerar c´odigo C, C++ e Framework PON C++ 2.0 a partir do c´odigo-fonte LingPON.
De forma a abstrair as entidades PON durante o processo de compila¸c˜ao, algumas
classes C++ foram criadas para armazenar as informa¸c˜oes pertinentes a cada entidade


65
PON, conforme apresentado na Figura 19
Figura 19: Diagrama de classes utilizada pelo compilador PON para representar entidades
PON [Ferreira 2016].
Ao analisar um fragmento do c´odigo fonte, o m´odulo de an´alise sint´atica interage
com a instˆancia da classe Compiler. A classe Compiler ´e uma classe utilit´aria que foi
criada com o objetivo de manipular, por meio de sua instˆancia, a cria¸c˜ao dos objetos que
representam as entidades PON durante o processo de compila¸c˜ao.
Ap´os a cria¸c˜ao de um novo objeto, o Compiler o adiciona em uma estrutura de
dados chamada tabela de s´ımbolos, a qual ´e posteriormente utilizada para gera¸c˜ao do
c´odigo alvo. Atualmente, o compilador PON suporta a gera¸c˜ao de c´odigo em C, C++
e Framework. Para maiores detalhes sobre a arquitetura da LingPON e seu respectivo
compilador, sugere-se a leitura de [Ferreira 2016].
Em tempo, novas funcionalidades foram adicionadas `a linguagem de programa¸c˜ao
PON durante a disciplina de “Linguagens e Compiladores”4 ofertada pela UTFPR em
2015 e ministrada por Prof. Dr. Jo˜ao Alberto Fabro e Prof. Dr. Jean Marcelo Sim˜ao. As
4Disciplina: T´opicos Avan¸cados Em Engenharia De Software. Tema: LINGUAGENS E COMPILA-
DORES. C´odigo CAES101. Programa PPGCA/UTFPR - Prof. Jo˜ao Alberto Fabro e Prof. Jean Marcelo
Sim˜ao. 3 Trimestre de 2016.


66
funcionalidades adicionadas a LingPON foram suporte a regras de forma¸c˜ao, compila¸c˜ao
para Notiﬁcation Oriented Computer Architecture [Linhares et al. 2015], compila¸c˜ao para
VHDL e uma nova vers˜ao do gerador de c´odigo C++, no qual ´e poss´ıvel gerar c´odigo
est´atico (static classes).
2.3.3
OUTRAS MATERIALIZAC¸ ˜OES EM SOFTWARE DO PON
As materializa¸c˜oes chamadas Framework PON 2.0 e LingPON 1.0 foram aqui deta-
lhadas porque s˜ao objeto de estudo comparativo no ˆambito dessa disserta¸c˜ao. Elas s˜ao ob-
jeto de estudo por serem as materializa¸c˜oes mais est´aveis no tocante a arqu´etipo/framework
e linguagem-compilador para o PON, bem como por terem sido j´a comparadas para com o
POO/PI ainda que em aplica¸c˜oes de envergadura assaz t´ımidas em geral. Isto conside-
rado, apenas a t´ıtulo de elucida¸c˜ao, ´e pertinente salientar que h´a outras materializa¸c˜oes
prototipais.
O Framework prototipal PON em C++ foi adaptado por Weber para trabalhar com
multi-threads de maneira bem prototipal tamb´em [Weber et al. 2010]. Subsequentemente,
Belmonte adaptou o Framework PON 2.0 em C++ para trabalhar com Threads, aplicando-
o para Multi-core a ﬁm de demonstrar a capacidade multi-processada do PON j´a obtendo
resultados positivos [Weber et al. 2010,Belmonte et al. 2016]. Ainda, Viana Melo adaptou
o Framework PON 2.0 em C++ para trabalhar com aplica¸c˜oes Fuzzy o que se demonstrou
funcional e ´util [Melo et al. 2013]. Por ﬁm, Schutz adaptou o Framework PON 2.0 em C++
para trabalhar com Redes Neurais o que se demonstrou pertinente sendo uma pesquisa
em andamento [Sch¨utz et al. 2015]. Ainda que interessante, esses Frameworks prototipais
fogem do escopo deste trabalho que n˜ao trata de multi-thread/processamento-paralelo,
fuzzy e redes neurais. Em todo caso, as aplica¸c˜oes ali desenvolvidas n˜ao tem a mesma
envergadura em termos de n´umeros Rules e FBES que a considerada neste presente
trabalho.
Al´em das adapta¸c˜oes dos Frameworks em C++, houve o desenvolvimento em
disciplina stricto senso sobre o PON, em 2015 5, de Framework em linguagem Java e C#.
O Framework em Java foi uma adapta¸c˜ao do primeiro Framework em C++ sendo que, n˜ao
obstante, em resultados preliminares o resultados dele se assemelharam ao do Framework
C++ 2.0. O primeiro Framework C# segue o mesmo quadro e resultados do Framework
5Disciplina: - T´opicos Avan¸cados Em Sistemas Embarcados. Tema: Paradigma Orientado a Notiﬁca¸c˜oe.
C´odigo CASE102 . Programa PPGCA/UTFPR - Prof. Prof. Jean Marcelo Sim˜ao. 1 Trimestre de 2015.
& Disciplina: - T´opicos Especiais Em EC: Paradigma Orientado a Notiﬁca¸c˜oes. Tema: LINGUAGENS E
COMPILADORES. C´odigo PGEID/PGEIM. Programa. CPGEI/UTFPR - Prof. Prof. Jean Marcelo
Sim˜ao. 1 Trimestre de 2015.


67
Java. Entretanto, al´em dos resultados serem preliminares n˜ao houve compara¸c˜oes para
com POO/PI. Em Mendon¸ca, h´a o relato de uma aplica¸c˜ao PON feita neste Framework
Java mas sem compara¸c˜oes com POO/PI [Mendon¸ca 2016]. Ainda, na edi¸c˜ao de 20166, foi
desenvolvido uma evolu¸c˜ao do Framework C#, o qual foi usado em aplica¸c˜ao h´ıbrida com
POO para simula¸c˜ao de ambiente IOT 7.
Tal qual o Framework, a LingPON tamb´em j´a tem deriva¸c˜oes. Entretanto, estas
deriva¸c˜oes encontram-se em est´agio prototipal, sem terem sido objetos de experimenta¸c˜oes
maiores e de bancas avaliadoras no ˆambito de mestrado ou aﬁns. Neste ˆambito, na edi¸c˜ao
2015 da disciplina de “Linguagens e Compiladores” dos Profs. J. A. Fabro e J. M. Sim˜ao,
a LingPON 1.0 teve funcionalidades adicionadas. Tais funcionalidade s˜ao suporte a regras
de forma¸c˜ao, compila¸c˜ao para Notiﬁcation Oriented Computer Architecture (NOCA ou
ArqPON) e compila¸c˜ao para VHDL.
Ainda, na edi¸c˜ao 2015 da disciplina de “Linguagens e Compiladores” dos Profs.
J. A. Fabro e J. M. Sim˜ao surgiu uma nova vers˜ao do gerador de c´odigo C++, no qual
´e poss´ıvel gerar c´odigo est´atico (static classes). Ainda que o c´odigo gerado pare¸ca ser,
nos resultados preliminares, mais r´apido que o c´odigo gerado C++ e C pela tecnologia
LingPON 1.0, ele ainda ´e prototipal e apresenta diﬁculdades maiores para conectar com
c´odigo n˜ao est´atico, o que ´e problem´atico como no caso de aplica¸c˜oes de robˆos. Por ﬁm, na
edi¸c˜ao 2016 da disciplina de “Linguagens e Compiladores” dos Profs. J. A. Fabro e J. M.
Sim˜ao, surge uma nova vers˜ao baseada em c´odigo orientados a namespace em C++ que
seria mais r´apida que as precedentes e sem problemas maiores de integra¸c˜ao, entretanto
isso ´e muito recente e largamente prototipal.
2.4
FUTEBOL DE ROBˆOS - ROBOCUP
A RoboCup ´e uma iniciativa internacional e interdisciplinar que visa promover
a pesquisa e desenvolvimento no campo da rob´otica, provendo tarefas comuns para a
avalia¸c˜ao de diferentes teorias, C´odigos e arquiteturas de robˆos. Como tarefa comum,
a RoboCup escolheu o futebol. Isto porque, para que um robˆo possa participar de uma
partida de futebol, muitas tecnologias precisam ser integradas e uma s´erie de avan¸cos
t´ecnicos precisam ser alcan¸cados, tais como mecˆanica de precis˜ao, controle eletrˆonico e
programa¸c˜ao distribu´ıda [Yoon 2015,Marling et al. 2003,Asada et al. 1998,Asada et al.
1999].
6Disciplina: - T´opicos Avan¸cados Em Sistemas Embarcados. Tema: Paradigma Orientado a Notiﬁca¸c˜oes.
C´odigo CASE102 . Programa PPGCA/UTFPR - Prof. Prof. Jean Marcelo Sim˜ao. 1 Trimestre de 2016.
7Vide http://www.dainf.ct.utfpr.edu.br/ jeansimao/PON/PON.htm


68
Atualmente, a RoboCup est´a dividida em cinco categorias, sendo que cada uma
possui seus pr´oprios desaﬁos a serem superados: Small Size League (SSL), Middle Size
League (MSL), Simulation League, Standard Platform League e Humanoid League. Esse
trabalho focar´a apenas na categoria SSL, a qual tem como principal objeto de estudo o
desenvolvimento de sistemas inteligentes capazes de controlar robˆos em ambientes altamente
dinˆamicos utilizando sistemas de controle h´ıbridos (centralizado/distribu´ıdo) [Yoon 2015].
Na categoria RoboCup SSL, cada time ´e composto por no m´aximo seis robˆos que
disputam a partida de futebol utilizando uma bola de golfe alaranjada em um campo,
cujas dimens˜oes s˜ao apresentadas na Figura 20. O robˆo apresenta um formato cil´ındrico,
com 180 mm de diˆametro e 150 mm de altura e possui um marcador central, que pode ser
amarelo ou azul, e marcadores diversos que identiﬁcam cada jogador de cada time.
As atividades durante a partida s˜ao capturadas por duas cˆameras posicionadas
acima do campo de jogo. As imagens ent˜ao s˜ao processadas pelo SSL-Vision, um software
executado em computador externo, de forma a identiﬁcar informa¸c˜oes importantes sobre a
partida, tais como posi¸c˜ao de cada um dos robˆos e da bola.
Figura 20: Dimens˜oes do campo oﬁcial da categoria SSL, em mil´ımetros.
Utilizando as informa¸c˜oes j´a processadas pelo SSL-Vision, um computador inde-
pendente deve produzir as estrat´egias para as a¸c˜oes dos robˆos e enviar comandos para
cada um dos robˆos atrav´es de uma conex˜ao sem ﬁo (wireless). O robˆo ent˜ao processa o
comando recebido e atua no ambiente, alterando o seu estado no campo de jogo. Tais
mudan¸cas ser˜ao capturadas pelas cˆameras e todo o processo de controle se repete ao longo
de toda a partida. A Figura 21 apresenta conﬁgura¸c˜ao de um ambiente RoboCup SSL.


69
Figura 21: Sistema RoboCup SSL [Yoon 2015]
Como apresentado na Figura 21, o sistema de controle dos robˆos na SSL ´e
centralizado. Os robˆos n˜ao possuem nenhuma estrat´egia ou capacidade para deliberar
sobre qual a¸c˜ao deve ser executada. Eles simplesmente processam comandos recebidos a
partir de uma unidade de controle onisciente e centralizada [Yoon 2015]
2.4.1
AMBIENTE SIMULADO ROBOCUP SSL
Visando permitir o desenvolvimento do software sem depender de robˆos reais, um
simulador do ambiente de competi¸c˜ao da RoboCup pode ser utilizado. Esse ambiente ´e
disponibilizado por pesquisadores que contribuem para a competi¸c˜ao, sendo extensivamente
utilizado por toda a comunidade, livremente, para suas pesquisas e desenvolvimento. Este
ambiente ´e composto por duas aplica¸c˜oes: grSim Simulator 8 e Referee Box 9.
O grSim Simulator ´e um simulador funcional do ambiente de jogo Robocup, cuja
interface ´e apresentada na Figura 22. Os robˆos simulados possuem caracter´ısticas muito
pr´oximas `as reais, tais como dimens˜oes, velocidade m´axima, in´ercia e acelera¸c˜ao. Al´em
disso, essa aplica¸c˜ao ´e respons´avel pelo envio de informa¸c˜oes relativas aos objetos em
campo seguindo o protocolo padr˜ao do sistema de vis˜ao, SSL-Vision [Monajjemi et al.
2011].
8Dispon´ıvel em http://www.parsianrobotic.ir/grsim/
9Dispon´ıvel em http://robocupssl.cpe.ku.ac.th/referee:start


70
Figura 22: Interface gr´aﬁca da aplica¸c˜ao grSim Simulator.
A aplica¸c˜ao que ir´a controlar os robˆos lˆe os dados referentes a cada um deles,
os processa e envia comandos espec´ıﬁcos `a cada um dos robˆos ao grSim Simulator, que
ir´a execut´a-los, atualizar as a¸c˜oes usando a f´ısica simulada e obter as novas percep¸c˜oes
do ambiente. Portanto, o grSim Simulator n˜ao possui l´ogica alguma de controle, apenas
executa comandos recebidos e disponibiliza, atrav´es de uma interface de rede, informa¸c˜oes
sobre o estado atual do ambiente de jogo `a quem interessar. Al´em disso, atrav´es de sua
interface gr´aﬁca, ´e poss´ıvel acompanhar em tempo real informa¸c˜oes espec´ıﬁcas de cada um
dos robˆos, tais como sua posi¸c˜ao e velocidade atual.
A aplica¸c˜ao Referee Box, por sua vez, ´e um programa simples que permite a um
operador neutro enviar ordens proferidas pelo ´arbitro diretamente ao software das equipes
competidoras. Al´em de enviar os comandos referentes a ordens do ´arbitro, a Referee Box
tamb´em atua como um utilit´ario auxiliar para o ´arbitro, na qual ´e poss´ıvel acompanhar o
tempo de jogo, gols marcados e os cart˜oes amarelos e vermelhos.


71
Figura 23: Interface gr´aﬁca da aplica¸c˜ao Referee Box.
A interface gr´aﬁca da aplica¸c˜ao Referee Box (Figura 23) apresenta quatro grandes
bot˜oes em sua parte superior. O bot˜ao Halt determina que todos os robˆos interrompam seus
movimentos completamente de forma imediata. Esse comando normalmente ´e executado
em casos de emergˆencia, nos quais o ´arbitro ou as equipes precisem de um longo tempo
para resolver a situa¸c˜ao. O bot˜ao Stop interrompe a partida e ordena que todos os robˆos
se posicionem a pelo menos 50 cm da bola. Este bot˜ao ´e utilizado ao in´ıcio da partida ou
quando algum time sofre um gol, de forma a reiniciar a partida. Na sequˆencia, o bot˜ao
Force Start indica um rein´ıcio de partida no qual ambas as equipes est˜ao autorizadas a
aproximar-se e tocar na bola imediatamente. Finalmente, o bot˜ao Normal Start determina
o in´ıcio de partida permitindo apenas um dos times a tocar na bola.


72
Nos retˆangulos de controle referente a cada uma das equipes est˜ao presentes os
quatro bot˜oes de rein´ıcio favor´aveis `a respectiva equipe. O bot˜ao Kickoﬀordena as
equipes a se prepararem para um pontap´e de sa´ıda. O bot˜ao Penalty ordena que os
times se preparem para a cobran¸ca de uma penalidade m´axima. Ambos s˜ao comandos de
prepara¸c˜ao, ou seja, ser˜ao realmente executados somente ap´os o comando Normal Start. Na
sequˆencia, o bot˜ao Freekick ordena o time a executar imediatamente um tiro livre direto.
Esse comando ´e usado para cobran¸cas de faltas. Finalmente, o bot˜ao Indirect ordena o
time a imediatamente executar um tiro livre indireto, em tiros de meta e escanteios.
Uma partida de futebol de robˆos inicia-se com o comando Stop. Nesse momento,
os robˆos come¸cam a se mover pelo campo de jogo. O ´arbitro ent˜ao escolhe uma equipe
que dar´a in´ıcio a partida. Finalmente, quando todos os robˆos j´a est˜ao em suas posi¸c˜oes,
o ´arbitro determina o in´ıcio de partida, atrav´es do comando Normal Start. Durante a
partida, uma s´erie de interrup¸c˜oes e rein´ıcios ir˜ao se suceder.
Nota-se ainda que, em uma partida de futebol de robˆos, cada membro do time
deve desempenhar uma fun¸c˜ao espec´ıﬁca em campo, com responsabilidades muito bem
deﬁnidas. Um goleiro, por exemplo, tem como responsabilidade evitar que os chutes do
time advers´ario entrem em sua baliza. J´a um atacante, n˜ao deve se preocupar em defender,
mas sim em fazer gols na baliza advers´aria. Dessa forma, o sistema de controle deve
tamb´em ser capaz de diferenciar as fun¸c˜oes que cada robˆo pode assumir durante uma
partida.
A Figura 24 apresenta uma vis˜ao geral sobre a responsabilidade de cada uma
das aplica¸c˜oes que comp˜oem o ambiente de simula¸c˜ao. A aplica¸c˜ao de controle dos robˆos
deve ser capaz de responder de maneira adequada aos diferentes comandos e informa¸c˜oes
recebidos de ambas as aplica¸c˜oes que comp˜oem o ambiente de simula¸c˜ao, deliberando
sobre qual a¸c˜ao deve ser executada por cada um dos robˆos que comp˜oem a equipe. A
decis˜ao sobre qual a¸c˜ao a ser executada ´e baseada em regras que permitem avaliar as
atuais condi¸c˜oes da partida para ent˜ao decidir quais comandos ser˜ao enviados para cada
um dos robˆos.
Figura 24: Diagrama representativo das aplica¸c˜oes que comp˜oem o ambiente simulado
Robocup SSL.


73
2.5
REFLEX˜AO SOBRE A REVIS˜AO DO ESTADO DA ARTE
Este presente cap´ıtulo apresentou uma breve revis˜ao acerca dos principais pro-
blemas encontrados nos paradigmas usuais de programa¸c˜ao, nomeadamente o PI e PD.
Ainda, uma revis˜ao mais aprofundada sobre o PON foi apresentada, descrevendo suas
principais caracter´ısticas.
O PON ´e um paradigma emergente o qual se apresenta como uma alternativa aos
paradigmas de programa¸c˜ao vigentes (e.g. paradigma imperativo e declarativo). Visando
solucionar algumas das principais deﬁciˆencias dos atuais paradigmas de programa¸c˜ao, tais
como redundˆancias estruturais e temporais, bem como os acoplamentos da´ı decorrentes, o
PON apresenta uma nova forma de estruturar e executar artefatos de software.
Por meio da programa¸c˜ao inspirada na forma declarativa (e.g fatos e regras), o
PON permite criar aplica¸c˜oes de forma mais natural, com maior proximidade `a cogni¸c˜ao
humana, em alto n´ıvel. Al´em disso, a execu¸c˜ao de aplica¸c˜oes PON se d´a atrav´es de
pequenas entidades computacionais reativas, as quais colaboram por meio de notiﬁca¸c˜oes
e formam o mecanismo de notiﬁca¸c˜oes do PON. Por se tratar de notiﬁca¸c˜oes precisas e
pontuais, o PON permite execu¸c˜ao otimizada e minimamente acoplada, caracter´ısticas estas
´uteis tanto para ‘mono-processamento’ bem como para processamento distribu´ıdo [Sim˜ao
e Stadzisz 2008].
Como apresentado na Subse¸c˜ao 2.2.8.1, o PON foi primeiramente materializado
na forma de um Framework, o qual hoje se encontra em sua terceira vers˜ao, dado que
houve a vers˜ao prototipal, a vers˜ao 1.0 e a vers˜ao 2.0. Tal materializa¸c˜ao possibilitou a
cria¸c˜ao de aplica¸c˜oes PON e consequente valida¸c˜ao dos conceitos relacionados a esse para-
digma. Entretanto, as aplica¸c˜oes desenvolvidas utilizando o Framework n˜ao apresentaram
desempenho satisfat´orio quando confrontados com a natureza do PON e comparados com
o c´alculo assint´otico da sua estrat´egia de inferˆencia apresentado na Subse¸c˜ao 2.2.5 [Ferreira
et al. 2013].
Portanto, vislumbrou-se a necessidade da cria¸c˜ao de uma linguagem de pro-
grama¸c˜ao e respectivo compilador para o PON, nomeado de LingPON ou tecnologia
LingPON. Dessa forma, a primeira vers˜ao da LingPON foi criada em [Ferreira 2016], a
partir de um vers˜ao prototipal feita em uma disciplina de Linguagens e Compiladores 10,
com o objetivo de abstrair as caracter´ısticas do PON em uma gram´atica apropriada.
10Disciplina “Linguagens e Compiladores” ofertada pela UTFPR em 2014, ministrada por Prof. Dr.
Jo˜ao Alberto Fabro e Prof. Dr. Jean Marcelo Sim˜ao e frequentada pelos alunos Adriano Francisco
Ronszcka, Cleverson Avelino Ferreira, Priscila Ap. de Moraes Ioris e Clayton Kossoski.


74
A cria¸c˜ao de uma linguagem nativa representou uma grande evolu¸c˜ao para o estado
da t´ecnica do PON. No tocante ao desempenho, as aplica¸c˜oes desenvolvidas utilizando
a LingPON apresentaram melhores resultados, relacionado a tempo de processamento,
quando comparadas `as suas vers˜oes desenvolvidas utilizando o Framework [Ferreira 2016].
No tocante a facilidade de programa¸c˜ao, a LingPON se destaca pela sua simplicidade
e clareza, tornando o desenvolvimento de aplica¸c˜oes PON mais simples nesse sentido,
permitido estruturar o conhecimento de uma aplica¸c˜ao em mais alto n´ıvel de forma mais
natural ao ser humano [Ferreira 2016].
Entretanto, mesmo com o surgimento de uma linguagem de programa¸c˜ao na-
tiva, apenas algumas poucas aplica¸c˜oes PON com certo n´ıvel de complexidade foram
desenvolvidas at´e o presente momento utilizando ambas as materializa¸c˜oes.
Em se tratando de Framework, a maioria das aplica¸c˜oes desenvolvidas apresenta-
vam baixo n´ıvel de complexidade, conforme apresentado no Apˆendice E. O principal motivo
para isso ´e que muitas dessas aplica¸c˜oes tinham como principal objetivo demonstrar e
validar as caracter´ısticas do PON, sendo para tal suﬁciente o desenvolvimento de pequenas
e m´edias aplica¸c˜oes aplicadas a cen´arios espec´ıﬁcos de teste. Ademais, as aplica¸c˜oes um
tanto mais complexas (como Controle de Sistema Manufatura em Framework prototipal
C++ [Sim˜ao 2001]), n˜ao foram efetivamente comparadas com as respectivas aplica¸c˜oes em
PI. Ainda, nenhuma aplica¸c˜ao foi comparada com o equvialente em PI totalmente feito
por outrem, este diferente do desenvolvedor PON. Mesmo no caso do CTA as aplica¸c˜oes
j´a existentes em PI eram corrigidas pelo desenvolvedor PON pertinente.
A LingPON, por sua vez, apresenta algumas limita¸c˜oes que diﬁcultam o desenvol-
vimento de aplica¸c˜oes PON com escopo mais abrangente. Entre as principais limita¸c˜oes,
pode-se destacar a redundˆancia na declara¸c˜ao de Rules e impossibilidade de relacionar
outros FBEs como Attributes. Em suma, falta a capacidade de FBEs agregarem outros
FBEs e de FBEs agregarem outras Rules.
De forma a solucionar tais limita¸c˜oes, o pr´oximo cap´ıtulo apresenta dois novos
conceitos, no ˆambito de relacionamento de agrega¸c˜ao entre entidades PON, que podem
facilitar o desenvolvimento de aplica¸c˜oes PON utilizando a LingPON.


75
3
DESENVOLVIMENTO
Esse cap´ıtulo apresenta as contribui¸c˜oes desse trabalho, as quais s˜ao relativas
ao PON. Conforme apresentado na Se¸c˜ao 1.4, esse trabalho apresenta como parte do
objetivo principal a evolu¸c˜ao da LingPON e seu respectivo compilador de forma a facilitar
a cria¸c˜ao de aplica¸c˜oes PON. A partir disso, outra parte do objetivo principal ´e propor uma
aplica¸c˜ao de complexidade reconhecida (futebol de robˆos) comparando-a com a mesma
aplica¸c˜ao desenvolvida sob o vi´es do PI e com outras materializa¸c˜oes do PON.
Nesse sentido, as contribui¸c˜oes para a LingPON e seu respectivo compilador
s˜ao apresentadas na Se¸c˜ao 3.1.
Na sequˆencia, a Se¸c˜ao 3.2 apresenta em detalhes o
desenvolvimento da aplica¸c˜ao de controle para uma partida de futebol de robˆos utilizando
materializa¸c˜oes do PON (Framework 2.0, atual vers˜ao da LingPON e a nova vers˜ao
da LingPON aqui proposta) e a compara¸c˜ao das mesmas entre si e com uma solu¸c˜ao
equivalente desenvolvida sob o vi´es do PI.
3.1
CONTRIBUIC¸ ˜OES PARA A LINGPON
Esta se¸c˜ao apresenta as contribui¸c˜oes deste trabalho para com a LingPON e o
seu respectivo compilador. Primeiramente, a subse¸c˜ao 3.1.1 apresenta em detalhes as
altera¸c˜oes realizadas na LingPON para permitir o relacionamento de FBEs atrav´es de
agrega¸c˜ao. Na sequˆencia, na se¸c˜ao 3.1.2 s˜ao apresentadas as altera¸c˜oes realizadas na
LingPON e seu respectivo compilador para suportar a agrega¸c˜ao de Rules em FBEs de
forma a permitir a cria¸c˜ao de Rules de forma mais direta e com menos redundˆancia de
linhas de c´odigo. Por ﬁm, a se¸c˜ao 3.1.3 apresenta a corre¸c˜ao (bug ﬁx) aplicada ao processo
de compila¸c˜ao da LingPON de forma a solucionar um erro encontrado na gera¸c˜ao de
c´odigo-alvo C++ com m´ultiplas instˆancias de FBEs na atual vers˜ao do compilador.
As contribui¸c˜oes para a LingPON s˜ao aqui apresentadas de forma literal, com o
objetivo de facilitar o entendimento das mesmas. Descri¸c˜oes mais detalhadas do ponto
de vista de altera¸c˜oes realizadas no c´odigo-fonte do compilador PON, no tocante ao


76
analisador l´exico, analisador sint´atico, analisador semˆantico e gerador de c´odigo, podem
ser encontradas no Apˆendice A deste trabalho.
3.1.1
AGREGAC¸ ˜AO ENTRE FBES
Conforme apresentado na Se¸c˜ao 1.3.2, a atual vers˜ao da LingPON e seu respectivo
compilador suportam apenas Attributes de tipos primitivos, isto ´e, boolean, integer, ﬂoat,
char ou string [Ferreira 2016]. Entretanto, de forma a aumentar o n´ıvel de encapsulamento
de Attributes e Methods no desenvolvimento de aplica¸c˜oes PON e, consequentemente,
facilitar o desenvolvimento de aplica¸c˜oes PON, este trabalho prop˜oe a possibilidade de
declarar Attributes que sejam deﬁnidos a partir de outros FBEs.
Para exempliﬁcar a vantagem de deﬁnir Attributes a partir de outro FBE, pode-se
imaginar uma aplica¸c˜ao PON na qual seja necess´ario criar um FBE que represente o
comportamento de um time de futebol. O time ´e composto por trˆes jogadores, cada qual
possuindo um nome, um n´umero e uma posi¸c˜ao de jogo. O C´odigo 15 apresenta o c´odigo
fonte criado para representar esse exemplo utilizando a vers˜ao original da LingPON.


77
C´odigo 15: Cria¸c˜ao do FBE Team na vers˜ao original do LingPON.
1 fbe Team
2
attributes
3
string atNamePlayer1 “ ”
4
integer atNumberPlayer1 0
5
string atPositionPlayer1 “ ”
6
string atNamePlayer2 “ ”
7
integer atNumberPlayer2 0
8
string atPositionPlayer2 “ ”
9
string atNamePlayer3 “ ”
10
integer atNumberPlayer3 0
11
string atPositionPlayer3 “ ”
12
end attributes
13
methods
14
method mtExecuteActionPlayer1()
15
method mtExecuteActionPlayer2()
16
method mtExecuteActionPlayer3()
17
end methods
18 end fbe
Analisando o c´odigo apresentado em C´odigo 15, constru´ıdo utilizando a vers˜ao
original da LingPON, nota-se a ocorrˆencia de redundˆancia na declara¸c˜ao dos Attributes
(linhas 3 `a 11) e Methods (linhas 14 `a 16). Portanto, de forma a reduzir a necessidade
de redundˆancia de c´odigo e, consequentemente, facilitar o desenvolvimento de aplica¸c˜oes
PON, a LingPON e seu respectivo compilador foram alterados de forma a suportar a
declara¸c˜ao de Attributes que sejam deﬁnidos a partir de outros FBEs.
Para suportar a declara¸c˜ao de Attributes n˜ao primitivos, algumas mudan¸cas no
analisador sint´atico utilizado pelo compilador foram propostas. Em um primeiro momento,
o arquivo de conﬁgura¸c˜ao do analisador sint´atico (Bison) foi alterado para que o mesmo
reconhecesse a declara¸c˜ao desse tipo de Attribute. Entretanto, isso ainda n˜ao foi suﬁciente,
uma vez que a tabela de s´ımbolos utilizada pelo compilador na gera¸c˜ao de c´odigo alvo
deveria gerenciar de maneira correta a rela¸c˜ao entre FBEs e seus Attributes n˜ao primitivos.
Nesse sentido, o gerenciador da tabela de s´ımbolos do compilador foi alterado. Com as
altera¸c˜oes feita no analisador sint´atico e na tabela de s´ımbolos, viabilizou-se a agrega¸c˜ao


78
entre FBEs. Neste sentido, dado que um FBE Team possui trˆes Attributes do tipo Player,
para cada nova instˆancia do FBE Team, trˆes novas instˆancias de Player s˜ao criadas,
adicionadas `a tabela de s´ımbolos e relacionadas com o FBE que a deﬁniu (Team).
Utilizando a nova vers˜ao do LingPON, foi poss´ıvel reescrever o c´odigo apresentado
no C´odigo 15 de forma muito mais leg´ıvel, conforme apresentado no C´odigo 16. Entre as
linhas 1 e 10, foi deﬁnido uma FBE Player, o qual possui os Attributes e Methods referente
ao jogador de futebol. A partir da linha 11, foi declarado o FBE Team, o qual possui trˆes
Attributes do tipo Player.
C´odigo 16: Cria¸c˜ao do FBE Team na nova vers˜ao do LingPON.
1 fbe Player
2
attributes
3
string atNamePlayer “ ”
4
integer atNumberPlayer 0
5
string atPositionPlayer “ ”
6
end attributes
7
methods
8
method mtExecuteActionPlayer()
9
end methods
10 end fbe
11 fbe Team
12
attributes
13
Player atPlayer1 ;
14
Player atPlayer2 ;
15
Player atPlayer3 ;
16
end attributes
17
methods
18
method mtTeamInfo()
19
end methods
20 end fbe
Caso o requisito da aplica¸c˜ao fosse alterado para o time suportar quatro jogadores,


79
na aplica¸c˜ao desenvolvida na vers˜ao original da LingPON, seria necess´ario adicionar trˆes
novos Attributes (atNamePlayer4, atNumberPlayer4 e atPositionPlayer4) e um novo
Method (mtExecuteActionPlayer4). A mesma mudan¸ca de requisito poderia ser feita, na
nova vers˜ao da LingPON, simplesmente adicionando um novo Attribute (atPlayer4) do
tipo Player no FBE Team e realizando as devidas altera¸c˜oes no m´etodo mtTeamInfo.
3.1.2
AGREGAC¸ ˜AO DE RULES EM FBES
Conforme apresentado na Se¸c˜ao 1.3.1, a atual vers˜ao da LingPON faz com que, no
c´odigo fonte, as Rules sejam relacionadas a instˆancias de FBEs. Com isso, para cada nova
instˆancia criada, novas Rules devem ser adicionadas ao sistema, criando assim redundˆancia
de c´odigo e consequente aumento de complexidade do c´odigo fonte.
Para exempliﬁcar esse problema, pode-se imaginar uma aplica¸c˜ao PON na qual
seja necess´ario controlar os movimentos de um robˆo em uma partida de futebol. De forma
a facilitar o entendimento do exemplo, o robˆo dever´a simplesmente correr atr´as da bola
quando sua posi¸c˜ao for diferente da posi¸c˜ao da bola.
Nesse sentido, os FBEs Robot e Ball apresentados no C´odigo 17, poderiam ser
criados para representar, respectivamente, os robˆos e a bola em uma partida de futebol.


80
C´odigo 17: Exemplo de FBE Robot.
1 fbe Robot
2
attributes
3
ﬂoat atRobotPos 0.0
4
end attributes
5
methods
6
method mtRunToBall ( ... )
7
end methods
8 end fbe
9
10 fbe Ball
11
attributes
12
ﬂoat atBallPos 0.0
13
end attributes
14
methods
15
method mtGetPosition ( ... )
16
end methods
17 end fbe
Conforme mencionado anteriormente, na atual vers˜ao da LingPON, cada uma
das Rules que determinam o comportamento l´ogico-causal do sistema est´a diretamente
relacionada a uma instˆancia de FBE. Neste sentido, caso seja necess´ario controlar dois
robˆos, ou seja, duas instˆancias do FBE Robot (robot1 e robot2), ser´a necess´ario criar duas
Rules, conforme apresentado em C´odigo 18.


81
C´odigo 18: Exemplo de declara¸c˜ao de Rules para controle de robˆos na vers˜ao
original do LingPON.
1 rule rlRunToBallRobot1
2
condition
3
subcondition condRobot1NotBallPos
4
premise prRb1NotBallPos robot1.atRobotPos != ball.atBallPos
5
end subcondition
6
end condition
7
action
8
instigation inRb1Move robot1.mtRunToBall();
9
end action
10 end rule
11
12 rule rlRunToBallRobot2
13
condition
14
subcondition condRobot2NotBallPos
15
premise prRb2NotBallPos robot2.atRobotPos != ball.atBallPos
16
end subcondition
17
end condition
18
action
19
instigation inRb2Move robot2.mtRunToBall();
20
end action
21 end rule
Ao analisar o c´odigo apresentado no C´odigo 18, ´e poss´ıvel observar que as duas
Rules s˜ao muito semelhantes em suas declara¸c˜oes. A ´unica real diferen¸ca entre elas ´e a
instˆancia do FBE Robot com a qual cada uma delas se relaciona. Enquanto a primeira
Rule est´a fazendo referˆencia para a instˆancia robot1, a segunda Rule referencia a instˆancia
robot2. Neste sentido, ´e clara a redundˆancia de c´odigo para a constru¸c˜ao das Rules na
atual vers˜ao do LingPON.
Para facilitar o desenvolvimento de aplica¸c˜oes PON complexas, isto ´e, com
m´ultiplas instˆancias de FBEs e m´ultiplas Rules, um novo conceito foi inserido na pro-
grama¸c˜ao de aplica¸c˜oes PON: FBE Rule. Uma FBE Rule ´e deﬁnida como uma Rule que,
ao inv´es de estar relacionada a uma instˆancia de FBE, est´a relacionada a uma classe de


82
FBE. Dessa forma, para cada nova instˆancia de FBE criada, todo o conjunto de FBE
Rules associado ao FBE ser´a criado de forma autom´atica, pelo pr´oprio compilador PON.
Neste quadro, cada FBE Rule trataria dessa instˆancia em espec´ıﬁco. Ademais, uma FBE
Rule pode referenciar instˆancias outras ao pr´oprio FBE, por exemplo a instˆancia ball do
FBE Ball.
Para tornar poss´ıvel a cria¸c˜ao de um conjunto de Rules para cada nova instˆancia de
FBE, foi necess´ario alterar o processo de compila¸c˜ao da LingPON. Conforme apresentado na
Figura 25, um pr´e-compilador foi inserido no processo de compila¸c˜ao de c´odigo-fonte PON.
O pr´e-compilador utiliza o mesmo analisador l´exico e sint´atico utilizado pelo compilador
PON, diferenciando-se apenas pelo gerador de c´odigo.
Figura 25: Fluxo de compila¸c˜ao de c´odigo utilizando o pr´e-compilador PON.
Primeiramente, o pr´e-compilador executa a etapa de an´alise l´exica, na qual os
caracteres presentes no c´odigo-fonte s˜ao lidos e agrupados em tokens. Essa etapa gera como
sa´ıda uma sequˆencia de tokens. Utilizando a sequˆencia de tokens gerada pelo analisador
l´exico, o pr´e-compilador executa a an´alise semˆantica, de forma a identiﬁcar se os tokens
provenientes do c´odigo-fonte est˜ao na sequˆencia correta.
Caso n˜ao seja encontrado nenhum erro semˆantico, o pr´e-compilador inicia a etapa


83
de gera¸c˜ao de c´odigo. Nesta ´ultima etapa, o pr´e-compilador identiﬁca as FBE Rules
presentes no c´odigo-fonte e os FBEs a elas associados. Para cada instˆancia de um FBE
que possui FBE Rule associada, o pr´e-compilador ir´a criar uma entidade Rule e associ´a-la
a uma instˆancia do FBE.
A etapa de pr´e-compila¸c˜ao tem como sa´ıda um c´odigo-fonte PON pr´e-compilado.
Esse c´odigo-fonte apresenta todas as Rules associadas a cada uma das instˆancias de FBE
presentes no c´odigo-fonte original.
Dessa forma, esse novo conceito diminui a necessidade de redundˆancia de c´odigo
na declara¸c˜ao de Rules, fazendo com que o n´umero de Rules a serem declaradas n˜ao seja
mais diretamente proporcional ao n´umero de instˆancias presentes em uma aplica¸c˜ao PON.
Utilizando o conceito de FBE Rules, presente na nova vers˜ao da LingPON, foi
poss´ıvel reescrever as Rules apresentadas no C´odigo 18 sem a necessidade de redundˆancias
na declara¸c˜ao das mesmas, conforme apresentado no C´odigo 19.
C´odigo 19: Exemplo de declara¸c˜ao de FBE Rule para controle de robˆos.
1 fbe Robot
2
attributes
3
string atRobotPos 0.0
4
end attributes
5
methods
6
method mtRunToBall ( ... )
7
end methods
8
fbeRule rlRunToBall
9
condition
10
subcondition condRobotNotBallPos
11
premise prRbNotBallPos Robot.atRobotPos != ball.atBallPos
12
end subcondition
13
end condition
14
action
15
instigation inMoveRobot Robot.mtRunToBall();
16
end action
17
end fbeRule
18 end fbe


84
Caso trˆes instˆancias do FBE Robot, apresentado no C´odigo 19, forem criadas e
nomeadas respectivamente como “robot1”, “robot2” e “robot3”, o pr´e-compilador PON
criar´a trˆes Rules no c´odigo PON pr´e-compilado, diferenciando-as apenas pela instˆancia
associada. Nota-se que a instˆancia de Ball (ball) foi referenciada na Premisse da FBE
Rule. Dessa forma, todas as Rules geradas no processo de compila¸c˜ao far˜ao referˆencia `a
mesma instˆancia do FBE Ball. O resultado da pr´e-compila¸c˜ao, presente no c´odigo PON
pr´e-compilado, pode ser observado no C´odigo 20


85
C´odigo 20: Rules criadas a partir do processo de pr´e-compila¸c˜ao
1
rule rlRunToBall0
2
condition
3
subcondition condRobotNotBallPos0
4
premise prRbNotBallPos robot1.atRobotPos != ball.atBallPos
5
end subcondition
6
end condition
7
action
8
instigation inMoveRobot0 robot1.mtRunToBall();
9
end action
10
end rule
11
rule rlRunToBall1
12
condition
13
subcondition condRobotNotBallPos1
14
premise prRbNotBallPos robot2.atGameStarted != ball.atBallPos
15
end subcondition
16
end condition
17
action
18
instigation inMoveRobot1 robot2.mtRunToBall();
19
end action
20
end rule
21
rule rlRunToBall2
22
condition
23
subcondition condRoboNotBallPos2
24
premise prRbNotBallPos robot3.atGameStarted != ball.atBallPos
25
end subcondition
26
end condition
27
action
28
instigation inMoveRobot2 robot3.mtRunToBall();
29
end action
30
end rule
Caso seja necess´ario alterar os requisitos do sistema de forma a controlar mais trˆes
robˆos, na aplica¸c˜ao desenvolvida utilizando a vers˜ao original da LingPON, seria necess´ario


86
declarar trˆes novas instˆancias do FBE Robot (robot3, robot4 e robot5) e adicionar trˆes
novas Rules ao c´odigo fonte. Essas altera¸c˜oes resultariam no acr´escimo de 30 linhas de
c´odigo ao c´odigo fonte.
A mesma mudan¸ca de requisito, utilizando a nova vers˜ao da LingPON, com
suporte a declara¸c˜ao de FBE Rules n˜ao exigiria nenhuma altera¸c˜ao na declara¸c˜ao do FBE
ou de Rules. A ´unica altera¸c˜ao no c´odigo fonte seria a declara¸c˜ao de trˆes novas instˆancias
do FBE Robot, a qual n˜ao resultaria em acr´escimo de linhas no c´odigo.
3.1.3
CORREC¸ ˜AO DE ERRO: GERAC¸ ˜AO DE C´ODIGO-ALVO C++ COM M´ULTIPLAS
INSTˆANCIAS DE FBE
Durante o desenvolvimento da aplica¸c˜ao de controle para partida de futebol de
robˆos, a qual ´e utilizada como estudo de caso deste trabalho, foi encontrado um erro
(bug) que compromete o desenvolvimento de aplica¸c˜oes PON utilizando a atual vers˜ao do
compilador PON (vers˜ao 1.0).
De forma sucinta, a atual vers˜ao do compilador n˜ao ´e capaz de distinguir diferentes
instˆancias de FBEs durante o processo de gera¸c˜ao de c´odigo-alvo em C++. Para o
compilador, todas as instˆancias de um determinado FBE s˜ao representados por uma mesma
classe C++. Este erro pode ser facilmente reproduzido pelo c´odigo PON apresentado no
C´odigo 21.


87
C´odigo 21: C´odigo utilizado para reproduzir erro de gera¸c˜ao de c´odigo-alvo
C++ na atual vers˜ao do LingPON.
1 fbe Robot
2
attributes
3
int atFunction 0
4
end attributes
5
methods
6
method mtDefense (atFunction = 2)
7
end methods
8 end fbe
9
10 inst
11
Robot robot1
12
Robot robot2
13 end inst
14
15 rule rlRobot1
16
condition
17
subcondition condition1
18
premise prRobotFunction1 robot1.atFunction == 1
19
end subcondition
20
end condition
21
action
22
instigation inRobot1Defense robot1.mtDefense();
23
end action
24 end rule
25 rule rlRobot2
26
condition
27
subcondition condition2
28
premise prRobotFunction1 robot2.atFunction == 1
29
end subcondition
30
end condition
31
action
32
instigation inRobot2Defense robot2.mtDefense();
33
end action
34 end rule


88
Ao analisar o C´odigo 21, observa-se que duas instˆancias do FBE Robot foram
criadas (robot1 e robot2) e, para cada instˆancia, uma Rule foi associada. Dessa forma, a
instˆancia robot1 deve relacionar-se apenas com a Rule rlRobot1 e a instˆancia robot2 com
rlRobot2.
Ao compilar este c´odigo-fonte com a op¸c˜ao de gera¸c˜ao de c´odigo em C++, a atual
vers˜ao do compilador ir´a gerar os arquivos de sa´ıda com sucesso. Entretanto, ao analisar
o conte´udo do arquivo C++ “Robot.cpp”, ´e poss´ıvel observar que tanto robot1 quanto
robot2 relacionam-se com as duas Rules , conforme apresentado no C´odigo 22.
C´odigo 22: C´odigo C++ gerado pela atual vers˜ao do compilador.
1 Robot::Robot(rlRobot1 * rlRobot1, rlRobot2 * rlRobot2)
2 {
3
this->rlRobot1 = rlRobot1;
4
this->rlRobot2 = rlRobot2;
5
...
6 }
Isto ocorre porque a atual vers˜ao do compilador PON transforma cada FBE
presente no c´odigo-fonte PON em uma classe no c´odigo gerado em C++. Com isso, n˜ao
existe diferencia¸c˜ao das Rules associadas `as instˆancias robot1 e robot2. Este problema n˜ao
fora observado em [Ferreira 2016] porque as aplica¸c˜oes PON desenvolvidas pelo mesmo,
a saber Mira ao Alvo e Sistema de Vendas, apresentavam apenas uma instˆancia de cada
FBE.
A solu¸c˜ao para este problema utilizando a estrutura e ﬂuxo de compila¸c˜ao do
atual compilador PON n˜ao ´e trivial, conforme fora discutido em reuni˜ao do grupo de
pesquisa PON da UTFPR. Entretanto, com o advento do pr´e-compilador, a solu¸c˜ao para
tal problema tornou-se de certa forma simples. Durante o processo de pr´e-compila¸c˜ao, o
pr´e-compilador ´e capaz de criar tantas c´opias de um determinado FBE quantas forem
o n´umero de suas instˆancias. Por exemplo, dado o C´odigo 21, o pr´e-compilador criaria


89
dois FBEs no c´odigo-fonte PON pr´e-compilado (Robotrobot1 e Robotrobot2), conforme
apresentado no C´odigo 23.


90
C´odigo 23: C´odigo PON pr´e-compilado gerado pelo pr´e-compilador PON
para solucionar problema com m´ultiplas instˆancias de FBEs.
1 fbe Robotrobot1
2 ...
3 end fbe
4
5 fbe Robotrobot2
6 ...
7 end fbe
8
9 inst
10
Robotrobot1 robot1
11
Robotrobot2 robot2
12 end inst
13
14 rule rlRobot1
15
condition
16
subcondition condition1
17
premise prRobotFunction1 robot1.atFunction == 1
18
end subcondition
19
end condition
20
action
21
instigation inRobot1Defense robot1.mtDefense();
22
end action
23 end rule
24 rule rlRobot2
25
condition
26
subcondition condition2
27
premise prRobotFunction1 robot2.atFunction == 1
28
end subcondition
29
end condition
30
action
31
instigation inRobot2Defense robot2.mtDefense();
32
end action
33 end rule


91
Dessa forma, o atual compilador interpretaria cada FBE e sua instˆancia relacionada
separadamente, gerando assim os arquivos C++ de maneira correta.
Esta solu¸c˜ao foi aplicada com sucesso e, utilizando o pr´e-compilador, foi poss´ıvel
criar a aplica¸c˜ao para controle de futebol de robˆos em PON, a qual utiliza m´ultiplas
instˆancias de um dado FBE.
3.2
ESTUDO DE CASO - SOFTWARE DE CONTROLE PARA O FUTEBOL DE
ROBˆOS
O objetivo principal desta se¸c˜ao ´e apresentar o desenvolvimento do sistema de
controle para uma partida de futebol de robˆos em PON, segundo regras e caracter´ısticas
da categoria SSL, utilizando o Framework PON vers˜ao 2.0, a atual vers˜ao da LingPON e
a nova vers˜ao da LingPON apresentada neste trabalho, bem como compar´a-las entre elas
e tamb´em com uma solu¸c˜ao funcionalmente equivalente constru´ıda sobre o PI por outrem.
Primeiramente, a aplica¸c˜ao de controle do Futebol de Robˆos foi codiﬁcada em
linguagem de programa¸c˜ao C++ POO/PI por outro desenvolvedor. Na sequˆencia, tal
aplica¸c˜ao serviu como base para o desenvolvimento da aplica¸c˜ao sob o vi´es do PON,
utilizando as materializa¸c˜oes Framework 2.0, tecnologia LingPON 1.0 (dita original) e a
nova vers˜ao desta tecnologia desenvolvida neste trabalho, aqui nomeada de LingPON 1.2.
Isto considerado, a subse¸c˜ao 3.2.1 apresenta uma descri¸c˜ao, em alto n´ıvel, de como
o sistema de controle deve funcionar em uma partida de futebol de robˆos. Na sequˆencia, a
subse¸c˜ao 3.2.2 apresenta os detalhes da aplica¸c˜ao desenvolvida sob o vi´es do POO/PI. A
se¸c˜ao 3.2.3 apresenta detalhes das aplica¸c˜oes desenvolvidas sob o vi´es do PON. A se¸c˜ao
3.2.4 apresenta as compara¸c˜oes realizadas utilizando as diferentes implementa¸c˜oes. Por ﬁm,
a Se¸c˜ao 3.2.5 apresenta as considera¸c˜oes ﬁnais sobre as diferentes solu¸c˜oes apresentadas no
presente cap´ıtulo.
3.2.1
ESPECIFICAC¸ ˜AO DO SOFTWARE DE CONTROLE PARA UMA PARTIDA
DE FUTEBOL DE ROBˆOS
Baseando-se em trˆes vari´aveis, nomeadamente cmdReferee, lastCmd e teamColor,
o sistema de controle deve ser capaz de avaliar e determinar o comportamento para cada
um dos robˆos que est˜ao sendo controlados. A vari´avel cmdReferee representa o ´ultimo


92
comando enviado pela aplica¸c˜ao Referee Box, descrita na subse¸c˜ao 2.4.1. A vari´avel
lastCmd, por sua vez, representa o valor predecessor enviado pela aplica¸c˜ao Referee Box,
ou seja, o pen´ultimo comando recebido. A vari´avel TeamColor representa a cor do time
que est´a sendo controlado, podendo assumir o valor Amarelo (Yellow) ou Azul (Blue).
A Figura 26 apresenta o diagrama de atividades em UML para algumas poucas
atividades recorrentes durante uma partida de futebol de robˆos alcan¸caveis a partir das trˆes
vari´aveis rec´em mencionadas. Um diagrama de atividades contendo todos as atividades
poss´ıveis torna-se invi´avel de ser apresentado, devido ao grande n´umero de condi¸c˜oes
a serem avaliadas pelas regras que regem o comportamento do sistema, as quais s˜ao
apresentadas no Apˆendice C.
Figura 26: Diagrama de atividades simpliﬁcado de uma partida de futebol de robˆos.
Como demonstrado em [Wiecheteck et al. 2011,Batista 2013], a partir da an´alise de
um diagrama de atividades pode-se levantar as regras l´ogico causais que regem a aplica¸c˜ao.
O levantamento de regras pode ser realizado respondendo as seguintes perguntas:
• Qual o objetivo da regra?
• O que precisa acontecer para que a regra seja executada?
• O que acontece se a regra for executada?
Dessa forma, aqui se enumeram duas regras que foram extra´ıdas do diagrama de
atividade apresentado na Figura 26 utilizando as perguntas descritas acima:
1. Nome da regra: Parar robˆos


93
• Qual o objetivo da regra? Mover robˆos para posi¸c˜oes de in´ıcio/re´ınicio de
partida.
• O que precisa acontecer para que a regra seja executada? O comando enviado
pelo Referee Box deve ser Stop.
• O que acontece se a regra for executada? Cada robˆo deve ir para sua posi¸c˜ao,
respeitando a distˆancia m´ınima de 50 cm da bola.
2. Nome da regra: Cobrar pˆenalti (time azul)
• Qual o objetivo da regra? Cobrar penalidade m´axima
• O que precisa acontecer para que a regra seja executada? O comando enviado
pelo Referee Box deve ser NormalStart, o time controlado deve ser Blue e o
pen´ultimo comando enviado pelo ´arbitro deve ser PenaltyBlue.
• O que acontece se a regra for executada? Um robˆo do time azul, que est´a sendo
controlado, deve cobrar a penalidade m´axima.
A decis˜ao sobre qual a¸c˜ao deve ser executada por cada um dos robˆos apresenta uma
certa varia¸c˜ao de complexidade entre os poss´ıveis cen´arios (decorrentes de atividades) em
uma partida de futebol. Para alguns comandos enviados pela Referee Box, a decis˜ao sobre
qual a¸c˜ao executar ´e realizada com facilidade. Por exemplo, quando a aplica¸c˜ao de controle
recebe o comando Stop, n˜ao ´e necess´ario veriﬁcar qual time est´a sendo controlado, pois,
independente do time que est´a sendo controlado, todos os robˆos dever˜ao se posicionar-se
de forma a defender o seu gol, a pelo menos 50 cm. da bola.
Entretanto, para alguns comandos essa decis˜ao torna-se mais complexa. Conforme
apresentado na Regra 2, quando o comando NormalStart ´e recebido, deve-se avaliar o
pen´ultimo comando recebido, o qual ´e nomeado comando de prepara¸c˜ao, e qual time est´a
sendo controlado pelo sistema. Isso ´e necess´ario devido a diferen¸ca que determinados
comandos geram em cada uma das equipes. Por exemplo, quando o comando de prepara¸c˜ao
PenaltyBlue ´e recebido, o time Blue deve se preparar para cobran¸ca de penalidade m´axima,
enquanto o time Yellow deve se preparar para defender a cobran¸ca.
Observa-se que os resultados das regras apresentadas acima geram um novo ﬂuxo
de avalia¸c˜oes. Por exemplo, apenas um robˆo integrante do time pode efetuar, de fato, a
cobran¸ca de penalidade m´axima. Desse modo, o sistema deve ser capaz de julgar e escolher
qual robˆo ir´a executar a cobran¸ca, conforme apresentado no diagrama de atividades da
Figura 27. Essa escolha pode ser realizada com base na fun¸c˜ao que cada um dos robˆos


94
exerce durante a partida. Por exemplo, pode-se determinar que o robˆo que atua como
meio-campo ´e quem dever´a executar a cobran¸ca de penalidade m´axima.
Figura 27: Diagrama de atividades para escolha do batedor de penalidade m´axima.
Ap´os a decis˜ao sobre qual a¸c˜ao deve ser executada, o software de controle deve ser
capaz de transformar essa decis˜ao em comandos de controle a serem executados por cada
um dos robˆos. Cada robˆo possui motores utilizados para deslocamento e um dispositivo
chutador utilizado para lan¸car a bola, isto ´e, realizar comandos de chute e passe.
Dessa forma, o software de controle deve calcular as a¸c˜oes a serem realizadas
por cada robˆo de forma a atingir o objetivo desejado. Por exemplo, quando a a¸c˜ao a ser
executada ´e cobrar uma penalidade m´axima, o software deve calcular qual a velocidade e
ˆangulo com que o robˆo deve dirigir-se `a bola e qual a potˆencia de chute deve ser utilizada
para que a cobran¸ca seja executada com sucesso.
Portanto, os sistemas de controle constru´ıdos sob o vi´es do PI e PON, a serem
apresentados nas se¸c˜oes subsequentes, devem ser capazes de materializar as diversas regras
que modelam o comportamento dos robˆos em uma partida de futebol de robˆos, realizar os
c´alculos necess´arios, incluindo os l´ogico-causais. Maiores detalhes sobre as especiﬁca¸c˜oes
t´ecnicas da categoria SSL da Robocup e informa¸c˜oes sobre os requisitos funcionais desta
aplica¸c˜ao podem ser encontrado no Apˆendice B deste trabalho.
3.2.2
SOLUC¸ ˜AO DESENVOLVIDA SOB O VI´ES DO PARADIGMA IMPERATIVO -
PROGRAMAC¸ ˜AO ORIENTADA A OBJETOS
Esta se¸c˜ao tem por objetivo apresentar em detalhes a codiﬁca¸c˜ao do sistema de
controle para uma partida de futebol de robˆos sob o vi´es do PI, utilizando a linguagem de
programa¸c˜ao C++. O c´odigo apresentado foi desenvolvido por prof. Jo˜ao A. Fabro e o
ent˜ao estudante de Engenharia da Computa¸c˜ao Andr´e Botta, que foi bolsista de inicia¸c˜ao


95
cient´ıﬁca da UTFPR [Botta 2012]. Apesar de ter sido desenvolvida por outrem, esta
aplica¸c˜ao ´e aqui apresentada por ter sido utilizada como base para o desenvolvimento das
trˆes aplica¸c˜oes PON apresentadas neste trabalho.
Seguindo o modelo de desenvolvimento orientado a objetos, cada entidade que
comp˜oe o sistema de controle foi representada em termos de classes, como apresentado no
diagrama de classes da Figura 281.
Figura 28: Diagrama de classes simpliﬁcado da solu¸c˜ao desenvolvida em PI.
Cada um dos robˆos ´e representado por um objeto da classe Robot. Essa classe
possui atributos que representam as principais caracter´ısticas de um robˆo, tais como
n´umero de identiﬁca¸c˜ao, posi¸c˜ao atual e velocidades normal e angular. De forma similar,
uma instˆancia da classe Ball representa a bola que est´a sendo utilizada na partida. Por
sua vez, a classe CommunicationSystem ´e utilizada como interface de comunica¸c˜ao entre o
software de controle e cada um dos robˆos que est˜ao sendo controlados.
Cada instˆancia da classe RobotBehavior cont´em as fun¸c˜oes de c´alculo utilizadas
pelas instˆancias da classe Robot para controlar seus movimentos. Um exemplo de tais
fun¸c˜oes ´e aquela que calcula a velocidade com que o robˆo deve deslocar-se em dire¸c˜ao
a bola. Neste sentido, os m´etodos e atributos presentes na classe RobotBehavior s˜ao
utilizados apenas pelas instˆancias da classe Robot. Portanto, n˜ao haveria necessidade de
1O diagrama de classes apresentado foi criado a partir dos esfor¸cos de Andr´e Botta.


96
separar a l´ogica relacionada aos robˆos em duas classes.
A classe GameFunctions, por sua vez, apresenta m´etodos utilizados para obter
informa¸c˜oes do time como um todo. Um exemplo de m´etodo presente nesta classe ´e o
utilizado para calcular qual robˆo est´a mais perto da bola em um determinado momento.
A classe Game, instanciada no in´ıcio da execu¸c˜ao da aplica¸c˜ao, ´e respons´avel por
instanciar todos os objetos que ser˜ao utilizados durante a execu¸c˜ao do software de controle.
Em sua inicializa¸c˜ao, o n´umero necess´ario de instˆancias da classe Robot ´e criado, como
tamb´em uma respectiva instˆancia da classe RobotBehavior. Para cada ciclo de execu¸c˜ao,
isto ´e, cada ciclo de leitura dos pacotes recebidos a partir do sistema SSL-Vision (descrita
na subse¸c˜ao 2.4.1) a classe Game aciona a execu¸c˜ao da classe Strategy.
Utilizando as informa¸c˜oes obtidas atrav´es das instˆancias da classe Robot e Game-
Functions, a instˆancia da classe Strategy ir´a determinar qual a¸c˜ao cada um dos robˆos dever´a
executar. ´E importante salientar que, devido a necessidade do objeto da classe Strategy
conhecer o estado de todos os robˆos, existe apenas uma instˆancia da classe Strategy, a qual
´e referenciada pelas diferentes instˆancias de Robot. Portanto, a classe Strategy desempenha
o papel de controlador central para todos as instˆancias de Robot.
Entretanto, apesar de a instˆancia da classe Strategy representar o conhecimento
l´ogico causal do sistema, n˜ao ´e f´acil entender quais s˜ao as as regras de controle que a
mesma aplica sobre os robˆos que est˜ao sendo controlados. Isto ocorre devido a limita¸c˜oes
do paradigma imperativo, utilizado na concep¸c˜ao do sistema de controle.
Conforme apresentado na se¸c˜ao 2.1, a concep¸c˜ao de software sob o vi´es do PI ´e
realizada utilizando sequˆencias de instru¸c˜oes, as quais realizam buscas sobre entidades
passivas (dados e comandos). Nesse sentido, as regras que regem o sistema foram imple-
mentadas com a utiliza¸c˜ao de estruturas de controle, tais como switch-case (escolha caso)
e if-then-else (se ent˜ao sen˜ao) e estruturas de repeti¸c˜ao como for (para passo) e while
(enquanto). Essas estruturas apresentam-se dispersas em diferente m´etodos e classes, fato
este que diﬁculta o entendimento das regras que atuam sobre o sistema.
Em um primeiro momento, a instˆancia da classe Strategy avalia qual foi o ´ultimo
comando enviado pela aplica¸c˜ao Referee Box, a qual atua como ´arbitro da partida. A
avalia¸c˜ao foi codiﬁcada utilizando a estrutura de controle switch-case, conforme apresentado
no C´odigo 24.
C´odigo 24: Estrutura de controle switch-case utilizada pela classe Strategy (Strategy.cpp)
para determinar qual a¸c˜ao ser´a executada.


97
1
void
Strategy :: makeStrategy
()
2
{
3
switch ( game -> getCmdReferee () )
4
{
5
case
Stop:
6
{
7
strategyStop ();
8
break;
9
}
10
case
Ready:
11
{
12
char
lastCmd = game -> getLastCmdReferee ();
13
if ( gameFunctions -> foulForEnemy () )
14
game -> setReadyEnemy ( true );
15
16
if ( game -> getTeamColor () == YELLOW )
17
{
18
if ( lastCmd
==
PenaltyYellow )
19
{
20
readyPenalty ();
21
}
22
else if ( lastCmd
==
KickOffYellow )
23
{
24
readyKickoff
();
25
}
26
else
27
{
28
if ( lastCmd
==
PenaltyBlue )
29
penaltyEnemy
();
30
else
31
{
32
strategyStart ();
33
}
34
}
35
}
36
else
37
{
38
if ( lastCmd
==
PenaltyBlue )
39
{
40
readyPenalty ();
41
}
42
else if ( lastCmd
==
KickOffBlue )
43
{
44
readyKickoff
();
45
}
46
else
47
{
48
if ( lastCmd
==
PenaltyYellow )
49
penaltyEnemy
();
50
else
51
{
52
strategyStart ();
53
}
54
}
55
}
56
break;
57
}
58
case
Start:
59
{
60
strategyStart ();
61
break;
62
}
63
64
case
KickOffYellow :
65
{
66
if ( game -> getTeamColor () == YELLOW )
67
{
68
strategyKickoff
();
69
}
70
else
71
{
72
strategyStop
();
73
}


98
74
break;
75
}
76
case
PenaltyYellow :
77
{
78
if ( game -> getTeamColor () == YELLOW )
79
{
80
penaltyTeam ();
81
}
82
else
83
{
84
penaltyEnemy ();
85
}
86
break;
87
}
88
case
DirectFreeKickYellow :
89
{
90
if ( game -> getTeamColor () == YELLOW )
91
{
92
strategyDirectKick
();
93
}
94
else
95
{
96
strategyStop ();
97
}
98
break;
99
}
100
case
IndirectFreeKickYellow :
101
{
102
if ( game -> getTeamColor () == YELLOW )
103
{
104
strategyIndirectKick ();
105
}
106
else
107
{
108
strategyStop ();
109
}
110
break;
111
}
112
case
KickOffBlue :
113
{
114
if ( game -> getTeamColor () == BLUE )
115
{
116
strategyKickoff
();
117
}
118
else
119
{
120
strategyStop
();
121
}
122
break;
123
}
124
case
PenaltyBlue :
125
{
126
if ( game -> getTeamColor () == BLUE )
127
{
128
penaltyTeam ();
129
}
130
else
131
{
132
penaltyEnemy ();
133
}
134
break;
135
}
136
case
DirectFreeKickBlue :
137
{
138
if ( game -> getTeamColor () == BLUE )
139
{
140
strategyDirectKick
();
141
}
142
else
143
{
144
strategyStop ();
145
}
146
break;


99
147
}
148
case
IndirectFreeKickBlue :
149
{
150
if ( game -> getTeamColor () == BLUE )
151
{
152
strategyIndirectKick ();
153
}
154
else
155
{
156
strategyStop ();
157
}
158
break;
159
}
160
default:
161
{
162
strategyHalt
();
163
break;
164
}
165
}
166
}
Conforme mencionado na se¸c˜ao 3.2.1, a decis˜ao sobre qual a¸c˜ao deve ser executada
por cada um dos robˆos apresenta diferentes n´ıveis de complexidade entre os poss´ıveis
cen´arios em uma partida de futebol. Quando o comando recebido ´e ‘Stop’, a classe Strategy
n˜ao precisa processar mais nenhuma informa¸c˜ao para determinar qual estrat´egia deve ser
executada, pois esse comando deﬁne por si s´o qual a¸c˜ao deve ser executada.
Entretanto, quando o comando recebido ´e ‘Ready’, o qual pode representar o
rein´ıcio da partida ap´os a marca¸c˜ao de uma penalidade m´axima, a classe Strategy deve
avaliar o comando de prepara¸c˜ao recebido anteriormente e a cor do time que est´a sendo
controlado. Isso ´e necess´ario porque o comportamento esperado para o rein´ıcio da partida
ap´os uma penalidade m´axima a favor do time que est´a sendo controlado ´e diferente daquele
quando a penalidade ´e assinalada a favor do time advers´ario.
Nesse sentido, a classe Strategy avalia o comando de prepara¸c˜ao, com base na cor
do time que est´a sendo controlado, utilizando a estrutura de controle if-then-else, conforme
apresentado entre as linhas 16 e 55 do C´odigo 24. Uma vez avaliado o comando enviado
pela aplica¸c˜ao Referee Box e, quando necess´ario, o comando de prepara¸c˜ao, a instˆancia da
classe Strategy deﬁne ent˜ao qual estrat´egia ser´a executada pelos robˆos que comp˜oem a
equipe que est´a sendo controlada.
Entretanto, em alguns casos, a classe Strategy deve ainda determinar qual dos
robˆos ir´a executar uma determinada a¸c˜ao. Por exemplo, quando o ´arbitro determina a
paralisa¸c˜ao da partida, representado pelo comando ‘Stop’, a estrat´egia adotada ´e posicionar
alguns robˆos pr´oximos `a bola. Para isso, a aplica¸c˜ao deve escolher quais robˆos devem
deslocar-se para pr´oximo `a bola.
O m´etodo respons´avel por executar a estrat´egia ‘Stop’ ´e apresentado no C´odigo


100
25. Nas linha 8 e 9 do C´odigo 25, o m´etodo avalia a posi¸c˜ao da bola em rela¸c˜ao ao gol que
est´a sendo defendido. Se a bola estiver pr´oxima ao gol que est´a sendo defendido e o ˆangulo
entre a bola e o gol for maior que 80◦, os robˆos que possuem a fun¸c˜ao “MIDFIELD ONLY”,
“STRIKER LEFT” e “STRIKER RIGHT” devem deslocar-se para junto `a posi¸c˜ao da bola.
Caso contr´ario, al´em destes trˆes robˆos se deslocarem para pr´oximo `a bola, os defensores
devem movimentar-se para pr´oximo `a ´area de defesa.
C´odigo 25: M´etodo da classe Strategy utilizado para executar a estrat´egia Stop.
1
void
Strategy :: stop ()
2
{
3
Behavior
behavior1 = DEFENDER_LEFT ;
4
Behavior
behavior2 = DEFENDER_RIGHT ;
5
double
angle = game ->getOurGoal () ->calculateAngleTo ( game ->getBall () ->getPosition () );
6
gameFunctions -> oppositeAngle ( angle );
7
8
if (
game ->getBall () ->getPosition () ->getDistanceTo ( game ->getOurGoal () ) <= bss -> distanceMinStop
9
|| abs ( angle * 180 / PI ) > 80 )
10
{
11
NDefense ( 3,
gameFunctions ->getRobot ( MIDFIELD_ONLY ),
12
gameFunctions ->getRobot ( STRIKER_LEFT ),
13
gameFunctions ->getRobot ( STRIKER_RIGHT ));
14
}
15
else
16
{
17
NDefense ( 3,
gameFunctions ->getRobot ( MIDFIELD_ONLY ),
18
gameFunctions ->getRobot ( STRIKER_LEFT ),
19
gameFunctions ->getRobot ( STRIKER_RIGHT ));
20
21
auxStopGoal2Pl (gameFunctions ->getRobot( behavior1 ),
22
gameFunctions ->getRobot( behavior2 ));
23
}
24
}
Com a estrat´egia a ser executada e o robˆo que ir´a a executar deﬁnidos, a classe
Strategy aciona a execu¸c˜ao de diferentes m´etodos das classes Robot, RobotBehavior e
GameFunctions. Esses m´etodos realizam c´alculos matem´aticos diversos que s˜ao utilizados
pela classe Strategy para enviar os comandos necess´arios para o robˆo executar a a¸c˜ao
desejada. Tais c´alculos est˜ao relacionados ao campo de estudo da rob´otica, o qual n˜ao faz
parte do escopo principal deste trabalho e por esse motivo n˜ao ser˜ao abordados.
Os C´odigos 24 e 25 demonstram como as regras que regem o comportamento do
sistema s˜ao apresentadas de forma difusa no c´odigo-fonte PI/POO. Esta caracter´ıstica
diﬁculta o entendimento do funcionamento da aplica¸c˜ao em uma primeira vista, exigindo
grande esfor¸co intelectual de quem lˆe o c´odigo-fonte. Isto acaba por diﬁcultar a manuten¸c˜ao
do c´odigo-fonte, uma vez que pequenas altera¸c˜oes em determinados m´etodos podem causar
consequˆencias inesperadas para o comportamento da aplica¸c˜ao.


101
3.2.3
SOLUC¸ ˜OES DESENVOLVIDAS SOB O VI´ES DO PARADIGMA ORIENTADO
A NOTIFICAC¸ ˜OES
Essa se¸c˜ao apresenta o desenvolvimento de aplica¸c˜oes de controle para uma partida
de futebol de robˆos desenvolvidas sob o vi´es do PON, sendo uma desenvolvida a partir do
Framework PON C++ 2.0, outra utilizando a LingPON 1.0 e outra ainda utilizando a
LingPON 1.2. Todas as solu¸c˜oes foram constru´ıdas reaproveitando parte do c´odigo n˜ao
efetivamente l´ogico-causal da solu¸c˜ao apresentado na se¸c˜ao anterior, principalmente as
fun¸c˜oes de c´alculo referentes a movimenta¸c˜ao dos robˆos.
Apesar dos avan¸cos e contribui¸c˜oes para a LingPON apresentados neste trabalho,
a LingPON ainda apresentava certas limita¸c˜oes. Isto ´e assaz natural em linguagem que se
encontra em fase de evolu¸c˜oes. Entretanto, o fato ´e que algumas limita¸c˜oes diﬁcultavam o
desenvolvimento de aplica¸c˜oes complexas, como ´e o caso do sistema de controle Robocup.
Entre essas limita¸c˜oes pode-se destacar a diﬁculdade de realizar c´alculos matem´aticos
complexos no c´odigo fonte LingPON e a incapacidade de utilizar bibliotecas externas, tais
como bibliotecas para comunica¸c˜ao via socket.
Por esse motivo, esse trabalho prop˜oe a constru¸c˜ao de uma aplica¸c˜ao modularizada,
isto ´e, composta por um m´odulo constru´ıdo sob o vi´es do PON e outro m´odulo constru´ıdo
segundo o PI para aqueles tipos de especiﬁcidades citadas. Dessa forma, por exemplo, o
c´odigo dedicado referente `a comunica¸c˜ao via socket foi mantido em PI. Entretanto, todas
as regras l´ogico-causais da aplica¸c˜ao foram transcritas para as estruturas computacionais
do PON. A raz˜ao pela qual foi utilizada essa abordagem ´e permitir que o mesmo mo-
delo estrutural da solu¸c˜ao pudesse ser aplicado no desenvolvimento das aplica¸c˜oes PON
utilizando o Framework PON C++ 2.0, a LingPON 1.0 e a LingPON 1.2.
Dessa forma, a Figura 29 apresenta o modelo estrutural PON obtido como solu¸c˜ao
para esse estudo de caso. O modelo em PON ´e demonstrado por meio de um diagrama de
classes UML. Em tempo, neste diagrama identiﬁca-se os elementos que comp˜oem a base
de fatos FBE com o estere´otipo ≪NOP FBE ≫.
Conforme apresentado no diagrama de classes da Figura 29, o FBE Robot re-
presenta cada um dos robˆos que est˜ao sendo controlados pela aplica¸c˜ao. Nas aplica¸c˜oes
desenvolvidas utilizando o Framework PON e LingPON 1.2, as Rules que regem o compor-
tamento de cada um dos robˆos s˜ao deﬁnidas no escopo do pr´oprio FBE Robot. Em tempo,
por n˜ao suportar a declara¸c˜ao de Rules no escopo de FBEs, as Rules foram declaradas
fora do escopo do FBE Robot na solu¸c˜ao desenvolvida utilizando a LingPON 1.0. Detalhes
espec´ıﬁcos sobre cada uma das implementa¸c˜oes s˜ao apresentados nas pr´oximas se¸c˜oes.


102
Figura 29: Diagrama de classes do software de controle para partida de futebol de robˆos
em PON.
As demais classes apresentadas no diagrama da Figura 29 assemelham-se muito
`as classes utilizadas para a constru¸c˜ao da solu¸c˜ao sob o vi´es do PI e foram desenvolvidas
utilizando apenas a linguagem de programa¸c˜ao C++, sem nenhum conceito relacionado
ao PON. A instˆancia da classe RobocupController ´e respons´avel por instanciar a classe
Team. A instˆancia da classe Team, por sua vez, ´e respons´avel por criar o n´umero de
instˆancias necess´arias do FBE Robot a serem controladas pela aplica¸c˜ao. Ademais, a
instˆancia da classe Team ´e respons´avel por atualizar o estado dos Attributes das instˆancias
do FBE Robot com as informa¸c˜oes recebidas a partir do sistema SSL-Vision e da aplica¸c˜ao
RefereeBox. Neste sentido, a classe Team foi criada de forma a permitir um melhor
gerenciamento de todos os robˆos que est˜ao sendo controlados pelo sistema.
A instˆancia da classe CommunicationSystem, por sua vez, representa a interface de
comunica¸c˜ao entre a aplica¸c˜ao de controle e os robˆos. A instˆancia da classe Ball representa
a bola que est´a sendo utilizada na partida. Em um primeiro momento, Ball foi modelada
para ser um FBE. Dessa forma, seria poss´ıvel a cria¸c˜ao de Rules a partir da correla¸c˜ao dos
FBEs Robot e Ball. Um exemplo de Rule que poderia ser deﬁnida a partir da correla¸c˜ao
destes FBEs seria a Rule que deﬁne que o robˆo deve deslocar-se para bola quando a


103
distˆancia entre eles for menor que 50 cm. De forma literal, esta Rule pode ser deﬁnida
como:
Se ( (robot1.atPositionX - ball.atPositionX) <0.5) Ent˜ao robot1.mtMoveToBall()
Entretanto, as materializa¸c˜oes em software do PON (Framework PON 2.0, Ling-
PON 1.0 e LingPON 1.2) n˜ao suportam a declara¸c˜ao de opera¸c˜oes aritm´eticas na declara¸c˜ao
de Premises. Por esse motivo, Ball foi deﬁnida como uma classe PI/POO convencional ao
inv´es de ser deﬁnida como um FBE.
Desse modo, o FBE Robot possui alguns Attributes booleanos (atIsReady, at-
BallEnemyField, atClosestToBall e atEnemyOnGoalLine) que deﬁnem sua percep¸c˜ao em
rela¸c˜ao ao ambiente, incluido percep¸c˜ao sobre outros robˆos e sobre a bola. Assim, ao
receber uma nova percep¸c˜ao do ambiente, cada Robot atualiza o estado destes Attributes.
E, quando um Attribute do FBE Robot tem seu estado alterado, o mesmo notiﬁca as
Premises relacionadas `as Rules do FBE Robot.
Dessa forma, o ﬂuxo de execu¸c˜ao da aplica¸c˜ao ´e controlado pela entidade PON
FBE Robot presente na aplica¸c˜ao. Assim, evita-se reavalia¸c˜oes desnecess´arias de express˜oes
l´ogico-causais presente na solu¸c˜ao desenvolvida sob o vi´es do PI, tais como a avalia¸c˜ao do
´ultimo valor enviado pela aplica¸c˜ao Referee Box, a cada ciclo de execu¸c˜ao, mesmo quando
o mesmo n˜ao foi alterado.
Outrossim, o cerne de uma aplica¸c˜ao PON est´a na constru¸c˜ao de Rules a partir
da associa¸c˜ao de Conditions com Premises e Instigations com Actions. Dessa forma, as
Rules podem ser apresentadas em uma tabela, conforme apresentado na Tabela 1, a qual
apresenta um pequeno grupo de Rules criadas para controlar os robˆos durante uma partida
de futebol.
Rule
Nome
Condition e suas Premises
Action e suas Instigations
1
rlMOStop
RobotPON.atPlayerRole == “MIDFIELD ONLY”
RobotPON.atCmdReferee == Stop
RobotPON->mtStopAtacante
2
rlMOBlueKickoﬀ
RobotPON.atPlayerRole== “MIDFIELD ONLY”
RobotPON.atCmdReferee == KickoﬀBlue
RobotPON.atTeam == Blue
RobotPON->mtMovePositionToKick
3
rlMOBlueReadyKickoﬀ
RobotPON.atPlayerRole== “MIDFIELD ONLY”
RobotPON.atCmdReferee == Start
RobotPON.atLastCmdReferee == KickoﬀBlue
RobotPON.atTeam == Blue
RobotPON->mtReadyKickoﬀ
Tabela 1: Rules, Conditions e suas Premises e Actions instigadas do software de controle
PON para futebol de robˆos.
A primeira Rule apresentada na Tabela 1 determina que o robˆo, cuja fun¸c˜ao ´e
“MIDFIELD ONLY”, mova-se a para a posi¸c˜ao de re´ınicio de partida quando o comando


104
recebido por parte da aplica¸c˜ao RefereeBox for “Stop”. De forma semelhante, a Rule
n´umero 2 determina que o robˆo, cuja fun¸c˜ao ´e “MIDFIELD ONLY”, mova-se para a posi¸c˜ao
que o permita chutar a bola em dire¸c˜ao ao gol advers´ario quando o comando recebido por
parte da aplica¸c˜ao RefereeBox for “KickoﬀBlue” e a cor do seu time for azul (Blue). Por
ﬁm, a Rule n´umero 3 determina que o robˆo, cuja fun¸c˜ao ´e “MIDFIELD ONLY”, execute a
a¸c˜ao de chutar a bola quando a cor do seu time for azul (Blue) e os dois ´ultimos comandos
recebidos por parte da aplica¸c˜ao RefereeBox forem, respectivamente, “KickoﬀBlue” e
“Start”.
Assim, um total de 74 Rules foram cridas a partir da associa¸c˜ao de Premises e
Instigations dentro do escopo do FBE PONRobot, conforme apresentado no Apˆendice
C e aplicadas nas solu¸c˜oes desenvolvidas sob o vi´es do PON. No mais, as se¸c˜oes poste-
riores apresentam maiores detalhes sobre a implementa¸c˜ao de cada uma das aplica¸c˜oes
desenvolvidas a partir das materializa¸c˜oes visadas do PON em software.
3.2.3.1
SOLUC¸ ˜AO DESENVOLVIDA SOB O VI´ES DO FRAMEWORK PON 2.0
Essa se¸c˜ao apresenta a aplica¸c˜ao de controle para uma partida de futebol de robˆos
constru´ıda utilizando o Framework PON C++ 2.0.
Al´em de possuir Attributes e Methods, o FBE Robot foi criado apresentando
tamb´em em sua deﬁni¸c˜ao um conjunto de Rules que deﬁnem qual ser´a seu comportamento
durante a execu¸c˜ao da aplica¸c˜ao. Essa abordagem garante uma programa¸c˜ao mais modular,
na qual cada FBE possui um conjunto de Rules. Dessa forma, ao criar uma nova instˆancia
do FBE PONRobot, n˜ao somente as entidades Attributes e Methods ser˜ao criadas, como
tamb´em as demais entidades que comp˜oem uma aplica¸c˜ao PON, tais como Premises,
Conditions, Rules, Actions e Instigations [Ronszcka 2012].
Dessa forma, o fragmento de c´odigo extra´ıdo do c´odigo-fonte da solu¸c˜ao desenvol-
vida e apresentado no C´odigo 26 mostra como a Rule 3 da Tabela 1 foi constru´ıda com
a utiliza¸c˜ao do Framework C++ 2.0 do PON. No c´odigo apresentado, o operador this
utilizado na declara¸c˜ao das Premises refere-se `a pr´opria instˆancia do FBE Robot. A Rule
apresentada determina que o robˆo, cuja fun¸c˜ao atribu´ıda ´e “MIDFIELD ONLY”, inicie a
partida no meio de campo ap´os um gol do time advers´ario.


105
C´odigo 26: C´odigo de uma Rule presente em PONRobot.cpp
1
PREMISE (prRoleMidﬁeldOnly, this->atRole,
2
new String(this, “MIDFIELD ONLY”),
3
Premise::EQUAL, Premise::STANDARD, false);
4
5
PREMISE (prRefereeCmdStartGame, this->atRefereeCmd,
6
new Char(this, Referee::Ready),
7
Premise::EQUAL, Premise::STANDARD, false);
8
9
PREMISE (prLastRefereeCmdKickoﬀBlue, this->atLastRefereeCmd,
10
new Char(this, Referee::KickOﬀBlue),
11
Premise::EQUAL, Premise::STANDARD, false);
12
13
PREMISE (prTeamBlue, this->atTeamColor,
14
new String(this, “BLUE”),
15
Premise::EQUAL, Premise::STANDARD, false);
16
17
RULE (rlMOBlueReadyKickoﬀ, scheduler, Condition::CONJUNCTION) ;
18
rlMOBlueReadyKickoﬀ->addPremise(prRoleMidﬁeldOnly) ;
19
rlMOBlueReadyKickoﬀ->addPremise(prRefereeCmdStartGame) ;
20
rlMOBlueReadyKickoﬀ->addPremise(prLastRefereeCmdKickoﬀBlue) ;
21
rlMOBlueReadyKickoﬀ->addPremise(prTeamBlue) ;
22
rlMOBlueReadyKickoﬀ->addInstigation(this->mtReadyKickoﬀ) ;
3.2.3.2
SOLUC¸ ˜AO DESENVOLVIDA SOB O VI´ES DO PARADIGMA ORIENTADO
A NOTIFICAC¸ ˜OES - LINGPON 1.0
Essa se¸c˜ao apresenta a aplica¸c˜ao de controle para uma partida de futebol de robˆos
desenvolvida utilizando a atual vers˜ao da LingPON (vers˜ao 1.0).
Conforme apresentado na se¸c˜ao 3.1, na atual vers˜ao da LingPON n˜ao ´e poss´ıvel
agregar Rules `a n´ıvel de FBEs. Dessa forma, todas as Rules que regem o comportamento
de um determinado robˆo em uma partida de futebol de robˆos foram criadas referenciando
cada uma das instˆancias do FBE Robot, conforme apresentado no C´odigo 27.


106
C´odigo 27: C´odigo de uma Rule desenvolvida utilizando a atual vers˜ao da
LingPON presente em robocup.pon
1
rule rlMOBlueReadyKickoﬀBlue
2
condition
3
subcondition condition41
4
premise prMidﬁeldOnly robot1.atRole == “MIDFIELD ONLY” and
5
premise prStartGame robot1.atRefereeCmd == ‘ ’ and
6
premise prLastCmdKickoﬀBlue robot1atLastRefereeCmd == ‘K’ and
7
premise prTeamBlue robot1.atTeamColor == “BLUE”
8
end subcondition
9
end condition
10
action
11
instigation inMOBlueReadyKickoﬀBlue robot1.mtReadyKickoﬀ();
12
end action
13
end rule
Neste sentido, o conjunto de 74 Rules criadas para a instˆancia “robot1” do FBE
Robot foi replicado para as outras 5 instˆancias do FBE Robot existentes na aplica¸c˜ao.
Portanto, ao inv´es de declarar 74 Rules, foi necess´ario declarar 444 Rules, fato este que
notoriamente inﬂuenciou no tamanho e na manutenibilidade do c´odigo-fonte desenvolvido
e no tempo necess´ario para o desenvolvimento da aplica¸c˜ao.
3.2.3.3
SOLUC¸ ˜AO DESENVOLVIDA SOB O VI´ES DO PARADIGMA ORIENTADO
A NOTIFICAC¸ ˜OES - LINGPON 1.2
Essa se¸c˜ao apresenta a aplica¸c˜ao de controle para uma partida de futebol de robˆos
desenvolvida utilizando a nova vers˜ao da LingPON (vers˜ao 1.2), desenvolvida e apresentada
neste trabalho.
O FBE Robot foi constru´ıdo utilizando o conceito de FBE Rules, o qual permite
declarar Rules dentro do escopo do FBE na LingPON. Assim, cada nova instˆancia do
FBE Robot possuir´a em seu escopo Attributes, Methods e todas as Rules necess´arias para
seu controle durante uma partida de futebol de robˆos.


107
Neste sentido, o C´odigo 28 apresenta como a Rule 3 da Tabela 1, cuja imple-
menta¸c˜ao utilizando o Framework PON 2.0 foi apresentado no C´odigo 26, foi codiﬁcada
segundo as deﬁni¸c˜oes da LingPON. Essa Rule determina que o robˆo, cuja fun¸c˜ao atribu´ıda
´e “MIDFIELD ONLY”, inicie a partida no meio de campo ap´os um gol do time advers´ario.
C´odigo 28: C´odigo de uma Rule desenvolvida utilizando a nova vers˜ao da
LingPON presente em robocup.pon
1 fbe Robot
2
attributes
3
string atRole “OFF”
4
char atRefereeCmd ‘N’
5
char atLastRefereeCmd ‘N’
6
string atTeamColor “none”
7
...
8
end attributes
9
methods
10
method begin method readyKickoﬀ(); end method’
11
...
12
end methods
13
fbeRule rlMOBlueReadyKickoﬀBlue
14
condition
15
subcondition condition41
16
premise prMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY” and
17
premise prStartGame Robot.atRefereeCmd == ‘ ’ and
18
premise prLastCmdKickoﬀBlue Robot.atLastRefereeCmd == ‘K’ and
19
premise prTeamBlue Robot.atTeamColor == “BLUE”
20
end subcondition
21
end condition
22
action
23
instigation inMOBlueReadyKickoﬀBlue Robot.mtReadyKickoﬀ();
24
end action
25
end fbeRule
26
...
27 end fbe


108
A utliza¸c˜ao de FBE Rules, adicionada `a LingPON no desenvolvimento deste
trabalho, permitiu a cria¸c˜ao do c´odigo-fonte mais compacto, em termos de n´umero de
linhas de c´odigo, quando comparado `a solu¸c˜ao desenvolvida a partir da LingPON 1.0. Isto
porque apenas 74 FBE Rules foram declaradas no c´odigo-fonte, ao inv´es de 444 Rules que
foram declaradas no c´odigo-fonte LingPON 1.0.
3.2.4
COMPARAC¸ ˜OES ENTRE A APLICAC¸ ˜AO DE CONTROLE DE FUTEBOL DE
ROBˆOS DESENVOLVIDA NOS PARADIGMA ORIENTADO A OBJETOS E
NO PARADIGMA ORIENTADO A NOTIFICAC¸ ˜OES
Nesta se¸c˜ao s˜ao apresentadas algumas compara¸c˜oes entra a solu¸c˜ao desenvolvida
sob o vi´es do POO/PI e as solu¸c˜oes desenvolvidas sob o vi´es do PON; Tais compara¸c˜oes
s˜ao no tocante a medidas de complexidade de c´odigo (i.e. quantidade de linhas de c´odigo e
tokens presente no c´odigo-fonte) e facilidade de manutenibilidade. Por ﬁm, s˜ao apresentadas
as reﬂex˜oes sobre as compara¸c˜oes.
3.2.4.1
COMPARAC¸ ˜OES DE COMPLEXIDADE DE C´ODIGO-FONTE ENTRE A
APLICAC¸ ˜AO DE CONTROLE DE FUTEBOL DE ROBˆOS DESENVOLVIDA
EM PI/POO E PON
Essa se¸c˜ao apresenta o experimento realizado para comparar a complexidade
do c´odigo-fonte das aplica¸c˜oes de controle para uma partida de futebol de robˆos. Esse
experimento ´e relativo ao objetivo espec´ıﬁco deste trabalho que visa comparar a aplica¸c˜ao
desenvolvida utilizando a nova vers˜ao da LingPON com solu¸c˜oes semelhantes desenvolvidas
sob o PI/POO e outras materializa¸c˜oes do PON (nomeadamente vers˜ao anterior da
LingPON e Framework PON 2.0).
As m´etricas utilizadas para compara¸c˜oes em complexidade de c´odigo-fonte foram
n´umero de linhas de c´odigo (LOC - lines of code) e n´umero de tokens na linguagem (i.e
medidas em C++ puro, Framework PON 2.0, LingPON atual e LingPON 1.2). O objetivo
´e comparar a complexidade de c´odigo entre programas similares (i.e. que solucionam o
mesmo problema) desenvolvidos em diferentes paradigmas de programa¸c˜ao e com t´ecnicas
diferentes.
Para a contagem de linhas de c´odigo-fonte foi utilizado a ferramenta cloc [Danial
2006].
Essa ferramenta foi escolhida por ser de licen¸ca livre e open-source.
Para a


109
contagem da quantidade de tokens presentes no c´odigo-fonte, foi criado um analisar l´exico
(implementado com a ferramenta ﬂex), cujo c´odigo-fonte ´e apresentado no Apˆendice D.
A contagem do n´umero de linhas de c´odigo e quantidade de tokens presentes no
c´odigo-fonte da aplica¸c˜ao desenvolvida utilizando o Framework PON foram realizadas
desconsiderando o c´odigo-fonte do Framework PON. Foi utilizada essa abordagem porque
o desenvolvedor n˜ao necessita ter conhecimento sobre o c´odigo interno do Framework PON,
ele deve apenas utilizar as fun¸c˜oes que o mesmo disponibiliza.
A Figura 30 apresenta os dados da medi¸c˜ao global do n´umero de linhas de c´odigo.
Essa medi¸c˜ao mostra uma diferen¸ca consider´avel de quantidade de linhas de c´odigo entre as
aplica¸c˜oes desenvolvidas utilizando a atual vers˜ao da LingPON e a nova vers˜ao apresentada
neste trabalho. Essa grande diferen¸ca se deve ao fato de, na atual vers˜ao da LingPON, o
desenvolvedor ter que declarar o mesmo conjunto de Rules para cada uma das instˆancias
do FBE Robot. Utilizando o conceito de FBE Rules presente na nova vers˜ao da LingPON,
a redundˆancia na declara¸c˜ao de Rules ´e mitigada e faz com que o n´umero de linhas de
c´odigo se aproxime das solu¸c˜oes desenvolvidas a partir do PI/POO e a partir do Framework
PON.
Figura 30: Gr´aﬁco linhas de c´odigo-fonte para cada uma das solu¸c˜oes apresentadas.
Nota-se que a solu¸c˜ao desenvolvida utilizando a nova vers˜ao da LingPON apresenta


110
um n´umero maior de linhas de c´odigo quando comparado com a solu¸c˜ao desenvolvida
a partir do Framework PON. Isso se deve principalmente ao fato de o Framework PON
utilizar pseudˆonimos para evitar redundˆancias nas declara¸c˜ao de entidades PON, os quais
possuem a capacidade de realizar um conjunto de instru¸c˜oes com apenas uma ´unica
chamada, conforme apresentado em [Ronszcka 2012].
A Figura 31 apresenta os dados obtidos atrav´es da medi¸c˜ao do n´umero de tokens
presentes no c´odigo-fonte para cada uma das aplica¸c˜oes desenvolvidas. Apesar de a solu¸c˜ao
desenvolvida utilizando a nova vers˜ao da LingPON apresentar mais linhas de c´odigo em
seu c´odigo-fonte quando comparada com a solu¸c˜ao Framework PON, o n´umero de tokens
presentes no c´odigo ´e ligeiramente menor.
Figura 31: Gr´aﬁco quantidade de tokens presentes no c´odigo-fonte de cada uma das
solu¸c˜oes apresentadas.
Ademais, ao contr´ario do que ocorre na aplica¸c˜ao desenvolvida a partir do PI/POO,
observa-se atrav´es dos fragmentos de c´odigo apresentados nas subse¸c˜oes 3.2.3.1, 3.2.3.2
e 3.2.3.3 que as solu¸c˜oes desenvolvidas a partir do PON apresentam a vantagem de
ter o conhecimento l´ogico-causal da aplica¸c˜ao expl´ıcito atrav´es de Rules e centralizados
em uma ´unica regi˜ao do c´odigo-fonte. Na aplica¸c˜ao desenvolvida segundo o PI/POO,
o conhecimento l´ogico-causal encontra-se disperso em diferentes classes, fato este que
diﬁculta o entendimento da aplica¸c˜ao e sua manuten¸c˜ao, conforme ser´a explorado na
subse¸c˜ao 3.2.4.2.


111
3.2.4.2
COMPARAC¸ ˜OES DE MANUTENIBILIDADE ENTRE A APLICAC¸ ˜AO DE
CONTROLE DE FUTEBOL DE ROBˆOS DESENVOLVIDA EM PI/POO E
PON
Essa se¸c˜ao apresenta o experimento realizado para comparar o n´ıvel de manuteni-
bilidade das aplica¸c˜oes de controle para uma partida de futebol de robˆos. Esse experimento
´e relativo ao objetivo espec´ıﬁco deste trabalho que visa veriﬁcar propriedades do PON de
facilidade de programa¸c˜ao por meio de suas materializa¸c˜oes.
As atividades de manuten¸c˜ao de software s˜ao atividades que visam modiﬁcar o
c´odigo-fonte de um sistema pr´e existente [Souza 2005]. Neste sentido, as atividades de
manuten¸c˜ao podem ser funcionalmente classiﬁcadas em trˆes categorias [Arthur 1988]:
• Manuten¸c˜ao corretiva: Visa consertar defeitos de um sistema para que o mesmo ﬁque
em conformidade com o requisitos sobre os quais fora inicialmente desenvolvido.
• Manuten¸c˜ao adaptativa: Adapta o sistema de forma que o mesmo atenda novos
requisitos, sejam eles relacionados a necessidades de usu´arios ou ambiente.
• Manuten¸c˜ao perfectiva: Modiﬁca o sistema de modo a aumentar a qualidade do
c´odigo-fonte do software, sem alterar sua funcionalidade.
Visando comparar o n´ıvel de manutenibilidade do c´odigo-fonte de cada uma
das aplica¸c˜oes desenvolvidas neste trabalho, foi proposta uma atividade de manuten¸c˜ao
adaptativa. Um novo requisito funcional deveria ser adicionado em cada um dos softwares
desenvolvidos.
O requisito funcional escolhido para essa compara¸c˜ao determina que,
quando o comando recebido a partir da aplica¸c˜ao Referee Box for ‘Halt’ (i.e suspender
partida), dois robˆos devem se deslocar at´e pr´oximos a bola e permanecer efetuando troca
de passes at´e que a partida seja reiniciada. Este requisito foi proposto apenas como forma
de avaliar a manutenibilidade, n˜ao sendo uma regra real do futebol de robˆos.
As m´etricas de compara¸c˜ao utilizadas foram o tempo despendido para desenvolver
o c´odigo necess´ario para o novo requisito e a quantidade de linhas no c´odigo-fonte alteradas.
O tempo utilizado para a manuten¸c˜ao est´a diretamente ligado ao custo do processo
de manuten¸c˜ao de um software e, portanto, deﬁne a viabilidade da manuten¸c˜ao a ser
realizada [Ferreira et al. 2008]. De forma a tornar a compara¸c˜ao justa e imparcial, o
estudante de Engenharia da Computa¸c˜ao Andr´e Botta2, autor e desenvolvedor da solu¸c˜ao
de controle desenvolvida sob o vi´es do PI/POO, foi convidado a contribuir com essa
2Curr´ıculo Lattes: http://lattes.cnpq.br/5735332297553810


112
atividade. Dessa forma, uma poss´ıvel curva de aprendizado para entender o c´odigo-fonte
j´a existente n˜ao interferiria na compara¸c˜ao.
Segundo [Arthur 1988], qualquer manuten¸c˜ao adaptativa deve ser realizada a
partir das seguintes atividades: identiﬁcar partes da arquitetura envolvidas, elaborar
alternativas, avaliar alternativas e implementar a alternativa escolhida. Dessa forma, o
mesmo processo foi aplicado para a adi¸c˜ao do novo requisito funcional nos quatro sistemas
desenvolvidos.
Ap´os uma semana de atividades e algumas tentativas de codiﬁcar o novo requisito
funcional, o estudante Andr´e Botta relatou que seria necess´ario alterar a arquitetura
do c´odigo-fonte da solu¸c˜ao desenvolvida em PI/POO de forma a permitir que a mesma
suportasse esse novo comportamento. Isso se deve principalmente a forma com a qual a
l´ogica que rege o comportamento dos robˆos est´a dispersa entre diferentes classes, tais como
Strategy, RobotBehavior e GameFunctions, conforme apresentado na subse¸c˜ao 3.2.2. Sendo
assim, a adi¸c˜ao de uma nova regra l´ogico-causal para atender o novo requisito funcional
exigiria profundas altera¸c˜oes nestas trˆes classes. Isto tornou-se invi´avel uma vez que as
altera¸c˜oes necess´arias para atender o novo requisito afetariam o funcionamento das regras
j´a existentes no sistema.
N˜ao satisfeito apenas com a tentativa do estudante Andr´e Botta, o autor3 deste
trabalho tamb´em tentou realizar a adi¸c˜ao deste novo requisito funcional. Por n˜ao ter
sido o autor do c´odigo-fonte e o mesmo n˜ao apresentar uma documenta¸c˜ao t´ecnica, um
certo tempo foi investido a ﬁm de entender o funcionamento do sistema de controle
desenvolvido a partir do PI/POO. A partir do momento que o funcionamento da aplica¸c˜ao
foi compreendido, iniciou-se os esfor¸cos para adicionar o novo requisito funcional.
Ap´os cerca de 3 horas de trabalho, uma solu¸c˜ao foi proposta. A solu¸c˜ao consistia
em adicionar altera¸c˜oes nas trˆes classes respons´aveis pela deﬁni¸c˜ao de qual estrat´egia e
movimento ser´a adotada pelo robˆo, a saber as classes Strategy, RobotBehavior e Game-
Functions. Ao executar a aplica¸c˜ao com o objetivo de validar o novo requisito, veriﬁcou-se
que seu funcionamento n˜ao estava como o esperado. Ao receber o comando ‘Halt’, dois
robˆos deslocaram-se at´e pr´oximo a bola e efetuaram a primeira troca de passes.
Entretanto, ap´os realizar o primeiro passe, o robˆo desloca-se em sentido ao gol
advers´ario. Isto se deu provavelmente `a alguma regra que j´a estava deﬁnida previamente
no sistema de controle. Todavia, por apresentar regras dispersas em diferentes classes, n˜ao
foi poss´ıvel localizar a regra (ou regras) que poderia estar interferindo no funcionamento
3Curr´ıculo Lattes: http://lattes.cnpq.br/8972298057414510


113
deste novo requisito.
Posteriormente, o professor Jo˜ao Fabro4, especialista e professor de programa¸c˜ao
em PI/POO, que foi o orientador do estudante Andr´e Botta durante o desenvolvimento
do software de controle de robˆos em PI/POO apresentada neste trabalho, tamb´em foi
convidado a participar do experimento. Segundo seus relatos, foram necess´arias 4 horas de
intensa programa¸c˜ao para o desenvolvimento de uma poss´ıvel solu¸c˜ao. Entretanto, assim
como no caso do estudante Andr´e Botta, foi relatada a impossibilidade da solu¸c˜ao atender
completamente aos requisitos.
Apesar de a constru¸c˜ao do algoritmo para atender este novo requisito ser rela-
tivamente simples, sua constru¸c˜ao sob o PI/POO n˜ao ´e trivial. Conforme relatado por
prof. Fabro, a diﬁculdade de programar este novo comportamento est´a na dinamicidade
necess´aria para que os robˆos executem o passe e, na sequˆencia, se posicionem para receber
o passe de seu companheiro. Utilizando o PI/POO, o programador deve explicitar a a¸c˜ao
que deve ser executada e quando deve ser executada, de forma sequencial. Entretanto,
o futebol de robˆos ´e um ambiente dinˆamico, no qual ´e dif´ıcil prever a sequˆencia em que
diferentes situa¸c˜oes ocorrer˜ao.
Neste sentido, veriﬁcou-se que a solu¸c˜ao desenvolvida pelo prof. Fabro aproximou-
se, de certo modo, do comportamento esperado pelo novo requisito. Quando recebido o
comando ‘Halt’, o robˆo kicker se desloca em dire¸c˜ao `a bola. Entretanto, o passe n˜ao ´e
executado na dire¸c˜ao do outro robˆo (partner). Al´em disso, ap´os o primeiro passe, os robˆos
come¸cam a deslocar-se para posi¸c˜oes aleat´orias. Desse modo, a solu¸c˜ao apresentada pelo
prof. Fabro n˜ao foi capaz de atender o novo requisito funcional proposto.
Em contrapartida, a adi¸c˜ao do novo requisito foi realizada com certa facilidade nas
trˆes aplica¸c˜oes PON. Isso se deve principalmente `a forma com a qual o comportamento dos
robˆos ´e expresso atrav´es de Rules nas aplica¸c˜oes PON, facilitando a atividade de identiﬁcar
as partes da arquitetura que deveriam ser alteradas para acomodar o novo requisito.
Dessa forma, o trabalho em adicionar o novo requisito ao sistema se concentrou
em criar Rules que fossem capazes de executar a a¸c˜ao descrita pelo requisito. Por ser um
comportamento dinˆamico, que envolve tanto a percep¸c˜ao espacial do campo e movimentos,
trˆes novas Rules para cada um dos dois robˆos foram criadas. Essas Rules tem como
objetivo posicionar cada um dos robˆos pr´oximo a bola e fazer com que o robˆo que esteja
mais pr´oximo a bola se locomova at´e a mesma e efetue o passe para um companheiro.
4Curr´ıculo Lattes: http://lattes.cnpq.br/6841185662777161


114
O tempo despendido para elaborar a solu¸c˜ao, isto ´e, elaborar as Rules que
deveriam ser adicionadas ao sistema e implement´a-las foi de aproximadamente uma hora.
Primeiramente, essa solu¸c˜ao foi desenvolvida no c´odigo-fonte LingPON 1.2. Posteriormente,
o mesmo conjunto de Rules foi aplicado `as solu¸c˜oes desenvolvidas a partir do Framework
PON e da LingPON 1.0.
A primeira Rule adicionada determina que, dado a condi¸c˜ao ‘Halt’ de partida, o
robˆo deve movimentar-se para a linha que divide os lados do campo da partida. A segunda
Rule determina que, se o robˆo for o jogador que est´a mais pr´oximo `a bola e se n˜ao houver
nenhum obst´aculo entre ele e o robˆo que ir´a receber o passe, o robˆo deve deslocar-se em
dire¸c˜ao `a bola. Por ﬁm, a terceira Rule determina que o robˆo deve tocar a bola para seu
companheiro quando estiver pr´oximo a bola. As Rules aqui descritas s˜ao apresentadas em
Framework PON e LingPON 1.2, respectivamente, nos C´odigo 29, 30 e 31.
O mesmo conjunto de Rules foi aplicado `a solu¸c˜ao desenvolvida utilizando a
LingPON 1.0. Entretanto, dada suas limita¸c˜oes, cada uma das Rules criadas foi relacionada
a uma instˆancia do FBE Robot. Portanto, foi necess´ario adicionar 18 novas Rules ao
sistema.


115
C´odigo 29: C´odigo das Premises criadas em Framework PON para atender
o novo requisito funcional.
1
PREMISE (prRoleStrickerRight, this->atRole,
2
new String(this, “STRIKER RIGHT”),
3
Premise::EQUAL, Premise::STANDARD, false);
4
5
PREMISE (prRefereeCmdHalt, this->atRefereeCmd,
6
new Char(this, ‘H’),
7
Premise::EQUAL, Premise::STANDARD, false);
8
9
PREMISE (prNotClosestToBall, this->atClosestToBall,
10
new Boolean(this, false),
11
Premise::EQUAL, Premise::STANDARD, false);
12
13
PREMISE (prClosestToBall, this->atClosestToBall,
14
new Boolean(this, true),
15
Premise::EQUAL, Premise::STANDARD, false);
16
17
PREMISE (prNotSetPassBall, this->atSetPassBall,
18
new Boolean(this, false),
19
Premise::EQUAL, Premise::STANDARD, false);
20
21
PREMISE (prSetPassBall, this->atSetPassBall,
22
new Boolean(this, true),
23
Premise::EQUAL, Premise::STANDARD, false);
24


116
C´odigo 30: C´odigo das Rules criadas em Framework PON para atender o
novo requisito funcional.
1
RULE (rlSRHaltNotClose, scheduler, Condition::CONJUNCTION) ;
2
rlSRHaltNotClose->addPremise(prRoleStrickerRight) ;
3
rlSRHaltNotClose->addPremise(prRefereeCmdHalt) ;
4
rlSRHaltNotClose->addPremise(prNotClosestToBall) ;
5
rlSRHaltNotClose->addInstigation(this->mtMoveRightWarmUp);
6
RULE (rlSRHaltClose, scheduler, Condition::CONJUNCTION) ;
7
rlSRHaltClose->addPremise(prRoleStrickerRight) ;
8
rlSRHaltClose->addPremise(prRefereeCmdHalt) ;
9
rlSRHaltClose->addPremise(prClosestToBall) ;
10
rlSRHaltClose->addPremise(prNotSetPassBall) ;
11
rlSRHaltClose->addInstigation(this->mtMoveIndirectKick);
12
13
RULE (rlSRHaltCloseReady, scheduler, Condition::CONJUNCTION)
14
rlSRHaltCloseReady->addPremise(prRoleStrickerRight)
15
rlSRHaltCloseReady->addPremise(prRefereeCmdHalt)
16
rlSRHaltCloseReady->addPremise(prClosestToBall)
17
rlSRHaltCloseReady->addPremise(prSetPassBall)
18
rlSRHaltCloseReady->addInstigation(this->mtMoveIndirectKick)


117
C´odigo 31:
C´odigo das Rules criadas em LingPON para atender o novo
requisito funcional.
1
fbeRule rlSRHaltNotClose
2
condition
3
premise prStrickerRight Robot.atRole == “STRIKER RIGHT” and
4
premise prRefereeCmdHalt Robot.atRefereeCmd == ‘H’ and
5
premise prNotClosestToBall Robot.atClosestToBall == false
6
end condition
7
action
8
instigation inSRHaltNotClose Robot.mtMoveRightWarmUp();
9
end action
10
end fbeRule
11
12
fbeRule rlSRHaltClose
13
condition
14
premise prStrickerRight Robot.atRole == “STRIKER RIGHT” and
15
premise prRefereeCmdHalt Robot.atRefereeCmd == ‘H’ and
16
premise prNotClosestToBall Robot.atClosestToBall == true and
17
premise prFreePartner Robot.atPartnerFreeID >=0 and
18
premise prNotSetPassBall Robot.atSetPassBall == false and
19
end condition
20
action
21
instigation inSRHaltClose Robot.mtMoveIndirectKick();
22
end action
23
end fbeRule
24
25
fbeRule rlSRHaltCloseReady
26
condition
27
premise prStrickerRight Robot.atRole == “STRIKER RIGHT” and
28
premise prRefereeCmdHalt Robot.atRefereeCmd == ‘H’ and
29
premise prNotClosestToBall Robot.atClosestToBall == true and
30
premise prFreePartner Robot.atPartnerFreeID >=0 and
31
premise prNotSetPassBall Robot.atSetPassBall == true
32
end condition
33
action
34
instigation inSRHaltCloseReady Robot.mtPassBallPartner();
35
end action
36
end fbeRule


118
Sendo assim, 80 novas linhas de c´odigo foram adicionadas ao c´odigo-fonte LingPON
1.2, 34 novas linhas ao c´odigo-fonte Framework PON e 534 novas linhas na solu¸c˜ao
desenvolvida utilizando a LingPON 1.0. Novamente, o menor n´umero de linhas de c´odigo
necess´arias para a solu¸c˜ao no c´odigo-fonte da solu¸c˜ao desenvolvida a partir do Framework
PON se d´a devido a utiliza¸c˜ao de pseudˆonimos para evitar redundˆancias nas declara¸c˜oes
de entidades PON, conforme apresentado em [Ronszcka 2012]. Ademais, a LingPON, em
sua origem, foi projetada para ser mais verbosa com o objetivo de ser mais facilmente
entendida.
3.2.5
REFLEX˜AO SOBRE AS COMPARAC¸ ˜OES
Como reﬂex˜oes ﬁnais desta se¸c˜ao de compara¸c˜oes, ´e pertinente ressaltar que as
aplica¸c˜oes foram comparadas a partir da solu¸c˜ao de um problema comum, a saber, um
sistema de controle para partida de futebol de robˆos.
Em um primeiro momento, foi comparada a complexidade de c´odigo-fonte entre
as quatro solu¸c˜oes apresentadas, utilizando como crit´erios a quantidade de linhas de c´odigo
e n´umero de tokens. Ao comparar as aplica¸c˜oes desenvolvidas utilizando a LingPON,
´e poss´ıvel observar reais avan¸cos da LingPON em sua nova vers˜ao.
O c´odigo-fonte
desenvolvido utilizando a nova vers˜ao da LingPON (1.2) apresentou 60.87% menos linhas
de c´odigo e 50% menos tokens do que na vers˜ao 1.0.
Em termos de linhas de c´odigo e tokens presentes no c´odigo-fonte, as solu¸c˜oes
desenvolvidas sob o vi´es do PON, utilizando o Framework PON e a LingPON 1.2, apre-
sentaram resultados melhores em rela¸c˜ao aos obtidos a partir da aplica¸c˜ao PI/POO. Isso
indica que o PON apresenta uma sintaxe t˜ao concisa quanto a encontrada na linguagem
C++, utilizada no desenvolvimento da aplica¸c˜ao PI/POO.
Entre as solu¸c˜oes PON, a aplica¸c˜ao desenvolvida utilizando a LingPON 1.2 apre-
sentou maior quantidade de linhas de c´odigo e menos tokens em seu c´odigo-fonte. Conforme
apresentado, o Framework PON utiliza pseudˆonimos criados atrav´es da linguagem de
programa¸c˜ao C++ para reduzir o n´umero de instru¸c˜oes utilizadas na cria¸c˜ao de entidades
PON, conforme apresentado em [Ronszcka 2012]. Neste sentido, acredita-se que a lingua-
gem de programa¸c˜ao PON pode ser ainda evolu´ıda no sentido de tornar as declara¸c˜oes mais
concisas, semelhante ao que foi feito no Framework PON com a utiliza¸c˜ao de pseudˆonimos.


119
Com isso, a LingPON apresentaria uma capacidade de representa¸c˜ao ainda maior.
Entretanto, as m´etricas de complexidade de c´odigo n˜ao est˜ao necessariamente
relacionadas a facilidade de programa¸c˜ao inerente a cada um dos paradigmas de pro-
grama¸c˜ao e suas linguagens de programa¸c˜ao. Ao desenvolver exatamente a mesma classe,
utilizando duas linguagens de programa¸c˜ao diferentes (i.e C++ e Java), a quantidade de
linhas de c´odigo e tokens presentes em cada uma das solu¸c˜oes ser´a certamente diferente,
uma vez que a sintaxe utilizada na constru¸c˜ao da classe ´e diferente para cada linguagem
de programa¸c˜ao. Entretanto, por se tratar da mesma classe, com m´etodos e atributos
idˆenticos, a complexidade em ambas ser´a a mesma. Isso justiﬁca o fato de tais m´etricas
n˜ao apresentarem signiﬁcado completo quando utilizadas de forma independente.
Por esse motivo, decidiu-se comparar o n´ıvel de manutenibilidade entre as solu¸c˜oes
de forma pr´atica, isto ´e, atrav´es da adi¸c˜ao de um novo requisito funcional ao sistema. O
requisito funcional foi escolhido de forma a n˜ao favorecer nenhuma das solu¸c˜oes. Neste
ˆambito, visando apresentar uma compara¸c˜ao imparcial, isto ´e, sem favorecimento do objeto
de estudo (PON), o autor da aplica¸c˜ao desenvolvida a partir do PI/POO foi convidado a
participar do experimento.
Esse experimento destacou a diﬁculdade em adicionar um novo requisito funcional
ao sistema desenvolvido segundo o PI/POO, o qual acabou por n˜ao ser adicionado devido
`a constata¸c˜ao de que tal altera¸c˜ao resultaria em altera¸c˜oes em diversas classes da aplica¸c˜ao.
Por outro lado, a adi¸c˜ao de um novo requisito funcional nos sistemas desenvolvidos sob o
vi´es do PON se deu de maneira direta, atrav´es da adi¸c˜ao de algumas Rules que ﬁzeram o
sistema atender o novo requisito funcional.
Ao comparar a diﬁculdade em adicionar um novo requisito nas aplica¸c˜oes desen-
volvidas a partir da LingPON ´e poss´ıvel observar que a LingPON 1.0 necessita de muito
mais linhas de c´odigo para resolver o mesmo problema quando comparada a LingPON 1.2.
Ao utilizar o conceito de FBE Rule, introduzido na nova vers˜ao da LingPON, foi poss´ıvel
solucionar o problema com apenas 80 novas linhas de c´odigo contra as 534 necess´arias
na atual vers˜ao da LingPON. Isso representa uma economia de aproximadamente 85%
de linhas de c´odigo e tem impacto direto na velocidade de desenvolvimento e do n´ıvel de
manutenibilidade da aplica¸c˜ao, uma vez que ´e mais f´acil manter 80 linhas de c´odigo ao
inv´es de 534.
A Tabela 2 apresenta de forma resumida os resultados obtidos a partir dos dois
experimentos apresentados neste cap´ıtulo.


120
Tabela 2: Resultados obtidos a partir dos experimentos de contabilidade de linhas de
c´odigo e quantidade de tokens presentes no c´odigo fonte e n´ıvel de manutenibilidade.
Aplica¸c˜ao
No de linhas
No de tokens
Foi poss´ıvel adicionar
o novo requisito?
PI/POO= C++
3649
23611
N˜ao
FW PON C++ 2.0
3232
21229
Sim
LingPON 1.0
8578
38142
Sim
LingPON 1.2
3357
19073
Sim


121
4
CONCLUS˜AO E TRABALHOS FUTUROS
Este cap´ıtulo apresenta as conclus˜oes deste trabalho e indica poss´ıveis trabalhos
futuros. Desta forma, a se¸c˜ao 4.1 apresenta a conclus˜ao dessa disserta¸c˜ao de mestrado,
relacionando as contribui¸c˜oes da mesma. Por ﬁm, a se¸c˜ao 4.2 vislumbra trabalhos futu-
ros que poder˜ao contribuir para a consolida¸c˜ao da LingPON e, consequentemente, do
Paradigma Orientado a Notiﬁca¸c˜oes (PON).
4.1
CONCLUS˜AO
Este trabalho teve como um dos objetivos a evolu¸c˜ao da linguagem de programa¸c˜ao
LingPON e seu respectivo compilador (i.e. da tecnologia LingPON) no tocante a facilidade
de programa¸c˜ao, visando facilitar a cria¸c˜ao de aplica¸c˜oes PON. Ademais, este trabalho teve
tamb´em como objetivo a elabora¸c˜ao de uma aplica¸c˜ao PON de complexidade reconhecida
(futebol de robˆos), utilizando diferentes materializa¸c˜oes (i.e. implementa¸c˜oes) em software
do PON, a serem comparadas com a mesma aplica¸c˜ao desenvolvida sob o vi´es do PI por
outrem.
Inicialmente, a quest˜ao de paradigmas de programa¸c˜ao foi apresentada de maneira
sucinta, a luz de trabalhos anteriores desenvolvidos pelo grupo de pesquisa PON da
UTFPR. Subsequentemente, tanto o PON quanto as suas duas principais materializa¸c˜oes
em software (ent˜ao vigentes), nomeadamente Framework PON 2.0 e LingPON 1.0, foram
detalhadas. Posteriormente, foram apresentadas algumas limita¸c˜oes da atual vers˜ao da
LingPON (vers˜ao 1.0), as quais tornam o desenvolvimento de aplica¸c˜oes PON lento e
complicado.
Visando solucionar tais limita¸c˜oes e permitir a cria¸c˜ao de aplica¸c˜oes PON com
menor esfor¸co, foram propostos dois avan¸cos `a LingPON. O primeiro avan¸co proposto
permite maior encapsulamento do ˆambito de FBEs por meio de declara¸c˜ao de Attributes
de tipos n˜ao primitivos, isto ´e, Attributes que sejam deﬁnidos por outros FBEs. O segundo
avan¸co proposto permite ao desenvolvedor declarar Rules no ˆambito de FBE, garantindo


122
assim que todas as instˆancias de um dado FBE possuam um determinado conjunto de
Rules. Portanto, os avan¸cos s˜ao `a luz de relacionamentos de agrega¸c˜ao dado que nesta
nova vers˜ao da tecnologia LingPON FBEs podem agregar outros FBEs e/ou Rules.
Inclusive para validar a evolu¸c˜ao da LingPON apresentada neste trabalho, foi
proposto o desenvolvimento de aplica¸c˜oes de controle para uma partida de futebol de
robˆos, segundo caracter´ısticas da categoria SSL da Robocup. Na verdade, tais aplica¸c˜oes
foram desenvolvidas utilizando o Framework PON 2.0, a LingPON 1.0 e a nova vers˜ao da
LingPON (chamada de LingPON 1.2). Como apresentado na subse¸c˜ao 2.3.2.2 (e mesmo
no Apˆendice D), nenhuma aplica¸c˜ao com tamanha complexidade, em termos de n´umero de
Rules (que demandassem reﬂex˜ao1) e instˆancias de FBEs, foi desenvolvida at´e o presente
momento utilizando a LingPON. Dessa forma, a aplica¸c˜ao de controle para uma partida de
futebol de robˆos, desenvolvida e apresentada neste trabalho, representa um grande avan¸co
para a tecnologia LingPON, contribuindo para seu avan¸co como linguagem de programa¸c˜ao.
Por consequˆencia, contribui tamb´em com o PON em si, n˜ao s´o pela complexidade da
aplica¸c˜ao, mas tamb´em por haver compara¸c˜oes com aplica¸c˜ao funcionalmente equivalente
desenvolvida em POO por outrem.
De fato, as solu¸c˜oes desenvolvidas para aplica¸c˜ao de controle de futebol de robˆos
LingPON 1.0, LingPON 1.2 e Framework PON 2.0 foram submetidas a compara¸c˜oes com
uma aplica¸c˜ao funcionalmente equivalente, constru´ıda por outro desenvolvedor, sobre o PI
POO C++. Este desenvolvimento em PI, feito por outrem, foi realizado antes da elabora¸c˜ao
e dos esfor¸cos dessa presente disserta¸c˜ao [Botta 2012]. Em tempo, tais compara¸c˜oes se
deram segundo indicadores de complexidade de c´odigo, especiﬁcamente linhas de c´odigo e
quantidade de tokens presentes no c´odigo-fonte, e n´ıvel de manutenibilidade. O n´umero
de linhas de c´odigo presente no c´odigo-fonte de cada uma das aplica¸c˜oes apresentadas foi
mensurado utilizando a ferramenta cloc [Danial 2006]. Para calcular o n´umero de tokens
presente no c´odigo-fonte em cada uma das aplica¸c˜oes apresentadas foi desenvolvido um
analisador l´exico a partir da ferramenta ﬂex. O n´ıvel de manutenibilidade, por sua vez,
foi medido atrav´es do tempo necess´ario para que um programador pudesse adicionar um
requisito funcional comum `as aplica¸c˜oes PON e PI.
No tocante a complexidade de c´odigo-fonte, foi poss´ıvel observar que a nova vers˜ao
da LingPON (vers˜ao 1.2), apresentada neste trabalho, permitiu a cria¸c˜ao de uma aplica¸c˜ao
funcionalmente idˆentica a desenvolvida a partir da atual vers˜ao da LingPON (vers˜ao
1.0) mas utilizando 61% menos linhas de c´odigo e 50% menos tokens. Isto inﬂuencia
1Rules que n˜ao fossem nas Premises apenas combina¸c˜ao simples de avalia¸c˜ao de instˆancias de FBEs.


123
diretamente na velocidade de desenvolvimento de aplica¸c˜oes PON atrav´es da LingPON e
fez com que o c´odigo-fonte LingPON apresentasse indicadores de complexidade de c´odigo
muito pr´oximos aos apresentados pela solu¸c˜ao em PI e a solu¸c˜ao desenvolvida utilizando o
Framework PON 2.0.
Atrav´es do experimento de n´ıvel de manutenibilidade, foi poss´ıvel observar que o
PON apresenta indicadores de maior expressividade em programa¸c˜ao quando comparado
ao PI, pois apresenta de forma mais expl´ıcita e coesa o conjunto de regras l´ogico-causais
que regem o comportamento do sistema. Isto se deve principalmente pela forma na qual
o conhecimento l´ogico-causal da aplica¸c˜ao PON ´e representado. Em PON, isso se d´a na
forma de regras expl´ıcitas coesas em base de regras, as quais, entretanto, s˜ao tratadas
por entidades orientadas a notiﬁca¸c˜ao chamadas Rules gerando o devido desacoplamento.
Essa caracter´ıstica contribui para um f´acil entendimento do c´odigo-fonte e consequente
aumento do n´ıvel de manutenibilidade. De fato, pelo experimento, percebeu-se que alterar
e/ou adicionar requisitos se torna mais f´acil nas aplica¸c˜oes PON quando comparadas a
aplica¸c˜ao PI.
Conforme os resultados apresentados, este trabalho contribuiu para a redu¸c˜ao da
complexidade de c´odigo em aplica¸c˜oes desenvolvidas utilizando a LingPON. Ao utilizar os
novos conceitos apresentados neste trabalho, em suma FBEs que podem agregar outros
FBEs e/ou Rules, ´e poss´ıvel desenvolver aplica¸c˜oes PON com c´odigo-fonte mais enxuto.
Desse modo, isso corrobora para o desenvolvedor encontrar ainda maior facilidade em
adicionar ou alterar as entidades PON presentes no c´odigo-fonte. Isto foi demonstrado
atrav´es do experimento de n´ıvel de manutenibilidade, no qual foi poss´ıvel observar ser
necess´ario utilizar 85% menos linhas de c´odigo na LingPON 1.2, quando comparada a
LingPON 1.0, para solucionar o problema proposto.
Tudo isto considerado, ´e poss´ıvel concluir que os avan¸cos relativos a LingPON
apresentados neste trabalho mostram-se promissores e certamente contribuem no caminho
para ajudar a consolidar o PON e sua respectiva linguagem de programa¸c˜ao como alterna-
tiva para o desenvolvimento de software. Utilizando a vers˜ao 1.2 da LingPON, proposta,
implementada e avaliada neste trabalho, foi poss´ıvel desenvolver um software complexo,
com maior n´umero de Rules (com conhecimento n˜ao ‘repetitivo’), instˆancias de FBEs e
aﬁns do que as aplica¸c˜oes que haviam sido desenvolvidas anteriormente. Ademais, a nova
vers˜ao da LingPON oferece maior concis˜ao e facilidade de programa¸c˜ao ao desenvolvedor
que deseja utilizar a LingPON, permitindo assim maior manutenibilidade e simplicidade
de programa¸c˜ao, tanto em rela¸c˜ao `a vers˜ao 1.0 da LingPON quanto at´e mesmo com rela¸c˜ao


124
`a uma implementa¸c˜ao em PI/POO.
Uma vez apresentada as conclus˜oes deste trabalho nesta presente sub-se¸c˜ao, na
pr´oxima s˜ao apresentados poss´ıveis trabalhos futuros, os quais podem contribuir para a
evolu¸c˜ao da tecnologia LingPON.
4.2
TRABALHOS FUTUROS
Apesar de bem apresentar caracter´ısticas que facilitam o desenvolvimento e
principalmente a manutenibilidade de softwares, o desenvolvimento de aplica¸c˜oes LingPON
´e ainda comprometido por algumas limita¸c˜oes remanescentes de sua materializa¸c˜ao.
Neste sentido, esta se¸c˜ao apresenta perspectivas de pesquisas que possam contribuir
para avan¸cos do estado da t´ecnica do PON.
4.2.1
SUPORTE A M´ULTIPLOS ARQUIVOS DE C´ODIGO-FONTE
Atualmente, o compilador PON suporta apenas a compila¸c˜ao de um ´unico arquivo
de c´odigo-fonte por vez. Dessa forma, o desenvolvedor deve escrever o c´odigo necess´ario
para sua aplica¸c˜ao em um ´unico arquivo c´odigo-fonte. Com isso, o arquivo de c´odigo-fonte
tende a ser demasiadamente extenso.
Uma poss´ıvel solu¸c˜ao para tal problema seria alterar o compilador de forma que
o mesmo permitisse referenciar arquivos externos. Dessa forma, seria poss´ıvel separar a
declara¸c˜ao de diferentes entidades PON em diferentes arquivos, tais como um arquivo para
cada FBE. Isso contribuiria para a redu¸c˜ao da extens˜ao dos arquivos de c´odigo fonte e,
consequentemente, melhor organiza¸c˜ao.
4.2.2
UTILIZAC¸ ˜AO DE BIBLIOTECAS EXTERNAS
Por se tratar de uma linguagem de programa¸c˜ao rec´em criada, a LingPON ainda
n˜ao suporta algumas funcionalidades acess´orias para o desenvolvimento de certas aplica¸c˜oes,
como comunica¸c˜ao via socket e intera¸c˜ao com interfaces de usu´ario. Para contornar essa
limita¸c˜ao, o desenvolvedor deve utilizar mecanismos n˜ao convencionais, tais como alterar
o c´odigo-fonte gerado pelo compilador PON de forma a adicionar as funcionalidades
necess´arias em sua aplica¸c˜ao.
Essa limita¸c˜ao da LingPON foi um dos fatores cr´ıticos que inﬂuenciaram no
desenvolvimento das aplica¸c˜oes apresentadas no estudo de caso. Por n˜ao permitir importar


125
e utilizar bibliotecas externas, o c´odigo-alvo gerado pelo compilador PON a partir do
c´odigo-fonte LingPON teve de ser manualmente alterado para que funcionasse corretamente.
Para solucionar essa limita¸c˜ao, uma poss´ıvel solu¸c˜ao seria permitir ao desenvolve-
dor referenciar e executar m´etodos de bibliotecas externas utilizando a pr´opria sintaxe
da LingPON. Isto seria algo semelhante ao que acontece na programa¸c˜ao utilizando a
linguagem de programa¸c˜ao C++.
4.2.3
SIMPLIFICAC¸ ˜AO DA SINTAXE DA LINGPON
Em sua origem, a LingPON foi concebida com o objetivo de ser did´atica em
termos de entidades PON. Por esse motivo, ao desenvolver uma aplica¸c˜ao utilizando a
LingPON ´e not´orio a percep¸c˜ao, por parte do desenvolvedor, de redundˆancia de keywords
ao se declarar as entidades PON, principalmente Rules. Isso se deve a necessidade em ter
que declarar se¸c˜oes de conditions, subConditions, premises, actions e instigations para
cada Rule.
Essa ideia segue no mesmo sentido dos avan¸cos apresentados por linguagens de
programa¸c˜ao consolidadas na ind´ustria de software, tais como C++ e Java, as quais
buscam permitir a constru¸c˜ao de c´odigo-fonte com o menor n´umero de instru¸c˜oes e linhas
de c´odigo poss´ıveis. Portanto, um poss´ıvel avan¸co para a LingPON seria a redeﬁni¸c˜ao
de sua sintaxe de forma a reduzir o n´umero de instru¸c˜oes e keywords necess´arias para a
constru¸c˜ao das entidades PON, algo semelhante ao que foi feito no Framework PON 2.0
com a utiliza¸c˜ao de pseudˆonimos [Ronszcka 2012].
Neste ˆambito, muito recentemente os discentes da disciplina de Linguagens e
Compiladores de 2016 do PPGCA/UTPFR2 criaram uma nova vers˜ao do LingPON, ainda
de todo prototipal, chamada (temporariamente ao menos) de LigPON NameSpace. Nesta
vers˜ao, em temos de linguagens, j´a se pode obter alguma redu¸c˜ao ou simplicidade do
escrever do c´odigo, conforme pode ser observado no Anexo E 3. Estes esfor¸cos podem ser
reaproveitados nos avan¸cos subsequentes da LingPON.
4.2.4
TESTE DE UNIDADE PARA O COMPILADOR
Por se tratar de um projeto em equipe, no qual diversos pesquisadores est˜ao
trabalhando simultaneamente e o utilizando em suas pesquisas, faz-se necess´ario garantir
2Disciplina “Linguagens e Compiladores” ofertada pelo PPGCA da UTFPR em 2016, ministrada por
Prof. Dr. Jo˜ao Alberto Fabro e Prof. Dr. Jean Marcelo Sim˜ao.
3O relat´orio t´ecnico apresentado no Anexo E foi entregue em Mar¸co de 2017.


126
que o compilador PON esteja sempre funcionado de acordo com seus requisitos.
Uma forma simples e f´acil de garantir essa condi¸c˜ao ´e a utiliza¸c˜ao correta de
testes automatizados que visam veriﬁcar se todos os requisitos continuam funcionando
corretamente ap´os cada altera¸c˜ao no c´odigo-fonte. Isso pode ser alcan¸cado atrav´es de
testes de unidade (unit tests), os quais testam se todos os m´etodos envolvidos no processo
de compila¸c˜ao est˜ao funcionando corretamente.
Caso uma altera¸c˜ao mude o comportamento esperado do compilador, isso pode
ser identiﬁcado de forma mais r´apida, sem afetar os demais usu´arios do compilador.
4.2.5
MELHORAR EXPERIMENTO DE N´IVEL DE MANUTENIBILIDADE
Este trabalho apresentou uma compara¸c˜ao de n´ıvel de manutenibilidade entre
aplica¸c˜oes PON, desenvolvidas utilizando o Framework PON 2.0, a LingPON 1.0 e a
LingPON 1.2, e uma aplica¸c˜ao desenvolvida em linguagem C++ POO/PI.
Por se tratar de uma aplica¸c˜ao complexa e voltada a uma situa¸c˜ao muito espec´ıﬁca
(partida de futebol de robˆos), essa compara¸c˜ao foi realizada com a participa¸c˜ao de apenas
trˆes desenvolvedores, a saber o estudante de Engenharia da Computa¸c˜ao Andr´e Botta, o
autor deste trabalho e o prof. Dr. Jo˜ao Fabro.
Essa compara¸c˜ao foi ´util para o desenvolvimento deste trabalho e permitiu observar
que o PON apresenta indicadores de um c´odigo-fonte mais expressivo, leg´ıvel e com maior
n´ıvel de manutenibilidade.
Entretanto, de forma a validar essa observa¸c˜ao, seria interessante repetir tal
experimento utilizando outras aplica¸c˜oes e envolvendo mais pessoas, de forma a melhorar
a conﬁabilidade dos resultados.
4.2.6
ESTUDO DE AGENTES APLICADOS AO PON
Em [Sim˜ao 2001] foi apresentada uma arquitetura de controle dinˆamico e a eventos
discretos de sistemas ﬂex´ıveis de manufatura (FMS), a qual era baseada em regras e
agentes. Em suma essa arquitetura acabou por se tornar o chamado Controle Orientado a
Notiﬁca¸c˜oes (CON). Nos anos subsequentes, essa arquitetura de CON evoluiu at´e se tornar
um paradigma de programa¸c˜ao, nomeadamente o PON.. Portanto, o PON encontrou
inspira¸c˜ao em conceitos oriundos da programa¸c˜ao orientada a agentes, particularmente
nos agentes reativos [Sim˜ao et al. 2001,Sim˜ao et al. 2001,Sim˜ao e Stadzisz 2002,Sim˜ao et


127
al. 2003].
A ideia geral de Programa¸c˜ao Orientada a Agentes (AOP) n˜ao ´e algo novo em
si. O primeiro trabalho a trazer esse conceito foi publicado em 1993 [Shoham 1993]. O
objetivo da Programa¸c˜ao Orientada a Agentes introduzida por Shoham foi a apresenta¸c˜ao
de um novo n´ıvel de abstra¸c˜ao p´os orienta¸c˜ao a objetos, fornecendo recursos de mais alto
n´ıvel [Ricci e Santi 2011].
Entretanto, nota-se que a programa¸c˜ao orientada a agentes ainda n˜ao teve impacto
signiﬁcativo nas pesquisas em linguagens de programa¸c˜ao e desenvolvimento de software
at´e hoje [Ricci e Santi 2011]. Isto se deve possivelmente ao fato de que os maiores esfor¸cos
ainda se concentraram em quest˜oes te´oricas relacionadas a agentes, ao inv´es de focar em
sua aplicabilidade para a computa¸c˜ao pr´atica [Ricci e Santi 2011] 4.
Outrossim, a aplica¸c˜ao de Futebol de Robˆos tamb´em atrai a comunidade que
trabalha no assunto de agentes. Em tempo, h´a tamb´em aplica¸c˜oes outras de agentes
em outros dom´ınios, como em aplica¸c˜oes de cunho industrial [Banaszewski 2009]. Enﬁm,
mesmo que haja ainda estudos de cunho te´orico ou acadˆemico no tocante a agentes,
salientando aqui a Programa¸c˜ao Orientada a Agentes (POA), haveria uma tendˆencia
natural a se estudar aplica¸c˜ao de agentes em situa¸c˜ao cada vez mais reais.
Neste sentido, um trabalho futuro seria pesquisar quais seriam as sinergias entre
PON e as tem´aticas de agentes, sublinhando LingPON e AOP. Talvez agentes e POA
permitam aprimorar o PON/LingPON ou reciprocamente o PON/LingPON possa ser um
viabilizador te´orico-tecnol´ogico do POA e aﬁns.
4Enquanto material de suporte, o Apˆendice E traz um resumo sobre Programa¸c˜ao Orientada a Agentes
e aﬁns


128
REFERˆENCIAS
AHO, A. V.; SETHI, R.; ULLMAN, J. D. Compiladores: Princıpios, t´ecnicas e ferramentas.
LTC, Rio de Janeiro, Brasil, 1995.
ARTHUR, L. J. Software evolution: the software maintenance challenge. [S.l.]:
Wiley-Interscience, 1988.
ASADA, M.; ICHINODA, S.; HOSODA, K. Action-based sensor space segmentation for
soccer robot learning. Applied Artiﬁcial Intelligence, Taylor & Francis, v. 12, n. 2-3,
p. 149–164, 1998.
ASADA, M. et al. Robocup: Today and tomorrow. Experimental Robotics VI, Springer
Science & Business Media, v. 250, p. 369, 1999.
BANASZEWSKI, R. F. Paradigma orientado a notiﬁca¸c˜oes: avan¸cos e compara¸c˜oes.
2009. Master in Science Thesis, Graduate School in Electrical Engineering and Industrial
Computer Science (CPGEI) at the Federal University of Technology - Paran´a (UTFPR).
Curitiba, Brazil. Dispon´ıvel em: http://files.dirppg.ct.utfpr.edu.br/cpgei/Ano_
2009/dissertacoes/Dissertacao_500_2009.pdf.
BANASZEWSKI, R. F. Proposta e implementaC¸ ˜Ao de um modelo cognitivo para agentes
de software baseado no paradigma orientado a notiﬁcaC¸ ˜Oes. 2009. Plano de Doutorado.
Curitiba - PR Brasil: CPGEI/UTFPR.
BATISTA, M. V. Proposta de um m´etodo de aplica¸c˜ao da teoria de projeto axiom´atico ao
desenvolvimento de software pon-por. Curitiba, 2013. Disserta¸c˜ao (Mestrado em Engenharia
El´etrica e Inform´atica Industrial) - Universidade Tecnol´ogica Federal do Paran´a. Dispon´ıvel
em: http://repositorio.utfpr.edu.br/jspui/handle/1/613.
BELMONTE, D.; SIMAO, J. M.; STADZISZ, P. C. Proposta de um m´etodo para distri-
bui¸c˜ao de carga de trabalho usando o paradigma orientado a notiﬁca¸c˜oes (pon). Revista
SODEBRAS, v. 8, n. 84, 2012.
BELMONTE, D. L. et al. A new method for dynamic balancing of workload and scalability
in multicore systems. IEEE Latin America Transactions, IEEE, v. 14, n. 7, p. 3335–
3344, 2016.
BOTTA, A. L. C. Modelos artiﬁciais integrados ao software de controle do time de futebol
de robˆos da utfpr. In: Sicite 2012. [S.l.: s.n.], 2012.
BROOKSHEAR, J. G. Computer science: an overview. [S.l.]: Addison-Wesley Long-
man Publishing Co., Inc., 2002.
BROOKSHEAR, J. G. Computer science: an overview. [S.l.]: Addison-Wesley Long-
man Publishing Co., Inc., 2012.


129
DANIAL,
A.
CLOC
-
Count
Lines
of
Code.
2006.
Dispon´ıvel
em:
<http://cloc.sourceforge.net/>.
D¨OLLNER, J. et al. Illustrative visualization of 3d city models. In: INTERNATIONAL
SOCIETY FOR OPTICS AND PHOTONICS. Electronic Imaging 2005. [S.l.], 2005. p.
42–51.
EUGSTER, P. T. et al. The many faces of publish/subscribe. ACM computing surveys
(CSUR), ACM, v. 35, n. 2, p. 114–131, 2003.
FAISON, T. Event-Based Programming. [S.l.]: Springer, 2006.
FERG,
S.
Event-driven
programming:
introduction,
tutorial,
history.
2006.
Dispon´ıvel em:
http://sourceforge.net/projects/eventdrivenpgm/files/event_
driven_programming.pdf Acessado em 03/02/2017.
FERREIRA,
C.
A.
Linguagem
e
compilador
para
o
paradigma
orien-
tado
a
notiﬁca¸c˜oes
(pon):
avan¸cos
e
compara¸c˜oes.
2016.
Disserta¸c˜ao
de
Mestrado,
PPGCA
UTFPR.
Dispon´ıvel
em:
http://www.utfpr.edu.br/
curitiba/estrutura-universitaria/diretorias/dirppg/programas/ppgca/
edital-de-defesas/2015/ppgca-mestrado-cleverson-avelino-ferreira.
FERREIRA, C. A. et al. Compilador para o paradigma orientado a notiﬁca¸c˜oes. 2013.
FERREIRA, K. A. M.; BIGONHA, M. A.; BIGONHA, R. S. Reestrutura¸c˜ao de software
dirigida por conectividade para redu¸c˜ao de custo de manuten¸c˜ao. Revista de Inform´atica
Te´orica e Aplicada, v. 15, n. 2, p. 155–180, 2008.
FORGY, C. L. Rete: A fast algorithm for the many pattern/many object pattern match
problem. Artiﬁcial intelligence, Elsevier, v. 19, n. 1, p. 17–37, 1982.
GABBRIELLI, M.; MARTINI, S. Programming languages: principles and para-
digms. [S.l.]: Springer Science & Business Media, 2010.
GENESERETH, M. R.; KETCHPEL, S. P. Software agents. Commun. ACM, v. 37,
n. 7, p. 48–53, 1994.
GREGORI, R. H. et al. Analysis of a triangle mesh slicing algorithm under the notiﬁcation
oriented and imperative paradigms. 2012. Framework NOP/PON C++ 2.0, Mestrando
PPGCA/UTFPR, 2012. Disciplina sobre Paradigma Orientado a Notiﬁca¸c˜oes (PON),
CPGEI-PPGCA/UTFPR (Prof. J. M. Sim˜ao), Curitiba - PR, Brasil.
GRUNE, D. et al. Modern compiler design. [S.l.]: Springer Science & Business Media,
2012.
HANSEN, S.; FOSSUM, T. Event based programming. 2010. Dispon´ıvel em: http:
//www.cs.uwp.edu/staff/hansen/EventsWWW/.
JASINSKI, R. P. Framework para gera¸c˜ao de hardware em vhdl a partir de modelos
em pon (paradigma orientado a notiﬁca¸c˜oes. 2012. Relat´orio da disciplina de L´ogica
Reconﬁgur´avel por Hardware. Programa de P´os-Gradua¸c˜ao em Engenharia El´etrica e
Inform´atica Industrial. Universidade Tecnol´ogica Federal do Paran´a.


130
KAISLER, S. H. Software paradigms. [S.l.]: John Wiley & Sons, 2005.
KERSCHBAUMER,
R.
et
al.
Paradigma
orientado
a
notiﬁca¸c˜oes
para
a
s´ıntese de l´ogica reconﬁgur´avel. 2015. LA-CCI/CBIC. ISBN: 9788569972006. Dis-
pon´ıvel em:
https://www.researchgate.net/publication/283018125_Paradigma_
Orientado_a_Notificaes_para_a_Sntese_de_Lgica_Reconfigurvel.
KOSSOSKI, C. Jogo em 2d desenvolvido em c++ pon e allegro. 2013. Disciplina sobre
Paradigma Orientado a Notiﬁca¸c˜oes (PON), CPGEI-PPGCA/UTFPR (Prof. J. M. Sim˜ao),
Curitiba - PR, Brasil.
KOSSOSKI, C.; STADZISZ, P. C.; M., S. J. Introdu¸c˜ao ao teste funcional de software
no paradigma orientado a notiﬁca¸c˜oes. In: VI Congresso Intern. de Computaci´on y
Telecom.-COMTEL, Lima, Peru. [S.l.: s.n.], 2014.
KRACHINSKI, V. et al. Analysis of a triangle mesh slicing algorithm under the noti-
ﬁcation oriented and imperative paradigms. 2015. Ling-PON-pilador
0.7, Mestrando
PPGCA/UTFPR, 2015. Disciplina sobre Paradigma Orientado a Notiﬁca¸c˜oes (PON),
CPGEI-PPGCA/UTFPR (Prof. J. M. Sim˜ao), Curitiba - PR, Brasil.
KRUG, D. L. Torre de han´Oi com lingpon – paradigma orientado a notiﬁca¸c˜oes. 2016.
Aplica¸c˜ao em Ling PON 1.0/1.5. IFPR (Professor) – Mestrando PPGCA/UTFPR, 2016.
Disciplina sobre Paradigma Orientado a Notiﬁca¸c˜oes (PON), CPGEI-PPGCA/UTFPR
(Prof. J. M. Sim˜ao e Prof. H. Panetto [visitante CPGEI e UL-Fran¸ca]), Curitiba - PR,
Brasil.
LEE, P.-Y.; CHENG, A. M. K. Hal: A faster match algorithm. IEEE Transactions on
Knowledge and Data Engineering, IEEE, v. 14, n. 5, p. 1047–1058, 2002.
LIBALLEG. Allegro:
A
game
programming
library. 2004. Dispon´ıvel em:
<http://liballeg.org/index.html/>.
LINHARES, R. R. Contribui¸c˜ao para o desenvolvimento de uma arquitetura de
computa¸c˜ao pr´opria ao paradigma orientado a notiﬁca¸c˜oes. Tese (Doutorado) —
Graduate School in Electrical Engineering and Industrial Computer Science (CPGEI) at
the Federal University of Technology - Paran´a (UTFPR). Curitiba, Brazil., 2015. Dispon´ıvel
em: http://repositorio.utfpr.edu.br/jspui/handle/1/1324.
LINHARES, R. R. et al. Compara¸c˜oes entre o paradigma orientado a objetos e o paradigma
orientado a notiﬁca¸c˜oes sob o contexto de um simulador de sistema telefˆonico. In: III
Congresso Intern. de Computaci´on y Telecom.-COMTEL, Lima, Peru. [S.l.:
s.n.], 2011.
LINHARES, R. R.; SIMAO, J. M.; STADZISZ, P. C. Noca - a notiﬁcation-oriented
computer architecture. IEEE Latin America Transactions, IEEE, v. 13, n. 5, p.
1593–1604, 2015.
MARLING, C. et al. Case-based reasoning for planning and world modeling in the robocup
small size league. In: IJCAI Workshop on issues in designing physical agents for
dynamic real-time environments. [S.l.: s.n.], 2003. p. 1–2.


131
MEDON¸cA, I. T. M. et al. M´etodo para desenvolvimento de sistemas orientados a
regras utilizando o paradigma orientado a notiﬁca¸c˜oes. 2015. LA-CCI/CBIC, 2015.
ISBN: 9788569972006. Dispon´ıvel em: https://www.researchgate.net/profile/Igor_
Mendonca/publication/282818387_Mtodo_para_Desenvolvimento_de_Sistemas_
Orientados_a_Regras_utilizando_o_Paradigma_Orientado_a_Notificaes”.
MELO, L. C. V.; FABRO, J. A.; SIM˜aO, J. M. Relat´Orio da adaptaC¸ ˜Ao do para-
digma orientado a notiﬁcaC¸ ˜Oes - pon para suporte a desenvolvimento de sistemas de
l´Ogica fuzzy. 2013. Framework NOP/PON 2.0 C++ (adaptado para fuzzy), Mestrando
CPGEI/UTFPR, 2013. Disciplina sobre Paradigma Orientado a Notiﬁca¸c˜oes (PON),
CPGEI-PPGCA/UTFPR (Prof. J. M. Sim˜ao), Curitiba - PR, Brasil.
MENDON¸cA, I. T. M. Metodologia de projeto de software orientado a notiﬁca¸c˜oes.
2016. Qualiﬁca¸c˜ao de Doutorado, Programa de P´os-Gradua¸c˜ao em Engenharia El´etrica e
Inform´atica Industria da Universidade Tecnol´ogica Federal do Paran´a (UTFPR). Curitiba
– Paran´a (PR), Brazil.
MIRANDA, F. S. Um estudo comparativo entre o paradigma orientado a notiﬁca¸c˜oes (pon)
e o paradigma orientado a objetos (poo) em um problema de uma cidade virtual. 2016.
Disciplina sobre Paradigma Orientado a Notiﬁca¸c˜oes (PON), CPGEI-PPGCA/UTFPR
(Prof. J. M. Sim˜ao e Prof. H. Panetto [visitante CPGEI e UL-Fran¸ca]), Curitiba - PR,
Brasil.
MIRANKER, D. P. Treat: A better match algorithm for ai production systems. Sixth
National Conference on Artiﬁcial Intelligence - AAAI’87, p. 42–47, 1987.
MIRANKER, D. P. et al. On the performance of lazy matching in production systems. In:
AAAI. [S.l.: s.n.], 1990. v. 90, p. 685–692.
MIRANKER, D. P.; LOFASO, B. J. The organization and performance of a treat-based pro-
duction system compiler. IEEE Transactions on Knowledge and Data Engineering,
IEEE, v. 3, n. 1, p. 3–10, 1991.
MONAJJEMI, V.; KOOCHAKZADEH, A.; GHIDARY, S. S. grsim–robocup small size
robot soccer simulator. In: RoboCup 2011: Robot Soccer World Cup XV. [S.l.]:
Springer, 2011. p. 450–460.
MONTE-ALTO, H. H. L. C. Desenvolvendo o jogo pac-man com o paradigma orientado a
notiﬁca¸c˜oes. 2015. Disciplina sobre Paradigma Orientado a Notiﬁca¸c˜oes (PON), CPGEI-
PPGCA/UTFPR (Prof. J. M. Sim˜ao), Curitiba - PR, Brasil.
NWANA, H. S. Software agents: An overview. The knowledge engineering review,
Cambridge Univ Press, v. 11, n. 03, p. 205–244, 1996.
PANESCU, D.; PASCAL, C.; OLAERU, R. M. A rule-based approach for a multi-robot
application. In: IEEE. System Theory, Control and Computing (ICSTCC), 2015
19th International Conference on. [S.l.], 2015. p. 75–80.
PETERS, E. Coprocessador para acelera¸c˜ao de aplica¸c˜oes desenvolvidas utilizando pa-
radigma orientado a notiﬁca¸c˜oes. 2012. Master in Science Thesis, Graduate School in


132
Electrical Engineering and Industrial Computer Science (CPGEI) at the Federal Univer-
sity of Technology Paran´a (UTFPR). Curitiba – Paran´a (PR), Brazil. Dispon´ıvel em:
http://repositorio.utfpr.edu.br/jspui/handle/1/325.
PETERS, E. et al. A new hardware coprocessor for accelerating notiﬁcation-oriented appli-
cations. In: IEEE. Field-Programmable Technology (FPT), 2012 International
Conference on. [S.l.], 2012. p. 257–260.
POO, D.; KIONG, D.; ASHOK, S. Object-oriented programming and Java. [S.l.]:
Springer Science & Business Media, 2007.
PORDEUS, L. F. Notiﬁcation oriented paradigm (nop): Cta simulator. 2015. Disciplina
sobre Paradigma Orientado a Notiﬁca¸c˜oes (PON), CPGEI-PPGCA/UTFPR (Prof. J. M.
Sim˜ao), Curitiba - PR, Brasil.
PORDEUS, L. F. Contribui¸c˜ao para avalia¸c˜ao e melhoria de uma arquitetura de com-
puta¸c˜ao pr´opria ao paradigma orientado a notiﬁca¸c˜oes. 2016. Qualiﬁca¸c˜ao de Mestrado.
CPGEI/UTFPR, Curitiba - PR, Brasil, 01/Julho 2016.
PORDEUS, L. F. et al. Trabalho e manual lingpon vers˜ao 2015. 2015. Relat´orio da
disciplina ’Linguagens e Compiladores’, Programa de P´os-Gradua¸c˜ao em Engenharia
El´etrica e Inform´atica Industria da Universidade Tecnol´ogica Federal do Paran´a (UTFPR).
Curitiba – Paran´a (PR), Brazil.
PRESSMAN, R.; MAXIM, B. Engenharia de Software-8a Edi¸c˜ao. [S.l.]: McGraw Hill
Brasil, 2016.
RESNICK, M. Turtles, termites, and traﬃc jams: Explorations in massively
parallel microworlds. [S.l.]: Mit Press, 1997.
RICCI, A.; SANTI, A. Agent-oriented computing: Agents as a paradigm for computer
programming and software development. In: CITESEER. Proc. of the 3rd Int’l Conf.
on Future Computational Technologies and Applications. Wilmington: Xpert
Publishing Services. [S.l.], 2011. p. 42–51.
RILEY, G.; GIARRATANO, J. Expert systems principles and practice. Massachusetts,
PWS, 1993.
RONSZCKA, A. F. Contribui¸c˜ao para a concep¸c˜ao de aplica¸c˜oes no paradigma orientado
a notiﬁca¸c˜oes (pon) sob o vi´es de padr˜oes. 2012. Master in Science Thesis, Graduate
School in Electrical Engineering and Industrial Computer Science (CPGEI) at the Federal
University of Technology Paran´a (UTFPR). Curitiba – Paran´a (PR), Brazil. Dispon´ıvel
em: http://repositorio.utfpr.edu.br/jspui/handle/1/327.
RONSZCKA, A. F. et al. Compara¸c˜oes quantitativas e qualitativas entre o paradigma
orientado a objetos e o paradigma orientado a notiﬁca¸c˜oes sobre um simulador de jogo.
In: III Congresso Intern. de Computaci´on y Telecom.-COMTEL, Lima, Peru.
[S.l.: s.n.], 2011.
ROY, P. V. et al. Programming paradigms for dummies: What every programmer
should know. New computational paradigms for computer music, IRCAM/De-
latour France, v. 104, 2009.


133
RUSSELL, S.; NORVIG, P. Artiﬁcial intelligence: a modern approach. 2009.
SCH¨uTZ, F. et al. Training of an artiﬁcial neural network with backpropagation algorithm
using notiﬁcation oriented paradigm. 2015. LA-CCI/CBIC, October.
SHOHAM, Y. Agent-oriented programming. Artiﬁcial intelligence, Elsevier, v. 60, n. 1,
p. 51–92, 1993.
SIM˜AO, J. et al. Rule and agent oriented software architecture for controlling automa-
ted manufacturing systems. Frontiers in Artiﬁcial Intelligence and Applications
(Advances on Logic Artiﬁcial Intelligence and Robotics). Amsterdam, The
Netherlands: IOS PRESS BOOKS v. 71, p. 224–231, 2001.
SIM˜AO, J. M. Proposta de uma arquitetura de controle para sistemas ﬂex´ıveis de
manufatura baseada em regras e agentes. 2001. Master in Science Thesis, Graduate
School in Electrical Engineering and Industrial Computer Science (CPGEI) at the Federal
University of Technology Paran´a (UTFPR). Curitiba – Paran´a (PR), Brazil.
SIM˜AO, J. M. A Contribution to the Development of a HMS simulation tool
and Proposition of a Meta-Model for Holonic Control. Tese (Doutorado) — School
in Electrical Engineering and Industrial Computer Science (CPGEI) at Federal University
of Technology - Paran´a (UTFPR, Brazil) and Research Center For Automatic Control
of Nancy (CRAN) - Henry Poincar´e University (UHP, France), 2005. Dispon´ıvel em:
http://arquivos.cpgei.ct.utfpr.edu.br/Ano_2005/teses/Tese_012_2005.pdf.
SIM˜AO, J. M. et al. Notiﬁcation oriented and object oriented paradigm comparison
via sale system. Journal of Software Engineering and Applications, Scientiﬁc
Research Publishing, v. 5, n. 09, p. 695–710, 2012. ISSN 1945-3116. DOI 10.4236/j-
sea.2012.56047. Dispon´ıvel em:
http://www.scirp.org/journal/PaperInformation.
aspx?paperID=22362.
SIM˜AO, J. M. et al. A game comparative study: Object-oriented paradigm and notiﬁcation-
oriented paradigm. Journal of Software Engineering and Applications, Scientiﬁc
Research Publishing, v. 5, n. 09, p. 722–736, 2012. ISSN 1945-3116. DOI 10.4236/j-
sea.2012.59085. Dispon´ıvel em:
http://www.scirp.org/journal/PaperInformation.
aspx?paperID=22364.
SIM˜AO, J. M. et al. Evaluation of the notiﬁcation oriented paradigm applied to sentient
computing. In: IEEE. Object/Component/Service-Oriented Real-Time Distribu-
ted Computing (ISORC), 2014 IEEE 17th International Symposium on. [S.l.],
2014. p. 253–260.
SIM˜AO, J. M. et al. Arquitetura de software de controle orientada a regras e agentes
para sistemas automatizados de manufatura. Simp´osio Brasileiro de Automa¸c ao
Inteligente (SBAI), Canela-RS, Anais SBAI, 2001.
SIM˜AO, J. M.; STADZISZ, P. C. An agent-oriented inference engine applied for supervi-
sory control of automated manufacturing systems. Frontiers in Artiﬁcial Intelligence
and Applications (Advances in Logic, Art. Int. and Robotics - LAPTEC 2002
Edited by Abe J. M., Silva Filho J. I..), IOS Press Books, Amsterdam - The
Netherlands, Vol. 85, v. 85, p. 234–241, 2002. ISBN: 1 58603 292 5, 2002.


134
SIM˜AO, J. M.; STADZISZ, P. C. Paradigma orientado a notiﬁca¸c˜oes (pon)–uma t´ecnica de
composi¸c˜ao e execu¸c˜ao de software orientado a notiﬁca¸c˜oes. 2008. PEDIDO DE PATENTE:
Privil´egio de Inova¸c˜ao. N´umero do registro: PI08055181, data de dep´osito: 26/11/2008,
INPI - Instituto Nacional da Propriedade Industrial. Universidade Tecnol´ogica Federal
do Paran´a - UTFPR (Demanda Agˆencia de Inova¸c˜ao, 2007). Dispon´ıvel em: http:
//bit.ly/1SAQod3.
SIM˜AO, J. M.; STADZISZ, P. C. Inference based on notiﬁcations: a holonic metamodel
applied to control issues. Systems, Man and Cybernetics, Part A: Systems and
Humans, IEEE Transactions on, IEEE, v. 39, n. 1, p. 238–250, 2009.
SIM˜AO, J. M.; STADZISZ, P. C.; K¨UNZLE, L. A. Rule and agent-oriented architecture to
discrete control applied as petri net players. Frontiers in Artiﬁcial Intelligence and
Applications (FAAI)-Advances in Intelligent Systems and Robotics”LAPTEC
2003, IOS Press, Amsterdam-The Netherlands, p. 121–129, 2003. ISBN 4 274 90624 8
C3055 (Ohmsha).
SIM˜AO, J. M. et al. Mecanismo de inferˆencia otimizado do paradigma orientado a
notiﬁca¸c˜oes (pon) e mecanismos de resolu¸c˜ao de conﬂitos para ambientes monoprocessados
e multiprocessados aplicados ao pon. 2010. Patent pending submitted to INPI/Brazil
(Instituto Nacional de Propriedade Industrial) in 03/2010 and Innovation Agency of
UTFPR in 2010. INPI Number: PI1003736-5. Dispon´ıvel em: http://bit.ly/1SgQMeK.
SIM˜AO, J. M.; TACLA, C. A.; STADZISZ, P. C. Holonic control metamodel. Systems,
Man and Cybernetics, Part A: Systems and Humans, IEEE Transactions on,
IEEE, v. 39, n. 5, p. 1126–1139, 2009.
SIM˜AO, J. M. et al. Notiﬁcation oriented paradigm (nop) and imperative paradigm: A
comparative study. 2012. Journal of Software Engineering and Applications (JSEA),
p.402-416, v.5, n.6, 2012. ISSN: 1945-3116. DOI 10.4236/jsea.2012.59083. Dispon´ıvel em:
https://www.researchgate.net/publication/272666606_Notification_Oriented_
Paradigm_%28NOP%29_and_Imperative_Paradigm_A_Comparative_Study.
SIM˜aO, J. M. et al. Paradigma orientado a notiﬁca¸c˜oes em hardware digital. 2012. [Pe-
dido de Prote¸c˜ao Industrial e Pedido de Patente enviados `a Agˆencia de Inova¸c˜ao da
UTFPR respectivamente em 11/05/2012 e 17/07/2012] Patent pending INPI/Brazil and
UTFPR, 2012. Patent INPI: BR 10 2012 026429 3. http://www.google.com/patents/
WO2014059497A1?cl=pt.
SIM˜aO, J. M. et al. Compara¸c˜oes entre duas materializa¸c˜oes do paradigma orientado a
notiﬁca¸c˜oes (pon): Framework pon prototipal versus framework pon prim´ario. 2012. IV
Congreso Internacional de Computaci´on y Telecomunicaciones, COMTEL 2012, Lima,
Peru.
SOUZA, T. B. A. Um modelo para avalia¸c˜ao de manutenibilidade de c´odigo-fonte orientado
a objeto. 2005. Trabalho de Gradua¸c˜ao em Engenharia de Software, Universidade Federal
de Pernambuco.
VALENC¸A, G. Z. Contribui¸c˜ao para materializa¸c˜ao do paradigma orientado a notiﬁca¸c˜oes
(pon) via framework e wizard. 2013. Disserta¸c˜ao (Mestrado em Computa¸c˜ao Aplicada -
PPGCA) – Universidade Tecnol´ogica Federal do Paran´a (UTFPR), Curitiba. Dispon´ıvel
em: http://repositorio.utfpr.edu.br/jspui/handle/1/393.


135
VAN-ROY, P.; HARIDI, S. Concepts, techniques, and models of computer pro-
gramming. [S.l.]: MIT press, 2004.
VISSER, U.; BURKHARD, H.-D. Robocup: 10 years of achievements and future challenges.
AI magazine, v. 28, n. 2, p. 115, 2007.
VOLPATO, N. Prototipagem r´apida: tecnologias e aplica¸c˜oes. [S.l.]: Edgard Clu-
cher, 2007.
WATT, D. A. Programming language design concepts. [S.l.]: John Wiley & Sons,
2004.
WEBER, L. et al. Viabilidade de controle orientado a notiﬁca¸c˜oes (con) em ambiente con-
corrente baseado em threads. 2010. In: XV Semin´ario de Inicia¸c˜ao Cient´ıﬁca e Tecnol´ogica
(XV SICITE), Campus UTFPR, Corn´elio Proc´opio, PR, Brasil. Anais do XV Semin´ario
de Inicia¸c˜ao Cient´ıﬁca e Tecnol´ogica da UTFPR.
WIECHETECK, L. V. B. M´etodo para projeto de software usando o paradigma orientado a
notiﬁca¸c˜oes–pon. 2012. Master in Science Thesis, Graduate School in Electrical Engineering
and Industrial Computer Science (CPGEI) at the Federal University of Technology – Paran´a
(UTFPR). Curitiba – Paran´a (PR), Brazil. Dispon´ıvel em: http://repositorio.utfpr.
edu.br/jspui/handle/1/212.
WIECHETECK, L. V. B.; STADZISZ, P. C.; SIM˜AO, J. M. Um perﬁl uml para o paradigma
orientado a notiﬁca¸c˜oes (pon). In: “Um Perﬁl UML para o Paradigma Orientado a
Notiﬁca¸c˜oes (PON)”. III Internacional Congress of Computationm and Tele-
comunications (Congreso Internacional de Computaci´on y Telecomunicaciones
- COMTEL), Lima, Peru. [S.l.: s.n.], 2011.
WITT, F. A. et al. Compara¸c˜ao entre o paradigma orientado a objetos (poo) e o paradigma
orientado a notiﬁca¸c˜oes (pon) em um controle discreto em l´ogica reconﬁgur´avel. 2011. Em:
XVI SICITE - Semin´ario de Inicia¸c˜ao Cient´ıﬁca e Tecnol´ogica da UTFPR, 2011, Ponta
Grossa - PR. Anais do XVI SICITE.
WOOLDRIDGE, M.; JENNINGS, N. R. et al. Intelligent agents: Theory and practice.
Knowledge engineering review, Cambridge Univ Press, v. 10, n. 2, p. 115–152, 1995.
WOOLDRIDGEY, M.; CIANCARINI, P. Agent-oriented software engineering: The state
of the art. In: SPRINGER. Agent-oriented software engineering. [S.l.], 2001. p. 1–28.
XAVIER, R. D. Paradigmas de desenvolvimeto de software: Compara¸c˜ao entre
abordagens orientada a eventos e orientada a notiﬁca¸c˜oes. Tese (Doutorado) —
Master Thesis, Universidade Tecnol´ogica Federal do Paran´a-UTFPR, Graduate School of
Electrical Engineering and Computer Science-CPGEI, Curitiba/PR, 2014.
YOON, M. Developing basic soccer skills using reinforcement learning for the
RoboCup Small Size League. Tese (Doutorado) — Stellenbosch University, 2015.


136
APˆENDICE A -- DESCRIC¸ ˜AO DAS ALTERAC¸ ˜OES REALIZADAS NA
LINGPON
Este apˆendice apresenta as contribui¸c˜oes deste trabalho para a LingPON. Primei-
ramente, a se¸c˜ao A.1 apresenta em detalhes as altera¸c˜oes realizadas na LingPON para
permitir o relacionamento de FBEs atrav´es de agrega¸c˜ao. Na sequˆencia, na se¸c˜ao A.2 s˜ao
apresentadas as altera¸c˜oes realizadas na LingPON para suportar a agrega¸c˜ao de Rules em
FBEs, a qual foi nomeada FBE Rules, de forma a permitir a cria¸c˜ao de Rules de forma
mais simples e com menor redundˆancia de linhas de c´odigo. Por ﬁm, na se¸c˜ao A.3 s˜ao
apresentadas as altera¸c˜oes realizadas na LingPON para solucionar o problema encontrado
na gera¸c˜ao de c´odigo C++ com m´ultiplas instˆancias de um dado FBE.
A.1
AGREGAC¸ ˜AO DE FBES
Em sua vers˜ao original, o analisador l´exico utilizado pelo compilador j´a suportava
a declara¸c˜ao de FBEs como Attributes de outros FBEs. Entretanto, os m´odulos de an´alise
sint´atica e gera¸c˜ao de c´odigo n˜ao eram capazes de identiﬁcar a rela¸c˜ao de agrega¸c˜ao de
FBEs na declara¸c˜ao de Premises e Instigations, conforme apresentado no C´odigo 32,
causando exce¸c˜ao e consequente encerramento prematuro do processo de compila¸c˜ao.


137
C´odigo 32: Exemplo de agrega¸c˜ao de FBEs n˜ao suportada na vers˜ao original
da LingPON
1 fbe Arm
2
attributes
3
ﬂoat atSize 0.0
4
end attributes
5
methods
6
method mtExecuteAction()
7
end methods
8 end fbe
9
10 fbe Robot
11
attributes
12
Arma atArm ;
13
end attributes
14 ...
15 end fbe
16
17 rule rlMoveArm
18
condition
19
subcondition condition1
20
premise prRobotArmSize robot.atArm.size == 10.0
21
end subcondition
22
end condition
23
action
24
instigation inMoveRobotArm robot.atArm.mtExecuteAction();
25
end action
26 end rule
Atrav´es do fragmento de c´odigo apresentado no C´odigo 33, ´e poss´ıvel observar que,
na vers˜ao original do compilador, uma Instigation poderia ser deﬁnida pela palavra chave
INSTIGATION, um Method (method use), o qual representa uma a¸c˜ao a ser executada
e, opcionalmente, um nome para essa Instigation. O Method, por sua vez, deveria ser
deﬁnido por um “id”, o qual representa um Method de um FBE que dever´a ser executado.


138
C´odigo 33: Deﬁni¸c˜ao de Instigation extra´ıdo do arquivo de conﬁgura¸c˜ao do
analisador sint´atico (Bison) utilizado pela atual vers˜ao do compilador PON.
1 instigation
: INSTIGATION method use
2
| INSTIGATION method use
3
;
4
5 method use
: id LP RP SEMICOLON
6
;
7
8 id
: ID
9
| ID POINT ID
10
;
De forma simplista, o analisador sint´atico da atual vers˜ao do compilador considera
a sequˆencia de caracteres anterior ao ponto como sendo o nome de uma instˆancia de
FBE e o restante como sendo o nome do Method referente `a esta instˆancia. No exemplo
apresentado no C´odigo 32, o nome da instˆancia a ser interpretada pelo compilador na
Instigation seria “robot” e o nome do Method “atArm.mtExecuteAction”. Como o FBE
Robot n˜ao possui nenhum Method com esse nome, o processo de compila¸c˜ao do c´odigo-fonte
seria abortado.
Visando solucionar este problema, algumas mudan¸cas foram realizadas no anali-
sador sint´atico do compilador PON. Em um primeiro momento, uma sutil altera¸c˜ao no
arquivo de conﬁgura¸c˜ao do analisador sint´atico foi efetuada de forma a permitir a correta
separa¸c˜ao do nome da instˆancia que dever´a executar a a¸c˜ao e qual m´etodo dever´a ser
invocado pela Instigation. Esta altera¸c˜ao ´e apresentada no C´odigo 34.
C´odigo 34: Nova deﬁni¸c˜ao da regra “id” no arquivo de conﬁgura¸c˜ao do
analisador sint´atico (Bison).
1 id
: ID
2
| ID POINT id
3
;


139
Utilizando essa nova deﬁni¸c˜ao da regra “id” do analisador sint´atico no exemplo
apresentado no C´odigo 32, o nome da instˆancia interpretada pelo compilador na Instigation
passa a ser “robot.atArm” e o nome do Method “mtExecuteAction”.
Com o problema de separa¸c˜ao de nomes de instˆancia e Method relacionados a
Instigation solucionado, deu-se in´ıcio `as altera¸c˜oes no c´odigo relacionado ao gerenciamento
da tabela de s´ımbolos utilizada pelo compilador.
Dado que um FBE Robot possui um Attribute do tipo Arm, para cada nova
instˆancia do FBE Robot criada, a nova vers˜ao do compilador dever´a criar uma nova
instˆancia do FBE Arm, adicion´a-la `a tabela de s´ımbolos do compilador e relacionar essa
nova instˆancia com a correta instˆancia do FBE Robot. O controle de quais instˆancias
devem ser criadas para criar a correta correla¸c˜ao entre os FBEs deve ser feito de maneira
recursiva, de forma a permitir a agrega¸c˜ao de FBEs em m´ultiplos n´ıveis.
Desse modo, o m´etodo createInstantiation da classe Compiler do compilador PON
foi alterado. As altera¸c˜oes realizadas s˜ao apresentadas entre as linhas 13 e 24 do C´odigo
35.


140
C´odigo 35: M´etodo da classe Compiler alterado para permitir a cria¸c˜ao de
instˆancias de FBEs de forma recursiva.
1 void createInstantiation(string fbeName, list<string>idList)
2 {
3
Entity *fbeFound = semanticAnalyser.getEntity(fbeName);
4
if (fbeFound == 0) {return;}
5
6
for (list<string>::iterator it = idList.begin(); it != idList.end(); ++it)
7
{
8
Entity *entityFound = semanticAnalyser.getEntity(*it);
9
if (entityFound == 0)
10
{
11
Instantiation *instantiation = new Instantiation(*it);
12
instantiation->fbe = (Fbe*)fbeFound;
13
list<Attribute*>attrs = ((Fbe*)(fbeFound))->attributes;
14
15
for (list<Attribute *>::iterator itAttr = attrs.begin();
16
itAttr != attrs.end(); ++itAttr)
17
{
18
if ((*itAttr)->aType == Attribute::A ID)
19
{
20
list<string> lsFbeAttribute;
21
lsFbeAttribute.push back(*it + “ ” + (*itAttr)->userEntityId);
22
createInstantiation((*itAttr)-textgreatervalue, lsFbeAttribute);
23
}
24
}
25
semanticAnalyser.addEntity(instantiation);
26
}
27
28 }


141
A.2
FBE RULES
Conforme mencionado na se¸c˜ao 3.1.2, um pr´e-compilador foi desenvolvido de forma
a possibilitar a cria¸c˜ao de FBE Rules. Este pr´e-compilador utiliza os mesmos m´odulos de
an´alise l´exica e sint´atica utilizados pelo compilador PON, diferenciando-se apenas pelo
m´odulo de gera¸c˜ao de c´odigo, o qual gera como sa´ıda um c´odigo-fonte PON intermedi´ario.
Dessa forma, ambos os m´odulos foram alterados para que fossem capazes de reconhecer e
interpretar as FBE Rules.
A primeira altera¸c˜ao foi realizada no analisador l´exico, uma vez que o mesmo deve
ser capaz de reconhecer a sequˆencia de caracteres que identiﬁcam as palavras chave fbeRule
e end fbeRule como tokens. Dessa forma, o arquivo “lex pon.l” foi alterado conforme
apresentado no C´odigo 36.
C´odigo 36: Altera¸c˜ao realizada no arquivo “lex pon.l” para suportar FBE
Rules.
1 fbeRule
return FBERULE;
2 end fbeRule
return END FBE RULE;
Posteriormente, o analisador sint´atico do compilador PON foi alterado de forma a
suportar a declara¸c˜ao de FBE Rules dentro o escopo de declara¸c˜ao de FBEs. Para isto,
duas altera¸c˜oes foram realizadas no arquivo “bison pon.y”. A primeira altera¸c˜ao realizada
foi a cria¸c˜ao da regra para a correta interpreta¸c˜ao de FBE Rules, conforme ´e apresentado
entre as linhas 1 e 3 do C´odigo 37. A segunda altera¸c˜ao foi realizada na regra que deﬁne
como um FBE pode ser declarado. A regra foi alterada para suportar, al´em de Attributes
e Methods, tamb´em a declara¸c˜ao de FBE Rules, conforme ´e apresentado entre as linhas 5
e 8 do C´odigo 37


142
C´odigo 37: Altera¸c˜oes realizadas no arquivo “bison pon.y” para suportar
FBE Rules.
1 fbeRules
: fbeRule
2
| fbeRule fbeRules
3
;
4
5 fbe body
: decl attributes decl methods fbeRules
6
| decl attributes decl methods
7
| decl attributes
8
;
Na sequˆencia, foi necess´ario aplicar altera¸c˜oes sobre a classe NOPCompiler, a
qual representa a classe respons´avel pela gera¸c˜ao de c´odigo do pr´e-compilador PON. Para
isso, foi criado um novo m´etodo, nomeado createFbeRules. Este m´etodo ´e respons´avel
por identiﬁcar o FBE associado `a uma FBE Rule e criar uma entidade Rule para cada
instˆancia declarada do FBE.
Primeiramente o pr´e-compilador veriﬁca qual o FBE relacionado `a entidade FBE
Rule que est´a sendo processada. Uma vez identiﬁcado, o pr´e-compilador percorre sua
tabela de s´ımbolos aﬁm de identiﬁcar todas as instˆancias declaradas do FBE.
Conhecendo a lista de instˆancias declaradas do FBE, o pr´e-compilador inicia
um la¸co de repeti¸c˜ao para criar uma nova entidade Rule para cada uma das instˆancias
presentes na lista. Dessa forma, uma Rule ´e criada no c´odigo-fonte intermedi´ario para
cada uma das instˆancias do FBE.
A.3
CORREC¸ ˜AO DE ERRO: GERAC¸ ˜AO DE C´ODIGO-ALVO C++ COM M´ULTIPLAS
INSTˆANCIAS DE FBE
Conforme apresentado na se¸c˜ao 3.1.3, um bug existente na atual vers˜ao do compi-
lador PON foi solucionado com aux´ılio do pr´e-compilador PON.
A solu¸c˜ao desenvolvida faz com que cada instˆancia de um dado FBE seja trans-
formado em um FBE no c´odigo-fonte PON intermedi´ario, durante o processo de pr´e-
compila¸c˜ao. Para isso, o m´etodo parseFbeByInstances, apresentado no C´odigo 38, foi
adicionado `a classe NOPCompiler.


143
C´odigo 38: C´odigo-fonte do m´etodo parseFbeByInstances adicionado `a classe
NOPCompiler.
1 void NOPCompiler::parseFbeByInstances() {
2
for (map<string, Instantiation*>::iterator it = mapInstantiations.begin();
3
it != mapInstantiations.end(); ++it)
4
{
5
Fbe *fbe = (it->second)->fbe;
6
7
std::string fbeName = fbe->userEntityId;
8
std::string instanceName = (it->second)->userEntityId;
9
10
Fbe *newFbe = new Fbe(fbeName + instanceName);
11
newFbe->methods = fbe->methods;
12
newFbe->premises = fbe->premises;
13
newFbe->attributes = copyAttributes(fbe->attributes);
14
15
for (list<Attribute *>::iterator itAttribute = newFbe-¿attributes.begin();
16
itAttribute != newFbe->attributes.end(); ++itAttribute)
17
{
18
if ((*itAttribute)->aType == Attribute::A ID)
19
{
20
(*itAttribute)->value = (*itAttribute)->value +
21
instanceName +
22
(*itAttribute)->userEntityId;
23
}
24
}
25
(it->second)->fbe = newFbe;
26
mapFBEs.erase(fbe->userEntityId);
27
mapFBEs[newFbe->userEntityId] = newFbe;
28
}
29 }
Para cada instˆancia de FBE presente no c´odigo-fonte PON, o m´etodo parseF-


144
beByInstances cria uma c´opia do FBE original, isto ´e, um FBE com os mesmos Methods,
Attributes e Premises associadas, conforme apresentado entre as linhas 10 e 24 do C´odigo
38. Entretanto, conforme apresentado na linha 10 do C´odigo 38, o nome do novo FBE
´e uma composi¸c˜ao do nome do FBE original e da instˆancia `a ele associada. Por exem-
plo, caso o nome do FBE seja “Robot” e o nome das instˆancias “robot1” e “robot2”, o
pr´e-compilador criar´a dois novos FBEs: Robotrobot1 e Robotrobot2.
Posteriormente, uma vez que o novo FBE esteja criado, o FBE antigo ´e removido
da tabela de s´ımbolos utilizada pelo compilador (linha 26) e o novo objeto FBE ´e ent˜ao
adicionado `a tabela de s´ımbolos (linha 27).
Desse modo, a atual vers˜ao do m´odulo de compila¸c˜ao e gera¸c˜ao de c´odigo para
C++ ´e capaz de interpretar e criar as classes e objetos em C++ de maneira correta,
relacionando `a cada instˆancia de FBE apenas as Rules `a ela associada.


145
APˆENDICE B -- ESPECIFICAC¸ ˜AO T´ECNICA - ROBOCUP SMALL SIZE
LEAGUE
B.1
DESCRIC¸ ˜AO DO AMBIENTE DE JOGO
Uma partida de futebol de robˆos na categoria SSL(Small Size League) ocorre em
um campo de jogo retangular, sobre um piso plano recoberto com um feltro ou carpete
ﬁno, na cor verde escuro. As dimens˜oes das linhas que demarcam o campo deﬁnem uma
´area de jogo retangular, de 9000mm x 6000 mm (9 x 6 metros). Deve haver uma ´area
lateral que permita aos jogadores sa´ırem da ´area delimitada do campo de jogo(por exemplo
para a cobran¸ca de um arremesso lateral). Esta ´area lateral deve ter 700 mm em todos os
lados, sendo que a 300 mm das linhas delimitantes, deve ser constru´ıda uma parede de
prote¸c˜ao de 100 mm de altura, para impedir que robˆos ou a bola saiam da ´area de jogo.
Os gols devem ter 160mm de altura, ﬁxos ao piso.
As dimens˜oes exatas do campo, bem como pinturas de ´area de goleiros, meio de
campo, e c´ırculo central, s˜ao apresentadas na Figura 32. Todas as linhas s˜ao pintadas em
cor branca, e devem ter 10 mm de espessura. As paredes laterais, e os gols, devem tamb´em
ser pintados de branco. Os gols n˜ao podem possuir tetos, pois deve ser poss´ıvel ver o
jogador que atua como goleiro mesmo se o mesmo entrar parcial ou totalmente dentro do
gol.
Entretanto, deve haver uma trave superior na parte frontal do gol, composta por
uma barra de a¸co com diˆametro n˜ao maior que 10 mm, por´em forte o suﬁciente para
rebater a bola e evitar d´uvida sobre se a bola entrou no gol, ou passou por cima do mesmo.
Esta barra deve ﬁcar a 155 mm de altura do solo. A parte superior do gol deve ser coberta
por uma rede, que n˜ao impe¸ca a vis˜ao superior dos marcadores do jogador goleiro, mas
impe¸ca a bola de sair do gol pela parte superior do mesmo.
A bola a ser utilizada deve ser uma bola de golfe, esf´erica, com aproximadamente
43 mm de diˆametro, aproximadamente 46 g de massa, e na cor alaranjada.
A partida ´e disputada por dois times de robˆos totalmente autˆonomos. Cada time


146
Figura 32: Campo de jogo (dimens˜oes em mil´ımetros).
´e composto de n˜ao mais que 6 (seis) robˆos, claramente identiﬁcados por n´umeros, para
que seja poss´ıvel ao juiz identiﬁcar cada robˆo individualmente. O robˆo que ir´a atuar como
goleiro deve ser previamente informado ao juiz, antes do in´ıcio da partida. A partida n˜ao
pode ter in´ıcio a n˜ao ser que ambos os times tenham ao menos um robˆo funcionando.
Substitui¸c˜ao de robˆos: ´E poss´ıvel substituir qualquer robˆo por outro (robˆos
reservas) quantas vezes for necess´ario, durante as interrup¸c˜oes da partida, mediante
informa¸c˜ao e autoriza¸c˜ao do ´arbitro. N˜ao h´a limite para o n´umero de substitui¸c˜oes.
Sempre que h´a uma substitui¸c˜ao, primeiramente o robˆo a ser substitu´ıdo deve deixar o
campo de jogo, e posteriormente, ap´os autoriza¸c˜ao do juiz, um novo robˆo entra no campo
de jogo, sendo posicionado no centro de campo, pr´oximo `a linha lateral de um lado ou de
outro. Se um robˆo deixar de funcionar, ap´os autoriza¸c˜ao, um integrante humano da equipe
de desenvolvimento pode adentrar ao campo para retirar este robˆo defeituoso, somente em
uma interrup¸c˜ao da partida, e com autoriza¸c˜ao pr´evia do ´arbitro, ap´os a autoriza¸c˜ao da
substitui¸c˜ao.
B.2
DESCRIC¸ ˜AO DOS ROBˆOS
Cada robˆo deve ser constru´ıdo de forma a estar contido em um cilindro de 180 mm
de diˆametro e 150 mm de altura, conforme apresentado na Figura 33. A parte superior do
robˆo deve ser plana, de forma a ser poss´ıvel colar um Identiﬁcador Padr˜ao, descrito na


147
se¸c˜ao “Uniformes”.
Figura 33: Dimens˜oes m´axima do robˆo (em mil´ımetros).
B.2.1
UNIFORMES
Cada robˆo deve possuir um identiﬁcador ´unico, de forma que seja poss´ıvel identiﬁc´a-
lo durante a partida de futebol de robˆos. Esse identiﬁcador ´e composto 5 marcadores que
est˜ao localizados na parte superior do robˆos, conforme apresentado na Figura 34.
Figura 34: Posi¸c˜ao do marcador central (azul ou amarelo), e dos 4 marcadores laterais
coloridos (magenta ou verde claro).
Utilizando este padr˜ao de identiﬁca¸c˜ao, cada time pode ter at´e 12 robˆos, dos
quais no m´aximo 6 poder˜ao ser utilizado ao mesmo tempo durante a partida de futebol,
conforme apresentado na Figura 35.
Como apresentado na Figura 36, o funcionamento de uma partida de futebol
de robˆos na categoria Small Size League(SSL) ´e o seguinte: um software padronizado,


148
Figura 35: Marcadores coloridos utilizados para a identiﬁca¸c˜ao.
denominado SSL-Vision [Zickler et al. 2009], continuamente processa imagens de v´ıdeo
obtidas atrav´es de cˆameras posicionadas superiormente ao campo, e a cada 1/60 segundos
(60 vezes por segundo) executa a captura das posi¸c˜oes dos jogadores em campo (de
ambos os times) e da bola, e repassa estas informa¸c˜oes atrav´es de uma rede cabeada,
usando protocolo UDP, para os computadores de controle tanto da equipe Azul quanto da
Equipe Amarela. Cabe aos sistemas de controle utilizar estas informa¸c˜oes para deﬁnir o
comportamento individual de cada robˆo de seu time, e repassar estes comandos atrav´es de
algum mecanismo de comunica¸c˜ao sem ﬁo aos respectivos robˆos para execu¸c˜ao.
Figura 36: Esquema geral de funcionamento do Futebol de Robˆos da categoria SSL.
Fonte: http://wiki.robcup.org/Small Size League
As regras de um jogo da categoria SSL procuram seguir o que se esperaria de um
jogo de futebol humano, com algumas diferen¸cas b´asicas. As regras b´asicas s˜ao descritas a
seguir:
•O jogo ´e disputado em dois tempos de 10 minutos cada, com um intervalo de n˜ao


149
mais de 5 minutos entre os tempos. Cada equipe pode requerer at´e 4 “tempos”
durante a partida, desde que o tempo total somado n˜ao ultrapasse 5 minutos. Por
exemplo, um time pode pedir dois tempos de 1 minuto cada, e mais um tempo de 3
minutos depois. Os tempos s´o podem ser pedidos durante uma parada do jogo;
•Em caso de empate, s˜ao disputados outros 2 tempos de jogo, que podem ser de 10
minutos, ou de 5 minutos cada; Em caso de continuidade do empate, pode haver
uma decis˜ao atrav´es de pˆenaltis alternados;
•In´ıcio de partida, ou rein´ıcio de partida ap´os um gol: o juiz posiciona a bola no centro
do campo, informa qual time dever´a reiniciar a partida (time azul ou amarelo), e
envia o comando para reiniciar a partida; O time respons´avel por reiniciar a partida
deve enviar um robˆo para que o mesmo toque na bola, reiniciando a partida;
H´a tamb´em um outro programa, denominado SSL-RefereeBox (cuja interface ´e
apresentada na Figura 37), que permite a um ´arbitro auxiliar informar, tamb´em atrav´es
do protocolo de rede local de comunica¸c˜ao (desta vez TCP) sobre as decis˜oes do ´arbitro a
cada momento. Os comandos que podem ser enviados pelo ´arbitro aos times s˜ao listados a
seguir:
Figura 37: Interface do programa SSL Referee Box, para envio de comandos do ´arbitro.


150
•Halt: informa a todos os robˆos de ambos os times para pararem de se mover
imediatamente, pois h´a alguma situa¸c˜ao de emergˆencia a ser tratada;
•Stop Game: ocorreu uma interrup¸c˜ao da partida (ou um gol, ou a bola saiu da
´area de jogo, ou foi marcada uma falta, ou pˆenalti). Este comando tamb´em ´e
executado imediatamente antes do in´ıcio de cada tempo de jogo, ou ap´os uma parada
de emergˆencia (comando Halt), para que os robˆos se preparem para o rein´ıcio da
partida;
•Normal Start: este comando ´e enviado somente ap´os o envio de um comando de
in´ıcio de partida (KickOﬀ), ou de cobran¸ca de pˆenalti, ap´os os jogadores terem tido
tempo de se posicionar adequadamente (os casos de in´ıcio de partida ocorrem nos
in´ıcios dos tempos de jogo, ou ap´os um time marcar um gol; no caso da marca¸c˜ao
de um pˆenalti, o ´arbitro primeiro envia um comando “Stop Game”, depois informa
qual time vai bater e qual vai defender, enviando o comando “Penalty Blue”, por
exemplo, em que um jogador do time azul se posiciona para bater o pˆenalti, e o
goleiro do time amarelo se posiciona para defender, e todos os outros jogadores de
ambos os times se posicionam atr´as da linha de meio de campo, no campo contr´ario
ao que ser´a utilizado para a cobran¸ca do pˆenalti);
•Force Start: este comando s´o ´e enviado pelo ´arbitro quando um time n˜ao consegue
realizar sua a¸c˜ao (iniciar a partida, bater um tiro indireto-por exemplo um tiro
lateral, ou bater um tiro direto, ou bater um pˆenalti) por um per´ıodo de 5 segundos;
ent˜ao o ´arbitro envia um comando “Stop Game”, e envia em seguida um comando
“Force Start” informando que ambos os times podem ir em dire¸c˜ao `a bola;
•Kickoﬀ: este comando enviado pelo ´arbitro para indicar o rein´ıcio da partida no
in´ıcio da partida, ap´os um gol, no in´ıcio do segundo tempo ou no in´ıcio de cada
per´ıodo de prorroga¸c˜ao. Ainda, um gol pode ser marcado a partir da cobran¸ca direta
de um kickoﬀ.
•Indirect Freekick: comando enviado pelo ´arbitro para indicar o rein´ıcio da partida
ap´os marca¸c˜ao de certas irregularidades durante a partida, tais como segurar a bola
por mais de 15 segundos ou segurar a bola ap´os solt´a-la sem que nenhum outro robˆo
tenha tocado na bola dentro de sua ´area de defesa. Al´em disso, ocorre a marca¸c˜ao
de “Indirect Kick” quando um robˆo encosta no robˆo “goleiro” do time advers´ario
dentro de sua ´area de defesa, ou ent˜ao quando um robˆo percorre mais de 1000 mm


151
mantendo a posse da bola ou quando um robˆo chuta a bola com velocidade maior
que 8 m/s.
•Penalty: comando enviando pelo ´arbitro quando um robˆo defensor realiza as seguintes
irregularidades dentro da ´area de defesa: choque de forma acentuada com um robˆo
do time advers´ario, segurar um robˆo advers´ario impossibilitando-o de se locomover
ou segurar a posse de bola de forma que impossibilite a continuidade da partida.
B.3
REQUISITOS FUNCIONAIS DA APLICAC¸ ˜AO DE CONTROLE
Os seguintes requisitos funcionais devem ser seguidos por um software que controle
o comportamento de um time de futebol de robˆos
Requisitos Funcionais relativos `a quantidade de robˆos em campo em um determi-
nado momento:
•RF01: Se 6 robˆos estiverem presentes no campo, o de menor n´umero de camisa deve
ser o goleiro, os 3 seguintes, em ordem de n´umero de camisa, devem se comportar
como zagueiros, e os dois seguintes devem se comportar como atacantes;
•RF02: Se 5 robˆos estiverem presentes no campo, o de menor n´umero de camisa deve
ser o goleiro, os 3 seguintes, em ordem de n´umero de camisa, devem se comportar
como zagueiros, e seguinte deve se comportar como atacante;
•RF03: Se 4 robˆos estiverem presentes no campo, o de menor n´umero de camisa deve
ser o goleiro, os 2 seguintes, em ordem de n´umero de camisa, devem se comportar
como zagueiros, e seguinte deve se comportar como atacante;
•RF04: Se 3 robˆos estiverem presentes no campo, o de menor n´umero de camisa deve
ser o goleiro, e os 2 seguintes, em ordem de n´umero de camisa, devem se comportar
como zagueiros;
•RF05: Se 2 robˆos estiverem presentes no campo, o de menor n´umero de camisa deve
ser o goleiro, e o outro deve se comportar como zagueiro;
•RF06: Se apenas 1 robˆo estivere presente no campo, o mesmo deve se comportar
como goleiro;
Requisito Funcional relativo `a movimenta¸c˜ao dos robˆos:


152
•RF07: O sistema de controle deve ser capaz de enviar comandos para mover cada
um dos robˆos, de forma individual, at´e uma posi¸c˜ao determinada pelas coordenadas
do plano cartesiano (x, y) e um determinado ˆangulo.
Requisitos Funcionais comuns `a todos os jogadores:
•RF08: Ao receber o comando “Halt”, todos os robˆos devem parar imediatamente;
•RF09: Ao receber o comando “Stop”, os robˆos devem manter a distˆancia m´ınima de
500mm. em rela¸c˜ao `a bola.
•RF10: Quando o ´ultimo comando recebido foi “Normal Start” e a bola estiver em
movimento, o robˆo deve tocar a bola para um companheiro do seu time caso a bola
esteja localizada em seu campo de defesa e haja algum companheiro sem marca¸c˜ao
advers´aria.
•RF11: Quando o ´ultimo comando recebido foi “Normal Start” e a bola estiver em
movimento, o robˆo deve chutar a bola em dire¸c˜ao ao gol advers´ario caso a bola esteja
localizada em seu campo de defesa e n˜ao haja nenhum companheiro sem marca¸c˜ao
advers´aria.
•RF12: Quando o ´ultimo comando recebido foi “Normal Start” e a bola estiver em
movimento, o robˆo deve chutar a bola em dire¸c˜ao ao gol advers´ario caso a bola esteja
localizada no campo advers´ario e n˜ao haja nenhum advers´ario entre o robˆo e o gol
advers´ario.
•RF13: Quando o ´ultimo comando recebido foi “Normal Start” e a bola estiver em
movimento, o robˆo deve tocar a bola para um companheiro de seu time caso a bola
esteja localizada no campo advers´ario e haja ao menos um advers´ario entre o robˆo e
o gol advers´ario.
Requisitos Funcionais relativos ao jogador que est´a com o comportamento de
“Goleiro” em um determinado momento:
•RF14: Ao receber o comando “Stop Game”, o robˆo que est´a na posi¸c˜ao “Goleiro”
deve se posicionar pr´oximo `a linha de fundo, em frente ao seu pr´oprio gol, de forma a
estar centralizado sobre a linha imagin´aria que liga a posi¸c˜ao atual da bola ao fundo
do gol, caso a distˆancia entre a bola e o gol defendido seja menor que 1800 mm.;


153
•RF15: Ao receber o comando “Stop Game”, o robˆo que est´a na posi¸c˜ao “Goleiro”
deve se posicionar junto `a linha de sua ´area de defesa, em frente ao seu pr´oprio gol,
de forma a estar centralizado sobre a linha imagin´aria que liga a posi¸c˜ao atual da
bola ao fundo do gol caso a distˆancia entre a bola e o gol defendido seja maior que
1800 mm.;
•RF16: Ao receber o comando “Normal Start”, o robˆo que est´a na posi¸c˜ao “Goleiro”
deve chutar a bola em dire¸c˜ao ao gol advers´ario caso a bola esteja `a uma distˆancia
menor que 800 mm em rela¸c˜ao ao gol que est´a sendo defendido e o robˆo seja o jogador
mais pr´oximo `a bola.
•RF17: Ao receber o comando “Normal Start”, o robˆo que est´a na posi¸c˜ao “Goleiro”
deve se posicionar pr´oximo `a linha de fundo, em frente ao seu pr´oprio gol caso a
bola esteja `a uma distˆancia menor que 800 mm. em rela¸c˜ao ao gol que est´a sendo
defendido e o robˆo n˜ao seja o jogador mais pr´oximo `a bola.
•RF18: Ao receber o comando “Penalty” favor´avel `a equipe advers´aria, o jogador que
est´a na posi¸c˜ao “Goleiro” deve se posicionar sobre a linha do gol que est´a sendo
defendido de forma a bloquear a cobran¸ca do time advers´ario.
•RF19: Ao receber o comando “Kickoﬀ” favor´avel `a equipe advers´aria, o jogador que
est´a na posi¸c˜ao “Goleiro” deve se deve se posicionar pr´oximo `a linha de fundo, em
frente ao seu pr´oprio gol, de forma a estar centralizado sobre a linha imagin´aria que
liga a posi¸c˜ao atual da bola ao fundo do gol.
•RF20: Ao receber o comando “Free Kick” favor´avel `a equipe advers´aria, o jogador
que est´a na posi¸c˜ao “Goleiro” deve se deve se posicionar pr´oximo `a linha de fundo,
em frente ao seu pr´oprio gol, de forma a estar centralizado sobre a linha imagin´aria
que liga a posi¸c˜ao atual da bola ao fundo do gol.
•RF21: Ao receber o comando “Indirect Kick” favor´avel `a equipe advers´aria, o jogador
que est´a na posi¸c˜ao “Goleiro” deve se deve se posicionar pr´oximo `a linha de fundo,
em frente ao seu pr´oprio gol, de forma a estar centralizado sobre a linha imagin´aria
que liga a posi¸c˜ao atual da bola ao fundo do gol.
Requisitos Funcionais relativos ao jogador que est´a com o comportamento de
“Defensor Direito” em um determinado momento:
•RF22: Ao receber o comando “Stop Game”, o robˆo que est´a na posi¸c˜ao “Defensor
Direito” deve se posicionar em frente `a linha de sua ´area de defesa e na dire¸c˜ao da


154
trave do lado direito do gol que est´a sendo defendido caso a distˆancia entre a bola e
o gol defendido seja maior que 1800 mm;
•RF23: Ao receber o comando “Stop Game”, o robˆo que est´a na posi¸c˜ao “Defensor
Direito” deve se posicionar em frente `a bola, de forma a estar posicionado entre a
bola e o gol defendido, caso a distˆancia entre a bola e o gol defendido seja menor
que 1800 mm;
•RF24: Ao receber o comando “Free Kick” para sua pr´opria equipe, o robˆo que est´a
na posi¸c˜ao “Defensor Direito” deve se posicionar em frente `a linha de sua ´area de
defesa e na dire¸c˜ao da trave do lado direito do gol que est´a sendo defendido.
•RF25: Ao receber o comando “Free Kick” para a equipe advers´aria, o robˆo que est´a
na posi¸c˜ao “Defensor Direito” deve se posicionar fora da linha imagin´aria que liga a
bola ao fundo do gol que est´a sendo defendido.
•RF26: Ao receber o comando “Indirect Kick”, independente para qual equipe, o
robˆo que est´a na posi¸c˜ao “Defensor Direito” deve se posicionar em frente `a linha
de sua ´area de defesa e na dire¸c˜ao da trave do lado direito do gol que est´a sendo
defendido.
•RF27: Ao receber o comando “Penalty” favor´avel `a equipe advers´aria, o robˆo que
est´a na posi¸c˜ao “Defensor Direito” deve se posicionar fora da ´area de defesa e ao
lado direito da bola, respeitando a distˆancia m´ınima para a cobran¸ca da penalidada
m´axima.
•RF28: Ao receber o comando “Normal Start”, o robˆo que est´a na posi¸c˜ao “Defensor
Direito” deve se posicionar em frente `a linha de sua ´area de defesa e na dire¸c˜ao da
trave do lado direito do gol que est´a sendo defendido.
Requisitos Funcionais relativos ao jogador que est´a com o comportamento de
“Defensor Esquerdo” em um determinado momento:
•RF29: Ao receber o comando “Stop Game”, o robˆo que est´a na posi¸c˜ao “Defensor
Esquerdo” deve se posicionar em frente `a linha de sua ´area de defesa e na dire¸c˜ao da
trave do lado esquerdo do gol que est´a sendo defendido caso a distˆancia entre a bola
e o gol defendido seja maior que 1800 mm.;
•RF30: Ao receber o comando “Stop Game”, o robˆo que est´a na posi¸c˜ao “Defensor
Esquerdo” deve se posicionar em frente `a bola, de forma a estar posicionado entre a


155
bola e o gol defendido, caso a distˆancia entre a bola e o gol defendido seja menor
que 1800 mm;
•RF31: Ao receber o comando “Free Kick” para sua pr´opria equipe, o robˆo que est´a
na posi¸c˜ao “Defensor Esquerdo” deve se posicionar em frente `a linha de sua ´area de
defesa e na dire¸c˜ao da trave do lado esquerdo do gol que est´a sendo defendido.
•RF32: Ao receber o comando “Free Kick” para a equipe advers´aria, o robˆo que est´a
na posi¸c˜ao “Defensor Esquerdo” deve se posicionar fora da linha imagin´aria que liga
a bola ao fundo do gol que est´a sendo defendido.
•RF33: Ao receber o comando “Indirect Kick”, independente para qual equipe, o
robˆo que est´a na posi¸c˜ao “Defensor Esquerdo” deve se posicionar em frente `a linha
de sua ´area de defesa e na dire¸c˜ao da trave do lado esquerdo do gol que est´a sendo
defendido.
•RF34: Ao receber o comando “Penalty” favor´avel `a equipe advers´aria, o robˆo que
est´a na posi¸c˜ao “Defensor Esquerdo” deve se posicionar fora da ´area de defesa e ao
lado esquerdo da bola, respeitando a distˆancia m´ınima para a cobran¸ca da penalidada
m´axima.
•RF35: Ao receber o comando “Normal Start”, o robˆo que est´a na posi¸c˜ao “Defensor
Esquerdo” deve se posicionar em frente `a linha de sua ´area de defesa e na dire¸c˜ao da
trave do lado esquerdo do gol que est´a sendo defendido.
Requisitos Funcionais relativos ao jogador que est´a com o comportamento de
“Meio-Campo” em um determinado momento:
•RF36: Ao receber o comando “Stop Game”, o robˆo que est´a na posi¸c˜ao “Meio-Campo”
deve se posicionar sobre a linha imagin´aria que liga a posi¸c˜ao atual da bola ao fundo
do gol que est´a sendo defendido por ele;
•RF37: Ao receber o comando “Kickoﬀ” favor´avel `a equipe advers´aria, o robˆo que
est´a na posi¸c˜ao “Meio-Campo” deve se posicionar sobre a linha imagin´aria que liga
a posi¸c˜ao atual da bola ao fundo do gol que est´a sendo defendido por ele;
•RF38: Ao receber o comando “Kickoﬀ” favor´avel `a sua equipe, o robˆo que est´a na
posi¸c˜ao “Meio-Campo” deve se posicionar para executar a cobran¸ca em dire¸c˜ao ao
gol advers´ario.


156
•RF39: Ao receber o comando “Normal Start” ap´os o comando “Kickoﬀ” favor´avel `a
sua equipe, o robˆo que est´a na posi¸c˜ao “Meio-Campo” deve executar a cobran¸ca em
dire¸c˜ao ao gol advers´ario.
•RF40: Ao receber o comando “Direct Kick” favor´avel `a sua equipe, o robˆo que est´a
na posi¸c˜ao “Meio-Campo” deve se posicionar para executar a cobran¸ca em dire¸c˜ao
ao gol advers´ario.
•RF41: Ao receber o comando “Normal Start” ap´os o comando “Direck Kick” favor´avel
`a sua equipe, o robˆo que est´a na posi¸c˜ao “Meio-Campo” deve executar a cobran¸ca
em dire¸c˜ao ao gol advers´ario.
•RF42: Ao receber o comando “Indirect Kick” favor´avel `a equipe advers´aria, o robˆo
que est´a na posi¸c˜ao “Meio-Campo” deve se posicionar sobre a linha imagin´aria que
liga a posi¸c˜ao atual da bola ao fundo do gol que est´a sendo defendido por ele;
•RF43: Ao receber o comando “Indirect Kick” favor´avel `a sua equipe, o robˆo que est´a
na posi¸c˜ao “Meio-Campo” deve se posicionar para executar a cobran¸ca em dire¸c˜ao `a
um de seus companheiros.
•RF44: Ao receber o comando “Normal Start” ap´os o comando “Indireck Kick”
favor´avel `a sua equipe, o robˆo que est´a na posi¸c˜ao “Meio-Campo” deve executar a
cobran¸ca em dire¸c˜ao `a um de seus companheiros.
•RF45: Ao receber o comando “Penalty” para a equipe advers´aria, o robˆo que est´a
na posi¸c˜ao “Meio-Campo” deve se posicionar atr´as do cobrador da penalida m´axima,
respeitando a distˆancia m´ınima.
•RF46: Ao receber o comando “Penalty” favor´avel `a sua equipe, o robˆo que est´a na
posi¸c˜ao “Meio-Campo” deve se posicionar para executar a cobran¸ca da penalida
m´axima.
•RF47: Ao receber o comando “Normal Start” ap´os o comando “Penalty” favor´avel `a
sua equipe, o robˆo que est´a na posi¸c˜ao “Meio-Campo” deve executar a cobran¸ca da
penalidade m´axima em dire¸c˜ao ao gol advers´ario.
Requisitos Funcionais relativos ao jogador que est´a com o comportamento de
“Atacante Esquerdo” em um determinado momento:


157
•RF48: Ao receber o comando “Stop Game”, o robˆo que est´a na posi¸c˜ao “Atacante
Esquerdo” deve se posicionar sobre a linha imagin´aria que liga a posi¸c˜ao atual da
bola ao fundo do gol que est´a sendo defendido por ele;
•RF49: Ao receber o comando “Direct Kick”, o robˆo que est´a na posi¸c˜ao “Atacante
Esquerdo” deve se posicionar pr´oximo `a trave esquerda do gol advers´ario.
•RF50: Ao receber o comando “Indirect Kick”, o robˆo que est´a na posi¸c˜ao “Atacante
Esquerdo” deve se posicionar pr´oximo `a trave esquerda do gol advers´ario.
•RF51: Ao receber o comando “Penalty” favor´avel `a sua equipe, o robˆo que est´a
na posi¸c˜ao “Atacante Esquerdo” deve se posicionar junto `a linha da ´area de defesa
do time advers´ario e ao lado esquerdo do robˆo que est´a efetuando a cobran¸ca da
penalidade m´axima.
•RF52: Ao receber o comando “Penalty” favor´avel `a equipe advers´aria, o robˆo que
est´a na posi¸c˜ao “Atacante Esquerdo” deve se posicionar pr´oximo `a trave esquerda
do gol advers´ario.
•RF53: Ao receber o comando “Normal Start”, o robˆo que est´a na posi¸c˜ao “Atacante
Esquerdo” deve se posicionar pr´oximo `a trave esquerda do gol advers´ario caso n˜ao
seja o robˆo da equipe que est´a sendo controlada mais pr´oximo `a bola.
Requisitos Funcionais relativos ao jogador que est´a com o comportamento de
“Atacante Direito” em um determinado momento:
•RF54: Ao receber o comando “Stop Game”, o robˆo que est´a na posi¸c˜ao “Atacante
Direito” deve se posicionar sobre a linha imagin´aria que liga a posi¸c˜ao atual da bola
ao fundo do gol que est´a sendo defendido por ele;
•RF55: Ao receber o comando “Direct Kick”, o robˆo que est´a na posi¸c˜ao “Atacante
Direito” deve se posicionar pr´oximo `a trave direita do gol advers´ario.
•RF56: Ao receber o comando “Indirect Kick”, o robˆo que est´a na posi¸c˜ao “Atacante
Direito” deve se posicionar pr´oximo `a trave direita do gol advers´ario.
•RF57: Ao receber o comando “Penalty” favor´avel `a sua equipe, o robˆo que est´a na
posi¸c˜ao “Atacante Direito” deve se posicionar junto `a linha da ´area de defesa do time
advers´ario e ao lado direito do robˆo que est´a efetuando a cobran¸ca da penalidade
m´axima.


158
•RF58: Ao receber o comando “Penalty” favor´avel `a equipe advers´aria, o robˆo que
est´a na posi¸c˜ao “Atacante Direito” deve se posicionar pr´oximo `a trave direita do gol
advers´ario.
•RF59: Ao receber o comando “Normal Start”, o robˆo que est´a na posi¸c˜ao “Atacante
Direito” deve se posicionar pr´oximo `a trave direita do gol advers´ario caso n˜ao seja o
robˆo da equipe que est´a sendo controlada mais pr´oximo `a bola.


159
APˆENDICE C -- CONJUNTO DE RULES APLICADAS `A SOLUC¸ ˜AO
DESENVOLVIDA SOB O VI´ES DO PON
Este apˆendice apresenta o conjunto de Rules que foram elaboradas e aplicadas `as
aplica¸c˜oes PON de controle para uma partida de futebol de robˆos utilizando diagrama de
Rules e a sintaxe deﬁnida pela LingPON.
C.1
DIAGRAMA DE OBJETOS PON
A Figura 38 apresenta a nota¸c˜ao proposta por [Kossoski et al.
2014] para
representar os objetos PON. Um FBE est´a representado como um objeto retangular. O
Attribute ´e representado como um triˆangulo. A Premise ´e representada como um losango
simbolizando uma decis˜ao. Uma Rule ´e representada com um objeto que desencadeia
um ﬂuxo de execu¸c˜ao em um sentido. Considerou-se Condition como parte integrante
da respectiva Rule. O Method ´e representado como uma engrenagem. O sentido das
notiﬁca¸c˜oes ´e representado como uma seta [Kossoski et al. 2014].
Figura 38: Elementos do diagrama de objetos PON [Kossoski et al. 2014].
Para facilitar o entendimento dos diagrama de objetos PON apresentados, a
Tabela 3 apresenta a deﬁni¸c˜ao de todas as Premises referenciadas pelos diagramas de
objetos PON.


160
Tabela 3: Deﬁni¸c˜ao das Premises utilizadas pelas Rules na aplica¸c˜ao de controle de
futebol de robˆos.
Premise
C´odigo da Premise
prRobotMoveX
Robot.atPosX != Robot.atPosToGoX
prRobotMoveY
Robot.atPosY != Robot.atPosToGoY
prAngleMove
Robot.atAngle != Robot.atAngleToGo
prRobotIsReady
Robot.atIsReady == TRUE
prRobotIsNotReady
Robot.atIsReady == FALSE
prBallEnemyField
Robot.atBallEnemyField == TRUE
prBallTeamField
Robot.atBallEnemyField == FALSE
prClosestToBall
Robot.atClosestToBall == TRUE
prNotClosestToBall
Robot.atClosestToBall == FALSE
prEnemyOnLineGoal
Robot.atEnemyOnGoalLine == TRUE
prNoEnemyOnLineGoal
Robot.atEnemyOnGoalLine == FALSE
prBallIsClose
Robot.atDistanceToBall < 300.0
prBallIsFar
Robot.atDistanceToBall ≥300.0
prBallCloseTeamGoal
Robot.atBallDistanceToTeamGoal ≤1800.0
prBallFarTeamGoal
Robot.atBallDistanceToTeamGoal > 1800.0
prBallInsideGoalArea
Robot.atBallDistanceToTeamGoal ≤800
prBallNotInsideGoalArea
Robot.atBallDistanceToTeamGoal > 800
prRefereeCmdStop
Robot.atRefereeCmd == ‘S’
prRefereeCmdKickoﬀBlue
Robot.atRefereeCmd == ‘K’
prRefereeCmdKickoﬀYellow
Robot.atRefereeCmd == ‘k’
prRefereeCmdStartGame
Robot.atRefereeCmd == ‘ ’
prRefereeCmdDirectKickBlue
Robot.atRefereeCmd == ‘F’
prRefereeCmdDirectKickYellow
Robot.atRefereeCmd == ‘f’
prRefereeCmdPenaltyBlue
Robot.atRefereeCmd == ‘P’
prRefereeCmdPenaltyYellow
Robot.atRefereeCmd == ‘p’
prRefereeCmdIndirectKickBlue
Robot.atRefereeCmd == ‘I’
prRefereeCmdIndirectKickYellow
Robot.atRefereeCmd == ‘i’
prLastRefereeCmdKickoﬀBlue
Robot.atRefereeCmd == ‘I’
prLastRefereeCmdKickoﬀYellow
Robot.atRefereeCmd == ‘i’
prLastRefereeCmdPenaltyBlue
Robot.atLastRefereeCmd == ‘P’
prLastRefereeCmdPenaltyYellow
Robot.atLastRefereeCmd == ‘p’
prActiveRole
Robot.atRole != “ ”
prLinePlayerRole
Robot.atRole != “GOALKEEPER”
prRoleGoalkeeper
Robot.atRole == “GOALKEEPER”
prRoleDefenderLeft
Robot.atRole == “DEFENDER LEFT”
prRoleDefenderRight
Robot.atRole == “DEFENDER RIGHT”
prRoleMidﬁeldOnly
Robot.atRole == “MIDFIELD ONLY”
prRoleStrickerLeft
Robot.atRole == “STRIKER LEFT”
prRoleStrickerRight
Robot.atRole == “STRIKER RIGHT”
prTeamLeftSide
Robot.atTeamSide = “LEFT”
prTeamRightSide
Robot.atTeamSide = “RIGHT”
prTeamBlue
Robot.atTeamColor == “BLUE”
prTeamYellow
Robot.atTeamColor == “YELLOW”
prFreePartner
Robot.atPartnerFreeID ≥0
prNoFreePartner
Robot.atPartnerFreeID < 0


161
A seguir, todas as Rules s˜ao apresentadas segundo o diagrama de objetos PON.
Figura 39: Diagrama de objetos PON das Rules rlRobotMoveX, rlRobotMoveY, rlAngle-
Move e rlBallFar.
Figura 40: Diagrama de objetos PON da Rule rlStartTargetToBall.


162
Figura 41: Diagrama de objetos PON das Rules rlStartFreePartner e rlStartFreePartner-
Pass.
Figura 42: Diagrama de objetos PON das Rules rlStartNoFreePartner e rlStartNoFree-
PartnerKick.


163
Figura 43: Diagrama de objetos PON das Rules rlStartEnemyPositionKick e rlStartE-
nemyFieldKick
.
Figura 44: Diagrama de objetos PON das Rules rlGoalkeeperStopCloseGoal e rlGoalKe-
eperStopFarGoal.


164
Figura 45: Diagrama de objetos PON das Rules rlGoalkeeperStartInsideAreaClosestBall
e rlGoalkeeperStartInsideAreaClosestBallKick.
Figura 46: Diagrama de objetos PON das Rules rlGoalkeeperStartInsideArea e rlGoalke-
eperStartOutsideArea.


165
Figura 47: Diagrama de objetos PON das Rules rlGoalkeeperBluePenaltyYellow e
rlGoalkeeperYellowPenaltyBlue.
Figura 48: Diagrama de objetos PON das Rules rlDefenderLeftStopBallFar e rlDefender-
LeftStopBallClose.


166
Figura 49: Diagrama de objetos PON das Rules rlDefenderLeftBlueDirectKickBlue e
rlDefenderLeftYellowDirectKickYellow.
Figura 50: Diagrama de objetos PON das Rules rlDefenderLeftBlueIndirectKickBlue e
rlDefenderLeftYellowIndirectKickYellow.
Figura 51: Diagrama de objetos PON das Rules rlDefenderLeftBluePenaltyYellow e
rlDefenderLeftYellowPenaltyBlue.


167
Figura 52: Diagrama de objetos PON da Rule rlDefenderLefStartBallNotClose.
Figura 53: Diagrama de objetos PON das Rules rlDefenderRightStopBallFar e rlDefen-
derRightStopBallClose.
Figura 54: Diagrama de objetos PON das Rules rlDefenderRightBlueDirectKickBlue e
rlDefenderRightYellowDirectKickYellow.


168
Figura 55: Diagrama de objetos PON das Rules rlDefenderRightBlueIndirectKickBlue e
rlDefenderRightYellowIndirectKickYellow.
Figura 56: Diagrama de objetos PON das Rules rlDefenderRightBluePenaltyYellow e
rlDefenderRightYellowPenaltyBlue.
Figura 57: Diagrama de objetos PON da Rule rlDefenderRightStartBallNotClose.


169
Figura 58: Diagrama de objetos PON da Rule rlMidﬁeldOnlyStop.
Figura 59: Diagrama de objetos PON das Rules rlMidﬁeldOnlyBlueKickoﬀe rlMidﬁel-
dOnlyYellowKickoﬀ.
Figura 60: Diagrama de objetos PON das Rules rlMidﬁeldOnlyBlueReadyKickoﬀBlue e
rlMidﬁeldOnlyYellowReadyKickoﬀYellow.


170
Figura 61: Diagrama de objetos PON das Rules rlMidﬁeldOnlyBlueDirectKick e rlMidﬁ-
eldOnlyYellowDirectKick.
Figura 62: Diagrama de objetos PON das Rules rlMidﬁeldOnlyBlueIndirectKick e
rlMidﬁeldOnlyYellowIndirectKick.
Figura 63: Diagrama de objetos PON das Rules rlMidﬁeldOnlyBluePenaltyBlue e
rlMidﬁeldOnlyYellowPenaltyYellow.


171
Figura 64: Diagrama de objetos PON das Rules rlMidﬁeldOnlyBluePenaltyYellow e
rlMidﬁeldOnlyYellowPenaltyBlue.
Figura 65: Diagrama de objetos PON das Rules rlMidﬁeldOnlyBlueReadyPenaltyBlue e
rlMidﬁeldOnlyYellowReadyPenaltyYellow.


172
Figura 66: Diagrama de objetos PON das Rules rlStrikerLeftStopTeamLeft e rlStriker-
LeftStopTeamRight.
Figura 67: Diagrama de objetos PON das Rules rlStrikerLeftBlueDirectKick e rlStriker-
LeftYellowDirectKick.


173
Figura 68: Diagrama de objetos PON das Rules rlStrikerLeftBlueIndirectKick e rlStri-
kerLeftYellowIndirectKick.
Figura 69: Diagrama de objetos PON das Rules rlStrikerLeftBluePenaltyBlue e rlStri-
kerLeftYellowPenaltyYellow.
Figura 70: Diagrama de objetos PON das Rules rlStrikerLeftBluePenaltyYellow e rlStri-
kerLeftYellowPenaltyBlue.


174
Figura 71: Diagrama de objetos PON da Rule rlStrikerLeftStartBallNotClose.
Figura 72: Diagrama de objetos PON das Rules rlStrikerRightStopTeamLeft e rlStriker-
RightStopTeamRight.
Figura 73: Diagrama de objetos PON das Rules rlStrikerRightBlueDirectKick e rlStri-
kerRightYellowDirectKick.


175
Figura 74: Diagrama de objetos PON das Rules rlStrikerRightBlueIndirectKick e rlStri-
kerRightYellowIndirectKick.
Figura 75: Diagrama de objetos PON das Rules rlStrikerRightBluePenaltyBlue e rlStri-
kerRightYellowPenaltyYellow.
Figura 76: Diagrama de objetos PON das Rules rlStrikerRightBluePenaltyYellow e
rlStrikerRightYellowPenaltyBlue.


176
Figura 77: Diagrama de objetos PON das Rules rlStrikerRightStartBallNotClose.


177
C.2
C´ODIGO-FONTE DAS RULES DESENVOLVIDAS PARA O SOFTWARE PON
De forma a facilitar o entendimento para o leitor, a primeira Rule ser´a apresentada
em um formato textual e relacionada ao c´odigo LingPON referente.
A Rule rlMOBlueReadyKickoﬀBlue deﬁne que se a fun¸c˜ao do robˆo (atRole) for
meio-campo (MIDFIELD ONLY), o comando atual enviado pelo ´arbitro (atRefereeCmd)
for “Inicie a jogada” (Start), o comando predecessor enviado pelo ´arbitro (atLastRe-
fereeCmd) for posse de bola para o time azul (‘K’) e a cor do time do robˆo (atTeam-
Color) for azul (Blue) ent˜ao o robˆo deve chutar a bola em dire¸c˜ao ao gol advers´ario
(Robot.mtReadyKickoﬀ). Esta Rule ´e executada no in´ıcio da partida no meio do campo
(kickoﬀ) pelo time Azul (Blue), ou ap´os um gol do time advers´ario, no rein´ıcio da partida.
O c´odigo LingPON referente a essa Rule ´e apresentado pela Rule 1.
Rule 1: C´odigo da Rule rlMOBlueReadyKickoﬀBlue.
1
fbeRule rlMOBlueReadyKickoﬀBlue
2
condition
3
premise prRoleMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY”
and
4
premise prRefereeCmdStartGame Robot.atRefereeCmd == ‘ ’ and
5
premise prLastCmdKickoﬀBlue Robot.atLastRefereeCmd == ‘K’ and
6
premise prTeamBlue Robot.atTeamColor == “BLUE”
7
end condition
8
action
9
instigation inMOBlueReadyKickoﬀBlue Robot.mtReadyKickoﬀ();
10
end action
11
end fbeRule
As demais 73 Rules que comp˜oem o conhecimento l´ogico-causal completo da
aplica¸c˜ao de controle para uma partida de futebol de robˆos s˜ao apresentadas na sequˆencia,
para ﬁns de eventuais consultas, e por motivos de completude da descri¸c˜ao da aplica¸c˜ao.


178
Rule 2: C´odigo da Rule rlRobotMoveX.
1
fbeRule rlRobotMoveX
2
condition
3
premise prRobotMoveX Robot.atPosX != Robot.atPosToGoX
4
end condition
5
action
6
instigation inMoveX Robot.mtExecuteMove();
7
end action
8
end fbeRule
Rule 3: C´odigo da Rule rlRobotMoveY.
1
fbeRule rlRobotMoveY
2
condition
3
premise prRobotMoveY Robot.atPosY != Robot.atPosToGoY
4
end condition
5
action
6
instigation inMoveY Robot.mtExecuteMove();
7
end action
8
end fbeRule
Rule 4: C´odigo da Rule rlAngleMove.
1
fbeRule rlAngleMove
2
condition
3
premise prAngleMove Robot.atAngle != Robot.atAngleToGo;
4
end condition
5
action
6
instigation inAngleMove Robot.mtAngleMove();
7
end action
8
end fbeRule


179
Rule 5: C´odigo da Rule rlBallFar.
1
fbeRule rlBallFar
2
condition
3
premise prBallIsFar Robot.atDistanceToBall >= 300 and
4
premise prActiveRole Robot.atRole != “ ” and
5
end condition
6
action
7
instigation inReset Robot.mtResetKick();
8
end action
9
end fbeRule
Rule 6: C´odigo da Rule rlStartFreePartner.
1
fbeRule rlStartFreePartner
2
condition
3
premise prRefereeCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prLinePlayerRole Robot.atRole != “GOALKEEPER” and
5
premise prBallTeamField Robot.atBallEnemyField == false and
6
premise prClosestToBall Robot.atClosestToBall == true and
7
premise prFreePartner Robot.atPartnerFreeID >= 0 and
8
premise prRobotIsNotReady Robot.atIsReady == false
9
end condition
10
action
11
instigation inPosPassBallPartner Robot.mtPosPassBall();
12
end action
13
end fbeRule


180
Rule 7: C´odigo da Rule rlStartFreePartnerPass.
1
fbeRule rlStartFreePartnerPass
2
condition
3
premise prRefereeCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prLinePlayerRole Robot.atRole != “GOALKEEPER” and
5
premise prBallTeamField Robot.atBallEnemyField == false and
6
premise prClosestToBall Robot.atClosestToBall == true and
7
premise prFreePartner Robot.atPartnerFreeID >= 0 and
8
premise prRobotIsNotReady Robot.atIsReady == true
9
end condition
10
action
11
instigation inPassBallPartner Robot.mtPassBallPartner()
12
end action
13
end fbeRule
Rule 8: C´odigo da Rule rlStartNoFreePartner.
1
fbeRule rlStartNoFreePartner
2
condition
3
premise prRefereeCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prLinePlayerRole Robot.atRole != “GOALKEEPER” and
5
premise prBallTeamField Robot.atBallEnemyField == false and
6
premise prClosestToBall Robot.atClosestToBall == true and
7
premise prFreePartner Robot.atPartnerFreeID <= 0 and
8
premise prRobotIsNotReady Robot.atIsReady == false
9
end condition
10
action
11
instigation inPosKickNoFreePartner Robot.mtMovePositionToKick()
12
end action
13
end fbeRule


181
Rule 9: C´odigo da Rule rlStartNoFreePartnerKick.
1
fbeRule rlStartNoFreePartnerKick
2
condition
3
premise prRefereeCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prLinePlayerRole Robot.atRole != “GOALKEEPER” and
5
premise prBallTeamField Robot.atBallEnemyField == false and
6
premise prClosestToBall Robot.atClosestToBall == true and
7
premise prFreePartner Robot.atPartnerFreeID <= 0 and
8
premise prRobotIsNotReady Robot.atIsReady == true
9
end condition
10
action
11
instigation inKickNoFreePartner Robot.mtReadyKickoﬀ()
12
end action
13
end fbeRule
Rule 10: C´odigo da Rule rlStartEnemyFieldPositionKick.
1
fbeRule rlStartEnemyFieldPositionKick
2
condition
3
premise prRefereeCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prLinePlayerRole Robot.atRole != “GOALKEEPER” and
5
premise prBallEnemyField Robot.atBallEnemyField == true and
6
premise prNoEnemyOnLineGoal Robot.atEnemyOnGoalLine == true
and
7
premise prClosestToBall Robot.atClosestToBall == true and
8
premise prRobotIsNotReady Robot.atIsReady == false and
9
end condition
10
action
11
instigation inPosKickEnemyField Robot.mtMovePositionToKick()
12
end action
13
end fbeRule


182
Rule 11: C´odigo da Rule rlStartEnemyFieldKick.
1
fbeRule rlStartEnemyFieldKick
2
condition
3
premise prRefereeCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prLinePlayerRole Robot.atRole != “GOALKEEPER” and
5
premise prBallEnemyField Robot.atBallEnemyField == true and
6
premise prNoEnemyOnLineGoal Robot.atEnemyOnGoalLine == true
and
7
premise prClosestToBall Robot.atClosestToBall == true and
8
premise prRobotIsNotReady Robot.atIsReady == true and
9
end condition
10
action
11
instigation inKickEnemyField Robot.mtReadyKickoﬀ()
12
end action
13
end fbeRule
Rule 12: C´odigo da Rule rlStartTargetToBall.
1
fbeRule rlStartTargetToBall
2
condition
3
premise prRefereeCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prActiveRole Robot.atRole != “ ” and
5
premise prNotClosestToBall Robot.atClosestToBall == false and
6
end condition
7
action
8
instigation inTargetToBall Robot.mtTargetToBall()
9
end action
10
end fbeRule


183
Rule 13: C´odigo da Rule rlGkStopCloseGoal.
1
fbeRule rlGkStopCloseGoal
2
condition
3
premise prRefereeCmdStop Robot.atRefereeCmd == ‘S’ and
4
premise prRoleGoalkeeper Robot.atRole == “GOALKEEPER” and
5
premise prBallCloseTeamGoal Robot.atBallDistTeamGoal <= 1800
6
end condition
7
action
8
instigation inGkStopClose Robot.mtGkEnemyPenalty()
9
end action
10
end fbeRule
Rule 14: C´odigo da Rule rlGkStopFarGoal.
1
fbeRule rlGkStopFarGoal
2
condition
3
premise prRefereeCmdStop Robot.atRefereeCmd == ‘S’ and
4
premise prRoleGoalkeeper Robot.atRole == “GOALKEEPER” and
5
premise prBallCloseTeamGoal Robot.atBallDistTeamGoal >1800
6
end condition
7
action
8
instigation inGkStopFarGoal Robot.mtGkOutArea()
9
end action
10
end fbeRule


184
Rule 15: C´odigo da Rule rlGkStartInsideAreaClosestBall.
1
fbeRule rlGkStartInsideAreaClosestBall
2
condition
3
premise prRefereeCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prRoleGoalkeeper Robot.atRole == “GOALKEEPER” and
5
premise prBallInGoalArea Robot.atBallDistTeamGoal <= 800 and
6
premise prClosestToBall Robot.atClosestToBall == true and
7
premise prRobotIsNotReady Robot.atIsReady == false
8
end condition
9
action
10
instigation inGkStartInside Robot.mtMovePositionToKick()
11
end action
12
end fbeRule
Rule 16: C´odigo da Rule rlGkStartInsideAreaClosestBallKick.
1
fbeRule rlGkStartInsideAreaClosestBallKick
2
condition
3
premise prRefereeCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prRoleGoalkeeper Robot.atRole == “GOALKEEPER” and
5
premise prBallInGoalArea Robot.atBallDistTeamGoal <= 800 and
6
premise prClosestToBall Robot.atClosestToBall == true and
7
premise prRobotIsNotReady Robot.atIsReady == true
8
end condition
9
action
10
instigation inGkAreaKick Robot.mtReadyKickoﬀ()
11
end action
12
end fbeRule


185
Rule 17: C´odigo da Rule rlGkStartInsideArea.
1
fbeRule rlGkStartInsideArea
2
condition
3
premise prRefereeCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prRoleGoalkeeper Robot.atRole == “GOALKEEPER” and
5
premise prBallInsideGoalArea Robot.atBallDistTeamGoal <= 800
and
6
premise prNotClosestToBall Robot.atClosestToBall == false
7
end condition
8
action
9
instigation inGkStartInArea Robot.mtGkEnemyPenalty()
10
end action
11
end fbeRule
Rule 18: C´odigo da Rule rlGkStartOutsideArea.
1
fbeRule rlGkStartOutsideArea
2
condition
3
premise prRefereeCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prRoleGoalkeeper Robot.atRole == “GOALKEEPER” and
5
premise prBallNotInGoalArea Robot.atBallDistTeamGoal >800
6
end condition
7
action
8
instigation inGkStartOutArea Robot.mtGkOutArea()
9
end action
10
end fbeRule


186
Rule 19: C´odigo da Rule rlGkBluePenaltyYellow.
1
fbeRule rlGkBluePenaltyYellow
2
condition
3
premise prRefereeCmdPenaltyYellow Robot.atRefereeCmd == ‘p’
and
4
premise prRoleGoalkeeper Robot.atRole == “GOALKEEPER” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inGkEnemyPenalty1 Robot.mtGkEnemyPenalty()
9
end action
10
end fbeRule
Rule 20: C´odigo da Rule rlGkYellowPenaltyBlue.
1
fbeRule rlGkYellowPenaltyBlue
2
condition
3
premise prRefereeCmdPenaltyYellow Robot.atRefereeCmd == ‘P’
and
4
premise prRoleGoalkeeper Robot.atRole == “GOALKEEPER” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inGkEnemyPenalty2 Robot.mtGkEnemyPenalty()
9
end action
10
end fbeRule


187
Rule 21: C´odigo da Rule rlDLtStopBallFar.
1
fbeRule rlDLtStopBallFar
2
condition
3
premise prRefereeCmdStop Robot.atRefereeCmd == ‘S’ and
4
premise prRoleDefLeft Robot.atRole == “DEFENDER LEFT” and
5
premise prBallFarTeamGoal Robot.atBallDistTeamGoal >1800
6
end condition
7
action
8
instigation inStopDLFar Robot.mtMoveLeftPost()
9
end action
10
end fbeRule
Rule 22: C´odigo da Rule rlDLStopBallClose.
1
fbeRule rlDLStopBallClose
2
condition
3
premise prRefereeCmdStop Robot.atRefereeCmd == ‘S’ and
4
premise prRoleDefLeft Robot.atRole == “DEFENDER LEFT” and
5
premise prBallCloseTeamGoal Robot.atBallDistTeamGoal == 800
6
end condition
7
action
8
instigation inDLStopBallClose Robot.mtMovePosAngleNeg3pl()
9
end action
10
end fbeRule
Rule 23: C´odigo da Rule rlDLBlueDirectKickBlue.
1
fbeRule rlDLBlueDirectKickBlue
2
condition
3
premise prRefCmdDirectKickBlue Robot.atRefereeCmd == ‘F’ and
4
premise prRoleDefLeft Robot.atRole == “DEFENDER LEFT” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inDLBlueDirectKickBlue Robot.mtMoveLeftPost()
9
end action
10
end fbeRule


188
Rule 24: C´odigo da Rule rlDLYellowDirectKickYellow.
1
fbeRule rlDLYellowDirectKickYellow
2
condition
3
premise prRefCmdDirectKickYellow Robot.atRefereeCmd == ‘f’ and
4
premise prRoleDefLeft Robot.atRole == “DEFENDER LEFT” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inDLYellowDirectKickYellow Robot.mtMoveLeftPost()
9
end action
10
end fbeRule
Rule 25: C´odigo da Rule rlDLtBlueIndirectBlue.
1
fbeRule rlDLtBlueIndirectBlue
2
condition
3
premise prRefCmdIndirectKickBlue Robot.atRefereeCmd == ‘I’ and
4
premise prRoleDefLeft Robot.atRole == “DEFENDER LEFT” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inDLtBlueIndirectBlue Robot.mtMoveLeftPost()
9
end action
10
end fbeRule


189
Rule 26: C´odigo da Rule rlDLYellowIndirectYellow.
1
fbeRule rlDLYellowIndirectYellow
2
condition
3
premise prRefCmdIndirectKickYellow Robot.atRefereeCmd == ‘i’
and
4
premise prRoleDefLeft Robot.atRole == “DEFENDER LEFT” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inDLYellowIndirectYellow Robot.mtMoveLeftPost()
9
end action
10
end fbeRule
Rule 27: C´odigo da Rule rlDLtBluePenaltyYellow.
1
fbeRule rlDLtBluePenaltyYellow
2
condition
3
premise prRefCmdPenaltyYellow Robot.atRefereeCmd == ‘p’ and
4
premise prRoleDefLeft Robot.atRole == “DEFENDER LEFT” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inDLtBluePenaltyYellow Robot.mtMovePenaltyDefLeft()
9
end action
10
end fbeRule


190
Rule 28: C´odigo da Rule rlDLYellowPenaltyBlue.
1
fbeRule rlDLYellowPenaltyBlue
2
condition
3
premise prRefCmdPenaltyBlue Robot.atRefereeCmd == ‘P’ and
4
premise prRoleDefLeft Robot.atRole == “DEFENDER LEFT” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inDLYellowPenaltyBlue Robot.mtMovePenaltyDefLeft()
9
end action
10
end fbeRule
Rule 29: C´odigo da Rule rlDLStartNotClose.
1
fbeRule rlDLStartNotClose
2
condition
3
premise prRefCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prRoleDefLeft Robot.atRole == “DEFENDER LEFT” and
5
premise prNotClosestToBall Robot.atClosestToBall == false
6
end condition
7
action
8
instigation inDLStartNotClose Robot.mtMoveLeftPost()
9
end action
10
end fbeRule
Rule 30: C´odigo da Rule rlDRStopBallFar.
1
fbeRule rlDRStopBallFar
2
condition
3
premise prRefereeCmdStop Robot.atRefereeCmd == ‘S’ and
4
premise prDefRight Robot.atRole == “DEFENDER RIGHT” and
5
premise prBallFarTeamGoal Robot.atBallDistTeamGoal >1800
6
end condition
7
action
8
instigation inDRStopBallFar Robot.mtMoveRightPost()
9
end action
10
end fbeRule


191
Rule 31: C´odigo da Rule rlDRStopBallClose.
1
fbeRule rlDRStopBallClose
2
condition
3
premise prRefereeCmdStop Robot.atRefereeCmd == ‘S’ and
4
premise prDefRight Robot.atRole == “DEFENDER RIGHT” and
5
premise prBallCloseTeamGoal Robot.atBallDistTeamGoal <= 1800
6
end condition
7
action
8
instigation inDRStopBallClose Robot.mtMovePosAnglePos3pl()
9
end action
10
end fbeRule
Rule 32: C´odigo da Rule rlDRBlueDirectKickBlue.
1
fbeRule rlDRBlueDirectKickBlue
2
condition
3
premise prRefCmdDirectKickBlue Robot.atRefereeCmd == ‘F’ and
4
premise prDefRight Robot.atRole == “DEFENDER RIGHT” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inDRBlueDirectKickBlue Robot.mtMoveRightPost()
9
end action
10
end fbeRule


192
Rule 33: C´odigo da Rule rlDRYellowDirectKickYellow.
1
fbeRule rlDRYellowDirectKickYellow
2
condition
3
premise prRefCmdCmdDirectKickYellow Robot.atRefereeCmd == ‘f’
and
4
premise prDefRight Robot.atRole == “DEFENDER RIGHT” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW’
6
end condition
7
action
8
instigation inDRYellowDirectKickYellow Robot.mtMoveRightPost()
9
end action
10
end fbeRule
Rule 34: C´odigo da Rule rlDRBlueIndirectKickBlue.
1
fbeRule rlDRBlueIndirectKickBlue
2
condition
3
premise prRefCmdIndirectKickBlue Robot.atRefereeCmd == ‘I’ and
4
premise prDefRight Robot.atRole == “DEFENDER RIGHT” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inDRBlueIndirectKickBlue Robot.mtMoveRightPost()
9
end action
10
end fbeRule


193
Rule 35: C´odigo da Rule rlDRtYellowIndirectKickYellow.
1
fbeRule rlDRtYellowIndirectKickYellow
2
condition
3
premise prRefCmdIndirectKickYellow Robot.atRefereeCmd == ‘i’
and
4
premise prDefRight Robot.atRole == “DEFENDER RIGHT” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inDRtYellowIndirectKickYellow Robot.mtMoveRightPost()
9
end action
10
end fbeRule
Rule 36: C´odigo da Rule rlDRBluePenaltyYellow.
1
fbeRule rlDRBluePenaltyYellow
2
condition
3
premise prRefCmdPenaltyYellow Robot.atRefereeCmd == ‘p’ and
4
premise prDefRight Robot.atRole == “DEFENDER RIGHT” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inDRBluePenaltyYellow Robot.mtMovePenaltyDefRight()
9
end action
10
end fbeRule


194
Rule 37: C´odigo da Rule rlDRYellowPenaltyBlue.
1
fbeRule rlDRYellowPenaltyBlue
2
condition
3
premise prRefCmdPenaltyBlue Robot.atRefereeCmd == ‘P’ and
4
premise prDefRight Robot.atRole == “DEFENDER RIGHT” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inDRYellowPenaltyBlue Robot.mtMovePenaltyDefRight()
9
end action
10
end fbeRule
Rule 38: C´odigo da Rule rlDRStartBallNotClose.
1
fbeRule rlDRStartBallNotClose
2
condition
3
premise prRefCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prDefRight Robot.atRole == “DEFENDER RIGHT” and
5
premise prNotClosestToBall Robot.atClosestToBall == false
6
end condition
7
action
8
instigation inDRStartBallNotClose Robot.mtMoveRightPost()
9
end action
10
end fbeRule
Rule 39: C´odigo da Rule rlMOStop.
1
fbeRule rlMOStop
2
condition
3
premise prRefereeCmdStop Robot.atRefereeCmd == ‘S’ and
4
premise prMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY”
5
end condition
6
action
7
instigation inMOStop Robot.mtMoveStopPosition()
8
end action
9
end fbeRule


195
Rule 40: C´odigo da Rule rlMOBlueKickoﬀ.
1
fbeRule rlMOBlueKickoﬀ
2
condition
3
premise prRefCmdKickoﬀBlue Robot.atRefereeCmd == ‘K’ and
4
premise prMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inMOBlueKickoﬀRobot.mtMovePositionToKick()
9
end action
10
end fbeRule
Rule 41: C´odigo da Rule rlMOYellowKickoﬀ.
1
fbeRule rlMOYellowKickoﬀ
2
condition
3
premise prRefCmdKickoﬀYellow Robot.atRefereeCmd == ‘k’ and
4
premise prMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inMOYellowKickoﬀRobot.mtMovePositionToKick()
9
end action
10
end fbeRule


196
Rule 42: C´odigo da Rule rlMOYellowReadyKickoﬀYellow.
1
fbeRule rlMOYellowReadyKickoﬀYellow
2
condition
3
premise prRefCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY” and
5
premise prLastRefCmdKickoﬀYellow Robot.atLastRefCmd == ‘k’
and
6
premise prTeamYellow Robot.atTeamColor == “YELLOW”
7
end condition
8
action
9
instigation inMOYellowReadyKickoﬀYellow Robot.mtReadyKickoﬀ()
10
end action
11
end fbeRule
Rule 43: C´odigo da Rule rlMOBlueDirectKick.
1
fbeRule rlMOBlueDirectKick
2
condition
3
premise prRefCmdDirectKickBlue Robot.atRefereeCmd == ‘K’ and
4
premise prMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inMOBlueDirectKick Robot.mtMovePositionToKick()
9
end action
10
end fbeRule


197
Rule 44: C´odigo da Rule rlMOYellowDirectKick.
1
fbeRule rlMOYellowDirectKick
2
condition
3
premise prRefCmdDirectKickYellow Robot.atRefereeCmd == ‘f’ and
4
premise prMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inMOYellowDirectKick Robot.mtMovePositionToKick()
9
end action
10
end fbeRule
Rule 45: C´odigo da Rule rlMOBlueIndirectKick.
1
fbeRule rlMOBlueIndirectKick
2
condition
3
premise prRefCmdIndirectKickBlue Robot.atRefereeCmd == ‘I’ and
4
premise prMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inMOBlueIndirectKick Robot.mtMoveIndirectKick()
9
end action
10
end fbeRule


198
Rule 46: C´odigo da Rule rlMOYellowIndirectKick.
1
fbeRule rlMOYellowIndirectKick
2
condition
3
premise prRefCmdIndirectKickYellow Robot.atRefereeCmd == ‘i’
and
4
premise prMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inMOYellowIndirectKick Robot.mtMoveIndirectKick()
9
end action
10
end fbeRule
Rule 47: C´odigo da Rule rlMOBluePenaltyBlue.
1
fbeRule rlMOBluePenaltyBlue
2
condition
3
premise prRefCmdPenaltyBlue Robot.atRefereeCmd == ‘P’ and
4
premise prMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inMOBluePenaltyBlue Robot.mtMovePenaltyKick()
9
end action
10
end fbeRule


199
Rule 48: C´odigo da Rule rlMOBluePenaltyYellow.
1
fbeRule rlMOBluePenaltyYellow
2
condition
3
premise prRefCmdPenaltyYellow Robot.atRefereeCmd == ‘p’ and
4
premise prMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inMOBluePenaltyYellow Robot.mtPenaltyDefCenter()
9
end action
10
end fbeRule
Rule 49: C´odigo da Rule rlMOYellowPenaltyYellow.
1
fbeRule rlMOYellowPenaltyYellow
2
condition
3
premise prRefCmdPenaltyYellow Robot.atRefereeCmd == ‘p’ and
4
premise prMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inMOYellowPenaltyYellow Robot.mtMovePenaltyKick()
9
end action
10
end fbeRule
Rule 50: C´odigo da Rule rlMOYellowPenaltyBlue.
1
fbeRule rlMOYellowPenaltyBlue
2
condition
3
premise prRefCmdPenaltyBlue Robot.atRefereeCmd == ‘P’ and
4
premise prMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inMOYellowPenaltyBlue Robot.mtPenaltyDefCenter()
9
end action
10
end fbeRule


200
Rule 51: C´odigo da Rule rlMOBlueReadyPenaltyBlue.
1
fbeRule rlMOBlueReadyPenaltyBlue
2
condition
3
premise prRefCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY” and
5
premise prLastRefCmdPenaltyBlue Robot.atLastRefCmd == ‘P’ and
6
premise prTeamBlue Robot.atTeamColor == “BLUE”
7
end condition
8
action
9
instigation inMOBlueReadyPenaltyBlue Robot.mtReadyPenalty()
10
end action
11
end fbeRule
Rule 52: C´odigo da Rule rlMOYellowReadyPenaltyYellow.
1
fbeRule rlMOYellowReadyPenaltyYellow
2
condition
3
premise prRefCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prMidﬁeldOnly Robot.atRole == “MIDFIELD ONLY” and
5
premise prLastRefCmdPenaltyYellow Robot.atLastRefCmd == ‘p’
and
6
premise prTeamYellow Robot.atTeamColor == “YELLOW”
7
end condition
8
action
9
instigation inMOYellowReadyPenaltyYellow Robot.mtReadyPenalty()
10
end action
11
end fbeRule


201
Rule 53: C´odigo da Rule rlSLStopTeamLeft.
1
fbeRule rlSLStopTeamLeft
2
condition
3
premise prRefCmdStop Robot.atRefereeCmd == ‘S’ and
4
premise prStrickerLeft Robot.atRole == “STRIKER LEFT” and
5
premise prTeamLeftSide Robot.atTeamSide == “LEFT”
6
end condition
7
action
8
instigation inSLStopTeamLeft Robot.mtMovePosAngleNeg()
9
end action
10
end fbeRule
Rule 54: C´odigo da Rule rlSLStopTeamRight.
1
fbeRule rlSLStopTeamRight
2
condition
3
premise prRefCmdStop Robot.atRefereeCmd == ‘S’ and
4
premise prStrickerLeft Robot.atRole == “STRIKER LEFT” and
5
premise prTeamRightSide Robot.atTeamSide == “RIGHT”
6
end condition
7
action
8
instigation inSLStopTeamRight Robot.mtMovePosAnglePos()
9
end action
10
end fbeRule
Rule 55: C´odigo da Rule rlSLBlueDirectKick.
1
fbeRule rlSLBlueDirectKick
2
condition
3
premise prRefCmdDirectKickBlue Robot.atRefereeCmd == ‘F’ and
4
premise prStrickerLeft Robot.atRole == “STRIKER LEFT” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inSLBlueDirectKick Robot.mtStrickerLeftDirect()
9
end action
10
end fbeRule


202
Rule 56: C´odigo da Rule rlSLYellowDirectKick.
1
fbeRule rlSLYellowDirectKick
2
condition
3
premise prRefCmdDirectKickYellow Robot.atRefereeCmd == ‘f’ and
4
premise prStrickerLeft Robot.atRole == “STRIKER LEFT” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inSLYellowDirectKick Robot.mtStrickerLeftDirect()
9
end action
10
end fbeRule
Rule 57: C´odigo da Rule rlSLBlueIndirectKick.
1
fbeRule rlSLBlueIndirectKick
2
condition
3
premise prRefCmdIndirectKickBlue Robot.atRefereeCmd == ‘I’ and
4
premise prStrickerLeft Robot.atRole == “STRIKER LEFT” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inSLBlueIndirectKick Robot.mtStrickerLeftDirect()
9
end action
10
end fbeRule


203
Rule 58: C´odigo da Rule rlSLYellowIndirectKick.
1
fbeRule rlSLYellowIndirectKick
2
condition
3
premise prRefCmdIndirectKickYellow Robot.atRefereeCmd == ‘i’
and
4
premise prStrickerLeft Robot.atRole == “STRIKER LEFT” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inSLYellowIndirectKick Robot.mtStrickerLeftDirect()
9
end action
10
end fbeRule
Rule 59: C´odigo da Rule rlSLBluePenaltyBlue.
1
fbeRule rlSLBluePenaltyBlue
2
condition
3
premise prRefCmdPenaltyBlue Robot.atRefereeCmd == ‘P’ and
4
premise prStrickerLeft Robot.atRole == “STRIKER LEFT” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inSLBluePenaltyBlue Robot.mtPenaltyAttackLeft()
9
end action
10
end fbeRule


204
Rule 60: C´odigo da Rule rlSLBluePenaltyYellow.
1
fbeRule rlSLBluePenaltyYellow
2
condition
3
premise prRefCmdPenaltyYellow Robot.atRefereeCmd == ‘p’ and
4
premise prStrickerLeft Robot.atRole == “STRIKER LEFT” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inSLBluePenaltyYellow Robot.mtStrickerLeftDirect()
9
end action
10
end fbeRule
Rule 61: C´odigo da Rule rlSLYellowPenaltyYellow.
1
fbeRule rlSLYellowPenaltyYellow
2
condition
3
premise prRefCmdPenaltyYellow Robot.atRefereeCmd == ‘p’ and
4
premise prStrickerLeft Robot.atRole == “STRIKER LEFT” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inSLYellowPenaltyYellow Robot.mtPenaltyAttackLeft()
9
end action
10
end fbeRule
Rule 62: C´odigo da Rule rlSLYellowPenaltyBlue.
1
fbeRule rlSLYellowPenaltyBlue
2
condition
3
premise prRefCmdPenaltyBlue Robot.atRefereeCmd == ‘P’ and
4
premise prStrickerLeft Robot.atRole == “STRIKER LEFT” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inSLYellowPenaltyBlue Robot.mtStrickerLeftDirect()
9
end action
10
end fbeRule


205
Rule 63: C´odigo da Rule rlSLStartBallNotClose.
1
fbeRule rlSLStartBallNotClose
2
condition
3
premise prRefCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prStrickerLeft Robot.atRole == “STRIKER LEFT” and
5
premise prNotClosestToBall Robot.atClosestToBall == false
6
end condition
7
action
8
instigation inSLStartBallNotClose Robot.mtStrickerLeftDirect()
9
end action
10
end fbeRule
Rule 64: C´odigo da Rule rlSRStopTeamLeft.
1
fbeRule rlSRStopTeamLeft
2
condition
3
premise prRefCmdStop Robot.atRefereeCmd == ‘S’ and
4
premise prStrikerRight Robot.atRole == “STRIKER RIGHT” and
5
premise prTeamLeftSide Robot.atTeamSide == “LEFT”
6
end condition
7
action
8
instigation inSRStopTeamLeft Robot.mtMovePosAnglePos()
9
end action
10
end fbeRule
Rule 65: C´odigo da Rule rlSRStopTeamRight.
1
fbeRule rlSRStopTeamRight
2
condition
3
premise prRefCmdStop Robot.atRefereeCmd == ‘S’ and
4
premise prStrikerRight Robot.atRole == “STRIKER RIGHT” and
5
premise prTeamRightSide Robot.atTeamSide == “RIGHT”
6
end condition
7
action
8
instigation inSRStopTeamRight Robot.mtMovePosAngleNeg()
9
end action
10
end fbeRule


206
Rule 66: C´odigo da Rule rlSRBlueDirectKick.
1
fbeRule rlSRBlueDirectKick
2
condition
3
premise prRefCmdDirectKickBlue Robot.atRefereeCmd == ‘F’ and
4
premise prStrikerRight Robot.atRole == “STRIKER RIGHT” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inSRBlueDirectKick Robot.mtStrickerRightDirect()
9
end action
10
end fbeRule
Rule 67: C´odigo da Rule rlSRYellowDirectKick.
1
fbeRule rlSRYellowDirectKick
2
condition
3
premise prRefCmdDirectKickYellow Robot.atRefereeCmd == ‘f’ and
4
premise prStrikerRight Robot.atRole == “STRIKER RIGHT” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inSRYellowDirectKick Robot.mtStrickerRightDirect()
9
end action
10
end fbeRule
Rule 68: C´odigo da Rule rlSRBlueIndirectKick.
1
fbeRule rlSRBlueIndirectKick
2
condition
3
premise prRefCmdIndirectKickBlue Robot.atRefereeCmd == ‘I’ and
4
premise prStrikerRight Robot.atRole == “STRIKER RIGHT” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inSRBlueIndirectKick Robot.mtStrickerRightDirect()
9
end action
10
end fbeRule


207
Rule 69: C´odigo da Rule rlSRYellowIndirectKick.
1
fbeRule rlSRYellowIndirectKick
2
condition
3
premise prRefCmdIndirectKickYellow Robot.atRefereeCmd == ‘i’
and
4
premise prStrikerRight Robot.atRole == “STRIKER RIGHT” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inSRYellowIndirectKick Robot.mtStrickerRightDirect()
9
end action
10
end fbeRule
Rule 70: C´odigo da Rule rlSRBluePenaltyBlue.
1
fbeRule rlSRBluePenaltyBlue
2
condition
3
premise prRefCmdPenaltyBlue Robot.atRefereeCmd == ‘P’ and
4
premise prStrikerRight Robot.atRole == “STRIKER RIGHT” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inSRBluePenaltyBlue Robot.mtPenaltyAttackRight()
9
end action
10
end fbeRule


208
Rule 71: C´odigo da Rule rlSRBluePenaltyYellow.
1
fbeRule rlSRBluePenaltyYellow
2
condition
3
premise prRefCmdPenaltyYellow Robot.atRefereeCmd == ‘p’ and
4
premise prStrikerRight Robot.atRole == “STRIKER RIGHT” and
5
premise prTeamBlue Robot.atTeamColor == “BLUE”
6
end condition
7
action
8
instigation inSRBluePenaltyYellow Robot.mtStrickerRightDirect()
9
end action
10
end fbeRule
Rule 72: C´odigo da Rule rlSRYellowsPenaltyYellow.
1
fbeRule rlSRYellowsPenaltyYellow
2
condition
3
premise prRefCmdPenaltyYellow Robot.atRefereeCmd == ‘p’ and
4
premise prStrikerRight Robot.atRole == “STRIKER RIGHT” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inSRYellowsPenaltyYellow Robot.mtPenaltyAttackRight()
9
end action
10
end fbeRule
Rule 73: C´odigo da Rule rlSRYellowsPenaltyBlue.
1
fbeRule rlSRYellowsPenaltyBlue
2
condition
3
premise prRefCmdPenaltyBlue Robot.atRefereeCmd == ‘P’ and
4
premise prStrikerRight Robot.atRole == “STRIKER RIGHT” and
5
premise prTeamYellow Robot.atTeamColor == “YELLOW”
6
end condition
7
action
8
instigation inSRYellowsPenaltyBlue Robot.mtStrickerRightDirect()
9
end action
10
end fbeRule


209
Rule 74: C´odigo da Rule rlSRStartBallNotClose.
1
fbeRule rlSRStartBallNotClose
2
condition
3
premise prRefCmdStartGame Robot.atRefereeCmd == ‘ ’ and
4
premise prStrikerRight Robot.atRole == “STRIKER RIGHT” and
5
premise prNotClosestToBall Robot.atClosestToBall == false
6
end condition
7
action
8
instigation inSRStartBallNotClose Robot.mtStrickerRightDirect()
9
end action
10
end fbeRule


210
APˆENDICE D -- ANALISADOR L´EXICO DESENVOLVIDO PARA A
CONTAGEM DO N ´UMERO DE TOKENS
Para auxiliar a contagem de tokens presente em cada um dos c´odigos-fonte
apresentados neste trabalho, foi desenvolvido um analisador l´exico a partir da ferramenta
Flex/Lex, a qual permite criar analisadores l´exicos de maneira f´acil e r´apida. Este analisador
l´exico foi desenvolvido com aux´ılio do prof. Fabro, o qual vislumbrou a possibilidade de
utilizar a ferramenta Flex/Lex para a contagem de tokens.
O c´odigo-fonte do analisador l´exico desenvolvido ´e apresentado no C´odigo 38.


211
C´odigo 38: C´odigo-fonte do analisador l´exico desenvolvido para efetuar a
contagem de Tokens das aplica¸c˜oes apresentadas.
1 % {
2
#include < stdio.h >
3
int tokens = 0;
4 % }
5
6 %%
7 [a-zA-Z0-9 ]+
{ tokens++; }
8 \“
{ tokens++; }
9 \{
{ tokens++; }
10 \}
{ tokens++; }
11 \(
{ tokens++; }
12 \)
{ tokens++; }
13 \[
{ tokens++; }
14 \]
{ tokens++; }
15 ;
{ tokens++; }
16 =
{ tokens++; }
17 “==”
{ tokens++; }
18 “!=”
{ tokens++; }
19 “>”
{ tokens++; }
20 “>=”
{ tokens++; }
21 “<”
{ tokens++; }
22 “<=”
{ tokens++; }
23 “->”
{ tokens++; }
24 “*”
{ tokens++; }
25 \n
{ }
26 “\\”([a-z]|[0-9]|[A-Z]|“ ”)*
{ }
27
28 int main (int argc, char **argv)
29 {
30
yyin = fopen( argv[1], “r”);
31
yylex();
32
printf(“Quantidade de Tokens: %8d”, tokens);
33
return tokens;
34 }


212
APˆENDICE E -- CENSO DAS APLICAC¸ ˜OES PON
Este Apˆendice apresenta um levantamento das aplica¸c˜oes PON desenvolvidas at´e
o presente momento, incluindo detalhes tais como materializa¸c˜ao PON utilizada para o
desenvolvimento, n´umero de Rules, quantidade de instˆancias de FBEs e resultados obtidos
com cada aplica¸c˜ao.
Os dados para cada uma das aplica¸c˜oes foram obtidos atrav´es de pesquisa realizada
com pessoas que trabalham ou j´a trabalharam com o PON. Cada pessoa enviou informa¸c˜oes
sobre as aplica¸c˜oes por elas desenvolvidas e todas as informa¸c˜oes recebidas foram agrupadas
em forma de uma ´unica tabela. Nesta tabela, as aplica¸c˜oes s˜ao apresentadas em ordem
cronol´ogica.
Esta tabela ´e de grande valor para pesquisadores que trabalham na linha de
pesquisa do PON. Isto porque, at´e o presente momento n˜ao se tinha contabilizado a
quantidade de aplica¸c˜oes que haviam sido desenvolvidas sob o vi´es do PON e t˜ao pouco a
complexidade, em termos de entidades PON, de cada uma dessas aplica¸c˜oes.
Posteriormente, algumas das aplica¸c˜oes PON desenvolvidas em softwares s˜ao
brevemente descritas, destacando a quantidade de entidades FBEs e Rules presente na
aplica¸c˜ao bem como resultados obtidos a partir de cada aplica¸c˜ao.


Autor(es)
Ano
Nome da Aplicação
Materialização
Contexto
Rules
Sub 
Conditions
Premises
Instigations
FBE 
Classes
Attributes
Methods
Instâncias 
de FBE
Comparado com 
o que?
Resumo Resultado
Jean Simão
2000
Construção do 
Framework CON acoplado 
ao Analytice II
-
Dissertação de 
Mestrado
1
1
1
1
1
1
1
1
N/A
Demonstrou viabilidade com um pequeno exemplo
Jean Simão
2000
CON Célula - Célula 
Robotizada - Analytice II
Framework CON 1.0 Dissertação de 
Mestrado
25
0
43
88
8
1
1
10
N/A
Permitiu demonstrar o conceito de Controle Orientado a 
Notificações em ANALYTICE II. Permitiu uma simulação em 
Analytice II.
Jardel Lucca
2008
Wizard para criação de 
controles de célula de 
manufatura sobre 
Analytice II
Framework CON 2.0 Iniciação Científica
8
-
15
15
-
14
15
3
N/A
Primeiras implementações de controles CON via aplicação em alto 
nível com interface gráfica amigável.
Roni 
Banaszewski
2009
Mira ao Alvo - Segundo 
Cenário
Framework C++ 1.0
Dissertação de 
Mestrado
5
0
17
6
4
6
202
PD
-
Roni 
Banaszewski
2009
Sistema de 
Condicionamento de Ar
Framework C++ 1.0
Dissertação de 
Mestrado
16
0
42
18
3
3
48
N/A
-
Adriano 
Ronszcka
2010
Pacman
Framework C++ 
1.0/2.0
Disciplina 
Programação 
Avançada
99
0
32
98
11
15
5
330
FW PON 1.0/2.0 
e PI/POO
O FW 2.0 apresentou desempenho 3x melhor em relação ao 1.0. 
Entretanto a versão em POO C++ ficou mais rápida que ambos (5x 
mais que o 2.0).
Luciana 
Wiecheteck
2011
Portão Eletrônico
Framework PON 1.0 Dissertação
8
4
8
8
3
3
1
1
N/A
Caso de estudo utilizado para validar o método DON proposto.         
Robson 
Linhares
2011
Central telefônica PON
Framework C++ 1.0
Tese de Doutorado
21
0
18
18
1
2
9
2
POO
A versão utilizando POO convencional apresenta resultados de 
desempenho significativamente melhores do que os da versão 
utilizando PON.
Luciana 
Wiecheteck
2011
 Simulador de Portão 
Eletrônico (SPE)
Não me recordo
Dissertação
8
4
8
8
3
-
-
-
N/A
Caso de estudo utilizado para validar o método DON
proposto.
Glauber 
Valença
2011
Sistema de controle de 
vendas
Framework 2.0
Dissertação
20
-
-
10
8
20
10
50
Framework C++ 
1.0 e PI/POO
Até 10x melhor em relacao ao Framework 1.0 e ganhos da OO 
utilizando cenários com a estrutura PONHASH.
Luciana 
Wiecheteck
2011
 Simulador de Portão 
Eletrônico (SPE)
Não me recordo
Dissertação
8
4
8
8
3
-
-
-
N/A
Caso de estudo utilizado para validar o método DON
proposto.
Glauber 
Valença
2011
Sistema de controle de 
vendas
Framework 2.0
Dissertação
20
-
-
10
8
20
10
50
Framework C++ 
1.0 e PI/POO
Até 10x melhor em relacao ao Framework 1.0 e ganhos da OO 
utilizando cenários com a estrutura PONHASH.
Rodrigo Gregori
2012
Meshslicing
Framework C++ 2.0
Disciplina PON
1
1
3
1
3
4
2
1
PI - Linguagem C A implementação de NOP é de fato menos performativa do que a 
implementação de IP.
Fernando 
Muchalski
2012
Cálculo de Produtividade
Framework C++ 2.0
Disciplina PON
1 a 4
1 a 4 
1 + (4 * N)
1
1
4
1
1
PI/POO
PON se mostrou menos eficiente que o POO. Porém, a diferença 
de desempenho apresentou uma tendência de queda a medida 
que o conjunto de dados processados aumentava.
Danilo 
Belmonte
2012
Airplane Flight Simulator
Framework C++ 
2.0+Threads
Qualificação de 
Doutorado
5
0
6
4
16
58
70
8
N/A
-
Eduardo Peters
2012
Mira ao Alvo
CoPON
Dissertação
100
100
300
200
3
12
17
3
Framework C++ 
2.0
Em média, o coprocessador PON (CoPON), apresentou ganho 
médio de 45x se considerarmos toda a aplicação PON.
Eduardo Peters
2012
 Simulador de Portão 
Eletrônico (SPE)
CoPON
Dissertação
8
4
8
8
3
-
-
-
Framework C++ 
2.0
Framework C++ 2.0
Luiz Viana Melo
2013
Sistema da máquina de 
lavar
Framework 2.0
Disciplina PON
9
0
6
18
1
2
2
1
Framework 
Fuzzy (Fabro)
A versão em PON teve desempenho inferior em relação ao sistema 
convencional.
Clayton 
Kossoski
2013
Simple Flight Combat PON Framework 
Otimizado
Disciplina PON
26
26
27
26
4
22
20
4
N/A
Foi possível fazer funcionar um jogo usando biblioteca Allegro e o 
framework PON otimizado. 
Danilo 
Belmonte
2013
Semaphore
Framework C++ 
2.0+Threads
Experimento para 
Tese de Doutorado
4
0
5
0
2
6
5
71
Framework C++ 
2.0
Framework C++ 2.0+Threads em Servidor com quantidades 
diferentes de core (núcleos) de processamento apresentou 
balanceamento de carga entre os diferentes processadores.
Priscila Moraes 
e Adriano 
Ronszcka
2013
Mira ao alvo
Compilador PON – 
Geração de código 
em C
Disciplina PON / 
Compiladores
100
100
300
200
3
12
17
3
N/A
Criação do primeiro compilador PON, o qual recebe como entrada 
um programa em PON e gera um programa em C correspondente.
Adriano Ronska 
e Cleverson 
Ferreira
2013
Mira ao alvo
Compilador PON – 
Geração de código 
em C++
Disciplina PON / 
Compiladores
100
100
300
200
3
7
9
3
N/A
Criação do primeiro compilador PON, o qual recebe como entrada 
um programa em PON e gera um programa em C correspondente.
Rodrigo Gregori
2013
TriMeshSlicing
Framework C++ 2.0
Geometria 
Computacional
1
3
1
2
4
2
12 a 2016
PI/POO
Tempo de execução médio 450% maior. Melhora da performance, 
se utilizado o Scheduler KEEPER


Autor(es)
Ano
Nome da Aplicação
Materialização
Contexto
Rules
Sub 
Conditions
Premises
Instigations
FBE 
Classes
Attributes
Methods
Instâncias 
de FBE
Comparado com 
o que?
Resumo Resultado
Robson 
Linhares
2013
Semáforos NOCA
NOCA 1.0 em FPGA
Tese de Doutorado
224
96
224
0
-
-
-
-
PI - Linguagem C O desempenho da versão PI executando em NiOS otimizado é 
amplamente superior ao apresentado pela aplicação PON.
Robson 
Linhares
2013
Mira alvo NOCA
NOCA 1.0 em FPGA
Tese de Doutorado
101
100
301
0
-
-
-
-
PI procedimental NOCA apresenta desempenho melhor que as outras plataformas 
para um número reduzido de regras ativadas.
Robson 
Linhares
2013
Sort NOCA
NOCA 1.0 em FPGA
Tese de Doutorado
45
41
62
0
-
-
-
-
PON HD
Algoritmo de ordenação implementado no NOCA apresentou 
complexidade algorítmica maior do que o esperado pela teoria do 
PON.
Robson 
Linhares
2013
Semáforos NOCA
NOCA 1.0 em FPGA
Tese de Doutorado
224
96
224
0
-
-
-
-
PI - Linguagem C O desempenho da versão PI executando em NiOS otimizado é 
amplamente superior ao apresentado pela aplicação PON.
Robson 
Linhares
2013
Mira alvo NOCA
NOCA 1.0 em FPGA
Tese de Doutorado
101
100
301
0
-
-
-
-
PI procedimental NOCA apresenta desempenho melhor que as outras plataformas 
para um número reduzido de regras ativadas.
Robson 
Linhares
2013
Sort NOCA
NOCA 1.0 em FPGA
Tese de Doutorado
45
41
62
0
-
-
-
-
PON HD
Algoritmo de ordenação implementado no NOCA apresentou 
complexidade algorítmica maior do que o esperado pela teoria do 
PON
Robson Xavier
2014
Simulador de Transporte 
Individual I
Framework 
Otimizado/LingPON 
1.0
Dissertação de 
Mestrado
6
0
8
6
3
3
6
3
POE (Dispatcher) PON é diferente de POE. Dispatcher mais rápido que PON. PON 
menos verboso que POE.
Robson Xavier
2014
Simulador de Transporte 
Individual II
Framework 
Otimizado
Dissertação de 
Mestrado
14
0
14
15
4
7
14
4
POE ( State)
PON é diferente de POE. Tempo de execução comparável entre 
implementações de acordo com o número de eventos. PON é 
menos verboso que POE.
Robson Xavier
2014
Simulador de Transporte 
Individual III
Framework 
Otimizado
Dissertação de 
Mestrado
22
0
18
24
4
7
14
5
POE (Observer)
PON é diferente de POE. Tempo de execução comparável entre 
implementações de acordo com o número de eventos. 
Desempenho que se adapta em PON. PON é menos verboso que 
POE.
Leonardo 
Pordeus
2015
CTA
LingPON 1.0
Disciplina PON
6
0
12
7
1
2
7
200
PI/POO
Apresentou resultados muito próximos ao da implementação em 
PI/POO (C++).
Leonardo 
Pordeus
2015
CTA (Intensidade de 
Tráfego)
LingPON 1.0
Disciplina PON
18
0
48
32
1
4
11
200
PI/POO
Apresentou resultados muito próximos ao da implementação em 
PI/POO (C++).
Helio Monte-
Alto
2015
Pac-Man
LingPON 1.0
Disciplina PON
385
385
1462
494
7
80
116
30
N/A
A aplicação implementada em LingPON permitiu identificar alguns 
pontos de melhoria em seu compilador.
Cleverson 
Ferreira
2015
Mira ao Alvo
LingPON 1.0
Dissertação de 
Mestrado
1
2
4
1
3
4
4
3
PI/POO
Código LingPON compilado para C e C++ apresentaram melhor 
desemepnho quando comparado ao PI/POO.
Cleverson 
Ferreira
2015
SalesOrder - LingPON
LingPON 1.0
Dissertação de 
Mestrado
25
25
27
27
4
19
28
4
PI/POO
Código LingPON compilado para C e C++ apresentaram melhor 
desemepnho quando comparado ao PI/POO.
Fernando 
Schutz
2015
RNAMLP para XOR
Framework C++ 2.0
Disciplina PON
4
-
9
2
20
4
5
PI - Linguagem C Tempo de execução muito mais longo na aplicação PON.
Luiz Viana Melo
2015
Sistema da máquina de 
lavar
LingPON Fuzzy
Dissertação de 
Mestrado
9
0
6
18
1
2
2
1
Framework 
Fuzzy (Fabro)
A versão em PON teve desempenho inferior em relação ao sistema 
convencional. Porém, o desenvolvimento foi mais fácil.
Vladimir 
Krachinski
2015
Meshslicing
LingPON 1.0
Disciplina PON
1
1
3
1
2
4
2
1
Framework C++ 
2.0
O desempenho do LingPON foi muito melhor do que o Framework 
2.0, e também mais simples de implementar, mas menos 
performática do que o IP.
Hinsching e 
Robson 
Linhares
2015
Busca Sequencial
LingPON 1.0
Iniciação Científica
150
150
400
6
3
4
5
52
PI - Linguagem C Verificou-se que o desempenho da aplicação desenvolvida em 
Linguagem C é melhor do que a aplicação LingPO N.
Igor Mendonça
2015
WarshipAttackGame
Framework Java
Estudos do PON
13
1
32
22
5
22
19
6
N/A
Elaboração de artigos CBIC e artigo completo submetido à IEEE-LA
Igor Mendonça
2015
EletronicGate
Framework Java
Estudos do PON
6
2
16
7
2
3
8
2
N/A
Exemplo de como usar interface swing com PON
Márcio Batista
2015
SalesOrder
Framework C++ 
1.0/2.0
Disciplina 
Programação 
Avançada
16
-
16
28
1
18
28
1
FW PON 1.0/2.0 
e PI/POO
Apesar do Framework 2.0 apresentar desempenho melhor quando 
comparado ao Framework 1.0, a aplicação concebida em POO 
apresentou melhores resultados comparado ao PON de maneira 
geral.
Leonardo 
Pordeus
2015
Sort
PON HD
Disciplina Lógica 
Reconfigurável
N-1
2*(N-1)
N-1
N
-
-
-
N
N/A
Apresetou resultado O(n). O número de ciclos de clock para 
ordenação no pior caso, era igual ao número de elementos.
Leonardo 
Pordeus
2015
PWM
PON HD
Disciplina Lógica 
Reconfigurável 
2
0
2
3
-
-
-
-
VHDL
A implementação em PON HD fez uso da mesma quantidade de 
unidades lógicas do que a implementação puramento em VHDL.
Ricardo 
Kerschbaumer
2015
Contador Digital
PON-HD + 
LingPONHD
Disciplina 
Compiladores
1
-
2
-
-
-
1
-
VHDL Manual
Performance e tamanho do circuito equivalentes
Robson 
Linhares
2015
Sort PON HD 
PON HD Prototipal
Tese de Doutorado
45
41
62
0
-
-
-
-
VHDL e NOCA 
FPGA
-


Autor(es)
Ano
Nome da Aplicação
Materialização
Contexto
Rules
Sub 
Conditions
Premises
Instigations
FBE 
Classes
Attributes
Methods
Instâncias 
de FBE
Comparado com 
o que?
Resumo Resultado
Leonardo 
Pordeus
2015
Sort
PON HD
Disciplina Lógica 
Reconfigurável
N-1
2*(N-1)
N-1
N
-
-
-
-
N/A
Apresetou resultado O(n). O número de ciclos de clock para 
ordenação no pior caso, era igual ao número de elementos.
Leonardo 
Pordeus
2015
PWM
PON HD
Disciplina Lógica 
Reconfigurável 
2
0
2
3
-
-
-
-
VHDL
A implementação em PON HD fez uso da mesma quantidade de 
unidades lógicas do que a implementação puramento em VHDL.
Ricardo 
Kerschbaumer
2015
Controlador Robô 
hexápode
PON-HD + 
LingPONHD
Disciplina 
Compiladores
127
-
50
-
-
-
103
-
N/A
Controlou o robô sem problemas
Ricardo 
Kerschbaumer
2015
Controlador Robô 
hexápode
PON-HD + LingPON
Disciplina 
Compiladores
127
-
50
-
-
-
103
-
N/A
Controlou o robô sem problemas
Ricardo 
Kerschbaumer
2015
Controlador simples de 
temperatura
PON-HD + LingPON
Disciplina 
Compiladores
3
-
4
-
-
-
2
-
N/A
Funcionou corretamente
Robson 
Linhares
2015
Sort PON HD 
PON HD Prototipal
Tese de Doutorado
45
41
62
0
-
-
-
-
VHDL e NOCA 
FPGA
-
Ricardo 
Kerschbaumer
2015
Ordenador paralelo de 
dados (odd even sort)
PON-HD
Disciplina PON
1 à 2999
-
de 2 à 5998
-
-
-
-
VHDL Manual
Performance e tamanho do circuito equivalentes
Ricardo 
Kerschbaumer
2015
Ordenador paralelo de 
dados
PON-HD
Disciplina PON
1 à 2999
-
de 2 à 5998
-
-
-
2 à 5999
-
VHDL Manual
Performance e tamanho do circuito equivalentes
Ricardo 
Kerschbaumer
2016
Contador + Driver p/ 3 
Displays de 7 segmentos
PON-HD + 
LingPONHD
Disciplina Lógica 
Reconfigurável
38
-
35
-
-
-
38
-
N/A
Funcionou corretamente
Marcos Talau
2016
DistributedFire Net Attr
NOP C++ 2.0-
PONNetwork
Disciplina PON 
2
6
2
6
3
2
6
N/A
A aplicação demonstrou que o PON é naturalmente distribuído.
Marcos Talau
2016
DistributedFire Net Prem
NOP C++ 2.0-
PONNetwork
Disciplina PON 
2
12
2
6
0
2
6
N/A
A aplicação demonstrou que o PON é naturalmente distribuído.
Marcos Talau
2016
SummerAirCond
NOP C++ 2.0-
PONNetwork
Disciplina PON
7
12
7
9
6
4
9
N/A
A aplicação demonstrou que o PON é naturalmente distribuído.
Marcos Talau
2016
StressTest Net
NOP C++ 2.0-
PONNetwork
Disciplina PON
n
n
4
n
8
4
N/A
Foi verificado que o uso de atributos via rede é mais eficiente que
o uso de premisas via rede.
Fabio Negrini e 
Leonardo 
Pordeus
2016
CTA
LingPON 1.0
Disciplina PON
46
46
126
89
3
12
34
100
PI/POO (C++)
A aplicação PON se apresentou mais lenta que versão 
desenvolvida sob o PI/POO.
Fernando 
Suyama
2016
RNA_FMS (p/ a  base de 
flores)
Framework C++ 2.0
Disciplina PON
17
0
10
45
3
39
5
9
PI - Linguagem C PI obteve os menores tempos de execução.
Fernando 
Suyama
2016
RNA_FMS (p/ a base de 
câncer de mama)
Framework C++ 2.0
Disciplina PON
23
0
10
58
3
45
5
12
PI - Linguagem C PI obteve os menores tempos de execução.
Tiago Martins
2016
Simulação de um veículo 
seguidor de linha 
utilizando V-REP e 
LingPon Embarcado
LingPon 1.0
Disciplina PON
10
13
39
10
1
20
10
1
PI - Linguagem C A aplicação PI apresentou resultados superiores a LingPON.
Eduardo Bilk
2016
BoxePON
LingPON StaticCPP
Disciplina PON
14
14
64
93
-
6
17
3
PI/POO
A aplicação PON não apresentou ganho aparente em termos de 
consumo energético em placa embarcada.
Fernando 
Schutz
2016
RNAMLP para IRIS
Framework C++ 2.0
Tese de Doutorado
10
-
19
3
65
10
9
PI - Linguagem C Tempo de execução muito mais longo na aplicação PON.
Fernando 
Schutz
2016
RNAMLP para IRIS
LingPON StaticCPP
Tese de Doutorado
9
9
18
9
3
37
9
9
PI - Linguagem C Tempo de execução da aplicação PON semelhante à aplicação PI.
Luiz Viana Melo
2016
Controlador de rotação no 
eixo X de Hexacóptero
LingPON Fuzzy
Dissertação de 
Mestrado
35
0
12
35
1
1
1
1
Framework 
Fuzzy (Emanoel 
Koslosky)
A versão em PON teve desempenho inferior em relação ao sistema 
convencional. Porém, o desenvolvimento foi mais fácil.
Frederico 
Miranda
2016
C#Pon1.1Hash
Framework C# 1.0
Disciplina PON
4224
0
51
4224
1
4
1
1
PI/POO
Tempo de execução da aplicação PON próximo ao da aplicação 
PI/POO.
Wagner 
Barreto
2016
Portão Eletrônico 
Distribuído
Framework Java
Disciplina PON
6
0
7
4
1
2
3
1
RPC
Para N apertos de botão implementação RPC troca N mensagens, 
implementação PON troca 2N mensagens.
Wagner 
Barreto
2016
2 Phase Commit
Framework Java
Disciplina PON
4
2
19
7
2
12
7
2
RPC
Convencional 3N mensagens. PON N+3 mensagens.
Douglas Krug
2016
Torre de Hanói
LingPON 1.0
Disciplina PON
8
16
41
53
3
11
50
7
PI - Linguagem C Aplicação LingPON se mostrou mais legível e com melhor 
desempenho quando comparada à solução PI.
Leonardo 
Santos
2016
Robocup - Framework C++ 
2.0
Framework C++ 2.0
Dissertação de 
Mestrado
74
74
53
30
1
20
30
6
PI/POO
A aplicação apresentou melhores métricas de complexidade de 
código (linhas e tokens) e melhor nível de manutenibilidade.
Leonardo 
Santos
2016
Robocup - LingPON 1.0
LingPON 1.0
Dissertação de 
Mestrado
444
444
318
180
6
120
180
6
PI/POO e 
Framework C++ 
2.0
Aplicação apresentou piores métricas de complexidade de código 
(linhas e tokens), devido principalmente à redundância de código 
da linguagem.


Autor(es)
Ano
Nome da Aplicação
Materialização
Contexto
Rules
Sub 
Conditions
Premises
Instigations
FBE 
Classes
Attributes
Methods
Instâncias 
de FBE
Comparado com 
o que?
Resumo Resultado
Leonardo 
Santos
2016
Robocup - LingPON 1.2
LingPON 1.2
Dissertação de 
Mestrado
74
74
53
30
1
20
30
6
PI/POO, 
Framework C++ 
2.0 e LingPON 
1.0
A aplicação apresentou métricas de complexidade de código 
similares ao código desenvolvido em Framework C++ 2.0 e 
melhores que o LingPON 1.0 e PI/POO.
Rodrigo 
Oliveira
2016
PON.IoT
Framework PON.IoT Dissertação de 
Mestrado
14
59
600
7
11
11
17
11
N/A
Verificou-se a utilização do PON em sistemas sencientes IoT com 
Raspberry Pi
Leonardo 
Pordeus
2016
Mira Alvo
Ling PON (2.0) para 
NOCA
Dissertação de 
Mestrado
101
0
201
301
101
201
301
100
NOCASim
Análise em desenvolvimento.
Leonardo 
Pordeus
2016
Mira Alvo
Ling PON (2.0) para 
NOCA
Dissertação
101
0
201
301
-
-
-
-
NOCASim
Análise em desenvolvimento.
Leonardo 
Pordeus
2017
Semáfaros
Ling PON (2.0) para 
NOCA
Dissertação de 
Mestrado
-
-
-
-
-
-
-
-
NOCASim
Aplicação em desenvolvimento.
Leonardo 
Pordeus
2017
Sort
Ling PON (2.0) para 
NOCA
Dissertação de 
Mestrado
-
-
-
-
-
-
-
-
NOCASim
Aplicação em desenvolvimento.
Leonardo 
Pordeus
2017
Semáfaros
Ling PON (2.0) para 
NOCA
Dissertação
-
-
-
-
-
-
-
-
NOCASim
Aplicação em desenvolvimento.
Leonardo 
Pordeus
2017
Sort
Ling PON (2.0) para 
NOCA
Dissertação
-
-
-
-
-
-
-
-
NOCASim
Aplicação em desenvolvimento.


217
E.1
MIRA AO ALVO
A aplica¸c˜ao Mira Ao Alvo foi desenvolvida por Banaszewski [Banaszewski 2009] sob
o Framework PON 1.0 sendo comparada com PI onde em suma os resultados de desempenho
foram favor´aveis ao Framework PON 1.0 dado inclusive a natureza da aplica¸c˜ao. Depois
esta aplica¸c˜ao foi redesenvolvida no ˆambito do trabalho de [Valen¸ca 2013] em Framework
PON 2.0 e comparadas com Framework 1.0, sendo os resultados favor´aveis ao Framework
PON 2.0. Posteriormente, a mesma aplica¸c˜ao foi desenvolvida por Ferreira [Ferreira 2016]
utilizando a LingPON 1.0, sendo comparada com Framework PON 2.0 obtendo resultados
de desempenho melhores que este.
A aplica¸c˜ao intitulada Mira ao Alvo consiste em um ambiente onde as entidades
do tipo mira interagem ativamente com as entidades do tipo alvo, conforme apresentado
na Figura 78. Neste ambiente, ambas as entidades s˜ao posicionadas a uma dada distˆancia,
sendo que a mira tenta atingir o alvo com o arremesso de um proj´etil.
Figura 78: Representa¸c˜ao da aplica¸c˜ao Mira ao Alvo [Banaszewski 2009]
.
Para ﬁns de compara¸c˜ao, a presente aplica¸c˜ao foi desenvolvidas com algumas
pequenas varia¸c˜oes, aﬁm de tornar a intera¸c˜ao entre miras e alvos mais complexa do que no
ambiente tradicional. Estas varia¸c˜oes s˜ao relativas `a quantidade de entidades mira e alvo, a
deﬁni¸c˜ao de novos estados para estas entidades e a inser¸c˜ao de novas entidades ao ambiente.
Isto fez-se necess´ario para permitir melhor compara¸c˜ao, em termos de desempenho, entre
diferentes paradigmas de programa¸c˜ao, incluindo o PON e PI.
De um modo geral, as entidades miras e as entidades alvos s˜ao representadas,


218
respectivamente, por arqueiros e ma¸c˜as. Cada arqueiro e cada ma¸ca ´e identiﬁcado por um
n´umero, sendo que o arqueiro somente pode ﬂechar uma ma¸ca que apresente o identiﬁcador
num´erico correspondente ao seu. Al´em desse atributo, cada ma¸c˜a possui um atributo que
representa seu estado atual, outro que expl´ıcita se a mesma j´a foi perfurada por uma ﬂecha
e, por ﬁm, um atributo que se refere a sua colora¸c˜ao.
Neste contexto, cada arqueiro somente pode interagir com a respectiva ma¸c˜a ap´os
a constata¸c˜ao de trˆes condicionantes: (a) se a cor da ma¸c˜a que est´a posicionada diretamente
`a sua frente ´e vermelho, (b) se a ma¸c˜a que est´a posicionada diretamente `a sua frente est´a
pronta para ser atingida, (c) se ela ´e identiﬁcada pelo seu n´umero correspondente (d) e
se o in´ıcio for autorizado (representado pelo tiro de uma arma) . Apenas se estas trˆes
condi¸c˜oes forem satisfeitas, o arqueiro est´a liberado para atingir a respectiva ma¸c˜a com a
proje¸c˜ao de sua ﬂecha, conforme apresentado na Figura 79.
Figura 79: Exemplo de uma Rule presente na aplica¸c˜ao Mira ao Alvo
.
Isto dito, a aplica¸c˜ao foi desenvolvida primeiramente pela deﬁni¸c˜ao de FBEAcher
e FBEApple com Attributes e Methods pertinentes. Ainda, um terceiro FBE nomeado
Controller foi criado a ﬁm de representar a arma que deﬁne o in´ıcio da intera¸c˜ao entre
arqueiros e ma¸cas. Neste contexto, diferentes vers˜oes desta aplica¸c˜ao, com diferentes
quantidades de FBEs e Rules, foram desenvolvidas com o objetivo de testar a performance
das materializa¸c˜oes PON. Em alguns casos, foram criadas at´e 100 Rules, sendo que cada
Rule foi associada a uma das 100 instˆancias criadas do FBEArcher e 100 instˆancias do
FBEApple. Entretanto, a cria¸c˜ao destas Rules foi feita atrav´es de la¸cos de repeti¸c˜ao, fato
este que n˜ao agrega complexidade real ao desenvolvimento da aplica¸c˜ao, pois trata-se
apenas de repeti¸c˜ao de Rules.
Atrav´es de compara¸c˜oes em termos de desempenho com uma solu¸c˜ao funcional-
mente equivalente desenvolvida no PI, foi poss´ıvel demonstrar que em cen´arios em que os
estados de atributos variam com baixa ou mediana frequˆencia, a reatividade e pontualidade
das notiﬁca¸c˜oes faz o PON prevalecer sobre o PI [Banaszewski 2009].


219
E.2
SISTEMA DE CONDICIONAMENTO DE AR
A aplica¸c˜ao de Sistemas de Condicionamento de Ar foi desenvolvida por Banas-
zewski [Banaszewski 2009], utilizando o Framework PON 1.0. Ainda que n˜ao tenha sido
redesenvolvida ainda em Framework PON 2.0 ou LingPON 1.0, ela apresenta complexidade
suﬁciente para merecer relato.
Isto dito, o Sistema de Condicionamento de Ar ´e hipoteticamente integrado a um
edif´ıcio de 16 andares. Cada andar possui uma bomba de calor, uma entrada ajust´avel de
ar e um sensor de temperatura (i.e termˆometro), os quais tem os seus estados controlados
por um componente centralizado nomeado Aplica¸c˜ao de Controle, conforme representado
pela Figura 80.
Figura 80: Representa¸c˜ao do Sistema de Condicionamento de Ar [Banaszewski 2009].
Neste ambiente, uma bomba de ar tem a fun¸c˜ao de aquecer ou resfriar o ar em um
determinado andar do edif´ıcio. Assim, em um determinado momento uma bomba de calor
pode se encontrar no estado de HEATING (aquecendo), COOLING (resfriando) ou OFF
(desligada). O ar enviado por uma bomba de ar entra no respectivo andar pela entrada de
ar ajust´avel, a qual pode assumir o estado OPENED (aberta) ou CLOSED (fechada).
Por sua vez, um sensor de temperatura pode apresentar os seguintes estados, os
quais representam a temperatura de um andar do edif´ıcio:
•TARGET: temperatura ideal pr´e-conﬁgurada.
•UPPER e LOWER GUARD: correspondem `as temperaturas na faixa aceit´avel
com varia¸c˜ao de 2◦C para mais ou para menos da temperatura ideal.


220
•HOT e COLD: correspondem repectivamente `as temperaturas que variam 6◦C
para mais ou para menos da temperatura ideal.
•TOO HOT e TOO COLD: correspondem `as temperaturas acima do estado HOT
e abaixo do estado COLD.
Neste ˆambito, a Aplica¸c˜ao de Controle controla os estados da bomba de calor
e das entradas de ar aﬁm de atingir e manter a temperatura ideal para cada andar do
edif´ıcio. Deste modo, para cada estado de temperatura recebido, a aplica¸c˜ao analisa um
conjunto de rela¸c˜oes causais e decide sobre as altera¸c˜oes de estados pertinentes.
Para a cria¸c˜ao da aplica¸c˜ao PON, foram criados tipos de FBEs com Attributes e
Methods pertinentes, os quais foram apropriadamente instanciados. Os FBEs criados foram
HeatPump, Vent e Sensor. Subsequentemente, de forma a tratar a regras de funcionamento
da aplica¸c˜ao em quest˜ao, foram criadas 16 Rules para cada andar do edif´ıcios. Como no
ambiente simulado o edif´ıcio possui 16 andares, um total de 256 Rules foram criadas para
o sistema de controle.
Aﬁm de comparar o desempenho do PON com o PI em sistemas embarcados, esta
aplica¸c˜ao foi desenvolvida sobre a plataforma embarcada relativa `a placa de hardware
eSysTech eAT55.
Os experimentos realizados com o Sistema de Condicionamento de Ar conﬁr-
maram a superioridade do PON, em termos de desempenho, em rela¸c˜ao ao PI, mesmo
quando executado sobre plataforma com recursos computacionais limitados. Isto se deve
principalmente `a redundˆancias temporais e estruturais inerente ao c´odigo desenvolvido
utilizando o PI [Banaszewski 2009].
E.3
SIMULADOR DE JOGO (PACMAN )
Desenvolvido sob o Framework PON 1.0 e 2.0 por Ronszcka [Ronszcka et al.
2011], esta aplica¸c˜ao consiste em um sistema de controle aplicado `a um simulador com
caracter´ısticas do cl´assico jogo Pacman1. Assim como o jogo de inspira¸c˜ao, o ambiente
simulado desenvolvido possui corredores que formam um labirinto, limitando as a¸c˜oes
de movimento dos personagens no cen´ario, nomeadamente o Pacman e seus inimigos, os
Fantasmas. Ainda, os personagens do simulador apresentam comportamento autˆonomo
1Os cr´editos do jogo e seus direitos autorais pertencem ao indiv´ıduo que o produziu ou a empresa que
o publicou. A utiliza¸c˜ao neste trabalho visa apenas o estudo acadˆemico, sem ﬁns lucrativos.


221
e predeterminado, ou seja, n˜ao s˜ao controlados por um usu´ario. A Figura 81 ilustra o
ambiente criado pelo simulador.
Figura 81: Ambiente gerado pelo simulador [Ronszcka et al. 2011].
Para o Pacman, o principal objetivo do jogo ´e maximizar os pontos ganhos. Ele
acumula pontos ao percorrer os corredores do labirinto em busca de pastilhas, que s˜ao
encontradas por todo o labirinto, dispondo de apenas 300 passos para tal. Enquanto busca
maximizar o n´umero de pontos, o Pacman deve ser capaz de fugir dos fantasmas que o
perseguem.
O simulador foi desenvolvido puramente em PI/POO e apresenta particularidades
que beneﬁciam a deﬁni¸c˜ao de regras para a movimenta¸c˜ao dos personagens nos corredores
do labirinto.
Dentre tais particularidades, destaca-se a classiﬁca¸c˜ao de esquinas em
categorias. As esquinas representam o encontro ou cruzamento de dois ou mais corredores
que comp˜oem o labirinto, cada qual com seu formato distinto. O labirinto utilizado no
simulador ´e formado por 9 diferentes formatos de esquinas, com o objetivo de minimizar a
quantidade de regras a serem criadas, uma vez que o tratamento das a¸c˜oes dos personagens
´e baseado nesta classiﬁca¸c˜ao.
A aplica¸c˜ao de controle deve ser capaz de controlar as a¸c˜oes do Pacman de forma
a maximizar sua quantidade de pontos ao ﬁm da execu¸c˜ao. Para ﬁns comparativos, a
aplica¸c˜ao de controle foi desenvolvida em PON (Framework PON 1.0 e 2.0) e PI/POO.


222
No total, foram criadas 99 estruturas causais (if-then-else no PI/POO e Rules no PON) e
11 tipos de classes de FBEs, nomeados Pacman, Ghost, Wall, Dot, EnergizerDot, Timer,
Maze, Score, GameState, VisualField e Corner.
Ademais, uma nova vers˜ao desta aplica¸c˜ao foi desenvolvida por Monte-Alto [Monte-
Alto 2015] utilizando a LingPON 1.0. Entretanto, esta aplica¸c˜ao n˜ao seguiu a mesma
modelagem da aplica¸c˜ao anterior, principalmente, segundo o autor, por limita¸c˜oes t´ecnicas
da LingPON 1.0. Nesta nova vers˜ao, a aplica¸c˜ao n˜ao possui interface gr´aﬁca. Ademais,
foram deﬁnidas para esta nova aplica¸c˜ao 385 Rules e 7 FBEs, nomeados Pacman, Ghost,
Wall, Dot, EnergizerDot, TickerEvent e MazeLimits.
Nos experimentos realizados com a aplica¸c˜ao desenvolvida sob o Framework PON
2.0, o PI/POO apresentou melhor desempenho quando comparado ao PON. Segundo
analises do autor, o fato de o Framework PON estar materializado sobre a linguagem
C++ afetou o desempenho da aplica¸c˜ao PON. Conclui-se ent˜ao que uma linguagem de
programa¸c˜ao e um compilador para o PON deveriam ser desenvolvidos para que o PON
alcan¸casse todo o seu potencial em termos de desempenho.
E.4
SIMULADOR DE TRANSPORTE INDIVIDUAL
Desenvolvido por Xavier [Xavier 2014] utilizando o Framework PON 2.0 e Ling-
PON, essa aplica¸c˜ao tem como objetivo simular o controle de um poss´ıvel exoesqueleto,
conforme o apresentado na Figura 82. A origem do desenvolvimento desta aplica¸c˜ao
surgiu de uma disciplina de mestrado em que se desenvolveu um simulador de um jogo
utilizando simples gr´aﬁcos 2D com essa tem´atica, a partir do qual se isolou apenas a parte
de tratamento de eventos para o desenvolvimento desta aplica¸c˜ao.
De maneira geral, esta aplica¸c˜ao caracteriza-se por um software simulador que
recebe eventos de dispositivos externos (i.e joystick e respectivos bot˜oes). Por simplicidade,
o autor desta aplica¸c˜ao decidiu por simular tamb´em os eventos provenientes dos dispositivos
externos, por meio da cria¸c˜ao de um software “gerador de eventos”.
Os principais requisitos do sistema s˜ao:
•O software simulador dever´a receber eventos de um joystick com dois bot˜oes (um
vermelho e um azul) e de uma chave liga e desliga.
•A chave liga e desliga o exoesqueleto como um todo.
•Os bot˜oes ligam e desligam um respectivo bra¸co mecˆanico (direito ou esquerdo). O


223
Figura 82: Figura conceitual de um exoesqueleto do projeto Hardiman I da General
Electric.
bot˜ao vermelho comanda o bra¸co esquerdo, enquanto o bot˜ao azul comanda o bra¸co
direito.
•O joystick movimenta ora o pr´oprio transporte (o exosqueleto), ora um ´unico
bra¸co mecˆanico (separadamente esquerdo ou direito), ou mesmo ambos os bra¸cos
simultaneamente. O movimento do bra¸co somente ocorre caso o pr´oprio esteja ligado
(ou caso ambos os bra¸cos estejam ligados). Como requisito, caso ambos os bra¸cos
mecˆanicos sejam ligados, ambos s˜ao movimentados em movimenta¸c˜ao conjunta e na
mesma dire¸c˜ao. Dessa forma, o joystick movimenta o exosqueleto nos eixos X e Y,
bem como controla os bra¸cos mecˆanicos (separadamente ou em conjunto) nos eixos
X, Y e Z.
A solu¸c˜ao t´ecnica PON desenvolvida para esta aplica¸c˜ao apresenta um conjunto
de vinte e duas Rules e quatro FBEs, a saber: Exoskeleton, Arm, Event e Simulation.
A aplica¸c˜ao desenvolvida foi utilizada para experimentos de compara¸c˜ao entre o
PON e o Paradigma Orientado a Eventos (POE). Os experimentos mostraram que na
aplica¸c˜ao POE, as decis˜oes sobre os comportamentos da aplica¸c˜ao ﬁcam dispersas pelo
software. Em contrapartida, no caso do PON, a tomada de decis˜ao ﬁca expressa de forma
centralizada ao utilizar Rules [Xavier 2014].


224
E.5
SISTEMA DE VENDAS
A aplica¸c˜ao Sistema de Vendas foi desenvolvida por Ronszcka utilizando o Fra-
mework PON 2.0 [Ronszcka et al. 2011]. Posteriormente, esta aplica¸c˜ao foi desenvolvida
tamb´em a partir da LingPON 1.0 por Ferreira [Ferreira 2016].
De modo geral, esta aplica¸c˜ao consiste na implementa¸c˜ao de um sistema de pedido
de vendas usual, isto ´e, uma tradicional aplica¸c˜ao CRUD (acrˆonimo de Create, Retrieve,
Update e Delete). O escopo dessa aplica¸c˜ao ´e resumido pelo diagrama de casos de uso
ilustrado na Figura 83.
Figura 83: Casos de uso do Sistema de Vendas.
Conforme ilustra a Figura 83, o ator Administrador ´e respons´avel por manter as
informa¸c˜oes do cadastro de formas de pagamentos. O ator Setor de Compras, por sua vez,
´e respons´avel por cadastrar e atualizar as informa¸c˜oes de produtos e do pr´oprio setor de
compras. Ainda, o ator Cliente, solicita uma venda a um respectivo ator Vendedor. Este,
por sua vez, cadastra o cliente e efetua a venda propriamente dita.
Inicialmente o cliente (denotado pelo ator cliente) solicita a compra para um
respectivo vendedor (denotado pelo ator vendedor).
Assim, o vendedor informar´a o
respectivo cliente que realizar´a o pedido. Uma vez escolhido e aprovado a venda para
determinado cliente, deve ser informado o produto que ir´a compor o pedido. O sistema
possui valida¸c˜oes quanto `a existˆencia de produtos e clientes. Ademais, veriﬁca-se o estoque
dispon´ıvel de tais produtos [Ferreira et al. 2013].
Ap´os todo o ciclo de informe de produtos, a venda poder´a ser ﬁnalizada ap´os a


225
inser¸c˜ao da forma de pagamento. Na implementa¸c˜ao desse sistema, existem apenas duas
formas de pagamento poss´ıveis, a Vista ou a Prazo. O cliente, em seu cadastro, possui uma
informa¸c˜ao sobre seu limite de cr´edito. Caso a forma de pagamento escolhida tenha sido a
Prazo, o sistema veriﬁca se o cliente tem permiss˜ao para efetuar a compra, confrontando o
valor total do pedido com seu limite de cr´edito [Ferreira et al. 2013].
Ademais, no cadastro do cliente h´a uma informa¸c˜ao que lhe concede um tipo de
classiﬁca¸c˜ao. Utiliza-se tal classiﬁca¸c˜ao para a concess˜ao de descontos especiais durante
a ﬁnaliza¸c˜ao da venda. Para tanto, existe um total de 20 tipos de 106 classiﬁca¸c˜ao de
clientes que disp˜oem de descontos que variam de uma faixa de 0% as 95% [Ferreira et al.
2013].
A t´ıtulo de exempliﬁca¸c˜ao, a Figura 84 demonstra a composi¸c˜ao da Rule res-
pons´avel por ﬁnalizar uma venda. Nela est˜ao relacionadas `as Premises que dever˜ao ser
satisfeitas para que a ﬁnaliza¸c˜ao da venda ocorra. Assim, a primeira Premise veriﬁcaria se
a forma de pagamento selecionada foi a prazo. Neste caso ´e necess´ario validar o limite
de cr´edito dispon´ıvel para o cliente, o qual faria parte da segunda Premise da Rule em
quest˜ao. A terceira e ´ultima Premise validaria o tipo de desconto concedido para o cliente
em quest˜ao (dentro os 20 poss´ıveis tipos de descontos).
Figura 84: Rule respons´avel por ﬁnalizar a venda [Ferreira et al. 2013].
Para a implementa¸c˜ao da aplica¸c˜ao foram criados 4 FBEs, nomeados Product,
Client, SalesOrder e SalesOrderItem. Ademais, para compor a base de regras da aplica¸c˜ao
foram criadas 20 Rules para cada instˆancia do FBE Product.
A aplica¸c˜ao desenvolvida sob o Framework PON foi utilizada para veriﬁcar os
benef´ıcios da aplica¸c˜ao de padr˜oes de projeto no desenvolvimento de aplica¸c˜oes PON.
Concluiu-se que a utiliza¸c˜ao de padr˜oes de projetos proporciona maior legibilidade e
manutenibilidade `a sistemas desenvolvidos utilizando o Framework PON.
A aplica¸c˜ao desenvolvida a partir da LingPON foi utilizada para ﬁns de compara¸c˜ao
de desempenho do c´odigo gerado pelo compilador com uma aplica¸c˜ao funcionalmente
equivalente desenvolvida sob o vi´es do PI/POO C++.
A vers˜ao em PI/POO C++
demonstrou desempenho pior quando comparada a aplica¸c˜ao desenvolvida em LingPON.


226
E.6
PORT˜AO ELETRˆONICO
Esta aplica¸c˜ao foi inicialmente desenvolvida por Wiecheteck [Wiecheteck et al.
2011] e aprimorada por Batista [Batista 2013] e Xavier [Xavier 2014]. Trata-se de soft-
ware exemplo tamb´em para tratamento de eventos, tendo como conceito um sistema de
automa¸c˜ao que recebe o evento de acionamento de um controle remoto para executar
opera¸c˜oes elementares como abrir e fechar automaticamente um port˜ao. Na verdade,
existem vers˜oes outras desta aplica¸c˜ao por ser usada como exerc´ıcio na disciplina que trata
de PON, disciplina esta lecionada junto ao CPGEI/UTFPR e PPGCA/UTFPR.
A aplica¸c˜ao ´e composta por quatro FBEs: Gate, Timer, Event e Light. Gate
representa o port˜ao eletrˆonico, Timer representa o contador de tempo, Light representa
a lˆampada e Event representa os eventos recebidos. Para cumprir os requisitos desta
aplica¸c˜ao foram implementadas 10 Rules.
Tanto em [Wiecheteck et al. 2011] como em [Batista 2013], esta aplica¸c˜ao foi
utilizada para demonstra¸c˜ao e valida¸c˜ao de m´etodos e t´ecnicas para o projeto de aplica¸c˜oes
PON. Em [Xavier 2014], a aplica¸c˜ao foi desenvolvida a partir do Framework PON e
LingPON. Estas aplica¸c˜oes foram comparadas com solu¸c˜oes semelhantes desenvolvidas a
partir do POE. Constatou-se que a programa¸c˜ao segundo o PON ´e mais f´acil, principalmente
pela forma como o conhecimento l´ogico-causal da aplica¸c˜ao ´e expresso em Rules [Xavier
2014].
E.7
CONTROLE DA ILUMINAC¸ ˜AO EM UMA CIDADE VIRTUAL 3D
Esta aplica¸c˜ao, desenvolvida utilizando o Framework PON C# 1.0 por Miranda
[Miranda 2016] como trabalho ﬁnal da disciplina de PON ofertada em 2016 na UTFPR,
prop˜oe a modelagem de um sistema para controlar a ilumina¸c˜ao do ambiente em uma
cidade virtual 3D. O relat´orio apresentado por Miranda nesta disciplina est´a presente no
Anexo C deste trabalho
Neste contexto, cidade virtual foi considerada como sendo um ambiente tridimen-
sional que reconstr´oi uma estrutura espacial complexa de uma cidade no computador e
que pode ser utilizada para ﬁns de planejamento e simula¸c˜oes (D¨OLLNER et al., 2005
apud MIRANDA, 2016).
A aplica¸c˜ao PON desenvolvida neste contexto trata-se de um m´odulo desenvolvido
para a cidade virtual 3D. Esta cidade virtual 3D ´e uma aplica¸c˜ao j´a existente, na qual ´e


227
poss´ıvel simular diferentes situa¸c˜oes presentes em uma cidade real, tais como varia¸c˜ao no
tr´afego de autom´oveis e diferentes condi¸c˜oes clim´aticas. Desse modo , aplica¸c˜ao PON foi
desenvolvida de forma a interagir com esta cidade virtual e controlar o funcionamento do
sistema de ilumina¸c˜ao ambiente.
Para controlar a ilumina¸c˜ao na cidade virtual foi criado apenas um FBE, o qual
possui trˆes atributos: clima (16 possibilidade), hor´ario (24 possibilidades) e visibilidade
(11 possibilidades). A partir destes trˆes atributos, 4224 Rules foram criadas. Apesar da
grande quantidade de entidades Rules presentes na aplica¸c˜ao, fato este que demonstraria
um alto n´ıvel de complexidade, o sistema de controle de ilumina¸c˜ao ainda ´e uma aplica¸c˜ao
simples. Isto porque as Rules presentes na aplica¸c˜ao foram geradas a partir da simples
combina¸c˜ao linear entre os poss´ıveis valores do trˆes Attributes presentes (clima, hor´ario e
visibilidade).
Ademais, esta aplica¸c˜ao ´e apenas um prot´otipo, o qual recebe um arquivo de
texto com os parˆametros a serem processados, processa essas informa¸c˜oes e disponibiliza
o resultado atrav´es da linha de comando. Neste sentido, at´e o presente momento a
aplica¸c˜ao PON n˜ao foi integrada com a cidade virtual, fato este que aumentaria o n´ıvel de
complexidade da aplica¸c˜ao.
E.8
WARSHIPATTACK GAME
O software desenvolvido ´e um jogo de combate a´ereo, sendo o equivalente a uma
implementa¸c˜ao simpliﬁcada do jogo cl´assico “River Raid”. Esse jogo foi escolhido por
possuir complexidade moderada, razo´avel para um estudo prospectivo.
Esse software possui uma interface gr´aﬁca em duas dimens˜oes que apresenta o
movimento de um avi˜ao controlado pelo jogador. O avi˜ao deve enfrentar inimigos que
aparecem em posi¸c˜oes aleat´orias. O objetivo do jogador com sua aeronave ´e terminar uma
fase vencendo o maior n´umero de inimigos.
Para a implementa¸c˜ao do software, apresentada em [Kossoski 2013], foi utilizado
o Framework PON e uma biblioteca gr´aﬁca externa, a saber Allegro [Liballeg 2004]. A
aplica¸c˜ao ´e composta por 6 entidades FBEs e 26 Rules.
Esta aplica¸c˜ao n˜ao foi comparada com aplica¸c˜oes desenvolvidas em outras materi-
aliza¸c˜oes ou paradigmas de programa¸c˜ao. O software foi utilizado para a apresenta¸c˜ao de
uma proposta de um m´etodo de teste para processos de desenvolvimento de aplica¸c˜oes
PON.


228
E.9
CTA SIMULATOR
Desenvolvida por Leonardo Pordeus [Pordeus 2015] utilizando a LingPON, esta
aplica¸c˜ao tem como objetivos desenvolver estrat´egias de controle de sem´aforos, simular
regi˜oes de tr´afego em uma ´area urbana e comparar o desempenho de diferentes estrat´egias
de controle. Para tal, esta aplica¸c˜ao deve ser capaz de simular elementos do mundo real,
tais como ve´ıculos, ruas, sem´aforos e cruzamentos.
O software foi dividido em dois m´odulos: um m´odulo de simula¸c˜ao e outro de
controle de estrat´egias. O m´odulo referente ao simulador foi desenvolvido utilizando
a linguagem de programa¸c˜ao C++, enquanto o m´odulo de controle de estrat´egias foi
desenvolvido tanto em PI (C++) quanto em PON (LingPON), para ﬁns de compara¸c˜ao
de desempenho.
Para modelar o sistema em entidades PON, foi criado apenas uma classe de FBE
para representar o sem´aforo. A quantidade de Rules depende da estrat´egia de controle
adotada, sendo que a estrat´egia com maior n´umero de Rules apresenta 18 Rules. Em um
dos cen´arios de teste que Pordeus utilizou, foram criados ao menos 100 pares de sem´aforos
e um total de 1800 Rules. Entretanto, isto n˜ao altera o n´ıvel de complexidade da aplica¸c˜ao,
uma vez que trata-se apenas de 100 repeti¸c˜oes do mesmo conjunto de 18 Rules.
Ao comparar o m´odulo de controle de estrat´egia desenvolvido em PON com a
solu¸c˜ao desenvolvida em PI/POO, concluiu-se que a aplicaca¸c˜ao desenvolvida segundo o
PON apresenta desempenho muito pr´oximo ao desempenho apresentado pela aplica¸c˜ao
PI/POO.
E.10
TORRE DE HAN´OI
A Torre de Han´oi ´e um problema cl´assico da matem´atica, fortemente utilizado
como um m´etodo l´udico para desenvolver o racioc´ınio, e tamb´em muito utilizado no ensino
de l´ogica e linguagens de programa¸c˜ao como um C´odigo que utiliza recursividade [Krug
2016].
Criado em 1883 pelo matem´atico ´Edouard Lucas, este problema consiste em um
jogo com trˆes hastes e um determinado n´umero de discos posicionados inicialmente na
haste da esquerda em ordem decrescente de tamanho, conforme ilustrado na Figura 85.
O objetivo do jogo ´e mover todos os discos para uma das hastes auxiliares. Embora
o objetivo do jogo seja simples, duas regras devem ser respeitadas:


229
Figura 85: Conﬁgura¸c˜ao Inicial da Torre de Han´oi [Krug 2016].
•Apenas um disco pode ser movido por vez.
•Um disco maior nunca pode ser colocado sobre um disco menor.
Para solucionar esse problema, Krug desenvolveu uma aplica¸c˜ao que soluciona o
problema da Torre de Han´oi utilizando a LingPON 1.0. Esta aplica¸c˜ao foi apresentada
como trabalho ﬁnal da disciplina de PON ofertada em 2016 na UTFPR. O relat´orio
apresentado por Krug nesta disciplina est´a presente no Anexo C deste trabalho
No c´odigo-fonte LingPON foram criadas trˆes entidades FBEs: Haste, Disco e
Controle. Devido a diﬁculdades encontradas na atual vers˜ao da LingPON, a implementa¸c˜ao
ﬁcou restrita a apenas 3 discos e 8 Rules [Krug 2016].
A solu¸c˜ao desenvolvida em LingPON teve seu desempenho e facilidade de pro-
grama¸c˜ao comparado com uma solu¸c˜ao equivalente desenvolvida utilizando o Paradigma
Procedimental (PP) atrav´es da linguagem de programa¸c˜ao C. Constatou-se que o desen-
volvimento da solu¸c˜ao em LingPON foi mais f´acil quando comparado ao PP. Isto porque o
c´odigo em LingPON ´e mais claro e de mais f´acil leitura do que o c´odigo em C. Em termos
de desempenho, a aplica¸c˜ao LingPON apresentou resultados melhores do que a solu¸c˜ao PP.
Em um cen´ario de teste no qual a aplica¸c˜ao deveria resolver 1000 vezes o mesmo problema,
a aplica¸c˜ao PP demorou 29.29 s., enquanto a solu¸c˜ao desenvolvida em LingPON 1.0 e
compilada para linguagem C demorou apenas 5 s. [Krug 2016].
E.11
ALGORITMO TRIANGULAR MESH SLICING
Uma t´ecnica comum ao processo de manufatura de pe¸cas industriais ´e a constru¸c˜ao
de um objeto s´olido tridimensional (3D) a partir de sucessivas camadas planas de material.
Os dados para a constru¸c˜ao do objeto vˆem de um modelo geom´etrico gerado por sistemas


230
computacionais, tais como Computer-Aided Design (CAD) ou obtido a partir de Tomograﬁa
Computadorizada. O modelo ´e ent˜ao fatiado, a ﬁm de obter superf´ıcies bidimensionais,
representando cada camada em que o material de fabrica¸c˜ao ser´a adicionado. Uma vez
processado, esses dados s˜ao enviados para uma m´aquina que “imprime” cada camada at´e
que o objeto seja constru´ıdo [Volpato 2007].
Para ﬁns de compara¸c˜ao, Krachinski [Krachinski et al. 2015] implementou o
algoritmo de corte tradicional utilizado no processo de manufatura de pe¸cas 3D, com base
na aplica¸c˜ao desenvolvida por Gregori [Gregori et al. 2012], utilizando o Framework PON
e LingPON, e os comparou com uma solu¸c˜ao equivalente desenvolvida sob o PI/POO.
O algoritmo de corte tradicional consiste em interceptar uma malha de triˆangulos
por planos 2D imagin´arios, variando a coordenada em rela¸c˜ao ao eixo Z. A estrat´egia
utilizada ´e simples e at´e mesmo lenta, mas ´util para ﬁns de compara¸c˜ao de desempenho.
A implementa¸c˜ao em PON desta aplica¸c˜ao consiste em trˆes classes de FBE, a
saber NOPTriangle, NOPTraditionalMesh e NOPOrderedMesh, e uma ´unica Rule. O FBE
NOPTriangle possui dois Attributes, atZMin e atZMax, os quais tˆem seus estados avaliados
pela ´unica Rule presente na aplica¸c˜ao.
Ap´os compara¸c˜oes de desempenho em diferente cen´arios, concluiu-se que as
aplica¸c˜oes PON apresentaram resultados piores do que o a solu¸c˜ao desenvolvida sob o PI.
E.12
REFLEX˜AO
Conforme apresentado neste Apˆendice, uma s´erie de aplica¸c˜oes PON foram desen-
volvidas utilizando o Framework PON e a LingPON. Cada uma das aplica¸c˜oes apresentadas
tinha um objetivo espec´ıﬁco, como compara¸c˜oes de desempenho ou facilidade de pro-
grama¸c˜ao.
`A luz do levantamento sobre as aplica¸c˜oes PON realizado neste trabalho, ´e
constatado que seria interessante para a consolida¸c˜ao do PON um experimento que
envolvesse o desenvolvimento de uma aplica¸c˜ao de maior envergadura que as previamente
desenvolvidas. A aplica¸c˜ao desenvolvida poderia ser utilizada para compara¸c˜oes entre
as duas materializa¸c˜oes em software mais est´aveis do PON, nomeadamente Framework
PON 2.0 e LingPON. Ademais, a compara¸c˜ao das aplica¸c˜oes PON com uma solu¸c˜ao
funcionalmente equivalente desenvolvida por outrem, externo ao grupo de pesquisa PON,
em PI/POO seria de grande valor para a consolida¸c˜ao do PON frente ao demais paradigmas
de programa¸c˜ao.


231
Conforme ´e apresentado na se¸c˜ao 2.4, o software de controle de futebol de robˆos
apresenta-se como uma excelente aplica¸c˜ao a ser desenvolvida sob o PON. Isto porque
esta ´e reconhecida como uma aplica¸c˜ao complexa perante a sociedade cient´ıﬁca, a qual ´e
comumente utilizada para valida¸c˜ao de novos conceitos e t´ecnicas relacionados `a computa¸c˜ao
[Yoon 2015]. Portanto, a apresenta¸c˜ao desta aplica¸c˜ao sob o vi´es do PON poder´a ser
de consider´avel valor, ou ao menos pertinente, para futuras publica¸c˜oes a respeito do
PON.


232
APˆENDICE F -- PROGRAMAC¸ ˜AO ORIENTADA A AGENTES
Um sistema baseado em agentes ´e aquele constru´ıdo sobre um determinado n´ıvel
de abstra¸c˜ao, chamado agente [Wooldridgey e Ciancarini 2001]. Sistemas baseado em
agentes podem ser compostos por apenas um agente, entretanto seu maior potencial
reside na aplica¸c˜ao de sistemas compostos por multi agentes. Por agente, entende-se uma
entidade computacional que apresenta as seguintes propriedades:
•Autonomia: agentes possuem informa¸c˜oes sobre seu estado atual e s˜ao capazes
de tomar decis˜oes sobre o que fazer sem interven¸c˜ao direta humana ou de outros
agentes. Tais informa¸c˜ao s˜ao mantidas encapsuladas pelo agente, de modo que n˜ao
seja acess´ıvel a nenhum outro agente que comp˜oe o sistema.
•Reatividade: todo agente est´a inserido em ambiente e deve ser capaz de, percebendo
qualquer altera¸c˜ao no meio em que est´a inserido, responder a tais impulsos.
•Proatividade: agentes n˜ao simplesmente agem em resposta ao ambiente em que
est˜ao inseridos, eles devem ser capaz de, por iniciativa pr´opria, tomar decis˜oes que
os aproximem de seus objetivos.
•Habilidade Social: agentes se comunicam uns com outros atrav´es de uma determinada
linguagem de comunica¸c˜ao [Genesereth e Ketchpel 1994] e, normalmente, possuem a
habilidade de cooperar um com os outros de forma a alcan¸car objetivos comuns.
Ao projetar um sistema baseado em agentes, ´e importante determinar o qu˜ao
soﬁsticado ser´a o racioc´ınio dos agentes. Entende-se por racioc´ınio o processo de escolha
de qual a¸c˜ao ser´a executada. Agentes deliberativos ou cognitivos possuem um modelo
expl´ıcito e simb´olico do ambiente em que est´a inserido e, portanto, s˜ao capazes de raciocinar,
planiﬁcar e negociar com outros agentes a ﬁm de coordenar suas a¸c˜oes [Wooldridge et al.
1995,Nwana 1996]. Por outro lado, agentes reativos s˜ao aqueles que n˜ao possuem modelos
internos de seus ambientes, ao inv´es disso, agem apenas de forma a responder `a est´ımulos
externos [Nwana 1996].


233
Agentes reativos apresentam certa semelhan¸ca com as entidades computacionais
que comp˜oem o PON. Ao ter seu estado alterado, por exemplo, um Attribute envia uma
notiﬁca¸c˜ao `as entidades Condition associadas. O Attribute n˜ao executa nenhum tipo de
delibera¸c˜ao para decidir se deve ou n˜ao enviar a notiﬁca¸c˜ao, ele apenas a envia como
resposta `a um est´ımulo (mudan¸ca de seu estado).
Normalmente, programadores familiarizados com abordagens orientada a objetos
n˜ao conseguem perceber nenhuma novidade na abordagem orientada a agentes. Isto
porque objetos s˜ao deﬁnidos como entidades computacionais que encapsulam algum
estado, s˜ao capazes de executar a¸c˜oes ou m´etodos neste estado e podem comunicar-se
atrav´es de mensagens. Portanto, h´a suposta rela¸c˜ao entre objetos e agentes [Wooldridgey
e Ciancarini 2001].
Entretanto, apesar de existirem evidentes semelhan¸cas, existem
diferen¸cas signiﬁcativas entre agentes e objetos que justiﬁcam sua diferencia¸c˜ao como n´ıvel
de abstra¸c˜ao.
A primeira diferen¸ca a ser destacada ´e referente ao grau de autonomia. Em
linguagens de programa¸c˜ao como Java e C++, pode-se declarar atributos e m´etodos com
escopo privado, ou seja, s˜ao acess´ıveis somente de dentro do pr´oprio objeto, respeitando
assim o princ´ıpio de encapsulamento da orienta¸c˜ao a objetos. Sendo assim, um objeto
pode ser idealizado como exibindo autonomia sobre o seu pr´oprio estado. Por´em, um
objeto n˜ao apresenta, por deﬁni¸c˜ao, controle sobre seu comportamento. Ademais, caso um
dado objeto tenha um m´etodo ”m” de escopo p´ublico, qualquer outro objeto que comp˜oe
o sistema poder´a invocar tal m´etodo, alterando seu estado interno. Nesse caso, o objeto
n˜ao ter´a controle sobre quando o m´etodo ser´a invocado [Wooldridgey e Ciancarini 2001].
Em um sistema multi agentes, entretanto, n˜ao existe a ideia de um agente
invocando m´etodos uns dos outros, mas sim solicitando que uma determinada a¸c˜ao seja
executada. Quando um agente recebe tal solicita¸c˜ao, ele pode decidir por executar ou
descartar a a¸c˜ao. Portanto, o controle sobre qual a¸c˜ao ser´a executada ´e diferente para
sistemas orientado a agente e objetos. No caso orientado a objetos, a decis˜ao encontra-se
com o objeto que chama o m´etodo. J´a no caso orientado a agentes, a decis˜ao recai sobre o
agente que recebe a solicita¸c˜ao [Wooldridgey e Ciancarini 2001].
Outra importante diferen¸ca diz respeito ao controle de execu¸c˜ao. Por deﬁni¸c˜ao,
cada agente tem sua pr´opria thread de execu¸c˜ao, a qual o mant´em em um ciclo inﬁnito de
observa¸c˜ao do ambiente, atualizando seu estado interno e selecionando quais a¸c˜oes ser˜ao
executadas, gerando assim descentraliza¸c˜ao de processamento [Resnick 1997].


234
ANEXO A -- BNF DA LINGPON 1.0
Neste anexo ´e apresentado a especiﬁca¸c˜ao da linguagem de programa¸c˜ao da
LingPON 1.0 segundo Backus-Naur Form (BNF) extra´ıda de [Ferreira 2016].
C´odigo 1: Especiﬁca¸c˜ao da linguagem PON LingPON 1.0 segundo Backus-Naur Form
(BNF) [Ferreira 2016].
1
PROGRAM
: fbes
inst
strategy
rules
main
2
| fbes
inst
strategy
rules
3
;
4
5
inst
: INST
declarations
END_INST
6
;
7
8
strategy
: STRATEGY
estrategy_declaration
END_STRATEGY
9
;
10
11
estrategy_declaration
: NO_ONE
12
| BREADTH
13
| DEPTH
14
;
15
16
17
declarations
: declaration
18
| declaration
declarations
19
;
20
21
declaration
: type
ids
22
;
23
24
;
25
ids
: id
26
| id COMMA
ids
27
;
28
29
rules
: rule
30
| rule
rules
31
;
32
33
rule
: RULE
rule_body
END_RULE
34
| RULE id
rule_body
END_RULE
35
| RULE
depends
id
rule_body
END_RULE
36
| RULE id
depends
id
rule_body
END_RULE
37
;
38
39
depends
: DEPENDS
40
;
41
42
rule_body
: decl_condition
decl_action
43
| decl_properties
decl_condition
decl_action
44
;
45
46
decl_properties
: PROPERTIES
properties_body
END_PROPERTIES


235
47
;
48
49
properties_body
: properties_type
value
50
| properties_body
properties_type
value
51
;
52
53
properties_type
: PRIORITY
54
| KEEPER
55
56
decl_condition
: CONDITION
condition_body
END_CONDITION
57
| CONDITION
id
condition_body
END_CONDITION
58
;
59
60
condition_body
: subcondition
operator
condition_body
61
| subcondition
62
;
63
64
operator
: AND
65
| OR
66
;
67
68
subcondition
: SUBCONDITION
id
subcondition_body
END_SUBCONDITION
69
;
70
71
subcondition_body
: premise
AND
subcondition_body
72
| premise
73
;
74
75
premise
: PREMISE
exp
76
| PREMISE
id exp
77
| PREMISE
IMP exp
78
| PREMISE
IMP id exp
79
;
80
81
exp
: fator
comp
fator
82
83
comp
: EQ
84
| NE
85
| LT
86
| GT
87
| LE
88
| GE
89
;
90
91
fator
: id
92
| NUMBER
93
| boolean
94
| FLOATVALUE
95
| STRINGVALUE
96
| CHARVALUE
97
;
98
99
boolean
: TRUE
100
| FALSE
101
;
102
103
decl_action
: ACTION
action_body
END_ACTION
104
| ACTION id
action_body
END_ACTION
105
;
106
107
action_body
: action_elements
action_body
108
| action_elements
109
;
110
111
action_elements
: instigation
112
| method_use
113
| exp
SEMICOLON
114
;
115
116
instigation
: INSTIGATION
method_use
117
| INSTIGATION
id
method_use
118
;
119


236
120
method_use
: id LP RP
SEMICOLON
121
;
122
123
id
: ID
124
| ID POINT ID
125
;
126
127
fbes
: fbe
128
| fbe
fbes
129
;
130
131
fbe
: FBE
fbe_body
END_FBE
132
| FBE id
fbe_body
END_FBE
133
;
134
135
fbe_body
: decl_attributes
decl_methods
136
| decl_attributes
137
;
138
139
decl_attributes
: ATTRIBUTES
attributes
END_ATTRIBUTES
140
;
141
142
attributes
: attributes_body
143
| attributes_body
attributes
144
;
145
146
attributes_body
: type id value
147
| type id
SEMICOLON
148
;
149
150
type
: BOOLEAN
151
| INTEGER
152
| PFLOAT
153
| STRING
154
| CHAR
155
| id
156
;
157
158
value
: NUMBER
159
| boolean
160
| id
161
| FLOATVALUE
162
| STRINGVALUE
163
| CHARVALUE
164
;
165
166
decl_methods
: METHODS
methods
END_METHODS
167
;
168
169
methods
: method_body
170
| method_body
methods
171
;
172
173
method_body
: METHOD id LP id ASSIGN id
method_operator
value RP
174
| METHOD id LP id ASSIGN id
method_operator
id RP
175
| METHOD id LP id ASSIGN
value RP
176
| METHOD id LP id ASSIGN id RP
177
| METHOD id LP RP
INNER_CODE_METHOD
178
;
179
180
method_operator
: PLUS
181
| MINUS
182
| MULT
183
| DIV
184
;
185
186
main
: MAIN
INNER_CODE_MAIN


237
ANEXO B -- BNF DA LINGPON 1.2
Neste anexo ´e apresentado a especiﬁca¸c˜ao da linguagem de programa¸c˜ao da
LingPON 1.2 segundo Backus-Naur Form (BNF). Em vermelho encontra-se destacado as
diferen¸cas entre a BNF da LingPON 1.0 e LingPON 1.2.
C´odigo 1: Especiﬁca¸c˜ao da linguagem PON LingPON 1.2 segundo Backus-Naur Form
(BNF).
1
PROGRAM
: fbes
inst
strategy
rules
main
2
| fbes
inst
strategy
rules
3
;
4
5
inst
: INST
declarations
END_INST
6
;
7
8
strategy
: STRATEGY
estrategy_declaration
END_STRATEGY
9
;
10
11
estrategy_declaration
: NO_ONE
12
| BREADTH
13
| DEPTH
14
;
15
16
17
declarations
: declaration
18
| declaration
declarations
19
;
20
21
declaration
: type
ids
22
;
23
24
;
25
ids
: id
26
| id COMMA
ids
27
;
28
29
rules
: rule
30
| rule
rules
31
| formRule
32
| formRule
rules
33
;
34
35
rule
: RULE
rule_body
END_RULE
36
| RULE id
rule_body
END_RULE
37
| RULE
depends
id
rule_body
END_RULE
38
| RULE id
depends
id
rule_body
END_RULE
39
;
40
41
formRule
: FORM_RULE
rule_body
END_FORM_RULE
42
| FORM_RULE
id
rule_body
END_FORM_RULE
43
| FORM_RULE
depends
id
rule_body
END_FORM_RULE
44
| FORM_RULE
id
depends
id
rule_body
END_FORM_RULE


238
45
;
46
47
fbeRules
: fbeRule
48
| fbeRule
fbeRules
49
;
50
51
fbeRule
: FBE_RULE
rule_body
END_FBE_RULE
52
| FBE_RULE
id
rule_body
END_FBE_RULE
53
| FBE_RULE
depends
id
rule_body
END_FBE_RULE
54
| FBE_RULE
id
depends
id
rule_body
END_FBE_RULE
55
;
56
57
rule_body
: decl_condition
decl_action
58
| decl_properties
decl_condition
decl_action
59
;
60
61
decl_properties
: PROPERTIES
properties_body
END_PROPERTIES
62
;
63
64
properties_body
: properties_type
value
65
| properties_body
properties_type
value
66
;
67
68
properties_type
: PRIORITY
69
| KEEPER
70
71
decl_condition
: CONDITION
condition_body
END_CONDITION
72
| CONDITION
id
condition_body
END_CONDITION
73
;
74
75
condition_body
: subcondition
operator
condition_body
76
| subcondition
77
;
78
79
operator
: AND
80
| OR
81
;
82
83
subcondition
: SUBCONDITION
id
subcondition_body
END_SUBCONDITION
84
;
85
86
subcondition_body
: premise
AND
subcondition_body
87
| premise
88
;
89
90
premise
: PREMISE
exp
91
| PREMISE
id exp
92
| PREMISE
IMP exp
93
| PREMISE
IMP id exp
94
;
95
96
exp
: fator
comp
fator
97
98
comp
: EQ
99
| NE
100
| LT
101
| GT
102
| LE
103
| GE
104
;
105
106
fator
: id
107
| NUMBER
108
| boolean
109
| FLOATVALUE
110
| STRINGVALUE
111
| CHARVALUE
112
;
113
114
boolean
: TRUE
115
| FALSE
116
;
117


239
118
decl_action
: ACTION
action_body
END_ACTION
119
| ACTION id
action_body
END_ACTION
120
;
121
122
action_body
: action_elements
action_body
123
| action_elements
124
;
125
126
action_elements
: instigation
127
| method_use
128
| exp
SEMICOLON
129
;
130
131
instigation
: INSTIGATION
method_use
132
| INSTIGATION
id
method_use
133
;
134
135
method_use
: id LP RP
SEMICOLON
136
;
137
138
id
: ID
139
| ID POINT id
140
;
141
142
fbes
: fbe
143
| fbe
fbes
144
;
145
146
fbe
: FBE
fbe_body
END_FBE
147
| FBE id
fbe_body
END_FBE
148
;
149
150
fbe_body
: decl_attributes
decl_methods
fbeRules
151
| decl_attributes
decl_methods
152
| decl_attributes
153
;
154
155
decl_attributes
: ATTRIBUTES
attributes
END_ATTRIBUTES
156
;
157
158
attributes
: attributes_body
159
| attributes_body
attributes
160
;
161
162
attributes_body
: type id value
163
| type id
SEMICOLON
164
;
165
166
type
: BOOLEAN
167
| INTEGER
168
| PFLOAT
169
| STRING
170
| CHAR
171
| id
172
;
173
174
value
: NUMBER
175
| boolean
176
| id
177
| FLOATVALUE
178
| STRINGVALUE
179
| CHARVALUE
180
;
181
182
decl_methods
: METHODS
methods
END_METHODS
183
;
184
185
methods
: method_body
186
| method_body
methods
187
;
188
189
method_body
: METHOD id LP id ASSIGN id
method_operator
value RP
190
| METHOD id LP id ASSIGN id
method_operator
id RP


240
191
| METHOD id LP id ASSIGN
value RP
192
| METHOD id LP id ASSIGN id RP
193
194
| METHOD id LP RP
INNER_CODE_METHOD
195
;
196
197
method_operator
: PLUS
198
| MINUS
199
| MULT
200
| DIV
201
;
202
203
main
: MAIN
INNER_CODE_MAIN


241
ANEXO C -- RELAT´ORIOS AINDA N˜AO PUBLICADOS SOBRE
APLICAC¸ ˜OES PON
Neste anexo se encontram dois relat´orios no formato de artigos. Esses relat´orios
foram o resultado da disciplina “T´opicos Especiais Em Engenharia da Computa¸c˜ao: Para-
digma Orientado A Notiﬁca¸c˜oes” ofertada pelo Curso de P´os-Gradua¸c˜ao em Engenharia
El´etrica e Inform´atica Industrial (CPGEI/UTFPR), sob a supervis˜ao do prof. Dr. Jean
Marcelo Sim˜ao. Esses relat´orios foram referenciados na Subse¸c˜ao E deste trabalho. Por
ﬁm, os relat´orios anexados tiveram o acordo dos autores e do professor da disciplina.


Torre de Hanói com LingPON – Paradigma Orientado
a Notificações
Douglas Lusa Krug
Instituto Federal do Paraná - IFPR
União da Vitória, PR
douglas.krug@ifpr.edu.br
Resumo- Este artigo relata a experiência da implementação
de um problema clássico de lógica de programação, a Torre de
Hanói, utilizando o Paradigma Orientado a Notificações – PON,
utilizando a Linguagem PON – LingPON. Através dele é possível
entender um pouco mais sobre este novo paradigma, observando
algumas comparações e sugestões de melhoria para o seu
desenvolvimento.
Abstract- This article reports the experience of implementing
a classical problem in programming logic, Hanoi Tower, using the
NOP - Notification Oriented Paradigm, using the NOP language -
LingPON. Through it is possible understand a little more about
this new paradigm, noting some comparisons and improvement
suggestions for its development.
Palavras chave- Paradigma Orientado a Notificações; Lógica
de Programação; Torre de Hanói.
Keywords- Notification Oriented Paradigm; Programming
Logic; Hanoi Tower.
I.    INTRODUÇÃO
O presente artigo relata o desenvolvimento de um
problema clássico no ensino de lógica de programação, Torre
de Hanói, utilizando o Paradigma Orientado a Notificações –
PON, materializado em Linguagem PON – LingPON.
O Paradigma Orientado a Notificações – PON, vem sendo
desenvolvido por um grupo de pesquisadores da Universidade
Tecnológica Federal do Paraná – UTFPR, apresentando-se
como uma alternativa para o desenvolvimento de aplicações
em plataforma de software e hardware, ele se propõe a
resolver certos problemas existentes nos paradigmas usuais de
programação, como o Paradigma Imperativo – PI, e o
Paradigma Declarativo – PD [1][2].
Desde sua concepção inicial, o PON vem passando por
evoluções e sendo validado em diversas aplicações, tanto em
software como em hardware.
Em termos de desenvolvimento de software, sua primeira
aplicação foi através de um framework, desenvolvido em C++,
em sua evolução como paradigma, nasceu a Linguagem PON,
denominada LingPON.
Para validar a facilidade de utilização da LingPON foi
escolhido um problema clássico no estudo de lógica de
programação, a Torre de Hanói, com o intuito de validar a
facilidade de programação da linguagem, e a versatilidade,
pois este problema é usualmente resolvido utilizando
recursividade.
Inicialmente será abordado um pouco sobre o PON e sua
materialização em LingPON, na sequência um breve histórico
sobre a Torre de Hanói e sua explicação.
Será também explicado a forma de desenvolvimento
utilizando a LingPON e uma comparação de desempenho
entre o desenvolvimento em PON e o desenvolvimento no
Paradigma Procedimental - PP.
Para finalizar serão apresentadas algumas dificuldades
encontradas, acompanhada de sugestões de melhoria para a
LingPON.
II.   PARADIGMA ORIENTADO A NOTIFICAÇÕES
    O Paradigma Orientado a Notificações – PON apresenta
melhorias em comparação aos paradigmas vigentes, que por
tempo vivem uma inércia de evolução, corrigindo certas
deficiências apresentadas nestes, mas também aproveitando-se
de pontos fortes que consagraram estes paradigmas.
    O PON encontra inspirações no PI, como a flexibidade
algorítimica e a abstração de classes/objetos da Programação
Orientada a Objetos – POO, assim como aproveita conceitos
próprios do PD, como a facilidade de programação em alto
nível e a representação do conhecimento em regras, dos
Sistemas Baseados em Regras – SBR [3].
    Os principais elementos do PON são as Fact Base Elements
– FBE e as Rules, as FBEs podem ser associadas a objetos do
mundo real, e as rules podem ser associadas a regras de
relação lógico causal.
    O modelo e a lógica de funcionamento do PON podem ser
descritos da seguinte forma: As Rules são compostas por
Conditions e Actions, as Conditions podem se relacionar com
uma ou mais Premisses, que por sua vez, são responsáveis por
verificar os Attributes de uma FBE. Cada Premisse é composta
por uma referência a um Attribute, por um operador lógico e
um valor. Esta referência de um Attribute utilizada na
Premisse é quem notifica a mudança de seu estado.
    Uma Rule pode ser composta de uma ou mais Premisses, a
partir do momento em que todas as Premisses são aprovadas, a
Rule é aprovada e notifica uma Action. A Action referencia
uma ou mais Instigations, as quais são associadas a Methods
da FBE. Sempre que o valor de um Attribute é alterado ele
mesmo notifica as Premisses que são relacionadas a ele. As
Premises, por sua vez, são reavaliadas e, através de uma
operação lógica é comparada ao novo valor do Attribute com
uma constante ou um valor notificado por outro Attribute.
Caso o resultado lógico da reavaliação da entidade Premises
seja alterado, a Premise notifica um conjunto de entidades


Conditions relacionadas a ela. Em seguida, as Conditions
também têm seus estados lógicos reavaliados de acordo com
os resultados lógicos das Premises. Assim, quando todas as
entidades Premises que compõem uma entidade Condition
apresentam seus valores lógicos verdadeiros, a entidade
Condition também é satisfeita, aprovando a execução da sua
respectiva Rule. Com isso, a entidade Action agregada a esta
Rule é executada, invocando os Methods necessários através
das entidades Instigations [4].
A partir deste mecanismo de notificações é possível
desenvolver programas com melhor desempenho, menor
número de redundâncias estruturais e temporais. Estes
programas são mais apropriados para paralelismo e
distribuição do que os sistemas computacionais desenvolvidos
por meio das soluções baseadas em paradigmas atuais [5].
Uma das formas de materialização do PON para software é
utilizando a LingPON e o compilador construído para ela.
De modo geral, o código fonte da LingPON segue um
padrão de declarações. Primeiramente, o desenvolvedor
precisa definir os FBEs de seu programa. Em seguida, o
desenvolvedor precisa declarar as instâncias de tais FBEs, bem
como definir a estratégia de escalonamento das Rules.
Subsequentemente, é necessário definir as Rules para fins de
avaliação lógico causal dos estados do FBEs por meio de
notificações. Por fim, é possível adicionar código específico
da linguagem alvo escolhida no processo de compilação (e.g.
C ou C++) com a utilização do bloco de código main [6].
III.   TORRE DE HANÓI
A Torre de Hanói é um problema clássico da matemática,
fortemente utilizado como um método lúdico para desenvolver
o raciocínio, e também muito utilizado no ensino de lógica e
linguagens de programação como um exemplo de algoritmo
que utiliza recursividade.
Este problema foi criado em 1883 pelo matemático
Francês Édouard Lucas e consiste em um jogo com três hastes,
e um determinado número de discos, postos inicialmente na
haste da esquerda, em ordem decrescente de tamanho,
conforme ilustrado na Figura 1.
Figura 1. Torre de Hanói – Configuração Inicial [7]
O objetivo do jogo é mover todos os discos para uma das
hastes auxiliares, ficando conforme ilustrado na Figura 2.
Figura 2. Torre de Hanói – Final [7]
Embora o objetivo do jogo seja simples, duas regras
devem ser seguidas:
1.
Apenas um disco pode ser movido por vez;
2.
Um disco maior nunca pode ser colocado em cima de
um disco menor.
É também esperado que o objetivo seja cumprido com um
número mínimo de movimentos, representado pela fórmula
matemática (2n - 1), onde n é igual ao número de discos.
Desta forma, quando temos apenas 3 discos o número
mínimo de movimentos necessário é 7, para 5 discos é 31 e
assim por diante.
O objetivo de escolha deste problema é validar o
paradigma e a LingPON quanto a facilidade de programação e
sua versatilidade, pois usualmente este problema é resolvido
utilizando recursividade.
IV.   DESENVOLVIMENTO EM LINGPON
 
A materialização escolhida para o desenvolvimento do
trabalho foi LingPON para atender ao objetivo que foi
proposto, e compilado para C, C++ 1.0 e C++ 1.1.
Inicialmente foram definidas as FBEs necessárias para
solucionar o problema, sendo elas Haste, Disco e Controle.
A FBE Haste conta com atributos que controlam o último
disco que está em cada haste, para poder validar se o disco que
está sendo movimentado para a haste é menor do que o que já
está presente na haste.
Na FBE Disco contém o atributo que identifica em qual
haste o disco está posicionado, seja haste A, B ou C.
Para a FBE Controle foram criados quatro atributos, sendo
um atributo para controlar o último disco movimentado, um
atributo para contar a quantidade de movimentos, um atributo
para controlar se um movimento está sendo realizado,
evitando paralelismo de movimentos, e um último atributo
para armazenar o último movimento realizado, evitando
repetição de movimentos.
Foram criadas 3 instâncias da FBE Haste, sendo uma
instância para cada haste que compõe o problema. Para a FBE
Disco foram criadas 3 instâncias também, sendo uma para
cada disco, neste caso, o número de instâncias deve ser
ampliado conforme o número de discos é ampliado. Caso seja
necessário aumentar o número de discos, também é necessário
criar novas regras para controlar os movimentos.


Já para a FBE Controle apenas uma instância foi criada,
pois ela serve para controlar os movimentos de todos os discos
entre todas as hastes.
Devido as dificuldades e sugestões que serão relatadas nos
tópicos “Dificuldades Encontradas” e “Sugestões de
Melhorias” a implementação em LingPON ficou restrita a
apenas 3 discos, a ideia inicial era deixar as regras flexíveis
assim como na implementação em PP.
Foram criadas 8 regras, sendo 7 para controlar os
movimentos e uma para indicar a finalização do processo. As
7 regras que controlam o movimento baseiam-se nas regras do
jogo, onde não é possível movimentar um disco maior para
cima de um disco menor, além disso elas controlam os
movimentos realizados, evitando movimentos desnecessários.
Também para evitar o paralelismo de movimentos um atributo
da FBE Controle foi utilizado para indicar o momento em que
o movimento está concluído.
V.   COMPARAÇÃO DE DESEMPENHO
Além de desenvolver um programa em LingPON para
melhorar o entendimento do paradigma, a ideia também é
desenvolver um algoritmo para solucionar o mesmo problema
em um paradigma vigente, para poder realizar algumas
comparações.
Para comparação deste trabalho os seguintes critérios
foram selecionados: facilidade de desenvolvimento;
legibilidade do código; número mínimo de movimentos; e
desempenho.
O desenvolvimento do algoritmo de comparação para
solucionar a Torre de Hanói foi desenvolvido em C, utilizando
o Paradigma Procedimental – PP, de forma não recursiva.
Quanto à facilidade de desenvolvimento, é possível
afirmar que a LingPON foi mais fácil, a partir do momento em
que entende-se o funcionamento da mesma, a programação
fica intuitiva.
A legibilidade do código gerado em LingPON é mais claro
e de mais fácil leitura do que o gerado em C.
Quanto à quantidade de linhas geradas, em C foram
geradas 180 linhas de código, já em LingPON foram geradas
286 linhas de código.
Ambos os algoritmos atingiram o objetivo de realizar a
tarefa com o número mínimo de movimentos necessário para
isso. Embora a flexibilidade e número de discos apenas foi
possível utilizando a implementação no paradigma vigente.
Quanto ao desempenho, pode-se afirmar, sem sombra de
dúvidas que o código gerado utilizando o PON é melhor do
que o gerado em PP.
Como não foi possível flexibilizar o número de discos em
PON, para realizar a comparação de desempenho entre as
implementações, foi optado por executar várias vezes o
mesmo algoritmo, dessa forma permitindo um elevado número
de movimentos para avaliar o desempenho.
Para comparação o código em LingPON foi compilado em
C, C++ 1.0 e C++ 1.1. Era desejável gerar o código também
para C++ 2.0 porém não foi possível devido a erros no
compilador que serão detalhados no tópico “Dificuldades
Encontradas”.
A Figura 3 demonstra uma tabela de comparação entre os
códigos compilados.
Figura 3. Tabela de Comparação de Desempenho
A tabela demonstra a execução dos programas compilados
e C (PP), C (PON), C++ 1.0 (PON) e C++ 1.1 (PON) para o
número de repetições que consta na coluna Repetições, o
tempo relatado é sem segundos.
Analisando os dados é possível observar que o código
gerado em C (PON) teve um desempenho melhor do que os
demais programas.
Também é possível observar que existe uma pequena
diferença de desempenho entre os programas compilados em
C++ 1.0 e C++ 1.1, ambos PON.
O desempenho do programa desenvolvido em C,
utilizando o PP, perdeu para todos os programas utilizando o
PON, independente da compilação.
Esta comparação pode ser observada melhor nas Figuras 4,
5, 6 e 7.
Figura 4. Gráfico em Coluna – Até 1000
Figura 5. Gráfico em Linhas – Até 1000


Figura 6. Gráfico em Coluna – A partir de 1000
Figura 7. Gráfico em Linhas – A partir de 1000
VI.   DIFICULDADES ENCONTRADAS
Como é de se esperar em qualquer tecnologia que está em
desenvolvimento, algumas dificuldades de implementação do
algoritmo proposto foram encontradas, estas serão relatadas
neste tópico.
Uma das dificuldades encontradas foi a instabilidade do
compilador, compreensível devido à constante evolução que o
mesmo vem passando no decorrer do tempo. Devido a esta
instabilidade não foi possível gerar o código alvo para C++
2.0, pois o mesmo estava convertendo o tipo de dados de todos
os atributos para boolean, independente do tipo definido em
LingPON.
Algo semelhante ocorreu no código gerado para C, porém
como a estrutura é diferente, este problema foi contornado
manualmente no código alvo gerado.
Um ponto que gerou certo retrabalho para criar uma
solução de contorno, é o fato de que quando mais de uma
instância de uma FBE está sendo utilizada, a notificação de
regras está sendo realizada indevidamente, não observando a
instância que está sendo utilizada nas premissas. Para
contornar este problema foi necessário criar um atributo
isolado para cada instância dentro da FBE, multiplicando o
número de atributos pelo número de instâncias.
O algoritmo escolhido é melhor solucionado quando é
possível utilizar vetores, atualmente a LingPON não
possibilita a utilização de vetores de forma direta, e a
utilização de um vetor construído não foi possível devido ao
problema comentado no parágrafo anterior.
Na medida da evolução do algoritmo em LingPON,
ocorreu a tentativa de flexibilização do número de discos, esta
flexibilização foi descartada devido a um problema
encontrado, que é a impossibilidade de comparar atributos
entre si nas premissas, sendo possível apenas comparar um
atributo com um valor constante.
VII.   SUGESTÕES DE MELHORIAS
Este trabalho além de auxiliar no entendimento do PON
também foi útil para encontrar algumas dificuldades de
implementação, e com base nisso sugerir melhorias, como é
esperado deste tipo de experimento.
Com base nas dificuldades encontradas, entendo que a
LingPON poderia ser aprimorada com as seguintes melhorias:
1.
Utilização de vetores: Embora seja possível utilizar
vetores construídos, entendo que um vetor clássico
poderia auxiliar o desenvolvimento de vários
algoritmos em LingPON, como é o do caso
apresentado;
2.
Comparação entre atributos nas premissas:
Atualmente foi possível construir as premissas
comparando um atributo a uma constante, entendo
que é necessário tornar esta comparação dinâmica,
sendo necessária a comparação de valores entre
atributos de diferentes instâncias;
3.
Alterar valor de atributos de diferentes instâncias:
Atualmente um método apenas consegue alterar o
valor de atributos da própria instância em LingPON,
entendo que o fato de permitir a alteração de atributos
de diferentes instâncias através dos métodos das
FBEs tornará o a LingPON mais robusta e dinâmica.
VIII.   CONCLUSÕES
A partir do estudo realizado sobre o PON e suas
materializações através de exposição em sala de aula, e
principalmente da prática realizada, foi possível conhecer um
pouco mais deste novo paradigma.
Com base no que foi relatado neste artigo, é possível
identificar uma grande facilidade de programação em
LingPON, fácil entendimento do código gerado e também um
grande ganho de desempenho em comparação com o
paradigma imperativo.
Como é esperado de uma tecnologia em desenvolvimento,
problemas ainda são encontrados, e através deles surgem
sugestões de melhorias.
Entendo que este trabalho pôde contribuir para o
desenvolvimento do paradigma, principalmente no que tange
sua materialização em LingPON.
REFERENCES
[1]  Robson Ribeiro Linhares, Jean Marcelo Simão e Paulo Cézar Stadzisz.
Arquitetura de Computador Orientada a Notificações – ARQPON.
Pedido de Patente. INPI, 2014.


[2] 
Jean Marcelo Simão e Paulo Cézar Stadzisz. Paradigma Orientado a
Notificações (PON) – Uma Técnica de Composição e Execução de
Software Orientado a Notificações. Pedido de Patente. INPI, 2008.
[3]  Robson Duarte Xavier. Paradigmas de Desenvolvimento de Software:
Comparação entre Abordagens Orientada a Eventos e Orientada a
Notificações. Dissertação de Mestrado, PPGCA/UTFPR. Curitiba, 2014.
Disponível
 
em:
http://repositorio.utfpr.edu.br/jspui/bitstream/1/1006/1/CT_PPGCA_M_
Xavier%2c%20Robson%20Duarte_2014.pdf.
[4]  Roni Fabio Banaszewski. Paradigma Orientado a Notificações: Avanços 
e Comparações. Dissertação de Mestrado, CPGEI/UTFPR. Curitiba, 
2009. Disponível em:  http://files.dirppg.ct.utfpr.edu.br/cpgei/Ano_2009/
dissertacoes/Dissertacao_500_2009.pdf.
[5]  Leonardo Faix Pordeus. Notification Oriented Paradigm (NOP): CTA
Simulator. Curitiba, 2015.
[6]  Cleverson Avelino Ferreira. Linguagem e Compilador para o Paradigma
Orientado a Notificações (PON): Avanços e Comparações. Dissertação
de Mestrado, PPGCA/UTFPR. Curitiba, 2015. Disponível em:
http://repositorio.utfpr.edu.br/jspui/bitstream/1/1414/1/CT_PPGCA_M_
Ferreira%2c%20Cleverson%20Avelino_2015.pdf.
[7]  Torres
 
de
 
Hanói.
 
Disponível
 
em:
https://pt.khanacademy.org/computing/computer-
science/algorithms/towers-of-hanoi/a/towers-of-hanoi 
Acessado em
Maio de 2016.


Um estudo comparativo entre o paradigma
orientado a notiﬁcac¸˜oes (PON) e o paradigma
orientado a objetos (OO) aplicado em um problema
de uma cidade virtual
Frederico Severo Miranda
CPGEI / UTFPR
Avenida Sete de Setembro, 3165
Curitiba-PR - CEP 80.230-910
E-mail: fdr.miranda@gmail.com
Resumo—Qual paradigma utilizar para processar informac¸˜oes
de um Web Service especialista em condic¸˜oes clim´aticas e ent˜ao
reproduzir a iluminac¸˜ao do ambiente de uma cidade real em uma
cidade virtual visando o menor tempo de processamento?
No ˆambito de responder a esta pergunta, uma soluc¸˜ao ´e
implementar algoritmos levando em conta o paradigma vigente
(OO) e um novo paradigma conhecido como paradigma orientado
a notiﬁcac¸˜oes (PON). Desta forma, ´e poss´ıvel compar´a-los para
descobrir qual paradigma ´e o mais eﬁciente.
Como resultado, seis algoritmos foram implementados bem
como uma bateria de testes foram realizadas com o objetivo de
avaliar o desempenho dos mesmos.
Com o desempenho dos algoritmos avaliados, conclui-se que
o algoritmo implementado com o conceito PON apresentou um
desempenho extremamente satisfat´orio sendo superado apenas
por um algoritmo dentre os seis implementados. O PON surge
como um novo conceito que obriga o desenvolvedor a mudar
sua maneira de pensar em como implementar softwares e que
se tiver esforc¸os concentrados poder´a constituir em um futuro
pr´oximo um novo patamar.
Keywords—Cidades Virtuais, Cidades Inteligentes, Cidades
Digitais, TIC, Programac¸˜ao Orientada a Notiﬁcac¸˜oes (PON).
I. INTRODUC¸ ˜AO
A Tecnologia da Informac¸˜ao e Comunicac¸˜ao (TIC) est´a pre-
sente na vida di´aria da sociedade. Ela tem sido utilizada no tra-
balho, nos relacionamentos, servic¸os p´ublicos, entretenimento
e lazer com o objetivo de superar a exclus˜ao social, melhorar
o desempenho econˆomico, criar oportunidades de emprego,
melhorar a qualidade de vida e promover a participac¸˜ao social
[1].
A TIC possibilitou a criac¸˜ao de v´arias aplicac¸˜oes inovadoras
que tornam a vida mais f´acil [2]. Mas atualmente n˜ao foram
encontradas plataformas computacionais com o objetivo de
centralizar e integrar aplicac¸˜oes voltadas `a populac¸˜ao envol-
vendo aspectos de car´ater social, governamental, comercial,
educacional, cient´ıﬁco e entretenimento que s˜ao associadas ao
ambiente f´ısico de vivˆencia (i.e., a cidade) das pessoas. Este
problema ´e observado na condic¸˜ao atual na qual s˜ao oferecidas
aplicac¸˜oes em diferentes formatos e prop´ositos para atender a
diversidade das demandas da sociedade, como as cidades digi-
tais, cidades inteligentes, software de entretenimento, m´ıdias
sociais, lojas eletrˆonicas e sites de busca, mas que praticamente
n˜ao se relacionam entre si e n˜ao tˆem v´ınculo regional (n˜ao se
associam com o ambiente de vivˆencia das pessoas). Diante
deste contexto, vislumbra-se uma cidade virtual que deve
reproduzir alguns aspectos do mundo real, como por exemplo,
as condic¸˜oes clim´aticas e iluminac¸˜ao ambiente.
Com a utilizac¸˜ao de Web Services especialistas ´e poss´ıvel
obter informac¸˜oes sobre as condic¸˜oes clim´aticas e ent˜ao re-
produzir a iluminac¸˜ao ambiente da cidade real. O problema
que existe neste cen´ario trata-se em como processar estas
informac¸˜oes da maneira mais r´apida poss´ıvel.
Diante deste fato, uma poss´ıvel soluc¸˜ao ´e implementar
algoritmos levando em conta o paradigma vigente (OO) e
um novo paradigma conhecido como programac¸˜ao orien-
tada a notiﬁcac¸˜oes (PON) e assim compar´a-los levando em
considerac¸˜ao o tempo de processamento.
Como resultado, s˜ao apresentados seis algoritmos para
resolver este problema de processamento das informac¸˜oes
advindas do Web Service. Al´em dos seis algoritmos e devido
a busca por otimizac¸˜ao, foi aprimorado o framework NOP C#
1.0 gerando assim o novo framework NOP C# 1.1.
O algoritmo implementado com o conceito do PON
mostrou-se eﬁciente para resolver o problema sobre condic¸˜oes
clim´aticas perdendo em tempo de processamento apenas para
um algoritmo dentre os seis implementados.
II. REVIS ˜AO DA LITERATURA
Esta sec¸˜ao ir´a abordar dois assuntos distintos para uma me-
lhor compreens˜ao da problem´atica envolvida. O primeiro ir´a
abordar a tem´atica referente a cidades virtuais, cidades digitais
e cidades inteligentes e o segundo ir´a abordar conceitos sobre
o paradigma orientado a notiﬁcac¸˜oes.
A. Cidades virtuais, cidades inteligentes e cidades digitais
Uma das criac¸˜oes mais importante e poderosa da humani-
dade foi a Internet. Pessoas, sistemas e “coisas” est˜ao conecta-
dos entre si com a possibilidade de compartilhar informac¸˜oes.


Algumas estimativas sugerem que em 2020, 50 bilh˜oes de re-
cursos estar˜ao conectados na internet [3]. O F´orum Econˆomico
Mundial acredita que esta hiperconectividade ir´a trazer um alto
impacto no futuro e considera que estamos vivendo em um
“mundo hiperconectado” [4]. Esta conectividade possibilita a
criac¸˜ao de novos produtos e servic¸os para melhorar a vida das
pessoas [5]. A conectividade possibilitou o avanc¸o em diversas
´areas de pesquisa, como por exemplo, o desenvolvimento das
cidades virtuais, cidades inteligentes e cidades digitais.
1) Cidades virtuais: Tecnologias tridimensionais (3D) tˆem
sido recentemente introduzidas em diferentes aplicac¸˜oes e
´areas tais como ambientes virtuais (mundo virtual/cidade vir-
tual), realidade aumentada, computac¸˜ao desktop, sistemas para
´area de sa´ude, jogos 3D, tele-operac¸˜ao e computac¸˜ao ub´ıqua
[6]. Cidades virtuais possuem v´arias deﬁnic¸˜oes, mas neste
artigo ser´a considerada como um ambiente tridimensional que
reconstr´oi uma estrutura espacial complexa de uma cidade no
computador e que pode ser utilizada para diversos ﬁns: pla-
nejamento urbano, gerenciamento de redes wireless, turismo
virtual, simulac¸˜ao de tr´afego, simulac¸˜ao de ambiente [7]. As
cidades virtuais para prop´ositos s´erios est˜ao se tornando cada
vez mais difundidas, isso ocorre pelo fato de suportarem uma
ampla gama de atividades que podem ser executadas. Estas
atividades s˜ao oriundas de diversas ´areas como educac¸˜ao,
entretenimento e socializac¸˜ao [8]. Apesar das advertˆencias
sobre o aumento da dependˆencia dos seres humanos com a
tecnologia, pesquisadores ainda preveem que em 2018 as cida-
des virtuais ser˜ao consideradas como a principal plataforma de
neg´ocios e oportunidades [9]. A ﬁgura 1 mostra um exemplo
de uma cidade virtual.
Figura 1.
Exemplo de uma cidade virtual.
2) Cidades inteligentes: Foi publicado pelas Nac¸˜oes Unidas
um relat´orio sobre a migrac¸˜ao de pessoas das ´areas rurais
para as ´areas urbanas. Este relat´orio mostra que em 1950
30% da populac¸˜ao mundial viviam em ´areas urbanas, em 2014
este n´umero sobe para 54% e em 2050 existe a previs˜ao de
que 66% da populac¸˜ao mundial estar´a vivendo nas cidades
[10]. As cidades constituem o principal local da realizac¸˜ao
de atividade humana e econˆomica, que fornecem aos seus
habitantes uma grande oportunidade de desenvolvimento. En-
tretanto, `a medida que crescem em tamanho e complexidade,
surge uma diversidade de problemas que podem ser dif´ıceis
de serem solucionados. O gerenciamento das ´areas urbanas
se faz necess´ario para suportar a competitividade econˆomica,
simultaneamente deve reforc¸ar a coes˜ao social e ambiental e
neste sentido aumentar a qualidade de vida da sua populac¸˜ao
[11]. Com o avanc¸o das TICs, surge o conceito de “Cidades
Inteligentes” como uma soluc¸˜ao para resolver problemas das
´areas urbanas [12]. Este conceito surgiu pela primeira vez
em 1990 e muitos pesquisadores tˆem enfatizado a tecnologia,
inovac¸˜ao e globalizac¸˜ao no processo de urbanizac¸˜ao [13]. As
cidades inteligentes possuem uma deﬁnic¸˜ao abrangente que
considera diversos fatores, mas sempre ´e associada com a
interconex˜ao entre fatores humano-sociais com a TIC [14].
Tamb´em pode ser deﬁnida como a integrac¸˜ao entre a infraes-
trutura tecnol´ogica e f´ısica para melhorar o desenvolvimento
econˆomico, pol´ıtico, social e urbano [15]. Assim sendo, a
tecnologia, comunicac¸˜ao e as rotinas di´arias das pessoas
coexistem em um mesmo ambiente [16]. A Figura 2 aborda
as 6 ´areas de atuac¸˜ao de uma cidade inteligente.
Figura 2. As principais ´areas de atuac¸˜ao de uma cidade inteligente. Adaptado
de [17].
Com a ind´ustria de TIC, ´e poss´ıvel incorporar sistemas e
sensores wireless que coletam informac¸˜oes e colaboram entre
si para ajudar os usu´arios em um objetivo espec´ıﬁco [18].
Como exemplo, podemos considerar uma aplicac¸˜ao no tr´afego
urbano, onde os carros coletam dados atrav´es de GPS, cˆameras
e outros sensores e enviam estas informac¸˜oes a outros carros
que est˜ao em quadras pr´oximas, informando assim um poss´ıvel
congestionamento [12].
3) Cidades
digitais:
Os
constantes
desaﬁos
sociais,
pol´ıticos e ﬁnanceiros enfrentados pelas cidades tˆem exigido
dos seus gestores uma busca por soluc¸˜oes inovadoras para
melhorar a qualidade de vidas da populac¸˜ao [19]. Os avanc¸os
na ind´ustria de TIC tem alterado o modo como gestores
p´ublicos e a populac¸˜ao interagem entre si, possibilitando a
criac¸˜ao de portais p´ublicos [20]. Estes portais WEB fazem
parte de um termo que envolve uma s´erie de deﬁnic¸˜oes e


caracter´ısticas conhecido como “Cidades Digitais”. Cidade
Digital ´e a uni˜ao entre aplicac¸˜oes WEB que melhoram a
qualidade de vida dos cidad˜aos e uma infraestrutura f´ısica que
suporta estas aplicac¸˜oes [21].
A Figura 3 mostra a composic¸˜ao de uma cidade digital.
Figura 3.
Composic¸˜ao de uma cidade digital.
Estas aplicac¸˜oes podem ser vistas como servic¸os WEB
[22] que conectam departamentos p´ublicos, empresas, escolas,
comunidades, organizac¸˜oes [23] com o objetivo de oferecer
servic¸os p´ublicos de qualidade para a populac¸˜ao (servic¸os ﬁs-
cais, servic¸os de sa´ude, servic¸os de pol´ıcia), servic¸os p´ublicos
para empresas, servic¸os de informac¸˜ao (condic¸˜oes clim´aticas,
informac¸˜ao geogr´aﬁca, tr´afego), servic¸os de entretenimento
(jogos, turismo) e servic¸os relacionados a recursos humanos
[24]. A cidade virtual tamb´em deve possuir uma infraestrutura
f´ısica para permitir que a inclus˜ao digital e interac¸˜oes sejam
poss´ıveis [25], como por exemplo, os telecentros que disponi-
bilizam Internet para uso gratuito e a construc¸˜ao de redes de
ﬁbra ´otica para interligar ´org˜aos p´ublicos [26].
B. Paradigma orientado a notiﬁcac¸˜oes - PON
Em linhas gerais, o Paradigma Orientado a Notiﬁcac¸˜oes
(PON) se prop˜oe a resolver certos problemas existentes nos pa-
radigmas usuais de programac¸˜ao, nomeadamente o Paradigma
Declarativo (PD) e o Paradigma Imperativo (PI). Na verdade, o
PON uniﬁca as principais caracter´ısticas e as vantagens do PD
(e.g. representac¸˜ao do conhecimento em regras) e do PI (e.g.
ﬂexibilidade de express˜ao e n´ıvel apropriado de abstrac¸˜ao).
Ademais, o PON supostamente resolve, j´a em termos de
modelo, v´arias das deﬁciˆencias e inconvenientes de PI e PD em
aplicac¸˜oes de software e mesmo de hardware, possivelmente
desde ambientes monoprocessados a completamente multipro-
cessados - copiado de [27].
De fato, o PON permite desacoplar express˜oes causais do
c´odigo-fonte, ao considerar cada uma destas e seus fatos
relacionados como entidades computacionais, as quais s˜ao
objetos nas atuais implementac¸˜oes em software e m´odulo de
circuito nas atuais implementac¸˜oes em hardware. Estas entida-
des s˜ao notiﬁcantes, permitindo assim uma escalabilidade de
desempenho em ambientes de processamento paralelo ou n˜ao,
bem como melhor aproveitamento de recursos em ambiente
distribu´ıdo, tanto em implementac¸˜oes de software quanto de
hardware - copiado de [27].
Particularmente no tocante a software, isto ´e diferente dos
programas usuais do PI (salientando os Orientados a Objetos
- OO) e do PD (salientado os chamados Sistemas Baseados
em Regras - SBR). Nestes, as express˜oes causais s˜ao passivas
e acopladas (sen˜ao fortemente acopladas) a outras partes do
c´odigo, al´em de haver algum ou mesmo muito desperd´ıcio de
processamento, conforme o caso - copiado de [27].
Acredita-se que o PON ainda pode evoluir, a luz do seu
c´alculo assint´otico, no tocante a quest˜oes de desempenho.
Ainda, vislumbra-se tamb´em a evoluc¸˜ao do PON no tocante
`a facilidade de programac¸˜ao. Com a linguagem PON (deno-
minada doravante “LingPon”) e seu compilador (denominado
doravante “compilador PON”), torna-se poss´ıvel desenvolver
aplicac¸˜oes espec´ıﬁcas em uma linguagem conformada ao PON
e gerar resultados, em termos de c´odigo, sem a adic¸˜ao de
estruturas de dados caras - copiado de [27].
III. MEDOTOLOGIA
Para resolver o problema da iluminac¸˜ao na cidade virtual,
foram adotados trˆes atributos que s˜ao obtidos atrav´es do Web
Service de condic¸˜oes clim´aticas:
• Weather: CLEAN, RAIN, MOSTLY CLOUD etc. (S˜ao
16 poss´ıveis valores).
• Hour: valores inteiros entre 0 e 23.
• Visibility: valores inteiros entre 0 e 10.
Em seguida foram mapeadas todas as combinac¸˜oes poss´ıveis
conforme ﬁgura 4. Assim, s˜ao criados 4224 (16*24*11)
cen´arios/regras e cada um associado com um resultado es-
pec´ıﬁco.
Figura 4.
Combinac¸˜oes entre os atributos Weather (1a coluna), Hour (2a
coluna) e Visibility (3a coluna). Neste exemplo est´a sendo mostrado apenas
o Weather CLEAN, mas devem ser consideradas todas as 16 possibilidades.
A 4a coluna (cor verde) representa o resultado espec´ıﬁco para cada regra.


Para o estudo comparativo proposto foram implementados
seis algoritmos nomeados da seguinte forma C#, C#Otim,
C#OtimV2, C#Pon, C#Pon1.1 e C#Pon1.1Hash.
A. C#
O algoritmo representado pela ﬁgura 5 foi implementado
sem utilizar as melhores pr´aticas em programac¸˜ao, pois o
objetivo principal era codiﬁcar da forma mais r´apida poss´ıvel.
Neste contexto temos um algoritmo que sempre avalia todas
as regras para qualquer entrada avaliada.
Figura 5.
Este algoritmo SEMPRE ir´a avaliar todas as regras. OBS: apenas
algumas linhas de c´odigos s˜ao exibidas, mas devem ser consideradas as 4224
regras
B. C#Otim
O algoritmo descrito na ﬁgura 6 foi implementado otimi-
zando o algoritmo C#. Desta forma, um melhor tratamento
de string´s foi realizado e quando uma determinada regra ´e
encontrada, o algoritmo interrompe sua execuc¸˜ao.
Figura 6.
Este algoritmo ﬁnaliza sua execuc¸˜ao quando uma regra ´e
encontrada. OBS: apenas algumas linhas de c´odigos s˜ao exibidas, mas devem
ser consideradas as 4224 regras.
C. C#OtimV2
O algoritmo descrito na ﬁgura 7 foi implementado utili-
zando o conceito de SWITCH CASE. Desta forma, indepen-
dente do cen´ario a ser avaliado, o mesmo ser´a encontrado
pontualmente.
D. C#PON
O algoritmo visualizado na ﬁgura 8 foi implementado
utilizando o paradigma orientado a notiﬁcac¸˜oes (PON) com
o uso do framework NOP C# 1.0.
Figura 7.
Este algoritmo encontra pontualmente o cen´ario avaliado, maxi-
mizando assim seu tempo de processamento. OBS: apenas algumas linhas de
c´odigos s˜ao exibidas, mas devem ser consideradas as 4224 regras.
Figura 8.
Algoritmo implementado com o conceito PON. OBS: Apenas
algumas linhas de c´odigos s˜ao exibidas, mas devem ser consideradas as 4224
regras.
E. C#PON1.1
O algoritmo representado pela ﬁgura 9 foi implementado
utilizando o paradigma orientado a notiﬁcac¸˜oes (PON) com
algumas alterac¸˜oes em sua modelagem. Neste contexto, todas
as premissas foram criadas uma ´unica vez evitando assim
redundˆancia estrutural.
Figura 9.
Devem ser consideradas a criac¸˜ao de 16 premissas Weather, 24
premissas do tipo Hour e por ﬁm 11 premissas do tipo Visibility. OBS: apenas
algumas linhas de c´odigos s˜ao exibidas, mas devem ser consideradas as 4224
regras.
Para este algoritmo, algumas alterac¸˜oes tamb´em foram
realizadas no framework NOP C# 1.0: melhor comparac¸˜ao
de string’s, alterac¸˜oes de comandos foreach e alterac¸˜ao de
comandos if...else. Todas estas alterac¸˜oes pontuais resultaram
em uma melhor performance do algoritmo levando em conta
seu tempo de execuc¸˜ao.
• Comparac¸˜ao de string´s: alterado conforme ﬁgura 10.


• Foreach: alterado alguns comandos foreach para o tradi-
cional comando for.
• if...else: alterado conforme ﬁgura 11.
Figura 10.
Melhor desempenho na forma de comparar string´s.
Figura 11.
Melhor desempenho para um cen´ario espec´ıﬁco do comando if.
F. C#PON1.1Hash
Este algoritmo utiliza o mesmo c´odigo do algoritmo
C#PON1.1. A diferenc¸a ´e que sua estrutura de dados ´e baseada
em HASH. Desta forma as alterac¸˜oes nos valores dos atributos
notiﬁcam exatamente as premissas que interessam.
Todos os seis algoritmos foram submetidos a uma bateria de
testes e executados (modo seguranc¸a) no sistema operacional
Windows 7 Home Premium 64-bit (AMD 4300 Quad-Core
3.8Ghz, 8 GB RAN). A bateria de testes ´e composta pelos
seguintes cen´arios: Test1, Test100, Test200, Test300, Test500,
Test600, Test700, Test800, Test900, Test1k, Test5k, Test6k,
Test7k, Test8k, Test10K.
Como exemplo, a leitura de cada teste se faz da seguinte
maneira (o mesmo racioc´ınio deve ser aplicado a todos os
outros testes):
• Test1: possui 5 arquivos com registros aleat´orios con-
tendo 1 registro.
• Test100: possui 5 arquivos com registros aleat´orios con-
tendo 100 registros.
• Test5k: possui 5 arquivos com registros aleat´orios con-
tendo 5000 registros.
• TestX: possui 5 arquivos com registros aleat´orios con-
tendo X registros.
Um exemplo de arquivo utilizado ´e mostrado na ﬁgura 12.
Cada um dos seis algoritmos (um por vez) foi executado
levando em conta como entrada os arquivos da bateria de
teste e ent˜ao o tempo de processamento foi anotado. Como
exemplo, ´e descrito a seguir o teste realizado com a bateria
Test100. Conforme dito anteriormente, todas as baterias pos-
suem cinco arquivos com registros aleat´orios, neste sentido,
os algoritmos C#, C#Otim, C#OtimV2, C#Pon, C#Pon1.1 e
C#Pon1.1Hash processam o primeiro arquivo que pertence ao
Figura 12.
Exemplo de arquivo utilizado.
Test100 e o tempo de execuc¸˜ao ´e anotado. Em seguida, os
mesmos processam o segundo arquivo e o tempo de execuc¸˜ao
´e anotado. Este processo continua at´e o quinto arquivo. O
mesmo racioc´ınio ´e aplicado a todas as baterias de testes.
IV. RESULTADOS
Este artigo apresenta como resultado um estudo comparativo
entre seis algoritmos, sendo que trˆes (C#Pon, C#Pon1.1 e
C#Pon1.1Hash) utilizam o paradigma orientado a notiﬁcac¸˜oes
(PON) e os outros trˆes (C#, C#Otim e C#OtimV2) utilizam o
paradigma orientado a objetos (OO).
A m´edia do tempo de execuc¸˜ao de cada algoritmo s˜ao
evidenciados conforme as tabelas I e II.
Tabela I
M´EDIA DO TEMPO DE EXECUC¸ ˜AO (EM SEGUNDOS) DOS ALGORITMOS.
Tabela II
M´EDIA DO TEMPO DE EXECUC¸ ˜AO (EM SEGUNDOS) DOS ALGORITMOS.
A representac¸˜ao do comportamento dos valores das tabelas I
e II podem ser visualizados na ﬁgura 13. Para uma melhor
visualizac¸˜ao deste comportamento apenas os melhores resul-
tados ser˜ao visualizados na ﬁgura 14.
Al´em do estudo comparativo, otimizac¸˜oes pontuais foram
realizadas no framework NOP C# 1.0. Estas otimizac¸˜oes se
referem a uma melhor comparac¸˜ao entre string´s, substituic¸˜ao
de alguns comandos foreach por for e um aprimoramento em
alguns blocos de comandos if...else. O framework NOP C#
1.0 foi evolu´ıdo para o framework NOP C# 1.1 de tal forma
que agora ´e poss´ıvel utilizar a estrutura de dados Hash para
notiﬁcar as premissas do PON.


Figura 13.
Comportamento do tempo de execuc¸˜ao dos algoritmos.
Figura 14.
Comportamento do tempo de execuc¸˜ao dos algoritmos.
V. CONCLUS ˜AO
Uma das soluc¸˜oes poss´ıveis para reproduzir a iluminac¸˜ao
ambiente de uma cidade real em uma cidade virtual ´e a
utilizac¸˜ao de Web Services especialistas. Um problema que
ocorre seria o tempo de processamento destas informac¸˜oes.
Diante deste fato, ´e proposto a implementac¸˜ao de 6 algorit-
mos para que os mesmos pudessem ser comparados levando
em conta o tempo de execuc¸˜ao.
Seis algoritmos s˜ao apresentados como resultado para re-
solver o problema de processamento das informac¸˜oes sobre
condic¸˜oes clim´aticas.
Comparando o desempenho dos seis algoritmos conclui-se
que o paradigma C#Pon1.1 apresenta um desempenho satis-
fat´orio sendo superado apenas por um algoritmo dentre os seis
implementados. A utilizac¸˜ao do PON em relac¸˜ao a codiﬁcac¸˜ao
´e simples, bastando apenas importar uma Dynamic-link library
(DLL) e ent˜ao utilizar seus recursos dispon´ıveis. A ideia por
tr´as da programac¸˜ao orientada a notiﬁcac¸˜oes (PON) obriga
o desenvolvedor a mudar sua maneira de pensar em como
codiﬁcar e que se tiver esforc¸os concentrados neste paradigma
pode-se tornar uma nova forma de desenvolver softwares.
Uma das desvantagens na utilizac¸˜ao do PON ´e quantidade
de linhas de c´odigo que s˜ao geradas em relac¸˜ao a outros
paradigmas, mas esta desvantagem n˜ao sobrep˜oe os benef´ıcios
disponibilizados pelo PON.
VI. TRABALHOS FUTUROS
Implementar um wizard para que seja poss´ıvel diminuir o
esforc¸o na gerac¸˜ao das regras do PON e buscar novas soluc¸˜oes
para processar as informac¸˜oes sobre condic¸˜oes clim´aticas e
ent˜ao comparar seu desempenho com os algoritmos imple-
mentados.
REFERˆENCIAS
[1] A. Grguric, S. Desic, M. Mosmondor, I. Benc, J. Krizanic, and P. La-
zarevski, “Proof-of-concept applications for validation of ICT services
for elderly care,” MIPRO, 2010 Proceedings of the 33rd International
Convention, pp. 355–359, 2010.
[2] K. S. Nwizege, F. Chukwunonso, C. Kpabeb, and S. Mmeah, “The
impact of ICT on computer applications,” Proceedings - UKSim 5th Eu-
ropean Modelling Symposium on Computer Modelling and Simulation,
EMS 2011, pp. 435–439, 2011.
[3] D. Evans, “The Internet of Things - How the Next Evolution of the
Internet is Changing Everything,” CISCO white paper, no. April, pp.
1–11, 2011.
[4] W. E. Forum, G. A. Council, and C. Systems, “Perspectives on a
Hyperconnected World,” no. January, 2013.
[5] I. Thomas, L. Fedon, A. Jara, and Y. Bocchi, “Towards a Human Centric
Intelligent Society: Using Cloud and the Web of Everything to Facilitate
New Social Infrastructures,” 9th International Conference on Innovative
Mobile and Internet Services in Ubiquitous Computing, pp. 319–324,
2015.
[6] E. Lombardo, Virtual, Augmented and Mixed Reality: Designing and
Developing Augmented and Virtual Environments, S. E. Shumaker,
Randall, Lackey, Ed.
Springer, 2014.
[7] J. D¨ollner, H. Buchholz, M. Nienhaus, and F. Kirsch, “Illustrative
Visualization of 3D City Models,” Visualization and Data Analysis, vol.
5669, no. c, pp. 42–51, 2005.
[8] M. Fominykh, E. Prasolova-Forland, M. Morozov, A. Gerasimov, F. Bel-
lotti, R. Berta, S. Cardona, and A. De Gloria, “Universcity: Towards
a holistic approach to educational virtual city design,” 2010 16th
International Conference on Virtual Systems and Multimedia, VSMM
2010, pp. 371–374, 2010.
[9] A. Hardin, J. Nicholson, A. Krishen, and D. Nicholson, “Virtual world
entrepreneurship,” Proceedings of the Annual Hawaii International
Conference on System Sciences, pp. 4315–4322, 2013.
[10] U. Nations, World Urbanization Prospects: The 2014 Revision, High-
lights (ST/ESA/SER.A/352), 2014.
[11] A. Monzon, “Smart Cities and Green ICT Systems (SMARTGREENS),
2015 International Conference on,” Smart Cities and Green ICT Systems
(SMARTGREENS), 2015 International Conference on, pp. 1–11, 2015.
[12] Y. Chuantao, X. Zhang, C. Hui, W. Jingyuan, C. Daven, and D. Bertrand,
“A literature survey on smart cities,” Sci China Inf Sci, vol. 58, no. 5818,
pp. 1–18, 2015.
[13] R. W. SMILOR, THE TECHNOPOLIS PHENOMENON, R. &. LIT-
TLEFIELD, Ed.
Rowman & Littleﬁeld Publishers, 1992.
[14] A. Caragliu, C. D Bo, K. Kourtit, and P. Nijkamp, Smart Cities, second
edi ed.
Elsevier, 2015, vol. 22.
[15] K. Layne and J. Lee, “Developing fully functional E-government: A
four stage model,” Government Information Quarterly, vol. 18, no. 2,
pp. 122–136, 2001.
[16] G. Piro, I. Cianci, L. A. Grieco, G. Boggia, and P. Camarda, “Informa-
tion centric services in Smart Cities,” Journal of Systems and Software,
vol. 88, no. 1, pp. 169–188, 2014.
[17] R. Gifﬁnger, C. Fertner, H. Kramar, R. Kalasek, N. Pichler, and
E. Meijers, “Smart cities: Ranking of European medium-sized cities,”
Tech. Rep. October, 2007.
[18] B. Mattoni, F. Gugliermetti, and F. Bisegna, “A multilevel method
to assess and design the renovation and integration of Smart Cities,”
Sustainable Cities and Society, vol. 15, pp. 105–119, 2015.


[19] D. A. Rezende, G. D. S. Madeira, L. D. S. Mendes, G. D. Breda, B. B.
Zarpel˜ao, and F. D. C. Figueiredo, “Information and telecommunications
project for a digital City: A Brazilian case study,” Telematics and
Informatics, vol. 31, no. 1, pp. 98–114, 2014.
[20] B. W. Wirtz and O. T. Kurtz, “Local e-government and user satisfaction
with city portals - the citizens service preference perspective,” Interna-
tional Review on Public and Nonproﬁt Marketing, 2016.
[21] G. S. Yovanof and G. N. Hazapis, “An architectural framework and
enabling wireless technologies for digital cities & Intelligent urban
environments,” Wireless Personal Communications, vol. 49, no. 3, pp.
445–463, 2009.
[22] L. S. Mendes, M. L. Bottoli, and G. D. Breda, “Digital cities and open
MANs: a new communications paradigm,” 2009 IEEE Latin-American
Conference on Communications, LATINCOM ’09 - Conference Procee-
dings, pp. 1–8, 2009.
[23] E. P. GUERREIRO, Cidade digital - Infoinclus˜ao social e tecnologia
em rede, 1st ed., Senac S˜ao Paulo, Ed.
Senac S˜ao Paulo, 2006.
[24] D. Zhu, Y. Li, J. Shi, Y. Xu, and W. Shen, “A service-oriented city
portal framework and collaborative development platform,” Information
Sciences, vol. 179, no. 15, pp. 2606–2617, 2009.
[25] F. Duarte, F. de Carvalho Figueiredo, L. Leite, and D. Alcides Rezende,
“A Conceptual Framework for Assessing Digital Cities and the Brazilian
Index of Digital Cities: Analysis of Curitiba, the First-Ranked City,”
Journal of Urban Technology, vol. 21, no. 3, pp. 37–48, 2014.
[26] Minist´erio das Comunicac¸˜oes, “Cidades Digitais,” 2014. [Online].
Available: http://www.mc.gov.br/cidades-digitais
[27] C. A. Ferreira, “LINGUAGEM E COMPILADOR PARA O PARA-
DIGMA ORIENTADO A NOTIFICAC¸ ˜OES ( PON ): AVANC¸ OS E
COMPARAC¸ ˜OES ,” p. 245, 2015.


254
ANEXO D -- RELAT´ORIO DA DISCIPLINA
LINGUAGENS/COMPILADORES - 2015
Este anexo apresenta o relat´orio apresentado pelos alunos Leonardo Pordeus,
Fernando Schutz, Leonardo Santos e Ricardo Kerschbaumer como trabalho ﬁnal da
disciplina “Linguagens e Compiladores” ofertada pela UTFPR em 2015 e ministrada por
Prof. Dr. Jo˜ao Alberto Fabro e Prof. Dr. Jean Marcelo Sim˜ao.


Introdução 
 
 
O Paradigma Orientado a Notificações (PON) é uma nova abordagem 
para o desenvolvimento de sistemas computacionais de maneira mais eficiente 
quando comparado a sistemas baseados em paradigmas tradicionais, como a 
Programação Procedimental e a Programação Orientada a Objetos (POO) do 
Paradigma Imperativo (PI), assim como os Sistemas baseados em Regras 
(SBR) 
do 
paradigma 
declarativo 
(PD) 
(SIMÃO; 
STADZISZ, 
2008) 
(BANASZEWSKI, 2009). 
O PON propõe uma solução para os problemas destes paradigmas, que 
apresentam deficiências com relação a redundâncias estruturais, temporais e 
forte acoplamento entre suas entidades, diminuindo o desempenho e gerando 
maior dificuldade de paralelização e distribuição. Tais vantagens são 
constituídas por uma maior facilidade na concepção de sistemas que 
apresentem paralelismo ou distribuição, além da redução ou eliminação de 
alguns dos problemas clássicos de software PI e PD, tais como redundâncias 
de execução e acoplamento excessivo entre entidades computacionais 
(SIMÃO; STADZISZ, 2008) (BANASZEWSKI, 2009). 
Para o desenvolvimento de softwares fazendo uso do PON, 
primeiramente 
foram 
realizadas 
pesquisas 
com 
framework 
C++ 
(BANASZEWSKI, 2009) e uma segunda versão otimizada do framework C++ 
(RONSZCKA, 2012), permitindo a criação de softwares PON sob abordagem 
de POO. Porém nessas abordagens há um elevado uso de estruturas de 
dados, como lists, vectors, hashs, entre outras, que degradam o desempenho 
das aplicações construídas sobre o conceito do PON. Assim, observou-se a 
necessidade de desenvolvimento de um compilador e de uma linguagem 
específica para o PON, denominada LingPon. 
Outras pesquisas também exploraram a implementação do PON em 
hardware com uso de lógica reconfigurável (SIMÃO et al, 2012)  seguindo os 
conceitos do PON. Peters (2012) propôs a implementação em lógica 


reconfigurável de um co-processador PON (CoPON), uma solução híbrida, na 
qual a parte da aplicação responsável pelo processamento factual é executada 
em um núcleo von Neumann e  a parte da aplicação responsável pelo cálculo 
lógico-causal e propagação de notificações é executada por meio de um co-
processador baseado nos princípios do PON. Outrossim, uma arquitetura de 
processador foi desenvolvida de acordo com o modelo do PON, sendo 
denominada 
Notification-Oriented 
Computer 
Architecture 
(NOCA) 
(LINHARES,2015). 
O trabalho da disciplina de linguagens e compiladores teve como 
objetivo dar continuidade a linguagem LingPon. A primeira versão do LingPon 
foi materializada na disciplina Linguagens e Compiladores no ano de 2014 e 
aprimorada por (FERREIRA, 2015) em sua dissertação de mestrado. Em sua 
primeira versão foi concebida uma gramática própria, definida por uma BNF 
(Backus Normal Form) e com as ferramentas flex e bison. A Figura  apresenta 
um diagrama de blocos da estrutura da primeira versão do compilador. Na qual, 
é composto por um código escrito na linguagem LingPon, que representa a 
aplicação, o compilador e três possíveis códigos intermediários (C, C++ e 
Framework). 
 
Figura  – Diagrama de Blocos LingPon 


Para a disciplina Linguagens e Compiladores de 2015 foram 
acrescentadas novas funcionalidades à linguagem, como regras de formação, 
compilação para Notification Oriented Computer Architecture (NOCA) 
(LINHARES, 2015), VHDL e uma nova versão C++, na qual é gerado um 
código seguindo os conceitos do PON de forma estática. 
Linguagem Atual 
 
a) Pré Requisitos e Instalação 
Para o desenvolvimento do compilador é necessário instalar 
previamente os analisadores léxicos e semânticos, que são as ferramentas 
Flex/Lex e Bison. Para a sua compilação também é necessário configurar o 
compilador g++. No Windows o compilador pode ser configurado através da 
ferramenta cygwin (https://cygwin.com/install.html) (Tutorial de instalação do 
cygwin: 
http://cs.calvin.edu/curriculum/cs/112/resources/installingEclipse/cygwin/ 
Marcar a opção de instalação do Flex e Bison). 
Não existe no momento um instalador do compilador. Para sua 
utilização é necessário primeiramente, realizar o check-out do projeto no 
servidor 
svn 
disponível 
no 
seguinte 
endereço 
(https://200.134.17.9/svn/NOP/NOP_Compilador/NOP_v2015/). Após realizar o 
check-out do projeto é necessário seguir o processo abaixo (no Windows, 
através do cygwin) para realizar a sua compilação. 
flex lex_pon.l 
bison -d bison_pon.y 
g++ lex.yy.c bison_pon.tab.c *.cpp -o pon 
 
b) Linguagem PON 
A linguagem PON pode ser dividida em cinco partes, sendo: 


 Declaração de FBE´s; 
 Instâncias das FBE´s; 
 Estratégias de escalonamento; 
 Definição das Rules; 
 Definição da função Main do programa. 
O Algoritmo a seguir apresenta o código referente a estrutura básica de 
um programa escrito na linguagem PON. 
 
Algoritmo 1: Estrutura da linguagem PON 
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
11 
12 
13 
14 
15 
16 
17 
18 
19 
20 
21 
22 
23 
24 
25 
26 
27 
28 
29 
30 
31 
32 
33 
34 
35 
36 
fbe Apple 
   . . . 
end_fbe 
 
fbe Archer 
   . . . 
end_fbe 
 
---------------- 
 
inst 
   Apple apple1, apple2 
   Archer archer1, archer2 
end_inst 
 
---------------- 
 
strategy 
   . . . 
end_strategy 
 
---------------- 
 
rule RlTurnOn1 
   . . . 
end_rule 
 
rule RlTurnOn2 
   . . . 
end_rule 
 
---------------- 
 
main { 
   . . . 
} 
 
O Algoritmo a seguir apresenta o exemplo de código para criação de 
uma FBE. 
 
Algoritmo 2: Exemplo de criação de FBEs 


 
1 
2 
3 
4 
5 
6 
7 
8 
9 
 
fbe Archer 
    Attributes 
        boolean atHasFired false 
    end_Attributes 
 
 
    Methods 
        method mtFire(atHasFired = true) 
        method mtInnerCode() begin_method cout << "" << endl; end_method 
    end_Methods 
end_fbe 
 
 
O Algoritmo a seguir demonstra como declarar instâncias das FBE’s. 
 
Algoritmo 3: Exemplo de instanciações de FBEs 
 
1 
2 
3 
4 
 
inst 
   Apple apple1, apple2 
   Archer archer1, archer2 
end_inst 
 
O Algoritmo a seguir apresenta como declarar o tipo de estratégia de 
escalonamento. Sendo as possibilidades: no_one, breath e depth. 
 
Algoritmo 4: Exemplo de definição de estratégia de escalonamento 
 
1 
2 
3 
 
strategy 
no_one 
end_strategy 
 
O Algoritmo a seguir apresenta como declarar uma Rule. 
 
Algoritmo 5: Exemplo de criação de Rules 
 
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
11 
12 
13 
14 
15 
16 
17 
18 
19 
20 
21 
22 
 
rule rlTurnOn 
 
   properties 
 
keeper true 
   end_properties 
 
   condition 
      subcondition A 
         premise imp prIsCrossed apple1.atIsCrossed == false 
            and 
         premise imp prHasFired archer1.atHasFired == false 
            and 
         premise prReadyToFire controller1.atHasFired == true 
      end_subcondition 
   end_condition 
 
   action 
      instigation inArcherFire1 archer1.mtFire 
      instigation inAppleCrossed1 apple1.mtExplode 
   end_action 
 
end_rule 
 
O Algoritmo a seguir apresenta como declarar a função Main. 


 
Algoritmo 6: Exemplo do código Main 
 
1 
2 
3 
4 
5 
 
main {  
 
apple->setisCrossed(false); 
 
archer->sethasFired(false); 
 
controller->setfire(true); 
} 
 
c) Tipos de atributos do PON 
Os tipos de atributos permitidos na linguagem PON são: 
 boolean 
 integer 
 string 
 
 char 
 pfloat 
Além desses tipos atributos, é possível realizar a composição de uma 
FBE. O algoritmo a seguir apresenta como realizar a composição em uma FBE. 
d) Compilando 
Para compilar e executar um programa utilizando o compilador PON é 
necessário executar os seguintes passos: 
1. Crie o programa PON conforme exemplificado anteriormente e salve em 
um arquivo de código fonte preferencialmente com a extensão .pon; 
2. Execute o processo de criação do compilador PON (pon em Linux e 
pon.exe em Windows). Veja etapa de geração do compilador. 
3. Execute o comando abaixo: 
./pon 1 < nome_do_programa.pon (Linux) 
./pon.exe 1 < nome_do_programa.pon (Windows) 
 


O comando descrito no passo três é composto pela chamada de 
execução do compilador PON criado com o nome pon. São necessários dois 
argumentos para executar o processo de compilação. O primeiro argumento é 
a opção de geração de código intermediário que varia de 1 a 7.  
1. C; 
2. C++; 
3. Framework; 
4. Pré-Compilador; 
5. NOCA; 
6. Static C++; 
7. VHDL; 
Já o segundo argumento atribui o código fonte inserido no arquivo 
nome_do_programa.pon e irá criar o código intermediário PON conforme opção 
selecionada. 
Obs: vale ressaltar que o código intermediário gerado será criado na 
pasta compiladosc para o código intermediário em C, cppcompilados para o 
código intermediário em C++ ou Static C++, compilados para código 
intermediário em Framework, nopcompilados para a opção do pré-compilador, 
nocacompilados para código NOCA e VHDLcompilados para código 
intermediário VHDL. 
Regras de Formação 
 
O conceito de Regras de Formação ou Formation Rules foi proposto 
por (SIMÃO, 2001; SIMÃO, STADZISZ e KÜNZLE,2003) para permitir a  
criação de Rules  específicas, a partir da representação genérica de uma Rule. 
Este conceito é bastante útil quando o conhecimento causal de uma Rule é 
comum para diferentes conjuntos de instâncias de FBEs, ou seja, um conjunto 
de Rules específicas se diferencia apenas nas instâncias referenciadas.  


Um exemplo do uso das Regras de Formação é em cenário de 
simulação de um conjunto de semáforos. Cada semáforo da simulação possui 
o mesmo conjunto de regras, se diferenciando apenas na instância declarada. 
Caso ocorra uma simulação com um número elevado de semáforos, seria 
necessário replicar as regras manualmente para cada instancia declarada. 
Tornando o processo de desenvolvimento muito trabalhoso. Com o uso de 
regras de formação, o conhecimento da regra é genérico para todas as 
instancias de semáforos. Assim, para cada instancia declarada, esta regra 
genérica é replicada para as instancias específicas.  
No trabalho realizado na disciplina, foi adicionado a BNF os tokens 
formRule e end_formRule para diferenciar de uma Rule comum. O Algoritmo 
abaixo apresenta a estrutura sintática de uma regra de formação na linguagem 
PON. Quando o conhecimento é genérico em uma regra, é feita referencia ao 
nome da FBE, ao invés do nome de uma instância específica. 
Algoritmo 8: Exemplo do código FormRule 
 
formRule rlTurnOn 
 
 
   condition 
      subcondition A 
         premise prIsCrossed Apple.atIsCrossed == false 
            and 
         premise prHasFired Archer.atHasFired == false 
            and 
         premise prReadyToFire Controller.atHasFired == true 
      end_subcondition 
   end_condition 
 
   action 
      instigation inArcherFire1 Archer.mtFire 
      instigation inAppleCrossed1 Apple.mtExplode 
   end_action 
 
end_formRule 
 
O processo de regras de formação se encontra na opção quatro, ou 
seja, pré-compilação. Na qual cada regra de formação é replicada na forma de 
combinação das FBEs que a compõem, na forma de regras tradicionais. 
Regras de FBE 
O conceito de Regras de FBE ou FBE Rules foi criado de forma a 
facilitar o desenvolvimento de aplicações PON que necessitam aplicar um 


conjunto de regras à todas as instâncias de um determinado FBE. Utilizando 
FBE Rules, torna-se possível a criação de FBEs como entidades 
computacionais autônomas, ou seja, que apresentam Rules intrínsecas à sua 
instanciação. Trata-se de um caso particular de Regra de Formação, na qual a 
Rule está relacionada apenas a um determinado tipo de FBE. 
No trabalho realizado na disciplina, foi adicionado a BNF os tokens 
fbeRule e end_fbeRule para diferenciar de uma Form Rule e de uma Rule 
comum. O Algoritmo abaixo apresenta a estrutura sintática de uma FBE Rule 
na linguagem PON.  
Algoritmo 9: Exemplo do código FbeRule 
fbeRule ruleRobot 
   condition 
     subcondition conditionNumber1 
       premise PrHasFired2 Robot.hasKicked == true 
     end_subcondition 
    end_condition 
    action 
       instigation instigation1 Robot.mtDebug();      
    end_action 
end_fbeRule 
 
O processo de compilação de FBE Rules se encontra na opção quatro, 
ou seja, pré-compilação. Cada FBE Rule é replicada para cada uma das 
instâncias da FBE que as compõem, na forma de regras tradicionais. 
Importante: Para que a regra seja aplicada a toda nova instância de 
uma determina FBE é necessário que as Premises e Instigations façam 
referência ao nome do FBE e não à sua instância. No exemplo acima, a 
Premise “PrHasFired2” possui como primeiro parâmetro “Robot.hasKicked”. 
Nesse caso, “Robot” é o nome de um FBE e, portanto, essa regra será aplicada 
a todas as instâncias de “Robot” que forem criadas, independentemente de 
quantas sejam. 
Ponteiros 
Para permitir a utilização inicial de ponteiros na LingPON, uma série de 
alterações foram feitas no código do compilador para C++. 
Primeiramente, foram criados dois novos tokens no interpretador léxico 
(Lex): NEW e PTR. O token NEW reconhece a sequência “new”, enquanto PTR 


reconhece “^”, que é o caractere especial que designa ponteiros nessa 
proposta. Dessa forma, sequências desse tipo podem ser reconhecidas: 
Archer^ archer = new Archer 
A próxima alteração foi feita no parser Bison. Foi criada uma estrutura 
do tipo list da Standard Library para armazenar todos os IDs de ponteiros que 
são reconhecidos, e essa estrutura será utilizada posteriormente na geração de 
código C++. A alteração feita no Bison permite reconhecer sequências do tipo 
em declarações de Insts: 
Archer^ archer 
Archer^ acher1, ^archer2, ^archer3 
Também permite a utilização dos ponteiros dentro de métodos, em 
construções do tipo: 
method mtNewArcher(archer1 = new Archer) 
 A próxima alteração foi feita na parte de geração de código C++. Para 
que não fosse necessário fazer uma alteração muito grande nesse trecho de 
código, foi criado um novo tipo de entidade dentro da classe Attribute, chamado 
A_PTR, juntamente com os tipos antigos A_BOOLEAN, A_INTEGER e assim 
por diante. O atributo do tipo A_PTR é utilizado dentro da classe CPPCompiler 
para fazer a geração de código do ponteiro. Para isso, um método auxiliar foi 
criado dentro da classe Compiler, que serve de base para CPPCompiler. O 
método createInstantiationPtr varre a lista de identificadores e cria atributos do 
tipo A_PTR, que posteriormente são lidos para imprimir código em C++ 
utilizando a sintaxe de ponteiros. 
NOCA 
O NOCA é uma arquitetura de computador alternativa às arquiteturas 
de computadores tradicionais, tais como von Neumann e fluxo de dados. Essa 
arquitetura foi desenvolvida de acordo com o modelo de execução PON, 
permitindo a execução de aplicações desenvolvidas segundo este paradigma. 
Para isso, Linhares (2015) listou os requisitos abaixo: 


A NOCA deve ser capaz de executar software composto unicamente 
de elementos do PON e, opcionalmente, também de funções sequenciais de 
acordo com o modelo von Neumann. 
 A NOCA deve ser genérica, no sentido de que qualquer alteração na 
aplicação PON sendo executada, dependa somente de alterações de 
software, portanto não requerendo qualquer reconfiguração de 
hardware. 
 A NOCA deve definir uma arquitetura de conjunto de instruções 
(Instruction Set Architecture, ou ISA) que implemente as funcionalidades 
dos elementos da cadeia de notificações do PON. 
 A NOCA deve definir unidades de processamento que sejam capazes de 
executar as instruções da ISA e o fluxo de notificações de forma 
paralela. 
 A NOCA deve ser capaz de executar uma aplicação PON mesmo que 
esta seja composta de mais elementos notificantes do que o número de 
unidades de processamento disponíveis para sua execução. Isto 
viabiliza a escalabilidade, no sentido de que o tamanho de uma 
aplicação PON a ser executada é limitado somente pela quantidade de 
memória disponível para armazenamento do respectivo software. 
Com base nesses requisitos, alguns elementos do metamodelo do 
PON, são mapeados para a ISA do NOCA (Attribute, Premise, Condition, 
Method e Method von Neumann). Do ponto de vista da linguagem PON, a 
compilação usando a opção seis, gera um código intermediário que contém a 
aplicação desenvolvida, formada apenas pelas instruções da ISA. 
Compilando para VHDL 
É possível compilar as aplicações escritas em PON diretamente para 
VHDL, de forma que o código gerado possa ser compilado e executado em 
uma FPGA. Como a cadeia de notificações do PON é executada de forma 
diferenciada no hardware da FPGA nem todos os elementos do PON tem seu 
paralelo no código VHDL. Os principais elementos são: O attribute que 


armazena os dados, as premises que realizam as avaliações sobre os dados e 
os methods que alteram os dados dos attributes. As conditions são apenas 
operações AND sobre as saídas das premises, as instigations são apenas 
ligações e assim por diante.  A seguir serão detalhados os procedimentos 
necessários para que se possa executar a aplicação PON em uma FPGA. 
Para que uma aplicação PON possa ser compilada para uma FPGA 
são necessários além do arquivo VHDL gerado na compilação, os seguintes 
arquivos: 
 data_type_pkg.vhd 
 NOP_attribute.vhd 
 NOP_method.vhd 
 NOP_premise.vhd 
A segui será feita uma breve descrição de cada um deles. 
O arquivo data_type_pkg.vhd contém a declaração genérica dos dados 
a serem armazenados no atributo, assim qualquer número de bits de qualquer 
tipo de dado pode ser armazenado em um atributo. Além disso, é possível 
concatenar um número variável de entradas em um atributo, resolvendo os 
conflitos por ordem de precedência. 
O arquivo NOP_attribute.vhd contém a declaração dos registradores 
que armazenam de forma genérica os dados dos attributes notificando as 
premises quando alguma alteração ocorre. 
O arquivo NOP_method.vhd contém o código das operações realizadas 
sobre os attributes e a lógica para fazer a atualização dos mesmos. 
O arquivo NOP_premise.vhd contém o código que realiza os testes 
sobre os valores dos attributes determinando assim se a condição é verdadeira 
ou não. 
A atual implementação do compilador PON para VHDL possui algumas 
limitações. A principal delas é que apenas os tipos de dados boolean e integer 
estão implementados. Os methods são capazes de realizar apenas as quatro 
operações básicas, soma, subtração, multiplicação e divisão, além da 


atribuição de valores. Os dados do tipo integer são interpretados como inteiros 
com sinal de 32 bits e o resultado da multiplicação é truncado em 32 bits. 
A resolução de conflitos é automática no código gerado, assim se dois 
ou mais methods tentarem atualizar o valor de um attribute ao mesmo tempo o 
attribute vai receber o valor do method que aparecer primeiro no código. 
Como não existe a estrutura “main” no VHDL, o bloco main do 
programa PON foi utilizado para determinar as entradas, as saídas, o nome da 
entidade e o nome do arquivo para o VHDL gerado. Para declarar um attribute 
como entrada é necessário adicionar a seguinte linha ao bloco main no PON. 
in <nome_fbe>.<nome_attribute> 
ex: in controlador.liga 
Para declarar um attribute como saída é necessário adicionar a 
seguinte linha ao bloco main no PON. 
out <nome_fbe>.<nome_attribute> 
ex: out controlador.contador 
Para determinar o nome da entidade e consequentemente o nome do 
arquivo VHDL gerado é necessário adicionar a seguinte linha ao bloco main no 
PON. 
entity <nome_entidade> 
ex: entity controlaRobo 
Assim 
a 
entidade 
no 
código 
gerado 
vai 
receber 
o 
nome 
<nome_entidade> e o arquivo VHDL gerado vai receber o nome 
<nome_entidade>.vhd. 
Se o compilados não encontrar a palavra “entity” no bloco main o nome 
adotado é “NOPHD”. 


Como o bloco main não é interpretado pelo flex/bison não é possível 
adicionar comentários ou realizar a verificação de erros, assim deve-se tomar 
cuidado com a sintaxe. 
Para que se possa realizar a compilação do código gerado devem ser 
realizadas algumas configurações no compilador VHDL. Inicialmente é 
necessário adicionar todos os arquivos ao projeto, o código gerado e os 
arquivos apresentados anteriormente. A seguir é necessário configurar a 
ferramenta para interpretar o VHDL como VHDL 2008. A versão 2008 não é 
padrão e é necessária para compilar os tipos de dados utilizados. 
Uma característica importante do código VHDL gerado é que os 
elementos do PON são componentes independentes, assim é possível utilizar o 
visualizador RTL para encontrar erros nas aplicações. 
Integração 
Cada funcionalidade nova na linguagem foi implementada de maneira 
individual, sendo necessário realizar a integração de cada uma das partes. 
Para isso foram realizadas reuniões no laboratório LSIP, a fim de resolver 
eventuais conflitos em arquivos fontes comuns do compilador. Como resultado, 
foram acrescentadas novas funcionalidades a linguagem e compiladores, com 
o objetivo de desenvolver o estado da técnica do compilador. A mostra o 
diagrama de blocos do compilador PON, após a realização das integrações dos 
trabalhos individuais da disciplina. 


 
Figura  – Diagrama de Blocos após Integração. 
Referências 
BANASZEWSKI, R. F. Paradigma Orientado a Notificações : Avanços e 
Comparações. Dissertação de Mestrado. CPGEI, UTFPR. Curitiba, Brasil, 
2009.  
FERREIRA, C. A. Linguagem e compilador para o paradigma orientado a 
notificações (PON): Avanços e comparações. 2015. Dissertação de 
Mestrado, PPGCA, UTFPR. Curitiba, Brasil, 2015. 
LINHARES, R. R., Contribuição para o desenvolvimento de uma 
arquitetura de computação própria ao paradigma orientado a notificações. 
Tese de Doutorado, CPGEI, UTFPR. Brasil, 2015. 
PETERS, E. Coprocessador para Aceleração de Aplicações Desenvolvidas 
Utilizando Paradigma Orientado a Notificações. 2012. Dissertação de 
Mestrado, CPGEI, UTFPR. Curitiba, Brasil, 2012. 
SIMÃO, J. M. Proposta de uma Arquitetura de Controle para Sistemas 
Flexíveis de Manufatura Baseada em Regras e Agentes. Dissertação de 


Mestrado, Universidade Tecnológica Federal do Paraná - UTFPR, Curso de 
Pós-Graduação em Engenharia Elétrica e Informática Industrial - CPGEI, 
Curitiba, 2001. 
SIMÃO, J.M., STADZISZ, P.C., KÜNZLE, L. Rule and Agent-oriented 
Architecture to Discrete Control Applied as Petri Net Player. (G. Torres, J. 
Abe, M. Mucheroni, & C. P.E., Eds.) 4th Congress of Logic Applied to 
Technology - LAPTEC 2003 , 101, p. 217, 2003. 
SIMÃO, J. M. ; STADZISZ, P. C.  Paradigma Orientado a Notificações (PON) 
- Uma Técnica de Composição e Execução de Software Orientada a 
Notificações. 
2008, 
Brasil.  
Patente: Privilégio de Inovação. Número do registro: PI08055181, data de 
depósito: 26/11/2008, título: "PEDIDO DE PATENTE: Paradigma Orientado a 
Notificações (PON) Uma Técnica de Composição e Execução de Software 
Orientada a Notificações." , Instituição de registro:INPI - Instituto Nacional da 
Propriedade 
Industrial. 
Instituição(ões) 
financiadora(s): 
Universidade 
Tecnológica Federal do Paraná. 
SIMÃO, J. M.; LINHARES, R. R. ; WITT, F. A. ; LIMA, C. R. E. ; STADZISZ, P. 
C. Paradigma Orientado a Notificações em Hardware Digital. 2012, Brasil.  
Patente: Privilégio de Inovação. Número do registro: BR102012026429, data de 
depósito: 16/10/2012, título: "PEDIDO DE PATENTE: Paradigma Orientado a 
Notificações em Hardware Digital" , Instituição de registro:INPI - Instituto 
Nacional da Propriedade Industrial. Instituição(ões) financiadora(s): UTFPR, 
2012b. 
RONSZCKA, A. F. Contribuição Para a Concepção de Aplicações no 
Paradigma Orientado a Notificacões (PON) Sob o Viés de Padrões. 2012. 
Dissertação de Mestrado, CPGEI, UTFPR. Curitiba, Brasil, 2012. Disponível em 
http://files.dirppg.ct.utfpr.edu.br/cpgei/Ano_2012/dissertacoes/CPGEI_Dissertac
ao_608_2012.pdf. 


271
ANEXO E -- RELAT´ORIO DA DISCIPLINA
LINGUAGENS/COMPILADORES - 2016
Este anexo apresenta o relat´orio apresentado pelos alunos Eduardo Bilk de Athayde
e Fabio Negrini como trabalho ﬁnal da disciplina “Linguagens e Compiladores” ofertada
pela UTFPR em 2016 e ministrada por Prof. Dr. Jo˜ao Alberto Fabro e Prof. Dr. Jean
Marcelo Sim˜ao.


UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ (UTFPR) 
PROGRAMA DE PÓS-GRADUAÇÃO EM  
COMPUTAÇÃO APLICADA (PPGCA) 
 
 
 
EDUARDO BILK DE ATHAYDE - DISCENTE PPGCA/UTFPR 
 
FABIO NEGRINI – DISCENTE CPGEI/UTFPR 
 
 
 
IMPLEMENTAÇÃO DE COMPILAÇÃO PARA C++ NAMESPACES PARA A 
LINGPON E OTIMIZAÇÕES NO TRATAMENTO DE PREMISSAS 
 
 
 
RELATÓRIO DE TRABALHO FINAL 
 
DISCIPLINA: TÓPICOS AVANÇADOS EM ENGENHARIA DE SOFTWARE 
 
CÓDIGO: CAES101 - TURMA: PGCA – ANO/PERÍODO 2016/03 
 
TEMA: LINGUAGENS E COMPILADORES. 
  
OBJETO DE ESTUDO: LINGPON – LINGUAGEM E COMPILADOR PARA 
PARADIGMA ORIENTADO A NOTIFICAÇÕES (PON). 
 
PROFESSORES:  
 
PROF. DR. JOÃO ALBERTO FABRO. 
 
PROF. DR. JEAN MARCELO SIMÃO. 
 
 
 
CURITIBA – PR, BRASIL 
DISCIPLINA TERCEIRO TRIMESTRE DE 2016   
RELATÓRIO MARÇO DE 2017 
 


2 
 
1 INTRODUÇÃO 
O Paradigma Orientado a Notificações (PON) teve sua origem em 2005 
quando foi apresentada uma proposta de abordagem holônica para sistemas de 
manufatura (HMS) como um meta-modelo [1]. Uma vez visto que este meta-modelo 
possuía potencial além desta abordagem, esforços foram direcionados para a 
definição deste em forma de paradigma [2]. 
Em tempo, no PON há dois conjuntos de entidades principais, nomeadamente 
as Fact Base Elements (FBEs) e as Rules. As FBEs tratam o conhecimento factual e 
execucional no âmbito do PON por meio de sub-entidades chamadas Attributes e 
Methods. Por sua vez, as entidades Rules tratam do conhecimento lógico causal do 
PON  por meio de sub-entidades Premises-Conditions e Actions-Instigations. Ainda, 
todo o processo de inferência de dá por notificações que partem dos FBE-Attributes 
para Rules, por meio de Premises-Conditions, e depois evoluem para os Methods-
FBE, por meio de Instigations-Actions. Este processo de inferência é detalhado em 
[1]. 
Em teoria, este processo de Inferência Orientado a Notificações (ION) do 
PON, traz benefícios como o evitar de redundâncias o que permitiriam bom 
desempenho, bem como o desacoplamento implícito de entidades o que facilitaria 
distribuição, dentre outros, Como uma consequência natural, materializações seria 
então a próxima etapa do avanço do PON para fins de verificar suas propriedades. 
Isto dito, o PON foi inicialmente materializado como um framework para a linguagem 
C++ [3] e, posteriormente, uma linguagem de programação própria e respectivo 
compilador, chamado de LingPON [4]. Desde então, os esforços estão sendo 
direcionados para a evolução da LingPON, seja para otimização de suas 
materializações, seja para melhora na linguagem tanto no aspecto de facilidade 
quanto no aspecto de novas ferramentas [4]. 
Primeiramente, a LingPON permitia gerar código em Framework C++ PON 
2.0, linguagem C segundo o PON e linguagem C++ segundo o PON [5]. Neste âmbito, 
subsequentemente o LingPON teve uma proposta de materialização em C++ estático, 
a qual apresentou considerável melhora em sua execução em relação a primeira 
versão da LingPON que ainda não estava a contento. Entretanto, o chamado LingPON 
estático ainda apresenta consideráveis limitações em sua usabilidade como 


3 
linguagem de programação, como a integração com código não estático, algo 
resolvido por definição na primeira versão do LingPON.  
Isto considerado, este documento apresenta duas melhorias no tocante ao 
LingPON. Essas melhorias são fruto da disciplina de Tópicos Avançados em 
Engenharia de Software ministrado na fase 3 do ano de 2016. O tema da disciplina foi 
Linguagens e Compiladores e objeto de estudo foi justamente a LingPON. 
A primeira parte deste documento propõe uma mudança na materialização de 
C++ estático para C++ orientado a namespaces que permitiu a melhor integração com 
bibliotecas externas em C++ e códigos não estáticos em geral, mantendo equivalente 
desempenho. A segunda parte é uma proposta para importação de codificação C++ a 
ser integrada à linguagem, integração esta que só foi possível com a mudança para 
namespaces. A terceira e última parte deste documento propõe várias melhorias nos 
controles das chamadas premissas ou premises da LingPON afim de otimizar e 
facilitar a sua utilização. 
 
 
1.1 PROBLEMÁTICA 
A implementação de compilação de LingPON para C++ com classes estáticas 
(StaticCPP), i.e. LingPON Estático, trouxe melhorias significativas na linguagem no 
tocante a desempenho  [5]. Contudo, ela trouxe um ônus para a extensibilidade do 
código PON. De fato, uma vez que todas as classes criadas são estáticas, não há 
possibilidade de incluir bibliotecas externas já que classes estáticas não podem conter 
elementos não estáticos. Em suma, ainda não há, em LingPON Estático, uma maneira 
razoável de incluir bibliotecas para uso em Methods de FBEs nem bibliotecas externas 
customizadas.  
Nesse contexto, o trabalho relatado por este documento teve como objetivo 
implementar a geração de código em LingPON para C++ com o uso de namespaces 
ao invés de classes estáticas, afim de sanar a problemática da extensibilidade do 
código PON e ao mesmo tempo manter o desempenho alcançado pela abordagem de 
implementação sem uso de sobrecargas de C++ OO em código gerado. 
Adicionalmente foi implementado um método para importação de código externo em 
PON, bem como para qualquer inclusão necessária para métodos PON. 


4 
Isto considerado, namespaces em C++ podem se referir a variáveis, funções, 
estruturas, enumerações, classes e membros de classes e/ou estruturas. Ademais, 
namespaces podem ajudar a tratar ambiguidade em nomes de entidades como 
variáveis, funções etc. De fato, a medida que uma aplicação cresce a necessidade de 
gerenciar ambiguidade aumenta, sendo os escopos proporcionados por namespaces 
uteis para tal. 
Neste âmbito, a Figura 1 mostra um exemplo de aumento de complexidade 
na gestão de escopos de uma aplicação. 
 
Figura 1 – Exemplo de bibliotecas com mesmo nome de classe. 
 
O alto uso de bibliotecas aumenta consideravelmente o risco de haver nome 
repetidos em um mesmo escopo. A biblioteca gráfica libGraphic mostrada na Figura 1 
contém uma classe para manipulação de elementos gráfico “Texto”, que representa 
uma caixa de texto. Por sua vez, a biblioteca libStrings representa uma biblioteca para 
manipulação de strings que possui uma classe “Texto” que nesse contexto manipula 
strings de grande tamanho. 
Isso posto, caso uma aplicação que deseje utilizar ambas classes mostradas 
na Figura 1 deve fazer gestão de seu escopo, afim de sanar a ambiguidade das 
classes associadas. Justamente, Namespaces são formas de manter código 
vinculado a um escopo definido pelo programador. Então, nesse caso, seria possível 
associar cada classe representada na Figura 1 a um namespace e, com isso, sanar a 
incompatibilidade. Isso promove a mesma versatilidade e velocidade que havia na 
implementação StaticCPP porém não impossibilita a utilização de código não estático 
nos métodos das FBEs. 
 
 


5 
2 IMPLEMENTAÇÃO NAMESPACES 
Para a criação da geração de código em namespace foram considerados os 
esforços do StaticCPP quanto a lógica de notificações e materialização de entidades 
PON demonstrados na Figura 2. Tais esforços serviram de base para a criação da 
geração de código em Namespaces. Em StaticCPP, cada uma dessas entidades do 
PON é materializada com uma classe estática. Entretanto, isso não interfere no 
tocante a dinâmica de notificações, cuja lógica é reaproveitável na abordagem por 
namespaces.  
  
Figura 2 – Diagrama de materialização de notificações e entidades do StaticCPP. 
 
A Figura 2 mostra a estrutura da cadeia de notificação entre as entidades 
PON: Method, Attribute, Premise e Subcondition. Esta é uma subdivisão 
organizacional de Condition de Rule, em suma. Isto dito, a execução do procedimento 
run() de um Method altera o valor de um Attribute, que por sua vez notifica as 
Premise(s) interessadas. Caso haja alteração em seu estado, esta notifica a(s) 
Subcondition(s) pertinente(s), então, caso a Subcondition seja aprovada ela dispara a 
execução do(s) Method(s) associados. 


6 
A abordagem para geração de código em namespaces seguiu a mesma 
lógica, contudo ao invés de gerar um arquivo para cada entidade agrupou-se todas as 
Premises em um arquivo “Premises”, todas as Subconditions em um arquivo 
“Subconditions” e cada Method e Attribute relativo a FBE foi compilado no arquivo 
“Instantiations”. A Figura 3 esboça a mudança. 
  
Figura 3 - Modificações de materialização da geração de código em namespaces em relação 
com StaticCPP. 
 
A Figura 3 demonstra a inclusão das entidades Method e Atribute dentro de 
uma entidade (namespace) chamada instantiation. O namespace instantiation contém 
todas as instâncias de FBE da aplicação. Por sua vez todas as Premises e 
Subconditions da aplicação são alocadas nos namespaces premise e subcondition 


7 
respectivamente.  Consolidando então as 3 entidades geradas em seus respectivos 
arquivos, para fins organizacionais, ie Instantiation, Premise e Subcondition. 
Os tópicos seguintes expõem em maior detalhe cada uma das entidades 
(arquivos) e seu mecanismo interno. 
 
2.1 INSTANTIATIONS 
O namespace Instantiations (.h | .cpp) agrega todas as instâncias de FBE 
declaradas no código LingPON. A Figura 4 mostra o exemplo de código LingPON da 
aplicação chamada portão eletrônico (electronicgate.pon) [REF]. 
 
 
Figura 4 - Declaração de FBEs e Instâncias do código LingPON electronicgate. 
 
Na Figura 4 as linhas 1-9 e 11-18 declaram, respectivamente as FBEs Gate e 
Event. Nas linhas 20-23 são declaradas as instâncias destas FBEs (gate e event, 
respectivamente). O código gerado da compilação do arquivo em questão pode ser 
visto na Figura 5. 


8 
 
Figura 5 - Arquivo instantiations.h gerado pela compilação para namespaces. 
 
Cada instância está dentro do namespace “instantiation” e cria um próprio 
namespace com métodos e atributos correlatos a declaração da FBE, cada qual em 
seu respectivo namespace também. 
Dessa forma uma chamada de método pode ser feita acessando cada 
namespace até o método. Por exemplo, a execução do método “opened” da instância 
“gate” pode ser invocada pela chamada instantiation::gate::mt::opened(). 
 
2.2 PREMISES  
Correlato com a lógica implementada em StaticCPP a geração de código em 
namespace também atribui os mesmos métodos (init, compare e notify) para cada 
Premise gerada em LingPON e as agrupa no arquivo chamado premises (.h | .cpp). 
Cada Premise encontra-se dentro no namespace “premise” e detém as 
variáveis state, cpy1st e cpy2nd. Sua mecânica segue a mesma já implementada no 
StaticCPP na qual é inicializada com o procedimento init e quando notificada 


9 
(execução do método notify) executa a comparação para verificar se a Premise foi 
aprovada (método compare).  
A Figura 6 ilustra as premissas geradas para o caso do programa 
electronicgate.pon. 
 
Figura 6 - Implementação de premissas em namespaces. 
 
 
2.3 SUBCONDITIONS 
As Subconditions detêm os procedimentos inc e dec e uma variável count. Os 
procedimentos são executados à medida que os estados das Premises são alterados 
e no momento em que o contador aponta que todas as Subcondition de uma 
determinada Rule estão aprovadas a respectiva Action é acionada. 
A lógica é inspirada no mesmo estilo daquela implementada no StaticCPP, 
sendo que agora  com o agrupamento de todas as subconditions em um namespace 
chamado subcondition. 
A Figura 7 mostra a geração do arquivo de cabeçalho das subcondition quanto 
que a Figura 8 mostra sua implementação. 


10 
 
Figura 7 - Geração das subconditions em namespaces. 
 
 
Figura 8 - Implementação de subconditions para namespaces. 
 
 


11 
Na Figura 8 as linhas 10-11 e 23-24 mostram as Instigations de Methods 
referentes ao documentado no código LingPON (Figura 9). 
 
Figura 9 - Código de Rules para LingPON. 
 
As linhas 37-38 e 50-51 mostradas na Figura 9 correspondem 
respectivamente ao código gerado na Figura 8 linhas 23-24 e 10-11. 
 
3 IMPORT.PON 
Com a finalização da implementação em namespace o problema para 
importar bibliotecas externas com classes não estáticas estava sanado. Contudo 
ainda não havia um método para realizar a inclusão de bibliotecas nos métodos PON. 
Para isso criou-se um arquivo padrão chamado import.pon que quando presente na 
compilação do código PON será interpretado e conterá as informações de inclusões 
necessárias segundo o programador. 


12 
A Figura 10 mostra a estrutura padrão para o arquivo de importação, bem 
como um exemplo para obtenção do código de abertura e fechamento do portão 
eletrônico (electronicgate.pon) por uma classe externa ao PON. 
 
Figura 10 - Estruturação do arquivo import.pon. 
 
Na Figura 10 a linha 1 e 4 delimitam a declaração que será inserida no arquivo 
das instâncias, enquanto as linhas 6 e 8 delimitam inclusões para o arquivo main.cpp. 
As linhas 2-3 mostram respectivamente a inclusão da biblioteca externa e a 
instanciação da classe que será usada no método da FBE.o identificador “exProvider” 
foi usado no método PON, como demonstrado na linha 6-7 da Figura 4. 
A linha 6-7 da Figura 4 também mostra uma nova sintaxe inserida no 
compilador LingPON (incluído na sua BNF) na qual o atributo que recebe o valor de 
um método externo (chamado entre as palavras chave begin_ e end_method) é 
colocado como parâmetro da chamada de método.  
Ou seja, na declaração method opened (gateState) begin_method 
exProvider.getOpen(); end_method o atributo gateState recebe o retorno da função 
exProvider.getOpen(). 
Para tanto foi necessário alterar a BNF (a partir do arquivo de projeto do 
compilador chamado bison_pon.y) para adicionar a opção de compilação nº 8 e a nova 
sintaxe do método, que não interfere nos compiladores anteriores. 
4 TESTES COMPARATIVOS 
A fim de investigar os impactos relativos a desempenho da implementação da 
geração de código para namespace, buscou-se a comparação com o o código gerado 
em StaticCPP. 
Para parametrização foi usado o código do electronicgate.pon, mostrado nas 
Figura 4 e Figura 9. Considerou-se o tempo em segundos de um milhão de 
acionamentos de portão (aprovação de Rule) como uma amostra. Dessa forma 


13 
coletou-se oito mil amostras compiladas com a otimização “-O3” do compilador GNU 
g++ em uma máquina Linux (no caso, em ambiente virtual). 
Uma vez que o ambiente estava suscetível a interferências do Sistema 
Operacional decidiu-se eliminar os mil valores mais altos da distribuição afim de 
reduzir o desvio padrão das amostras. 
Isso posto os resultados obtidos (Figura 11) mostraram-se satisfatórios uma 
vez que não reduziram o desempenho em relação ao programa gerado pela 
compilação para StaticCPP: 
 Valor mínimo amostrado em código StaticCPP: 39,91s 
 Valor mínimo amostrado em código Namespaces: 39,97s 
 Valor médio amostrado em código StaticCPP: 44,57s 
 Valor médio amostrado em código Namespaces: 44,10s 
 Valor mediano amostrado em código StaticCPP: 44,54s 
 Valor mediano amostrado em código Namespaces: 43,85s 
 Valor máximo amostrado em código StaticCPP: 48,27s 
 Valor máximo amostrado em código Namespaces: 48,76s 
 
Figura 11 – Gráfico comparativo entre Namespace  e StaticCPP 
 
Nesse contexto a implementação de geração de código em namespace 
mostra-se de grande valia uma vez que sana a deficiência do código gerado em 
staticCPP sem penalizar o desempenho. 
 
5 OTIMIZAÇÕES NO TRATAMENTO DE PREMISE 
39.91
44.57
44.54
48.27
39.97
44.10
43.85
48.76
MIN
MÉDIA
MED
MAX
staticClass
Namespace


14 
5.1 VINCULAR PREMISE NOMINAIS DE VÁRIAS RULES EM UMA ÚNICA PREMISE 
 
Motivação 
 
 
Sempre que uma Premise em PON é criada, ela é identificada pelas variáveis 
envolvidas para que sejam notificadas em caso de mudança de seu valor. Uma 
mesma Premise utilizada em várias Rules em PON acaba então sendo uma 
duplicidade desnecessária e que acaba impactando na performance, visto que dois 
elementos podiam ser convertidos em apenas um. Ademais, isso confrontava a 
própria teoria do PON sobre o evitar implícitos de redundâncias. 
O objetivo desta melhoria é converter em um mesmo elemento Premise as 
Premises atualmente redundantes em LingPON de forma a otimizar o número de 
elementos na tabela de compilação e, consequentemente, reduzir o número de 
notificações durante sua execução.  
 
Realização 
 
Tome-se como base o exemplo abaixo, onde as premissas PON serão 
identificas em um mesmo elemento: 
 
rule rlOpeningGate 
    condition 
 
subcondition a1 
                 premise prRemoteControlOn  event.atEventState == 1 and 
 
        premise prGateIsClosed gate.atGateState == 0     
 
end_subcondition 
    end_condition 
    ... 
end_rule 
 
rule rlClosingGate 
    condition 
 
subcondition a2 
 
        premise prRemoteControlOn  event.atEventState ==1 and 
                premise prGateIsOpened gate.atGateState == 1 
 
end_subcondition 
    end_condition 
    ... 
end_rule 


15 
 
 
De fato, já havia uma codificação anterior onde havia uma vinculação das 
Premises de mesmo nome em um único elemento mas não era utilizada. Foi feita uma 
revisão do código para melhor verificação de seu funcionamento depurando para 
garantir o vínculo a um mesmo elemento. 
 
 
entityFound = semanticAnalyser.getEntity(internalID); 
 
 
if (entityFound == 0) { 
 
 
 
premise = new Premise(internalID); 
 
 
premise->ref = leftId; 
 
 
premise->ref1 = rightId; 
 
 
premise->imp = imp; 
 
Resultados 
 
Como demonstração de resultado, o compilador foi modificado para gerar log de saída 
e apresentar o resultado da compilação e demonstrar que as duas chamadas da 
mesma Premises foram identificadas e unificadas em um mesmo elemento. 
 
fbe Gate 
    attributes 
        integer atGateState 0 
    end_attributes    
    methods 
         method mtOpened(atGateState = 1) 
         method mtClosed(atGateState = 0) 
    end_methods 
end_fbe 
 
fbe Event 
    attributes 
        integer atEventState 0 
    end_attributes 
    methods 
        method mtReset(atEventState = 0)          
    end_methods 
end_fbe 
 
inst 
    Gate gate 
    Event event    
end_inst 
 
strategy 
    no_one 
end_strategy 
 


16 
rule rlOpeningGate 
    condition 
 
subcondition a1 
         
premise prRemoteControlOn event.atEventState == 1 and 
 
        premise prGateIsClosed gate.atGateState == 0     
 
end_subcondition 
    end_condition 
    action 
 
 
instigation inNone1 event.mtReset(); 
        instigation inOpening1 gate.mtOpened();          
    end_action 
end_rule 
 
rule rlClosingGate 
    condition 
 
subcondition a2 
 
        premise prRemoteControlOn event.atEventState == 1 and 
         
premise prGateIsOpened gate.atGateState == 1 
 
end_subcondition 
    end_condition 
    action 
 
 
instigation inNone2 event.mtReset(); 
        instigation inClosing1 gate.mtClosed();        
    end_action 
end_rule 
 
main { 
 
 
//configura o portão como fechado 
 
gate->setatGateState(0); 
 
 
 
//abre o portão 
 
event->setatEventState(1); 
 
 
 
//fecha portão 
 
event->setatEventState(1); 
 
} 
 
 
 
 
 
 
 
 


17 
 
 


18 
5.2  PERMITIR INFORMAR APENAS O IDENTIFICADOR DA PREMISE QUANDO 
ESTA FOR PREVIAMENTE DECLARADA 
Motivação 
 
 
Na LingPON, a declaração de uma premissa possui os seguintes argumentos: 
nome, variável FBE, operador, operando (que pode ser uma variávelFBE ou uma 
constante). A figura abaixo demonstra com detalhes todos os elementos: 
 
 
 
Em casos onde uma Premise em PON possa ser reaproveitada a redefinição 
dos argumentos que seguem o nome passam a ser redundantes, visto que a Premise 
em PON já foi anteriormente definida. Manutenções no código passam a ser 
oneradas, pois a mudança de uma premissa obriga e revisão em todos os pontos onde 
a mesma premissa é utilizada. 
 
O objetivo desta melhoria é permitir que uma Premise, uma vez declarada e 
nominada, possa ser reutilizada apenas declarando seu identificador. Esta nova 
sintaxe possui a vantagem de ser mais limpa e, caso a Premise seja redefinida, não 
será necessário alterar todas as instâncias desta premissa, bastando alterar apenas 
sua primeira definição. 
 
Realização 
 
O exemplo abaixo, a Premise prRemoteControlOn declarada abaixo: 
rule rlOpeningGate 
    condition 
 
subcondition a1 
                 premise prRemoteControlOn event.atEventState == 1 and 
 
        premise prGateIsClosed gate.atGateState == 0     


19 
 
end_subcondition 
    end_condition 
    … 
end_rule 
 
É novamente utilizada em outra condição: 
rule rlClosingGate 
    condition 
 
subcondition a2 
 
        premise prRemoteControlOn event.atEventState == 1 and 
                 premise prGateIsOpened gate.atGateState == 1 
 
end_subcondition 
    end_condition 
    … 
end_rule 
 
Com a melhoria proposta, a chamada à premissa pode ser substituída pela 
seguinte sintaxe: 
 
rule rlClosingGate 
    condition 
 
subcondition a2 
 
        premise prRemoteControlOn and 
                 premise prGateIsOpened gate.atGateState == 1 
 
end_subcondition 
    end_condition 
    … 
end_rule 
 
 
No arquivo bison_pon.y, nas declarações de premissas, foi adicionada uma 
redefinição de premissa: 
premise  
 
: PREMISE exp {$$ = compiler->createPremise("", ((PremiseCompType*)$2)->leftId, 
((PremiseCompType*)$2)->op, ((PremiseCompType*)$2)->rightId,0);} 
 
 
 
 
| PREMISE id {$$ = compiler->linkPremise($2);} 
 
 
 
 
| PREMISE id exp  {$$ = compiler->createPremise($2, ((PremiseCompType*)$3)-
>leftId, ((PremiseCompType*)$3)->op, ((PremiseCompType*)$3)->rightId,0);} 
 
 
 
 
| 
PREMISE 
IMP 
exp 
 
{$$ 
= 
compiler->createPremise("", 
((PremiseCompType*)$3)->leftId, ((PremiseCompType*)$3)->op, ((PremiseCompType*)$3)->rightId,1);} 
 
 
 
 
 
 
 
| 
PREMISE 
IMP 
id 
exp 
 
{$$ 
= 
compiler->createPremise($3, 
((PremiseCompType*)$4)->leftId, ((PremiseCompType*)$4)->op, ((PremiseCompType*)$4)->rightId,1);} 
 
 
 
 
 
; 
 
 


20 
Adicionalmente o método Compiler::linkPremisse foi definido conforme 
abaixo: 
Entity * Compiler::linkPremise(std::string userEntityId){ 
 
 
Entity *entityFound = semanticAnalyser.getEntity(userEntityId); 
 
Premise *premise; 
 
 
if (entityFound==0){ 
 
 
semanticAnalyser.addError("Não foi possível localizar definição da premissa " + userEntityId); 
 
 
return NULL; 
 
}else{ 
 
 
return (Entity *)premise; 
 
} 
} 
 
Resultado 
 
Como demonstração de resultado, o compilador foi modificado para gerar log de saída 
e apresentar o resultado da compilação e demonstrar que as duas chamadas da 
mesma Premise foram identificadas e unificadas em um mesmo elemento, sendo que 
a segunda declaração da Premise foi informado apenas o primeiro argumento –nome: 
fbe Gate 
    attributes 
        integer atGateState 0 
    end_attributes    
    methods 
 
 
method mtOpened(atGateState = 1) 
         method mtClosed(atGateState = 0) 
    end_methods 
end_fbe 
 
fbe Event 
    attributes 
        integer atEventState 0 
    end_attributes 
    methods 
        method mtReset(atEventState = 0)          
    end_methods 
end_fbe 
 
inst 
    Gate gate 
    Event event    
end_inst 
 
strategy 
    no_one 
end_strategy 
 
rule rlOpeningGate 
    condition 
 
subcondition a1 
         
premise prRemoteControlOn event.atEventState == 1 and 


21 
 
        premise prGateIsClosed gate.atGateState == 0     
 
end_subcondition 
    end_condition 
    action 
 
instigation inNone1 event.mtReset(); 
        instigation inOpening1 gate.mtOpened();          
    end_action 
end_rule 
 
rule rlClosingGate 
    condition 
 
subcondition a2 
 
        premise prRemoteControlOn and 
         
premise prGateIsOpened gate.atGateState == 1 
 
end_subcondition 
    end_condition 
    action 
 
instigation inNone2 event.mtReset(); 
        instigation inClosing1 gate.mtClosed();        
    end_action 
end_rule 
 
main { 
 
 
//configura o portão como fechado 
 
gate->setatGateState(0); 
 
 
 
//abre o portão 
 
event->setatEventState(1); 
 
 
 
//fecha portão 
 
event->setatEventState(1); 
 
} 
 
 


22 
 
 


