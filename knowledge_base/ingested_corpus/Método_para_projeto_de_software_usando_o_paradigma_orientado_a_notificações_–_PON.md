# Método para projeto de software usando o paradigma orientado a notificações – PON.pdf

UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ 
PROGRAMA DE PÓS-GRADUAÇÃO EM ENGENHARIA ELÉTRICA  
E INFORMÁTICA INDUSTRIAL 
 
 
 
 
 
 
LUCIANA VILAS BOAS WIECHETECK 
 
 
 
 
 
 
 
MÉTODO PARA PROJETO DE SOFTWARE USANDO O PARADIGMA 
ORIENTADO A NOTIFICAÇÕES – PON 
 
 
 
 
 
DISSERTAÇÃO  
 
 
 
 
 
 
CURITIBA 
2011


 


LUCIANA VILAS BOAS WIECHETECK 
 
 
 
 
 
 
 
 
 
MÉTODO PARA PROJETO DE SOFTWARE USANDO O PARADIGMA 
ORIENTADO A NOTIFICAÇÕES – PON 
 
 
 
 
Dissertação apresentada ao Programa de Pós-
Graduação em Engenharia Elétrica e Informática 
Industrial da Universidade Tecnológica Federal do 
Paraná, como requisito parcial para obtenção do grau 
de “Mestre em Ciências” – Área de Concentração: 
Engenharia de Automação e Sistemas. 
 
Orientador: Prof. Dr. Paulo Cézar Stadzisz 
Co-Orientador: Prof. Dr. Jean Marcelo Simão 
 
 
 
 
 
 
 
CURITIBA 
2011


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Dados Internacionais de Catalogação na Publicação 
 
W642      Wiecheteck, Luciana Vilas Boas 
                     Método  para  projeto  de  software  usando  o  paradigma  orientado  a  notificações – PON /  
                Luciana Vilas Boas Wiecheteck .— 2011. 
                     196 p. : il. ; 30 cm 
 
Orientadora: Paulo Cézar Stadzisz. 
Coorientador: Jean Marcelo Simão. 
Dissertação (Mestrado) – Universidade Tecnológica Federal do Paraná. Programa de Pós-
graduação em Engenharia Elétrica e Informática Industrial.  Curitiba, 2011. 
Bibliografia: p. 183-188. 
 
1. Arquitetura de computador. 2. UML (Linguagem de modelagem padrão). 3. Paradigma 
orientado a notificações. 4. Software – Desenvolvimento. 5. Simulação (Computadores). 6. 
Engenharia elétrica – Dissertações. I. Stadzisz, Paulo Cézar, orient. II. Simão, Jean Marcelo, 
coorient. III. Universidade Tecnológica Federal do Paraná. Programa de Pós-graduação em 
Engenharia Elétrica e Informática Industrial. IV. Título. 
 
CDD (22. ed.) 621.3 
Biblioteca Central da UTFPR, Campus Curitiba 




 
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Dedico esta dissertação aos meus queridos pais, Gilberto 
e Cristina, fontes de amor e força, aos meus irmãos, 
Rafael e Flávia, companheiros eternos, e ao meu marido, 
Bruno, luz e inspiração da minha vida. 




AGRADECIMENTOS 
 
 
 
À Universidade Tecnológica Federal do Paraná – UTFPR, pelo suporte e infra-estrutura 
disponibilizada. 
Ao professor Paulo Cezar Stadzisz, pela orientação, conhecimentos e experiências 
transmitidos ao longo destes anos, apoio este que tornou possível a conclusão deste trabalho. 
Ao professor Jean Simão, pela co-orientação, fornecendo auxílio, conhecimento e prontidão 
que muito me auxiliaram no decorrer desta caminhada.  
Aos colegas da UTFPR que muito me ajudaram compartilhando conhecimento e experiências.  
Aos meus pais Gilberto e Maria Cristina, que desde os primórdios da minha vida me 
proporcionaram amor, ética e força. Agradeço a vocês por todo voto de confiança que sempre 
me deram e me dão, força esta que me impulsiona para a vida e me faz acreditar em meus 
sonhos.  
Aos meus irmãos, Rafael e Flávia, fontes sublimes de amor e companheirismo em minha 
vida. 
Ao meu marido Bruno, homem este que doou muitas horas de sua vida me apoiando e 
aconselhando, a fim de que hoje eu pudesse ganhar o título de mestre. A este homem 
maravilhoso o meu muito obrigada por me ajudar nas dificuldades, por me dar forças para 
superar os obstáculos, por entender minha ausência por muitas vezes e, por fim, por celebrar e 
vibrar por toda e qualquer vitória na minha vida.  
Aos amigos e familiares pela força durante todo este processo. 
À amiga e colega de mestrado, Ana Maria, com a qual foi possível compartilhar todos esses 
anos de estudos, desafios e vitórias. 
A Deus, que me deu força em todos os momentos dessa caminhada e me ensinou que, ao eu 
acreditar Nele, eu estaria acreditando em mim.  
 
 
 
 


 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Para obter algo que você nunca teve, precisa fazer algo que você nunca fez. 
 
(Chico Xavier)




RESUMO 
 
 
WIECHETECK, Luciana V. B. Método para Projeto de Software usando o Paradigma 
Orientado a Notificações – PON. 2011. 196 f. Dissertação.  Programa de Pós-Graduação em 
Engenharia Elétrica e Informática Industrial (CPGEI), Universidade Tecnológica Federal do 
Paraná (UTFPR), 2011. 
 
Esta pesquisa propõe um método para projetos de software que empregam o Paradigma 
Orientado a Notificações (PON) no seu desenvolvimento. O PON tem sido materializado em 
termos de programação, mas não possuía ainda um método formalizado para orientar os 
desenvolvedores na elaboração de projetos de software. O método proposto, denominado 
Desenvolvimento Orientado a Notificações (DON), foi desenvolvido a partir de duas etapas: 
(1) a criação de um perfil UML denominado Perfil PON, que define os principais conceitos 
do PON por meio da utilização de mecanismos de extensão da UML; e (2) a criação do 
método DON, propriamente dito, que faz uso do Perfil PON e apresenta uma sequência de 
passos para a construção de projetos neste novo paradigma. O método DON foi aplicado em 
um caso de estudo que envolve a modelagem de um Simulador de Portão Eletrônico, sendo 
que os resultados desta pesquisa demonstram que o método criado possui grande valia na 
definição de programas em PON. 
 
Palavras-chave: Modelagem de Software. Unified Modeling Language (UML). Perfil UML. 
Paradigma Orientado a Notificações (PON) 
 
 




ABSTRACT 
 
 
WIECHETECK, Luciana V. B. Method for software modeling using the Notification 
Oriented Paradigm – NOP. 2011. 196 f. Dissertação.  Programa de Pós-Graduação em 
Engenharia Elétrica e Informática Industrial (CPGEI), Universidade Tecnológica Federal do 
Paraná (UTFPR), 2011. 
 
This research proposes a method for software modeling that uses the Notification Oriented 
Paradigm (NOP). NOP has already been consolidated in terms of programming but did not 
possess a formalized method for software design. The proposed method is called Notification 
Oriented Design (NOD) and was developed in two steps: (1) the creation of a UML profile, 
called NOP Profile, which defines the main concepts of NOP by means of extension 
mechanisms usage; and (2) the development of DON itself, which uses NOP Profile and 
defines a step sequence to design projects in this new paradigm. The NOD method was 
applied in a study case that involves the modeling of an electronic gate simulator. The results 
showed that the proposed UML profile has an important value in the modeling of NOP 
programs and can be used in software design processes that use this new programming 
paradigm. 
 
Keywords: Software Modeling. Unified Modeling Language (UML). UML Profile. 
Notification Oriented Paradigm (NOP) 
 
 
 
 




LISTA DE FIGURAS 
 
 
Figura 1 - Arquitetura Interna de um SBR (adaptado de FRIEDMAN-HILL, 2003). ............. 28 
Figura 2 - Relação entre PON e os outros paradigmas (adaptado de Banaszewski, 2009) ...... 31 
Figura 3 - Metodologia do Trabalho......................................................................................... 34 
Figura 4 - Cadeia de notificações entre as entidades colaboradoras do PON (adaptado de 
Banaszewski et. al., 2007) ........................................................................................................ 40 
Figura 5 - Exemplo de uma Rule em PON ............................................................................... 41 
Figura 6 - Inferência por Notificações ...................................................................................... 42 
Figura 7 - Estrutura do framework do PON ............................................................................. 44 
Figura 8 - Representação dos objetos FBE em um sistema de portão eletrônico ..................... 45 
Figura 9 - Diagrama de classes Core - Estrutura de um objeto FBE ........................................ 46 
Figura 10 - Representação de uma Regra em PON .................................................................. 48 
Figura 11 - Diagrama de classes Core - Estrutura de um objeto Rule ...................................... 50 
Figura 12 - Diagrama de Classes – Pacote Application ........................................................... 51 
Figura 13 - Exemplo da estrutura FBE (adaptado de Banaszewski (2009)) ............................ 53 
Figura 14 - Inicialização dos FBEs e Rules em C++ ................................................................ 54 
Figura 15 - Diagrama de classes Core - Particularidades ......................................................... 55 
Figura 16 - Premise Exclusive em C++ (BANASZEWSKI,2009)........................................... 57 
Figura 17 - Exemplo de uma expressão causal complexa em C++ .......................................... 57 
Figura 18 - Representação de uma expressão causal  complexa com subcondições ................ 58 
Figura 19 - Código exemplo da RuleDerived em C++ ............................................................. 59 
Figura 20 - Diagrama de Sequência - interação entre os Holons ............................................. 59 
Figura 21 - RUP – Processo iterativo e incremental ................................................................ 60 
Figura 22 - Arquitetura do RUP ............................................................................................... 61 
Figura 23 - Trabalhadores, atividades e artefato ...................................................................... 63 
Figura 24 - Fluxo de Trabalho da Disciplina de Requisitos ..................................................... 64 
Figura 25 - Arquitetura OMG em quatro camadas ................................................................... 66 
Figura 26 - Arquitetura MOF de Metadados (OMG,2002) ...................................................... 68 
Figura 27 - Classificação dos Diagramas da UML (OMG, 2007) ........................................... 69 
Figura 28 - Interfaces Fornecida e Requerida (adaptado de LIMA, 2008) .............................. 70 
Figura 29 - Contextualização Perfil UML (Adaptado de ABDULLAH, 2006) ....................... 71 
Figura 30 - Exemplo de estereótipo no metamodelo ................................................................ 73 
Figura 31 - Exemplo de valor etiquetado no metamodelo........................................................ 73 
Figura 32 - Exemplo de Topologia em Estrela ......................................................................... 75 
Figura 33 - Exemplo de Metamodelo do Domínio (Passo 1) ................................................... 76 
Figura 34 - Exemplo da Definição dos Estereótipos (Passo2) ................................................. 76 
Figura 35 - Exemplo da Definição das Metaclasses (Passo 3) ................................................. 77 
Figura 36 - Exemplo da Definição de Valor Etiquetado .......................................................... 78 
Figura 37 - Exemplo de Rede de Petri ...................................................................................... 80 
Figura 38 - Exemplo de rede de Petri Ordinária (CARDOSO e VALETTE, 1997) ................ 81 
Figura 39 - Redes de Petri de um Controle (SIMÃO, 2005) .................................................... 86 
Figura 40 - Etapas para a Construção do Método para Projetos em PON................................ 89 
Figura 41 - Arquitetura MOF de quatro camadas..................................................................... 90 
Figura 42 - Modelo do Domínio do PON ................................................................................. 91 
Figura 43 - Modelo do domínio - pacote Core ......................................................................... 93 
Figura 44 - Modelo do domínio - pacote Application .............................................................. 94 
Figura 45 - Relação de importação o metamodelo da UML e o Perfil PON ............................ 95 
Figura 46 - Composição do NOP Profile ................................................................................. 95 


 
 
Figura 47 - NOP Profile – Core-Class ..................................................................................... 99 
Figura 48 - NOP Profile – Core-Object ................................................................................. 101 
Figura 49 - NOP Profile – Core-Component.......................................................................... 104 
Figura 50 - NOP Profile – Core-Association ......................................................................... 115 
Figura 51 - NOP Profile - Application ................................................................................... 120 
Figura 52 - DON contextualizado no RUP ............................................................................. 126 
Figura 53 - Método DON – Ciclo 1 ........................................................................................ 127 
Figura 54 - Método DON – Ciclo 2 ........................................................................................ 128 
Figura 55 - Método DON – Ciclo 3 ........................................................................................ 129 
Figura 56 - Modelo de Caso de Uso ....................................................................................... 131 
Figura 57 - Modelo de Classes ............................................................................................... 132 
Figura 58 - Modelo de Estados de Alto Nível ........................................................................ 133 
Figura 59 - Modelo de Componentes - Abrir Portão (Passo 1) .............................................. 135 
Figura 60 - Modelo de Componentes - Abrir Portão (Passo 2) – Representação das premissas 
e instigações como interfaces ................................................................................................. 137 
Figura 61 - Modelo de Componentes - Abrir Portão (Passo 2) – Representação das premissas 
e instigações como componentes ............................................................................................ 138 
Figura 62 - Modelo de Componentes - Abrir Portão (Passo 3) .............................................. 139 
Figura 63 - Modelo de Componentes - Abrir Portão (Passo 3 Completo) ............................. 141 
Figura 64 - Mapeamento Modelo de Componentes para Modelo de Sequência .................... 142 
Figura 65 - Modelo de Objetos - Abrir Portão ....................................................................... 143 
Figura 66 - Modelo de Sequência – Inicialização .................................................................. 145 
Figura 67 - Modelo de Sequência – Abrir Portão ................................................................... 147 
Figura 68 - Modelo de Comunicação - Abrir Portão .............................................................. 149 
Figura 69 - Modelo de Rede de Petri - Abrir Portão .............................................................. 152 
Figura 70 - Modelo de Rede de Petri - Abrir Portão - Resumido ........................................... 153 
Figura 71 - Caso de Estudo - Modelo de Casos de Uso ......................................................... 159 
Figura 72 - Caso de Estudo - Modelo de Classes ................................................................... 160 
Figura 73 - Caso de Estudo - Modelo de Estados de Alto Nível ............................................ 160 
Figura 74 - Case de Estudo - Abrir Portão - Modelo de Componentes .................................. 165 
Figura 75 - Case de Estudo - Fechar Portão - Modelo de Componentes ............................... 167 
Figura 76 - Case de Estudo - Parar Portão - Modelo de Componentes .................................. 168 
Figura 77 - Case de Estudo - Inicialização - Modelo de Sequência – Parte 1 ........................ 170 
Figura 78 - Case de Estudo - Inicialização - Modelo de Sequência – Parte 2 ........................ 171 
Figura 79 - Case de Estudo - Abrir Portão - Modelo de Sequência ....................................... 172 
Figura 80 - Case de Estudo - Fechar Portão - Modelo de Sequência ..................................... 173 
Figura 81 - Case de Estudo - Parar Portão (Parar de Abrir) - Modelo de Sequência ............. 174 
Figura 82 - Case de Estudo - Parar Portão (Parar de Fechar) - Modelo de Sequência ........... 175 
Figura 83 - Caso de Estudo - Modelo de Redes de Petri ........................................................ 177 


LISTA DE TABELAS 
 
 
Tabela 1 - Enumerações do NOP Profile - Core .................................................................... 101 
Tabela 2 - Valores etiquetados do NOP Profile - Core .......................................................... 102 
Tabela 3 - Estereótipo NOP_FBE .......................................................................................... 104 
Tabela 4- Estereótipo NOP_Rule ........................................................................................... 105 
Tabela 5 - Estereótipo NOP_Attribute ................................................................................... 106 
Tabela 6 - Estereótipo NOP_Premise ..................................................................................... 107 
Tabela 7 - Estereótipo NOP_Condition .................................................................................. 108 
Tabela 8 - Estereótipo NOP_SubCondition ............................................................................ 109 
Tabela 9 - Estereótipo NOP_Action ....................................................................................... 109 
Tabela 10 - Estereótipo NOP_Instigation .............................................................................. 110 
Tabela 11 - Estereótipo NOP_Method ................................................................................... 111 
Tabela 12 - Estereótipo NOP_MethodPointer........................................................................ 112 
Tabela 13 - Estereótipo NOP_MethodDerived ....................................................................... 113 
Tabela 14 - Estereótipo AttributeNotifiesPremise .................................................................. 115 
Tabela 15 - Estereótipo PremiseNotifiesCondition ................................................................ 116 
Tabela 16 - Estereótipo ConditionNotifiesRule ...................................................................... 116 
Tabela 17 - Estereótipo RuleNotifiesAction............................................................................ 116 
Tabela 18 - Estereótipo ActionNotifiesInstigation ................................................................. 117 
Tabela 19 - Estereótipo InstigationNotifiesMethod ................................................................ 117 
Tabela 20 - Estereótipo InstigationNotifiesAttribute .............................................................. 118 
Tabela 21 - Estereótipo MethodNotifiesAttribute ................................................................... 118 
Tabela 22 - Estereótipo PremiseNotifiesSubCondition .......................................................... 118 
Tabela 23 - Estereótipo SubConditionNotifiesCondition ....................................................... 119 
Tabela 24 - Enumeração do NOP Profile - Application ......................................................... 120 
Tabela 25 - Valor Etiquetado do NOP Profile - Application ................................................. 121 
Tabela 26 - Estereótipo NOP_Application ............................................................................. 121 
Tabela 27 - Estereótipo initFactBase ..................................................................................... 122 
Tabela 28 - Estereótipo initRules ........................................................................................... 122 
Tabela 29 - Estereótipo codeApplication................................................................................ 122 
Tabela 30 - initSharedPremises .............................................................................................. 123 
Tabela 31 - Estereótipo configureStartApplicationAction...................................................... 123 
Tabela 32 - Modelo de Componentes – Tabela das Regras ................................................... 136 
Tabela 33 - Caso de Estudo - Tabela das Regras ................................................................... 163 
 
 
 
 
 
 


 
 


 
 
 
 
LISTA DE ABREVIATURAS, SIGLAS E ACRÔNIMOS 
 
 
CASE  
Computer-Aided Software Engineering  
CH 
 
Controle Holônico 
DON  
Desenvolvimento Orientado a Notificações 
EA 
 
Enterprise Architecture 
FBE 
 
Fact Base Element 
IDL 
 
Interface Definition Language 
MOF   
Meta-Object Facility 
OCL  
Object Constraint Language 
OMG  
Object Management Group 
OMT  
Object Modeling Technique 
OOSE  
Object-Oriented software Engineering 
PON  
Paradigma Orientado a Notificações 
POO  
Paradigma de Orientação a Objetos 
PF 
 
Paradigma Funcional 
PL 
 
Paradigma Lógico 
PP 
 
Paradigma Procedimental 
PRR 
 
Production Rule Representation 
RUP  
Rational Unified Process 
SBR 
 
Sistema Baseado em Regra 
SMH  
Sistema de Manufatura Holônico 
SPE 
 
Simulador de Portão Eletrônico 
SPEM  
Software Process Engineering Metamodel 
UML  
Unified Modeling Language 
URML  
UML-Based Rule Modeling Language 
 
 


 
 
 


 
 
 
 
SUMÁRIO 
 
 
1 INTRODUÇÃO ................................................................................................................... 25 
1.1 CONTEXTO DO TRABALHO DE PESQUISA ............................................................... 25 
1.1.1 Engenharia de Software ................................................................................................... 25 
1.1.2 Paradigmas de Programação ............................................................................................ 27 
1.2 MOTIVAÇÃO .................................................................................................................... 31 
1.3 OBJETIVOS ....................................................................................................................... 32 
1.4 METODOLOGIA ............................................................................................................... 33 
1.5 ORGANIZAÇÃO DO TRABALHO ................................................................................. 35 
2 FUNDAMENTAÇÃO TEÓRICA ...................................................................................... 37 
2.1 PARADIGMA ORIENTADO A NOTIFICAÇÕES .......................................................... 37 
2.1.1 Visão Geral ...................................................................................................................... 37 
2.1.2 Mecanismo de Notificações ............................................................................................ 39 
2.1.3 Framework do PON ........................................................................................................ 43 
2.1.3.1 Pacote Core .................................................................................................................. 44 
2.1.3.1.1 Estrutura classe FBE .................................................................................................. 44 
2.1.3.1.2 Estrutura da classe Rule ............................................................................................. 48 
2.1.3.2 Pacote Application ........................................................................................................ 51 
2.1.3.3 Particularidades ............................................................................................................ 55 
2.1.4 Modelagem em PON ....................................................................................................... 59 
2.2 PROCESSO UNIFICADO DA RATIONAL (RUP) ......................................................... 60 
2.2.1 Visão geral ....................................................................................................................... 60 
2.2.2 Estrutura Dinâmica: Desenvolvimento Iterativo ............................................................. 62 
2.2.3 Estrutura Estática: Descrição do Processo....................................................................... 62 
2.3 LINGUAGEM E PERFIL UML ........................................................................................ 65 
2.3.1 Contextualização ............................................................................................................. 66 
2.3.2 Linguagem UML ............................................................................................................. 68 
2.3.2.1 Porta e Interface ............................................................................................................ 70 
2.3.3 Perfil UML ...................................................................................................................... 71 
2.3.3.1 Elaboração de Perfis UML ........................................................................................... 74 
2.4 REDES DE PETRI ............................................................................................................. 78 
2.4.1 Aspectos Gerais ............................................................................................................... 79 
2.4.2 Tipos de Redes de Petri ................................................................................................... 81 
2.4.3 Redes de Petri e sistemas de regras ................................................................................. 84 
2.4.4 Redes de Petri e o PON ................................................................................................... 85 


 
 
2.5 CONSIDERAÇÕES SOBRE A FUNDAMENTAÇÃO TEÓRICA ................................. 86 
3 VISÃO GERAL DO MÉTODO PROPOSTO E PERFIL UML PARA O PON ........... 89 
3.1 VISÃO GERAL DO MÉTODO PROPOSTO ................................................................... 89 
3.2 PERFIL UML PARA O PON ............................................................................................ 90 
3.2.1 Descrição do Modelo do Domínio................................................................................... 91 
3.2.2 NOP Profile (Perfil PON)................................................................................................ 94 
3.2.2.1 NOP Profile - Core ....................................................................................................... 97 
3.2.2.1.1 Pacote Core Elements ................................................................................................ 97 
3.2.2.1.1.1 Pacote Core Elements - Representação Gráfica ..................................................... 99 
3.2.2.1.1.2 Pacote Core Elements - Representação Tabular ................................................... 104 
3.2.2.1.2 Pacote Core Relationships ....................................................................................... 114 
3.2.2.1.2.1 Pacote Core Relationships - Representação Gráfica ............................................ 114 
3.2.2.1.2.2 Pacote Core Relationships - Representação Tabular ............................................ 115 
3.2.2.2 NOP Profile - Application .......................................................................................... 119 
3.2.2.2.1 NOP Profile Application - Representação Gráfica .................................................. 119 
3.2.2.2.2 NOP Profile Application - Representação Tabular ................................................. 121 
3.3 CONSIDERAÇÕES SOBRE O NOP PROFILE ............................................................. 123 
4 DESCRIÇÃO DO MÉTODO PROPOSTO .................................................................... 125 
4.1 DESENVOLVIMENTO ORIENTADO A NOTIFICAÇÕES (DON) ............................ 125 
4.1.1 Capturar Requisitos ....................................................................................................... 129 
4.1.2 Criar Modelo de Casos de Uso ...................................................................................... 130 
4.1.3 Criar Modelo de Classes ................................................................................................ 131 
4.1.4 Criar Modelo de Estados de Alto Nível......................................................................... 132 
4.1.5 Criar Modelo de Componentes ...................................................................................... 134 
4.1.6 Criar Modelo de Sequência ........................................................................................... 142 
4.1.7 Criar Modelo de Comunicação ...................................................................................... 148 
4.1.8 Criar Modelo de Redes de Petri ..................................................................................... 150 
4.2 VERIFICAÇÃO E VALIDAÇÃO ................................................................................... 154 
4.3 CONSIDERAÇÕES SOBRE O DON .............................................................................. 155 
5 CASO DE ESTUDO .......................................................................................................... 157 
5.1 VISÃO GERAL ................................................................................................................ 157 
5.2 REQUISITOS ................................................................................................................... 157 
5.3 MODELO DE CASOS DE USO ..................................................................................... 158 
5.4 MODELO DE CLASSES ................................................................................................. 159 
5.5 MODELO DE ESTADOS DE ALTO NÍVEL ................................................................. 160 
5.6 MODELOS DE COMPONENTES .................................................................................. 163 
5.7 MODELOS DE SEQUÊNCIA ......................................................................................... 169 


 
 
 
 
5.8 MODELO DE REDES DE PETRI ................................................................................... 176 
5.9 CONSIDERAÇÕES SOBRE O CASO DE ESTUDO .................................................... 177 
6 CONCLUSÕES .................................................................................................................. 179 
6.1 CONTRIBUIÇÕES .......................................................................................................... 180 
6.2 DIFICULDADES E LIMITAÇÕES ................................................................................ 181 
6.3 TRABALHOS FUTUROS ............................................................................................... 181 
REFERÊNCIAS ................................................................................................................... 183 
APÊNDICE - CÓDIGO FONTE DO SIMULADOR DE PORTÃO ELETRÔNICO 
(SPE) ...................................................................................................................................... 189 
  
 
 
 
 
 
 
 
 
 
 
 
 


 
 


25 
 
 
 
1. INTRODUÇÃO 
 
 
Essa dissertação de mestrado propõe um método para projeto de software que utiliza 
o Paradigma Orientado a Notificações – PON. De forma sucinta, o PON foi criado a partir de 
um metamodelo genérico para controle discreto aplicado à simulação de sistemas de 
manufatura inteligentes (SIMÃO, 2001, 2005), sendo proposto, posteriormente, como um 
novo paradigma de programação (SIMÃO e STADZISZ, 2008). 
Neste capítulo, a seção 1.1 apresenta o contexto, as motivações e os objetivos do 
presente trabalho. A seção 1.2, por sua vez, resume os fatores motivadores do tema em 
questão. A seção 1.3 detalha os objetivos pretendidos com a realização deste trabalho. A 
seção 1.4, ainda, descreve a metodologia utilizada no desenvolvimento deste trabalho. A 
seção 1.5, por fim, apresenta a organização dos capítulos que compõem esta dissertação de 
mestrado. 
 
1.1. 
CONTEXTO DO TRABALHO DE PESQUISA 
 
Particularmente, esta presente seção se divide em subseção 1.1.1  e subseção 1.1.2. A 
subseção 1.1.1  introduz os conceitos de engenharia de software e a subseção 1.1.2 apresenta 
os conceitos de paradigmas de programação e a contextualização do PON nesse panorama. 
 
1.1.1. Engenharia de Software 
 
A engenharia de software é a área de conhecimento da computação responsável por 
oferecer meios para a elaboração de projetos de sistemas computacionais (PRESSMAN, 
1995). No desenvolvimento de software, o engenheiro se envolve em uma sequência de 
atividades que produzem uma variedade de documentos (ou seja, artefatos de projeto), 
supostamente resultando em um programa satisfatório e executável. Segundo Pressman 
(1995), a engenharia de software é constituída basicamente por três elementos fundamentais: 
métodos, ferramentas e procedimentos.  
Os métodos oferecem os detalhes de “como fazer” para construir o software. Os 
métodos envolvem um amplo conjunto de tarefas como planejamento e estimativa de projeto, 
análise de requisitos, projeto da estrutura de dados, arquitetura de programa e algoritmo de 
processamento, codificação, teste e manutenção. Os métodos de engenharia de software 


26 
 
muitas vezes introduzem uma notação gráfica ou orientada à linguagem especial e introduzem 
um conjunto de critérios para a qualidade de software. 
Por sua vez, as ferramentas têm o objetivo de fornecer apoio automatizado ou semi-
automatizado aos métodos por meio de programas de suporte ao desenvolvimento. Dentre 
essas, existem os sistemas chamados Engenharia de Software Auxiliada por Computador 
(CASE – Computer-Aided Software Engineering), que combinam software, hardware e banco 
de dados para criar um ambiente de suporte à engenharia de software. 
Finalmente, os procedimentos (ou metodologia) constituem o elo entre os métodos e 
as ferramentas, possibilitando o desenvolvimento de software. Eles definem a sequência em 
que os métodos serão aplicados, os produtos a serem entregues (por exemplo, documentos e 
relatórios), os controles que ajudam a assegurar a qualidade e a coordenar mudanças, e os 
pontos de referência que auxiliam na avaliação do desenvolvimento do software.  
A engenharia de software compreende um conjunto de etapas que envolve métodos, 
ferramentas e procedimentos. Uma sequência dessas etapas com feedbacks que resultam na 
produção e na evolução de um software é chamada de Processo de Engenharia de Software. 
Uma visão tradicional do processo de software é uma sequência de atividades de 
desenvolvimento do produto. No entanto, há outros tipos de processos de software como os 
caracterizados por uma sobreposição de atividades necessárias para especificar, projetar e 
testar o retorno (feedback) dos resultados do software que está sendo elaborado (PETERS e 
PEDRYCZ, 2001). 
Entre os processos de engenharia de software atuais destaca-se o Processo Unificado 
da Rational (RUP - Rational Unified Process) (KRUCHTEN, 2003). O RUP é um processo 
proprietário de engenharia de software baseado em fases e disciplinas, que atribui tarefas e 
responsabilidades dentro de uma organização de desenvolvimento, sendo baseado em uma 
abordagem iterativa. Sua meta é garantir a produção de software de alta qualidade que atenda 
às necessidades dos usuários dentro de cronogramas e orçamentos desejáveis. Um projeto 
elaborado em RUP faz uso da orientação a objetos sendo projetado e documentado utilizando 
a notação da Linguagem de Modelagem Unificada (UML - Unified Modeling Language).  
A UML, ao seu turno, é uma linguagem de modelagem utilizada para modelar 
sistemas computacionais por meio do Paradigma de Orientação a Objetos (POO) (GUEDES, 
2004). Essa linguagem de modelagem tornou-se a linguagem padrão de software adotada 
internacionalmente pela indústria de software. A UML não é uma metodologia de 
desenvolvimento, o que significa que ela não diz o que fazer primeiro e em seguida ou como 
projetar seu sistema, mas sim auxilia a definir e visualizar os modelos do sistema a ser 


27 
 
 
 
desenvolvido. Basicamente, a UML permite que desenvolvedores expressem, representem e 
visualizem os produtos de seu trabalho em diagramas padronizados, fazendo parte dos 
métodos de engenharia de software. 
A UML fornece um conjunto rico de conceitos de modelagem e notações que foram 
desenvolvidos para satisfazer as necessidades de projetos típicos de modelagem de software. 
No entanto, há casos em que são necessárias características adicionais de modelagem além 
daquelas definidas pela UML padrão, como no caso de domínios específicos de aplicação (ex. 
tempo-real) ou implementação de certas tecnologias (ex. CORBA). Em verdade, a UML 
provê a modelagem dessas necessidades específicas por meio dos seus mecanismos de 
extensão, que permitem a adição de novos elementos de modelagem ao metamodelo da UML. 
Um conjunto desses mecanismos de extensão, agrupados dentro de um pacote UML 
estereotipado <<profile>>, formam o que é chamado de Perfil UML (OMG, 2003; FUENTES 
e VALLECILLO, 2004). 
 
1.1.2. Paradigmas de Programação 
 
Uma das partes essenciais na construção de software é o paradigma de programação 
que será adotado (KAMBAYASHI e LEDGARD, 2004). Um paradigma de programação 
fornece aos programadores um framework (ou arquétipo) conceitual coeso para ser utilizado 
no domínio de interesse e ajudar a analisar problemas desse domínio. Cada paradigma de 
programação oferece um conjunto de linguagens de programação permitindo que problemas 
possam ser expressos e executados em máquinas computacionais (PUN e KAHN, 1995).  
BANASZEWSKI (2009) explicita que, atualmente, baseado em diversos autores da 
área (WATT, 2004; SCOTT, 2000; BROOKSHEAR, 2006), existem quatro paradigmas de 
programação principais, que são: Paradigma Procedimental (PP), Paradigma Orientado a 
Objetos (POO), Paradigma Funcional (PF) e Paradigma Lógico (PL). Ainda, PP e POO 
poderiam ser classificados como um a paradigma mais genérico chamado Paradigma 
Imperativo (PI), enquanto que PF e PL poderiam ser classificados como Paradigma 
Declarativo (PD). 
O PP é baseado na organização sequencial de variáveis (simples ou compostas) e 
comandos (primitivos ou compostos). Os valores armazenados nas variáveis representam os 
estados das entidades (abstratas ou relativas ao mundo real) e os comandos agem sobre estas 
variáveis, sendo ambos (comandos e variáveis) organizados em funções e procedimentos 


28 
 
(BROOKSHEAR, 2006). A
COBOL, ALGOL, BASIC,
O POO propõe a 
de relacionamentos entre 
permitem instanciar “obje
abstraem os objetos do m
relevantes para a implem
(variáveis e mesmo constan
de linguagens que utilizam
Os paradigmas PF
mais simplificada do progr
as particularidades da imp
conhecimento sobre a reso
mais precisamente, foca na
meio de funções. Funções
argumentos para outras fu
Paradigma Funcional as lin
Por sua vez, o PL
modelo, um mecanismo de
relações causais (regras) a 
2000). Os conceitos do PL
Baseados em Regras (SBR
(Base de Regras), de uma
Máquina de Inferência pa
arquitetura dos SBRs (Figu
de um SBR. 
Figura 1 - Arquite
Alguns exemplos de linguagens baseadas n
, PASCAL e C.  
concepção de sistemas computacionais por m
entidades computacionais chamadas “class
etos” (POO e KIONG, 2008). Na verdade
mundo (real ou abstrato) apresentando some
mentação dos sistemas, por meio do agrup
ntes) e comportamentos (métodos ou funçõe
este paradigma são a SIMULA, Smalltalk, C
F e PL, por sua vez, têm como característica
amador com o computador, uma vez que pos
plementação. Esses paradigmas focam ma
olução do problema do que na implementaç
a construção de programas a partir da mani
 podem invocar outras funções ou mesmo 
nções (SCOTT, 2000). São exemplos de lin
nguagens LISP, Miranda, Haskell, Sisal, pH e
L se fundamenta no modelo relacional cau
e inferência realiza buscas por valores (fatos)
fim de provar um teorema ou atingir um da
L podem ser particularmente aplicados na co
R), que são constituídos de uma memória par
a memória para armazenar os fatos (Base 
ara inferir sobre estas duas bases. Estes co
ura 1) e são utilizados para realizar o chama
etura Interna de um SBR (adaptado de FRIEDMAN-H
o PP são FORTRAN, 
meio da composição e 
ses” que descrevem e 
, os objetos do POO 
ente as características 
pamento de atributos 
es membro). Exemplos 
C++, JAVA e C#. 
a principal a interação 
ssui meios para ocultar 
ais na organização do 
ção do mesmo. O PF, 
ipulação de dados por 
serem passadas como 
nguagens baseadas no 
e ML. 
usal. No âmbito deste 
) que satisfaçam certas 
ado objetivo (SCOTT, 
onstrução de Sistemas 
ra armazenar as regras 
de Fatos) e de uma 
omponentes formam a 
ado ciclo de inferência 
 
HILL, 2003). 


29 
 
 
 
Um ciclo de inferência consiste em três fases: 
• Matching: compara os fatos em relação às regras visando ativá-las. As regras ativadas 
são colocadas de forma desordenada em um repositório chamado Conjunto de 
Conflito. 
• Seleção: ordena as regras ativadas conforme alguma estratégia de resolução de 
conflito para formar o conjunto ordenado de regras chamado Agenda.  
• Execução: seleciona a primeira regra da Agenda e executa a sua ação. Nesta execução, 
a regra pode inserir novos elementos na Base de Fatos ou solicitar um serviço externo.  
 
A fase de matching é a que mais compromete o desempenho dos SBRs. O problema 
ocorre ainda mais enfaticamente na implementação dos SBRs que não possuem um 
mecanismo satisfatório de inferência. A ineficiência destes sistemas se deve à avaliação 
redundante entre fatos e regras, uma vez que muitos dos testes realizados em cada ciclo de 
matching apresentam os mesmos resultados dos ciclos anteriores, desperdiçando 
processamento.  
Para evitar esse problema, algumas soluções foram propostas a fim de guardar os 
estados já avaliados em ciclos anteriores. Assim, as comparações são realizadas somente das 
regras contra os estados dos elementos da base de fatos atualizados recentemente. Exemplos 
destes tipos de algoritmos são o RETE (FORGY, 1982), o TREAT (MIRANKER, 1987), o 
LEAPS (MIRANKER et. al., 1990) e o HAL (LEE e CHENG, 2002). 
BANASZEWSKI (2009) evidencia em seu trabalho que esses paradigmas de 
programação apresentados – PP, POO, PF e PL – possuem deficiências que afetam aspectos 
como: o desempenho das aplicações; a facilidade de programação (particularmente no PP e 
POO) ou a flexibilidade de programação (particularmente no PD); e a obtenção de 
“desacoplamento” (ou acoplamento mínimo) entre os módulos do software, dificultando seus 
reaproveitamentos assim como o uso de multiprocessamento. Todos esses paradigmas são 
similares ao serem baseados em buscas ou no percorrer sobre entidades passivas, que 
constituem em fatos (ex: fatos ou estados de variáveis ou de atributos de outras entidades) e 
comandos de decisão (ex: expressões causais como se-então ou regras). Nestes casos, as 
buscas afetam o desempenho das aplicações por gerar redundância de processamento e 
reduzem as possibilidades de se alcançar uma dependência mínima dos módulos por gerar um 
acoplamento implícito entre eles (SIMÃO e STADZISZ, 2008, 2009a). 


30 
 
Em relação ao requisito facilidade de programação, de certa forma, é mais difícil 
programar nos paradigmas PP e POO, uma vez que é necessário manipular diretamente os 
comandos das linguagens e organizá-los a fim de definir o fluxo de execução dos programas. 
Já o PF e o PL poupam o programador dessas particularidades de programação mas, no 
entanto, possuem em geral menos flexibilidade para acesso a hardware e para certas 
otimizações algorítmicas. Outrossim, mesmo se paradigmas podem ser combinados, como 
detalhado em Banaszewski (2009), eles não resolvem o problema ainda que possam atenuá-lo 
se bem conjugados, o que não é evidente uma vez que cada paradigma tem seu próprio modus 
operandi.  
Com o objetivo de propor uma solução para esse conjunto de deficiências dos 
paradigmas de programação atuais, foi desenvolvido o Paradigma Orientado a Notificações 
(PON). O PON foi criado a partir de um metamodelo genérico para controle discreto aplicado 
à simulação de sistemas de manufatura inteligentes, proposto por J.M Simão (SIMÃO, 2001, 
2005). Esse metamodelo foi evoluído para uma solução geral de controle discreto, além de 
uma solução geral de inferência (SIMÃO e STADZISZ, 2002, 2008; SIMAO et.al., 2003; 
SIMÃO, STADZISZ e KÜNZLE, 2003), sendo proposto, posteriormente, como um novo 
paradigma de programação (SIMÃO e STADZISZ, 2008, 2009a). 
O PON encontra inspirações no PI, tais como a flexibilidade algorítmica e a 
abstração em forma de classes/objetos da POO. O PON também aproveita conceitos próprios 
do PD, como facilidade de programação em alto nível e a representação do conhecimento em 
regras dos SBR. Assim, o PON provê a possibilidade de uso (de parte) de ambos os estilos de 
programação em seu modelo, ainda que os evolua e mesmo os revolucione (de certa maneira) 
no tocante ao processo de inferência ou cálculo lógico-causal (SIMÃO e STADZISZ, 2008, 
2009a; BANASZEWSKI, 2009). A Figura 2 ilustra a relação do PON com os paradigmas de 
programação POO e PL, mais especificamente com os SBRs.    


 
 
 
Figura 2 - Relação e
 
1.2. 
MOTIVAÇÃO 
 
O PON tem sido 
técnicas e métodos formali
de software.  Em BANAS
técnicas de Engenharia de S
Como mencionad
(ex:objetos) e dos SBRs do
POO é natural utilizar a UM
e regras do PON motivam
SBRs. Quando discorrendo
de regras Jess, Friedman-H
sistema baseado em regras
do seu domínio de aplicaçã
etapa é decidir como os fat
autor ressalta que o proces
geralmente envolve exper
subjetivo e encoraja os 
implementar a aplicação.  
Visando auxiliar 
descrito por Friedman-Hill 
de sistemas. Um exemplo
entre PON e os outros paradigmas (adaptado de Banas
materializado em termos de programação, m
izados para orientar os desenvolvedores na e
SZEWSKI (2009) é citada a necessidade do
Software para o PON envolvendo conceitos d
do anteriormente, o PON é inspirado no
o PL (ex: base de fatos e regras). Uma vez qu
ML para sua modelagem. No entanto, os con
m uma análise das abordagens de modelage
o sobre o processo de modelagem de sistemas
Hill (2003) descreve que o primeiro passo n
 é coletar o conhecimento do sistema a ser 
ão.  Com base no conhecimento do domínio
tos devem ser e como dividir as regras em m
so de design é idealizado e projetar um siste
rimentação. Além disso, o autor adiciona 
projetistas a experimentarem diferentes 
a modelagem de SBRs, que não se aprese
(2003), existem algumas abordagens de mod
o é a Representação de Regras de Produç
31 
 
szewski, 2009) 
mas não possuía ainda 
elaboração de projetos 
o desenvolvimento de 
da UML. 
s conceitos do POO 
ue o PON baseia-se no 
ceitos de base de fatos 
em existentes para os 
s que utilizam o motor 
na criação de qualquer 
desenvolvido, ou seja, 
o adquirido, a próxima 
módulos. No entanto, o 
ema baseado em regras 
que esse processo é 
abordagens para se 
enta solidificada como 
delagem para esse tipo 
ção (Production Rule 


32 
 
Representation – PRR) (OMG, 2009), que é um padrão de representação de regras de 
produção definido pela OMG. O PRR exprime os requisitos para uma representação de regra 
de produção padronizada, como os usados em motores de regras de diversos vendedores 
atualmente, e provê, basicamente, a definição de regras de produção para inferência de 
encadeamento para frente.  
Outra abordagem é a Linguagem de Modelagem Baseada em Regras - UML (UML-
Based Rule Modeling Language – URML) definida pelo REWERSE Working Group 
(REWERSE, 2011), que permite a modelagem de regras baseada em modelos de classes da 
UML. A URML suporta a modelagem de regras de derivação, regras de produção e regras de 
reação.  Nessa linguagem, uma regra é representada como um círculo que possui um 
identificador de regra, as flechas de chegada representam as condições da regra ou eventos em 
disparo, e as flechas de saída representam as conclusões das regras ou ações produzidas.  
Embora seja possível o emprego convencional da UML e processos conhecidos no 
desenvolvimento de software com o PON, e até mesmo, o emprego de abordagens existentes 
para modelagem de SBRs, as especificidades do PON motivam o uso mais particularizado de 
linguagens de modelagem e processos de software.  
A fim de se obter uma particularização das linguagens de modelagem, no caso da 
UML, é necessário utilizar seus mecanismos de extensão para a criação de um Perfil UML 
que venha expressar os conceitos do PON. Adicionalmente, esse novo perfil UML deve ser 
aplicado de maneira particular às fases que requerem a modelagem do sistema dentro de um 
processo de software como o RUP, o que acarreta na criação de um novo método de projeto 
de software a ser aplicado especificamente na construção de sistemas em PON.  
Adicionalmente à modelagem UML, os conceitos de Redes de Petri podem ser 
empregados na modelagem de software em PON. Em Simão (2005), é apresentada a 
compatibilidade entre o metamodelo para controle discreto (que originou o PON) e as redes 
de Petri. Isso é importante para a modelagem, uma vez que um sistema composto por PON 
pode ser expresso pelas Redes de Petri permitindo sua avaliação formal. 
 
1.3. 
OBJETIVOS 
 
Este trabalho de pesquisa se insere no contexto dos estudos feitos no CPGEI na área 
de Engenharia de Software e, particularmente, no tema de pesquisa do PON – Paradigma de 
Orientação a Notificações. 


33 
 
 
 
O objetivo geral do trabalho é propor um método para projetos de software que 
empregam o PON, visando orientar projetistas ou programadores durante a elaboração de 
projetos de software neste novo paradigma de programação.  
Os objetivos específicos deste trabalho de pesquisa são: 
• Propor um perfil UML, denominado NOP Profile (Perfil PON), por meio da 
especificação de mecanismos de extensão da UML, que definem os principais 
conceitos do PON, melhor adequando sua modelagem em UML.  
• Propor um conjunto de técnicas de projeto, denominado DON – Desenvolvimento 
Orientado a Notificações, para desenvolvimento de software empregando o PON, que 
se adapta a processos de software conhecidos como o RUP, e faz uso do NOP Profile. 
Este conjunto de técnicas de projeto deve propor etapas que guiem os projetistas ou 
programadores na elaboração de projetos em PON, fazendo uso de modelos UML e 
Redes de Petri. 
• Realizar estudo prático de aplicação do método DON desenvolvido. 
 
1.4. 
METODOLOGIA 
 
A metodologia utilizada no desenvolvimento deste trabalho é ilustrada pela Figura 3 
(representação análoga à Leal (2010)), sendo composta por cinco etapas: Revisão 
Bibliográfica, Revisão Sistemática, Definição da Proposta, Avaliação e Redação. 
 


34 
 
A primeira fase c
referencial teórico consist
artigos sobre o PON, além
especificamente sobre o RU
como o perfil UML. Adic
redes de Petri.  
A segunda fase, R
inicial e identificar trabal
Baseados em Regras (SBR
como regras e base de fat
(Grupo de Gerência de 
representação, utilização e 
framework do PON visan
modelagem de software. 
Na terceira fase, D
fases anteriores, os eleme
Figura 3 - Metodologia do Trabalho 
 
onsistiu em uma revisão inicial da literatura
ente. Nesta fase foram estudadas dissertaç
m de livros e artigos científicos sobre proce
UP, linguagens de projeto (UML) e seus me
cionalmente, foi estudada a modelagem de s
Revisão Sistemática, teve objetivo de ampliar 
lhos que abordassem a modelagem de sof
Rs), uma vez que o PON reaproveita conc
tos. Além disso, foram estudados artigos e 
Objetos) sobre perfil UML a fim de me
aplicabilidade. Por fim, foi realizado um estu
ndo identificar suas necessidades específica
Definição da Proposta, foi possível analisar e
ntos necessários para a criação de um mé
 
a a fim de formar um 
ções e publicações de 
esso de software, mais 
ecanismos de extensão 
software utilizando as 
a revisão bibliográfica 
oftware para Sistemas 
ceitos desses sistemas, 
documentos da OMG 
elhor entender a sua 
udo mais detalhado do 
as no que se refere à 
e definir, com base nas 
todo para projetos de 


35 
 
 
 
software que empregam o PON. Nessa fase, foram identificadas duas etapas na criação do 
método: definição de um perfil UML para o PON e definição do método para projetos em 
PON, propriamente dito, que necessita dos conceitos definidos no perfil. 
A quarta fase consistiu na criação de um caso de estudo para avaliação do método 
proposto. O caso de estudo desenvolvido é referente a um sistema que simula um portão 
eletrônico, denominado Simulador de Portão Eletrônico (SPE). Nesta fase foi modelado o 
SPE aplicando-se o método DON e, na sequência, foi realizado a sua implementação em C++. 
Por fim, na quinta fase, denominada Redação, foi realizado o trabalho de escrita de 
artigos e submissão dos mesmos, escrita do documento de dissertação e defesa do presente 
trabalho. 
 
1.5. 
ORGANIZAÇÃO DO TRABALHO 
 
O presente trabalho está organizado nos seguintes capítulos e seções. No capítulo 2 
são apresentados os conceitos fundamentais que formam a base conceitual utilizada para 
estruturar esta dissertação, que são eles: PON (Paradigma Orientado a Notificacoes), RUP 
(Rational Unified Process), UML (Unified Modeling Language), Perfil UML e Redes de 
Petri. 
O capítulo 0, por sua vez, apresenta uma visão geral dos resultados obtidos que 
envolvem duas partes: a criação do perfil UML para o PON (NOP Profile) e a construção do 
método DON (Desenvolvimento Orientado a Notificações) propriamente dito. O capítulo 0 
apresenta o perfil UML criado e o capítulo 0 apresenta o método DON desenvolvido. 
O capítulo 0 apresenta um caso de estudo que aplica o método DON proposto na 
modelagem de um software. O caso de estudo é referente à modelagem completa do sistema 
SPE e a sua implementação. 
No capítulo 6, por fim, são apresentadas as conclusões sobre o trabalho 
desenvolvido, assim como as perspectivas de possíveis trabalhos futuros. 
 
 
 


36 
 
 
 


37 
 
 
 
2. FUNDAMENTAÇÃO TEÓRICA 
 
Este capítulo apresenta os conceitos fundamentais utilizados para estruturar esta 
dissertação. Primeiramente, a seção 2.1 contextualiza o PON, apresenta seus conceitos e 
detalhes de implementação, e a seção 2.2 apresenta os conceitos do Processo Unificado da 
Rational (Rational Unified Process - RUP). A seção 2.3 apresenta conceitos relevantes da 
UML e introduz detalhadamente o conceito perfil UML. E, por fim, a seção 2.4 apresenta as 
redes de Petri e seus principais tipos existentes, além da relação entre redes de Petri e 
Sistemas Baseados em Regras.  
 
2.1. 
PARADIGMA ORIENTADO A NOTIFICAÇÕES 
 
Esta seção introduz os conceitos do Paradigma Orientado a Notificações (PON).  A 
seção 2.1.1 contextualiza o PON e apresenta uma visão geral sobre o mesmo. A seção 2.1.2 
descreve o mecanismo de notificações do PON. A seção 2.1.3 apresenta detalhes de 
implementação do PON por meio da descrição do seu framework e, por fim, a seção 2.1.4, 
descreve, muito brevemente, modelagem em PON. 
 
2.1.1. Visão Geral 
 
O Paradigma Orientado a Notificações (PON) é um novo paradigma de programação 
que foi criado a partir da dissertação de mestrado e tese de doutorado de Jean Marcelo Simão 
(SIMÃO, 2001, 2005). Simão propôs uma abordagem de controle que permite organizar as 
colaborações entre entidades de manufatura (ex: recursos ou equipamentos) com o objetivo de 
alcançar agilidade na produção. O resultado dessa proposta foi a criação de um Sistema de 
Manufatura Holônico (SMH) em que as entidades envolvidas no processo produtivo são 
modeladas como unidades ‘inteligentes’ denominadas Holons (HLs), como por exemplo, 
Resource-HLs,  Product-HLs, que possuem suas cooperações coordenadas por um Controle 
Holônico (CH). Neste âmbito, foi criado um metamodelo de CH para controle discreto 
aplicado na simulação de sistemas de manufatura inteligentes. Este metamodelo foi aplicado à 
ferramenta de projeto e simulação de sistemas de manufaturas chamada ANALYTICE II 
(SIMÃO, 2005; SIMÃO, STADZISZ e MOREL, 2006; SIMÃO, STADZISZ e TACLA, 
2009b).   


38 
 
Nesse metamodelo, as relações causais do sistema são concebidas na forma de 
regras, denominadas Rule, que decidem sobre as cooperações com base em conhecimento 
específico recebido dos Resource-HLs. O metamodelo oferece um mecanismo de inferência 
que permite compor e executar softwares de controle no dominio de sistemas de manufatura 
de maneira eficiente, sendo este fato confirmado pela implementação e análise do 
metamodelo sobre diversas perspectivas no simulador ANALYTICE II (SIMÃO, 2005; 
SIMÃO et.al., 2008). Os resultados da implementação e análise são apresentados em 
(SIMÃO, 2001, 2005; SIMÃO e STADZISZ, 2002; SIMÃO, STADZISZ e MOREL, 2006; 
SIMÃO et. al., 2008; SIMÃO, STADZISZ, TACLA, 2009b). 
Devido ao fato do metamodelo ser genérico e dos resultados terem sido motivadores, 
foi proposto um metamodelo como uma solução geral de controle discreto, além de uma 
solução geral de inferência (SIMÃO e STADZISZ, 2002, 2008; SIMÃO, STADZISZ e 
KÜNZLE, 2003). Posteriormente, o metamodelo foi proposto como um novo paradigma de 
programação recebendo o nome de Paradigma Orientado a Notificações (PON) (SIMÃO e 
STADZISZ, 2008). Outros trabalhos têm sido desenvolvidos com  o intuito de apresentar e 
discutir o PON como um paradigma de programação em ascensão, como os de Banaszewski 
et.al (2007), Banaszewski (2008, 2009), enquanto outros trabalhos ainda discutem assunto 
pertinentes ao PON como os atualmente chamado Controle Orientado a Notificações (CON) e 
Inferência Orientada a Notificações (ION) (LUCCA et. al.,  2008; SIMÃO e STADZISZ, 
2009a; SIMÃO, STADZISZ e TACLA et.al., 2009b; WEBER, 2010). 
O PON se inspira no Paradigma Orientado a Objetos (POO) e no Paradigma Lógico 
(PL), com ênfase nos conceitos dos Sistemas Baseados em Regras (SBR). O PON unifica as 
principais características e vantagens do SBR – como a representação do conhecimento na 
forma de regras – e do POO – como a flexibilidade de expressão e nível apropriado de 
abstração – propondo resolver várias de suas deficiências em aplicações de software 
monoprocessado e multiprocessado. Entre essas deficiências podem ser salientadas as 
redundâncias estruturais/temporais e o acoplamento forte entre as entidades computacionais 
(SIMÃO e STADZISZ, 2008). 
O PON atualmente está materializado na forma de um framework/wizard em C++ 
enquanto uma linguagem e compilador PON permanecem como um trabalho futuro. Muito 
embora um paradigma possa se materializar em outro (como um programa POO materializado 
em uma linguagem procedimental) e isto seja natural em paradigmas emergentes, seria mais 
confortável e apropriado um ambiente efetivamente voltado para o PON (Banaszewski, 2009). 


39 
 
 
 
As entidades básicas do PON são os “Elementos da Base de Fatos” (Fact Base 
Elements - FBE) e as “Regras” (Rules). A entidade “Elementos da Base de Fatos” representa 
os elementos de uma base de fatos, como o próprio nome diz, e a entidade “Regra” gerencia o 
conhecimento causal sobre qualquer comportamento do sistema, representando e gerenciando 
as expressões-causais desse sistema. 
No framework do PON, as entidades “Elementos da Base de Fatos” e “Regras” 
foram implementadas como classes – FBE e Rule respectivamente – e, consequentemente, são 
instanciadas como objetos que apresentam qualidades que os diferem dos objetos típicos da 
OO, uma vez que possuem características de autonomia, reação e colaboração por 
notificações (BANASZEWSKI et. al., 2007; BANASZEWSKI, 2009).  
Um objeto FBE descreve seus estados e seus serviços por meio de seus atributos e 
métodos, sendo que os mesmos detectam e reagem a mudanças em seus estados contribuindo 
para que objetos Rule sejam avaliados.  No entanto, os objetos FBE se relacionam com os 
objetos Rule de forma indireta, por intermédio de outros objetos, os objetos colaboradores 
(BANASZEWSKI et. al., 2007; BANASZEWSKI, 2009).  
Os objetos Rule com o auxílio de seus objetos colaboradores, gerenciam suas 
avaliações lógicas e decidem o momento de suas execuções. Este mecanismo gera, portanto, 
uma cadeia de notificações e permite que as avaliações lógicas se desenvolvam 
independentemente umas das outras (BANASZEWSKI et. al., 2007; BANASZEWSKI, 2009. 
A seção seguinte descreve este mecanismo de notificações. 
 
2.1.2. Mecanismo de Notificações 
 
O PON possui objetos que tratam dos elementos da base de fatos, que são 
genericamente modelados pela classe FBE (Fact Base Element), conforme modelado na 
Figura 4. Cada FBE trata de seus atributos por meio de objetos da classe Attribute e seus 
serviços por meio de objetos da classe Method. Os objetos FBE, por meio de seus Attributes e 
Methods, são passíveis de correlação causal por meio de Rules, as quais se constituem em 
elementos fundamentais do PON.  
 


40 
 
Figura 4 - Cadeia de notificaçõ
Cada Premise rep
Attribute. Uma Condition
verdadeiras, permitirão a e
executa uma Action, que po
realizar a chamada de um M
o estado de um Attribute, o 
A Figura 5 apres
representação facilita a v
colaboradores. Por exemp
Condition e um objeto Act
da execução das ações da 
conhecimento lógico e caus
ões entre as entidades colaboradoras do PON (adaptad
2007) 
 
presenta uma comparação de um Attribute a
n, então, é composta de uma ou mais P
execução da Rule. Uma Rule com todas as 
ode realizar uma ou mais Instigations. Cada 
Method, que realizará algum tipo de processa
que fecha o ciclo de notificação das inferênc
senta um exemplo de Rule na forma de um
visualização de que cada Rule é compos
plo, a Rule apresentada – RuleOpeningGa
ion. A Condition trata da decisão da Rule, e
Rule. Assim sendo, Condition e Action trab
sal da Rule. 
 
do de Banaszewski et. al., 
a um valor ou a outro 
Premises que, quando 
Premises verdadeiras 
Instigation pode tanto 
amento, quanto alterar 
cias. 
ma regra causal. Esta 
sta de outros objetos 
ate – tem um objeto 
enquanto a Action trata 
balham para realizar o 


 
 
 
 
A Rule da Figura 
Eletrônico) citado na seçã
portão (FBE Gate) caso o c
Condition é composta po
inteligente. Estas duas Pr
RemoteControl: a) o portã
remoto foi pressionado? 
estados dos atributos das FB
Na verdade, cada P
De fato, para cada mudan
avaliações (lógicas) somen
estados. Igualmente, a part
avaliações (causais) somen
estados. Entretanto, isto tu
inteligentes, o que se cons
esboçado na Figura 6. 
Figura 5 - Exemplo de uma Rule em PON 
5 é referente a uma regra do sistema SPE 
ão 1. A Condition desta Rule lida com a d
controle remoto (FBE RemoteControl) tenha 
or duas Premises que se constituem em o
remises fazem as seguintes verificações so
ão eletrônico está fechado? (atGateState =C
(atRemoteStatus=TRUE). Assim, conclui-s
BEs compõem os fatos a serem avaliados pel
Premise avalia o estado de um (ou mesmo do
ça de estado de um Attribute da FBE, ocor
nte nas Premises relacionadas com eventuai
tir da mudança de estado das Premises, ocor
nte nas Conditions relacionadas com eventu
udo se dá por meio de uma cadeia de noti
stitui no fundamento do PON conforme mo
41 
 
(Simulador de Portão 
decisão de abertura do 
sido pressionado. Esta 
outro tipo de objeto-
obre as FBEs Gate e 
Closed) e b) o controle 
se (em geral) que os 
as Premises. 
ois) Attributes de FBE. 
rrem automaticamente 
is mudanças nos seus 
rrem automaticamente 
uais mudanças de seus 
ficações entre objetos 
odelado na Figura 4 e 


42 
 
 
Figura 6 - Inferência por Notificações 
 
Em suma, cada Attribute notifica as Premises relevantes sobre seus estados somente 
quando se fizer efetivamente necessário. Cada Premise, por sua vez, notifica as Conditions 
relevantes dos seus estados usando o mesmo princípio. Baseado nestes estados notificados é 
que a Condition pode ser aprovada ou não. Se a Condition é aprovada, a respectiva Rule pode 
ser ativada executando sua Action (BANASZEWSKI, 2009). 
Por sua vez, uma Action também é um objeto inteligente que se conecta a objetos 
inteligentes de outro tipo, as Instigations. Neste exemplo, a Action contém duas Instigations 
que fazem com que: a) o portão passe para o estado “abrindo” (executando o método 
opening()) e b) configura o estado do controle remoto para desligado (executando o método 
statusOff()). Efetivamente, o que uma Instigation faz é instigar um ou mais métodos 
responsáveis por realizar serviços ou habilidades de uma FBE.  
Cada método de um FBE é também tratado por um objeto inteligente, chamado de 
Method. A execução de um Method geralmente muda o estado de um ou mais Attributes. Na 
verdade, os conceitos de Attribute e Method representam uma evolução dos conceitos de 
atributos e métodos de classe da OO. A diferença é o desacoplamento explícito da classe 


43 
 
 
 
proprietária e a “inteligência” colaborativa pontual para com Premises e Instigations (SIMÃO 
e STADZISZ, 2008).  
Considerando-se isto, nota-se que a essência da computação no PON está organizada 
e distribuída entre entidades autônomas e reativas que colaboram por meio de notificações 
pontuais. Este arranjo forma o mecanismo de notificações, o qual determina o fluxo de 
execução das aplicações. Por meio deste mecanismo, as responsabilidades de um programa 
são divididas entre os objetos do modelo, o que permite execução otimizada e ‘desacoplada’ 
(ou minimamente acoplada) útil para aproveitamento correto de mono-processamento, bem 
como o processamento distribuído. 
A natureza do PON leva a uma nova maneira de compor software, onde os fluxos de 
execução são distribuídos e colaborativos nas entidades. Muito embora o PON permita 
compor software em alto nível na forma de regras, sem o conhecimento de sua essência, este 
conhecimento é deveras importante. Por exemplo, é importante saber dos impactos de 
desempenho e das estratégias de distribuição, como o agrupamento de elementos de maior 
fluxo de notificações juntos. Assim sendo, o PON permite uma nova maneira de estruturar, 
executar e pensar os artefatos de software. 
 
2.1.3. Framework do PON 
 
Esta dissertação se baseia no framework descrito em Banaszewski (2009) que 
contempla o PON implementado para ambientes monoprocessados. Vale notar que há estudos 
visando à implementação do PON para ambientes multiprocessados, como o de Weber et. al 
(2010), mas se encontram em desenvolvimento.  
A Figura 7 ilustra a estrutura do framework do PON (em notação UML) que é 
composta por dois pacotes de classes: Core e Application. As responsabilidades desses 
pacotes são as seguintes: 
• Core: contém as classes que modelam os objetos colaboradores do PON que 
participam do mecanismo de notificações. 
• Application: permite a definição de uma nova aplicação em PON e fornece o ponto de 
extensão entre os dois pacotes do framework. O ponto de extensão permite que uma 
aplicação, que é definida no pacote Application, use os serviços do pacote Core.  
 


44 
 
A seção 2.1.3.1
Application e, por sua 
implementação. 
 
2.1.3.1. 
Pacote Core 
 
O pacote Core é 
colaboradores. Este pacote
anteriormente. As classes
relacionam por meio de se
Instigation e Method – sen
execução da aplicação. Nes
do mecanismo de notificaç
as classes Attribute e Prem
que a classe Premise é a n
Core são apresentados do p
 
2.1.3.1.1. Estrutura class
 
A classe FBE repr
(real ou abstrato) de um pr
entidades por meio de se
representado como uma cla
FBE, denominadas Gate (
Essas subclasses FBE perte
Figura 7 - Estrutura do framework do PON 
 
descreve o pacote Core, a seção 2.1.3.
vez, a seção 2.1.3.3 descreve algumas
formado, basicamente, pelas classes Rule e
e é ilustrado pelo diagrama de classes da
s Rule e FBE se apresentam nas extrem
eus objetos colaboradores – Attribute, Premi
ndo que, a colaboração entre esses objetos,
sse diagrama, os papéis dos relacionamentos 
ções ocorre. Por exemplo, o relacionamento 
ise indica que a classe Attribute é o notificado
notificada (notified). Nas seções seguintes, o
ponto de vista da estrutura das classes FBE e R
se FBE 
resenta os elementos da base de fatos, como a
roblema computacional, e descreve os estado
eus atributos e métodos. Cada novo tipo
asse derivada da classe FBE. A Figura 8 ilus
(Portão) e RemoteControl (Controle Remot
encem ao SPE (Simulador de Portão Eletrônic
 
2 descreve o pacote 
s particularidades de 
e FBE e seus objetos 
Figura 4 apresentado 
midades opostas e se 
ise, Condition, Action, 
determina o fluxo de 
indicam como o fluxo 
“Changes State” entre 
ora (notifier), ao passo 
s elementos do pacote 
Rule. 
as entidades do mundo 
os e os serviços dessas 
o na base de fatos é 
stra duas subclasses da 
to) em notação UML. 
co). 


 
 
 
Figura 8 - Repr
Como já mencion
Attribute e Method.  Um 
instâncias da classe Attrib
“métodos” representados c
subclasse FBE consistem n
POO na qual os atributos e
classes do pacote Core pela
resentação dos objetos FBE em um sistema de portão e
 
nado anteriormente, uma classe FBE agreg
objeto FBE pode referenciar vários objeto
ute, assim como, um objeto FBE pode refe
como instâncias da classe Method. Os atribut
nos objetos colaboradores das suas instância
e métodos são entidades passivas. A Figura 9
a perspectiva da estrutura de uma classe FBE.
45 
 
eletrônico 
ga objetos das classes 
os “atributos” que são 
erenciar vários objetos 
tos e métodos de uma 
as, diferenciando-se da 
9 ilustra o diagrama de 
. 


46 
 
Figura 9 - Diagrama de classes Core - Estrutura de um objeto FBE 
 


47 
 
 
 
Os objetos Attributes são responsáveis por reagir a mudanças em seus estados 
gerando notificações para as condições dos objetos Rule pertinentes, que por sua vez avaliam 
a mudança ocorrida e atualizam o estado lógico das suas respectivas regras. Já os objetos 
Methods encapsulam a funcionalidade de um método, que tem como responsabilidade receber 
notificações oriundas de objetos colaboradores da ação de um objeto Rule gerando a sua 
execução (BANASZEWSKI, 2009). 
A classe Attribute é estendida por várias subclasses que encapsulam os tipos 
primitivos comuns das linguagens imperativas (ex: booleano, inteiro, ponto-flutuante, 
caractere e cadeia de caracteres). Em cada uma dessas subclasses da classe Attribute há a 
implementação de uma versão particular de um método chamado setValue(TipoDeDados 
valor) onde: 
• TipoDeDados – se refere ao tipo de dados que a subclasse encapsula; 
• valor – se refere ao parâmetro que modifica o valor interno de uma dada instância da 
subclasse. 
Basicamente, a responsabilidade do método setValue é receber um valor por 
parâmetro e atribuí-lo ao dado encapsulado na instância em questão. Caso o valor recebido 
seja diferente do anterior, o Attribute pode gerar notificações às premissas das regras 
associadas ao objeto Attribute. 
Por sua vez, a classe Method é estendida por duas subclasses: MethodPointer e 
MethodDerived. A subclasse MethodPointer  modela os objetos que encapsulam a chamada 
de um método definido na estrutura de uma classe FBE, sendo que o endereço desse método é 
atribuído ao objeto no momento de sua criação. Portanto, o método é implementado no 
próprio escopo da classe FBE. Por sua vez, a subclasse MethodDerived permite que classes 
sejam definidas explicitamente pelo programador por meio de sua extensão e implementação 
das instruções, que constituem a execução do método. Portanto, é um método declarado no 
escopo da classe FBE, mas que guarda referência para a chamada de um método de outra 
classe.  Uma instância de uma classe MethodDerived, quando notificada pelo respectivo 
objeto Instigation (a ser explicado na próxima seção), executará o método implementado em 
seu próprio escopo atribuindo maior capacidade de distribuição aos objetos, uma vez que a 
estrutura dos FBEs se encontra mais desacoplada de suas implementações. 
Ambas as classes – MethodPointer e MethodDerived – possuem a mesma interface – 
o método execute – para serem invocadas por um objeto Instigation, porém com versões de 
implementação diferentes.   


48 
 
2.1.3.1.2. Estrutura da cl
 
A classe Rule ger
sistema, representando a
anteriormente, um objeto R
trabalham juntos para real
indiretamente com outros 
Condition pode possuir ref
lógico sobre os estados d
Premise possui três elemen
F
 
• Reference: guarda r
Premise quando oco
• Operator: operador 
Value. Em PON um
(diferente), GREA
GREATEROREQU
• Value: pode ser um
Closed e TRUE). 
Quando um novo
respectivos objetos Attribu
lasse Rule 
rencia o conhecimento causal sobre qualqu
as expressões-causais desse sistema. Co
Rule é composto por um objeto Condition e 
lizar o conhecimento causal da regra. A cla
dois objetos colaboradores: Premises e Ins
ferências para um ou mais objetos Premises
dos objetos FBE. Como pode ser observad
ntos principais que colaboram entre si para a s
 
Figura 10 - Representação de uma Regra em PON  
referência a um objeto Attribute, que por sua
orre mudança em seu estado (ex: atGateState
r lógico usado para fazer comparações entre o
m operador lógico pode ser dos tipos: EQUAL
ATERTHAN (maior que), SMALLERTH
UAL (maior ou igual) e SMALLEROREQUA
ma constante ou uma referência para outro
 
o objeto Premise é criado, ele se conecta 
utes (Reference e/ou Value), armazenando su
uer comportamento do 
omo já mencionado 
um objeto Action, que 
asse Rule relaciona-se 
stigations. Um objeto 
s, que realizam o teste 
o na Figura 10, cada 
sua avaliação: 
 
a vez notifica o objeto 
 e atRemoteStatus). 
os valores Reference e 
L (igual), DIFFERENT 
HAN (menor que), 
AL (menor ou igual). 
o objeto Attribute (ex: 
automaticamente aos 
ua referência em uma 


49 
 
 
 
estrutura de dados implementada nos próprios Attributes (ex: lista encadeada ou tabela hash). 
Assim, com qualquer alteração nos valores desses Attributes, os mesmos terão como notificar 
os objetos Premises conectados a si. A Figura 11 ilustra o diagrama de classes do pacote Core 
pela perspectiva da estrutura da classe Rule. Neste diagrama de classes, Reference é dado pelo 
attributeA da classe Premise, Operator é dado por operattor e Value  por attributeB. 
Os objetos Premises são relacionadas nas análises causais por meio de um operador 
lógico definido no objeto Condition, representado pelo atributo logicalOperator da classe 
Condition. Como pode ser observado na Figura 11, esse atributo pode assumir um dos tipos 
definidos pela classe LogicalOperator: CONJUNCTION (conjunção), DISJUNCTION 
(disjunção) ou SINGLE (usado quando a Condition possui apenas uma Premise e dispensa 
avaliações lógicas). O operador lógico de um objeto Condition é definido por meio da 
passagem de uma constante identificadora ao construtor do objeto Rule. 
Por sua vez, um objeto Action pode possuir referências para um ou mais objetos 
Instigations, que constituem o corpo dos objetos Actions. Quando uma regra é aprovada, o 
objeto Action notifica os objetos Instigations relacionados, que por sua vez invocam os 
serviços dos objetos Methods. Por meio dos objetos Instigations, o objeto Rule modifica os 
estados dos objetos FBEs. 
No entanto, o objeto Instigation pode desviar o fluxo de notificações estabelecido 
inicialmente, que é referente à notificação estrita de um método (Instigation  Method  
Attribute), e notifica o Attribute diretamente, reduzindo assim a quantidade de notificações 
para atingir o mesmo objetivo. Esta representação, ilustrada pelo relacionamento “Changes 
State” entre as classes Instigation e Attribute da Figura 11, também facilita a compreensão da 
semântica da Rule, uma vez que as particularidades de alteração de um Attribute se 
apresentam no mesmo escopo da Rule ao invés de se encontrarem implementadas em um 
método. 


50 
 
Figura 11 - Diagrama de classes Core - Estrutura de um objeto Rule 
 


 
 
 
Portanto, a estrutu
juntamente com a adesão d
para a regra, o objeto Rule
para constituírem o mecan
transparente ao program
explicitamente pelo progra
Rule. 
 
2.1.3.2. 
Pacote Applicat
 
A Figura 12 ilustra
classe denominada Applica
pacotes do framework do 
definida no pacote Applicat
Fig
 
A classe Applicat
sendo que, o primeiro é us
ura de uma Rule é representada pela instancia
e premissas e instigações. De acordo com os 
e cria os objetos colaboradores em tempo de 
nismo de notificações, sendo que esse proc
mador. Os objetos Condition e Action, 
mador, são criados automaticamente na insta
tion 
a o diagrama de classes do pacote Application
ation que é a classe que representa o ponto de 
PON. O ponto de extensão permite que u
tion, use os serviços do pacote Core.  
gura 12 - Diagrama de Classes – Pacote Application 
tion possui dois métodos principais – initF
ado para definir os objetos FBE e o segundo
51 
ação de um objeto Rule 
parâmetros fornecidos 
execução e os conecta 
cesso ocorre de forma 
caso não definidos 
anciação de um objeto 
n. Nesta figura há uma 
extensão entre os dois 
uma aplicação, que é 
 
FactBase e initRules – 
o, por sua vez, é usado 


52 
 
para definir os objetos Rule. Adicionalmente, a classe Application possui mais três métodos 
relevantes para o contexto dessa dissertação: 
•  initSharedPremises: usado para a definição de objetos Premises que serão 
compartilhados por Conditions. 
• configureStartApplicationAction: usado para a definição de objetos Actions 
relacionados com a inicialização da Rule. 
• codeApplication: usado para a definição do código da aplicação. 
A classe Application também possui um atributo scheduler que é do tipo 
SchedulerStrategy que, por sua vez, armazena a estratégia de resolução de conflitos para 
aprovação da Rules. A classe SchedulerStrategy é estendida por quatro subclasses a fim de 
definir as seguintes estratégias: 
• BREADTH: se baseia no escalonamento FIFO,  
• PRIORITY: organiza os objetos Rules de acordo com as prioridades definidas nos 
mesmos,  
• DEPTH: se baseia no escalonamento FILO,  
• UNCACHED: a regra é adicionada ao escalonador e aprovada imediatamente  
Quando não há estratégia definida e a regra não é enviada ao escalonador, mas é 
aprovada imediatamente, é utilizada a estratégia NO_ONE. 
Na Figura 12, há uma classe denominada SimpleApplication que representa a classe 
definida pelo programador e estende o pacote Core do framework por meio da classe 
Application.  A classe SimpleApplication possui a definição do método construtor com um 
parâmetro do tipo integer que determina a estratégia de resolução de conflitos das regras do 
programa. 
A partir da identificação e implementação das classes FBEs é possível definir esses 
mesmos objetos FBEs no escopo do método initFactBase() e as regras no escopo do método 
initRules(). Para facilitar o entendimento de como as definições desses métodos ocorrem, o 
exemplo do portão será retomado. A Figura 13 ilustra as subclasses das FBEs – 
RemoteControl e Gate – e suas estruturas estendidas com as classes Attribute e Method. 


 
 
 
Figura 13 - E
 
Na Figura 13, a cl
instância da subclasse Inte
atRemoteStatus, que é ins
possuem a declaração de 
Method. Estas classes são 
que MtStatusClosing é d
MethodDerived. No exem
MethodPointer que encaps
classe MtStatusClosing foi 
classe MethodDerived e im
(neste caso, fazer o portão f
Baseado nesse ex
preenchimento dos método
RemoteControl são realizad
e 5). As Rules são definida
definição de uma regra - rl
que a regra rlOpeningGate
de regra default utilizado 
completa constituída de ob
de regra como será mostrad
Exemplo da estrutura FBE (adaptado de Banaszewski (
lasse Gate possui a declaração do atributo a
eger, e a classe RemoteControl possui a d
stância de subclasse Boolean. Adicionalmen
métodos que constituem as instâncias das
MethodPointer e MtStatusClosing no exemp
definida explicitamente pelo programador 
mplo, o objeto mtStatusOpening é uma 
ula a chamada do método Opening() definid
definida explicitamente pelo programador po
mplementação das instruções que constituem
fechar). 
xemplo apresentado, o trecho de código d
os initFactBase e initRules. As instanciaçõ
das no método initFactBase() da classe Simpl
as no escopo do método initRules sendo que
lOpeningGate - no método initRules (linha 1
é uma instância da classe RuleObject. Essa c
no framework, em que uma regra é estru
bjetos Premise, Condition, Action e Instigati
do na seção 2.1.3.3. 
53 
 
(2009)) 
tGateState, que é uma 
declaração do atributo 
nte essas classes FBE 
s subclasses da classe 
plo em questão, sendo 
ao estender a classe 
instância da classe 
da na classe Gate. Já a 
or meio da extensão da 
m a execução método 
a Figura 14 ilustra o 
ões dos FBEs Gate e 
leApplication (linhas 4 
e, neste exemplo, há a 
10).  Pode-se observar 
classe representa o tipo 
uturada em sua forma 
ion. Mas há outro tipo 


54 
 
Fi
 
No exemplo em qu
na instanciação do objeto
Condition é composto por d
por dois objetos Instigatio
estado do controle remoto 
portão está fechado (CLO
addPremise, que recebe os 
construtor - Reference, Va
regra rlOpeningGate (linha
Value ao valor “0”, sen
(Premise::EQUAL). No ex
relacionadas 
por 
me
“Condition::CONJUNCTIO
O objeto Action p
dependendo da forma co
conectados ao objeto Actio
Na linha 13, o Instigation
atribuição será realizada pe
objeto Method. Neste caso
valor constante para ser atr
método addMethod, o que 
sendo passado como referên
Pode-se ressaltar q
definidos como instâncias 
igura 14 - Inicialização dos FBEs e Rules em C++ 
uestão, os objetos Condition e Action são cri
o Rule (mas poderiam ser instanciado man
dois objetos Premises (linhas 11 e 12) e o obj
ons (linhas 13 e 14). As duas Premises ate
é verdadeiro e se o estado do portão é “0”
OSED)). Essas Premises são criadas pela 
três parâmetros necessários para a invocação
alue e Operator. Por exemplo, na criação da
a 12), o Reference corresponde ao Attribute 
ndo que ambos são comparados pelo Op
xemplo em questão, as premissas da regra 
eio 
de 
uma 
conjunção 
definida
ON” (linha 10). 
possui dois objetos Instigation que possuem
omo são definidos. Os objetos Instigatio
on por meio da execução do método addInsti
n é conectado pelo método addInstigation, 
elo método setValue da classe Attribute, sem
o, addInstigation recebe uma referência par
ribuído ao Attribute. Já na linha 14, o Instiga
significa que a atribuição será realizada dent
ncia (mtStatusOpening é um ponteiro para se
que, os objetos Rules, Condition, Premise, A
da suas respectivas classes do framework. P
 
iados automaticamente 
nualmente). O objeto 
jeto Action é composto 
stam o seguinte: se o 
” (que significa que o 
execução do método 
o do respectivo método 
a segunda Premise da 
gate->atGateState e o 
perator de igualdade 
rlOpeningGate estão 
a 
pela 
constante 
m execuções diferentes 
ons são basicamente 
igation ou addMethod. 
o que significa que a 
m a intervenção de um 
ra um Attribute e um 
ation é conectado pelo 
tro do método que está 
eu respectivo método). 
ction e Instigation são 
Por sua vez, um novo 


 
 
 
FBE é definido como um
instanciados objetos FBEs d
 
2.1.3.3. 
Particularidade
 
A seção anterior 
apresenta algumas partic
dissertação. Essas particul
aprovação de um objeto R
conteúdo do Rule. A Figura
de implementação. 
 
Figu
a subclasse da classe FBE do framework s
dessa classe definida pelo programador. 
es 
apresentou uma visão geral do framework
cularidades de implementação que são 
laridades são referentes a alguns compone
Rule – Attribute, Premise e Conditon – e a
a 15 ilustra o pacote Core pela perspectiva de
ura 15 - Diagrama de classes Core - Particularidades 
55 
sendo, posteriormente, 
k do PON. Esta seção 
relevantes para esta 
entes participantes da 
a execução do próprio 
e suas particularidades 
 


56 
 
• Re-notificações 
 
Visando evitar notificações desnecessárias, ou seja, 
em duplicidade, a 
implementação default de um Attribute somente notifica os objetos Premises vinculados 
àquele Attribute quando o estado do Attribute for alterado. Esta solução é satisfatória para a 
maioria das aplicações, mas não para algumas que demandam que uma regra seja reavaliada e 
re-executada mesmo quando os estados dos seus atributos não são mais alterados. Para sanar 
essa necessidade, a classe Attribute possui a opção de iniciar um fluxo de notificações mesmo 
quando a atribuição de um valor não corresponde à mudança de seu estado. Isso é possível por 
meio de uma nova versão do método setValue(TipoDeDados valor), cuja assinatura é 
setValue(TipoDeDados valor, int flag) como ilustrado na Figura 15. Nessa nova assinatura, 
valor se refere ao novo estado atribuído ao Attribute e flag se refere ao uso de re-notificações. 
Se a re-notificação for desejada, o programador deve usar a flag Attribute::RENOTIFY, caso 
contrário basta usar a assinatura padrão do método. 
 
• Implementação Premise 
 
No mecanismo padrão do framework do PON, os objetos Premises notificam todos 
os objetos Conditions que são referenciados em sua lista encadeada. Porém, há situações 
particulares em que um Premise não precisa notificar todos os objetos Conditions de sua lista, 
bastando que as notificações ocorram até que um dos objetos Conditions seja satisfeito. 
Nestes casos, somente um único objeto Rule é executado em relação ao estado de um objeto 
Premise específico. Em PON, esse comportamento é possível por meio da utilização da 
premise exclusive (premissa exclusive) – definida pelo atributo “exclusive” da classe Premise 
na Figura 15 –, que oferece um comportamento opcional a um objeto Premise.  Para que este 
comportamento seja ativado, necessita-se que o programador defina explicitamente esta opção 
por meio da atribuição da flag Premise::EXCLUSIVE ao construtor de uma Premise. A Figura 
16 ilustra a utilização da Premissa Exclusiva no exemplo do robô-motorista de Banaszewski 
(2009). Neste exemplo, a utilização da flag pode ser observada nas linhas 3, 10 e 17, na 
premissa que confirma o direcionamento do veículo em um cruzamento. 


57 
 
 
 
 
Figura 16 - Premise Exclusive em C++ (BANASZEWSKI,2009) 
 
Pela implementação padrão da classe Premise, os três objetos Conditions destes 
Rules seriam avaliados consecutivamente. Porém, com o comportamento de exclusividade, a 
Premise afetada pelo sinal do semáforo (linhas 3, 10 ou 17) notifica as Conditions até que a 
primeira delas seja satisfeita. 
 
• Implementação da Condition 
 
As classes Conditions possuem uma funcionalidade opcional, que permite que elas 
organizem a relação entre suas Premises por meio de diferentes combinações de operadores 
lógicos. Há casos que requerem a utilização de mais de um operador lógico, como o caso da 
Figura 17 que apresenta uma implementação comum de expressão causal complexa em PP ou 
PPO. 
 
Figura 17 - Exemplo de uma expressão causal complexa em C++ 
 
É possível utilizar mais de um operador lógico por Condition a fim de representar 
expressões complexas, mas neste caso, deve-se agrupar os objetos Premise que estão 


58 
 
relacionados por um mesmo tipo de operador lógico, por meio do uso de uma especialização 
da classe Condition, a classe SubCondition (Figura 15). Com a utilização de SubConditions, 
as Premises notificam a Condition indiretamente, por meio das suas SubConditions. Neste 
contexto, as SubConditions fazem o papel das Premises, notificando as respectivas Conditions 
no momento em que tiverem seus estados lógicos alterados. Para uma Condition, é indiferente 
receber notificações de SubConditions ou Premises, uma vez que os seus estados lógicos são 
atualizados da mesma maneira. 
Utilizando SubCondition, a expressão causal da Figura 17 é representada em apenas 
um regra como na Figura 18. Na representação padrão da Condition seriam necessárias duas 
regras para representar essa expressão causal. 
 
Figura 18 - Representação de uma expressão causal  complexa com subcondições 
 
• Implementação da Rule 
 
Uma Rule possui duas classes derivadas: RuleObject e RuleDerived (Figura 15). A 
classe RuleObject representa o tipo de regra default utilizado no framework, em que uma 
regra é estruturada em sua forma completa constituída de objetos Premise, Condition, Action 
e Instigation. No entanto, é possível implementar o conteúdo de execução (Action) da Rule 
diretamente em seu corpo, por meio do método invocado em sua execução, que é o execute(). 
A implementação ocorre por meio da utilização da classe RuleDerived. Nesta, a ação da Rule 
é implementada com toda a flexibilidade do PP ou POO, permitindo atribuições de valores e 
chamadas de métodos implementados de forma imperativa. A Figura 19 ilustra uma exemplo 
de utilização da RuleDerived. 


59 
 
 
 
 
Figura 19 - Código exemplo da RuleDerived em C++ 
 
2.1.4. Modelagem em PON 
 
Apesar de o PON não possuir técnicas formalizadas para orientar os desenvolvedores 
na elaboração de seu projeto, há a utilização de modelos em outros trabalhos sobre o PON. 
Simão (2005) faz uso de diagramas de sequência em seu trabalho para modelar as interações 
entre as entidades Holons, como ilustrado na Figura 20. 
 
Figura 20 - Diagrama de Sequência - interação entre os Holons 
 
Adicionalmente, Simão apresenta a compatibilidade entre seu metamodelo para 
controle discreto e as redes de Petri, que permite a modelagem discreta de sistemas 
distribuídos (tema que será discutido na seção 2.4.4).  
 
 


60 
 
2.2. 
PROCESSO UNIFICADO DA RATIONAL (RUP) 
 
Esta seção introduz os principais conceitos do processo de software denominado 
Rational Unified Process (RUP) (Processo Unificado da Rational). A seção 2.2.1 apresenta 
uma visão geral sobre esse processo e as seções  2.2.2 e 2.2.3 apresentam conceitos relevantes 
para essa dissertação sobre a sua estrutura. 
 
2.2.1. Visão geral 
 
A maioria das equipes de software ainda usa o processo em cascata para 
desenvolvimento de projetos, no qual cada fase é completada em uma sequência rigorosa de 
levantamento de requisitos, análise e projeto, implementação, integração e testes. Ou ainda, 
mais comum, é utilizada uma abordagem em cascata modificada com ciclos de feedbacks 
adicionados ao fluxo original. Essas abordagens postergam a fase de teste até o fim do ciclo 
de vida do projeto, quando problemas tendem a ser árduos e caros para se resolver, além de 
causar riscos às datas de entrega (KROLL e KRUCHTEN, 2003). Em contraste, o Processo 
Unificado da Rational (Rational Unified Process – RUP) utiliza uma abordagem iterativa, que 
é uma sequência de passos e iterações incrementais. Cada iteração inclui algumas, ou a 
maioria das disciplinas de desenvolvimento (requisitos, análise, projeto, implementação e 
testes) como é ilustrado na Figura 21. 
 
Figura 21 - RUP – Processo iterativo e incremental 
 


 
 
 
Nessa abordagem
definidos e produz um tr
sucessiva constrói resultad
sistema até que o produto
disciplinas de requisitos e
terão maior ênfase em impl
O RUP foi proje
software. Mais particular
Engineering Metamodel (S
UML. A Figura 22 ilustr
(dimensões):  
• Estrutura dinâmic
processo. Ela mostr
marcos, desenvolve
• Estrutura estática
Ela descreve como
logicamente agrupa
m iterativa, cada iteração tem um conjun
rabalho de construção parcial do sistema 
dos no trabalho da iteração anterior, a fim 
o final esteja completo. Iterações iniciais t
análise e projeto, enquanto que iterações ma
lementação e testes. 
etado com técnicas similares àquelas utiliz
rmente, o RUP é modelado usando-se 
SPEM) – um padrão para modelagem de p
ra a arquitetura completa do RUP, que p
ca – a dimensão horizontal representa a e
ra como o processo, expresso em termos de ci
e-se durante o ciclo de vida do projeto. 
– a dimensão vertical representa a estrutura
 os elementos do processo – atividades, art
ados em disciplinas (workflows). 
Figura 22 - Arquitetura do RUP 
 
 
61 
nto de objetivos bem 
final. Cada iteração 
de evoluir e refinar o 
terão mais ênfase nas 
ais ao final do projeto 
zadas em projetos de 
o Software Process 
processos baseados na 
possui duas estruturas 
estrutura dinâmica do 
iclos, fases, iterações e 
a estática do processo. 
tefatos e papéis – são 
 


62 
 
2.2.2. Estrutura Dinâmica: Desenvolvimento Iterativo 
 
A estrutura dinâmica do RUP trata do ciclo de vida ou dimensão do tempo de um 
projeto. O RUP fornece uma abordagem estruturada para o desenvolvimento iterativo, 
dividindo o projeto em quatro fases: Concepção, Elaboração, Construção e Transição. Cada 
fase contém uma ou mais iterações que focam nas entregas técnicas necessárias para se 
alcançar os objetivos de cada fase. Devem haver tantas iterações quanto forem necessárias 
para se alcançar o objetivo satisfatoriamente. Se um objetivo não puder ser atingido dentro da 
fase necessária, então outra iteração deve ser adicionada à fase.  As descrições das fases são 
as seguintes (KRUCHTEN, 2003): 
• Concepção – estabelecer um bom entendimento geral de todos os requisitos do 
sistema e estabelecer o escopo do mesmo. 
• Elaboração – planejar as atividades necessárias e recursos exigidos, bem como 
especificar as características e projetar a arquitetura.  
• Construção – realizar a implementação do sistema a fim de criar sua primeira versão 
operacional. 
• Transição – criar a versão final do sistema e entregá-la ao cliente, além de treinar, 
apoiar e manter o produto até que o cliente esteja satisfeito. 
 
As quatro fases constituem um ciclo de desenvolvimento e produzem uma geração 
de software. Um produto de software é criado em um ciclo de desenvolvimento inicial, sendo 
que o produto evoluirá em sua próxima geração por uma repetição sequencial das fases de 
concepção, elaboração, construção e transição, mas com diferentes ênfases em cada uma 
delas. 
 
2.2.3. Estrutura Estática: Descrição do Processo 
 
A estrutura estática do RUP define como os elementos do processo estão 
logicamente agrupados dentro de disciplinas do processo. Um processo descreve quem está 
fazendo o quê, como e quando. Como pode ser observado na Figura 23, o RUP é 
representado por três elementos do processo principais: 


63 
 
 
 
 
Figura 23 - Trabalhadores, atividades e artefato 
 
• Papel/Worker (quem): define o comportamento e as responsabilidades de um 
indivíduo ou grupo de indivíduos. 
•  Atividade/Activity (como): define o trabalho que o papel deve desempenhar. A 
atividade tem um objetivo claro, geralmente expresso em termos da criação ou 
atualização de um artefato como um modelo, um componente ou um plano.  
• Artefato/Artifact (o quê): é um elemento de informação que é produzido, modificado 
ou utilizado por um processo. Os artefatos são usados como entrada para que os 
papéis desempenhem uma atividade e são também os resultados de tais atividades. 
Um artefato pode ser diversas coisas: um modelo como um modelo de casos de uso; 
um elemento de modelo dentro de um modelo, como uma classe, um caso de uso ou 
um subsistema; um documento como uma Visão ou Caso de Negócio; um código 
fonte; e um executável como um protótipo. Um artefato pode ser documentado mais 
formalmente (usando-se uma ferramenta) ou informalmente (capturado em uma 
mensagem de email). 
 
Uma mera listagem de todos os papéis, atividades e artefatos não constituem 
realmente um processo. É necessário descrever uma sequência significativa de atividades que 


64 
 
produz algum resultado de valor e mostra a interação entre os papéis. Para tanto, existe um 
quarto elemento, o Fluxo de Trabalho. 
 
• Fluxo de Trabalho (quando): descreve um encadeamento de atividades que produz 
artefatos como resultado, além de mostrar a interação entre os papéis envolvidos no 
processo. Um fluxo de trabalho pode ser de diferentes tipos sendo que, os dois mais 
comuns são:  
― Disciplinas: são fluxos de trabalho de alto nível (ilustrados na Figura 22 em seu 
eixo vertical, ex: modelagem de negócios); 
― Detalhes do Fluxo de Trabalho: são fluxos de trabalho dentro de uma disciplina. 
Um fluxo de trabalho, em termos de UML, pode ser representado por um diagrama de 
sequência, um diagrama de colaboração ou, ainda, por um diagrama de atividades, 
como ilustrado na Figura 24. 
 
Figura 24 - Fluxo de Trabalho da Disciplina de Requisitos 
O RUP é composto por nove disciplinas, sendo que cada uma abrange um 
determinado aspecto do sistema (KRUCHTEN, 2003):  


65 
 
 
 
• Modelagem de negócios: entender a estrutura e a dinâmica da organização na qual um 
sistema será distribuído e derivar os requisitos necessários do sistema. 
• Requisitos: estabelecer o que o sistema deve fazer juntamente com os clientes e outros 
interessados no sistema; definir os limites do sistema e, de acordo com as exigências 
deste novo sistema, criar casos de uso que serão a base para estimar o custo e o 
esforço de desenvolvimento do sistema.  
• Análise e Projeto: transformar os requisitos do sistema a ser construído em uma 
solução arquitetural do software. Devem ser produzidos modelos com as 
especificações técnicas a serem seguidas na implementação de cada caso de uso. 
• Implementação: transformar os modelos criados durante a fase de Análise e Projeto 
em código-fonte utilizável e testar unitariamente o código produzido. 
• Teste: a proposta desta disciplina é avaliar a qualidade do produto, o que não envolve 
somente o teste do produto final. Essa disciplina se inicia logo no início do projeto, 
com a avaliação da arquitetura do sistema, e continua com a avaliação do produto final 
a ser entregue ao cliente. 
• Implantação ou Distribuição: garantir que o software produzido esteja disponível 
para seus usuários finais. 
• Gerência de configuração e mudança: controlar as mudanças e manter a integridade 
de cada um dos artefatos produzidos no projeto. Cada um desses artefatos (ou itens de 
configuração) deve ser identificado, auditado e possuir níveis de configuração e 
manutenção definidos. 
• Gerência de projeto: balancear objetivos que competem entre si, gerenciar riscos, 
monitorar o projeto e satisfazer as regras que garantirão a entrega de um produto que 
irá atender às expectativas de clientes e usuários finais. 
• Ambiente: configurar o ambiente para que o processo e suas atividades possam ser 
executados. Devem-se prover nesta disciplina os processos e ferramentas necessárias 
para que todas as atividades do projeto possam ser devidamente executadas por cada 
papel. 
 
2.3. 
LINGUAGEM E PERFIL UML 
 
Este seção aborda conceitos sobre a UML e suas particularidades relevantes para 
essa dissertação. A seção 2.3.1 apresenta a definição de modelos e a arquitetura de quatro 


66 
 
camadas da OMG para defi
UML para essa disserta
detalhadamente os conceit
apresentar um método para
 
2.3.1. Contextualização 
 
O aumento da co
como os arquitetos e engen
maior com a estrutura e q
aspectos de modelagem n
abstrair os sistemas auxilian
uma forma simplificada, 
utilizadas (FUENTES e VA
De acordo com M
elementos que o descreve”
de Objetos) define uma 
conceituais para criar um
modelagem e o metamode
denominadas M0 (informa
(OMG, 2002) (Figura 25):
 
F
 
finição de modelos. A seção 2.3.2 apresenta c
ação como ‘porta’ e ‘interface’. E a s
tos de mecanismos de extensão da UML e 
a definição de perfis.  
omplexidade dos sistemas de informação te
nheiros de software trabalham. Inicialmente h
ualidade do código, sendo que hoje há uma
no processo de desenvolvimento de softwar
ndo o desenvolvimento de aplicações maiore
independentemente da linguagem de progr
ALLECILLO, 2004).  
Mellor et al. (2004), “o modelo de um siste
”. A OMG (Object Management Group - Gru
arquitetura de quatro camadas que separa
m modelo: as instâncias, o modelo do siste
elo da linguagem. Na terminologia da OM
ação), M1 (modelo), M2 (metamodelo) e M
Figura 25 - Arquitetura OMG em quatro camadas  
conceitos relevantes da 
seção 2.3.3 introduz 
Perfil UML, além de 
em desafiado o modo 
havia uma preocupação 
a atenção especial aos 
re. Modelos permitem 
es e mais complexas de 
ramação e plataforma 
ema é um conjunto de 
upo de Gerenciamento 
a os diferentes níveis 
ema, a linguagem de 
MG essas camadas são 
M3 (meta-metamodelo) 
 


67 
 
 
 
• Camada de Informação (M0): compreende os dados que se deseja descrever, ou seja, 
as instâncias do sistema. O objeto “EmpregadoObj” denominado “João” é exemplo de 
um elemento da camada M0. 
 
• Camada de Modelo (M1): é composta por modelos (metadados) que descrevem os 
dados da camada M0. A camada M1 define, por exemplo, uma classe denominada 
“Empregado” que possui o atributo “Nome”. Os elementos da camada M1 são 
classificações dos elementos da camada M0, da mesma forma que cada elemento da 
camada M0 é uma instância de um elemento da camada M1. 
 
• Camada do Metamodelo (M2): compreende a descrição da estrutura e semântica do 
modelo definido da camada M1. É um modelo para descrever outros modelos, sendo 
chamado de metamodelo. Um metamodelo é uma linguagem abstrata para definir tipos 
de metadado. Um exemplo de metamodelo é a UML, que define os conceitos como 
“Classes”, “Atributos” e “Associações”. Todo elemento da camada M1 é uma 
instância de um elemento M2, assim como todo elemento da camada M2 categoriza os 
elementos da camada M1.  
 
• Camada de Meta-Metamodelo (M3): finalmente, a camada M3 define os conceitos, 
estrutura e semântica que são utilizados para definir os metamodelos. Como exemplo, 
o conceito “Classe” da UML, que pertence à camada M2, é uma instância dos 
elementos correspondentes da camada M3.  Na camada M3 é definido o que é uma 
“Classe” e qual a sua relação com os outros conceitos (ex: uma Classe é um 
classificador e possui associações, um conjunto de atributos e métodos, etc.). Um 
exemplo de meta-metamodelo é a linguagem MOF (Meta-Object Facility) criada pela 
OMG, que é definida como linguagem abstrata composta de um framework para 
especificação e construção de metamodelos.  
 
Portanto, considerando a arquitetura exposta, define-se que o metamodelo da UML é 
descrito como uma instância do meta-metamodelo da linguagem MOF, e um modelo UML é 
descrito como uma instância do metamodelo da UML (OMG, 2002). A Figura 26 ilustra uma 
instanciação típica da arquitetura MOF com metamodelos para representar diagramas UML e 
OMG IDL (Interface Definition Language – Linguagem de Definição de Interface). 


68 
 
 
 
Figura 26 - Arquitetura MOF de Metadados (OMG,2002) 
 
2.3.2. Linguagem UML 
 
A Linguagem de Modelagem Unificada (Unified Modeling Language - UML) é 
definida como uma linguagem para especificação, visualização, construção e documentação 
de artefatos de sistemas de software por meio do uso do Paradigma Orientado a Objetos 
(OMG, 2003; GUEDES, 2005). A UML surgiu da união dos três métodos de modelagem 
mais populares entre os profissionais de engenharia de software até meados de década de 90: 
o método Booch, o método OMT (Object Modeling Technique) e o método OOSE (Object-
Oriented Software Engineering) (GUEDES, 2004). A união desses métodos foi financiada 
pela Rational Software, sendo que a OMG adotou a UML como linguagem padrão de 
modelagem em 1997.  
Como visto na seção anterior, a arquitetura da UML é baseada em uma estrutura de 
metamodelos de quatro camadas definida pela OMG, que separa os diferentes níveis 
conceituais para construir um modelo. O metamodelo da UML é definido como uma das 
quatro camadas dessa arquitetura sendo descrito por uma combinação de notação gráfica, 
linguagem natural e linguagem formal (OMG, 2003). Portanto, a UML não é uma linguagem 
de programação e sim uma linguagem de modelagem que tem por objetivo auxiliar na 
definição das características do software, tais como seus requisitos, seu comportamento, sua 


69 
 
 
 
estrutura lógica, a dinâmica de seus processos e suas necessidades físicas em relação ao 
equipamento sobre o qual o sistema deverá ser implantado (LIMA, 2008).  
Na UML os sistemas são constituídos por modelos que representam diferentes pontos 
de vista, sendo que cada um descreve um aspecto particular de uma mesma solução. Esses 
pontos de vistas são denominados visões (LIMA, 2008). Por meio dessas visões, a UML 
permite criar modelos com alto nível de abstração, descrevendo como o sistema deve 
funcionar integrado ao ambiente.   
Conforme o desenvolvimento do sistema ocorre, são construídos, refinados e 
detalhados diversos modelos. Um modelo é formado por um conjunto de diagramas que 
apresentam diferentes versões em diferentes níveis de detalhamento. Apesar de um diagrama 
representar parcialmente um aspecto do sistema, ele é semanticamente consistente com os 
demais diagramas das outras visões. (LIMA, 2008). 
Os diagramas da UML são divididos em dois grupos principais: diagramas 
estruturais e diagramas comportamentais. O primeiro grupo descreve os elementos estruturais 
que compõem o sistema, representando suas partes e seus relacionamentos. Já o segundo 
grupo descreve o comportamento dos elementos e suas interações.  A Figura 27 ilustra a 
classificação dos diagramas da UML. 
 
Figura 27 - Classificação dos Diagramas da UML (OMG, 2007) 
 
 
 
 


70 
 
2.3.2.1. 
Porta e Interfa
 
De acordo com LI
ponto de interação entre um
classificador e suas partes i
ambiente e, também, os 
associada a uma ou mais in
requerido pelo sistema. As 
classificador ou de suas par
Já uma “interfac
específicas e pode ser de do
• Interfaces Fornec
representadas por um
 
• Interfaces Requeri
uma determinada c
implementar esses s
por uma linha sólida
 
A Figura 28 ilustra
possui um sistema de tran
criada uma classe “Mot
“Transmissão”, uma interf
porta, e “Energia” (ou alim
motor espera que o ambien
Figura 28 - I
 
 
 
ce 
IMA (2008) uma “porta” é um elemento usad
m classificador, geralmente uma classe, e se
internas. Ela pode indicar os serviços que um
serviços que ela requer desse ambiente. U
nterfaces garantindo que o classificador supor
portas são representadas por quadrados sobr
rtes internas. 
ce” é usada para descrever os serviços d
ois tipos (GUEDES, 2005):  
idas: descrevem serviços implementados
m círculo fechado ligado à classe por uma ret
idas: descrevem os serviços que outras clas
classe, que não precisa ter conhecimento 
serviços. São representadas por um semicírcu
a.  
a um exemplo dos conceitos de porta e interf
nsmissão e precisa de energia para trabalha
or” contendo uma porta “PortaMotor” c
face fornecida que especifica um serviço qu
mentação), uma interface requerida que espec
te forneça para realizar seu comportamento.
 
Interfaces Fornecida e Requerida (adaptado de LIMA,
do para especificar um 
eu ambiente ou entre o 
a classe oferece ao seu 
Uma porta pode estar 
rte um comportamento 
epostos à borda de um 
disponíveis de classes 
por uma classe. São 
ta sólida. 
sses devem fornecer a 
de quais classes irão 
ulo ligado a uma classe 
face, no qual um motor 
ar. Neste exemplo foi 
com duas interfaces: 
ue o motor oferece na 
cifica um serviço que o 
 2008) 


71 
 
 
 
2.3.3. Perfil UML 
 
A UML fornece um conjunto rico de conceitos de modelagem e notações que foram 
desenvolvidos para satisfazer as necessidades de projetos típicos de modelagem de software. 
No entanto, há casos em que são necessárias características adicionais de modelagem além 
daquelas definidas pela UML padrão, como no caso de domínios específicos de aplicação (ex: 
sistemas em tempo-real, modelagem de processos de negócios, finanças) ou implementação 
de tecnologias (ex: .NET, J2EE ou CORBA). Essas necessidades especiais podem ser 
satisfeitas por meio da utilização de mecanismos de extensão da UML. Esses mecanismos 
permitem a adição de novos elementos de modelagem ao metamodelo da UML e a qualquer 
outro metamodelo definido pelo MOF, assim como a outros perfis UML. Um conjunto desses 
mecanismos de extensão agrupados dentro de um pacote UML estereotipado <<profile>> 
formam um Perfil UML (OMG, 2003; FUENTES e VALLECILLO, 2004). A Figura 29 
ilustra a contextualização do Perfil UML dentro da arquitetura MOF de quatro camadas, que é 
definido na camada de metamodelos (M2).  
 
Figura 29 - Contextualização Perfil UML (Adaptado de ABDULLAH, 2006) 


72 
 
Atualmente, existem vários perfis UML que estão disponíveis para uso público. 
Alguns deles têm sido adotados e padronizados pela OMG, tais como, o Perfil UML para 
CORBA e para CCM (CORBA Component Model) (OMG, 2005a), o Perfil UML para EAI 
(Enterprise Application Integrations) (OMG, 2004) e o Perfil UML para Scheduling, 
Performance e Time (OMG, 2007). Outros perfis UML têm sido definidos por organizações 
privadas e companhias de software, e têm sido utilizados em vários domínios de aplicação. 
Este é o caso, por exemplo, do Perfil UML para aplicações EJB chamado “UML/EJB 
Mapping Specification” que tem sido desenvolvido pelo JCP (Java Community Process). 
Também existem perfis UML para linguagens de programação como Java e C#. 
A OMG fornece algumas razões para estender e adaptar a UML padrão (OMG, 
2007): 
• adaptar uma terminologia a plataformas e domínios específicos; 
• fornecer uma sintaxe para construtores que não têm uma notação; 
• fornecer um notação diferente para símbolos já existentes; 
• adicionar semântica que não é claramente especificada no metamodelo da UML; 
• adicionar semântica que não existe no metamodelo da UML; 
• modificar restrições já existentes no metamodelo, restringindo sua forma de utilização;  
• adicionar informações que podem ser úteis na hora de transformar um modelo em 
outro modelo ou códigos. 
 
O metamodelo da UML pode ser estendido por meio da utilização de três 
mecanismos de extensão definidos pela própria UML: estereótipo, valor etiquetado e restrição 
(LIMA, 2008).  
• Estereótipo: permite a definição de um novo elemento de modelo com base em um 
elemento já existente na UML. Um estereótipo pode basear-se em qualquer elemento 
da UML representando uma subclasse de um elemento já existente com a mesma 
forma (atributos e relacionamentos), mas com diferentes funcionalidades. Estereótipos 
devem consistir de restrições extras e valores etiquetados para adicionar informações 
necessárias aos novos elementos, sendo que são representados com um nome entre 
<<>> e (<<stereotype>>). A Figura 30 ilustra um exemplo de metamodelo no qual o 
estereótipo “Regra” estende a metaclasse “Class” da UML por meio de um 
relacionamento de extensão (<<extends>>) que indica que as propriedades da 
metaclasse estão sendo herdadas pelo estereótipo.  


 
 
 
Fi
• Valor etiquetado:
UML, os valores 
elementos. Um valo
No metamodelo os 
define o estereótipo
Como exemplo, foi
30 representado por
Figu
 
• Restrição: é uma 
metamodelo ou mo
Tal especificação é 
mais ou menos for
modelo diretamente
notação matemática
como um texto em
Language) (OMG, 
Graficamente, ela p
nota UML anexada
exemplo, a seguinte
ter associação com
(ABDULLAH, 200
 
 
 
igura 30 - Exemplo de estereótipo no metamodelo 
 
enquanto os estereótipos permitem adicion
etiquetados permitem adicionar novas p
or etiquetado pode ser adicionado a qualquer
valores etiquetados são representados como a
o e no modelo eles são representados por u
i adicionado um valor etiquetado ao estereóti
r “Identificador” na Figura 31. 
ura 31 - Exemplo de valor etiquetado no metamodelo 
informação semântica anexada a um ou
odelo para expressar uma condição que o si
escrita em uma determinada linguagem de re
rmal. Uma restrição pode ser adicionada tan
e quanto a estereótipos. Uma restrição pode se
a, pseudocódigo, linguagem de programação,
m português – ou formal – como a OC
2010), que é a linguagem de restrição da 
pode ser adicionada ao modelo ou metamod
a ou adicionada no compartimento “constrai
e restrição em OCL especifica que o estereóti
m os estereótipos <<Condition>> e <<Ac
6)): 
73 
nar novos elementos à 
propriedades a esses 
r elemento do modelo. 
atributos da classe que 
um par (nome, valor). 
ipo “Regra” da Figura 
 
u mais elementos do 
stema deve satisfazer. 
estrições, que pode ser 
nto a um elemento de 
er especificada usando 
 linguagem informal – 
L (Object Constraint 
UML (LIMA, 2008). 
delo por meio de uma 
ints” da classe. Como 
ipo <<Rule>> só pode 
ction>> (adaptado de 


74 
 
<<Rule>> constraints 
context Rule inv: 
self.allOppositeAssociationEnds -> forAll 
participant. isStereotype (`Condition´) or 
participant .isStereotype (`Action´) 
 
Portanto, um Perfil UML é um conjunto desses mecanismos de extensão agrupados 
dentro de um pacote UML estereotipado <<profile>>. Esses mecanismos permitem a 
extensão da sintaxe e semântica dos elementos UML devendo, no entanto, respeitar as 
semânticas originais dos elementos sendo estendidos. 
 
2.3.3.1. 
Elaboração de Perfis UML 
 
Os Perfis UML foram definidos originalmente na versão 1.0 da UML, sendo que sua 
utilização pela comunidade de software era limitada por definições ambíguas e pela falta de 
um guia de uso preciso (FUENTES et. al., 2002). A nova UML 2.0 tratou desses assuntos 
apresentando uma melhoria significativa em relação à primeira versão. No entanto, a nova 
versão limita-se à definição dos conceitos de Perfil UML e seus objetivos, não apresentando 
um guia detalhado sobre os passos para se construir um perfil. Selic (2007) acrescenta que há 
pouco material publicado para guiar os desenvolvedores de Perfis UML, resultando na 
existência de vários perfis tecnicamente inválidos uma vez que eles infringem o padrão UML 
de alguma forma (e consequentemente não podem ser suportados por ferramentas UML 
padrão). 
Com o intuito de orientar a construção de perfis UML, Fuentes e Vallecillo (2004) 
sugerem um conjunto de passos para a construção de perfis com base na UML 2.0, adotado 
por trabalhos como o de Machado (2006).  O guia possui cinco passos que podem ser 
nomeados da seguinte forma: Criação do Metamodelo de Domínio, Definição dos 
Estereótipos, Definição das Metaclasses, Definição dos Valores Etiquetados e Definição das 
Restrições; sendo que o primeiro passo refere-se ao levantamento dos elementos do domínio e 
os quatro últimos referem-se à construção do perfil UML propriamente dito. Nesta seção 
serão descritos cada um desses passos detalhadamente. Para elucidar cada um dos passos será 
usado o seguinte exemplo extraído do próprio trabalho de Fuentes e Vallecillo (2004): deseja-
se modelar as conexões entre os elementos de um sistema de informação que possui uma 
topologia em estrela (Figura 32) no qual existem nós que se conectam com nós centrais, que 


 
 
 
por sua vez podem se cone
tipos de nós: nós locais (
mesma estrela com seu nó 
caso conectem nós centrais
nó da mesma estrela deve c
 
• Passo 1 - Criação do M
 
Primeiramente é necess
ser definido pelo perfi
termos de metamodelo
definido 
utilizando
relacionamentos hierárq
fosse definir um perf
entidades do domínio,
estrutura e o comportam
para o exemplo da to
MainNode), um relacio
MainNode deriva da c
Edge) e um atributo loc
ctar entre si.  Neste domínio de aplicação pod
(Node) conectados por links (LocalEdge), c
central, ou nós remotos (MainNode) conect
s entre si. Cada nó é identificado por sua pos
compartilhar a mesma localização geográfica.
Figura 32 - Exemplo de Topologia em Estrela 
Metamodelo de Domínio 
sário definir o conjunto de elementos que com
il UML e o relacionamento entre eles, o q
(modelo para descrever outros modelos). Um
os 
mecanismos 
padrões 
oferecidos 
p
quicos, associações, etc.) de forma usual co
fil UML. No metamodelo deve-se adicion
, o relacionamento entre elas e as restriç
mento dessas entidades. A Figura 33 mostra o
opologia em estrela, que é composto de d
onamento de generalização entre as duas cl
classe Node), dois relacionamentos de asso
cation para a classe Node. 
75 
dem ser definidos dois 
caso conectem nós da 
tados por links (Edge), 
sição (location) e todo 
. 
 
mpreendem o sistema a 
que pode ser feito em 
m metamodelo pode ser 
pela 
UML 
(classes, 
omo se o objetivo não 
nar as definições das 
ções que controlam a 
o metamodelo definido 
duas classes (Node e 
asses (uma vez que a 
ociação (LocalEdge e 


76 
 
Figura
Adicionalmente, c
conjunto de restrições defin
exemplo a restrição é “tod
geográfica”.  
• 
Passo 2 - Definição do
 
Com a definição d
UML, sendo que a primei
UML estereotipado <<prof
do metamodelo que se des
elementos do metamodelo 
34 apresenta os estereótipo
correspondem às classes
(LocalEdge e Edge).  
Figura
 
a 33 - Exemplo de Metamodelo do Domínio (Passo 1)
 
como parte deste metamodelo, também é n
nidas para ele, que são as restrições passada
do nó da mesma estrela deve compartilhar 
 
s Estereótipos 
do metamodelo do domínio pode-se iniciar 
ira etapa é a identificação dos estereótipos. 
file>> deve-se incluir um estereótipo para ca
seja incluir no perfil. Estes estereótipos terã
para esclarecer a relação entre o perfil e o m
os identificados no metamodelo da Figura 33
(Node, MainNode) e dois que correspo
 
a 34 - Exemplo da Definição dos Estereótipos (Passo2)
) 
necessário expressar o 
as pelo domínio. Neste 
a mesma localização 
a construção do perfil 
Dentro de um pacote 
ada elemento relevante 
ão o mesmo nome dos 
metamodelo. A Figura 
: dois estereótipos que 
ndem às associações 
) 


 
 
 
• 
Passo 3 - Definição da
 
Após identificados
metamodelo da UML (met
tais elementos são as classe
forma, cada estereótipo de
metaclasse de UML que f
conceito ou relação. Na F
exemplo em questão: Class
Figura
 
• 
Passo 4 – Definição do
 
Os atributos que a
valores etiquetados no per
Deve-se incluir seus tipos e
33 é definido como um valo
s Metaclasses  
s os estereótipos, devem ser adicionados ao p
taclasses) que os estereótipos definidos irão 
es, associações, atributos, operações, transaçõ
eve estender, por meio da utilização do relac
foi utilizada no metamodelo do domínio pa
Figura 35 podem ser observadas as metacla
s e Association. 
 
a 35 - Exemplo da Definição das Metaclasses (Passo 3)
os Valores Etiquetados 
aparecem no metamodelo da aplicação deve
rfil UML, que são representados como atr
e valores iniciais. O atributo “location” da cl
or etiquetado na Figura 36. 
77 
perfil os elementos do 
estender. Exemplo de 
ões, pacotes, etc. Desta 
cionamento extends, a 
ara a definição de um 
asses identificadas no 
) 
em ser definidos como 
ributos do estereótipo. 
asse “Node” da Figura 


78 
 
Fig
 
• 
Passo 5 – Definição da
 
As restrições do perfil s
multiplicidades das asso
negócio da aplicação 
exemplo, é apresentad
aplicação (Figura 33
multiplicidades das ass
compartilhar a mesma l
<<MainNode>> cons
Context MainNode 
inv: self.localnodes -
inv: self.target -> forA
 
2.4. 
REDES DE PETR
 
As redes de Petr
possibilita uma representa
conceitos gerais sobre rede
na seção 2.4.2. A literatu
baseado em regras, sendo 
apresenta estudos já realiza
ura 36 - Exemplo da Definição de Valor Etiquetado 
as Restrições 
são obtidas das restrições do domínio da aplic
ociações que aparecem no metamodelo do do
são usadas para definir as restrições co
da uma restrição em OCL obtida da desc
) (mas existem outras restrições nesse
sociações LocalEdge e Edge): “todo nó da
localização geográfica”:  
straints 
-> forAll (n:Node | n.location = self.location) 
rAll (n:MainNode | n.location <> self.location) 
RI 
ri constituem uma técnica de especificaçã
ação gráfica e matemática de sistemas. Est
es de Petri na seção 2.4.1 e os tipos básicos qu
ura mostra que uma rede de Petri pode re
que esse tema é abordado na seção 2.4.3. P
ados que analisam a relação entre as redes de P
cação. Por exemplo, as 
omínio ou as regras de 
orrespondentes. Como 
crição do domínio da 
e exemplo como as 
a mesma estrela deve 
ão e modelagem que 
ta seção apresenta os 
ue elas podem assumir 
epresentar um sistema 
Por fim, a seção 2.4.4 
Petri e o PON. 


79 
 
 
 
2.4.1. Aspectos Gerais 
 
O modelo de rede de Petri foi proposto por Carl Petri para modelar a comunicação 
entre autômatos utilizados, na época, para representar sistemas a eventos discretos. A rede de 
Petri é uma ferramenta gráfica e matemática que se adapta bem a um grande número de 
aplicações nas quais as noções de eventos e de evoluções simultâneas são importantes. As 
redes de Petri possuem mecanismos de análise poderosos, que permitem a verificação de 
propriedades e da corretude do sistema especificado. Usando uma rede de Petri pode-se 
modelar sistemas paralelos, concorrentes, assíncronos e não-determinísticos (MACIEL et 
al.,1996).  
Os elementos básicos de uma rede de Petri são (CARDOSO e VALETTE, 1997): 
• Lugar: é representado por um círculo e pode ser interpretado como uma condição, um 
estado parcial, uma espera, um procedimento, um conjunto de recursos, um estoque, 
uma posição geográfica em um sistema de transporte, etc. Normalmente, todo lugar 
tem um predicado associado, como por exemplo, “controle remoto pressionado” na 
Figura 37. 
• Transição: é representada por uma barra ou retângulo, sendo associada a um evento 
ou ação que ocorre no sistema. Na Figura 37 a transição é representada pela transição 
t, que neste caso significa iniciar a operação. 
• Ficha ou marca: este último elemento é representado por um ponto dentro de um 
lugar. É um indicador significando que a condição associada ao lugar está válida. 
Pode representar um objeto (recurso ou peça) em certa posição geográfica, ou ainda, 
uma estrutura de dados que se manipula. O conjunto de fichas nos lugares da rede de 
Petri representa a situação atual, ou seja, em que condição encontra-se o sistema 
modelado. Por exemplo, uma ficha no lugar “controle remoto pressionado” da Figura 
37 indica que o controle remoto foi pressionado (predicado verdadeiro). Se não há 
fichas nesse lugar, o predicado é falso, portanto entende-se que o controle não está 
pressionado. 
 


80 
 
O estado do sistem
cada lugar representa um “
associada uma transição no
(que faz com que este passe
transição ao qual este está
transição é composto de do
1) Retirar as fichas do
verdadeiras após a o
2) Depositar as fichas
após a ocorrência do
 
Por exemplo, sup
associada à transição t (Fi
uma marca no lugar “contr
fechado”. A ocorrência do
transição t na rede de Petr
uma marca do lugar “portã
(Figura 37b). 
 
 
 
Figura 37 - Exemplo de Rede de Petri 
 
ma é dado pelas fichas nos lugares das rede
“estado parcial” do sistema. A cada evento qu
o modelo de redes de Petri. A ocorrência de 
e do estado atual ao próximo estado) é repres
á associado (CARDOSO & VALETTE, 199
ois passos: 
os lugares de entrada, indicando que as co
ocorrência do evento. 
em cada lugar de saída, indicando que as con
o evento. 
ondo que a ocorrência do um evento “inici
gura 37a), esta transição t só pode ocorrer 
role remoto pressionado” e (ao menos) uma m
o evento “iniciar a operação”, no sistema, e
ri: é retirada uma marca do lugar “controle r
ão fechado”, e é colocada uma marca no lu
 
es de Petri, sendo que 
ue ocorre no sistema é 
um evento no sistema 
entada pelo disparo da 
97). O disparo de uma 
ondições não são mais 
ndições estarão válidas 
iar a operação” esteja 
se houver (ao menos) 
marca no lugar “portão 
equivale ao disparo da 
remoto pressionado” e 
ugar “Portão Abrindo” 


81 
 
 
 
2.4.2. Tipos de Redes de Petri 
 
Um modelo básico de rede de Petri, também chamado de rede ordinária, é definido 
como uma quádrupla R = <P, T, Pre, Post> onde: 
• P é um conjunto finito de lugares de dimensão n; 
• T é um conjunto finito de transições de dimensão m; 
• Pre: P x T → N é a aplicação de entrada (lugares precedentes ou incidência anterior), 
com N sendo o conjunto dos números naturais; 
• Post: P x T → N é a aplicação de saída (lugares seguintes ou incidência posterior). 
A quádrupla R = <P, T, Pre, Post> com P = {p1,p2,p3}, T = {a,b,c,d} e os valores 
das aplicações de entrada e saída dados por: Pre (p2,c) = 3, Pre (p1,b) = Pre (p2,a) = Pre 
(p3,d) = 1, Post (p2,d) = 3 e Post (p1,a) = Post (p2, b) = Post (p3, c) = 1, é uma rede de Petri 
ilustrada pela Figura 38. 
 
Figura 38 - Exemplo de rede de Petri Ordinária (CARDOSO e VALETTE, 1997) 
 
A rede ordinária, constituída somente pela estrutura (lugares e transições) e 
marcação, modela somente a relação de causalidade entre as ações: o evento a da Figura 38 
acontece antes do evento b. Nas redes ordinárias apenas a estrutura é representada não se 
resolvendo os conflitos. Quando se deseja uma modelagem mais fiel é necessário adicionar 
condições suplementares de disparo, o que é possível por meio de outros tipos de rede de 
Petri: Redes Interpretadas, Redes de Alto Nível e Redes com representação do tempo. Na 
sequência são apresentadas cada uma dessas redes conforme descrito por Cardoso e Valette 
(1997). 
a) Redes Interpretadas: são associadas variáveis às transições da rede – representando 
condições e ações existentes no sistema. Tais variáveis podem indicar o estado de 
atuadores, sensores, etc., permitindo, deste modo, modelar a interpretação com o ambiente 
externo. Uma rede interpretada é uma rede não-autômata que introduz o tempo, a 


82 
 
interação com o ambiente ou dados contidos nas fichas. Uma rede ordinária é autômata, 
pois o disparo das transições depende apenas da estrutura da rede e de sua marcação. 
  
b) Redes de Alto Nível: há uma estruturação dos dados do sistema, diferenciando-se os 
dados globais dos dados locais. Por dados locais entende-se dados que só intervêm em 
certas condições ou ações, e que só são acessíveis em certos instantes. As redes de Alto 
Nível podem ser de três tipos – coloridas, predicado-transição e a objetos – que associam, 
de forma estruturada, uma parte dos dados às fichas. A seguir são descritas sucintamente 
cada uma dessas redes. 
 
― Rede de Petri Colorida: são associadas cores (números inteiros ou conjunto de 
etiquetas) às fichas com o objetivo de diferenciá-las. Como consequência, a cada 
lugar é associado o conjunto de cores das fichas que podem pertencer a este lugar. 
Igualmente, a cada transição se associa um conjunto de cores que corresponde às 
diferentes maneiras de disparar uma transição. Nos casos mais simples, quando 
todos os processos possuem a mesma estrutura e são independentes uns dos outros, 
as cores das transições são associadas diretamente aos processos, sendo que o 
conjunto de cores dos lugares e das transições é idêntico. 
 
― Rede de Petri Predicado-Transição: no caso da rede de Petri colorida, o poder de 
descrição é melhorado substituindo-se os inteiros da matriz de incidência de uma 
rede de Petri ordinária por funções. No caso das redes predicado-transição, as 
transições de uma rede de Petri ordinária são interpretadas como regras em um 
sistema de lógica proposicional (sem variáveis), e o poder de descrição é 
aumentado substituindo-se por regras da lógica de primeira ordem (regras com 
variáveis). Assim, não somente a representação é mais concisa, mas o modelo 
permite estudar melhor as propriedades estruturais e comportamentais do sistema. 
Uma regra (transição) descreve, portanto, um conjunto de eventos e não mais 
somente um evento. A família é definida pelo conjunto de possíveis substituições 
de variáveis por valores. Ao invés de regras do tipo: 
se uma peça pc1 e máquina M2, fazer usinagem; u12 
se uma peça pc2 e máquina M2, fazer usinagem; u22 
se uma peça pci e máquina Mj , fazer usinagem; uij 


83 
 
 
 
                tem-se regras do tipo: 
se uma peça <x> e uma máquina <y>, fazer usinagem <u>. 
 
Estas variáveis <x>, <y> e <u> assumirão, respectivamente, valores no conjunto de 
constantes {pci} descrevendo as peças em espera, o conjunto {Mj} das máquinas livres, e o 
conjunto {uij} das operações a serem realizadas. Estas constantes possuem um papel análogo 
ao das cores na rede colorida, mas são associadas variáveis aos arcos da rede de Petri 
predicado-transição ao invés de funções. 
 
― Rede de Petri a Objetos: este tipo de rede pode ser considerado como uma 
utilização da rede de Petri predicado-transição no contexto de uma abordagem a 
objetos. As fichas não são mais constantes, mas sim instâncias de n-uplas de 
classes de objetos. Além dos atributos definidos pela classe, um atributo implícito 
possui o nome do lugar em que o objeto se localiza. As operações são associadas 
às transições e correspondem às pré-condições (filtros) que operam sobre os 
atributos dos objetos situados nos lugares de entrada, e às condições que 
modificam estes valores. Uma operação associada a uma transição t só poderá ser 
executada por um objeto se este estiver localizado em um lugar de entrada de t. 
 
c) Redes com representação do tempo: as redes de Petri possibilitam descrever a 
causalidade (um evento é consequência de um outro), decisão e independência entre 
eventos: o evento a é causa do evento b, o evento a precede evento b, os eventos a e b são 
ordenados no tempo. Essa é uma maneira de descrever uma ordem parcial em um 
conjunto de eventos e de introduzir o tempo de modo quantitativo. Diversos trabalhos 
foram realizados no sentido de utilizar explicitamente o tempo, como um parâmetro 
contínuo e quantificável, seja para avaliação do desempenho, seja para a verificação 
formal. Existem duas grandes classes dessa interpretação: rede de Petri temporal e rede de 
Petri temporizada. 
 
― Rede de Petri Temporizada: neste tipo de rede associa-se um tempo θ às 
transições, ou ainda, aos lugares e arcos. Na sequência são descritos o tempo 
associado ao lugar e à transição.  


84 
 
o Tempo associado ao lugar: neste tipo de rede, se um lugar representa uma 
atividade A, então deve-se colocar θ como a duração dessa atividade. 
o Tempo associado à transição: esta rede é obtida associando-se a cada 
transição da rede ordinária uma duração de tiro. Sua semântica é uma 
noção de atraso durante a qual as fichas utilizadas para disparar a transição 
não ficam disponíveis ou visíveis em nenhum lugar. A partir do momento 
que a ficha se torna visível em um lugar, ela pode ser utilizada 
imediatamente por qualquer transição de saída desse lugar. Portanto, o 
disparo não é instantâneo e possui uma duração. Esta associação de tempo 
à transição somente tem sentido se a transição é interpretada como uma 
atividade e não como um evento instantâneo.  
 
― Rede de Petri Temporal: esta rede é obtida associando-se a cada transição uma 
duração de sensibilização. O disparo é instantâneo, no entanto, a transição deve 
estar sensibilizada durante o intervalo de tempo dado. A cada transição é associado 
um intervalo (θmin; θmax), sendo que, a duração de sensibilização deve ser maior 
que θmin e menor que θmax.  Diferente do modelo rede de Petri temporizada, durante 
a sensibilização de uma transição, as fichas continuam a ser “vistas” por outras 
transições de saída do lugar. 
 
2.4.3. Redes de Petri e sistemas de regras 
 
Pesquisas realizadas têm mostrado a adequabilidade do mapeamento entre regras e as 
redes de Petri, como Bako e Vallete (1990), Cardoso e Valette (1997), He et.al. (1999) e Ehrig 
(2008).  Dada a sua característica de fazer evoluir o estado a partir de regras representadas por 
transições, a rede de Petri pode ser igualmente considerada como um sistema de regras 
baseado em uma representação na forma: se condição então ação. Segundo Cardoso e Valette 
(1997) a correspondência entre as redes de Petri e os sistemas de regras é baseada nas 
seguintes correspondências:  
• O conjunto de transições da rede, com suas condições e ações, representadas pelos 
vetores Pre(.,t) e Post(.,t) constituem a base de regras. 
• A marcação inicial corresponde à base de fatos inicial, ou contexto inicial. 


85 
 
 
 
• O controle é dado pela estrutura da rede: se transições são paralelas, a ordem de 
disparo é indiferente; se as transições estão em conflito efetivo, apenas uma poderá ser 
disparada. 
Cardoso e Valette (1997) ressaltam que a vantagem da utilização da rede de Petri 
para representar um sistema de regras é devido ao seu formalismo que permite análise.  
 
2.4.4. Redes de Petri e o PON 
 
Em Simão (2005), é apresentada a compatibilidade entre o metamodelo para controle 
discreto (que originou o PON) e as redes de Petri. A Figura 39 ilustra um fragmento de uma 
rede de Petri usada para simular os elementos colaboradores de um controle de manufatura. 
Nesta figura, cada regra é interpretada como uma transição, as condições e ações da regra são 
representados pelos arcos, e os estados dos atributos de um elemento são representados por 
lugares na rede.  
Os diferentes estados de um atributo geram mais de um lugar na rede formando um 
conjunto de lugares para um mesmo atributo. Esses lugares são delimitados por retângulos na 
rede de Petri, sendo que a marcação de um lugar representa o estado de um Attribute. 
Portanto, na mudança do estado de um Attribute (mudanças das fichas), as Rules relacionadas 
(transições) são notificadas pelas Premises (arcos). Depois que uma Rule (transição) é 
disparada, os Instigation realizam, por meio dos Methods, mudanças nos estados de alguns 
Attributes gerando outras sensibilizações na rede. 


86 
 
 
Figura 39 - Redes de Petri de um Controle (SIMÃO, 2005) 
 
2.5. 
CONSIDERAÇÕES SOBRE A FUNDAMENTAÇÃO TEÓRICA 
 
Este capítulo apresentou os conceitos fundamentais utilizados para estruturar esta 
dissertação. A seção 2.1 introduziu o Paradigma Orientado a Notificações e seus principais 
conceitos. Foi apresentado o mecanismo de notificações do PON juntamente com detalhes de 
sua implementação (framework). Observou-se que o framework é composto por dois pacotes: 
Core e Application, sendo que o primeiro contém a implementação dos elementos 
participantes do mecanismo de notificação do PON, e o segundo contém os elementos que 
oferecem o ponto de extensão entre uma nova aplicação e o pacote Core, além da 
implementação das estratégias de resolução de conflito das regras. O mecanismo de 
funcionamento do PON e os detalhes da sua implementação são essenciais para fundamentar 
os resultados obtidos nos capítulos 0 e 0.  
A seção 2.2 apresentou o RUP e seus principais conceitos. O RUP será útil para o 
método a ser proposto para o PON, uma vez que o objetivo dessa dissertação não é criar um 
novo processo de software, e sim, aproveitar um processo já existente adaptando-o conforme 
o necessário para as necessidades específicas do PON. A escolha do RUP fez-se porque o 
RUP é um processo bastante utilizado atualmente além de utilizar a UML para criação de seus 


87 
 
 
 
modelos.  O uso da UML é natural na modelagem para PON, uma vez que este é baseado na 
Orientação a Objetos. Analisando mais especificamente como se encaixa o RUP nessa 
dissertação, será necessário realizar adaptações, mais especificamente, na disciplina de 
Análise e Projeto, a fim de suprir as características intrínsecas do PON, o que naturalmente 
vai adaptar a UML para realizar a modelagem de regras.  
Por sua vez, a seção 2.3 apresentou conceitos relevantes da UML a serem aplicados 
nos resultados dessa dissertação. A UML é naturalmente aplicada na disciplina de Análise e 
Projeto do RUP, como apresentado na seção 2.2, na construção de modelos que expressam o 
sistema a ser desenvolvido.  Embora a UML contemple boa parte das necessidades de 
modelagem, ela não consegue atender a todas. Para tais casos, como foi apresentado, a UML 
pode ser adaptada ou estendida a fim de satisfazer domínios específicos de aplicação. Uma 
vez que o PON possui um framework particular, será necessário utilizar os conceitos da UML 
juntamente com seus mecanismos de extensão a fim de personalizar o metamodelo da UML 
para o PON. A partir de um perfil UML para o PON, será possível melhor adequar a UML 
para a modelagem de sistemas neste novo paradigma de programação. 
Por fim, a seção 2.4 apresentou conceitos sobre as redes de Petri e seus tipos 
principais a fim de estudar sua aplicabilidade ao PON. As redes de Petri constituem uma 
técnica de especificação ou modelagem que possibilita uma representação gráfica e 
matemática de sistemas, permitindo a análise e simulação desses sistemas. Além disso, 
pesquisas realizadas têm mostrado a adequabilidade do mapeamento entre regras e as redes de 
Petri, o que é favorável ao PON uma vez que este tem inspiração nos Sistemas Baseados em 
Regras. Simão (2005), em seu trabalho, apresenta a compatibilidade entre o metamodelo para 
controle discreto (que originou o PON) e as redes de Petri, a qual pode ser utilizada ou 
adaptada para a modelagem de sistemas neste novo paradigma de programação. 
 
 


88 
 
 
 


 
 
 
3. VISÃO GERAL DO
PON 
 
O capítulo 2 intro
projetos de software que u
proposto foi desenvolvido 
Petri, além do próprio PON
perfil UML desenvolvido. 
resultados. 
 
3.1. 
VISÃO GERAL D
 
O método propost
– e será empregado em proj
com as práticas atuais de 
modelagem orientadas ao
programação.  
O método DON fo
denominado NOP Profile
suprir as necessidades espe
criação do método DON qu
de passos para a construçã
criação do método uma vez
essas etapas.  
Figura 40 -
O MÉTODO PROPOSTO E PERFI
oduziu os conceitos que fundamentam a pro
utilizam o Paradigma Orientado a Notificaçõ
utilizando os conceitos de RUP, UML, Pe
N. Neste capítulo 0 é apresentada uma visão
O capítulo 0 apresenta, por sua vez, o mé
DO MÉTODO PROPOSTO 
to denomina-se DON – Desenvolvimento Or
ojetos de software baseados em PON. O Méto
engenharia de software, porém apresenta té
o desenvolvimento de softwares nesse 
oi desenvolvido a partir de duas etapas: (1) a c
(Perfil PON), que especializa o metamode
ecíficas do PON e melhor adequar sua modela
ue faz uso do perfil UML desenvolvido e apr
ão de projetos em PON. A etapa de criação 
z que o perfil especifica os elementos do PO
Etapas para a Construção do Método para Projetos em
 
89 
IL UML PARA O 
oposta do método para 
ões (PON). O método 
erfil UML e Redes de 
o geral do método e o 
étodo proposto e seus 
ientado a Notificações 
odo DON é compatível 
écnicas específicas de 
novo paradigma de 
criação do perfil UML 
elo da UML a fim de 
agem em UML, e (2) a 
resenta uma sequência 
do perfil antecedeu a 
ON. A Figura 40 ilustra 
 
m PON 


90 
 
A Figura 41 cont
arquitetura MOF de quatro
UML para satisfazer as nec
base no novo perfil e no m
DON para criar modelos U
F
 
3.2. 
PERFIL UML PA
 
O perfil UML pa
método de criação de perfis
reconhecidos pela OMG, c
UML Profile for Schedulab
essas fontes concordam q
artefatos: o modelo do do
modelo do domínio descrev
criação do perfil UML, 
restrições. Uma vez identifi
e Vallecillo (2004) sugere
criação de um perfil: Defin
textualiza onde o NOP Profile e o método
o camadas da OMG. O NOP Profile especia
cessidades particulares do PON e encontra-se
metamodelo da UML já existente, será poss
ML, na camada M1, da aplicação a ser mode
Figura 41 - Arquitetura MOF de quatro camadas 
RA O PON 
ara o PON, denominado NOP Profile, foi e
s UML proposto por Fuentes e Vallecillo (20
como o UML Profile for CORBA Componen
bility, Performance, and Time Specification (
que a construção de um perfil UML envol
omínio (ou metamodelo) e o perfil UML 
ve o framework do domínio da aplicação qu
permitindo identificar seus estereótipos, v
ficado o modelo do domínio, é possível criar 
em, após a criação do modelo do domínio, 
nição dos Estereótipos, Definição das Metac
o DON se aplicam na 
aliza o metamodelo da 
e na camada M2. Com 
sível utilizar o método 
lada em PON. 
 
elaborado baseado no 
004) e nos perfis UML 
nts (OMG, 2005a) e o 
(OMG, 2005b). Todas 
lve a criação de dois 
propriamente dito. O 
ue serve de base para a 
valores etiquetados e 
o perfil UML. Fuentes 
quatro passos para a 
classes, Definição dos 


 
 
 
Valores Etiquetados e Defi
perfil após a execução dess
O modelo do dom
serem apresentados no c
modelagem Enterprise Arc
completa e que provê um 
criados graficamente e pod
XML, o perfil pode ser imp
perfil podem ser usados n
software, como Raphsody
características técnicas leva
A seção 3.2.1 apr
perfil UML obtido. 
 
3.2.1. Descrição do Mode
 
A identificação do
de desenvolvimento de um
usando-se os elementos de
caso, os conceitos do dom
para capturar as propriedad
representados por associaç
foi elaborado utilizando-se
pacotes de classes do fram
(Figura 42). 
 
finição das Restrições. Este capítulo apresent
sas etapas. 
mínio e perfil UML do PON, assim como o
capítulo 0, foram desenvolvidos utilizando
hitect 7.0 (EA) (SPARX, 2011). A EA é uma
mecanismo genérico para criação de perfis
dem ser exportados no formato XML. Uma 
portado dentro de um projeto de software do 
nos diagramas do sistema a ser modelado. O
da IBM, também poderiam ser utilizadas. 
aram à escolha do EA neste trabalho. 
esenta o modelo do domínio do PON e a se
elo do Domínio 
os conceitos do domínio da aplicação é o está
m perfil. Um modelo conceitual do domínio
e modelagem da UML como classes, pacotes
mínio são representados pelas classes e os at
des desses conceitos, sendo que as relações 
ções. No âmbito desta dissertação, o modelo
e o diagrama de classes da UML, sendo
mework do PON apresentados na seção 2.1
Figura 42 - Modelo do Domínio do PON 
91 
ta o resultado final do 
os modelos do DON a 
o-se a ferramenta de 
a ferramenta de projeto 
s UML. Os perfis são 
vez salvo no formato 
EA e os elementos do 
Outras ferramentas de 
O baixo custo e boas 
eção 3.2.2 apresenta o 
gio inicial do processo 
o pode ser construído 
s e associações. Neste 
tributos são utilizados 
entre os conceitos são 
o do domínio do perfil 
composto pelos dois 
.3: core e application 
 


92 
 
Por meio desses diagramas foi possível identificar o significado e o uso dos 
elementos, relações e restrições do PON. Nesta seção os diagramas de classes são 
apresentados de maneira resumida, contendo os elementos relevantes para a criação do perfil. 
Entende-se por elementos relevantes as classes, atributos e métodos que fazem a interface do 
framework do PON para o programador. Não são considerados aqui aqueles elementos que 
fazem parte do framework, mas que são transparentes ao programador. O objetivo é 
identificar e expressar, por meio do perfil UML, os elementos que serão utilizados pelo 
projetista e programador em PON.  
A Figura 43 mostra o Diagrama de Classes do pacote Core do framework, que possui 
as classes responsáveis por modelar os objetos participantes do mecanismo de notificações. 
Este diagrama consolida todas as perspectivas do diagrama de classe do pacote Core, 
apresentadas 
na 
seção 
2.1.3, 
em 
um 
só 
diagrama. 


 
 
 
Figura 43 - Modelo do domínio - pacote Core 
93 
 


94 
 
Por sua vez, a Fi
permite a utilização do fram
classe Application que faz 
resolução de conflitos das r
Fi
 
Em ambos os dia
PON, as relações entre sua
entidades e seus relacionam
do Perfil PON (as descriçõ
abordadas na seção 2.1.3).
 
3.2.2. NOP Profile (Perfi
 
Com a identificaçã
do perfil UML.  No esco
denominado Perfil PON (N
(Figura 45) e os especializa
igura 44 exibe o diagrama de classes do pa
mework do PON pelo programador. Nesse di
a interface com o pacote Core, e a classe Sch
regras.  
gura 44 - Modelo do domínio - pacote Application 
agramas pode-se observar as definições das 
as entidades, assim como suas restrições que
mentos. São esses os elementos que serão uti
ões detalhadas sobre cada uma das classes de
l PON) 
ão dos modelos do domínio do PON, o próxi
opo dessa dissertação, foi criado um perfi
NOP Profile), que importa os conceitos do 
a a fim de definir os principais conceitos do fr
acote Application que 
iagrama destacam-se a 
heduler que promove a 
 
entidades próprias do 
e limitam o uso dessas 
ilizados para a criação 
esses diagramas foram 
mo passo foi a criação 
il UML para o PON 
metamodelo da UML 
ramework do PON.   
 


 
 
 
Figura 45 - R
O Perfil PON é 
compreende outros dois pa
cada um dos modelos de do
para acompanhar a língua 
Profile Core é composto p
perfil NOP Profile é repres
o mesmo ocorre com cada u
ilustra a composição do NO
 
O NOP Profile é d
• Sintaxe abstrata: é 
consistindo de um d
em linguagem natu
classes UML mo
relacionamentos.  
• Semântica: é descri
alguma notação adic
O formato da des
CORBA Components (OM
Relação de importação o metamodelo da UML e o Perf
 
composto por um pacote UML denomina
acotes – NOP Profile Application e NOP Pr
omínio do framework do PON (os nomes do
na qual foi desenvolvido o framework do P
por outros dois pacotes: Core Elements e C
sentado por um pacote UML estereotipado <
um dos outros pacotes que compõem o perfil
OP Profile. 
Figura 46 - Composição do NOP Profile 
descrito utilizando-se duas visões descritas em
obtida como um modelo descrito em um s
diagrama de classes da UML e, adicionalme
ural (linguagem portuguesa). É apresentada
strando as metaclasses e definindo os 
ita primeiramente por uso da linguagem natu
cional, dependendo da parte do modelo sendo
scrição do perfil foi baseado no documento
MG, 2005a). O Perfil PON especifica um c
95 
fil PON 
ado NOP Profile que 
rofile Core – um para 
o perfil estão em inglês 
PON). O pacote NOP 
Core Relationships. O 
<<profile>>, sendo que 
l do PON. A Figura 46 
 
m OMG (2003): 
subconjunto da UML, 
ente, de uma descrição 
a em um diagrama de 
estereótipos e seus 
ural, mas pode incluir 
o descrito. 
o do UML Profile for 
conjunto de extensões 


96 
 
UML consistindo de estereótipos, valores etiquetados e restrições. O estereótipo é o 
mecanismo de extensão mais relevante provendo uma direção para classificar os elementos do 
PON. A especificação dos estereótipos e dos valores etiquetados é realizada de duas formas 
nesta dissertação: gráfica e tabular. A representação gráfica, que representa a sintaxe abstrata 
do NOP Profile, é realizada por meio da utilização de diagramas de classes da UML e possui 
as seguintes definições: 
• Cada estereótipo é representado por uma caixa classificadora com o estereótipo 
<<stereotype>>. 
• Cada valor etiquetado é representado como um atributo do estereótipo. 
• Cada estereótipo é um cliente dentro de um relacionamento de dependência da UML 
com a metaclasse da UML que ele estende. Essas dependências são estereotipadas 
com <<extends>>. 
• Relacionamentos de generalização entre estereótipos são expressos pela maneira 
padrão da UML, ou seja, pelo relacionamento de generalização. 
 
Por sua vez, a representação tabular dos estereótipos também expressa a sintaxe 
abstrata do perfil pela descrição dos elementos em linguagem natural, além de descrever a sua 
semântica. As colunas da representação tabular são basicamente definidas da seguinte 
maneira: 
• Estereótipo: o nome do estereótipo. 
• Classe UML Base: o elemento do metamodelo da UML que serve de base para o 
estereótipo. 
• Generalização: o elemento de generalização do estereótipo em definição, caso exista.  
• Valores Etiquetados: uma lista de todos os valores etiquetados que podem estar 
associados com o estereótipo. 
• Descrição: uma descrição informal com possíveis comentários explanatórios. 
• Restrições: descrição das restrições em texto português. 
• Semântica: descrição da semântica do estereótipo. 
 
Na representação tabular dos valores etiquetados, as colunas são definidas como: 
• Valor Etiquetado: o nome do valor etiquetado. 
• Estereótipo: o nome do estereótipo que pode estar associado com o valor etiquetado. 
• Tipo: o nome do tipo dos valores que podem estar associados ao valor etiquetado. 


97 
 
 
 
• Valor Inicial: o valor inicial que o valor etiquetado possui, se possuir. 
• Descrição: descrição informal com possíveis comentários explanatórios. 
 
No caso em que os elementos das colunas não são especificados para um 
determinado estereótipo ou valor etiquetado, o campo é preenchido com o símbolo “NA”. As 
seções seguintes apresentam os resultados dos perfis UML obtidos – “NOP Profile Core” e 
“NOP Profile Application” – aplicando-se o método de criação de perfis descrito por Fuentes 
e Vallecillo (2004) e baseando-se nas documentações da OMG.  
 
3.2.2.1. 
NOP Profile - Core 
 
O pacote NOP Profile – Core é composto por elementos de extensão da UML 
(estereótipos, valores etiquetados e restrições) que representam e descrevem os objetos 
participantes do mecanismo de notificações do PON. Esses elementos de extensão foram 
obtidos a partir da análise do modelo do domínio da Figura 43 (diagrama de classes do 
framework core). Em um primeiro passo, acompanhando a proposta de Fuentes e Vallecillo 
(2004), foi criado um estereótipo para cada elemento relevante definido no modelo do 
domínio e, em um segundo momento, foram associados esses estereótipos aos elementos do 
metamodelo da UML por meio do relacionamento de extensão (<<extends>>). A fim de 
facilitar o entendimento e visualização do pacote NOP Profile – Core, ele é composto por 
dois pacotes principais:  
• Core-Elements: define estereótipos referentes aos elementos que compõem os FBEs e 
aos elementos participantes do mecanismo de notificações do PON. É composto por 
três outros pacotes: Core-Class, Core-Object e Core-Component. 
• Core-Relationships: define estereótipos de relacionamentos e de mensagens aplicáveis 
entre os estereótipos do Core-Elements. É composto por outros quatro pacotes: Core-
Assembly, Core-Association, Core-Sequence e Core-Collaboration. 
 
3.2.2.1.1. Pacote Core Elements 
 
Antes de apresentar os estereótipos criados nestes pacotes é importante recapitular 
alguns conceitos do PON. Como mencionado na seção 2.1.3, a classe FBE representa os 
elementos da base de fato e a classe Rule gerencia o conhecimento causal sobre qualquer 


98 
 
comportamento do sistema, representando as expressões-causais desse sistema. Essas classes 
se relacionam por meio de seus objetos colaboradores – Attribute, Premise, Condition, Action, 
Instigation e Method – sendo que a colaboração entre esses objetos determina o fluxo de 
execução da aplicação. Como ressaltado na seção 2.1.3.2, quando o programador cria um 
novo programa em PON, os elementos Rule e os elementos colaboradores - Premise, 
Condition, Action, Instigation - são expressos somente como instâncias das respectivas 
classes no framework, ou seja, o programador não cria classes para esses elementos, apenas 
objetos. As regras de um sistema em PON são definidas como instâncias da classe Rule do 
framework no escopo do método initRules. O mesmo ocorre com os elementos Premise, 
Condition, Instigation e Action, só que esses têm suas instâncias criadas automaticamente 
pelo framework na criação de uma regra (mas caso o programador deseje, eles também podem 
ser instanciados manualmente). 
Já os novos elementos FBEs são criados pelo programador como uma subclasse 
FBE, adicionando, assim, um novo elemento de dados à base de fatos, que posteriormente 
serão instanciados.  Ao criar um novo FBE, o programador também define seus métodos e 
atributos como sendo dos tipos das classes Method e Attribute do framework do PON. Os 
Methods e Atributes de um FBE entram na cadeia de notificação do PON quando adicionados 
às premissas e instigações das Rules. Portanto, os Methods e Attributes são métodos e 
atributos do ponto de vista de um FBE, mas também são objetos do ponto de vista do 
mecanismo de notificação do PON. 
Recapitulados esses conceitos do PON, são apresentados na sequência os 
estereótipos criados no pacote NOP Profile – Core Elements. Este pacote é divido em outros 
três pacotes:  
• Core-Class: possui estereótipos referentes às classes responsáveis por compor a 
estrutura dos elementos FBEs. Estes estereótipos são utilizados para criar diagramas 
de classes da aplicação. 
• Core-Object: possui os estereótipos referentes às classes responsáveis por modelar os 
objetos participantes do mecanismo de notificações do PON. Estes estereótipos são 
utilizados para criar diagramas de objetos, sequência e comunicação. 
• Core-Component: possui os mesmos estereótipos do pacote Core-Object, ou seja, 
possui estereótipos que representam os objetos participantes do mecanismo de 
notificações do PON. No entanto, esses estereótipos representam componentes da 
UML, a fim de serem aplicados em diagramas de componentes. 


 
 
 
A representação gr
nos seus três pacotes: Clas
estereótipos que estendem 
será apresentada apenas um
mesmo quando pertinente.
 
3.2.2.1.1.1. 
Pacote Core
 
O pacote Core-C
compor a estrutura dos el
<<NOP_FBE>> que esten
definido pelo programad
Adicionalmente, como uma
os estereótipos <<NOP_A
Attribute e Operation, 
<<NOP_MethodPointer>>
derivadas 
da 
classe 
M
<<NOP_Method>>. A F
utilizados para modelar dia
 
O pacote Core-O
responsáveis por modelar 
ráfica dos pacotes é realizada subdividindo o 
ss, Object e Component. Esses pacotes com
diferentes metaclasses nos diferentes pacotes
ma tabela por estereótipo que descreve as dife
e Elements - Representação Gráfica 
Class possui estereótipos referentes às clas
lementos FBEs. Para o elemento FBE foi c
nde a metaclasse Class, uma vez que um
or representa uma subclasse da classe 
a subclasse FBE é composta por métodos e at
Atribute>> e <<NOP_Method>> que este
respectivamente. Também foram criad
> e <<NOP_MethodDerived>> para rep
Method 
e, 
portanto, 
são 
especializaç
Figura 47 ilustra o pacote Core-Class. E
agramas de classes de aplicações em PON. 
Figura 47 - NOP Profile – Core-Class 
Object, por sua vez, possui os estereótipos 
os objetos participantes do mecanismo de 
99 
pacote Core Elements 
mpartilham os mesmos 
s. Na descrição tabular 
erentes perspectivas do 
sses responsáveis por 
criado um estereótipo 
m novo elemento FBE 
FBE do framework. 
tributos, foram criados 
endem as metaclasses 
dos os estereótipos 
presentar as classes 
ões 
do 
estereótipo 
Estes estereótipos são 
 
referentes às classes 
notificações do PON. 


100 
 
Portanto, para cada elemento do mecanismo de notificações do PON – Rule, Attribute, 
Premise, Condition, Action, Instigation e Method – foram criados estereótipos – 
<<NOP_Rule>>,<<NOP_Attribute>>, 
<<NOP_Premise>>, 
<<NOP_Condition>>, 
<<NOP_Action>>, <<NOP_Instigation>> e <<NOP_Method>>  respectivamente – que 
estendem a metaclasse Object, uma vez que todos esses elementos, quando criada uma 
aplicação em PON, representam instâncias das classes correspondentes do framework do 
PON.  
Apesar do FBE também fazer parte do mecanismo de notificações do PON por meio 
de seus estereótipos <<NOP_Method>> e <<NOP_Attribute>>, ele não foi definido no pacote 
Core-Object porque ele já faz parte do pacote Core-Class. Ou seja, uma vez definida uma 
classe 
<<NOP_FBE>> 
no 
modelo, 
poderão, 
então, 
serem 
instanciados 
objetos 
<<NOP_FBE>>. 
Também foram criados um estereótipo <<NOP_SubCondition>> que estende a 
mesma metaclasse de seu pai, <<NOP_Condition>>, e representa o elemento SubCondition 
do PON. Os estereótipos <<NOP_MethodPointer>> e <<NOP_MethodDerived>> também 
foram adicionados neste pacote e estendem o estereótipo <<NOP_Method>>. A Figura 48 
ilustra o pacote Core-Object desenvolvido. Estes estereótipos podem ser aplicados em 
diagramas de objeto, sequência e comunicação.  


 
 
 
 
Além desses este
definem propriedades aos
etiquetado é representado c
valores etiquetados criado
Core, que são três: Logica
enumerações. 
 
Enumeração 
Descriç
LogicalOperator 
Define 
valores 
Conjun
AttributeType 
Define 
Figura 48 - NOP Profile – Core-Object  
ereótipos, foram adicionados valores etiqu
s estereótipos criados. Como comentado 
como um atributo de um estereótipo no perfil
os, primeiro são apresentadas as enumeraçõ
alOperator, AttributeType e Operator. A Ta
Tabela 1 - Enumerações do NOP Profile - Core 
ção 
os tipos que um operador lógico pode assum
possíveis são: Single (não é definido o
ction (Conjunção) e Disjunction (Disjunção). 
os tipos primitivos existentes em PON, que são
101 
 
etados ao perfil, que 
em 2.3.3, um valor 
l. A fim de explicar os 
ões criadas no pacote 
abela 1 descreve essas 
mir em PON. Os 
operador lógico), 
o: Boolean_NOP, 


102 
 
Char_NOP, Double_NOP, Integer_NOP e String_NOP. 
Operator 
Define os operadores de comparação possíveis em PON, que são: 
EQUAL, 
DIFFERENT, 
GREATERTHAN, 
SMALLERTHAN, 
GREATEROREQUAL, SMALLEROREQUAL. 
 
Os valores etiquetados definidos no pacote Core são apresentados na Tabela 2.  
 
Tabela 2 - Valores etiquetados do NOP Profile - Core 
Valor 
Etiquetado 
Estereótipo 
Tipo 
Valor 
Inicial 
Descrição 
renotify 
NOP_Attribute 
booleano 
false 
Define 
se 
um 
objeto 
Attribute deve utilizar a re-
notificação. 
attributeType 
NOP_Attribute 
AttributeType 
NA 
Define o tipo do atributo de 
um objeto NOP_Attribute. 
exclusive 
NOP_Premise 
booleano 
false 
Define 
se 
um 
objeto 
Premise é exclusivo ou 
não. 
attribute 
NOP_Premise 
Attribute* 
NA 
Guarda referência a um 
objeto 
Attribute, 
que 
notifica o objeto Premise 
quando ocorre mudança em 
seu estado. 
operator 
NOP_Premise 
Operator 
NA 
Operador lógico usado para 
fazer comparações entre os 
valores attribute e  value. 
value 
NOP_Premise 
Attribute* 
NA 
Pode ser uma constante ou 
uma referência para outro 
objeto 
Attribute. 
É 
comparado aos valores de 
attribute. 
logicalOperator 
NOP_Condition 
logicalOperator 
NA 
Define o operador lógico 
de 
um 
objeto 
NOP_Condition. 
isDerived 
NOP_Rule 
booleano 
false 
Define se uma Rule é 
Derived. 


103 
 
 
 
attribute 
NOP_Instigation 
Attribute* 
NA 
Guarda referência a um 
objeto 
Attribute 
a 
ser 
modificado 
por 
um 
Instigation. 
value 
NOP_Instigation 
Attribute* 
NA 
Pode ser uma constante ou 
uma referência para outro 
objeto Attribute. É o valor 
atribuído a um Attribute a 
fim de alterar seu valor, 
após a notificação de um 
Instigation. No perfil, é o 
valor atribuído ao valor 
etiquetado attribute. 
method 
NOP_Instigation 
Method* 
NA 
Guarda referência a um 
objeto 
Method 
a 
ser 
executado 
por 
um 
Instigation. 
 
O pacote Core-Component, por sua vez, possui os mesmos estereótipos do pacote 
Core-Object que representam os objetos participantes do mecanismo de notificações do PON. 
No entanto, esses estereótipos estendem a metaclasse Component, a fim de serem aplicados 
em diagramas de componentes (representação esta a ser explicada no método DON). A Figura 
49 ilustra o pacote Core-Component. Adicionalmente, o estereótipo <<NOP_FBE>> do 
pacote Core-Class também estende a metaclasse Componet para representar elementos FBEs 
nos diagramas de componentes. 
 


104 
 
 
3.2.2.1.1.2. 
Pacote Core
 
As tabelas a segui
todo, detalhadamente. Ess
descritas nas Tabela 1 e Tab
Estereótipo 
Class
<<NOP_FBE>> 
Class
Descrição 
Representa os elem
virtual) de um problema com
por meio de seus atributos e m
Restrições 
• 
Uma classe <<NOP_FBE
• 
Uma classe <<NOP_FBE
• 
Um <<NOP_ FBE>> pod
• 
Um <<NOP_ FBE>> pod
Semântica 
Figura 49 - NOP Profile – Core-Component 
e Elements - Representação Tabular 
ir apresentam cada um dos estereótipos do p
sas tabelas fazem uso dos valores etique
bela 2. 
 
Tabela 3 - Estereótipo NOP_FBE 
se UML Base 
Generalização 
Valo
s, Component 
NA 
NA
mentos da base de fatos, como as entidades do 
mputacional, e descreve os estados e os serviços 
métodos.  
E>> é composta por <<NOP_Attribute>> e <<NO
E>> pode pertencer a uma classe <<NOP_Applica
de associar-se a um ou mais <<NOP_Attribut
de associar-se a vários <<NOP_Method>>. 
 
pacote Core, como um 
etados e enumerações 
ores Etiquetados 
mundo (real ou 
dessas entidades 
OP_Method>>. 
ation>>. 
te>>. 


105 
 
 
 
O estereótipo <<NOP_FBE>> é referente à classe FBE do framework do PON e 
estende a metaclasse Class da UML, uma vez que um novo elemento FBE definido pelo 
programador representa uma subclasse da classe FBE, que posteriormente será instanciada. 
Uma classe estereotipada <<NOP_FBE>> pode ser composta por vários métodos e atributos 
estereotipados <<NOP_Attributes>> e <<NOP_Methods>>.  
Este estereótipo também estende a metaclasse Component a fim de permitir sua 
representação como um componente. 
 
Tabela 4- Estereótipo NOP_Rule 
Estereótipo 
Classe UML Base 
Generalização 
Valores Etiquetados 
<<NOP_Rule>> 
Object, Component 
NA 
isDerived 
Descrição 
Gerencia o conhecimento causal sobre qualquer comportamento do sistema, 
representando as expressões causais desse sistema.  
Restrições 
• 
Um objeto <<NOP_Rule>> somente pode se associar com objetos estereotipados 
<<NOP_Condition>> e <<NOP_Action>>, que fazem parte da sua estrutura. 
• 
Um objeto <<NOP_Rule>> pode receber notificação de um objeto estereotipado 
<<NOP_Condition>>. 
• 
Um objeto <<NOP_Rule>> pode notificar um objeto estereotipado <<NOP_Action>>. 
• 
Um objeto <<NOP_Rule>> deve possuir um valor etiquetado isDerived definido, que por 
default é falso. Quando omitido do diagrama, significa que é falso. 
Semântica  
O estereótipo <<NOP_Rule>> é referente à classe Rule do framework e estende a 
metaclasse Object da UML, uma vez que representa um objeto no mecanismo de notificações 
do PON. Um objeto estereotipado <<NOP_Rule>> é composto por um objeto 
<<NOP_Condition>> e um objeto <<NOP_Action>>, que trabalham juntos para realizar o 
conhecimento causal da regra. O objeto <<NOP_Condition>> se preocupa com a parte de 
decisão relacionada com os objetos FBE, ao passo que o objeto <<NOP_Action>> 
responsabiliza-se com a execução dos métodos desses objetos.  
No framework do PON a classe Rule possui duas classes derivadas: RuleObject e 
RuleDerived. A RuleObject permite estruturar uma regra na sua forma completa, com 
Condition e Action. Já a RuleDerived perrmite implementar o conteúdo de execução (Action) 
da Rule diretamente em seu corpo, por meio do método invocado em sua execução, que é o 
execute(). Nesta, a ação da Rule é implementada com toda a flexibilidade do PP ou POO, 
permitindo atribuições de valores e chamadas de métodos implementados de forma imperativa. 


106 
 
Geralmente uma instância da Rule é do tipo RuleObject, informação esta representada 
pelo valor etiquetado isDerived configurado para falso. Caso a regra seja do tipo RuleDerived, 
esse valor etiquetado deve ser verdadeiro.  
Este estereótipo também estende a metaclasse Component a fim de permitir sua 
representação como um componente. 
 
Tabela 5 - Estereótipo NOP_Attribute 
Estereótipo 
Classe Base 
Generalização 
Valores Etiquetados 
<<NOP_Attribute>> 
Object, 
Attribute, 
Component 
NA 
renotify, attributeType 
Descrição 
Representa os atributos de um FBE. É responsável por reagir a mudanças no seu 
estado notificando os objetos estereotipados <<NOP_Premise>> aos quais ele está associado, 
a fim de iniciar uma cadeia de notificações.  
Restrições 
• 
Um estereótipo <<NOP_Attribute>>  só pode relacionar-se com objetos de estereótipos: 
a. <<NOP_FBE>> – para fazer parte da estrutura do FBE 
b. <<NOP_Premise>> – para notificar alteração de seu estado 
c. <<NOP_Method>> e <<NOP_Instigation>> – para ter seu valor alterado. 
• 
Um objeto <<NOP_Attribute>>  pode pertencer a um objeto <<NOP_FBE>>. 
• 
Um objeto <<NOP_Attribute>>  pode notificar um ou mais objetos <<NOP_Premise>>. 
• 
Um objeto <<NOP_Attribute>>  pode ter seu estado mudado por um ou mais objetos 
<<NOP_Method>>. 
• 
Um objeto <<NOP_Attribute>>  pode ter seu estado mudado por um ou mais objetos 
<<NOP_Instigation>>. 
• 
Um objeto <<NOP_Rule>> deve possuir um valor etiquetado renotify definido, que por 
default é falso. Quando omitido do diagrama, significa que é falso. 
• 
Quando estender um Object ou Component, um <<NOP_Rule>> deve possuir um valor 
etiquetado attributeType definido. 
Semântica  
O estereótipo <<NOP_Attribute>> refere-se à classe Attribute do framework e 
estende as metaclasses Attribute e Object da UML. O objeto Attribute faz parte da composição 
de um objeto FBE. Ao criar um novo FBE, o programador define os atributos desse FBE como 
sendo do tipo da classe Attribute do framework. Uma vez instanciado o FBE e os seus 
Attributes adicionados às premissas e instigações das regras, os Attributes entram na cadeia de 
notificação do PON. Portanto, os Attributes são atributos do ponto de vista de um FBE e, por 


107 
 
 
 
isso, estendem a metaclasse Attribute, mas também são objetos do ponto de vista do 
mecanismo de notificação do PON e, por isso, também estendem a metaclasse Object. O valor 
etiquetado attributeType define o tipo de um objeto Attribute, que pode assumir um dos valores 
definidos na enumeração AttributeType. 
Este estereótipo também estende a metaclasse Component a fim de permitir sua 
representação como um componente. 
 
Tabela 6 - Estereótipo NOP_Premise 
Estereótipo 
Classe Base 
Generalização 
Valores Etiquetados 
<<NOP_Premise>> 
Class, Component 
NA 
exclusive, attribute, 
operator, value 
Descrição 
Realiza o cálculo lógico sobre os estados dos objetos FBE, a fim de aprovar as 
condições das regras.  
Restrições 
Um estereótipo <<NOP_Premise>> só pode relacionar-se com objetos de 
estereótipos: 
a. <<NOP_Attribute>> – para receber notificações dos atributos que tiveram seus 
estados alterados.  
b. <<NOP_Condition>> – para gerar notificações às condições 
c. Em uma representação com abstração maior, um <<NOP_Premise >> pode 
receber notificações de objetos <<NOP_FBE >>, subentendendo-se que os 
Attribute e Method dos FBEs estão implícitos. 
• 
Um objeto <<NOP_Premise>> pode ser notificado por um ou dois objetos 
<<NOP_Attribute>>. 
• 
Um objeto <,NOP_Premise>> pode notificar um ou mais objetos <<NOP_Condition>>. 
• 
Um objeto <<NOP_ Premise >> deve possuir um valor etiquetado exclusive definido, que 
por default é falso. Quando omitido do diagrama significa que é falso. 
• 
Um <<NOP_Premise >> deve possuir um valor etiquetado attribute, operator e value 
definidos. 
Semântica  
O estereótipo <<NOP_Premise>> refere-se à classe Premise do framework e estende 
a metaclasse Object da UML, uma vez que ele representa um objeto no mecanismo de 
notificações do PON. Um ou mais objetos Premise compõem a condição de uma regra. Cada 
Premise possui três elementos principais que colaboram entre si para a sua avaliação, 
representados pelos valores etiquetados attribute, operator e value. O attribute é comparado ao 


108 
 
value por meio do operator. Por meio da colaboração desses elementos, têm-se a aprovação ou 
não do objeto Instigation. Adicionalmente, um objeto Premise pode ser exclusivo ou não 
(conceito de Premise Exclusive), informação dada pelo valor etiquetado exclusive. 
Este estereótipo também estende a metaclasse Component a fim de permitir sua 
representação como um componente. 
 
Tabela 7 - Estereótipo NOP_Condition 
Estereótipo 
Classe Base 
Generalização 
Valores Etiquetados 
<<NOP_Condition>> 
Object, Component 
NA 
logicalOperator 
Descrição 
É responsável pela parte de decisão de uma regra, fazendo parte, portanto, da 
composição de um objeto estereotipado <<NOP_Rule>>.  
Restrições 
• 
Um estereótipo <<NOP_Condition>>  só pode relacionar-se com objetos de estereótipos: 
a.  <<NOP_Rule>> - para fazer parte da estrutura do <<NOP_Rule>> e gerar 
notificação ao <<NOP_Rule>> para informar sua aprovação. 
b. <<NOP_Premise>> - para receber notificações das avaliações dos estados lógicos 
dos objetos <<NOP_Premise>>. 
c. Em uma representação com abstração maior, um <<NOP_Condition >> pode 
receber notificações de objetos <<NOP_FBE >>, subentendendo-se que seus 
Premise e Instigation e, consequentemente seus Attribute e Method, estão 
implícitos. 
• 
Um objeto <<NOP_Condition>> pode ser notificado por um ou mais objetos 
<<NOP_Premise>>. 
• 
Um objeto <<NOP_Condition>> pode notificar um objeto <<NOP_Rule>>. 
• 
Possui um estereótipo especializado: <NOP_SubCondition>> 
• 
Um objeto <<NOP_Condition>> deve possuir um valor etiquetado logicalOperator 
definido. 
Semântica  
O estereótipo <<NOP_Condition>> refere-se à classe Condition do framework e 
estende a metaclasse Object da UML, uma vez que ele representa um objeto no mecanismo de 
notificações do PON. Um objeto estereotipado <<NOP_Condition>> armazena os resultados 
dos cálculos lógicos dos objetos <<NOP_Premise>> que estão associados a este 
<<NOP_Condition>> e, quando todos os objetos <<NOP_Premise>> são verdadeiros, ou 
satisfazem o operador lógico da condição, o <<NOP_Condition>> notifica o <<NOP_Rule>> 
pertinente. Um objeto <<NOP_Condition>> utiliza o valor etiquetado logicalOperator para 


109 
 
 
 
definir o operador lógico que será aplicado entre os objetos <<NOP_Premise>>. 
Este estereótipo também estende a metaclasse Component a fim de permitir sua 
representação como um componente. 
 
Tabela 8 - Estereótipo NOP_SubCondition 
Estereótipo 
Classe Base 
Generalização 
Valores Etiquetados 
<<NOP_SubCondition>> 
Object, 
Component 
<<NOP_Condition>>
logicalOperator 
Descrição 
É responsável pela parte de decisão de uma regra. No entanto, representa um 
agrupamento dos objetos <<NOP_Premise>> que estão relacionados por um mesmo tipo de 
operador lógico dentro de um <<NOP_Condition>>. 
Restrições 
• 
Um estereótipo <<NOP_SubCondition>> é uma especialização do estereótipo 
<<NOP_Condition>>, sendo que ambos relacionam-se por meio de um relacionamento de 
especialização padrão da UML. 
• 
Um objeto <<NOP_SubCondition >> deve possuir um valor etiquetado logicalOperator 
definido. 
Semântica  
O estereótipo <<NOP_SubCondition>> é referente à classe SubCondition do 
framework. Este estereótipo, igualmente a sua superclasse, estende a metaclasse Object da 
UML, uma vez que representa um objeto no mecanismo de notificações do PON. 
Com a utilização de <<NOP_SubCondition>>, os objetos <<NOP_Premise>> 
notificam 
os 
objetos 
<<NOP_Condition>> 
indiretamente, 
por 
meio 
dos 
<<NOP_SubCondition>>. Neste contexto, os <<NOP_SubCondition>> fazem o papel dos 
<<NOP_Premise>>, notificando os respectivos <<NOP_Condition>> no momento em que 
tiverem seus estados lógicos alterados. Para um objeto <<NOP_Condition>> é indiferente 
receber notificações de <<NOP_SubCondition>> ou <<NOP_Premise>>, uma vez que os seus 
estados lógicos são atualizados da mesma maneira. 
Este estereótipo também estende a metaclasse Component a fim de permitir sua 
representação como um componente. 
 
Tabela 9 - Estereótipo NOP_Action 
Estereótipo 
Classe Base 
Generalização 
Valores Etiquetados 
<<NOP_Action>> 
Object, Component 
NA 
NA 
Descrição 


110 
 
Um estereótipo <<NOP_Action>> é responsável pela parte de ação de uma regra, 
sendo responsável por iniciar a cadeia de execução dos métodos dos objetos NOP_FBE ao 
gerar notificações aos estereótipos <<NOP_Instigation>>. 
Restrições 
• 
Um estereótipo <<NOP_Action>> só pode relacionar-se com objetos de estereótipos: 
a.  <<NOP_Rule>> - para fazer parte da estrutura do <<NOP_Rule>> e receber 
notificação para iniciar a cadeia de execução da regra. 
b. <<NOP_Instigation>> – para gerar notificações às instigações da regra. 
c. Em uma representação com abstração maior, um <<NOP_ Action >> pode gerar 
notificações a objetos <<NOP_FBE >>, subentendendo-se que seus Premise e 
Instigation e, consequentemente, seus Attribute e Method, estão implícitos. 
• 
Um objeto <<NOP_Action>> pode ser notificado por um objeto <<NOP_Rule>>. 
• 
Um objeto <<NOP_Action>> pode notificar um ou mais objetos <<NOP_Instigation>>. 
Semântica  
O estereótipo <<NOP_Action>> refere-se à classe Action do framework e estende a 
metaclasse Object da UML, uma vez que ele representa um objeto no mecanismo de 
notificações do PON. Um objeto <<NOP_Action>> notifica um ou mais objetos 
<<NOP_Instigation>>, que por sua vez notificam os objetos <<NOP_Method>>. 
Este estereótipo também estende a metaclasse Component a fim de permitir sua 
representação como um componente. 
 
Tabela 10 - Estereótipo NOP_Instigation 
Estereótipo 
Classe Base 
Generalização 
Valores Etiquetados 
<<NOP_Instigation>>
Object, Component 
NA 
attribute, 
value, 
method 
Descrição 
Um objeto <<NOP_Instigation>> é responsável por invocar os métodos dos FBEs, 
que, por sua vez, são executados e alteram os estados de seus atributos ou outros FBEs. Mas 
eles também podem alterar os estados dos FBEs diretamente, sem a intervenção dos métodos. 
Restrições 
• 
Um estereótipo <<NOP_Instigation>> só pode relacionar-se com objetos de estereótipos: 
a. <<NOP_Action>> - recebendo notificações da ação da regra 
b. <<NOP_Method>> - para gerar notificações para a execução de métodos 
c. <<NOP_Attribute>> - para alterar diretamente o estado de um 
<<NOP_Attribute>>, sem o intermédio do <<NOP_Method>>. 
d. Em uma representação com abstração maior, um <<NOP_Instigation >> pode 


111 
 
 
 
gerar notificações a objetos <<NOP_FBE >>, subentendendo-se que os Attribute e 
Method dos FBEs estão implícitos. 
• 
Um objeto <<NOP_Instigation>> pode ser notificado por um ou mais objetos 
<<NOP_Condition>>. 
• 
Um objeto <<NOP_Instigation>> pode notificar zero ou um objeto <<NOP_Method>>. 
• 
Um objeto <<NOP_Instigation>> pode alterar zero ou um objeto <<NOP_Attribute>>. 
• 
Um objeto << NOP_Instigation >> deve possuir os valores etiquetados definidos method 
ou attribute e value. 
Semântica 
O estereótipo <<NOP_Instigation>> refere-se à classe Instigation do framework e 
estende a metaclasse Object da UML, uma vez que ele representa um objeto no mecanismo de 
notificações do PON.  Um objeto <<NOP_Instigation>> é responsável por invocar os serviços 
de um objeto <<NOP_Method>> (de forma local ou remota) que, por sua vez, altera os estados 
dos objetos <<NOP_Attribute>>. Um ou mais <<NOP_Instigation>> constituem o corpo de 
um objeto <<NOP_Action>>. De forma alternativa, também é possível que um objeto 
<<NOP_Instigation>> relacione-se com um objeto <<NOP_Attribute>> alterando seu estado 
diretamente. Neste caso, o objeto Method não participa da cadeia de notificação.  
O valor etiquetado method é usado para definir qual o Method a ser executado. No 
caso em que os <<NOP_Instigations>> notificam os Attribute diretamente, deve-se utilizar os 
valores etiquetados attribute e value, sendo que o primeiro define qual o Attribute a ser alterado 
e o segundo o valor que o Attribute deve receber. 
Este estereótipo também estende a metaclasse Component a fim de permitir sua 
representação como um componente. 
 
Tabela 11 - Estereótipo NOP_Method 
Estereótipo
Classe Base
Generalização
Valores Etiquetados
<<NOP_Method>> 
Object, 
Operation, 
Component 
NA 
NA 
Descrição 
O estereótipo <<NOP_Method>> encapsula a funcionalidade de um método que 
pode ser usado de duas formas: guardar referência para a chamada de um método de um objeto 
ou implementar o método em seu próprio escopo (funções implementadas por suas subclasses). 
O <<NOP_Method>> tem como responsabilidade receber notificações de objetos 
<<NOP_Instigation>> de uma regra gerando a sua execução. 
Restrições 
• 
Um estereótipo<<NOP_Method>>  só pode relacionar-se com objetos de estereótipos: 


112 
 
a. <<NOP_FBE>> - para fazer parte da estrutura do FBE 
b. <<NOP_Instigation>> - para receber notificações de execução 
c. <<NOP_Attribute>> - para alterar o estado dos atributos da regra 
• 
Um objeto <<NOP_Method>>  pode pertencer a um objeto <<NOP_FBE>>. 
• 
Um objeto <<NOP_Method>>  pode receber notificação de um ou mais objetos 
<<NOP_Instigation>>. 
• 
Um objeto <<NOP_Method>>  pode alterar o estado de um ou mais objetos 
<<NOP_Attribute>>. 
• 
Possui 
dois 
estereótipos 
especializados: 
<<NOP_MethodPointer>> 
e 
<<NOP_MethodDerived>> 
Semântica  
O estereótipo <<NOP_Method>> refere-se à classe Method do framework e estende 
as metaclasses Method e Object da UML. No framework, um objeto Method faz parte da 
composição de um objeto FBE. Ao criar um novo FBE, o programador define os métodos 
desse FBE como sendo do tipo da classe Method do framework. Quando adicionados às 
instigações das regras, os Methods entram na cadeia de notificação do PON. Portanto, os 
Method são métodos do ponto de vista de um FBE e, por isso, estendem a metaclasse 
Operation, mas também são objetos do ponto de vista do mecanismo de notificação do PON, e 
por isso também estendem a metaclasse Object.  
Este estereótipo também estende a metaclasse Component a fim de permitir sua 
representação como um componente. 
 
Tabela 12 - Estereótipo NOP_MethodPointer 
Estereótipo 
Classe Base 
Generalização 
Valores Etiquetados 
<<NOP_MethodPointer>>
Object, 
Operation, 
Component 
<<NOP_Method>> 
NA 
Descrição 
Encapsula a funcionalidade de um método guardando referência para a chamada de um 
método de um objeto implementado no escopo do FBE. 
Restrições 
• 
Um 
estereótipo 
<<NOP_MethodPointer>> 
é 
uma 
especialização 
do 
estereótipo 
<<NOP_Method>>, sendo que ambos relacionam-se por meio de um relacionamento de 
especialização padrão da UML. 
• 
Possui as mesmas restrições do estereótipo <<NOP_Method>>. 
Semântica  
O estereótipo <<NOP_MethodPointer>> é referente à classe MethodPointer do 


113 
 
 
 
framework. Este estereótipo, igualmente a sua superclasse, estende as metaclasses Object e 
Operation da UML.  
Em PON, uma classe MethodPointer  modela os objetos que encapsulam a chamada de um 
método definido e declarado na estrutura de uma classe FBE, sendo que o endereço desse método é 
atribuído ao objeto no momento de sua criação. 
Este estereótipo também estende a metaclasse Component a fim de permitir sua 
representação como um componente. 
 
Tabela 13 - Estereótipo NOP_MethodDerived 
Estereótipo 
Classe Base 
Generalização 
Valores 
Etiquetados 
<<NOP_MethodDerived>> 
Object, Operation, 
Component 
<<NOP_Method>> 
NA 
Descrição 
Encapsula a funcionalidade de um método guardando referência para a chamada de 
um método de um objeto. 
Restrições 
• 
Um estereótipo <<NOP_MethodDerived>> é uma especialização do estereótipo 
<<NOP_Method>>, sendo que ambos relacionam-se por meio de um relacionamento de 
especialização padrão da UML. 
• 
Possui as mesmas restrições do estereótipo <<NOP_Method>>. 
Semântica  
O estereótipo <<NOP_MethodDerived>> é referente à classe MethodDerived do 
framework. Este estereótipo, igualmente a sua superclasse, estende as metaclasses Object e 
Operation da UML.  
Um estereótipo <<NOP_MethodDerived>> permite que o conjunto de instruções  de 
um método sejam implementandos em suas classes estendidas. Esta prática atribui maior 
capacidade de distribuição aos objetos, uma vez que a estrutura dos FBEs se encontra mais 
desacoplada de suas implementações. 
Este estereótipo também estende a metaclasse Component a fim de permitir sua 
representação como um componente. 
 
 
 
 


114 
 
3.2.2.1.2. Pacote Core Relationships 
 
 
O pacote Core-Relationships define estereótipos de relacionamentos e de mensagens 
aplicáveis entre os estereótipos do Core-Elements, sendo que é composto por quatro pacotes:  
• Core-Association: define estereótipos de relacionamento aplicáveis entre os objetos 
participantes do mecanismo do PON e estende a metaclasse que define o nome deste 
pacote: a metaclasse Association. Estes relacionamentos são aplicados entre objetos 
em diagramas de objetos. 
• Core-Assembly: possui os mesmos estereótipos de relacionamento definidos no Core-
Association, mas neste pacote esses estereótipos estendem a metaclasse Assembly. 
Estes relacionamentos são aplicados entre componentes em diagramas de 
componentes.  
• Core-Sequence: possui os mesmos estereótipos definidos no Core-Association, mas 
neste pacote esses estereótipos estendem a metaclasse Sequence a fim de representar 
mensagens entre objetos. Estes estereótipos são aplicados entre objetos em diagramas 
de sequência. 
• Core-Collaboration: possui os mesmos estereótipos definidos no Core-Association, 
mas neste pacote esses estereótipos estendem a metaclasse Collaboration a fim de 
representar mensagens entre objetos. Estes estereótipos são aplicados entre objetos em 
diagramas de comunicação. 
 
As subseções seguintes apresentam a representação gráfica e tabular desses pacotes. 
 
3.2.2.1.2.1. 
Pacote Core Relationships - Representação Gráfica 
 
A Figura 50 ilustra o pacote Core Relationship – Association. Este pacote define 
estereótipos de associações que representam as notificações que ocorrem entre os objetos 
colaboradores do PON, sendo que eles estendem a metaclasse Association da UML. Para cada 
um dos relacionamentos relevantes em termos de modelagem definidos no modelo de 
domínio da Figura 43, foi criado um estereótipo de associação que define a notificação e suas 
restrições.  


 
 
 
Como já comenta
três metaclasses: a metacla
Core-Collaboration para re
do PON; além da meta
relacionamento entre esse
restrições aos relacionamen
para poderem ser aplicados
Sequence, Core-Collabora
Association, eles não serão
 
3.2.2.1.2.2. 
Pacote Core
 
As tabelas a seguir
T
Estereótipo 
<<AttributeNotifiesPremise>>
Descrição 
Relacionamento de
<<NOP_Premise>> que ocor
A fim de represe
Figura 50 - NOP Profile – Core-Association 
 
do, estes mesmos dez estereótipos de associ
asse Sequence no pacote Core-Sequence e Co
epresentar mensagens entre os objetos do mec
aclasse Assembly no pacote Core-Assem
es objetos. Estes estereótipos definem dif
ntos entre os elementos do PON, e estendem 
s em diferentes modelos no método DON. C
tion e Core-Assembly possuem os mesmos 
ilustrados nesta seção. 
e Relationships - Representação Tabular 
r apresentam os estereótipos de relacionamen
 
Tabela 14 - Estereótipo AttributeNotifiesPremise 
Classe Base 
> 
Assembly, Association, Sequence, Collab
e notificação entre os estereótipos <<NOP
rre no sentido NOP_Attribute  NOP_Premise. 
entar os diagramas com um nível de abstra
115 
 
iação estendem outras 
ollaboration no pacote 
canismo de notificação 
mbly para representar 
ferentes semânticas e 
diferentes metaclasses 
Como os pacotes Core-
estereótipos do Core-
nto e suas definições.  
boration 
P_Attribute>> e 
ação maior, este 


116 
 
relacionamento também pode ocorrer entre: 
• 
<<NOP_FBE>> e <<NOP_Premise>>  indicando que, apesar do <<NOP_Attribute>> estar 
omitido do diagrama, subentende-se que uma notificação ocorreu entre um Attribute e um 
Premise.  
• 
<<NOP_FBE>> e <<NOP_Condition>> indicando que, apesar do <<NOP_Attribute>> e 
<<NOP_Premise>> estarem omitidos do diagrama, subentende-se que uma notificação 
ocorreu entre um Attribute e um Condition.  
Restrições 
• 
Um estereótipo <<NOP_Attribute>> pode notificar um ou mais estereótipos 
<<NOP_Premise>>. 
 
Tabela 15 - Estereótipo PremiseNotifiesCondition 
Estereótipo 
Classe Base 
<<PremiseNotifiesCondition>> 
Assembly, Association, Sequence, Collaboration 
Descrição 
Relacionamento de notificação entre os estereótipos <<NOP_Premise>> e 
<<NOP_Condition>> que ocorre no sentido NOP_Premise  NOP_Condition.  
Restrição 
• 
Um 
estereótipo 
<<NOP_Premise>> 
pode 
notificar 
um 
ou 
mais 
estereótipos 
<<NOP_Condition>>. 
 
Tabela 16 - Estereótipo ConditionNotifiesRule 
Estereótipo 
Classe Base 
<<ConditionNotifiesRule>> 
Assembly, Association, Sequence, Collaboration 
Descrição 
Relacionamento de notificação entre os estereótipos <<NOP_Condition>> e 
<<NOP_Rule>> que ocorre no sentido NOP_Condition  NOP_Rule.  
Restrição 
• 
Um estereótipo <<NOP_Condition>> pode notificar um estereótipo <<NOP_Rule>>. 
 
Tabela 17 - Estereótipo RuleNotifiesAction 
Estereótipo 
Classe Base 
<<RuleNotifiesAction>> 
Assembly, Association, Sequence, Collaboration 
Descrição 
Relacionamento 
de 
notificação 
entre 
os 
estereótipos 
<<NOP_Rule>> 
e 


117 
 
 
 
<<NOP_Action>> que ocorre no sentido NOP_Rule  NOP_Action.  
Restrição 
• 
Um estereótipo <<NOP_Rule>> pode notificar um estereótipo <<NOP_Action>>. 
 
Tabela 18 - Estereótipo ActionNotifiesInstigation 
Estereótipo 
Classe Base 
<<ActionNotifiesInstigation>> 
Assembly, Association, Sequence, Collaboration 
Descrição 
Relacionamento de notificação entre os estereótipos <<NOP_Action>> e 
<<NOP_Instigation>> que ocorre no sentido NOP_Action  NOP_Instigation.  
Restrição 
• 
Um 
estereótipo 
<<NOP_Action>> 
pode 
notificar 
um 
ou 
mais 
estereótipos 
<<NOP_Instigation>>. 
 
Tabela 19 - Estereótipo InstigationNotifiesMethod 
Estereótipo 
Classe Base 
<<InstigationNotifiesMethod>> 
Assembly, Association, Sequence, Collaboration 
Descrição 
Relacionamento de notificação entre os estereótipos <<NOP_Instigation>> e 
<<NOP_Method>> que ocorre no sentido NOP_Instigation  NOP_Method.  
A fim de representar os diagramas com um nível de abstração maior, este 
relacionamento também pode ocorrer entre: 
• 
<<NOP_Action>> e <<NOP_FBE>> indicando que, apesar do <<NOP_Instigation>>, 
<<NOP_Method>> e <<NOP_Attribute>> estarem omitidos do diagrama, subentende-se 
que uma notificação ocorreu entre um Action e um Instigation,  na sequência outra 
notificação ocorreu entre um Instigation e um Method e, por fim, outra entre o Method e o 
Attribute. 
• 
<<NOP_Instigation>> e <<NOP_FBE>>  indicando que, apesar do <<NOP_Method>> e 
<<NOP_Attribute>> estarem omitidos do diagrama, subentende-se que uma notificação 
ocorreu entre um Instigation e um Method e, na sequência, entre um Method e um Attribute 
do FBE. 
• 
<<NOP_Rule>> e <<NOP_FBE>> indicando que, apesar do <<NOP_Action>>, 
<<NOP_Instigation>>, <<NOP_Method>> e <<NOP_Attribute>> estarem omitidos do 
diagrama, subentende-se que uma notificação ocorreu entre um Rule e um Action, na 
sequência entre Action e um Instigation, na sequência ainda entre um Instigation e um 
Method e, por fim, outra entre o Method e o Attribute. 


118 
 
Restrição 
• 
Um estereótipo <<NOP_Instigation>> pode notificar zero ou um estereótipo 
<<NOP_Method>>. 
 
Tabela 20 - Estereótipo InstigationNotifiesAttribute 
Estereótipo 
Classe Base 
<<InstigationNotifiesAttribute>> 
Assembly, Association, Sequence, Collaboration 
Descrição 
Relacionamento de notificação entre os estereótipos <<NOP_Instigation>> e 
<<NOP_Attribute>> que ocorre no sentido NOP_Instigation  NOP_Attribute.  
A fim de representar os diagramas com um nível de abstração maior, este 
relacionamento também pode ocorrer entre: 
• 
<<NOP_Action>> e <<NOP_FBE>> indicando que, apesar do <<NOP_Instigation>> e 
<<NOP_Attribute>> estarem omitidos do diagrama, subentende-se que uma notificação 
ocorreu entre um Action e um Instigation e, na sequência, outra notificação ocorreu entre 
um Instigation e um Attribute. 
Restrição 
• 
Um estereótipo <<NOP_Instigation>> pode notificar zero ou um estereótipo 
<<NOP_Attribute>>. 
 
Tabela 21 - Estereótipo MethodNotifiesAttribute 
Estereótipo 
Classe Base 
<<MethodNotifiesAttribute>> 
Assembly, Association, Sequence, Collaboration 
Descrição 
Relacionamento de notificação entre os estereótipos <<NOP_Method>> e 
<<NOP_Attribute>> que ocorre no sentido NOP_Method  NOP_Attribute.  
Restrição 
• 
Um estereótipo <<NOP_Method>> pode notificar zero ou mais estereótipos 
<<NOP_Attribute>>. 
 
Tabela 22 - Estereótipo PremiseNotifiesSubCondition 
Estereótipo 
Classe Base 
<<PremiseNotifiesSubCondition>> 
Assembly, Association, Sequence, Collaboration 
Descrição 
Relacionamento de notificação entre os estereótipos <<NOP_Premise>> e 
<<NOP_SubCondition>> que ocorre no sentido NOP_Premise  NOP_SubCondition.  


119 
 
 
 
Restrição 
• 
Um estereótipo <<NOP_Premise>> pode notificar zero ou mais estereótipos 
<<NOP_SubCondition>>. 
 
Tabela 23 - Estereótipo SubConditionNotifiesCondition 
Estereótipo 
Classe Base 
<<SubConditionNotifiesCondition>>
Assembly, Association, Sequence, Collaboration 
Descrição 
Relacionamento de notificação entre os estereótipos <<NOP_SubCondition>> e 
<<NOP_Condition>> que ocorre no sentido NOP_SubCondition  NOP_Condition.  
Restrição 
• 
Um 
estereótipo 
<<NOP_SubCondition>> 
pode 
notificar 
um 
estereótipo 
<<NOP_Condition>>. 
 
 
3.2.2.2. 
NOP Profile - Application 
 
Seguindo os mesmos passos para a criação do NOP Profile – Core, foi construído o 
NOP Profile – Application. No framework do PON, o pacote Application contém as classes 
que promovem a resolução de conflitos centralizados, além da classe que fornece o ponto de 
extensão entre os dois pacotes framework. O ponto de extensão permite que uma aplicação, 
que é definida no pacote Application, use os serviços do pacote Core.  
 
3.2.2.2.1. NOP Profile Application - Representação Gráfica 
 
O perfil Application foi obtido a partir da análise do modelo do domínio da Figura 44 
(pacote Application do framework do PON). Neste perfil, a classe Application do modelo do 
domínio foi transformada em um estereótipo <<NOP_Application>>  que estende a 
metaclasse Class do metamodelo da UML, uma vez que uma nova aplicação em PON é 
representada como uma subclasse da classe Application. Os métodos, que são herdados 
automaticamente quando cria-se uma subclasse da classe Application do framework do PON, 
foram transformados em estereótipos que estendem a metaclasse Operation da UML, sendo 
eles: 
initFactBase, 
initRules, 
codeApplication, 
initSharedPremises 
e 
configureStartApplication. A Figura 51 ilustra o perfil Application construído. 


120 
 
 
 
A classe “Schedu
como valores possíveis,
enumeração. 
Tab
Enumeração 
Descriç
SchedulerStrategy
O este
estratég
opções 
• BR
• 
PR
def
• 
DE
• 
UN
ime
• NO
env
util
 
Figura 51 - NOP Profile - Application 
ulerStrategy” foi transformada em uma enu
as suas classes especializadas. A Tabe
bela 24 - Enumeração do NOP Profile - Application 
ção 
ereótipo SchedulerStrategy é uma enumeraçã
gias de resolução de conflito disponíveis no PO
são:  
READTH: se baseia no escalonamento FIFO, 
RIORITY: organiza os objetos Rules de acordo c
finidas nos mesmos,  
EPTH: se baseia no escalonamento FILO,  
NCACHED: a regra é adicionada ao escalon
ediatamente. 
O_ONE: quando não há estratégia definida 
viada ao escalonador, mas é aprovada im
lizada esta estratégia. 
 
umeração que possui, 
la 24 descreve essa 
o que define as 
ON, sendo que as 
 
com as prioridades 
nador e aprovada 
e a regra não é 
mediatamente, é 


121 
 
 
 
O atributo scheduler da classe Application do modelo do domínio foi adicionado ao 
estereótipo <<NOP_Application>> como um valor etiquetado de mesmo nome, podendo 
assumir os valores definidos pela enumeração SchedulerStrategy. A Tabela 25 descreve o 
valor etiquetado scheduler. 
 
Tabela 25 - Valor Etiquetado do NOP Profile - Application 
Valor 
Etiquetado 
Estereótipo 
Tipo 
Valor 
Inicial 
Descrição 
scheduler 
Application 
SchedulerStrategy
NA 
Define a estratégia para a 
resolução de conflitos entre 
as regras. 
 
3.2.2.2.2. NOP Profile Application - Representação Tabular 
 
Nesta seção são descritos os estereótipos do pacote Application. 
 
 
Tabela 26 - Estereótipo NOP_Application 
Estereótipo 
Classe Base 
Generalização 
Valores Etiquetados 
<<NOP_Application>>
Class 
NA 
scheduler 
Descrição 
O estereótipo <<NOP_Application>> representa o ponto de extensão do framework, 
ou seja, representa a classe que permite que uma aplicação, que é definida no pacote Application, 
use os serviços do pacote Core. Além disso, define a estratégia para a resolução de conflitos 
centralizados. 
Restrições 
• 
Uma classe estereotipada <<NOP_Application>> automaticamente importa os estereótipos 
do pacote Core do framework do PON. 
• 
Uma classe estereotipada <<NOP_Application>> deve possuir um valor etiquetado 
scheduler definido. 
• 
Uma classe estereotipada deve obrigatoriamente possuir um método estereotipado 
<<initFactBase>> e um <<initRules>>. 
• 
Uma classe estereotipada <<NOP_Application>> pode se relacionar com uma ou mais 
classes <<NOP_FBE>> 
• 
Um objeto estereotipado <<NOP_Application>> pode se relacionar com um ou mais objetos 
<<NOP_FBE>>, 
<<NOP_Attribute>>, 
<<NOP_Method>>, 
<<NOP_Rule>>, 


122 
 
<<NOP_Condition>> e <<NOP_Action>> a fim de satisfazer diferentes níveis de abstração 
em um diagrama. 
Semântica  
O estereótipo << NOP_Application>> refere-se à classe Application do framework do 
PON e estende a metaclasse Class, uma vez que uma nova aplicação em PON é definida como 
uma subclasse da classe Application. A classe Application possui os métodos para a definição 
dos FBEs e Rules da aplicação a ser desenvolvida (initFactBase e initRules respectivamente). 
Ele possui um valor etiquetado scheduler que define a estratégia para a resolução de conflitos 
entre as regras. 
 
Tabela 27 - Estereótipo initFactBase 
Estereótipo 
Classe Base 
<<initFactBase>> 
Operation 
Descrição 
O estereótipo initFactBase é referente ao método responsável por instanciar os 
objetos FBEs definidos na aplicação. 
 
Tabela 28 - Estereótipo initRules 
Estereótipo 
Classe Base 
<<initRules>> 
Operation 
Descrição 
O estereótipo initRules é referente ao método responsável por definir os objetos 
Rules da aplicação. 
 
Tabela 29 - Estereótipo codeApplication 
Estereótipo 
Classe Base 
<<codeApplication>> 
Operation 
Descrição 
O estereótipo codeApplication é referente ao método responsável por definir o 
código da aplicação. 
 
 
 
 
 


123 
 
 
 
Tabela 30 - initSharedPremises 
Estereótipo 
Classe Base 
<<initSharedPremises>> 
Operation 
Descrição 
O estereótipo initSharedPremises é referente ao método responsável por definir os 
objetos Premises que serão compartilhados por objetos Conditions.  
 
Tabela 31 - Estereótipo configureStartApplicationAction 
Estereótipo 
Classe Base 
<<configureStartApplicationAction>>
Operation 
Descrição 
O estereótipo configureStartApplicationAction é referente ao método responsável por 
definir os Instigations  do objeto Action relacionado com a Rule de inicialização do sistema. 
 
3.3. 
CONSIDERAÇÕES SOBRE O NOP PROFILE 
 
Este capítulo apresentou uma visão geral do método proposto, que foi desenvolvido 
em duas etapas, criação do NOP Profile e criação do método DON, além da apresentação e 
detalhamento do perfil UML criado para o PON, o NOP Profile. O NOP Profile especializa o 
metamodelo da UML a fim de melhor adequar a UML para a modelagem de softwares que 
utilizam este novo paradigma de programação. O perfil desenvolvido especificou elementos 
do framework do PON que fazem a interface do framework com o programador. Não foram 
considerados neste trabalho aqueles elementos que fazem parte do framework, mas que são 
transparentes ao programador. O objetivo foi identificar e expressar, por meio do perfil UML, 
os elementos que serão utilizados pelo projetista e programador em PON. 
 
 
 
 
 


124 
 
 
 


125 
 
 
 
4. DESCRIÇÃO DO MÉTODO PROPOSTO  
 
Como apresentado no capítulo 1, a engenharia de software é constituída basicamente 
por três elementos fundamentais: métodos, ferramentas e procedimentos. Os métodos, em 
particular, oferecem os detalhes de “como fazer” para construir o software e envolvem 
atividades como planejamento e estimativa de projeto, análise de requisitos, projeto da 
estrutura de dados, arquitetura de programa e algoritmo de processamento, codificação, teste e 
manutenção. Os métodos de engenharia de software muitas vezes introduzem uma notação 
gráfica ou orientada à linguagem especial. 
Portanto, concluída a fase de criação do perfil UML para o PON, o NOP Profile, 
iniciou-se a criação do método DON – Desenvolvimento Orientado a Notificações – que tem 
por objetivo orientar projetistas na construção de projetos de software no Paradigma 
Orientado a Notificações (PON). O DON se adapta a processos de software conhecidos e 
emprega o NOP Profile em seus projetos. Além disso, faz uso de ferramentas de modelagem, 
sendo que no caso desta dissertação foram utilizadas a Enterprise Architecture (SPARX, 
2011) para modelagem em UML e Visual Object Net++ (DRATH, 2011) para modelagem em 
Redes de Petri. 
 
4.1. 
DESENVOLVIMENTO ORIENTADO A NOTIFICAÇÕES (DON) 
 
O DON é um método para projetos de softwares que compreende as fases de 
requisitos e projeto de um processo de software. Mais especificamente, quando aplicado ao 
processo RUP, o DON envolve a disciplina de “Requisitos” e adapta a disciplina de “Análise 
e Projeto” a fim de satisfazer as necessidades de modelagem do PON. A Figura 52 ilustra o 
RUP e a contextualização do DON dentro desse processo. 


126 
 
 
Como apresentado
são descritas da seguinte fo
• Requisitos: estabele
interessados no sist
deste novo sistema
esforço de desenvol
• Análise e Projeto:
solução arquitetur
especificações técni
Aplicando-se ness
incremental viabilizando s
envolvem a criação de diag
os elementos estruturais 
relacionamentos. Já o seg
interações.  
As oito etapas do 
Uso, Criar Modelo de Cla
Componentes, Criar Model
Figura 52 - DON contextualizado no RUP 
o na seção 2.2 as disciplinas de “Requisitos”
orma: 
ecer o que o sistema deve fazer juntamente co
tema; definir os limites do sistema e, de acor
a, criar casos de uso que serão a base para
lvimento do sistema.  
: transformar os requisitos do sistema a se
al do software. Devem ser produzido
icas a serem seguidas na implementação de ca
sas disciplinas, o DON apresenta-se como u
sua adaptação ao RUP. O DON é compost
gramas estruturais e comportamentais. O pri
que compõem o sistema, representando 
gundo grupo descreve o comportamento d
método DON são: Capturar Requisitos, Cria
asses, Criar Modelo de Estados de Alto Ní
lo de Sequência, Criar Modelo de Comunicaç
 
” e “Análise e Projeto” 
om os clientes e outros 
rdo com as exigências 
a estimar o custo e o 
er construído em uma 
s modelos com as 
ada caso de uso. 
um método iterativo e 
to de oito etapas que 
imeiro grupo descreve 
suas partes e seus 
dos elementos e suas 
ar Modelo de Casos de 
ível, Criar Modelo de 
ção e Criar Modelo de 


 
 
 
Redes de Petri. As duas pr
seis restantes são referente
DON e suas etapas. 
 
 
O Modelo de Cla
apresentado na sequência) 
vez, o Modelo de Casos d
Modelo de Comunicação e
do sistema. 
 
O método DON é 
• Ciclo 1 – caracteriza-se
pela etapa “Capturar R
Petri”. Este ciclo é ilust
 
rimeiras são referentes à disciplina de “Req
s à disciplina de “Análise e Projeto”. A Figu
Figura 53 - Método DON – Ciclo 1 
asses, o Modelo de Componentes e o Mod
realizam a modelagem estrutural de um siste
de Uso, Modelo de Estados de Alto Nível, M
 Modelo de Redes de Petri realizam a model
composto por três ciclos básicos: 
e pela execução de todas as etapas do méto
Requisitos” e finalizando-se pela etapa “Criar
trado pela própria Figura 53. 
127 
quisitos” do RUP, e as 
ura 53 exibe o Método 
 
delo de Objetos (a ser 
ema em PON. Por sua 
Modelo de Sequência, 
lagem comportamental 
do DON, iniciando-se 
r Modelo de Redes de 


128 
 
• Ciclo 2 – este ciclo re
criar o Modelo de Caso
forem necessárias (itera
Uso satisfatório (Figura
 
• Ciclo 3 – este terceiro c
Modelo de Casos de Us
do Modelo de Classes 
ciclo também deve po
modelagem satisfatória
criação do Modelo d
Componentes e Modelo
Sequência e Comunicaç
omitidas dependendo da
estringe-se à captura dos requisitos do sistem
os de Uso do mesmo. Esse ciclo deve ser ex
ações) até se obter todos os requisitos e um
a 54). 
Figura 54 - Método DON – Ciclo 2 
ciclo tem por objetivo refinar a modelagem d
so.  Este ciclo é composto por seis etapas e i
e é finalizado com a criação do Modelo de
ssuir quantas iterações forem necessárias a
a e completa do sistema. As etapas mandató
de Classes, Modelo de Estados de Alto
o de Redes de Petri, sendo que as demais etap
ção– ajudam a enriquecer a modelagem do si
as necessidades do projeto. A Figura 55 ilustr
ma com o objetivo de 
ecutado quantas vezes 
m Modelo de Casos de 
 
o sistema com base no 
nicia-se com a criação 
e Redes de Petri. Este 
a fim de obter-se uma 
órias desse ciclo são a 
o Nível, Modelo de 
pas – Criar Modelo de 
istema, mas podem ser 
ra este ciclo. 


 
 
 
 
Não há uma ordem
exemplo, uma iteração do 
uma iteração do Ciclo 3 e
iterações para se obter o ref
As seções seguint
“Criar Modelo de Casos de
do NOP Profile definido na
do PON. 
 
4.1.1. Capturar Requisit
 
Esta é a primeira 
Nesta etapa não há alteraç
subseção e as subseções 
(Simulador de Portão Eletr
Figura 55 - Método DON – Ciclo 3 
m obrigatória para a iteração dos ciclos sendo
Ciclo 1 e uma do Ciclo 3, assim como duas
e, novamente, uma iteração do Ciclo 2. O o
finamento desejado dos modelos do sistema.
tes apresentam as etapas do método DON. C
e Uso”, todas as outras etapas são desenvolv
a seção 3.2, a fim de melhor expressar os ele
tos 
etapa do DON e tem por objetivo obter os 
ções específicas para o PON.  Visando exem
seguintes fazem referência a um caso de 
rônico), sistema este mencionado nos capítu
129 
 
o possível realizar, por 
s iterações do Ciclo 2, 
objetivo é executar as 
Com exceção da etapa 
vidas com a utilização 
ementos do framework 
requisitos do sistema. 
mplificar o DON, esta 
uso do sistema SPE 
ulos anteriores. O caso 


130 
 
de uso chama-se “Abrir Portão” e, a título de exemplo, apenas controla a abertura de um 
portão eletrônico por meio de um controle remoto. Dadas essas considerações, foram 
identificados os seguintes requisitos para este sistema: 
• O sistema deverá controlar o portão eletrônico, sendo que o portão deve iniciar fechado e 
possui um contador que começa zerado. 
• O controle remoto deve iniciar desligado. 
• O sistema deverá iniciar abertura do portão eletrônico quando o controle remoto for 
pressionado e, após 30 segundos, o portão estará aberto.  
• O contador deverá ser zerado após a abertura completa do portão. 
 
4.1.2. Criar Modelo de Casos de Uso 
 
Com base nos requisitos obtidos na etapa “Capturar Requisitos” são criados os casos 
de uso do software. Nesta etapa também não há alterações específicas para o PON, devendo 
ser criado o diagrama de Casos de Uso de maneira usual. Considerando os requisitos do 
fragmento do SPE obtidos na etapa “Capturar Requisitos”, tem-se os seguintes atores e casos 
de uso: 
Atores 
• Portão Eletrônico – representa o portão eletrônico e pode assumir os estados fechado, 
abrindo e aberto. O portão também possui um contador para controlar seu tempo de 
abertura. 
• Controle Remoto – representa o controle remoto e pode assumir os estados pressionado ou 
ligado e não pressionado ou desligado. 
 
Casos de Uso 
• Abrir Portão – define o início da abertura do portão.  Considera-se que o portão inicia-se 
fechado e, uma vez que o controle remoto é pressionado, o portão começa a abrir. Após 30 
segundos o portão estará aberto. 
 
A Figura 56 ilustra o caso de uso “Abrir Portão” do fragmento do sistema SPE, com 
os atores ControleRemoto e Portão. 


 
 
 
4.1.3. Criar Modelo de C
 
O Modelo de Clas
e permite a visualização da
a classe que representa um
sistema, sendo que estes úl
Os atores que armazenam i
PON. Este diagrama faz uso
Uma nova aplicaç
framework. No exemplo e
estereótipo <<NOP_Applic
este estereótipo à classe 
programador herda o valor
exemplo, scheduler foi d
operação initFactBase, 
SimpleApplication. 
No Modelo de C
ControleRemoto e Portão,
Gate. Essas classes repre
estereótipo <<NOP_FBE>
Modelo de Classes são id
<<NOP_FBE>> (que post
recebem o estereótipo 
<<NOP_MethodPointer>>
Para a classe Gate
que o portão pode assum
representa o contador ou tim
Figura 56 - Modelo de Caso de Uso 
 
Classes 
ses no DON é baseado no diagrama de classe
as classes utilizadas pelo software. No Modelo
ma aplicação em PON e são identificados o
ltimos são obtidos a partir do atores do Mod
informações úteis ao sistema transformam-se 
o dos pacotes Application e Core-Class do N
ção em PON deve começar estendendo a 
em questão, essa classe chama-se SimpleAp
cation>> definido no pacote Core-Class do p
SimpleApplication, automaticamente esta 
r etiquetado “scheduler” (exibido no compart
definido como “BREATH”. Adicionalmente
initRules e codeApplication foram ad
Casos de Uso da Figura 56 foram iden
 que são transformados na respectivas clas
esentam classes FBE no PON e, são assi
>> que recebem. Baseando-se no Modelo 
dentificados os atributos e os métodos das 
teriormente serão utilizados na definição das
<<NOP_Attribute>> e os métodos rec
> ou <<NOP_MethodDerived>>.  
e foram criados o atributo “atGateState”, qu
mir (0-CLOSED, 1-OPENING e 2-OPENED
mer do portão. Também foram identificados o
131 
 
es da UML, que define 
o de Classes é definida 
os elementos FBE do 
delo de Casos de Uso. 
em elementos FBE do 
NOP Profile. 
classe Application do 
pplication e recebe o 
perfil. Quando aplicado 
classe definida pelo 
timento “tags”). Neste 
e, os estereótipos de 
dicionados à classe 
tificados dois atores, 
ses RemoteControle e 
m interpretadas, pelo 
de Casos de Uso, no 
classes estereotipadas 
s regras). Os atributos 
cebem o estereótipo 
ue controla os estados 
D), e “atTimer”, que 
os métodos “Opening” 


132 
 
e 
“Opened” 
para 
ex
<<NOP_MethodPointer>>
de MethodPointer e Metho
classes (ex: mtStatusOpen
entanto, a nível de modelag
são  aplicados aos próprios 
Para a classe Rem
métodos “statusOn” e “stat
A Figura 57 ilustra o model
 
 
4.1.4. Criar Modelo de E
 
Os Modelos de A
identificação das regras do
Estados ou Diagrama de A
sofridas nos estados de um
outras instâncias que inter
facilitam a identificação d
elementos de decisão. 
xecutar 
o 
processo 
de 
abertura 
d
>. Na verdade, em nível de implementação,
odDerived que encapsulam as chamadas dos m
ned = new MethodPointer<Gate>(this, &
gem, os estereótipos <<MethodPointer>> e 
métodos para facilitar a modelagem.  
moteControl foram identificados o atributo “
tusOff”, ambos também estereotipados <<NO
lo de classes obtido. 
Figura 57 - Modelo de Classes 
Estados de Alto Nível 
Atividades de Alto Nível dos FBE têm po
 sistema e podem ser representados pelo Dia
Atividades da UML. Esses diagramas acom
ma instância de uma classe e, consequentem
agem com a instância em questão. Desta fo
de regras e suas premissas, sendo que esta
do 
portão, 
ambos 
são criadas instâncias 
métodos definidos nas 
&Gate::Opened);). No 
<<MethodDerived>> 
“atRemoteStatus” e os 
OP_MethodPointer>>. 
 
r objetivo auxiliar na 
agrama de Máquina de 
mpanham as mudanças 
mente, nos estados de 
orma, esses diagramas 
s são expressas pelos 


 
 
 
Portanto, o início 
da alteração dos estados d
Modelo de Estados de Al
completo, conforme a n
funcionamento do sistema
interação entre os FBEs a fi
A Figura 58 mostr
um diagrama de atividades
portão e satisfaz a análise 
decisão indicam o próximo
próprio portão assim como 
 
O levantamento d
nos elementos <<NOP_FB
de Alto Nível. Adicionalme
como apresentado na sequê
Qual o objetivo da regra?
O que precisa acontecer p
O que acontece se a regra
 
Aplicando essas p
duas regras neste caso de u
 
a) Regra 1 
Qual o objetivo da regra?
da identificação das regras em PON pode oc
os elementos FBEs. Esta análise pode acarr
lto Nível por FBE, por caso de uso ou, a
ecessidade. O intuito não é ter um dia
a, mas sim um diagrama simples e de alto 
fim de facilitar a identificação das regras.  
ra o Modelo de Estados de Alto Nível do FB
s. Este modelo foi criado em função da alte
do caso de uso “Abrir Portão” como um t
o estado do portão, sendo que as condições 
os estados do controle remoto.  
Figura 58 - Modelo de Estados de Alto Nível 
as regras é uma atividade de síntese (criativ
BE>> identificados no Modelo de Classes e n
ente, responder a algumas perguntas básicas
ência, auxilia na identificação das regras:  
?  
para que a regra seja executada?  
a for executada?  
perguntas ao exemplo em questão, observa
so: 
? Iniciar o processo de abertura do portão. 
133 
correr por uma análise 
retar na criação de um 
ainda, para o sistema 
agrama detalhado do 
nível que apresenta a 
BE “Gate” por meio de 
eração dos estados do 
todo. Os elementos de 
avaliam os estados do 
 
va) realizada com base 
no Modelo de Estados 
em linguagem natural, 
-se a identificação de 


134 
 
O que precisa acontecer para que a regra seja executada? O portão tem que estar no estado 
fechado, o controle remoto tem que ser pressionado e o contador do portão tem que estar 
zerado. 
O que acontece se a regra for executada? O portão deve mudar do estado fechado para 
abrindo e o controle remoto deve ser desligado a fim de simular que ele não está mais 
pressionado. 
 
b) Regra 2 
Qual o objetivo da regra? Finalizar o processo de abertura do portão. 
O que precisa acontecer para que a regra seja executada? O portão tem que estar no estado 
abrindo e o contador do portão tem que ser maior que 30 segundos. 
O que acontece se a regra for executada? O portão deve mudar do estado abrindo para 
aberto e o contador deve ser zerado. 
 
4.1.5. Criar Modelo de Componentes 
 
O modelo de Componentes é responsável por modelar a composição estática das 
regras do sistema, que nessa etapa devem possuir premissas e instigações. As regras começam 
a ser identificas na etapa “Criar Modelos de Estados de Alto Nível”, mas é nesta etapa, “Criar 
Modelo de Componentes”, que as regras são definitivamente elaboradas, recebendo nome, 
premissas e instigações. A criação deste modelo é feita pelo uso do Diagrama de 
Componentes da UML que permite representar as regras causais de forma inovadora, uma vez 
que as regras, suas premissas e instigações são representadas por componentes. 
Como observado por FRIEDMAN-HILL (2003), quebrar as regras em pequenos 
grupos ajuda a facilar a escrita e entendimento de um programa basedo em regras. 
Compartilhando a mesma idéia, para cada caso de uso definido no Modelo de Casos de Uso 
deve ser criado um Modelo de Componentes. Para facilitar o entendimento da construção das 
regras, a criação do Modelo de Componentes é dividida em 3 passos: “Definir as regras”, 
“Definir as premissas e instigações” e “Relacionar as regras aos FBEs”. Na sequência, cada 
um destes passos é apresentado e exemplificado.  Este modelo faz uso do pacote Core-
Components e Core-Assembly do NOP Profile. 
 
 
 


 
 
 
• Passo 1 - Definir as reg
 
O primeiro passo
definir as regras do mesmo
denominado “Abrir Portão
caso de uso. No Modelo d
regras: “Regra 1” e “Re
rlOpenedGate respectivam
componente <<NOP_Rule
facilitar a visualização d
estereotipado <<NOP_Rul
elementos Action, Rule e C
relacionamento pertinentes
restrições entre esses com
representadas como compo
 
Figura 59 -
 
gras 
para a criação do Modelo de Componentes
o. O Modelo de Casos de Uso da Figura 56 p
o” e, portanto, será criado um Modelo de C
de Estados de Alto Nível da Figura 58 for
egra 2”, que nesta fase recebem os nome
mente. Para cada uma dessas regras devem
e>>, um <<NOP_Action>> e um <<NOP
das regras, pode ser adicionado um com
le>> que representa a regra como um 
Condition.  A relação entre eles é representad
 definidos no pacote Core-Assembly, que ex
mponentes. A Figura 59 exibe as duas r
onentes.  
- Modelo de Componentes - Abrir Portão (Pa
135 
s de um caso de uso é 
possui um caso de uso 
Componentes para este 
ram identificadas duas 
es rlOpeningGate  e 
m ser adicionados um 
P_Condition>>. Para 
mponente abrangente 
todo englobando os 
da pelo estereótipos de 
xprimem a semântica e 
regras identificadas e 
 
asso 1) 


136 
 
Na criação de um componente <<NOP_Rule>> automaticamente aparece o valor 
etiquetado isDerived que, por padrão, é configurado como false (um valor etiquetado localiza-
se no compartimento denominado tags de um componente). Além disso, o valor etiquetado 
logicalOperator também aparece automaticamente no componente <<NOP_Condition>>, 
valor este que será definido no Passo 2 com a identificação das premissas e instigações. 
 
• Passo 2 – Definir as premissas e instigações  
 
O segundo passo da criação do Modelo de Componentes é identificar as premissas e 
as instigações das regras. Por meio da análise dos atributos e métodos dos FBEs do Modelo 
de Classes e das descrições das regras identificadas no Modelo de Alto Nível, são 
determinadas as premissas e as instigações. Retornando ao exemplo em questão, a Tabela 32 
apresenta as premissas e instigações definidas para cada uma das regras do caso de uso “Abrir 
Portão".  
 
Tabela 32 - Modelo de Componentes – Tabela das Regras 
Caso de Uso 
Nome Regra 
Premissas 
Instigações 
Abrir Portão 
R1- rlOpeningGate 
atGateState==CLOSED  && 
atRemoteStatus==true 
&&  
atTimer==0 
atGateState=OPENING, 
atRemoteStatus=false 
Abrir Portão 
R2 - rlOpenedGate 
atGateState==OPENING 
&& 
atTimer>30 
atGateState=OPENED,  
atTimer=0 
 
Uma vez identificadas, as premissas e instigações podem ser representadas de 
algumas formas no Modelo de Componentes, dependendo do grau de abstração que se deseja 
utilizar. Em um grau de abstração maior, as premissas e instigações são representadas como 
interfaces dos componentes. A Figura 60 ilustra essa representação. Como pode ser 
observado, as premissas das condições são representadas por interfaces requeridas, uma vez 
que as premissas representam serviços que outros componentes devem fornecer para a 
satisfação da regra (ex: atRemoteStatus=true, atTimer=0 e atGateState=CLOSED da regra 
rlOpeningGate). Por outro lado, as instigações das ações são representadas pelas interfaces 
fornecidas, uma vez que as instigações fornecem ações para a alteração dos elementos FBEs  
(ex: statusOff() e Opening() que alteram os atributos dos FBEs da regra rlOpeningGate). 
Ambas as interfaces são ligadas ao meio externo por meio de portas. 
 


 
 
 
Figura 60 - Modelo de Compone
Nesta etapa é def
aplicado entre as premissa
das condições das duas regr
Em um nível de ab
de outra forma: como co
rlOpeningGate nesta repre
objetos colaboradores do 
premissas e instigações co
<<NOP_Premise>> ou <<
diferentes, como pode ser o
caso de estudo. Neste caso
não é utilizado. 
entes - Abrir Portão (Passo 2) – Representação das pre
interfaces 
 
finido, pelo valor etiquetado logicalOperato
as de um  <<NOP_Condition>>. Na Figura
ras é representado por “CONJUNCTION”.  
bstração menor, as premissas e instigações po
mponentes ao invés de interfaces. A Figu
esentação. Esta representação ilustra melhor
PON, além de favorecer a identificação
ompartilhadas. Esse compartilhamento sign
<NOP_Instigation>> é compartilhado entre 
observado no Modelo de Componentes da Fig
de compartilhamento, o componente abrang
137 
 
emissas e instigações como 
or, o operador lógico 
a 60 o operador lógico 
odem ser representadas 
ura 61 ilustra a regra 
r a independência dos 
o e representação de 
nifica que um mesmo 
duas ou mais regras 
gura 76 pertencente ao 
gente <<NOP_Rule>> 


138 
 
Figura 61 - Modelo de Compone
 
• Passo 3 – Relacionar a
Uma vez identific
objetos FBE ao modelo e 
componentes estereotipado
e Methods.  A Figura 62 ilu
 
entes - Abrir Portão (Passo 2) – Representação das pre
componentes 
as regras aos FBEs 
 
adas as premissas e as instigações, o próxim
conectá-los às regras. Os FBEs são adiciona
os <<NOP_FBE>>, que encapsulam a repres
ustra a regra rlOpeningGate nesta representaç
 
emissas e instigações como 
mo passo é adicionar os 
ados ao modelo como 
sentação dos Attributes 
ção.  


 
 
 
Figura 
 
Neste passo, fora
estereótipo <<NOP_FBE
representados por interface
(ex: atGateState do Gate)
atributos dos <<NOP_FBE
outro componente solicita 
sugerida essa representação
em um grau de abstração 
<<NOP_Method>>, uma v
A comunicação e
ocorre por meio dos elem
exemplo, conecta o atrib
62 - Modelo de Componentes - Abrir Portão (Passo 3
am adicionados os componentes Remoteco
>>. Os Attributes dos componentes <
es fornecidas, uma vez que o <<NOP_FBE
). Por sua vez, seus Methods, ou as altera
E>>, são representados por interfaces requ
a alteração (ex: atGateState=OPENING do
o, nada impede que os Attributes e Method
menor, como componentes estereotipados <
vez que o NOP Profile suporta esses estereótip
entre os componentes internos da regra e o
mentos port (porta) da UML. Na Figura 6
buto atRemoteStatus do componente Remo
139 
 
3) 
ontrol e Gate com o 
<<NOP_FBE>> são 
>> fornece o atributo 
ações diretas sobre os 
ueridas, uma vez que 
o Gate). Apesar de ser 
ds sejam representados 
<<NOP_Attribute>> e 
pos. 
os componentes FBEs 
62, a porta port1, por 
oteControl com uma 


140 
 
premissa do condition_rlOpening, que testa se o valor de atRemoteStatus é verdadeiro. Caso 
todas as premissas sejam satisfeitas, o componente <<NOP_Action>> executa as instigações 
statusOff() e Opening(). Essas instigações também são conectadas aos <<NOP_FBEs>> por 
meio de portas. Por exemplo, a porta port4 conecta a instigação que executa o método 
statusOff() ao RemoteControl e altera o estado do atRemoteStatus  para falso. 
Com o Modelo de Componentes pode-se visualizar a estrutura estática da regra e seu 
relacionamento com os <<NOP_FBEs>>. A Figura 63 exibe o Modelo de Componentes 
completo para o caso de uso “Abrir Portão”, sendo composto das duas regras: rlOpeningGate 
e rlOpenedGate. Por meio deste modelo também é possível identificar as dependências entre 
as regras do sistema. Por exemplo, pode-se observar na Figura 63 que o resultado de uma 
instigação da regra rlOpeningGate,  atGateState=OPENING, é uma premissa da regra 
rlOpenedGate. 


 
 
 
Figura 63 - Modelo de Componentes - Abrir Portão (Passo 3 Completo) 
141 
 


142 
 
4.1.6. Criar Modelo de S
 
O Modelo de Se
aplicação PON, modeland
ordem ou instante em que 
da execução das regras. Est
64 ilustra o processo de
Componentes obtém-se um
Sequência. 
Figura 64 - Ma
O Modelo de Obj
utilização do pacote Core-
componente do Modelo d
premissas e instigações
Componentes, neste Model
Figura 65 ilustra o Modelo
de Objetos não é um mode
Modelo de Componentes, 
criação do Modelo de Sequ
houve este mapeamento de 
 
Sequência 
quência determina a sequência de eventos
do as notificações disparadas entre os objet
elas ocorrem e, consequentemente, é possív
te diagrama baseia-se no diagrama de sequên
e obtenção do Modelo de Sequência: a p
m Modelo de Objetos que serve de base para a
apeamento Modelo de Componentes para Modelo de S
 
etos baseia-se no diagrama de objetos da U
-Object e Core-Association do NOP Profile
e Componentes é substituído por um objet
tenham sido representadas como interfa
lo de Objetos elas também deverão ser subst
o de Objetos do caso de uso “Abrir Portão”.
elo obrigatório, uma vez que ele possui as m
mas apenas converte os “componentes” em
uência. Portanto, quando ele não for modela
componentes para objetos.  
s que ocorre em uma 
tos colaboradores e a 
vel identificar a ordem 
ncia da UML. A Figura 
partir do Modelo de 
a criação do Modelo de 
 
Sequência 
UML e é criado com a 
e. Neste modelo, cada 
to sendo que, caso as 
aces no Modelo de 
tituídas por objetos. A 
No entanto, o Modelo 
mesmas informações do 
m “objetos” visando à 
ado, subentende-se que 


 
 
 
Figura 65 - Modelo de Objetos - Abrir Portão
143 
 


144 
 
Portanto, a partir do modelo da Figura 65 foi possível construir o Modelo de 
Sequência da Figura 67, que será apresentado mais adiante. O Modelo de Sequência, por sua 
vez, faz uso dos pacotes Core-Object, Core-Sequence do NOP Profile.  A fim de facilitar a 
modelagem do sistema, os Modelos de Sequência podem ser criados com um nível de 
abstração maior, no qual os Attributes, Methods, Premise e Instigation são suprimidos. Neste 
modelo são utilizadas mensagens estereotipadas do pacote Core-Sequence que ajudam a 
entender o significado das mensagens trocadas entre os objetos, principalmente quando há a 
supressão de alguns deles. 
A aprovação de uma condição é representada por uma mensagem assíncrona entre os 
objetos <<NOP_Condition>> e <<NOP_Rule>>, que possui uma nota de restrição do tipo 
Pré-condição (Pre-condition) e exibe todas as premissas que participaram da aprovação da 
condição. Esta nota também ajuda a recapitular as premissas que participaram dessa 
aprovação, uma vez que cada uma é aprovada em instantes diferentes da execução do código. 
Essa aprovação também pode ser adicionada ao campo “Condition” de uma mensagem, que 
ilustra a condição entre colchetes (ex: [atRemoteStatus==true && atTimer==0 && 
atGateState==CLOSED]). No entanto, na ferramenta Enterprise Architecture 7.0, o campo 
Condition das mensagens no diagrama de sequência não aceita muitos caracteres. Devido a 
este fato, foi optado por se utilizar as notas de restrições. 
Apesar dos elementos Attribute, Method, Premise e Instigation não aparecerem no 
modelo, subentende-se que eles existem e fazem parte da cadeia de notificações. Mas nada 
impede que o projetista explicite esses elementos, uma vez que o NOP Profile suporta a 
representação dos mesmos. Um exemplo dessa explicitação é a realizada por Simão (2005) no 
diagrama de sequência da Figura 20. 
Para um melhor entendimento do Modelo de Sequência do caso de uso “Abrir 
Portão”, o Modelo de Sequência do caso de uso “Inicialização” é apresentado na Figura 66 
(este caso de uso não foi mencionado no fragmento do SPE em estudo nesta seção, mas 
pertence ao SPE completo). Este caso de uso “Inicialização” ocorre antes do caso de uso 
“Abrir Portão” e é responsável por executar as inicializações do SPE, a instanciação da classe 
Application, assim como as instanciações dos objetos FBE e das regras do sistema.  
Na Figura 66 pode-se observar a existência do objeto myApplication que é uma 
instância da classe SimpleApplication e recebe o estereotipo <<NOP_Application>>.  Na 
instanciação do  myApplication, a estratégia de resolução de conflitos, definida no Modelo de 
Classes pelo valor etiquetado scheduler, é passada como parâmetro ao construtor de 
Application. O myApplication executa o método initFactBase instanciando os objetos FBEs, 


 
 
 
no caso objRemoteControl
de Objetos da Figura 65.  
F
Os objetos objRem
objeto objRemoteControl, 
e objGate. Estes objetos, entre outros, são o
Figura 66 - Modelo de Sequência – Inicialização 
moteControl e objGate, por sua vez, fazem 
por exemplo, cria um Attribute – atR
145 
os mesmos do Modelo 
 
suas inicializações. O 
emoteState – e dois 


146 
 
MethodPointer – mtStatusOn e mtStatusOff que são ponteiros para os métodos statusOn e 
statusOff, respectivamente.  
Na sequência, myApplication executa o método initRules, que instancia duas regras: 
rlOpeningGate 
e 
rlOpenedGate. 
A 
instanciação 
do 
<<NOP_Condition>> 
e 
<<NOP_Action>> ocorrem de maneira implícita ao programador quando uma regra é criada. 
No entanto, a fim de fornecer um melhor entendimento da interação entre os objetos 
colaboradores, a condição e ações das regras são explicitadas no Modelo de Sequência (assim 
como foi feito nos Modelos de Componentes e Objetos). As premissas são adicionadas pelo 
método addPremise da regra, sendo que suas instanciações também ocorrem de maneira 
implícita ao programador neste exemplo. O mesmo ocorre com as instigações que são 
adicionadas pelos métodos addMethod ou addInstigation.  
Uma vez definidas as regras, as instanciações dos <<NOP_FBE>> podem acarretar 
em notificações dos seus Attribute a outros objetos colaboradores do sistema, uma vez que 
essas instanciações podem definir valores iniciais aos Attribute que, por sua vez, geram 
notificações às premissas das regras quando pertinente. Isso pode ser observado na Figura 66, 
em que o objeto <<NOP_FBE>> gera duas notificações à condition_rlOpening (condição da 
regra rlOpeningGate):  atGateState==CLOSED e atTimer==0 .  Estas notificações iniciais 
ocorreram porque, nas suas instanciações, esses atributos foram inicializados e satisfizeram 
duas das premissas da condição da regra rlOpeningGate.  No entanto, como a premissa 
“atRemoteState==true” ainda não foi satisfeita, a regra rlOpeningGate não pode ser 
executada. Este modelo de sequência é finalizado por um loop que aguarda o controle remoto 
ser pressionado.  
Dado o Modelo de Sequência do caso de uma “Inicialização”, a Figura 67 ilustra o 
Modelo de Sequência do caso de uso “Abrir Portão”. 


 
 
 
 Figura 67 - Modelo de Sequência – Abrir Portão 
147 
 


148 
 
No diagrama de Sequência do caso de uso “Abrir Portão” ocorre a aprovação e 
execução das duas regras rlOpeningGate e rlOpenedGate. Uma vez que o controle remoto é 
pressionado no caso de uso “Inicialização”, o Attribute atRemoteStatus tem seu valor alterado 
para true desencadeando a aprovação da regra rlOpeningGate (uma vez que as outras 
premissas já foram aprovadas no caso de uso “Inicialização”). A ação desta regra, 
action_rlOpening, possui duas instigações – statusOff() e Opening() – que alteram os estados 
dos <<NOP_FBE>>. Essas alterações, por sua vez, acarretam na aprovação das premissas da 
regra rlOpened - “atGateState==OPENING” e “atTimer>30” – e, consequentemente, na 
aprovação desta regra. 
Como já visto anteriormente, quando um Attribute tem seu estado alterado, todas as 
Premise que o referenciam recebem a notificação de alteração do estado deste Attribute, 
mesmo que essa alteração não satisfaça a Premise. No entanto, optou-se por abstrair os 
Modelos de Sequência e apenas mostrar aquelas notificações que resultam na aprovação de 
Rules ou aquelas que satisfazem uma Premise mesmo que não aprove a Rule. Porém, todas as 
notificações podem ser explicitadas no Modelo de Sequência a fim de melhor acompanhar o 
desencadeamento no fluxo de notificações. Esta explicitação é importante para analisar a 
estratégia de resolução de conflitos escolhida, que pode alterar a ordem cronológica com que 
as regras são notificadas. Assim, o diagrama de Sequência pode ajudar a analisar essas 
interações prevendo problemas futuros na ordem da execução das regras. 
 
4.1.7. Criar Modelo de Comunicação 
 
O Modelo de Comunicação é baseado no diagrama de Comunicação da UML e 
apresenta as mesmas informações do Modelo de Sequência, mas com enfoque diferente, uma 
vez que este modelo não se preocupada com a cronologia do processo, mas sim como os 
objetos estão vinculados e quais mensagens eles trocam entre si. O Modelo de Comunicação 
faz uso dos pacotes Core-Object e Core-Collaboration do NOP Profile. A Figura 68 exibe o 
Modelo de Comunicação do caso de uso “Abrir Portão” obtido a partir do Modelo de 
Sequência da Figura 67. Por meio do pacote Core-Collaboration é possível aplicar os 
estereótipos nas mensagens trocadas entre os objetos. 
 


 
 
 
Figura 68 - Modelo de Comunicação - Abrir Portão 
149 
 


150 
 
4.1.8. Criar Modelo de Redes de Petri 
 
Como destacado em Doll (2002), na UML, para cada objeto cujo comportamento 
seja relevante, deve ser construído um diagrama de estados que representa todos os estados 
desse objeto. O modelo dinâmico do sistema consiste, portanto, em vários diagramas de 
estados isolados, funcionando concorrentemente, não existindo uma visão dinâmica global. 
Na prática, percebe-se que poucos projetos conseguem construir modelos dinâmicos do 
sistema inteiro em razão da explosão no número de estados. Surge, então, a necessidade de 
representar a visão dinâmica do sistema utilizando uma outra abordagem que evite esta 
limitação. Uma solução para essa limitação é a utilização de redes de Petri na modelagem 
dinâmica de sistemas, como proposto no trabalho de Doll. Algumas das características de 
redes de Petri, ressaltadas por Doll, que as tornam propícias para capturar especificações 
comportamentais, orientadas a objetos e concorrentes são: as redes de Petri permitem a 
modelagem de concorrência, sincronização e compartilhamento de recursos em um sistema; 
além de que existem muitos resultados teóricos associados a redes de Petri para a análise 
comportamental, tais como detecção de bloqueio e análise de desempenho.  
Adicionalmente, como apresentado no capítulo 2, pesquisas realizadas têm mostrado 
a adequabilidade do mapeamento entre regras e as redes de Petri. Dada a sua característica de 
fazer evoluir o estado a partir de regras representadas por transições, as redes de Petri pode ser 
igualmente consideradas como sistema de regras baseados em uma representação na forma: se 
condição então ação. Simão (2005) também destaca a viabilidade da utilização de redes de 
Petri na modelagem de SBRs, e apresentada a compatibilidade entre o metamodelo para 
controle discreto (que originou o PON) e as redes de Petri. 
Dadas essas considerações, optou-se por propor as redes de Petri para realizar a 
modelagem dinâmica do sistema, o que é feito pela criação do Modelo de Redes de Petri do 
DON. Este modelo apresenta a interação dinâmica entre os objetos do sistema e permite fazer 
a validação do modelo por meio da sua simulação ou análise. O DON orienta a criação dos 
Modelos de Redes de Petri por caso de uso e, posteriormente, deve-se fazer a integração de 
todos esses modelos em um único Modelo de Rede de Petri.  
Simão (2005) apresentada a compatibilidade entre o predecessor do PON e as redes 
de Petri, na qual cada regra é interpretada como uma transição, as condições e ações da regra 
são representados pelos arcos, e os estados dos atributos de um elemento são representados 
por lugares na rede. Aproveitando essa interpretação, e adaptando-a conforme a necessidade, 


151 
 
 
 
o Modelo de Rede de Petri do DON pode ser obtido a partir do Modelo de Componentes de 
acordo com o seguinte mapeamento para uma rede de Petri ordinária: 
1. Os componentes estereotipados <<NOP_Condition>>, <<NOP_Rule>> e 
<<NOP_Action>> do Modelo de Componentes são substituídos por transições no 
Modelo de Rede de Petri. 
2. As interfaces ou componentes <<NOP_Premise>> e <<NOP_Instigation>> são 
substituídos por lugares na rede. Além de premissas e instigações, essa 
representação expressa os estados dos atributos de um elemento, uma vez que uma 
premissa ou instigação testa ou altera o estado de um atributo. 
3. Os relacionamentos de notificação também são substituídos por lugares. 
 
A  Figura 69 exibe a rede de Petri obtida a partir do Modelo de Componentes da 
Figura 63, adicionado de um temporizador para controlar o timer do portão. Para o SPE foi 
utilizada uma rede de Petri ordinária, porque esse tipo de rede satisfez as necessidades de 
modelagem do sistema. No entanto, para outros casos pode ser necessário utilizar outros tipos 
de redes. Essa rede foi modelada utilizando-se a ferramenta Visual Object Net++ (DRATH, 
2011). Este tipo de rede explicita a estrutura das regras e a interação entre os objetos 
colaboradores do PON. 
 


152 
 
 
Figura 69 - Modelo de Rede de Petri - Abrir Portão 


153 
 
 
 
Uma vez criadas as redes de Petri de todos os casos de uso, elas devem ser integradas 
em uma única rede que pode possuir um maior nível de abstração. Neste caso, as transições de 
condição (ex: condition_rlOpening) e as transições de ação (ex: action_rlOpening) podem ser 
suprimidas, além dos lugares de notificação (Notifies), gerando assim uma rede de Petri 
resumida em relação à proposta anterior. Esta rede de Petri resumida segue o modelo proposto 
por Simão (2005), no qual as condições e ações da regra são representados pelos arcos, sendo 
que as regras continuam sendo interpretadas como transições e os estados dos atributos 
também continuam sendo representados por lugares na rede. Portanto, para um mapeamento 
direto do Modelo de Componentes para este tipo de rede de Petri resumida, seguem-se as 
seguintes etapas: 
1. Os estereótipos <<NOP_Rule>> dos Modelos de Componentes são substituídos 
por transições na rede de Petri.  
2. Os atributos e seus estados que pertencem aos <<NOP_Premise>>  e aos 
<<NOP_Instigation>> são representados por lugares na rede. 
3. Os estereótipos <<NOP_Premise>> ou interfaces requeridas são representados 
pelos arcos que chegam em uma transição que representa um <<NOP_Rule>>. 
4. Os estereótipos <<NOP_Instigation>> ou interfaces fornecidas são substituídos 
por arcos que saem de uma transição que representa um <<NOP_Rule>>.  
A Figura 70 ilustra o modelo de rede de Petri resumido do caso de uso “Abrir 
Portão”. 
 
Figura 70 - Modelo de Rede de Petri - Abrir Portão - Resumido 


154 
 
Adicionalmente, podem ser adicionados quadrados que envolvam todos os estados de 
um mesmo FBE na rede de Petri a fim de melhor identificar os FBEs, assim como realizado 
por Simão (2005) na Figura 39 da fundamentação. 
 
4.2. 
VERIFICAÇÃO E VALIDAÇÃO 
 
Os modelos UML criados podem ser verificados por meio de funcionalidades 
padrões disponíveis nos sistemas CASEs. No caso do EA, ele permite a realização de 
validações por meio do Model Validation (Validação de Modelo) que permite validar modelos 
UML contra regras UML conhecidas, assim como contra qualquer restrição definida nos 
modelos pelo uso da OCL (SPARX, 2011). O Model Validation pode ser executado para 
validar um elemento individual da UML, um diagrama ou um pacote inteiro, como descrito na 
sequência: 
• Validar um elemento individual da UML assegura que o elemento e seus derivados, 
atributos e operações, e relacionamentos estão de acordo com a sintaxe da UML. 
• Validar um diagrama UML significa validar a corretude do diagrama assim como 
validar qualquer elemento e conectores dentro do diagrama. 
• Validar um pacote UML significa validar o pacote e todos os seus sub-pacotes, 
elementos, conectores e diagramas dentro do mesmo. 
 
Por sua vez, as redes de Petri permitem sua validação aplicando-se técnicas 
conhecidas de análise das mesmas (CARDOSO e VALETTE, 1997). Como já destacado 
anteriormente, as redes de Petri permitem a modelagem de concorrência, sincronização e 
compartilhamento de recursos em um sistema, além de que existem muitos resultados teóricos 
associados a redes de Petri para a análise comportamental, tais como detecção de bloqueio e 
análise de desempenho. A validação de um cenário de interação entre objetos pode ser 
realizada através da elaboração do grafo de alcançabilidade para aquele cenário particular. 
Além disso, as próprias ferramentas de modelagem de redes de Petri permitem a execução do 
modelo e sua análise e validação, como é o caso da ferramenta utilizada Visual Object Net 
++. 
Além disso, os modelos podem ser verificados com respeito às regras próprias do 
PON definidas pelo NOP Profile e suas restrições, e pelo próprio framework PON. Por fim, o 
estudo de caso permite uma validação inicial do método DON.  


155 
 
 
 
Este trabalho não incluiu pesquisas sobre validações dos modelos gerados com o 
DON, sendo que este tema poderá ser objeto de estudo de trabalhos futuros. Além disso, 
outros estudos de caso e experimentos ainda serão necessários e serão conduzidos em 
trabalhos de pesquisa futuros. 
 
4.3. 
CONSIDERAÇÕES SOBRE O DON 
 
Este capítulo apresentou o método de projeto para o PON desenvolvido, o DON 
(Desenvolvimento Orientado a Notificações). Fazendo uso do NOP Profile, o DON guia os 
projetistas no desenvolvimento de projetos em PON por meio de etapas. Basicamente o 
método inicia-se com o levantamento dos requisitos e definição dos casos de usos no Modelo 
de Casos de Uso. Na sequência o projetista deve criar o Modelo de Estados e Alto Nível a fim 
de identificar as regras do software. Uma vez identificadas, as regras têm sua estrutura 
estática modelada, de forma inovadora, pelo Modelo de Componentes. Com esta estrutura 
definida, as regras têm suas interações modeladas nos Modelos de Sequência e de 
Comunicação. Por fim, a modelagem dinâmica das regras é modelada no Modelo de Redes de 
Petri, obtido a partir do mapeamento do Modelo de Componentes.  
Adicionalmente, o método orienta a identificação, definição da estrutura estática e 
dinâmica das regras por caso de uso. No entanto, os Modelos de redes de Petri de cada caso 
de uso devem ser unidos ao final do projeto para uma modelagem dinâmica completa do 
software. 
O método também visa auxiliar a introdução de novos projetistas e programadores 
neste novo paradigma, uma vez que os orienta no entendimento do funcionamento do PON, 
além de evidenciar todos os elementos importantes e necessários em um novo programa em 
PON. 
 
 


156 
 
 
 


157 
 
 
 
5. CASO DE ESTUDO 
 
Este capítulo apresenta um caso de estudo utilizado para validar o método DON 
proposto. O caso de estudo é referente ao Simulador de Portão Eletrônico (SPE) mencionado 
durante essa dissertação. Este sistema foi escolhido por se tratar de um sistema com um 
número de regras pequeno – seis regras –, mas satisfatório para a aplicação e ilustração dos 
resultados obtidos nesta dissertação (originalmente eram oito regras, mas com o uso de 
SubCondition tornaram-se seis). Adicionalmente, este sistema foi implementado no 
Paradigma Orientado a Notificações em C++ (APÊNDICE). 
 
5.1. 
VISÃO GERAL 
 
O programa do caso de estudo é um simulador de portão eletrônico de garagem, 
denominado Simulador de Portão Eletrônico (SPE).  Este programa simula operações básicas 
de abertura e fechamento de um portão, além de interrupções na execução dessas atividades 
como, parar de abrir o portão. As seções seguintes apresentam os resultados de cada uma das 
etapas do método DON. 
 
5.2. 
REQUISITOS 
 
A etapa inicial do método DON é “Capturar Requisitos”. Os requisitos identificados 
para o SPE são os seguintes: 
• O sistema deverá controlar o processo de abertura e fechamento de um portão eletrônico, 
sendo que o portão deve iniciar fechado e possui um contador que começa zerado. 
• O sistema deverá controlar o estado do controle remoto, que pode ser ligado ou desligado, 
e é acionado conforme o desejo do usuário 
• Os processos de abertura e de fechamento do portão duram 30 segundos cada um.  
• Estando o portão fechado, o sistema deverá iniciar abertura do mesmo quando o controle 
remoto for pressionado e, após 30 segundos, o portão estará aberto. O contador deverá ser 
zerado após a abertura completa do portão. 
• Uma vez aberto o portão, e caso o controle remoto seja pressionado novamente, o sistema 
deverá iniciar o processo de fechamento do portão, que estará completamente fechado 
após 30 segundos. 


158 
 
• Durante o processo de abertura do portão, em que não se passaram ainda os 30 segundos, 
caso haja uma interrupção do controle remoto, o portão pára de abrir ficando semi-aberto. 
Apertando-se o controle novamente o portão volta a fechar. 
• O mesmo pode ocorrer durante o processo de fechamento do portão em que não 
completaram-se os 30 segundos. Caso o controle remoto seja pressionado, o portão pára 
de fechar ficando semi-aberto. Com uma nova interrupção do controle remoto o portão 
retorna ao processo de abertura. 
 
5.3. 
MODELO DE CASOS DE USO 
 
Uma vez definidos os requisitos do sistema foi possível passar para a etapa “Criar 
Modelo de Casos de Uso”. Para o SPE foram obtidos os seguintes atores e casos de uso:  
Atores 
• Portão Eletrônico – representa o portão eletrônico e pode assumir os estados fechado, 
abrindo, aberto, fechando, parar de abrir e parar de fechar. O portão também possui um 
contador para controlar seu tempo de abertura. 
• Controle Remoto – representa o controle remoto e pode assumir os estados “ligado” e 
“desligado”. 
• Usuário – pessoa que controla o controle remoto. 
 
Casos de Uso 
• Inicialização– define as configurações iniciais do sistema. 
• Abrir Portão – define o início da abertura do portão.  Considera-se que o portão inicia-se 
fechado e, uma vez que o controle remoto é pressionado, o portão começa a abrir. Após 30 
segundos o portão está aberto. 
• Fechar Portão – define o início o fechamento do portão.  Considera-se que o portão está 
aberto e, uma vez que o controle remoto é pressionado, o portão começa a fechar. Após 30 
segundos o portão está fechado. 
• Parar Portão – uma vez que o portão esteja sendo aberto ou fechado, caso o controle 
remoto seja pressionado, o portão interrompe sua operação. Caso o controle remoto seja 
pressionado novamente, o portão inicia a operação contrária a que ele estava executando 
quando foi interrompido. 
 


 
 
 
A Figura 71 ilustra
Fig
 
5.4. 
MODELO DE CL
 
A Figura 72 ilustr
Modelo de Casos de Uso.
SimpleApplication estereoti
de conflitos como “BREA
<<NOP_FBE>>: Gate e R
<<NOP_Attribute>>, 
atT
<<NOP_MethodPointer>> 
O atributo atGateState pod
OPENED, 3-CLOSING, 4-
A classe Remot
<<NOP_Attribute>> 
den
<<NOP_MethodPointer>> 
a o Modelo de Casos de Uso obtido. 
gura 71 - Caso de Estudo - Modelo de Casos de Uso 
ASSES 
ra o Modelo de Classes obtido com a análi
. Foi definida uma nova aplicação em PON
ipada <<NOP_Application>>, que define a e
ADTH”. Além disso, foram criadas duas 
RemoteControl. A classe Gate possui dois at
Timer 
e 
atGateState, 
e 
seis 
mét
- Closed, Closing, Opening, Opened, StopC
de assumir um dos seguintes valores: 0-CLO
-STOP_OPENING e 5-STOP_CLOSING.  
teControl, por sua vez, possui um a
nominado 
atRemoteStatus, 
e 
dois 
mé
- statusOn e statusOff. 
159 
 
se dos requisitos e do 
N por meio da classe 
estratégia de resolução 
classes estereotipadas 
tributos estereotipados 
todos 
estereotipados 
Closing e StopOpening. 
SED, 1-OPENING, 2-
atributo estereotipado 
todos 
estereotipados 


160 
 
 
5.5. 
MODELO DE EST
 
A Figura 73 ilust
modelo e do Modelo de Cl
por caso de uso. 
Figura 7
Figura 72 - Caso de Estudo - Modelo de Classes 
TADOS DE ALTO NÍVEL 
tra o Modelo de Estados de Alto Nível do
lasses foi possível identificar as regras deste 
73 - Caso de Estudo - Modelo de Estados de Alto Nív
 
 
o SPE. A partir deste 
sistema, separando-as 
 
el 


161 
 
 
 
Caso de Uso – Abrir Portão 
a. Regra 1 
Qual o objetivo da regra? Iniciar o processo de abertura do portão. 
O que precisa acontecer para que a regra seja executada? O portão tem que estar no estado 
fechado (CLOSED), o controle remoto tem que ser pressionado e o contador tem que estar 
zerado. 
O que acontece se a regra for executada? O portão deve mudar para o estado abrindo 
(OPENING) e o controle remoto deve ser desligado a fim de simular que ele não está mais 
pressionado. 
 
b. Regra 2 
Qual o objetivo da regra? Abrir o portão efetivamente. 
O que precisa acontecer para que a regra seja executada? O portão tem que estar no estado 
abrindo (OPENING) e o contador do portão tem que ser maior que 30 segundos. 
O que acontece se a regra for executada? O portão deve mudar para o estado aberto 
(OPENED) e o contador deve ser zerado. 
 
c. Regra 3 
Qual o objetivo da regra? Iniciar o processo de abertura do portão caso seu processo de 
fechamento tenha sido interrompido. 
O que precisa acontecer para que a regra seja executada? O portão tem que estar no estado 
parar de fechar (STOP_CLOSING), o controle remoto tem que ser pressionado e o contador 
tem que estar zerado. 
O que acontece se a regra for executada? O portão deve mudar para o estado abrindo 
(OPENING) e o controle remoto deve ser desligado a fim de simular que ele não está mais 
pressionado. 
 
Caso de Uso – Fechar Portão 
d. Regra 4 
Qual o objetivo da regra? Iniciar o processo de fechamento do portão. 
O que precisa acontecer para que a regra seja executada? O portão tem que estar no estado 
aberto (OPENED), o controle remoto tem que ser pressionado e o contador tem que estar 
zerado. 


162 
 
O que acontece se a regra for executada? O portão deve mudar para o estado fechando 
(CLOSING) e o controle remoto deve ser desligado a fim de simular que ele não está mais 
pressionado. 
 
e. Regra 5 
Qual o objetivo da regra? Fechar o portão efetivamente. 
O que precisa acontecer para que a regra seja executada? O portão tem que estar no estado 
fechando (CLOSING) e o contador do portão tem que ser maior que 30 segundos. 
O que acontece se a regra for executada? O portão deve mudar para o estado fechado 
(FECHADO) e o contador deve ser zerado. 
 
f. Regra 6 
Qual o objetivo da regra? Iniciar o processo de fechamento do portão caso seu processo de 
abertura tenha sido interrompido. 
O que precisa acontecer para que a regra seja executada? O portão tem que estar no estado 
parar de abrir (STOP_OPENING), o controle remoto tem que ser pressionado e o contador 
tem que estar zerado. 
O que acontece se a regra for executada? O portão deve mudar para o estado fechando 
(CLOSING) e o controle remoto deve ser desligado a fim de simular que ele não está mais 
pressionado. 
 
Caso de Uso – Parar Portão 
g. Regra 7  
Qual o objetivo da regra? Interromper o processo de abertura do portão. 
O que precisa acontecer para que a regra seja executada? O portão tem que estar no estado 
abrindo (OPENING), o controle remoto tem que ser pressionado e o contador tem que ser 
menor que 30 segundos.  
O que acontece se a regra for executada? O portão deve mudar para o estado parar de abrir 
(STOP_OPENING), o controle remoto deve ser desligado a fim de simular que ele não está 
mais pressionado e o contador deve ser zerado. 
 
h. Regra 8 
Qual o objetivo da regra? Interromper o processo de fechamento do portão. 


163 
 
 
 
O que precisa acontecer para que a regra seja executada? O portão tem que estar no estado 
fechando (CLOSING), o controle remoto tem que ser pressionado e o contador tem que ser 
menor que 30 segundos.  
O que acontece se a regra for executada? O portão deve mudar para o estado parar de 
fechar (STOP_CLOSING), o controle remoto deve ser desligado a fim de simular que ele não 
está mais pressionado e o contador deve ser zerado. 
 
5.6. 
MODELOS DE COMPONENTES 
 
As regras do software, em processo de modelagem, são estruturadas no Modelo de 
Componentes. Cada regra identificada no Modelo de Estados de Alto Nível recebe um nome 
nesta etapa e, com base nas suas descrições definidas no próprio Modelo de Estados de Alto 
Nível e nos atributos e métodos das classes do Modelo de Classes, as premissas e instigações 
são definidas. A fim de facilitar a visualização das regras, as mesmas foram colocadas na 
Tabela 33, que indica qual o caso de uso que a regra pertence, seu nome, suas premissas e 
instigações. 
 
 Tabela 33 - Caso de Estudo - Tabela das Regras 
Caso de 
Uso 
Nome Regra  
Premissas  
Instigações 
Abrir 
Portão 
R1- rlOpeningGate 
atGateState==CLOSED  && 
atRemoteStatus==true 
&&  
atTimer==0 
atGateState=OPENING, 
atRemoteStatus=false 
Abrir 
Portão 
R2 - rlOpenedGate 
atGateState==OPENING 
&& 
atTimer>30 
atGateState=OPENED,  
atTimer=0 
 
Abrir 
Portão 
R3 
- 
rlOpeningStoppedGate 
atGateState==STOP_CLOSING 
&& atRemoteStatus==true &&  
atTimer==0 
atGateState=OPENING, 
atRemoteStatus=false 
Fechar 
Portão 
R4 - rlClosingGate 
atGateState==OPENED 
&& 
atRemoteStatus==true 
&& 
atTimer==0 
 
atGateState=CLOSING,   
atRemoteStatus=false 
 
Fechar 
Portão 
R5 - rlClosedGate 
atGateState==CLOSING 
&& 
atTimer>30 
atGateState=CLOSED,  
atTimer=0 
Fechar 
R6 
- 
atGateState==STOP_OPENING 
atGateState=CLOSING, 


164 
 
Portão 
rlClosingStoppedGate 
&& atRemoteStatus==true && 
atTimer==0 
atRemoteStatus=false 
Parar de 
Abrir 
R7 
- 
rlStopOpeningGate 
atGateState==OPENING 
&& 
atRemoteStatus==true 
&& 
atTimer<30 
atGateState=STOP_OPENING,  
atRemoteStatus=false, 
atTimer=0 
Parar de 
Abrir 
R8 - rlStopClosingGate 
atGateState==CLOSING 
&& 
atRemoteStatus==true 
&& 
atTimer<30 
atGateState=STOP_CLOSING,  
atRemoteStatus=false, 
atTimer=0 
 
Uma vez definidas suas premissas e instigações as regras são modeladas do Modelo 
de Componentes, sendo que é criado um modelo por caso de uso. No exemplo em questão, 
apenas não foi criado um modelo de componentes para o caso de uso “Inicialização”, uma vez 
que não foram identificadas regras para o mesmo. 
A Figura 74 ilustra o Modelo de Componentes do caso de uso “Abrir Portão”. Neste 
modelo optou-se por representar as premissas e instigações por interfaces e representar a regra 
sem o componente maior abrangente. Pode-se observar neste modelo que, apesar de terem 
sido definidas três regras neste caso de uso, há apenas duas regras modeladas. Isto ocorreu 
porque, durante a modelagem do Modelo de Componentes, foi identificado que as regras 
rlOpeningGate e rlOpeningStoppedGate possuíam duas premissas compartilhadas – 
atRemoteStatus==true &&  atTimer==0 – e todas as instigações compartilhadas –  
atGateState=OPENING e atRemoteStatus=false. Este cenário sugere que não há necessidade 
de criar duas regras, já que as instigações são as mesmas, mas sim criar uma regra e utilizar o 
conceito de subCondition (representado pelo estereótipo <<NOP_SubCondition>>) pelo qual 
é possível adicionar mais de um operador lógico por condição de uma mesma regra. Como 
pode ser observado na Figura 74, a condição da regra rlOpeningGate, denominada 
condition_rlOpening, define um operador lógico de conjunção (CONJUNCTION) a ser 
aplicado entre suas premissas ou, no caso, entre suas sub-condições.  Essa 
condition_rlOpening 
possui 
duas 
sub-condições 
- 
subCond1_rlOpening 
e 
subCond2_rlOpening - sendo que a subCond1_rlOpening também define um operador lógico 
de conjunção a ser aplicado entre suas premissas (atRemoteStatus==true, atTimer==0). Por 
sua vez, a  subCond2_rlOpening define um operador lógico de disjunção (DISJUNCTION) a 
ser aplicado entre suas premissas (atGateState==CLOSED, atGateState==STOP_CLOSING).  


 
 
 
Figura 74 - Case de Estudo - Abrir Portão - Modelo de Componentes 
165 
 


166 
 
Portanto, essa representação de condição da Figura 74 define a seguinte expressão 
lógica: se (atRemoteStatus==true && atTimer==0 && (atGateState==CLOSED || 
atGateState==STOP_CLOSING)) então... .  
A Figura 75 ilustra o Modelo de Componentes criado para o caso de uso “Fechar 
Portão”. O mesmo caso do caso de uso “Abrir Portão” ocorreu para este caso de uso, no qual 
também foram utilizados estereótipos <<NOP_SubCondition>>. Neste caso, foi identificado 
que as regras rlClosingGate e rlClosingStoppedGate possuíam duas premissas compartilhadas 
– atRemoteStatus==true,  atTimer==0 – e todas as instigações compartilhadas –  
atGateState=CLOSING e atRemoteStatus=false – também favorecendo o uso do conceito de 
sub-condições.  
Por sua vez, a Figura 76 apresenta o Modelo de Componentes do caso de uso “Parar 
Portão”. Neste caso de uso foi identificado que cada uma das suas regras – 
rlStopOpeningGate e rlStopClosingGate  – possuem três premissas e três instigações, sendo 
que essas regras compartilham duas premissas e duas instigações. Portanto, ao invés de criar-
se duas premissas “atRemoteStatus=true”, por exemplo, deve ser criada uma só e 
compartilhada entre as duas regras. O mesmo ocorre com as instigações.  Para melhor 
expressar o conceito de compartilhamento de premissas e instigações, estas são representadas 
como componentes no Modelo de Componentes.  


 
 
 
Fig
 
gura 75 - Case de Estudo - Fechar Portão - Modelo de Componentes 
167 
 


168 
 
Figura 76 - Case de Estudo - Parar Portão - Modelo de Componentes 
 


169 
 
 
 
5.7. 
MODELOS DE SEQUÊNCIA 
 
Uma vez definidas as estruturas das regras nos Modelo de Componentes, é possível 
mapear esses modelos para Modelos de Objetos e, a partir destes, obter os Modelos de 
Sequência a fim de determinar a sequência de eventos que ocorre em uma aplicação PON. No 
entanto, os modelos de objetos não serão apresentados nesta seção, subentendendo-se que 
houve este mapeamento.  
A Figura 77 e Figura 78 compõem o modelo de sequência do caso de uso 
“Inicialização”. Neste modelo é apresentada a inicialização do sistema que incluiu a definição 
dos <<NOP_FBE>> e <<NOP_Rule>>. Após a criação desses estereótipos, os Attributes dos 
<<NOP_FBE>> notificam as Premises dos <<NOP_Rule>> quando pertinente. A Figura 78 
ilustra essa situação. As mensagens estereotipadas <<AttributeNotifiesPremise>> e enviadas 
do objeto objGate para o objeto condition_rlOpening ocorreram porque os Attributes do 
objGate pertencem às Premise daquela condição. Adicionalmente, esta figura ilustra que o 
objGate também notificou outro <<NOP_Condition>>, o condition_rlClosing, uma vez que a 
premissa “atTimer==0” também pertence a esta outra condição.  


170 
 
Figura 77 - Case de Estudo - Inicialização - Modelo de Sequência –
 
– Parte 1 


 
 
 
Figura 78 - Case de Estudo - Inicialização - Modelo de Sequência – Parte 2 
 
 
 
171 
 


172 
 
A Figura 79 ilust
antecedido pelo caso de U
Parar de Fechar”. Neste 
rlOpenedGate. A primeir
STOP_CLOSING e atTim
Portão” ou ainda “Parar P
satisfeita no próprio caso 
com que as premissas da r
atTimer>30). Por sua vez,
notifiquem as premissas da
se observar que nesses dia
fim de abstrair o modelo
significado das mensagens
deles. 
 
Figura 79
tra o modelo de sequência do caso de uso 
Uso “Inicialização” ou “Fechar Portão” ou a
caso de uso há a aprovação de duas reg
ra tem duas de suas premissas (atGate
mer==0) satisfeitas no caso de uso “Inici
Portão – Parar de Fechar”, e a terceira (atR
de uso “Abrir Portão”. A aprovação da reg
regra rlOpenedGate sejam aprovadas (atGat
a aprovação da regra rlOpenedGate faz com
a regra rlClosingGate (atTimer==0 e atGateSt
agramas o estereótipo <<NOP_Action>> tam
o. Portanto, os estereótipos de mensagens 
s trocadas entre os elementos quando há ess
9 - Case de Estudo - Abrir Portão - Modelo de Sequên
“Abrir Portão” que é 
ainda “Parar Portão – 
gras rlOpeningGate e 
eState==CLOSED ou 
alização” ou “Fechar 
RemoteStatus==true) é 
gra rlOpeningGate faz 
teState==OPENING e 
m que suas instigações 
tate=OPENED). Pode-
mbém foi suprimido a 
ajudam a entender o 
a supressão de alguns 
 
ncia 


 
 
 
A Figura 80 ilustr
antecedido pelo caso de uso
uso há a aprovação de duas
premissas (atGateState==
satisfeitas no caso de uso 
(atRemoteStatus==true) é s
regra rlClosingGate faz c
(atGateState==CLOSED e 
com que suas instigações n
e atGateState=CLOSED). 
 
Figura 80
A Figura 81 ilustr
Abrir)” que é antecedido p
uso há a aprovação de duas
ra o modelo de sequência do caso de uso “
o “Abrir Portão” ou “Parar Portão – Parar de
s regras rlClosingGate e rlClosedGate. A prim
OPENED ou atGateState==STOP_OPEN
“Abrir Portão” ou “Parar Portão – Parar d
satisfeita no próprio caso de uso “Fechar Po
com que as premissas da regra rlClosedG
atTimer>30). Por sua vez, a aprovação da r
otifiquem duas das premissas da regra rlOpen
0 - Case de Estudo - Fechar Portão - Modelo de Sequên
 
ra o modelo de sequência do caso de uso “P
pelo caso de uso “Inicialização” ou “Fechar P
s regras rlOpeningGate e rlStopOpeningGate
173 
“Fechar Portão” que é 
e Abrir”. Neste caso de 
meira tem duas de suas 
ING e atTimer==0) 
de Abrir”, e a terceira 
rtão”. A aprovação da 
Gate sejam aprovadas 
regra rlClosedGate faz 
ningGate (atTimer==0 
 
ncia 
Parar Portão (Parar de 
Portão”. Neste caso de 
e. A primeira regra tem 


174 
 
duas de suas premissas (a
“Inicialização” ou “Fechar 
caso de uso “Parar Portão
“atGateState==OPENING”
remoto seja pressionado 
“atTimer<30” e atRemoteS
regra rlStopOpeningGate f
regra rlClosing (atTimer==
Figura 81 - Case 
 
A Figura 82 ilustr
Fechar)” que é antecedido p
atGateState==OPENED e atTimer==0) satis
Portão”, e a terceira (atRemoteStatus==true)
”. A aprovação da regra rlOpeningGate faz
” da regra rlStopOpeningGate seja aprovad
antes do término da abertura do portão
Status==true” também são satisfeitas. Por su
faz com que suas instigações notifiquem d
=0 e atGateState=STOP_OPENING).  
 
de Estudo - Parar Portão (Parar de Abrir) - Modelo de
ra o modelo de sequência do caso de uso “P
pelo caso de uso “Abrir Portão” ou “Parar Po
feitas no caso de uso 
 é satisfeita no próprio 
z com que a premissa 
da e, caso o controle 
o, as suas premissas 
ua vez, a aprovação da 
duas das premissas da 
 
e Sequência 
Parar Portão (Parar de 
ortão – Parar de Abrir”. 


 
 
 
Neste caso de uso há a a
primeira regra tem duas de
atTimer==0) satisfeitas no 
terceira (atRemoteStatus==
Fechar”. 
A 
aprovação 
“atGateState==CLOSING”
remoto seja pressionado a
“atTimer<30” e atRemoteS
regra rlStopClosingGate fa
rlOpening (atTimer==0 e a
Figura 82 - Case d
Como pode ser ob
com que as notificações oco
aprovação de duas regras rlClosingGate e 
e suas premissas (atGateState==OPENED o
caso de uso “Abrir Portão” ou “Parar Portão
=true) é  satisfeita no próprio caso de uso “P
da 
regra 
rlClosingGate 
faz 
com 
” da regra rlStopClosingGate seja aprovad
antes do término do fechamento do portã
Status==true” também são satisfeitas. Por su
az com que suas instigações notifiquem duas d
atGateState=STOP_CLOSING).  
de Estudo - Parar Portão (Parar de Fechar) - Modelo d
bservado, os Modelos de Sequência permitem
orrem, além da interação entre os casos de us
175 
rlStopClosingGate. A 
u STOP_OPENING e 
o – Parar de Abrir” e a 
Parar Portão – Parar de 
que 
a 
premissa 
da e, caso o controle 
ão, as suas premissas 
ua vez, a aprovação da 
das premissas da regra 
 
de Sequência 
m modelar a sequência 
sos.  


176 
 
Optou-se, neste caso de estudo, por não criar os Modelos de Comunicação, uma vez 
que eles apresentam as mesmas informações do Modelo de Sequência, mas com enfoque 
diferente. No entanto, para enriquecer a modelagem é interessante fazer uso desses Modelos. 
 
5.8. 
MODELO DE REDES DE PETRI 
 
Por fim, o Modelo de Redes de Petri tem por objetivo modelar a dinâmica entre os 
elementos do PON. A interação dos objetos começa a ser analisada nos Modelos de 
Sequência, mas é no modelo de Redes de Petri que essa interação é efetivamente modelada. 
Neste caso de estudo foi criada uma rede de Petri resumida por meio do mapeamento de cada 
Modelo de Componentes para uma única rede de Petri: 
1. Os estereótipos <<NOP_Rule>> dos Modelos de Componentes são substituídos 
por transições na rede de Petri.  
2. Os atributos e seus estados que pertencem aos <<NOP_Premise>>  e aos 
<<NOP_Instigation>> são representados por lugares na rede. 
3. Os estereótipos <<NOP_Premise>> ou interfaces requeridas são representados 
pelos arcos que chegam em uma transição que representa um <<NOP_Rule>>. 
4. Os estereótipos <<NOP_Instigation>> ou interfaces fornecidas são substituídos 
por arcos que saem de uma transição que representa um <<NOP_Rule>>.  
A Figura 83 ilustra o Modelo de Redes de Petri criada para este caso de estudo. Os 
estados inicias desta rede são representados pelas fichas nos lugares “atGateState=CLOSED”, 
“atRemoteStatus=false” e “atTimer=0”. A rede inicia sua execução quando uma ficha é 
colocada no lugar “Pressionar botão”, que dispara a transição “Ativando” colocando uma 
ficha no lugar “atRemoteStatus=true”, retirando a ficha do lugar “atRemoteStatus=false” . 
Este 
estado 
“atRemoteStatus=true”, 
por 
sua 
vez, 
juntamente 
com 
os 
estados 
“atGateState=CLOSED” e “atTimer=0” disparam a transição rlOpeningGate. Uma vez 
disparada essa transição rlOpeningGate, são removidas as fichas dos estados atuais e 
colocadas nos estados “atRemoteStatus=false” e “atGateState=OPENING”, e assim por 
diante. Como foi visto, a ativação do controle remoto é simulada pela inserção de uma ficha 
no lugar “Pressionar botão”. 
 O mapeamento de cada Modelo de Componentes para redes de Petri parciais que 
depois são unidas em uma só, ou diretamente para uma única rede, facilita enormemente a 
criação dessas redes de Petri. Com a rede de Petri criada é possível executá-la e analisar, de 


177 
 
 
 
forma efetiva, a dinâmica do sistema como um todo. Com a simulação das redes de Petri é 
possível, por exemplo, identificar estados que foram modelados erroneamente e podem 
interromper a execução do sistema. Além disso, no caso do PON, é possível observar a 
interação entre as regras e a ordem com que elas são executadas. 
 
 
Figura 83 - Caso de Estudo - Modelo de Redes de Petri 
 
5.9. 
CONSIDERAÇÕES SOBRE O CASO DE ESTUDO  
 
Neste capítulo foi apresentado um caso de estudo, em que o método DON é utilizado 
na especificação de um Simulador de Portão Eletrônico. A visão geral do processo de análise 
e projeto de um sistema, baseado no processo unificado e adotando o método DON, é 
mostrada de forma detalhada.  
O método proposto, juntamente com o NOP Profile, facilita a modelagem de 
sistemas em PON uma vez que, se fosse utilizada UML convencional, os conceitos do PON 
não seriam apropriadamente modelados. A utilização do perfil é simplificada e não exige que 
o usuário seja um especialista em perfis UML. O usuário deve importar o perfil UML e 
utilizar o padrão “Arrastar e Soltar” ao qual está acostumado, uma vez que os estereótipos 


178 
 
ficam disponíveis no menu da ferramenta de modelagem. Além disso, o caso de estudo 
mostrou que o método é satisfatório na identificação de regras e, a estruturação das mesmas 
no Modelo de Componentes, auxilia na identificação de possíveis SubConditions, além de 
premissas e instigações compartilhadas. Adicionalmente, a estruturação das regras em 
componentes facilita o mapeamento das mesmas para as redes de Petri. 
Assim, pode-se mais facilmente modelar um sistema em PON aplicando-se as etapas 
do método DON. Através do estudo de caso mostrado neste capítulo, pôde-se observar que o 
perfil e o método são apropriados para a modelagem de sistemas em PON.  
 
 
 
 


179 
 
 
 
6. CONCLUSÕES  
 
Com o objetivo de propor uma solução para um conjunto de deficiências dos 
paradigmas de programação atuais, foi desenvolvido o Paradigma Orientado a Notificações 
(PON). O PON unifica as principais características e vantagens dos SBRs – como a 
representação do conhecimento na forma de regras – e do POO – como a flexibilidade de 
expressão e nível apropriado de abstração – propondo resolver várias de suas deficiências em 
aplicações de software monoprocessado e multiprocessado. Entre essas deficiências, podem 
ser citadas a sintaxe inapropriada, redundâncias estruturais e temporais, e acoplamento forte 
entre as entidades computacionais (SIMÃO e STADZISZ, 2008). 
O PON tem sido materializado em termos de programação, mas não possuía ainda 
um método formalizado para orientar os desenvolvedores na elaboração de projetos de 
software. Embora seja possível o emprego convencional da UML e processos conhecidos no 
desenvolvimento de software com o PON, suas especialidades motivam o uso mais 
particularizado de linguagens de modelagem e processos de software. 
Diante deste cenário, o objetivo deste trabalho foi estudar e propor um método para 
guiar os projetistas de software na elaboração de projetos específicos com o PON. Como pode 
ser observado no capítulo 2 de fundamentação do trabalho, existem propostas para a 
especificação de regras como a URML e o PPR, mas que não se aplicaram apropriadamente 
ao PON, justamente pelo PON envolver conceitos particulares em seu framework, que não se 
adaptam às propostas existentes.  
Portanto, com base na lacuna identificada foi proposto um método para auxiliar na 
elaboração de projetos de software que utilizam o PON, que pode ser aplicado em processos 
de software conhecidos, como o RUP, especialmente nas fases de análise e projeto. O método 
foi desenvolvido em duas fases: especificação dos conceitos do PON por meio da criação de 
um perfil UML e definição das etapas para o processo de elaboração de projetos em PON, 
aplicando o perfil UML criado, melhor adequando a UML para a representação de modelos 
em PON. 
O método visou sua compatibilidade com as práticas atuais de engenharia de 
software, porém apresentando técnicas específicas de modelagem orientadas ao 
desenvolvimento de software baseado nesse novo paradigma de programação. 
Pode-se concluir com o trabalho desenvolvido, que o método DON apresenta-se 
viável em termos de compatibilidade com o PON, UML e RUP. Além disso, por meio de 


180 
 
estudos práticos e do caso de estudo, verificou-se a viabilidade e interesse prático na sua 
utilização. O DON simplifica e fornece uma orientação para desenvolvimento de modelos 
UML particulares para o PON. 
 
6.1. 
CONTRIBUIÇÕES 
 
Como contribuições deste trabalho, pode-se destacar: 
• A criação do NOP Profile que viabiliza a modelagem em UML de programas em 
PON. 
• A formalização parcial dos elementos do framework do PON por meio do NOP 
Profile. 
• O método se apresenta iterativo podendo se adequar a processos de software como o 
RUP. 
• O método DON oferece suporte para a criação de programas em PON, provendo 
orientação desde a identificação das regras e a modelagem das mesmas em UML, até o 
mapeamento dessas para as redes de Petri. 
• O método, além de oferecer passos para as construções de programas em PON, 
também evidencia as propriedades essenciais dos elementos do PON que precisam ser 
definidas em nível de projeto ou, pelo menos, ajuda o projetista estar ciente de que 
essas propriedades existem. Isso é dado pelos valores etiquetados definidos nos 
elementos como, por exemplo, logicalOperator, scheduler e exclusive. 
• A utilização da notação UML, que é de fácil entendimento tanto para o meio 
acadêmico quanto ao industrial e possui semântica para transmitir informações aos 
projetistas e desenvolvedores.  
• Portabilidade do NOP Profile, uma vez que ele pode ser salvo no formato XML e 
importado em projetos de software do EA. 
• A utilização de redes de Petri que possuem mecanismos de análise que permitem a 
verificação de propriedades e da corretude do sistema especificado. 
 
 
 
 
 


181 
 
 
 
6.2. 
DIFICULDADES E LIMITAÇÕES 
 
Durante a realização desta dissertação foram encontradas algumas dificuldades e 
limitações, das quais as principais são:  
• Encontrar um guia detalhado sobre os passos para se construir um perfil, uma vez que 
a UML 2.0 limita-se à definição dos conceitos de Perfil UML e seus objetivos, não 
apresentando um guia detalhado sobre os passos para se construir um perfil. Este fato 
também é ressaltado por Selic (2007) que acrescenta que há pouco material publicado 
para guiar os desenvolvedores de Perfis UML. 
• Pelo fato de PON ser um paradigma de programação novo, há pouco material sobre 
modelagem neste paradigma envolvendo especialmente a UML. Na literatura, também 
não foi encontrado muito material sobre modelagens que envolvem os conceitos 
conjuntos de Orientação a Objetos e Sistemas Baseados em Regras. 
• Encontrar ferramentas de modelagem UML adequadas. Não foram encontras 
ferramentas de modelagem UML sem custo que oferecessem suporte à construção de 
perfil UML de forma gráfica e de fácil entendimento e utilização.  
 
6.3. 
TRABALHOS FUTUROS 
 
A fim de dar-se continuidade às atividades realizadas neste trabalho, os seguintes 
trabalhos futuros são sugeridos: 
• Formalizar as restrições do perfil UML, descritas neste trabalho em linguagem natural, 
por meio do seu mapeamento para a linguagem de restrições da UML, a OCL. 
• Fazer experimentos com todas as estratégias de resolução de conflitos das regras e 
analisar o impacto das mesmas na modelagem. 
• Aplicar o DON em diferentes casos de estudos a fim de identificar diferentes cenários 
de modelagem e trazer eventuais evoluções ao DON e ao NOP Profile. 
• Evoluir o método para a modelagem de software multiprocessados em PON. 
• O NOP Profile pode vir a ser evoluído e utilizado em MDA (Metamodel Driven 
Architecture). 
• O NOP Profile permite a modelagem de programas em PON. O mesmo deve ser 
evoluído para permitir a extensão e criação de outros perfis UML.  


182 
 
 
 


183 
 
 
 
REFERÊNCIAS 
 
 
ABDULLAH, M. S. A UML Profile for Conceptual Modelling of Knowledge-Based 
Systems. Thesis, The University of York, Department of Computer Science, 2006. 
 
 
BAKO, B.; VALETTE, R. Towards a Descentralization of Rule-Based Systems 
Controlled by Petri Nets: An Application to FMS. Fourth International Symposium on 
Knowledge Engineering, 1990. 
 
 
BANASZEWSKI, R. F. Advances on Notification Oriented Paradigm. Qualificação de 
Mestrado, Universidade Tecnológica Federal do Paraná - UTFPR, Curso de Pós-Graduação 
em Engenharia Elétrica e Informática Industrial - CPGEI, Curitiba, 2008. 
 
 
BANASZEWSKI, R. F. Paradigma Orientado a Notificações: Avanços e Comparações. 
Dissertação de Mestrado, Programa de Pós-Graduação em Engenharia Eletrônica e 
Informática Industrial (CPGEI), Universidade Tecnológica Federal do Paraná (UTFPR) 
Curitiba-PR. 
Disponível 
em: 
http://arquivos.cpgei.ct.utfpr.edu.br/Ano_2009/dissertacoes/Dissertacao_500_2009.pdf, 2009. 
 
 
BANASZEWSKI, R. F.; SIMÃO, J. M.; TACLA, C. A.; STADZISZ, P. C. Notification 
Oriented Paradigm (NOP) – A Software Development Approach based on Artificial 
Intelligence Concepts. VI Congress of Logic Applied to Technology - LAPTEC, Santos, 
2007. 
 
 
BROOKSHEAR, J. G. Computer Science: An Overview. 9 ed., Addison Wesley, 2006. 
 
 
CARDOSO, J.; VALETTE R. Redes de Petri. Editora da UFSC, 1997. 
 
 
DÖLL, L. M. (2002). Proposta de uma Metodologia para a Modelagem da Ddinâmica de 
Sistemas Orientados a Objetos usando Redes de Petri Predicado/Transição. Dissertação 
de mestrado, CEFET-PR, 2002. 
 
 
DRATH, R. Visual Object Net++. http://www.r-drath.de/Home/Visual_Object_Net++.html. 
Acessado em 15/07/11, 2011. 
 
 
EHRIG, H., et al. Petri Net Transformations. Petri Nets: Theory and Applications, por 
Vedran Kordic, Berlin: I-Tech Education and Publishing, 2008. 
FORGY, C. RETE: A Fast Algorithm for the Many Pattern/Many Object Pattern Match 
Problem. Artificial Intelligence , 19 (1), pp. 17-37, 1982. 
 


184 
 
 
FRIEDMAN-HILL, E. Jess in Action: Java Rule-Based Systems in Java. Greenwich, CT, 
USA: Manning Publications Co, 2003. 
 
 
FUENTES, L.; VALLECILLO, A. An Introduction to UML Profiles. The European Journal 
for the Informatics Professional, Vol. 5, Nº2, 2004. 
 
 
FUENTES, L.; VALLECILLO, A.; TROYA, J.M. Using UML Profiles for Documenting 
Web-Based Application Frameworks. Annals of Software Engineering, 13, pp. pp. 249–
264, 2002. 
 
 
GUEDES, G. T. UML 2: Guia de Consulta Rápida. Novatec, 2005. 
 
 
GUEDES, G. T. UML Uma abordagem Prática. Novatec, 2004. 
 
HE, X.; CHU, W.C.; YANG H.; YANG S. J. H. A New Approach to Verify Rule-Based 
Systems Using Petri Nets. Twenty-Third Annual International Computer Software and 
Applications Conference (IEEE), 1999. 
 
 
KAMBAYASHI, Y.; LEDGARD, H. F. The Separation Principle: A Programming 
Paradigm. IEEE Software , vol. 21, no. 2 , pp. 78-87, 2004 
 
 
KROLL, P.; KRUCHTEN, P. The Rational Unified Process Made Easy: A Practitioner's 
Guide to the RUP. Addison-Wesley, 2003. 
 
 
KRUCHTEN, P. Introdução ao RUP Rational Unified Process. Editora Ciência Moderna, 
2003. 
 
 
LEAL, G. C. Uma Abordagem Integrada de Desevolvimento e Teste de Software para 
Equipes Distribuídas. Dissertação, Programa de Pós-Graduação em Ciência da Computação 
da Universidade Estadual de Maringá, Maringá, 2010. 
 
 
LEE, P.-Y.; CHENG, A. M. HAL: A Faster Match Algorithm. IEEE Transactions on 
Knowledge and Data Engineering, 14 (5), pp. 1047-1058, 2002. 
 
 
LIMA, A. S. UML 2.0: do requisito à solução (3ª ed.). Editora Érica, 2008. 
 
 
LUCCA, J.; SIMÃO, J. M.; BANASZEWSKI, R. F.; STADZISZ, P. C.; TACLA, C. A. 
Interface sobre Meta-modelo de Controle do Simulador ANALYTICE II e suas 


185 
 
 
 
Utilizações para Comparações de Políticas de Controle de Manufatura. Seminário de 
Iniciação Científica e Tecnológica da UTFPR - SICITE 2008, 2008 
 
 
MACHADO, T. L. VISUAL IMML: Um Perfil UML para a Modelagem de Interfaces de 
Usuário. Dissertação, Universidade Federal do Rio Grande do Norte, Departamento de 
Informática e Matemática Aplicada, 2006. 
 
 
MACIEL, P.R.M.; LINS, R. D.; CUNHA, P.R.F. Introdução às Redes de Petri e 
Aplicações. 10ª Escola da Computação. Universidade Federal de Pernambuco, 1996. 
 
 
MELLOR, S.; SCOTT, K.; UHL, A.; WEISE, D. MDA Distilled: Principles of Model-
Driven Architecture. Addison-Wesley, 2004. 
 
 
MIRANKER, D. P. TREAT: A better Match Algorithm for AI Production Systems. 
AAAI'87, (pp. 42-47), 1987. 
 
 
MIRANKER, D. P.; BRANT, D. A.; LOFASO, B.; GADBOIS, D. On the Performance of 
Lazy Matching in Production Systems. 8th National Conference on Artificial Intelligence 
AAAI (pp. 685-692 ). AAAI Press / The MIT Press, 1990. 
 
 
OMG. Meta Object Facility (MOF) Core Specification. Version 2.0, OMG document 
formal/06-01-01, 2006. 
 
 
OMG. Meta Object Facility (MOF) Specification. Version 1.4, OMG document 
formal/2002-04-03, 2002. 
 
 
OMG. Object Constraint Language. Version 2.2, OMG document formal/2010-02-01, 
2010. 
 
 
OMG. OMG Unified Modeling Language (OMG UML), Superstructure. Version 2.1.2, 
OMG document formal/2007-11-02, 2007. 
 
 
OMG. OMG Unified Modeling Language Specification. Version 1.5, OMG document 
formal/03-03-01, 2003. 
 
 
OMG. Production Rule Representation (PRR). Version 1.0, OMG document formal/2009-
12-01, 2009. 
 
 


186 
 
OMG. UML Profile and Interchange Models for Enterprise Application Integration 
(EAI) Specification. Version 1.0, OMG document formal/04-03-26, 2004. 
 
 
OMG. UML Profile for CORBA Components. Version 1.0, OMG document formal/05-07-
06, 2005a. 
 
 
OMG. UML Profile for Schedulability, Performance, and Time Specification. Version 
1.1, OMG document formal/05-01-02, 2005b. 
PETERS, J. F.; PEDRYCZ, W. Engenharia de Software Teoria e Prática. Editora Campus, 
2001. 
 
 
POO, D.; KIONG, D. Object-Oriented Programming and Java. Springer, 2008. 
 
 
PRESSMAN, R. Engenharia de Software. Makron Books, 1995. 
 
 
PUN, P. K.; KAHN, H. J. A Multiparadigm Programming Approach for Developing 
Knowledge-Based Systems. 19th International Computer Software and Applications 
Conference (COMPSAC'95), pp.362, 1995 
 
 
REWERSE Working Group I1. UML-Based Rule Modeling Language (URML). 
https://oxygen.informatik.tu-cottbus.de/rewerse-i1/?q=URML. Acessado em 16/05/11, 2011. 
 
 
SCOTT, M. L. Programming Language Pragmatics. San Francisco, CA, USA: Morgan 
Kaufmann Publishers Inc, 2000. 
 
 
SELIC, B. A Systematic Approach to Domain-Specific Language Design Using UML. 
10th IEEE International Symposium on Object and Component-Oriented Real-Time 
Distributed Computing (ISORC'07), 2007 
 
 
SIMÃO, J. M. Proposta de uma Arquitetura de Controle para Sistemas Flexíveis de 
Manufatura Baseada em Regras e Agentes. Dissertação de Mestrado, Curso de Pós-
Graduação em Engenharia Elétrica e Informática Industrial (CPGEI) do Centro Federal de 
Educação Tecnológica do Paraná (CEFET-PR), atual Universidade Tecnológica Federal do 
Paraná (UTFPR), , Curitiba-PR , Brazil, 2001. 
 
 
SIMÃO, J. M. A Contribution to the Development of a HMS Simulation Tool and 
Proposition of a Meta-Model for Holonic Control. Double Doctoral Thesis – Tese de 
Doutorado Co-tutelada CPGEI/CEFET-PR/UTFPR (Brasil) & CRAN-UHP (França). Curso 
de Pós-Graduação em Engenharia Elétrica e Informática Industrial (CPGEI) do Centro 
Federal de Educação Tecnológica do Paraná (CEFET-PR), atual Universidade Tecnológica 


187 
 
 
 
Federal do Paraná (UTFPR), Curitiba, Brasil. Centre de Recherche en Automatique de Nancy 
(CRAN) – Université Henri Poincaré (UHP), Nancy, Lorraine, France. Tese Disponível em: 
http://arquivos.cpgei.ct.utfpr.edu.br/Ano_2005/teses/Tese_012_2005.pdf, 2005. 
 
 
SIMÃO, J.M.; FABRO, J.; STADZISZ, P.C.; ARRUDA, L.; ISHIMATSU, S. An Agent-
Oriented Fuzzy Inference Engine. Bauru, 2003. 
 
 
SIMÃO, J.M.; STADZISZ, P.C. An Agent-Oriented Inference Engine applied for 
Supervisory Control of Automated Manufacturing Systems. In: &. J. J. Abe, Advances in 
Logic, Artificial Intelligence and Robotics. Amsterdam, The Netherlands: IOS Press Books, 
2002. 
 
 
SIMÃO, J.M.; STADZISZ, P. C. Paradigma Orientado a Notificações (PON) – Uma 
Técnica de Composição e Execução de Software Orientado a Notificações. Pedido de 
Patente submetida ao INPI/Brazil (Instituto Nacional de Propriedade Industrial) em 2008 e a 
Agência de Inovação/UTFPR em 2007. Nº INPI Efetivo PI0805518-1.Patente submetida ao 
INPI. Brasil, 2008. 
 
 
SIMÃO, J.M.; STADZISZ, P.C. Inference Process Based on Notifications: The Kernel of 
a Holonic Inference Meta-Model Applied to Control Issues. IEEE Transactions on 
Systems, Man and Cybernetics. Part A, Systems and Humans , Vol. 39, Issue 1, 238-250, 
Digital Object Identifier 10.1109/TSMCA.2008.20066371; 2009a. 
 
 
SIMÃO, J.M.; STADZISZ, P.C.; BANASZEWSKI, R. F.; TACLA, C.A. Holonic 
Manufacturing 
Execution 
Systems 
for 
Customised 
and 
Agile 
Production: 
Manufacturing Plant Simulation. V Congresso Brasileiro de Engenharia de Fabricação. 
Artigo disponível em: http://www.grima.ufsc.br/cobef4/files/161019166.pd, 2008. 
 
 
SIMÃO, J.M., STADZISZ, P.C., KÜNZLE, L. Rule and Agent-oriented Architecture to 
Discrete Control Applied as Petri Net Player. 4th Congress of Logic Applied to 
Technology - LAPTEC (101), p. 217, 2003. 
 
 
SIMÃO, J.M.; STADZISZ, P.C.; MOREL, G. Manufacturing Execution System for 
Customized Production. Journal of Material Processing Technology , 179 (1-3), 268, 2006. 
 
 
SIMÃO, J.M.; STADZISZ, P.C.; TACLA, C.A. Holonic Control Meta-Model. IEEE 
Transactions on Systems, Man and Cybernetics. Part A, Systems and Humans, Artigo aceito, 
2009b. 
SPARX 
SYSTEMS. 
. 
Enterprise 
Architect. 
http://www.sparxsystems.com/products/ea/index.html. Acessado em 05/07/2011, 2011. 
 
 


188 
 
WATT, D. Programming Language Design Concepts. J. Willey & Sons (2004). 
 
 
WEBER, L. Viabilidade de Controle Distribuído a partir do Meta-Modelo de Controle. 
PROGRAMA INSTITUCIONAL DE INICIAÇÃO CIENTÍFICA (PIBIC), Relatório Final - 
Bolsista CNPq, UTFPR, 2010. 
 
 
WEBER, L.; Belmonte, D. L.; Banaszewski, R.F.; Stadzisz, P.C.; Simão, J.M. Viabilidade de 
Controle Orientado a Notificações (CON) em Ambiente Concorrente baseado em 
threads. Seminário de Iniciação Científica e Tecnológica da UTFPR - SICITE 2010, 2010. 


189 
 
 
 
APÊNDICE - CÓDIGO FONTE DO SIMULADOR DE PORTÃO 
ELETRÔNICO (SPE) 
 
Este anexo apresenta o código fonte do Simulador de Portão Eletrônico, 
implementado em C++, que foi modelado no caso de estudo do capítulo 0. Este código é 
composto 
por 
seis 
arquivos: 
ISimpleApplication.h, 
SimpleApplication.cpp, 
IRemoteControl.h, RemoteControl.cpp, IGate.h e Gate.cpp.  
 
ISimpleApplication.h 
#ifndef _ISIMPLEAPPLICATION_H_
#define _ISIMPLEAPPLICATION_H_ 
 
#include "IApplication.h" 
#include "IRemoteControl.h" 
#include "IGate.h" 
#include "IScheduler.h" 
#include <vector> 
#include <iterator> 
#include <map> 
 
class SimpleApplication : public Application{ 
 
public: 
 
SimpleApplication(Scheduler* scheduler); 
 
SimpleApplication(int schedulerStrategy); 
 
~SimpleApplication(); 
 
 
 
 
void initRules(); 
 
void initFactBase(); 
 
void initSharedPremises(); 
 
void configureStartApplicationAction(); 
 
void codeApplication(); 
 
private: 
 
Gate* objGate; 
 
RemoteControl* objRemoteControl; 
}; 
 
 
#endif 
 
ISimpleApplication.cpp 
#include "ISimpleApplication.h"
#include "IRuleObject.h" 
 
#include <iostream> 
using std::cout; 
using std::endl; 
using std::cin; 
 
SimpleApplication::SimpleApplication(int 
schedulerStrategy):Application(schedulerStrategy){ 


190 
 
   
this->startApplication();
} 
 
SimpleApplication::~SimpleApplication(){ 
} 
 
void SimpleApplication::initFactBase(){ 
 
 
 
objRemoteControl = new RemoteControl(); 
 
 
objGate = new Gate(); 
} 
 
void SimpleApplication::initRules(){ 
 
 
 
 
RuleObject* rlOpeningGate = new RuleObject("Rule_Opening",scheduler, 
Condition::CONJUNCTION); 
 
rlOpeningGate->addSubCondition(Condition::CONJUNCTION, false); 
       rlOpeningGate->addPremiseToSubCondition(objRemoteControl->atRemoteStatus, 
Boolean::TRUE_NOP, Premise::EQUAL, false ); 
 
rlOpeningGate->addPremiseToSubCondition(objGate->atTimer, 0 , 
Premise::EQUAL, false );  
 
rlOpeningGate->addSubCondition(Condition::DISJUNCTION, false); 
 
rlOpeningGate->addPremiseToSubCondition(objGate->atGateState, 0, 
Premise::EQUAL, false ); //gate=CLOSED 
 
rlOpeningGate->addPremiseToSubCondition(objGate->atGateState, 5, 
Premise::EQUAL, false ); //gate=STOP_CLOSING 
 
rlOpeningGate->addInstigation(objRemoteControl->atRemoteStatus, false); 
 
rlOpeningGate->addMethod(objGate->mtStatusOpening); 
       rlOpeningGate->end();   
 
 
RuleObject* rlOpenedGate = new RuleObject("Rule_Opened",scheduler, 
Condition::CONJUNCTION); 
 
rlOpenedGate->addPremise(objGate->atGateState, 1, Premise::EQUAL, false 
); //gate=OPENING 
 
rlOpenedGate->addPremise(objGate->atTimer, 30 , Premise::GREATERTHAN, 
false ); 
 
rlOpenedGate->addInstigation(objGate->atTimer, 0); 
 
rlOpenedGate->addMethod(objGate->mtStatusOpened); 
       rlOpenedGate->end();   
 
 
 
RuleObject* rlClosingGate = new RuleObject("Rule_Closing",scheduler, 
Condition::CONJUNCTION); 
 
rlOpeningGate->addSubCondition(Condition::CONJUNCTION, false); 
       rlOpeningGate->addPremiseToSubCondition(objRemoteControl->atRemoteStatus, 
Boolean::TRUE_NOP, Premise::EQUAL, false ); 
 
rlOpeningGate->addPremiseToSubCondition(objGate->atTimer, 0 , 
Premise::EQUAL, false );  
 
rlOpeningGate->addSubCondition(Condition::DISJUNCTION, false); 
 
rlOpeningGate->addPremiseToSubCondition(objGate->atGateState, 2, 
Premise::EQUAL, false ); //gate=OPENED 
 
rlOpeningGate->addPremiseToSubCondition(objGate->atGateState, 4, 
Premise::EQUAL, false ); //gate=STOP_OPENING 
 
rlOpeningGate->addInstigation(objRemoteControl->atRemoteStatus, false); 
 
rlOpeningGate->addMethod(objGate->mtStatusClosing); 
       rlOpeningGate->end();   
 
 
 
 
RuleObject* rlClosedGate = new RuleObject("Rule_Closed",scheduler, 
Condition::CONJUNCTION); 
       rlClosedGate->addPremise(objGate->atGateState, 3, Premise::EQUAL, false 
); //gate=CLOSING 
 
rlClosedGate->addPremise(objGate->atTimer, 30 , Premise::GREATERTHAN, 


191 
 
 
 
false );
 
rlClosedGate->addInstigation(objGate->atTimer, 0); 
 
rlClosedGate->addMethod(objGate->mtStatusClosed); 
       rlClosedGate->end();      
 
 
 
Premise* pre_RemoteStatus = new Premise(objRemoteControl->atRemoteStatus, 
Boolean::TRUE_NOP, Premise::EQUAL); 
 
Premise* pre_Timer = new Premise(objGate->atTimer, 30 , 
Premise::SMALLERTHAN, false); 
 
Instigation* inst_RemoteStatus = new Instigation(objRemoteControl-
>atRemoteStatus, false); 
 
Instigation* inst_Timer = new Instigation(objGate->atTimer, 0); 
 
 
 
RuleObject* rlStopOpeningGate = new      RuleObject  ("Rule_StopOpening", 
scheduler , Condition::CONJUNCTION);  
       rlStopOpeningGate->addPremise(pre_RemoteStatus); 
 
rlStopOpeningGate->addPremise(pre_Timer); 
 
rlStopOpeningGate->addPremise(objGate->atGateState, 1, Premise::EQUAL, 
false ); //gate=OPENING 
 
rlStopOpeningGate->addInstigation(inst_RemoteStatus); 
 
rlStopOpeningGate->addInstigation(inst_Timer); 
 
rlStopOpeningGate->addMethod(objGate->mtStatusStopOpening); 
       rlStopOpeningGate->end();   
 
 
RuleObject* rlStopClosingGate = new   RuleObject ("Rule_StopClosing", 
scheduler, Condition::CONJUNCTION); 
       rlStopClosingGate->addPremise(pre_RemoteStatus); 
 
rlStopClosingGate->addPremise(pre_Timer); 
 
rlStopClosingGate->addPremise(objGate->atGateState, 3, Premise::EQUAL, 
false ); //gate=CLOSING 
 
rlStopClosingGate->addInstigation(inst_RemoteStatus); 
 
rlStopClosingGate->addInstigation(inst_Timer);  
 
rlStopClosingGate->addMethod(objGate->mtStatusStopClosing); 
       rlStopClosingGate->end();  
 
} 
 
void SimpleApplication::initSharedPremises(){ 
 
} 
 
void SimpleApplication::configureStartApplicationAction(){ 
 
 
 
} 
 
void SimpleApplication::codeApplication(){ 
 
int remoteControlPressed; 
 
int i; 
 
int count=0; 
 
int timer=0; 
 
 
cout << "Remote control inital status: " << objRemoteControl-> 
atRemoteStatus->getValue() << endl;  
 
cout << "Gate inital status: " << objGate->atGateState->getValue() << 
endl; 
 
cout << "Gate inital status: " << objGate->atTimer->getValue() << endl; 
 
 
for(i=0;i<10;i++) 
 
{ 
 
 
cout << "Press button? [1/0]"; 
 
 
cin >> remoteControlPressed;             
 


192 
 
if (remoteControlPressed == 1)
 
 
{ 
 
 
 
objRemoteControl->atRemoteStatus->setValue(true); 
 
 
} 
 
 
 
 
 
cout << "---------------- " << endl;  
 
 
cout << "Remote control status: " << objRemoteControl-> 
atRemoteStatus->getValue() << endl;  
 
 
cout << "Gate status: " << objGate->atGateState->getValue() << 
endl;  
 
 
cout << "Timer status: " << objGate->atTimer->getValue() << endl;  
 
 
cout << "---------------- " << endl;  
 
 
 
} 
 
 
getchar(); 
 
 
 
} 
 
int main( int argc, char* argv[] ) 
{ 
 
SimpleApplication *myApplication = new   SimpleApplication 
(SchedulerStrategy::BREADTH); 
 
return 0; 
} 
 
 
 
IGate.h 
#ifndef _IGATE_H_
#define _IGATE_H_ 
 
#include "IFBE.h" 
#include "IBoolean.h" 
#include "IInteger.h" 
 
#include <string> 
 
#include <stdio.h> 
#include <windows.h> 
 
using namespace std; 
 
class Gate : public FBE 
{ 
 
private: 
 
 
public: 
 
Gate(void); 
 
~Gate(void); 
 
 
 
//Attributes 
 
Integer * atGateState; 
 
Integer * atTimer; 
 
 
//Methods 
 
void Opened(); 
 
void Closed(); 
 
void Opening(); 


193 
 
 
 
void Closing();
 
void StopOpening(); 
 
void StopClosing(); 
  
static void WINAPI ThreadUm(void*); 
 
static void WINAPI ThreadDois(void*); 
 
void run(); 
 
 
 
MethodPointer<Gate>*         mtStatusOpened; 
 
MethodPointer<Gate>*         mtStatusClosed; 
 
MethodPointer<Gate>*         mtStatusOpening; 
 
MethodPointer<Gate>*         mtStatusClosing; 
 
MethodPointer<Gate>*         mtStatusStopOpening; 
 
MethodPointer<Gate>*         mtStatusStopClosing; 
 
}; 
#endif 
 
IGate.cpp 
#include "IGate.h"
#include <iostream> 
 
using std::cout; 
using std::endl; 
 
/* 
gate states: 
 
0 - closed 
1 - opening  
2 - opened  
3 - closing  
4 - stop opening  
5 - stop closing  
 
*/ 
 
Gate::Gate(void) : FBE(){ 
 
atGateState = new Integer(this, 0); 
 
 
atTimer = new Integer(this, 0); 
 
 
 
mtStatusOpened = new MethodPointer<Gate>(this, &Gate::Opened); 
 
mtStatusClosed = new MethodPointer<Gate>(this, &Gate::Closed); 
 
mtStatusOpening = new MethodPointer<Gate>(this, &Gate::Opening); 
 
mtStatusClosing = new MethodPointer<Gate>(this, &Gate::Closing); 
 
mtStatusStopOpening = new MethodPointer<Gate>(this, &Gate::StopOpening);  
 
mtStatusStopClosing = new MethodPointer<Gate>(this, &Gate::StopClosing); 
} 
 
Gate::~Gate(void){ 
} 
 
void Gate::Closed() 
{ 
 
atGateState->setValue(0); 
 
cout << "Gate closed ... (gate value = " << atGateState->getValue() << 
")" << endl; 
} 
 
void Gate::Opened() 
{ 


194 
 
atGateState->setValue(2);
 
cout << "Gate opened ... (gate value = " << atGateState->getValue() << 
")" << endl; 
} 
 
void Gate::Closing() 
{ 
 
atGateState->setValue(3); 
 
cout << "Gate closing ... (gate value = " << atGateState->getValue() << 
")" << endl; 
 
       unsigned long iID; 
       HANDLE hThreadDois; 
 
hThreadDois = 
CreateThread(NULL,0,(LPTHREAD_START_ROUTINE)Gate::ThreadDois, this,0,&iID); 
 
system("PAUSE>>NULL"); 
       TerminateThread(hThreadDois,0); 
} 
 
void Gate::Opening() 
{ 
 
atGateState->setValue(1); 
 
 
cout << "Gate opening ... (gate value = " << atGateState->getValue() << 
")" << endl; 
 
       unsigned long iID; 
       HANDLE hThreadUm; 
 
hThreadUm = CreateThread(NULL,0,(LPTHREAD_START_ROUTINE)Gate::ThreadUm, 
this,0,&iID); 
 
system("PAUSE>>NULL"); 
       TerminateThread(hThreadUm,0); 
} 
 
void Gate::StopClosing() 
{ 
 
atGateState->setValue(5); 
 
cout << "Gate stopped closing ... (gate value = " << atGateState-
>getValue() << ")" << endl; 
} 
 
void Gate::StopOpening() 
{ 
 
atGateState->setValue(4); 
 
cout << "Gate stopped opening ... (gate value = " << atGateState-
>getValue() << ")" << endl; 
} 
 
void WINAPI Gate::ThreadUm(void* obj) 
{ 
 
Gate* gate = (Gate*) obj; 
 
gate->run(); 
} 
 
void WINAPI Gate::ThreadDois(void* obj) 
{ 
 
Gate* gate = (Gate*) obj; 
 
gate->run(); 
} 
 
void Gate::run() 
{ 


195 
 
 
 
atTimer->setValue(0);
     
 
for(int i=0;i<29;i++) 
 
{ 
 
 
atTimer->setValue(i); 
 
 
 
cout << "timer: " << atTimer->getValue() << endl; 
 
 
Sleep(200); 
 
} 
}
 
 
IRemoteControl.h 
#ifndef _IREMOTECONTROL_H_
#define _IREMOTECONTROL_H_ 
 
#include "IFBE.h" 
#include "IBoolean.h" 
 
class RemoteControl : public FBE 
{ 
public: 
 
RemoteControl(void); 
 
~RemoteControl(void); 
 
 
 
//Attributes 
 
Boolean* atRemoteStatus; 
     
 
//Methods 
 
void statusOn(); 
 
void statusOff(); 
 
 
 
MethodPointer<RemoteControl>*         mtStatusOn; 
 
MethodPointer<RemoteControl>*         mtStatusOff; 
}; 
 
#endif 
 
IRemoteControl.cpp 
#include "IRemoteControl.h"
#include <iostream> 
 
RemoteControl::RemoteControl(void) : FBE(){ 
 
atRemoteStatus = new Boolean(this, false); 
 
 
mtStatusOn = new MethodPointer<RemoteControl>(this, 
&RemoteControl::statusOn); 
 
mtStatusOff = new MethodPointer<RemoteControl>(this, 
&RemoteControl::statusOff); 
} 
 
RemoteControl::~RemoteControl(void){ 
} 
 
void RemoteControl::statusOn(){ 
 
cout << "Remote Control On" << endl; 
 
atRemoteStatus->setValue(true); 
} 
 
 
 


196 
 
void RemoteControl::statusOff(){
 
cout << "Remote Control Off" << endl; 
 
atRemoteStatus->setValue(false);  
} 
 


