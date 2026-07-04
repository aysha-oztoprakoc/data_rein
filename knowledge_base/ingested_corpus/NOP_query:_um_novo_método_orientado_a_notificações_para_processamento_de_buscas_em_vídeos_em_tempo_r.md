# NOP query: um novo método orientado a notificações para processamento de buscas em vídeos em tempo real.pdf

UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ
PROGRAMA DE PÓS-GRADUAÇÃO EM ENGENHARIA ELÉTRICA E
INFORMÁTICA INDUSTRIAL
CLAYTON KOSSOSKI
NOP QUERY – UM NOVO MÉTODO ORIENTADO A NOTIFICAÇÕES
PARA PROCESSAMENTO DE BUSCAS EM VÍDEOS EM TEMPO
REAL
TESE
CURITIBA
2024


CLAYTON KOSSOSKI
NOP QUERY – UM NOVO MÉTODO ORIENTADO A
NOTIFICAÇÕES PARA PROCESSAMENTO DE BUSCAS EM
VÍDEOS EM TEMPO REAL
NOP Query – A new notification-based method
for processing video queries on the fly
Tese apresentado(a) como requisito para ob-
tenção do título(grau) de Doutor em Ciên-
cias, do Programa de Pós-Graduação em
Engenharia Elétrica e Informática Industrial,
da Universidade Tecnológica Federal do Pa-
raná (UTFPR).
Orientador: Prof. Dr. Heitor Silvério Lopes
Coorientador: Prof. Dr. Jean Marcelo Simão
CURITIBA
2024
4.0 Internacional
Esta licença permite compartilhamento, remixe, adaptação e criação a partir do
trabalho, mesmo para fins comerciais, desde que sejam atribuídos créditos ao(s)
autor(es).
Conteúdos elaborados por terceiros, citados e referenciados nesta obra não são
cobertos pela licença.


Ministério da Educação
Universidade Tecnológica Federal do Paraná
Campus Curitiba
CLAYTON KOSSOSKI
NOP QUERY - UM NOVO MÉTODO ORIENTADO A NOTIFICAÇÕES PARA PROCESSAMENTO DE BUSCAS EM VÍDEOS EM
TEMPO REAL
Trabalho de pesquisa de doutorado apresentado como requisito para
obtenção do título de Doutor Em Ciências da Universidade
Tecnológica Federal do Paraná (UTFPR). Área de concentração:
Engenharia De Computação.
Data de aprovação: 01 de Novembro de 2024
Dr. Ademir Cristiano Gabardo, Doutorado - Industrial Monitoring Control Lty
Dr. Fabricio Enembreck, Doutorado - Pontifícia Universidade Católica do Paraná (Pucpr)
Dr. George Darmiton D Cunha Cavalcanti, Doutorado - Universidade Federal de Pernambuco (Ufpe)
Dr. Paulo Cezar Stadzisz, Doutorado - Universidade Tecnológica Federal do Paraná
Dr. Thiago Henrique Silva, Doutorado - Universidade Tecnológica Federal do Paraná
Documento gerado pelo Sistema Acadêmico da UTFPR a partir dos dados da Ata de Defesa em 31/12/2024.
 


I dedicate this work to my family and friends
and especially in memory of my father
Demétrio.


ACKNOWLEDGEMENTS
This work could not have been completed without the help of several people and/or
institutions to whom I pay tribute. Certainly, these paragraphs will not cover all the people who
have been part of this important phase in my life. For this reason, I apologize in advance to those
who are not present in these words, but you can be sure that they are part of my thoughts and my
gratitude.
First of all, I thank God and my parents Demétrio and Anita for life.
To my brother and family, for their kindness, encouragement and total support at every
moment of my life.
To my advisor, Prof. Dr. Heitor Silvério Lopes, who showed me the paths to follow and
for the trust he deposited in me. You are my greatest inspiration for becoming a professor.
To my co-advisor, Prof. Dr. Jean Marcelo Simão, who insistently teaches me to improve
every day.
To the Federal University of Technology – Paraná, my alma mater.
To all the professors, colleagues in the department and co-workers who helped directly
and indirectly, in the accomplishment of this work.
Finally, I would like to express my gratitude to all those who contributed, whether
through their actions or ideas, to the completion of this work.
This study was financed in part by the Coordenação de Aperfeiçoamento de Pessoal de
Nível Superior – Brasil (CAPES) – Finance Code 001.
4112


“Difficulties strengthen the mind, as labor does
the body.” (Lucius Annaeus Seneca).


RESUMO
KOSSOSKI, Clayton. NOP Query – Um novo método orientado a notificações para
processamento de buscas em vídeos em tempo real. 2024. 142 f. Tese (Doutorado em
Engenharia Elétrica e Informática Industrial) – Universidade Tecnológica Federal do Paraná.
Curitiba, 2024.
Com o rápido crescimento dos dados de vídeo, a procura de eventos em vídeos está se tornando
cada vez mais relevante, surgindo muitos desafios relacionados com o custo computacional e a
latência, especialmente para aplicações em tempo real. Neste contexto, trabalhos importantes
destacaram muitos problemas quando se lida com grandes conjuntos de dados de vídeo ou
dados em fluxo contínuo, incluindo um elevado custo de processamento, programação impe-
rativa complexa, elevada latência no processamento de consultas e uma grande complexidade
para detectar e recuperar eventos espaço-temporais em vídeos. Além disso, não existe uma
linguagem de consulta normalizada para vídeos nem um motor de pesquisa eficiente, o que
exige uma solução pragmática, como foi o caso do ANSI SQL para bases de dados relacionais.
Do ponto de vista epistemológico e ontológico, a origem do problema estaria além das abor-
dagens atuais, atingindo seus paradigmas usuais de programação e idiossincrasias correlatas,
como a tendência ao mau uso da capacidade de processamento e o acoplamento de partes do
programa. A chamada “inadequação de paradigma” seria uma causa relevante e até primária de
problemas de desenvolvimento de software que impedem soluções inovadoras no sistema de
consulta de vídeo, tanto quanto em outros domínios que envolvem processamento distribuído e
de alta demanda. A PON introduziu uma nova forma de pensar e desenvolver software em que
pequenas entidades colaborativas executam a execução de fatos e o processamento de decisões
lógicas com base em notificações precisas. Inspirada nas lacunas atuais no domínio da consulta
de vídeo e nas vantagens do PON e das ferramentas de desenvolvimento existentes, esta tese
propõe um novo método de processamento de consultas que lida com múltiplos eventos de vídeo
e reage com baixa latência quando ocorrem correspondências. É proposta uma conformação
distinta da estrutura PON, que é aplicada à operações de consulta para evitar buscas intensivas
da base de dados, como o armazenamento, a recuperação e os gatilhos. Para efetuar pesquisas
de consulta, é proposta, desenvolvida e utilizada uma nova linguagem de consulta de vídeo.
Além disso, um novo conjunto de dados e dois estudos de caso com vários experimentos são
propostos e desenvolvidos para mostrar a viabilidade da solução baseada em PON proposta para
este domínio. Os experimentos no conjunto de dados rotulados demonstraram a adequação do
método proposto para o processamento de baixa latência com complexidade polinomial. Os
resultados são melhores do que o estado da arte, que funciona a um custo exponencial.
Palavras-chave: Método de Processamento de Consultas. Linguagem de Consulta de Videos.
Paradigma Orientado a Notificações. Conjunto de dados. Estudo de caso.


ABSTRACT
KOSSOSKI, Clayton. NOP Query – A new notification-based method for processing video
queries on the fly. 2024. 142 p. Thesis (PhD in Graduate Program in Electrical and Computer
Engineering) – Universidade Tecnológica Federal do Paraná. Curitiba, 2024.
With the rapid growth of video data, the search for events in videos is becoming increasingly
relevant, and many challenges related to computational cost and latency arise, especially for
real-time applications. In this context, important works have highlighted many issues when
dealing with large video datasets or streaming data, including high processing cost, complex
imperative programming, high latency with query processing and a lot of complexity to detect
and retrieve spatiotemporal events in videos. Additionally, there is a lack of a video standard
query language and an efficient search engine, which requires a pragmatic solution, as was the
case with ANSI SQL for relational databases. From the epistemological and ontological point
of view, the origin of the problem would be beyond the current approaches, reaching its usual
programming paradigms and related idiosyncrasies, such as the tendency to misuse processing
capacity and program part coupling. The so-called “paradigm unfitness” would be a relevant
and even primary cause of software development problems that hinder breakthrough solutions
in the video query system as much as other domains involving distributed and high-demanding
processing. Considering the need for new and efficient solutions, the so-called Notification-
Oriented Paradigm (NOP) could be a suitable alternative. NOP introduced a new way of thinking
and developing software in which small collaborative entities perform fact execution and logical
decision processing based on precise notifications. Inspired by the current gaps in the field of
video querying and the advantages of NOP and existing development tools, this thesis proposes
a new query-processing method that handles multiple video events and reacts with low latency
when matches occur. A distinct conformation of the state-of-the-art NOP Framework is proposed
and applied to query the system domain to avoid intensive database operations such as storage,
retrieval, and triggers. In order to perform query searches, a new video querying language is
proposed, developed, and used. In addition, a new dataset and two case studies with several
experiments are proposed and developed to show the feasibility of the proposed NOP-based
solution for this domain. Experiments on the labeled dataset demonstrated the suitability of the
proposed method for low-latency processing with polynomial complexity. The results are better
than the state of the art, which works at exponential cost.
Keywords: Query Processing Method. Video Query Language. Notification Oriented Paradigm.
Dataset. Case Study.


LIST OF ALGORITHMS
Algorithm 1 – Example of redundant code in Imperative Programming . . . . . . . . .
26
Algorithm 2 – Example of NOPL statements for FBE Sensor and Rule rlTriggerSensor
shown in Figure 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
Algorithm 3 – Example of NOP Framework C++ statements for FBE Sensor and Rule
rlTriggerSensor shown in Figure 2
. . . . . . . . . . . . . . . . . . . .
33
Algorithm 4 – Example of NOP sharing entities using the NOP Framework C++ 4.0 . .
36
Algorithm 5 – The SVQ query language . . . . . . . . . . . . . . . . . . . . . . . . .
59
Algorithm 6 – Query example with one predicate
. . . . . . . . . . . . . . . . . . . .
72
Algorithm 7 – Query example with two predicates . . . . . . . . . . . . . . . . . . . .
72
Algorithm 8 – Data Stream Processor pseudocode . . . . . . . . . . . . . . . . . . . .
82


LIST OF FIGURES
Figure 1 – Overview of main programming paradigms . . . . . . . . . . . . . . . . . .
25
Figure 2 – Example of instances of FBE Sensor and Rule rlTriggerSensor with their
constituents for a sensor application
. . . . . . . . . . . . . . . . . . . . .
29
Figure 3 – NOP Inference System
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
Figure 4 – Notification Flows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
Figure 5 – Notification mechanism . . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
Figure 6 – Neural networks according number of layers. a) Non-deep feedforward neural
network (shallow network). b) Deep neural network. . . . . . . . . . . . . .
44
Figure 7 – Data representations learned by a digit-classification model . . . . . . . . .
44
Figure 8 – Architecture of an image classification using CNN . . . . . . . . . . . . . .
45
Figure 9 – Processing pipeline overview . . . . . . . . . . . . . . . . . . . . . . . . .
46
Figure 10 – Basic scheme for making specialized classifiers
. . . . . . . . . . . . . . .
51
Figure 11 – The use of cascaded classifiers to process video queries . . . . . . . . . . .
52
Figure 12 – Cascade of operators and their computing cost . . . . . . . . . . . . . . . .
53
Figure 13 – Basic overview of ingestion time and query time . . . . . . . . . . . . . . .
54
Figure 14 – Ingestion and retrieval scheme of the video database.
. . . . . . . . . . . .
55
Figure 15 – How the graph database represents spatiotemporal relationships . . . . . . .
56
Figure 16 – Overview of spatiotemporal relationships . . . . . . . . . . . . . . . . . . .
59
Figure 17 – Overview of the NOP Query Method workflow . . . . . . . . . . . . . . . .
65
Figure 18 – Apache Kafka overview . . . . . . . . . . . . . . . . . . . . . . . . . . . .
66
Figure 19 – Overview of the Data Stream Collector and Stream Data Buffer sequence
diagram
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
68
Figure 20 – Overview of the components of the Data Stream Collector and Stream Data
Buffer
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
68
Figure 21 – Overview of the Query Manager and Data Stream Collector sequence diagram 70
Figure 22 – Overview of the components of the Query Manager and Stream Data Buffer
70
Figure 23 – Overview of a language recognizer . . . . . . . . . . . . . . . . . . . . . .
71
Figure 24 – Overview of the components of the Data Stream Processor and Stream Data
Buffer
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
74
Figure 25 – Overview of the Data Stream Processor and Stream Data Buffer sequence
diagram
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
75
Figure 26 – NOP Query Core overview . . . . . . . . . . . . . . . . . . . . . . . . . .
76
Figure 27 – Spatial position coordinates perspective . . . . . . . . . . . . . . . . . . . .
77
Figure 28 – Result of the Static NOP Query Chain (SQC)
. . . . . . . . . . . . . . . .
78
Figure 29 – Block diagram of the Morphable FBE
. . . . . . . . . . . . . . . . . . . .
79
Figure 30 – Class diagram of the Morphable FBE . . . . . . . . . . . . . . . . . . . . .
79
Figure 31 – Block diagram of the Morphable Rule
. . . . . . . . . . . . . . . . . . . .
80
Figure 32 – Class diagram of the Morphable Rule . . . . . . . . . . . . . . . . . . . . .
80
Figure 33 – Class diagram of the Morphable FBE and Morphable Rule
. . . . . . . . .
81
Figure 34 – Overview of Query Manager and Data Stream Processor . . . . . . . . . . .
83
Figure 35 – Data Stream Collector and Data Stream Processor . . . . . . . . . . . . . .
84
Figure 36 – Frame 1 of the example video stream . . . . . . . . . . . . . . . . . . . . .
85
Figure 37 – Frame 2 of the example video stream . . . . . . . . . . . . . . . . . . . . .
85
Figure 38 – Frame 3 of the example video stream . . . . . . . . . . . . . . . . . . . . .
86


Figure 39 – Frame 4 of the example video stream . . . . . . . . . . . . . . . . . . . . .
86
Figure 40 – Frame 5 of the example video stream . . . . . . . . . . . . . . . . . . . . .
87
Figure 41 – Frame 6 of the example video stream . . . . . . . . . . . . . . . . . . . . .
87
Figure 42 – Frame 7 of the example video stream . . . . . . . . . . . . . . . . . . . . .
88
Figure 43 – Frame 8 of the example video stream . . . . . . . . . . . . . . . . . . . . .
88
Figure 44 – Frame 9 of the example video stream . . . . . . . . . . . . . . . . . . . . .
88
Figure 45 – Frame 10 of the example video stream . . . . . . . . . . . . . . . . . . . .
89
Figure 46 – Sample of the Noscope’ Jackson Town Square dataset . . . . . . . . . . . .
91
Figure 47 – Sample of the NS100KCOLORID dataset
. . . . . . . . . . . . . . . . . .
92
Figure 48 – Processing time results considering query construction and search time using
short time window sizes.
. . . . . . . . . . . . . . . . . . . . . . . . . . .
96
Figure 49 – CPU processing time results including the NOP Query construction and
search time using large time window sizes. . . . . . . . . . . . . . . . . . .
97
Figure 50 – Memory usage results considering large time window sizes. . . . . . . . . .
98
Figure 51 – Number of Rules created considering large time window sizes.
. . . . . . .
99
Figure 52 – [Complete pipeline] CPU processing time, Memory consumption, and Rules
produced considering the NOP Query construction and search time using
large time window sizes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
Figure 53 – Instances of the OBJECT operator
. . . . . . . . . . . . . . . . . . . . . . 128
Figure 54 – Instances of the CONJ operator . . . . . . . . . . . . . . . . . . . . . . . . 129
Figure 55 – Instances of the LEFT operator . . . . . . . . . . . . . . . . . . . . . . . . 131
Figure 56 – Instances of the SEQ operator . . . . . . . . . . . . . . . . . . . . . . . . . 132
Figure 57 – Instances of the FBEs – COUNT Operator . . . . . . . . . . . . . . . . . . 133
Figure 58 – Instances of the Rules – COUNT Operator . . . . . . . . . . . . . . . . . . 134
Figure 59 – Instances of the Time Manager FBE
. . . . . . . . . . . . . . . . . . . . . 135
Figure 60 – Instances of the Time Manager Rules . . . . . . . . . . . . . . . . . . . . . 136


LIST OF TABLES
Table 1 – Video query languages and their support for common operators: ✓=“yes”,
𝑃=“partially”, −=“no” . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
60
Table 2 – Operators and queries used in the experiments following NOP Query Lang
syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
93


LIST OF ACRONYMS
ACID
Atomicity, Consistency, Isolation, and Durability
AcOP
Actor Oriented Paradigm
AgOP
Agent-Oriented Paradigm
AI
Articial Intelligence
ANTLR
ANother Tool for Language Recognition
AOP
Aspect-Oriented Paradigm
API
Application Programming Interface
CCTV
Closed-Circuit Television
CED
Complex Event Detection
CEP
Complex Event Processing
CER
Complex Event Recognition
CNN
Convolutional Neural Networks
COP
Component Oriented Paradigm
CRUD
Create, Read, Update, Delete
CV
Computer Vision
DAG
Directed Acyclic Graph
DCNNs
Deep Convolutional Neural Networks
DL
Deep Learning
DNN
Deep Neural Network
DP
Declarative Paradigm
DQC
Dynamic NOP Query Chain
EOP
Event Oriented Paradigm
FBE
Fact Base Elements
FP
Functional Paradigm
FPS
Frames per Second
GPU
Graphical Processing Unit
GPUs
Graphical Processing Units
GT Models
Ground-Truth Models
HC
Holonic Control
HCI
Human-Computer Interface
IoT
Internet of Things
IP
Imperative Paradigm
JSON
JavaScript Object Notation


LP
Logical Paradigm
ML
Machine Learning
MQTT
Message Queuing Telemetry Transport
NN
Neural Networks
NOCA
Notication Oriented Computer Architecture
NOM
Notication Oriented Software Design Methodology
NOP
Notication Oriented Paradigm
NOP Query
Notication Oriented Querying Method
NOPL
Notication Oriented Paradigm Language
NOPQL
NOP Query Lang
NoSQL
Not Only SQL
OOP
Object-Oriented Paradigm
PP
Procedural Paradigm
RBS
Rule-Based Systems
RIMON
Requirements and Interdependencies MOdeling Notation
RON
Requirements Oriented to Notications
SDEs
Simple Derived Events
SQC
Static NOP Query Chain
SQL
Structured Query Language
SVQ
Streaming Video Queries
VEQL
Video Event Query Language


SUMMARY
1
INTRODUCTION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
1.1
BACKGROUND . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
1.2
MOTIVATION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
1.3
JUSTIFICATION
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
1.4
THESIS STATEMENT
. . . . . . . . . . . . . . . . . . . . . . . . . . .
22
1.5
RESEARCH OBJECTIVES
. . . . . . . . . . . . . . . . . . . . . . . .
22
1.6
CONTRIBUTIONS
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
1.7
OUTLINE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
2
THEORETICAL BACKGROUND AND STATE OF THE ART . . . . .
24
2.1
CURRENT DEVELOPMENT PARADIGMS AND THEIR SHORTCO-
MINGS
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
2.1.1
Emerging Paradigms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
2.2
NOTIFICATION ORIENTED PARADIGM
. . . . . . . . . . . . . . .
28
2.2.1
NOP Inference System . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28
2.2.2
NOP Implementation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
2.2.3
NOP concepts and features
. . . . . . . . . . . . . . . . . . . . . . . . . .
32
2.2.3.1
Mechanism of Rules for conflict resolution . . . . . . . . . . . . . . . . . .
32
2.2.3.2
NOP entities sharing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
2.2.3.3
Formation Rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
2.2.4
NOP Framework C++ 4.0 . . . . . . . . . . . . . . . . . . . . . . . . . . .
38
2.2.5
Brief overview of the main existing contributions to the NOP
. . . . . . . .
38
2.3
RELATED TECHNOLOGIES AND STATE OF THE ART . . . . . . .
42
2.3.1
Computer Vision . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
43
2.3.2
Processing pipeline
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
45
2.3.2.1
Ingestion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
46
2.3.2.1.1
Video capture CODECs . . . . . . . . . . . . . . . . . . . . . . . . . . . .
47
2.3.2.1.2
Data preprocessing
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
47
2.3.2.1.3
Computer vision pipeline
. . . . . . . . . . . . . . . . . . . . . . . . . . .
50
2.3.2.1.4
Ingestion time and querying time
. . . . . . . . . . . . . . . . . . . . . . .
52
2.3.2.2
Storage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
54
2.3.2.3
Retrieval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
57
2.3.2.4
Consumption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
57
2.3.3
Video Query languages
. . . . . . . . . . . . . . . . . . . . . . . . . . . .
58
2.3.4
Complex Event Processing
. . . . . . . . . . . . . . . . . . . . . . . . . .
62
2.4
SUMARIZING THE EXISTING GAPS IN THE LITERATURE . . . .
63
3
NOTIFICATION ORIENTED QUERYING METHOD (NOP QUERY)
PROPOSAL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
64
3.1
NOP QUERY OVERVIEW . . . . . . . . . . . . . . . . . . . . . . . . .
64
3.2
STREAM DATA BUFFER – APACHE KAFKA . . . . . . . . . . . . .
65
3.3
DATA STREAM COLLECTOR
. . . . . . . . . . . . . . . . . . . . . .
67
3.4
QUERY MANAGER . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
69
3.5
DATA STREAM PROCESSOR . . . . . . . . . . . . . . . . . . . . . . .
73
3.5.1
NOP Query Core . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
75


3.5.1.1
Static NOP Query Chain (SQC) . . . . . . . . . . . . . . . . . . . . . . . .
76
3.5.1.2
Dynamic NOP Query Chain (DQC) . . . . . . . . . . . . . . . . . . . . . .
78
3.5.2
Didactic step by step demonstration of the NOP Query Method pipeline . . .
82
3.5.3
Reflexions about the NOP Query Method . . . . . . . . . . . . . . . . . . .
87
4
EXPERIMENTS AND RESULTS . . . . . . . . . . . . . . . . . . . . . .
90
4.1
MOTIVATIONS
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
90
4.2
THE NEW NS100KCOLORID DATASET . . . . . . . . . . . . . . . .
91
4.3
PREPARATORY STEPS
. . . . . . . . . . . . . . . . . . . . . . . . . .
92
4.3.1
Operators, Queries and Rules . . . . . . . . . . . . . . . . . . . . . . . . .
93
4.3.2
Hardware and Software Configuration
. . . . . . . . . . . . . . . . . . . .
95
4.4
CASE STUDY 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
95
4.4.1
Experiment 1: Comparison with the Literature . . . . . . . . . . . . . . . .
96
4.4.2
Experiment 2: Estimation of the Computational Complexity . . . . . . . . .
96
4.5
CASE STUDY 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
99
4.6
DISCUSSION OF THE EXPERIMENTAL RESULTS
. . . . . . . . .
99
5
CONCLUSION AND FUTURE WORK . . . . . . . . . . . . . . . . . . 103
5.1
CONCLUSION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
5.2
FUTURE RESEARCH DIRECTIONS . . . . . . . . . . . . . . . . . . . 104
REFERENCES . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
APPENDICES
127
APPENDIX A – INSTANCES OF THE FBES AND RULES – NOP
QUERY . . . . . . . . . . . . . . . . . . . . . . . . . . 128
APPENDIX B – TOKENS AND PRODUCTIONS OF THE PROPO-
SED NOP QUERY LANG . . . . . . . . . . . . . . . . 137


16
1 INTRODUCTION
This doctoral work is part of a research project on the Notification Oriented Paradigm
(NOP). The project itself is made up of a theoretical and technical basis with various develop-
ments (SIMÃO, 2005; BANASZEWSKI, 2009; RONSZCKA, 2019; NEVES, 2021). This thesis,
in particular, is focused on proposing a new and distinct method for processing video queries by
conforming the NOP and adapting of its respective materializations in a framework in order to
compare results with the state of the art.
In this introductory chapter, Section 1.1 offers an overview of video querying and a
short review of existing state-of-the-art approaches. Section 1.2 outlines the motivation behind
the study. Section 1.3 provides the justification for the research. Section 1.4 presents the thesis
statement. Section 1.5 details the research objectives of the thesis. Section 1.6 highlights the
contributions made by this work. Finally, Section 1.7 concludes the chapter with an outline of
the document.
1.1
BACKGROUND
Querying videos is an old dream of the computer vision community (OGLE; STONE-
BRAKER, 1995; LI et al., 1997). It was driven by the database community and their “swiss army
knife” tools available in the Structured Query Language (SQL). The problem is that SQL and
traditional databases work with structured data, whereas videos are composed by frames, which
are unstructured data types. Therefore, handling of unstructured data is a difficult task because it
requires advanced hardware and software algorithms to process videos and extract high-level
information from raw data, such as some suitable data relating to people, objects, video events
and actions (KANG et al., 2017; KANG et al., 2019a).
Recently, video querying in large-scale datasets or streaming contexts has gained
increased attention because of its broad range of applications. In particular, Complex Event
Detection (CED) presents many challenges, including object detection, tracking, identifying
spatiotemporal relationships, and event matching. These tasks are often made more difficult by
factors like environmental changes, obstructions, and tracking errors (HONARPARVAR et al.,
2024).
For example, traffic must be constantly supervised in smart cities (LU et al., 2015;


17
STONEBRAKER et al., 2020). In this context, traffic authorities may need a system that allows
direct queries to detect high-volume traffic, locate vehicles by features (e.g., license plate, color
or model), or track suspicious vehicles that are traveling together such as a criminal escort car,
among others (STONEBRAKER et al., 2020; HSIEH et al., 2018; HSIEH, 2019; KANG et al.,
2019a).
Due to the high volume, speed and variety of data produced by large scale video
querying/retrieval systems, these can be considered big data applications (ZHANG et al., 2017;
LU et al., 2016; ALAM et al., 2020a). Unlike traditional data, the term Big Data refers to
large, growing datasets that include heterogeneous formats: structured, unstructured and semi-
structured data. Big Data has a complex nature that requires powerful technologies and advanced
algorithms. Thus, traditional processing and analysis tools can no longer be efficient in the
case of big data applications (OUSSOUS et al., 2018). For instance, most data scientists and
experts define Big Data by the following three main characteristics (called 3Vs) (FURHT;
VILLANUSTRE, 2016; OUSSOUS et al., 2018):
• Volume: It refers to large volumes of digital data generated continuously from various
devices and applications (e.g. IP cameras, smartphones, social networks, sensors, records,
etc.)
• Velocity: It refers to data that is generated quickly and must be processed quickly in order
to extract useful information and relevant insights.
• Variety: It refers to data generated from various distributed sources and in various formats
(e.g. videos, documents, comments, logs). Typically, large datasets can consist of structured
and unstructured data, public or private, local or distant, shared or confidential, complete
or incomplete, etc.
Fortunately, in the last ten years at least, there has been a lot of progress in the de-
velopment of software and hardware that is making it possible to work with large masses of
video. Particularly, the area of computer vision has evolved due to advances in machine learning,
including deep learning (GOODFELLOW et al., 2016; ROSEBROKE, 2017; CHOLLET, 2021),
detection models (FARHADI; REDMON, 2018; BOCHKOVSKIY et al., 2020), large training
datasets (KANG et al., 2017; WEN et al., 2020; JODOIN et al., 2014; MOT2016, 2022; XIPG,
2021; RISTANI et al., 2016), graphical processing libraries1, video description (AAFAQ et
1
https://docs.opencv.org/4.x/index.html


18
al., 2019), and development frameworks (POUYANFAR et al., 2018a; DONG et al., 2021).
With regard to advances in hardware, it is worth pointing out the distributed processing of large
volumes of data and, in particular, the use of Graphical Processing Unit (GPU) to speed up model
training and object detection in big data context (POUYANFAR et al., 2018b; ALAM et al.,
2020b).
These advances, however, are not enough for the issues related to video querying,
especially regarding computational cost and latency (KANG et al., 2017; YI et al., 2017; HSIEH
et al., 2018; KANG et al., 2019a; YADAV et al., 2020; HWANG et al., 2022). In these literature,
computational cost refers to the processing time of a video querying application and latency
refers to the time required between starting a query and retrieving it when the query matches
with an event in video. Both these concepts are directly related to the tools and processing steps
used in the processing pipeline of a video querying application. It is particularly relevant because
video querying at scale is much more challenging than a standalone application on a single
node. The complexity involves many hardware, software, network connections, databases, and
high-level applications.
1.2
MOTIVATION
Important works have highlighted many disadvantages when dealing with querying
video events in large datasets or streaming data, including high processing cost (KANG et al.,
2017; KANG et al., 2019a; HWANG et al., 2022), complex imperative programming (KANG et
al., 2019a; KANG, 2022), high latency with query processing (HSIEH et al., 2018; HSIEH, 2019;
YADAV, 2019) and a lot of complexity to detect and retrieve spatiotemporal events (YADAV;
CURRY, 2019a; YADAV, 2021). Additionally, there is a lack of a standard query language and
an efficient search engine, which requires a pragmatic solution, as was the case with ANSI SQL
relational databases back in time (MELTON; SIMON, 1993). Hence, as already stated, even
though there have been general technical advances in software and hardware, the state of the art
is not yet able to provide satisfactory solutions to the problems mentioned above.
Currently, the processing pipeline of videos at scale comprises four main stages (XU et
al., 2019): ingestion, storage, retrieval, and consumption, which is briefly described below with
the respective challenges:
• Ingestion: It is responsible for computing fast operations, such as reading video stre-


19
ams from IP cameras, IoT devices or video files. Various decoding and data pre-
processing/cleaning operations can be used to convert the data into frames and videos.
• Storage: It receives data from the ingest and stores frames or videos in relational databases
or NoSQL databases. Storage can be of entire videos, parts of videos (scenes), specific
frames containing data on interesting objects or events (keyframe), individual frames, or
even spatiotemporal info (e.g., a car to the left of a truck).
• Retrieval: It computes heavy query tasks, such as event detection, video description, among
others.
• Consumption: And finally, the data produced by the retrieval phase feeds consumers with
some meaningful alerts and reports, usually using a high-level interface such as a website
or an application. This data can also be used for decision-making.
For example, the ingestion phase depends on the throughput of the detection models
and the hardware available to process a large data stream. According to the Keras page of APIs
and models2, using a powerful server, the Xception model can process 125 FPS or about 4 video
streams at 30 FPS, and the VGG16 model can process 238 FPS or about 8 video streams at 30
FPS. So this could be a factor that limits throughput when considering a large number of video
streams in a smart city context.
The storage phase, on the other hand, typically uses relational or NoSQL databases
to store various types of data. Both have advantages and disadvantages. Relational databases
allow complex queries (e.g. aggregation, joins) and triggers that can be used to alert when event
matches occur. However, they are considered slow with large masses of data. For example, some
authors who have used relational databases (e.g., Postgres) have commented that application
bottlenecks have occurred due to the dependence on triggers (SIPSER, 2020; STONEBRAKER
et al., 2020). On the other hand, Not Only SQL (NoSQL) databases are gaining attention for
being more suitable for dealing with big data, as they are schema-free and include features such as
horizontal scalability, data replication, distributed indexing and simple Application Programming
Interface (API). In the literature, recent approaches have adopted NoSQL, such as MongoDB
(HSIEH, 2019; HSIEH et al., 2018) and graph databases (POMS et al., 2018; QIN et al., 2021;
YADAV; CURRY, 2019a; YADAV, 2021; YADAV et al., 2020). In particular, graph databases are
considered suitable for storing spatial relationships (e.g. left, right) and temporal relationships
2
https://keras.io/api/applications/


20
(e.g. before, after) among objects. For example, the authors in Yadav e Curry (2019a) store
metadata for each object and its relationship in a graph database, where each node represents
an object with its attributes (e.g. label and color) and the spatiotemporal relationships between
objects are represented by the edges connected to other nodes. Therefore, for each frame read,
the graph database must be updated with new attributes or additional information of nodes and
edges.
The recovery phase usually works in an offline context, i.e., at a different time to the
ingestion phase, because it involves heavy tasks such as query processing, inference using
Ground-Truth Models (GT Models), cluster analysis, complex database aggregations, and ex-
pensive machine learning operations (HSIEH et al., 2018; HSIEH, 2019; ZHANG et al., 2017;
ANDERSON et al., 2019). For this reason, it is usually not possible to run queries on videos
with low latency or in a real-time context.
Finally, the consumption phase focuses on offer some human-machine interaction, such
as through a web page or mobile application, to display alerts when the query matches events
in the videos. It also involves writing queries using a high-level language, if available. In the
literature, for example, there are few works that offer a user interface or even a query language
for interacting with the (HSIEH et al., 2018; KANG et al., 2019a) system.
Moreover, several streaming video queries applications are written in Python language
(KANG et al., 2017; YI et al., 2017; KAKKAR et al., 2023; HAYNES et al., 2018; KHANI et
al., 2023; MOLL et al., 2022; KANG et al., 2019a; KANG et al., 2021; YADAV et al., 2020;
YADAV, 2021; YADAV et al., 2021a; CHUNDURI et al., 2022), including video storage systems
(HAYNES et al., 2021; KRISHNAN et al., 2018; XU et al., 2019). Although popular in this area,
Python is one of the least efficient in terms of processing time and memory consumption among
the dozens of programming languages analyzed (PEREIRA et al., 2021; PEREIRA et al., 2017).
The best programming languages in terms of these characteristics are C, Rust and C++.
From the epistemological and ontological point of view, the origin of the problem
would be beyond the current approaches, reaching its usual programming paradigms and related
idiosyncrasies, such as the tendency to misuse processing capacity and program part coupling
(LINHARES et al., 2020). The so-called “paradigm unfitness” would be a relevant and even
primary cause of software development problems that hinder breakthrough solutions in the video
query system as much as other domains involving distributed and high-demanding processing
(SIMÃO; STADZISZ, 2008; SIMÃO et al., 2009; RONSZCKA, 2012; RONSZCKA, 2019).


21
In fact, computer systems are developed with programming languages from current paradigms,
thus inheriting their idiosyncrasies (and disadvantages). Thus, the level of abstraction of a
programming language is linked to the essence of its paradigms (SEBESTA, 2019). In short,
there are two major programming paradigms, namely the Imperative Paradigm (IP) and the
Declarative Paradigm (DP), which intersect in some respects, with the DP sometimes being
considered an abstraction or high-level layer on top of the IP (BANASZEWSKI, 2009; XAVIER,
2014; KAISLER, 2005; GABBRIELLI; MARTINI, 2010).
The IP can be divided into two other paradigms, the Procedural Paradigm (PP) and
the Object-Oriented Paradigm (OOP), with the PP governing languages such as C and Pascal
and the OOP governing languages such as Java and C#, with some hybridizations such as C++
and Python (BANASZEWSKI, 2009; ROY, 2009; KAISLER, 2005). The DP, in turn, can be
subdivided into two other paradigms such as the Functional Paradigm (FP) and the Logical
Paradigm (LP), with the FP governing languages such as LISP (which is a hybrid of the PP)
and the LP governing languages such as Prolog and ASP (ROY; HARIDI, 2004; GABBRIELLI;
MARTINI, 2010). In fact, it is common for programming languages to be based on more than one
(sub)paradigm, such as the examples mentioned above. In addition to these, current programming
languages such as Javascript, Swift, Scala, Ruby, Python, Go and Lua also make use of multiple
paradigms in their essence.
However, in general, it is indifferent whether these (sub)paradigms are used together
or not, in the sense that they all have the same (or at least similar) problems, such as inade-
quate syntax, structural and temporal redundancies and, in particular, the strong coupling of
computational entities (SIMÃO; STADZISZ, 2008; SIMÃO et al., 2009; SIMÃO; STADZISZ,
2009). This coupling and also the redundancies of IP/DP exist due to an orientation towards
the process of logical-causal evaluation based on searches, usually in a monolithic form, in
passive factual entities (SIMÃO; STADZISZ, 2008; SIMÃO et al., 2009; SIMÃO; STADZISZ,
2009). Thus, there are still open questions about software development, in terms of enabling the
composition of non-redundant and non-coupled code (GABBRIELLI; MARTINI, 2010; SIMÃO
et al., 2012). Therefore, evidently, new solutions that simplify the task of building software with
features that address these issues are desirable and necessary. In this context, the programming
and even computing solution called the Notification Oriented Paradigm (NOP) was proposed
with the aim of mitigating the highlighted problems (SIMÃO, 2005; SIMÃO; STADZISZ, 2008;
SIMÃO et al., 2009; SIMÃO; STADZISZ, 2009; BELMONTE et al., 2012; SIMÃO et al., 2012;


22
RONSZCKA et al., 2015; LINHARES et al., 2020).
In short, the so-called NOP solves, in terms of a model, some of the problems that exist
in the usual software application programming paradigms, from single-process environments to
fully multiprocess or distributed environments. Basically, the NOP execution mechanism prevents
the existence of structural redundancies (i.e., code repetition) and temporal redundancies (i.e.,
unnecessary code re-evaluation), which are common problems in other programming approaches.
Moreover, the NOP execution mechanism unifies some of the characteristics and advantages
found in DP (i.e., representation of knowledge in rules) and IP (i.e., flexibility of expression and
appropriate level of abstraction) (RONSZCKA, 2019; SIMÃO; STADZISZ, 2008; SIMÃO et al.,
2009; SIMÃO; STADZISZ, 2009).
1.3
JUSTIFICATION
The NOP aims at promoting better performance in system execution and somehow
easier construction of complex systems, especially parallel and distributed systems (LINHARES
et al., 2020; SIMÃO; STADZISZ, 2008; SIMÃO et al., 2009; SIMÃO; STADZISZ, 2009).
Essentially, the NOP splits a computational system into collaborative and decoupled entities
with minimal sub-entities. Their decoupled notifier sub-entities collaborate by means of a well-
orchestrated and precise notification chain. It indeed avoids redundancies and coupling, thereby
savings processing power, and allowing processing distribution.
Several researchers have highlighted the advantages of NOP, with some specifically fo-
cusing on its benefits for software development (BANASZEWSKI, 2009; WIECHETECK, 2011;
VALENçA, 2012; RONSZCKA, 2012; MENDONÇA, 2020; NEVES et al., 2021), programming
language (OSHIRO, 2021; RONSZCKA, 2019; RONSZCKA et al., 2017a; FERREIRA, 2015),
computational parallelism (NEGRINI et al., 2019; SCHÜTZ et al., 2018; KERSCHBAUMER,
2018), and low-cost operations (SIMÃO et al., 2012; RONSZCKA et al., 2015; RONSZCKA et
al., 2017b; RONSZCKA, 2019), among others.
This thesis introduces a new approach to processing video queries. It addresses existing
gaps in video querying and leverages the benefits of NOP and current development tools. The
proposed method efficiently handles multiple video events and provides quick responses when
matches are found.


23
1.4
THESIS STATEMENT
The aim of this thesis is to enable low-cost, low-latency querying of video events with
the following research question:
Is it possible to develop a method based on the Notification Oriented Paradigm for
processing video events with low computational cost and low latency?
1.5
RESEARCH OBJECTIVES
The main goal of this thesis is to propose and evaluate a new method for querying video
events that is both cost-effective and low-latency, using concepts and tools from the Notification
Oriented Paradigm.
In order to accomplish this, the following specific objectives were proposed:
1. Propose a new video querying method based on the Notification Oriented Paradigm data
flow.
2. Adapting NOP and the NOP Framework C++ 4.0 with new capabilities to support the
proposed method.
3. Investigate a distributed architecture for a big data application in the domain of video
querying, utilizing the NOP suite of available tools.
1.6
CONTRIBUTIONS
This work presents three main contributions:
• The Notification-Oriented Querying Method (NOP Query).
• New features called Morphable FBE and Morphable Rule was added to NOP through the
proposed NOP Query Core.
• A big data pipeline designed for processing the NOP Query Method.
Additionally, three derived contributions:
• The introduction of a novel video query language, called NOP Query Lang (NOPQL).


24
• A detailed case study that systematically assesses the performance of NOP Query, focusing
on CPU processing time, memory usage, and the number of Rules generated during the
experiments.
• A new large-scale labeled traffic surveillance dataset used in the case study. It was made
publicly available to the research community to support the reproducibility of the experi-
ments.
It is important to note that this thesis does not contribute directly to the field of computer
vision, as it primarily focuses on the query engine responsible for processing events in videos.
Therefore, it presents a significant contribution to the field of software engineering and complex
event processing and an indirect contribution to the field of computer vision.
1.7
OUTLINE
Chapter 2 presents the theoretical background and the literature review. Chapter 3
presents the proposed NOP Query Method. Chapter 4 presents the experiments and results
that demonstrate the applicability and viability of the proposed method. Chapter 5 presents the
conclusions and perspectives for future works beyond this thesis.


25
2 THEORETICAL BACKGROUND AND STATE OF THE ART
This Chapter presents the theoretical aspects, technologies, and related work used in
the development of this research. Section 2.1 presents a brief overview of current development
paradigms and their drawbacks. Section 2.2 presents the Notification Oriented Paradigm and its
advantages over other paradigms. Section 2.3 reviews some technologies related to this work,
including Computer Vision, Processing Pipeline, Video Query Languages, and Complex Event
Processing. Finally, section 2.4 summarizes the main gaps found in the literature reviewed.
2.1
CURRENT DEVELOPMENT PARADIGMS AND THEIR SHORTCOMINGS
Works that explore NOP usually present a broad overview of programming paradigms
so as to characterize NOP as a new development paradigm. Many productions and advances
on NOP have emerged as master’s dissertations (WIECHETECK, 2011; FERREIRA, 2015;
KOSSOSKI, 2015; OSHIRO, 2021; BANASZEWSKI, 2009; VALENçA, 2012; PORDEUS,
2017; NOVAES, 2019; NEGRINI, 2019; NEVES, 2021; BABU, 2022), doctoral theses (SIMÃO,
2005; LINHARES, 2015; SCHUTZ, 2019; KERSCHBAUMER, 2018; RONSZCKA, 2019;
MENDONÇA, 2020), and also as publications in scientific journals (SIMÃO et al., 2012;
RONSZCKA et al., 2015; RONSZCKA et al., 2017b; KERSCHBAUMER et al., 2018; SCHÜTZ
et al., 2018; LINHARES et al., 2020; MENDONÇA et al., 2020; PORDEUS et al., 2021; FABRO
et al., 2021; KOSSOSKI et al., 2024) . Such productions usually highlight the advantages of NOP
over existing approaches and present the current state of the art (PORDEUS, 2017; SCHUTZ,
2019; RONSZCKA, 2019; MENDONÇA, 2020; NEVES, 2021). The content of this Section has
been derived from the above references.
The demand for software is increasing every year, but it cannot meet the industry’s
needs due to the “software crisis”, which dates back to the 1960s (NAUR; RANDELL, 1968)
and continues throughout the history of software engineering. The problem is related to the
difficulty of writing valuable programs that meet the user’s requirements, considering issues
such as ease of maintenance, development within restricted time, and foreseen budget (ZYKOV,
2018; JOHANSON; HASSELBRING, 2018).
Over the years, software complexity has increased due to the evolution of computers
and systematic demands. For instance, more recent issues include parallelism, distribution,


26
optimization, software quality, human-related factors, and energy efficiency (ZYKOV, 2018;
MENDONÇA, 2020; CORRAL-GARCÍA et al., 2019; PEREIRA et al., 2021). Therefore, the
usual software development process would currently require high-level programming languages
to create applications.
However, programming languages have not evolved as expected, which is due to
their paradigms. According to Roy (2009), programming languages belong to one or more
development paradigms or “concepts” which are abstractions that govern the way that the
programmer make a computer program. Following this literature, at least 27 programming
(sub) paradigms exist, but many programming languages are hybrid and use features from
more than one paradigm. Besides, even if the classification given is by one given author is not
absolute, since it demands on considered parameter and viewpoint. As presented by some authors
(BANASZEWSKI, 2009; GABBRIELLI; MARTINI, 2010; BROOKSHEAR, 2011; SEBESTA,
2019; RONSZCKA, 2019), the usual programming paradigms (dominant and emerging) could be
classified as subsets of two larger paradigms, the Imperative Paradigm (IP) and the Declarative
Paradigm (DP). Figure 1 illustrates the classification of these paradigms in a more summarized
way.
Figure 1 – Overview of main programming paradigms
Programming
Paradigms
Imperative
Paradigm
Declarative
Paradigm
Procedural
Paradigm
Object Oriented
Paradigm
Logic
Paradigm
Functional
Paradigm
Agent Driven
Paradigm
Aspect Oriented
Paradigm
Component
Oriented Paradigm
Data Oriented
Paradigm
Event Oriented
Paradigm
Dominant Paradigms
Emergent Paradigms
Source: Developed by the author. Based on Ronszcka (2019).
As Figure 1 illustrates, IP can be understood as consisting of the Procedural Paradigm
(PP) and the Object-Oriented Paradigm (OOP), which differ essentially in the way elements and
instructions are represented and organized, with OOP being considered richer and supposedly


27
more structured in terms of code expression. The DP, in turn, can be understood as consisting
essentially of the Logical Paradigm (LP) and the Functional Paradigm (FP).
Basically, in the IP, the developers must describe how the program executes step by
step. Therefore, an imperative program is a set of instructions given to a computer, and the
running order is very relevant. Also, the execution mechanism consists of searches that run over
passive entities such as variables and data structures corresponding to the data and state. Due
to the repetition of the search and the passivity of the elements present in the procedural and
object-oriented languages, code snippets tend to become interdependent, leading to couplings
and related redundancy issues in program execution (BANASZEWSKI, 2009; RONSZCKA,
2019). Algorithm 1 presents an example of redundant code in IP.
Algorithm 1 – Example of redundant code in Imperative Programming
1: ...
2: while (true) do
3:
if ((object_1.attribute_1 = 1) and
4:
(object_2.attribute_2 = 1) and
5:
(object_3.attribute_3 = 1))
6:
then
7:
object_1.method_1();
8:
object_2.method_1();
9:
object_3.method_1();
10:
end_if
11: . . .
12:
if ((object_1.attribute_1 = 1) and
13:
(object_2.attribute_n = n) and
14:
(object_3.attribute_n = n))
15:
then
16:
object_1.method_n();
17:
object_2.method_n();
18:
object_3.method_n();
19:
end_if
20: end_while
21: . . .
Source: Developed by the author. Based on Simão et al. (2012).
In this context, causal expressions are passively evaluated, causing the so-called tem-
poral and structural redundancies (BANASZEWSKI, 2009). Essentially, passive elements are
variables and data structures, logical-causal expressions are “if-then” structures or similar. Tem-
poral redundancy occurs when there is the revaluation of unnecessary causal expressions in the
presence of already evaluated and unchanged states. In contrast, structural redundancy occurs
when knowledge about a state resulting from evaluating a logical expression is not shared among
other relevant causal expressions in different parts of code, causing unnecessary revaluations
(SIMÃO et al., 2009; BANASZEWSKI, 2009; GABBRIELLI; MARTINI, 2010; SIMÃO et al.,


28
2012; RONSZCKA, 2019). For example, in the C/C++ language, the decision statements (e.g.,
if-else and switch) are executed in repetition loops (e.g., for, while, do-while).
In contrast, the Declarative Paradigm proposes to solve some of the deficiencies of the
Imperative Paradigm, mainly those related to the difficulty of programming in multicore environ-
ments and structural and temporal redundancies (RONSZCKA, 2019). However, most of these
deficiencies persist due to the execution mechanisms based on searches under passive elements,
which reproduce these same problems. Additionally, the use of expensive data structures makes
this paradigm slow (BANASZEWSKI, 2009; NEVES, 2021; RONSZCKA, 2019).
Still, declarative programming languages have a more simplified programming model
but do not offer the same flexibility as imperative languages. Because of that, there are limitations
to writing efficient code. Finally, declarative programming needs better decoupling support and
complicates parallel and distributed processing (LINHARES, 2015).
Furthermore, depending on the point of view, PP, OOP, LP, FP could be considered
paradigms and not subparadigms, even though they have characteristics that are closer to each
other (RONSZCKA, 2019). Hence, programming languages often include more than one current
(sub)paradigm, such as C++, which is procedural and object-oriented. There are even languages
that intersect paradigms, such as LISP, which has logical-declarative and imperative-procedural
aspects.
2.1.1
Emerging Paradigms
With regard to the second layer of paradigms that represent emerging paradigms,
showed in Figure 1, there are other hybridisms. Generally, emerging programming paradigms are
established by means of an archetype or framework in a materialization of a dominant paradigm,
which forms an intermediate layer between the concepts of the emerging paradigm and the
dominant paradigm (VALENçA, 2012; FERREIRA, 2015; NEVES, 2021).
Thus, emerging paradigms can in some cases be implemented under the principles of
different dominant paradigms. An example would be the case of the Agent-Oriented Paradigm
(AgOP), which has been implemented using imperative and declarative approaches. Emerging
paradigms can also be the subject of hybrid multi-paradigm implementation (BANASZEWSKI,
2009; XAVIER, 2014; RONSZCKA, 2019).
However, the dominant paradigms IP and DP have similar problems of redundancies,
couplings, and unnecessary processing (BANASZEWSKI, 2009; NEVES, 2021; LINHARES,


29
2015; RONSZCKA, 2019). Due to this fact, they inherit the reported problems but bring some
new features. The best-known emerging paradigms are Component Oriented Paradigm (COP),
Event Oriented Paradigm (EOP), Aspect-Oriented Paradigm (AOP), AgOP, and Actor Oriented
Paradigm (AcOP) (RONSZCKA, 2019).
Although each paradigm has features and strengths, programming languages lack ad-
vantages for writing clean code, minimal coupling, and avoiding redundancies. These drawbacks
affect the computational cost, code reuse, parallel, and distributed processing (BANASZEWSKI,
2009; SIMÃO et al., 2009; SIMÃO; STADZISZ, 2009; SIMÃO et al., 2012). To summarize,
the software industry faces problems related to low productivity, the demand for high-quality
software, and increased complexity, and the current paradigms do not meet such needs.
2.2
NOTIFICATION ORIENTED PARADIGM
The Notification Oriented Paradigm (NOP) is an emerging paradigm that originated
from a manufacturing discrete control solution (SIMÃO; STADZISZ, 2009), which later evolved
into a general discrete control solution, an alternative inference solution, and then a programming
paradigm and even a computational paradigm (SIMÃO et al., 2012). As a main differential,
NOP has two groups of distinct processing entities, namely: factual-executional entities and
logical-causal entities, which collaborate through punctual, precise notifications.
The factual-executional entities deal with the execution of procedures/actions that
change their states, whereas the logical-causal entities decide which actions should be executed.
In turn, the fact-execution entities are the Fact Base Elements (FBE) with their Attributes and
Methods. The logical-causal entities are the Rules elements with their Conditions-Premises and
Actions-Instigations (LINHARES et al., 2020; RONSZCKA et al., 2017b). Still, FBEs and Rules,
with their constituents, can be and usually are represented in a declarative way (NEVES et al.,
2021).
For illustration, Figure 2 presents an example of the NOP entities for a given sensor
application. The FBE named Sensor, somehow similar to an instance of a class in the Object-
Oriented Paradigm (OOP), represents a sort of notifier instance composed of two boolean
Attributes, atIsRead and atIsActivated, and a Method named mtTrigger that sets the values of
atIsRead to true and atIsActivated to false. In turn, the associated notifiable Rule rlSensorTrigger
comprises a Condition related to Premises and an Action related to an Instigation. When both
Condition’s Premises are true after notifications of the pertinent Attributes, it fires the Rule


30
rlSensorTrigger, which causes the Action’s Instigation to start the Method mtTrigger from the
FBE Sensor. As the example suggests, the FBE and Rule constituents collaborate through precise
notifications.
Figure 2 – Example of instances of FBE Sensor and Rule rlTriggerSensor with their constituents for a sensor
application
Instance
Attribute Bool atIsRead
Attribute Bool atIsActivated
Method mtProcess
atIsRead <- True
atIsActivated <- False
Condition
If
Action
Instigation
Then
Notify
Notify
Instigate
Premise(s)
Rule SensorRule.N
Reference Operator Value
Instance
FBE Sensor.N
FBE Sensor.N Attribute atIsRead       =      False &
FBE Sensor.N Attribute atIsActivated =      True
Instigate FBE Sensor.N Method mtProcess()
Source: Developed by the author. Based on Neves et al. (2021)
2.2.1
NOP Inference System
Actually, the core mechanism of the paradigm is the so-called NOP Inference System
(SIMÃO; STADZISZ, 2002; SIMÃO; STADZISZ, 2009; PETERS et al., 2012), which is modeled
in Figure 3 and exemplified in Figure 4. Each NOP entity can send and/or receive precise and
pertinent notifications, thereby allowing the evaluation of states only when a notification arrives.
This collaborative notification-oriented behavior provides a new form to develop and execute
software (and even hardware) applications based on small reactive notifiable entities (LINHARES
et al., 2020; SIMÃO et al., 2012).
Figure 3 – NOP Inference System
Rule
Instigation
1
1
0..*
1..*
1..2
0..*
1..*
1
1
0..*
1..*
0..*
1
0..*
1
Activate
Instigate
Change state
*
*
Notify state
Notify state
Action
Condition
FBE
Method
Attribute
Premise
Source: Kossoski et al. (2024)


31
The following items explain the NOP entities according to the inference chain, taking
into account Figure 3 and Figure 4:
• Fact Base Element (FBE): Entity (e.g., a type or class) that contains the notifier Attributes
and inciteful Methods.
• Attribute: Entity that is responsible for storing a value that represents property states of an
FBE and can precisely notify related Premises when their value changes.
• Premise: Entity that, after being notified by an Attribute, compares that Attribute with
another Attribute or a constant via a logic-relational operator (e.g., =,̸ =, >, <), and
subsequently notifies related Condition when its logical state changes.
• Condition: Entity that groups one or more Premises and, when notified by any of them,
performs a logical operation (e.g., conjunction or a disjunction) over their states and
notifies its concerned Rule if its logical value changes.
• Rule: Entity with a Condition and an Action that determines the execution of its Action
when its Condition is approved (e.g., its logical state is true).
• Action: Entity that, when instigated by its Rule, activates its Instigations to execute,
properly parametrizing them if necessary.
• Instigation: Entity related to one or more Actions that, when instigated by an Action,
instigates a set of Method entities to execute, properly parametrizing them if necessary.
• Method: Entity that, when instigated by an Instigation, executes a function or service of
a FBE and, therefore, may change the states of Attributes, thereby feeding a notification
inference cycle.
The NOP organization reduces or even eliminates some of the issues concerning classi-
cal development paradigms, such as the IP and DP, which, respectively, and even notably, include
OOP and Rule-Based Systems (RBS) (RONSZCKA et al., 2017b; LINHARES et al., 2020).
Examples of those issues are the often strong coupling of code parts and the related structural
and temporal redundancies concerning logical-causal evaluation processing (RONSZCKA et al.,
2017b).
The problems mentioned above do not happen in NOP since the precise notifications,
e.g., between Attributes and Premises, avoid temporal redundancy. Also, the Conditions sharing


32
Figure 4 – Notification Flows
FactBase1
Attribute1
Attribute2
AttributeN
MethodN
Method2
Method 1
Premise1
Premise2
Premise3
PremiseN
Instigation1
Instigation2
Instigation3
InstigationN
Condition1
Action1
Rule2
Condition2
Action2
Rule1
FactBaseN
Attribute1
Attribute2
AttributeN
MethodN
Method2
Method 1
Condition3
Action3
RuleN
Condition4
Action4
Rule3
Source: Kossoski et al. (2024)
Premise collaborations avoid structural redundancy. In this sense, NOP differs from OOP
approaches because it is not loop-oriented, and NOP differs from rule-based approaches because
it does not have a monolithic factual search-oriented inference engine (SIMÃO et al., 2009;
SIMÃO; STADZISZ, 2009; RONSZCKA et al., 2015; LINHARES et al., 2020).
To summarize, the NOP allows software development with at least three elementary
properties (SIMÃO; STADZISZ, 2002; SIMÃO; STADZISZ, 2008; RONSZCKA, 2019; LI-
NHARES et al., 2020).
1. High-level rule-oriented modeling and programming, which helps easiness in some softwa-
re/system development (RONSZCKA, 2019).
2. Avoidance of structural and temporal redundancies, which allows achieving proper system
performance (SIMÃO; STADZISZ, 2008; SIMÃO; STADZISZ, 2009; RONSZCKA,
2019).
3. Implicit entity decoupling, which can favor parallel and/or distributed computing (KERS-
CHBAUMER, 2018; LINHARES, 2015; NEGRINI, 2019; FIGUEIREDO, 2022).


33
More detailed information about the NOP and its extensive research can be found in
other works (LINHARES, 2015; RONSZCKA, 2019; MENDONÇA, 2020; OSHIRO, 2021; NE-
VES et al., 2021; LINHARES et al., 2020; KERSCHBAUMER et al., 2018; KERSCHBAUMER,
2018; SIMÃO et al., 2014).
2.2.2
NOP Implementation
The NOP state-of-the-art, named Notification Oriented Paradigm Language (NOPL),
combines a programming language and a compilation system for specific targets. Despite being
very performant, the NOPL was not yet applied to large or industrial-level projects. For now, it is
used to demonstrate NOP properties in academic and benchmark applications (RONSZCKA,
2019; FABRO et al., 2021). Alternatively, the NOP state-of-techniques is the so-called NOP
Framework C++ 4.0/4.5 (NEVES, 2021; NEVES et al., 2021; BABU, 2022) which would be
proper nowadays for large or industrial projects. This framework is an evolution of the previous
ones and achieved maturity to be more extensively applied. As it is a notification-oriented
framework over C++, changing the usual way that C++ operates, it is naturally less performant
than the quite prototypal NOPL Technology with dedicated language and compilers. Nevertheless,
this framework is still performant and stable for real NOP applications (BABU, 2022; FABRO et
al., 2021; PORDEUS et al., 2021; LEDESMA; SIMÃO, 2022).
Considering the example of Figure 2, Algorithm 2 presents the corresponding code
for NOPL, and Algorithm 3 presents the corresponding code using NOP Framework C++ 4.0.
More details about the NOPL can be found in Ronszcka et al. (2017a), Ronszcka (2019), Negrini
(2019), Fabro et al. (2021), Oshiro (2021) and the NOP Framework C++ 4.0 can be found
in Neves (2021), Neves et al. (2021), Babu (2022), Ledesma e Simão (2022). Currently, the
framework is available to the community 1 and its structure and details are widely disclosed in
the academy (RONSZCKA et al., 2017b; RONSZCKA et al., 2015; BABU, 2022), including the
works cited in this Section.
2.2.3
NOP concepts and features
In addition to the general structure of the NOP, organized through the model of reactive
and notifying entities, a set of concepts and functionalities are essential for the proper organization
1
https://nop.dainf.ct.utfpr.edu.br/nop-public


34
Algorithm 2 – Example of NOPL statements for FBE Sensor and Rule rlTriggerSensor shown in Figure 2
1: FBE Sensor
2:
private boolean atIsRead = false
3:
private boolean atIsActivated = false
4:
private method mtTrigger
5:
assignment
6:
this.atIsRead = true
7:
this.atIsActivated = false
8:
end_assignment
9:
end_method
10:
rule rlSensorTrigger
11:
condition
12:
subcondition
13:
premise prIsReadFalse
14:
this.atIsRead == false
15:
end_premise
16:
and
17:
premise prIsActivated
18:
this.atIsActivated == true
19:
end_premise
20:
end_subcondition
21:
end_condition
22:
action sequential
23:
instigation sequential
24:
call this.mtTrigger();
25:
end_instigation
26:
end_action
27: end_rule
28: end_fbe
and execution of the notification flow. In this context, the following subsections explore the
details of the main resources and functionalities of the NOP.
2.2.3.1
Mechanism of Rules for conflict resolution
In general, one of the key features of NOP execution is the decoupled processing of
the elements within its model, which can even be parallelized if the architecture supports it. A
critical aspect of NOP execution involves identifying and resolving potential conflicts during
execution (PORDEUS, 2017; RONSZCKA, 2019). Essentially, a conflict arises when two or
more entities (e.g., multiple Rules) simultaneously depend on the same shared resource (e.g., an
Attribute, Premise, or Condition). Since the shared resource must be used exclusively by only
one entity at any given time, this creates a conflict (SIMÃO; STADZISZ, 2010).
For example, when controlling a car, a conflict occurs if one approved Rule attempts to
move the car right while another Rule attempts to move it left. In this scenario, the FBE Car, its
State Attribute, and its Move Method are shared and exclusive. To address such conflicts, a stra-
tegy must be implemented to prevent them (PORDEUS, 2017; RONSZCKA, 2019). Additionally,


35
Algorithm 3 – Example of NOP Framework C++ statements for FBE Sensor and Rule rlTriggerSensor shown
in Figure 2
1: /* Include the NOP Framework C++ 4.0 */
2: #include “libnop/framework.h”
3:
4: /* Create the class Sensor */
5: class Sensor
6: {
7: public:
8:
9:
/* Create the Attribute atIsRead */
10:
NOP::SharedAttribute<bool> atIsRead
11:
{ NOP::BuildAttribute<bool>(false) };
12:
13:
/* Create the Attribute atIsActivated */
14:
NOP::SharedAttribute<bool> atIsActivated
15:
{ NOP::BuildAttribute<bool>(false) };
16:
17:
/* Create the Premise prIsRead */
18:
NOP::SharedPremise prIsRead
19:
{ NOP::BuildPremise(this.atIsRead, false, NOP::Equal()) };
20:
21:
/* Create the Premise prIsActivated */
22:
NOP::SharedPremise prIsActivated
23:
{ NOP::BuildPremise(this.atIsActivated, true, NOP::Equal()) };
24:
25:
/* Create the Condition cnRlSensorTrigger */
26:
NOP::SharedCondition cnRlSensorTrigger =
27:
NOP::BuildCondition<NOP::Conjunction>(prIsRead, prIsActivated);
28:
29:
/* Create the Method mtTrigger */
30:
NOP::Method mtTrigger{
31:
this.AtIsRead = true;
32:
this.atIsActivated = false;
33:
};
34:
35:
/* Create the Instigation inMtTrigger */
36:
NOP::SharedInstigation inMtTrigger =
37:
NOP::BuildInstigation(mtTrigger);
38:
39:
/* Create the Action acMtTrigger */
40:
NOP::SharedAction acMtTrigger =
41:
NOP::BuildAction(inMtTrigger);
42:
43:
/* Create the Rule rlSensorTrigger */
44:
NOP::SharedRule rlSensorTrigger =
45:
NOP::BuildRule(cnRlSensorTrigger, acMtTrigger);
46:
47: /* End class */
48: };


36
the conflict resolution strategy should (or at least could) be deterministic, meaning it consistently
makes the same decision in the same context. As a result, NOP includes a deterministic conflict
resolution mechanism, ensuring deterministic evolution. This mechanism can be implemented in
various ways (RONSZCKA, 2019).
For monoprocess and multiprocess environments, Banaszewski (2009) proposed a Rule
scheduler based on a linear data structure (such as a stack, queue, or list). These structures
hold references to the approved Rules, as shown in Figure 5. The Rules are stored in the order
of their approval and can be reorganized according to the principles of the adopted strategy
(BANASZEWSKI, 2009). In this monoprocess and multiprocess context, this approach naturally
results in deterministic conflict resolution.
Figure 5 – Notification mechanism
Rule.4
Rule.1
Rule.2
Rule.3
Rule.0
Fire!
Notification Mechanism
Source: Adapted from Ronszcka (2019)
In this sense, depending on the conflict resolution strategy predetermined by the deve-
loper, the Rules in question will be effectively executed. In this context, the conflict resolution
models used for NOP in single-process environments are (RONSZCKA, 2019):
• BREADTH: It is based on First In, First Out (FIFO) scheduling, i.e., it refers to the
execution of Rule entities, following a queue-type data structure;
• DEPTH: It is based on Last In, First Out (LIFO) scheduling, i.e., it refers to the execution
of Rule entities, following a stack-type data structure;
• PRIORITY: it organizes Rule entities according to the priorities defined in them; and


37
• NO_ONE: The Rules are approved and executed immediately, not using the escalation
mechanism.
• KEEPER: It was proposed by Muchalski et al. (2012) to keep an approved Rule in the
execution queue until it was disapproved. If there are no state changes between one record
and the next, the Rule will remain approved and can be executed without the need for
renotifications. This strategy leaves it up to the developer to choose when to request the
execution of rules (MUCHALSKI et al., 2012).
2.2.3.2
NOP entities sharing
Essentially, a NOP program is created by defining a set of entities based on the paradigm
model, which are organized to form a coherent sequence of notifications aimed at solving a
specific problem. Properly organizing these entities is crucial for building an effective and
well-structured program. In this context, sharing entities in NOP is considered best practice,
as it enhances both development efficiency and performance. Proper implementation of entity
sharing helps prevent the creation of redundant entities and eliminates unnecessary notifications
(RONSZCKA, 2012; RONSZCKA, 2019).
Entity sharing can be implemented in two ways: manually, where the developer orga-
nizes the program (as in NOP Frameworks), or automatically, where the “assembler” system
manages the entities and removes redundant elements. To illustrate this best practice in the NOP
Framework C++ 4.0, a hypothetical alarm system scenario is used. In this scenario, sensors are
grouped into sectors, and each sector utilizes shared system knowledge. As a practical example,
Algorithm 4 presents a code snippet demonstrating entity sharing within the NOP Framework
C++ 4.0.
This example builds upon Algorithm 3, incorporating the Premise prIsDeactivated and
the Condition cnRlSensorTrigger2. For clarity, the shared entities are highlighted in red, while
the newly added entities are shown in blue. For example, the shared entity atIsActivated is
utilized by both the Premises prIsActivated and prIsDeactivated. Similarly, the shared entity
prIsRead is used by the conditions cnRlSensorTrigger and cnRlSensorTrigger2.
Furthermore, entity sharing can also extend to the Method entity, which may be triggered
by multiple Rules within the program. In fact, in NOP, virtually all entities within the model can
be shared, particularly when this process is handled automatically (RONSZCKA, 2019).


38
Algorithm 4 – Example of NOP sharing entities using the NOP Framework C++ 4.0
1: /* Include the NOP Framework C++ 4.0 */
2: #include “libnop/framework.h”
3:
4: /* Create the class Sensor */
5: class Sensor
6: {
7: public:
8:
9:
/* Create the Attribute atIsRead */
10:
NOP::SharedAttribute<bool> atIsRead
11:
{ NOP::BuildAttribute<bool>(false) };
12:
13:
/* Create the Attribute atIsActivated */
14:
NOP::SharedAttribute<bool> atIsActivated
15:
{ NOP::BuildAttribute<bool>(false) };
16:
17:
/* Create the Premise prIsRead */
18:
NOP::SharedPremise prIsRead
19:
{ NOP::BuildPremise(this.atIsRead, false, NOP::Equal()) };
20:
21:
/* Create the Premise prIsActivated */
22:
NOP::SharedPremise prIsActivated
23:
{ NOP::BuildPremise(this.atIsActivated, true, NOP::Equal()) };
24:
25:
/* Create the Premise prIsDeactivated */
26:
NOP::SharedPremise prIsDeactivated
27:
{ NOP::BuildPremise(this.atIsActivated, false, NOP::Equal()) };
28:
29:
/* Create the Condition cnRlSensorTrigger */
30:
NOP::SharedCondition cnRlSensorTrigger =
31:
NOP::BuildCondition<NOP::Conjunction>(prIsRead, prIsActivated);
32:
33:
/* Create the Condition cnRlSensorTrigger2 */
34:
NOP::SharedCondition cnRlSensorTrigger2 =
35:
NOP::BuildCondition<NOP::Conjunction>(prIsRead, prIsDeactivated);
36:
...
37:
38: /* End class */
39: };


39
2.2.3.3
Formation Rules
The concept of Formation Rules was introduced in Notification Oriented Control (NOC)
(SIMÃO, 2001; SIMÃO; STADZISZ, 2003). In essence, each Formation Rule enables the
creation of specific Rules derived from the generic representation of a Rule (PORDEUS, 2017;
SANTOS, 2017). This concept proves valuable when the causal knowledge of a Rule is shared
across different sets of FBE instances, meaning that a set of specific Rules only differs in the
combinations of referenced instances.
As an example, consider a hypothetical traffic surveillance alarm system where all
administrator users have access to all connected alarm systems. In this scenario, triggers must
be defined for each connected alarm center, and this condition must be replicated for each
combination of users and alarm centers. If there are many users and alarm centers, without
utilizing the Formation Rules concept, it would be necessary to manually replicate the Rules
for each declared instance, making the development process time-consuming and error-prone
(RONSZCKA, 2019).
In contrast, by using Formation Rules, the logical-causal knowledge of this special
Rule is provided in a generic form, based on the class model of the User FBE and the Central
FBE, rather than specific instances of each FBE. As a result, during program assembly, each
combination of User and Central instances (e.g., user1 x central1, user1 x central2, user2 x
central1, user2 x central2) would generate specific instances of this generic Rule, resulting in a
composition of N x M instances (RONSZCKA, 2019).
Based on this concept, the developer does not need to manually input the characteristics
required to create each specific Rule. Since these Rules share the same logical-causal knowledge,
automating the replication of Rules is desirable, as it reduces the likelihood of errors and improves
the overall readability of the code. This is because the final application code will consist of only
the generic Rule, rather than multiple copies of similar Rules (RONSZCKA, 2019).
2.2.4
NOP Framework C++ 4.0
The NOP C++ 4.0 Framework was developed by Neves (2021), Neves et al. (2021).
Among its new features, compared to previous versions, is its focus on generic programming
and the adoption of modern C++ language features, introduced in the latest language standards
such as C++17 and C++20. These advancements have made the Framework more flexible


40
and efficient, simplifying the development of NOP applications. Additionally, the Framework
supports multithreaded and multicore processing, provides type flexibility for Attributes and
algorithmic flexibility for Conditions, and reduces verbosity in instructions. The following design
patterns were implemented: Observer, Iterator, Singleton, and Builder.
In summary, several advancements have been implemented, positioning this framework
as the state of the art in NOP development. Comprehensive benchmark comparisons were
conducted with previous versions of the framework and other algorithms, with the authors
reporting satisfactory results. The NOP C++ 4.0 framework outperforms other available NOP
frameworks.
Additionally, many efforts have been made to make NOP development more straight-
forward and popular. However, as NOP is a relatively new paradigm, some artifacts and ma-
terialization may still need to reach the maturity level necessary for developing a complete
industry-level software project. Besides, a gap exists concerning industrial-like projects using
NOP Framework C++ 4.0. To the best of the author’s knowledge, only academic example
problems were still approached to assess the feasibility of NOP Framework C++ 4.0 and even
the NOP technologies in general. Even if some of those academic examples are relevant for
NOP demonstrations, more complex applications are necessary to evaluate their potential in a
real-world scenario (BABU, 2022; FABRO et al., 2021; PORDEUS, 2017). In essence, new
applications may contribute to the maturity and popularity of NOP as a general development
paradigm, always regarding its philosophical and current technological foundations.
2.2.5
Brief overview of the main existing contributions to the NOP
This section presents the main contributions about NOP until present date.
• Simão (2005): This doctoral thesis proposed a Contribution to the Development of a
HMS Simulation Tool and Proposition of a Meta-Model for Holonic Control (HC). The
philosophical foundations of the NOP are actually discussed in this document, even if
as a Notification Oriented Control for HC already envisaged as a more generic solution
therein. The concept of paradigm better appear in certain publication, such as (SIMÃO;
STADZISZ, 2008) and them is deeper investigated in the following works, advised and
co-advised by Prof. J. M. Simão (coauthor or author of the subsequent publications).
• Banaszewski (2009): This master’s thesis presents the NOP, classifies it as an effective


41
paradigm, discusses its qualities and advantages and in which contexts they apply and,
above all, compares it with current usual paradigms. These comparisons are made through
explanations, theoretical studies, and practical studies in which the efficiency of execution
is highlighted. For the practical studies, the dissertation proposed the Framework NOP
C++ 1.0 (BANASZEWSKI, 2009), based on Simão’s previous one, the Framework NOP
C++ Prototypal (SIMÃO; STADZISZ, 2008). The dissertation concludes on the advan-
tages and relevance of NOP, as well as opening up research perspectives on it, such as
multiprocessing.
• Valença (2012): This master’s thesis proposes a new version of the NOP Framework and
the evolution of its Wizard interface. In the end, they are validated by quantitative and
qualitative comparisons with previous artifacts (RONSZCKA et al., 2017b).
• Pordeus (2017): This master’s thesis proposed a new hardware co-processor suitable for
the acceleration of notification-oriented applications. This architecture was implemented
in hardware using both low-cost and high-end FPGAs (LINHARES et al., 2020).
• Ronszcka (2012): This master’s thesis proposed a contribution to the design of applications
in the Notification Oriented Paradigm by defining and using NOP patterns and, moreover,
co-developed the Framework NOP C++ 2.0 (RONSZCKA et al., 2017b) by using popular
design patterns.
• Xavier (2014): The aim of this paper is to compare two different software development
paradigms, the emerging Notification Oriented Paradigm (NOP) and the Event Oriented
Paradigm (EOP). Objectives, methods and tools are presented, and two case studies are
described (the first in three scenarios), along with their reflections, experiments and data.
The comparison is theoretical and practical, correlating structuring characteristics in NOP
and POE according to a common taxonomy, measuring them in source code complexity
(number of lines of code, scopes and tokens) and comparing them in measurements during
execution (response time and total execution time), by building and experimenting with
case studies in both paradigms. The performance analysis shows that the NOP application
outperformed the other two for both datasets in terms of execution time, memory usage,
and energy consumption.
• Ferreira (2015): This master’s thesis proposed a prototypal programming language and a


42
compiler for NOP, called LingPON 1.0 (RONSZCKA et al., 2017a). This programming
language was enhanced by Ronszcka (2019) and renamed NOPL 1.0.
• Kossoski (2015): This master’s thesis proposes a testing method for software projects that
use NOP in their development. It focused on the unit testing and integration testing phases.
• Linhares (2015): This doctoral thesis presents a contribution to the development of a
computing architecture, called Notification Oriented Computer Architecture (NOCA),
which is suitable for the execution of software developed according to the NOP computing
model. It was designed based on principles of generality, flexibility and scalability, allowing
it to run NOP software of any level of complexity from a program memory without
depending on reconfiguration of the hardware that implements ARQPON itself. Moreover,
the architecture developed is organized as a fine-grained multiprocessor that executes
instructions hierarchically through sets of specialized cores (LINHARES et al., 2020).
• Melo (2016): This master’s thesis adapted NOP for the development of fuzzy systems.
• Pordeus (2017): This master’s thesis presents the development of a simulator for the
NOCA architecture, which is called NOCASim. The implementation of NOCA in software
form aims to simulate its operation with the number of simulated processors in the same
proportion as the number of NOP elements that compose an application (LINHARES et
al., 2020).
• Santos (2017): This master’s thesis proposes a new version of LingPON (version 1.2),
based on NOPL Technology 1.0. The LingPON 1.3 allows new possibilities such as entity
aggregations, in which it is possible to create complex applications more easily and directly.
The advances have been validated for software development, particularly for a robot soccer
application (Robocup), which is considered a complex type of software, against equivalent
implementation in Framework NOP C++ 2.0 and OOP Programming (SANTOS et al.,
2017).
• Kerschbaumer (2018): This doctoral thesis proposed a new NOP solution for digital
hardware, called PON-HD 1.0, which has been developed to facilitate synthesis for FPGA.
With PON-HD 1.0, it is possible to generate VHDL code for FPGA directly from a
NOP program written in a high-level language. This language and its compiler are called
LingPON-HD 1.0, based on NOPL Technology 1.0 (KERSCHBAUMER et al., 2018).


43
• Ronszcka (2019): This doctoral thesis proposed a method for the creation of programming
languages and compilers for the NOP in distinct platforms, as well its implementations as
NOPL Technology Prototypal, 1.0 and 2.0 (RONSZCKA et al., 2017b; RONSZCKA et
al., 2017a).
• Negrini (2019): This master’s thesis presented a NOP solution for multicore environments.
To achieve this goal, the author proposed a framework called Framework NOP Elixir that
reproduces each NOP element as an Erlang microactor. This structure is then integrated
with NOPL technology. With this synergy of technologies, it was possible to combine the
concurrency and balance of the Erlang architecture with the implicit decoupling of NOP
entities and the high-level programming provided by NOPL (NEGRINI et al., 2019).
• Novaes (2019): This master’s thesis proposes a method and a language for graphically
modeling software and systems requirements, under the name Requirements and Interde-
pendencies MOdeling Notation (RIMON). This language makes it possible to represent
requirements and their interdependencies in a systematic, precise and expressive way,
with the aim of helping to improve the quality of software and systems requirements
specifications. Based on the concepts of the Requirements Oriented to Notifications (RON)
approach (NOVAES et al., 2018), RIMON has been designed to be visually appealing in
its possible commercial use.
• Schutz (2019): This doctoral thesis proposes NeuroPON, which is an extraordinary appro-
ach to developing Artificial Neural Networks using the Notification Oriented Paradigm
(SCHUTZ, 2019).
• Mendonça (2020): This doctoral thesis proposed the Notification Oriented Software
Design Methodology (NOM), with a focus on NOP, i.e. design-oriented rules, facts,
and notifications. NOM defines a comprehensive set of activities to support designers in
modeling NOP software from software requirements. A new modeling process is adopted,
called Holonic Flow Modeling, which is based on holonic systems and their concepts of
hierarchy of holons (holarchies), whose approach predicts that a holon can be decomposed
into a subset of holons that detail the holon of the higher level (MENDONÇA et al., 2020).
• Oshiro (2021): This master’s thesis proposed a new compiler, based on the NOPL Tech-
nology 2.0 compilation system, for the Namespace-oriented C++ Modular Notifier Code,


44
aimed at NOPL 2.0 and its programming language adjustments. This compiler for NOPL
2.0, together with its code generator, is called NPCPP 2.0 (OSHIRO et al., 2021).
• Neves (2021): This master’s thesis developed the aforementioned NOP Framework C++
4.0 (NEVES et al., 2021).
• Babu (2022): This research focused on analyzing some of the green potential of NOP
in a simulated sensor correlation application in a smart city, comparing the performance
of a NOP implementation with other common and popular object-oriented programming
languages. In order to explore the NOP Framework C++ 4.0, a prototype air quality
monitoring system was developed, considering the presence of air quality sensors in three
different locations of a supposed smart city. In addition to the prototype implemented in
the NOP Framework C++ 4.0 it was also implemented in the C++ and Java programming
languages, in order to compare them.
• Figueiredo (2022): This master’s thesis presents advances in the state of the art, imple-
menting the NOP IoT Framework C++ 4.0 which allows the distribution of the NOP’s
constituent entities using a Publish/Subscribe architecture and the Message Queuing Tele-
metry Transport (MQTT) protocol, both commonly used in IoT environments. The types
of NOP entities are also classified in relation to their possible distribution modes. Three
experiments are presented using NOP through the NOP IoT Framework C++ 4.0 with the
aim of verifying the functional and non-functional aspects of NOP and comparing it with
the EOP through implementations in C++ using the Publish/Subscribe architecture and
MQTT (FIGUEIREDO, 2022).
• Kossoski et al. (2024): This paper proposed the Notification Oriented Querying Method
and Prototype (NOP Query), a new querying processing method based on NOP, focusing
on search and matching in a continuous flow context. This work forms the context of this
doctoral thesis.
2.3
RELATED TECHNOLOGIES AND STATE OF THE ART
This Section provides a brief overview of the different technologies used in this thesis,
including computer vision, modern distributed video processing architectures, video query
languages, and complex event processing.


45
2.3.1
Computer Vision
Computer Vision (CV) is a sub-field of computer engineering that helps computers
understand images and videos. In academic papers, computer vision typically refers to the
research and development of algorithms and models to automate tasks that require visual
perception. These tasks include image recognition, object detection, facial recognition, image
generation, among others. Computer vision techniques are often used in applications such as
image and video analysis, autonomous vehicles, medical image analysis, and augmented reality,
so forth (ROSEBROCK, 2016).
For a computer, images are simply a large numeric matrix. However, for humans, images
have different components and meanings. This is the so-called semantic gap problem, which
refers to the difference between how a human perceives the contents of an image and how an
image can be represented in such a way that a computer can understand the contents (SILVEIRA,
2023; ROSEBROKE, 2017). Image algorithms process low-level data, such as pixels and colors,
while humans understand high-level data, such as objects and events. The issue is to link sets of
basic elements to meaningful concepts that human beings can perceive (ALAM et al., 2020b).
Many advances have been made in CV, as well as other topics such as natural language
processing, and speech recognition due to significant improvements in Artificial Intelligence (AI)
research in terms of computing power and data available to train detection models. Two important
and related areas of AI are Deep Learning (DL) and Machine Learning (ML). Although DL falls
within the domain of Neural Networks (NN), which is a subfield of ML, DL differs from ML
in its ability to automatically extract features from unstructured data, eliminating much of the
human intervention required in classic ML methods. NN, in turn, are fundamental components
of DL, consisting of layers of interconnected nodes with weights and thresholds. In this case, the
term “deep” refers to the multiple layers of these networks (ROSEBROKE, 2017; CHOLLET,
2021).
In particular, the DL architecture refers (almost always) to a neural network stacked on
top of each other with more than one hidden layer (NIELSEN, 2015; CHOLLET, 2021), as shown
in Figure 6. This strategy allows the network to extract features from finer granules. However,
it increases the processing cost. These layered representations, or hierarchical representations,
are a mathematical structure for learning from data based on successive layers of increasingly
meaningful representations. DL has made breakthroughs in all the historically difficult areas of


46
Figure 6 – Neural networks according number of layers. a) Non-deep feedforward neural
network (shallow network). b) Deep neural network.
Source: Nielsen (2015)
computing, including image classification at a near-human level, speech recognition, handwriting
transcription, autonomous driving, advanced translation, text-to-speech, and web search results,
among others.
Figure 7 – Data representations learned by a digit-classification model
Source: Chollet (2021)
Based on DL, Convolutional Neural Networks (CNN) are the most advanced method
for many computer vision tasks such as object detection and classification (BOCHKOVSKIY et
al., 2020; SANDLER et al., 2018; HE et al., 2017; HE et al., 2016). In a CNN, the hidden layers
perform convolutions, including multiplication or another scalar product, and their activation
function is usually a ReLU (NAIR; HINTON, 2010). Other layers follow, such as pooling, fully
connected, and normalization layers (GOODFELLOW et al., 2016).
The technology uses three basic concepts: local receptive fields, shared weights, and


47
Figure 8 – Architecture of an image classification using CNN
Source: Saha (2018)
pooling (NIELSEN, 2015). Figure 8 shows a common CNN architecture. Local receptive fields
are a technique to avoid connecting each input pixel to each hidden neuron. The connections
occur in small, localized regions of the input image in a small window (e.g., 5 × 5 pixels). Each
local receptive field has a different hidden neuron in the first hidden layer. Then, it moves the
local receptive field one pixel to the right (i.e., one neuron) to connect to a second hidden neuron.
Shared weights allows the network to learn the same pattern, regardless of its position in the
input. In turn, the pooling operation involves sliding a two-dimensional filter over each channel
of the resource map and summarizing the resources that are in the region covered by the filter.
For this reason, the map from the input layer to the hidden layer is called a feature map and the
weights that define the feature map are the shared weights. The grouping layers simplify the
information by taking each feature map that comes out of the convolutional layer and preparing a
condensed feature map. There are many local receptive fields, shared weights and pooling layers.
Finally, the last fully connected layer is a regular neural network that accepts the last flattened
pooling layer as input.
2.3.2
Processing pipeline
This section introduces the core concepts of the video query pipeline, covering the main
aspects from data ingestion to consumption. It is particularly significant because video querying


48
at scale presents far more challenges than a standalone application running on a single server.
The complexity arises from the involvement of various hardware, software, network connections,
databases, and high-level applications. Given the numerous challenges, several solutions for
handling video in a big data context have been developed over time. Currently, the processing
pipeline at scale consists of four main phases (XU et al., 2019): ingestion, storage, retrieval, and
consumption, as illustrated in Figure 9, and further explained in the following sections.
Figure 9 – Processing pipeline overview
Data capture from video sources
- IP Camera
- IoT devices
- video file
Decoding from different files and
protocols
- mp4, ogg,
- H.265, RTMP, DASH)
Preprocessing
- data cleaning
- select relevant frames
DBMS
- SQL
- NoSQL
Video
Scene
Frame
Keyframe
Retrieval video
- from DBMS
- from live stream
- using a query language or not
RETRIEVAL
STORAGE
INGESTION
Human Computer Interface
- website or app
- alerts
- reports
- decision making
CONSUMPTION
Source: Developed by the author


49
2.3.2.1
Ingestion
The ingestion phase has been widely studied over the years, resulting in extensive
approaches in the literature. To better understand the ingestion phase, it is possible to split into
video capture by CODECs (enCODer-DECoder)), pre-processing tasks, object detection and
labeling, ingestion time, and query time.
2.3.2.1.1
Video capture CODECs
A CODEC is a software, hardware, or combined solution that can digitize, compress,
and decompress audio or video signals. It transforms raw data into digital data that can be
transmitted, received, stored, and compressed to reduce storage space, increase the transmission
bit rate, or both (PUNCHIHEWA; BAILEY, 2020). According to this author, popular video
encoding includes:
• H.264/AVC (Advanced Video Coding): is one of the most popular used video compression
standards because it offers high-quality compression and is widely supported by devices
and platforms.
• H.265/HEVC (High-Efficiency Video Coding): is a newer standard that offers greater
compression efficiency, compared to H.264/AVC, and provides the same quality but with
smaller file sizes, offering the same bit rate.
• VP9: is an open-source video compression standard developed by Google that offers similar
compression efficiency to H.265/HEVC for streaming applications such as YouTube.
• AV1: is another open-source video compression standard developed by the Alliance for
Open Media that offers even better compression efficiency than VP9 and H.265/HEVC.
Due to its advantages, it is expected to be widely adopted for streaming video.
• MPEG-2: This is an older video compression standard that is still used in some applications,
such as DVDs and broadcast television because it offers good quality. However, it is less
efficient than the newer standards such as H.264/AVC and H.265/HEVC.


50
2.3.2.1.2
Data preprocessing
Image preprocessing refers to manipulating raw image data to transform it into a
usable and meaningful format. This procedure eliminates unwanted distortions and enhances
specific qualities essential for computer vision applications. It is a fundamental initial stage in
preparing image data for input into machine learning models. Notably, preprocessing has gained
attention since DL models (GOODFELLOW et al., 2016) became popular for object detection
due to their high accuracy. However, DL models are expensive to compute at scale, even using
Graphical Processing Units (GPUs) (KANG et al., 2017; KANG et al., 2019a). The selection
of preprocessing steps depends on the attributes of the data and the nature of the task at hand
(KANG et al., 2020).
For example, consider the following classic problem related to a surveillance system:
“The Road Traffic Authority may need a system that allows direct queries for tasks such as
detecting high-volume traffic on specific roads, locating vehicles by characteristics (for example,
license plate, color, model or a combination of features), or tracking suspicious vehicles traveling
together (such as a criminal escort car)” (KANG et al., 2019a; ANDERSON et al., 2019; KANG
et al., 2019b; LU et al., 2016; ZHANG et al., 2017; XU et al., 2019). According to the literature,
this situation raises several issues:
• Computational cost: Due to its computational cost, preprocessing can be understood as an
optimization problem or a multi-objective optimization problem Applications that deal
with large-scale videos or streaming data require solutions that avoid wasting computing
power and communication resources.
• Many visual concepts: The meaning of an image can be simple, such as a car, or complex,
such as recognizing activities related to that car. In addition, image detection models can
fail with different lighting conditions, object size, partial occlusion and position changes.
• Limitation of training data: An efficient and general image detection model must be trained
with a large dataset of images using suitable parameters. This requires skilled programmers,
time and budget for suitable hardware.
• Dynamic queries: In the context of video surveillance, users expect a video processing
system to be able to answer questions about past events (e.g. how many people were at a


51
particular bus station in July?) or current events (e.g. which streets are busiest now?). This
implies additional complexity.
• Complex code: Computer vision projects and libraries published in repositories such as
Github usually have complex code and data structures.
Popular preprocessing tasks include:
• Resizing: Standardizes the frame size to ensure consistent input for machine learning
algorithms.
• Grayscaling: Converts color images to grayscale to simplify the data and reduce computa-
tional requirements.
• Noise reduction: Helps to remove unwanted noise from images using filters such as
smoothing and blurring.
• Normalization: Normalizes pixel intensity values to a desired range, usually between 0
and 1, to improve model training.
• Binarization: Converts grayscale images into black and white by applying a threshold.
• Contrast enhancement: Adjusts image contrast using histogram equalization to improve
the visual quality of images.
Moreover, video processing on a large scale may require additional preprocessing
strategies, particularly concerning the volume and speed at which data is generated and stored:
• Varying image resolution: lower frame resolution can accelerate the inference time, but
reduces the detection accuracy (XU et al., 2019).
• Frame compression: video CODECs use redundant information within each frame to
improve compression by identifying regions with high similarity and storing each region
only once (HAYNES et al., 2021).
• Adjusting frame rate ingestion: it is similar to varying image resolution, but it is focused
on accelerated inferences on live streams.
• Background subtraction: it helps to identify foreground objects and extract motion vectors
to isolate areas with moving objects (DAUM et al., 2021).


52
• Frame difference detector: it highlights temporal differences between frames and determi-
nes whether the video content has been changed (KANG et al., 2017).
• Analysis of a specific part of the video or frame: it identifies the video sequences or frame
regions that are most relevant to send to a cloud server (offloading) to compute heavy tasks
when the local node cannot handle them. It comprises a filter and forwards selected data
to be computed in a more powerful machine (PAKHA et al., 2018; CANEL et al., 2019;
CHAO et al., 2020).
• Automatic configuration adjustments to speed up processing: it is used to tune three input
configurations (or knobs) of videos – resolution, segment length, and sampling rate – to
accelerate query processing according to some threshold (CHUNDURI et al., 2022).
• Window size to process events occurring between a specific number of frames or time
interval: it avoids processing the entire video due to the high computational cost (YADAV;
CURRY, 2019a; YADAV et al., 2021b; YADAV; CURRY, 2019b; YADAV et al., 2020;
KOUDAS et al., 2022).
• Mix of many different configurations: it uses various strategies to reduce the computational
cost according to a specific threshold or resource constraints (POMS et al., 2018).
2.3.2.1.3
Computer vision pipeline
Object detection is a technique that uses neural networks to localize and classify objects
in images (ROSEBROKE, 2017). This computer vision task has a wide range of applications,
from medical imaging to self-driving cars (CHOLLET, 2021). Basically, according to this
literature, the object detection process involves two main steps:
• Object localization: this step focuses on locating objects in an image by creating bounding
boxes around them, which define the spatial dimensions of the object. In more advanced
scenarios, techniques such as key point localization are used to identify specific points on
the object (e.g., landmarks or joints).
• Object classification or labeling: once one or more objects have been located, this step
determines what they represent, usually by defining a name or label (e.g., a person or a
car).


53
As previously stated, currently, CNN are the most popular type of Deep Neural Network
(DNN), and they are widely used for locating and classifying objects in frames or images
(ROSEBROKE, 2017; CHOLLET, 2021). In the recent years, two variants of CNN have been
extensively used in the ingestion phase: Ground-Truth Models and Specialized Models. GT
Models are the most widely studied because they are highly accurate, free, ready to use, and have
a wide range of support for many programming languages. For example, popular GT Models
include Yolo, Faster R-CNN, Resnet, MobileNet, and SSD (WANG et al., 2021; LIU et al.,
2016; SANDLER et al., 2018; HE et al., 2017). However, they are costly in the context of video
processing due to the high inference time. For example, according to (KHANI et al., 2023), a
current state-of-the-art NVIDIA V100 GPU can support only two video streams running the
YOLOv5-L model at 30 Frames per Second (FPS). If running on large processing clouds, the
total cost will be around $1,100 per month. This is also evidenced by the Keras2 website, which
shows the most popular models and their CPU and GPU inference times.
As naive processing of all frames using expensive models is impractical for many tasks,
especially in video or big data contexts, many researchers have proposed different types of small
or Specialized Models (KANG et al., 2017; KANG et al., 2019a). They are based on GT Models
but trained with fewer layers and focused on particular contexts. Because they are not generalists,
Specialized Models are suitable for some types of applications, i.e., they act as binary classifiers,
returning whether the specified objects are present in a given frame or image (e.g., a white car).
For example, Figure 10 presents a basic scheme for making Specialized Models. Trai-
ning the specialized model requires a dataset of labeled data, usually from the same video stream
in which this model will be used. Basically, the video stream is previously stored in a labeled
dataset and then this dataset is used to train the specialized model.
Due to its limitations, the use of just one specialized model is not practical. For this
reason, the common approach is to use a cascade of Specialized Models, each of which is more
accurate and usually more expensive than the other (XU et al., 2019), as shown in Figure 11.
In the cascade set, each classifier only checks for the presence of a specific feature or class. If
the accuracy is below a threshold, then the next classifier is called to check. The execution is
stopped when the model produces a prediction with high-confidence (e.g., greater than 90%).
Only when the cheap models fail, the ground-truth model used. Several authors developed their
Specialized Models and cascade classifiers. They called cheap CNNs, small CNNs, proxy models,
2
https://keras.io/api/applications/


54
Figure 10 – Basic scheme for making specialized classifiers
Labeled dataset with a reference model
Small pickup
SUV
Van
Bus
Used to train
cheap models
Produces
Specialized
 classifiers
Uses different 
settings
Source: Developed by the author
Figure 11 – The use of cascaded classifiers to process video queries
Query: "bus" +
target video
Specialized
classifier 1
Specialized
classifier 1
Specialized
classifier 1
Specialized
classifier 1
Cascaded classifiers
Use a reference model
if below threshold
Binary classification
Is there a bus?
Yes!
Time A
Time B
Source: Developed by the author
hierarchical models, specialized neural networks, and micro-classifiers (ANDERSON et al.,
2019; KANG et al., 2019a; KANG et al., 2019b; HSIEH et al., 2018; KANG et al., 2020; SHEN
et al., 2014; HAN et al., 2016; SHEN et al., 2017; MULLAPUDI et al., 2019; CANEL et al.,
2019; KANG et al., 2020; CHAO et al., 2020; HÖNIG et al., 2023).
Considering the significant human effort for proper software development and hard-
ware capacity required to create a new detection model, several papers have proposed different
strategies to create labeled video datasets and inexpensive models, including class refinement
(ZHANG; KUMAR, 2019), CNN hyperparameter tuning (ANDERSON et al., 2019), appro-
ximate filtering (KANG et al., 2019a), inference cost reduction (HSIEH, 2019), noisy data


55
reduction (AGARWAL; NETRAVALI, 2023), query optimization (CHAO et al., 2020), trade-off
between accuracy and inference speed (LI et al., 2020b), optimization of temporal relations
(de Boer et al., 2017), and probabilistic predicates (KANG et al., 2021; YANG et al., 2022;
ROMERO et al., 2022; MOLL et al., 2022; LU et al., 2018).
A complete pipeline, from data ingestion to classification, is exemplified in Figure 12. In
essence, detection models can be categorized into two groups, known as early and late operators,
depending on the computational cost, the function, and the order in which they are employed. In
a holistic view, the early operators, such as video ingest and decode, frame difference detector,
and cheap models, are faster but intended for basic, low-cost tasks. They activate later operators
such as GT Models, motion detectors, object trackers, and OCR readers on a small fraction of
the video for more in-depth analysis. Generally, the cost of late operators can differ by three
orders of magnitude from early operators (KANG et al., 2017).
Figure 12 – Cascade of operators and their computing cost
Frame difference
detector
Cheap detection
models
Ground-truth
models
Motion detectors
and tracking
OCR/license
plate readers
Video ingestion
and decoding
Cheap
Frame A
Frame B
Frame C
ABC09
Costly
Early operators
Late operators
Costly
Very costly
Source: Developed by the author
2.3.2.1.4
Ingestion time and querying time
When querying a large number of images, such as video datasets or streaming video in
real-time, the latency between the search command and the retrieval of the video is often regarded
a very important problem (YI et al., 2017; HSIEH et al., 2018; HSIEH, 2019). However, the


56
processing time between the user’s search command and the system’s retrieval typically varies
from seconds to hours of intensive computing, depending on the activity envisaged (KANG et
al., 2017; HSIEH et al., 2018). In this context, a video query system usually performs tasks that
need to be fast (or even in real-time), such as video ingestion and object detection. These systems
also have to perform tasks that normally do not need to be done in real-time or even so fast, such
as database reading, or storing consolidated data for persistence. For this reason, some studies
have divided processing strategies into ingest time and query time (CHAO et al., 2023).
a) Ingestion time (or online mode): focuses on data ingestion, data filtering, read frames,
frame difference detector, and detection using cheap models. Given the fast response time,
ingestion time is usually also referred to as online processing.
b) Query time (or offline mode): focuses on heavy processing, such as query processing,
inference using GT Models, cluster analysis, complex database operations, feeding trend
dashboards, human-machine interaction (e.g., web page or mobile app), and expensive
machine learning operations. Query time is also known as search time, profiling (ZHANG
et al., 2017), or offline processing (ANDERSON et al., 2019).
An overview of ingestion time and query time is shown in Figure 13. Hsieh et al. (2018)
presented the first architecture that formalized and divided processing between ingestion time
and query time. At ingest time, the solution uses cheap models to create an approximate index of
all possible object classes for each frame. At query time, it takes advantage of this approximate
index to provide low latency and, at the same time, compensate for the low accuracy of cheap
models by using GT Models when necessary. The objective is to respond “after the fact”, or
retrospectively, queries about objects of certain classes (e.g., cars, people) over many days of
recorded video.
Similarly, retrospective video analysis has also been explored by Agarwal e Netravali
(2023), Kang et al. (2017), Kang et al. (2019a). In addition, some studies also consider a variety
of ingestion time and query time separately, using different strategies to manage resources, online
and offline processing (ZHANG et al., 2017; HSIEH et al., 2018; KANG et al., 2017; KANG et
al., 2019a).
Moreover, various approaches have been proposed for different types of problems.
For example, Zhang et al. (2017) perform mathematical operations to distribute processing
in a cluster in which a scheduler optimizes video resolution, frame rate and sliding window


57
Figure 13 – Basic overview of ingestion time and query time
Ground truth CNN
Objects
Frames
Ingestion time
Query time
Storage
Querying
for class X
CNN
especialization
Objects below
threshold
Frames with
objects of class X
4
23
2
1
5
Object detection,
tracking, etc.
Objects above
threshold
Source: Developed by the author. Adapted from Hsieh et al. (2018).
settings to minimize the delay caused between processing and search time. Hung et al. (2018)
used a centralized manager and working machines to execute queries configured as a directed
Directed Acyclic Graph (DAG), in which each transformation processes a time-ordered stream
of messages (e.g., video frames). Chen et al. (2022) built indexes for all desired objects of the
given videos during an ingestion time and evaluates query answers efficiently in the query time.
In a different way, Poms et al. (2018) represent video collections as a table in a database that
performs calculations expressed as data flow graphs on those frames.
2.3.2.2
Storage
With advances in information technology, the amount of data produced and stored is
increasing very fast. Consequently, multimedia content (e.g., audio, image, video) is widely used
by humans and machines (e.g. IoT devices) for many applications today. Therefore, the need to
store, organize, and efficiently retrieve this data has been a research motivation for companies
and universities for decades (DÖNDERLER et al., 2005; COLLINS, 2020; LU et al., 2015).
However, traditional relational databases are not suitable for dealing with multimedia data due to
the type of unstructured data, the large volume, and the speed with which it is produced. Even
more recently, streaming applications bring additional complexity because they need to process,
store, and retrieve in real-time (YADAV; CURRY, 2019b).
Figure 14 presents an overview of a common video database system. Typically, video
sources such as Closed-Circuit Television (CCTV), cell phones, and Internet of Things (IoT)
devices send content to a server responsible for storing the raw footage and video metadata, such
as objects, events and the time of occurrences. The metadata is then used by query engine to


58
help search the raw footage. On the other side, an user interface such as a webpage or mobile
application allows some interaction with this database to obtain relevant videos of interest, alerts
of events, and situations that happened.
Figure 14 – Ingestion and retrieval scheme of the video database.
Video sources
(CCTV, mobile, etc)
Ingest policy
Store video
metadata
Create queries,
triggers, etc
Relevant
video
Store raw video footage
UI web server
Video server
Source: Developed by the author. Based on Stonebraker et al. (2020).
An interesting method for storing the spatiotemporal attributes of video events was
introduced by Yadav e Curry (2019a), Yadav e Curry (2019b), Yadav et al. (2020). Figure 15
shows an example of this approach. Given a video stream, the system detects objects along with
their attributes (e.g., car1, red) and stores them in the graph database. The objects are represented
as nodes, while their spatiotemporal relationships (e.g., left, below, after) are stored as edges
connecting the nodes. For each frame the database is updated according to the video stream.
While this approach is quite interesting, it can be costly in terms of processing time and query
latency.
Moreover, although NoSQL has many advantages, unlike relational databases, it does
not have the true key properties of a transaction: Atomicity, Consistency, Isolation, and Durability
(ACID). An ACID transaction is defined by a database operation that exhibits these properties,
and systems that support these operations are classified as transactional systems (MEIER,
2019). The properties of each read, write, or modification of a table are guaranteed by ACID
transactions. However, NoSQL intentionally sacrifices these properties for improved performance
and scalability.
Even so, several authors have developed new video database management systems. For
instance, Haynes et al. (2021) presented a new video storage system designed to automatically
organize the data in the storage hardware structure in an efficient and granular format, eliminating


59
Figure 15 – How the graph database represents spatiotemporal relationships
Car1
Car2
Car3
Rel2
Rel1
Rel3
Truck1
Rel4
Car1
Car2
Car3
Rel2
Rel1
Rel3
Motor
cycle1
Rel5
Car3
Black
Car2
Green
Car1
Red
Car2
Green
Truck1
White
Truck1
White
Motorcycle1
Orange
Truck1
Rel4
Car1
Car2
Car3
Rel2
Rel1
Rel3
Source: Developed by the author. Based on Yadav et al. (2020).
the redundancies found in videos captured from multiple cameras. On the other hand, Daum et
al. (2021) proposed a new system that uses spatial random access to encode videos and optimize
the file layout according to the content.
In turn, Collins (2020) presented a prototype of a query engine for video data using
active and relational database concepts. The author developed an ingest module that processes
video sources with a GPU server and stores data and metadata about each frame. In addition,
a retrieval module provides a user interface that accepts some search and query criteria and
presents matching video queries.
Still, Krishnan et al. (2018) studied execution trade-offs in visual analytics and illustra-
ted a complex relationship between storage, latency, and accuracy. Also, Haynes et al. (2018)
presented a new database management system for managing virtual, augmented, and mixed
reality video content, offering a query language and algebra, allowing declarative queries.
Finally, there is an extensive list of video database systems and related technologies
(DÖNDERLER et al., 2005; OGLE; STONEBRAKER, 1995; ¸SAYKOL et al., 2005).
2.3.2.3
Retrieval
There are several image indexing and retrieval techniques. The first technique consists
of associating images with a specific object or location of interest (e.g., a given image is a
photograph of a specific building on the Stanford campus (PHILBIN et al., 2007; KANG et al.,


60
2017)).
The second technique consists of searching for similarities in a large corpus of images
(e.g., reverse image search on Bing Visual Search). It can be achieved, for instance, using
histogram comparisons, template matching, and feature matching. Data mining algorithms,
mainly based on clustering, such as k-nearest neighbors, can also perform binary classification.
The third technique is content-based video indexing and retrieval, which uses advan-
ced video segmentation, feature extraction, dimensionality reduction, and machine learning
algorithms (SPOLAÔR et al., 2020).
The fourth technique uses approaches based on deep learning (DL), since it revolutioni-
zed image similarity tasks using pre-trained Deep Convolutional Neural Networks (DCNNs),
such as ResNet, VGG, and Inception, or inexpensive models.
The fifth technique consists of storing video metadata, such as object, color, plate,
and timestamp, and using it to retrieve the original footage. These metadata usually need to be
obtained using specific detection models for each task.
2.3.2.4
Consumption
The consumption phase interacts directly with end users or other machines to provide
the results obtained by the video processing system. In general, end users write some query
language to perform tasks, such as finding a specific object or event or configuring triggers to be
fired when a certain condition occurs. Some solutions offer a Human-Computer Interface (HCI),
such as a web page or mobile application, to improve usability. However, most studies do not
offer query language or HCI. More details about video query languages are presented later in
Section 2.3.3.
For example, Hsieh et al. (2018) offer a simple interface in which the user selects the
target video and the object class. A piece of video is displayed if the system encounters the
object. However, Kang et al. (2019a) present an interesting user interface based on a web page
that offers a query language similar to SQL, with support for operators such as: select, from,
group by, having, sum, limit, and gap. Searches can be made by video name, timestamp, and
object class. It is possible to filter the number of occurrences of each object instance. If the query
matches the metadata in the database, the SQL result will return the timestamp of the event and
the respective segment of the video.


61
2.3.3
Video Query languages
In the literature, there are several ways to perform video queries. The most popular
approach is to use the same query language as the database system that stores the video or the
video metadata (ANDERSON et al., 2019; COLLINS, 2020; STONEBRAKER et al., 2020;
SIPSER, 2020; CHAO et al., 2023). Some works extended SQL with spatiotemporal operators
or event query capabilities, creating a new language (XARCHAKOS; KOUDAS, 2019; LU et al.,
2015; CHAO et al., 2020; YADAV; CURRY, 2019b; KANG et al., 2019a). Still, other works do
not mention any query language, although they perform queries (KANG et al., 2017; ZHANG
et al., 2017; KANG et al., 2022; HSIEH et al., 2018). In any case, all of these approaches use
the so-called query operator. For example, according to this literature, the most popular query
operators are the following:
• Objects: This operator retrieves the object of interest, for example, a person or a vehicle.
• Object attributes: Attributes complement information about objects. For example, when it
is considered a particular person’s object, attributes can be height, clothes, and accessories
such as a hat and glasses.
• Spatiotemporal operators: Spatiotemporal operators are two types of features that distin-
guish video query languages from others, as shown in Figure 16. Spatial operators are
related to the spatial positioning of objects, as well as their relationships. For example:
“The white truck is to the left of the red car”. Temporal operators are related to the temporal
order in which the objects appear, as well as their relationships. For example, “The white
truck appears before the red car”. A detailed discussion of spatiotemporal operators is
presented in (YADAV et al., 2020).
Some video query languages have very interesting features. For example, the Streaming
Video Queries (SVQ) (LU et al., 2015; XARCHAKOS; KOUDAS, 2019; CHAO et al., 2020)
extends the traditional SQL language but uses a relational database management system to map
each statement to the corresponding SQL queries. The grammar supports native SQL operators
such as: select, distinct, from, where, group by, order by, group-items, having, asc, desc, and,
or, not. It also supports various features related to the declaration and use of variables and
spatiotemporal operators (LU et al., 2015; XARCHAKOS; KOUDAS, 2019; CHAO et al.,
2020).


62
Figure 16 – Overview of spatiotemporal relationships
Point
Line
Polygon
Geometry
Disjoint
Touch
Inside
Topology
Intersect
A
B
Left(A,B)
Front(A,B)
Direction
A
B
above
below
left
right
t1
t2
t1 before t2
Temporal relations
t1
t2
t1 overlaps t2
t1
t2
t1 overlaps t2
t1
t2
t1 starts t2
t1
t2
t1 meets t2
t1
t2
t1 finishes t2
t1
t2
t1 during t2
t1
t2
t1 equals t2
Spatial relations
Source: Developed by the author. Based on Yadav et al. (2020).
For example, Listing 5 selects all the frames in which there is a car to the left of a
yellow bus. In the query syntax, 𝐶𝑖are classifiers for different types of objects, such as vehicle
types and colors, and 𝐹𝑖are bounding box features for objects in the frame, using vehDetector,
an object detection algorithm.
Algorithm 5 – The SVQ query language
1: SELECT cameraID, frameID, C1
2: (F1 (vehBox1)) AS vehType1,
3: C1 (F1 (vehbox2)) AS vehType2,
4: C2 (F2 (vehBox1)) AS vehColor
5: FROM (PROCESS inputVideo
6: PRODUCE cameraID, frameID, vehBox1, vehBox2
7: USING VehDetector)
8: WHERE vehType1 = bus
9: AND vehColor = yellow
10: AND vehType2 = car
11: AND (ORDER(vehType1, vehType2) = LEFT
Source: Developed by the author.
FrameQL (KANG et al., 2019a) also extends the SQL and supports spatiotemporal
operators. It provides a table-like schema for querying videos using SQL relational algebra.
Supported attributes include time, location, object class, bounding boxes, and object identifier
(tracking), among others. This query language represents videos as virtual relations, with one
relation per video in which each tuple corresponds to a single object in a frame, and the same
object can have one or more tuples associated with it (i.e., appear in several frames). Moreover,
the engine automatically fills the attributes using computer vision methods (KANG et al., 2019a).


63
SVQ (XARCHAKOS; KOUDAS, 2019; CHAO et al., 2020) extends the SQL and
presents a set of approximate filters to accelerate queries involving spatial relations between
objects (e.g., a car to the left of a truck). In addition, the queries support real-time processing,
object counting, and checking the state of predicates before proceeding with frame analysis.
The Video Event Query Language (VEQL) (YADAV; CURRY, 2019b; YADAV, 2019;
YADAV, 2021; YADAV et al., 2021b) differs from the others because it is based on Complex
Event Processing (CEP) systems and graph databases. In a CEP system, information flows as
notifications of events occurring in the external world. The engine filters events and combines
them into conditions that represent higher-level events (CUGOLA; MARGARA, 2012). It,
therefore, focuses on detecting specific occurrences of low-level patterns and events that are part
of higher-level events. When a match occurs, the CEP mechanism notifies the interested parties.
According to Yadav e Curry (2019b), the main features of CEP systems are the straightforward
expression of events and the detection of patterns in real-time. A wide variety of spatiotemporal
operators and low-latency query correspondences are provided.
Table 1 summarizes the many video query languages and their support for the most
common operators.
Table 1 – Video query languages and their support for common operators: ✓=“yes”, 𝑃=“partially”, −=“no”
Objects
AttributesSpatial
op.
Temporal
op.
BilVideo (DÖNDERLER et al., 2005)
✓
✓
✓
✓
CVQL (KUO; CHEN, 1996)
✓
−
𝑃
−
EVAQL (KAKKAR et al., 2023)
✓
𝑃
−
−
FRAMEQL (KANG et al., 2019a)
✓
✓
−
−
MOQL (LI et al., 1997)
✓
−
𝑃
𝑃
ROLE (LIU et al., 2018)
✓
✓
✓
✓
SVQ (XARCHAKOS; KOUDAS, 2019; CHAO et
al., 2020)
✓
✓
✓
−
SVQL (LU et al., 2015)
✓
✓
✓
✓
VEQL (YADAV; CURRY, 2019b)
✓
✓
✓
✓
VERL (FRANCOIS et al., 1996)
✓
𝑃
𝑃
✓
VIQS (HWANG; SUBRAHMANIAN, 1996)
✓
−
𝑃
𝑃
VISUAL (¸SAYKOL et al., 2005)
✓
✓
𝑃
−
VRQL (HAYNES et al., 2018; HAYNES et al.,
2020)
✓
✓
✓
✓
Source: Developed by the author
Some of the following video query operators have appeared more recently in the
literature based on event query languages and CEP systems. More details can be found in: Kang
et al. (2019a), Kang et al. (2022), Yadav e Curry (2019a), Cugola e Margara (2012).
• The 𝑎𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛operator allows computing some statistics over the video frames. Com-


64
mon aggregations include count, sum, average, maximum, and minimum operator. For
example, compute the average number of cars per frame.
• The 𝑐𝑜𝑛𝑗operator retrieves the objects(s) of interest, evaluating two or more attributes.
For example, show the number of instances of cars and trucks in a time window.
• The 𝑐𝑜𝑢𝑛𝑡operator is a type of aggregation. Some approaches extend this operator by
supporting more features, such as counting objects between frames. For example, to warn
if there is high-volume traffic on a street.
• The 𝑖𝑡𝑒𝑟𝑎𝑡𝑖𝑜𝑛operator defines the repeated occurrences of a matching event, similar to a
loop in a programming language.
• The 𝑗𝑜𝑖𝑛operator allows performing a join and, subsequently, a 𝑠𝑒𝑙𝑒𝑐𝑡𝑖𝑜𝑛, 𝑎𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛,
or 𝑙𝑖𝑚𝑖𝑡query. For example, an Amber Alert application can check whether the detected
license plates belong to a stolen car database.
• The 𝑙𝑖𝑚𝑖𝑡operator allows finding a cardinality-limited number of events occurring within
some time interval. For example, selecting ten instances of buses at stop signs.
• The 𝑝𝑟𝑜𝑗𝑒𝑐𝑡𝑖𝑜𝑛operator extracts only a part of the information to compute video events.
• The 𝑟𝑒𝑛𝑎𝑚𝑖𝑛𝑔operator changes the name of a field.
• The 𝑠𝑒𝑙𝑒𝑐𝑡𝑖𝑜𝑛operator allows the selection of particular objects or events of interest. For
example, selecting from all instances of a person in a video database.
• The 𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒operator retrieves the occurrence of objects of interest, evaluating their
temporal relationship. Typically, the sequence operator is used with the window operator.
For example, select a “car” object and a “truck” object that appears in the same 10-second
time window.
• The 𝑠𝑖𝑚𝑖𝑙𝑎𝑡𝑖𝑟𝑦operator allows searching for portions of the video similar to a reference
frame or video clip. For example, given a picture or video clip of a soccer player’s goal,
find similar events. Such queries often involve iterative, ad-hoc analysis to arrive at the
final query.
• The 𝑤𝑖𝑛𝑑𝑜𝑤operator establishes an interval scope in which the query should be performed,
generally based on frame numbers or timestamps. It is often used to limit the time interval


65
that a query works, aiming at reducing the computational cost of searches. For example,
bus and truck objects can be selected to travel together within 10 seconds.
2.3.4
Complex Event Processing
Complex Event Processing (CEP) (CUGOLA; MARGARA, 2012), Complex Event
Recognition (CER) (GIATRAKOS et al., 2020), or Complex Event Detection (CED) (HONAR-
PARVAR et al., 2024) refers to collections of simple events that derive from complex events
when they satisfy some pattern. This feature allows processing systems to react to events. CEP
languages, for example, can query complex patterns that correspond to input events based on
their content, input order, and relationships. There are several CEP systems and languages in
the literature that differ in their architectures, data models, pattern languages, and processing
mechanisms. Two surveys about CEP systems were published in Cugola e Margara (2012),
Giatrakos et al. (2020).
Basically, the input of a CEP system is a stream of events, also called Simple Derived
Events (SDEs), along with a set of patterns, defining relationships between the SDEs. An
event has the structure of a tuple of values that can be numeric or categorical (e.g., event type,
timestamp). During the event computation, it detects instances that satisfy an expected pattern
and produces complex event output. Time is critical, so the temporal formalism defines the
detection patterns According to Giatrakos et al. (2020), there are three main types of CEP
systems:
• In automata-based systems, patterns are usually defined in a language similar to SQL
that is later compiled into some form of automata (often non-deterministic) for pattern
matching. The automaton is then fed with the data stream, changing state as the predicates
on the current state transitions are satisfied.
• In logic-based systems, patterns often have the form of a rule, with antecedent, consequent,
and condition which, if satisfied, lead to the detection of a CEP. Many underlying mecha-
nisms for performing inference can be used, from PROLOG-based systems to directed
graphs (similar to automata).
• The tree-based systems differ from the other two above-mentioned systems in many ways:
they assume that CEPs avoid semantic ambiguities when hierarchies of events are present,


66
and translate patterns to trees, whose leaves store events and internal nodes correspond to
operators.
Beyond the above-mentioned systems, there are also hybrid approaches that consider a
mixture of trees, automata, and logic concepts, but the consequences on the semantics, soundness,
and completeness are unclear. The CEP languages use operators to perform queries. The most
basic are 𝑠𝑒𝑙𝑒𝑐𝑡𝑖𝑜𝑛and 𝑠𝑒𝑞𝑢𝑒𝑛𝑐𝑒. There are many operators, but not all languages support them
(GIATRAKOS et al., 2020).
• 𝑆𝑒𝑙𝑒𝑐𝑡𝑖𝑜𝑛: Selects those events whose attributes satisfy a set of predicates/relations, tem-
poral or otherwise.
• 𝑆𝑒𝑞𝑢𝑒𝑛𝑐𝑒: Two events following each other in time.
• 𝐷𝑖𝑠𝑗𝑢𝑛𝑐𝑡𝑖𝑜𝑛: Either of two events occurring, regardless of their temporal relation.
• 𝐼𝑡𝑒𝑟𝑎𝑡𝑖𝑜𝑛: An event occurring N times in sequence, where N > 0.
• 𝐶𝑜𝑛𝑗𝑢𝑛𝑐𝑡𝑖𝑜𝑛: Both events occur, regardless of their temporal relation.
• 𝑁𝑒𝑔𝑎𝑡𝑖𝑜𝑛: Absence of event occurrence.
• 𝑃𝑟𝑜𝑗𝑒𝑐𝑡𝑖𝑜𝑛: Returns an event whose attribute values are a transformed subset of the
attribute values of its sub-events.
• 𝑊𝑖𝑛𝑑𝑜𝑤𝑖𝑛𝑔: The event pattern must occur within a specified time window.
2.4
SUMARIZING THE EXISTING GAPS IN THE LITERATURE
In the literature reviewed, these are the main gaps found:
• High video processing cost (KANG et al., 2017; HUNG et al., 2018; WANG et al., 2018;
KANG et al., 2019a; KRAFT et al., 2020; LAI et al., 2021; HWANG et al., 2022; LI et
al., 2023; KHANI et al., 2023).
• Complex imperative deployment programming (KANG et al., 2019a; KANG, 2022).
• High latency with query processing (HSIEH et al., 2018; YADAV, 2019; CHAO et al.,
2020; HSIEH, 2019; CHAO et al., 2023).


67
• Too much complexity to detect and retrieve spatiotemporal events (YADAV; CURRY,
2019a; YADAV, 2021).
• The high cost of relational databases, such as triggers and stored procedures (COLLINS,
2020; STONEBRAKER et al., 2020; SIPSER, 2020; CHAO et al., 2023).
• The high cost of graph databases (POMS et al., 2018; QIN et al., 2021; YADAV et al.,
2021b; YADAV, 2021).
• Lack of a standard query language and an efficient search engine, which requires a
pragmatic solution, as was the case with ANSI SQL relational databases.


68
3 NOTIFICATION ORIENTED QUERYING METHOD (NOP QUERY) PROPOSAL
This Chapter introduces the Notification Oriented Querying Method (NOP Query),
a new processing method for streaming queries. Section 3.1 presents an overview of the NOP
Query Method. Section 3.2 presents the Stream Data Buffer – Apache Kafka, adopted to provide
the distributed system architecture for the proposed method. Section 3.3 presents the Data Stream
Collector module. Section 3.4 presents the Query Manager module. Finally, Section 3.5 presents
the Data Stream Processor module which contains the core of the NOP Query method, the Static
NOP Query Chain and the Dynamic NOP Query Chain.
3.1
NOP QUERY OVERVIEW
The NOP Query method proposes a new approach to dealing with streaming video
queries, using the fundamentals of NOP and the tools available. Since the NOP Query Method
is built upon a modified and extended version of the NOP Framework C++ 4.0, it is inherently
reactive in terms of notifications and designed to innovate query processing. Essentially, there
are at least four main differences in NOP Query Method from the existing approaches:
• It avoids loop-based coding, which causes unnecessary logical evaluations.
• It avoids database operations such as Create, Read, Update, Delete (CRUD), triggers, and
stored procedures, thereby reducing wasted processing power and potentially allowing
distributed processing.
• It offers a new video querying language that is free and available for the community to
extend the project.
• It is based on a distributed architecture fit for the big data scenario.
NOP Query presents feasible solutions to the following shortcomings: a) Complex
programming for imperative implementation, b) High latency with query processing, c) Too
much complexity to detect and retrieve spatiotemporal events, d) High cost of relational databases,
such as triggers and stored procedures, e) Lack of a standard query language and an efficient
search engine. It is innovative because it offers an original contribution to this important open
area, proven to be suitable, and extends NOP and its applicability to a new frontier.


69
Once these features have been highlighted, Figure 17 shows, through the UML Activity
Diagram, an overview of the NOP Query method workflow. Basically, the complete NOP Query
workflow is comprised of four key components: the Stream Data Buffer, the Data Stream Collec-
tor, the Query Manager, and Data Stream Processor. The key and most innovative contribution
of this thesis is in the Data Stream Processor, particularly with the Static NOP Query Chain,
the Dynamic NOP Query Chain, and the Query Manager, which introduces a new video query
language called NOP Query Lang. The following subsections detail each of these components.
Figure 17 – Overview of the NOP Query Method workflow
Query Manager
Consume content from
input stream
Assign an input number
and compute basic
preprocessing operations
Data Stream Collector
Consume the events
Filter data according to the
time constraints
Create the Static NOP
Query Chain
Read queries following the
NOP Query Lang syntax
Compile the query
Produce object containing
the query elements
Filter data according to the
Static NOP Query Chain
Create or update the 
Dynamic NOP Query Chain
Show alerts when query
matches with the events
Produce alerts when query
matches with the events
Create a model following
the Static NOP Query
Chain
Produce events containing 
id, timestamp, and content
Data Stream Processor
The Stream Data Buffer enables
communication between
the Collector, Processor
and Query Manager
Source: Developed by the author
3.2
STREAM DATA BUFFER – APACHE KAFKA
To handle a substantial volume of lossless video stream data, it is imperative to employ
fast and robust temporary data storage. For this reason, Apache Kafka was adopted as a buffer
queue for the data generated and consumed by various systems of the proposed NOP Query
Method.
Apache Kafka is a distributed data flow platform that can publish, subscribe to, store
and process streams of records in real-time. It is designed to handle data streams from multiple
sources and deliver them to multiple consumers (CONFLUENT, 2024). Figure 18 presents an
overview of the Apache Kafka.


70
Figure 18 – Apache Kafka overview
Source: Cloudera (2019)
Basically, it’s a distributed system consisting of different types of servers and clients
that communicate events via a high-performance TCP network protocol. All these servers and
clients are designed to work together. Following there are some key terminology (CONFLUENT,
2024):
• Brokers: A broker is a server in the Kafka storage layer that stores event streams from one
or more sources. Typically, a Kafka cluster is made up of several brokers. Each broker in a
cluster is also a bootstrap server, in the sense that it can connect to an agent in a cluster. In
addition, each broker has an IP and port number like any server application.
• Topics: The Kafka cluster organizes and stores streams of events in a durable way in
categories called topics, which are Kafka’s most fundamental unit of organization. A topic
is a record of events, similar to a folder in a file system, in which the events are the files
in that folder. A topic is append-only, which means that when a new event message is
recorded in a topic, the message is appended to the end of the record. The events in the
topic are immutable, which means that they cannot be modified once they have been
recorded. A consumer reads a record at a given offset (i.e., address) and their subsequent
records. Topics in Kafka are always multi-producer and multi-subscriber: a topic can have
zero, one or many producers recording events in it, as well as zero, one or many consumers
subscribing to those events.
• Producers: Producers are clients who record events in Kafka. They specify the topic to
write and controls how events are assigned to the partitions in a topic. This can be done in


71
a round-robin manner for load balancing or according to some semantic partition function,
such as the event key. In addition, each Producer has an IP and port number like any
client/server application.
• Consumers: These are clients who read Kafka events. They are responsible for controlling
the flow of records read from a topic. Normally, a consumer moves linearly as it reads the
records; however, it is possible to consume records in any order, from the oldest one to the
most recent. In addition, each Producer has an IP and port number like any client/server
application.
Currently, the NOP Query is designed to run in a distributed environment, using the
Stream Data Buffer, or standalone (one computer), without the Stream Data Buffer component.
Standalone mode increases processing speed because the Stream Data Buffer causes a natural
overload. If necessary, it is possible to change the Stream Data Buffer Apache Kafka to any other
similar solution.
3.3
DATA STREAM COLLECTOR
Data Stream Collector is responsible for receiving video data from IP Cameras, video
files or JSON files, computing basic operations such as frame decoding and sending data in
JavaScript Object Notation (JSON) format to Data Stream Processor. For instance, JSON 1 is a
standard text-based format for representing structured data based on the syntax of JavaScript
objects. It is commonly used to transmit data between systems (for example, sending data from
the server to the client). Figure 19 shows the sequence diagram and Figure 20 shows an overview
of this architecture using the component diagram.
If the stream comes from IP cameras or video files, Collector decodes it according to the
required format, extracts discrete video frames and sends them to the Stream Data Buffer. It is
important to note that each video source has its own peculiarities, such as different specifications,
CODECS, resolution, and frame rate. For this reason, the Collector sets a default resolution size
and frame rate on input. Various parameters can be configured to optimize the data ingestion.
In the end, all the frames are encoded in the JPG format and converted into a JSON file to be
sent to the Stream Data Buffer (Apache Kafka). Basically, each IP data source is identified with
an address and name which is used for mapping in a Collector configuration file. If the stream
1
https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON


72
Figure 19 – Overview of the Data Stream Collector and Stream Data Buffer sequence diagram
collectorScript
:DataStreamCollector
kafka
:StreamDataBuffer
(topic: ingestion)
Camera
Streaming
JSON
{"cameraId":"cam-surv-1",
"timestamp":1713056693,
"data":"ZnJhbWU=..."}
Source: Developed by the author
Figure 20 – Overview of the components of the Data Stream Collector and Stream Data Buffer
Stream Data Buffer
Data Stream Collector
Topic: ingestion
Data: Basic event object
Source: Developed by the author
comes from a video file or a JSON file, the full or relative path must be entered. A Python script
is responsible for computing the Collector. The JSON resulting from the Collector module for
each frame is as follows:
{"cameraId":"cam-surv-1", "timestamp":1713056693,
"data":"ZnJhbWU=..."}
Basically, each frame is composed of 𝑛𝑎𝑚𝑒of the video source, 𝑡𝑖𝑚𝑒𝑠𝑡𝑎𝑚𝑝and 𝑑𝑎𝑡𝑎
containing a base64 encoded string that represents the byte array of the frame. These properties
are converted into structured JSON messages and, when this file is ready, it is sent as a message
to the “ingestion” topic in the KafkaProducer client.


73
Generally, Kafka’s default configuration works with small messages, from bytes to
kilobytes. However, the data property, which is the base64 result of the video frame, generates
a large file, usually reaching up to several megabytes. Consequently, Kafka may need to be
configured to process such large messages. The relevant KafkaProducer properties that need to
be modified include: batch.size, compression.type, and max.request.size. Further information
about 𝐾𝑎𝑓𝑘𝑎𝑃𝑟𝑜𝑑𝑢𝑐𝑒𝑟configuration can be found in the official website2.
3.4
QUERY MANAGER
The Query Manager is responsible for receiving queries using the NOP Query Lang
(NOPQL) syntax, translating/converting them into a JSON array and sending them to the “queries”
topic in the Stream Data Buffer. Afterwards, this record is consumed by the NOP Query Core,
explained later in the Section 3.5.1. This new query language was developed because the existing
languages are not fully available or free to use. Additionally, the proposed NOP Query Lang is
easy to write and understand. Moreover, it will be available for the community to extend the
project.
Figure 21 shows and example using the sequence diagram and Figure 22 shows an
overview of this architecture using the component diagram. Following this example, basically,
the manager has written a query following the NOP Query Lang grammar to select a red car
from the camera1 input stream. This query is then compiled and translated into JSON notation
and sent to the ingestion topic of the Stream Data Buffer.
In order to read the user input, the ANTLR 43 parser was used. ANother Tool for
Language Recognition (ANTLR) version 4 is an advanced parser generator that can be used to
read, process, execute or translate binary or structured text files into different outputs (e.g., Python
source code to C++ and video query to JSON file). It is widely used in academia and industry
to create all kind of languages, tools and structures (PARR, 2013). From a formal language
description called a grammar, ANTLR generates a parser for that language that can automatically
create parse trees, which are data structures that represent how a grammar corresponds to the
input. ANTLR also automatically generates tree walkers that can be used to visit the nodes of
these trees and execute application-specific code.
According to Parr (2013), to implement a programming language, it is necessary to
2
https://docs.confluent.io/platform/current/installation/configuration/producer-configs.html
3
https://www.antlr.org/


74
Figure 21 – Overview of the Query Manager and Data Stream Collector sequence diagram
a:AntlrProgram
(Query Manager)
kafka
:StreamDataBuffer
(topic: queries)
Manager
Query
JSON
[{"operator":"object"},{"window":"10"
{"objects"[{"number":"1","color":"red",
"label":"car"}]}]
SELECT (object) FROM camera1
WHERE Object[1].label=car AND
Object[1].color=red WINDOW=10
Source: Developed by the author
Figure 22 – Overview of the components of the Query Manager and Stream Data Buffer
Stream Data Buffer
Query Manager
Topic: alerts
Data: alerts of query maches
Topic: queries
Data: query object
Source: Developed by the author
create an application that reads sentences and reacts appropriately to the input symbols. For
instance, a language is a set of valid sentences, a sentence is made up of phrases, and a phrase is
made up of subphrases and vocabulary symbols. In general terms, if an application calculates
or “execute” sentences, it is possible to call that application an interpreter. Examples include
calculators, configuration file readers and Python interpreters. If the goal is to convert sentences
from one language to another, this application is called translator. Examples include Python
to C++ converters and compilers. In order to react properly, the interpreter or translator needs


75
to recognize all the valid sentences, phrases and subphrases of a given language. Recognizing
a sentence means that we can identify the various components and differentiate it from other
sentences.
For example, consider the assignment operation following the syntax of a new query
language: 𝑙𝑎𝑏𝑒𝑙= 𝑐𝑎𝑟;. Figure 23 gives an overview of the language recognition process.
Figure 23 – Overview of a language recognizer
Source: Developed by the author. Based on Parr (2013).
In the language recognizer process, the characters corresponding to the assignment are
read by the lexer program, which checks each word and recognizes the tokens corresponding
to the valid text. The parser then assembles the parse tree or syntax tree which records how the
parser recognized the structure of the input sentence and its component sentences. The internal
nodes of the parsing tree are the names of phrases that group together and identify their children.
The root node is the name of the most abstract phrase, in this case stat (short for “attribution”).
The leaves of a parse tree are always the input tokens.
In the current version, the proposed NOP Query Lang supports one or two query
predicates. Currently, the number of predicates refers to the number of FBEs identified in the
query. The FBE is expressed with the keyword “Object” followed by a number in square brackets.
For example, considering this context and using NOP Query Lang, Algorithm 6 shows a query
with a predicate in which an object with the label bus (e.g., Object[1].label=bus) is searched for
in the stream of camera1 (source) in a time interval of 10 seconds. Algorithm 7 demonstrates a
query with two predicates, where objects are searched based on their spatial positions relative to
each other. In this example, the query searches for a white truck object that is located to the left
and below a red car object. The source is camera1 and the time window is 10 seconds. Still, the
lowercase “object” or “left” query operators, expressed in parentheses after the select operator,
is explained in Section 4.3.1 and Appendix A. Supported operators include object, conj, left, seq


76
and count.
Algorithm 6 – Query example with one predicate
1: SELECT (object)
2: FROM camera1
3: WHERE Object[1].label=bus
4: WINDOW=10
Source: Developed by the author.
Algorithm 7 – Query example with two predicates
1: SELECT (left)
2: FROM camera1
3: WHERE Object[1].label=car AND Object[1].color=red
4: AND Object[2].label=truck AND Object[2].color=white
5: AND (Object[2] LEFT Object[1])
6: AND (Object[2] BELOW Object[1])
7: WINDOW=10
Source: Developed by the author.
The corresponding JSON output from Algorithm 7 is shown in the Listing 3.1. Additio-
nally, the complete code of productions, tokens, inputs and respective outputs of the NOP Query
Lang is available in Appendix B.
Listing 3.1 – Output of the query example with two predicates
1 [
2
{
3
" o p e r a t o r " :
" l e f t "
4
} ,
5
{
6
" window " :
"10"
7
} ,
8
{
9
" o b j e c t s " :
[
10
{
11
" number " :
"1" ,
12
" c o l o r " :
" red " ,
13
" l a b e l " :
" car "
14
} ,
15
{
16
" number " :
"2" ,


77
17
" c o l o r " :
" white " ,
18
" l a b e l " :
" t r u c k "
19
}
20
]
21
} ,
22
{
23
" s p a t i a l O p e r a t o r s " :
[
24
{
25
" f i r s t O p e r a n d " :
"2" ,
26
" secondOperand " :
"1" ,
27
" o p e r a t o r " :
"LEFT"
28
} ,
29
{
30
" f i r s t O p e r a n d " :
"2" ,
31
" secondOperand " :
"1" ,
32
" o p e r a t o r " :
"BELOW"
33
}
34
]
35
} ,
36
{
37
" countOperator " :
{}
38
}
39 ]
3.5
DATA STREAM PROCESSOR
The Data Stream Processor computes heavy tasks using late operators and run the NOP
Query Core, composed by Static NOP Query Chain and Dynamic NOP Query Chain, using
the NOP Framework C++ 4.0. Figure 25 shows the sequence diagram and Figure 24 shows an
overview of this architecture with the component diagram. Basically, this part is composed by
Data Stream Processor and NOP Query Core, which contains the Static NOP Query Chain and
the Dynamic NOP Query Chain. As shown, the Stream Data Buffer can be used to exchange


78
information between the system components.
Figure 24 – Overview of the components of the Data Stream Processor and Stream Data Buffer
Data Stream Processor
NOP Query Core
Stream Data Buffer
Topic: ingestion
Data: basic event
object
Topic: queries
Data: query object
Topic: alerts
Data: Alerts when
query matches
Static NOP
Query Chain
Dynamic NOP
Query Chain
Events Processor
Events
SQC
Alerts
Source: Developed by the author
For instance, the Video Stream Processor receives events from the “ingestion” topic,
generates an OpenCV object from the “data” property of the JSON file, decodes the frame into
a JPG and uses late operators to extract more information using GT Models, object tracking,
color detection, license plate recognition, among others. In essence, it takes advantage of various
Python 3 libraries and deep learning models, including object detection and labeling using
Yolov44, color recognition5, and DeepSort for tracking and ID assigning each object. Because of
the distributed architecture, several libraries for computer vision tasks can be added and run in
parallel using more Kafka topics to exchange information. When each frame is processed, the
resulting data is converted to a JSON file following the Noscope schema6, for example:
4
https://github.com/AlexeyAB/darknet
5
https://github.com/ahmetozlu/color_recognition
6
https://github.com/stanford-futuredata/noscope


79
Figure 25 – Overview of the Data Stream Processor and Stream Data Buffer sequence diagram
kafka
:StreamDataBuffer
nopQueryProgram
:NOPQueryEngine
(Data Stream Processor)
Events data JSON string
(Topic: events)
Events data JSON string
(Topic: events)
[{"operator":"object"},{"window":"10"
{"objects"[{"number":"1","color":"red",
"label":"car"}]}]
{"cameraId":"camera1", "frame":11,
"confidence":0.7,
"objectname":"car", "color":"red",
"xmin":10, "ymin":10,
"xmax":100, "ymax":100, "id":3,
timestamp:1713056693
laterOperators
:DataStreamCollector
Queries data JSON string
(Topic: queries)
Query matches JSON string
(Topic: alerts)
[{"found":"car"},{"cameraId":"camera1"},
{timestamp: 1726769088}, {query: xyz}]
Source: Developed by the author
{"cameraId":"camera1", "frame":11, "confidence":0.7,
"objectname":"car", "color":"red", "xmin":10, "ymin":10,
"xmax":100, "ymax":100, "id":3, timestamp:1713056693}
In the just above exemplified Noscope schema, the properties 𝑥𝑚𝑖𝑛, 𝑦𝑚𝑖𝑛, 𝑥𝑚𝑎𝑥and
𝑦𝑚𝑎𝑥correspond to the bounding box (in pixels) of an red car object in the frame number 11
of the camera Id “camera1”. This event data is consumed by the NOP Query Core, which is
explained below.
3.5.1
NOP Query Core
The NOP Query Core handles the main function of the proposed NOP Query Method,
which is to find event matches and trigger alerts when expected events occur in the data stream.
This work builds on the strengths of the NOP Framework C++ 4.0, improving it by adding a
new way to dynamically create and link NOP elements. It also introduces two new concepts:
Morphable FBE and Morphable Rule, which are key contributions of this thesis. Due to the new
features and development tools introduced, this contribution naturally differs from existing video
querying methods. Figure 26 presents the NOP Query Core overview. Basically, the NOP Query


80
Core is composed of two main submodules: Static NOP Query Chain (SQC) and Dynamic NOP
Query Chain (DQC), which is detailed in the following Subsections.
Figure 26 – NOP Query Core overview
<<Entity>>
MorphableRule: Rule
<<Entity>>
Cn1: Condition
<<Entity>>
Ac1: Action
<<Entity>>
Vehicle: FBE
<<Entity>>
cnConcrete1: Condition
Concrete Rule
<<Entity>>
PrN: Premise
N
N
<<Entity>>
PrConcrete1: Premise
<<Entity>>
PrConcrete2: Premise
<<Entity>>
PrConcrete3: Premise
<<Entity>>
PrConcrete4: Premise
<<Entity>>
PrConcrete5: Premise
<<Entity>>
PrConcrete6: Premise
<<Entity>>
AcConcrete1: Action
<<Entity>>
InConcrete1: Instigation
<<Entity>>
Vehicle: FBE
<<Entity>>
AtConcrete1: Attribute
<<Entity>>
AtConcrete2: Attribute
<<Entity>>
MtConcrete1: Method
<<Entity>>
MtConcrete2: Method
<<Entity>>
MorphableFBE: FBE
<<Entity>>
At1: Attribute
<<Entity>>
At2: Attribute
<<Entity>>
Mt1: Method
<<Entity>>
Mt2: Method
Concrete FBE
NOP Query Method Core
Source: Developed by the author
3.5.1.1
Static NOP Query Chain (SQC)
The Static NOP Query Chain (SQC) is a static schema that represents the query ex-
pression. It describes the elements of the query expressed as a NOP Inference Chain (presented
in Section 2.2.1), with all the NOP elements, and the respective Attribute values. A SQC is
assembled once per query from a set of steps.
In the first step, the SQC reads user/manager JSON queries from the topic “queries”
and assembles the Static NOP Query Chain with Attributes for object names/labels (e.g., car,


81
truck) and colors (e.g., red, white).
In the second step, the SQC assembles the corresponding Premises for labels, colors,
and position values (X and Y), following the scheme shown in Figure 27, using the 2D coordinates
from a computer vision system:
Figure 27 – Spatial position coordinates perspective
Source: Developed by the author. Original image of the UTFPR-HSD public dataset available at http:
//labic.utfpr.edu.br/datasets/UTFPR-HSD.html, accessed on 14 July 2024.
• Premise 1: “car left truck”, “Attribute X (FBE 1) < Attribute X (FBE 2)”;
• Premise 2: “car below truck”, “Attribute Y (FBE 1) > Attribute Y (FBE 2)”;
• Premise 3: “Attribute Color (FBE 1) = red”;
• Premise 4: “Attribute Label (FBE 1) = car”;
• Premise 5: “Attribute Color (FBE 2) = white”;
• Premise 6: “Attribute Label (FBE 2) = truck”.
In the third step, the SQC creates the Condition with all these Premises and sets the
conjunction operator. In the fourth step, the SQC creates the Rule with the associated Condition,
Instigation, and Action elements. Finally, the Method is created to display a alert message if
the query is matched. This message is then sent to the “alerts” topic. Thus, the result of the
SQC process with all these entities and expected states required for query matches is shown in
Figure 28. To illustrate, the Attribute values are suggested according to the query needs.


82
Figure 28 – Result of the Static NOP Query Chain (SQC)
<<FBE>>
'Object' (1)
<<Attribute>>
atPosX=200
<<Attribute>>
atPosY=100
<<Attribute>>
atColor="red"
<<Attribute>>
atLabel="car"
<<FBE>>
'Object' (2)
<<Attribute>>
atPosX=100
<<Attribute>>
atPosY=200
<<Attribute>>
atColor="white"
<<Attribute>>
atLabel="truck"
<<Premise>> 
prTruckBelowCar (P2)
<<Premise>> 
prColorRed (P3)
<<Premise>> 
prLabelCar (P4)
<<Premise>> 
prColorWhite (P5)
<<Premise>> 
prLabelTruck (P6)
<<Rule>>
rlWhiteTruckLeft
BelowRedCar (R1)
<<Condition>> 
cnWhiteTruckLeft
BelowRedCar (C1)
<<Instigation>>
I1
<<Action>>
A1
<<Method>>
showAlert()
<<Premise>> 
prTruckLeftCar (P1)
Source: Developed by the author
3.5.1.2
Dynamic NOP Query Chain (DQC)
The Dynamic NOP Query Chain (DQC) is responsible for assembling the NOP Query
Chain that represents events in the video stream. To accomplish this, the SQC is continuously
checked whenever a new Object ID comes to the system. If the new object contains the expected
Attribute values (e.g., label=car or color=red), the DQC adds it and links it to other objects
associated with a different predicate (e.g., label=truck or color=white). The DQC is dynamic
because the actual NOP Chain connections between elements are formed as the data is ingested.
When a new ID or object appears and partially matches the query, the connections are updated
accordingly. This process is referred to in this work as the new concept of Morphable FBE, as
illustrated in block diagram in Figure 29 and classes diagram in Figure 30.
Essentially, the Morphable FBE is grounded in the concept of Formation Rules (pre-
sented in Section 2.2.3.3). However, it differs from Formation Rules in that the corresponding
NOP elements (e.g., FBE, Attributes, and Methods), can be assembled or updated for each new
occurrence of an expected event. Therefore, the Morphable FBE can tolerate missing data when
the corresponding NOP elements does not fully match the SQC. For instance, the Morphable
FBE is suitable when an object of a real video stream come without some Attribute (e.g., color),
or when the confidence of the object detection model is lower than some threshold (e.g., 50%),
for example. Thus, a new FBE can use one or more available Attributes and the Morphable FBE


83
supports this feature.
Figure 29 – Block diagram of the Morphable FBE
FBE (1) 'Vehicle'
Attribute X=100
Attribute Y=230
Attribute Color="red"
Attribute Label="car"
FBE (2) 'Vehicle'
Attribute X=70
Attribute Y=300
Attribute Color="white"
Attribute Label="truck"
Premise P1
Premise P2
Premise P3
Premise P4
Premise P5
Premise P6
Rule R1
Condition C1
Instigation I1
Action A1
Method showAlert()
Morphable FBE
Source: Developed by the author
Figure 30 – Class diagram of the Morphable FBE
<<Entity>>
Vehicle: FBE
<<Entity>>
AtLabel: Attribute
<<Entity>>
AtColor: Attribute
<<Entity>>
MtShowAlert: Method
<<Entity>>
Mt2: Method
<<Entity>>
MorphableFBE: FBE
<<Entity>>
At1: Attribute
<<Entity>>
At2: Attribute
<<Entity>>
Mt1: Method
<<Entity>>
Mt2: Method
Concrete FBE
Source: Developed by the author
Likewise, the new concept of Morphable Rule, illustrated in block diagram in Figure 31
and class diagram in Figure 32, are also based on Formation Rules but differs because considers
that Rule elements (e.g., Premise, Condition, Rule, Instigation, Action, and the respective Rule)
can also be incomplete until all the necessary Premises states are available to complete the
required Condition. Moreover, the Morphable Rule cannot be activated if the Condition is


84
incomplete. Due to this new feature of NOP Framework C++ 4.0, the NOP Query method
handles this exception circumstance. In turn, the class diagram in Figure 33 gives an overview of
the concepts of Morphable FBE and Morphable Rule together.
Figure 31 – Block diagram of the Morphable Rule
FBE (1) 'Vehicle'
Attribute X=100
Attribute Y=230
Attribute Color="red"
Attribute Label="car"
FBE (2) 'Vehicle'
Attribute X=70
Attribute Y=300
Attribute Color="white"
Attribute Label="truck"
Premise P1
Premise P2
Premise P3
Premise P4
Premise P5
Premise P6
Rule R1
Condition C1
Instigation I1
Action A1
Method showAlert()
Morphable Rule
Source: Developed by the author
Figure 32 – Class diagram of the Morphable Rule
<<Entity>>
MorphableRule: Rule
<<Entity>>
Cn1: Condition
<<Entity>>
Ac1: Action
<<Entity>>
Vehicle: FBE
<<Entity>>
cnWhiteTruckLeftBelowRedCar:
Condition
Concrete Rule
<<Entity>>
PrN: Premise
N
N
<<Entity>>
PrLabelCar: Premise
<<Entity>>
PrColorRed: Premise
<<Entity>>
PrLabelTruck: Premise
<<Entity>>
PrColorWhite: Premise
<<Entity>>
PrTruckLeftCar: Premise
<<Entity>>
PrTruckBelowCar: Premise
<<Entity>>
Ac1: Action
<<Entity>>
In1: Instigation
Source: Developed by the author
For example, as shown in the SQC in Figure 28, if a new object/FBE appears with a
label or color that matches the structure of the SQC (such as atLabel = “car” or atColor = “red”),
it is added to the DQC and linked to all the other existing FBE objects labeled as “truck”. In this
manner, each object relevant to the SQC becomes part of a “dynamic network” of related objects,


85
Figure 33 – Class diagram of the Morphable FBE and Morphable Rule
<<Entity>>
MorphableRule: Rule
<<Entity>>
Cn1: Condition
<<Entity>>
Ac1: Action
<<Entity>>
Vehicle: FBE
<<Entity>>
cnWhiteTruckLeftBelowRedCar:
Condition
Concrete Rule
<<Entity>>
PrN: Premise
N
N
<<Entity>>
PrLabelCar: Premise
<<Entity>>
PrColorRed: Premise
<<Entity>>
PrLabelTruck: Premise
<<Entity>>
PrColorWhite: Premise
<<Entity>>
PrTruckLeftCar: Premise
<<Entity>>
PrTruckBelowCar: Premise
<<Entity>>
Ac1: Action
<<Entity>>
In1: Instigation
<<Entity>>
Vehicle: FBE
<<Entity>>
AtLabel: Attribute
<<Entity>>
AtColor: Attribute
<<Entity>>
MtShowAlert: Method
<<Entity>>
Mt2: Method
<<Entity>>
MorphableFBE: FBE
<<Entity>>
At1: Attribute
<<Entity>>
At2: Attribute
<<Entity>>
Mt1: Method
<<Entity>>
Mt2: Method
Concrete FBE
Source: Developed by the author
as defined by the query. The following procedure is applied to each new FBE Car in the NOP
Query Core:
• Check every FBEs “Truck” in the DQC;
• For each FBE Truck present, then connects it to the current FBE Car;
• If this connection exists, update the corresponding Attributes and start the notification
mechanism when its state changes.
A similar process occurs when the object belongs to the second predicate of the query,
with the match being performed across all the FBEs of the first predicate. When two FBEs are
combined to form the DQC, the corresponding Premises P3 and P5 (color), as well as P4 and P6
(label), are created. In the subsequent step, the corresponding Condition, Rule, Instigation, and


86
Action are generated. The SQC is evaluated once, while the DQC is updated each time a new
relevant object arrives from the stream. For each event, the Data Stream Processor performs the
following actions presented in the Algorithm 8.
It is important to note that this process applies to all elements of the first predicate in
relation to all elements of the second predicate. Therefore, the concept of Shared Entities, as
introduced in Section 2.2.3.2, is utilized.
Algorithm 8 – Data Stream Processor pseudocode
1: Decode the JSON into and object containing the properties: 𝑐𝑎𝑚𝑒𝑟𝑎𝐼𝑑, 𝑓𝑟𝑎𝑚𝑒, 𝑐𝑜𝑛𝑓𝑖𝑑𝑒𝑛𝑐𝑒, 𝑜𝑏𝑗𝑒𝑐𝑡𝑁𝑎𝑚𝑒,
𝑐𝑜𝑙𝑜𝑟, 𝑥𝑚𝑖𝑛, 𝑦𝑚𝑖𝑛, 𝑥𝑚𝑎𝑥, 𝑦𝑚𝑎𝑥, 𝑖𝑑, and 𝑡𝑖𝑚𝑒𝑠𝑡𝑎𝑚𝑝.
2: Update the Time from the JSON file’s timestamp property
3: if The Object 𝐹𝐵𝐸is new then
4:
Load the JSON file as an 𝐹𝐵𝐸object
5:
if The query contains one predicate only then
6:
Create query 𝑅𝑢𝑙𝑒𝑠for this 𝐹𝐵𝐸object
7:
Insert this 𝐹𝐵𝐸object into a list of objects
8:
end if
9:
if The query contains two predicates then
10:
Create query 𝑅𝑢𝑙𝑒𝑠for this 𝐹𝐵𝐸object
11:
Insert this 𝐹𝐵𝐸object into a list of objects
12:
Create matching 𝑅𝑢𝑙𝑒𝑠for this 𝐹𝐵𝐸object with all other 𝐹𝐵𝐸objects with different query predicates
13:
end if
14: else
15:
if The FBE object exists then
16:
Update the existing 𝐹𝐵𝐸′ object with the current 𝐴𝑡𝑡𝑟𝑖𝑏𝑢𝑡𝑒𝑠of the JSON file properties
17:
end if
18: end if
19: if The query matches then
20:
print Send a message to the topic Kafka “alerts”
21: end if
Source: Developed by the author.
3.5.2
Didactic step by step demonstration of the NOP Query Method pipeline
The process is initiated when a manager inputs a query in accordance with the NOP
Query Language (NOPQL) syntax. More details about this language are available at Appendix
B. As demonstrated in Figure 34, the query seeks to select a frame that includes two objects: the
first, a red car, and the second, a white truck. Additionally, the query specifies that the second
object must be positioned to the left and below the first object, based on the spatial operators. The
query is then parsed by ANTLRv4, which generates a JSON array that contains the tokens along
with their corresponding lexemes. These tokens are forwarded to the Data Stream Processor
module, which constructs the corresponding Static NOP Query Chain (SQC). Once the SQC
is constructed, the corresponding values of the FBE are stored in alignment with the expected


87
values specified by the query.
Figure 34 – Overview of Query Manager and Data Stream Processor
SELECT (left) FROM camera1
WHERE Object[1].label=car AND
Object[1].color=red AND
Object[2].label=truck AND
Object[2].color=white AND
(Object[2] LEFT Object[1]) AND
(Object[2] BELOW Object[1])
WINDOW=10
 [{"operator":"left"},{"window":"10"},
 {"objects":
[{"number":"1","color":"red","label":"car"},
 {"number":"2","color":"white","label":"truck"}]},
 {"spatialOperators":
[{"firstOperand":"2","secondOperand":"1",
 "operator":"LEFT"},
{"firstOperand":"2","secondOperand":"1",
 "operator":"BELOW"}]}]
Kafka' topic: "queries"
Static NOP Query Chain
Source: Developed by the author
When the NOP Query Core generates the SQC and the video querying stream is ingested
by the system, the Dynamic NOP Query Chain (DQC) is initialized. A script extracts frames
from one or more input videos, generates a JSON file containing the camera ID, timestamp,
and frame data encoded in base64 format, and sends this file to Kafka’s “ingestion” topic, as
demonstrated in Figure 35. Subsequently, the Data Stream Processor module decodes the base64
data into frames and performs resource-intensive tasks, such as detections using ground truth
models, motion detection, and optical character recognition (OCR) or license plate recognition.
The processed data is then transformed into a JSON object and sent to the “events” topic. Finally,
the Dynamic NOP Query Chain consumes these JSON files and executes queries based on the
Morphable FBE and Morphable Rule.
Consider the arrival of a new frame at the Dynamic NOP Query Chain (DQC) module,
as illustrated in Figure 36. Upon processing the frame, a new object is detected, identified by
ID 1, with the label “car” and the color “red”. The query associated with this frame specifies
the need for a “car” label and the color “red”. In response to this query, the NOP Query Core
generates the initial version of the DQC, as demonstrated below this figure.
In the sequence, Frame 2, as shown in Figure 37, represents the continuation of the
video stream in which the detection algorithm for Object ID 1 successfully identified the object’s
label but failed to detect its color. This may occur if the detection confidence falls below a certain
threshold (e.g., 50%), resulting in the absence of color data for this object. Similarly, the new
object ID 2 has been detected; however, it remains unlabeled, and its color is not identified.


88
Figure 35 – Data Stream Collector and Data Stream Processor
Kafka' topic: "ingestion"
{"cameraId":"cam-surv-1",
"timestamp":1713056693,
"data":"ZnJhbWU=..."}
Data Stream Processor
Kafka' topic: "events"
{"cameraId":"camera1",
"frame":11, "confidence":0.7,
"objectname":"car",
"color":"red", "xmin":10,
"ymin":10, "xmax":100,
"ymax":100, "id":3,
timestamp:1713056693}
NOP Query Engine
Static NOP
Query Chain
Dynamic NOP
Query Chain
Source: Developed by the author
To address these missing attributes, the design of the Dynamic NOP Query Chain structure
was intentionally developed to be robust and tolerant to such gaps in data. This approach is
particularly suitable for big data scenarios and addresses the dimension of veracity.
In turn, Frame 3, shown in Figure 38, demonstrates that Object ID 1 is labeled as “car”
and Object ID 2 is labeled as “truck”. These labels are consistent with the expectations of the
Static NOP Query Chain, leading to the addition of a new FBE to the Dynamic NOP Query
Chain. In addition, Premise P1 has been activated because it requires FBE 1 (Object ID 1) below
FBE 2 (Object ID 2). As a result, Premises P1, P4, and P6 have been activated; however, the
Morphable Rule is not yet complete.
Continuing with Frame 4, shown in Figure 39, this frame presents a case where both
FBEs contain the label and color as expected by the Static NOP Query Chain. However, Premise
P2 remains false, requiring FBE 2 to be positioned below FBE 1. As illustrated in the Dynamic
NOP Query Chain below the figure, only one Premise is needed to activate the respective
Condition, Rule, and the entire set of this Morphable Rule.


89
Figure 36 – Frame 1 of the example video stream
ID: 1
Car
Red
Source: Developed by the author
Figure 37 – Frame 2 of the example video stream
ID: 2
ID: 1
Car
Source: Developed by the author


90
Figure 38 – Frame 3 of the example video stream
ID: 2
Truck
ID: 1
Car
Source: Developed by the author
Figure 39 – Frame 4 of the example video stream
ID: 2
Truck
White
ID: 1
Car
Red
Source: Developed by the author


91
The following Frames 5 (Figure 40), 6 (Figure 41), 7 (Figure 42), and 8 (Figure 43)
present a scenario in which the spatial Attributes of both FBEs are updated; however, these
updates do not affect the existing state of the Dynamic NOP Query Chain. In Frame 9 (Figure 44),
a critical event occurs, where the spatial Attributes of the vertical position (Y-axis) are identical.
Finally, Frame 10 (Figure 45) illustrates the scenario when FBE 2 is positioned below FBE 1,
activating the corresponding Premise P2. This leads to the activation of the entire Morphable
Rule, and the query is matched. Consequently, the Method triggers an alert indicating that the
query event has been detected in the current video stream.
Figure 40 – Frame 5 of the example video stream
Source: Developed by the author
Figure 41 – Frame 6 of the example video stream
Source: Developed by the author
3.5.3
Reflexions about the NOP Query Method
The following topics offer some thoughts on the NOP Query Method:


92
Figure 42 – Frame 7 of the example video stream
Source: Developed by the author
Figure 43 – Frame 8 of the example video stream
Source: Developed by the author
Figure 44 – Frame 9 of the example video stream
Source: Developed by the author
• This work presents an original approach that applies NOP concepts and the tools available
in the area of video querying.
• The concepts of Morphable FBE and Morphable Rule is new and refers to a dynamic NOP


93
Figure 45 – Frame 10 of the example video stream
Query Matched!
Source: Developed by the author
Chain structure that is assembled during the data ingestion process.
• NOP Query can be used to process many types of data, not just video, because the NOP
Query Core only computes data about events.
• NOP Query method is robust and innovative because it has been designed to run both in
standalone mode and in a heavily loaded cluster.
• The distributed architecture of this entire solution favors the adaptation of the proposed
method to a wide range of uses.
• Each NOP Query element must have a name that is used to link to other elements during
the DQC assembly process. Likewise, each FBE must have an ID to identify the object
and thus assemble the Morphable FBE.
• All rules have been configured without the need for conflict resolution (see Section 2.2.3.1).
However, it may be important to consider the potential need for conflict resolution in future
versions of NOP Query, particularly for applications that require more refined event
handling.


94
4 EXPERIMENTS AND RESULTS
This Chapter presents two case studies to empirically assess the proposed NOP Query
Method and its feasibility. The experiments aim to evaluate the overall performance of the NOP
Query, considering computational cost, memory usage and the number of Rules created.
Section 4.1 presents the motivation for these experiments. Section 4.2 presents and
discusses a new dataset created specially for this work, based on a popular dataset from the
literature. Section 4.3 presents the preparatory steps and the environment settings. Section 4.4
presents Case Study 1, which compares the NOP Query with other work from the literature.
Section 4.5 then presents Case Study 2, which details the implementation of NOP Query in a
real distributed big data scenario. Finally, section 4.6 discusses the experimental results and
highlights the advantages of the proposed method and its implementation.
4.1
MOTIVATIONS
Section 2.3 presented the state of the art in the area of video processing and querying.
Based on existing work, the 2.4 section has compiled the main gaps and open problems, parti-
cularly pointed out by many authors, including doctoral theses: Kang et al. (2017), Hsieh et al.
(2018), Yadav (2019), Yadav e Curry (2019c), Kang et al. (2019a), Yadav e Curry (2019a), Chao
et al. (2020), Hsieh (2019), Yadav (2021), Kang (2022), Chao et al. (2023).
In the literature, many authors have proposed different solutions for video querying
and compared the results with other works (AGARWAL; NETRAVALI, 2023; LI et al., 2020a;
YADAV et al., 2021a; HSIEH et al., 2018; YADAV, 2021; KANG et al., 2019a; HSIEH, 2019;
HWANG et al., 2022; CANEL et al., 2019). Usually, the solutions are tested with some video
databases or real-time footage content (e.g., YouTube broadcasts) (SCHOOL, 2018; LAUSANNE,
2020; LEMMER, 2019; KABUKICHO, 2020; HOLE, 2018). The problem is that almost all of
the original YouTube broadcasts are not available because it is only a live video stream and there
are few video databases or video files available for accurate comparison (KANG et al., 2017;
WEN et al., 2020; JODOIN et al., 2014; MOT2016, 2022; XIPG, 2021; RISTANI et al., 2016).
Among the datasets available, Kang et al. (2017) published the Noscope’ “Jackson Town
Square” dataset1, which became one of the most popular datasets used in query experiments about
1
Available at: https://github.com/stanford-futuredata/noscope


95
traffic surveillance in general (KOUDAS et al., 2022; XU et al., 2019). This dataset (KANG et
al., 2017) contains 60 hours of surveillance video and the respective labeled CSV dataset with
annotations for each object (event) found in each frame. The CSV file contains 1,064,237 events
(object detections) in 6,426,647 frames with the following fields: frame, objectname (label),
confidence, xmin, ymin, xmax, and ymax. Figure 46 shows a sample of the Noscope dataset.
Figure 46 – Sample of the Noscope’ Jackson Town Square dataset
Source: Developed by the author
In fact, the popular Noscope dataset is suitable for queries related to objects and spatio-
temporal attributes. However, two important attributes are missing from the annotated CSV
file for comparing with the literature: the color and the respective ID of the objects. All these
attributes are required by the experiments comparing the computational cost (YADAV; CURRY,
2019c; YADAV et al., 2020; YADAV, 2021). Furthermore, the proposed NOP Query Method also
requires these attributes, as mentioned in Section 3.5.1 (NOP Query Engine). To demonstrate the
viability of the proposed NOP Query, a new dataset was developed based on the above-mentioned
dataset, and two case studies were performed.
Case study 1 presents two sets of experiments in which the first compares the results
with the literature, and the second is an extension of the first with more load and large time
windows to be processed. This case study follows the server-only architecture and does not use
the Stream Data Buffer, like the literature compared. Case study 2 is an extension of the second
experiment in case study 1, which includes the Stream Data Buffer to favor communication
between the Data Flow Collector, the Data Flow Processor and the Query Manager, following
a fully distributed architecture, and demonstrating the potential of the NOP Query method.
Therefore, the experiments of the case study 2 considers the entire pipeline of a real, distributed
video surveillance analysis application.


96
4.2
THE NEW NS100KCOLORID DATASET
A new dataset was created using part of the original Noscope dataset (about 10%), but
sufficient for the experiments because it comprises a large time window of about 190 minutes
of data stream in the original dataset. This new dataset was named NS100KCOLORID, and
it contains 102,835 labeled events in 858,806 frames. Basically, this Noscope’s subset was
improved by adding two more fields: the predominant color of the vehicle (red, blue, green,
yellow, white, grey, black, pink and teal) and a unique ID for each object obtained using the
late operator for object tracking DeepSort (WOJKE et al., 2017). Still, aiming at improving the
data quality, only the events with at least 50% confidence were added, following the literature
approaches that establishes such minimal confidence level for detecting objects in a video
stream (YADAV; CURRY, 2019c; YADAV et al., 2020). Figure 47 presents a sample of the
NS100KCOLORID dataset.
Figure 47 – Sample of the NS100KCOLORID dataset
Source: Developed by the author
As the NS100KCOLORID dataset offers more data to explore the capabilities of the
NOP query, various tests can be carried out focusing on CPU processing time (latency), memory
consumption, and Rules produced from different video streaming queries. In fact, most of the
authors in the literature reviewed used live broadcasts from surveillance cameras on YouTube
that are no longer available. Therefore, the carefully annotated dataset created for this study
may be useful to other researchers in the future. This dataset will be available on the GitHub
repository 2.
2
https://github.com/bioinfolabic/NS100KCOLORID


97
4.3
PREPARATORY STEPS
Section 4.3.1 presents the operators, queries and Rules used in the experiments and
Section 4.3.2 presents the hardware and software configurations that support the case studies.
4.3.1
Operators, Queries and Rules
The case studies performed used the same operators and similar dataset as those used in
the literature of the following work Yadav e Curry (2019c), Yadav et al. (2020), Yadav (2021).
For example, Table 2 shows the operators and examples of queries following the NOP Query
Lang notation. These operators are described below. More details about the implementation of
these operators in the NOP Query method are available in Appendix A and Appendix B.
Table 2 – Operators and queries used in the experiments following NOP Query Lang syntax
Operator
Query example
OBJECT
SELECT (object)
FROM 𝑐𝑎𝑚𝑒𝑟𝑎1
WHERE 𝑂𝑏𝑗𝑒𝑐𝑡[1].𝑙𝑎𝑏𝑒𝑙= 𝑐𝑎𝑟
WINDOW = 10
CONJ
SELECT (conj)
FROM 𝑐𝑎𝑚𝑒𝑟𝑎1
WHERE 𝑂𝑏𝑗𝑒𝑐𝑡[1].𝑙𝑎𝑏𝑒𝑙= 𝑡𝑟𝑢𝑐𝑘
AND 𝑂𝑏𝑗𝑒𝑐𝑡[2].𝑙𝑎𝑏𝑒𝑙= 𝑏𝑢𝑠
WINDOW = 10
LEFT
SELECT (left)
FROM 𝑐𝑎𝑚𝑒𝑟𝑎1
WHERE 𝑂𝑏𝑗𝑒𝑐𝑡[1].𝑙𝑎𝑏𝑒𝑙= 𝑐𝑎𝑟
AND 𝑂𝑏𝑗𝑒𝑐𝑡[2].𝑙𝑎𝑏𝑒𝑙= 𝑡𝑟𝑢𝑐𝑘
AND (𝑂𝑏𝑗𝑒𝑐𝑡[1] LEFT 𝑂𝑏𝑗𝑒𝑐𝑡[2])
AND (𝑂𝑏𝑗𝑒𝑐𝑡[2] BELOW 𝑂𝑏𝑗𝑒𝑐𝑡[2])
WINDOW = 10
SEQ
SELECT (seq)
FROM 𝑐𝑎𝑚𝑒𝑟𝑎1
WHERE 𝑂𝑏𝑗𝑒𝑐𝑡[1].𝑙𝑎𝑏𝑒𝑙= 𝑐𝑎𝑟
AND 𝑂𝑏𝑗𝑒𝑐𝑡[2].𝑐𝑜𝑙𝑜𝑟= 𝑦𝑒𝑙𝑙𝑜𝑤
WINDOW = 10
COUNT
SELECT (count)
FROM 𝑐𝑎𝑚𝑒𝑟𝑎1
COUNT(𝑂𝑏𝑗𝑒𝑐𝑡) >= 5
FOREACH_FRAME WINDOW = 10
Source: Developed by the author
• The 𝑜𝑏𝑗𝑒𝑐𝑡operator retrieves the frame of interest within a time window. For instance,
the query example selects/finds the frame of an object with the label “car” within a time
window of 10 s, considering each second is composed of 30 frames. This operator is the
most simple one and evaluates only one attribute.


98
• The 𝑐𝑜𝑛𝑗or conjunction operator retrieves the frame of interest, evaluating objects and
attributes within the time window. The query example selects the frame in which an object
appears with the label “car” and another object with the label “truck” within a 10 s time
window.
• The 𝑙𝑒𝑓𝑡operator retrieves the frame of interest, evaluating the spatial relationship “left”
between objects in the same frame. The query example selects the frame in which an
object with the label “car” appears at the left of the object with the label “truck” within a
10 s time window.
• The 𝑠𝑒𝑞operator retrieves the frame of interest, evaluating their temporal relationship in a
given time window interval. The query example alerts if an object with the label “car” and
another with the label “truck” appear within the same time window of 10 s.
• The 𝑐𝑜𝑢𝑛𝑡operator is the most complex than the former ones, and it counts the number
of objects, evaluating their temporal occurrence within the same time window interval.
The count of objects should be consistent across several frames, denoted by each frame
clause. The query example counts any objects that appeared within a time window of 10 s
and alerts if the count is greater or equal to 5.
• Additionally, the 𝑤𝑖𝑛𝑑𝑜𝑤operator also establishes a time interval scope in which the
queries are performed based on frame numbers or timestamps. It is often used to limit the
time interval to reduce the computational cost of searches. This operator is very important
and restricts the time window size of the entire query.
The NOP Framework C++ 4.0 requires NOP elements to perform the processing. Each
of the necessary NOP Rules is briefly explained below:
• The operator object require one Rule per target object/attribute.
• Both operators, left and conj, require one Rule for each pair of target objects.
• Three Rules are needed for the seq operator. Rule (a) checks when the first expected
predicate of the query appears in the time window (e.g., car). Rule (b) checks when the
second expected predicate of the query appears in the time window (e.g., truck). Rule (c)
fires when the seq is reached.


99
• The count operator requires five Rules: Rule (a) check if there is an object in the frame.
Rule (b) count the number of objects in the same frame. Rule (c) check that the count
matches the query. Rules (d) and (e) reset the count operator when count’ Rule fires.
4.3.2
Hardware and Software Configuration
As mentioned in section 3.5.1, the NOP Query Engine was implemented in the C++
programming language. In addition, the prototype experiments were performed using Intel
Core i7-8750H CPU, 16 GB RAM, Linux Ubuntu 20.04 Kernel 5.4.0-125-generic, NOP C++
Framework 4.0, and g++ 11 compiler. It is important to notice that the GPU was not used in this
experiment because this method focuses only on query processing, where GPUs can be useful,
but not essential. In fact, the activity of object detection was not considered, since these are, by
nature, the activities required by GPUs. For this reason, the proposed dataset already includes
object ID and color attributes.
Since the proposed NOP Query Method is modular and supports distributed processing,
the case studies were conducted in different ways. Case Study 1 uses NOP Query Engine only to
compute the results without Data Stream Buffer. Still, the work in the literature was executed
on a server-only architecture. Therefore it was not run in a fully distributed configuration. Case
Study 2 considers the complete processing pipeline described in the Chapter 3, using the Stream
Data Buffer. Due to the use of Kafka this experiment has a natural overhead which is produced
by the Data Stream Processor.
4.4
CASE STUDY 1
The Case Study 1 consists of two experiments based on the paper published by Kossoski
et al. (2024). The first experiment aims to compare the results obtained with the proposed
methods with similar works in the literature: Yadav e Curry (2019c), Yadav e Curry (2019a),
Yadav et al. (2020), Yadav et al. (2021b). More specifically, it is aimed to compare the computa-
tional complexity (Big O notation) of CPU processing time (also called latency) and memory
consumption. The second experiment aims to estimate the computational complexity of CPU
processing time, memory consumption and the number of Rules produced for each time window,
using larger processing intervals than those used in the compared literature. In addition, the
second experiment was projected to extensively explore NOP Query Engine.


100
The operators mentioned in Section 4.3.1 were used in both experiments. Since the first
one is aimed at establishing some comparison with the literature, it is limited to the scope and
operators of the time window size found in (YADAV et al., 2020). In that work, the authors
tested six different time windows (5 s, 10 s, 25 s, 1 min, 5 min, 10 min). The second experiment
uses a broader range of time windows, from 10 min to 190 min, and it is aimed to estimate the
computational complexity of the proposed approach experimentally.
4.4.1
Experiment 1: Comparison with the Literature
Figure 48 shows the CPU processing time considering the same queries, operators,
and window sizes common in the literature (YADAV; CURRY, 2019c).
Figure 48 – Processing time results considering query construction and search time using short time win-
dow sizes.
Source: Developed by the author
A total of 300 tests were carried out, and the results shown correspond to the average of
10 runs per query and different time windows. Four trend curves (linear, polynomial, logarithmic,
and exponential) were fitted for the left operator, which is the most expensive. The processing
time considers the construction of the NOP query, the search time, and the reaction time when
the query is matched.
From these results, it was not possible to infer the computational cost, because the time
windows are too short. However, the results of Yadav e Curry (2019c) show an exponential cost
from 1 min onwards.


101
4.4.2
Experiment 2: Estimation of the Computational Complexity
The second experiment aims at estimating the computational complexity of CPU and
memory usage, as well as the number of Rules created considering large time window sizes
(from 10 min to 190 min). A total of 950 runs were done, and the results shown correspond to
the average of 10 runs per query and time window size. Likewise the former experiment, four
curves were fitted to estimate the computational cost.
As mentioned earlier, the left operator was also used to estimate the trend lines. In this
version of the experiments, all the objects that correspond, even partially, to the query operators
are configured with the Dynamic Query Chain. Therefore, the tests were extensive and explored
all the combinations to find out their processing capacity at high workloads.
Figure 49 shows the results of the CPU processing time considering the construction of
the NOP Query and the search time. Observe that the left, conj, and seq operators are expensive
because they evaluate pairs of objects within the time window size. Particularly, the left operator
is the most expensive because it evaluates the spatial positions of the objects and their Attribute
values. In this application, spatial changes are very frequent, since the objects are moving. In turn,
the object and count operators are the least expensive because the object operator only evaluates
one object at a time, and the count operator only adds the counter when an object appears in the
time window. The results suggest that the computational complexity of the operator on the left,
which is the most expensive, increases polynomially, as indicated by the metric of the coefficient
of determination (R-squared). Therefore, the proposed approach performs better than others in
the literature.
Figure 50 presents the results regarding memory usage. It is important to keep in mind
that the current version of the experiment does not have any garbage collection, when the
objects and the respective NOP elements are not used. The focus here is to test NOP Query in
a CPU-intensive and memory-consuming setting. It was observed that the left, conj, and seq
operators require more memory because they evaluate pairs of objects. The results suggest that
the computational complexity of the operator on the left, which is the most expensive, increases
polynomially. Once again, it can be observed that the object and count operators perform with
constant computational cost because the dataset contains a similar distribution of objects across
time window sizes.
Figure 51 presents the amount of Rules produced. The Rules are created when a


102
Figure 49 – CPU processing time results including the NOP Query construction and search time using large
time window sizes.
Source: Developed by the author
new object matches, even partially, with the query expression. It means that the number of
Rules created was high due to the lack of a garbage collector. If some strategy were used to
remove unused NOP elements from memory, the final number of Rules would be lower, but this
experiment was designed precisely to explore the potential of the proposed approach. Therefore,
it is possible to observe how the system behaves with a large mass of data processed. Again, the
results suggest that the computational complexity of the operator on the left, which is the most
expensive, increases polynomially.
4.5
CASE STUDY 2
This Section presents experiments for evaluating CPU processing time, memory con-
sumption and Rules produced considering the entire pipeline, using the Kafka broker, from
ingestion to outputs. The experiment protocol, operators, time windows, and average values were
configured as shown in Section 4.4.2 (Experiment 2 of the Case Study 1). Similarly, the ingestion
method is based on “brute force”, while the ingestion came from the NS100KCOLORID dataset.
Figure 52 presents the CPU processing time, memory consumption, and Rules produced.
As shown, the trend curves here are very similar to those of Case Study 1, Experiment 2.
It is seen that the computational cost is still between linear and polynomial for the “left” spatial


103
Figure 50 – Memory usage results considering large time window sizes.
Source: Developed by the author
Figure 51 – Number of Rules created considering large time window sizes.
Source: Developed by the author
operator. It is important to mention that the Kafka’s default configuration was used, with no
optimizations because the application ran on just one machine. Even so, the results are very
encouraging and better than the literature (e.g., exponential). Therefore, it can be stated that the
system is viable.


104
Figure 52 – [Complete pipeline] CPU processing time, Memory consumption, and Rules produced considering
the NOP Query construction and search time using large time window sizes
Source: Developed by the author


105
4.6
DISCUSSION OF THE EXPERIMENTAL RESULTS
Section 2.2.1 (NOP Inference System) highlighted the features and advantages of NOP
to avoid structural and temporal redundancies and reduce wasted processing and unnecessary
evaluations. The promising results obtained in case studies corroborate the theoretical concepts
of NOP, suggesting that the proposed approach can be very suitable for surveillance and query
applications, regarding computational cost and latency.
Interestingly, the object, seq and count operators do not increase processing time or
memory consumption even with large time windows. This behavior differs greatly from the
literature and shows that NOP Query is the best alternative for handling these queries.
It is worth mentioning that the current version of this project does not use multithreading
or multiprocessing at level of the NOP Framework C++ 4.0. However, the results are satisfactory
even when using simple threads in a server-only architecture (e.g., run the entire application on
a single machine) and a fully distributed architecture (e.g., run the entire application using the
Stream Data Buffer). The results of these case studies show the computational complexity curves
as the workload increases. However, as the charts presented, even if the computational cost does
not tend to be linear, it is polynomial, but not exponential, thereby being treatable. Still, as
mentioned above, the results obtained in the literature have an exponential computational cost,
therefore suggesting that the proposed approach is computationally more efficient than those
from the literature.
The thesis of Simão (2005) proposed an discusses the asymptotic analysis of the propo-
sed earlier version of the “NOP” algorithm’s complexity, particularly in the worst-case scenario.
According to the author, in this scenario, all attributes notify all premises, and subsequently,
all premises notify all conditions of the rules. This behavior is represented by the worst-case
function 𝑇𝑤𝑜𝑟𝑠𝑡(𝑥) = 𝑥3, where the parameter 𝑥represents the number of notifying elements,
and the result corresponds to the number 𝑛of notifications or comparisons performed. Based
on this, the proposed decision-making inference process exhibits a complexity of 𝑂(𝑛3) in the
worst case.
In particular, for the proposed NOP Query algorithm described in Algorithm 8, the
worst-case scenario occurs when all existing FBEs from the input stream have a single attribute
relevant to the query. Consequently, this requires a connection with additional elements of the
other query predicate (considering two predicates in the query). Under such conditions, the


106
computational complexity in the worst case can be expressed as 𝑂(𝑛2).
Besides, by induction and based on the NOP literature, it is possible to infer that if
more processing cores and Kafka’s optimizations were available, the results would tend towards
logarithmic complexity. In turn, logarithmic complexity grows much more slowly than the current
polynomial complexity. Moreover, the use of multithreads or multiprocessing in this approach is
planned as future work.
The current performance limiting factor is the memory consumption required to connect
all the NOP entities for each identified object. In this way, Figure 3 (NOP Inference System)
and Figure 28 (Result of the Static NOP Query Chain) show how the connection between the
NOP entities occurs. Each entity is an object relating to other objects, and this requires memory
space. Still, as mentioned before, the current version of this work does not have a garbage
collector feature to test the “worst” possible scenario. Even so, the results are very promising,
as mentioned before. In fact, other approaches in the literature also use a lot of memory due to
their idiosyncrasies and much more processing resources due to their computational paradigm
orientation.
Furthermore, this approach offers manageable performance even when dealing with a
lot of data/object movement by taking advantage of the NOP properties as mentioned before. As
a matter of fact, this is another advantage over literature.
Summarizing the experimental results, the following highlights can be suggested:
• The computational complexity of the proposed approach does not grow exponentially, and
it is treatable between polynomial and even logarithmic complexity.
• Only when some Attribute value changes (e.g., label, color, or positions), the corresponding
Premise is notified to reevaluate its state and fire a notification if the new state is different.
Because of such behavior, the system performance is high, and the latency is low.
• Unlike the literature, the latency is low for short and long window sizes.
• Unlike the literature, the latency and memory consumption of the object, seq and count
operators are low.
• It is possible to develop complex event queries using NOP Rules.


107
• The NOP Query works as an active database without permanent triggers. It is the foun-
dation of a new technology called “Reactive database based on NOP”, currently under
development.
• This querying method is natively focused on real-time processing.


108
5 CONCLUSION AND FUTURE WORK
This chapter presents the conclusions of the doctoral thesis, in the light of the objectives
proposed in Chapter 1 (Introduction). In addition, this chapter naturally discusses a number of
glimpses of the contributions made by the current thesis, which serve as a list of future work.
5.1
CONCLUSION
Streaming video queries have been one of the most challenging research areas in
computer vision, software engineering, and big data. In recent years, several approaches to video
queries have emerged. However, none have become popular due to many limitations related to
the high latency between the user’s query, search time, and notifications when a query matches.
These approaches also require intensive CPU and memory usage, several database operations
per second, complex data structures, and high network usage. In addition, the related solutions
are usually created as monolithic structures. Although GPU processing enables fast computing,
existing video query approaches are still expensive for real-time processing. Considering these
aspects, this doctoral thesis presents the following contributions.
First, a new lean query processing method, NOP Query (Notification Oriented Querying
Method), was presented as a straightforward and intuitive approach to dealing with streaming
video queries. As far as we know, this is the pioneering work based on NOP for this context. NOP
Query inherits important features from NOP, such as formalism and tools that are constantly being
improved. Moreover, this thesis proposes the new concepts of Morphable FBE and Morphable
Rule, which consider the assembly of these NOP elements during application execution.
Secondly, a new dataset based on the popular Noscope has been developed by ad-
ding two more fields (color and ID), making it more suitable for this type of research. The
NS100KCOLORID dataset is available to the community to promote further research and com-
parisons.
Thirdly, a new video query language has been developed with support for many selecti-
ons and spatiotemporal operators. It is available for the community to use and improve.
Fourthly, systematic experiments were carried out and the results were compared
with those in the literature. In addition, an extensive experiment was performed with the entire
processing pipeline in the context of big data. In this way, the experiments evaluated the suitability


109
of the NOP Query method and its potential for processing large amounts of data and different
types of queries. These experiments can be useful for future work and comparisons with other
emerging technologies.
Finally, NOP Query is a prominent application that creates and manages thousands of
Rules, simultaneously demonstrating the NOP Framework C++ 4.0’s ability to process complex
queries. A priori, NOP Query can be used in any domain where the system receives inputs and
needs to process them with low latency to compute information or event/semantic inferences.
Additionally, this work has demonstrated the viability of NOP Query for applications that
require resource optimization and fast processing, especially in the context of video queries and
event matching.
It can be concluded that this thesis successfully addresses the thesis statement presented
in Chapter 1. Therefore, the contributions and findings demonstrate that NOP Query is capable
of processing video queries with both low computational cost and low latency.
5.2
FUTURE RESEARCH DIRECTIONS
Due to its original contribution and potentially great applicability, several future works
can be derived from this thesis.
As far as author know, this work is the first to focus solely on video event data and query
processing without considering tasks such as pre-processing, convolutional neural network costs,
and database operations. Therefore, the proposed solution and results show the real computational
cost without the burden of third-party computer vision and database libraries. Future work could
test the NOP query in the real world, considering a large surveillance system, using an entire
computer vision pipeline and GPU processing. NOPL support will be added, and the results will
be compared with the NOP Framework C++ 4.0 results.
Still, future work can include other query operators, such as those presented by (KANG
et al., 2019a; KANG et al., 2022; YADAV; CURRY, 2019a):
• The 𝑠𝑒𝑙𝑒𝑐𝑡𝑖𝑜𝑛operator allows the selection of particular objects or events of interest.
For example, users may search for instances of people.
• The 𝑎𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛operator allows computing some statistics over the video frames. Com-
mon aggregations include count, sum, average, maximum, and minimum operators.


110
For example, a city planner may be interested in computing the average number of cars
per frame or counting the number of pedestrians that cross in front of a camera.
• The 𝑙𝑖𝑚𝑖𝑡operator allows finding a cardinality-limited number of events occurring within
some time interval. For example, a city planner may search for ten instances of buses at
stop signs.
• The 𝑠𝑖𝑚𝑖𝑙𝑎𝑡𝑖𝑟𝑦operator allows searching for portions of the video similar to an input
frame or video clip. For example, a football analyst may input a frame or video clip of a
goal of a soccer player. Such queries often involve iterative, ad hoc analysis to arrive at the
final query.
• The 𝑗𝑜𝑖𝑛operator allows performing a join and, subsequently, a 𝑠𝑒𝑙𝑒𝑐𝑡𝑖𝑜𝑛, 𝑎𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛,
or 𝑙𝑖𝑚𝑖𝑡query. For example, an amber alert application may join extracted license plates
with an external data source.
• The 𝑝𝑟𝑜𝑗𝑒𝑐𝑡𝑖𝑜𝑛operator extracts only a part of the information to compute video events.
Other possible future work for NOP Query include the domain of Complex Event
Processing (CEP) systems, also known as event stream processing. This technology is used
to query data before storing them in a database or, in some cases, without storing them. The
main objective of CEP is to identify significant events, such as opportunities or threats, in real-
time situations and quickly respond to them. More details about CEP systems can be found
at (CUGOLA; MARGARA, 2015; CUGOLA; MARGARA, 2012). Examples of CEP systems
include:
• Stock market trading systems: real-time analysis of market data;
• Mobile devices: handling incoming streams of events.
• Fraud detection: identifying suspicious patterns.
• Business activity monitoring: monitoring business processes.
• Security monitoring: detecting anomalies.
• Transportation industry: real-time tracking.
• Governmental intelligence gathering: analyzing diverse data sources.


111
Moreover, the topics below present brief theoretical comparisons with NOP Query and
other related technologies, in order to glimpse the potential applicability of this method:
• Active Database X NOP Query: According to Cugola e Margara (2012), traditional
relational databases are passive, providing data only when explicitly requested by users or
applications.In contrast, active databases consist of a series of triggers that are fired when
certain conditions occur. They were developed to overcome the limitations of relational
databases. Interestingly, most modern relational databases include active database features
in the form of database triggers. However, this approach is challenging to maintain due to
the complexity of understanding the effects of these triggers. On the other hand, the NOP
Chain, the core of the NOP Query, is succinct, easy to understand, and easily maintainable.
The chain of notifications starts when some Attribute changes its value and notifies its
related Premise(s), feeding the notification chain. The NOP Query can be an engine for
a new type of (Re)active Database in which the Rules and related NOP elements are the
central focus instead of triggers.
• Knowledge Graph X NOP Query: Knowledge graphs are a structured representation
of facts consisting of entities, relations, and semantic descriptions. Entities can be real
objects or abstract concepts, edges represent the relationship between entities and semantic
descriptions contain properties with well-defined meanings (JI et al., 2022). They are
frequently used in various domains because of their rich structured knowledge. The
technology most closely related to NOP Query is the knowledge graph, as shown in Yadav
e Curry (2019c) and Yadav et al. (2020). Both technologies can express objects and
relationships through entities/nodes and connections.
• Information Retrieval X NOP Query: Information retrieval aims to find relevant documents
in a large collection, minimizing manual effort (UNTERKALMSTEINER et al., 2016;
HAMBARDE; PROENçA, 2023). Meanwhile, NOP Query also performs data/event retri-
eval following a different method from the existing literature, especially for applications
where the entries are regular, as the start of the notification chain depends on the change in
the values of Attribute(s). The NOP query can also support information retrieval offline,
e.g., without regular entries, but requires further experimentation to adapt to this context.
• Big Data X NOP Query: In the literature, video streaming applications also belong in the
big data context due to the high speed with which videos are generated, the large video


112
files stored, and the variety of video formats and sources (SELMY et al., 2024; ALAM et
al., 2020b). NOP Query’s features are suitable for the big data context due to the reduced
computational cost, the distributed elements (e.g., parallelizable), and the fact that they
avoid intensive writing to and reading from secondary memory, following current trends
in big data frameworks, such as Apache Spark1 and Apache Storm2.
• Incremental Learning X NOP Query: Traditional machine learning systems are implemen-
ted in a closed-world context, which requires all training data before the offline training
process (ZHOU et al., 2024). However, real-world applications often face the entry of new
classes, which requires the training of new models. NOP Query’s reactive and intuitive
approach can favor the detection of new classes when objects are left unlabeled in the
Morphable Rules for long periods. Approaches such as machine learning for data streams
(GOMES et al., 2019), novelty detection in data streams (COSTA et al., 2023) and open
world recognition (GUTOSKI et al., 2023) can be useful for inspiring new solutions based
on NOP concepts and tools.
1
https://spark.apache.org/
2
https://storm.apache.org/


113
REFERENCES
AAFAQ, Nayyer; MIAN, Ajmal; LIU, Wei; GILANI, Syed Zulqarnain; SHAH, Mubarak. Video
description: A survey of methods, datasets, and evaluation metrics. ACM Computing Surveys,
v. 52, n. 6, p. 1–37, 2019.
AGARWAL, Neil; NETRAVALI, Ravi. Boggart: Towards General-Purpose acceleration of
retrospective video analytics. In: 20th USENIX Symposium on Networked Systems Design
and Implementation (NSDI 23). Boston, MA: USENIX Association, 2023. p. 933–951. ISBN
978-1-939133-33-5.
ALAM, Aftab; KHAN, Muhammad Numan; KHAN, Jawad; LEE, Young-Koo. Intellibvr-
intelligent large-scale video retrieval for objects and events utilizing distributed deep-learning
and semantic approaches. In: IEEE. 2020 IEEE International Conference on Big Data and
Smart Computing (BigComp). [S.l.], 2020. p. 28–35.
ALAM, Aftab; ULLAH, Irfan; LEE, Young-Koo. Video big data analytics in the cloud: A
reference architecture, survey, opportunities, and open research issues. IEEE Access, v. 8, p.
152377–152422, 2020.
ANDERSON, Michael R.; CAFARELLA, Michael; ROS, German; WENISCH, Thomas F.
Physical representation-based predicate optimization for a visual analytics database. In:
Proceedings of the International Conference on Data Engineering. [S.l.: s.n.], 2019. v.
2019-April, p. 1466–1477.
BABU, Md Abu Ahammed. Notification Oriented Paradigm as a Green Technology:
Development of a Simulated Sensor Correlation Application with NOP C++ Framework
4.0 and Comparing Green Aspects with usual OOP Languages. 2022. Dissertação (Mestrado)
— Luleå University of Technology, Department of Computer Science, Electrical and Space
Engineering, 2022.
BANASZEWSKI, Roni Fábio. Paradigma Orientado a Notificações - Avanços e
Comparações. 2009. Dissertação (Mestrado) — Curso de Pós-Graduação em Engenharia
Elétrica e Informática Industrial (CPGEI), Universidade Tecnológica Federal do Paraná
(UTFPR), Curitiba, 2009.
BELMONTE, Danillo L; RONSZCKA, Adriano F; LINHARES, Robson R; BANASZEWSKI,
Roni F; TACLA, Cesar A; STADZISZ, Paulo C; BATISTA, Márcio V et al. Notification-oriented
and object-oriented paradigms comparison via sale system. Journal of Software Engineering
and Applications, v. 5, n. 9, p. 695–710, 2012.


114
BOCHKOVSKIY, Alexey; WANG, Chien-Yao; LIAO, Hong-Yuan Mark. Yolov4: Optimal
speed and accuracy of object detection. CoRR, abs/2004.10934, 2020. Disponível em:
https://arxiv.org/abs/2004.10934.
BROOKSHEAR, J Glenn. Computer Science: An Overview. 11. ed. [S.l.]: Prentice Hall, 2011.
CANEL, Christopher; KIM, Thomas; ZHOU, Giulio; LI, Conglong; LIM, Hyeontaek;
ANDERSEN, David G; KAMINSKY, Michael; DULLOOR, Subramanya. Scaling video
analytics on constrained edge nodes. In: TALWALKAR, A.; SMITH, V.; ZAHARIA, M. (Ed.).
Proceedings of Machine Learning and Systems. [S.l.: s.n.], 2019. v. 1, p. 406–417.
CHAO, Daren; CHEN, Kaiwen; KOUDAS, Nick. SVQ-ACT: Querying for Actions over Videos.
In: IEEE 39th International Conference on Data Engineering (ICDE). [S.l.: s.n.], 2023. p.
3599–3602.
CHAO, Daren; KOUDAS, Nick; XARCHAKOS, Ioannis. SVQ++: Querying for Object
Interactions in Video Streams. In: Proceedings of the 2020 ACM SIGMOD International
Conference on Management of Data. New York, NY, USA: Association for Computing
Machinery, 2020. (SIGMOD ’20), p. 2769–2772. ISBN 9781450367356. Disponível em:
https://doi.org/10.1145/3318464.3384701.
CHEN, Yueting; YU, Xiaohui; KOUDAS, Nick. Ranked window query retrieval over video
repositories. In: IEEE International Conference on Data Engineering. [S.l.: s.n.], 2022. p.
2776–2791.
CHOLLET, Francois. Deep learning with Python. Shelter Island, NY, USA: Simon and
Schuster, 2021.
CHUNDURI, Pramod; BANG, Jaeho; LU, Yao; ARULRAJ, Joy. Zeus: Efficiently localizing
actions in videos using reinforcement learning. In: Proc. of the 2022 International Conference
on Management of Data. New York, NY, USA: ACM, 2022. p. 545–558.
CLOUDERA. Cloudera Apache Kafka Guide. Pallo Alto, California, USA: Cloudera, Inc,
2019.
COLLINS, Zachary. Active database interface for video search. 2020. Dissertação (Master of
Engineering Thesis) — Massachusetts Institute of Technology, 2020.
CONFLUENT. Introduction to Apache Kafka. 2024. Disponível em: https://docs.confluent.io/
kafka/introduction.html.


115
CORRAL-GARCÍA, Javier; LEMUS-PRIETO, Felipe; GONZÁLEZ-SÁNCHEZ, José-Luis;
PÉREZ-TOLEDANO, Miguel-Ángel. Analysis of energy consumption and optimization
techniques for writing energy-efficient code. Electronics, v. 8, n. 10, p. 1192, 2019.
COSTA, Joel D.; FARIA, Elaine R.; SILVA, Jonathan A.; GAMA, João; CERRI, Ricardo.
Novelty detection for multi-label stream classification under extreme verification latency.
Applied Soft Computing, v. 141, p. 110265, 2023. ISSN 1568-4946.
CUGOLA, Gianpaolo; MARGARA, Alessandro. Processing flows of information: From data
stream to complex event processing. ACM Computing Surveys (CSUR), v. 44, n. 3, p. 1–62,
2012.
CUGOLA, Gianpaolo; MARGARA, Alessandro. The complex event processing paradigm. In:
. Data Management in Pervasive Systems. Cham: Springer, 2015. p. 113–133.
DAUM, Maureen; HAYNES, Brandon; HE, Dong; MAZUMDAR, Amrita; BALAZINSKA,
Magdalena. TASM: A tile-based storage manager for video analytics. In: Proc. of IEEE 37th
International Conference on Data Engineering. [S.l.: s.n.], 2021. p. 1775–1786.
de Boer, M. H. T.; ESCHER, C; SCHUTTE, K. Modelling temporal structures in video event
retrieval using an AND-OR graph. In: Proc. of the Ninth International Conferences on
Advances in Multimedia. Venice, Italy: [s.n.], 2017. p. 85–88.
DÖNDERLER, Mehmet Emin; SAYKOL, Ediz; ARSLAN, Umut; ULUSOY, Özgür;
GÜDÜKBAY, Ulugur. BilVideo: Design and implementation of a video database management
system. Multimedia Tools and Applications, Springer, v. 27, n. 1, p. 79–104, 2005.
DONG, Shi; WANG, Ping; ABBAS, Khushnood. A survey on deep learning and its applications.
Computer Science Reviews, v. 40, n. C, 2021.
FABRO, João Alberto; SANTOS, Leonardo Araujo; FREITAS, Matheus Diniz de; RONSZCKA,
Adriano Francisco; SIMÃO, Jean Marcelo. NOPL-notification oriented programming language –
a new language and its application to program a robotic soccer team. In: Proc. of the EPIA
Conference on Artificial Intelligence. Cham: Springer International Publishing, 2021. p.
445–455.
FARHADI, Ali; REDMON, Joseph. Yolov3: An incremental improvement. arXiv preprint
arXiv:1804.02767, v. 1804, p. 1–6, 2018.
FERREIRA, Cleverson Avelino. Linguagem e compilador para o Paradigma Orientado a
Notificações – avanços e comparações. 2015. Dissertação (Master of Engineering Thesis) —
Federal University of Technology - Paraná (UTFPR), Curitiba, PR, Brazil, 2015.


116
FIGUEIREDO, Luis Henrique Pelegrin. NOP Framework C++ 4.0 IoT: Notification Oriented
Paradigm for Internet of Things Environment. 2022. Dissertação (Mestrado) — Federal
University of Technology - Paraná (UTFPR), Curitiba, PR, Brazil, 2022.
FRANCOIS, Alexandre R J; NEVATIA, Ram; HOBBS, Jerry; BOLLES, Robert C; SMITH,
John R; HWANG, Eenjun; SUBRAHMANIAN, V S. VERL: an ontology framework for
representing and annotating video events. Journal of visual communication and image
representation, Elsevier, v. 12, n. 4, p. 44–60, 1996.
FURHT, Borko; VILLANUSTRE, Flavio. Introduction to big data. Big data technologies and
applications, Springer, p. 3–11, 2016.
GABBRIELLI, M; MARTINI, S. Programming Languages: Principles and Paradigms. 1st.
ed. [S.l.: s.n.], 2010. (Undergraduate Topics).
GIATRAKOS, Nikos; ALEVIZOS, Elias; ARTIKIS, Alexander; DELIGIANNAKIS, Antonios;
GAROFALAKIS, Minos. Complex event recognition in the big data era: a survey. The VLDB
Journal, Springer, v. 29, n. 1, p. 313–352, 2020.
GOMES, Heitor Murilo; READ, Jesse; BIFET, Albert; BARDDAL, Jean Paul; GAMA, João.
Machine learning for streaming data: state of the art, challenges, and opportunities. ACM
SIGKDD Explorations Newsletter, ACM New York, NY, USA, v. 21, n. 2, p. 6–22, 2019.
GOODFELLOW, Ian; BENGIO, Yoshua; COURVILLE, Aaron. Deep Learning. [S.l.]: MIT
Press, 2016. ISBN 978-0262035613.
GUTOSKI, Matheus; LAZZARETTI, André Eugenio; LOPES, Heitor Silvério. Unsupervised
open-world human action recognition. Pattern Analysis and Applications, Springer, v. 26, n. 4,
p. 1753–1770, 2023.
HAMBARDE, Kailash A.; PROENçA, Hugo. Information retrieval: Recent advances and
beyond. IEEE Access, v. 11, p. 76581–76604, 2023.
HAN, Seungyeop; SHEN, Haichen; PHILIPOSE, Matthai; AGARWAL, Sharad; WOLMAN,
Alec; KRISHNAMURTHY, Arvind. MCDNN: An approximation-based execution framework
for deep stream processing under resource constraints. In: Proc. of the 14th Annual
International Conference on Mobile Systems, Applications, and Services. New York, NY,
USA: Association for Computing Machinery, 2016. p. 123–136. ISBN 9781450342698.
HAYNES, Brandon; DAUM, Maureen; HE, Dong; MAZUMDAR, Amrita; BALAZINSKA,
Magdalena; CHEUNG, Alvin; CEZE, Luis. Vss: A storage system for video analytics. In: Proc.
of International Conference on Management of Data. New York, NY, USA: Association for
Computing Machinery, 2021. (SIGMOD ’21), p. 685–696. ISBN 9781450383431.


117
HAYNES, Brandon; DAUM, Maureen; MAZUMDAR, Amrita; BALAZINSKA, Magdalena;
CHEUNG, Alvin; CEZE, Luis. VisualWorldDB: A DBMS for the Visual World. In: Proc. of
Conference on Innovative Data Systems Research. [S.l.: s.n.], 2020.
HAYNES, Brandon; MAZUMDAR, Amrita; ALAGHI, Armin; BALAZINSKA, Magdalena;
CEZE, Luis; CHEUNG, Alvin. LightDB: A DBMS for Virtual Reality Video. Proceedings of
the VLDB Endowment, v. 11, n. 10, p. 1192–1205, 2018.
HE, Kaiming; GKIOXARI, Georgia; DOLLÁR, Piotr; GIRSHICK, Ross. Mask r-cnn. In:
Proceedings of the IEEE international conference on computer vision. [S.l.: s.n.], 2017. p.
2961–2969.
HE, Kaiming; ZHANG, Xiangyu; REN, Shaoqing; SUN, Jian. Deep Residual Learning for
Image Recognition. In: Proceedings of the IEEE conference on computer vision and pattern
recognition. [S.l.: s.n.], 2016. p. 770–778.
HOLE, See Jackson. Jackson Hole, Wyoming – Town Square Live Cam. 2018. Disponível
em: https://www.youtube.com/watch?v=1EiC9bvVGnk.
HONARPARVAR, Sepehr; ASHENA, Zahra Bagheri; SAEEDI, Sara; LIANG, Steve. A
systematic review of event-matching methods for complex event detection in video streams.
Sensors, v. 24, n. 22, 2024. ISSN 1424-8220.
HÖNIG, Robert; ACKERMANN, Jan; CHI, Mingyuan. Bi-encoder cascades for efficient image
search. In: IEEE/CVF International Conference on Computer Vision Workshops. [S.l.: s.n.],
2023. p. 1350–1355.
HSIEH, Kevin. Machine Learning Systems for Highly-Distributed and Rapidly-Growing
Data. 2019. Tese (PhD Thesis) — Carnegie Mellon University, Pittsburgh, USA, 2019.
HSIEH, Kevin; ANANTHANARAYANAN, Ganesh; BODIK, Peter; VENKATARAMAN,
Shivaram; BAHL, Paramvir; PHILIPOSE, Matthai; GIBBONS, Phillip B; MUTLU, Onur.
Focus: Querying large video datasets with low latency and low cost. In: Proceedings of the 13th
USENIX Symposium on Operating Systems Design and Implementation. Carlsbad, CA,
USA: [s.n.], 2018. p. 269–286.
HUNG, Chien Chun; ANANTHANARAYANAN, Ganesh; BODIK, Peter; GOLUBCHIK,
Leana; YU, Minlan; BAHL, Paramvir; PHILIPOSE, Matthai. VideoEdge: Processing camera
streams using hierarchical clusters. In: Proceedings - 2018 3rd ACM/IEEE Symposium on
Edge Computing, SEC 2018. [S.l.]: IEEE, 2018. p. 115–131.
HWANG, Eenjun; SUBRAHMANIAN, V S. Querying video libraries. Journal of Visual
Communication and Image Representation, Elsevier, v. 7, n. 1, p. 44–60, 1996.


118
HWANG, Jinwoo; KIM, Minsu; KIM, Daeun; NAM, Seungho; KIM, Yoonsung; KIM,
Dohee; SHARMA, Hardik; PARK, Jongse. CoVA: Exploiting Compressed-Domain analysis
to accelerate video analytics. In: USENIX Annual Technical Conference. [S.l.]: USENIX
Association, 2022. p. 707–722.
JI, Shaoxiong; PAN, Shirui; CAMBRIA, Erik; MARTTINEN, Pekka; YU, Philip S. A survey
on knowledge graphs: Representation, acquisition, and applications. IEEE Transactions on
Neural Networks and Learning Systems, v. 33, n. 2, p. 494–514, 2022.
JODOIN, Jean-Philippe; BILODEAU, Guillaume-Alexandre; SAUNIER, Nicolas. Urban
tracker: Multiple object tracking in urban mixed traffic. In: Proc. of IEEE Winter Conference
on Applications of Computer Vision. [S.l.: s.n.], 2014. p. 885–892.
JOHANSON, Arne; HASSELBRING, Wilhelm. Software engineering for computational
science: Past, present, future. Computing in Science & Engineering, IEEE, v. 20, n. 2, p.
90–109, 2018.
KABUKICHO, Shinjuku. Shinjuku Kabukicho Live Camera. 2020. Disponível em:
https://www.youtube.com/watch?v=EHkMjfMw7oU.
KAISLER, Stephen H. Software paradigms. Hoboken, New Jersey, USA: John Wiley & Sons,
2005.
KAKKAR, Gaurav Tarlok; CAO, Jiashen; CHUNDURI, Pramod et al. Eva: An end-to-end
exploratory video analytics system. In: Proceedings of the Seventh Workshop on Data
Management for End-to-End Machine Learning. New York, NY, USA: ACM, 2023.
KANG, Daniel. Efficient and Accurate Systems for Querying Unstructured Data. 2022.
Tese (PhD Thesis) — Stanford University, Palo Alto, USA, 2022.
KANG, Daniel; BAILIS, Peter; ZAHARIA, Matei. Blazeit: Optimizing declarative aggregation
and limit queries for neural network-based video analytics. Proceedings of VLDB Endowment,
v. 13, n. 4, p. 533–546, 2019.
KANG, Daniel; BAILIS, Peter; ZAHARIA, Matei. Challenges and opportunities in DNN-based
video analytics: A demonstration of the blazeit video query engine. In: Proceedings of the 9th
Biennial Conference on Innovative Data Systems Research. Asilomar, California, USA:
[s.n.], 2019.
KANG, Daniel; EMMONS, John; ABUZAID, Firas; BAILIS, Peter; ZAHARIA, Matei.
Noscope: Optimizing neural network queries over video at scale. Proceedings of the VLDB
Endowment, v. 10, n. 11, p. 1586–1597, 2017.


119
KANG, Daniel; GAN, Edward; BAILIS, Peter; HASHIMOTO, Tatsunori; ZAHARIA, Matei.
Approximate selection with guarantees using proxies. Proceedings of the VLDB Endowment,
v. 13, n. 12, p. 1990–2003, 2020.
KANG, Daniel; GUIBAS, John; BAILIS, Peter; HASHIMOTO, Tatsunori; SUN, Yi; ZAHARIA,
Matei. Accelerating approximate aggregation queries with expensive predicates. Proceedings of
the VLDB Endowment, v. 14, n. 11, p. 2341–2354, 2021.
KANG, Daniel; MATHUR, Ankit; VEERAMACHENENI, Teja; BAILIS, Peter; ZAHARIA,
Matei. Jointly optimizing preprocessing and inference for dnn-based visual analytics. In: . [S.l.:
s.n.], 2020. v. 14, n. 2, p. 87–100.
KANG, Daniel; ROMERO, Francisco; BAILIS, Peter; KOZYRAKIS, Christos; ZAHARIA,
Matei. VIVA: An end-to-end system for interactive video analytics. In: Proceedings of the 12th
Conference on Innovative Data Systems Research (CIDR). Chaminade, USA: [s.n.], 2022.
KERSCHBAUMER, Ricardo. Proposição do Paradigma Orientado a Notificações no
Desenvolvimento de Circuitos Lógico-Digitais Reconfiguráveis. 2018. Tese (Doutorado) —
Universidade Tecnológica Federal do Paraná, Curitiba, PR, Brazil, 2018.
KERSCHBAUMER, Ricardo; LINHARES, Robson R; SIMÃO, Jean M; STADZISZ, Paulo C;
LIMA, Carlos R Erig. Notification oriented paradigm to implement digital hardware. Journal of
Circuits, Systems and Computers, v. 27, n. 8, p. 1850124, 2018.
KHANI, Mehrdad; ANANTHANARAYANAN, Ganesh; HSIEH, Kevin; JIANG, Junchen;
NETRAVALI, Ravi; SHU, Yuanchao; ALIZADEH, Mohammad; BAHL, Victor. RECL:
Responsive Resource-Efficient continuous learning for video analytics. In: 20th USENIX
Symposium on Networked Systems Design and Implementation (NSDI 23). Boston, MA:
USENIX Association, 2023. p. 917–932. ISBN 978-1-939133-33-5.
KOSSOSKI, Clayton. Proposta de um método de teste para processos de desenvolvimento
de software usando o Paradigma Orientado a Notificações. 2015. Dissertação (Mestrado) —
Federal University of Technology - Paraná (UTFPR), Curitiba, PR, Brazil, 2015.
KOSSOSKI, Clayton; SIMÃO, Jean Marcelo; LOPES, Heitor Silvério. Modeling and
performance analysis of a notification-based method for processing video queries on the fly.
Applied Sciences, MDPI, v. 14, n. 9, p. 3566, 2024.
KOUDAS, Nick; LI, Raymond; XARCHAKOS, Ioannis. Video monitoring queries. IEEE
Transactions on Knowledge and Data Engineering, IEEE Educational Activities Department,
v. 34, n. 10, p. 5023–5036, 2022.


120
KRAFT, Peter; KANG, Daniel; NARAYANAN, Deepak; PALKAR, Shoumik; BAILIS, Peter;
ZAHARIA, Matei. A demonstration of willump: A statistically-aware end-to-end optimizer for
machine learning inference. Proceedings of the VLDB Endowment, v. 13, n. 12, p. 2833–2836,
2020.
KRISHNAN, Sanjay; DZIEDZIC, Adam; ELMORE, Aaron J. Deeplens: Towards a visual data
management system. In: Proc. of 9th Biennial Conference on Innovative Data Systems
Research. [S.l.: s.n.], 2018. p. 1–10.
KUO, Tony C T; CHEN, Arbee L P. A content-based query language for video databases. In:
IEEE. Proc. of the 3rd IEEE International Conference on Multimedia Computing and
Systems. [S.l.], 1996. p. 209–214.
LAI, Ziliang; HAN, Chenxia; LIU, Chris; ZHANG, Pengfei; LO, Eric; KAO, Ben. Top-k
deep video analytics: A probabilistic approach. In: . New York, NY, USA: Association for
Computing Machinery, 2021. (SIGMOD ’21), p. 1037–1050. ISBN 9781450383431. Disponível
em: https://doi.org/10.1145/3448016.3452786.
LAUSANNE, Ville de. Place de la Palud. 2020. Disponível em: https://www.youtube.com/
watch?v=GbAZX-NDPLg.
LEDESMA, M. K.; SIMÃO, J. M. Avanços em Paradigma Orientado a Notificações -
Framework PON C++ 4.5 e seu gerador de código em Tecnologia LingPON 3.0 (Advances
in Notification Oriented Paradigm - NOP Framework C++ 4.5 and its code generator in
NOPL Technology 3.0). Santa Helena, PR, Brazil: [s.n.], 2022. XII Seminário de Extensão
e Inovação (XII SEI - Extension and Innovation Seminar) & XXVII Seminário de Iniciação
Científica e Tecnológica da UTFPR (XXVII SICITE - UTFPR Scientific and Technological
Initiation Seminar).
LEMMER, Webcam. Binnenhaven lemmer. 2019. Disponível em: https://www.youtube.com/
watch?v=NyzxJMWxDeo.
LI, John Z; OZSU, M Tamer; SZAFRON, Duane; ORIA, Vincent. MOQL: A multimedia object
query language. In: Proc. of the 3rd International Workshop on Multimedia Information
Systems. [S.l.: s.n.], 1997. p. 19–28.
LI, Yuanqi; PADMANABHAN, Arthi; ZHAO, Pengzhan; WANG, Yufei; XU, Guoqing Harry;
NETRAVALI, Ravi. Reducto: On-camera filtering for resource-efficient real-time video
analytics. In: Proceedings of the Annual Conference of the ACM Special Interest
Group on Data Communication on the Applications, Technologies, Architectures, and
Protocols for Computer Communication. New York, NY, USA: Association for Computing
Machinery, 2020. (SIGCOMM ’20), p. 359–376. ISBN 9781450379557. Disponível em:
https://doi.org/10.1145/3387514.3405874.


121
LI, Ziyu; KATSIFODIMOS, Asterios; BOZZON, Alessandro; HOUBEN, Geert Jan. Complex
event processing on real-time video streams. In: CEUR Workshop Proceedings. [S.l.: s.n.],
2020. p. 2652.
LI, Ziyu; SCHöNFELD, Mariette; HAI, Rihan; BOZZON, Alessandro; KATSIFODIMOS,
Asterios. Optimizing machine learning inference queries for multiple objectives. In: 2023 IEEE
39th International Conference on Data Engineering Workshops (ICDEW). [S.l.: s.n.], 2023.
p. 74–78.
LINHARES, Robson Ribeiro. Contribuição para o desenvolvimento de uma arquitetura
de computação própria ao paradigma orientado a notificações. 2015. Tese (Doutorado) —
Universidade Tecnológica Federal do Paraná, Curitiba, PR, Brazil, 2015.
LINHARES, Robson R; PORDEUS, Leonardo F; SIMÃO, Jean M; STADZISZ, Paulo C.
NOCA a notification-oriented computer architecture: Prototype and simulator. IEEE Access,
v. 8, p. 37287–37304, 2020.
LIU, Meng; WANG, Xiang; NIE, Liqiang; TIAN, Qi; CHEN, Baoquan; CHUA, Tat-
Seng. Cross-modal moment localization in videos. In: Proceedings of the 26th ACM
International Conference on Multimedia. New York, NY, USA: Association for
Computing Machinery, 2018. (MM ’18), p. 843–851. ISBN 9781450356657. Disponível em:
https://doi.org/10.1145/3240508.3240549.
LIU, Wei; ANGUELOV, Dragomir; ERHAN, Dumitru; SZEGEDY, Christian; REED, Scott;
FU, Cheng Yang; BERG, Alexander C. SSD: Single shot multibox detector. Lecture Notes in
Computer Science, v. 9905, p. 21–37, 2016.
LU, Chenglang; LIU, Mingyong; WU, Zongda. SVQL: A SQL extended query language for
video databases. International Journal of Database Theory and Application, v. 8, n. 3, p.
235–248, 2015.
LU, Yao; CHOWDHERY, Aakanksha; KANDULA, Srikanth. Optasia: A Relational Platform
for Efficient Large-Scale Video Analytics. In: . New York, NY, USA: Association for
Computing Machinery, 2016. (SoCC ’16), p. 57–70. ISBN 9781450345255. Disponível em:
https://doi.org/10.1145/2987550.2987564.
LU, Yao; CHOWDHERY, Aakanksha; KANDULA, Srikanth; CHAUDHURI, Surajit.
Accelerating machine learning inference with probabilistic predicates. In: Proceedings of the
2018 International Conference on Management of Data. New York, NY, USA: Association
for Computing Machinery, 2018. (SIGMOD ’18), p. 1493–1508. ISBN 9781450347037.
Disponível em: https://doi.org/10.1145/3183713.3183751.
MEIER, Michael Kaufmann Andreas. SQL & NoSQL Databases: Models, Languages,
Consistency Options and Architectures for Big Data Management. [S.l.]: Springer, 2019.


122
MELO, Luiz Carlos Viana. Adaptação do paradigma orientado a notificações para
desenvolvimento de sistemas fuzzy. 2016. Dissertação (Mestrado) — Federal University of
Technology - Paraná (UTFPR), Curitiba, PR, Brazil, 2016.
MELTON, Jim; SIMON, Alan R. Understanding the new SQL: a complete guide. San
Francisco, CA, USA: Morgan Kaufmann, 1993.
MENDONÇA, Igor Thiago Marques. Metodologia de Projeto de Software Orientado a
Notificações. 2020. Tese (Doutorado) — Universidade Tecnológica Federal do Paraná, Curitiba,
PR, Brazil, 2020.
MENDONÇA, Igor Thiago Marques; SIMÃO, Jean Marcelo; STADZISZ, Paulo Cézar.
Notification-oriented software design methodology. IEEE Latin America Transactions, v. 18,
n. 06, p. 1144–1153, 2020.
MOLL, O.; BASTANI, F.; MADDEN, S.; STONEBRAKER, M.; GADEPALLY, V.; KRASKA,
T. Exsample: Efficient searches on video repositories through adaptive sampling. In: Proc. of
IEEE 38th International Conference on Data Engineering (ICDE). [S.l.: s.n.], 2022. p.
3065–3077.
MOT2016. Multiple object tracking benchmark. 2022. Disponível em: https:
//motchallenge.net/data/MOT16/.
MUCHALSKI, Fernando José; MAZIERO, Carlos Alberto; STADZISZ, Paulo Cezar; SIMÃO,
Jean Marcelo. Estudo Comparativo entre o Paradigma de Programação Orientado
a Objetos e o Paradigma Orientado a Notificações em um Sistema para Cálculo de
Produtividade. 2012. Relatórios do 3º trimestre de 2012 disciplina do PON (CPGEI/PPGCA).
MULLAPUDI, Ravi Teja; CHEN, Steven; ZHANG, Keyi; RAMANAN, Deva; FATAHALIAN,
Kayvon. Online model distillation for efficient video inference. In: Proceedings of the
IEEE/CVF International Conference on Computer Vision. [S.l.: s.n.], 2019. p. 3573–3582.
NAIR, Vinod; HINTON, Geoffrey E. Rectified linear units improve restricted boltzmann
machines. In: 27th International Confer- ence on Machine Learning (ICML). Haifa, Israel:
[s.n.], 2010.
NAUR, Peter; RANDELL, Brian. Software Engineering - Report on a conference sponsored
by the NATO Science Committee. [S.l.], 1968.
NEGRINI, Fabio. Tecnologia NOPL Erlang-Elixir – Paradigma Orientado a Notificações
via uma abordagem orientada a microatores assíncronos. 2019. Dissertação (Mestrado) —
Federal University of Technology - Paraná (UTFPR), Curitiba, PR, Brazil, 2019.


123
NEGRINI, Fabio; RONSZCKA, Adriano Francisco; LINHARES, Robson Ribeiro; FABRO,
João Alberto; STADZISZ, Paulo Cézar; SIMÃO, Jean Marcelo. NOPL-Erlang: Programação
multicore transparente em linguagem de alto nível [in portuguese]. Cadernos do IME-Série
Informática, v. 43, n. 2, p. 70–74, 2019.
NEVES, Felipe dos Santos; SIMÃO, Jean Marcelo; LINHARES, Robson Ribeiro. Application
of generic programming for the development of a C++ framework for the Notification Oriented
Paradigm. In: Proceedings of the 11th International Conference on Information Society and
Technology. Kopaonik, Serbia: [s.n.], 2021. v. 1, p. 56–61.
NEVES, Felipe Santos. Framework PON C++ 4.0: Contribuição para concepção de
aplicações no Paradigma Orientado a Notificações por meio de programação genérica
[in Portuguese]. 2021. Dissertação (Mestrado) — Federal University of Technology - Paraná
(UTFPR), Curitiba, PR, Brazil, 2021.
NIELSEN, Michael A. Neural networks and deep learning. San Francisco, CA, USA:
Determination Press, 2015. v. 25.
NOVAES, Paulo JD; SIMÃO, Jean M; STADZISZ, Paulo C. Integration between requirements
modeling and software development in the notification oriented paradigm: A security system
case study. Anais do Computer on the Beach, v. 9, p. 432–441, 2018.
NOVAES, Paulo José Dantas. Método e Linguagem para Modelagem Gráfica de Requisitos
de Software e Sistemas. 2019. Dissertação (Mestrado) — Federal University of Technology -
Paraná (UTFPR), Curitiba, PR, Brazil, 2019.
OGLE, Virginia E.; STONEBRAKER, Michael. Chabot: Retrieval from a Relational Database
of Images. Computer, v. 28, n. 9, p. 40–48, 1995.
OSHIRO, Larissa Keiko. Contribuição para o Paradigma Orientado a Notificações:
Evolução da Tecnologia LingPON 2.0 via Aprimoramento da Linguagem e Compilador
para Código Notificante Modular em C++. 2021. Dissertação (Mestrado) — Federal
University of Technology - Paraná (UTFPR), Curitiba, PR, Brazil, 2021.
OSHIRO, L. K.; RONSZKA, A. F.; FABRO, J. A.; SIMÃO, J. M. Linguagem e Compilador
para o Paradigma Orientado a Notificações: Uma Solução Performante Orientada a
Regras (Language and Compiler for the Notification-Driven Paradigm: A Performing
Rules-Driven Solution). São Paulo, SP, Brazil: [s.n.], 2021. 12th Regional High Performance
School of São Paulo (12ª Escola Regional de Alto Desempenho de São Paulo).
OUSSOUS, Ahmed; BENJELLOUN, Fatima-Zahra; LAHCEN, Ayoub Ait; BELFKIH,
Samir. Big data technologies: A survey. Journal of King Saud University-Computer and
Information Sciences, Elsevier, v. 30, n. 4, p. 431–448, 2018.


124
PAKHA, Chrisma; CHOWDHERY, Aakanksha; JIANG, Junchen. Reinventing video streaming
for distributed vision analytics. In: Proceedings of 10th USENIX Workshop on Hot Topics in
Cloud Computing. Boston, MA, USA: USENIX Association, 2018.
PARR, Terence. The Definitive ANTLR 4 Reference. Dallas, Texas, USA: The Pragmatic
Bookshelf, 2013.
PEREIRA, Rui; COUTO, Marco; RIBEIRO, Francisco; RUA, Rui; CUNHA, Jácome;
FERNANDES, João Paulo; SARAIVA, João. Energy efficiency across programming languages:
how do energy, time, and memory relate? In: Proceedings of the 10th ACM SIGPLAN
International Conference on Software Language Engineering. New York, NY, USA:
Association for Computing Machinery, 2017. (SLE 2017), p. 256–267. ISBN 9781450355254.
Disponível em: https://doi.org/10.1145/3136014.3136031.
PEREIRA, Rui; COUTO, Marco; RIBEIRO, Francisco; RUA, Rui; CUNHA, Jácome;
FERNANDES, João Paulo; SARAIVA, João. Ranking programming languages by energy
efficiency. Science of Computer Programming, Elsevier, v. 205, p. 102609, 2021.
PETERS, Eduardo; JASINSKI, Ricardo P; PEDRONI, Volnei A; SIMÃO, Jean M. A new
hardware coprocessor for accelerating notification-oriented applications. In: Proc. of the IEEE
International Conference on Field-Programmable Technology. Seoul, Korea: [s.n.], 2012. p.
257–260.
PHILBIN, James; CHUM, Ondrej; ISARD, Michael; SIVIC, Josef; ZISSERMAN, Andrew.
Object retrieval with large vocabularies and fast spatial matching. In: IEEE. 2007 IEEE
conference on computer vision and pattern recognition. Minneapolis, MN, USA, 2007.
p. 1–8.
POMS, Alex; CRICHTON, Will; HANRAHAN, Pat; FATAHALIAN, Kayvon. Scanner:
Efficient video analysis at scale. ACM Transactions on Graphics, v. 37, n. 4, p. 1–13, 2018.
PORDEUS, Leonardo Faix. Simulação de uma arquitetura de computação própria ao
Paradigma Orientado a Notificações. 2017. Dissertação (Mestrado) — Federal University of
Technology - Paraná (UTFPR), Curitiba, PR, Brazil, 2017.
PORDEUS, Leonardo Faix; LINHARES, R. R.; STADZISZ, P. C.; SIMÃO, J. M. NOP-DH–
evaluation over bitonic sort algorithm. Microprocessors and Microsystems, v. 85, p. 104314,
2021.
POUYANFAR, Samira; SADIQ, Saad; YAN, Yilin; TIAN, Haiman; TAO, Yudong; REYES,
Maria Presa; SHYU, Mei-Ling; CHEN, Shu-Ching; IYENGAR, S. S. A survey on deep learning:
Algorithms, techniques, and applications. ACM Computing Surveys, v. 51, n. 5, 2018.


125
POUYANFAR, Samira; YANG, Yimin; CHEN, Shu-Ching; SHYU, Mei-Ling; IYENGAR,
S. S. Multimedia big data analytics: A survey. ACM Computing Surveys, Association for
Computing Machinery, New York, NY, USA, v. 51, n. 1, jan 2018. ISSN 0360-0300. Disponível
em: https://doi.org/10.1145/3150226.
PUNCHIHEWA, Amal; BAILEY, Donald. A review of emerging video codecs: Challenges
and opportunities. In: IEEE. 2020 35th International Conference on Image and Vision
Computing New Zealand (IVCNZ). Wellington, New Zealand, 2020. p. 1–6.
QIN, An; XIAO, Mengbai; WU, Yongwei; HUANG, Xinjie; ZHANG, Xiaodong. Mixer:
efficiently understanding and retrieving visual content at web-scale. Proceedings of the VLDB
Endowment, v. 14, n. 12, p. 2906–2917, 2021.
RISTANI, Ergys; SOLERA, Francesco; ZOU, Roger; CUCCHIARA, Rita; TOMASI, Carlo.
Performance measures and a data set for multi-target, multi-camera tracking. In: Proc. of
European Conference on Computer Vision Workshop on Benchmarking Multi-Target
Tracking. Cham, Germany: [s.n.], 2016.
ROMERO, Francisco; HAUSWALD, Johann; PARTAP, Aditi; KANG, Daniel; ZAHARIA,
Matei; KOZYRAKIS, Christos. Optimizing video analytics with declarative model relationships.
Proceedings of the VLDB Endowment, v. 16, n. 3, p. 447–460, 2022.
RONSZCKA, Adriano Francisco. Contribuição para concepção de aplicações no Paradigma
Orientado a Notificações (PON) sob o viés de padrões. 2012. Dissertação (Mestrado) —
Federal University of Technology - Paraná (UTFPR), Curitiba, PR, Brazil, 2012.
RONSZCKA, Adriano Francisco. Método para a Criação de Linguagens de Programação e
Compiladores para o Paradigma Orientado a Notificações em Plataformas Distintas. 2019.
Tese (Doutorado) — Universidade Tecnológica Federal do Paraná, Curitiba, PR, Brazil, 2019.
RONSZCKA, Adriano F; BANASZEWSKI, Roni F; LINHARES, Robson R; TACLA, Cesar A;
STADZISZ, Paulo C; SIMÃO, Jean M. Notification-oriented and rete network inference: a
comparative study. In: Proc. of the IEEE International Conference on Systems, Man, and
Cybernetics. [S.l.: s.n.], 2015. p. 807–814.
RONSZCKA, Adriano Francisco; FERREIRA, Cleverson Avelino; STADZISZ, Paulo Cézar;
FABRO, João Alberto; SIMÃO, Jean Marcelo. Notification-oriented programming language and
compiler. In: Proc. of the VII Brazilian Symposium on Computing Systems Engineering.
Curitiba, PR, Brazil: [s.n.], 2017. p. 125–131.
RONSZCKA, Adriano Francisco; VALENCA, Glauber Zarate; LINHARES, Robson Ribeiro;
FABRO, João Alberto; STADZISZ, Paulo Cézar; SIMÃO, Jean Marcelo. Notification Oriented
Paradigm Framework 2.0: An implementation based on design patterns. IEEE Latin America
Transactions, v. 15, n. 11, p. 2220–2231, 2017.


126
ROSEBROCK, Adrian. Practical python and OpenCV – An introductory, example driven
guide to image processing and computer vision. Ebook: Pyimagesearch, 2016.
ROSEBROKE, Adrian. Deep Learning for Computer Vision with Python. Ebook:
PyImageSearch, 2017.
ROY, Peter Van. Programming paradigms for dummies: What every programmer should know.
New Computational Paradigms for Computer Music, IRCAM/Delatour France, p. 9, 2009.
ROY, Peter Van; HARIDI, Seif. Concepts, techniques, and models of computer programming.
Cambridge, MA, USA: MIT Press, 2004.
SAHA, Sumit. A Comprehensive Guide to Convolutional Neu-
ral Networks. 2018. Disponível em: https://towardsdatascience.com/
a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way.
SANDLER, Mark; HOWARD, Andrew; ZHU, Menglong; ZHMOGINOV, Andrey; CHEN,
Liang Chieh. MobileNetV2: Inverted Residuals and Linear Bottlenecks. Proceedings of the
IEEE Computer Society Conference on Computer Vision and Pattern Recognition, p.
4510–4520, 2018.
SANTOS, Leonardo Araújo. Linguagem e compilador para o Paradigma Orientado a
Notificações: Avanços para facilitar a codificação e sua validação em uma aplicação
de controle de futebol de robôs. 2017. Dissertação (Mestrado) — Federal University of
Technology - Paraná (UTFPR), Curitiba, PR, Brazil, 2017.
SANTOS, L. A.; SIMÃO, J. M.; FABRO, J. A. Linguagem e Compilador para o Paradigma
Orientado a Notificações: avanços para a redução de complexidade de código (Language
and Compiler for the Notification Oriented Paradigm: advances in reducing code
complexity). Curitiba, PR, Brazil: [s.n.], 2017. VII Brazilian Symposium on Computing Systems
Engineering (SBESC - Simpósio Brasileiro de Engenharia de Sistemas Computacionais).
¸SAYKOL, Ediz; GÜDÜKBAY, U˘gur; ULUSOY, Özgür. A database model for querying visual
surveillance videos by integrating semantic and low-level features. In: CANDAN, K. Selçuk;
CELENTANO, Augusto (Ed.). Proc. of Advances in Multimedia Information Systems.
Berlin, Germany: Springer, 2005. p. 163–176.
SCHOOL, Oxford Martin. Webcam from the Oxford Martin School on Broad Street. 2018.
Disponível em: https://www.youtube.com/watch?v=St7aTfoIdYQ.
SCHUTZ, Fernando. NeuroPON: Uma abordagem para o desenvolvimento de Redes
Neurais Artificiais utilizando o Paradigma Orientado a Notificações. 2019. Tese (Doutorado)
— Universidade Tecnológica Federal do Paraná, Curitiba, PR, Brazil, 2019.


127
SCHÜTZ, Fernando; FABRO, João A; RONSZCKA, Adriano F; STADZISZ, Paulo C;
SIMÃO, Jean M. Proposal of a declarative and parallelizable artificial neural network using the
notification oriented paradigm. Neural Computing and Applications, v. 30, n. 6, p. 1715–1731,
2018.
SEBESTA, Robert W. Concepts of Programming Languages. 12th. ed. New York, NY, USA:
Pearson, 2019.
SELMY, Hend A.; MOHAMED, Hoda K.; MEDHAT, Walaa. Big data analytics deep learning
techniques and applications: A survey. Information Systems, v. 120, p. 102318, 2024. ISSN
0306-4379.
SHEN, Haichen; HAN, Seungyeop; PHILIPOSE, Matthai; KRISHNAMURTHY, Arvind. Fast
video classification via adaptive cascading of deep models. In: Proc. of the IEEE Conference
on Computer Vision and Pattern Recognition. [S.l.]: IEEE, 2017. p. 3646–3654.
SHEN, Haichen; PHILIPOSE, Matthai; AGARWAL, Sharad; WOLMAN, Alec. MCDNN: An
Execution Framework for Deep Neural Networks on Resource-Constrained Devices. In: Proc. of
the 14th Annual International Conference on Mobile Systems, Applications, and Services.
[S.l.: s.n.], 2014. p. 123–136.
SILVEIRA, Tiago Buatim Nion da. Semantic-Related Challenges in Computational
Intelligence: a Transdisciplinary Approach. 2023. Tese (PhD Thesis) — Universidade
Tecnológica Federal do Paraná, Curitiba, PR, Brazil, 2023.
SIMÃO, Jean Marcelo. Proposta de uma Arquitetura de Controle para Sistemas Flexíveis
de Manufatura Baseada em Regras e Agentes. 2001. Dissertação (Mestrado) — Federal
University of Technology - Paraná (UTFPR), Curitiba, PR, Brazil, 2001.
SIMÃO, Jean Marcelo. A Contribution to the Development of a HMS Simulation Tool and
Proposition of a Metal-Model for Holonic Control. 2005. Tese (PhD. Thesis) — Centro
Federal de Educação Tecnológica do Paraná (CEFET-PR) and Henri Poincaré University (UHP),
Curitiba, PR, Brazil, 2005.
SIMÃO, Jean M; RENAUX, Douglas PB; LINHARES, Robson R; STADZISZ, Paulo C.
Evaluation of the notification oriented paradigm applied to sentient computing. In: Proceedings
of the IEEE 17th International Symposium on Object/Component/Service-Oriented
Real-Time Distributed Computing. [S.l.: s.n.], 2014. p. 253–260.
SIMÃO, Jean Marcelo; STADZISZ, Paulo Cézar. An agent-oriented inference engine applied for
supervisory control of automated manufacturing systems. In: Frontiers in Artificial Intelligence
and Applications (Advances in Logic, Artificial Intelligence and Robotics—LAPTEC 2002).
[S.l.]: IOS Press, 2002. v. 85, p. 234–241.


128
J. M. Simão e P. C. Stadzisz. Paradigma Orientado a Notificações (PON) Uma Técnica de
Composição e Execução de Software Orientada a Notificações (Notification Oriented
Paradigm (NOP) - A Notification Oriented Technique to Software Composition and
Execution). 2008. Patent Demandat INPI/Brasil (Instituto Nacional de Propriedade Industrial) -
Nº INPI/Brazil: PI08055181.
SIMÃO, Jean Marcelo; STADZISZ, Paulo Cézar. Inference based on notifications: a
holonic metamodel applied to control issues. IEEE Transactions on Systems, Man, and
Cybernetics-Part A: Systems and Humans, v. 39, n. 1, p. 238–250, 2009.
J. M. Simão e P. C. Stadzisz. Mecanismo de Resolução de Conflito e Garantia de
Determinismo para o Paradigma Orientado a Notificações (PON). 2010. Patent Demandat
INPI/Brasil (Instituto Nacional de Propriedade Industrial) - Nº INPI/Brazil: PI10002960.
SIMÃO, Jean Marcelo; TACLA, Cesar Augusto; STADZISZ, Paulo Cézar. Holonic control
metamodel. IEEE Transactions on Systems, Man, and Cybernetics – Part A: Systems and
Humans, v. 39, n. 5, p. 1126–1139, 2009.
SIMÃO, Jean M; TACLA, Cesar A; STADZISZ, Paulo C; BANASZEWSKI, Roni F. Notification
oriented paradigm (NOP) and imperative paradigm: A comparative study. Journal of Software
Engineering and Applications, v. 5, n. 6, p. 402–416, 2012.
SIMÃO, Jean Marcelo Simão; STADZISZ, Paulo Cézar. An agent-oriented fuzzy inference
engine. In: Simpósio Brasileiro de Automação Inteligente (SBAI). [S.l.: s.n.], 2003.
SIPSER, Aaron. Video ingress system for surveillance video querying. 2020. Dissertação
(Master of Engineering Thesis) — Massachusetts Institute of Technology, 2020.
SPOLAÔR, Newton; LEE, Huei Diana; TAKAKI, Weber Shoity Resende; ENSINA,
Leandro Augusto; COY, Claudio Saddy Rodrigues; WU, Feng Chung. A systematic review on
content-based video retrieval. Engineering Applications of Artificial Intelligence, Elsevier,
v. 90, p. 103557, 2020.
STONEBRAKER, Michael; BHARGAVA, Bharat; CAFARELLA, Michael; COLLINS,
Zachary; MCCLELLAN, Jenna; SIPSER, Aaron; SUN, Tao; NESEN, Alina; SOLAIMAN, K;
MANI, Ganapathy et al. Surveillance video querying with a human-in-the-loop. In: Proceedings
of the Workshop on Human-in-the-Loop Data Analytics. Portland, OR, USA: [s.n.], 2020. p.
14–19.
UNTERKALMSTEINER, Michael; GORSCHEK, Tony; FELDT, Robert; LAVESSON, Niklas.
Large-scale information retrieval in software engineering-an experience report from industrial
application. Empirical Software Engineering, Springer, v. 21, p. 2324–2365, 2016.


129
VALENçA, Glauber Z. Contribuição para a Materialização do Paradigma Orientado a
Notificações (PON) via Framework e Wizard. 2012. Dissertação (Mestrado) — Federal
University of Technology - Paraná (UTFPR), Curitiba, PR, Brazil, 2012.
WANG, Chien-Yao; BOCHKOVSKIY, Alexey; LIAO, Hong-Yuan Mark. Scaled-yolov4:
Scaling cross stage partial network. In: Proc. of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition (CVPR). [S.l.]: IEEE, 2021. p. 13029–13038.
WANG, Wei; GAO, Jinyang; ZHANG, Meihui; WANG, Sheng; CHEN, Gang; NG, Teck Khim;
OOI, Beng Chin; SHAO, Jie; REYAD, Moaz. Rafiki: Machine learning as an analytics service
system. Proceedings of the VLDB Endowment, v. 12, n. 2, p. 128–140, 2018.
WEN, Longyin; DU, Dawei; CAI, Zhaowei; LEI, Zhen; CHANG, Ming-Ching; QI, Honggang;
LIM, Jongwoo; YANG, Ming-Hsuan; LYU, Siwei. UA-DETRAC: A New Benchmark
and Protocol for Multi-Object Detection and Tracking. Computer Vision and Image
Understanding, v. 193, p. 102907, 2020.
WIECHETECK, Luciana Villas Boas. Método para projeto de software usando o Paradigma
Orientado a Notificações – PON. 2011. Dissertação (Mestrado) — Federal University of
Technology - Paraná (UTFPR), Curitiba, PR, Brazil, 2011.
WOJKE, Nicolai; BEWLEY, Alex; PAULUS, Dietrich. Simple online and realtime tracking with
a deep association metric. In: Proceedings of the IEEE International Conference on Image
Processing (ICIP). [S.l.: s.n.], 2017. p. 3645–3649.
XARCHAKOS, Ioannis; KOUDAS, Nick. Svq: Streaming video queries. In: Proceedings of the
2019 International Conference on Management of Data. New York, NY, USA: Association
for Computing Machinery, 2019. (SIGMOD ’19), p. 2013–2016. ISBN 9781450356435.
Disponível em: https://doi.org/10.1145/3299869.3320230.
XAVIER, R. D. Paradigmas de Desenvolvimento de Software: Comparação entre
abordagens Orientada a Eventos e Orientada a Notificações (Software Development
Paradigms: Comparison between Event Driven and Notification Oriented Approaches).
2014. Dissertação (Mestrado) — Federal University of Technology - Paraná (UTFPR), Curitiba,
PR, Brazil, 2014.
XIPG. Xipg Video Test Media. 2021. Disponível em: https://media.xiph.org/video/derf/.
XU, Tiantu; BOTELHO, Luis Materon; LIN, Felix Xiaozhu. VStore: A data store for analytics
on large videos. In: Proceedings of the 14th EuroSys Conference. New York, NY, USA:
Association for Computing Machinery, 2019. p. 1–17. ISBN 9781450362818.


130
YADAV, Piyush. High-performance complex event processing framework to detect event patterns
over video streams. In: Proceedings of the 20th International Middleware Conference
Doctoral Symposium. New York, NY, USA: Association for Computing Machinery, 2019. p.
47–50.
YADAV, Piyush. Query-aware adaptive windowing for spatiotemporal complex video
event processing for internet of multimedia things. 2021. Tese (Doutorado) — University of
Galway, Ireland, 2021.
YADAV, Piyush; CURRY, Edward. VEKG: Video event knowledge graph to represent video
streams for complex event pattern matching. In: Proceedings of the IEEE First International
Conference on Graph Computing. Laguna Hills, CA, USA: IEEE, 2019. p. 13–20.
YADAV, Piyush; CURRY, Edward. VidCEP: Complex Event Processing Framework to Detect
Spatiotemporal Patterns in Video Streams. In: Proc. of IEEE International Conference on Big
Data. Los Angeles, CA, USA: IEEE, 2019. p. 2513–2522.
YADAV, Piyush; CURRY, Edward. VidCEP: Complex event processing framework to detect
spatiotemporal patterns in video streams. In: Proceedings of the IEEE International
Conference on Big Data. New York, NY, USA: Association for Computing Machinery, 2019. p.
2513–2522.
YADAV, Piyush; SALWALA, Dhaval; CURRY, Edward. Vid-win: Fast video event matching
with query-aware windowing at the edge for the internet of multimedia things. IEEE Internet of
Things Journal, 2021.
YADAV, Piyush; SALWALA, Dhaval; CURRY, Edward. Vid-win: Fast video event matching
with query-aware windowing at the edge for the internet of multimedia things. IEEE Internet of
Things Journal, 2021.
YADAV, Piyush; SALWALA, Dhaval; DAS, Dibya Prakash; CURRY, Edward. Knowledge
graph driven approach to represent video streams for spatiotemporal event pattern matching in
complex event processing. International Journal of Semantic Computing, v. 14, n. 03, p.
423–455, 2020.
YANG, Zhihui; WANG, Zuozhi; HUANG, Yicong; LU, Yao; LI, Chen; WANG, X. Sean.
Optimizing machine learning inference queries with correlative proxy models. Proceedings of
the VLDB Endowment, v. 15, n. 10, p. 2032–2044, 2022.
YI, Shanhe; HAO, Zijiang; ZHANG, Quan Qingyang; ZHANG, Quan Qingyang; SHI, Weisong;
LI, Qun. LAVEA: Latency-Aware video analytics on edge computing platform. In: Proceedings
of the International Conference on Distributed Computing Systems. New York, NY, USA:
Association for Computing Machinery, 2017. p. 2573–2574. ISBN 9781450350877.


131
ZHANG, Haoyu; ANANTHANARAYANAN, Ganesh; BODIK, Peter; PHILIPOSE, Matthai;
BAHL, Paramvir; FREEDMAN, Michael J. Live video analytics at scale with approximation and
delay-tolerance. In: Proceedings of the 14th USENIX Symposium on Networked Systems
Design and Implementation. Boston, MA: USENIX Association, 2017. p. 377–392. ISBN
978-1-931971-37-9.
ZHANG, Yuhao; KUMAR, Arun. Panorama: a data system for unbounded vocabulary querying
over video. Proceedings of the VLDB Endowment, v. 13, n. 4, p. 477–491, 2019.
ZHOU, Da-Wei; SUN, Hai-Long; NING, Jingyi; YE, Han-Jia; ZHAN, De-Chuan. Continual
learning with pre-trained models: A survey. In: IJCAI. [S.l.: s.n.], 2024. p. 8363–8371.
ZYKOV, Sergey V. Managing software crisis: a smart way to enterprise agility. Cham,
Switzerland: Springer, 2018. v. 92.


APPENDICES


133
APPENDIX A – INSTANCES OF THE FBES AND RULES – NOP QUERY
This appendix presents the instances of all the FBEs and Rules required by the NOP
Query method. Each query operator is then explained below.
The use of the OBJECT Operator is exemplified in Listing A.1, following the NOP
Query Lang syntax, and the corresponding output which is produced in JSON format. Figure 53
shows the FBE and Rule instances produced. This is a very simple operator, as it only requires
one FBE and one Rule to implement the query. Basically, when a FBE with the desired label
(e.g., car) appears within the time window (e.g., 10 seconds), the Rule is activated with its
corresponding Instigation and Method.
Listing A.1 – Exmaple of NOP Query Lang and OBJECT operator
1−−−−OBJECT i n p u t :
2
SELECT ( o b j e c t ) FROM camera1 WHERE Object [ 1 ] . l a b e l = car WINDOW=10
3−−−−OBJECT output :
4
[{" o p e r a t o r " : " o b j e c t "} ,{" window " : " 1 0 " } ,
5
{" o b j e c t s " : [ { " number " : " 1 " , " c o l o r " : " none " ," l a b e l " : " car "}]} ,
6
{" s p a t i a l O p e r a t o r s " : [ ] } , { " countOperator " : { } } ]
Figure 53 – Instances of the OBJECT operator
(a) OBJECT Operator FBE
(b) OBJECT Operator Rule
Source: Developed by the author
The use of the CONJ Operator is exemplified in Listing A.2, following the NOP Query
Lang syntax, and the corresponding output which is produced in JSON format. Figure 54 shows
the FBEs and Rule instances produced. This conjunction operator requires two FBEs to evaluate
and produce the desired result. It is therefore more complex than the OBJECT operator. Basically,


134
when both FBEs (e.g., bus and truck) appear in the same frame within a given time window (e.g.
10 seconds), the Rule is fired. In addition, attributes such as label and color are supported.
Listing A.2 – Example of NOP Query Lang and CONJ operator
1−−−−CONJ i n p u t :
2
SELECT ( conj ) FROM camera1 WHERE Object [ 1 ] . l a b e l = car
3
AND Object [ 2 ] . l a b e l = t r u c k WINDOW=10
4−−−−CONJ output
5
[{" o p e r a t o r " : " conj "} ,{" window " : " 1 0 " } ,
6
{" o b j e c t s " : [ { " number " : " 1 " , " c o l o r " : " none " ," l a b e l " : " car "} ,
7
{" number " : " 2 " , " c o l o r " : " none " ," l a b e l " : " t r u c k " } ] } ]
Figure 54 – Instances of the CONJ operator
(a) CONJ Operator FBE
(b) CONJ Operator Rule
Source: Developed by the author
The use of the LEFT Operator is exemplified in Listing A.3, following the NOP Query
Lang syntax, and the corresponding output which is produced in JSON format. Figure 55 shows
the FBEs and Rule instances produced. The spatial operators (e.g., left, right, below, above)


135
requires two FBEs to evaluate and produce the desired result. It is therefore more complex than
the CONJ operator. Basically, when a car FBE appears to the left of a truck FBE in the same
frame within a given time window (e.g. 10 seconds), the Rule is fired. In addition, attributes such
as right, above and below are supported. Spatial attributes add more processing cost because
when each position (e.g., atPosX or atPosY) is updated by FBEs a new notification is produced.
Listing A.3 – Example of NOP Query Lang and LEFT operator
1−−−−LEFT i n p u t
2
SELECT ( l e f t ) FROM camera1 WHERE Object [ 1 ] . l a b e l = car
3
AND Object [ 2 ] . l a b e l = t r u c k AND
4
( Object [ 1 ] LEFT Object [ 2 ] ) WINDOW=10
5−−−−LEFT output
6
[{" o p e r a t o r " : " l e f t "} ,{" window " : " 1 0 " } ,
7
{" o b j e c t s " : [ { " number " : " 1 " , " c o l o r " : " none " ," l a b e l " : " car "} ,
8
{" number " : " 2 " , " c o l o r " : " none " ," l a b e l " : " t r u c k "}]} ,
9
{" s p a t i a l O p e r a t o r s " : [ { " f i r s t O p e r a n d " : " 1 " , " secondOperand " : " 2 " ,
10
" o p e r a t o r " : " LEFT " } ] } ]
The use of the SEQ Operator is exemplified in Listing A.4, following the NOP Query
Lang syntax, and the corresponding output which is produced in JSON format. Figure 56 shows
the FBEs and Rule instances produced. This operator is more complex than the LEFT operator
because it requires three Rules. In the example, the query evaluates the sequence or temporal
relationship of two FBEs (e.g. car and truck) for each frame, given the temporal window interval
(e.g., 10 seconds).
Listing A.4 – Example of NOP Query Lang and SEQ operator
1−−−−SEQ i n p u t
2
SELECT ( seq ) FROM camera1
3
WHERE Object [ 1 ] . l a b e l = car AND
4
Object [ 2 ] . l a b e l = t r u c k WINDOW=10
5−−−−SEQ output
6
[{" o p e r a t o r " : " seq "} ,{" window " : " 1 0 " } ,
7
{" o b j e c t s " : [ { " number " : " 1 " , " c o l o r " : " none " ," l a b e l " : " car "} ,
8
{" number " : " 2 " , " l a b e l " : " t r u c k " ," c o l o r " : " none " ," l a b e l " : " none " } ] } ]


136
Figure 55 – Instances of the LEFT operator
(a) LEFT operator FBEs
(b) LEFT operator Rules
Source: Developed by the author
The use of the COUNT Operator is exemplified in Listing A.5, following the NOP
Query Lang syntax, and the corresponding output which is produced in JSON format. Figure 57
shows the FBEs and the Figure 58 presents the Rule instances produced. This operator is more
complex than the previous ones, because it counts the number of objects (e.g., 5), evaluating their
temporal occurrence within the same time window (e.g., 10 seconds) for each frame. Various
Attributes are used to control the flow of this operator, including when the Rule fires and when
it resets the counter. Each of the five Rules used to implement the Count operator is explained
below:
• Rule Count Minimum Objects Intra Frame: Counts the number of objects in the same
frame (e.g., 5).
• Rule Count Reached: Sends an alert when the Count operator matches the query.


137
Figure 56 – Instances of the SEQ operator
(a) SEQ Operator FBE
(b) SEQ Operator Rules
Source: Developed by the author


138
• Rule Reset Intra Frame: Resets the count if the number of objects in a frame is less than
the minimum (e.g., 5).
• Rule Reset Inter Frames: Resets the count if the number of objects between two frames is
less than the minimum (e.g., 5).
• Rule Object in frame: Sends an alert when an object is in a frame.
Listing A.5 – Example of NOP Query Lang and COUNT operator
1−−−−COUNT i n p u t
2
SELECT ( count ) FROM camera1 COUNT( Object ) >= 5 FOREACH_FRAME WINDOW
3−−−−COUNT output
4
[{" o p e r a t o r " : " count "} ,{" window " : " 1 0 " } ,
5
{" countOperator " : { " countValue " : " 5 " , " countOperator ":" >="}}]
Figure 57 – Instances of the FBEs – COUNT Operator
Source: Developed by the author
Finally, the use of the Time Manager FBE is exemplified in Listing A.5, following
the NOP Query Lang syntax, and the corresponding output which is produced in JSON format.


139
Figure 58 – Instances of the Rules – COUNT Operator
Source: Developed by the author
Figure 59 shows the FBEs instances and Figure 60 shows the Rules instances produced. This
is the most important FBE and Rules because it controls the time of all operators. Below, each
Attribute is explained:
• atStart: Stores the start of the time window.
• atEnd: Stores the end of the time window. It is calculated according to this formula:
𝑎𝑡𝐸𝑛𝑑= 𝑎𝑡𝑆𝑡𝑎𝑟𝑡+ 𝑎𝑡𝑇𝑖𝑚𝑒𝑊𝑖𝑛𝑑𝑜𝑤𝑆𝑖𝑧𝑒.
• atPrevious: Stores the number of the previous frame.
• atTimeWindowSize: Stores the size of the time window specified in the query.
• atTimeChanged: Is set to True when the frame number is changed.
• atCountObjectIntraFrame: Stores the count of the number of objects in the same frame.
• atCountObjectInterFrames: Stores the count of objects between different frames.


140
• atLastIntraFrame: Stores the number of the last frame containing the expected number of
objects (e.g. 5).
• atLastInterFrame: Stores the last frame containing the expected number of objects.
• atCurrentFrame: Stores the current frame number.
• atLastFrameCountReached: Stores the last frame when the Count Rule was triggered.
• atGreatTimeDifference: Stores the number of frames between the last Count reached and
the current frame number.
• atMinimumCountIntraFrame: Stores the number of minimum objects in the same frame.
Figure 59 – Instances of the Time Manager FBE
Source: Developed by the author


141
Figure 60 – Instances of the Time Manager Rules
Source: Developed by the author


142
APPENDIX B – TOKENS AND PRODUCTIONS OF THE PROPOSED NOP QUERY
LANG
This appendix presents the tokens (Listing B.1) and productions (Listing B.2) of the
proposed NOP Query Language (NOPQL), using the ANTLRv41 Java library for development.
This prototypical language is based on VEQL (YADAV; CURRY, 2019c), but it differs in several
key aspects: it requires parentheses for each object (e.g., Object[1], Object[2]); the WINDOW
clause does not require a complement (e.g., WITHIN TIMEFRAME_WINDOW(10)); and the
WITH_CONFIDENCE clause is unnecessary, as the language only considers objects with a
confidence level of 50% and above. In this version, the same operators as those in VEQL have
been retained to enable comparison with the literature. Additionally, the NOP Query Lang is
freely available for study, use, and modify.
Listing B.1 – Productions of the NOP Query Language
1 SELECT :
’SELECT ’ ;
2 OBJECT :
’ Object ’ ;
3 WINDOW:
’WINDOW’ ;
4 PAR_OPEN:
’ ( ’ ;
5 PAR_CLOSE : ’ ) ’ ;
6 BRACK_OPEN:
’ [ ’ ;
7 BRACK_CLOSE:
’ ] ’ ;
8 LEFT :
’LEFT ’ ;
9 BELOW:
’BELOW’ ;
10 COUNT:
’COUNT’ ;
11 FROM:
’FROM’ ;
12 WHERE:
’WHERE’ ;
13 DOT:
’ . ’ ;
14 AND:
’AND’ ;
15 SEMICOLON:
’ ; ’ ;
16 COMMA:
’ , ’ ;
17 EQ:
’= ’;
18 EQUAL:
’EQUAL’ ;
1
https://github.com/jpavlich/antlr4-tutorial/blob/master/doc/instalacion.md


143
19 NEQ:
’ < > ’;
20 GREATEREQUAL:
’ >= ’;
21 FOREACHFRAME:
’FOREACH\_FRAME’ ;
22 ID :
[ a−zA−Z \ _ ] [ a−zA−Z \ _0 −9]*;
23 NUMBER:
[0 −9]+;
24 WS:
[
\ t e x t b a c k s l a s h {n }\ t e x t b a c k s l a s h { t }\ t e x t b a c k s l a s h { r }]+ −> skip ;
Listing B.2 – Productions of the NOP Query Language
1 s e l e c t : SELECT o p e r a t o r
from
( where )*
( count )* window {
2
logGenerator . showSymbolTable ( symbolTable ) ;
3
logGenerator . generateJSON ( symbolTable ,
o b j e c t L i s t ,
s p a t i a l O p e r a t o r s L i s t
4
jsonCountOperator ) ;
5
\ \
generateCSV ( ) ;
6 };
7
8 o p e r a t o r : PAR_OPEN op PAR_CLOSE {
9 System . out . p r i n t l n ( $op . t e x t ) ;
10
i f ( $op . value . equals ( " o b j e c t " )
| |
$op . value . equals ( " conj " )
11
| |
$op . value . equals ( " l e f t " )
| |
$op . value . equals ( " seq " )
12
| |
$op . value . equals ( " count " ) ) {
13
symbolTable . put ( " o p e r a t o r " ,
$op . t e x t ) ;
14 }
15 };
16
17 op
r e t u r n s
[ Object
value ] :
ID {
18
i f ( $ID . t e x t . equals ( " o b j e c t " )
| |
$ID . t e x t . equals ( " conj " )
19
| |
$ID . t e x t . equals ( " l e f t " )
| |
$ID . t e x t . equals ( " seq " )
20
| |
$ID . t e x t . equals ( " count " ) ) {
21
$value = $ID . t e x t ;
22 }
23 };
24


144
25 number
r e t u r n s
[ Object
value ] : NUMBER {
26
$value = $NUMBER. t e x t ;
27 };
28
29 from : FROM source ;
30
31 source :
ID {
32 symbolTable . put ( " source " , $ID . t e x t ) ;
33 };
34
35 where : WHERE o b j e c t A n d A t t r i b u t e
(AND o b j e c t A n d A t t r i b u t e )*
36
(AND s p a t i a l R e l a t i o n ) * ;
37
38 o b j e c t A n d A t t r i b u t e : OBJECT BRACK_OPEN number BRACK_CLOSE
39 DOT attributeName EQ a t t r i b u t e V a l u e
{
40
i f ( $attributeName . t e x t . equals ( " l a b e l " )
41
| |
$attributeName . t e x t . equals ( " c o l o r " ) ) {
42
symbolTable . put ($OBJECT . t e x t +"."+ $number . value +
43 " . " + $attributeName . value ,
$ a t t r i b u t e V a l u e . value ) ;
44
45
Boolean
hasObject =
f a l s e ;
46
i f ( o b j e c t L i s t . s i z e () >0){
47
f o r
( i n t
i = 0;
i < o b j e c t L i s t . s i z e ( ) ;
i ++) {
48
i f ( o b j e c t L i s t . get ( i ) . getNumber ( ) . equals
49
( S t r i n g . valueOf ( $number . t e x t ) ) ) {
50
hasObject = t r u e ;
51
52
i f ( $attributeName . t e x t . equals ( " l a b e l " ) ) {
53
o b j e c t L i s t . get ( i ) . s e t L a b e l ( S t r i n g . valueOf
54
( $ a t t r i b u t e V a l u e . t e x t ) ) ;
55
}
56
i f ( $attributeName . t e x t . equals ( " c o l o r " ) ) {


145
57
o b j e c t L i s t . get ( i ) . s e t C o l o r ( S t r i n g . valueOf
58
( $ a t t r i b u t e V a l u e . t e x t ) ) ;
59
}
60
i f ( $attributeName . t e x t . equals ( " c o l o r " ) ) {
61
o b j e c t L i s t . get ( i ) . s e t C o l o r ( S t r i n g . valueOf
62
( $ a t t r i b u t e V a l u e . t e x t ) ) ;
63
}
64
}
65
}
66
}
67
i f ( hasObject == f a l s e ){
68
ObjectQuery
obj = new ObjectQuery ( ) ;
69
obj . setNumber ( S t r i n g . valueOf ( $number . t e x t ) ) ;
70
71
i f ( $attributeName . t e x t . equals ( " l a b e l " ) ) {
72
obj . s e t L a b e l ( S t r i n g . valueOf ( $ a t t r i b u t e V a l u e . t e x t ) ) ;
73
}
74
i f ( $attributeName . t e x t . equals ( " c o l o r " ) ) {
75
obj . s e t C o l o r ( S t r i n g . valueOf ( $ a t t r i b u t e V a l u e . t e x t ) ) ;
76
}
77
o b j e c t L i s t . add ( obj ) ;
78
}
79 }
80 };
81
82 s p a t i a l R e l a t i o n : PAR_OPEN f i r s t S p a t i a l O p e r a n d
s p a t i a l O p e r a t o r
83
secondSpatialOperand PAR_CLOSE;
84
85 f i r s t S p a t i a l O p e r a n d
r e t u r n s
[ Object
value ] : OBJECT
86 BRACK_OPEN number BRACK_CLOSE {
87 symbolTable . put ( " f i r s t O p e r a n d " ,
$number . value ) ;
88 };


146
89
90 secondSpatialOperand
r e t u r n s
[ Object
value ] : OBJECT
91 BRACK_OPEN number BRACK_CLOSE {
92 symbolTable . put ( " secondOperand " ,
$number . value ) ;
93
S p a t i a l O p e r a t o r
sp = new S p a t i a l O p e r a t o r ( ) ;
94 sp . s e t F i r s t O p e r a n d ( S t r i n g . valueOf (
95
symbolTable . get ( " f i r s t O p e r a n d " ) ) ) ;
96 sp . s e t O p e r a t o r ( S t r i n g . valueOf (
97
symbolTable . get ( " s p a t i a l O p e r a t o r " ) ) ) ;
98 sp . setSecondOperand ( S t r i n g . valueOf (
99
symbolTable . get ( " secondOperand " ) ) ) ;
100
s p a t i a l O p e r a t o r s L i s t . add ( sp ) ;
101 };
102
103 s p a t i a l O p e r a t o r :
(LEFT)*
(BELOW)* {
104
i f ( $LEFT . t e x t
!=
n u l l ){
105
symbolTable . put ( " s p a t i a l O p e r a t o r " ,
106
S t r i n g . valueOf ( $LEFT . t e x t ) ) ;
107 }
108
i f ($BELOW. t e x t
!=
n u l l ){
109
symbolTable . put ( " s p a t i a l O p e r a t o r " ,
110
S t r i n g . valueOf ($BELOW. t e x t ) ) ;
111 }
112 };
113
114 a t t r i b u t e V a l u e
r e t u r n s
[ Object
value ] :
ID {
115
$value = $ID . t e x t ;
116 };
117
118 attributeName
r e t u r n s
[ Object
value ] :
ID {
119
$value = $ID . t e x t ;
120 };


147
121
122 count : COUNT PAR_OPEN (OBJECT)*
(OBJECT DOT attributeName
123 EQ a t t r i b u t e V a l u e )* PAR_CLOSE (GREATEREQUAL)*
(GREATER)*
124 (EQUAL)*
number FOREACHFRAME {
125
i f ( $attributeName . t e x t
!=
n u l l ){
126
jsonCountOperator . put ( " attributeName " ,
127
S t r i n g . valueOf ( $attributeName . t e x t ) ) ;
128 }
129
i f ( $ a t t r i b u t e V a l u e . t e x t
!=
n u l l ){
130
jsonCountOperator . put ( " a t t r i b u t e V a l u e " ,
131
S t r i n g . valueOf ( $ a t t r i b u t e V a l u e . t e x t ) ) ;
132 }
133
i f ($GREATEREQUAL !=
n u l l ){
134
jsonCountOperator . put ( " countOperator " ,
135
S t r i n g . valueOf ($GREATEREQUAL. t e x t ) ) ;
136 }
137
i f ($GREATER !=
n u l l ){
138
jsonCountOperator . put ( " countOperator " ,
139
S t r i n g . valueOf ($GREATER. t e x t ) ) ;
140 }
141
i f ($EQUAL !=
n u l l ){
142
jsonCountOperator . put ( " countOperator " ,
143
S t r i n g . valueOf ($EQUAL. t e x t ) ) ;
144 }
145
jsonCountOperator . put ( " countValue " ,
146
S t r i n g . valueOf ( $number . t e x t ) ) ;
147 };
148
149window : WINDOW EQ number {
150 symbolTable . put ( " window " ,
$number . t e x t ) ;
151 };


