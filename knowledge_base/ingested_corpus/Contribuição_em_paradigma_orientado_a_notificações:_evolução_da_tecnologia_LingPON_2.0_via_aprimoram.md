# Contribuição em paradigma orientado a notificações: evolução da tecnologia LingPON 2.0 via aprimoramento da linguagem e compilador para código notificante modular em C++.pdf

UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ 
 
 
 
 
 
LARISSA KEIKO OSHIRO 
 
 
 
 
 
 
CONTRIBUIÇÃO EM PARADIGMA ORIENTADO A NOTIFICAÇÕES: 
EVOLUÇÃO DA TECNOLOGIA LINGPON 2.0 VIA  
APRIMORAMENTO DA LINGUAGEM E COMPILADOR PARA CÓDIGO 
NOTIFICANTE MODULAR EM C++ 
 
 
 
 
 
 
 
 
 
 
CURITIBA 
2021  


 
 
 
 
LARISSA KEIKO OSHIRO 
 
 
 
 
 
 
CONTRIBUIÇÃO EM PARADIGMA ORIENTADO A NOTIFICAÇÕES: 
EVOLUÇÃO DA TECNOLOGIA LINGPON 2.0 VIA  
APRIMORAMENTO DA LINGUAGEM E COMPILADOR PARA CÓDIGO 
NOTIFICANTE MODULAR EM C++ 
Contribution to the Notification Oriented Paradigm:  
NOPL Technology 2.0 Evolution by Language Enhancement and  
Compiler for C++ Notifying Modular Code 
Dissertação apresentada ao Programa de Pós-Graduação 
em Engenharia Elétrica e Informática Industrial da 
Universidade Tecnológica Federal do Paraná, como 
requisito parcial à obtenção do título de Mestra em 
Ciências.  
Área de Concentração: Engenharia de Computação. 
 
Orientador: Prof. Dr. Jean Marcelo Simão 
Coorientador: Dr. Adriano Francisco Ronszcka 
 
 
 
 
 
 
CURITIBA 
2021
 
   4.0 Internacional 
Esta licença permite que outros distribuam, remixem, adaptem e criem a 
partir do seu trabalho, mesmo para fins comerciais, desde que lhe 
atribuam o devido crédito pela criação original. 


 
  
  
LARISSA KEIKO OSHIRO 
CONTRIBUIÇÃO EM PARADIGMA ORIENTADO A NOTIFICAÇÕES: EVOLUÇÃO DA TECNOLOGIA 
LINGPON 2.0 VIA APRIMORAMENTO DA LINGUAGEM E COMPILADOR PARA CÓDIGO NOTIFICANTE 
MODULAR EM C++. 
Trabalho de pesquisa de mestrado apresentado como 
requisito para obtenção do título de Mestra Em Ciências 
da Universidade Tecnológica Federal do Paraná (UTFPR). 
Área de concentração: Engenharia De Computação. 
Data de aprovação: 11 de Novembro de 2021 
Prof Andre Eugenio Lazzaretti, Doutorado - Universidade Tecnológica Federal do Paraná 
Prof Fabiano Silva, Doutorado - Universidade Federal do Paraná (Ufpr) 
Prof Joao Alberto Fabro, Doutorado - Universidade Tecnológica Federal do Paraná 
Prof Roni Fabio Banaszewski, - Universidade Tecnológica Federal do Paraná 
Documento gerado pelo Sistema Acadêmico da UTFPR a partir dos dados da Ata de Defesa em 11/11/2021. 
Ministério da Educação  
Universidade Tecnológica Federal do Paraná  
Campus Curitiba 


AGRADECIMENTOS 
 
 Agradecimentos de ordem pessoal 
Primeiramente, manifesto minha eterna gratidão e dedico este trabalho em memória a 
Rosalino Oshiro, meu querido pai e amigo, que infelizmente veio a falecer durante esse período 
de estudos. Seu exemplo de vida é o meu maior incentivo para vencer em todos os aspectos da 
minha vida, especialmente no profissional. Agradeço imensamente também aos meus 
familiares, em especial à minha querida mãe, Laura Kiyomi Uchida Oshiro, ao meu irmão, 
Aécio Yoshikazu Oshiro, e também à minha cunhada, Heloísa Akiko Miyashita, por estarem 
sempre presentes, incentivando-me e apoiando-me com muito amor e sabedoria, em todos os 
momentos de minha vida.  
Um profundo agradecimento ao filósofo e pacifista budista, Dr. Daisaku Ikeda, quem 
considero como meu mestre da vida, por seus nobres e constantes incentivos.  
Agradeço a todos os meus queridos amigos que de alguma maneira, direta ou 
indiretamente, apoiaram-me e torceram para que eu alcançasse mais essa conquista, além de 
compreender a minha ausência em alguns momentos. 
 
 Agradecimentos de ordem profissional 
Gostaria de agradecer à MPS Informática, em especial aos gerentes Lígia Maria 
Albuquerque e Paulo Jaime, por me permitirem conciliar a realização deste mestrado em 
conjunto com as atividades de trabalho.  
Agradeço profundamente aos orientadores Prof. Dr. Jean Marcelo Simão e Dr. Adriano 
Francisco Ronszcka, pelos incansáveis incentivos, orientações, paciência e compreensão 
durante este período de estudos.  
Agradeço aos professores Dr. André Eugênio Lazzaretti, Dr. Fabiano Silva, Dr. João 
Alberto Fabro e Dr. Roni Fabio Banaszewski, por aceitarem a compor a banca examinadora e 
por disponibilizarem o seu valioso tempo para avaliar este trabalho.  
Agradeço também aos professores, colegas e amigos do grupo de pesquisa, em especial 
ao doutorando Leonardo Faix Pordeus, por estar sempre disposto em ajudar quando era preciso.  
Ainda, gostaria de agradecer à UTFPR e ao CPGEI pela oportunidade de realizar este 
mestrado.  


 
 
 
RESUMO 
OSHIRO, Larissa Keiko. Contribuição para o Paradigma Orientado a Notificações: 
Evolução da Tecnologia LingPON 2.0 via Aprimoramento da Linguagem e Compilador 
para Código Notificante Modular em C++. 2021. 333 f. Dissertação de Mestrado. Programa 
de Pós-Graduação em Engenharia Elétrica e Informática Industrial (CPGEI). – Universidade 
Tecnológica Federal do Paraná, Curitiba, 2021. 
O Paradigma Orientado a Notificações (PON) apresenta uma solução que une a flexibilidade de 
programação do Paradigma Imperativo e a facilidade de programação do Paradigma Declarativo, além 
de proporcionar uma nova visão de programar, estruturar e executar software. O PON apresenta três 
propriedades elementares que consistem em: (a) facilidade de programação em alto nível; (b) eliminação 
de redundâncias que levaria ao desempenho apropriado de execução; e (c) desacoplamento que 
permitiria paralelismo/distribuição implícitos. Para materializar os princípios desse paradigma foram 
desenvolvidas linguagens de programação e um conjunto de compiladores próprios ao PON. Esse 
conjunto de linguagens e compiladores faz parte de uma solução denominada de Tecnologia LingPON, 
a qual se encontra em sua segunda versão, conhecida como Tecnologia LingPON 2.0. Esta deu origem 
à LingPON 2.0, uma linguagem de programação mais completa que a precedente, permitindo a criação 
de aplicações PON em programação de alto nível orientada a regras. A evolução da Tecnologia 
LingPON permitiu, concomitantemente, a criação do MCPON, um método de criação de linguagens e 
compiladores para o PON, bem como a definição de uma única estrutura de dados intermediária em 
formato de grafo de entidades notificantes, nomeada de Grafo PON. O MCPON e o Grafo PON, 
conjuntamente, possibilitam a construção de compiladores para plataformas distintas. Nos últimos anos 
foram implementados alguns compiladores com geradores de código para linguagens-alvo (targets) 
distintos, tanto para software quanto para hardware digital. Dentre eles, destaca-se em software, o 
prototipal compilador para Código Notificante Modular em C++ orientado a Namespaces single-
threaded, implementado para a versão Tecnologia LingPON 1.0, chamado de NPCPP 1.0. Este NPCPP 
1.0 apresentou, em estudos precedentes, o melhor resultado em termos de desempenho para arquitetura 
Von Neumann, mas ainda não como esperado à luz da teoria do PON. Neste âmbito, essa dissertação 
propõe um novo compilador, baseado no sistema de compilação da Tecnologia LingPON 2.0 para o 
target de Código C++ Notificante Modular orientado a Namespaces para a LingPON 2.0 e ajustes desta 
linguagem de programação. Tal compilador, para a LingPON 2.0 com seu gerador de códigos, é 
denominado de NPCPP 2.0. Para demonstrar o NPCPP 2.0 foram realizados alguns experimentos, os 
quais se dão por meio de aplicações padronizadas (benchmarks), advindas tanto do grupo de pesquisa 
do PON quanto externamente. Tais benchmarks foram desenvolvidos em NPCPP 1.0, NPCPP 2.0 e em 
linguagem imperativa (particularmente C++ usual), permitindo, assim, comparações de desempenho. 
Os resultados dos experimentos mostram o desempenho apropriado do NPCPP 2.0, enquanto 
desenvolvimento em alto nível, superando o NPCPP 1.0 e se aproximando dos resultados em C++ usual. 
Ainda, os resultados de experimentos também demonstram uma melhora na estrutura geral dos códigos 
gerados pelo NPCPP 2.0 com código gerado de forma desacoplada. Portanto, esta pesquisa contribui 
com uma materialização que apresenta a viabilidade de duas das três propriedades elementares do PON 
em termos de arquitetura Von Neumann. 
 
 
Palavras-chave: Paradigma Orientado a Notificações, Tecnologia LingPON 2.0, Compilador para o 
PON, Código Notificante Modular em C++, NPCPP 2.0. 


 
 
 
ABSTRACT 
OSHIRO, Larissa Keiko. Contribution to the Notification Oriented Paradigm: NOPL 
Technology 2.0 Evolution by Language Enhancement and Compiler for C++ Notifying 
Modular Code. 2021. 333 f. Dissertação de Mestrado. Programa de Pós-Graduação em 
Engenharia Elétrica e Informática Industrial (CPGEI). Universidade Tecnológica Federal do 
Paraná (UTFPR). Curitiba, 2021. 
The Notification Oriented Paradigm (NOP) presents a solution that combines Imperative Paradigm 
programming flexibility and Declarative Paradigm programming easiness, providing, furthermore, a 
new vision of programming, structuring, and running software. The NOP presents three elementary 
properties, which consist of: (a) easiness in terms of high-level development; (b) redundancy elimination 
that would allow appropriate execution performance; and (c) decoupling that would allow for implicit 
parallelism and/or distribution. A set of programming languages and compilers for this paradigm have 
been developed to materialize the NOP principles. This set of languages and compilers is part of a 
solution called NOPL Technology, which is in its second version named NOPL Technology 2.0. This 
version originated the NOPL 2.0, a complete programming language compared to the previous one, 
which allows the creation of NOP applications in rule-oriented high-level programming. The NOPL 
Technology evolution allows the concurrent development of MCNOP, a method to create programming 
languages and compilers for NOP and a definition of a single intermediate data structure in the format 
of a notifying entity graph, called NOP Graph. The MCNOP, concomitantly with NOP Graph, make it 
possible to build compilers to distinct platforms. Some compilers with code generators have been 
implemented to different targets for software and digital hardware in recent years. Among them, the 
prototypal ‘single-threaded’ C++ Notifying Modular Code oriented to Namespaces’ compiler stands out 
in software implemented for NOPL 1.0 version and is called NPCPP 1.0. In previous research, this 
NPCPP 1.0 presented the best performance for Von Neumann architecture. However, these results were 
still not as proper as when considering the NOP theory. In this context, this M.Sc. dissertation proposes 
a new compiler, based on the NOPL Technology 2.0 compilation system, for C++ Modular Notifying 
Code oriented to Namespaces target for NOPL 2.0 and adjustments of its programming language. This 
compiler, for NOPL 2.0, along with its code generator, is called NPCPP 2.0. To demonstrate NPCPP 
2.0, some experiments were carried out through benchmarks from the NOP research group and external 
benchmarks. These benchmarks were developed using NPCPP 1.0, NPCPP 2.0, and imperative 
programming language (usual C++), allowing performance comparisons. According to the results of the 
experiments, NPCPP 2.0 presents a proper performance in terms of high-level development, surpassing 
NPCPP 1.0 results and achieving approximate results to C++ in terms of performance. Furthermore, the 
results of experiments also demonstrate an improvement in the general structure of generated codes by 
NPCPP 2.0 with decoupled code. Still, the research presents the viability of two of the three elementary 
properties of NOP in Von Neumann architecture. 
 
Keywords: Notifications Oriented Paradigm, NOPL Technology 2.0, NOPL 2.0, NOP Compiler, C++ 
Notifying Modular Code, NPCPP 2.0. 
 
 
 
 
 


 
 
 
LISTA DE ILUSTRAÇÕES 
 
Figura 1 - Exemplo de interação entre as entidades do PON ................................................... 23 
Figura 2 -  Ciclo de notificações entre as entidades do PON ................................................... 24 
Figura 3 - Diagrama de Objetos que representa instância do Grafo PON ................................ 30 
Figura 4 - Visão geral das etapas do MCPON.......................................................................... 31 
Figura 5 - Exemplo genérico de ciclo de notificações entre entidades em PON ...................... 42 
Figura 6 - Diagrama de Blocos Interno em SysML representando as notificações entre entidades 
em PON ................................................................................................................. 43 
Figura 7 - Variante de digrama de instância em UML com relações ....................................... 44 
Figura 8 - Taxonomia de Paradigmas de Programação de Peter Van Roy incluindo o PON .. 46 
Figura 9 - Taxonomia de Paradigmas de Programação incluindo o PON ................................ 52 
Figura 10 - Notificações baseadas em lista encadeada e tabela hash ....................................... 54 
Figura 11 - Exemplo de notificações de um Attribute impertinente ativo ............................... 55 
Figura 12 - Exemplo de notificações desativadas de um Attribute impertinente ..................... 56 
Figura 13 - Exemplo de reativação de uma entidade temporariamente desativada .................. 56 
Figura 14 - Exemplo de notificações com Unique Premise ..................................................... 57 
Figura 15 - Modelo centralizado de resolução de conflitos...................................................... 58 
Figura 16 - Exemplo de Formation Rule .................................................................................. 62 
Figura 17 - Exemplo de Master Rule ....................................................................................... 63 
Figura 18 - Exemplo de Agregação de FBEs ........................................................................... 65 
Figura 19 - Representação ilustrativa de um Grafo PON ......................................................... 70 
Figura 20 - Processo de compilação e os componentes do compilador PON .......................... 73 
Figura 21 - Comparação de tempo de execução do Mira-Alvo em Tecnologia LingPON 
Prototipal................................................................................................................ 73 
Figura 22 - Comparação de tempo de execução (em ms) do.................................................... 77 
Figura 23 - Experimento de tempo de execução entre versões da LingPON ........................... 81 
Figura 24 -  Comparação entre versão estática e versão espaço de nomes para o programa 
Sensores ................................................................................................................. 82 
Figura 25 - Sistema de Compilação Eletivo para o PON ......................................................... 88 
Figura 26 - Modelo Genérico do Grafo PON ........................................................................... 92 
Figura 27 - Exemplo de programa mapeado em uma instância do Grafo PON ....................... 95 
Figura 28 - Etapas e subetapas do MCPON ............................................................................. 97 
Figura 29 - Exemplo de redundâncias em um grafo especializado ........................................ 101 


 
 
 
Figura 30 - Exemplo de bibliotecas com mesmo nome da classe .......................................... 108 
Figura 31 - Materialização da LingPON em Namespaces ..................................................... 109 
Figura 32 - Estrutura do diagrama de classes do sistema de compilação do MCPON .......... 110 
Figura 33 - Principais alterações no código gerado utilizando PThreads .............................. 116 
Figura 34 - Principais alterações no código gerado utilizando Thread Pooling .................... 116 
Figura 35 - Comparação entre as versões Namespace mono e multithreading ...................... 117 
Figura 36 - Representação de instância do Grafo PON 2.0 para a aplicação de Redes de Sensores
 ............................................................................................................................. 122 
Figura 37 - Materialização da LingPON 2.0 em namespaces ................................................ 129 
Figura 38 - Resultado comparativo de implementações do NPCPP 2.0 com e ...................... 147 
Figura 39 - Resultado comparativo de implementações do NPCPP 2.0 com e sem Única 
Premissa .............................................................................................................. 151 
Figura 40 - Resultado comparativo de implementações do NPCPP 2.0 com e sem Premise 
impertinente ......................................................................................................... 155 
Figura 41 -Resultado comparativo com 10% das Rules aprovadas ........................................ 157 
Figura 42 - Resultado comparativo com 40% das Rules aprovadas ....................................... 158 
Figura 43 - Resultado comparativo com 70% das Rules aprovadas ....................................... 158 
Figura 44 - Resultado comparativo com 100% das Rules aprovadas ..................................... 158 
Figura 45 - Resultado comparativo com 10% das Rules aprovadas na EC2 da AWS ........... 159 
Figura 46 - Resultado comparativo com 40% das Rules aprovadas na EC2 da AWS ........... 160 
Figura 47 - Resultado comparativo com 70% das Rules aprovadas na EC2 da AWS ........... 160 
Figura 48 - Resultado comparativo com 100% das Rules aprovadas na EC2 da AWS ......... 160 
Figura 49 - Representação do ambiente simulado pelo CTA ................................................. 162 
Figura 50 - Diagrama de estado da estratégia de controle independente ............................... 164 
Figura 51 - Diagrama de estado da estratégia de controle baseado em congestionamento .... 165 
Figura 52 - Diagrama de classes em UML do Simulador CTA integrado com as estratégias de 
controle em C++ notificante modular orientado a namespaces .......................... 168 
Figura 53 - Gráfico do resultado do experimento com a aplicação do Simulador CTA ........ 173 
Figura 54 - Exemplo de uma sequência bitonic ..................................................................... 174 
Figura 55 - Estágios do processo de ordenação do Bitonic Sort ............................................ 175 
Figura 56 - Resultado comparativo para o Bitonic Sort ......................................................... 178 
Figura 57 - Resultado comparativo para o Bitonic Sort na EC2 da AWS .............................. 179 
Figura 58 - Estrutura das árvores de decisão do Random Forest ........................................... 181 
Figura 59 - Resultado comparativo para o Random Forest na EC2 da AWS ........................ 184 


 
 
 
Figura 60 - Gráfico com resultados do Eletronicgate nas versões ......................................... 191 
Figura 61 - Ordenação dos parâmetros de Methods em LingPON 2.0 e nos códigos gerados
 ............................................................................................................................. 204 
Figura 62 - Resultado comparativo do Bitonic Sort com mais de 64 elementos .................... 332 
 
 
 
 
 
 
 


 
 
 
LISTA DE QUADROS 
Quadro 1 - Propriedades elementares contempladas até a versão 1.2 da Tecnologia LingPON
 ............................................................................................................................... 35 
Quadro 2 - Propriedades elementares contempladas na Tecnologia LingPON 2.0 .................. 35 
Quadro 3 - Propriedades elementares contempladas nas materializações do PON .................. 53 
Quadro 4 - Resumo dos conceitos de programação do PON ................................................... 66 
Quadro 5 - Conceitos de programação contemplados nas materializações do PON ................ 67 
Quadro 6 - Propriedades fundamentais do PON contempladas na Tecnologia LingPON 
Prototipal................................................................................................................ 74 
Quadro 7 - Conceitos de programação PON contempladas na Tecnologia LingPON Prototipal
 ............................................................................................................................... 74 
Quadro 8 - Propriedades fundamentais do PON contempladas na Tecnologia LingPON 1.0 . 78 
Quadro 9 - Conceitos de programação PON contempladas na Tecnologia LingPON 1.0 ....... 78 
Quadro 10 -  Propriedades fundamentais do PON contempladas na Tecnologia LingPON 1.2
 ............................................................................................................................... 83 
Quadro 11 - Conceitos de programação PON contemplados na Tecnologia LingPON 1.2 ..... 83 
Quadro 12 - Propriedades fundamentais do PON contempladas na Tecnologia LingPON 2.089 
Quadro 13 - Conceitos de programação PON contemplados na Tecnologia LingPON 2.0 ..... 90 
Quadro 14 - Subetapas do método MCPON contempladas nos targets das Tecnologias 
LingPON 1.X e 2.0 .............................................................................................. 106 
Quadro 15 - Lista de imperfeições encontradas no NPCPP 1.0 e afinadas no NPCPP 2.0 .... 138 
Quadro 16 - Relação de melhorias propostas no âmbito da Tecnologia LingPON 2.0 e do 
NPCPP 2.0 ........................................................................................................... 139 
Quadro 17 - Relação de número de elementos do PON criados de acordo com o número de 
árvores.................................................................................................................. 183 
Quadro 18 - Lista de melhorias sugeridas para trabalhos futuros .......................................... 202 


 
 
 
LISTA DE CÓDIGOS 
Código 1 - Exemplo de código com redundâncias temporais e estruturais em código C/C++ 20 
Código 2 - Exemplo de criação de FBE e Rule em LingPON .................................................. 29 
Código 3 - Trecho de código do namespace Instantiations, gerado pelo NPCPP 1.0 ............. 33 
Código 4- Exemplo de compartilhamento de Premise para a aplicação de Redes de Sensores na 
LingPON ................................................................................................................ 60 
Código 5 - Exemplo de declaração de FBE Rule para o programa Sensores ........................... 64 
Código 6 - Exemplo de utilização do padrão keeper na LingPON .......................................... 66 
Código 7 - Exemplo de programa implementado em LingPON prototipal .............................. 71 
Código 8 - Exemplo de programa implementado em LingPON 1.0 ........................................ 75 
Código 9 - Exemplo de programa implementado em LingPON 1.2 ........................................ 79 
Código 10 - Exemplo de implementação na NOPL (projeto Sensors) ..................................... 85 
Código 11 - Exemplo de programa a ser mapeado em uma instância do Grafo PON ............. 93 
Código 12 - Exemplo de integração para construção de instâncias do Grafo PON ............... 100 
Código 13 - Exemplo de algoritmo para iteração do Grafo PON .......................................... 102 
Código 14 - Exemplo de geração de código para entidade Premise ...................................... 103 
Código 15 - Método separateMaps() da classe Compiler ...................................................... 110 
Código 16 - Chamada do método separateMaps() da classe Compiler na classe NPCompiler
 ............................................................................................................................. 112 
Código 17 - Trecho do processo de tradução de Rule para C++ notificante modular ............ 112 
Código 18 - Trecho de código gerado para instâncias de FBE na LingPON Namespace ...... 113 
Código 19 - Trecho de código gerado para Premises na LingPON Namespace .................... 114 
Código 20 - Trecho de código gerado para Subcondition na LingPON Namespace ............. 114 
Código 21 - Exemplo de implementação em LingPON 2.0 para a aplicação Redes de Sensores
 ............................................................................................................................. 121 
Código 22 - Arquivo .h da classe Compiler ........................................................................... 123 
Código 23 - Classe NamespacesCompiler.h do NPCPP 2.0 .................................................. 123 
Código 24 - Processo inicial de iteração com o Grafo PON na construção do NPCPP 2.0 ... 124 
Código 25 - Processo de tradução de Attributes para Namespaces ........................................ 125 
Código 26 - Declaração de Instances de FBE do projeto Sensors.pon ................................... 128 
Código 27 - Exemplo de declarações de Instances de FBE no FBE Main do projeto Sensors.pon
 ............................................................................................................................. 129 
Código 28 - Interação entre os namespaces gerados pelo NPCPP 2.0 ................................... 130 


 
 
 
Código 29 - Trecho do arquivo Instance gerado pela implementação em namespaces ......... 131 
Código 30 - Trecho do arquivo Premise gerado pela implementação em namespaces ......... 132 
Código 31 -  Exemplo de Rule que não contém o nível SubCondition e de Rule que o contém
 ............................................................................................................................. 133 
Código 32 - Trecho do arquivo Rule gerado pela implementação em namespaces ............... 135 
Código 33 - Trecho do arquivo Method gerado pela implementação em namespaces .......... 136 
Código 34 - Implementação de Main.cpp em namespaces .................................................... 137 
Código 35 - Adição da verificação se a Premise já estava satisfeita e permaneça com estado 
verdadeiro ............................................................................................................ 140 
Código 36 - Adição do método eql() no namespace Rule ...................................................... 141 
Código 37 - Verificação do estado das Premises no início da execução de um programa .... 142 
Código 38 - Exemplo de Compartilhamento de Premises em LingPON 2.0 para o Bitonic Sort
 ............................................................................................................................. 143 
Código 39 - Exemplo do namespace Premise sem o tratamento de compartilhamento de 
Premise ................................................................................................................ 145 
Código 40 - Exemplo do namespace Premise com o tratamento de compartilhamento de 
Premise ................................................................................................................ 146 
Código 41 - Alteração no arquivo bison.y para inclusão do parâmetro unique ..................... 148 
Código 42 - Exemplo de sintaxe para indicar que a Premise é uma Unique Premise ........... 149 
Código 43 - Alteração no arquivo Premise.cpp do Grafo PON para a inclusão do parâmetro 
unique .................................................................................................................. 149 
Código 44 - Exemplos de declaração de Unique Premise e de Premise padrão em namespaces
 ............................................................................................................................. 150 
Código 45 - Trecho do FBE Semaphore do Simulador CTA com exemplo de Premise 
Impertinente ......................................................................................................... 152 
Código 46 - Alterações no namespace Instances com o tratamento de Premise Impertinente
 ............................................................................................................................. 153 
Código 47 - Alterações no namespace Premises com o tratamento de Premise Impertinente
 ............................................................................................................................. 154 
Código 48 - Parte do arquivo fonte Semaphore em LingPON 2.0 utilizado .......................... 165 
Código 49 - Método da API que notifica a estratégia de controle sobre a alteração de um 
Attribute ............................................................................................................... 169 
Código 50 - Método da API que notifica o semáforo do simulador sobre a alteração de seu 
estado ................................................................................................................... 170 


 
 
 
Código 51 - Trecho do FBE Main em LingPON 2.0 para Bitonic Sort ................................. 175 
Código 52 - Trecho do FBE Comparator  em LingPON 2.0 para Bitonic Sort ..................... 177 
Código 53 - Trecho da implementação do Random Forest em LingPON 2.0 ....................... 182 
Código 54 - Rule do Eletronicgate que contém Methods nos quais serão ............................. 185 
Código 55 - Inclusão dos targets dos gerados de código multithreading no Bison.y ............ 185 
Código 56 - Implementação da criação de PThreads para o NPCPP 2.0 ............................... 186 
Código 57 - Criação de semáforos para a implementação de PThreads ................................ 187 
Código 58 - Código gerado com PThreads resultante da compilação a partir de LingPON 2.0
 ............................................................................................................................. 187 
Código 59 - Código gerado com PThreads, e utilização de semáforos ................................. 188 
Código 60 - Alteração no NPCPP 2.0 para a criação de Thread Pooling .............................. 189 
Código 61 - Código gerado com Thread Pooling resultante da compilação a partir de LingPON 
2.0 ........................................................................................................................ 189 
Código 62 - Método ClosingGate() com implementações para aumentar a carga do 
processamento...................................................................................................... 190 
Código 63 - Exemplo de Methods com expressões aritméticas no parâmetro ....................... 205 
Código 64 - Arquivo .h da classe NamespacesCompiler. ...................................................... 217 
Código 65 - Arquivo .cpp da classe NamespacesCompiler ................................................... 218 
Código 66 - Arquivo Main.nop do programa Rede de Sensores implementado em LingPON 2.0
 ............................................................................................................................. 245 
Código 67 - Arquivo Sector.nop do programa Rede de Sensores implementado em LingPON 
2.0 ........................................................................................................................ 246 
Código 68 - Arquivo Alarm.nop do programa Rede de Sensores implementado em LingPON 
2.0 ........................................................................................................................ 247 
Código 69 - Arquivo Sensor.nop do programa Rede de Sensores implementado em LingPON 
2.0 ........................................................................................................................ 248 
Código 70 - Arquivo Siren.nop do programa Rede de Sensores implementado em LingPON 2.0
 ............................................................................................................................. 248 
Código 71 - Arquivo .h da classe SMSSender utilizada no programa Rede de Sensores ....... 248 
Código 72 - Arquivo .cpp da classe SMSSender utilizada no programa Rede de Sensores ... 248 
Código 73 - Arquivo Instances.h do programa Rede de Sensores pelo NPCPP 2.0 .............. 249 
Código 74 - Arquivo Instances.cpp do programa Rede de Sensores gerado pelo NPCPP 2.0
 ............................................................................................................................. 251 
Código 75 - Arquivo Premises.h do programa Rede de Sensores gerado pelo NPCPP 2.0 .. 255 


 
 
 
Código 76 - Arquivo Premise.cpp do programa Rede de Sensores gerado pelo NPCPP 2.0 257 
Código 77 - Arquivo Rules.h do programa Rede de Sensores gerado pelo NPCPP 2.0 ........ 264 
Código 78 - Arquivo Rules.cpp do programa Rede de Sensores gerado pelo NPCPP 2.0..... 264 
Código 79 - Arquivo Methods.h do programa Rede de Sensores gerado pelo NPCPP 2.0 ... 266 
Código 80 - Arquivo Methods.cpp do programa Rede de Sensores gerado pelo NPCPP 2.0 267 
Código 81 - Arquivo Main.cpp do programa Rede de Sensores gerado pelo NPCPP 2.0 ..... 267 
Código 82 - FBE Main da aplicação do Despertador Eletrônico ........................................... 269 
Código 83 - FBE Despertador da aplicação do Despertador Eletrônico ................................ 270 
Código 84 - FBE Contador da aplicação do Despertador Eletrônico ..................................... 270 
Código 85 - Arquivo .h da classe externa utilizada na aplicação do Despertador Eletrônico 271 
Código 86 - Arquivo .cpp da classe externa utilizada na aplicação do Despertador Eletrônico
 ............................................................................................................................. 271 
Código 87 - Arquivo .h do namespace Instance gerado para a aplicação Despertador Eletrônico
 ............................................................................................................................. 272 
Código 88 - Arquivo .h do namespace Premises gerado para a aplicação Despertador Eletrônico
 ............................................................................................................................. 272 
Código 89 - Arquivo .h do namespace Rules gerado para a aplicação Despertador Eletrônico
 ............................................................................................................................. 273 
Código 90 - Arquivo .h do namespace Methods gerado para a aplicação Despertador Eletrônico
 ............................................................................................................................. 274 
Código 91 - Arquivo Main.nop da estratégia de controle independente em LingPON 2.0.... 275 
Código 92 - Arquivo Semaphore.nop da estratégia de controle independente em LingPON 2.0
 ............................................................................................................................. 275 
Código 93 - Arquivo .h da API SimuladorNamespaceAPI para a ......................................... 278 
Código 94 - Arquivo .cpp da API SimuladorNamespaceAPI para a ...................................... 278 
Código 95 - Arquivo Main.nop da estratégia de controle baseado em................................... 281 
Código 96 - Arquivo Semaphore.nop da estratégia baseado em congestionamento em LingPON 
2.0 ........................................................................................................................ 281 
Código 97 - Arquivo .h da API SimuladorNamespaceAPI para a ......................................... 288 
Código 98 - Arquivo .cpp da API SimuladorNamespaceAPI para a ...................................... 288 
Código 99 - Arquivo .h da classe NamespacesPThreadCompiler ......................................... 293 
Código 100 - Arquivo .cpp da classe NamespacesPThreadCompiler ................................... 294 
Código 101 - Arquivo .h da classe NamespacesTPoolCompiler ........................................... 313 
Código 102 - Arquivo .cpp da classe NamespacesTPoolCompiler ........................................ 314 


 
 
 
LISTA DE ABREVIATURAS E SIGLAS 
 
 
 
SIGLA 
Original 
Tradução 
ARQPON 
Arquitetura de Computador para o Paradigma 
Orientado a Notificações 
Notification-Oriented Computer 
Architecture 
API 
Application Programming Interface 
Interface de Programação de Aplicações 
BNF 
Backus-Naur Form 
Forma de Backus-Naur 
CoPON 
Coprocessador PON 
NOP Coprocessor 
CTA 
Controle de Tráfego Automatizado 
Automated Traffic Control 
DON 
Desenvolvimento Orientado a Notificações 
Notification Oriented Development 
FBE 
Fact Base Element 
Elemento da Base de Fatos 
FPGA 
Field Programmable Gate Array 
Arranjo de Portas Programável em Campo 
ION 
Inferência Orientada a Notificações 
Notification Oriented Inference 
LingPON 
Linguagem do PON 
PON Language 
MCPON 
Método de Compilação para o PON 
PON Compilation Method 
MDE 
Model-Driven Engineering 
Engenharia Orientada a Modelo 
MON 
Metodologia de Projeto de Software 
Orientada a Notificações 
Notification Oriented Software Design 
Methodology 
NOCA 
Notification-Oriented Computer Architecture 
Arquitetura de Processador para o 
Paradigma Orientado a Notificações 
NOPL 
Notification-Oriented Paradigm Language 
Linguagem do Paradigma Orientado a 
Notificações 
NPCPP 
Gerador de Código em C++ Notificante 
Orientado a Namespaces 
Notifying C++ Oriented to Namespaces 
Generator Code 
PD 
Paradigma Declarativo 
Declarative Paradigm 
PF 
Programação Funcional 
Functional Programming 
PI 
Paradigma Imperativo 
Imperative Paradigm 
PON 
Paradigma Orientado a Notificações 
Notification Oriented Paradigm 
POO 
Programação Orientada a Objetos 
Object Oriented Programming 
PP 
Programação Procedimental 
Procedural Programming 
RNA 
Redes Neurais Artificiais 
Artificial Neural Networks 


 
 
 
SUMÁRIO 
1 
INTRODUÇÃO ............................................................................................................... 18 
1.1 
Contextualização - Paradigma Orientado a Notificações ........................................ 19 
1.2 
Motivação ..................................................................................................................... 26 
1.3 
Justificativa .................................................................................................................. 27 
1.4 
Objetivos ....................................................................................................................... 37 
1.5 
Organização do Trabalho ........................................................................................... 38 
2 
FUNDAMENTAÇÃO TEÓRICA .................................................................................. 39 
2.1 
Contextualização Geral sobre o Paradigma Orientado a Notificações ................... 39 
2.1.1 
Bases do Paradigma Orientado a Notificações (PON) .......................................................... 40 
2.1.2 
Materializações do PON ........................................................................................................ 47 
2.1.3 
Propriedades elementares e conceitos de programação do PON ........................................... 52 
2.2 
Visão Geral da Tecnologia LingPON, GRAFO PON E MCPON ........................... 67 
2.2.1 
Método MCPON ................................................................................................................... 68 
2.2.2 
Grafo PON ............................................................................................................................ 69 
2.2.3 
Tecnologia LingPON ............................................................................................................ 70 
2.3 
Detalhamento do Método MCPON ............................................................................ 91 
2.3.1 
Etapas do MCPON ................................................................................................................ 96 
2.3.2 
Materializações do PON à luz do MCPON ......................................................................... 105 
2.4 
Gerador 
de 
Código 
para 
C++ 
Notificante 
Modular 
Orientado 
a 
Namespaces.............. .............................................................................................................. 107 
2.4.1 
Namespaces ou Espaço de Nomes ....................................................................................... 107 
2.4.2 
LingPON e implementação em C++ Notificante Modular orientado a Namespaces Single-
threaded.... .......................................................................................................................................... 108 
2.4.3 
LingPON e implementação em C++ Notificante Modular orientado a Namespaces 
Multithreading ..................................................................................................................................... 115 
2.5 
Considerações sobre o Capítulo................................................................................118 
3 
O COMPILADOR NPCPP 2.0 ..................................................................................... 120 
3.1 
Gerador de Código C++ Notificante Modular Orientado a Namespaces para 
LingPON 2.0 (NPCPP 2.0) ................................................................................................... 121 
3.1.1 
Navegação no Grafo PON e Gerador de Código NPCPP 2.0 ............................................. 122 
3.1.2 
Gerador de Código do NPCPP 2.0 – Construção via Aplicação Redes de Sensores .......... 128 
3.2 
Melhorias da Tecnologia LingPON 2.0 e do NPCPP 2.0 ........................................ 138 
3.2.1 
Aprovação da Premise quando seu estado continua verdadeiro ......................................... 140 
3.2.2 
Verificação dos estados das Premises no início da execução do programa ........................ 142 
3.2.3 
Implementação de Compartilhamento de Premises ............................................................ 143 
3.2.4  
Implementação de Premissa Única ou Unique Premise ...................................................... 147 
3.2.5  
Implementação de Premise Impertinente ............................................................................ 152 
3.3 
Experimentos e Resultados ....................................................................................... 156 
3.3.1 
Aplicação Rede de Sensores ............................................................................................... 156 
3.3.2 
Controle de Tráfego Automatizado (Simulador CTA) ........................................................ 161 
3.3.3 
Bitonic Sort .......................................................................................................................... 173 
3.3.4 
Random Forest .................................................................................................................... 180 
3.4 
Gerador de Código C++ Notificante Orientado a Namespaces Multithreading para 
LingPON 2.0 (NPCPP 2.0 Multithreading) ......................................................................... 184 
3.5 
Considerações ............................................................................................................. 192 


 
 
 
4 
CONCLUSÕES E TRABALHOS FUTUROS ............................................................ 196 
4.1 
Conclusão ................................................................................................................... 196 
4.2 
Trabalhos futuros ...................................................................................................... 202 
4.2.1 
Melhorias apenas no Grafo PON......................................................................................... 203 
4.2.2 
Melhorias na Tecnologia LingPON 2.0 .............................................................................. 204 
4.2.3 
Aumento do conjunto de aplicações em NPCPP 2.0 ........................................................... 206 
4.2.4 
Melhorias no NPCPP 2.0 .................................................................................................... 207 
REFERÊNCIAS ................................................................................................................... 209 
APÊNDICE A ....................................................................................................................... 217 
APÊNDICE B ........................................................................................................................ 245 
APÊNDICE C ....................................................................................................................... 249 
APÊNDICE D ....................................................................................................................... 269 
APÊNDICE E ........................................................................................................................ 275 
APÊNDICE F ........................................................................................................................ 293 
APÊNDICE G ....................................................................................................................... 313 
APÊNDICE H ....................................................................................................................... 332 
 
 
 


18 
 
 
1 INTRODUÇÃO 
Este trabalho de mestrado corresponde a um dos estudos que compõem um projeto de 
pesquisa mais amplo em torno do Paradigma Orientado a Notificações (PON), liderado pelo 
Prof. Jean Marcelo Simão. Este presente esforço de pesquisa, nesta dissertação, consiste na 
construção de um compilador para uma linguagem de programação específica para o PON, 
denominada LingPON. Tal compilador deve gerar códigos para o alvo ou target chamado de 
‘Código Notificante Modular em C++ orientado a Espaços de Nomes ou Namespaces’ 
(NPCPP), sendo que a geração de código neste target se dá a partir de código-fonte 
implementado em LingPON.  
A implementação desse compilador para NPCPP se encontra no âmbito da chamada 
Tecnologia LingPON 2.0, a qual consiste em um conjunto de linguagens e respectivo sistema 
de compiladores, todos harmonizados via um dado método chamado MCPON. Objetivamente, 
o MCPON consiste em um método próprio de criação de linguagens e compiladores elaborado 
para o PON. Substancialmente, tais linguagens e compiladores, conjuntamente em um dado 
sistema de compilação de acordo com o MCPON, são a essência da Tecnologia LingPON 
(RONSZCKA, 2019).  
Em suma, a contribuição deste trabalho diz respeito a um novo compilador que 
permite, à luz da Tecnologia LingPON 2.0, obter código em C++ orientado a notificações e 
organizado via o artifício de namespaces, chamado de NPCPP 2.0, além de ajustes nesta versão 
da Tecnologia LingPON. A intenção fundamental, via este compilador NPCPP 2.0 em 
Tecnologia LingPON 2.0, é alcançar código declarativo em alto nível com performance 
realmente apropriada, cf. preconiza a teoria do PON, via um dado conjunto de benchmarks.  
Neste âmbito, este capítulo apresenta a introdução sobre este presente trabalho. A 
Seção 1.1 descreve a contextualização do tema abordado neste estudo. Em seguida, nas seções 
1.2 e 1.3, são apresentadas, respectivamente, a motivação e a justificativa do trabalho. Ainda, 
na Seção 1.4 são apresentados os objetivos referentes à pesquisa de mestrado. Por fim, na Seção 
1.5 está descrita a organização dos demais capítulos deste presente documento, assim chamado 
de manuscrito de dissertação de mestrado1.    
                                                          
1 Este presente texto ou manuscrito de dissertação de mestrado baseia-se, em partes, no texto prévio da mesma 
autora, em um Trabalho Individual junto ao CPGEI/UTFPR, o qual se constituiu em um formato de qualificação 
de mestrado (OSHIRO, 2020). 


19 
 
 
1.1 
Contextualização - Paradigma Orientado a Notificações  
Os softwares estão cada vez mais inseridos no cotidiano das pessoas, de diversificadas 
maneiras. Por exemplo, há software em equipamentos eletrônicos (como em celulares e 
computadores), em sistemas de segurança (como em câmera ditas inteligentes), em sistemas 
hospitalares (como em monitores de sinais vitais) e no trânsito (como em sistema de radares). 
Isto dito, a alta demanda por desenvolvimento de software tem exigido cada vez mais 
facilitadores e garantias no seu desenvolvimento, o que inevitavelmente envolve a fase de 
programação. No entanto, as linguagens de programação existentes apresentam certas 
deficiências sistêmicas, as quais são oriundas, em geral, em sua base existencial, ou seja, nos 
assim chamados paradigmas de programação (RAYMOND, 2003; BANASZEWSKI, 2009; 
RONSZCKA, 2012; XAVIER, 2014; RONSZCKA, 2019; MENDONÇA, 2020). 
No campo do desenvolvimento de software, cada linguagem de programação pode ser 
classificada, de acordo com suas características (i.e., funcionalidades, estruturação, modo de 
execução, dentre outros fatores), em um ou mais paradigmas de programação. Atualmente, 
pode-se considerar que há dois paradigmas de programação ditos gerais segundo a literatura 
pertinente, nomeadamente o Paradigma Imperativo (PI) e o Paradigma Declarativo (PD) 
(GABBRIELLI e MARTINI, 2010). No entanto, estes paradigmas com os seus subparadigmas, 
por assim dizer, apresentam algumas deficiências (BANASZEWSKI, 2009).  
Neste sentido, há uma certa complexidade na programação do PI, particularmente 
quando em escala, bem como a inflexibilidade técnica de codificação do PD. Mais 
precisamente, no PI, as decisões e os laços de iteração são escritos de forma explícita por meio 
de avaliações lógicos causais (i.e., avaliações de expressões ou ‘regras’ se-então), não raro 
percorrendo ou pesquisando em estruturas de dados. No PD, por sua vez, isto se dá 
principalmente por meio de recursões e/ou de máquinas de inferência, sendo que estas, na 
prática, são implementadas geralmente com linguagens do PI. Em todo caso, tais soluções 
acabam ocasionando alguma e não raro muitas redundâncias temporais (i.e., reavaliações 
desnecessárias no tempo) e redundâncias estruturais (i.e., repetição de estruturas de decisão ao 
longo do código) (BANASZEWSKI, 2009; SIMÃO e STADZISZ, 2009a; GABBRIELLI e 
MARTINI, 2010; SIMÃO et al., 2012a). 
Em suma, as redundâncias temporais e estruturais consequentemente acarretam 
processamento desnecessário e, portanto, em problemas como gasto desnecessário de energia 
elétrica, gastos desnecessários com poder de processamento suplementar e esforços 


20 
 
 
suplementares em desenvolvimento e testes. Ainda, tais redundâncias também acarretam 
efetiva tendência a acoplamentos de unidades de código, dado a interdependência que 
ocasionam. Tais problemas, conjuntamente ou mesmo isoladamente, afetam diretamente o 
desempenho na execução de programas, interferindo inclusive em seu potencial processamento 
paralelo e/ou distribuído (GAUDIOT e SOHN, 1990; BANERJEE et al., 1995; PAN et al., 
1998; RAYMOND, 2003; SIMÃO e STADZISZ, 2009a; SIMÃO et al., 2012a; SCOTT, 2016; 
RONSZCKA, 2019). 
Estas redundâncias até podem ser contornadas nestes paradigmas, mas não sem esforço 
intelectual e mesmo considerável conhecimento técnico. Isto se dá particularmente em PI que é 
industrialmente mais utilizado dado a fatores como inércia cognitiva por ser o primeiro 
paradigma existente e a própria inflexibilidade e idiossincrasias do PD. Entretanto, tal 
conhecimento técnico inevitavelmente leva tempo para se adquirir e, em escala, o tratamento de 
redundâncias pode ser intratável em PI e mesmo em PD (BANASZEWSKI, 2009; SIMÃO e 
STADZISZ, 2009a; SIMÃO et al., 2012a). Neste âmbito, o Código 1 apresenta um exemplo 
típico de código PI, em linguagem de programação C/C++, no qual as usuais redundâncias 
temporais e estruturais são evidenciadas em termos precisos e técnicos. 
 
Código 1 - Exemplo de código com redundâncias temporais e estruturais em código C/C++ 
Fonte: Adaptado de BANASZEWSKI (2009) 
 
Na linha 6 do Código 1, destacada em vermelho, pode-se verificar uma avaliação que 
se repete a cada ciclo iterativo, mesmo que não haja alterações em relação às avaliações 
anteriores. Isto caracteriza uma redundância temporal: o teste '(sensorA_ActiveAlarm == true)' 
será executado toda vez que o laço de repetição (i.e., loop) "while" for executado, independente 
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
...  
n-5 
n-4 
n-3 
n-2 
n-1 
n 
bool sensorA_ActiveAlarm         = true; 
bool sensorB_ActiveAlarm         = false; 
bool sensorB_PresenceDetected    = true; 
// ...  
while ( sensorB_PresenceDetected == true ) { 
       if ( sensorA_ActiveAlarm == true ) { 
             sensorB_ActiveAlarm = true;    
       } 
       if ( ( sensorB_PresenceDetected == true  ) &&  
             ( sensorB_ActiveAlarm        == false ) ) { 
              sensorB_ActiveAlarm = true;  
        } 
       // ...  
       if ( ( sensorB_PresenceDetected == true ) &&  
          ( sensorB_ActiveAlarm           == true ) && 
          ( sensorA_PresenceDetected   == true ) ) { 
             sensorA_ActiveAlarm = true;  
        } 
} 


21 
 
 
da variável ter ou não ter mudado seu estado desde a última vez que foi testada. Por sua vez, a 
redundância estrutural é observada pelas linhas 9 e n-5, destacadas em azul, em que o teste 
'(sensorB_PresenceDetected == true)' é realizado em duas posições do código, sendo 
necessário duas avaliações da mesma variável a cada execução do loop "while". Além disso, 
estas redundâncias podem estar dispersas no código, com n linhas de distância, criando 
dificuldades até mesmo para desenvolvedores experientes tratá-las ou mitigá-las, sendo inviável 
em código de escala considerável. Ainda, tais redundâncias podem representar consideráveis 
desperdícios de processamento (PAN et al., 1998; SIMÃO e STADZISZ, 2009a).  
Além deste código em PI, outros subparadigmas ou técnicas englobadas no PI, no PD 
ou em intersecções deles apresentam situações similares conforme apresentado em (BANERJEE 
et al., 1995; RAYMOND, 2003; SIMÃO e STADZISZ, 2009a; SIMÃO et al., 2012a). Neste 
âmbito das redundâncias salientadas, em suma, a programação procedimental, orientada a 
objetos e mesmo funcional são similares finalmente. Ainda, a programação lógico-declarativa 
em alto nível é usualmente implementada sobre o PI, não necessariamente livres de 
redundâncias. Mesmo em soluções de máquinas de inferência pensadas para não ter 
redundâncias, como os conhecidos algoritmos Rete (FORGY, 1982; CHENG e CHEN, 2000; 
LEE e CHENG, 2002; KANG e CHENG, 2004) e HAL (LEE e CHENG, 2002), ainda há 
algumas redundâncias (SIMÃO e STADZISZ, 2009a; RONSZCKA et al., 2015). Ademais e 
peculiarmente, mesmo nestas máquinas de inferência, o custo de processamento das pesquisas 
nas estruturas de dados tornam o processamento usualmente com maiores "custos de execução 
computacional" que em PI redundante (SIMÃO e STADZISZ, 2009a; BANASZEWSKI, 2009; 
SCOTT, 2016; RONSZCKA, 2019). 
Além do mais, em função das redundâncias, orientação a pesquisas e percorrimentos 
via laços de repetição e similares, os paradigmas vigentes tendem a gerar módulos não 
desacoplados, conforme já previamente salientado. Assim, faz-se necessário conhecimento 
técnico em programação e também modelagem para se obter módulos consideravelmente 
desacoplados. Em todo caso, a modularidade é normalmente almejada para fins diversos como 
organização, reaproveitamento de códigos/módulos, isolamento de erros e processamento 
paralelo e/ou distribuído. Entretanto, obtê-la não é algo evidente nos paradigmas vigentes 
(BROOKSHEAR, 2012; SCOTT, 2016). 
Neste contexto, as deficiências dos atuais paradigmas, dentre outros, foram motivações 
para o desenvolvimento de uma nova técnica chamada Paradigma Orientado a Notificações 
(PON). Historicamente, o PON surge a partir de técnicas precedentes dos assim chamados 
Controle Orientado a Notificações (CON) e Inferência Orientada a Notificações (ION). No 


22 
 
 
PON, assim como no CON e ION, não há laços de repetição com execução forçada e similares, 
uma vez que as interações entre as entidades se dão por notificações pontuais e precisas entre 
elas (SIMÃO, 2001; SIMÃO e STADZISZ, 2002; SIMÃO, 2005; SIMÃO e STADZISZ, 2008; 
SIMÃO e STADZISZ, 2009b). 
De fato, o PON corresponde a um paradigma emergente que foi desenvolvido com o 
objetivo de amenizar alguns problemas dos paradigmas dominantes, nomeadamente o PI e o 
PD. Entretanto, o PON não apenas traz soluções para as deficiências desses paradigmas 
vigentes, como também incorpora algumas de suas vantagens. Neste âmbito, o PON permite a 
programação de forma similar a ‘orientada a objetos’ oriunda do PI, porém com objetos reativo-
notificantes, no tocante ao processamento dito facto-execucional. Tal qual, o PON também 
incorpora em sua essência uma programação ‘baseada em regras’ do PD, para o processamento 
dito lógico-causal, porém com entidade-regras notificáveis (BANASZEWSKI, 2009; 
SANTOS, 2017; RONSZCKA, 2019).  
Assim sendo, o PON é uma técnica que une a facilidade de desenvolvimento em alto 
nível da programação declarativa no tocante ao desenvolvimento lógico-causal e a flexibilidade 
de desenvolvimento do paradigma imperativo no tocante a programação facto-execucional, 
bem as articulando por meio da orientação a notificações. Sobretudo, o PON resolve problemas 
de ambos os paradigmas precedentes no que concerne a execução lógico-causal por não se 
orientar a pesquisas de dados ou laços de repetição ou afins (BANASZEWSKI, 2009; 
SANTOS, 2017; RONSZCKA, 2019). 
Substancialmente, o PON é constituído por dois conjuntos de entidades de 
processamento: o conjunto facto-execucional e o conjunto lógico-causal. O primeiro conjunto 
corresponde a entidades notificantes, os chamados Elementos da Base de Fatos (Fact Base 
Elements - FBE, em inglês). O segundo conjunto, por sua vez, corresponde às entidades 
notificáveis denominadas Regras (Rules, em inglês), que receberão notificações dos FBEs 
(RONSZCKA, 2019). A Figura 1 apresenta, no contexto de um sistema de monitoramento de 
sensores e alarmes, justamente as entidades constituintes do PON e a relação entre os dois 
conjuntos de entidades e seus construtos (OSHIRO et al., 2021). 
 
 
 
 
 
 


23 
 
 
Figura 1 - Exemplo de interação entre as entidades do PON 
 
Fonte: Adaptado de NEVES (2020). 
 
Como mostra a Figura 1, enquanto entidades, os FBEs e as Rules são compostos por 
entidades menores que possibilitam a interação por meio de notificações entre FBEs e Rules e 
vice-versa. Os FBEs são entidades utilizadas para representar estados e serviço de objetos do 
mundo (seja entidades reais, seja entidades abstratas) em sistema computacional 
(BANASZEWSKI, 2009; PORDEUS, 2017; NEVES, 2021; OSHIRO et al., 2021). Por suas 
vezes, as Rules, por serem entidades lógico-causais, gerenciam o conhecimento sobre qualquer 
comportamento lógico-causal do programa. Tal conhecimento lógico-causal usualmente 
provém de uma regra se-então (condição-ação), o que seria uma forma natural de expressão 
deste tipo de conhecimento (BANASZEWSKI, 2009; NEVES, 2021). Na Figura 2 é possível 
visualizar o mecanismo de funcionamento e o ciclo de notificações das entidades do PON, mais 
precisamente das entidades ditas menores e constituintes de FBEs e de Rules.  
 
 
 
 


24 
 
 
Figura 2 -  Ciclo de notificações entre as entidades do PON
 
Fonte: Adaptado de BANASZEWSKI (2009) 
 
Como pode-se observar na Figura 2, o ciclo de notificações ocorre da seguinte 
maneira: (a) quando cada Attribute-FBE tem seu valor alterado, ele notifica somente as 
Premises efetivamente pertinentes; (b) quando cada Premise tem seu valor booleano alterado, 
ela notifica somente as Conditions-Rules efetivamente pertinentes; (c) quando cada Condition-
Rule é aprovada, ela notifica somente as Actions-Rules efetivamente pertinentes; (d) quando 
cada Action-Rule é notificada a executar, ela notifica somente as Instigations efetivamente 
pertinentes; e (e) quando cada Instigation é notificada para executar, ela notifica apenas os 
Methods-FBEs efetivamente pertinentes, os quais podem alterar um ou mais Attributes-FBEs 
pertinentes, realimentando assim o fluxo de notificações (PORDEUS 2017; OSHIRO et al., 
2021). 
Primordialmente, o PON propõe uma nova forma de programação, orientada a regras, 
fatualidades e notificações, sendo que dentre suas propriedades decorrentes se destacam três, 
ditas elementares: 
 
 A facilidade de programação em alto nível, baseada em uma estruturação composta por 
entidades facto-execucionais, na forma de elementos notificantes, e por entidades 
lógico-causais, na forma de regras notificáveis (RONSZCKA et al., 2017; 
RONSZCKA, 2019). 
 


25 
 
 
 A eliminação de redundâncias estruturais (i.e., repetição de código) e temporais (i.e., 
reavaliação desnecessária de expressões), graças à orientação a notificações, o que 
implica em um melhor desempenho na execução de programas (BANASZEWSKI, 
2009; SIMÃO et al., 2012a; RONSZCKA et al., 2015; RONSZCKA, 2019). 
 
 A capacidade de desacoplamento ou acoplamento mínimo (conforme o ponto de vista) 
entre as entidades notificantes e notificáveis, o que possibilita a implementação de 
software com execução paralela e/ou distribuída, dentre outros (BELMONTE et al., 
2016; SCHÜTZ et al., 2018; OLIVEIRA, 2018; NEGRINI, 2019; NEGRINI et al., 
2019; RONSZCKA, 2019). 
 
Com base nestas três propriedades elementares, visando buscar validar as 
características fundamentais do PON, foi elaborado um conjunto de implementações na forma 
de arquétipos ou frameworks sobre linguagens de programação C++ (BANASZEWSKI, 2009; 
RONSZCKA, 2012; VALENÇA 2012; BELMONTE 2012; CHIERICI, 2020; NEVES, 2021), 
C# (HENZEN, 2015; OLIVEIRA, 2019), Java (HENZEN, 2015; BARRETO et al., 2018), 
Erlang/Elixir (NEGRINI, 2019; NEGRINI et al., 2019) e mesmo Akka (MARTINI, 2018), 
atribuindo assim a característica de orientação a notificação a elas.  
Tais implementações ou materializações do PON na forma de frameworks sobre 
linguagens usuais de programação, provendo naturalmente conotação distinta a elas (i.e., 
orientação a notificação), serviram para avaliar a pertinência do paradigma como uma solução 
efetiva para resolver alguns dos problemas de programação presentes em outros paradigmas 
usuais. Entretanto, estes frameworks permitiram validar as características computacionais do 
PON apenas parcialmente, inclusive em função das estruturas de dados utilizadas para viabilizar 
o mecanismo de notificação de maneira genérica (RONSZCKA, 2019).  
Assim sendo, visando melhorar a validação das características fundamentais do PON, 
foi finalmente desenvolvida uma dada linguagem de programação específica para o paradigma, 
certamente em conjunto com um compilador próprio, implementados em um dito ‘ecossistema 
computacional’ denominado Tecnologia LingPON prototipal. Posteriormente, foram 
implementados novos compiladores com targets para plataformas distintas, bem como avanços 
na linguagem LingPON, evoluindo e nomeando esta nova versão do ‘ecossistema’ de 
Tecnologia LingPON 1.0 (FERREIRA, 2015; MELO, 2016; SANTOS, 2017; PORDEUS, 
2017; RONSZCKA et al., 2017; KERSCHBAUMER, 2018; RONSZCKA, 2019; MARTINI et 


26 
 
 
al., 2021). Essa tecnologia toda para construção de linguagens de programação e compiladores 
para o PON foi alvo de aprimoramentos, maturações e avanços consideráveis, sendo que 
atualmente se encontra na versão 2.0, o que naturalmente foi chamada de Tecnologia LingPON 
2.0 (NEGRINI, 2019; NEGRINI et al., 2019; RONSZCKA, 2019; OSHIRO et al., 2021). 
 
1.2 
Motivação 
O surgimento do PON traz a possibilidade de novas contribuições no âmbito de 
sistemas computacionais, uma vez que apresenta uma nova visão para estruturar, executar e 
desenvolver software e mesmo hardware (LINHARES, 2015; RONSZCKA, 2019; SCHÜTZ, 
2019; MENDONÇA, 2020). Em suma, salientado o domínio de software, o PON é uma técnica 
que possibilita a programação em alto nível baseada em regras (assim como nos Sistemas 
Baseado em Regras), bem como possibilita a execução eficiente ao evitar redundâncias 
estruturais e temporais. Além disso, por meio do desacoplamento implícito de seus entes, o 
PON viabiliza a execução paralela e/ou distribuída, se a plataforma alvo assim o permitir 
(FERREIRA, 2015; SANTOS, 2017; NEGRINI, 2019; OLIVEIRA, 2019; RONSZCKA, 
2019).  
Isto dito, o PON é foco de algumas pesquisas na área de software, sendo que para 
materializar seus fundamentos foram elaborados diversos Frameworks (primeiramente um 
Framework C++ em versão prototipal, evoluindo para as versões 1.0, 2.0, 3.0 e 4.0, além de 
Frameworks Java, C#, Akka e Elixir/Erlang), que possibilitaram a construção de aplicações 
PON e a validação de alguns conceitos desse paradigma (NEVES, 2021; NEVES et al., 2021). 
Posteriormente, houve o uso do PON para o desenvolvimento de sistemas em hardware digital 
(HD), bibliotecas de componentes e mesmo com framework em FPGA (Field-Programmable 
Gate Array), o que foi chamado de PON-HD (PORDEUS et al., 2016; KERSCHBAUMER, 
2018; KERSCHBAUMER et al., 2018).  
Não obstante a importância dessas materializações pregressas do PON, tanto para 
evoluir o estado da arte quanto o estado da técnica, nenhuma delas conseguiu alcançar 
efetivamente o potencial das suas três propriedades elementares, as quais são aqui relembradas: 
(a) desenvolvimento efetivamente em alto nível; (b) evitar redundâncias estruturais e temporais 
visando eficiência de desempenho; e (c) desacoplamento visando inclusive organização, 
paralelismo e mesmo distribuição implícitos. Neste sentido, para buscar solução para a situação 
posta, foi necessária a criação de uma tecnologia envolvendo uma linguagem de programação 


27 
 
 
e um sistema de compilação próprio para o PON, o que foi evoluindo ao longo do tempo 
(RONSZCKA, 2019).  
Essa nova solução foi denominada Tecnologia LingPON, que consiste em linguagens 
de programação e compiladores organizados pelo já mencionado sistema de compilação próprio 
para o PON. Inicialmente, o primeiro compilador gerou código para o próprio Framework PON 
C++ 2.0 que então era o estado da técnica. Entretanto, subsequentemente surgiram outros 
compiladores para código notificante específico em C e em C++, apartando-se de estrutura de 
dados dos frameworks e assim melhorando significativamente o desempenho (RONSZCKA et 
al., 2017).  
De forma concomitante, a evolução dessa solução deu origem a um método conhecido 
como MCPON (Método de Compilação do PON), que apresenta um método de compilação 
próprio ao PON para a criação de linguagens e compiladores. Particularmente, como elemento 
basilar, o MCPON define e utiliza uma representação intermediária uniforme em formato de 
grafo de entidades notificantes, conhecida como Grafo PON. Isto assim se deu porque os 
relacionamentos por notificação das entidades do PON se dão em uma forma tal que se 
assemelha finalmente à um grafo, conforme é notório na Figura 2 acima apresentada 
(RONASZCKA, 2019). 
A Tecnologia LingPON via MCPON, com sua representação intermediária via Grafo 
PON como elemento fundamental do sistema de compilação, tem contribuído cada vez mais 
para o desenvolvimento de sistemas computacionais que buscam atender as três propriedades 
elementares do PON e, portanto, visam a alcançar seu potencial (NEGRINI, 2019; 
RONSZCKA, 2019). Assim sendo, para continuar com esse avanço e, principalmente, 
materializar apropriadamente os princípios do PON, faz-se necessário validar a Tecnologia 
LingPON de forma a atingir de maneira cada vez mais satisfatória a potencialidade das três 
propriedades elementares do novo paradigma aqui em voga. 
 
1.3 
Justificativa 
Conforme descrito anteriormente, observou-se que para materializar o PON de forma 
mais efetiva foi necessário criar uma linguagem de programação e compilador próprios para o 
PON. Porém, ao tentar construir os primeiros protótipos dessa linguagem e compilador 
baseados na teoria de compilação tradicional, observou-se que esta não apresentava todas as 
características desejadas para a construção de compiladores que fossem adequados ou de acordo 


28 
 
 
para com as características do PON. Isto assim se deu porque a teoria e as técnicas decorrentes 
de compilação tradicional baseiam-se em um mapeamento sequencial, representado em forma 
hierárquica os programas por meio de árvores sintáticas e orientado a elementos passivos a 
serem percorridos ou pesquisados (RONSZCKA, 2019).  
Uma vez que no PON os elementos ou entidades de cada programa interagem por meio 
de notificações, formando um arranjo que se assemelha a um grafo de notificações, percebeu-
se que o mapeamento ideal de um programa PON deveria se dar em formato de um grafo 
justamente, no qual as entidades constituintes deste se conectam por meio de caminhos de 
notificações, por assim dizer. Para isso, foi necessária a criação de um novo método de 
compilação, baseado em técnicas e conceitos adequados aos princípios de notificação do PON 
sendo, portanto, um método orientado a grafo de notificações (RONSZCKA, 2019).  
Esse método, conhecido como Método de Compilação do PON (MCPON), é formado 
por um conjunto de diretrizes, regras e etapas para a construção de linguagens adequadas, 
representação intermediária comum em Grafo PON, sistema de compiladores e validações para 
o PON. A materialização desse método engloba o desenvolvimento de linguagens e tecnologia 
de compilação apropriadas para o PON, constituindo um arcabouço técnico chamado de 
Tecnologia LingPON (RONSZCKA, 2019). Tal projeto, liderado pelo pesquisador A. F. 
Ronszcka, contou com contribuição de diversos pesquisadores do grupo de pesquisa do PON, 
os quais auxiliaram na construção de linguagens e compiladores para o PON, sempre à luz do 
MCPON (implicitamente ou explicitamente), seja na sua versão dita intermediária seja na sua 
versão dita final (FERREIRA, 2015; MELO, 2016; PORDEUS, 2017; SANTOS, 2017; 
KERSCHBAUMER, 2018; SCHÜTZ, 2019; NEGRINI, 2019; RONSZCKA, 2019).  
O MCPON foi finalmente estruturado de forma a proporcionar uma melhor 
organização na construção de materializações efetivas para o PON, possibilitando construir 
linguagens e compiladores para plataformas distintas a partir de uma representação única via 
Grafo PON como elemento central e basilar do método e também de sistema de compilação. 
Naturalmente, a construção desta solução para plataformas distintas se deu com o intuito de 
explorar tanto a potencialidade do PON em cada plataforma, quanto a natureza desta permitir, 
via linguagem própria ao PON (LingPON) a partir de uma representação homogênea e comum 
entre as plataformas que é o Grafo PON (RONSZCKA, 2019).  
Em suma, portanto, qualquer sistema desenvolvido para o PON via LingPON (i.e., 
linguagem de programação para o PON) pode e deve ter sua representação mapeada em uma 
instância do Grafo PON. Neste âmbito, o Código 2 exemplifica um dado programa em 
LingPON, linguagem criada à luz das primeiras etapas do MCPON. Cada programa em 


29 
 
 
LingPON, via etapas subsequentes de MCPON implementadas em sistema de compilação 
apropriado, resultará em uma dada instância do Grafo PON. Em tempo, o programa do Código 
2 representa o mesmo exemplo já trazido da Figura 1 anteriormente apresentada.  
 
Código 2 - Exemplo de criação de FBE e Rule em LingPON 
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
37 
38 
39 
40 
41 
42 
43 
44 
fbe Alarm  
    attributes  
        boolean atOn false  
        integer atTimer 0  
    end_attributes  
    methods  
        method mtRingTheSiren(atTimer = 60)  
    end_methods 
end_fbe 
 
fbe Sensor  
    attributes  
        boolean atActivated false  
    end_attributes 
end_fbe 
 
fbe Sector  
    attributes  
        boolean atIntruderDetected false  
    end_attributes  
    methods  
        method mtNotifyInvasion (atIntruderDetected = true) 
    end methods 
end_fbe 
 
inst 
    Alarm alarm1 
    Sensor sensor1 
    Sector sector1   
end_inst 
 
rule rlFireAlarm 
    condition       
        premise prAlarmOn alarm1.atOn == true 
        and            
        premise prSensorState sensor1.atActivated == true   
        and 
        premise prSector sector1.atIntruderDetected == false 
    end_condition    
    action      
        instigation inFireAlarm alarm1.mtRingTheSiren();    
        instigation inNotifyInvasion sector1.mtNotifyInvasion(); 
    end_action 
end_rule 
Fonte: Adaptado de RONSZCKA (2019) 
 
De forma sucinta, a estrutura da linguagem apresentada no Código 2 é baseada em 
declarações, sendo o programa constituído por três blocos principais que correspondem à 
definição de FBEs (linhas 1 a 24), às instanciações de FBEs (linhas 26 a 30) e à declaração das 
Rules (linhas 32 a 44) (RONSCKA, 2019). O Código 2, o qual exemplifica a criação de um 


30 
 
 
FBE e de uma Rule de um sistema de monitoramento de alarmes, mostra que o FBE é 
constituído por um conjunto de Attributes e pela declaração de seus Methods. Ainda, é possível 
observar no código em questão que as Rules são compostas por blocos lógico-causais, 
representados por Condition e Action, obedecendo o mecanismo de estruturação do PON, 
descrito anteriormente (RONSZCKA, 2019). 
Uma vez detalhado o Código 2, recorda-se que sua compilação em sistema de 
compilação de Tecnologia LingPON resultaria, sempre à luz do MCPON, em uma dada 
instância do Grafo PON. A Figura 3 justamente apresenta o diagrama de instâncias ou “objetos” 
de entidades PON para a instância do Grafo PON relativa ao programa do Código 2. 
Naturalmente, o grafo instanciado em questão representa um dado exemplo pontual do modelo 
genérico de entidades do PON e suas dependências, além das possíveis conexões, que consiste 
o modelo do Grafo PON em si. 
 
Figura 3 - Diagrama de Objetos que representa instância do Grafo PON 
 
Fonte: Autoria própria 
 
Basicamente, a Figura 3 representa a construção de um grafo especializado ou 
instanciado, para o sistema de Redes de Sensores, baseado nas diretrizes do Grafo PON. As 
entidades representadas na cor amarela (Alarm, Sensor e Sector) ilustram os FBEs, os quais 
estão ligadas cada qual com suas instâncias (alarm1, sensor1 e sector1), na cor azul, 


31 
 
 
representando as FBEInstances. Cada instância de FBE pode apresentar uma ou mais entidades 
do tipo Attribute e uma ou mais entidades do tipo Method, ambas representadas na cor laranja. 
Os grupos apresentados na cor verde representam as entidades lógico-causais, as Rules, 
compostas pelas entidades Premise e Condition, que formam o conjunto condicional, e pelas 
entidades Action e Instigation, que compõem o conjunto de acional das regras de decisão. Por 
fim, o diagrama também apresenta as entidades que auxiliam na conexão das entidades 
notificantes e que estão representadas pela cor rosa (i.e., Call, Attribution e Factor) 
(RONSZCKA, 2019). 
Como pode-se observar, o Grafo PON tem um papel fundamental no mapeamento 
completo de aplicações PON, advindas de uma ou mais linguagens de programação próprias ao 
PON. Assim, o Grafo PON tem o objetivo de auxiliar no processo de tradução, permitindo 
mapear de forma fidedigna a essência de cada aplicação PON em uma dada instância do Grafo 
PON. Em tempo, atualmente o Grafo PON é materializado na forma de um “framework para 
construção de compiladores” que contribui para realizar tal mapeamento e criar tais instâncias. 
Justamente, a partir deste framework que as instâncias podem ser percorridas por geradores de 
código para gerar código para targets em plataformas distintas.  
A partir do Grafo PON foi criado o MCPON, construído baseado por um conjunto de 
técnicas próprias ao PON e composto por cinco etapas bem definidas, como mostra a Figura 4. 
 
Figura 4 - Visão geral das etapas do MCPON
 
Fonte: ROSZCKA (2019) 
 


32 
 
 
Conforme a Figura 4 ilustra, todas etapas são efetivamente e fortemente dependentes 
do Grafo PON. Basicamente, a primeira etapa do método tem a função de construir linguagens 
particulares para o PON usando os princípios usuais de compiladores como gramáticas, Backus-
Naur Form (BNF), analisador léxico e analisador sintático. A segunda etapa, que se inter-
relaciona com a etapa anterior, visa definir o processo de construção de instâncias do Grafo 
PON. A terceira etapa, por sua vez, tem o objetivo de construir otimizadores a fim de eliminar 
possíveis redundâncias no grafo gerado. A quarta etapa visa transformar/traduzir os grafos em 
códigos-alvo de linguagens e plataformas distintas. Por fim, a quinta etapa visa a construção de 
validadores, com o objetivo de verificar a integralidade de cada compilador gerado 
(RONSZCKA, 2019; OSHIRO 2020). Em tempo, todas estas etapas serão detalhadas em seção 
de capítulo subsequente e pertinente. 
 Ainda, a construção do MCPON e do Grafo PON foi prototipada via soluções 
tecnológicas chamadas Tecnologia LingPON prototipal, Tecnologia LingPON 1.0, Tecnologia 
LingPON 1.2 e Tecnologia LingPON 2.0. Em suma, cada Tecnologia LingPON corresponde a 
um conjunto de linguagens de programação de alto nível e um sistema de compilação 
especificamente desenvolvido para o PON (NEGRINI, 2019; RONSZCKA, 2019).  
Ademais, com o objetivo de materializar um ecossistema de compilação para o PON, 
para cada Tecnologia LingPON (i.e., prototipal, 1.0, 1.2 e 2.0) foram implementados alguns 
compiladores com geradores de códigos para plataformas/linguagens-alvo (targets) a fim de 
validar a Tecnologia LingPON como um todo. A partir desses compiladores foi possível 
observar a viabilidade de transformar aplicações escritas em versões da linguagem PON 
(LingPON) em linguagens-alvo correspondentes a esses targets, tanto no campo de software 
quanto de hardware digital. Foi possível observar que todas as implementações atingiram o 
quesito em relação à programação em alto nível, inclusive para os targets de hardware2. 
Dentre as implementações em software, de interesse deste presente trabalho, destaca-
se o prototipal gerador de código com foco na solução em C++ específico notificante em 
namespaces, implementado via Tecnologia LingPON 1.2 e denominado de NPCPP 1.0. Neste 
caso, o termo ‘específico’ significa que cada entidade em PON no código gerado em C++ será 
um código em si, sem se utilizar de estruturas de dados genéricas. Em um primeiro momento, 
foi implementada a versão conhecida como NPCPP 1.0 single-thread, apenas para ambientes 
single-threaded justamente. O Código 3 exemplifica um trecho do código gerado pelo NPCPP 
                                                          
2 Ainda que os resultados em hardware sejam de todo interessantes e pertinentes ao PON, este trabalho 
de pesquisa se interessa pelo PON em software. 


33 
 
 
1.0 single-threaded a partir de um programa em LingPON, mais especificamente do programa 
correspondente ao apresentado anteriormente pelo Código 2. 
 
Código 3 - Trecho de código do namespace Instantiations, gerado pelo NPCPP 1.0  
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
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
48 
49 
50 
51 
52 
53 
54 
55 
#include "instances.h" 
#include "premises.h" 
#include <string> 
 
namespace instantiations { 
    namespace alarm1 { 
        namespace at { 
            namespace atOn { 
                bool value = 0; 
                void setValue( bool newValue ) { 
                    if  (value != newValue ) { 
                        value = newValue; 
                        premise::prAlarmOn:: 
                                 notify_alarm_atOn( newValue );       
                    }   
                } 
            }  
            namespace atTimer { 
                bool value = 0; 
                void setValue( bool newValue ) { 
                    if  (value != newValue ) { 
                        value = newValue;  
                    }   
                } 
            } 
        } 
        namespace mt { 
            namespace mtRingTheSiren { 
                instance::sectorA::at::atTimer::setValue(60); 
            } 
        } 
    }     
    namespace sensor1 { 
        namespace at{ 
            namespace atActivated { 
                bool value = 0; 
                void setValue( bool newValue ) { 
                    if ( value != newValue ) { 
 
           value = newValue; 
 
           premise::prSensorState:: 
                          notify_sensor_atActivated( newValue );        
                    }  
                }    
            }   
        }   
    }   
    namespace sector1{ 
        namespace at{ 
            namespace atIntruderDetected { 
                bool value = 0; 
                void setValue( bool newValue ) { 
                    if ( value != newValue ) { 
 
           value = newValue; 
 
           premise::prSector:: 
                          notify_sensor_atIntruderDetected( newValue ); 


34 
 
 
56 
57 
58 
59 
60 
61 
62 
63 
64 
65 
                    }  
                }    
            }   
        } 
        namespace mt { 
            namespace mtNotifyInvasion { 
                instance::sectorA::at:: 
                          atIntruderDetected::setValue(true); 
. . . 
} 
Fonte: Autoria própria 
 
O Código 3 apresenta um trecho do código resultante para o chamado trecho 
namespace Instantiations, no qual estão contidos cada instância de FBE com seus respectivos 
Attributes e Methods. Por exemplo, nas linhas 6 a 32 do Código 3, é declarada a instância do 
FBE Alarm, sendo que nas linhas 7 a 26 são declarados os seus Attributes (atOn e atTimer) e 
nas linhas 27 a 31 consta a declaração de seu Method (mtRingTheSiren). Para representar a 
notificação Attribute-Premise, nas linhas 13 e 14 é apresentada a chamada, via namespace para 
a função setValue, da Premise interessada (prAlarm), quando o valor do Attribute atOn da 
instância do FBE Alarm é alterado. Uma vez que a função dos Methods é alterar o valor de um 
Attribute, quando o Method mtRingTheSiren é instigado, ocorre a notificação via namespace 
do Attribute atTimer, como mostra a linha 29 do Código 3, para que seu valor seja alterado. 
Isto dito, em se tratando da arquitetura sequencial monocore e single-threaded (Von 
Neumann [GODFREY; HENDRY, 1993]), essa versão de gerador de código NPCPP 1.0 foi a 
que obteve melhores resultados considerando o desempenho no âmbito da Tecnologia 
LingPON Prototipal e Tecnologia LingPON 1.X (que compreende as versões 1.0 e 1.2), em 
relação aos demais compiladores para o PON, incluindo um com target código C específico 
notificante orientado a procedimentos, outro com target C++ específico notificante orientado a 
objetos e outro ainda com target static C++ específico notificante (RONSCKA, 2019; OSHIRO 
et al., 2021). Posteriormente, foi criado o NPCPP 1.0 na versão dita multithreads (MARTINI, 
2018). Nesta, foi possível observar a viabilidade de paralelização de Methods. No entanto, não 
foi explorada a paralelização de execução das demais entidades do paradigma (RONSZCKA, 
2019). Neste âmbito, o Quadro 1 apresenta as propriedades elementares contempladas nas 
materializações referentes à Tecnologia LingPON, da prototipal até a versão 1.2. 
 
 
 
 
 
 


35 
 
 
Quadro 1 - Propriedades elementares contempladas até a versão 1.2 da Tecnologia LingPON 
Fonte: Adaptado de PORDEUS (2020) 
 
Em relação à compilação de código-fonte PON para targets em software, muito 
embora tenha havido uma série de implementações prototipais no tocante a Tecnologia 
LingPON 1.0, este trabalho está interessado na Tecnologia LingPON 2.0 que aplica o MCPON 
de maneira mais completa e a versão mais atual do Grafo PON em sua concepção. Assim sendo, 
por sua vez, o Quadro 2 mostra a relação das propriedades elementares do PON atendidas por 
cada target testado no tocante a Tecnologia LingPON 2.0 (RONSZCKA, 2019). 
 
Quadro 2 - Propriedades elementares contempladas na Tecnologia LingPON 2.0 
                Materialização 
 
 
Propriedade 
 
Software 
Hardware 
Gerador 
de Cód. 
FW 
C++ 
FW 
C++ 
FW 
C++ 
FW 
C++ 
FW 
FW 
FW 
FW 
LingPON 
2.0 
Alvo 
(target) 
1.0 
2.0 
3.0 
4.0 
JAVA 
C# 
ERLANG 
AKKA 
PONHD 
Programação em alto nível 
 
 
 
 
 
 
 
 
 
Paralelismo via desacoplamento 
 
 
 
 
 
 
 
 
 
Distribuição via desacoplamento 
 
 
 
 
 
 
 
 
 
Desempenho via não redundância 
 
~ 
 
~ 
~ 
 
 
 
 
 Contempla totalmente a propriedade 
~  Contempla parcialmente a propriedade 
Fonte: Adaptado de NEVES (2021) 
 
No âmbito de Tecnologia LingPON 2.0 para software, é possível observar que foram 
criados compiladores via MCPON tendo como plataforma alvo para geração de código PON 
diversos Frameworks do PON: Framework PON C++ 1.0, Framework PON C++ 2.0, 
Framework PON C++ 3.0, Framework PON C++ 4.0, Framework PON 1.0 Java, Framework 
PON 1.0 C# e Framework PON Erlang/Elixir. Particularmente, ainda em termos de 
paralelismo, Negrini (2019) verificou em sua pesquisa que, se bem articulado, a utilização de 
aplicações via Tecnologia LingPON com Framework PON Erlang/Elixir em termos de software 
multicore é promissora. 
                       
 Materialização 
 
Propriedade 
Software 
Hardware 
Prot. 
Prot. 
Prot. 
1.2 
1.0 
1.2 
1.2 
1.2 
1.0 
FW 
2.0 
C a 
notif. 
C++ a 
notif. 
C++ 
Estático 
Fuzzy 
NCPP 
1.0 
NCPP 1.0 
Thread 
NOCA 
PONHD 
Programação em alto 
nível 
 
 
 
 
 
 
 
 
 
Paralelismo via 
desacoplamento 
 
 
 
 
 
 
~ 
 
 
Distribuição via 
desacoplamento 
 
 
 
 
 
 
 
 
 
Desempenho via não 
redundância 
 
 
 
 
 
 
 
 
 


36 
 
 
Apesar de tais esforços culminarem em um conjunto de materializações orientadas à 
natureza de execução do PON, tais implementações em Tecnologia LingPON 2.0 ainda não 
tendem a contemplar de forma completa as propriedades elementares do paradigma em termos 
de software, particularmente no tocante a desempenho, dado que se teve primeiramente como 
targets os próprios frameworks do PON que, por definição, apresenta sobrecargas de estruturas 
de dados para animar a execução orientadas a notificações.  
Portanto, neste âmbito, este presente trabalho foca na contribuição para a Tecnologia 
LingPON 2.0 por meio de um novo compilador com gerador de códigos cujo target é o C++ 
Notificante Modular orientado a Namespaces 2.0, ou simplesmente NPCPP 2.0, além de algum 
ajuste na própria Tecnologia LingPON 2.0, buscando uma implementação mais abrangente em 
termos de ambiente monoprocessado, além de possibilitar a geração e a execução de códigos 
de forma organizado-desacoplada.  
Ainda, na implementação prototipal do NPCPP 1.0 via Tecnologia LingPON 1.X, 
havia imperfeições no sentido de não contemplar alguns conceitos de programação do PON de 
maneira mais ampla, conforme será detalhado no decorrer deste trabalho. Na verdade, isto se 
dava inclusive por conta de imperfeições do Grafo PON na Tecnologia LingPON 1.0 
(RONSZCKA, 2019). Sendo assim, este trabalho visa contribuir para a materialização do PON 
via Tecnologia LingPON 2.0 com uma solução de desenvolvimento em alto nível e desempenho 
apropriado. É pertinente salientar que, conforme o Quadro 2, não havia até então nenhum 
compilador de código específico-notificante para a versão 2.0 da LingPON, sendo que as 
materializações correspondentes à Tecnologia LingPON 2.0 para software se referiam somente 
a frameworks constituintes do estado da técnica. 
Para tanto, esta presente pesquisa propõe testar a Tecnologia LingPON 2.0, 
particularmente com o target NPCPP 2.0, em benchmarks conhecidos pelo grupo de pesquisa 
do PON como as aplicações de redes de sensores (RONSZCKA, 2019) e CTA (Controle de 
Tráfego Automatizado) (RENAUX et al., 2014). Basicamente, o programa de rede de sensores 
simula um sistema de alarmes que dispara um alerta ao identificar a presença de um “invasor”, 
enquanto o CTA funciona como um simulador de controle de tráfego de uma área urbana. 
Ademais, este trabalho visa testar e validar a solução proposta também por meio de aplicações 
conhecidas da literatura, como o algoritmo de ordenação Bitonic Sort e o algoritmo de 
aprendizagem de máquina Random Forest.  
 


37 
 
 
1.4 
Objetivos 
Esta presente seção apresenta os objetivos desta dissertação de mestrado, os quais se 
dividem em objetivo geral e objetivos específicos. Isto dito, à luz do apresentado nas seções 
anteriores, o objetivo geral dessa pesquisa de mestrado consiste em: 
 
No âmbito da Tecnologia LingPON 2.0, à luz do MCPON, desenvolver o compilador 
para o target de Código C++ Notificante Modular orientado a Namespaces, o NPCPP 
2.0, ajustando e transpondo os elementos do Grafo PON de maneira apropriada. Este 
resultante compilador na Tecnologia LingPON 2.0 deve permitir a facilidade de 
programação declarativa em alto nível e desempenho apropriado de execução, a ser 
validado por um conjunto de benchmarks. Dessa forma, o objetivo é apresentar uma 
materialização para o PON que explora a viabilidade do desenvolvimento em alto-nível 
com performance aceitável, respeitando o conjunto atual de conceitos do PON.  
 
Para atingir o objetivo geral apresentado, este trabalho visa a alcançar os seguintes 
objetivos específicos no âmbito da Tecnologia LingPON 2.0, à luz do MCPON: 
 
 Implementar o compilador no tocante ao gerador de código para o alvo ou target NPCPP 
2.0, à luz da Tecnologia LingPON 2.0, visando gerar programas com desempenho 
apropriado, ou seja, com tempo de processamento de execução aceitável. 
 Possibilitar a geração e execução de códigos no target do NPCPP 2.0 de maneira 
desacoplada, permitindo organização do código gerado. 
 Testar a solução NPCPP 2.0 com benchmarks do grupo de pesquisa do PON, mais 
precisamente sob a aplicação chamada Sensores e sob a aplicação chamada Controle de 
Tráfego Automatizado (CTA).  
 Testar a solução NPCPP 2.0 com benchmarks externos apropriados, mais precisamente 
os conhecidos algoritmos Bitonic Sort e Random Forest.  
 Comparar, quando possível, os benchmarks feitos pelo NPCPP 2.0 em relação às 
soluções assaz equivalentes (i.e., com código específico-notificante em C++) na 
prototipal NPCPP 1.0 e naturalmente em C++ usual baseado na POO.  
 


38 
 
 
1.5 
Organização do Trabalho 
Este documento está dividido em quatro capítulos, incluindo este presente capítulo de 
Introdução. No subsequente Capítulo 2 é apresentada uma revisão sobre o PON e seus 
fundamentos, bem como sobre o estado da arte das tecnologias utilizadas no desenvolvimento 
deste trabalho e as materializações existentes do paradigma.  
O Capítulo 3, por sua vez, apresenta o desenvolvimento do compilador NPCPP 2.0 
(i.e., o target ‘C++ Notificante Modular orientado a Namespaces’) na Tecnologia LingPON 
2.0. Ainda no Capítulo 3, são apresentados os experimentos e resultados realizados para validar 
o NPCPP 2.0.  
Por fim, no Capítulo 4 são apresentadas as conclusões deste trabalho, além de trazer 
reflexões para trabalhos futuros.  


39 
 
 
2 FUNDAMENTAÇÃO TEÓRICA 
Este capítulo apresenta os conceitos fundamentais para o embasamento dessa 
pesquisa3. Primeiramente, é apresentada na Seção 2.1 uma contextualização geral sobre o 
Paradigma Orientado a Notificações (PON). Em seguida, a Seção 2.2 traz uma visão geral do 
método MCPON, do Grafo PON (elemento mais fundamental deste método), da LingPON 
(linguagem de programação) e da Tecnologia LingPON como um todo, a qual envolve inclusive 
um sistema de compilação para a LingPON, sempre à luz do MCPON com seu Grafo PON. Em 
particular, há os geradores de código no sistema de compilação que permitem, a partir do Grafo 
PON, alcançar código para plataformas distintas de qualquer programa em LingPON mapeado 
em instâncias do Grafo PON.  
Neste trabalho, há interesse especial na geração de código para o alvo (ou target) em 
C++ Notificante Modular orientado a Namespaces (NPCPP). Para tanto, é necessário 
compreender as etapas do método MCPON, as quais serão apresentadas na Seção 2.3. Ainda, 
na sequência deste capítulo, a Seção 2.4 descreve, de forma mais detalhada, as versões single-
threaded e multithread do compilador para C++ Notificante Modular orientado a Namespaces 
1.0 (NPCPP 1.0), implementado via versão 1.2 da Tecnologia LingPON. Por fim, são 
apresentadas na Seção 2.5 algumas reflexões sobre este capítulo, salientando a lacuna (ou gap) 
existente no contexto dado. 
 
2.1 
Contextualização Geral sobre o Paradigma Orientado a Notificações 
O PON é um paradigma que proporciona uma nova maneira de implementar, estruturar 
e executar software. Para um melhor entendimento, esta seção apresenta o paradigma de uma 
forma mais detalhada: primeiramente são apresentadas as bases dos fundamentos teóricos do 
PON; em seguida são detalhadas quais são as propriedades elementares e dos conceitos de 
programação que o sustentam e, por fim, são apresentadas as implementações existentes que 
contribuem na materialização do paradigma.  
 
                                                          
3 A título de informação, caso o leitor apresente conhecimento sobre as seções deste capítulo, poderá 
não as ler ou postergar a leitura, sem prejuízo ao entendimento desta dissertação. Ou em caso de apenas uma 
revisão sobre os fundamentos mais relevantes, é sugerida a leitura da subseção 2.1.3. e da seção 2.4. 


40 
 
 
2.1.1 Bases do Paradigma Orientado a Notificações (PON) 
A base do PON foi proposta inicialmente em Simão (2001, 2005) como uma solução 
de controle discreto para sistemas inteligentes de manufatura (SIMÃO, 2001; SIMÃO et al., 
2002; SIMÃO, 2005), o que posteriormente foi chamado de Controle Orientado a Notificações 
(CON) (SIMÃO e STADZISZ, 2009b). Esta solução definiu uma forma de orquestrar o controle 
de manufatura por meio de colaboração por notificações precisas e pertinentes entre entidades 
relacionadas, levando a cooperação destas. Posteriormente, tal solução foi estendida e aplicada 
como uma solução genérica de inferência de software, o que foi subsequentemente chamado de 
Inferência Orientada a Notificações (ION) (SIMÃO e STADZISZ, 2002; SIMÃO et al., 2003; 
SIMÃO e STADZISZ, 2009b; RONSZCKA et al., 2015).  
Subsequentemente, a solução CON/ION evoluiu para um paradigma de 
programação/desenvolvimento. Primeiramente, isto em termos de programação com expressão 
e execução efetiva em código (BANASZEWSKI et al., 2007; SIMÃO e STADZISZ, 2008; 
SIMÃO e STADZISZ, 2009b; SIMÃO et al., 2012b; BANASZEWSKI, 2009; RONSZCKA, 
2012; VALENÇA, 2011; FERREIRA, 2015; OLIVEIRA, 2019; NEGRINI, 2019). 
Posteriormente e, então concomitantemente, também em termos de modelagem via diagramas 
e métodos (NOVAES, 2019; MENDONÇA 2020; WIECHETECK, 2011). Por fim, mais 
genericamente, tal solução alcançou a forma de um paradigma de desenvolvimento de sistemas 
computacionais (PETERS, 2012; MELO, 2016; PORDEUS, 2017; KERSCHBAUMER, 2018; 
SCHÜTZ, 2019; RONSZCKA, 2019; PORDEUS, 2020a). 
Em suma, o PON foi proposto como um novo paradigma de desenvolvimento, 
primeiramente de software e subsequentemente em hardware, o qual tende a apresentar 
apropriado nível de abstração e proporcionar melhor desempenho e facilidades para o 
paralelismo/distribuição em comparação com sistemas baseados em paradigmas tradicionais. 
No âmbito de paradigmas tradicionais, exemplos importantes são a programação advinda do 
Paradigma Orientado a Objetos - Imperativo (POO/PI) e os Sistemas Baseados em Regras 
(SBR) advindo do Paradigma Lógico-Declarativo (PL/PD) (SIMÃO e STADZISZ, 2008; 
SIMÃO; STADZISZ, 2009; SIMÃO et al., 2012; PORDEUS, 2017; RONSZCKA, 2019; 
PORDEUS, 2020a). 
Quando comparado com esses paradigmas, o PON apresenta vantagens, uma vez que 
aporta solução para alguns dos problemas que eles apresentam. Particularmente, uma dessas 
vantagens é, em suma, uma maior facilidade na concepção de sistemas que apresentem 


41 
 
 
paralelismo e/ou distribuição, por evitar implicitamente o acoplamento excessivo entre 
entidades computacionais. Outra vantagem é a efetiva redução de alguns dos problemas 
clássicos de software do PI e do PD, tais como redundâncias de execução, o que no PON 
também está diretamente relacionado ao minimizar acoplamento excessivo (SIMÃO e 
STADZISZ, 2008; SIMÃO e STADZISZ, 2009a; SIMÃO et al., 2012; PORDEUS, 2017; 
RONSZCKA, 2019; PORDEUS, 2020a). 
Conforme mencionado anteriormente, uma aplicação baseada no modelo PON é 
estruturalmente representada na forma de dois tipos fundamentais de entidades, nomeadamente 
Elemento de Base de Fatos (FBE – Fact Base Element, em idioma inglês) e Regras (Rules, 
também em idioma inglês). As FBEs (i.e., as instâncias de FBE) são entidades facto-
execucionais utilizadas para representar objetos do mundo vislumbrado (sejam entidades reais, 
sejam entidades abstratas) em um sistema computacional, por meio de conjuntos exclusivos (à 
priori) de estados tratados por entidades chamadas de Attributes (Atributos) e também por meio 
de serviços tratados por entidades chamadas de Methods (Métodos) (SIMÃO e STADZISZ, 
2008; 2009a; BANASZEWSKI, 2009; SIMÃO et al., 2012; PORDEUS, 2017; RONSZCKA, 
2019; PORDEUS, 2020a; OSHIRO et al, 2021). 
Por sua vez, cada Rule (i.e., cada instância de Rule) é, em suma, uma entidade lógico-
causal que se compõe de uma entidade Condition (Condição) que se associa a entidades do tipo 
Premise (Premissa) e de uma entidade Action (Ação) que se associa a entidades do tipo 
Instigation (Instigação). Estas entidades todas, nomeadamente Rules, FBEs associadas, e seus 
constituintes, podem ser conjuntamente tratadas de forma declarativa orientada a instâncias 
factuais e regras lógico-causais, tal qual exemplifica a Figura 5 (SIMÃO e STADZISZ, 2008; 
2009a; BANASZEWSKI, 2009; SIMÃO et al., 2012; PORDEUS, 2017; RONSZCKA, 2019; 
OSHIRO et al, 2021), bem como por outros formalismos que possam ser equivalentes (SIMÃO 
et al., 2003; WIECHETECK, 2011; MENDONÇA et al., 2015; RONSZCKA, 2019; 
MENDONÇA et al., 2020). 
 
 
 
 
 
 
 
 


42 
 
 
Figura 5 - Exemplo genérico de ciclo de notificações entre entidades em PON 
 
Fonte: Adaptado de NEVES (2020) 
 
Em linhas gerais, como mostra a Figura 5, declarativamente, as entidades Rules 
definem o chamado cálculo lógico-causal a ser efetuado sobre os estados dos FBEs, controlando 
assim a execução de seus serviços. Muito embora Rules e seus constituintes possam 
univocamente ser representados de forma declarativa via regras lógico-causais, bem como 
FBEs e seus constituintes possam univocamente ser representados declarativamente via 
instâncias (objetos ou frames) notificantes, em termos práticos, as entidades (principais e 
constituintes) são atômicas, desacopladas e se relacionam colaborativamente entre si em um 
orquestramento por notificações. Ademais, a colaboração entre estes elementos (ou entidades) 
ocorre por meio de notificações diretas e estritamente necessárias, conforme modela a Figura 6 
via um diagrama de blocos em SysML.  
 
 


43 
 
 
Figura 6 - Diagrama de Blocos Interno em SysML representando as notificações entre entidades em PON 
 
Fonte: Adaptado de PORDEUS (2020). 
 
Uma variante de digrama de instância em UML é esboçada pela Figura 7, pela qual é 
possível observar que tal colaboração se dá, em suma, como segue: quando é identificada a 
mudança de estado em cada Attribute de um determinado FBE, esse Attribute automaticamente 
notifica apenas e somente as Premises correspondentes, as quais registram o valor atual deste 
e, então, reavaliam seus próprios estados lógicos. Caso o valor lógico de dada Premise 
notificada seja modificado, esta Premise notifica as Conditions pertinentes, as quais então 
reavaliam seus estados lógicos. A aprovação de uma Condition com estado lógico verdadeiro é 
dada quando todas as Premises pertinentes tenham notificadas com estado verdadeiro 
(BANASZEWSKI, 2009; RONSZCKA, 2012; FERREIRA, 2015, PORDEUS, 2020a; 
OSHIRO et al., 2021).  
 
 
 
 
 
 


44 
 
 
Figura 7 - Variante de digrama de instância em UML com relações  
entre as entidades do PON que levam ao fluxo de notificações 
 
Fonte: Adaptado de BANASZEWSKI (2009) 
 
Dito de outra forma, se os estados de todas as Premises correspondentes são satisfeitos, 
a Condition é aprovada, consequentemente podendo ativar sua respectiva Rule. Quando essa 
Rule for ativada, será executada sua Action correspondente, que é uma entidade computacional 
conectada a uma ou mais Instigations. Cada Instigation instiga (ou aciona), por meio de 
Methods, um conjunto de serviços/funcionalidades de um conjunto de FBEs (BANASZEWSKI, 
2009; RONSZCKA, 2012; FERREIRA, 2015). Geralmente ou ao menos possivelmente, os 
Methods acabam por alterar os estados dos Attributes, reativando, portanto, o ciclo de Inferência 
Orientada a Notificações (ION) (PORDEUS 2017; PORDEUS, 2020a; OSHIRO et al., 2021). 
Todo o processo de colaborações pontuais entre as entidades do PON tem sido 
chamado de ION, termo oriundo antes do entendimento do PON enquanto paradigma, cf. 
supramencionado. Isto dito, dado que a ION se constitui de notificações diretas entre as 
entidades que compõem o PON, de forma reativa em decorrência das mudanças de estados 
destas entidades, cria-se assim desacoplamento ou acoplamento mínimo, conforme o ponto de 
vista, entre as entidades. O emprego de notificações diretas desacoplantes entre as entidades 


45 
 
 
que constituem os FBEs e as Rules, por meio de sub-entidades, elimina a necessidade de 
mecanismos de inferência monolítico para realizar o matching (i.e., casamento) entre entidades 
facto-execucionais e entidades lógico-causais. Isto torna o ION, essência da existência do PON, 
um processo de inferência absolutamente distinto dos processos utilizados em software PI (PP 
- Programação Procedural - e POO) e em PD (SBR-PL, PL e PF - Programação Funcional) 
(SIMÃO e STADZISZ, 2002, 2008, 2009; BANASZEWSKI, 2009; RONSZCKA et al., 2015; 
PORDEUS, 2017; PORDEUS, 2020a).  
Os conceitos lógicos e estruturais inerentes ao processo de inferência do PON, a ION, 
permitem que este novo paradigma apresente uma forma inovadora de conceber soluções para 
problemas. Particularmente, o PON permite que estas soluções sejam conceitualmente 
descentralizadas dado o desacoplamento implícito, possibilitando, consequentemente e em 
implementações apropriadas, alcançar paralelismo e distribuição tão fino quanto a arquitetura 
computacional o permitir. Ainda, este modelo de inferência peculiar do PON tende a reduzir 
alguns dos problemas clássicos das abordagens tradicionais em PI e PD, tais como as 
redundâncias estruturais (repetições de código) e temporais (repetições ao longo do tempo) 
(SIMÃO e STADZISZ, 2002, 2008, 2009; RONSZCKA et al., 2015; PORDEUS, 2020a; 
NEVES, 2021).  
Além disso, os conceitos do PON permitem a concepção de soluções para tais 
problemas com um nível de abstração mais intuitivo à forma cognitiva humana, isto no sentido 
de ser em alto nível e declarativamente orientado a regras e entidades factuais, inspirando-se na 
orientação a regras de Sistemas Baseados em Regras e afins (SIMÃO e STADZISZ, 2002, 
2008, 2009; XAVIER, 2014; PORDEUS, 2017; PORDEUS, 2020a). Neste âmbito, ainda que 
o PON aproveite alguns conceitos de paradigmas anteriores como Sistemas Baseados em 
Regras acima citado, Orientação a Objetos e Orientação e Eventos, ele é distinto em função de 
suas propriedades ímpares oriundo justamente da inferência suis generis orquestrada de 
maneira orientada a notificações nos termos já dados. Oportunamente, a Figura 8 apresenta uma 
adaptação da taxonomia proposta por Van Roy (2009), incluindo o PON em relação aos 
principais paradigmas de programação (XAVIER, 2014; PORDEUS, 2020a). 
 
 
 
 
 
 


46 
 
 
Figura 8 - Taxonomia de Paradigmas de Programação de Peter Van Roy incluindo o PON 
 
Fonte: XAVIER (2014)  
 
Desta taxonomia de Peter Van Roy (2009), cada elemento representa um paradigma e 
seu respectivo conjunto de conceitos gerais. Por sua vez, as setas entre dois quadros representam 
a inclusão de novos conceitos, no sentido de que os quadros derivados contemplam os conceitos 
dos paradigmas anteriores, acrescidos de um ou mais conceitos novos que, conjuntamente, os 
definem como um paradigma distinto dos demais. Os conceitos gerais abordados na taxonomia 
em questão são basicamente elementos primitivos básicos que, conjuntamente, dão origem aos 
paradigmas (VAN ROY, 2009; XAVIER, 2014; PORDEUS, 2020a).  
Em resumo, os principais conceitos gerais abordados são: record ou registros 
(elementos como estruturas de dados), closures ou recipientes com escopo léxico (como 
funções, classes, métodos etc.), concurrence ou concorrência (duas ou mais entidades ativas ao 
mesmo tempo e concorrendo por recursos), named state ou estado nomeado (entidades 
existentes em lugar dado e com estado definido) e determinism ou determinismo 


47 
 
 
(comportamento previsível e não mutável sobre as mesmas condições dadas) (VAN ROY, 
2009; XAVIER, 2014; RONSZCKA, 2019; PORDEUS, 2020a). 
Ainda, o posicionamento do PON no local dado segundo a Figura 8 se dá por um 
conjunto de fatores. Na verdade, o posicionamento de um paradigma em geral, graficamente e 
semanticamente, ocorre pela estrutura intrínseca da própria taxonomia a luz de fatores de 
expressividade de estado, forma de programação e soma das características únicas (XAVIER, 
2014; PORDEUS, 2020a).  
No caso do PON, tais fatores acima listados foram assim interpretados: (a) 
expressividade de estado - ativação por notificações tem expressividade menor que passagem 
de mensagem e maior que estado não nomeado; (b) forma de programação - mais declarativa 
ou mais imperativa, sendo que no eixo horizontal buscou-se equilíbrio no tocante a natureza 
das Rules, FBEs e seus constituintes; e (c) soma de características únicas – segundo o eixo 
vertical a luz das idiossincrasias do PON (XAVIER, 2014; PORDEUS, 2020a). 
De forma geral, os paradigmas adjacentes ao PON na classificação dada são um tanto 
mais próximos ou menos distantes dele. Por fim, a posição na qual se encontra o PON na 
taxonomia utilizada é ainda o local mais equidistante e graficamente viável entre os paradigmas 
ditos “ancestrais” do PON: nomeadamente a Orientação a Objetos e Declarativo (XAVIER, 
2014; PORDEUS, 2020a). Por fim, o PON vis-à-vis a paradigmas precedentes foi 
extensivamente discutido em trabalhos pregressos do grupo de pesquisa do PON 
(BANASZEWSKI, 2009, RONSZCKA, 2012, XAVIER, 2014; LINHARES, 2015, 
KERSCHBAUMER, 2018). 
 
2.1.2 Materializações do PON 
O PON tem sido alvo de pesquisas em uma considerável diversidade de áreas nos 
últimos anos, tais como: engenharia de software, engenharia de sistemas, redes neurais, lógica 
fuzzy, sistemas embarcados, sistemas em tempo real, sistemas sencientes, hardware em lógica 
reconfigurável e arquiteturas de computação. Ademais, a tendência de ele ser expandido para 
novos domínios do conhecimento como Engenharia Orientada a Modelo (MDE - Model-Driven 
Engineering), ontologias e mesmo engenharia concorrente. Atualmente, em todo caso, existem 
materializações do PON tanto em software quando em hardware, buscando contemplar em algo 
as áreas do seu atual universo de discurso. Em tempo, as primeiras materializações foram 


48 
 
 
essencialmente em software e apenas posteriormente surgiram as em hardware 
(BANASZEWSKI, 2009, PORDEUS, 2017; RONSZCKA, 2019; PORDEUS, 2020a). 
Para o desenvolvimento de softwares fazendo uso do PON, primeiramente foram 
realizadas pesquisas por meio de arquétipo logicial (i.e., de software) chamado Framework 
PON C++ Prototipal (versão 0.5), sendo este derivado dos Frameworks CON C++ (versão 1.0 
e 2.0), que surgiram a partir dos esforços de pesquisa de mestrado e de doutorado de J. M. 
Simão (2001, 2005). Subsequentemente, foi desenvolvido o Framework PON C++ 1.0, também 
chamado, inicialmente, de “Original” (BANASZEWSKI, 2009; SIMÃO et al., 2012c).  
Depois, evolutivamente, foi desenvolvida e utilizada uma segunda versão melhorada 
de framework PON em C++, sendo este chamado de Framework PON C++ 2.0, também por 
vezes chamado de “Otimizado” por otimizar ou melhorar o tempo de processamento em relação 
aos frameworks anteriores (RONSZCKA, 2012; VALENÇA, 2012). Essas materializações do 
PON, em forma de frameworks ou arquétipos, permitiram a criação de softwares PON sob a 
linguagem C++ do POO/PI, mas aplicando nela a abordagem por notificações, provendo-a 
assim de conotação distinta (PORDEUS, 2017; PORDEUS, 2020a). Ainda, no mesmo 
contexto, houve versões de framework PON em linguagens de programação C# e Java 
(BARRETO et al., 2018; HENZEN, 2015; OLIVEIRA, 2019; PORDEUS, 2020a). 
Outrossim, houve uma pesquisa a respeito do balanceamento de carga de software 
PON em ambientes multicore utilizando uma versão modificada do Framework PON C++ 2.0, 
chamado de Framework PON C++ 3.0 (BELMONTE, 2012; BELMONTE et al., 2012; 
BELMONTE et al., 2016; SCHÜTZ et al., 2018). Ainda no âmbito de multicore, houve depois 
mesmo um Framework PON Akka (MARTINI, 2018) e um Framework PON Erlang/Elixir 
(NEGRINI, 2019), alcançando sinergia para com estas tecnologias, bem como um recente 
Framework PON C++ 4.0 que é considerado o estado da técnica em PON (NEVES, 2021; 
NEVES et al., 2021). Por fim, outras implementações prototipais como Framework PON em 
Java, C# e mesmo C++ tiveram experimentos envolvendo agora distribuição via Transmission 
Control Protocol/Internet Protocol (TCP/IP), conforme (TALAU, 2016; BARRETO et al., 
2018; OLIVEIRA, 2019). 
Os frameworks em PON permitiram a demonstração de factibilidades do PON, como 
a possibilidade efetiva de paralelismo em núcleos e mesmo distribuição em máquinas distintas. 
Entretanto, o custo de execução computacional das estruturas de dados utilizadas na concepção 
deles, mesmo na versão dita ‘otimizada’ em C++ (i.e., Framework PON C++ 2.0) ou na até 
então mais contemporânea e performática (i.e., Framework PON C++ 4.0), apresentaram 
imperfeições no tocante a performance. Particularmente, o peso das estruturas de dados e afins 


49 
 
 
não permite alcançar todo o potencial do PON em termos de tempo de processamento, isto à 
luz de seu cálculo assintótico que é O(n) no caso médio e O(n3) no inverossímil pior caso, 
conforme cálculos apresentados nos trabalhos de (SIMÃO, 2005; FERREIRA, 2015; 
RONSZCKA et al., 2015; RONSZCKA, 2019). Dado este fato posto, fez-se necessário 
vislumbrar outros tipos de materializações para o PON (PORDEUS, 2020a).  
Neste âmbito dado, houve a concepção de um conjunto de linguagens e compiladores 
específicos para o PON denominado Tecnologia LingPON, em uma versão prototipal e logo 
após em uma versão 1.0, os quais permitiram alcançar tempos de processamentos mais 
apropriados (FERREIRA, 2015). Não obstante, a Tecnologia LingPON continuou em evolução 
para se alcançar uma segunda versão chamada de a Tecnologia LingPON 2.0 ou apenas 
Tecnologia NOPL (SANTOS, 2017; PORDEUS, 2017; SANTOS et al., 2017; RONSZCKA et 
al., 2017; PORDEUS, 2020a). Em tempo, as Tecnologias LingPON Prototipal, 1.0 e 2.0 são 
todas, na prática, subordinadas a um método próprio intitulado de Método de Compilação para 
o PON ou MCPON (RONSZCKA, 2019). 
Ronszcka (2019) propôs tal método para a criação de materializações para o PON de 
forma padronizada, incialmente na forma de um conjunto de passos explicados verbalmente e 
depois textualmente, denominando-o por fim de MCPON e tendo-o modelado ou formalizado 
na forma diagramas em Linguagem Unificada de Modelagem (UML – Unified Modelling 
Language). O método MCPON trata principalmente da concepção e definição de linguagens de 
programação específicas e da implementação de compiladores próprios para o PON, de forma 
tal que se permita coerência entre eles, inclusive em plataformas distintas (RONSZCKA, 2019; 
PORDEUS, 2020a).  
A construção destas linguagens para o PON e, particularmente, destes compiladores 
via MCPON é orientada a partir de um grafo diferenciado, denominado Grafo PON. O Grafo 
PON atua no processo de compilação como uma linguagem de representação intermediária, 
sendo que, inicialmente, a tecnologia foi materializada em forma de um arquétipo ou 
framework, permitindo mapear os elementos de uma aplicação PON em um grafo de entidades 
organizadas, bem como suas notificações de forma desacoplada a luz do próprio paradigma. 
Ainda, é justamente o Grafo PON que permite a integração e compatibilidade entre as diferentes 
materializações construídas para plataformas distintas em um sistema de compilação, na forma 
de um framework próprio, que compõe a Tecnologia LingPON (RONSZCKA, 2019; 
PORDEUS, 2020a). Todos estes elementos são, naturalmente, objeto de seção subsequente 
nesta dissertação.  


50 
 
 
No contexto de engenharia de software, por sua vez, Wiecheteck (2011) propôs um 
método de modelagem denominado Desenvolvimento Orientado a Notificações (DON). Este 
método consiste na concepção de software PON baseando-se em práticas de engenharia de 
software com Processo Unificado, UML e Redes de Petri (WIECHETECK, 2011; BATISTA, 
2013; MENDONÇA et al., 2015; MENDONÇA et al., 2020; PORDEUS, 2020a). No entanto, 
o DON aplica uma adaptação da abordagem convencional de modelagem orientada a objetos, 
não necessariamente favorecendo tanto quanto esperado a modelagem de software PON no 
tocante a atividade inventiva das decisões lógico-causais e elementos de base para tal 
(MENDONÇA, 2016).  
Assim, Mendonça et al. (2020) propõem uma nova metodologia de projeto de software 
para o PON, chamada de Metodologia de Projeto de Software Orientada a Notificações (MON) 
ou, em idioma inglês, Notification Oriented Software Design Methodology (NOM), a qual visa 
facilitar a concepção de aplicações para este paradigma (MENDONÇA, 2016; MENDONÇA 
et al., 2020). Também houve pesquisas no tocante a concepção, requisitos e testes relativos ao 
PON (BATISTA, 2013; KOSSOSKI, 2015; NOVAES, 2019; PORDEUS, 2020a). Certamente, 
todas estas pesquisas seriam integráveis à Tecnologia LingPON mencionada, inclusive à luz do 
Grafo PON já considerado, quiçá permitindo alcançar Model-Driven Engineering (MDE) em 
PON (PORDEUS, 2020a).  Neste sentido, em um relatório técnico, há algum ensaio neste 
sentido (SKORA, 2020). 
Adicionalmente, um conjunto de pesquisas também explorou a implementação do 
PON em hardware. Uma primeira pesquisa e projeto chamados de PON em Hardware Digital 
(PON-HD) faz uso de lógica reconfigurável (FPGA - Field Programmable Gate Array), 
visando explorar o seu potencial de paralelização (WITT et al., 2011; SIMÃO et al., 2012b; 
KERSCHBAUMER et al., 2015; PORDEUS et al., 2016; KERSCHBAUMER et al., 2018a; 
PORDEUS, 2020a). Outra pesquisa correlata permitiu alcançar uma solução mais efetiva em 
PON-HD (Hardware Digital), aliada a Tecnologia LingPON ademais. Esta solução permite a 
geração de uma aplicação PON em circuitos específicos a partir de um código em alto nível por 
meio da linguagem e compilador próprios da Tecnologia LingPON, o que é chamado de 
Tecnologia LingPON-HD (KERSCHBAUMER et al., 2015; KERSCHBAUMER et al., 2018b; 
KERSCHBAUMER, 2018; PORDEUS, 2020a; KERSCHBAUMER et al., 2021; PORDEUS 
et al., 2021). 
Outrossim, em outra pesquisa, Peters (2012) propôs a implementação em lógica 
reconfigurável de um coprocessador PON (CoPON). Isto se constitui em uma solução híbrida, 
na qual a parte da aplicação responsável pelo processamento facto-execucional em um núcleo 


51 
 
 
Von Neumann, usando uma adaptação do Framework PON C++ 1.0, enquanto a parte da 
aplicação responsável pelo cálculo lógico-causal e, portanto, pela propagação de notificações 
(advindas da parte factual) é justamente executada por meio de um coprocessador, usando 
FPGA, baseado nos princípios do PON. O resultado foi a paralelização no cálculo lógico causal 
e efetivo ganho de tempo de tal processamento (PETERS, 2012; PETERS et al., 2012). No 
entanto, apesar dos excelentes resultados, tanto CoPON quanto PON-HD (aquele baseado 
neste), tem limitação no número de entidades PON a serem executadas em hardware próprio 
para tal (PORDEUS, 2020a). 
Neste contexto, uma arquitetura de computação foi desenvolvida de acordo com o 
modelo do PON para resolver aquela deficiência, baseado no dueto de memória e 
processadores, sendo denominada de ArqPON (ou Notification-Oriented Computer 
Architecture, NOCA, em idioma inglês). A ArqPON é uma arquitetura de computador 
alternativa às arquiteturas de computadores tradicionais, tais como Von Neumann e fluxo de 
dados. A ArqPON tem como objetivo implementar um ambiente de execução mais propício à 
dinâmica de notificações do PON, permitindo a execução de aplicações desenvolvidas segundo 
este paradigma, de forma que seja possível aproveitar, até certo ponto, as suas propriedades 
intrínsecas de paralelização (LINHARES, 2015; LINHARES et al., 2015; PORDEUS, 2017; 
PORDEUS, 2020a).  
Esta arquitetura foi implementada na forma de um protótipo por meio do uso de 
linguagem de descrição de hardware em conjunto com um dispositivo FPGA (LINHARES, 
2015; LINHARES et al., 2015). Ainda, a ArqPON foi avaliada por meio um simulador em 
software, o qual permitiu a realização de experimentos com uma alta escalabilidade simulada. 
Por meio deste simulador, denominado ArqPONSim ou NOCASim, foi possível inclusive obter 
um número de unidades de processamento na mesma proporção do que o número de elementos 
PON que compõem uma aplicação, reduzindo, assim, as limitações de escala impostas pela 
plataforma em hardware para estudo desta arquitetura dada (PORDEUS, 2017). Atualmente há, 
ademais, uma pesquisa em andamento com nova proposta de solução em termos de arquitetura 
computacional do PON, chamada ArqTotalPON, a qual busca um modelo arquitetural ainda 
mais purista no tocante a notificações associando em alguma medida a Tecnologia LingPON, 
em particular ao Grafo PON, cf. (PORDEUS, 2020a).  
Outras pesquisas ainda foram e vêm sendo realizadas a fim de explorar o uso do PON 
em novas frentes, como: lógica fuzzy em PON (em Framework C++ 2.0 e Tecnologia LingPON 
1.0 adaptadas) (MELO et al., 2015; MELO, 2016), redes neurais em PON tanto em software 
(adaptação de framework PON 2.0 e também da  LingPON 1.0) quanto hardware (Tecnologia 


52 
 
 
LingPON-HD) (SCHUTZ et al., 2015; SCHUTZ, 2019), sistemas em tempo real em teoria e 
protótipos em algumas aplicações mais recentes (LINHARES et al., 2014; ATHAYDE, 2016), 
computação senciente em teoria e prática (OLIVEIRA, 2019; SIMÃO et al., 2014; MAMANN, 
2020) e sistemas assaz complexos exemplificado na forma de futebol de robôs e simulação de 
Controle de Tráfego de Automóveis (CTA) (SANTOS, 2017; NEGRINI, 2019; NEGRINI et 
al., 2020; SANTOS et al., 2021). 
Por fim, a Figura 9 abaixo apresenta um panorama geral das pesquisas realizadas para 
a concepção e desenvolvimento do PON. Em tempo, as caixas em pontilhado são pesquisas 
previstas em fase de elaboração (PORDEUS, 2020a). 
 
Figura 9 - Taxonomia de Paradigmas de Programação incluindo o PON 
 
Fonte: Adaptado de PORDEUS (2020) 
 
2.1.3 Propriedades elementares e conceitos de programação do PON 
As materializações implementadas para o PON representam contribuições para a 
validação do paradigma, tanto em software quanto em hardware, todavia não contemplaram por 
completo e conjuntamente as propriedades elementares do paradigma, nomeadamente 
desenvolvimento declarativo orientado a regras em alto-nível, não redundância visando 
desempenho e desacoplamento visando inclusive organização, reaproveitamento e 
paralelismo/distribuição. Ademais, muitas vezes, tais materializações apresentaram-se de 
maneira incompleta e mesmo inconsistente entre si (PORDEUS, 2020a).  


53 
 
 
Isto dito, mais precisamente e oportunamente, pode-se aqui apresentar definições das 
propriedades elementares do PON conforme segue: 
 
 Programação declarativa em alto nível visando facilidade de desenvolvimento: 
Facilidade de desenvolvimento declarativo pela orientação a entidades factuais e a 
regras em alto nível, sendo cada programa organizado justamente em um conjunto de 
entidades facto-execucionais e outro conjunto correlato de entidades lógico-causais 
(PORDEUS, 2020a). 
 Não-Redundância 
visando 
desempenho 
apropriado: 
Baixo 
tempo 
de 
processamento graças à ausência de redundâncias temporais e redundâncias estruturais 
à luz da estratégia utilizada para implementação ou materialização e da plataforma 
utilizada para tal (PORDEUS, 2020a). 
 Desacoplamento visando Paralelismo/Distribuição: Modelo organizado e 
reaproveitável preparado para execução paralela/distribuída fina em função do 
desacoplamento implícito entre as entidades que compõem o PON, tanto quanto a 
plataforma de execução permitir (PORDEUS, 2020a).  
 
O quadro a seguir mostra as principais materializações do PON, apresentadas na seção 
anterior, vis-à-vis ao contemplar ou não das propriedades elementares do PON. Percebe-se que 
nenhuma materialização ainda contemplava essas três propriedades elementares, com destaque 
especial para a efetiva contemplação do desenvolvimento em altíssimo nível de forma 
declarativa.  
 
Quadro 3 - Propriedades elementares contempladas nas materializações do PON 
        Materialização 
 
Propriedade 
Software 
Hardware 
FW 
Prot. 
FW 
1.0 
FW 
2.0 
FW 
3.0 
FW 
JAVA C# 
FW 3.0 + 
PON IP 
PONHD 
Prot. 
CoPON 
Prot. 
NOCA 
1.0 
PONHD 
1.0 
Programação em 
alto nível 
 
 
 
 
 
 
 
 
 
 
Paralelismo via 
desacoplamento 
 
 
 
 
 
 
 
 
 
 
Distribuição via 
desacoplamento 
 
 
 
 
 
 
 
 
 
 
Desempenho via 
não redundância 
 
 
 
 
 
 
 
 
 
 
Fonte: RONSZCKA (2019) 
 
Além da estrutura geral do PON, constituída por entidades reativas e notificantes que 
levam as suas propriedades elementares supra postas, o paradigma apresenta alguns conceitos 
de programação que auxiliam no desenvolvimento de aplicações em PON e na execução 


54 
 
 
adequada do fluxo de notificações, o quais também deveriam ser bem cobertos pelas 
materializações do PON (RONSZCKA, 2019; NEVES, 2020). Esses conceitos são 
apresentados com mais detalhes a seguir, na próxima subseção. 
 
2.1.3.1 Reatividade das Entidades 
De acordo com o fluxo de notificações do PON, apresentado anteriormente, quando 
há alteração de estado, as entidades reativas geram notificações pontuais entre si, o que 
consequentemente 
proporciona 
eliminação 
de 
algumas 
avaliações 
lógico-causais 
desnecessárias. Ainda em relação às avaliações lógico-causais, este conceito de reatividade por 
notificações permite evitar redundâncias temporais, uma vez que tais avaliações somente 
ocorrem após a mudança de estado de Attributes e de suas respectivas Premises, bem como 
evitar redundâncias estruturais, considerando que há a possibilidade de as Conditions 
compartilharem a colaboração de Premises (BANASZEWSKI, 2009; NEVES, 2021).  
Ainda, é possível que a reatividade no PON seja aprimorada com a utilização, por 
exemplo, de tabelas hash para os Attibutes, viabilizando as notificações das Premises apenas 
em casos específicos, ou seja, apenas quando o estado dos respectivos Attributes é alterado para 
um estado de interesse. A Figura 10 ilustra a notificação de Premises de um programa em que 
o Attribute atSignal tem seu estado alterado de vermelho (RED) para verde (GREEN) em dois 
cenários: um caso em que é utilizada lista encadeada simples e outro caso em que se faz uso de 
tabela hash (BANASZEWSKI, 2009; NEVES, 2021). 
 
Figura 10 - Notificações baseadas em lista encadeada e tabela hash 
 
Fonte: BANASZEWSKI (2009) 
 


55 
 
 
2.1.3.2 Entidades Impertinentes 
Ainda no âmbito de reatividade das entidades, podem ocorrer casos em que são 
executadas notificações consideradas desnecessárias. Um exemplo disso seria uma situação em 
que um Attribute que, apesar de não ser preponderante para a aprovação de uma Rule em um 
dado contexto, apresenta constantes mudanças de estado, disparando o fluxo de notificações 
novamente a cada variação em seu estado. Estas notificações são consideradas desnecessárias 
e acabam impactando negativamente no desempenho de execução (RONSZCKA, 2012; 
RONASCKA, 2019; NEVES, 2021). 
A Figura 11 representa um exemplo hipotético de controle de temperatura com dois 
Attributes denominados de atTemperature e atStatus, sendo que o Attribute atTemperature terá 
seu valor modificado constantemente e o Attribute atStatus terá seu valor alterado 
esporadicamente. Entretanto, a Condition da Rule será aprovada apenas quando o valor de 
atStatus for true e o atTemperature atingir um dado valor mínimo. Neste caso, o Attribute 
atTemperature é considerado uma entidade impertinente, pois as diversas notificações geradas 
por ele são consideradas desnecessárias, já que, por si só, não aprovam a Condition. 
 
Figura 11 - Exemplo de notificações de um Attribute impertinente ativo 
 
Fonte: RONSZCKA (2012) 
 
Para evitar notificações desnecessárias e redundantes, neste contexto, o Attribute 
atTemperature teria as notificações para suas Premises desativadas temporariamente, até 
segunda ordem (RONSZCKA, 2012; RONSZCKA, 2019; NEVES, 2021). A Figura 12 
apresenta o mesmo exemplo da figura anterior, porém com o Attribute atTemperature sendo 
classificado como impertinente e, portanto, com as notificações para suas Premises 
temporariamente desabilitadas. 


56 
 
 
 
Figura 12 - Exemplo de notificações desativadas de um Attribute impertinente 
 
Fonte: RONSZCKA (2012) 
 
Ao desativar temporariamente as notificações do Attribute atTemperature, as 
constantes variações de seu valor não impactariam no disparo desnecessário do fluxo de 
notificações. As notificações do Attribute impertinente seriam geradas apenas na certeza da 
satisfação de Premises vinculadas ao atStatus. Nessa situação, quando o conjunto de demais 
Premises pertinentes para a aprovação de uma dada Condition-Rule forem satisfeitas, a 
Condition fica responsável por demandar às Premises relativas a Attributes impertinentes que 
determinem a realização das notificações, até segunda ordem. Assim, uma vez que o Attribute 
atStatus apresentasse estado verdadeiro, a Condition-Rule ilustrada solicitaria à Premise 
relativa ao Attribute atTemperature que este realize notificações a ela (RONSZCKA, 2012; 
RONSZCKA, 2019; NEVES, 2021), conforme ilustra a Figura 13. 
 
Figura 13 - Exemplo de reativação de uma entidade temporariamente desativada  
 
Fonte: RONSZCKA (2012) 
 


57 
 
 
Após a aprovação e execução da Rule, o Attribute impertinente é novamente 
desativado no contexto da Condition/Rule em questão, sempre por intermédio da Premise a ele 
relacionada. Desta forma, o Attribute impertinente voltaria a ignorar Premise em questão da 
Condition daquela Rule. Naturalmente, isto até que o Attribute em pauta fosse requisitado 
novamente pela Condition (RONSZCKA, 2012; RONSZCKA, 2019; NEVES, 2021). 
 
2.1.3.3 Unique Premise ou Premissa Única  
Unique Premise (ou Premissa Única) é aquela Premise que notifica diversas 
Conditions excludentes entre si, as quais contra-notificam a Unique Premise. Quando uma 
destas Conditions responde ou contra-notifica com uma confirmação de aprovação à Unique 
Premise, esta encerra seu ciclo de notificações para as demais Conditions. Desta forma, as 
notificações às próximas Conditions não são executadas, uma vez que certamente não serão 
aprovadas, evitando processamentos desnecessários (SIMÃO et al., 2010b). 
Este mecanismo de decisão é representado pela Figura 14, em que a Unique Premise 
percorre a sua lista de três Conditions de forma sequencial, da esquerda para a direita. Na 
primeira notificação, a respectiva Condition não é aprovada, confirmando este estado para a 
Unique Premise. Em seguida, a segunda Condition é notificada, a qual atualiza o seu estado 
lógico, enviando a confirmação de aprovação à Unique Premise. Por fim, portanto, a terceira 
Condition simplesmente não é notificada (SIMÃO et al., 2010b). 
 
Figura 14 - Exemplo de notificações com Unique Premise  
 
Fonte: SIMÃO et al. (2010b) 
 


58 
 
 
2.1.3.4 Escalonamento de Rules e Estratégias de resolução de conflitos 
Considerando que uma das principais características do PON é a execução de forma 
desacoplada dos elementos de seu modelo, podendo ser inclusive paralela e/ou distribuída se a 
arquitetura permitir, uma questão importante no paradigma é a identificação e resolução de 
possíveis conflitos que a execução desacoplada pode originar. Um conflito ocorre quando duas 
atividades diferentes dependem ao mesmo tempo de um mesmo elemento/recurso 
compartilhado, o qual deve ser utilizado de maneira exclusiva (SIMÃO, 2005; SIMÃO et al., 
2010a; SIMÃO et al., 2010b; RONSZCKA, 2012; PORDEUS, 2017; RONSZCKA, 2019; 
NEVES, 2021). 
Mais precisamente, o conflito no PON pode ocorrer quando duas ou mais Conditions de 
Rules referenciam, via uma mesma Premise, a um mesmo Attribute de FBE que permite apenas 
acesso exclusivo. Assim, é possível que apenas uma Rule seja executada de cada vez. Neste 
caso, é necessário que, inclusive em ambientes monoprocessados, o sistema apresente um modo 
de estabelecer a ordem de execução de Rules (RONSZCKA, 2019; NEVES, 2021).  
Para solucionar a situação de conflito dada, é possível aplicar um escalonador de Rules 
que utiliza estruturas de dados lineares (e.g., pilha, filha ou lista) particularmente no caso de 
ambientes monoprocessados (BANASZEWSKI, 2009; RONSZCKA, 2019; NEVES, 2021). A 
Figura 15 exemplifica este mecanismo, no qual o escalonador recebe as Rules na ordem em que 
são aprovadas e as executa de acordo com a estratégia de resolução de conflito escolhida, o que 
seria assaz similar à resolução conflitos em geral de sistemas baseados em regras 
(BANASZEWSKI, 2009; RONSZCKA, 2019; NEVES, 2021).  
 
Figura 15 - Modelo centralizado de resolução de conflitos  
 
Fonte: BANASZEWSKI (2009) 
 


59 
 
 
Conforme a estratégia de resolução de conflitos pré-determinada pelo desenvolvedor, 
as Rules em questão serão efetivamente executadas (RONSZCKA, 2019). Nesse âmbito, os 
modelos de resolução de conflitos empregados para o PON, em ambientes monoprocessados, 
têm sido:  
 
 BREADTH ou LARGURA: escalonamento First In, First Out (FIFO), ou seja, refere-se 
à execução de entidades Rule seguindo uma estrutura de dados do tipo fila, na qual o 
primeiro a entrar é o primeiro a sair; 
 DEPTH ou PROFUNDIDADE: baseia-se no escalonamento Last in, First Out (LIFO), 
ou seja, refere-se à execução de entidades Rule seguindo uma estrutura de dados do tipo 
pilha, na qual o último a entrar é o primeiro a sair;  
 PRIORITY ou PRIORIDADE: organiza as entidades Rule de acordo com as prioridades 
definidas nas mesmas; e  
 NO_ONE ou NENHUM: as Rules são aprovadas e executadas imediatamente, não 
utilizando o mecanismo de escalonamento outro. 
 
Este modelo é uma solução eficiente para ambientes monoprocessados e útil para 
multicore, no entanto não se mostra adequado para ambientes distribuídos por não apresentar 
ser um mecanismo centralizado justamente. Isto posto, Banaszewski (2009) propôs tal 
mecanismo para que execute o escalonamento de maneira eficiente em ambiente 
monoprocessado, particularmente em ambiente monoprocesso ou single-threaded.  
Para que este sistema de escalonamento proposto por Banaszewski (2009) seja 
integrado ao modelo de resolução de conflitos, é necessário alterar a forma pela qual as Rules 
são executadas neste modelo. Ao invés de uma Rule aprovada instigar sua execução imediata, 
essa deve repassar o controle da execução da sua respectiva Action para o componente 
escalonador de Rules. Assim, ela é adicionada a uma fila de execução, considerando a 
prioridade de execução das respectivas Rules. Por sua vez, essas Rules são executadas de forma 
escalonada (NEVES, 2021). 
 
2.1.3.5 Compartilhamento de entidades do PON 
O compartilhamento de entidades tem o objetivo de eliminar a criação de entidades 
temporalmente e estruturalmente redundantes, o que está relacionado com o conceito da 


60 
 
 
‘reatividade das entidades’ (RONSZCKA, 2019; PORDEUS, 2020a). Um exemplo de uso 
desse mecanismo no PON seria um cenário em que diferentes Rules estão relacionadas às 
mesmas Premises, Conditions ou Instigations, as quais seriam compartilhadas já em tempo de 
construção do programa (NEVES, 2021).  
O Código 4 representa um exemplo de entidades compartilhadas para a aplicação de 
monitoramento de redes de sensores e alarmes em LingPON. Neste cenário, há três Premises 
(prAlarmOn, prSensor1 e prSensor2) e duas Conditions/Rules (em Rule Alarm 1 e Rule Alarm 
2), sendo que ambas as Rules dependem da Premise prAlarmOn. Neste contexto, a Premise 
prAlarmOn é considerada como uma entidade compartilhada, sendo que ambas as 
Conditions/Rules serão notificadas quando a Premise em questão for satisfeita (NEVES, 2021).  
 
Código 4- Exemplo de compartilhamento de Premise para a aplicação de Redes de Sensores na LingPON 
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
rule rlFireAlarm1 
 
condition       
 
 
premise prAlarmOn alarm.atOn   == true and            
 
 
premise prSensor1 sensor1.atStatus == true   
 
end_condition    
 
action      
 
 
instigation  
             
method siren.mtRingTheSiren();   
            end_instigation 
 
end_action 
end_rule 
. . . 
rule rlFireAlarm 
 
condition       
 
 
premise prAlarmOn and            
 
 
premise prSensor2 sensor2.atStatus == true   
 
end_condition    
 
action      
 
 
instigation  
             
method siren.mtRingTheSiren();   
            end_instigation 
 
end_action 
end_rule 
Fonte: Autoria própria 
 
É possível observar no Código 4 que a Premise compartilhada, uma vez declarada e 
nominada, pode ser reutilizada apenas declarando seu identificador, conforme mostrado pela 
linha 15. 
 


61 
 
 
2.1.3.6 Formation Rules ou Regras de Formação 
Este conceito permite a criação de Rules específicas a partir da representação genérica 
de uma Rule orientada a classes e não instâncias. Este conceito é aplicado quando o 
conhecimento causal de uma Rule é comum para diferentes conjuntos de instâncias de FBEs, 
ou seja, um conjunto de Rules específicas se diferencia apenas nas combinações das instâncias 
referenciadas (RONSZCKA, 2019; PORDEUS, 2020a). Em casos em que diversas Rules 
apresentam a mesma estrutura, porém se diferenciam apenas por serem referenciadas por 
instâncias de FBEs diferentes, o uso da Formation Rules é muito útil (RONSZCKA, 2019). 
Para exemplificar, considera-se um cenário hipotético de um sistema de alarme, no 
qual todos os usuários administradores do sistema teriam acesso a todas 124 as centrais de 
alarme conectadas. Nesse cenário, para avisar cada usuário administrador sobre eventuais 
disparos em cada uma das centrais de alarme conectadas, seria necessário replicar o 
conhecimento dessa condição para cada combinação de usuários e centrais de alarme. No caso 
de um cenário sem a utilização do conceito de Formation Rules seria necessário replicar as 
Rules manualmente para cada instância declarada, tornando o processo de desenvolvimento 
custoso e tendente a erros (RONSZCKA, 2019). 
 Em contrapartida, com o uso das Formation Rules, o conhecimento lógico-causal 
dessa Rule especial é informada de forma genérica, com base no modelo da classe de FBE User 
e FBE Central, em vez de instâncias pontuais de cada qual. Assim, em tempo de montagem do 
programa, cada combinação de instâncias de User e de Central (e.g., user1 x central1, user1 x 
central2, user2 x central1, user2 x central2), teriam instâncias pontuais e específicas dessa Rule 
genérica, formando uma composição de N x M instâncias (RONSZCKA, 2019). 
A Figura 16 ilustra um exemplo de Formation Rule que pode ser utilizada para gerar 
as instâncias das Rules referentes ao cenário hipotético apresentado de sistema de alarmes e 
usuários administradores. 
 
 
 
 
 
 
 


62 
 
 
Figura 16 - Exemplo de Formation Rule 
 
Fonte: Adaptado de BANASZEWSKI (2021) 
 
Uma Formation Rule é mais genérica do que uma Rule tradicional. Para sua descrição 
é utilizado o sufixo Form, que define as lógicas utilizadas como base para instanciar de forma 
efetiva cada uma das entidades do PON. As suas entidades Form somente analisam se o FBE é 
de uma determinada classe. Uma Formation Rule filtra e cria combinações de FBEs, sendo que 
cada combinação resulta na criação de uma Rule independente. Em suma, uma Formation Rule 
aplica conceitos genéricos a fim de criar Rules específicas, mantendo a capacidade de 
notificação entre os objetos colaboradores. A função principal desse conceito é gerar 
automaticamente a partir de um modelo várias instâncias de Rules que compartilham a 
semântica deste modelo (NEVES, 2021). 
 
2.1.3.7 Master Rule ou Dependência em Rules 
Este mecanismo é aplicado quando uma Rule é responsável pela ativação de outra 
Rule. Ou seja, quando Rules não são ativadas apenas pelo mecanismo de notificação 
convencional (i.e., por meio de uma Condition com valor lógico verdadeiro), porém pela 
ativação por meio do mecanismo de notificações convencional somada à aprovação de outra 
Rule da qual depende, a qual passa a ser chamada de Master Rule (RONSZCKA, 2019). Este 
mecanismo pode ser observado na representação da Figura 17. 
 
 


63 
 
 
Figura 17 - Exemplo de Master Rule 
 
Fonte: Autoria própria 
 
A Figura 17 mostra um exemplo de Master Rule correspondente a um sistema de 
monitoramento de alarme e sensores, com duas Rules e com dois FBEs para sensores. As duas 
Rules (rlFireAlarm1 e rlFireAlarm2) são compostas por duas Premises iguais, sendo que a Rule 
rlFireAlarm2 depende ainda de uma terceira Premise referente ao FBE Sensor2. Conforme 
exemplifica a Figura 17, com a aplicação de Master Rule neste cenário, a Rule rlFireAlarm2 
passa a ser aprovada somente após a aprovação da Rule rlFireAlarm1. 
Por consequência do uso deste mecanismo de Master Rule, a Rule dependente não 
precisa replicar as Premises que existem no contexto da Master Rule como ocorria na 
inexistência deste mecanismo. Assim, neste contexto dado, há uma redução de notificações 
geradas pelas Premises e Conditions que seriam compartilhadas pelas Rules dependentes no 
caso da ausência do mecanismo de Master Rule. No caso da existência do mecanismo em pauta 
justamente, quando essas Premises e Conditions forem aprovadas, suas notificações são 
direcionadas apenas a uma única Rule (Master Rule) que, por sua vez, notifica as demais Rules 
dependentes (RONSZCKA, 2012; RONSZCKA, 2019). 
 
2.1.3.8 FBE Rules ou Agregações de Rules em FBEs 
Basicamente, este conceito permite agregar uma Rule dentro do escopo de uma dada 
FBE (RONSZCKA, 2019; PORDEUS, 2020a). Na verdade, as agregações de Rules em FBEs 
podem ser consideradas como um caso particular do conceito de Formation Rules, no qual a 
Rule está relacionada apenas a um determinado tipo de FBE e é agregado dentro do escopo 
deste. Formation Rule aparece como um elemento com escopo global na aplicação, criando 


64 
 
 
relacionamentos N para M entre os FBEs participantes dessa regra especial. No caso específico 
de FBE Rules, as Rules possuem um escopo local ao FBE e todas as instâncias possuiriam 
obrigatoriamente uma instância da Rule em questão, formando um relacionamento N para 1 
(RONSZCKA, 2019). 
Para uma melhor compreensão, considera-se um cenário hipotético de um sistema de 
alarme, no qual, para ativar o disparo de alarmes, um dado tipo de sensor infravermelho 
precisaria atingir um certo nível de radiação. Em termos de implementação, seria necessária 
uma Rule específica para cada instância desse sensor. No caso de um cenário com um número 
elevado de sensores, sem a utilização do conceito de FBE Rules seria necessário replicar as 
Rules manualmente para cada instância declarada. Com a utilização do conceito de FBE Rules, 
por outro lado, seria possível criar uma Rule genérica que seria instanciada automaticamente a 
cada novo sensor adicionado ao sistema (RONSZCKA, 2019). O Código 5 apresenta um 
exemplo da estrutura sintática de um FBE Rule na LingPON. 
 
Código 5 - Exemplo de declaração de FBE Rule para o programa Sensores 
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
fbe Sensor 
    attributes 
        string atState false 
    end_attributes 
    fbeRule rlCheckSensorState  
        condition  
            subcondition  
                premise prSensorState Sensor.atState == true  
            end_subcondition  
        end_condition  
        action instigation  
            inFireAlarm alarm.fire();  
        end_action  
    end_fbeRule  
end_fbe 
Fonte: RONSZCKA (2019) 
 
De acordo com o Código 5, as palavras reservadas fbeRule e end_fbeRule (linhas 5 e 
14, respectivamente) identificam a declaração de uma Rule específica para o FBE Sensor. Na 
linha 8 do Código 4, a Premise em questão faz menção ao FBE Sensor e não a uma instância 
em particular. Assim, caso três instâncias do FBE Sensor forem criadas e nomeadas 
respectivamente como “sensor1”, “sensor2” e “sensor3”, o pré-compilador criará três Rules no 
código pré-compilado, diferenciando-as apenas pela instância associada. Nesse âmbito, ao 
aplicar o novo conceito não é necessário criar explicitamente no código-fonte uma Rule para 
cada um dos três sensores (RONSZCKA, 2019). 
 


65 
 
 
2.1.3.9 FBE Agregator ou FBE Agregador 
Este conceito permite a agregação entre FBEs, ou seja, a criação de FBE dentro do 
escopo de outra FBE, além dos tipos de dados primitivos (i.e., boolean, char, integer, float e 
string). Com a criação de FBEs compostos, não há a necessidade de replicar estruturas, 
tornando o código mais coeso e sucinto. Isto permite atingir níveis de organização mais efetivos, 
melhorando particularmente a escrita e a legibilidade de programas baseados no PON 
(RONSZCKA, 2019). 
Para exemplificar, considera-se o cenário de um sistema de monitoramento de alarmes 
e sensores, no qual o FBE Sector é composto (i.e., agrega) por um sensor (FBE Sensor) e este, 
por sua vez, apresenta um alarme (FBE Alarm). Para cada instância da FBE Sector seria 
possível criar uma instância de cada uma das FBEs agregadas, bem como o relacionamento 
pontual entre elas (RONSZCKA, 2019). A Figura 18 ilustra este cenário. 
 
Figura 18 - Exemplo de Agregação de FBEs 
 
Fonte: Autoria própria 
 


66 
 
 
2.1.3.10 Keeper Rule ou Regra Mantenedora  
Este conceito permite que uma Rule execute sua Action quantas vezes for necessário 
enquanto a respectiva Rule estiver aprovada e não apenas quando for aprovada, ou seja, apenas 
quando ocorre alteração no estado de Attributes (RONSZCKA, 2019; NEVES, 2021). O Código 
6 apresenta um exemplo do uso do padrão keeper na LingPON. 
 
Código 6 - Exemplo de utilização do padrão keeper na LingPON 
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
rule rlFireAlarm  
    properties 
        keeper true  
    end_properties  
    conditions  
. . . 
    end_conditions  
    action  
. . .  
    end_action  
end_rule 
Fonte: Adaptado de RONSZCKA (2019) 
 
2.1.3.11 Resumo dos conceitos 
O Quadro 4 a abaixo mostra um resumo dos nomes dos principais conceitos de programação em 
PON e sua funcionalidades. 
 
Quadro 4 - Resumo dos conceitos de programação do PON 
Reatividade das 
entidades 
Notificações pontuais entre as entidades do PON à luz do cálculo assintótico e da 
plataforma utilizada 
Entidades 
impertinentes 
Quando uma entidade PON permite desativar temporariamente a geração de notificações 
para evitar notificações desnecessárias e redundantes 
Unique Premise 
Premise que notifica diversas Conditions excludentes entre si. Quando uma dessas 
Conditions é aprovada, encerra o fluxo de notificação da Premise para demais 
Conditions 
Escalonamento de 
Rules e Resolução 
de conflitos 
Mecanismo de decisão das ordens das execuções das Rules aprovadas 
Compartilhamento 
de entidades 
Compartilhamento de entidades do PON com o objetivo de eliminar a criação de 
entidades redundantes temporalmente e estruturalmente 
Formation Rules 
Permite a criação de Rules específicas a partir da representação genérica de uma Rule 
orientada a classes e não instâncias 
Master Rules 
Conceito aplicado quando uma Rule é responsável pela ativação de outra Rule. Ou seja, 
quando uma Rule depende de outra 
FBE Rules 
Permite agregar uma Rule dentro do escopo de uma dada FBE 
FBE Agregator 
Permite agregar uma FBE dentro do escopo de uma dada FBE 


67 
 
 
Keeper Rule 
Permite uma Rule executar sua Action com uma dada frequência enquanto ela estiver 
aprovada e não apenas quando for aprovada 
Fonte: Adaptado de PORDEUS (2020) 
 
Por sua vez, o Quadro 5 abaixo mostra as materializações do PON vis-à-vis ao contemplar 
ou não desses conceitos de programação. Muito embora algumas materializações contemplem 
grande parte dos conceitos, elas simplesmente não contemplam as propriedades elementares do 
PON, cf. discutido na Seção 2.1.2, particularmente o desenvolvimento declarativo em alto-
nível. 
 
Quadro 5 - Conceitos de programação contemplados nas materializações do PON 
        Materialização 
 
Propriedade 
Software 
Hardware 
FW 
Prot. 
FW 
1.0 
FW 
2.0 
FW 
3.0 
FW 
JAVA C# 
FW 3.0 + 
PON IP 
PONHD 
Prot 
CoPON 
Prot. 
NOCA 
1.0 
PONHD 
1.0 
Reatividade das 
entidades 
 
 
 
 
 
 
 
 
 
 
Entidades 
impertinentes 
 
 
 
 
 
 
 
 
 
 
Unique Premise 
 
 
 
 
 
 
 
 
 
 
Escalonamento de 
Rules e Resolução 
de conflitos 
 
 
 
 
 
 
 
 
 
 
Compartilhamento 
de entidades 
 
 
 
 
 
 
 
 
 
 
Formation Rules 
 
 
 
 
 
 
 
 
 
 
Master Rules 
 
 
 
 
 
 
 
 
 
 
FBE Rules 
 
 
 
 
 
 
 
 
 
 
FBE Agregator 
 
 
 
 
 
 
 
 
 
 
Keeper Rule 
 
 
 
 
 
 
 
 
 
 
Fonte: RONSZCKA (2019) 
 
2.2 
Visão Geral da Tecnologia LingPON, GRAFO PON E MCPON 
A Tecnologia LingPON surgiu para materializar o PON de uma maneira mais 
adequada e que vem sendo melhorada a cada versão, desde sua versão preliminar (ou 
prototipal), passando pela 1.0 e, finalmente, chegando na versão atual, a versão 2.0. Isto 
certamente graças ao método MCPON, seus conceitos de base e seu elemento basilar chamado 
de Grafo PON. Este presente trabalho visa contribuir com o estudo e desenvolvimento da 
tecnologia em questão, na versão 2.0 mais precisamente, sempre à luz do método dado, o 
MCPON.  
Uma contribuição visada neste trabalho se trata da expansão linguística inclusive em 
termos de conceitos de programação do PON da chamada LingPON 2.0, a principal linguagem 


68 
 
 
da atual Tecnologia LingPON 2.0. Outra contribuição refere-se a uma melhor completude na 
compilação, de instância de Grafo PON da LingPON 2.0, para a geração de código alvo (target) 
em C++ Notificante Modular orientado a Espaço de Nomes (Namespaces). 
Neste âmbito, esta seção apresenta os principais conceitos fundamentais para o 
embasamento dessa pesquisa no tocante a Tecnologia LingPON. Primeiramente, será 
apresentada uma visão geral do método MCPON, do Grafo PON (elemento fundamental deste 
método), da LingPON (sua linguagem de programação) e da Tecnologia LingPON em si que 
envolve também um sistema de compilação (sempre à luz do MCPON com seu Grafo PON). 
Em particular, no sistema de compilação, há os geradores de código que permitem, a partir do 
Grafo PON, alcançar código para plataformas distintas de qualquer programa em LingPON 
mapeado em instância do Grafo PON.  
Neste trabalho, há interesse especial na geração de código para o target em C++ 
Notificante Modular orientado a Namespaces (NPCPP). Assim, na sequência deste capítulo, 
em outra seção serão descritas de forma mais detalhada as versões single-threaded e 
multithread do gerador de código NPCPP 1.0, compilador para o target C++ Notificante 
Modular orientado a Namespaces, construído via Tecnologia LingPON 1.2. Por fim, em outra 
seção ainda, serão apresentadas algumas reflexões sobre este capítulo, salientando a lacuna ou 
gap existente no contexto dado da Tecnologia LingPON 2.0 para o target em questão. 
 
2.2.1 Método MCPON 
 
Conforme apresentado no Capítulo 1, como o PON se baseia em uma nova forma de 
construir e conectar as colaborações de um programa por meio de entidades notificantes, os 
métodos e técnicas em que se baseiam as teorias tradicionais de compilação não apresentam 
características desejadas e ideais para a criação de compiladores próprios para o PON. Por isso, 
em sua tese de doutorado, A. F. Ronszcka criou o Método de Compilação para o PON 
(MCPON), um novo método para uniformizar a construção de linguagens e compiladores 
próprios para o PON em plataformas distintas baseado em um novo conceito que é o Grafo 
PON (RONSZCKA, 2019). 
Para a estruturação do MCPON, a primeira etapa foi definir um conjunto de diretrizes 
e regras para a construção de uma representação intermediária mais adequada para programas 
PON. Essa representação substituiria as representações baseadas em árvore e, mesmo, as 
representações codificadas em linguagens de mais baixo nível, utilizadas nos métodos de 


69 
 
 
compilação tradicionais. Pelas características notificantes do paradigma, foi concluído que a 
estrutura de dados mais apropriada para representar um programa PON seria em forma de grafos 
de notificações, justamente o assim chamado Grafo PON (RONSZCKA, 2019). 
O Grafo PON, então desenvolvido para compor essa representação intermediária, 
mapeia por completo os programas PON na forma de entidades notificantes desacopladas em 
instâncias deste peculiar grafo, sem perder a essência do paradigma. Dessa forma, o Grafo PON 
se constitui em um dos elementos fundamentais do MCPON. Sempre orbitando no Grafo PON, 
o método de compilação em questão, o MCPON, é composto por cinco etapas bem definidas 
(RONSZCKA, 2019). Naturalmente, estas etapas serão detalhadas em seção subsequente 
pertinente.  
 
2.2.2 Grafo PON 
Em linhas gerais, o MCPON traz uma inovação, em especial, no processo de 
compilação. Inovação essa que permite traduzir programas distintos escritos em linguagens 
próprias para o PON em uma única estrutura de dados, que possui a forma de grafo genérico de 
notificações. Essa estrutura, conhecida como Grafo PON, conforme já dito, foi implementada 
como um framework em C++ orientado a objetos, de forma que permite criar sua instância para 
comportar os programas advindos da LingPON, bem como navegar nas instâncias para fins de 
geração de código (RONSZCKA, 2019). 
Uma vez que um programa PON naturalmente segue um modelo de interconexões de 
entidades notificantes, seria inviável a utilização de árvores sintáticas abstratas para o seu 
mapeamento, como ocorre nos métodos tradicionais de compilação. Neste âmbito, uma 
instância do Grafo PON seria a representação completa de todos os elementos participantes no 
processo de notificação de um dado programa PON (RONSZCKA, 2019). 
Seguindo as diretrizes do MCPON, para a construção dos grafos especializados, ou 
instâncias do Grafo PON, cada instância armazenaria todos os elementos de um dado programa 
escrito em LingPON (ou outra linguagem baseada em PON). Ainda, tal instância permitiria 
mapear tanto as particularidades das entidades que compõe o programa, quanto as conexões de 
toda a cadeia de notificações, conforme apresentado anteriormente na Seção 1.3. Por esse 
motivo, é possível reconstruir qualquer programa PON baseado nesta representação 
intermediária especializada, com a condição de que sejam seguidas algumas diretrizes para a 
construção dessa estrutura (RONSZCKA, 2019). 


70 
 
 
A Figura 19 representa de forma ilustrativa como seria a composição de uma instância 
do Grafo PON. 
 
Figura 19 - Representação ilustrativa de um Grafo PON 
 
Fonte: RONSZCKA (2019) 
 
Conforme a Figura 19 mostra, cada recorrência de um elemento significativo de um 
dado programa (e.g. FBE, Instâncias de FBE, Attributes de instâncias de FBE etc.) seria 
mapeada no Grafo PON por um nó. Ainda, cada relação notificante entre as entidades é 
representada por ligações (i.e., arestas) (RONSZCKA, 2019). 
O Grafo PON foi construído com a finalidade de auxiliar no processo de compilação, 
de forma a mapear por completo a essência de um dado programa em PON em uma dada 
instância do grafo. É por meio deste mapeamento fidedigno que se permite a tradução dessa 
instância do grafo para um código-alvo desejado. Portanto, esse processo finalmente 
corresponde a uma das principais etapas de um compilador para o PON (RONSZCKA, 2019). 
 
2.2.3 Tecnologia LingPON 
Para materializar o PON de forma efetiva foi necessário o desenvolvimento de uma 
linguagem de programação específica e um sistema de compilação próprio para esse novo 
paradigma. A primeira linguagem prototipal para o PON foi denominada de LingPON 
Prototipal e, juntamente com o seu respectivo sistema de compilação também prototipal, foi 


71 
 
 
criado um conjunto de técnicas próprias ao PON, que conjuntamente, deram origem a 
Tecnologia LingPON e, concomitantemente, ao método MCPON.  
A Tecnologia LingPON (LingPON e respectivo sistema de compilação) em versão 
prototipal evoluiu dando origem as novas versões da Tecnologia LingPON, nomeadamente a 
Tecnologia LingPON 1.0 e, a sua atual versão mais estável, a Tecnologia LingPON 2.0, também 
conhecida NOPL (NOP Language) em idioma inglês (RONSZCKA, 2019). Nas subseções 
subsequentes serão apresentadas cada versão dessa Tecnologia LingPON, bem como suas 
características e contribuições. 
 
2.2.3.1  Tecnologia LingPON Prototipal 
A Tecnologia LingPON Prototipal foi liderada por A. F. Ronszcka, sendo a 
especificação da linguagem em si definida por ele, bem como a primeira versão do sistema de 
compilação, cujo primeiro target foi para o Framework PON C++ 2.0, framework este 
desenvolvido por Valença (2012) e por Ronszcka (2012). Neste âmbito, também A. F. 
Ronszcka iniciou a definição dos passos a serem seguidos na composição de compiladores para 
o PON (RONSZCKA et al., 2013), o que subsequentemente foi chamado de MCPON na sua 
tese de doutorado (RONSZCKA, 2019). 
De maneira geral, a especificação da linguagem de programação propriamente dita, 
chamada de LingPON prototipal, segue uma estrutura de programação declarativa. Um 
programa em PON é basicamente definido em três blocos principais: definição de FBEs, 
instanciações de FBEs e declaração das Rules (RONSZCKA, 2019). O Código 7 traz um 
exemplo de programa em LingPON prototipal. 
 
Código 7 - Exemplo de programa implementado em LingPON prototipal 
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
fbe Alarm  
    attributes  
        boolean atOn false  
    end_attributes  
end_fbe  
fbe Sensor  
    attributes  
        boolean atState false  
    end_attributes  
end_fbe  
fbe Siren  
    attributes  
        boolean atOn false  
    end_attributes  
    methods  


72 
 
 
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
37 
38 
39 
40 
        method mtRingTheSiren(atOn = true)  
    end_methods  
end_fbe  
 
inst  
    Alarm alarm  
    Sensor sensor  
    Siren siren  
end_inst  
 
strategy  
    no_one  
end_strategy 
 
rule rlFireAlarm 
    condition       
        premise prAlarmOn alarm.atOn   == true and            
        premise prSensor sensor.atStatus == true   
    end_condition    
    action      
        instigation  
            method siren.mtRingTheSiren();   
        end_instigation 
    end_action 
end_rule 
Fonte: RONSZCKA (2019) 
 
A implementação da LingPON Prototipal foi acompanhada pelo desenvolvimento do 
Sistema de Compilação Preliminar, no qual surge o primeiro conceito e mesmo materialização 
do Grafo PON. Neste quadro, a luz do Grafo PON, inicialmente foi composto por três geradores 
de código distintos, os quais tinham como códigos-alvo ou target: (1) o Framework PON C++ 
2.0, (2) código notificante em linguagem C e (3) código notificante em linguagem C++. O 
gerador para o target C notificante foi desenvolvido por P. A. de Moraes Ioris, enquanto o 
target C++ notificante foi desenvolvido por C. A. Ferreira, ambos seguindo os passos do proto-
MCPON na época. A Figura 20 traz a visão geral do processo de compilação utilizado para tais 
geradores de código. 
 
 
 
 
 
 
 
 
 


73 
 
 
Figura 20 - Processo de compilação e os componentes do compilador PON 
 
Fonte: FERREIRA (2015) 
 
A Tecnologia LingPON Prototipal foi um avanço considerável para o grupo de 
pesquisa do PON, pois dela se originou, finalmente, uma linguagem própria ao paradigma sendo 
esta declarativa e em alto nível. Ademais, no tocante a geração de código nos targets de códigos 
notificantes em C e em C++, o ganho de desempenho vis-à-vis em relação ao Framework 2.0 
foi substancial. A Figura 21 mostra a comparação de resultados de tempo de execução em um 
cenário com 100 Rules em Tecnologia LingPON Prototipal com targets: “C” (C específica a 
notificações), 
“C++” 
(C++ 
específica 
a 
notificações) 
e 
“Framework” (Framework PON C++ 2.0).  
 
Figura 21 - Comparação de tempo de execução do Mira-Alvo em Tecnologia LingPON Prototipal 
 
Fonte: RONSZCKA (20219) 
 


74 
 
 
A aplicação Mira Alvo, utilizada para as comparações apresentadas na Figura 21, é 
semanticamente equivalente ao exemplo de sensores e alarmes usado no código em LingPON, 
sendo que basicamente são alterados o nome das FBEs para um novo contexto. Isto dito, a fim 
de realizar comparações de eficiência entre as três versões de código geradas, um estudo 
comparativo de desempenho foi realizado para três cenários: 1, 10 e 100 Rules, sendo que para 
cada um destes cenários foram executadas 1, 10, 100, 1.000, 10.000 e 100.000 iterações. Além 
disso, os testes foram realizados em duas arquiteturas de sistemas operacionais (i.e., 32 e 64 
bits). Em suma, a versão em C notificante executou o mesmo programa com muito menos 
tempo em comparação com a versão C++ notificante e a versão baseada no Framework PON 
C++ 2.0 em praticamente todos os cenários de testes (RONSZCKA et al., 2013; RONSZCKA, 
2019).  
 
Quadro 6 - Propriedades fundamentais do PON contempladas na Tecnologia LingPON Prototipal 
                     Materialização 
 
Propriedade 
 
Software 
Alvo (target) 
FW 2.0 
C notificante 
C++ notificante 
Ano 
2013 
2013 
2013 
Prog. Alto nível 
✓ 
✓ 
✓ 
Desacoplamento/Paralelismo 
 
 
 
Desacoplamento/Distribuição 
 
 
 
Não-Redundância/Desempenho 
 
✓ 
 
Fonte: Adaptado de PORDEUS (2020) 
 
O Quadro 6 apresenta a relação das propriedades elementares do PON contempladas 
por cada um dos targets, à luz da Tecnologia LingPON prototipal. O Quadro 7, por sua vez, 
mostra tais materializações em relação aos conceitos de programação implementados. 
 
Quadro 7 - Conceitos de programação PON contempladas na Tecnologia LingPON Prototipal 
                           Materialização 
 
Conceitos de 
 Programação 
 
Software 
Alvo (target) 
FW 2.0 
C notificante 
C++ notificante 
Ano 
2013 
2013 
2013 
Reatividade das entidades 
✓ 
✓ 
✓ 
Escalonamento de Rules 
 
 
 
Estratégias de resolução de conflito 
 
 
 
Compartilhamento de entidades 
 
 
 
Regras de formação 
 
 
 
Propriedades reativas dos Attributes 
 
 
 
Master Rule 
 
 
 
Entidades impertinentes 
 
 
 
FBE Rules 
 
 
 
FBE Agregator 
 
 
 
Keeper Rule 
 
 
 
Vetores 
 
 
 
Unique Premise 
 
 
 
Fonte: Adaptado de PORDEUS (2020) 
 


75 
 
 
De maneira geral, os resultados mostraram um potencial do PON em termos de 
desempenho, no entanto, essa versão prototipal possibilitou apenas a implementação de 
programas básicos, e.g., execução de Methods com atribuições simples. Neste sentido, foi 
desenvolvida por C. A. Ferreira a versão conhecida como Tecnologia LingPON 1.0, a fim de 
adicionar outras funcionalidades essenciais e desejáveis a LingPON enquanto linguagem (e.g. 
Methods com operações aritméticas e Methods para integração com códigos legados em 
C/C++), bem como melhoria do sistema de compilação com estas funcionalidades. Também 
houve melhorias de código gerado nos target existentes (particularmente para o C++ 
notificante) e, ademais, novos targets (FERREIRA, 2015; RONSZCKA, 2019). 
 
2.2.3.2  Tecnologia LingPON 1.0 
A Tecnologia LingPON 1.0 foi a primeira versão mais elaborada no tocante a linguagem 
de programação LingPON, sendo que apresenta alguns conceitos que não haviam sido 
contemplados e implementados ainda na Tecnologia LingPON Prototipal. Um desses conceitos 
seria o conjunto das Propriedades das Rules, que consiste em um sub-bloco opcional de 
propriedades. Isto é definido pelas palavras reservadas property e end_property no escopo das 
Rules, possibilitando a definição de algumas características adicionais para essas entidades 
enfim. As linhas 30 a 44 do Código 8 mostram um exemplo de Rule que apresenta o bloco de 
propriedades (FERREIRA, 2015; RONSZCKA, 2019). 
 
Código 8 - Exemplo de programa implementado em LingPON 1.0 
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
fbe Alarm  
    attributes  
        boolean atOn false  
    end_attributes  
end_fbe  
fbe Sensor  
    attributes  
        boolean atState false  
    end_attributes  
end_fbe  
fbe Siren  
    attributes  
        boolean atOn false  
    end_attributes  
    methods  
        method mtRingTheSiren(atOn = true)  
    end_methods  
end_fbe  
 
inst  


76 
 
 
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
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
48 
    Alarm alarm  
    Sensor sensor  
    Siren siren  
end_inst  
 
strategy 
    no_one 
end_strategy 
 
rule rlFireAlarm 
    properties 
        priority 1 
        keeper true 
    end_properties 
    condition   
        subcondition a1 
            premise prAlarmOn alarm.atOn   == true and        
            premise prSensor sensor.atStatus == true   
        end_subcondition 
    end_condition    
    action      
        instigation inFireAlarm siren.mtRingTheSiren();    
    end_action 
end_rule 
 
main { 
    sensor->setatStatus(true); 
} 
Fonte: Adaptado de RONSZCKA (2019) 
 
Em sua pesquisa, Ferreira (2015) definiu também um novo bloco, denominado main, 
na estrutura geral de um programa em PON. O Código 8 apresenta um exemplo de utilização 
dessa contribuição, nas linhas 46 a 48. O bloco main basicamente é utilizado para a definição 
das primeiras atribuições dos valores do Attributes e, consequentemente, para a inicialização 
do programa. Uma vez que o valor de um ou mais Attributes é alterado, é possível dar início ao 
fluxo de execução de notificações. É pertinente observar que o conteúdo dentro do escopo do 
bloco main não é traduzido para a linguagem-alvo, mas apenas transcrito para o código gerado. 
Portanto, é necessário que este trecho de código esteja implementado de acordo com a 
linguagem-alvo escolhida (RONSZCKA, 2019).  
Outro conceito implementado nesta versão da LingPON é o de Entidades 
Impertinentes, favorecendo o desempenho da execução, uma vez que evita notificações 
desnecessárias (FERREIRA, 2015; RONSZCKA, 2019). Em suma, para a implementação 
desses conceitos foi necessário adicionar novas palavras reservadas a LingPON e, 
consequentemente, adequar os analisadores léxico e sintático para tratar os novos símbolos 
adequadamente. Além disso, foi necessário adicionar novos elementos no Grafo PON de modo 
a mapear fidedignamente tais conceitos. No entanto, não houve modificação elementar no 
Sistema de Compilação Preliminar em si salvo a dita expansão do grafo (RONSZCKA, 2019).  


77 
 
 
                  Milissegundos 
A Figura 22 apresenta os resultados, obtidos em milissegundos, de testes realizados 
utilizando o programa Mira ao Alvo, semanticamente equivalente ao exemplo de sensores e 
alarmes (cf. já dito), para aplicar aos targets C notificante, C++ notificante e Framework PON 
C++ 2.0. Em tempo, Ferreira (2015) fez uma série de ajustes, melhorias e mesmo eliminação 
de imperfeições no tocante ao target C++ notificante nesta nova versão.  
 
Figura 22 - Comparação de tempo de execução (em ms) do  
programa Mira-Alvo na Tecnologia LingPON 1.0 
 
 
 
 
 
 
 
 
 
 
 
 
Fonte: FERREIRA (2015) 
 
Conforme os resultados apresentados na Figura 22, tanto o código específico PON 
gerado para linguagem C quanto para linguagem C++ obtiveram resultados melhores em termos 
de tempo de execução quando comparado ao código PON gerado Framework PON em C++. 
Tais resultados se explicam porque os códigos C notificante e C++ notificante não usam 
estruturas de dados genéricas e sim módulos para cada entidade PON que se notificam entre si 
por meio de ponteiros diretos. Ao bem da verdade, estes resultados proveram entusiasmo ao 
grupo de pesquisa do PON, pois finalmente programas em PON começavam a efetivamente 
condizer com o previsto em cálculo assintótico em termos de performance.  
Neste âmbito, em 2016, inicialmente Melo adaptou o Framework PON C++ 2.0 para 
as particularidades da lógica nebulosa (fuzzy). Ainda, Melo (2016) também apresentou um novo 
dialeto da LingPON (denominada LingPONFuzzy), à luz do MCPON, contemplando também 
as novas características criadas para atender a lógica fuzzy. Por conta das mudanças realizadas 
na linguagem, Melo precisou fazer adaptações tanto na etapa de análise léxica quanto na etapa 
de análise sintática. Além disso, para o Grafo PON também foram propostas e criadas novas 
entidades, assim como foram mapeadas características adicionais, principalmente para suportar 
as adaptações da linguagem.  


78 
 
 
Também foi desenvolvida outra materialização do PON no campo de Hardware Digital 
(HD). Mais precisamente, Kerschbaumer (2018) desenvolveu uma implementação do PON 
para HD, na qual todos os elementos desse paradigma são modelados em blocos de lógica 
reconfigurável, utilizando a linguagem VHDL. Essa implementação foi denominada de PON-
HD 1.0, acompanhada de sua respectiva linguagem de programação conhecida como LingPON 
HD, sendo desenvolvida para facilitar a síntese em FPGA. Entretanto, esta LingPON HD 
prototipal inicialmente não fez uso do Grafo PON (RONSZCKA, 2019).  
Em um segundo momento, no entanto, Kerschbaumer (2018) criou uma nova versão 
de geração de código, especialmente para o PON-HD 1.0, à luz do método MCPON. A criação 
desse novo gerador de código seguindo os padrões do MCPON possibilitou que a compilação 
em PON-HD fosse compatível com o sistema de compilação do PON orientada ao Grafo PON, 
permitindo a construção de programas em alto nível, além de apresentar também as 
propriedades elementares de paralelismo e desempenho efetivo. Com isso, a Tecnologia 
LingPON-HD 1.0 se tornou a primeira materialização efetiva do PON em um ambiente 
totalmente paralelo (RONSZCKA, 2019). 
É possível observar a relação das propriedades elementares do PON contempladas para 
cada um dos targets para a Tecnologia 1.0 pelo Quadro 8 e a relação dos conceitos de 
programação implementados para essas materializações são apresentadas no Quadro 9.  
 
Quadro 8 - Propriedades fundamentais do PON contempladas na Tecnologia LingPON 1.0 
Materialização 
 
 
   Propriedade 
 
Software 
Hardware 
Alvo (target) 
FW 2.0 
C 
C++ 
Fuzzy 
PONHD 1.0 
Ano 
2013 
2013 
2013 
2016 
2018 
Prog. Alto nível 
 
✓ 
✓ 
✓ 
✓ 
✓ 
Desacoplamento/Paralelismo 
 
 
 
 
 
✓ 
Desacoplamento/Distribuição 
 
 
 
 
 
 
Não-Redundância/Desempenho 
 
 
✓ 
 
 
✓ 
Fonte: Adaptado de PORDEUS (2020) 
 
Quadro 9 - Conceitos de programação PON contempladas na Tecnologia LingPON 1.0 
                          Materialização 
 
 
Conceitos de programação 
 
Software 
Hardware 
Alvo (target) 
FW 2.0 
C 
C++ 
Fuzzy 
PONHD 1.0 
Ano 
2013 
2013 
2013 
2016 
2018 
Reatividade das entidades 
✓ 
✓ 
✓ 
✓ 
✓ 
Escalonamento de Rules 
 
 
 
 
 
Estratégias de resolução de conflito 
 
 
 
 
 
Compartilhamento de entidades 
 
 
 
 
 
Regras de formação 
 
 
 
 
✓ 
Propriedades reativas dos Attributes 
 
 
 
 
✓ 
Master Rule 
 
 
 
 
 
Entidades impertinentes 
 
 
 
 
 


79 
 
 
FBE Rules 
 
 
 
 
 
FBE Agregator 
 
 
 
 
 
Keeper Rule 
✓ 
 
 
 
 
Vetores 
 
 
 
 
 
Unique Premise 
 
 
 
 
 
Fonte: Adaptado de PORDEUS (2020) 
 
Em termos de facilidade de programação, a Tecnologia LingPON 1.0 se mostrou como 
uma alternativa mais prática em relação à versão prototipal, em que pese um conjunto de 
imperfeições e mesmo falhas (bugs) percebidos ao longo dos seus usos experimentais. Além 
disso, essa versão ainda apresenta alguns problemas de falta de padronização, como por 
exemplo a própria criação do novo bloco principal main, o qual uma vez utilizado, torna o 
código compilável apenas na plataforma pré-definida (RONSZCKA, 2019). A Tecnologia 
LingPON continuou evoluindo à medida que algumas melhorias foram implementadas, sendo 
que a versão seguinte é a assim denominada Tecnologia LingPON 1.2, detalhada a seguir. 
 
2.2.3.3  Tecnologia LingPON 1.2 
A versão LingPON 1.2 foi estruturada visando à melhoria em termos de facilidade de 
programação, desenvolvendo a linguagem para possibilitar sua aplicação em programas de 
maior complexidade (RONSZCKA, 2019). Uma dessas evoluções foi a implementação do 
conceito de Regras de Formação (Formation Rules), que consiste na possibilidade de criar 
regras específicas a partir de uma Rule genérica, conforme mencionado anteriormente. 
Ademais, a versão em questão apresenta também o conceito de FBE Rules, que permite FBE 
agregar Rules, conforme também já ensinado anteriormente.  
Outro ponto de melhoria foi que a LingPON apresentava algumas limitações referentes 
à agregação de FBEs em FBEs. Para solucionar isso, a LingPON 1.2 possibilita criar agregações 
entre FBEs, a fim de que esses possam comportar outros FBEs. Dessa forma, aumenta-se o 
encapsulamento tal qual o conceito de FBE Rule justo supramencionado também provê suas 
contribuições em termos de encapsulamento (SANTOS, 2017; RONSZCKA, 2019). 
No Código 9, é possível observar justamente um exemplo de agregação de FBEs (linha 
9), bem como um exemplo do uso de FBE Rules (linhas 11 a 20). 
 
Código 9 - Exemplo de programa implementado em LingPON 1.2 
1 
2 
3 
4 
fbe Alarm  
    attributes  
        boolean atOn false  
    end_attributes  


80 
 
 
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
end_fbe  
fbe Sensor  
    attributes  
        boolean atState false  
        Alarm alarm 
    end_attributes 
    fbeRule rlCheckSensorState  
        condition  
            subcondition  
                premise prSensorState Sensor.atState == true      
            end_subcondition  
        end_condition  
        action  
            instigation inFireAlarm alarm.fire();  
        end_action  
    end_fbeRule  
end_fbe 
fbe Siren  
    attributes  
        boolean atOn false  
    end_attributes  
end_fbe  
 
inst  
    Sensor sensor  
    Siren siren  
end_inst  
 
strategy 
    no_one 
end_strategy 
Fonte: Adaptado de RONSZCKA (2019) 
 
No âmbito da Tecnologia LingPON 1.2, adicionalmente uma nova versão de geração 
de código foi criada, denominada LingPON Estática (Static), a qual proporcionou uma 
diminuição no tempo de processamento em relação a outras gerações de código em linguagem 
C++. Em linhas gerais, uma das características fundamentais dessa versão foi eliminar a 
utilização de atributos e métodos de instância, transformando todos eles em elementos estáticos 
(static). Dessa forma, a estrutura geral do programa gerado não utiliza variáveis nem instâncias 
de classe não estática (i.e., classes usuais) (SCHÜTZ et al., 2015; SCHÜTZ, 2019; 
RONSZCKA, 2019).  
Ademais, na assim chamada LingPON Estática, o espaço de armazenamento para os 
objetos é alocado quando o programa inicia e desalocado quando o programa termina, 
utilizando apenas uma instância do objeto. Este processo elimina o tempo de alocação dinâmica 
durante a execução do programa. Cada uma das entidades PON proposta para essa versão foi 
compilada no formato de classe estática (SCHÜTZ et al., 2015; SCHÜTZ, 2019; RONSZCKA, 
2019). 


81 
 
 
Foram realizados experimentos para validar essa versão e comparar seu desempenho 
com duas outras versões: linguagem C específica a notificações (Tecnologia LingPON 1.0) e 
linguagem C++ específica a notificações (Tecnologia LingPON 1.0). Nesse experimento foram 
realizadas um milhão de alterações nos Attributes, de modo a ativar as Rules pertinentes. A 
Figura 23 apresenta os resultados do experimento, no qual o gráfico foi dividido em duas partes. 
A primeira parte (lado esquerdo) apresenta o resultado para compilação monoprocessada sem 
parâmetros de otimização para o compilador G++. O segundo experimento (lado direito) levou 
em conta a ativação da otimização O3 no compilador G++ (SCHÜTZ et al., 2015; SCHÜTZ, 
2019; RONSZCKA, 2019). 
 
Figura 23 - Experimento de tempo de execução entre versões da LingPON 
 
Fonte: RONSZCKA (2019) 
 
Conforme é apresentado na Figura 23, no primeiro experimento, a versão de código C 
específico a notificações apresentou os melhores resultados, mesmo em comparação com a 
nova versão de código C++ estático (a notificações certamente). Entretanto, a versão de código 
C++ estático apresentou-se mais eficiente que a versão de código C++ específico a notificações 
(SCHÜTZ et al., 2015). Com ela foi possível observar uma melhora significativa das versões 
de código C++ específico a notificações e versão de código C++ estática em comparação com 
a versão C específica a notificações (SCHÜTZ et al., 2015; RONSZCKA, 2019). 
Apesar de a versão LingPON Estática ter apresentado um desempenho satisfatório, 
houve uma dificuldade em termos de integração com outros códigos legados em C++. Essa 
dificuldade se deu principalmente por todo o código ser orientado a atributos e métodos 
estáticos do C++, o que inviabiliza a integração com código usual (SCHÜTZ et al., 2015; 
SCHÜTZ et al., 2018; RONSZCKA, 2019). Neste sentido, Athayde e Negrini (2016) 
construíram uma versão de geração de código chamada de LingPON Espaço de Nomes 


82 
 
 
(Namespaces), no qual cada entidade do PON é tratada por um espaço de nomes (namespace) 
e não classe ou objetos visando assim eliminar sobrecargas de OO e afins. Dessa forma, foi 
possível manter o baixo tempo de processamento da versão estática, propondo uma solução 
para os problemas de integração dessa última por não usar nada estático justamente 
(ATHAYDE E NEGRINI, 2016; RONSZCKA, 2019).  
Já no âmbito do Sistema de Compilação, Negrini (2016) propôs alterações em algumas 
etapas do MCPON, particularmente na BNF (Backus-Naur Form) da linguagem LingPON 1.2 
e na análise sintática, além da fase de criação de otimizadores genéricos independentes de 
target. Em suma, tais otimizações buscaram eliminar a redundância de Premises, buscando 
manter a essência de não-redundância do PON preservada, dado que se havia observado 
imperfeições neste âmbito justamente (RONSZCKA, 2019). 
As versões LingPON Static e LingPON Namespace foram testadas com o programa 
Eletronicgate (portão eletrônico) e, para esse experimento, considerou-se o tempo, em 
segundos, de um milhão de acionamentos de portão (aprovação da Rule). Ainda, a compilação 
no G++ foi realizada em otimização O3 em um ambiente Linux, para ambas as versões 
(ATHAYDE e NEGRINI, 2016). O experimento em si contou com oito mil amostras do 
resultado, o qual é apresentado pela Figura 24. Os resultados foram comparados por meio dos 
seguintes parâmetros: valor mínimo (MIN), valor médio (MÉDIA), valor mediano (MED) e 
valor máximo (MAX) amostrados do tempo de execução. 
 
Figura 24 -  Comparação entre versão estática e versão espaço de nomes para o programa Sensores 
 
Fonte: RONSZCKA (2019) 
 
Conforme apresenta a Figura 244, os resultados se mostraram satisfatórios, uma vez 
que não reduziram o desempenho em relação à versão de código específico do PON em C++ 
                                                          
4 Até este momento, o compilador dito LingPON Static foi o que apresentou melhor resultado 
em termos de desempenho, conforme mostrado pela Figura 23, ainda que limítrofe em relação ao 
compilador LingPON Namespace. 


83 
 
 
estático. Nesse contexto, tal implementação trouxe um impacto positivo, uma vez que resolve 
a deficiência de não possibilitar a extensibilidade do código, presente na versão do código 
específico PON em C++ estático, cf. já dito anteriormente neste presente trabalho (ATHAYDE 
e NEGRINI, 2016; RONSZCKA, 2019). 
Posteriormente, Martini (2018) adaptou a versão de geração de código namespaces 
referente à Tecnologia LingPON 1.2, no âmbito de suportar multithreading em computadores 
x86-64. De forma sucinta, foram feitas alterações nos Methods, particularmente na chamada de 
cada qual para executarem em threads. De modo a testar a eficiência de suas implementações, 
Martini criou um teste de benchmark que calcula repetidas vezes o algoritmo de validação de 
dados denominado CRC32 para um dado conjunto de bytes. Os cenários incluíram variações 
do número de execuções do algoritmo com resultados apresentado em escala em segundos. Essa 
versão permitiu verificar a viabilidade de paralelização em Methods, não explorando, no 
entanto, esse conceito com outras entidades (RONSZCKA, 2019; MARTINI et al., 2021). 
Em termos de arquitetura computacional, Pordeus (2017) realizou adaptações na 
Tecnologia LingPON 1.2 para gerar AssemblyPON, útil tanto à ArqPON ou NOCA 
(Notification Oriented Computer Architecture) quanto ao ArqPONSim ou NOCASim, 
respectivamente arquitetura computacional própria ao PON e seu simulador. De forma geral, a 
codificação em AssemblyPON para NOCA favoreceu a facilidade de programação, uma vez 
que já não exigiam mais, por parte do usuário, conhecimento especializado para a utilização de 
tais tecnologias (RONSZCKA, 2019). 
Os Quadros 10 e 11 apresentam, respectivamente, as propriedades elementares e os 
conceitos de programação do PON que foram contemplados pela Tecnologia LingPON 1.2. 
 
Quadro 10 -  Propriedades fundamentais do PON contempladas na Tecnologia LingPON 1.2 
                      Materialização 
 
   Propriedade 
 
Software 
Hardware 
Alvo (target) 
C++ estático 
Namespace 
Namespace Thread 
NOCA 
Ano 
2015 
2016 
2018 
2015 
Prog. Alto nível 
✓ 
✓ 
✓ 
✓ 
Desacoplamento/Paralelismo 
 
 
~ 
✓ 
Desacoplamento/Distribuição 
 
 
 
 
Não-Redundância/Desempenho 
✓ 
✓ 
✓ 
✓ 
Fonte: Adaptado de PORDEUS (2020) 
 
Quadro 11 - Conceitos de programação PON contemplados na Tecnologia LingPON 1.2 
                  Materialização 
 
 
Conceitos de programação 
 
Software 
Hardware 
Alvo (target) 
C++ estático 
Namespace 
Namespace Thread 
NOCA 
Ano 
2015 
2016 
2018 
2015 
Reatividade das entidades 
✓ 
✓ 
✓ 
✓ 


84 
 
 
Escalonamento de Rules 
 
 
 
 
Estratégias de resolução de conflito 
 
 
 
 
Compartilhamento de entidades 
 
 
 
 
Regras de formação 
✓ 
✓ 
✓ 
✓ 
Propriedades reativas dos Attributes 
✓ 
✓ 
✓ 
✓ 
 
 
 
 
 
Master Rule 
 
 
 
 
Entidades impertinentes 
✓ 
✓ 
✓ 
 
FBE Rules 
✓ 
✓ 
✓ 
 
FBE Agregator 
✓ 
✓ 
✓ 
 
Vetores 
 
 
 
 
Unique Premise 
 
 
 
 
Fonte: Adaptado de PORDEUS (2020) 
 
2.2.3.4 Tecnologia LingPON 2.0 
A criação de uma linguagem de programação própria para o PON representa um 
avanço significativo e mostra o quanto este paradigma é promissor. Os resultados apresentaram 
um avanço considerável em termos de facilidade de programação e desempenho, duas 
propriedades fundamentais do paradigma. No entanto, as versões do LingPON foram 
desenvolvidas, até então, de forma assaz despadronizadas, buscando atender apenas 
determinadas especificações mínimas em termos de padrões. Dessa forma, a integração de 
código entre uma versão para outra se torna mais trabalhosa, dificultando a evolução da 
linguagem.  
Neste âmbito, foi desenvolvida a versão atual e mais estável da linguagem, conhecida 
como NOPL ou LingPON 2.0, cujo objetivo é proporcionar uma linguagem mais universal, 
mais completa e mais efetiva para que possa ser base de qualquer sistema PON, 
independentemente da plataforma (RONSZCKA, 2019). Neste sentido, um programa 
implementado na LingPON 2.0 é composto a partir de um FBE Main, o qual seria o ponto 
inicial para a definição de outros FBEs e seus relacionamentos. Cada FBE apresenta seu próprio 
escopo interno, podendo ser formado por Attributes, Methods, Rules e até mesmo por instâncias 
de outros FBEs, sem limite de níveis/camadas. Isso possibilita a construção modular e também 
fractal de programas a nível de modelo (RONSZCKA, 2019). 
Até a versão anterior da LingPON, o modelo de estruturação é baseado apenas em um 
escopo global. Na LingPON 2.0, a organização da linguagem segue um modelo de programação 
baseado na organização holônica5 das entidades do PON, que são estruturadas por meio de 
                                                          
5 O termo programação holônica (derivada do neologismo holon) é utilizado no sentido de permitir a 
relação todo-parte entre instâncias de FBE em programas PON. Isto é, uma instância de FBE pode ser o “todo” 


85 
 
 
escopos locais. Na prática, o programa é organizado por meio da definição de FBEs, cada qual 
em um arquivo próprio e internamente por meio da composição de instâncias de FBEs, 
caracterizando uma relação holônica (todo-parte) entre elas e definindo a agregação de FBEs.  
Conforme já dito acima, a LingPON 2.0 corrobora com a organização holônica de 
entidades via o encapsulamento de FBEs. É possível encapsular instâncias de Attributes e 
instâncias de FBEs (agregadas), bem como definições de Methods particulares a cada FBE. 
Nesse ínterim, também é possível externar (ou tornar públicas) cada uma destas. A 
reorganização holônica, com possibilidade de externar apenas as entidades pertinentes, auxilia 
na garantia de coesão e desacoplamento dos elementos de um programa PON (RONSZCKA, 
2019). 
Outrossim, principalmente em aplicações mais complexas, há casos em que é 
necessário o uso de bibliotecas de terceiros. Essa melhoria também foi implementada na 
LingPON 2.0. Trata-se de um bloco novo para definições sem restrições que permite incluir 
bibliotecas padrão da linguagem C/C++, definições de namespaces e inclusões de classes de 
terceiros (RONSZCKA, 2019). O Código 10 apresenta um exemplo de implementação na 
linguagem NOPL, destacando essas novas características dessa versão. 
 
Código 10 - Exemplo de implementação na NOPL (projeto Sensors) 
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
//arquivo sensor.pon 
fbe Sensor 
    public boolean atState = false 
end_fbe 
 
//arquivo siren.pon 
fbe Siren 
    public integer atTime = 0 
end_fbe 
 
//arquivo alarm.pon 
fbe Alarm 
    public boolean atStatus = false 
end_fbe 
 
//arquivo sector.pon 
fbe Sector 
    private Boolean atIntruderDetected = false 
 
    private Alarm alarm 
     
    private Siren siren1 
    private Siren siren2 
 
    private Sensor sensor1 
    private Sensor sensor2 
                                                          
(holos, do grego) em seu escopo local, mas apenas “parte” (on, do grego, como em partícula próton, elétron e 
nêutron) dentro de um escopo de outra instância de FBE (SIMÃO, 2005; RONSZCKA, 2019). 


86 
 
 
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
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
48 
49 
50 
51 
52 
53 
54 
55 
56 
57 
58 
59 
60 
61 
62 
63 
64 
65 
66 
67 
68 
69 
70 
71 
72 
73 
74 
75 
76 
77 
78 
79 
80 
81 
82 
83 
84 
85 
86 
87 
 
    private method mtNotifyInvasion 
        attribution 
            this.atIntruderDetected = true 
        end_attribution 
    end_method 
     
    rule rlFireAlarm 
        condition 
            subcondition 
                premise prSectorIntruderDetected 
                    this.atIntruderDetected == false 
                end_premise 
                and 
                premise prAlarmOn 
                    alarm.atStatus == true 
                end_premise 
            end_subcondition 
            and 
            subcondition 
                premise prSensorA1State 
                    sensor1.atState == true 
                end_premise 
                or 
                premise prSensorA2State 
                    sensor2.atState == true 
                end_premise 
            end_subcondition 
        end_condition 
        action sequential 
            instigation parallel 
                call siren1.mtFire(10) 
                call siren2.mtFire(30) 
            end_instigation 
            instigation 
                call this.mtNotifyInvasion() 
            end_instigation 
        end_action 
    end_rule 
 
    properties 
        strategy PRIORITY 
    end_properties 
end_fbe 
 
//arquivo main.pon 
fbe Main 
    external NAMESPACES 
        #include "SMSSender.h" 
        #include <iostream> 
        using namespace std; 
    end_external 
 
    private Sector sectorA 
    private Sector sectorB 
 
    private method mtSendSms 
        params 
            String cellphone 
        end_params 
        code NAMESPACES 


87 
 
 
88 
89 
90 
91 
92 
93 
94 
95 
96 
97 
98 
99 
100 
101 
102 
103 
104 
105 
106 
107 
108 
109 
110 
111 
112 
113 
114 
115 
116 
117 
118 
119 
120 
121 
122 
            SMSSender *sender = new SMSSender(); 
            sender->send(cellphone); 
        end_code 
    end_method 
     
    rule rlInvasionDetection 
        condition 
            premise prSectorAInvaded 
                sectorA.atIntruderDetected == true 
            end_premise 
            or 
            premise prSectorBInvaded 
                sectorB.atIntruderDetected == true 
            end_premise 
        end_condition 
        action sequential 
            instigation sequential 
                call this.mtSendSms 
                    params 
                        "41-999999999" 
                        "41-987654321" 
                    end_params 
            end_instigation 
        end_action 
    end_rule 
 
    properties 
        strategy PRIORITY 
    end_properties 
 
 
    main 
        sectorA.atIntruderDetected = false 
 
  sectorB.atIntruderDetected = false 
    end_main 
end_fbe 
Fonte: Adaptado de RONSZCKA (2019) 
 
Como é possível observar no Código 10, são apresentadas as definições dos FBEs 
Sensor (linhas 2 a 4), Siren (linhas 7 a 9), Alarm (linhas 12 a 14), Sector (linhas 17 a 70) e Main 
(linhas 73 a 122). É importante ressaltar que cada uma dessas entidades é definida em arquivos 
distintos, cada qual representando seu próprio escopo local, caracterizando a organização 
holônica das entidades. Para configurar o encapsulamento de FBEs, cada entidade de FBE pode 
apresentar em sua definição dois tipos de objetos: (a) privados, os quais são visíveis apenas 
internamente ao escopo local, e (b) públicos, os quais são visíveis também externamente ao 
escopo local da FBE em questão. A linha 3 do Código 10 exemplifica a declaração de um 
Attribute como público (RONSZCKA, 2019).  
As entidades Instigation e Action da Rule rlFireAlarm (linha 34) apresentam um novo 
parâmetro, cuja função é indicar se a execução dos Methods será de forma sequencial ou 
paralela. Tal Action deverá ser executada (linha 56) de maneira sequencial, em que a Instigation 
da linha 57 precisa ser executada por completo para que, então, seja executada a Instigation da 


88 
 
 
linha 61. Ainda, é importante observar que a primeira Instigation apresenta execução de forma 
paralela, ou seja, seus dois Methods (linhas 58 e 59) podem ser executados paralelamente 
(RONSZCKA, 2019). 
A definição da FBE Main (linha 73) apresenta o bloco external (linhas 74 a 78), onde 
é feita a inclusão de bibliotecas de terceiros necessárias para a compilação e execução do 
Method mtSendSms (linhas 83 a 91) com o código especializado no target, que neste caso 
corresponde ao Namespaces. Essa possibilidade de integrar código de Method com a linguagem 
do target também é um avanço da LingPON 2.0 (RONSZCKA, 2019).  
Além do mais, uma evolução apresentada na LingPON 2.0, que permitiu uma maior 
flexibilidade na programação, é a possibilidade de a linguagem suportar a implementação de 
vetores. Todos esses avanços citados caracterizam uma expansão da linguagem que, 
consequentemente, exigem adaptações no Sistema de Compilação. A exemplo da possibilidade 
da LingPON 2.0 suportar a implementação de vetores, foi necessário expandir o sistema de 
compilação para que pudesse instanciar automaticamente cada entidade pertinente a fim de 
popular o grafo adequadamente (LAUTERT, 2018; RONSZCKA, 2019). 
Tais alterações no sistema de compilação foram implementadas seguindo as diretrizes 
do método MCPON em sua versão Efetiva, compondo uma nova versão denominada de Sistema 
de Compilação Efetivo, a qual está representada pela Figura 25. 
 
Figura 25 - Sistema de Compilação Eletivo para o PON 
 
Fonte: RONSZCKA (2019) 
 
De acordo com a Figura 25, o Sistema de Compilação Efetivo para o PON se apresenta 
de forma coesa e desacoplada, permitindo ao desenvolvedor trabalhar individualmente em cada 
uma das fases ou, pelo menos, em camadas distintas, de modo a aproveitar todo o restante que 
já está construído e validado (RONSZCKA, 2019).  


89 
 
 
Da mesma forma que ocorreu com as versões anteriores, para validar a Tecnologia 
LingPON 2.0 foram construídos, à luz do MCPON Efetivo, geradores de código específicos 
para plataformas distintas, buscando atingir as principais propriedades elementares do 
paradigma. Os targets definidos para a criação dos geradores de código são: (a) Framework 
PON C++ 1.0; (b) Framework PON C++ 2.0; (c) Framework PON C++ 3.0 adaptado 
(Multithread & PON IP); (d) Framework PON C++ 4.0; (e) Framework PON Java; (f) 
Framework PON C#; (g) Framework PON Erlang/Elixir; (h) Assembly NOCA; (i) PONHD 
(RONSZCKA, 2019; NEGRINI, 2019; SKORA, 2020; NEVES, 2021). Além dessas 
materializações, também há o JuNOC++ (Just a Notification Oriented C++), que se destaca por 
surgir como uma tentativa de Chierici (2020) de criar um framework do PON com base na 
fundamentação apresentada na dissertação de Banaszewski (2009) (NEVES, 2021). O Quadro 
12 traz uma síntese das propriedades elementares do PON contemplados pela Tecnologia 
LingPON 2.0.  
 
Quadro 12 - Propriedades fundamentais do PON contempladas na Tecnologia LingPON 2.0 
                Materialização 
 
 
 
   Propriedade 
 
Software 
Hardware 
Gerador 
de Cód. 
FW 
C++ 
FW 
C++ 
FW 
C++ 
FW 
C++ 
FW 
FW 
FW 
LingPO
N 2.0 
LingPON 
2.0 
Alvo 
(target) 
1.0 
2.0 
3.0 
4.0 
JAVA 
C# 
ERLANG 
NOCA 
PONHD 
Prog. Alto nível 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
Desacoplamento/Paralelismo 
 
 
✓ 
✓ 
 
✓ 
✓ 
✓ 
Desacoplamento/Distribuição 
 
 
✓ 
 
 
 
 
 
 
Não-Redundância/Desempenho 
 
~ 
 
~ 
~ 
 
 
✓ 
✓ 
 Contempla totalmente a propriedade 
~  Contempla parcialmente a propriedade 
Fonte: Adaptado de NEVES (2021) 
 
É possível observar, conforme o Quadro 12, que todos os targets atingiram 
efetivamente a primeira propriedade elementar do PON, i.e., programação declarativa em alto 
nível, justamente por ser basearem em uma linguagem de programação apropriada ao PON. O 
target para Framework PON Erlang/Elixir apresentou a viabilidade de paralelização das 
entidades do PON, as quais foram aplicadas sob uma plataforma orientada a atores e troca de 
mensagens. Por outro lado, nesse paralelismo em multinúcleo, não atingiu um tempo de 
processamento adequado em cada núcleo/processador, principalmente pelo custo 
computacional da estrutura de comunicação (NEGRINI, 2019; NEGRINI et al., 2019a; 
NEGRINI et al., 2019b).  
Em relação ao target Framework PON C++ 3.0 foi possível associar a facilidade de 
programação em alto nível com as já presentes características de paralelismo por meio de suas 


90 
 
 
implementações baseadas em threads, bem como também pela distribuição via PON IP. A 
principal contribuição deste target foi a possibilidade de configurar o programa de maneira 
específica sem a necessidade de alterações na linguagem principal. No entanto, este target não 
se apresenta de forma otimizada em termos de desempenho, justamente por se basear em uma 
implementação orientada por objetos dinâmicos e listas de ponteiros, na forma de framework 
ademais (RONSZCKA, 2019). 
O Quadro 13, por sua vez, apresenta a relação dos conceitos de programação PON 
contemplados pela Tecnologia LingPON 2.0. 
 
Quadro 13 - Conceitos de programação PON contemplados na Tecnologia LingPON 2.0 
       Materialização 
 
 
 
Conceitos de 
programação 
 
Software 
Hardware 
Gerador 
de Cód. 
FW 
C++ 
FW 
C++ 
FW 
C++ 
FW 
C++ 
FW 
FW 
FW 
NOCA 
PONHD 
Alvo 
(target) 
1.0 
2.0 
3.0 
4.0 
JAVA 
C# 
ERLANG 
VHDL 
VHDL 
Reatividade das entidades 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
Escalonamento de Rules 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
 
✓ 
 
Estratégias de resolução de 
conflito 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
 
✓ 
 
Compartilhamento de entidades 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
Regras de formação 
✓ 
✓ 
✓ 
 
✓ 
✓ 
✓ 
✓ 
✓ 
Propriedades reativas dos 
Attributes 
 
✓ 
✓ 
✓ 
 
 
 
 
 
Master Rule 
 
✓ 
✓ 
✓ 
 
 
 
 
 
Entidades impertinentes 
 
✓ 
✓ 
 
 
 
 
 
 
FBE Rules 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
FBE Agregator 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
Vetores 
✓ 
✓ 
✓ 
 
✓ 
✓ 
✓ 
✓ 
✓ 
Unique Premise 
 
 
 
 
 
 
 
 
 
Fonte: Adaptado de NEVES (2021) 
 
O Quadro 13 mostra que os targets Frameworks C++ PON 2.0 e 3.0, na Tecnologia 
LingPON 2.0, foram materializações que apresentava, quase todos os conceitos do PON (com 
exceção do conceito Unique Premise). É importante ressaltar que todos os demais targets 
também poderiam implementar os conceitos, bastando ‘apenas’ contemplar explicitamente os 
conceitos faltantes em suas construções. Naturalmente, isto exigiria algum tempo e alguma 
dedicação para se chegar a termo enfim (RONSZCKA, 2019). 
Isto dito, a Tecnologia LingPON 2.0 apresenta avanços consideráveis em relação à 
versão LingPON 1.X, organizando as entidades baseado nos sistemas holônicos e 
proporcionando a integração com códigos de outros programas, inclusive de outras linguagens 
ou paradigmas. Muitos dos conceitos na LingPON 2.0 são implícitos graças às evoluções no 


91 
 
 
MCPON e no Grafo PON Efetivos, como o caso de FBE Rules e FBE Agregador que são 
basicamente a organização holônica definida para esta nova linguagem, conforme apresentado 
anteriormente (RONSZCKA, 2019).  
 
2.3 
Detalhamento do Método MCPON 
Este presente trabalho tem interesse em evoluir a LingPON 2.0, bem como expandir o 
compilador para o target C++ Notificante Modular orientado a Namespaces. Assim sendo, para 
bem entender as contribuições desta presente pesquisa, é inevitavelmente necessário entender 
pormenores do MCPON. Neste sentido, serão apresentadas mais detalhadamente as etapas que 
compõem o método MCPON nesta presente seção. Em suma, essa seção traz a essência da tese 
de Ronszcka (2019), sendo apresentadas as etapas do MCPON na versão contemporânea do 
método em questão. 
Conforme descrito anteriormente, a Tecnologia LingPON 1.X constituiu-se à luz de 
uma versão preliminar do método MCPON. Tal tecnologia envolve uma linguagem de 
programação preliminar e um sistema de compilação compartilhado também preliminar, o qual 
permitiu a composição dos geradores de código distintos para plataformas distintas 
(PORDEUS, 2020a).  
 De fato, o MCPON preliminar foi aplicado como um conjunto de diretrizes e passos 
a serem seguidos para a construção de uma linguagem e um sistema de compilação associado. 
No entanto, a falta de um método bem definido e formalizado acarretou na geração de algumas 
implementações de dialetos da linguagem não tão padronizadas e desenvolvidas de forma a 
atender uma determinada especificação, conceito ou mesmo materialização. Ainda, nem todos 
os geradores de código contemplaram plenamente os chamados ‘conceitos de programação’ do 
PON (PORDEUS, 2020a), como apresentado de maneira mais detalhada na Seção 2.2.3. 
 Nesse âmbito, Ronszcka (2019) aprimorou as etapas do MCPON preliminar, 
melhorando o método para a criação efetivamente padronizada de materializações para o PON, 
denominado MCPON Efetivo, o que levou à Tecnologia LingPON 2.0 já introduzida na Seção 
2.2.3.4. Ainda assim, o conceito geral continua o mesmo, principalmente pela concepção e 
definição de linguagens de programação, bem como pela implementação de compiladores 
próprios para o PON, além da materialização em si no tocante a geradores de código. 
Particularmente, estes artefatos são orientados por um elemento balizador na forma de um grafo 


92 
 
 
diferenciado, denominado Grafo PON, agora melhorado no MCPON efetivo (PORDEUS, 
2020a). 
 O princípio do Grafo PON surgiu no MCPON preliminar e, tal qual o método, evoluiu 
ao longo do tempo, culminando na versão atual dada pelo MCPON efetivo. Em linhas gerais, o 
Grafo PON mapeia os elementos de um programa PON e o fluxo de execução baseado no 
mecanismo de inferência. O Grafo PON é composto, principalmente, por entidades e relações 
que compõe o modelo original do PON. Assim, o MCPON via Grafo PON busca a integração 
e compatibilidade entre as diferentes materializações construídas por ter uma representação 
comum intermediária entre eles apropriada ao PON (PORDEUS, 2020a). A Figura 26 
representa o modelo genérico de entidades, suas dependências e suas possíveis conexões. 
 
Figura 26 - Modelo Genérico do Grafo PON 
 
Fonte: RONSZCKA (2019) 
 
Basicamente, os elementos que compõem o Grafo PON são divididos em quatro 
grupos, cada qual representado por uma cor na Figura 26. O primeiro grupo é composto pela 
entidade NOPGraph, representada no diagrama pela cor verde. Essa entidade é o ponto central 
do mapeamento das entidades de um programa PON e possui uma relação direta com a classe 


93 
 
 
FBE e com a classe FBEInstance. Assim, um Grafo PON deve conter no mínimo uma definição 
e uma instância de FBE para ser considerado um programa PON (RONSZCKA, 2019).  
Um segundo grupo que compõe o Grafo PON é composto por entidades principais que 
compõem o modelo original do PON. Estas dizem respeito as entidades notificantes e estão 
representadas em amarelo no diagrama. Pela cor rosa, está representado o terceiro grupo que é 
o das entidades auxiliares que permitem, inclusive, interconexões entre as entidades principais. 
Na verdade, esse grupo também tem a função de complementar a estrutura do grafo com 
informações particulares de cada entidade que as agregam. Por fim, há o quarto grupo que é o 
das entidades complementares, representado na cor laranja, que representam as parametrizações 
no processo de compilação e são particulares as entidades de FBE (RONSZCKA, 2019). 
Cada instância do Grafo PON é uma representação completa de todas as entidades 
presentes do mecanismo de inferência por notificações do PON que compõem um programa 
dado em PON. Mais precisamente, cada instância é criada para representar as ligações entre os 
elementos de um programa em PON que permite alcançar as colaborações por notificação sendo 
estas a essência do mecanismo distribuído de inferência do PON. Assim, todo e qualquer 
programa desenvolvido para o PON pode ter sua representação mapeada em instâncias do Grafo 
PON sem perda semântica e de forma padronizada (RONSZCKA, 2019; PORDEUS, 2020a). 
 O Código 11 apresenta um programa PON em LingPON 2.0 a ser representado por 
meio do Grafo PON. Este programa consiste na simulação do acionamento e leitura de um 
conjunto de sensores. Cada sensor é representado por uma FBE Sensor que define os seguintes 
Attributes booleanos: isRead, que indica se o sensor já foi lido; e activated, indicando se o 
sensor está ativo ou inativo (PORDEUS, 2020a). 
 
Código 11 - Exemplo de programa a ser mapeado em uma instância do Grafo PON 
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
fbe Main 
    private Sensor sensor 
    private Counter counter 
    properties 
        strategy BREADTH 
    end_properties 
    main 
    end_main 
end_fbe 
fbe Counter 
    private Integer count = 0 
    private method incrementCounter 
        code NAMESPACES 
            this.count = this.count + 1; 
        end_code 
    end_method 
    private method restartCounter 
        assignment 
            this.count = 0 


94 
 
 
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
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
48 
49 
50 
51 
52 
53 
54 
55 
56 
57 
58 
59 
60 
        end_assignment 
    end_method 
    rule rl_counter 
        condition 
            premise pr_counter this.count <= LIMIT end_premise 
        end_condition 
        action 
            instigation  
                call this.restartCounter 
            end_instigation 
        end_action 
   end_rule 
end_fbe 
   
fbe Sensor 
    private boolean isRead = false 
    private boolean activated = false 
    private method readSensor 
        assignment 
            this.isRead = true 
        end_assignment 
    end_method 
    private method deactivateSensor 
        assignment 
 
this.activated = false 
        end_assignment 
    end_method 
    
    rule rl_sensor 
      condition 
         premise pr_is_read this.isRead != false end_premise and 
         premise pr_activated this.activated == true end_premise 
      end_condition 
      action 
         instigation parallel 
            call this.readSensor 
            call this.deactivateSensor 
            call counter.incrementCounter 
         end_instigation 
      end_action 
    end_rule 
end_fbe 
Fonte: PORDEUS (2020a) 
 
As Rules da aplicação consistem em alterar o Attribute isRead para true conforme as 
seguintes Conditions sejam atendidas: o sensor está ativo e ainda não foi lido. A Rule de 
exemplo pode ser instanciada para N sensores, apesar de o Código 11 apresentar a instanciação 
para apenas um sensor. Assim, a dinâmica de execução consiste em rodar M iterações, nas quais 
N sensores têm seus estados alterados para “ativo”. Caso o sensor ativo ainda não tenha sido 
lido, ou seja, isRead é igual a false, a Rule correspondente é ativada e o sensor é lido. O número 
de sensores ativos é alterado para cada experimento, alterando o número de Rules ativadas como 
consequência (PORDEUS, 2020a). 
Ademais, esta aplicação define outra entidade responsável por contar os sensores que 
já foram lidos na iteração atual. Essa entidade define um Attribute para armazenar o valor a ser 


95 
 
 
incrementado atomicamente a cada leitura do sensor. Quando o valor da contagem atinge o 
limite das Rules ativadas (ou seja, o total de sensores a serem lidos definido pela constante 
LIMIT), os Attributes são reinicializados e uma nova iteração é executada (PORDEUS, 2020a). 
O diagrama de objetos em UML apresentado na Figura 27 ilustra a construção de um 
grafo especializado de acordo com as diretrizes do Grafo PON a partir do programa apresentado 
no Código 7.  
 
Figura 27 - Exemplo de programa mapeado em uma instância do Grafo PON 
 
Fonte: PORDEUS (2020a) 
 
Na Figura 27, as entidades Sensor e Counter são representações de FBE (ilustradas 
pela cor amarela). Cada uma dessas entidades, possui suas respectivas instâncias neste dado 
programa (counter, sensor), que são ilustradas pela cor azul. Na prática, um programa PON 
pode ter dezenas, centenas ou até milhares de instâncias de FBE, as quais seriam todas 
representadas individualmente e pontualmente no Grafo PON (PORDEUS, 2020a). 


96 
 
 
Ainda, cada instância de FBE pode possuir um conjunto de entidades do tipo Attribute, 
bem como do tipo Method, representadas no diagrama pela cor laranja. Ademais, as entidades 
auxiliares que conectam os elementos notificantes, em especial, as chamadas de métodos (i.e., 
Call) e atribuições (i.e., Assignment e Factor) são representadas pela cor rosa. Em resumo, a 
construção do Grafo PON permite que um programa seja mapeado integralmente na forma de 
um grafo especializado, que por sua vez, serve como referência para método MCPON 
(RONSZCKA, 2019; PORDEUS, 2020a). 
 A elaboração do método MCPON Efetivo levou a concepção da Tecnologia LingPON 
2.0, que contemplou uma segunda versão da LingPON, um novo sistema de compilação 
fundado sobre o Grafo PON em versão madura. Por sua vez, o Grafo PON foi implementado 
como um framework em C++ de modo a permitir a criação e a população de sua instância 
(RONSZCKA, 2019). Com o advento do método MCPON, este permitiu que alguns conceitos 
fundamentais do PON se tornassem implícitos ao desenvolvedor com esta tecnologia, conforme 
mostrado na explicação da decorrente Tecnologia LingPON 2.0 (PORDEUS, 2020a). Isto 
posto, a seguir serão apresentadas finalmente as etapas que constituem o método MCPON. 
 
2.3.1 Etapas do MCPON 
A Figura 28 apresenta as etapas que constituem o método MCPON, que corresponde 
a um método de compilação próprio para o PON.  
 


97 
 
 
Figura 28 - Etapas e subetapas do MCPON 
 
Fonte: RONSZCKA (2019) 


98 
 
 
Conforme a Figura 28, o MCPON é constituído pelas cinco etapas: (1) Definição da 
linguagem; (2) Construção do Grafo PON; (3) Construção de Otimizadores; (4) Geração de 
código e (5) Validação do processo. Tais etapas se completam com o objetivo principal de 
permitir construir linguagens e compiladores para o PON em plataformas distintas. Além disso, 
é importante ressaltar que o desenvolvedor pode utilizar qualquer ferramenta, técnica ou 
linguagem de programação para a implementação do método MCPON, desde que o Grafo PON 
seja construído de acordo com as diretrizes definidas para sua composição (RONSZCKA, 
2019). Nas seções a seguir, serão apresentadas cada etapa que constitui o método MCPON. 
 
2.3.1.1  Definição da linguagem 
Em linhas gerais, a primeira etapa do MCPON consiste na definição de uma linguagem 
de programação especializada para o PON. Isto inclui toda a elaboração desta, como suas 
particularidades e características (e.g., gramática, estrutura sintática etc.). É nesta etapa que são 
definidas as palavras-chave utilizadas na definição dos elementos de um programa, bem como 
as regras gramaticais da linguagem para a respectiva construção dos analisadores léxico e 
sintático. Em tempo, a análise léxica consiste em verificar se todos os símbolos utilizados no 
código são válidos, enquanto a análise sintática é responsável por verificar se os símbolos estão 
encadeados de acordo com a especificação sintática da linguagem (RONSZCKA, 2019). 
Esta etapa foi construída em forma de um framework de compilação para o PON. Para 
isso, a análise léxica do compilador PON foi construída com base na ferramenta Flex/Lex, que 
tem como entrada um arquivo contendo tokens definidos e reconhecidos com a utilização de 
expressões regulares. Desta forma, esta ferramenta produz um módulo de software de 
escaneamento que pode ser compilado e acoplado a outros módulos, como o módulo de análise 
sintática. Já a análise sintática se dá através da ferramenta Bison, que consiste em um programa 
que, baseado em uma gramática livre de contexto, constrói um programa C/C++ que analisa 
um arquivo de entrada (código-fonte) de acordo com as regras gramaticais (FERREIRA, 2015; 
RONSZCKA, 2019). 
Particularmente, para a construção dessa etapa foi utilizada a Forma de Backus-Naur 
(abreviada como BNF, de Backus-Naur Form), que consiste na forma mais utilizada como 
notação para as gramáticas de linguagens de programação (RONSZCKA, 2019). Uma BNF é 
definida para representar uma gramática livre de contexto, ou seja, um modo formal para 
descrever linguagens formais (FERREIRA, 2015).  


99 
 
 
O resultado gerado ao fim desta primeira etapa é essencialmente um programa que 
realiza toda a análise léxica e sintática desta nova linguagem, cujo mapeamento subsequente é 
integralmente direcionado para a construção de grafos especializados com base nas diretrizes 
do Grafo PON, que constitui a etapa seguinte (RONSZCKA, 2019). 
 
2.3.1.2  Construção de instâncias do Grafo PON 
Uma vez que o início da construção das instâncias do Grafo PON são estabelecidas 
durante a fase de análises (léxica e sintática) da Etapa 1, esta se intersecciona diretamente com 
a segunda etapa. De forma sucinta, a segunda etapa consiste em instanciar os elementos do 
Grafo PON de modo a popular um grafo especializado, o qual representa integralmente o 
programa definido como entrada na primeira etapa. 
O Grafo PON é constituído, originalmente, por um conjunto de 27 entidades, as quais 
são supostamente projetadas para serem suficientes para mapear qualquer programa PON. 
Além disso, as instâncias de elementos específicos (como entidades do tipo FBE, ou até mesmo 
Rules internas à uma instância de FBE) são criadas em um processo interdependente e posterior 
ao das análises léxica e sintática.  
Nesse processo são identificados os elementos que possuem instâncias a serem criadas, 
os quais são instanciadas e relacionados com as demais entidades pertinentes. É importante 
ressaltar que a criação de um grafo especializado que define o estado e o fluxo de execução de 
um programa, precisa ser composto pontualmente pelas entidades mapeadas na análise de um 
código-fonte e instanciadas de acordo com as diretrizes do MCPON para a correta construção 
do grafo (RONSZCKA, 2019).  
Enquanto as entidades vão sendo “descobertas” no processo de análise e instanciadas, 
a conexão entre elas também é igualmente armazenada no grafo. Dessa forma, o grafo 
especializado é constituído com base na interconexão de todas as entidades instanciadas, 
representando assim um programa em PON integralmente (RONSZCKA, 2019). 
Nesta etapa, ainda, é feita a integração do algoritmo responsável pelas análises com a 
construção do Grafo PON. O Código 12 apresenta um exemplo sucinto da implementação de 
partes do método MCPON desenvolvida com base na linguagem de programação C++ e a 
ferramenta Bison (BISON, 2019; RONSZCKA, 2019). 
 
 


100 
 
 
Código 12 - Exemplo de integração para construção de instâncias do Grafo PON 
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
Fbe                  : FBE ID attributes methods {  
                             return graph->createFBE($2, $3, $4);  
                     }  
 
attributes           : ATTRIBUTES attributes_body END_ATTRIBUTES {  
                             return $2;  
                     }  
 
attributes_body      : attribute attributes_body  
                             | attribute attributesTmp->push($1);     
                               return attributesTmp;  
                     }  
 
attribute            : ID EQUAL VALUE {  
                             return graph->createAttribute($1, $3); 
                     } 
Fonte: RONSZCKA (2019) 
 
De acordo com o Código 12, é possível integrar o algoritmo responsável pelas análises 
com a criação de instâncias de grafos especializados. Na prática, isso poderia ser desenvolvido 
com base em um conjunto de métodos que encapsulam a instanciação das entidades do Grafo 
PON. A linha 2 do Código 12 está efetivamente criando uma instância de um FBE, com base 
nas informações extraídas das regras sintáticas. Ainda, o objeto graph representa a 
materialização do conceito do grafo em linguagem C++, servindo de interface tanto para a 
instanciação de entidades PON quanto para posterior armazenamento das mesmas em uma 
estrutura de dados (RONSZCKA, 2019). 
Como resultado final desta etapa, espera-se um programa que gera grafos 
especializados de acordo com as diretrizes do Grafo PON. O diagrama de objetos em UML 
ilustrado pela Figura 26 (Seção 2.3) corresponde a um exemplo de construção de um grafo 
especializado de acordo com as diretrizes do Grafo PON a partir de um programa apresentado 
no Código 11 (Seção 2.3). 
 
2.3.1.3  Construção de otimizadores 
A terceira etapa do MCPON possui o objetivo principal de auxiliar na construção de 
otimizadores para os grafos gerados, de modo a reduzir ou quiçá eliminar possíveis 
redundâncias presentes na estrutura de tais grafos, oriundos das etapas anteriores, assim como 
gerar otimizações específicas para os targets visados na Etapa 4 (i.e., geração de código). Para 
tanto, a Etapa 3 estabelece duas categorias de otimizadores. De um lado, do front-end, constitui-


101 
 
 
se os otimizadores genéricos, independentes de target. Do outro lado, do back-end, constitui-
se os otimizadores especializados, dependentes do target (RONSZCKA, 2019). 
Como exemplo de possível redundância gerada na etapa anterior, considera-se uma 
determinada expressão lógico-causal (e.g., a == 2), repetida ao longo do código-fonte de um 
programa PON. Para o PON, teoricamente, essas expressões seriam transformadas em uma 
única conexão entre o Attribute e a Premise em questão, compartilhando o estado dessa Premise 
com todas as Conditions pertinentes. Entretanto, a organização de um grafo durante as primeiras 
duas etapas do método não valida essa redundância e, portanto, duplicaria a entrada de tal 
Premise no grafo. A Figura 29 apresenta um exemplo de grafo especializado com um exemplo 
de redundância pontual (RONSZCKA, 2019). 
 
Figura 29 - Exemplo de redundâncias em um grafo especializado 
 
Fonte: RONSZCKA (2019) 
 
A Figura 29 ilustra o diagrama de objeto de parte de um programa PON em forma de 
grafo especializado, o qual apresenta um problema de redundância. De acordo com o diagrama, 
tanto a Instigation inAlarmIsFired1 quanto a Instigation inAlarmIsFired2 (e suas entidades 


102 
 
 
auxiliares Call) fazem chamadas ao Method mtRingSiren, sem nenhuma diferença em suas 
propriedades internas. Neste caso, uma regra de otimização eliminaria a existência de uma 
destas 
entidades, 
reconectando 
a 
entidade 
acAlarmIsFired2 
com 
a 
Instigation 
inAlarimIsFired1, mantendo a essência do programa intacta e mais enxuta (RONSZCKA, 
2019). 
Finalizada essa etapa, estaria disponível um grafo otimizado, bem como as devidas 
configurações definidas para a quarta etapa, responsável pela geração efetiva de código. Nesse 
âmbito, a próxima etapa do MCPON tem como entrada uma estrutura otimizada e preparada 
para a correta geração de código para o target escolhido (RONSZCKA, 2019). 
 
2.3.1.4  Geração de código 
A Etapa 4 consiste na construção efetiva de geradores de código, alinhado com a etapa 
anterior, na qual foram gerados grafos otimizados para esse fim. Basicamente, tais grafos 
servem de entrada para o processo de tradução e geração de código (RONSZCKA, 2019), 
conforme mencionado anteriormente. 
Esta etapa, particularmente, consiste na fase de síntese do processo de compilação. Em 
geral, para esta etapa são definidas as particularidades do target para o qual a compilação (i.e., 
tradução/transcrição) dos grafos será destinada. Para isso, primeiramente, o desenvolvedor 
precisará definir a plataforma e linguagem-alvo para a qual se destina o target. Com base nisso, 
ele deve explorar as características do PON como a paralelização e/ou a distribuição tanto 
quanto a plataforma/linguagem-alvo permitir. Ainda, uma vez definidas a plataforma e a 
linguagem-alvo, o desenvolvedor deverá construir um gerador de código apropriado para a 
tradução dos elementos das instâncias do Grafo PON em código-alvo na linguagem escolhida 
(RONSZCKA, 2019). 
Os Códigos 13 e 14 exemplificam, respectivamente, um algoritmo de iteração do Grafo 
PON em linguagem C++ e a escrita de um arquivo para a construção da entidade Premise no 
código-alvo. 
 
Código 13 - Exemplo de algoritmo para iteração do Grafo PON 
1 
2 
3 
4 
5 
6 
7 
void CodeGenerationExample::iterateOverRules(Instance *instance,  
                                             int level) {  
 
    map *rules = NOPGraph::getRules(instance);  
    for (map::iterator it=rules->begin(); it!=rules->end(); ++it) {  
 
        Rule *rule = it->second;  


103 
 
 
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
        Condition *condition = NOPGraph::getConditions(rule);  
 
        map*subconditions=NOPGraph::getSubconditions(condition);  
        for (map::iterator it=subconditions->begin();  
                           it!=subconditions->end(); ++it){ 
 
            Subcondition *subcondition = it->second; 
 
            map *premises = NOPGraph::getPremises(subcondition);  
            for (map::iterator it = premises->begin();  
                               it != premises->end(); ++it){  
 
                Premise *premise = it->second;  
                generateCodePremise(premise, level); 
 
            }  
 
        }  
        map *premises = NOPGraph::getPremises(condition);  
        for (map::iterator it = premises->begin();  
                           it != premises->end(); ++it){  
 
            Premise *premise = it->second;  
            generateCodePremise(premise, level);  
        }  
    }  
} 
Fonte: RONSZCKA (2019) 
 
O Código 13 apresenta a recuperação de um conjunto de Rules a partir do Grafo PON 
(linha 4). Com base neste, a iteração basicamente percorre tal conjunto de Rules (linha 5), 
recuperando as entidades relacionadas (linhas 16 e 26)  e direcionando as chamadas de métodos 
para funções específicas de geração de código (linhas 21 e 31). Na sequência, o Código 14 
exemplifica a escrita de um arquivo de código-alvo fazendo uso da biblioteca sstream, 
apresentado na linha 5. Cada detalhe de uma Premise, ao longo do percorrimento de suas 
características, poderia ser traduzido diretamente para o fluxo de saída, mapeado em um arquivo 
de código-alvo pertinente (RONSZCKA, 2019). 
 
Código 14 - Exemplo de geração de código para entidade Premise 
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
void CodeGenerationExample::generateCodePremise(Premise *premise,  
                                                int level){  
 
    level++;  
    sstream << getLevel(level) << "Premise* " << premise->getName()  
                                              << "(";  
    Expression *expression = NOPGraph:: getExpression(premise);  
    Factor *leftFactor = expression->getLeftFactor();  
 
    if (leftFactor->getFactorId() == Factor::ELEMENT_FACTOR) {  
 
        ElementFactor *element = (ElementFactor*)leftFactor;  
        sstream << element->getInstance()->getName();  
        sstream << "->"; sstream  


104 
 
 
15 
16 
17 
18 
19 
20 
21 
22 
23 
                << element->getAttribute()->getName();  
 
    } else {  
 
        sstream << leftFactor->getStringValue();  
 
    }  
. . .  
} 
Fonte: RONSZCKA (2019) 
 
Ao final desta etapa, obtém-se a tradução efetiva e completa de um grafo especializado 
em um conjunto de arquivos de código compilado para a plataforma-alvo definida igualmente 
nesta etapa. Com base em tais arquivos, o desenvolvedor poderia fazer a conexão destes com a 
ferramenta de compilação da plataforma-alvo, a qual se destina tal materialização 
(RONSZCKA, 2019). 
 
2.3.1.5  Validação do processo 
Após a etapa de geração de código, o processo de compilação já está completo. 
Entretanto, são fundamentais a verificação e a validação do processo como um todo. De maneira 
a manter a consistência e a qualidade dos compiladores gerados, o método MCPON apresenta 
esta etapa adicional, especificamente para a validação do processo (RONSZCKA, 2019).  
Esta última etapa, basicamente, contempla as validações dos targets gerados por meio 
de um conjunto de pequenos programas PON, em forma de grafos previamente criados (i.e., 
programas interpretados e mapeados em função do Grafo PON). Tais instâncias do Grafo PON 
possuem o intuito de validar as principais características do PON por meio de testes 
minimalistas e pontuais que visam medir a integralidade e abrangência de conceitos 
implementados no compilador (i.e., gerador de código) criado. Ainda, como complemento aos 
testes de validação, é recomendado a compilação de programas completos, os quais também 
podem estar mapeados na forma de instâncias de grafos completos (RONSZCKA, 2019). 
 


 
 
 
 
105 
 
 
 
 
2.3.2 Materializações do PON à luz do MCPON 
Com o objetivo de melhorar os resultados esperados do PON, bem como contemplar 
mais propriedades e conceitos de programação do paradigma, foi desenvolvido um conjunto de 
linguagens/compiladores próprios e prototipais ao PON, denominado Tecnologia LingPON 
1.X, à luz do MCPON e de uma versão simplificada do Grafo PON (principalmente com as 
classes em amarelo na Figura 15) (RONSZCKA, 2019). 
 Ainda em sua versão experimental, no tocante a software, a Tecnologia LingPON 1.X 
permitiu, dentre outros, o desenvolvimento em alto nível orientado a regras, bem como a 
geração de código específico em C procedimental e C++ notificante orientado a objetos, 
seguindo os conceitos do PON, com melhores tempos de resposta do que as materializações 
dos frameworks (RONSZCKA et al., 2017; RONSZCKA, 2019; PORDEUS, 2020a). 
Em hardware, por sua vez, a Tecnologia LingPON 1.X serviu como base para 
melhorias em relação a facilidade de desenvolvimento no tocante à ArqPON e no tocante ao 
PON-HD. Em Pordeus (2017), foram realizadas implementações na Tecnologia LingPON 1.X 
que permitiram a codificação em AssemblyPON para a ArqPON. Por sua vez, Kerschbaumer 
(2018) propôs uma solução prévia chamada PON – Hardware Digital (PON-HD) que gera 
código VHDL, o que conjuntamente constitui a Tecnologia LingPON-HD 1.0 (PORDEUS, 
2020a). 
Conforme já relatado, o método MCPON evoluiu e foi mais bem formalizado, assim 
como o seu Grafo PON, o que levou a composição da chamada Tecnologia LingPON 2.0. Esse 
MCPON dito efetivo, no tocante à Tecnologia LingPON 2.0, foi aplicado por um grupo de 
desenvolvedores, que ao adquirirem conhecimentos básicos sobre a construção de linguagens 
e compiladores, puderam aplicar etapas do método proposto em implementações de geradores 
de código para plataformas distintas. No entanto, esses geradores de código na Tecnologia 
LingPON 2.0 abordaram de forma efetiva apenas materializações em software, sendo que as 
materializações em hardware ocorreram apenas de maneira extremamente prototipal 
(PORDEUS, 2020a). 
O Quadro 14 apresenta a evolução da utilização do método MCPON nas principais 
materializações do PON. 


 
 
 
 
106 
 
 
 
 
Quadro 14 - Subetapas do método MCPON contempladas nos targets das Tecnologias LingPON 1.X e 2.0 
Fonte: PORDEUS (2020a) 
Versão 
 
Tecnologia LingPON Proto e 1.X 
Tecnologia LingPON 2.0 
                              Materialização 
 
 
 
   Subetapas 
 
Software 
Hardware 
Software 
Hardware 
Gerador 
de Cód. 
Proto Proto Proto 
1.2 
1.0 
1.2 
1.2 
1.2 
1.0 
2.0 
2.0 
2.0 
2.0 
2.0 
2.0 
2.0 
2.0 
Alvo 
(target) 
FW 
2.0 
C 
C++ 
C++ 
estático Fuzzy 
NameSpace 
NameSpace 
Thread 
NOCA PONHD 
1.0 
FW 
C++ 
1.0 
FW 
C++ 
2.0 
FW 
C++ 
3.0 
FW 
JAVA 
FW 
C# 
FW 
ERLANG NOCA PONHD 
Ano 
2013 
2013 
2013 
2015 
2016 
2016 
2018 
2015 
2018 
2018 
2013 2018 
2018 
2018 
2019 
2018 
2018 
Subetapa 1.1 
Definição das características da 
linguagem 
 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
Subetapa 1.2 
Definição das palavras-chave e 
analisador léxico 
 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
Subetapa 1.3 
Definição das regras gramaticais e 
analisador sintático 
 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
Subetapa 2.1 
Instanciar as entidades e popular 
instâncias do Grafo PON 
 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
Subetapa 2.2 
Construir a integração das análises 
com o Grafo PON 
 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
Subetapa 2.3 
Definição das regras semânticas e 
analisador semântico 
 
 
 
 
 
 
 
 
 
 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
Subetapa 3.1 
Criação de otimizadores genéricos 
independentes de target 
 
 
 
 
 
 
✓ 
✓ 
 
 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
Subetapa 3.2 
Criação de otimizadores especializados 
dependentes de target 
 
 
 
 
 
 
 
 
 
 
 
✓ 
✓ 
 
 
 
 
 
Subetapa 4.1 
Iterar instâncias do Grafo PON 
 
 
 
 
 
 
 
 
 
 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
 
 
Subetapa 4.2 
Construção de geradores de código 
 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
 
 
Subetapa 5.1 
Testes de integridade 
 
 
 
 
 
 
 
 
 
 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
 
 
Subetapa 5.2 
Compilação de programas completos 
 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
✓ 
 
 


107 
 
 
No Quadro 14 são consideradas as implementações relacionadas às Tecnologias 
LingPON Prototipal, LingPON 1.X e LingPON 2.0 para a construção de geradores de código 
alvo. Ainda, o Grafo PON permitiria identificar as respectivas interconexões de um Grafo PON 
e fracioná-lo por meio de sub grafos de forma a segmentar seus elementos em memórias 
distintas e até mesmo organizá-los para processar estes sub grafos de forma paralela/distribuída. 
Por fim, o Grafo PON permitiria também organizar as entidades que compõem o modelo PON 
de forma mais apropriada para cada materialização distinta (PORDEUS, 2020a).  
 
2.4 
Gerador de Código para C++ Notificante Modular Orientado a Namespaces 
Como apresentado anteriormente, para estudar e explorar a eficiência da Tecnologia 
LingPON, foram criados compiladores para a geração de códigos para diversas plataformas. 
Dentre eles, encontram-se as versões de gerador de código para C++ Notificante Modular 
orientado a Namespaces para single-threaded e multithreadead, ambas criadas visando ao 
desenvolvimento da Tecnologia LingPON 1.X. Esses dois geradores de código são essenciais 
para o desenvolvimento do presente trabalho e, portanto, serão descritos a seguir.  
 
2.4.1 Namespaces ou Espaço de Nomes 
Namespaces ou Espaço de Nomes é basicamente uma maneira de organizar itens 
(classes, enumerações, estruturas etc.) de uma forma lógica. O uso de namespaces pode ser 
bastante útil e positivo em se tratando de programação com orientação a objetos. Isto porque 
trata-se de funções, estruturas ou classes utilizadas de forma a organizar os códigos em grupos 
lógicos. À medida que um projeto se desenvolve e cresce, naturalmente aumenta o número de 
classes e estruturas. Dessa forma, aumenta também a necessidade de evitar a ambiguidade ao 
nomear esses elementos. (ATHAYDE e NEGRINI, 2016; RONSZCKA, 2019; OSHIRO et al., 
2021).  
É possível evitar esses conflitos de ambiguidade de uma maneira prática usando 
namespaces (ATHAYDE e NEGRINI, 2016; RONSZCKA, 2019; OSHIRO, 2020). A Figura 
30 ilustra um exemplo de caso em que pode gerar esse tipo de conflito.  
 
 


108 
 
 
Figura 30 - Exemplo de bibliotecas com mesmo nome da classe 
 
Fonte: ATHAYDE E NEGRINI (2016) 
 
Supondo que uma mesma aplicação faz referência a duas bibliotecas distintas 
libStrings e libGraphic, da Figura 30, sendo que cada uma contém uma classe com o mesmo 
nome “Texto”, porém usada para manipular tipos de elementos (enumerações, funções ou 
variáveis) diferentes. A classe “Texto” da biblioteca gráfica libGraphic corresponde a uma 
classe para manipulação de elementos gráficos, que representam uma caixa de texto. Por sua 
vez, a biblioteca libStrings possui uma classe “Texto” que nesse contexto manipula strings de 
grande tamanho. A probabilidade de gerar conflitos de ambiguidade é grande, caso a gestão do 
código não seja bem articulada. Neste sentido, é possível associar cada classe “Texto” a um 
namespace diferente para evitar tais conflitos (ATHAYDE e NEGRINI, 2016). 
 
2.4.2 LingPON e implementação em C++ Notificante Modular orientado a Namespaces 
Single-threaded 
Em 2016, Athayde e Negrini (2016) implementaram um assim chamado gerador de 
código C++ notificante modular orientado a namespaces para LingPON 1.0. Este gerador de 
código, posteriormente denominado de NPCPP 1.0, foi uma adaptação da chamada versão C++ 
estática da geração de código e foi criado com o objetivo de eliminar as dificuldades de 
integração da versão estática com outros códigos legados em C++, porém mantendo o baixo 
tempo de processamento desta. Como mencionado anteriormente, o PON obedece a lógica de 
notificações entre suas entidades. Dessa forma, para a geração de códigos em namespace, cada 
instância de certas entidades notificantes do PON (nomeadamente Subconditions, Premises, 
Methods e Attributes e FBEs ou Instances) foi transformada em um namespace específico a fim 


109 
 
 
de preservar a dinâmica de notificações (ATHAYDE e NEGRINI, 2016; RONSZCKA, 2019), 
conforme mostra a Figura 31.   
 
Figura 31 - Materialização da LingPON em Namespaces 
 
Fonte: Adaptado de Athayde e Negrini (2016) 
 
A Figura 31 apresenta o fluxo de notificações nos códigos gerados. Na geração de 
código em C++ notificante modular orientado a namespaces, em um mesmo arquivo 
(namespace), chamado “Instantiations”, foram agrupadas todas as Instances de um FBE 
(contendo seus respectivos Attributes e Rules), no arquivo (namespace) “Premises” se 
encontram todas as Premises dos FBEs, e, por fim, no arquivo (namespace) “SubConditions” 
foram agrupados todas as SubConditions a serem verificadas, sendo este namespace uma 
subdivisão organizacional de Condition de Rule, em suma (ATHAYDE e NEGRINI, 2016).  
Esta implementação corresponde justamente à quarta etapa do MCPON, na qual o 
desenvolvedor define a plataforma e linguagem-alvo para a qual se destina o target e 


110 
 
 
implementa um gerador de código apropriado para a tradução dos elementos das instâncias do 
Grafo PON de acordo com o target escolhido, sendo neste caso dado certamente o C++ 
notificante modular orientado a namespaces.  
Para tanto, foi criada uma classe chamada NPCompiler, implementada na linguagem 
C++, na qual são feitas a iteração inicial com o Grafo PON via sua materialização como um 
framework em C++ e a tradução dos elementos deste para o target C++ notificante modular 
orientado a namespaces. A Figura 32 mostra o diagrama de classes para essa implementação. 
 
Figura 32 - Estrutura do diagrama de classes do sistema de compilação do MCPON 
 
Fonte: Adaptado de RONSZCKA (2019) 
 
Conforme apresenta o diagrama de classes da Figura 32, a classe NOPGraph se 
apresenta como uma interface para criação de instâncias do Grafo PON, que além disso também 
armazena todas as entidades instanciadas no processo de análise. Tais entidades, por suas vezes, 
são derivadas da Classe Entity. A classe Compiler, basicamente, representa a estrutura do 
sistema de compilação como um todo, encapsulando todas as etapas do processo de compilação 
de um programa LingPON (RONSCKA, 2019). 
O Código 15 apresenta o método separateMaps() da classe Compiler, representando o 
processo inicial de iteração do Grafo PON.  
 
Código 15 - Método separateMaps() da classe Compiler 
1 
2 
3 
4 
5 
6 
void Compiler::separateMaps() { 
 
    for (std::map<std::string, Entity*>::iterator  
                  it = semanticAnalyser.entities.begin();  
                  it != semanticAnalyser.entities.end(); ++it)  
    { 


111 
 
 
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
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
48 
49 
50 
51 
52 
53 
54 
55 
56 
57 
58 
59 
60 
61 
62 
63 
64 
65 
        switch(((Entity*)(it->second))->type) { 
         
            case Entity::E_ATRIBUTE : { 
                mapAttributes[(it->second)->userEntityId]  
                               = (Attribute*)(it->second); 
            } break; 
 
            case Entity::E_RULE : { 
                mapRules[(it->second)->userEntityId]  
                          = (Rule*)(it->second); 
            } break; 
 
            case Entity::E_FBERULE : {             
                mapFbeRules[(it->second)->userEntityId]  
                             = (FbeRule*)(it->second); 
            } break;         
 
            case Entity::E_FORM_RULE : { 
                mapFormRules[(it->second)->userEntityId]  
                              = (FormRule*)(it->second); 
            } break; 
 
            case Entity::E_CONDITION :  
                mapConditions[(it->second)->userEntityId]  
                               = (Condition*)(it->second); 
            } break; 
 
            case Entity::E_ACTION : { 
                mapActions[(it->second)->userEntityId]  
                            = (Action*)(it->second); 
            } break; 
 
            case Entity::E_PREMISE : { 
                mapPremises[(it->second)->userEntityId]  
                             = (Premise*)(it->second); 
            } break; 
 
            case Entity::E_INSTIGATION : { 
                mapInstigations[(it->second)->userEntityId]  
                                 = (Instigation*)(it->second); 
            } break; 
 
            case Entity::E_SUBCONDITION : { 
                mapSubCondition[(it->second)->userEntityId]  
                                 = (SubCondition*)(it->second); 
            } break; 
 
            case Entity::E_FBE : { 
                mapFBEs[(it->second)->userEntityId]  
                         = (Fbe*)(it->second); 
            } break; 
 
            case Entity::E_INSTANTIATION : { 
                mapInstantiations[(it->second)->userEntityId]  
                                 = (Instantiation*)(it->second); 
            } break; 
        }     
    } 
} 
Fonte: Autoria própria 
 


112 
 
 
O Código 16, por sua vez, apresenta (linha 4) a chamada deste método pela classe 
NPCompiler para iniciar o processo como um todo.  
 
Código 16 - Chamada do método separateMaps() da classe Compiler na classe NPCompiler 
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
void NPCompiler::assemble() { 
 
  importExterns(); 
  Compiler::separateMaps(); 
  createAllRules(mapRules); 
  createAllPremises(mapPremises); 
  createAllInstigations (mapInstigations); 
  createAllInstantiations (mapInstantiations); 
 
  createHeader(); 
  createBody(); 
  createFooter(); 
  createFbes(); 
 
} 
Fonte: Autoria própria 
 
O Código 17 apresenta um trecho do processo de tradução de Rule para a linguagem-
alvo deste caso, C++ notificante orientado a namespaces. 
 
Código 17 - Trecho do processo de tradução de Rule para C++ notificante modular  
orientado a namespaces 
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
for (auto const &it : mapRules) { 
 
    std::list<Entity *> conditions = (it.second)->conditions;   
    std::list<Entity *> instigations = (it.second)->instigations; 
    int numPremises = 0; 
    std::string subConditionName = ""; 
 
    for (auto const &itCond : conditions) { 
        numPremises = ((SubCondition)(itCond))->premisses.size();  
        subConditionName   = ((SubCondition*)( 
                               itCond))->userEntityId; 
 
        fileH << "\tnamespace " << subConditionName <<"{"  
              << std::endl; 
        fileH << "\t\textern int count;" << std::endl; 
        fileH << "\t\textern void inc();" << std::endl; 
        fileH << "\t\textern void dec();" << std::endl; 
        fileH << "\t}" << std::endl; 
 
        fileCPP << "\tnamespace " << subConditionName <<"{"  
                << std::endl; 
        fileCPP << "\t\tint count = 0;" << std::endl; 
        fileCPP << "\t\tvoid inc(){" << std::endl; 
        fileCPP << "\t\t\tcount++;" << std::endl; 
        fileCPP << "\t\t\tif (count == "<<numPremises<<"){"  
                << std::endl; 
 
        //instigations 
        std::string methodName = ""; 
        std::string methodCall = ""; 


113 
 
 
31 
32 
33 
34 
35 
36 
37 
38 
39 
40 
      
        for (auto const &itInst : instigations) { 
 
            methodName = ((Instigation *)(itInst))->method; 
            methodName.replace(methodName.find("."),1,"::mt::"); 
 
            fileCPP << "\t\t\t\tinstantiation::" << methodName  
                    << "();" << std::endl; 
 
      } 
Fonte: ATHAYDE E NEGRINI (2016) 
 
De acordo com o Código 18, o código gerado substitui totalmente a utilização de 
classes e passa a ser baseado em namespaces, cada qual possuindo relevância global dentro de 
seu escopo. Para isso, a linha 1 apresenta o namespace Instantiation, o qual seria global para o 
programa todo. Ademais, nesse namespace em questão, são definidas todas as instâncias de 
FBEs do programa (linhas 2 e 17). A palavra extern é utilizada para declarar a existência dos 
elementos globais (i.e., variáveis e métodos) no cabeçalho do programa (arquivo.h), para que 
cada arquivo fonte (arquivo.cpp) conheça sobre a existência desses elementos globais e possam 
acessá-los normalmente. Entretanto, as definições concretas estão presentes em um arquivo 
fonte específico e único (RONSZCKA, 2019).  
 
Código 18 - Trecho de código gerado para instâncias de FBE na LingPON Namespace 
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
namespace instantiation {  
    namespace alarm1 {  
        namespace at {  
            namespace atOn {  
                extern bool value;  
                extern void setValue(bool newValue);  
            }  
            namespace atTimer {  
                extern int value;  
                extern void setValue(int newValue);  
            }  
        }  
        namespace mt {  
            extern bool mtRingTheBell();  
        }  
    }  
    namespace sensorPresence1 {  
        namespace at {  
            namespace atState {  
                extern bool value;  
                extern void setValue(bool newValue);  
            }  
. . . 
} 
Fonte: RONSZCKA (2019) 
 
Na sequência, o Código 19 apresenta um exemplo do trecho do arquivo de cabeçalho 
contendo as Premises do programa. Da mesma maneira que ocorre com as instâncias de FBEs, 


114 
 
 
as Premises também possuem um namespace de escopo global para o programa denominado 
de premise, na qual se encontram todas as Premises do programa (RONSZCKA, 2019).  
 
Código 19 - Trecho de código gerado para Premises na LingPON Namespace 
1 
2 
3 
4 
5 
6 
7 
8 
9 
namespace premise {  
    namespace prSensorPresence1 {  
        extern bool atState;  
        extern bool cpy1st, cpy2nd;  
        extern void init();  
        extern void notify_sensorPresence1_atState(bool newValue);  
        extern void compare();  
    }  
} 
Fonte: RONSZCKA (2019) 
 
Seguindo a mesma linha, o Código 20 mostra a definição do namespace para as 
SubConditions. É possível observar, na linha 7, como se dá o acesso global aos demais 
elementos do programa, os quais são acessíveis por meio dos namespaces globais (e.g. 
instantiation) (RONSZCKA, 2019). 
 
Código 20 - Trecho de código gerado para Subcondition na LingPON Namespace 
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
namespace subCondition {  
    namespace scIntruderIdentified {  
        int count;  
        void inc() {  
            count++;  
            if (count == 2) {  
                instantiation::alarm1::mt::mtRingTheBell();  
            }  
        }  
        void dec() {  
            count--;  
        }  
    }  
Fonte: RONSZCKA (2019) 
 
Em suma, uma das vantagens dessa versão é que, apesar de ser um código em C++, o 
código gerado não faz uso de classes. Em vez disso, os namespaces substituem, em partes, a 
essência estrutural das classes e, principalmente, aninham um namespace em outro, tornando o 
código mais organizado e principalmente reduzindo o número de classes e arquivos, além de 
evitar sobrecargas de execução de classes e objetos, como tabelas virtuais de polimorfismo 
(RONSZCKA, 2019; OSHIRO et al., 2021). Ainda, como mencionado anteriormente na Seção 
2.2.3.3, a versão de gerador de código contendo como linguagem-alvo o C++ Notificante 
Modular orientado a Namespaces, NPCPP 1.0, foi uma das materializações que obteve 
melhores resultados (em limítrofe com o compilador LingPON Static) considerando o 
desempenho e legibilidade, em termos de plataforma Von Neumann monocore.  


115 
 
 
Com esses dois aspectos, o NPCPP 1.0 representa uma materialização interessante no 
quesito de desempenho. No entanto, esse compilador apresenta alguns pontos negativos que 
devem ser considerados. Foram identificadas algumas inconsistências no funcionamento, 
apresentando erros de segmentação e erros em relação ao tamanho do nome de Attributes, além 
de limitações decorrentes da versão 1.X da Tecnologia LingPON, o que torna o seu uso difícil. 
Além disso, o NPCPP 1.0 foi testado apenas em uma aplicação, o Eletronicgate (portão 
eletrônico), considerada uma implementação de simples performance e, portanto, não sendo um 
exemplo muito apropriado em termos de benchmarks. Portanto, esta versão de compilador, 
apesar de se destacar dentre as materializações até então, ainda assim se trata de uma 
implementação prototipal. 
 
2.4.3 LingPON e implementação em C++ Notificante Modular orientado a Namespaces 
Multithreading 
Com o objetivo de testar a paralelização da LingPON, em termos de software, Martini 
(2018) adaptou a versão de geração de código NPCPP 1.0, apresentada no item anterior, para 
suportar multithreading em computadores x86-64. Para isso, foram utilizados dois padrões de 
multithreading: bibliotecas PThread e Thread Pool. 
Considerando uma aplicação PON com um escopo composto por inúmeras Rules, a 
maior parte do tempo de processamento poderia estar atrelada aos Methods. Por esse motivo, 
as threads foram implementadas para serem aplicadas a essa entidade do PON, muito embora 
o argumento de que a maior parte do tempo de processamento esteja relacionada aos Methods 
ainda seja debatível (MARTINI, 2018; MARTINI et al., 2021).  
A aplicação utilizada neste experimento foi o Eletronicgate. Conforme mencionado 
na seção anterior, esse programa é considerado primitivo e justamente para torná-lo de maior 
complexidade e apropriado para testar a eficiência das implementações, Martini adicionou ao 
Eletronicgate uma implementação que calcula repetidas vezes o algoritmo de validação de 
dados denominado CRC32 para um dado conjunto de bytes, sobrecarregando o processador (ou 
núcleo), levando a migração de threads para outros núcleos. Os cenários incluíram variações 
do número de execuções do algoritmo com resultados apresentado em escala de segundos 
(MARTINI, 2018; RONSZCKA, 2019; MARTINI et al., 2021).  


116 
 
 
As Figuras 33 e 34 mostram as principais alterações no código gerado (NPCPP 1.0), 
após a implementação de multithreading utilizando, respectivamente, as bibliotecas PThread e 
Thread Pool. 
 
Figura 33 - Principais alterações no código gerado utilizando PThreads 
 
Fonte: MARTINI (2018) 
 
Figura 34 - Principais alterações no código gerado utilizando Thread Pooling 
 
Fonte: MARTINI (2018) 
 
A Figura 35 apresenta o gráfico com o resultado das implementações multithreading, 
bem como compara com o resultado da versão monoprocessada. 
 
 
 
 
 
 
 
 


117 
 
 
 
Figura 35 - Comparação entre as versões Namespace mono e multithreading 
 
Fonte: MARTINI (2018) 
 
Conforme o resultado mostrado pelo Figura 35, é possível concluir que as duas versões 
multiprocessadas, apresentaram um desempenho nitidamente melhor do que a versão single-
threaded do gerador de código. Ainda, dentre as versões multithreading, a técnica Thread 
Pooling apresenta um resultado mais eficaz. Isto porque utiliza um pool de threads em tempo 
de execução, enquanto para a técnica PThreads existe todo um overhead de criação e 
manutenção das threads utilizadas durante a execução do programa (RONSZCKA, 2019). 
Por fim, Martini concluiu que as técnicas de multithreading podem fornecer resultados 
melhores de desempenho, no entanto a falta de implementação de mecanismos de controle que 
garantam principalmente o determinismo dificultam o uso destas técnicas em aplicações mais 
complexas (MARTINI, 2018; RONSZCKA, 2019; MARTINI et al., 2021). 
Essa materialização explorou apenas a implementação de multithreads em Methods. 
Porém a viabilidade de paralelização nessa entidade, sugere a possibilidade de testar a 
implementação de multithreads nas demais entidades, como Rules e Premises, paralelizando o 
sistema de notificações como um todo.  
 


118 
 
 
2.5 
Considerações sobre o Capítulo 
Para alcançar de forma efetiva o objetivo de materializar o PON, foi necessário criar 
um novo método de compilação, uma vez que os métodos nos quais se baseiam as teorias 
tradicionais de compilação não são devidamente adequados para a criação de compiladores 
próprios para o PON. Esse novo método, conhecido como MCPON, apresenta um mapeamento 
de entidades e seus relacionamentos via uma estrutura única de dados em forma de grafos, 
denominada Grafo PON. Essa contribuição, proposta, modelada, implementada e 
testada/validada por Ronszcka (2019), representa um avanço notório para o paradigma. 
No âmbito do MCPON, um ponto fundamental para o avanço do paradigma foi a 
criação de linguagens próprias. A LingPON evoluiu desde sua versão prototipal, passando pela 
LingPON 1.X, até alcançar a versão efetiva LingPON 2.0 ou NOPL, que consiste em uma 
linguagem padronizada e universal para a construção de programas PON, proporcionando uma 
programação em alto nível. Ademais, em cada Tecnologia LingPON com sua versão do Grafo 
PON, os programas são mapeados para representações comuns de forma de instância do grafo, 
permitindo a criação de geradores de código para plataformas distintas.    
Neste contexto, o presente capítulo descreveu também as implementações de versões 
single-threaded e multithreading de geração de códigos para C++ Notificante Modular 
orientado a Namespaces, também conhecido como NPCPP. Entretanto, esses geradores de 
código foram implementados para a Tecnologia LingPON 1.X, não sendo essa a versão mais 
completa da linguagem. Na versão multithreading do compilador, foi explorada a viabilidade 
de paralelização apenas em Methods, utilizando uma versão alterada da aplicação 
Eletronicgate, tornando-a mais complexa e adequada para os experimentos. Ainda no âmbito 
de paralelismo, Negrini (2019) constatou, utilizando o target Framework PON Erlang/Elixir, 
que apesar da viabilidade de paralelização das entidades do PON, a performance da capacidade 
de processamento ainda se apresenta desbalanceada em cada núcleo. 
Apesar de a versão monoprocessada do NPCPP 1.0 ter sido uma das que apresentou 
melhor resultado de desempenho em termos de arquitetura Von Neumann monocore 
(concorrendo com a versão C++ Static), este compilador representa uma materialização ainda 
muito prototipal, uma vez que apresenta inconsistências em seu funcionamento e limitações 
advindas já da própria Tecnologia LingPON 1.0, dificultando a realização de experimentos. Em 
decorrência disso, há apenas um experimento realizado com o NPCPP 1.0, sendo utilizada uma 


119 
 
 
aplicação de baixa complexidade (Eletronicgate), considerada, portanto, um exemplo de 
benchmark não muito apropriado. 
Neste sentido, refletiu-se que seria importante a construção de um compilador para 
C++ Notificante Modular orientado a Namespaces, utilizando a Tecnologia LingPON 2.0, uma 
vez que esta é a versão mais atual e estável da tecnologia.  Ainda, um compilador para o target 
em questão que, além de suportar a versão 2.0 da LingPON, contemplasse os conceitos de 
programação, como Premissa Única e Entidades Impertinentes, deve apresentar uma 
performance ainda melhor, já que a aplicação de tais conceitos elimina notificações 
desnecessárias, conforme apresentado anteriormente. Isto permitiria ainda experimentos com 
aplicações mais efetivas, dado que para os testes até então foram utilizadas aplicações não muito 
complexas. 
Isto posto, a presente pesquisa visa ao desenvolvimento de uma materialização, que 
viabiliza uma programação em alto nível e desempenho apropriado, e a eventuais ajustes na 
versão atual da Tecnologia LingPON, identificados durante o desenvolvimento deste trabalho. 
Tal materialização corresponde ao primeiro compilador para a LingPON 2.0, visto que as 
demais implementações para esta versão da Tecnologia LingPON se encontram no âmbito de 
frameworks. 
Conforme apresentado anteriormente, na versão multithreading do NPCPP 1.0, foi 
iniciada a exploração de paralelização em Methods. A aplicação da mesma metodologia no 
NPCPP 2.0 permite a possibilidade de viabilidade de paralelização do PON. No entanto, a 
presente pesquisa não chega a trabalhar com execução em diversos núcleos, como foi realizado 
na materialização Framework PON Erlang/Elixir. 
Por fim, os experimentos e testes do NPCPP 2.0 com diferentes benchmarks (desde 
um mais simples até um com mais complexidade), oriundos tanto do grupo de pesquisa já 
conhecido do PON, como da literatura computacional, permitem uma validação mais efetiva 
desta materialização. O desenvolvimento do NPCPP 2.0, à luz da Tecnologia LingPON 2.0, 
tornaria essa tecnologia um tanto ainda mais completa, podendo instigar o surgimento de novas 
materializações efetivas para o PON. 


120 
 
 
3 O COMPILADOR NPCPP 2.0 
Este capítulo tem o objetivo de apresentar o desenvolvimento do compilador NPCPP 
2.0, enquanto artefato visado nesta dissertação de mestrado, no âmbito da Tecnologia LingPON 
2.0. Tal desenvolvimento compreende a etapa de geração de código do supra explicado método 
MCPON. Neste caso, o target é para C++ Notificante Modular orientado a Namespaces 
(NPCPP 2.0). Naturalmente, utiliza-se a LingPON em versão 2.0 e, ademais, a expande em 
termos de conceitos do PON (em termos de completude linguística, por assim dizer), sempre 
no contexto da Tecnologia LingPON 2.0 e à luz do MCPON. Por fim, este capítulo também 
apresenta validações feitas com projetos em PON no tocante aos avanços propostos, usando 
bechmarks oriundos do grupo de pesquisa e também externos.  
Mais precisamente, o capítulo primeiramente apresenta a construção do gerador de 
código para C++ Notificante Modular orientado a Namespaces construído para a versão 2.0 da 
LingPON. Este compilador, conforme já explicitado, foi denominado de NPCPP 2.0 e foi 
construído, em um primeiro momento, para executar em um ambiente single-threaded. Ainda, 
foi utilizada uma aplicação usual do grupo de pesquisa do PON, a qual consiste em uma 
simulação simplificada de Rede de Sensores para fins de testes na etapa de sua construção. 
Concomitantemente, o uso do compilador NPCPP 2.0 por alguns membros do grupo de 
pesquisa do PON incitou seu refino contínuo sob uma metodologia de desenvolvimento em 
espiral. 
Na sequência, o capítulo apresenta experimentos e resultados de benchmarks 
realizados. Naturalmente, há um conjunto de resultados com a própria aplicação de Rede de 
Sensores acima mencionada. Além disto, mais especificamente, apresentam-se os resultados 
advindos dos experimentos com a aplicação mais complexa e chamada de Simulador de 
Controle de Tráfego Automatizado (CTA), a qual é oriunda do próprio grupo de pesquisa do 
PON. Por fim, bem se apresentam os resultados de uma aplicação com o algoritmo de ordenação 
Bitonic Sort, este oriundo da literatura da ciência da computação. 
Subsequentemente, são ainda apresentadas também algumas alterações desse 
compilador NPCPP 2.0 na Tecnologia LingPON 2.0 visando explorar a viabilidade de 
paralelização, tal como foi experimentado na versão do NPCPP 1.0 multithreading para a 
Tecnologia LingPON 1.2, implementada por Martini (2018). Em seguida e relacionadamente, 
são apresentadas comparativamente as melhorias realizadas na versão 2.0 do NPCPP, em 
relação à sua versão 1.0 do NCPP. 


121 
 
 
 
3.1 
Gerador de Código C++ Notificante Modular Orientado a Namespaces para 
LingPON 2.0 (NPCPP 2.0) 
Como apresentado anteriormente, a primeira versão de um compilador C++ Notificante 
Modular orientado a Namespaces foi implementado por Athayde e Negrini (2016), para a qual 
foi utilizada a LingPON 1.2. Pelo fato de essa versão ter apresentado bons resultados no quesito 
de desempenho e legibilidade em Tecnologia LingPON 1.X, esse presente trabalho propõe o 
desenvolvimento de uma versão desse compilador para a versão 2.0 da LingPON, denominando-
o de NPCPP 2.0, de forma tal que também se possa, inclusive, proporcionar contribuições de 
desempenho em Tecnologia LingPON 2.0.  
 
Código 21 - Exemplo de implementação em LingPON 2.0 para a aplicação Redes de Sensores 
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
fbe Sector 
    private Boolean atIntruderDetected = false 
    private Alarm alarmA 
    private Sensor sensorA1 
    private Sensor sensorA2 
 
    private method mtNotifyInvasion 
        attribution 
            this.atIntruderDetected = true 
        end_attribution 
    end_method     
 
    rule rlFireAlarmA 
        condition 
                premise prSectorInPeaceA 
                    this.atIntruderDetected == false 
                end_premise 
                and 
                premise prAlarmAOn 
                    alarmA.atStatus == true 
                end_premise 
                and 
                premise prSensorA1State 
                    sensorA1.atState == true 
                end_premise 
        end_condition 
        action 
            instigation 
                call this.mtNotifyInvasion() 
            end_instigation 
        end_action 
    end_rule 
end_fbe 
Fonte: Autoria própria 
 


122 
 
 
Em tempo, o desenvolvimento do NPCPP 2.0 exige todo um engenho particular dado 
que a Tecnologia LingPON 2.0 apresenta um sistema de construção de compiladores distinta da 
precedente Tecnologia LingPON 1.X, particularmente no tocante a toda uma evolução do Grafo 
PON expressa em seu framework, cf. explicado na Seção 2.2. Neste sentido, o Código 21 
apresenta um exemplo de código em LingPON 2.0 de uma aplicação conhecida como Redes de 
Sensores, enquanto a Figura 36 apresenta a representação da respectiva instância de Grafo PON 
2.0. Tanto no código quanto no grafo há peculiares da Tecnologia LingPON 2.0, as quais serão 
discutidas nas próximas subseções.  
 
Figura 36 - Representação de instância do Grafo PON 2.0 para a aplicação de Redes de Sensores 
 
Fonte: Autoria própria 
 
3.1.1 Navegação no Grafo PON e Gerador de Código NPCPP 2.0 
Como detalhado no capítulo anterior, a implementação do compilador, enquanto 
gerador de código, compreende a Etapa 4 do MCPON, na qual é realizada a iteração inicial com 
o Grafo PON via seu framework para, então, ser feita a tradução das entidades PON para o target 
definido. Para tal iteração, o Grafo PON, o qual se materializa em um framework C++ em 
Tecnologia LingPON 2.0, apresenta uma classe principal chamada Compiler, a partir da qual se 
derivam, por meio do conceito de herança, as classes que compõem os geradores de códigos 
específicos. O arquivo .h da classe Compiler está representado pelo Código 22. 
 


123 
 
 
Código 22 - Arquivo .h da classe Compiler 
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
#ifndef _COMPILER_H_ 
#define _COMPILER_H_ 
 
class NOPGraph; 
 
#include <string> 
 
class Compiler { 
 
    public: 
 
        Compiler(); 
        virtual ~Compiler(); 
 
        virtual void generateCode() = 0; 
 
        std::string getLevel(int level); 
 
        NOPGraph *graph; 
 
}; 
 
#endif 
Fonte: RONSZCKA (2019) 
 
O Código 23, por sua vez, apresenta o arquivo .h da classe NamespacesCompiler do 
NPCPP 2.0. Ainda no Código 23, a linha 19 ilustra o relacionamento de herança desta em relação 
à classe Compiler e o método generateCode(), apresentado na linha 27, é reimplementado do 
método virtual da classe base (linha 15 do Código 22). 
 
Código 23 - Classe NamespacesCompiler.h do NPCPP 2.0 
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
#ifndef _NAMESPACES_COMPILER_H_ 
#define _NAMESPACES_COMPILER_H_ 
 
class Instance; 
class Premise; 
class Attribute; 
class Condition; 
class Rule; 
 
#include "Compiler.h" 
 
#include <string> 
#include <iostream> 
#include <fstream> 
#include <list> 
 
using namespace std; 
 
class NamespacesCompiler : public Compiler { 
 
public: 
 
 
std::list<std::string> init_premises; 
 
std::string getInstanceCompleteName(Instance* instance); 


124 
 
 
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
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
48 
49 
50 
51 
52 
 
std::string getIncludeBlock(); 
 
 
void generateCode(); 
 
void generateCodeInstance (Instance *mainInstance); 
 
void generateAllPremises   (Instance *mainInstance); 
 
void generateAllAttributes  (Instance *mainInstance); 
 
void generateAllMethods    (Instance *mainInstance); 
 
void generateAllRules         (Instance *mainInstance); 
 
void generateBody(); 
 
 
void generateCodeAttribute(ofstream& fileH, ofstream& fileCPP,  
                                 Instance *instance, int level); 
 
void generateCodeMethod   (ofstream& fileH, ofstream& fileCPP,  
                                 Instance *instance, int level); 
 
void generateCodeRule     (ofstream& fileH, ofstream& fileCPP,  
                                 Instance *instance, int level); 
 
void generateCodePremise  (ofstream& fileH, ofstream& fileCPP,  
                                 Instance *instance, int level); 
 
void generatePremise      (ofstream& fileCPP, ofstream& fileH,  
                                 Premise *premise, std::string instName,  
                                 std::string ruleName, int subConds,  
                                 int level); 
 
void generateInstigation  (ofstream& fileCPP, ofstream& fileH,  
                                 Instance *instance, Rule *rule, int level); 
 
 
 
void assemble(); 
}; 
#endif 
/* NAMESPACES_2_0_COMPILER_H */ 
Fonte: Autoria própria 
 
Conforme a implementação de novas alterações da versão 2.0 da LingPON, foi 
necessário adaptar o Grafo PON no âmbito da Tecnologia LingPON 2.0 e da versão efetiva do 
MCPON. Dessa forma, na construção do NPCPP 2.0, a iteração inicial com o grafo foi 
implementada de maneira diferente, se comparado com o do NPCPP 1.0 da Tecnologia 
LingPON 1.2. No caso deste último, eram realizadas chamadas a métodos pontuais, os quais 
manipulavam a construção do Grafo PON, armazenando os dados extraídos nas entidades 
pertinentes (RONSZCKA, 2019), cf. Código 15 da Seção 2.4.2. Já para a construção do NPCPP 
2.0, a interação é feita por intermédio da instância classe NOPGraph, a qual se apresenta como 
uma interface para criação de instâncias do Grafo PON, que além disso também armazena todas 
as entidades instanciadas no processo de análise. Para ilustrar melhor esta questão, o Código 24 
apresenta o processo inicial da iteração com a materialização do Grafo PON, por meio da 
instância da classe NOPGraph (representada por graph, na linha 5), para a LingPON 2.0 na 
construção do gerador de código em questão.  
 
Código 24 - Processo inicial de iteração com o Grafo PON na construção do NPCPP 2.0 
1 
2 
3 
4 
void NamespacesCompiler::generateCode(){ 
 
     // A partir da instância do Grafo PON,  
     // gera os arquivos (namespaces) das entidades PON 


125 
 
 
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
    generateCodeInstance(graph->getFbeMainInstance());   
    // Geração do arquivo main.cpp   
    generateBody(); 
 
} 
 
void NamespacesCompiler::generateCodeInstance(Instance 
*mainInstance){ 
 
    // Método que recupera todas as instâncias de Attributes  
    // e de FBEs e gera o namespace ‘instances’  
    generateAllAttributes(mainInstance);     
    // Método que recupera todas instâncias de Methods  
    // e gera o namespace ‘methods’ 
    generateAllMethods(mainInstance);     
    // Método que recupera todas instâncias de Rules  
    // e gera o namespace ‘rules’ 
    generateAllRules(mainInstance);     
    // Método que recupera todas instâncias de Premises  
    // e gera o namespace ‘premises’ 
    generateAllPremises(mainInstance); 
 
} 
Fonte: Autoria própria 
 
O Código 25, por sua vez, apresenta o processo de tradução de Attributes para o target 
NPCPP 2.0 (C++ Notificante Modular orientado a Namespaces). Este código faz parte do 
método generateCodeAttribute() da classe NamespacesCompiler (cujo código completo é 
apresentado no Apêndice A) e exemplifica como é realizado o percorrimento da instância do 
Grafo PON e geração de código a partir dela. Em linhas gerais, o método 
generateCodeAttribute() recebe como parâmetro a instância do FBE Main da instância do Grafo 
PON. A partir disso, é possível recuperar as instâncias de todos os Attributes do programa PON, 
conforme mostra a linha 7, e para cada instância de Attribute, é possível recuperar as instâncias 
de todas as Premises interessadas, como mostra a linha 55 do Código 25. 
 
Código 25 - Processo de tradução de Attributes para Namespaces 
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
void NamespacesCompiler:: generateCodeAttribute(ofstream& fileH,  
                                  ofstream& fileCPP,  
                                  Instance *instance, int level) 
{ 
// ...  
    
map< string, Attribute*> *attributes = instance->getAttributes(); 
     
for ( map< string, Attribute*>::iterator it = attributes->begin();  
                              it != attributes->end(); ++it )    
{ 
    // retorna o nível de identação no código gerado 
    string tab = getLevel(level);   
 
    Attribute *attribute = it->second; 
 


126 
 
 
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
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
48 
49 
50 
51 
52 
53 
54 
55 
56 
57 
58 
59 
60 
61 
62 
63 
64 
65 
66 
67 
68 
69 
71 
72 
73 
74 
75 
76 
77 
78 
    fileH << tab << "\t\t namespace at {" << endl; 
    fileH << tab << "\t\t\t namespace "   << attribute->getName()  
                 << " {"                  << std::endl; 
    fileH << tab << "\t\t\t\t extern "  
                 << returnType( attribute->getType()->getTypeId() )  
                 << " value;"             << std::endl; 
    fileH << tab << "\t\t\t\t extern void setValue(" 
                 << returnType(attribute->getType()->getTypeId() )  
                 << " newValue);"         << std::endl; 
    fileH << tab << "\t\t\t }"            << std::endl; 
    fileH << tab << "\t\t }"              << std::endl; 
 
    fileCPP << tab << "\t\t namespace at {" << std::endl; 
    fileCPP << tab << "\t\t\t namespace "   << attribute->getName()  
                   << " {" << std::endl; 
 
    fileCPP << tab << "\t\t\t\t"  
                   << returnType( attribute->getType()->getTypeId() ) 
                   << " value = "  
                   << attribute->getFactor()->getStringValue()  
                   << ";" << std::endl; 
    fileCPP << tab << "\t\t\t\t void setValue( " 
                   << returnType( attribute->getType()->getTypeId() ) 
                   << " newValue) {" << endl; 
         
    fileCPP << tab << "\t\t\t\t\t if (value != newValue) {" << endl; 
    fileCPP << tab << "\t\t\t\t\t\t value = newValue;"      << endl; 
 
    map<std::string, Premise*> *premises = attribute->getPremises(); 
    for ( map<std::string, Premise*>::iterator it = premises->begin(); 
                           it != premises->end(); ++it )  
    { 
        Premise *premise   = it->second; 
             
        string cmpInstName = getInstanceCompleteName(  
                                premise->getParentInstance() ); 
        string cmp1st_att  = ""; 
 
        Expression *expression = premise->getExpression(); 
        Factor     *leftFactor = expression->getLeftFactor(); 
 
        if ( leftFactor->getFactorId() == Factor::ELEMENT_FACTOR ) { 
 
            ElementFactor *element = (ElementFactor*) leftFactor; 
            cmp1st_att = element->getInstance()->getName(); 
            cmp1st_att = cmp1st_att + "_"; 
            cmp1st_att = cmp1st_att +  
                         element->getAttribute()->getName(); 
 
            fileCPP << tab << "\t\t\t\t\t\tpremise::" 
                           << cmpInstName        << "::"  
                           << premise->getName() 
                           << "::notify_"        << cmp1st_att  
                           << "(newValue);"      << std::endl; 
 
        } 
    } 
 
    fileCPP << tab << "\t\t\t\t\t }" << std::endl; 
    fileCPP << tab << "\t\t\t\t }"   << std::endl; 
    fileCPP << tab << "\t\t\t }"     << std::endl; 


127 
 
 
79 
80 
81 
82 
83 
84 
85 
86 
87 
88 
89 
90 
91 
92 
93 
94 
95 
96 
97 
98 
99 
100 
101 
102 
103 
    fileCPP << tab << "\t\t }"       << std::endl; 
    
} 
level++; 
 
map<std::string, Instance*> *otherInsts = instance->getInstances(); 
if ( otherInsts->size() > 0 ) { 
    for ( map<std::string, Instance*>::iterator  
              it = otherInsts->begin(); it != otherInsts->end(); ++it) 
    {    
         
        Instance *otherInst = it->second;       
        if ( otherInst->getName() != "this" ) { 
 
            generateCodeAttribute (fileCPP, fileH, otherInst, level); 
 
        } 
    } 
} 
 
fileH   << tab << "\t}" << std::endl;  // end of instance 
fileCPP << tab << "\t}" << std::endl;  // end of instance     
 
// . . .  
} 
Fonte: Autoria própria 
 
O resultado esperado desse processo de tradução apresentado pelo Código 25 é um 
arquivo (namespaces), no qual são definidos Attributes de todas as FBEs do programa fonte e 
quais Premises devem ser notificadas quando cada um dos Attributes tiverem seus estados 
alterados. Para tanto, basicamente, as linhas 1 a 43 do Código 25 implementam a definição do 
Attribute, enquanto a notificação de suas respectivas Premises interessadas estão implementadas 
pelas linhas 45 a 71.  
Conforme mencionado no capítulo anterior, na versão 2.0 da LingPON é possível 
instanciar FBEs dentro de outros FBEs (conceito de Agregação de FBEs). Neste sentido, 
supondo a tradução de um atributo da FBE Main, sendo que esse atributo se trata de uma 
instância de um FBE, é necessário percorrer também os Attributes dessa FBE e repetir o processo 
de tradução. É possível observar a implementação dessa repetição nas linhas 84 a 97 do Código 
25. 
A seção seguinte apresenta o processo de geração de códigos do NPCPP 2.0, bem como 
os códigos gerados em namespaces. Para auxiliar na construção desse gerador de códigos foi 
utilizada a aplicação Redes de Sensores. 
 


128 
 
 
3.1.2 Gerador de Código do NPCPP 2.0 – Construção via Aplicação Redes de Sensores 
Para validar o NPCPP 2.0 na fase de construção, foi utilizado uma aplicação 
denominada de Redes de Sensores. De maneira geral, tal aplicação consiste em uma simulação 
simplificada de sistema de monitoramento composto por um conjunto de sensores e alarmes. 
Neste contexto, quando é “detectada” a presença de um invasor, o alarme é acionado e o sistema 
simula a notificação da invasão via mensagem de texto.  
O código fonte do programa Redes de Sensores em LingPON 2.0 é apresentado na 
íntegra no Apêndice B, enquanto um extrato pertinente dele foi apresentado na seção acima 
pelos Códigos 26 e 27. A estrutura desta aplicação apresenta elementos próprios da LingPON 
2.0, as quais não estavam contidos na versão 1.0 da linguagem. Exemplos de tais elementos são 
a inclusão de bibliotecas externas, encapsulamento de Rules em FBEs e instanciação de FBEs 
dentro de outro FBE, os quais são melhor detalhados a seguir.  
De fato, a LingPON 2.0 apresenta alguns conceitos que as versões anteriores da 
linguagem não contêm, como particularmente esta organização hierárquico-flexível ou 
holônica, conforme já descrito anteriormente. Neste sentido, por exemplo, o Código 26 
apresenta, nas linhas 9 e 10, as declarações de duas instâncias do FBE Sector no FBE Main, 
representando a agregação de FBEs.  
 
Código 26 - Declaração de Instances de FBE do projeto Sensors.pon 
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
fbe Main 
 
   includes FRAMEWORK CPP 2 0  
      #include “SMSSender.h” 
#include <iostream>  
using namespace std; 
   end includes 
 
   private Sector sectorA  
   private Sector sectorB 
 
… 
 
end_fbe 
Fonte: Autoria própria 
 
Por sua vez, o Código 27 mostra que o FBE Sector contém uma instância do Attribute 
“atIntruderDetected” (linha 3) e instâncias de outros FBEs declaradas nas linhas 5 a 14. Para a 
geração de código, as instâncias de todos os FBEs agregados são percorridas até alcançar todos 
os Attributes do programa fonte, os quais são agrupados e definidos em um namespace 
denominado Instances. 


129 
 
 
Código 27 - Exemplo de declarações de Instances de FBE no FBE Main do projeto Sensors.pon 
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
fbe Sector 
 
   private Boolean atIntruderDetected = false 
 
   private Alarm alarmA 
   private Alarm alarmB 
 
   private Siren sirenA1 
   private Siren sirenA2  
   private Siren sirenB1 
 
   private Sensor sensorA1 
   private Sensor sensorA2  
   private Sensor sensorB1 
 
... 
 
end_fbe 
Fonte: Autoria própria 
 
Neste sentido, a materialização da LingPON em namespaces também foi reformulada 
para Tecnologia LingPON 2.0 em relação ao que havia na Tecnologia LingPON 1.2. A Figura 
37 apresenta como se dá essa nova estruturação em namespaces. 
 
Figura 37 - Materialização da LingPON 2.0 em namespaces 
 
Fonte: Adaptado de ATHAYDE e NEGRINI (2016) 
 
A Figura 37 apresenta a uma modelagem dos namespaces principais ou globais do 
NPCCPP 2.0, sobre o quais demais namespaces são organizados internamente, de maneira tal 
a tratar programas em LingPON na Tecnologia LingPON 2.0. Da mesma maneira que na 
materialização anterior, a geração de códigos desta versão transforma cada instância de certas 
entidades notificantes do PON em namespaces específicos.  


130 
 
 
No NPCPP 1.0, os códigos gerados são representados por três namespaces globais, 
nomeadamente Instantiations, Premises e SubConditions, enquanto no caso do NPCPP 2.0 
foram definidos quatro namespaces globais, nomeadamente os namespaces Rules, Premises, 
Methods e Instances (i.e., instâncias de FBEs) conforme apresentado na Figura 37. No NPCPP 
2.0 o namespace Instances contém as entidades-namespace Attributes e as entidades-
namespace Instances de FBEs, sendo cada entidade um (sub) namespace. Ainda, namespace 
Premise contém apenas as entidades-namespace Premises. Por sua vez, o namespace Rule 
contém as entidades-namespace Rules, bem como implicitamente as entidades-namespace 
Conditions as entidades-namespace SubConditions delas. Por fim, o namespace Method 
contém apenas as entidades-namespace Methods. O Código 28 ilustra como seria a notificações 
entre os namespaces gerados pelo NPCPP 2.0. 
 
Código 28 - Interação entre os namespaces gerados pelo NPCPP 2.0 
 
Fonte: Autoria própria 


131 
 
 
Basicamente, o processo de notificações entre as entidades na materialização em 
namespaces ocorre da seguinte maneira: quando uma entidade-namespace Attribute tem seu 
valor alterado, é feita uma chamada pela função notify das Premises interessadas via o 
namespace em questão; a cada entidade-namespace Premise satisfeita, é feita uma chamada, 
via namespace, das respectivas entidades-namespace Rule via funções pertinentes. Para cada 
entidade-namespace Rule é realizada uma verificação de quantas de suas respectivas entidades-
namespace Premise foram satisfeitas pela contabilização nela dos estados advindos via 
notificações. Se a quantidade de entidades-namespace Premise necessárias para a Rule ser 
aprovada for atingida, ocorre uma chamada via namespace das entidades-namespace Method 
interessados, os quais não raro acabam por alterar o valor de uma entidade-namespace Attribute 
via função setValue, notificando-os via namespace pertinente e realimentando o fluxo de 
notificações. 
Na versão anterior de materialização em namespaces, as declarações de Attributes e 
de Methods eram apresentadas em um mesmo arquivo e namespace chamados Instantiation, no 
qual agrupam-se as instâncias dos FBEs, contendo as definições de seus respectivos Attributes 
e Methods, cf. apresentado pelo Código 18 da Seção 2.4.2. 
Em contrapartida, na nova versão da geração de códigos (NPCPP 2.0), as declarações 
das entidades Attributes e Methods se encontram em arquivos e namespaces separados (i.e., 
cada qual em seu próprio namespace), conforme exemplificado pelo Código 29, namespace 
Instance resultante referente à aplicação Rede de Sensores em LingPON 2.0, representado pelo 
Código 21.  
 
Código 29 - Trecho do arquivo Instance gerado pela implementação em namespaces 
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
#include "instances.h" 
#include "premises.h" 
#include <string> 
namespace instance{ 
    namespace sector{ 
        namespace at{ 
            namespace atIntruderDetected{ 
                bool value = 0; 
                void setValue(bool newValue){ 
                    if (value != newValue){ 
                        value = newValue; 
                        premise::main::prSectorInvaded:: 
                            notify_sector_atIntruderDetected(newValue);   
                    }   
                }   
            }   
        }     
        namespace alarmA{ 
            namespace at{ 
                namespace atStatus{ 


132 
 
 
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
                    bool value = 0; 
                    void setValue(bool newValue){ 
                        if (value != newValue){ 
 
                      value = newValue; 
 
                      premise::sector::prAlarmAOn:: 
                                notify_alarmA_atStatus(newValue);        
                        }    
                    }    
                }   
            }   
        }   
    } 
} 
Fonte: Autoria própria 
 
Como é possível observar no Código 29, dentro do namespace global denominado 
“Instance” é gerado um namespace próprio para cada instância de FBE com seus respectivos 
Attributes. A atribuição de valores dos Attributes é feita acessando o namespace do método 
setValue() de cada atributo. Nas linhas 26 e 27 do Código 29, é apresentada a chamada, via 
namespace pertinente para a função notify_sector_atIntruderDetected(), da Premise 
interessada, quando o valor do Attribute atStatus da instância do FBE AlarmA é alterado.  
Seguindo a mesma lógica da compilação do namespace Instance, o arquivo 
(namespace) Premise, apresentado pelo Código 30, contém as Premises de todos os FBEs de 
um projeto PON.  
 
Código 30 - Trecho do arquivo Premise gerado pela implementação em namespaces 
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
#include "premises.h" 
#include "rules.h" 
#include <string> 
 
namespace premises{ 
    namespace sector{ 
        namespace prAlarmAOn{ 
            bool state = false; 
            bool cpy1st, cpy2nd; 
            void init(){  
                cpy1st = 0;  
                cpy2nd = 1;  
            } 
            void compare(){ 
                if(cpy1st  ==  cpy2nd){ 
                    if(state == false){ 
                        state = true; 
                        rule::sectorA::rlFireAlarmA::inc1(); 
                    }else{  
                        rule::sectorA::rlFireAlarmA::eql1();  
                    } 
                }else{ 
                    if(state == true){ 
                        state = false; 
 
                  rule::sectorA::rlFireAlarmA::dec1();   
                    }    


133 
 
 
27 
28 
29 
30 
31 
32 
33 
34 
35 
                }    
            } 
            void notify_alarmA_atStatus(bool newValue){ 
                cpy1st = newValue; 
                compare();                     
            }   
        }   
    }   
} 
 
Fonte: Autoria própria 
 
 
 
Conforme apresenta o Código 30, cada Premise contém duas variáveis (cpy1st e 
cpy2nd) utilizadas para fazer a comparação (dentro do método compare(), representado pelas 
linhas 14 a 28) e averiguar se a Premise em questão foi satisfeita. Em caso afirmativo, ocorre 
uma chamada, via namespace, das respectivas Rules via funções pertinentes, conforme 
apresentam as linhas 18, 20 e 25 do Código 30. 
A lógica de compilação do namespace Rule foi a que obteve mais alterações em 
relação ao compilador NPCPP 1.0. Isto porque, diferente das versões anteriores da linguagem, 
na LingPON 2.0 a entidade Condition pode ser composta tanto por diversas SubConditions (as 
quais são constituídas por um conjunto de Premises), quanto por um conjunto apenas de 
Premises (sem apresentar o nível SubCondition). O Código 31 mostra um exemplo de Rule 
(linhas 2 a 27) constituída por apenas Condition e Premises e um exemplo de Rule (linhas 31 a 
58) composta por SubCondition, além de Condition e Premises. 
 
Código 31 -  Exemplo de Rule que não contém o nível SubCondition e de Rule que o contém 
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
fbe Main 
    rule rlInvasionDetection 
        condition 
            premise prSectorAInvaded 
                sectorA.atIntruderDetected == true 
            end_premise 
            or 
            premise prSectorBInvaded 
                sectorB.atIntruderDetected == true 
            end_premise 
        end_condition 
        action sequential 
            instigation 
                call this.mtSendSms 
                    params 
                        "41-999999999" 
                    end_params 
                end_call 
 
          call this.mtSendSms 
                    params 
                        "47-999999999" 
                    end_params 
                end_call 
 
          call sectorA.mtNotifyInvasion() 
            end_instigation 


134 
 
 
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
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
48 
49 
50 
51 
52 
53 
54 
55 
56 
57 
58 
59 
        end_action 
    end_rule 
end_fbe 
 
fbe Sector 
   rule rlFireAlarmA 
        condition 
            subcondition 
                premise prSectorInPeaceA 
                    this.atIntruderDetected == false 
                end_premise 
                and 
                premise prAlarmAOn 
                    alarmA.atStatus == true 
                end_premise 
            end_subcondition 
            and 
            subcondition 
                premise prSensorA1State 
                    sensorA1.atState == true 
                end_premise 
                or 
                premise prSensorA2State 
                    sensorA2.atState == true 
                end_premise 
            end_subcondition 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtNotifyInvasion() 
            end_instigation 
        end_action 
    end_rule 
end_fbe 
Fonte: Autoria própria 
 
Durante essa parte do desenvolvimento do NPCPP 2.0, para a construção do 
namespace Rule, foi identificada que no Grafo PON não era possível recuperar as instâncias 
das Rules a partir da instância dos FBEs. Dessa forma, juntamente com Adriano F. Ronszcka, 
foi realizada esta melhoria na Tecnologia LingPON 2.0, a qual facilita a construção das 
interações das entidades do PON pelos compiladores.  
Na sequência, o Código 32 apresenta o namespace Rules, referente ao código em 
LingPON representado pelo Código 31, no qual é contabilizado quantas de suas respectivas 
Premises foram satisfeitas. A função inc(), na linha 5, indica que a Premise que a chamou 
passou a ser satisfeita, enquanto a função dec(), na linha 14, é chamada quando a respectiva 
Premise deixou de ser satisfeita. Por sua vez, no caso da função eql(), na linha 17, significa que 
a respectiva Premise tinha sido satisfeita e na atual verificação permanece neste mesmo estado. 
Se é atingida a quantidade de Premises necessárias para a Rule ser aprovada, os Methods 
interessados são chamados via namespaces, como é apresentado nas linhas 8 a 11, por exemplo.  


135 
 
 
Código 32 - Trecho do arquivo Rule gerado pela implementação em namespaces 
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
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
48 
49 
50 
51 
52 
53 
54 
55 
56 
57 
58 
59 
60 
namespace rule{ 
    namespace main{ 
        namespace rlInvasionDetection{ 
            int count = 0; 
            void inc(){ 
                count++; 
                if (count >= 1){ 
                    method::main::mtSendSms:: 
                                  mtSendSms("41-999999999"); 
                    method::main::mtSendSms:: 
                                  mtSendSms("47-999999999"); 
                } 
            } 
            void dec(){ 
                count--; 
            } 
            void eql(){ 
                if (count >= 1){ 
                    method::main::mtSendSms:: 
                                  mtSendSms("41-999999999"); 
                    method::main::mtSendSms:: 
                                  mtSendSms("47-999999999"); 
                } 
            } 
 
        } 
    } 
    namespace sectorA{ 
        namespace rlFireAlarmA{ 
            int count1 = 0; 
            bool status1; 
            int count2 = 0; 
            bool status2; 
            void inc1(){ 
                count1++; 
                status1 = false; 
                if (count1 == 2){ 
                    status1 = true; 
                    compareStatusSubConditions(); 
                } 
            } 
            void dec1(){ 
                count1--; 
            } 
            void eql1(){ 
                status1 = false; 
                if (count1 == 2){ 
                    status1 = true; 
                    compareStatusSubConditions(); 
                } 
            } 
            void inc2(){ 
                count2++; 
                status2 = false; 
                if (count2 >= 1){ 
                    status2 = true; 
                    compareStatusSubConditions(); 
                } 
            } 
            void dec2(){ 


136 
 
 
61 
62 
63 
64 
65 
66 
67 
68 
69 
70 
71 
72 
73 
74 
75 
76 
77 
                count2--; 
            } 
            void eql2(){ 
                status2 = false; 
                if (count2 >= 1){ 
                    status2 = true; 
                    compareStatusSubConditions(); 
                } 
            } 
            void compareStatusSubConditions(){ 
                if((status1 == true) && (status2 == true)){ 
                    method::sectorA::mtNotifyInvasion:: 
                                     mtNotifyInvasion(); 
                } 
            } 
        } 
    } 
Fonte: Autoria própria 
 
Em linhas gerais, para cada Condition (ou SubCondition, dependendo do caso) é feito 
um controle (por meio da variável count) contabilizando o número de Premises que foram 
aprovadas. Quando é atingido o número mínimo de Premises necessárias para que a Rule em 
questão seja satisfeita, é feita a chamada do namespace Method para a execução do 
correspondente Method. No caso de a Condition apresentar o nível de SubCondition, é feita 
uma verificação a mais (realizada via método compareStatusSubConditions()), certificando de 
que todas as SubCondition necessárias sejam aprovadas para, somente então, a execução do 
Method correspondente ser chamada. 
O Código 33 mostra o código compilado do namespace Method, no qual constam os 
Methods de todos os FBEs da aplicação Redes de Sensores, representada pelo Código 21.  
 
Código 33 - Trecho do arquivo Method gerado pela implementação em namespaces 
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
#include "methods.h" 
#include "instances.h" 
#include <string> 
 
        #include "SMSSender.h" 
        #include <iostream> 
        using namespace std; 
     
namespace method{ 
    namespace main{ 
        namespace mtSendSms{ 
            void mtSendSms(std::string cellphone){ 
 
 
                SMSSender *sender = new SMSSender(); 
                sender->send(cellphone); 
         
            } 
        } 
    } 
    namespace sectorA{ 
        namespace mtNotifyInvasion{ 


137 
 
 
22 
23 
24 
25 
26 
27 
28 
            void mtNotifyInvasion(){ 
                instance::sectorA::at::atIntruderDetected:: 
                                       setValue(1); 
            } 
        } 
    } 
    namespace sectorB{ 
Fonte: Autoria própria 
 
É possível observar no Código 33 um exemplo da inclusão de uma biblioteca externa 
(declarada pelas linhas 5 a 7), representada pela classe “SMSSender.h”, a qual foi implementada 
em C++ (de acordo com o target do compilador). As linhas 14 e 15 representam, 
respectivamente, a instanciação dessa classe externa e a utilização de seu método dentro do 
escopo do Method “mtSendSms” (linha 12). 
Para testar o funcionamento do código compilado pelo NPCPP 2.0 (o qual é 
apresentado de forma completa no Apêndice C), principalmente no âmbito da lógica de 
notificações entre as entidades, foi preciso implementar a "Main.cpp" e atribuir manualmente 
os valores de Attributes, como verificado pelas linhas 10 a 12 do Código 34.  
 
Código 34 - Implementação de Main.cpp em namespaces 
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
int main() { 
    ... 
 
    timeval time; 
    double initial; 
    double final; 
    gettimeofday(&time,0); 
    initial = (time.tv_sec * 1000.0) + (time.tv_usec / 1000.0); 
 
    instance::sectorB::at::atIntruderDetected::setValue(0); 
    instance::sectorB::alarmB::at::atStatus::setValue(1); 
    instance::sectorB::sensorB1::at::atState::setValue(1); 
 
    ... 
} 
Fonte: Autoria própria 
 
A aplicação de Redes de Sensores auxiliou a consolidar o primeiro passo para a 
construção do NPCPP 2.0, implementando conceitos e inovações específicos da LingPON 2.0, 
o que subsequentemente acabou se transformando em uma publicação no ERAD-SP em 2021 
(OSHIRO et al., 2021). Após esta etapa inicial de desenvolvimento, o próximo passo consiste 
em implementações de melhorias e conceitos de programação do PON visando a um melhor 
desempenho e funcionamento do compilador. Tais detalhes são apresentados na próxima seção. 
 


138 
 
 
3.2 
Melhorias da Tecnologia LingPON 2.0 e do NPCPP 2.0 
A construção básica do NPCPP 2.0 foi inspirada, a princípio, no já então existente 
NPCPP 1.0, porém levando em consideração também as características e conceitos específicos 
da versão 2.0 da Tecnologia LingPON que não estavam contidos em sua versão anterior. Assim, 
conforme já descrito, para construir um compilador que suportasse tais características específicas 
presentes na versão atual da LingPON, bem como validá-lo, foi utilizado o programa de Rede 
de Sensores escrito em LingPON 2.0. Neste âmbito, em um primeiro momento, percebeu-se que 
o NPCPP 2.0 herdava algumas imperfeições oriundas do NPCPP 1.0, o que o tornava de caráter 
prototipal. O Quadro 15 apresenta essas inconsistências identificadas, por pesquisadores do 
grupo de pesquisa do PON, na versão 1.0 do compilador e que foram afinadas no NPCPP 2.0. 
 
Quadro 15 - Lista de imperfeições encontradas no NPCPP 1.0 e afinadas no NPCPP 2.0 
  
Inconsistências herdadas do NPCPP 1.0 
Pesquisador 
Realizado 
1 Ajuste ao verificar a aprovação da Premise, quando 
seu estado continua verdadeiro 
Larissa K. Oshiro 
✓ 
2 Verificação dos estados das Premises no início da 
execução do programa 
Larissa K. Oshiro 
✓ 
3 Eliminar códigos repetidos quando há 
compartilhamento de Premises 
Jean M. Simão/ 
Adriano F. Ronszcka 
✓ 
4 Implementação de Premise Impertinente 
Leonardo F. Pordeus 
✓ 
Fonte: Autoria própria 
 
Ainda, após tais correções, a fim de aprimorar mais o NPCPP 2.0, durante o 
desenvolvimento do compilador, discentes-pesquisadores de uma disciplina de pós-graduação 
stricto sensu pertinente ao PON6 testaram o NPCPP 2.0 e a Tecnologia LingPON 2.0 a fim de 
identificar melhorias nessas duas ferramentas. Para tanto, foi aplicada uma atividade na qual os 
discentes-pesquisadores deveriam implementar em LingPON 2.0 uma simulação da 
funcionalidade “Soneca” do despertador de um celular. Os detalhes dessa atividade, bem como 
um exemplo de implementação dessa aplicação se encontram no Apêndice D. Algumas 
imperfeições foram identificadas e melhorias foram propostas por Felipe dos Santos Neves e 
Lucas Tachini Garcia e se encontram especificadas pelo Quadro 16. Apenas o item 6 do Quadro 
16 não foi identificada pelos discentes, mas pelo pesquisador do grupo do PON, Jean M. Simão.  
 
                                                          
6 A disciplina ‘Tópicos Especiais Em EC: PON’ foi ministrada por Jean Marcelo Simão em 
2019 e os discentes-pesquisadores que participaram de avaliações do NPCPP 2.0 foram: Anderson 
Eduardo de Lima, Felipe dos Santos Neves, Lucas Tachini Garcia, Luis Henrique Sant’Ana e Omero 
Francisco Bertol. 


139 
 
 
Quadro 16 - Relação de melhorias propostas no âmbito da Tecnologia LingPON 2.0 e do NPCPP 2.0 
  
Melhorias propostas 
Componentes a serem ajustados 
Realizado 
1 
No processo de compilação, ordenar os 
parâmetros dos Methods conforme são 
escritos no programa fonte 
Grafo PON 
X 
2 Execuções de expressões aritméticas nos 
parâmetros dos Methods 
LingPON 2.0 e Grafo PON 
X 
3 Execuções de expressão de negação nas 
Premises 
LingPON 2.0 e Grafo PON 
X 
4 Criação de um sistema de log  
Grafo PON 
X 
5 Expansão de Formation Rules no âmbito de 
vetores 
LingPON 2.0 e Grafo PON 
X 
6 Implementação de Unique Premise 
LingPON 2.0, Grafo PON e NPCPP 2.0 
✓ 
Fonte: Autoria própria. 
 
Os Quadros 15 e 16 mostram melhorias identificadas tanto no âmbito do compilador 
NPCPP 2.0, quanto da Tecnologia LingPON 2.0 (englobando a LingPON e o Grafo PON). Como 
é possível observar no Quadro 16, nem todas as melhorias foram efetivamente realizadas. O 
critério de prioridade selecionado para a execução dessas alterações foram: 
a. Inconsistências no compilador: Com o objetivo de construir um compilador o mais 
consolidado possível, que suportasse de maneira coerente as atribuições do PON e 
Tecnologia LingPON, todas a melhorias identificadas do NPCPP 2.0 em relação ao 
NPCPP 1.0 foram realizadas.  
b. Melhorias que afetam diretamente no desempenho de execução: Um dos objetivos 
deste trabalho é apresentar uma materialização do PON que apresente um alto 
desempenho de execução. Portanto, foram priorizadas as alterações que 
impactariam neste quesito. 
c. Demais melhorias ou funcionalidades adicionais na Tecnologia LingPON 2.0: Por 
último, a prioridade ficaria para as alterações que apresentam um aperfeiçoamento 
da Tecnologia LingPON 2.0, porém não afetam em seu funcionamento nem no 
desempenho de execução (redução de redundâncias) do NPCPP 2.0. 
Dessa forma, todos os itens do Quadro 15, os quais se referem apenas ao compilador, 
foram efetuados. Do Quadro 16, os itens que se enquadram nos quesitos 1 e 2 também foram 
priorizados e os que se enquadram no quesito 3 ficam como sugestão para os trabalhos futuros. 
Na sequência, cada uma das próximas seções descreve uma melhoria realizada.  
 


140 
 
 
3.2.1 Aprovação da Premise quando seu estado continua verdadeiro 
Esta alteração refere-se a uma melhoria feita referente à versão 1.0 do NPCPP. O 
compilador apresentava algumas inconformidades no processo de verificação da aprovação de 
Premises. Quando o valor de um Attribute é alterado, é verificado se todas as Premises 
interessadas são satisfeitas, contabilizando quantas destas são verdadeiras. Conforme explicado 
anteriormente, mais especificamente na Seção 3.1.1, nos códigos gerados em namespace 
funciona da seguinte maneira: quando uma Premise é satisfeita, é chamada, via namespace 
pertinente, a função inc() da respectiva Rule, na qual se contabiliza que tal Premise tem seu 
estado como verdadeiro. No caso em que a Premise deixou de ser satisfeita, chama-se então, via 
namespace pertinente, a função dec1() da respectiva Rule, na qual é refeito o cálculo para a 
Premise, agora com valor false.  
Porém, eram consideradas apenas as Premises que tinham seu status alterado para 
verdadeiro no momento da verificação em questão, ou seja, as Premises que já estavam como 
verdadeiras antes da verificação e, mesmo após, continuavam como verdadeiras, não eram 
contabilizadas no NPCPP 1.0 e, em um primeiro momento, no NPCPP 2.0. Dessa forma, o 
compilador não contabilizava de maneira correta o número total de Premises aprovadas após a 
alteração no estado de um Attribute e, portanto, havia casos em que as Rules interessadas 
deveriam ser notificadas e essa notificação não ocorria. Para solucionar essa questão, foi 
necessário ajustar no NPCPP 2.0 para que, no namespace Rule dos códigos compilados, 
houvesse uma nova função chamada eql(), indicando quando as Premise já estavam satisfeitas 
e, mesmo após a alteração no estado do Atributte correspondente, ainda mantiveram seu estado 
como verdadeiro. O Código 35 apresenta como fica a lógica no namespace Premise, gerado para 
a aplicação de Redes de Sensores, com a adição da chamada da função eql() (linhas 19 a 21) do 
namespace Rule. 
 
Código 35 - Adição da verificação se a Premise já estava satisfeita e permaneça com estado verdadeiro 
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
# include "premises.h" 
#include "rules.h" 
#include <string> 
 
namespace premises{ 
    namespace sector{ 
        namespace prAlarmAOn{ 
            bool state = false; 
            bool cpy1st, cpy2nd; 
            void init(){  
                cpy1st = 0;  
                cpy2nd = 1;  


141 
 
 
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
            } 
            void compare(){ 
                if(cpy1st  ==  cpy2nd){ 
                    if(state == false){ 
                        state = true; 
                        rule::sectorA::rlFireAlarmA::inc(); 
                    }else{  
                        rule::sectorA::rlFireAlarmA::eql();  
                    } 
                }else{ 
                    if(state == true){ 
                        state = false; 
 
           rule::sectorA::rlFireAlarmA::dec();       
                    }    
                }    
            } 
. . . 
} 
Fonte: Autoria própria 
 
Por sua vez, o Código 36 apresenta, nas linhas 15 a 20, um exemplo da implementação 
do método eql() no namespace Rule. 
 
Código 36 - Adição do método eql() no namespace Rule 
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
namespace rule{ 
    namespace main{ 
        namespace rlInvasionDetection{ 
            int count = 0; 
            void inc(){ 
                count++; 
                if (count >= 1){ 
                    method::main::mtSendSms::mtSendSms("41-999999999"); 
                    method::main::mtSendSms::mtSendSms("47-999999999"); 
                } 
            } 
            void dec(){ 
                count--; 
            } 
            void eql(){ 
                if (count >= 1){ 
                    method::main::mtSendSms::mtSendSms("41-999999999"); 
                    method::main::mtSendSms::mtSendSms("47-999999999"); 
                } 
            } 
        } 
. . .  
} 
Fonte: Autoria própria 
 
Como é possível observar no Código 36, o método eql(), assim como no método inc(), 
se responsabiliza por notificar os Methods interessados. Porém, o método eql() é chamado 
quando a respectiva Premise já apresentava estado verdadeiro e, mesmo após a alteração no 
estado de um dado Attribute, seu estado se manteve verdadeiro. Em contrapartida, o método 
inc() é acionado quando, após a alteração de um Attribute, o estado da Premise em questão é 


142 
 
 
alterado de não satisfeita para satisfeita. Neste caso, além de notificar os Methods interessados, 
a Premise é contabilizada no cálculo de Premises satisfeitas. 
 
3.2.2 Verificação dos estados das Premises no início da execução do programa 
Ainda em relação à validação do estado das Premises, no início da execução de um 
programa PON, é importante verificar se o status inicial dessas entidades, o que não estava sendo 
validado no NPCPP 2.0. Sem essa verificação inicial, a execução do programa era iniciada com 
todas as Premises apresentando sempre estado de não satisfeita, o que não resultava no fluxo de 
notificações esperado. Há casos em que um Attribute é inicializado com um valor que satisfaça 
uma determinada Premise do programa. Nesta situação, portanto, a Premise deve já estar com o 
seu estado calculado como verdadeiro ao iniciar a execução do programa.  
A solução, realizada na implementação do NPCPP 2.0 (cujo código-fonte completo 
consta no Apêndice A), foi adicionar à Classe NamespacesCompiler uma lista de strings 
denominada init_premises, na qual são guardadas as chamadas do método notify() de todas as 
Premises do programa. É válido relembrar que o método notify() é responsável pela verificação 
do estado da Premise. Uma vez populada, a lista init_premises é chamada na compilação do 
arquivo main.cpp dos códigos gerados para listar todos os métodos de notificação das Premises 
logo no início da execução do programa.  O Código 37 mostra um exemplo, referente à aplicação 
de Redes de Sensores, de código compilado do main.cpp, em que é realizada essa verificação 
inicial das Premises (linhas 10 a 25).  
 
Código 37 - Verificação do estado das Premises no início da execução de um programa 
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
#include <stdio.h> 
#include <sys/time.h> 
#include <iostream> 
#include "premises.h" 
#include "instances.h" 
 
using namespace std; 
 
int main() { 
 
premise::sectorA::prAlarmAOn::init(); 
 
premise::sectorA::prSectorInPeaceA::init(); 
 
premise::sectorA::prSensorA1State::init(); 
 
premise::sectorA::prSensorA2State::init(); 
 
premise::sectorA::prAlarmBOn::init(); 
 
premise::sectorA::prSectorInPeaceB::init(); 
 
premise::sectorA::prSensorB1State::init(); 
 
premise::sectorB::prAlarmAOn::init(); 
 
premise::sectorB::prSectorInPeaceA::init(); 
 
premise::sectorB::prSensorA1State::init(); 


143 
 
 
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
37 
38 
39 
40 
41 
42 
 
premise::sectorB::prSensorA2State::init(); 
 
premise::sectorB::prAlarmBOn::init(); 
 
premise::sectorB::prSectorInPeaceB::init(); 
 
premise::sectorB::prSensorB1State::init(); 
 
premise::main::prSectorAInvaded::init(); 
 
premise::main::prSectorBInvaded::init(); 
 
 
timeval time; 
 
double initial; 
 
double final; 
 
gettimeofday(&time,0); 
 
initial = (time.tv_sec * 1000.0) + (time.tv_usec / 1000.0); 
 
 
instance::sectorB::at::atIntruderDetected::setValue(0); 
 
instance::sectorB::alarmB::at::atStatus::setValue(1); 
 
instance::sectorB::sensorB1::at::atState::setValue(1); 
 
 
gettimeofday(&time,0); 
 
final = (time.tv_sec * 1000.0) + (time.tv_usec / 1000.0); 
 
double resultado = final - initial; 
 
cout << resultado << endl; 
 
return 0; 
} 
Fonte: Autoria própria 
 
3.2.3 Implementação de Compartilhamento de Premises 
O tratamento desse conceito foi realizado no NPCPP 2.0 quando se iniciou a 
implementação da aplicação Bitonic Sort para a LingPON 2.0. O Bitonic Sort é um algoritmo no 
qual se enquadra a aplicação do conceito de compartilhamento de Premises, no qual é possível 
eliminar notificações repetidas quando uma mesma Premise notifica duas ou mais Conditions. 
A explicação mais detalhada do Bitonic Sort e sua implementação em LingPON 2.0 estão 
apresentados nas próximas seções, mais especificamente na Seção 3.3.2.1. Por ora, é apresentado 
pelo Código 38 um trecho específico em LingPON 2.0 apenas para o entendimento do tratamento 
do conceito de programação do PON em questão. 
 
Código 38 - Exemplo de Compartilhamento de Premises em LingPON 2.0 para o Bitonic Sort 
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
fbe Comparator 
    private Integer atX1 = 0 
    private Integer atX2 = 0 
    private Integer atDirection = 0 
    private Boolean atSwapControl = false  
 
. . . 
 
 
    rule rlAscending 
        condition 
            premise prX1GreaterThanX2 
                this.atX1 > this.atX2 
            end_premise 


144 
 
 
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
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
            and 
            premise prAscending 
                this.atDirection == 1 
            end_premise 
            and 
            premise prControl 
                this.atSwapControl == 1 
            end_premise 
        end_condition 
        action sequential 
. . . 
        end_action 
    end_rule 
 
 
    rule rlDescending 
        condition 
            premise prX2GreaterThanX1 
                this.atX2 > this.atX1 
            end_premise 
            and 
            premise prDescending 
                this.atDirection == 0 
            end_premise 
            and 
            premise prControl 
                this.atSwapControl == 1 
            end_premise 
        end_condition 
        action sequential 
. . . 
        end_action 
    end_rule 
… 
end_fbe 
Fonte: Autoria própria 
 
Nas linhas 19 a 21 e 38 a 40 do Código 38, é possível observar que a Premise prControl 
faz parte de duas Conditions/Rules diferentes. Tais Rules, rlAscendig e rlDescending, são 
responsáveis por verificar e comparar dois algarismos da sequência para ordenar de forma 
ascendente e descendente, respectivamente.  
A importância de a implementação possuir tratamento de compartilhamento de 
Premises está diretamente ligada com a eliminação de redundâncias estruturais, conforme 
mencionado na Seção 2.1.3.5. Sem esse tratamento, o compilador transcrevia a definição de uma 
mesma Premise cada vez que era apresentada no código fonte. Dessa forma, o código de 
definição da Premise era apresentado repetidas vezes no namespace Premise, incorrendo 
justamente em redundâncias estruturais. 
No caso de compilação para namespaces do NPCPP 1.0, conforme explicado na Seção 
3.1.1, essa inconsistência gerava declarações repetidas de uma mesma Premise para notificar 
duas ou mais Rules diferentes, conforme apresentado no Código 39. 


145 
 
 
Código 39 - Exemplo do namespace Premise sem o tratamento de compartilhamento de Premise 
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
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
48 
49 
50 
namespace Premise{ 
    namespace main{ 
        namespace prMergeControl { 
            bool state = (false); 
            bool cpy1st = false; 
            bool cpy2nd = true; 
            void compare() { 
                if (cpy1st == cpy2nd) { 
                    if (state == false) { 
                        state = true; 
                        rule::main::rlBitonicSort::inc(); 
                    } else { 
                        rule::main::rlBitonicSort::eql(); 
                    } 
                } else { 
                    if (state == true) { 
                        state = false; 
                        rule::main::rlBitonicSort::dec(); 
                    } 
                } 
            } 
            void notify_this_atMergeControl(bool newValue) { 
                cpy1st = newValue; 
                compare(); 
            } 
        } 
        namespace prMergeControl { 
            bool state = (false); 
            bool cpy1st = false; 
            bool cpy2nd = true; 
            void compare() { 
                if (cpy1st == cpy2nd) { 
                    if (state == false) { 
                        state = true; 
                        rule::main::rlFinalMerge::inc(); 
                    } else { 
                        rule::main::rlFinalMerge::eql(); 
                    } 
                } else { 
                    if (state == true) { 
                        state = false; 
                        rule::main::rlFinalMerge::dec(); 
                    } 
                } 
            } 
            void notify_this_atMergeControl(bool newValue) { 
                cpy1st = newValue; 
                compare(); 
            } 
        } 
Fonte: Autoria própria 
 
O Código 39 apresenta trecho do código compilado do namespace Premise para a 
aplicação Bitonic Sort, na qual havia o caso de Premise compartilhada. Na implementação em 
LingPON, a Premise prMergeControl faz parte de duas regras: rlBitonicSort e rlFinalMerge. 
Como é possível observar no Código 39, a Premise em questão foi declarada duas vezes: a 


146 
 
 
primeira declaração (linha 3) representa a notificação desta entidade para a Rule rlBitonicSort e 
a segunda declaração (linha 27), para a Rule rlFinalMerge. Com o tratamento da Premise 
compartilhada no compilador, o namespace Premise passa a ser conforme apresentado pelo 
Código 40, eliminando redundâncias desnecessárias.  
 
Código 40 - Exemplo do namespace Premise com o tratamento de compartilhamento de Premise 
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
namespace Premise{ 
    namespace main{ 
        namespace prMergeControl { 
            bool state = (false); 
            bool cpy1st = false; 
            bool cpy2nd = true; 
            void compare() { 
                if (cpy1st == cpy2nd) { 
                    if (state == false) { 
                        state = true; 
                        rule::main::rlBitonicSort::inc(); 
                        rule::main::rlFinalMerge::inc(); 
                    } else { 
                        rule::main::rlBitonicSort::eql(); 
                        rule::main::rlFinalMerge::eql(); 
                    } 
                } else { 
                    if (state == true) { 
                        state = false; 
                        rule::main::rlBitonicSort::dec(); 
                        rule::main::rlFinalMerge::dec(); 
                    } 
                } 
            } 
            void notify_this_atMergeControl(bool newValue) { 
                cpy1st = newValue; 
                compare(); 
            } 
        } 
Fonte: Autoria própria 
 
 
Foi realizada uma comparação de desempenho do NPCPP 2.0 com e sem a 
implementação do tratamento de Compartilhamento de Premises, cujos resultados são 
apresentados pela a Figura 38.  
 
 
 
 
 
 
 
 


147 
 
 
Figura 38 - Resultado comparativo de implementações do NPCPP 2.0 com e  
sem Compartilhamento de Premises 
 
Fonte: Autoria própria 
 
De acordo com a Figura 38, é possível observar que o tratamento de compartilhamento 
de Premises afeta diretamente e consideravelmente o desempenho do processamento de 
execução, por conta da diminuição de notificações, o que levou, neste experimento, a uma 
redução no mínimo 30% do tempo de execução em todos os casos experimentados. 
 
3.2.4 
Implementação de Premissa Única ou Unique Premise 
Conforme detalhado na Seção 2.1.3.3, o conceito de Unique Premise auxilia na 
eliminação de notificações desnecessárias. No caso, por exemplo, do Bitonic Sort, uma mesma 
Premise faz parte de duas Rules, excludentes entre si. Conforme o Código 39, apresentado na 
seção anterior, a Premise prControl pertence às Rules rlAscending e rlDescending, responsáveis 
pela verificação da direção da ordenação da sequência, conforme mencionado anteriormente. 
Como a ordenação sempre apresentará um sentido apenas, as Rules se tornam excludentes entre 
si. Sem o tratamento de Unique Premise, quando a Premise em questão é satisfeita, esta notifica 
sempre as duas Rules interessadas, mesmo que a aprovação de uma implicaria automaticamente 
a não aprovação da outra, gerando processamentos desnecessários. Para implementar esse 
conceito foi necessário efetuar alterações no Grafo PON, na LingPON e no compilador NPCPP 
2.0. O Código 41, nas linhas 29 a 42, apresenta as implementações adicionadas no arquivo 
66,00
149,50
449,00
1159,00
44,00
56,50
106,50
267,00
8
1 6
32
64
TEMPO DE EXECUÇÃO (MICROSSEGUNDOS)
NÚMERO DE ELEMENTOS DA SEQUÊNCIA BITONIC
COMPARAÇÃO DE DESEMPENHO - BITONIC SORT
Sem Compartilhamento de Premise
Com Compartilhamento de Premise


148 
 
 
bison.y para a inclusão do parâmetro unique na sintaxe da Premise na LingPON 2.0, para indicar 
quando se trata de uma Premissa Única. 
 
Código 41 - Alteração no arquivo bison.y para inclusão do parâmetro unique  
na sintaxe da Premise LingPON 2.0 
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
37 
38 
39 
40 
41 
42 
Premise    : PREMISE expression END_PREMISE { 
               validate( 
                   graph->addEntity((Entity*)graph->createPremise( 
                                "", (Expression*) $2, false, false) 
                   ) 
               ); 
           } 
           | PREMISE id expression END_PREMISE { 
               validate( 
                   graph->addEntity((Entity*)graph->createPremise( 
                                $2, (Expression*) $3, false, false) 
                   ) 
               ); 
           } 
           | PREMISE IMPERTINENT expression END_PREMISE { 
               validate( 
                   graph->addEntity((Entity*)graph->createPremise( 
                                "", (Expression*) $3, true, false) 
                   ) 
               ); 
           } 
           | PREMISE IMPERTINENT id expression END_PREMISE { 
               validate( 
                   graph->addEntity((Entity*)graph->createPremise( 
                                $3, (Expression*) $4, true, false) 
                   ) 
               ); 
           } 
           | PREMISE UNIQUE expression END_PREMISE { 
               validate( 
                   graph->addEntity((Entity*)graph->createPremise( 
                                "", (Expression*) $3, false, true) 
                   ) 
               ); 
           } 
           | PREMISE UNIQUE id expression END_PREMISE { 
               validate( 
                   graph->addEntity((Entity*)graph->createPremise( 
                                $3, (Expression*) $4, false, true) 
                   ) 
               ); 
           }; 
Fonte: Autoria própria 
 
O Código 42, por sua vez, apresenta na linha 19 a sintaxe da Premise com a inclusão 
da palavra reservada unique, para indicar que a Premise é uma Unique Premise. Quando não é 
apresentada a palavra unique, a Premise em questão não é considerada como Unique Premise, 
por default. 
 
 


149 
 
 
Código 42 - Exemplo de sintaxe para indicar que a Premise é uma Unique Premise 
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
fbe Comparator 
    private Integer atX1 = 0 
    private Integer atX2 = 0 
    private Integer atDirection = 0 
    private Boolean atSwapControl = false  
 
. . . 
 
 
    rule rlAscending 
        condition 
            premise prX1GreaterThanX2 
                this.atX1 > this.atX2 
            end_premise 
            and 
            premise prAscending 
                this.atDirection == 1 
            end_premise 
            and 
            premise unique prControl 
                this.atSwapControl == 1 
            end_premise 
        end_condition 
        action sequential 
. . . 
        end_action 
    end_rule 
 
Fonte: Autoria própria 
 
O Código 43 apresenta, destacadas em vermelho, as alterações referentes à adição do 
parâmetro unique na classe Premise, a qual faz parte da interação com o Grafo PON. 
 
Código 43 - Alteração no arquivo Premise.cpp do Grafo PON para a inclusão do parâmetro unique 
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
#include "elements/Premise.h" 
. . . 
 
Premise::Premise(Instance *instance, std::string name, Expression 
*expression, bool impertinent, bool unique) 
    : Entity(instance, name) { 
 
    this->expression = expression; 
    this->impertinent = impertinent; 
    this->unique = unique; 
 
    this->initialLogicalValue = false; 
 
    this->attributes = new std::map<std::string, Attribute*>(); 
     
    this->condition = 0; 
    this->subcondition = 0; 
     
} 
. . . 
 
bool Premise::getUnique() { 
 
    return this->unique; 
 


150 
 
 
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
} 
. . . 
 
Premise* Premise::clone(Instance *instance) { 
 
    Expression *expression = this->expression->clone(); 
     
    return new Premise(instance, this->getName(), expression,  
                       this->impertinent, this->unique); 
 
} 
Fonte: Autoria própria 
 
Por sua vez, o Código 44 mostra um trecho de um namespace Premise do programa 
Bitonic Sort, compilado para o target NPCPP 2.0, no qual apresenta a diferença entre uma 
Premise padrão e uma Premise considerada Unique Premise.  
 
Código 44 - Exemplos de declaração de Unique Premise e de Premise padrão em namespaces 
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
namespace prMergeControl { 
    bool state = (false); 
    bool cpy1st = false; 
    bool cpy2nd = true; 
    void compare() { 
        if (cpy1st == cpy2nd) { 
            if (state == false) { 
                state = true; 
                if(rule::main::rlBitonicSort::inc() != true){ 
                    rule::main::rlFinalMerge::inc(); 
                } 
            } else { 
                if (rule::main::rlBitonicSort::eql() != true){ 
                    rule::main::rlFinalMerge::eql(); 
                } 
            } 
. . .  
} 
namespace prCounterFinalMerge { 
    bool state = (false); 
    int cpy1st = 0; 
    int cpy2nd = 16; 
    void compare() { 
        if (cpy1st > cpy2nd) { 
            if (state == false) { 
                state = true; 
                rule::main::rlFinalMerge::inc(); 
            } else { 
                rule::main::rlFinalMerge::eql(); 
            } 
. . . 
} 
Fonte: Autoria própria 
 
Para o tratamento deste conceito, no caso de se tratar de uma Unique Premise, os 
métodos inc() e eql() do namespace Rule foram transformados em função para retornar um valor 
indicando se a Rule em questão for aprovada ou não. Apenas em caso negativo, as demais Rules 


151 
 
 
passam a ser notificadas. Caso contrário, a Premise cessa seu fluxo de notificações, evitando 
processamento desnecessário. Esta verificação é exemplificada pelas linhas 9 e 13 do Código 
44. A linha 19 mostra a declaração de uma Premise padrão (prCounterFinalMerge), que não é 
considerada Unique Premise. Neste caso, os métodos inc() e eql() não precisam retornar valor, 
conforme mostram as linhas 27 e 29. Se a Premise prCounterFinalMerge notificasse mais Rules, 
além da rlFinalMerge, estas seriam notificadas normalmente por se tratar de Rules que não são 
excludentes entre si. 
Para validar a implementação desse conceito no NPCPP 2.0, foi realizada uma 
comparação de desempenho do compilador com e sem a implementação de Unique Premise, 
conforme apresenta a Figura 39. É pertinente salientar que para ambos os casos, o conceito de 
compartilhamento de Premise já estava implementado e, portanto, está sendo considerado. A 
aplicação utilizada foi o algoritmo Bitonic Sort. 
 
Figura 39 - Resultado comparativo de implementações do NPCPP 2.0 com e sem Única Premissa 
 
Fonte: Autoria própria 
 
Na Figura 39, é possível observar que com a implementação do conceito de Unique 
Premise, houve uma leve melhora no tempo de desempenho do NPCPP 2.0, diminuindo em 
cerca de 5% o tempo de processamento, no mínimo, em todos os casos. Um aspecto importante 
a ser ressaltado é que no caso do Bitonic Sort, a Unique Premise afeta apenas duas Rules, ou 
seja, a diferença da quantidade de notificações desnecessárias neste caso é de apenas uma única 
Rule. Neste sentido, em uma aplicação em que a Unique Premise notifique diversas Rules 
excludentes entre si, naturalmente deste conceito terá maior impacto no tempo do 
processamento.  
46
58,1
104,8
267,3
42,5
55
99,8
263,5
8
16
32
64
TEMPO DE EXECUÇÃO (MICROSSEGUNDOS)
NÚMERO DE ELEMENTOS DA SEQUÊNCIA BITONIC
COMPARAÇÃO DE DESEMPENHO - BITONIC SORT
Sem Premissa Única
Com Premissa Única


152 
 
 
3.2.5 
Implementação de Premise Impertinente 
A implementação do conceito de Premise impertinente no NPCPP 2.0 se deu com a 
utilização da aplicação Simulador CTA, a qual está descrita com mais detalhes na Seção 3.3.2. 
Neste momento, está descrito apenas detalhes da aplicação que são pertinentes para o 
entendimento do tratamento de Premise impertinente. 
Em linhas gerais, o Simulador CTA simula o tráfego de veículos do mundo real, no 
qual há um controle de abertura e fechamento dos semáforos, de acordo com o tipo de estratégias 
de controle. O Código 45 apresenta um trecho da implementação do FBE Semaphore em 
LingPON 2.0 para a estratégia conhecida como Controle Independente. Neste caso, o 
funcionamento dos semáforos depende basicamente apenas de dois fatores: (a) tempo, em 
segundos, dos semáforos, que está representado no Código 45 pelo Attribute atSeconds (linha 
4); e (b) estado dos semáforos (podendo apresentar estado vermelho, verde ou amarelo), que está 
representado pelo Attribute atSemaphoreState, na linha 3 do Código 45. 
 
Código 45 - Trecho do FBE Semaphore do Simulador CTA com exemplo de Premise Impertinente 
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
fbe Semaphore 
     
    private Integer atSemaphoreState = 5 
    private Integer atSeconds = 0 
. . .     
    rule rlHorizontalTrafficLightGreen 
        condition 
            premise impertinent prSeconds 
                this.atSeconds == 2 
            end_premise 
            and 
            premise prSemaphoreState 
                this.atSemaphoreState == 5 
            end_premise 
        end_condition 
        action 
            instigation 
                call this.mtHorizontalTrafficLightGREEN() 
                call this.mtSetStateAPI 
                    params 
 
 
            0 
                    end_params 
                end_call 
            end_instigation 
        end_action 
    end_rule 
 
. . . 
end_fbe 
Fonte: Adaptado de NEGRINI et al. (2019) 
 


153 
 
 
Ainda, na linha 8 do Código 45, é possível observar que a Premise prSeconds está 
declarada como impertinente, por meio da palavra reservada impertinent. Isto porque o Attribute 
prSeconds notifica a Premise prSeconds cada vez que o valor do tempo de contagem do 
semáforo varia, ou seja, a cada segundo. No entanto, a Condition/Rule será aprovada apenas 
quando o Attribute atSemaphoreState, que varia mais esporadicamente, apresentar um 
determinado valor. Dessa forma, a Premise prSeconds é considerada impertinente, uma vez que 
seu respectivo Attribute pode disparar notificações desnecessárias, neste caso. 
 
Com a implementação do tratamento deste conceito no NPCPP 2.0, houve alterações nos 
namespaces Instances e Premises dos códigos gerados pelo compilador. O Código 46 apresenta 
as alterações no namespace Instances. 
 
Código 46 - Alterações no namespace Instances com o tratamento de Premise Impertinente 
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
37 
38 
#include "instances.h" 
#include "premises.h" 
#include <string> 
#include <iostream> 
     
namespace instance { 
    namespace main { 
        namespace Semap { 
            namespace at { 
                namespace atSeconds { 
                    int value = 0; 
                    bool active = false; 
                    void setValue(int newValue) { 
                        if (active == true){ 
                            if (value != newValue) { 
                                value = newValue; 
                                premise::main::Semap::prAtSeconds3:: 
                                    notify_ Semap _atSeconds(newValue) 
                                premise::main::Semap::prAtSeconds4:: 
                                    notify_ Semap _atSeconds(newValue) 
                                premise::main::Semap::prAtSeconds5:: 
                                    notify_ Semap _atSeconds(newValue) 
                                premise::main::Semap::prAtSeconds6:: 
                                    notify_ Semap _atSeconds(newValue) 
                                premise::main::Semap::prSeconds:: 
                                    notify_ Semap _atSeconds(newValue) 
                                premise::main::Semap::prSeconds2:: 
                                    notify_ Semap _atSeconds(newValue); 
                            } 
                        } 
                    } 
                    void activate(bool value) { 
                        active = value;                         
                    } 
                } 
            } 
. . . 
} 
Fonte: Autoria própria 
 


154 
 
 
Conforme o Código 46 apresenta, foi adicionada uma nova variável denominada active 
para o Attribute correspondente à Premise impertinente. Esta variável tem a função de indicar 
quando as notificações do Attribute atSeconds estão ativadas ou desativadas temporariamente. 
As notificações deste Attributes são ativadas apenas quando a Premise prSemaphoreState (linha 
13 do Código 45) for satisfeita. Neste sentido, o namespace Premise gerado pelo NPCPP 2.0 
também apresentou alterações, conforme mostra o Código 47. 
 
Código 47 - Alterações no namespace Premises com o tratamento de Premise Impertinente 
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
37 
38 
39 
40 
41 
42 
43 
44 
#include "premises.h" 
#include "rules.h" 
#include <string> 
#include <iostream> 
     
namespace premise { 
    namespace main { 
        namespace Semap { 
. . . 
            namespace prSemaphoreState { 
                bool state = (true); 
                int cpy1st = 5; 
                int cpy2nd = 5; 
                compare() { 
                    if (cpy1st == cpy2nd) {    // Premise foi satisfeita 
                        if (state == false) { 
                            state = true; 
                            rule::main::Semap:: 
                                  rlHorizontalTrafficLightGreen::inc(); 
                        } else { 
                            rule::main::Semap:: 
                                  rlHorizontalTrafficLightGreen::eql(); 
                        } 
                        instance::main::Semap::at:: 
                                  atSeconds::activate(true); 
                        return true; 
                    } else {               // Premise não foi satisfeita 
                        if (state == true) { 
                            state = false; 
                            rule::main::Semap:: 
                                  rlHorizontalTrafficLightGreen::dec(); 
                            instance::main::Semap::at:: 
                                      atSeconds::activate(false); 
                        } 
                        return false; 
                    } 
                } 
                notify_Semap_atSemaphoreState(int newValue) { 
                    cpy1st = newValue; 
                    compare(); 
                } 
            } 
. . . 
} 
Fonte: Autoria própria 


155 
 
 
Por meio do Código 46, é possível observar que quando a Premise prSemaphoreState 
for satisfeita (linha 15), o valor da variável active do Attribute atSeconds é alterado, via chamada 
em namespace da função activate() deste Attribute, para verdadeiro (linhas 24 e 25), tornando 
suas notificações ativadas. Por outro lado, caso a Premise prSemaphoreState não for satisfeita 
(linha 27), o valor da variável active do Attribute atSeconds é alterado para falso (linhas 32 e 
33), desativando as notificações desnecessárias. 
Os desempenhos do compilador para as implementações com e sem o tratamento de 
Premise impertinente foram comparados e estão apresentados na Figura 40. É pertinente 
salientar que para ambos os casos, o conceito de compartilhamento de Premise já estava 
implementado e, portanto, está sendo considerado.  
 
Figura 40 - Resultado comparativo de implementações do NPCPP 2.0 com e sem Premise impertinente 
 
Fonte: Autoria própria 
 
Conforme mostra a Figura 40, com o tratamento de Premises impertinentes, o 
desempenho aumenta consideravelmente. Em todos os casos, o tempo de processamento de 
execução da implementação com Premises impertinentes reduz mais de 42,5% em relação ao 
tempo da implementação sem o tratamento deste conceito, no caso da estratégia de controle 
independente, e mais de 44,8% no caso de estratégia baseado em congestionamento. Este 
resultado e o de itens anteriores confirmam a importância e relevância dos conceitos de 
programação do PON para as implementações, especialmente as que carregam redundâncias 
temporais e estruturais. 
 
134230
199352
294410
395686
5824
114041
169180
220585
159036
230140
339067
442712
61924
125230
185896,5
243941
500
1000
1500
2000
TEMPO DE EXECUÇÃO (MS)
NÚMERO DE REPETIÇÕES
RESULTADO COMPARATIVO DO SIMULADOR CTA
Estratégia de Controle Independente -Sem Premise Impertinente
Estratégia de Controle Independente - Com Premise Impertinente
Controle Baseado em Congestionamento - Sem Premise Impertinente
Controle Baseado em Congestionamento - Com Premise Impertinente


156 
 
 
3.3 
Experimentos e Resultados 
Conforme mencionado na seção anterior, para validar o NPCPP 2.0 de uma maneira 
mais efetiva foi necessário realizar testes em aplicações, além da Rede de Sensores. Para tanto, 
foram utilizados benchmarks que apresentam características diferentes em suas 
implementações e, por isso, foi possível testar com cada qual um conceito diferente do PON no 
NPCPP 2.0, verificando o comportamento deste. Tais benchmarks são conhecidos como 
Simulador CTA, Bitonic Sort e Random Forest. Para os experimentos apresentados nesta seção, 
as implementações do NPCPP 2.0 foram geradas considerando a ativação da otimização O3 do 
compilador G++ em ambiente Linux. 
O Simulador CTA corresponde a um sistema que simula o tráfego de veículos e, 
devido à sua estruturação na implementação, permitiu testar a impertinência de entidades do 
PON, mais especificamente neste caso, em relação às Premises, conforme descrito na Seção 
3.2.5. A descrição mais completa do Simulador CTA e os resultados dos experimentos desta 
aplicação estão apresentados na Seção 3.3.1.  
O Bitonic Sort, por sua vez, é um algoritmo de ordenação já conhecido da literatura 
computacional e, devido à sua estruturação, auxiliou na implementação do conceito Unique 
Premise, tanto na linguagem LingPON 2.0 naturalmente expandindo isto para o Grafo PON, 
quanto no NPCPP 2.0, como mencionado na Seção 3.2.4. Além disso, o experimento com o 
Bitonic Sort tem teor interessante para analisar o comportamento do NPCPP 2.0 e, inclusive, 
do PON, pois em sua implementação a presença de redundâncias (temporais e estruturais) é 
mínima, diferente da aplicação de Redes de Sensores. Isto dito, a Seção 3.3.2 descreve sobre a 
aplicação Bitonic Sort e seus respectivos resultados obtidos.   
 
3.3.1 Aplicação Rede de Sensores 
Conforme mencionado anteriormente, a aplicação Rede de Sensores teve papel 
fundamental para a construção do NPCPP 2.0. Esta seção apresenta os resultados dos testes 
com um primeiro esforço de validação. Os resultados obtidos pelos testes dos códigos gerados 
pelo NPCPPP 2.0 (apresentados pelos Códigos 22, 23, 25, 26 e 27), a partir do programa em 
LingPON 2.0 representado pelo Código 21, foram comparados com resultados de 
implementações equivalentes e geradas pelo NPCPP 1.0 e também para com o desempenho de 


157 
 
 
solução em Paradigma Imperativo, mais especificamente implementado em POO C++. 
Naturalmente, buscou-se empregar aproximadamente (ou ao menos consideravelmente) o 
mesmo esforço na escrita deste código em C++ que o feito em LingPON. 
O sistema de Redes de Sensores apresenta um total de 10 Rules e foi executado para 
quatro cenários, nos quais 10%, 40%, 70% e 100% das Rules são aprovadas, e cada um dos 
cenários foi testado com as seguintes quantidades de iterações: 500, 1000, 1500 e 2000. Os testes 
foram realizados em um ambiente com eventuais variações de preempção de sistema operacional 
e afins, Linux Mint 19 (64 bits) em uma máquina com 12 GB RAM, Intel Core i3 – 7100 CPU 
@ 3.90 GHz. Os resultados foram obtidos em tempo de execução, em milissegundos, e 
correspondem à mediana dos valores obtidos de 15 execuções. As Figuras 41 a 44 apresentam 
os resultados de cada um dos quatro cenários das implementações em OO C++, do NPCPP 1.0 
e do NPCPP 2.0, para todas as iterações nos quatro cenários.  
 
Figura 41 -Resultado comparativo com 10% das Rules aprovadas 
 
Fonte: Autoria própria 
 
 
 
 
 
 
 
 
 
 
 
 
7,727392
52,60756
64,63306
74,78106
7,048826
33,10936
52,92898
63,73804
6,467186
21,86978
35,40996
51,069
500
1000
1500
2000
TEMPO DE EXECUÇÃO (MS)
NÚMERO DE REPETIÇÕES
COMPARAÇÃO DE DESEMPENHO -
10% REGRAS APROVADAS
C++ OO usual
NPCPP 1.0
NPCPP 2.0


158 
 
 
Figura 42 - Resultado comparativo com 40% das Rules aprovadas 
 
 
 Fonte: Autoria própria 
 
Figura 43 - Resultado comparativo com 70% das Rules aprovadas 
 
Fonte: Autoria própria 
 
Figura 44 - Resultado comparativo com 100% das Rules aprovadas 
 
Fonte: Autoria própria 
298,5926
447,327
660,437
837,7578
273,6684
430,1954
599,1058
754,7156
233,7984
392,7114
544,6262
694,2398
500
1000
1500
2000
TEMPO DE EXECUÇÃO (MS)
NÚMERO DE REPETIÇÕES
COMPARAÇÃO DE DESEMPENHO -
40% REGRAS APROVADAS
C++ OO usual
NPCPP 1.0
NPCPP 2.0
437,077
842,3546
1214,886
1552,65
425,1084
825,2394
1127,982
1506,496
383,4296
790,8266
1098,376
1417,338
500
1000
1 5 0 0
2000
TEMPO DE EXECUÇÃO (MS)
NÚMERO DE REPETIÇÕES
COMPARAÇÃO DE DESEMPENHO -
70% REGRAS APROVADAS
C++ OO usual
NPCPP 1.0
NPCPP 2.0
610,0144
1160,426
1751,738
2213,6
538,753
1122,7968
1708,676
2134,964
449,4984
1087,9432
1647,066
2098,668
500
1000
1500
2000
TEMPO DE EXECUÇÃO (MS)
NÚMERO DE REPETIÇÕES
COMPARAÇÃO DE DESEMPENHO -
100% REGRAS APROVADAS
C++ OO usual
NPCPP 1.0
NPCPP 2.0


159 
 
 
De acordo com os resultados apresentados, a implementação do NPCPP 2.0 é o que 
apresenta o melhor desempenho para todos os cenários apresentados, seguido do desempenho 
do NPCPP 1.0. Em outras palavras, os tempos de execução dessas duas implementações, 
baseadas em interações entre entidades notificantes, são menores que o da implementação em 
OO C++. Este resultado demonstra a capacidade do PON em termos de eliminar as redundâncias 
estruturais e temporais de programas, resultando em uma melhora de desempenho. É importante 
salientar que quanto maior o número de redundâncias em um programa, maior deveria ser o 
impacto do PON na melhoria de desempenho de execução. 
Conforme citado, o experimento foi realizado em um ambiente sujeito a preempções. 
Foi calculado o desvio padrão para todos os casos, apresentando um valor de até 30% do valor 
da mediana, caso extremo referente ao cenário de 10% das regras aprovadas com 2000 iterações. 
Para validar melhor o experimento, foram realizados, então, esses mesmos testes em uma 
máquina virtual EC2 disponibilizada pela AWS (Amazon Web Service) Ubuntu Server 18.04 
LTS, com processador Intel Xeon E5-2676 v3 @ 2.40GHz. Os resultados obtidos na EC2 estão 
representados pelas Figuras 45 a 48. 
 
Figura 45 - Resultado comparativo com 10% das Rules aprovadas na EC2 da AWS 
 
Fonte: Autoria própria 
 
 
 
 
 
 
12,2229
21,7629
30,0122
39,8669
11,8569
20,095
28,167
35,866
11,7891
19,9709
28,0789
35,8562
500
1 0 0 0
1 5 0 0
2 0 0 0
TEMPO DE EXECUÇÃO (EM MILISSEGUNDOS)
NÚMERO DE ITERAÇÕES
RESULTADO REDE DE SENSORES - 10% RULES APROVADAS
C++ OO usual
NPCPP 1.0
NPCPP 2.0


160 
 
 
Figura 46 - Resultado comparativo com 40% das Rules aprovadas na EC2 da AWS 
 
Fonte: Autoria própria 
 
Figura 47 - Resultado comparativo com 70% das Rules aprovadas na EC2 da AWS 
 
Fonte: Autoria própria 
 
Figura 48 - Resultado comparativo com 100% das Rules aprovadas na EC2 da AWS 
 
Fonte: Autoria própria 
146,401
287,695
430,946
572,831
144,908
284,296
425,689
565,287
139,435
275,028
411,463
546,029
500
1000
1500
2 0 0 0
TEMPO DE EXECUÇÃO (EM 
MILISSEGUNDOS)
NÚMERO DE ITERAÇÕES
RESULTADO REDE DE SENSORES - 40% RULES APROVADAS
C++ OO usual
NPCPP 1.0
NPCPP 2.0
286,763
562,332
852,915
1156,99
280,454
552,24
847,196
1151,1
275,173
545,296
836,909
1108,91
500
1000
1500
2 0 0 0
TEMPO DE EXECUÇÃO (EM 
MILISSEGUNDOS)
NÚMERO DE ITERAÇÕES
RESULTADO REDE DE SENSORES - 70% RULES APROVADAS
C++ OO usual
NPCPP 1.0
NPCPP 2.0
411,828
843,738
1251,62
1697,7
405,305
815,85
1242,51
1669,52
398,772
791,594
1220,97
1626,51
500
1000
1500
2000
TEMPO DE EXECUÇÃO (EM 
MILISSEGUNDOS)
NÚMERO DE ITERAÇÕES
RESULTADO REDE DE SENSORES - 100% RULES APROVADAS
C++ OO usual
NPCPP 1.0
NPCPP 2.0


161 
 
 
Os resultados obtidos dos experimentos realizados na máquina virtual da AWS 
confirmam que o NPCPP 2.0 obteve o melhor desempenho, seguido pelo NPCPP 1.0 e o C++ 
OO, em terceiro. No entanto, o desvio padrão calculado para este caso apresenta um valor 
menor que no ambiente com preempções, obtendo um valor máximo de 7% do valor da 
mediana. O NPCPP 2.0 apresentou um tempo de execução menor que o C++ OO em todos os 
casos, sendo que a maior diferença máxima (de 10%) foi no caso de 10% de Rules aprovadas 
para 2000 iterações e a mínima diferença (de 2,44%) foi no caso de 100% de aprovação das 
Rules para 1500 iterações 
Apesar de este primeiro experimento com NPCPP 2.0 representar uma contribuição 
para a materialização do PON, ainda foi necessário validá-lo em aplicações PON de maior 
complexidade. Neste sentido, a próxima seção irá descrever, portanto, experimentos com outras 
aplicações, de maiores complexidades, bem como os seus resultados obtidos. 
 
3.3.2 Controle de Tráfego Automatizado (Simulador CTA) 
Com o objetivo de validar de maneira mais efetiva o NPCPP 2.0, o gerador de código 
foi integrado com um projeto que simula um controle de tráfego, denominado simulador CTA 
(Controle de Tráfego Automatizado), sendo que os resultados foram comparados com o 
desempenho de implementações em Paradigma Imperativo realizadas em estudos precedentes.  
 
3.3.2.1 Descrição do Simulador CTA 
O Simulador CTA consiste em um projeto desenvolvido por um grupo de docentes da 
Universidade Tecnológica Federal do Paraná (UTFPR) e tem o objetivo de simular o tráfego de 
veículos de um mundo real. Basicamente, esse projeto é compreendido por dois módulos: um 
módulo simulador e um módulo de controle.  O módulo simulador permite representar objetos 
do mundo real, enquanto o módulo de controle permite justamente definir estratégias de 
controle de semáforos. Em tempo, naturalmente, a implementação de tais estratégias de controle 
pode ser realizada em diferentes paradigmas de programação. Neste sentido, o Simulador CTA 
pode e foi pensado para ser utilizado para comparar desempenho das estratégias desenvolvidas 
em paradigmas diferentes (RENAUX et al., 2014; NEGRINI, 2019; NEGRINI et al., 2019). 


162 
 
 
 
3.3.2.1.1  Simulador 
O simulador apresenta objetos de uma região de tráfego do mundo real, tais como 
veículos, semáforos, ruas, quadras, sensores, pistas e cruzamentos. Esses cruzamentos são 
constituídos por dez ruas horizontais e dez ruas verticais de mão única, como se fosse uma 
matriz 10x10 e formando 100 intersecções no total, conforme é apresentado na Figura 49 
(PADILHA, 2014; RENAUX et al., 2014; NEGRINI, 2019; NEGRINI et al., 2019). 
 
Figura 49 - Representação do ambiente simulado pelo CTA 
 
Fonte: RENAUX et al. (2014) 
 
Em cada intersecção há dois sinaleiros (um na rua vertical e outro na rua horizontal), 
os quais constituem, juntos, um semáforo, que pode apresentar os mesmos estados de um 
semáforo real: verde, amarelo ou vermelho. Ainda, assim como no mundo real, os dois 
sinaleiros de um cruzamento não podem estar verdes ao mesmo tempo (PADILHA, 2014; 
RENAUX et al., 2014; NEGRINI et al., 2019). 
Cada rua pode conter de uma a quatro pistas, sendo possível popular cada pista com 
até 25 veículos, os quais são criados de forma constante no intervalo de 0.1, 0.2, 0.3, 0.4 ou 0.5 
veículos por segundo. Quando são criados, os veículos começam a se movimentar em uma 
velocidade equivalente a 20m/s e devem parar o movimento se o sinaleiro da quadra em que se 
encontram estiver vermelho ou se a próxima quadra estiver lotada. Ainda, em cada intersecção, 


163 
 
 
de 5% a 35% dos veículos podem virar para outra quadra (PADILHA, 2014; RENAUX et al., 
2014; NEGRINI, 2019; NEGRINI et al., 2019).  
Por fim, o comprimento das quadras é de 100 metros e em cada uma delas há sensores 
para detectar a quantidade de veículos parados no sinal vermelho. Neste contexto, se a quadra 
estiver com menos de 60% de ocupação, o sensor apresenta o estado FEW, se a quadra estiver 
com ocupação entre 60% e 99%, o sensor passa para o estado MANY, e se a quadra estiver 
100% ocupada, o estado do sensor é FULL (RENAUX et al., 2014; NEGRINI, 2019; NEGRINI 
et al., 2019).  
A princípio, a simulação não é realizada por efeitos gráficos, mas é registrada em um 
arquivo de log com eventos dispostos de maneira sequencial e, a partir deste arquivo é possível 
obter a animação utilizando o Animador CTA (NEGRINI, 2017). 
 
3.3.2.1.2  Estratégia de Controle de Semáforos 
O simulador CTA pode apresentar três tipos de estratégia de controle de semáforos: 
controle independente, controle baseado em congestionamento e controle baseado em tráfego 
facilitado. A estratégia de controle independente é a mais simples e não considera os sensores 
que avaliam a quantidade de carros. Assim, cada sinaleiro simplesmente possui um determinado 
tempo para permanecer em cada estado (PADILHA, 2014; RENAUX et al., 2014; NEGRINI, 
2019; NEGRINI et al., 2019) 
Por sua vez, a estratégia baseada em congestionamento avalia o estado dos sensores, 
pois o tempo dos semáforos depende da quantidade de veículos parados e o tempo do estado do 
sinaleiro (PADILHA, 2014; RENAUX et al., 2014; NEGRINI, 2019; NEGRINI et al., 2019).  
Se a porcentagem de veículos parados estiver entre 60% e 100% e o tempo do sinaleiro em 
vermelho é menor que 24 segundos, o tempo total deste sinaleiro em vermelho é ajustado para 
30 segundos. Se a porcentagem de veículos parados estiver entre 60% e 100% e o tempo do 
sinaleiro em estado vermelho for maior que 24 segundos e menor que 40 segundos, o estado do 
sinaleiro oposto é alterado para amarelo e o tempo restante do sinaleiro em vermelho é ajustado 
para 6 segundos. No entanto, o tempo do sinaleiro em vermelho não será alterado se a 
porcentagem de veículos for entre 60% e 100% e o tempo do sinaleiro em vermelho for de 40 
segundos ou mais (RENAUX et al., 2014; NEGRINI, 2019; NEGRINI et al., 2019). 
Por fim, a terceira estratégia de controle é a baseada em tráfego facilitado. Nesse tipo 
de controle, o semáforo conhece o estado dos sensores e o tempo do estado do semáforo 


164 
 
 
anterior. Além disso, um dos sinaleiros de cada semáforo possui uma flag para sinalizar que a 
rua correspondente possui tráfego facilitado. Se o congestionamento for menor que 60%, o 
semáforo abre 5 segundos depois que sinaleiro do semáforo anterior abrir. Se a porcentagem de 
congestionamento estiver entre 60% e 99%, nada é alterado. Porém, se o nível de 
congestionamento for de 100%, então o semáforo abre 5 segundos antes que o sinaleiro do 
semáforo anterior abrir (PADILHA, 2014; RENAUX et al., 2014; NEGRINI et al., 2019). 
 
3.3.2.2 Implementação das Estratégias em LingPON 2.0 
O NPCPP 2.0 foi aplicado em apenas dois tipos de estratégias de controle: o controle 
independente e o controle baseado em congestionamento. O controle independente é modelado 
pelo diagrama de estado da Figura 50.  
 
Figura 50 - Diagrama de estado da estratégia de controle independente 
 
Fonte: RENAUX et al. (2014). 
 
Por sua vez, o controle baseado em congestionamento é modelado pelo diagrama de 
estado da Figura 51. 
 


165 
 
 
Figura 51 - Diagrama de estado da estratégia de controle baseado em congestionamento
 
Fonte: RENAUX et al. (2014). 
 
Para a implementação dessas estratégias em LingPON 2.0, cada transição do diagrama 
foi transformada em Rule. Os Attributes correspondem ao tempo e ao estado do semáforo e, no 
controle de congestionamento, aos sensores de quantidade de veículos parados dos sinaleiros 
vertical e horizontal. Ainda, as Premises foram implementadas de forma que são aprovadas 
quando os Attributes atingem os valores conforme os diagramas de estados apresentados. Para 
ilustrar como é a estrutura da estratégia de controle implementada em LingPON 2.0, o Código 
48 representa o FBE Semaphore da estratégia de controle independente. Os códigos fonte 
completos em LingPON 2.0 implementados para as duas estratégias são apresentados no 
Apêndice E. 
 
Código 48 - Parte do arquivo fonte Semaphore em LingPON 2.0 utilizado  
para a implementação do NPCPP 2.0 
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
fbe Semaphore 
    private Integer atId = 0 
    private Integer atSemaphoreState  =  5  
    private Integer atSeconds = 0 
   
    private method mtResetTimer    
        attribution 
            this.atSeconds = 0 
        end_attribution 
    end_method 
 
    private method mtHorizontalTrafficLightGREEN 


166 
 
 
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
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
48 
49 
50 
51 
52 
53 
54 
55 
56 
57 
58 
59 
60 
61 
62 
63 
64 
        attribution 
            this.atSemaphoreState = 0  
        end_attribution 
    end_method 
     
    private method mtHorizontalTrafficLightYELLOW 
        attribution 
            this.atSemaphoreState = 1  
        end_attribution 
    end_method 
 
    private method mtHorizontalTrafficLightRED 
        attribution 
            this.atSemaphoreState = 2  
        end_attribution 
    end_method 
 
    rule rlHorizontalTrafficLightGreen  
        condition 
            premise impertinent prSeconds 
                this.atSeconds  == 2  
            end_premise 
            and 
            premise prSemaphoreState 
                this.atSemaphoreState == 5  
            end_premise 
        end_condition 
        action sequential 
            instigation parallel  
                call this.mtHorizontalTrafficLightGREEN()  
                call this.mtSetStateAPI(0) 
            end_instigation  
        end_action 
    end_rule 
 
    rule rlHorizontalTrafficLightYellow 
        condition 
            premise impertinent prSeconds2 
                this.atSeconds  == 40  
            end_premise 
  
 
and 
            premise prSemaphoreState2 
                this.atSemaphoreState == 0  
            end_premise 
        end_condition 
        action sequential 
            instigation parallel  
                call this.mtHorizontalTrafficLightYELLOW()  
                call this.mtSetStateAPI(1) 
            end_instigation 
        end_action 
    end_rule 
Fonte: Autoria própria 
 
Conforme já mencionado anteriormente na Seção 3.2.5, concomitantemente à 
implementação do Simulador CTA em LingPON 2.0 foi possível desenvolver no NPCPP 2.0 o 
tratamento das Premises impertinentes, o que viabilizou uma melhora no desempenho de 
processamento de execução. 


167 
 
 
3.3.2.3 API para integração com o Simulador CTA 
O simulador apresenta representações de objetos do mundo real de um tráfego de área 
urbana (e.g., como ruas, quadras, cruzamentos, sensores e semáforos). Toda dinâmica desse 
sistema se dá de acordo com a estratégia de controle contida no objeto semáforo. O simulador 
e seu respectivo objeto Semáforo foram implementados em C++ (NEGRINI et al., 2016), 
enquanto as estratégias de controle foram compiladas em C++ notificante modular orientado a 
namespaces.  
Para vincular a classe Semaphore do simulador com a instância do FBE gerado em 
C++ notificante orientado a namespaces, foi necessário criar uma API (Application 
Programming 
Interface), 
que 
consiste 
em 
uma 
classe 
em 
C++, 
denominada 
SimuladorNamespaceAPI, contendo métodos estáticos para fazer essa integração entre as duas 
linguagens de programação. A Figura 52 apresenta o diagrama de classes em UML do 
Simulador CTA. 


168 
 
 
Figura 52 - Diagrama de classes em UML do Simulador CTA integrado com as estratégias de controle em C++ notificante modular orientado a namespaces 
 
Fonte: Adaptado de RENAUX et al. (2014). 


169 
 
 
Conforme a Figura 52 ilustra, o diagrama de classes é composto pelo módulo do 
simulador (Simulator_Module) e pelo módulo das estratégias de controle (Controller_Module). 
O módulo do simulador apresenta as classes que representam os objetos de um ambiente urbano 
e o relacionamento entre elas. O módulo das estratégias de controle, por sua vez, é responsável 
pelo controle de semáforos de acordo com o tipo de estratégia de controle definida.  
Mais precisamente, os componentes Controller_NOP_CTA e Controller_NOP_CBCL 
correspondem, respectivamente, às estratégias de controle independente e de controle baseada 
em congestionamento, cujos códigos foram compilados em NPCPP 2.0 a partir de 
implementação em LingPON 2.0. Ainda, a API implementada para integrar as estratégias de 
controle implementadas em NPCPP 2.0  com o Simulador CTA é representada pelas classes 
SimuladorNamespaceAPI_CTA e SimuladorNamespaceAPI_CBCL. 
Os Códigos 49 e 50 apresentam exemplos de métodos do SimuladorNamespaceAPI 
que fazem essa integração.  
 
Código 49 - Método da API que notifica a estratégia de controle sobre a alteração de um Attribute 
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
void SimuladorNamespaceAPI::setSemaphoreStateNop(int id, int 
state) 
{ 
  switch (id) 
  { 
    case  1 : 
      instance::main::S1__vector_0::at:: 
                atSemaphoreState::setValue(state);  
      break; 
    case  2 : 
      instance::main::S1__vector_1::at:: 
                atSemaphoreState::setValue(state);  
      break; 
    case  3 : 
      instance::main::S1__vector_2::at:: 
                atSemaphoreState::setValue(state); 
      break; 
    case  4 : 
      instance::main::S1__vector_3::at:: 
                atSemaphoreState::setValue(state); 
      break; 
    case  5 : 
      instance::main::S1__vector_4::at:: 
                atSemaphoreState::setValue(state); 
      break; 
    case  6 : 
      instance::main::S1__vector_5::at:: 
                atSemaphoreState::setValue(state); 
      break; 
    case  7 : 
      instance::main::S1__vector_6::at:: 
                atSemaphoreState::setValue(state); 
      break; 
    case  8 : 
      instance::main::S1__vector_7::at:: 


170 
 
 
36 
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
                atSemaphoreState::setValue(state); 
      break; 
    case  9 : 
      instance::main::S1__vector_8::at:: 
                atSemaphoreState::setValue(state); 
      break; 
    case  10 : 
      instance::main::S1__vector_9::at:: 
                atSemaphoreState::setValue(state); 
      break; 
  } 
} 
Fonte: Autoria própria 
 
Quando o estado de um semáforo do simulador é alterado, a estratégia de controle deve 
ser notificada para serem feitas as validações de acordo com a estratégia em questão.  O Código 
49 mostra a chamada do namespace Instance a fim de alterar o valor do Attribute atState da 
instância do FBE Semaphore correspondente. Pelo fluxo de notificações do PON, as Premises 
correspondentes serão verificadas e, se todas forem satisfeitas, a respectiva Rule será notificada, 
chamando um método, por sua vez, modifica o valor novamente algum Attribute do FBE. Nesse 
momento é preciso informar o objeto semáforo do simulador que o estado dele alterou. Dessa 
forma, a classe SimuladorNamespaceAPI é chamada pela implementação da estratégia de 
controle e seu método SetStateSim() (linha 26 do Código 50) informa o objeto semáforo do 
simulador sobre a alteração de estado, conforme apresenta o Código 50. Tal método, como é 
possível observar, foi implementado de uma maneira pouco dinâmica, o que torna um pouco 
inviável se considerar uma aplicação com um número grande de semáforos, mas que ainda 
assim bem atendeu ao necessário para o experimento.  
 
Código 50 - Método da API que notifica o semáforo do simulador sobre a alteração de seu estado 
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
#include "SimuladorNamespaceAPI.h" 
#include "../Traffic_Light.h" 
#include "instances.h" 
#include <string> 
using namespace std; 
using namespace instance; 
 
void SimuladorNamespaceAPI::addSemaphore(Semaphore* semaphore) 
{ 
 
apiSemaphores.push_back(semaphore); 
} 
 
Semaphore* SimuladorNamespaceAPI::getSemaphoreSim(int id) 
{ 
 
std::list<Semaphore*>::const_iterator it; 
 
 
for (it = (&apiSemaphores)->begin();  
                 it != (&apiSemaphores)->end(); ++it) { 
 
 
Semaphore* semaphore = (*it); 
 
 
if (semaphore->GetId() == id) 


171 
 
 
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
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
48 
49 
50 
51 
52 
53 
54 
55 
56 
57 
58 
59 
60 
61 
62 
63 
64 
65 
66 
67 
68 
69 
70 
71 
72 
73 
74 
75 
76 
77 
78 
79 
80 
81 
 
 
{ 
 
 
 
return semaphore; 
 
 
} 
 
} 
} 
 
void SimuladorNamespaceAPI::setStateSim(int id, int state) 
{ 
 
Semaphore* semaphore = getSemaphoreSim(id); 
 
 
switch (state) 
 
{ 
 
case 0: 
 
 
semaphore->GetHorizontalTrafficLight()-> 
                       SetState(GREEN); 
 
 
semaphore->GetVerticalTrafficLight()-> 
                       SetState(RED); 
 
 
break; 
 
case 1: 
 
 
semaphore->GetHorizontalTrafficLight()-> 
                       SetState(YELLOW); 
 
 
semaphore->GetVerticalTrafficLight()-> 
                       SetState(RED); 
 
 
break; 
 
case 2: 
 
 
semaphore->GetHorizontalTrafficLight()-> 
                       SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(RED); 
 
 
break; 
 
case 3: 
 
 
semaphore->GetHorizontalTrafficLight()-> 
                       SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()-> 
                       SetState(GREEN); 
 
 
break; 
 
case 4: 
 
 
semaphore->GetHorizontalTrafficLight()-> 
                       SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()-> 
                       SetState(YELLOW); 
 
 
break; 
 
case 5: 
 
 
semaphore->GetHorizontalTrafficLight()-> 
                       SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(RED); 
 
 
break; 
 
case 6: 
 
 
semaphore->GetHorizontalTrafficLight()-> 
                       SetState(GREEN); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(RED); 
 
 
break; 
 
case 7: 
 
 
semaphore->GetHorizontalTrafficLight()-> 
                       SetState(YELLOW); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(RED); 
 
 
break; 
 
case 8: 
 
 
semaphore->GetHorizontalTrafficLight()-> 
                       SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()-> 
                       SetState(GREEN); 


172 
 
 
82 
83 
84 
85 
86 
87 
88 
89 
90 
 
 
break; 
 
case 9: 
 
 
semaphore->GetHorizontalTrafficLight()-> 
                       SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()-> 
                       SetState(YELLOW); 
 
 
break; 
 
} 
} 
Fonte: Autoria própria 
 
 
A próxima seção apresenta os resultados obtidos das implementações das estratégias de 
controle independente e de controle baseada em congestionamento do NPCPP 2.0 e as 
comparações com os resultados de implementações realizados em estudos precedentes. 
 
3.3.2.4 Testes e Resultados 
A aplicação do Simulador CTA havia sido testada em estudos precedentes. Justamente, 
Negrini (2015) realizou esse estudo comparando uma materialização do PON para com a 
linguagem C++ OO usual do PI sobre o desempenho do Simulador CTA. A materialização PON 
corresponde aos códigos gerados em C++ OO específico-notificante a partir da LingPON 1.0 da 
Tecnologia LingPON 1.0.  
A fim de validar o NPCPP 2.0 e aproveitar essa pesquisa de Negrini, suas 
implementações foram executadas novamente para que os respectivos resultados fossem 
comparados aos resultados obtidos pelo compilador desenvolvido neste trabalho7. As 
implementações foram executadas nos seguintes números de repetições: 500, 1000, 1500 e 2000 
sendo que cada repetição representa 1 segundo do semáforo. Os experimentos apresentados 
para o Simulador CTA foram realizados em um ambiente sujeito a variações de preempção de 
sistema operacional e afins, Windows 10 (64 bits) em uma máquina com 12 GB RAM, Intel 
Core i3 – 7100 CPU @ 3.90 GHz. Os resultados comparativos, os quais são obtidos em tempo 
de execução em milissegundos, são verificados pela Figura 53. Estes resultados correspondem 
à mediana uma amostra de 10 execuções. É válido ressaltar que para esse experimento já estão 
sendo consideradas os tratamentos para o conceito de Premises impertinentes. 
 
 
 
                                                          
7 O teste não foi realizado para o NPCPP 1.0, pois esta implementação apresentava diversas 
inconsistências, o que dificultariam os experimentos. 


173 
 
 
COMPARAÇÃO DOS RESULTADOS – SIMULADOR CTA 
 
Figura 53 - Gráfico do resultado do experimento com a aplicação do Simulador CTA 
 
 
 
 
 
Fonte: Autoria própria 
 
Analisando os dados da Figura 53, é possível observar que em todos os casos, a 
implementação C++ OO específico-notificante gerado a partir de LingPON apresentou um 
desempenho inferior. Por outro lado, a implementação em NPCPP 2.0 apresenta um 
desempenho muito próximo ao do C++ OO implementado sob os princípios da programação 
imperativa, principalmente para a estratégia de controle baseado em congestionamento, na qual 
o NPCPP 2.0 até supera o C++ OO em termos de desempenho. A implementação do conceito 
de Premises impertinentes permitiu um desempenho satisfatório para o NPCPP 2.0. 
 
3.3.3 Bitonic Sort 
Conforme descrito no início desta seção, o Bitonic Sort é uma aplicação que apresenta 
características diferentes das aplicações apresentadas anteriormente, principalmente da 
presença mínima de redundâncias. Experimentos com este tipo de aplicação é relevante para 
validar o comportamento do NPCPP 2.0, e do próprio PON, o qual naturalmente deve se 
53612,5
97512
148755,5
203194
70692
129974
193098
254414
58248
114041,5
161918,5
220585
500
1000
1500
2000
TEMPO DE EXECUÇÃO 
(MS)
NÚMERO DE REPETIÇÕES
CONTROLE INDEPENDENTE
65724,5
128732,5
186114,5
244300,5
83940
155511
222786,5
299634
61924
125230
185896,5
244809,5
500
1000
1500
2000
TEMPO DE EXECUÇÃO 
(MS)
NÚMERO DE REPETIÇÕES
CONTROLE BASEADO EM CONGESTIONAMENTO


174 
 
 
apresentar de maneira diferente do que nos experimentos com Redes de Sensores e Simulador 
CTA. 
 
3.3.3.1 Descrição do Bitonic Sort 
Criado por Ken Batcher (1968), o Bitonic Sort corresponde a um algoritmo de 
ordenação executado por meio de uma sequência de comparações pré-definidas, ou seja, a 
sequência de comparações não depende dos valores dos elementos. No entanto, o número de 
comparações depende da quantidade de elementos de entrada. Em eventuais ambientes 
multiprocessados, o desempenho da execução é favorecido, uma vez que os comparadores do 
algoritmo podem ser executados de forma paralela. Tal algoritmo executa operações de divisão 
e mesclagem para ordenar uma sequência de N elementos utilizando log2 N estágios 
(BATCHER, 1968; PETERS et al., 2012). 
Uma sequência é considerada como bitonic quando é composta por duas subsequências, 
sendo a primeira de ordem crescente e a segunda, decrescente. Neste sentido, para que uma 
sequência [0 ... n-1] seja bitonic, é necessário existir um índice i tal que 0 <= i <= n-1, respeitando 
as regras 𝑥0 <= 𝑥1 <= ... <= 𝑥𝑖 e 𝑥𝑖 >= 𝑥𝑖+1 >= ... >= 𝑥𝑛−1. Para visualizar melhor, a Figura 54 
representa um exemplo de sequência bitonic (MULLAPUDI, 2014). 
 
Figura 54 - Exemplo de uma sequência bitonic  
 
Fonte: Adaptado de MULLAPUDI (2014) 
 
O algoritmo Bitonic Sort é dividido em duas etapas: na primeira etapa a sequência de 
entrada é transformada em uma sequência bitonic e na segunda a sequência bitonic é ordenada 
de forma crescente. Ademais, esse algoritmo pode ser dividido em várias etapas, sendo que cada 
etapa é composta por log2 𝑋 passos, em que X corresponde ao número de elementos da 
subsequência. Para uma sequência de entrada [3 7 4 8 6 2 1 5], de 8 elementos, M corresponderia 
a 2 elementos para o primeiro estágio, 4 elementos para o segundo estágio e 8 elementos para o 
terceiro estágio (BATCHER, 1968; PETERS et al., 2012). 
 
 
 


175 
 
 
Figura 55 - Estágios do processo de ordenação do Bitonic Sort  
 
Fonte: Adaptado de MULLAPUDI (2014) 
 
A Figura 55 apresenta os três estágios do processo de ordenação com Bitonic Sort. No 
primeiro estágio, o algoritmo divide a sequência [3 7 4 8 6 2 1 5] em 4 pares de subsequências 
([3 7], [4 8], [6 2], [1 5]), ordena essas subsequências de forma crescente e decrescente 
(alternando entre os pares) e mescla em 2 subsequências ([3 7 8 4], [2 6 5 1]) do tipo bitonic de 
4 elementos (BATCHER, 1968; PETERS et al., 2012). 
No segundo estágio, estas 2 subsequências são novamente ordenadas, de forma 
crescente e decrescente, e mescladas formando uma sequência do tipo bitonic de 8 elementos, 
conforme a Figura 54. Por fim, no terceiro estágio, a sequência bitonic é ordenada em apenas 
uma direção, resultando em uma sequência crescente BATCHER, 1968; PETERS et al., 2012). 
Os Códigos 51 e 52 apresentam parte da implementação do algoritmo Bitonic Sort 
escrita em LingPON 2.0. Basicamente, a implementação foi dividida em dois FBE: (a) o FBE 
Main; e (b) o FBE Comparator. O Código 51 apresenta a implementação do FBE Main, 
responsável pela maior parte das Rules para a lógica do Bitonic Sort. 
 
Código 51 - Trecho do FBE Main em LingPON 2.0 para Bitonic Sort 
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
fbe Main 
    private Integer atCounter = 0 
    private Integer atStartAsc = 0 
    private Integer atStartDesc = 0 
    private Comparator compA 
    private Integer[8] atVec 
    private Boolean atMergeControl = false 
    private Boolean atCounterUp = false 
 
 
    private method mtBitonicSort 
        params 
            Integer direction 
            Integer start 
        end_params 
        code NAMESPACES 
            int k = instance::main::at::atCounter::value/2; 


176 
 
 
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
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
48 
49 
50 
51 
52 
53 
54 
55 
56 
57 
58 
59 
60 
61 
62 
63 
64 
65 
66 
67 
68 
69 
70 
71 
72 
73 
74 
75 
76 
77 
            if (k > 1 && instance::main::at::atCounterUp::value == false){ 
                instance::main::at::atCounter::setValue( 
                              instance::main::at::atCounter::value / 2); 
            } 
            instance::main::at::atStartDesc::setValue( 
                           instance::main::at::atStartAsc::value +   
                           instance::main::at::atCounter::value); 
            if (direction >= 0){ 
 
          method::main::mtMerge::mtMerge(start, k, direction); 
            } 
        end_code 
    end_method 
 
    private method mtMerge 
        params 
            Integer start 
            Integer k 
            Integer direction 
        end_params 
        code NAMESPACES 
            for (int i = start; i < start + k; i++) { 
                instance::main::compA::at::atX1::setValue( 
                          BitonicSortAPI::getValueVector(i)); 
                instance::main::compA::at::atX2::setValue( 
                          BitonicSortAPI::getValueVector(i + k)); 
                instance::main::compA::at::atDirection::setValue( 
                          direction); 
                instance::main::compA::at::atSwapControl::setValue(true); 
                BitonicSortAPI::setValueVector(  
                          i, instance::main::compA::at::atX1::value); 
                BitonicSortAPI::setValueVector( 
                          i + k, instance::main::compA::at::atX2::value); 
                instance::main::compA::at::atSwapControl::setValue(false); 
            } 
            if (k > 1) { 
                int aux = k / 2; 
                mtMerge(start, aux, direction); 
                mtMerge(start + aux, aux, direction);  
            } 
        end_code 
    end_method 
. . . 
    rule rlBitonicSortRecursive 
        condition 
            premise prCounterRecursive 
                this.atCounter > 2 
            end_premise 
            and 
            premise prMergeControlRecursive 
                this.atMergeControl == false 
            end_premise 
        end_condition 
        action 
            instigation 
                call this.mtBitonicSort 
                    params 
                        -1 
 
           0 
                    end_params 
                end_call 
            end_instigation 


177 
 
 
78 
79 
80 
81 
82 
83 
84 
85 
        end_action 
    end_rule 
. . . 
    main 
        this.atVec = [3,7,4,8,6,2,1,5] 
        this.atCounter = 8 
    end_main 
end_fbe 
Fonte: Autoria própria 
 
 
O Código 52, por sua vez, apresenta a implementação do FBE Comparator, no qual são 
executadas Rules para verificações relativas à comparação entre os elementos da sequência a ser 
ordenada. 
 
Código 52 - Trecho do FBE Comparator  em LingPON 2.0 para Bitonic Sort 
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
37 
38 
39 
40 
41 
42 
43 
fbe Comparator 
    private Integer atX1 = 0 
    private Integer atX2 = 0 
    private Integer atDirection = 0 
    private Boolean atSwapControl = false  
 
    private method mtSwap 
        params 
            Integer newValueX1 
            Integer newValueX2 
        end_params 
        code NAMESPACES 
            this.atSwapControl = 0; 
            this.atX1 = newValueX1; 
            this.atX2 = newValueX2; 
        end_code 
    end_method 
 
 
    rule rlAscending 
        condition 
            premise prX1GreaterThanX2 
                this.atX1 > this.atX2 
            end_premise 
            and 
            premise prAscending 
                this.atDirection == 1 
            end_premise 
            and 
            premise prControl 
                this.atSwapControl == 1 
            end_premise 
        end_condition 
        action sequential 
            instigation 
                call this.mtSwap 
                    params 
                        this.atX2 
                        this.atX1 
                    end_params 
                end_call 
            end_instigation 
        end_action 
    end_rule 
 


178 
 
 
44 
45 
… 
end_fbe 
Fonte: Autoria própria 
 
A próxima seção apresenta os resultados das implementações do Bitonic Sort geradas 
pelo NPCPP 2.0, em ambos os casos de com e sem o conceito de Premissa Única, bem como os 
resultados obtidos com implementações em C++ OO e Python. 
 
3.3.3.2 Testes e Resultados 
A aplicação Bitonic Sort foi testada também em Python, além do C++ OO usual e da 
implementação em NPCPP 2.08. Foram executadas ordenações para sequências de 8, 16, 32 e 
64 elementos e para o cálculo do tempo de execução, foi considerado apenas o tempo da 
execução das funções referentes à ordenação (não considerando a inicialização da estrutura em 
si). Os testes foram executados em um ambiente sujeito a variações de preempção de sistema 
operacional e afins, Linux Mint 19 (64 bits) em uma máquina com 12 GB RAM, Intel Core i3 – 
7100 CPU @ 3.90 GHz. Os resultados foram obtidos em tempo de execução, em milissegundos, 
e correspondem à mediana dos valores obtidos de 20 execuções.  A Figura 56 apresenta a 
comparação dos resultados do tempo de execução, em microssegundos.  
 
Figura 56 - Resultado comparativo para o Bitonic Sort 
 
Fonte: Autoria própria 
 
                                                          
8 Da mesma maneira que nos testes do Simulador CTA, o Bitonic Sort não foi aplicado para 
o NPCPP 1.0, por conta das diversas inconsistências que esta implementação apresenta, dificultando 
os experimentos. 
8
15
31
67
27
80,25
224,8
471,6
44
56,5
106,5
267
8
16
32
64
TEMPO DE EXECUÇÃO 
(MICROSSEGUNDOS)
NÚMERO DE ELEMENTOS DA SEQUÊNCIA BITONIC
COMPARAÇÃO DE DESEMPENHO - BITONIC SORT
C++ OO usual
Python
NPCPP 2.0


179 
 
 
Conforme os resultados apresentados, a implementação C++ OO usual foi a que obteve 
o melhor desempenho de execução, seguido do NPCPP 2.0. Pode-se afirmar que os resultados 
confirmaram as expectativas esperadas em relação ao desempenho do NPCPP 2.0. Uma vez que 
um dos pontos fortes do PON está em eliminar as redundâncias e, o algoritmo Bitonic Sort 
apresenta existência irrelevante de redundâncias, é esperado que o PON não desempenhe tão 
bem quanto na aplicação de Redes de Sensores.  
Ainda assim, o NPCPP 2.0 apresentou um desempenho de execução consideravelmente 
melhor que o Python, na maioria dos casos. Como mostra a Figura 56, no caso de ordenação 
com 8 elementos, o NPCPP 2.0 foi o que obteve o tempo de execução mais alto. No entanto, a 
partir de 16 elementos aumentou, o desempenho do NPCPP 2.0 se apresentou melhor em relação 
ao Python. O fato de apenas no primeiro caso o NPCPP 2.0 apresentar um desempenho inferior 
pode ser decorrente das preempções, inclusive considerando que os tempos de execuções neste 
caso são extremamente baixos. 
 
Foi calculado o desvio padrão para todos os casos, apresentando um valor de até 33% do 
valor da mediana, caso extremo referente ao cenário de 8 elementos na sequência. Para validar 
melhor o experimento, foram realizados, então, esses mesmos testes em uma máquina virtual 
EC2 disponibilizada pela AWS (Amazon Web Service) Ubuntu Server 18.04 LTS, com 
processador Intel Xeon E5-2676 v3 @ 2.40GHz. Os resultados obtidos na EC2 estão 
representados pela Figuras 57. 
 
Figura 57 - Resultado comparativo para o Bitonic Sort na EC2 da AWS 
 
Fonte: Autoria própria 
 
3
5
9,5
20
34,49995
74
177
430,49995
20
47
111
270
8
16
32
64
TEMPO DE EXECUÇÃO (MICROSSEGUNDOS)
NÚMERO DE ELEMENTOS DA SEQUÊNCIA BITONIC
COMPARAÇÃO DE DESEMPENHO - BITONIC SORT
C++
Python
NPCPP 2.0


180 
 
 
Da mesma forma que ocorreu com o experimento de Rede de Sensores, o teste realizado 
na máquina virtual da AWS confirma os resultados obtidos anteriormente no ambiente com 
preempções, sendo que a implementação em C++ OO obteve o melhor desempenho, e o NPCPP 
2.0, apesar de apresentar um tempo de execução maior (de até 12.5 vezes mais) que o C++, 
obteve consideravelmente um melhor desempenho que a implementação em Python, uma 
linguagem de programação que também traz o desenvolvimento em alto nível. Além disso para 
todos os casos dos experimentos executados no ambiente da AWS foi calculado o desvio padrão, 
obtendo um valor máximo de 8% do valor da mediana. 
Além do valor do desvio padrão, outra diferença entre os resultados obtidos no ambiente 
preemptivo e na máquina da AWS é que no segundo experimento, o comportamento do NPCPP 
2.0 se assemelha ao do C++ OO: à medida que o número de elementos aumenta, o tempo de 
execução aumenta de forma proporcional; com 16 elementos, por exemplo, o tempo de execução 
para o NPCPP 2.0 é 2,35x ao do tempo obtido com 8 elementos, assim como com 32 elementos, 
o tempo de execução desse compilador é 2,36x ao tempo obtido com 16 elementos. Ou seja, o 
aumento é constante. Em contrapartida, no primeiro experimento, o NPCPP 2.0 apresenta uma 
elevação consideravelmente maior no tempo de execução à medida que o número de elemento 
aumenta. Isso possivelmente se deve à presença de preempções do ambiente de teste. A 
implementação em C++ OO, por sua vez, apresenta nos dois experimentos um aumento 
constante e proporcional ao número de elementos: se dobra o número de elementos, praticamente 
dobra também o tempo de execução. Porém, apenas com esses experimentos realizados ainda é 
prematuro concluir que o NPCPP 2.0 apresente um comportamento semelhante à da 
implementação em C++ OO. Para averiguar isto, é necessário que sejam realizados mais 
experimentos, considerando, inclusive e principalmente, um número mais elevado de elementos 
da sequência. 
Mesmo que o NPCPP 2.0 não apresente a melhor performance neste experimento, este 
tipo de teste é importante para analisar e confirmar o comportamento do compilador e do próprio 
PON em diferentes situações e tipos de aplicação. 
 
3.3.4 Random Forest 
Esta seção apresenta a aplicação Random Forest, uma implementação mais complexa 
que as anteriores e que também foi alvo de experimentos com NPCPP 2.0, cujos resultados 
foram comparados com implementações em C++ OO e em Python. 


181 
 
 
3.3.4.1 Descrição do Random Forest 
A aplicação Random Forest basicamente consiste em um algoritmo de aprendizado de 
máquina (machine learning), muto utilizado para fins de classificação e regressão (NEVES, 
2021). Neste algoritmo, são criadas diversas árvores de decisão (decision trees). as quais são 
treinadas individualmente, para estabelecerem regras de tomada de decisão, e combinadas a fim 
de obter um resultado com o menor erro de classificação e/ou regressão. A Figura 58 apresenta 
a estrutura das árvores de decisão independentes do Random Forest. 
 
Figura 58 - Estrutura das árvores de decisão do Random Forest 
 
Fonte: PORDEUS (2020b) 
 
A estrutura das árvores de decisão, ilustrada pela Figura 58, se assemelha a um 
fluxograma: em cada “ponto” é verificada uma condição; se esta for atendida, o fluxo segue por 
um ramo, e caso contrário, por outro ramo. Este caminho sempre leva a uma nova condição, até 
a finalização da árvore. O percorrimento em cada árvore é realizado separadamente, viabilizando 
a execução de maneira paralela. Ao final da execução de todas as árvores os resultados são 
combinados para todo o conjunto (CRIMINISI; SHOTTON; KONUKOGLU, 2011; NEVES, 
2021). 
O fato de as árvores de decisão serem constituídas por diversas condições significa que 
o algoritmo Random Forest é composto por uma série de expressões lógicas do tipo if-else. Desta 
maneira, este algoritmo implementado em LingPON permitiria a eliminação de redundâncias 
estruturais e temporais, permitindo também a paralelização da execução de árvores (PORDEUS, 
2020b, NEVES, 2021). 
Para a implementação em PON, Pordeus (2020b) desenvolveu um algoritmo que 
possibilita a geração de códigos em LingPON 2.0, além de gerar para C do PP. Tais códigos 
resultantes são baseados em árvores de decisão geradas com o auxílio da biblioteca scikit-learn 


182 
 
 
da linguagem Python e contemplam apenas a sua utilização para fins de classificação. O Código 
53 apresenta trechos do algoritmo em LingPON 2.0. 
 
Código 53 - Trecho da implementação do Random Forest em LingPON 2.0 
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
37 
38 
39 
40 
41 
42 
43 
44 
45 
46 
47 
48 
49 
50 
51 
52 
53 
fbe Forest 
    private Integer attr0 = 0 
    private Integer attr1 = 0 
    private Integer attr2 = 0 
    private Integer attr3 = 0 
    private Integer count_setosa = 0 
    private Integer count_versicolor = 0 
    private Integer count_virginica = 0 
    private boolean trigger_tree_0 = false 
    private boolean trigger_tree_1 = false 
 
    private method mtCountsetosa 
        code NAMESPACES 
            this.count_setosa = this.count_setosa + 1; 
        end_code 
    end_method 
 
    private method mtTrigger0 
        assignment 
            this.trigger_tree_0 = true 
        end_assignment 
    end_method 
 
    private method mtTrigger1 
        assignment 
            this.trigger_tree_1 = true 
        end_assignment 
    end_method 
 
. . . 
 
    rule rlTree_0_1 
        condition 
            premise pr_3_le_75  
                this.attr3 <= 75  
            end_premise  
            and 
            premise prTrigger0  
                this.trigger_tree_0 == true  
            end_premise 
 
 
end_condition 
 
 
action 
                instigation parallel 
                    call this.mtCountsetosa 
                    call this.mtTrigger1 
                    call this.mtTrigger0 
            end_instigation 
        end_action 
    end_rule 
 
. . . 
 
end_fbe 
 
Fonte: PORDEUS (2020) 
 
 
 


183 
 
 
 
O Código 53 mostra na linha 32 a definição de uma Rule. Na implementação em PON, 
as Rules são construídas de forma que possibilita que suas respectivas Premises avaliem o valor 
de Attributes, que representam os dados de entrada da classificação, com relação aos valores 
atribuídos durante o processo de treinamento das árvores (NEVES, 2021).  
Como a implementação do Random Forest possibilita a utilização de um número variável 
de árvores de decisão, o algoritmo desenvolvido por Pordeus (2020b) foi implementado de forma 
que também é possível gerar código para diferentes números de árvores. Neste experimento 
foram utilizados os valores de 1, 10, 20, 50, 100 e 200 árvores para o dataset conhecido como 
Iris. No Quadro 17 é possível observar os números de elementos necessários para a construção 
de cada versão do classificador para os diferentes números de árvores 
 
 
Quadro 17 - Relação de número de elementos do PON criados de acordo com o número de árvores 
Dataset Iris 
 Número de árvores 
1 
10 
20 
50 
100 
200 
Attributes 
7 
34 
64 
154 
304 
604 
Premises 
8 
39 
56 
80 
93 
114 
Rules 
9 
90 
173 
437 
839 
1690 
Methods 
6 
60 
120 
300 
600 
1200 
Fonte: PORDEUS (2020b) 
 
 
Na próxima seção são apresentados o experimento e as comparações dos resultados de 
desempenho obtidos para o algoritmo do Random Forest. 
 
3.3.4.2 Testes e Resultados 
Conforme citado no início da subseção 3.3.4, a aplicação Random Forest foi testada na 
implementação gerada pelo NPCPP 2.0, em Python, além do C do PP9. Os experimentos foram 
realizados para os números de árvores de decisão conforme o Quadro 16 e executados direto na 
máquina da Amazon Web Service EC2 Ubuntu Server 18.04 LTS, com processador Intel Xeon 
E5-2676 v3 @ 2.40GHz. A Figura 59 representa a comparação desses resultados (mediana dos 
valores do tempo de execução para 20 repetições), em microssegundos.  
 
 
 
 
 
                                                          
9 O Random Forest não foi aplicado para o NPCPP 1.0, por conta das diversas inconsistências que esta 
implementação apresenta, dificultando os experimentos. 


184 
 
 
Figura 59 - Resultado comparativo para o Random Forest na EC2 da AWS 
 
Fonte: Autoria própria 
 
O desvio padrão foi calculado para todos os casos e o valor máximo obtido corresponde 
a cerca de 9% do valor da mediana. Observando os resultados apresentados, a implementação C 
foi a que obteve o melhor desempenho de execução, seguido do NPCPP 2.0 e, por último, o 
Python. Apesar de o algoritmo Random Forest ser composto essencialmente pela expressão 
lógica if-else, a eliminação de redundâncias não foi o suficiente para o NPCPP 2.0 apresentar 
um desempenho melhor que a implementação em C. Isto ainda pode ocorrer por algum ruído do 
sistema. O experimento é composto por quatro entradas e foi testado de maneira que elas variem 
de maneira aleatória. Uma outra maneira de testar o comportamento do PON para essa aplicação 
seria controlar para que apenas uma das entradas tenha seu valor alterado. Isto permitiria que o 
número de notificações realizadas na implementação em PON diminuiria, melhorando assim o 
tempo de execução. 
 
3.4 
Gerador de Código C++ Notificante Orientado a Namespaces Multithreading para 
LingPON 2.0 (NPCPP 2.0 Multithreading) 
Conforme mencionado anteriormente, Martini (2018) adaptou o gerador de código 
NPCCP 1.0 (i.e., C++ notificante modular orientado a namespaces da versão LingPON 1.0) 
para suportar multithreading e, com isso, foi possível verificar a viabilidade de paralelização 
dos Methods, cf. detalhado na Seção 2.4.3 no Capítulo 2 (MARTINI et al., 2021). Seguindo a 
4
14
25
68
100,5
206
536,2085
1736,12
3004,48
6623,465
12837,5
24962,45
19,5
115,5
269,5
1124,5
2597
7942,5
1
10
20
50
100
200
TEMPO DE EXECUÇÃO (MICROSSEGUNDOS)
NÚMERO DE ÁRVORES
COMPARAÇÃO DE DESEMPENHO - RANDOM FOREST
C
Python
NPCPP 2.0


185 
 
 
mesma abordagem foi realizada uma adaptação similar para o NPCPP 2.0 e utilizadas as 
bibliotecas PThread e Thread Pooling como tecnologias de multithreads.  
A aplicação utilizada para auxiliar na implementação de multithreads foi o programa 
Eletronicgate (portão eletrônico), que simula o processo de abrir e fechar de um portão 
eletrônico, implementado em LingPON 2.0. O Código 54 mostra uma Rule do programa fonte, 
que apresenta Methods nos quais serão implementados multithreads.  
 
Código 54 - Rule do Eletronicgate que contém Methods nos quais serão  
implementados multithreads 
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
rule rlClosingGate 
    condition 
        premise prRemoteControlClosingOn  
          event.atEventState == 1  
        end_premise 
        and 
        premise prGateIsOpened  
          gate.atGateState == 1 
        end_premise 
    end_condition 
    action  
      instigation  
        call event.mtReset(); 
        call gate.mtClosed(); 
      end_instigation 
    end_action 
end_rule 
Fonte: Autoria própria 
 
Como detalhado no capítulo anterior, as partes léxica e sintática do compilador são 
utilizadas as ferramentas Flex e Bison, respectivamente. Isto relembrado, foi ainda igualmente 
necessário incluir na parte sintática os targets correspondentes aos geradores de código 
multithreading, como é mostrado pelo Código 55.  
 
Código 55 - Inclusão dos targets dos gerados de código multithreading no Bison.y 
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
target   : CODE_GENERATION_EXAMPLE { 
                    $$ = graph->createTarget( 
                               Target::CODE_GENERATION_EXAMPLE_TARGET); 
            } 
            | NAMESPACES { 
                    $$ = graph->createTarget( 
                               Target::NAMESPACES_TARGET); 
            } 
            | NAMESPACES_PTHREAD { 
                    $$ = graph->createTarget( 
                               Target::NAMESPACES_PTHREAD_TARGET); 
            } 
 
     | NAMESPACES_TPOOL { 
                    $$ = graph->createTarget( 
                               Target::NAMESPACES_TPOOL_TARGET); 
            }; 
Fonte: Autoria própria 


186 
 
 
 
Conforme o Código 55 apresenta, as linhas 9 a 15 representam a inclusão no Bison.y 
do target referente ao NPCPP 2.0 multithreading implementado com a tecnologia pThread, 
enquanto as linhas 10 a 12 representam a inclusão do target do gerador de código implementado 
com a tecnologia Thread Pooling. 
Neste trabalho, as threads foram implementadas para serem aplicadas apenas aos 
Methods. Para tal, foram criadas a implementação das classes NamespacesPThreadCompiler e 
NamespacesTPoolCompiler, as quais são derivadas da classe NamespacesCompiler do 
framework do Grafo PON e correspondem aos geradores de código implementados com 
PThread e ThreadPooling, respectivamente. Neste contexto, o Código 56 apresenta exatamente 
o 
ponto 
no 
qual 
foram 
adicionadas 
as 
implementações 
das 
threads 
em 
NamespacesPThreadCompiler, cuja implementação é apresentada na íntegra pelo Apêndice F. 
 
Código 56 - Implementação da criação de PThreads para o NPCPP 2.0 
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
else { 
    char buf[3]; 
    sprintf(buf, "%i", subConds);   
 
    if(methodCallInc.compare("") != 0)  
        methodCallInc += "\t\t\t\t\t"; 
    if(methodCallDec.compare("") != 0) 
        methodCallDec += "\t\t\t\t\t"; 
    methodCallInc += "while(rule::" + instName + "::" + ruleName + 
                     "::inc_running" + buf + " == 1) {};\n"; 
    methodCallDec += "while(rule::" + instName + "::" + ruleName +  
                     "::dec_running" + buf + " == 1) {};\n"; 
     
    if(methodCallInc.compare("") != 0)  
        methodCallInc += "\t\t\t\t\t"; 
    if(methodCallDec.compare("") != 0)  
        methodCallDec += "\t\t\t\t\t"; 
    methodCallInc += "pthread_create( 
                      &id" + std::to_string(subConditionCounter) +   
                     ", NULL, &rule::" + instName + "::" + ruleName +   
                     "::inc" + buf + ", NULL);\n"; 
    methodCallDec += "pthread_create( 
                      &id" + std::to_string(subConditionCounter+1) + 
                     ", NULL, &rule::" + instName + "::" + ruleName +  
                     "::dec" + buf + ", NULL);\n"; 
} 
Fonte: Autoria própria 
 
O trecho de código apresentado pelo Código 56 faz parte do método generatePremise() 
do gerador de código. As linhas 5 a 25 apresentam as implementações adicionadas para a 
criação das threads utilizando PThreads. Estas são criadas por meio da declaração 
pthread_create e, antes de uma nova thread ser criada, é verificado se o processo de outra thread 


187 
 
 
aberta  no mesmo método já terminou. Isto é feito por meio de um semáforo, garantindo a 
consistência de dados. O Código 57 apresenta outro trecho, do mesmo método do Código 56, 
que ilustra a adição de semáforos utilizados, representados por inc_running e dec_running.  
 
Código 57 - Criação de semáforos para a implementação de PThreads 
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
// implementação dos métodos 
fileH << tab << "\t\t\textern bool inc_running;" << std::endl; 
fileH << tab << "\t\t\textern bool dec_running;" << std::endl; 
fileH << tab << "\t\t\textern void* inc(void* arg);"  
             << std::endl; 
fileH << tab << "\t\t\textern void* dec(void* arg);"  
             << std::endl; 
fileCPP << tab << "\t\t\tbool inc_running = 0;" << std::endl; 
fileCPP << tab << "\t\t\tbool dec_running = 0;" << std::endl; 
fileCPP << tab << "\t\t\tvoid* inc(void* arg){" << std::endl; 
fileCPP << tab << "\t\t\t\tinc_running = 1;" << std::endl; 
fileCPP << tab << "\t\t\t\tcount++;" << std::endl; 
fileCPP << tab << "\t\t\t\tif (count " << expressionConjunction  
               << " " << numPremises << ") {" << std::endl; 
 
//instigations             
generateInstigation(fileCPP, fileH, instance, rule, level);       
 
fileCPP << tab << "\t\t\t\t}" << std::endl; 
fileCPP << tab << "\t\t\t\tinc_running = 0;" << std::endl; 
fileCPP << tab << "\t\t\t}" << std::endl; 
fileCPP << tab << "\t\t\tvoid* dec(void* arg){" << std::endl; 
fileCPP << tab << "\t\t\t\tdec_running = 1;" << std::endl; 
fileCPP << tab << "\t\t\t\tcount--;" << std::endl; 
fileCPP << tab << "\t\t\t\tdec_running = 0;" << std::endl; 
fileCPP << tab << "\t\t\t}" << std::endl; 
fileCPP << tab << "\t\t}" << std::endl; 
fileH << tab << "\t\t}" << std::endl; 
Fonte: Autoria própria 
 
O código resultante da compilação do NPCPP 2.0 multithreading utilizando PThreads, 
para a aplicação Eletronicgate em LingPON 2.0 (Código 53), é apresentado pelo Código 58.  
 
Código 58 - Código gerado com PThreads resultante da compilação a partir de LingPON 2.0 
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
namespace premise{ 
    namespace main{ 
        namespace prGateIsOpened{ 
            bool state = false; 
            int cpy1st, cpy2nd; 
            pthread_t id0, id1;  
            void init(){ 
                cpy1st = 0; 
                cpy2nd = 1; 
                if (cpy1st == cpy2nd){ 
                    state = true; 
                    while (rule::main::rlClosingGate:: 
                           inc_running == 1) {} 
                    pthread_create(&id0,NULL, 
                           & rule::main::rlClosingGate::inc,NULL); 
                } 
            }  


188 
 
 
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
            void compare(){ 
                if(cpy1st == cpy2nd){ 
                    if(state == false){ 
                        state = true; 
                        while (rule::main::rlClosingGate:: 
                               inc_running == 1) {} 
                        pthread_create(&id0,NULL,& rule::main:: 
                               rlClosingGate::inc,NULL); 
                    } 
                }else{ 
                    if(state == true){ 
                        state = false; 
                        while (rule::main::rlClosingGate:: 
                               dec_running == 1) {} 
                        pthread_create(&id1,NULL,& rule::main:: 
                               rlClosingGate::dec,NULL); 
                    } 
                } 
            }      
Fonte: Autoria própria 
 
A criação de semáforos necessários para implementação dessa tecnologia de 
multithreading está destacada no Código 59. 
 
Código 59 - Código gerado com PThreads, e utilização de semáforos 
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
namespace rule{ 
    namespace main{ 
        namespace rlClosingGate{ 
            int count = 0; 
            bool inc_running = 0; 
            bool dec_running = 0; 
            void closingGate(){ 
                FILE* fp = NULL; 
                fp = fopen(“Arquivo.txt”, “a”); 
                if (fp != NULL){ 
                    fprintf(fp, “Fechando o portão”); 
                    for (int i = 0; i <= NUM_LOOPS; i++){ 
                        fprintf(fp, “%d ”, i); 
                    } 
                    fprintf(fp, “\n”); 
                    fprintf(fp, “Fechado\n”); 
                } 
                fclose(fp); 
            }  
            void* inc(void* arg){ 
                inc_running = 1; 
                count++; 
                if(count == 2){ 
                    closingGate(); 
                    method::main::event::mtReset::mtReset(); 
                    method::main::gate::mtClosed::mtClosed(); 
                } 
                inc_running = 0; 
            } 
            void* dec(void* arg){ 
                dec_running = 1; 
                count--; 
                dec_running = 0; 


189 
 
 
34 
35 
36 
37 
            } 
        }    
    } 
}   
Fonte: Autoria própria 
 
O Código 60, por sua vez, apresenta a implementação de multithreads via tecnologia 
Thread Pooling no método generatePremise() da classe NamespacesTPoolCompiler do 
respectivo gerador de código. A implementação completa desta classe é apresentada no 
Apêndice G. 
 
Código 60 - Alteração no NPCPP 2.0 para a criação de Thread Pooling 
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
else { 
        char buf[3];  
        sprintf(buf, "%i", subConds);  
 
        /*methodCallInc = methodCallInc + buf; 
        methodCallDec = methodCallDec + buf;*/   
 
        if(methodCallInc.compare("") != 0)  
                methodCallInc += "\t\t\t\t\t"; 
        if(methodCallDec.compare("") != 0)  
                methodCallDec += "\t\t\t\t\t"; 
        methodCallInc += "thpool_add_work(thpool1, &rule::" +  
                         instName + "::" + ruleName + "::inc" +  
                         buf + ", NULL);\n"; 
        methodCallDec += "thpool_add_work(thpool2, &rule::" +  
                         instName + "::" + ruleName + "::dec" +  
                         buf + ", NULL);\n"; 
    } 
     
    fileH << tab << "\t\t\textern bool state;" << std::endl; 
    fileH << tab << "\t\t\textern " << cmpAttType  
          << " cpy1st, cpy2nd;" << std::endl; 
    fileH << tab << "\t\t\textern threadpool thpool1;" << std::endl; 
Fonte: Autoria própria 
 
As Thread Pooling são adicionadas via declaração “thpool_add work”, como apresenta 
o Código 60. Esse tipo de tecnologia de multithread possui um próprio gerenciamento, que 
dispensa a necessidade de semáforos: assim que um thread pool finaliza a sua tarefa, ele retorna 
a uma fila de threads em espera. Ou seja, as threads podem ser reutilizadas, o que economiza 
tempo de processamento em não precisar criar novas threads para cada tarefa. O Código 61 
apresenta o código resultante da geração de código pelo NPCPP 2.0 da versão Thread Pooling 
referente ao código em LingPON 2.0 da aplicação Eletronicgate (Código 54). 
 
Código 61 - Código gerado com Thread Pooling resultante da compilação a partir de LingPON 2.0 
1 
2 
3 
4 
namespace premise{ 
    namespace main{ 
        namespace prGateIsOpened{ 
            bool state = false; 


190 
 
 
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
            int cpy1st, cpy2nd; 
            threadpool thpool1;   
            void init(){ 
                cpy1st = 0; 
                cpy2nd = 1; 
                thpool1 = thpool_init(1); 
 
                if (cpy1st == cpy2nd){ 
                    state = true; 
                    thpool_add_work (thpool1,  
                          rule::main::rlClosingGate::inc, NULL); 
                    thpool_wait(thpool1); 
                } 
            }  
            void compare(){ 
                if(cpy1st == cpy2nd){ 
                    if(state == false){ 
                        state = true; 
                        thpool_add_work (thpool1,  
                             rule::main::rlClosingGate::inc, NULL); 
                        thpool_wait(thpool1); 
                    } 
                }else{ 
                    if(state == true){ 
                        state = false; 
                        thpool_add_work (thpool1,  
                             rule::main::rlClosingGate::dec, NULL); 
                        thpool_wait(thpool1); 
                    } 
                } 
            }      
Fonte: Autoria própria 
 
Para a realização dos testes, as implementações foram executadas em um ambiente 
sujeito a variações de preempção de sistema operacional e afins, Linux Mint 19 (64 bits) em uma 
máquina com 12 GB RAM, Intel Core i3 – 7100 CPU @ 3.90 GHz, contendo 2 núcleos com 4 
threads.    
Como a aplicação Eletronicgate é um sistema simples, foi adicionado uma 
implementação a mais a cada método que é chamado a fim de aumentar a carga de 
processamento. Tal implementação corresponde à gravação de arquivo, no qual são gravadas a 
ação do portão eletrônico (fechamento ou abertura do portão). Ainda, para aumentar mais essa 
carga, foi adicionado um laço (loop) do tipo “for”. O Código 62 apresenta a implementação do 
método closingGate() (nas linhas 8 a 20), que contém em seu escopo um loop e a gravação de 
um arquivo, no qual são gravadas a ação do portão eletrônico (neste caso corresponde a fechar 
o portão) e a iteração do loop. 
 
Código 62 - Método ClosingGate() com implementações para aumentar a carga do processamento 
1 
2 
namespace rule{ 
    namespace main{ 


191 
 
 
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
        namespace rlClosingGate{ 
            int count = 0; 
            bool inc_running = 0; 
            bool dec_running = 0; 
 
            void closingGate(){ 
                FILE* fp = NULL; 
                fp = fopen(“Arquivo.txt”, “a”); 
                if (fp != NULL){ 
                    fprintf(fp, “Fechando o portão”); 
                    for (int i = 0; i <= NUM_LOOPS; i++){ 
                        fprintf(fp, “%d ”, i); 
                    } 
                    fprintf(fp, “\n”); 
                    fprintf(fp, “Fechado\n”); 
                } 
                fclose(fp); 
            }  
. . . 
} 
Fonte: Autoria própria 
 
 
O sistema foi executado nos seguintes números de repetições: 5000, 50000 e 500000, 
sendo que para cada amostragem execução foi realizada diversas vezes. Os resultados das 
implementações com threads foram comparados com os resultados obtidos para a 
implementação do NPCPP 2.0 monocore.  As comparações dos resultados, que apresenta em 
tempo de execução em milissegundos, são verificados pela Figura 60.  
 
Figura 60 - Gráfico com resultados do Eletronicgate nas versões  
single-threaded, PThread e Thread Pooling 
 
Fonte: Autoria própria 
 
0,027551
0,341204
3,105136
0,020657
0,230713
0,904298
0,015497
0,055971
0,437821
5000
50000
500000
TEMPO DE EXECUÇÃO (MS)
CICLOS DE REPETIÇÕES
RESULTADO COMPARATIVO COM MULTITHREADING
Monothread
Multithread – Pthread
Multithread – Thread Pooling


192 
 
 
Com base nos dados da Figura 60, é possível observar que o desempenho do código 
implementado com multithreads é consideravelmente melhor que a versão single-threaded. 
Ainda, dentre as versões multithreading, o sistema com Thread Pooling obteve o melhor 
resultado. Por fim, é pertinente ressaltar que o projeto Eletronicgate pode ser considerado como 
um projeto sem muita complexidade, o que significa que em uma aplicação grande, a diferença 
nos desempenhos possivelmente será ainda maior. 
 
3.5 
Considerações 
Este trabalho visa apresentar o desenvolvimento, no âmbito da Tecnologia LingPON 
2.0, do compilador para o target C++ Notificante Modular orientado a Namespaces, conhecido 
como NPCPP 2.0, uma materialização do PON que viabiliza duas das três propriedades 
fundamentais do paradigma.  
Conforme estudos precedentes, foi identificado que o compilador NPCPP 1.0 obteve 
um dos melhores desempenhos no tocante a Tecnologia LingPON 1.X, em termos de plataforma 
Von Neumann. Apesar de apresentar este aspecto relevante, o NPCPP 1.0 se trata de uma versão 
prototipal, por conta de uma série de inconsistências que apresentava em seu funcionamento. 
Em decorrência disso, há dificuldade para realizar experimentos com aplicações mais complexas 
e, portanto, essa versão do compilador foi testada em apenas um único experimento simples 
denominado Eletronicgate, o qual não se apresenta como um bom exemplo de benchmark. 
Ainda, uma vez que a Tecnologia LingPON evoluiu para a versão 2.0, apresentando inclusive 
implementação de novos conceitos na LingPON e uma efetiva modificação do Grafo PON, 
naturalmente fazia-se necessário inclusive realizar adaptações e novas validações para os 
geradores de códigos precedentes mais pertinentes, nos quais naturalmente se encontra o NPCPP 
1.0. 
Neste sentido, foi construído um novo compilador NPCPP para a versão 2.0 da 
LingPON, denominado de NPCPP 2.0. Algumas adaptações foram necessárias para contemplar 
os novos conceitos implementados (e.g., organização holônica), conforme foi apresentado no 
decorrer do capítulo. Para validar o NPCPP 2.0, foram realizados experimentos com diferentes 
tipos de aplicações para analisar o comportamento do compilador em diferentes contextos.  
A primeira aplicação utilizada para validar a implementação foi a Rede de Sensores, 
um programa que apresenta uma complexidade não muito alta, mas o suficiente para auxiliar 
nessa primeira etapa de construção do compilador em função de suas redundâncias temporais e 


193 
 
 
estruturais. O sistema foi testado para quatro cenários diferentes nos quais são aprovadas 10%, 
40%, 70% e 100% das Rules. O resultado foi comparado para com implementações equivalentes 
para a versão 1.0 do NPCPP e em C++ OO PI. Eis que o NPCPP 2.0 foi a implementação que 
obteve o melhor desempenho de execução, seguido do NPCPP 1.0.  Considerando que a Rede 
de Sensores é uma aplicação com presenças de redundâncias temporais e estruturais, este 
resultado demonstra a capacidade do PON em termos de eliminar tais redundâncias de 
programas, o que resulta em uma melhora de desempenho quando em implementações PON.  
Nesta fase de construção do compilador foram identificadas e aplicadas melhorias de 
imperfeições que foram herdadas da versão prototipal 1.0, tais como a validação consistente dos 
estados das Premises, além de implementações dos conceitos de programação do PON 
conhecidos como Compartilhamento de Premises e Premises Impertinentes. Além disso, foi 
detectada uma imperfeição na Tecnologia LingPON, mais especificamente no Grafo PON, 
quanto à interação entre as entidades. Ainda, o NPCPP 1.0 foi testado por interessados e 
pesquisadores do PON, quando foram detectadas algumas melhorias no compilador e na 
Tecnologia LingPON 2.0. Foram priorizadas as melhorias que afetavam diretamente no 
funcionamento lógico e no desempenho de execução do compilador. Neste contexto relatado, 
das imperfeições reportadas pelos pesquisadores do PON, foi implementado o conceito de 
Unique Premise, Premise Impertinente e Compartilhamento de Premise, sendo necessário 
executar alterações na Tecnologia LingPON 2.0, além do NPCPP 2.0. As comparações dos 
resultados obtidos pelo NPCPP 2.0 com e sem o tratamento de tais conceitos de programação do 
PON revelam a importância de implementá-los para melhorar o desempenho de execução.  
No caso de Unique Premise e de Premise Impertinente, a utilização ou não desse 
conceito ainda fica à cargo do desenvolvedor, uma vez que é necessário indicar no código fonte 
quando se trata desse tipo de Premise. O Compartilhamento de Premise, por sua vez, foi 
implementado de forma que o próprio compilador identifica a necessidade de utilização desse 
conceito. Neste sentido, uma possível automatização dos conceitos de Unique Premise e Premise 
Impertinente também permitiria uma facilidade ainda maior no desenvolvimento dos programas. 
O desenvolvimento dessa ‘automatização’ certamente seria muito útil e interessante, porém 
requer uma análise de como implementar essa ‘capacidade’ no compilador para identificar ou 
prever a frequência que o valor de um dado Attribute sofreria alterações ao longo do programa. 
As melhorias que não foram desenvolvidas e que constam como pendentes referem-se a 
alterações gerais ou funcionalidades adicionais que não estão diretamente ligadas a alguma 
inconsistência do compilador nem no aperfeiçoamento do desempenho de execução e, portanto, 
serão descritas no próximo capítulo como sugestões para trabalhos futuros. 


194 
 
 
Com o objetivo de validar mais efetivamente o NPCPP 2.0, o compilador foi testado 
no sistema Simulador CTA, um programa com uma complexidade um pouco maior que a 
supramencionada aplicação de Rede de Sensores até então usada. Para o caso do Simuladpr CTA 
foi necessária a implementação de uma classe externa, em C++, que atuasse como uma API e 
fizesse a ligação entre o simulador, implementado na linguagem C++, e as estratégias de 
controle, implementadas via Tecnologia LingPON 2.0 com NCPP 2.0. Os resultados do CTA 
implementado em NPCPP foram comparados com os resultados de estudos precedentes 
realizados utilizando implementação na linguagem C++ usual do PI e implementação em C++ 
OO específico-notificante compilada a partir de compilador da Tecnologia LingPON 1.0. Nos 
resultados desses testes, foi identificado que a implementação gerada pelo NPCPP 2.0 obteve 
um desempenho muito próximo ao da implementação baseada em C++ usual sob os princípios 
da programação imperativa, o que tornou o resultado satisfatório. No caso da estratégia de 
controle basedo em congestionamento, por exemplo, o NPCPP 2.0 apresentou um tempo de 
execução menor que o C++ OO de uma maneira geral. Já a implementação C++ OO específico-
notificante gerada a partir da LingPON foi a que obteve um desempenho inferior ao das demais 
implementações. Não foram realizados experimentos dessa aplicação para o NPCPP 1.0, por 
conta das inconsistências encontradas naquele prototipal compilador, dificultando a realização 
dos testes. 
Em seguida, o NPCPP 2.0 foi validado em uma aplicação de ordenação conhecida como 
Bitonic Sort. Diferente da implementação de Rede de Sensores e mesmo do Simulador CTA, o 
Bitonic Sort apresenta uma presença mínima de redundâncias. Para os experimentos, a aplicação 
foi testada para o NPCPP 2.0, em C++ OO usual e em Python. O melhor desempenho foi 
apresentado pelo C++ OO, o que, neste caso em específico, já era um resultado esperado por 
conta da mínima existência de redundâncias no algoritmo Bitonic Sort. Entretanto, isto não 
desconsidera também a possibilidade de haver alguma notificação desnecessária que não tenha 
sido notada no NPCPP 2.0. A linguagem Python, apesar de apresentar um desenvolvimento em 
alto nível, assim como a LingPON em que pese as diferenças de paradigmas, apresentou o maior 
tempo de execução de uma maneira geral. Este experimento foi importante para analisar e 
confirmar o comportamento do NPCPP 2.0, e do próprio PON, em diferentes situações e tipos 
de aplicação. Além disso, com esse experimento foi possível comparar implementação em PON 
com uma linguagem de baixo nível e bom desempenho (C++ OO) e com outra linguagem de 
desenvolvimento em alto nível, mas um desempenho não muito favorável (Python). Pelos 
resultados obtidos, foi possível observar que a implementação gerada pelo NPCPP 2.0 representa 
uma solução que une a facilidade de desenvolvimento e um desempenho de execução aceitável.  


195 
 
 
Pelo mesmo motivo citado para a aplicação Simulador CTA, também não foram realizados 
experimentos do Bitonic Sort com o NPCPP 1.0. 
Um último experimento com o NPCPP 2.0 foi ainda realizado, utilizando a aplicação 
Random Forest, que é um algoritmo de aprendizagem de máquina. Para este experimento, foram 
testadas implementações em C, em Pyhton, além dos códigos gerados pelo NPCPP 2.0. Apesar 
de o Random Forest ser um algoritmo composto essencialmente por expressões lógicas if-else, 
pelos resultados obtidos, a linguagem C apresentou o melhor desempenho, seguida do NPCPP 
2.0. Este experimento foi realizado de modo que os valores das quatro entradas variassem de 
maneira aleatória. Uma maneira diferente de testar o comportamento e desempenho do NPCPP 
2.0 seria controlar ou até mesmo limitar para que apenas uma variável tivesse seu valor alterado 
por vez. Assim, a possibilidade de notificações e verificações desnecessárias seria menor. 
Ainda, visando verificar a viabilidade de paralelização, o compilador NPCPP 2.0 foi 
adaptado para suportar multithreads nos Methods. Para esta implementação foram utilizadas 
duas bibliotecas tradicionais de padrões de multithreads: PThreads e Thread Pooling. Essas 
implementações foram comparadas à versão single-threaded do target NPCPP 2.0. Da mesma 
maneira como ocorreu nos estudos da versão NPCPP 1.0, os resultados apresentados neste 
presente trabalho mostram que as versões multithreading apresentam um desempenho superior 
em relação à versão single-threaded, com um certo destaque à versão implementada com Thread 
Pooling, a qual apresentou o melhor resultado dentre as três versões. 
Em linhas gerais, o desenvolvimento deste trabalho mostrou que o compilador NPCPP 
2.0 apresenta um bom desempenho no âmbito da Tecnologia LingPON 2.0, além do alto nível 
de programação inerente desta tecnologia. Por meio dos experimentos de aplicações com 
características diferentes, foi possível observar que as aplicações do PON apresentam vantagens 
quando há redundâncias estruturais e temporais nos programas. Ainda, mesmo quando a 
presença de redundâncias é mínima, como no caso do Bitonic Sort, o NPCPP 2.0 teve um 
desempenho melhor que o Python, por exemplo. Por fim, mesmo que de maneira pontual, o 
trabalho explorou a possibilidade de paralelização nas entidades Methods, apresentando um 
desempenho melhor em comparação com a versão single-threaded. Assim, esta pesquisa 
apresentou o primeiro compilador para a LingPON 2.0, que corresponde a uma materialização 
que viabiliza duas das três propriedades elementares do PON, no tocante ao bom desempenho 
conjuntamente com desenvolvimento em alto nível. 
 
 
 


196 
 
 
4 CONCLUSÕES E TRABALHOS FUTUROS 
Este capítulo apresenta na Seção 4.1 as conclusões dessa dissertação de mestrado, à 
luz dos objetivos propostos no Capítulo 1 e do desenvolvimento do trabalho apresentado no 
Capítulo 3. Na sequência, a Seção 4.2 apresenta alguns pontos levantados como perspectivas 
para trabalhos futuros.  
 
 
4.1 
Conclusão 
O desenvolvimento deste trabalho fez parte de um conjunto de pesquisas que 
auxiliaram a co-validar o MCPON no tocante a Tecnologia LingPON 2.0. Mais precisamente, 
esta pesquisa teve como foco apresentar uma materialização para o PON que explora a 
viabilidade de duas das três propriedades elementares do paradigma, no âmbito da Tecnologia 
LingPON 2.0, à luz do método MCPON.  
Isto posto, primeiramente, é importante recordar que tais propriedades elementares do 
PON são: (a) facilidade de programação de software em alto nível; (b) execução eficiente pela 
ausência de redundâncias e; (c) desacoplamento implícito entre os elementos viabilizando 
organização, reaproveitamento de código e mesmo a execução paralela e/ou distribuída 
conforme permita a plataforma de execução visada. Isto dito, a dissertação buscou demonstrar 
a viabilidade de desenvolvimento em alto nível em PON, efetivamente de forma declarativa 
orientada a regras, ao mesmo tempo que apresentasse performance realmente apropriada a partir 
de código organizado em dado target visado no âmbito Tecnologia LingPON 2.0.  
Previamente a esta dissertação, utilizando o método MCPON, foram implementados 
em estudos precedentes alguns compiladores com geradores de código para linguagens-alvo 
(target) distintas, conforme relatado em Ronszcka (2019). Dentre eles, é possível destacar a 
versão prototipal implementada por Athayde e Negrini (2016) para Tecnologia LingPON 1.0, 
que gera códigos para o target C++ Notificante Modular orientado a Namespaces single-
threaded. Essa versão, denominada posteriormente como NPCPP 1.0, apresentou, no tocante a 
Tecnologia LingPON 1.0, um dos melhores resultados, com resultados em limítrofe para com 
a versão C++ Static, em termos de desempenho e legibilidade, no âmbito da arquitetura Von 
Neumann. Ainda, para a versão 1.0 da Tecnologia LingPON, Martini (2018) criou uma versão 
para o NPCPP 1.0 que permite parte da execução em multithreads e multicore.  


197 
 
 
No entanto, esta primeira versão do NPCPP foi testada em apenas uma aplicação de 
natureza simplória, denominada Portão Eletrônico ou Eletronic Gate. Isto porque o prototipal 
NPCPP 1.0 apresentava uma série de inconsistências, o que dificultava a realização de 
experimentos com aplicações de maior complexidade. Outro ponto negativo do NPCPP 1.0 é 
que este compilador prototipal não suportava conceitos de programação que já estavam 
implementados na Tecnologia LingPON 1.0, tais como Compartilhamento de Premises e 
Premises Impertinentes. Ainda, o compilador foi construído para a versão 1.0 da Tecnologia 
LingPON, a qual se encontra atualmente em sua versão mais estável conhecida como 
Tecnologia LingPON 2.0.  
Partindo do princípio de que nessa versão mais atual, cita-se Tecnologia LingPON 2.0, 
foram implementados alguns conceitos de programação do paradigma que as versões 1.X 
anteriores não apresentam (i.e., FBE Agregador e Master Rule), foi proposta a construção do 
compilador com gerador de código C++ Notificante Modular orientado a Namespaces para a 
LingPON 2.0, denominado de gerador de código NPCPP 2.0. Assim, buscou-se manter o 
desempenho eficiente e a facilidade de programação em alto nível que a primeira versão 
apresenta, mas agora em versão menos prototipal e com experimentação mais efetiva. Na 
verdade, o NPCPP 2.0 contemplou o determinado pela LingPON e Grafo PON da Tecnologia 
LingPON 2.0 que, em suma, é distintamente mais completa que a precedente. Ademais, ao 
longo do desenvolvimento dessa pesquisa foram identificados e realizados alguns ajustes na 
LingPON 2.0, bem como no próprio Grafo PON, inclusive implementando um conceito do 
PON (i.e. Unique Premise) que faltava na Tecnologia LingPON 2.0, já o contemplando 
inclusive no compilador NPCPP 2.0. 
Em um primeiro momento, para auxiliar na construção do compilador do NPCPP 2.0, 
foi utilizada a aplicação Rede de Sensores como elemento de validação. O objetivo principal 
dessa primeira etapa do NPCPP 2.0 consistiu em, além de gerar corretamente códigos para o 
target em questão a partir da LingPON 2.0, validar se o fluxo de notificações entre os arquivos 
(namespaces) dos códigos gerados fluíam de forma correta. Por este motivo, foi utilizado um 
programa com uma complexidade não muito elevada, mas ainda assim apropriado para tal. 
Mesmo nesta etapa inicial da construção do compilador foi possível realizar o primeiro 
experimento, cujos resultados foram favoráveis para o NPCPP 2.0. Tal experimento, utilizando 
a aplicação Rede de Sensores, permitiu a comparação de desempenho de implementações 
realizadas em NPCPP 1.0 e NPCPP 2.0, bem como de implementação equivalente escrita em 
C++ usual, orientada a objeto do Paradigma Imperativo. O NPCPP 2.0 foi o que obteve o menor 
tempo de execução, seguido pelo NPCPP 1.0 e, por fim, a implementação orientada a objetos. 


198 
 
 
A aplicação de Rede de Sensores é uma implementação que apresenta redundâncias estruturais 
e temporais consideráveis, demonstrando a capacidade do PON de melhorar o desempenho de 
execução por conta da eliminação de redundâncias de programas. Em tempo, esses resultados 
foram resumidamente publicados no evento 12ª Escola Regional de Alto Desempenho de São 
Paulo, cf. (OSHIRO et al., 2021). 
Uma vez finalizada a parte inicial da construção do compilador, a etapa seguinte 
consistiu em aperfeiçoá-lo. Dentre as melhorias realizadas, encontram-se a verificação e 
eventual eliminação de imperfeições que já tinham sido encontradas no NPCPP 1.0. Ainda, o 
NPCPP 2.0 foi testado por um grupo de três discentes-pesquisadores, no âmbito de uma dada 
disciplina stricto-sensu sobre o PON com uma singela aplicação de simulação de “alarme 
eletrônico”, sendo que algumas possíveis melhorias foram sugeridas tanto no âmbito do gerador 
de código, como também no âmbito da LingPON 2.0 e do Grafo PON. Ainda, outras melhorias 
foram sendo debatidas com pesquisadores do grupo de pesquisa do PON, ao longo do tempo, 
adicionando-se a estas. Isto posto, conforme o Quadro 17 do capítulo anterior, especificamente 
da Seção 3.2, algumas dessas melhorias já foram implementadas, como por exemplo a 
implementação do conceito de Unique Premise. Como já explicado, foram priorizados os 
reparos referentes ao funcionamento lógico e coerente do compilador e as melhorias que afetam 
diretamente no desempenho de execução dos programas. As melhorias que não foram 
implementadas são naturalmente descritas na seção seguinte de trabalhos futuros.  
Esta etapa de aperfeiçoamento do compilador ao longo do desenvolvimento permitiu, 
particularmente, a implementação de três conceitos fundamentais de programação do PON: 
Compartilhamento de Premises, Premises Impertinentes e Unique Premise. Os dois primeiros 
conceitos foram implementados ‘apenas’ no compilador e o último, no compilador e no âmago 
da Tecnologia LingPON 2.0, mais precisamente na linguagem de programação LingPON 2.0, 
no framework de compilação e no Grafo PON. Após a finalização do tratamento de cada 
conceito, foram realizados testes comparativos de tempo de execução do NPCPP 2.0, com o 
intuito de avaliar e, até mesmo, confirmar o impacto desses conceitos no desempenho de 
execução dos programas PON. Nos três casos foi constatada uma melhora de desempenho, 
conforme recordado a seguir, destacando que os testes nesse momento já perpassavam a 
aplicação de sensores, alcançando o Simulador CTA e Bitonic Sort particularmente.   
Mais precisamente no tocante aos conceitos de Compartilhamento de Premises e 
Premises Impertinentes, o tempo de execução diminui consideravelmente. No caso de 
Compartilhamento de Premises, por exemplo, o tempo de execução baixou em 30% no mínimo 
no experimento com Bitonic Sort, conforme discutido no capítulo anterior, especificamente na 


199 
 
 
Seção 2.3.2. Com a implementação de Premises Impertinentes, por sua vez, o resultado 
melhorou em mais de 40% no experimento com o Simulador CTA conforme apresentado na 
Seção 2.3.5. Os resultados em relação à Unique Premise também apresentaram uma queda no 
tempo de execução, mas de uma maneira mais branda, tendo baixado em 5% o tempo de 
execução no experimento do Bitonic Sort. Isto se dá, entretanto, porque a aplicação utilizada 
neste experimento, o algoritmo Bitonic Sort, apresenta poucos casos de notificações 
desnecessárias, conforme explicado na Seção 3.2.4. Em uma aplicação na qual a presença de 
notificações desnecessárias no contexto de Unique Premise for mais elevada, o impacto no 
desempenho seria consequentemente maior. Em todo caso, a implementação desse conceito 
permitiu um melhor resultado de desempenho, abrindo caminho para experimentações 
subsequentes daí decorrentes.  
Além dos resultados obtidos, outro ponto importante para refletir em relação a esses 
conceitos de programação é sobre as suas implementações. O Compartilhamento de Premises, 
por exemplo, foi desenvolvido de maneira tal que a identificação de casos desse conceito no 
programa seja de responsabilidade do compilador. Dessa maneira, o desenvolvedor não precisa 
se preocupar em identificar sempre quando se trata de casos de Compartilhamento de Premises, 
evitando possíveis equívocos. Isto é o que aconteceria nos casos de Premises Impertinentes e 
Unique Premise, em que a identificação desses conceitos ainda não estão automatizados. No 
caso da Unique Premise, por exemplo, fica sob responsabilidade do desenvolvedor de 
identificar quando duas ou mais Rules são excludentes entre si. Dependendo da complexidade 
da aplicação, isto acaba sendo dificultoso, além de tender a erros. Esta questão de automatizar 
a identificação desses conceitos é uma discussão muito construtiva para a evolução do NPCPP 
2.0, sendo necessária uma boa análise para desenvolver essa capacidade do compilador de 
identificar ou prever o comportamento das entidades envolvidas nesses conceitos.   
A última etapa do desenvolvimento do compilador foi a validação, ou seja, a 
comparação de seus resultados com os resultados de outras implementações no tocante aos 
experimentos com Simulador CTA, Bitonic Sort e Random Forest, que passaram a fazer parte 
dos benchmarks visados. O primeiro experimento desta etapa utilizou a aplicação do Simulador 
CTA, um programa que simula um ambiente urbano de tráfego de veículos por meio de 
estratégias de controle de semáforos, sendo que foram testadas a estratégia de controle 
independente e a estratégia baseada em congestionamento. Os resultados obtidos da integração 
do sistema CTA com as estratégias de controle de tráfego implementadas em NPCPP 2.0 foram 
comparados com os resultados de implementação na linguagem C++ OO usual do PI e 
implementação em C++ OO específico-notificante gerada a partir de LingPON 1.0. De uma 


200 
 
 
maneira geral, o NPCPP 2.0 apresentou tempos de execução satisfatórios, sendo melhores que 
os em C++ OO específico-notificante e muito próximos ao do C++ OO usual e, em alguns 
casos, levemente melhor. O código C++ OO específico-notificante era um dos melhores em 
termos de resultados na Tecnologia LingPON 1.0, diga-se em boa hora, cf. (SCHÜTZ et al., 
2015). Ainda, o NPCPP 1.0 não foi usado dado seu estado prototipal, com uma coleção de erros 
(i.e., bugs) que inviabilizariam ou, ao menos, dificultariam veementemente sua utilização e 
aplicações mais complexas como a do CTA.  
Outro experimento realizado utilizou o algoritmo de ordenação Bitonic Sort, conforme 
acima dito, o qual foi testado em implementações geradas pelo NPCPP 2.0 e implementações 
escritas em Python e C++ OO usual, sendo que esta última foi a que obteve o melhor 
desempenho. Em tempo, pertinente e mesmo fundamental recordar que a aplicação Bitonic Sort 
é um algoritmo que apresenta presença mínima de redundâncias. Por conta disso, considerando 
que um dos pontos fortes do PON é a eliminação de redundâncias, o NPCPP 2.0 apresentou um 
tempo de execução maior que o do C++ OO usual. Ainda assim, no entanto, seu desempenho 
foi melhor que o de uma implementação do Bitonic Sort em Python, linguagem esta atualmente 
popular no paradigma imperativo. O experimento com o Pyhton permitiu comparar o 
desempenho do NPCPP 2.0 com outra linguagem também de programação em alto nível, 
mostrando que, apesar disso, o Python apresenta um desempenho inferior. Em outras palavras, 
a comparação com os resultados obtidos pela linguagem em C++ (desenvolvimento em baixo 
nível e bom desempenho) e pelo Python (desenvolvimento em alto nível e desempenho a 
desejar), mostrou que o NPCPP 2.0 corresponde a uma solução que traz o equilíbrio entre a 
facilidade de programação e um desempenho adequado. Ainda, considerando o experimento 
realizado no ambiente disponibilizado pela AWS, os resultados sugerem que o comportamento 
do NPCPP 2.0 se assemelhe ao da implementação em C++ OO, apresentando um aumento 
escalar e constante no tempo de execução à medida que o número de elementos da sequência 
aumenta. No entanto, é necessário realizar mais experimentos para confirmar o comportamento 
do NPCPP 2.0, conforme descrito na seção de trabalhos futuros. Este experimento foi relevante 
no sentido de analisar e confirmar o comportamento do NPCPP 2.0, e do próprio PON, em 
casos em que não há redundâncias estruturais nem temporais. Neste sentido, o NPCPP 2.0 não 
chega a degradar consideravelmente a performance de execução de programas, quando as 
redundâncias não estão em pauta.  
Para o experimento com a aplicação Random Forest, algoritmo de machine learning 
(aprendizado de máquina) destinado para fins de classificação e regressão, os resultados obtidos 
pelo NPCPP 2.0 foram comparados com os de implementações em Pyhton e em C, sendo este 


201 
 
 
último o que apresentou o melhor desempenho. Ainda que essa aplicação apresente em sua 
implementação condições lógicas do tipo if-else, o que pode caracterizar redundâncias 
estruturais, o NPCPP 2.0 apresentou o segundo menor tempo de execução. Isto pode ter ocorrido 
por ainda existir alguma notificação desnecessária que ainda não foi identificada. Uma 
alternativa para tal, seria controlar os valores das entradas de maneira que variassem um de cada 
vez. Seria possível, assim, testar o comportamento do NPCPP 2.0 para identificar a presença de 
possíveis notificações desnecessárias. 
Outrossim, em que pese todo seu estado prototipal, o NPCPP 1.0 chegou a explorar, 
mesmo que de maneira parcial, a possibilidade de execução paralela. Assim sendo, 
naturalmente e suplementarmente, buscou-se garantir essa mesma abertura para a viabilidade 
de paralelização na solução NPCPP 2.0. Em termos de paralelismo, neste contexto dado, foram 
implementadas duas versões do NPCPP 2.0 para suportar multithreads nos Methods, cada qual 
utilizando uma tecnologia diferente de multithreading. As tecnologias utilizadas foram as 
bibliotecas PThreads e Thread Pooling. Os resultados destas duas versões multithreading 
foram comparados ao resultado obtido pela versão single-threaded via uma versão da aplicação 
de portão eletrônico na qual Methods tinham processamento tal que fosse pertinente para 
multithreading em multicore. Os resultados apontam que a versão do NPCPP 2.0 para 
multithreading/multicore apresenta melhor desempenho que a versão do NPCPP 2.0 para 
single-threaded, com destaque à implementação com Thread Pooling, versão que apresentou o 
melhor desempenho. Estas duas implementações com multithreads representam, ainda que 
inicialmente, a viabilidade de paralelização, muito embora isto não tenha sido o foco deste 
presente trabalho, finalmente.  
Em tempo, O NPCPP 2.0 contribuiu ainda para uma pesquisa desenvolvida 
paralelamente por Lucas V. S. de Mamann, mestrando do CPGEI, o qual adaptou o compilador 
apresentado por este trabalho para gerar códigos para hardware microprocessado a fim de serem 
aplicados em sistemas distribuídos de redes. Nesta aplicação foi desenvolvida, basicamente, um 
sistema com sensores e atuadores para Internet das Coisas comunicando-se em rede. Esta 
pesquisa, apresentada no SBESC 2021 demonstrou-se o potencial da compilação para o target 
NPCPP 2.0 mesmo para plataformas microprocessadas, podendo também apresentar resultados 
satisfatórios para sistemas distribuídos (MAMANN, 2020).  
Em suma, enquanto artefato, a contribuição deste trabalho consiste, à luz da 
Tecnologia LingPON 2.0, na construção do compilador NPCPP 2.0, sendo considerado como 
o primeiro compilador com gerador de códigos específico-notificantes para a versão 2.0 da 
LingPON, visto que as demais materializações da Tecnologia LingPON 2.0 tinham como 


202 
 
 
targets a geração de código para os frameworks PON. A partir do NPCPP 2.0, tem-se uma 
materialização do PON que explora a viabilidade de duas das três propriedades elementares do 
paradigma, particularmente do desenvolvimento em alto nível em versão contemporânea da 
LingPON, alcançando resultados apropriados via comparação com equivalente código C++, 
sabidamente performante no âmbito das linguagens imperativas. Ainda, também se traz alguma 
contribuição na propriedade de desacoplamento por apresentar código gerado de forma 
organizado-desacoplada, que permitiu inclusive o paralelismo de Methods.  
Por fim, o compilador NPCPP 2.0 apresenta conceitos de programação do PON que 
não haviam sido implementados na versão prototipal, nomeadamente Compartilhamento de 
Premises, Premises Impertinentes e Unique Premise, os quais ‘podam’ as notificações que 
finalmente não são necessárias. Isto permitiu a corroboração da relevância de tais conceitos em 
termos de desempenho de execução em PON. Além disso, durante o desenvolvimento do 
compilador NPCPP 2.0 foram identificadas e implementadas pequenas alterações na 
Tecnologia LingPON 2.0, culminando na implementação do conceito de Unique Premise e na 
colaboração da melhoria de interação entre algumas entidades no Grafo PON. No mais, 
naturalmente, o que se alcançou com NPCPP 2.0 pode ser aprimorado em alguns aspectos, 
incluindo este de poda de notificações, os quais são descritos na próxima seção. 
 
4.2 
Trabalhos futuros 
Conforme anteriormente apresentado, mais precisamente na Seção 3.2, nem todas as 
melhorias no NPCPP 2.0, apontadas por pesquisadores e discentes-pesquisadores envoltos no 
PON, que utilizaram a proposta Tecnologia LingPON 2.0 ou ao menos tiveram contato com 
ela, foram realizadas. Estas melhorias não implementadas, apresentadas pelo Quadro 18 nos 
itens de 1 a 5, correspondem a funcionalidades adicionais que não afetam diretamente no seu 
funcionamento ou no desempenho de execução (i.e., redução de redundâncias) do compilador 
NPCPP 2.0. 
 
Quadro 18 - Lista de melhorias sugeridas para trabalhos futuros 
  
Melhorias identificadas 
Componentes a serem 
ajustados 
1 
No processo de compilação, ordenar os parâmetros 
dos Methods conforme são escritos no programa 
fonte 
Grafo PON, NPCPP 2.0 
2 Execuções 
de 
expressões 
aritméticas 
nos 
parâmetros dos Methods 
LingPON 2.0, Grafo PON e 
NPCPP 2.0 


203 
 
 
3 Execuções de expressão de negação nas Premises 
LingPON 2.0, Grafo PON e 
NPCPP 2.0 
4 Criação de um sistema de log  
Grafo PON e NPCPP 2.0 
5 Expansão de Formation Rules no âmbito de vetores 
LingPON 2.0, Grafo PON e 
NPCPP 2.0 
6 Implementações de multithreads em demais 
entidades do PON  
NPCPP 2.0 
Fonte: Autoria própria 
 
Além das melhorias já apresentadas na Seção 3.2, o Quadro 18 apresenta um último 
item referente à implementação mais aprofundada de execução paralela no NPCPP 2.0. As 
melhorias do Quadro 18 são detalhadas nos itens a seguir, bem sabendo que há naturalmente 
um conjunto de outras melhorias possíveis e evidentes para desenvolvimentos voltados ao 
estado da técnica, como a possibilidade mais intensiva de vetores e matrizes, a alocação de 
memória dinâmica, o uso de arquivos, a melhoria de integração com bibliotecas externas e 
assim por diante. 
 
4.2.1 Melhorias apenas no Grafo PON 
Conforme o Quadro 17, foram apontados dois tipos de alterações para os parâmetros 
da entidade Method. O primeiro refere-se à ordenação dos parâmetros dos Methods e 
corresponde a uma melhoria no âmbito do Grafo PON. Nos códigos gerados, os parâmetros dos 
Methods nem sempre são apresentados na mesma ordem definida pelo código fonte em 
LingPON 2.0, mas são ordenados em ordem alfabética. Para ilustrar melhor, a Figura 61 
apresenta um exemplo desta situação. 
 
 
 
 
 
 
 
 
 
 
 
 


204 
 
 
Figura 61 - Ordenação dos parâmetros de Methods em LingPON 2.0 e nos códigos gerados 
 
Fonte: Autoria própria 
 
Como é apresentado na Figura 61, a ordem dos parâmetros no método mtEnviarSMS() 
do código gerado é alfabética e não corresponde à ordem definida no programa fonte em PON. 
Durante os testes foi constatado que na etapa de geração de código, os parâmetros já se 
apresentam ordenados alfabeticamente e, portanto, a melhoria deve ser aplicada no Grafo PON. 
Ainda, durante o período de acompanhamento e testes, foi sugerido como melhoria no 
Grafo PON a criação de um console de debug ou um sistema de log de varredura para descrever 
o fluxo que está sendo executado e facilitar a depuração.  
 
4.2.2 Melhorias na Tecnologia LingPON 2.0 
Esta seção descreve sobre as melhorias referentes à Tecnologia LingPON, ou seja, que 
abrangem não apenas o Grafo PON, mas também a linguagem LingPON. Uma delas é a 
possibilidade de executar expressões aritméticas nos parâmetros de Methods. O Código 63 
apresenta um exemplo desse tipo de parâmetro.  


205 
 
 
Código 63 - Exemplo de Methods com expressões aritméticas no parâmetro 
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
rule rlOpennigGate 
    condition 
        premise prRemoteControlOpenOn  
          event.atEventState == 0  
        end_premise 
        and 
        premise prGateIsClosed  
          gate.atGateState != 0 
        end_premise 
    end_condition 
    action  
        instigation  
          call gate.mtOpen(); 
          call this.CountGateIsOpened(this.atDelay + 10); 
        end_instigation 
    end_action 
end_rule 
Fonte: Autoria própria 
 
A linha 14 do Código 63 apresenta o Method CountGateIsOpened() recebendo como 
parâmetro uma expressão aritmética. Este tipo de parametrização ainda não é possível ser 
processado atualmente pelo Grafo PON. 
Outra melhoria apontada é em relação a execução de expressão de negação em 
Premises. A linha 8 do Código 63 apresenta uma Premise cuja verificação é dada por uma 
expressão de negação. O Grafo PON e a LingPON apresenta também limitações para 
expressões de negação em Premises.  
O item 5 do Quadro 17 corresponde a limitações apresentadas pelo conceito de 
Formation Rules, conceito de programação do PON apresentado na Seção 2.1.3.6. Foi 
constatado pelo grupo de já mencionados pesquisadores do PON em 2019, que a implementação 
de Formation Rules e vetores expande os vetores apenas até a Condition e as Premises, não 
sendo possível chamar métodos nas Instigations que pertençam aos FBEs dos vetores pela 
notação de índice variável. 
Além dos itens de melhorias listados no Quadro 17, algumas imperfeições na 
Tecnologia LingPON 2.0 foram identificadas durante o desenvolvimento de um trabalho 
realizado por Skora (2020), em disciplina stricto sensu pertinente ao PON em 2020. Um 
objetivo deste estudo desse discente, oriundo do curso de Engenharia da Computação no 
DAINF/UTFPR, é justamente avaliar a capacidade do Grafo PON de conseguir instanciar cada 
programa em LingPON 2.0. Durante esses esforços foi detectado, por exemplo, que no 
framework do Grafo, a memória é alocada dinamicamente, porém em nenhum momento é 
liberada, além de que muitos ponteiros não são aterrados e muitas coleções que deveriam ser 
inicializados ficam vazias. Outra melhoria apontada em (SKORA, 2020) é com relação ao fato 


206 
 
 
de as classes do Framework do Grafo PON não estarem em um namespace próprio, dificultando 
sua utilização para desenvolver um target que usa os Frameworks PON C++, uma vez que esses 
também terão classes com nomes de entidades do PON. 
No âmbito da linguagem LingPON 2.0, ademais, ele percebeu que é possível criar e 
redeclarar entidades com o mesmo nome, sendo do mesmo tipo ou não. Uma possível evolução 
tanto do Grafo PON como na LingPON 2.0 com esses afinamentos possibilitaria uma maior 
facilidade e abrangência de uso da Tecnologia LingPON 2.0, além de permitir a consolidação 
dessa tecnologia não apenas como estado da arte, como também enquanto estado da técnica do 
PON ao longo do tempo. 
 
 
4.2.3 Aumento do conjunto de aplicações em NPCPP 2.0 
O desenvolvimento deste trabalho apresentou casos de uso do NPCPP 2.0 com 
diferentes aplicações, tais como Redes de Sensores, Bitonic Sort, Simulador CTA e Random 
Forest. Apesar de essas aplicações demostrarem o potencial do compilador em termos de 
desempenho e desenvolvimento em alto nível, o NPCPP 2.0 poderia ser explorado em outras 
aplicações de complexidade ainda maiores, como por exemplo o Futebol de Robôs, 
recentemente utilizadas em experimentos com outra materialização do PON voltada ao estado 
da técnica e não estado da arte, o Framework PON C++ 4.0 (NEVES, 2021). Uma outra 
abordagem interessante em termos de experimentos seria a aplicação do NeuroPON, que 
consiste em um modelo computacional, desenvolvido por Schütz (2019), que permite a 
construção de Redes Neurais Artificiais (RNA) com conceitos do PON. A aplicação do 
NeuroPON em softwares, por exemplo, possibilita um alto nível de desacoplamento de seus 
módulos, o que foi explorado em termos de PON em hardware e de frameworks PON para 
multicore (NEGRINI, 2019; SCHÜTZ, 2019). 
Ainda, recordando o que já comentado na seção anterior, para averiguar o 
comportamento do NPCPP 2.0 no experimento da aplicação Bitonic Sort, é necessário realizar 
mais experimentos. O teste realizado com o Bitonic Sort em ambiente preemptivo obteve um 
resultado, o qual sugere que o desempenho do NPCPP 2.0 varia de maneira logarítmica 
conforme varia a quantidade de elementos da sequência. Já no experimento executado na 
máquina virtual da AWS, o desempenho do NPCPP 2.0 apresenta uma variação constante e 
escalar, proporcional à quantidade de elementos da sequência. Muito provavelmente, essa 
diferença de resultados decorre das preempções e instabilidades do sistema operacional no 


207 
 
 
ambiente do primeiro experimento. No entanto, tais testes foram realizados com um número 
pequeno de elementos (até 64 elementos). Para analisar e confirmar de maneira mais consistente 
o comportamento do NPCPP 2.0 perante ao algoritmo Bitonic Sort, é necessário realizar mais 
experimentos e com uma amostra maior de elementos a serem ordenados.10 
 
4.2.4 Melhorias no NPCPP 2.0 
Isto dito, este presente trabalho chegou a explorar a possibilidade de execução paralela, 
implementando multithreads na entidade Method, o que possibilitou a viabilidade, de maneira 
inicial, da paralelização do PON via NPCPP 2.0. No entanto, esta viabilidade não foi testada 
nas demais entidades do PON. Neste sentido, é possível realizar um estudo mais aprofundado 
do NPCPP 2.0 para permitir gerar programas em soluções multithreads principalmente para 
ambientes multicore (como aplicações com o supramencionado NeuroPON) e comparar o 
desempenho de execução com o da versão single-threaded, desenvolvida neste trabalho. Desta 
maneira, seria possível uma materialização do PON que satisfaça de forma mais efetiva a 
terceira propriedade elementar do paradigma. 
Durante o desenvolvimento deste trabalho, Mamann (2020) desenvolveu em paralelo 
uma implementação do NPCPP 2.0 adaptado para gerar códigos para microcontroladores, 
podendo ser utilizado em sistemas distribuídos. No entanto, o desenvolvimento dessa 
implementação foi baseado considerando o compilador apresentado na qualificação de 
mestrado desta pesquisa (OSHIRO, 2020), portanto seria pertinente implementar os demais 
recursos apresentados nessa dissertação, tais como Premises Impertinentes e Compartilhamento 
de Premises. 
Ainda no âmbito de ambientes multiprocessados, Simão e Stadzisz (2010) 
apresentaram uma solução que permite a garantia de determinismo baseada em sincronização 
de acesso às entidades do PON. Basicamente, tal mecanismo permite que cada entidade 
notificada contra-notifique a entidade notificante informando, por exemplo, se seu estado foi 
modificado ou não, possibilitando ao notificante ter certeza de que todos os notificados tiveram 
oportunidade de avaliar a notificação enviada. O notificante em questão, então, notifica 
novamente os elementos modificados (em termos de estado lógico) para que prossigam com 
suas atividades no fluxo de notificações (SIMÃO e STADZISZ, 2010). Neste sentido, salienta-
                                                          
10 Foi realizado um experimento adicional pós-defesa deste trabalho, cujos resultados estão 
apresentados no Apêndice H. 


208 
 
 
se a possibilidade da implementação de uma evolução do NPCPP 2.0 buscando um 
comportamento determinístico por meio dessa sincronização de acessos às entidades do PON e 
mesmo outros mecanismo suplementares como os descritos em (SIMÃO et al., 2010), o que 
seria particularmente pertinente para processamento paralelo e ainda mais para processamento 
distribuídos como os daqueles experimentos iniciados por Mamann. 
Conforme já mencionado anteriormente, outra questão relevante para a evolução do 
compilador, principalmente em termos de facilidade de programação, seria a possibilidade de 
automatizar os conceitos Unique Premise e Premise Impertinente. Atualmente, a 
responsabilidade de identificar ou prever as Premises que se enquadram nesses casos fica a 
cargo do desenvolvedor, o que também aumenta a possibilidade de ocorrer erros.  Uma vez que 
o compilador se encarregue de realizar os tratamentos desses conceitos de maneira automática, 
assim como ocorre com o conceito Premise Compartilhada, facilitaria consideravelmente o 
desenvolvimento.


209 
 
 
 
REFERÊNCIAS 
ATHAYDE, E. B; NEGRINI, F. Implementação de Compilação para C++ Namespaces 
para a LingPON e Otimizações no Tratamento de Premissas. Trabalho realizado na 
disciplina Tópicos Avançados em Engenharia de Software (CAES101 – PPGCA/UTFPR) 
publicado no Anexo E da Dissertação de Mestrado de Leonardo Araújo Santos. UTFPR. 
Curitiba, Brasil, 2016. 
BANASZEWSKI, R. F. Paradigma Orientado a Notificações: Avanços e Comparações. 
Dissertação de Mestrado, Pós-Graduação em Engenharia Elétrica e Informática Industrial 
(CPGEI), UTFPR, Curitiba, 2009. 
BANERJEE, P.; CHANDY, J. A.; GUPTA, M.; HODGES, E. W.; HOLM, J. G.; LAIN, A.; 
PALERMO, D. J.; RAMASWAMY, S.; SU, E. The Paradigm Compiler for Distributed 
Memory Multicomputers. IEEE Computer 28 (10), pp. 37-47, 1995. 
BARRETO, W. R. M.; VENDRAMIN, A. C. B. K.; SIMÃO, J. M. Notification Oriented 
Paradigm for Distributed Systems. In: Computer on the Beach 2018, Florianopolis, 2018. 
BATCHER, K. E. (1968). Sorting networks and their applications. In Proceedings of the 
April 30-May 2, 1968, Spring Joint Computer Conference, AFIPS '68, p. 307-314, New York, 
NY, USA. ACM. 
BELMONTE, D. Método para Distribuição da Carga de Trabalho dos Softwares PON em 
Multicore. Trabalho de Qualificação de Doutorado, Pós-Graduação em Engenharia Elétrica e 
Informática Industrial (CPGEI), UTFPR, 2012. 
BELMONTE, D.; LINHARES, R. R.; STADZISZ, P. C.; SIMAO, J. M.. A new Method for 
Dynamic Balancing of Workload and Scalability in Multicore Systems. IEEE Latin 
America Transactions, ISSN: 1548-0992. 2016. 
BROOKSHEAR, G. Computer Science: An Overview. Addison Wesley, 2012. 
CHIERICI, G. B. JuNOC++ e NOPL Lite: uma nova forma de compor aplicações do 
Paradigma Orientado a Notificações em alto nível por meio de um novo framework em 
C++ e um dialeto de NOPL. [S.l.]: CPGEI/UTFPR, 2020. Trabalho realizado na disciplina 
Tópicos Especiais em EC: Paradigma Orientado A Notificações (TEC0301). 


210 
 
 
CRIMINISI, Antonio; SHOTTON, Jamie; KONUKOGLU, Ender. Decision forests: A unified 
framework for classification, regression, density estimation, manifold learning and semi-
supervised learning. Foundations and Trends in Computer Graphics and Vision, v. 7, p. 81–
227, 01 2011. 
FERREIRA, C. A. Linguagem e Compilador para o Paradigma Orientado a Notificações 
(PON): Avanços e Comparações. Dissertação de Mestrado, PPGCA/UTFPR. Curitiba, Brasil, 
2015.  
GABBRIELLI, M.; MARTINI, S. Programming Languages: Principles and Paradigms. 1st 
ed. Springer Publishing Company, Incorporated, 2010. 
GAUDIOT, J. L.; SOHN, A. S. Data-Driven Parallel Production Systems. IEEE Trans. On 
Software Eng.. V. 16. No 3, pg. 281-293, 1990. 
GODFREY, M. D.; HENDRY, D. F. The Computer As Von Neumann Planned It. IEEE 
Annals of the History Of Computing, 15(1), p. 11-21, 1993. 
HENZEN, A. F. Portabilidade do Framework PON de C++ standard para C# e Java. 
Relatório da disciplina de Tópicos Especiais Em Ec: Paradigma Orientado A Notificações. 
CPGEI-PPGCA/UTFPR, Curitiba - PR, Brasil, 2015. 
KERSCHBAUMER, R. Proposição do Paradigma Orientado a Notificações no 
Desenvolvimento de Circuitos Lógico Digitais Reconfiguráveis. Tese de doutorado – Pós-
Graduação em Engenharia Elétrica e Informática Industrial (CPGEI), UTFPR, 2018. 
KERSCHBAUMER, R.; LINHARES, R. R.; SIMÃO, J. M.; STADZISZ, P. C.; LIMA, C. R. 
E. Notification Oriented Paradigm to Implement Digital Hardware. Journal of Circuits 
Systems and Computers, 2018. 
KERSCHBAUMER, R.; KAVIATKOVSKI, A. A.; GARCIA, G. R.; LIMA, C. R. E.; SIMÃO, 
J. M. The Notification Oriented Paradigm Language to Digital Hardware as an intuitive 
high-level synthesis tool. REVISTA DE INFORMÁTICA TEÓRICA E APLICADA: RITA, 
v. 28, p. 90-106, 2021. 
LINHARES, R. R., Contribuição para o desenvolvimento de uma arquitetura de 
computação própria ao paradigma orientado a notificações. Tese de Doutorado, CPGEI, 
UTFPR. Brasil, 2015. 


211 
 
 
MAMANN, L.V. S. PON Aplicado a Microcontroladores. [S.l.]: CPGEI/UTFPR, 2020. 
Trabalho realizado na disciplina Tópicos Especiais em EC: Paradigma Orientado A 
Notificações (TEC0301). 
MARTINI, G. H. K. NOP language on multi-core architecture computers. Definição 
Framework NOP AKKA. Aluno Externo CPGEI/UTFPR. Disciplina sobre Paradigma 
Orientado a Notificações (PON), CPGEI-PPGCA/UTFPR (Profs. J. M. Simão & R. R. 
Linhares), Curitiba - PR, Brasil, 2018. 
MARTINI, G. H. K.; SIMÃO J. M.; FABRO, J. A.; RONSZCKA, ADRIANO F. Multi-
threading capability evaluation of the Notification Oriented Programming Language for 
the x86 Architecture. In: 11th International Conference on Information Society and 
Technology - ICIST, 2021, Kopaonik. Book: ICIST 2021 Proceedings - Proceedings of the 11th 
International Conference on Information Society and Technology. Belgrade, Serbia: ISOS 
Conference Proceedings Series, 2021. v. 1. p. 44-49. 
MELO, L. C., Adaptação Do Paradigma Orientado A Notificações Para Desenvolvimento 
De Sistemas Fuzzy. Dissertação de Mestrado, Programa de Pós-Graduação em Computação 
Aplicada (PPGCA), UTFPR. Curitiba, Brasil, 2016. 
MENDONÇA, I. T. M. Metodologia de projeto de software orientado a notificações. 2020. 
Tese (Doutorado em Engenharia Elétrica e Informática Industrial) - Universidade Tecnológica 
Federal do Paraná, Curitiba, 2020. 
MULLAPUDI, A. Bitonic Sort. [S.l.]: University at Buffalo, 2014. Lecture for CSE633: 
Parallel Algorithms (Spring 2014).  
NEGRINI, F. Comparação entre Paradigma Orientado a Notificações e Paradigma 
Imperativo sobre um Simulador de Tráfego. Trabalho realizado na disciplina Paradigma 
Orientado a Notificações. CPGEI-PPGCA/UTFPR, Curitiba - PR, Brasil, 2016. 
NEGRINI, F. Animador CTA – Um aplicativo para demonstração gráfica de simuladores 
de controladores de trânsito. Trabalho realizado na disciplina Estudos especiais em 
paradigmas de programação (EE2261). CPGEI/UTFPR. 2017. 
NEGRINI, F. LingPON 2.0 e Compilador para Framework Erlang: Programação 
Multicore Transparente já é uma Realidade.  Dissertação de Mestrado – Pós-Graduação em 
Engenharia Elétrica e Informática Industrial (CPGEI), UTFPR, 2019. 


212 
 
 
NEGRINI, F.; LINHARES, ROBSON R.; Fabro J. A.; STADZISZ, PAULO C.; Simao, J. M. 
NOPL-Erlang: Programação multicore transparente em linguagem de alto nível. In: V 
Escola Regional de Alto Desempenho do Rio de Janeiro (ERAD-RJ 2019), 2019, Rio de 
Janeiro.  
NEGRINI, F.; RONSZCKA, A. F.; LINHARES, R. R.; FABRO, J. A.; STADZISZ, P. C.; 
SIMÃO J. M. NOPL-Erlang: Programação Multicore Transparente em Linguagem de 
Alto Nível. Cadernos do IME Série Informática (CIME-SI), Vol. 43, Dezembro 2019, ISSN: 
1413-9014 – Advindo do homônimo artigo no ERAD-RJ 2019 (Best Paper). Disponível em: 
.br/index.php/cadinf/issue/view/2407. Acessado 22/10/2021.   
NEVES, F. S. Framework PON C++ 4.0: Contribuição para a Concepção no Paradigma 
Orientado a Notificações por meio de Programa Genérico. Dissertação de Mestrado – Pós-
Graduação em Engenharia Elétrica e Informática Industrial (CPGEI), UTFPR, 2021. 
NEVES, F. S.; SIMÃO, J. M.; LINHARES, R. Application of generic programming for the 
development of a C++ framework for the notification oriented paradigm. In: ICIST. 2021. 
p. 56–61. 
OLIVEIRA, R. N. Assistência à autonomia domiciliar empregando paradigma orientado 
a notificações, Dissertação de Mestrado, CPGEI, UTFPR. Curitiba, Brasil, 2019. 
OSHIRO, L. K. Contribuição para a Tecnologia LingPON 2.0: avanços na completude 
linguística e no gerador de código para o código-alvo ‘C++ notificante via Espaço de 
Nomes’. Trabalho de Qualificação de Mestrado, Pós-Graduação em Engenharia Elétrica e 
Informática Industrial (CPGEI), UTFPR, 2020. 
OSHIRO, L. K.; RONSZKA, A. F.; FABRO J. A.; SIMÃO, J. M. Linguagem e Compilador 
para o Paradigma Orientado a Notificações: Uma Solução Performante Orientada a 
Regras. 12ª Escola Regional de Alto Desempenho de São Paulo, 2021, São Paulo. 
PAN J.; DESOUZA G. N.; KAK A. C.: FuzyyShell: A Large-Scale Expert System Shell 
Using Fuzzy Logic for Uncertainty Reasoning. IEEE Transactions on Fuzzy Systems, Vol. 
6, No 4, November 1998. 
PRAYUDHA, 
B. 
“Biblioteca 
avr-enc28j60,” 
2014. 
Disponível 
em:https://github.com/bprayudha/avr-enc28j60. Acesso em: 01 Ago.2021. 


213 
 
 
PETERS, E. Coprocessador para Aceleração de Aplicações Desenvolvidas Utilizando 
Paradigma Orientado a Notificações. 2012. Dissertação de Mestrado – Pós-Graduação em 
Engenharia Elétrica e Informática Industrial (CPGEI), UTFPR, 2012. 
PETERS, H.; SCHULZ-HILDEBRANDT, O.; LUTTENBERGER, N. “A novel sorting 
algorithm for many-core architectures based on adaptive bitonic sort,” 2012 IEEE 26th 
International Parallel and Distributed Processing Symposium, vol. 1, pp. 227–237, 2012. 
PETERS, E.; JASINSKI, R. P.; PEDRONI, V. A.; SIMAO, J. M. A new hardware 
coprocessor for accelerating Notification-Oriented applications. International Conference 
on FieldProgrammable Technology (FPT), South Korea, 2012. 
PORDEUS, L. F.; KERSCHBAUMER, R.; LINHARES, R. R.; WITT, F. A.; STADZISZ, P. 
C.; LIMA, C. R. E.; SIMÃO, J. M. Notification Oriented Paradigm to Digital Hardware. 
Revista SODEBRAS, v. 11, p. 116-122, 2016. 
PORDEUS, L. F. Simulação de uma Arquitetura de Computação Própria ao Paradigma 
Orientado a Notificações. Dissertação de Mestrado – Pós-Graduação em Engenharia Elétrica 
e Informática Industrial (CPGEI), UTFPR, 2017. 
PORDEUS, L. F. ArqTotalPON - Contribuição para Arquitetura de Computação própria 
e efetiva ao Paradigma Orientado a Notificações. Qualificação de Doutorado, Pós-
Graduação em Engenharia Elétrica e Informática Industrial (CPGEI), UTFPR, 2020. 
PORDEUS, L. F.; LINHARES, R. R.; STADZISZ, P. C.; SIMÃO, J. M. NOP-DH - Evaluation 
Over Bitonic Sort Algorithm. Microprocessors and Microsystems, v. 85, p. 104314, 2021. 
RAYMOND, E. S. R. The Art of UNIX Programming. Pp. 327, A. Wesley, 2003.  
RONSZCKA, A. F. Contribuição para a Concepção de Aplicações no Paradigma 
Orientado a Notificações (PON) sob o viés de Padrões. Dissertação de mestrado – Pós-
Graduação em Engenharia Elétrica e Informática Industrial (CPGEI), UTFPR, 
2012. 
RONSZCKA, A. F.; BANASZEWSKI, R. F.; LINHARES, R. R.; TACLA, C. A.; STADZISZ, 
P. C.; SIMAO, J. M. Notification-Oriented and Rete Network Inference: A Comparative 
Study. Systems, Man, and Cybernetics (SMC), 2015 IEEEInternational Conference on. p. 807–
814, 2015. 


214 
 
 
RONSZCKA, A. F.; FERREIRA, C. A.; STADZISZ, P. C.; FABRO, J. A.; SIMÃO, J. M. 
Notification-Oriented Programming Language and Compiler. SBESC – VII Brazilian 
Symposium on Computing Systems Engineering, 2017. 
RONSZCKA, A. F. Método para a Criação de Linguagens de Programação e 
Compiladores para o Paradigma Orientado a Notificações em Plataformas Distintas. Tese 
de Doutorado – Pós-Graduação em Engenharia Elétrica e Informática Industrial (CPGEI), 
UTFPR, 2019. 
SANTOS, L. A. Linguagem e Compilador para o Paradigma Orientado a Notificações: 
avanços para facilitar a codificação e sua validação em uma aplicação de controle de 
futebol de robôs. Dissertação de Mestrado – PósGraduação em Engenharia Elétrica e 
Informática Industrial (CPGEI), UTFPR, 2017. 
SANTOS, L. A.; FABRO, J. A.; DE FREITAS, M. D.; RONSZCKA, A. F. ; SIMÃO, J. M. 
NOPL - Notification Oriented Programming Language - A New Language, and Its 
Application to Program a Robotic Soccer Team. In: Goreti Marreiros; Francisco S. Melo; 
Nuno Lau; Henrique Lopes Cardoso; Luís Paulo Reis. (Org.). Lecture Notes in Computer 
Science. 1ed.: Springer International Publishing, 2021, v. 12981, p. 445-455.. 
SCOTT, M. L. Programming Language Pragmatics. Ed. 4. Elsevier Science & Technology., 
2016. 
SCHÜTZ, F.; SANTOS, L. A.; PORDEUS, L. F.; KERSCHBAUER, R. Manual da LingPON: 
Evoluções na linguagem e compilador. Trabalho realizado nas disciplinas Tópicos Especiais 
em EC: Linguagens e Compiladores (TEC0302 – CPGEI/UTFPR) e Tópicos Avançados em 
Engenharia de Software (CAES101 – PPGCA/UTFPR) publicado no Anexo D da Dissertação 
de Mestrado de Leonardo Araújo Santos. UTFPR. Curitiba, Brasil, 2015. 
SCHÜTZ, F.; FABRO J. A.; RONSZCKA, A. F.; STADZISZ, P. C.; SIMÃO, J. M. Proposal 
of a declarative and parallelizable artificial neural network using the notification-oriented 
paradigm. Neural Computing and Applications, p. 1-12, 2018. 
SCHÜTZ, F. NEURO-PON: Uma Abordagem para o Desenvolvimento de Redes Neurais 
Artificiais Utilizando o Paradigma Orientado a Notificações. Tese (Doutorado). Curso de 
Pós-Graduação em Engenharia Elétrica e Informática Industrial – CPGEI, UTFPR. 2019. 
SIMÃO, J. M. Proposta de uma Arquitetura de Controle para Sistemas Flexíveis de 
Manufatura Baseada em Regras e Agentes. 2001. Dissertação de Mestrado, Universidade 


215 
 
 
Tecnológica Federal do Paraná - UTFPR, Curso de Pós-Graduação em Engenharia Elétrica e 
Informática Industrial - CPGEI, Curitiba, 2001. 
SIMÃO, J. M.; STADZISZ, P. C. An Agent-Oriented Inference Engine applied for 
Supervisory Control of Automated Manufacturing Systems. In: Abe J. M., Silva Filho J. I. 
(Org.). Frontiers in Artificial Intelligence and Applications (Advances in Logic, Artificial 
Intelligence and Robotics, LAPTEC 2002). Amsterdam, The Netherlands: IOS PRESS 
BOOKS, 2002, v. 85, p. 234-241, 2002. 
SIMÃO, J. M. A Contribution To The Development Of A HMS Simulation Tool And 
Proposition Of A Meta-Model For Holonic Control. 2005. Tese de doutorado. Curso de Pós-
Graduação em Engenharia Elétrica e Informática Industrial  - CPGEI, CEFET-PR. Curitiba, 
Brasil, 2005. 
SIMÃO, J. M.; STADZISZ, P. C. Paradigma Orientado a Notificações (PON) – Uma 
Técnica de Composição e Execução de Software Orientado a Notificações. Pedido de 
Patente submetida ao INPI/Brasil (Instituto Nacional de Propriedade Industrial) em 2008 e a 
Agência de Inovação/UTFPR em 2007. Nº INPI PI08055181. Patente submetida ao INPI. 
Brasil, 2008. 
SIMÃO, J. M.; STADZISZ, P. C. Inference Based on Notifications: A Holonic Metamodel 
Applied to Control Issues. IEEE Trans. on Systems, Man and Cybernetics. Part A, Syst. and 
Humans, v. 39, p. 238-250, 2009a.  
SIMÃO, J. M., TACLA, C. A., STADZISZ, P. C., Holonic Control Meta-Model. IEEE  
Transactions on Systems, Man and Cybernetics. Part A, Systems and Humans, 2009b. 
SIMÃO, J. M.; STADZISZ, P. C. Mecanismo de Resolução de Conflito e Garantia de 
Determinismo para o Paradigma Orientado a Notificações (PON). Pedido de Patente 
submetida ao INPI/Brasil (Instituto Nacional de Propriedade Industrial) em 2010. Nº INPI 
PI10002960. Brasil, 2010. 
SIMÃO, J. M.; BANASZEWSKI, R. F; TACLA, C. A.; STADZISZ, P. C. Mecanismo de 
Inferência Otimizado do Paradigma Orientado a Notificações (PON) e Mecanismos de 
Resolução de Conflitos para Ambientes Monoprocessados e Multiprocessados Aplicados 
ao PON. Pedido de Patente submetida ao INPI/Brasil (Instituto Nacional de Propriedade 
Industrial) em 2010. Nº INPI PI10037365. Brasil, 2010. 


216 
 
 
SIMÃO, J. M.; TACLA, C. A.; STADZISZ, P. C.; BANASZEWSKI, R. F. Notification 
Oriented Paradigm (NOP) and Imperative Paradigm: A Comparative Study. Journal of 
Software Engineering and Applications, 5(6), p. 402-416, 2012a.  
SIMÃO, J. M.; STADZISZ, P. C.; TACLA, C. A.; LINHARES, R. R.; BELMONTE, D. L.; 
BANASZEWSKI, R. F. Comparações entre duas materializações do Paradigma Orientado 
a Notificações (PON): Framework PON Prototipal versus Framework PON Primário. IV 
Congreso Internacional de Computación y Telecomunicaciones. Lima, Peru, 2012b.  
SKORA, L. E. B. Criação de alvos de compilação para a NOPL e ferramentas de 
serialização-desserialização para o Grafo PON. [S.l.]: CPGEI/UTFPR, 2020. Trabalho 
realizado na disciplina Paradigmas de Programação. 
VALENÇA, G. Z. Contribuição para Materialização do Paradigma Orientado a 
Notificações (PON) Via Framework e Wizard. Dissertação de Mestrado, Programa de Pós-
Graduação em Computação Aplicada (PPGCA), UTFPR. Curitiba, Brasil, 2012. 
WIECHETECK, L. V. B. Método para projeto de software usando o paradigma orientado 
a notificações – PON. Dissertação de Mestrado – Pós-Graduação em Engenharia Elétrica e 
Informática Industrial (CPGEI), UTFPR, 2011. 
WITT, F. A.; SIMAO, J. M.; LINHARES, R. R.; STADZISZ, P. C.; LIMA, C. R. E. 
Comparação entre o Paradigma Orientado a Objetos (POO) e o Paradigma Orientado a 
Notificações (PON) em um Controle Discreto em Lógica Reconfigurável. Em: XVI SICITE 
- Seminário de Iniciação Científica e Tecnológica da UTFPR, 2011, Ponta Grossa - PR. Anais 
do XVI SICITE, 2011. 
XAVIER, R. D. Paradigmas de Desenvolvimento de Software: Comparação entre 
abordagens Orientada a Eventos e Orientada a Notificações, Dissertação de Mestrado, 
Programa de Pós-Graduação em Computação Aplicada (PPGCA), UTFPR. Curitiba, Brasil, 
2014.


217 
 
 
APÊNDICE A 
CLASSE NAMESPACESCOMPILER NPCPP 2.0 SINGLE-THREADED 
 
Este apêndice apresenta os arquivos .h e .cpp da classe NamespacesCompiler, do 
NPCPP 2.0 single-threaded, apresentada na Seção 3.1.1. Para a construção desta versão do 
gerador de código foi utilizado o programa Sensors, cujos códigos fonte em LingPON 2.0 e 
códigos gerados em C++ notificante modular orientado a namespaces são apresentados na 
íntegra pelos APÊNDICES B e C, respectivamente. 
 
Código 64 - Arquivo .h da classe NamespacesCompiler. 
#ifndef _NAMESPACES_COMPILER_H_ 
#define _NAMESPACES_COMPILER_H_ 
 
class Instance; 
class Premise; 
class Attribute; 
class Condition; 
class Rule; 
 
#include "Compiler.h" 
 
#include <string> 
#include <iostream> 
#include <fstream> 
#include <list> 
#include <map> 
 
using namespace std; 
 
class NamespacesCompiler : public Compiler { 
 
public: 
 
 
std::list<std::string> init_premises; 
 
 
int VerificaPremiseRepetida(std::list<std::string> list_premises,  
                          std::string premiseName); 
 
std::list<std::string> RetornaRulesVinculadas(std::string premise_Name,  
                          std::map<std::string, Rule*> *rules); 
 
 
bool ExistePremisesImpertinentes(Attribute *attribute); 
 
std::list<std::string> RetornaAttributesImpAtivar(Premise* premiseImp, 
                          std::string instName); 
 
 
std::string getInstanceCompleteName(Instance* instance); 
 
 
std::string getIncludeBlock(); 
 
 
void generateCode(); 
 
void generateCodeInstance(Instance *mainInstance); 
 
void generateAllPremises(Instance *mainInstance); 
 
void generateAllAttributes(Instance *mainInstance); 
 
void generateAllMethods(Instance *mainInstance); 
 
void generateAllRules(Instance *mainInstance); 
 
void generateBody(); 


218 
 
 
 
 
void generateCodeAttribute(ofstream& fileH, ofstream& fileCPP, Instance *instance,  
                                  int level); 
 
void generateCodeMethod(ofstream& fileH, ofstream& fileCPP, Instance *instance,  
                                  int level); 
 
void generateCodeRule(ofstream& fileH, ofstream& fileCPP, Instance *instance,  
                                  int level); 
 
void generateCodePremise(ofstream& fileH, ofstream& fileCPP, Instance *instance,  
                                  int level); 
 
 
void generatePremise(ofstream& fileCPP, ofstream& fileH, Premise *premise,  
                                  std::string instName, std::list<std::string>  
                                  names_rulesVinculadas, int subConds, int level); 
 
void generateInstigation(ofstream& fileCPP, ofstream& fileH, Instance *instance,  
                                  Rule *rule, int level); 
 
 
 
void assemble(); 
}; 
 
#endif /* NAMESPACES_2_0_COMPILER_H */ 
Fonte: Autoria própria 
 
Código 65 - Arquivo .cpp da classe NamespacesCompiler 
#include "generation/namespaces/NamespacesCompiler.h" 
 
#include "NOPGraph.h" 
 
#include "elements/Fbe.h" 
#include "elements/Instance.h" 
#include "elements/Attribute.h" 
#include "elements/Method.h" 
#include "elements/Premise.h" 
#include "elements/Subcondition.h" 
#include "elements/Condition.h" 
#include "elements/Rule.h" 
#include "elements/Action.h" 
#include "elements/Instigation.h" 
#include "elements/Expression.h" 
#include "elements/Factor.h" 
#include "elements/ElementFactor.h" 
#include "elements/Symbol.h" 
#include "elements/Type.h" 
#include "elements/Param.h" 
#include "elements/CodeBlock.h" 
#include "elements/Assignment.h" 
#include "elements/Target.h" 
#include "elements/Call.h" 
#include "elements/Conjunction.h" 
#include "elements/Argument.h" 
#include "elements/IncludeBlock.h" 
#include "elements/MainBlock.h" 
 
#include <string.h> 
#include <iostream> 
#include <fstream> 
#include <vector> 
#include <list> 
#include <map> 
 
// Function that returns the type of the Attribute 
std::string returnType(int attType) { 
    std::string ret = ""; 
    switch (attType) { 
 
case Type::BOOLEAN_TYPE: 


219 
 
 
 
    ret = "bool"; 
            break; 
        case Type::INTEGER_TYPE: 
            ret = "int"; 
            break; 
        case Type::DOUBLE_TYPE: 
            ret = "float"; 
            break; 
        case Type::STRING_TYPE: 
            ret = "std::string"; 
            break; 
        case Type::CHAR_TYPE: 
            ret = "char"; 
            break; 
        default: 
            ret = "undefined"; 
            break; 
    }//end switch 
    return ret; 
} 
 
// Function that returns the default type of the Attribute 
std::string returnDefault(short attType) { 
    std::string ret = ""; 
    switch (attType) { 
        case Type::BOOLEAN_TYPE: 
            ret = "false"; 
            break; 
        case Type::INTEGER_TYPE: 
            ret = "0"; 
            break; 
        case Type::DOUBLE_TYPE: 
            ret = "0.0"; 
            break; 
        case Type::STRING_TYPE: 
            ret = "\"\""; 
            break; 
        case Type::CHAR_TYPE: 
            ret = "\" \""; 
            break; 
        default: 
            ret = "null"; 
            break; 
    }//end switch 
    return ret; 
}     
 
// Function that returns the operator 
std::string returnOperation(short attOp) { 
    std::string ret = ""; 
    switch (attOp) { 
        case Symbol::EQUAL_SYMBOL: 
            ret = " == "; 
            break; 
        case Symbol::NOT_EQUAL_SYMBOL: 
            ret = " != "; 
            break; 
        case Symbol::LESSER_THAN_SYMBOL: 
            ret = " < "; 
            break; 
        case Symbol::GREATER_THAN_SYMBOL: 
            ret = " > "; 
            break; 
        case Symbol::LESS_OR_EQUAL_SYMBOL: 
            ret = " <= "; 
            break; 


220 
 
 
        case Symbol::GREATER_OR_EQUAL_SYMBOL: 
            ret = " >= "; 
            break; 
        default: 
            ret = "undefined"; 
            break; 
    }//end switch 
    return ret; 
} 
 
int NamespacesCompiler::VerificaPremiseRepetida(std::list<std::string> list_premises, 
std::string premiseName){ 
 
    for (std::list<std::string>::iterator itIni = list_premises.begin(); itIni!= 
list_premises.end(); ++itIni) { 
 
        if (strcmp(itIni->c_str(),premiseName.c_str())==0) return 0; // já existe na 
existe 
 
    } 
    return -1; 
} 
 
std::list<std::string> NamespacesCompiler::RetornaRulesVinculadas(std::string 
premise_Name, std::map<std::string, Rule*> *rules){ 
 
    std::list<std::string> lista_rulesVinculadas;    
    std::string ruleName = ""; 
 
    for (std::map<std::string, Rule*>::iterator it = rules->begin(); it != rules-
>end(); ++it) { 
        Rule *ruleAux = it->second; 
       // cout<<"Rule XXX: "<<ruleAux->getName()<<endl; 
 
        Condition *condition = ruleAux->getCondition(); 
 
        std::map<std::string, Subcondition*> *subConditions = condition-
>getSubconditions(); 
 
        if (subConditions->size() > 0) { 
            for (std::map<std::string, Subcondition*>::iterator it = subConditions-
>begin(); it != subConditions->end(); ++it) { 
 
                Subcondition *subCondition = it->second; 
 
                std::map<std::string, Premise*> *premises = subCondition-
>getPremises(); 
                for (std::map<std::string, Premise*>::iterator it = premises->begin(); 
it != premises->end(); ++it) { 
 
                    Premise *premise = it->second; 
                    std::string premiseName = premise->getName(); 
 
                    int aux = 10; 
                    aux =strcmp(premise_Name.c_str(),premiseName.c_str()); 
 
                    if (aux==0){ 
                        bool existe = 0; 
                        for (std::list<std::string>::iterator itIni = 
lista_rulesVinculadas.begin(); itIni!= lista_rulesVinculadas.end(); ++itIni) { 
 
                            if (strcmp(itIni->c_str(),ruleAux->getName().c_str())==0) { 
                                existe = 1; 
                            } 
 
                        } 


221 
 
 
                        if (existe == 0){ 
                            //cout<<"lista.add"<<ruleAux->getName()<<std::endl; 
                            lista_rulesVinculadas.push_back(ruleAux->getName()); 
                        } 
                    } 
                } 
            } 
 
        }else{ 
            std::map<std::string, Premise*> *premises = condition->getPremises(); 
            for (std::map<std::string, Premise*>::iterator it = premises->begin(); it 
!= premises->end(); ++it) { 
 
                Premise *premise = it->second; 
                std::string premiseName = premise->getName(); 
 
                int aux = 10; 
                aux =strcmp(premise_Name.c_str(),premiseName.c_str()); 
 
                if (aux==0){ 
                    bool existe = 0; 
                    for (std::list<std::string>::iterator itIni = 
lista_rulesVinculadas.begin(); itIni!= lista_rulesVinculadas.end(); ++itIni) { 
 
                        if (strcmp(itIni->c_str(),ruleAux->getName().c_str())==0) { 
                            existe = 1; 
                        } 
 
                    } 
                    if (existe == 0){ 
                        //cout<<"lista.add"<<ruleAux->getName()<<std::endl; 
                        lista_rulesVinculadas.push_back(ruleAux->getName()); 
                    } 
                } 
 
            } 
        } 
         
    } 
    cout<<std::endl; 
    return lista_rulesVinculadas; 
     
} 
 
std::list<std::string> NamespacesCompiler::RetornaAttributesImpAtivar(Premise* 
premiseImp, std::string instName){ 
     
    Condition* condition = premiseImp->getCondition(); 
    std::list<std::string> attributes_list; 
     
    std::map<std::string, Subcondition*> *subConditions = condition-
>getSubconditions(); 
    if (subConditions->size() > 0) { 
        for (std::map<std::string, Subcondition*>::iterator it = subConditions-
>begin(); it != subConditions->end(); ++it) { 
 
            Subcondition *subCondition = it->second; 
 
            std::map<std::string, Premise*> *premises = subCondition->getPremises(); 
            for (std::map<std::string, Premise*>::iterator it = premises->begin(); it 
!= premises->end(); ++it) { 
 
                Premise *premise = it->second; 
                 
                if(strcmp(premise->getName().c_str(),premiseImp-
>getName().c_str())!=0){ 


222 
 
 
 
                    Expression *expression = premise->getExpression(); 
                    Factor *leftFactor = expression->getLeftFactor(); 
                    if (leftFactor->getFactorId() == Factor::ELEMENT_FACTOR) { 
 
                        ElementFactor *element = (ElementFactor*)leftFactor; 
 
                        Attribute* att = element->getAttribute(); 
                        if(att != 0x0) { 
                            std::string attributeName = att->getName(); 
 
                            std::string path = "instance::main::" + instName +"::at::" 
+ attributeName + "::ativar(true);"; 
                            attributes_list.push_back(path); 
                        } 
                    } 
                } 
            } 
        } 
 
    }else{ 
         
        std::map<std::string, Premise*> *premises = condition->getPremises(); 
        for (std::map<std::string, Premise*>::iterator it = premises->begin(); it != 
premises->end(); ++it) { 
 
            Premise *premise = it->second; 
             
            std::cout<<premise->getName()<<std::endl; 
            std::cout<<premiseImp->getName()<<std::endl; 
            if(strcmp(premise->getName().c_str(),premiseImp->getName().c_str())!=0){ 
 
                 
                Expression *expression = premise->getExpression(); 
                Factor *leftFactor = expression->getLeftFactor(); 
                if (leftFactor->getFactorId() == Factor::ELEMENT_FACTOR) { 
 
                    ElementFactor *element = (ElementFactor*)leftFactor; 
                     
                    Attribute* att = element->getAttribute(); 
                    if(att != 0x0) { 
                        std::string attributeName = att->getName(); 
 
                        std::string path = "instance::main::" + instName +"::at::" + 
attributeName + "::ativar(true);"; 
                        attributes_list.push_back(path); 
                    } 
                } 
            } 
 
        } 
         
    } 
 
    return attributes_list; 
 
} 
 
bool NamespacesCompiler::ExistePremisesImpertinentes(Attribute *attribute){ 
 
    std::map<std::string, Premise*> *premises = attribute->getPremises(); 
    for (std::map<std::string, Premise*>::iterator it = premises->begin(); it != 
premises->end(); ++it) { 
 
        Premise *premise = it->second; 
        if(premise->getImpertinent() == true){ 


223 
 
 
            return true; 
        } 
 
    } 
    return false; 
} 
 
std::string NamespacesCompiler::getInstanceCompleteName(Instance* instance) { 
 
    std::string cmpInstName = instance->getName(); 
 
    if (cmpInstName == "this") { 
         
        cmpInstName = "main"; 
 
    } else { 
 
        while (instance->getParentInstance() != 0) { 
 
            if (instance->getParentInstance()->getName() == "this") { 
                cmpInstName = "main::" + cmpInstName; 
                break; 
            } 
 
            cmpInstName = instance->getParentInstance()->getName() + "::" + 
cmpInstName; 
 
            instance = instance->getParentInstance(); 
 
        } 
 
    } 
 
    return cmpInstName; 
 
} 
 
std::string NamespacesCompiler::getIncludeBlock() { 
 
    Fbe *fbe = graph->getFbeMainInstance()->getFbe(); 
 
    std::map<std::string, IncludeBlock*> *includes = fbe->getIncludes(); 
 
    if (includes != 0) { 
 
        for (std::map<std::string, IncludeBlock*>::iterator it = includes->begin(); it 
!= includes->end(); ++it) { 
         
            IncludeBlock *include = it->second; 
 
            if (include->getTarget()->getTargetId() == Target::NAMESPACES_TARGET) { 
 
                return include->getCode(); 
 
            } 
 
        } 
 
    } 
 
    return ""; 
 
} 
 
void NamespacesCompiler::generateCode() { 
 


224 
 
 
    generateCodeInstance(graph->getFbeMainInstance()); 
     
    generateBody(); 
 
} 
 
void NamespacesCompiler::generateCodeInstance(Instance *mainInstance) { 
 
    // Attributes 
    generateAllAttributes(mainInstance); 
     
    // Methods 
    generateAllMethods(mainInstance); 
     
    // Rules 
    generateAllRules(mainInstance); 
     
    // Premises 
    generateAllPremises(mainInstance); 
 
} 
 
void NamespacesCompiler::generateAllAttributes(Instance *mainInstance) { 
 
    std::cout << "generateAllAttributes" << std::endl; 
 
    //creation instances.h file 
    ofstream fileH; 
    std::string filenameH = "Generated/instances.h"; 
    fileH.open(filenameH.c_str(), ios::out); 
    fileH << "#pragma once" << std::endl; 
    fileH << "#include <string>" << std::endl; 
    fileH << "#include <iostream>" << std::endl; 
    fileH << "namespace instance {" << std::endl; 
 
    //Creation of instances.cpp file 
    ofstream fileCPP; 
    std::string filenameCPP = "Generated/instances.cpp"; 
    fileCPP.open(filenameCPP.c_str(), ios::out); 
    fileCPP << "#include \"instances.h\"" << std::endl; 
    fileCPP << "#include \"premises.h\"" << std::endl; 
    fileCPP << "#include <string>" << std::endl; 
    fileCPP << "#include <iostream>" << std::endl; 
 
    fileCPP << getIncludeBlock() << std::endl; 
 
    fileCPP << "namespace instance {" << std::endl; 
 
    generateCodeAttribute(fileCPP, fileH, mainInstance, 0); 
     
    fileH << "}"<< std::endl;// end of at namespace 
    fileH.close(); 
    fileCPP << "}"<< std::endl;// end of at namespace 
    fileCPP.close(); 
} 
 
void NamespacesCompiler::generateCodeAttribute(ofstream& fileCPP, ofstream& fileH, 
Instance *instance, int level) { 
 
    std::cout << "generateCodeAttribute: " << instance->getName() << std::endl; 
 
    std::string tab = getLevel(level); 
    std::string tabImp = ""; 
 
    std::string instName = ""; 
 


225 
 
 
    if (instance->getName() != "this") { 
        instName = instance->getName(); 
    } else { 
        instName = "main";  
    } 
 
    fileH << tab << "\tnamespace "<< instName <<" {" << std::endl; 
    fileCPP << tab << "\tnamespace " << instName << " {" << std::endl; 
 
    std::map<std::string, Attribute*> *attributes = instance->getAttributes(); 
    for (std::map<std::string, Attribute*>::iterator it = attributes->begin(); it != 
attributes->end(); ++it) { 
 
        Attribute *attribute = it->second; 
 
        std::cout << "Attribute: " << attribute->getName() << std::endl; 
 
        bool temPremisesImpertinentes = ExistePremisesImpertinentes(attribute); 
 
        fileH << tab << "\t\tnamespace at {" << std::endl; 
        fileH << tab << "\t\t\tnamespace "<< attribute->getName() << " {" << std::endl; 
        fileH << tab << "\t\t\t\textern "<< returnType(attribute->getType()-
>getTypeId()) <<" value;" << std::endl; 
 
        if(temPremisesImpertinentes == true){ 
            fileH << tab << "\t\t\t\textern bool ativado;" << std::endl; 
        } 
 
        fileH << tab << "\t\t\t\textern void setValue("<< returnType(attribute-
>getType()->getTypeId()) <<" newValue);" << std::endl; 
        fileH << tab << "\t\t\t}"<< std::endl; 
        fileH << tab << "\t\t}"<< std::endl; 
 
        fileCPP << tab << "\t\tnamespace at {" << std::endl; 
        fileCPP << tab << "\t\t\tnamespace " << attribute->getName() << " {" << 
std::endl; 
 
        fileCPP << tab << "\t\t\t\t" << returnType(attribute->getType()->getTypeId()) 
<< " value = " << attribute->getFactor()->getStringValue() << ";" << std::endl; 
         
        if(temPremisesImpertinentes == true){ 
            fileCPP << tab << "\t\t\t\tbool ativado = false;" << std::endl; 
        } 
         
        fileCPP << tab << "\t\t\t\tvoid setValue("<< returnType(attribute->getType()-
>getTypeId()) << " newValue) {" << std::endl; 
         
        if(temPremisesImpertinentes == true){ 
            fileCPP << tab << "\t\t\t\t\tif (ativado == true) {" << std::endl; 
            tabImp = "\t"; 
        } 
         
        fileCPP << tab << tabImp << tabImp << "\t\t\t\t\tif (value != newValue) {" << 
std::endl; 
        fileCPP << tab << tabImp << "\t\t\t\t\t\tvalue = newValue;" << std::endl; 
 
        std::map<std::string, Premise*> *premises = attribute->getPremises(); 
        int totalPremises = premises->size(); 
        int totalPremisesImp = 0; 
        int premisesCounter = 0; 
        for (std::map<std::string, Premise*>::iterator it = premises->begin(); it != 
premises->end(); ++it) { 
 
            premisesCounter++; 
 
            Premise *premise = it->second; 


226 
 
 
             
            std::string cmpInstName = getInstanceCompleteName(premise-
>getParentInstance()); 
            std::string cmp1st_att = ""; 
 
            bool isImpertinent = premise->getImpertinent(); 
 
            Expression *expression = premise->getExpression(); 
            Factor *leftFactor = expression->getLeftFactor(); 
 
            if (leftFactor->getFactorId() == Factor::ELEMENT_FACTOR) { 
 
                ElementFactor *element = (ElementFactor*)leftFactor; 
                cmp1st_att = element->getInstance()->getName(); 
                cmp1st_att = cmp1st_att + "_"; 
                cmp1st_att = cmp1st_att + element->getAttribute()->getName(); 
 
                fileCPP << tab << tabImp << "\t\t\t\t\t"; 
                 
                if(isImpertinent){ 
                    totalPremisesImp++; 
 
                    for(int i = 0; i < totalPremisesImp; i++){ 
                        fileCPP << "\t"; 
                    } 
                    if (premisesCounter != totalPremises){ 
                        fileCPP << "if("; 
                    } 
                    else{ 
                        fileCPP << "bool finalRule = "; 
                    } 
                } 
                else{ 
                    for(int i = 0; i < totalPremisesImp; i++){ 
                        fileCPP << "\t"; 
                    } 
                    fileCPP << "\t"; 
                } 
 
                //debug 
                //fileCPP << tab << "\t\t\t\t\t\tstd::cout << 
\"premise::"<<cmpInstName<<"::"<<premise-
>getName()<<"::notify_"<<cmp1st_att<<"(newValue)\" << std::endl;"<< std::endl; 
                fileCPP << "premise::"<<cmpInstName<<"::"<<premise-
>getName()<<"::notify_"<<cmp1st_att<<"(newValue)"; 
 
                if (premise->getImpertinent() && premisesCounter != totalPremises){ 
                    fileCPP << " == false){" << std::endl; 
                } 
                else{ 
                    fileCPP << ";" << std::endl; 
                } 
 
                init_premises.push_back("premise::" + cmpInstName + "::" + premise-
>getName() + "::notify_" + cmp1st_att + "(" + attribute->getFactor()->getStringValue() 
+ ");"); 
 
            } 
 
        } 
 
        int contador = totalPremisesImp; 
        premisesCounter = totalPremises; 
        for (std::map<std::string, Premise*>::iterator itPremiseImp = premises->end(); 
itPremiseImp != premises->begin(); --itPremiseImp) { 
 


227 
 
 
            if(itPremiseImp != premises->end()){ 
 
                Premise *premise = itPremiseImp->second; 
                if(premise->getImpertinent() ){ 
                    if(premisesCounter != totalPremises){ 
                        fileCPP << tab << "\t\t\t\t\t"; 
                        for(int i = contador; i > 0; i--){ 
                            fileCPP << "\t"; 
                        } 
                        fileCPP << "}" << std::endl; 
                    } 
                    contador--; 
                } 
                premisesCounter--;     
            } 
        } 
        if (contador == 1){ 
            fileCPP << tab << tabImp << "\t\t\t\t\t\t}" << std::endl;; 
        } 
 
        fileCPP << tab << tabImp << "\t\t\t\t\t}" << std::endl;//end if 
 
        if(temPremisesImpertinentes == true){ 
            fileCPP << tab << "\t\t\t\t\t}" << std::endl; 
        } 
 
        fileCPP << tab << "\t\t\t\t}" << std::endl;// end setValue function 
        if(temPremisesImpertinentes == true){ 
            fileCPP << tab << "\t\t\t\tvoid ativar(bool value) {" << std::endl; 
            fileCPP << tab << "\t\t\t\t\tativado = value;" << std::endl; 
            fileCPP << tab << "\t\t\t\t}" << std::endl; 
 
            fileH << tab << "\t\t\extern void ativar(bool value);" << std::endl; 
        } 
        fileCPP << tab << "\t\t\t}" << std::endl;// end of attribute 
        fileCPP << tab << "\t\t}"<< std::endl;// end of at 
         
    } 
 
    level++; 
 
    std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
 
    if (otherInsts->size() > 0) { 
 
        // loop para serem implementadas as premises das instances 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it != 
otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;      // otherInst -> corresponde a 
"instances das instances" 
             
            if (otherInst->getName() != "this") { 
 
                generateCodeAttribute(fileCPP, fileH, otherInst, level); 
 
            } 
 
        } 
 
    } 
     
 
    fileH << tab << "\t}"<< std::endl;// end of instance 
    fileCPP << tab << "\t}"<< std::endl;// end of instance 
     


228 
 
 
} 
 
void NamespacesCompiler::generateAllPremises(Instance *mainInstance) { 
 
    std::cout << "generateAllPremises" << std::endl; 
 
 
    //creation premises.h file 
    ofstream fileH; 
    std::string filenameH = "Generated/premises.h"; 
    fileH.open(filenameH.c_str(), ios::out); 
    fileH << "#pragma once" << std::endl; 
    fileH << "#include <string>" << std::endl; 
    fileH << "#include <iostream>" << std::endl; 
    fileH << "namespace premise {" << std::endl; 
 
    //Creation of premises.cpp file 
    ofstream fileCPP; 
    std::string filenameCPP = "Generated/premises.cpp"; 
    fileCPP.open(filenameCPP.c_str(), ios::out); 
    fileCPP << "#include \"premises.h\"" << std::endl; 
    fileCPP << "#include \"rules.h\"" << std::endl; 
    fileCPP << "#include <string>" << std::endl; 
    fileCPP << "#include <iostream>" << std::endl; 
 
    fileCPP << getIncludeBlock() << std::endl; 
 
    fileCPP << "namespace premise {" << std::endl; 
 
    // implementation of fbe main premises 
    generateCodePremise(fileCPP, fileH, mainInstance, 0); 
     
    fileCPP << "}"<<std::endl; // end of pr namespace 
    fileCPP.close(); 
     
    fileH << "}"<<std::endl; // end of pr namespace 
    fileH.close(); 
 
} 
 
void NamespacesCompiler::generateCodePremise(ofstream& fileCPP, ofstream& fileH, 
Instance *instance, int level) { 
 
 
    std::cout << "generateCodePremise: " << instance->getName() << std::endl; 
 
    std::string tab = getLevel(level); 
 
    int subConds = 0; 
    std::string ruleName = ""; 
    std::string instName = ""; 
 
    if (instance->getName() != "this") { 
        instName = instance->getName(); 
    } else { 
        instName = "main";  
    } 
     
    std::map<std::string, Rule*> *rules = instance->getRules(); 
    std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
 
    if (rules->size() > 0 || otherInsts->size() > 0) { 
 
        fileH << tab << "\tnamespace "<< instName <<" {" << std::endl; 
        fileCPP << tab << "\tnamespace " << instName << " {" << std::endl; 
 
        std::string cmpInstName = getInstanceCompleteName(instance); 
        std::list<std::string> names_premise; 


229 
 
 
        std::list<std::string> names_rulesVinculadas; 
         
        for (std::map<std::string, Rule*>::iterator it = rules->begin(); it != rules-
>end(); ++it) { 
 
            Rule *rule = it->second; 
 
            subConds = 0; 
            ruleName = rule->getName(); 
            //cout<<"Nome da Rule: "<<ruleName<<endl; 
 
            Condition *condition = rule->getCondition(); 
 
            std::map<std::string, Subcondition*> *subConditions = condition-
>getSubconditions(); 
 
            if (subConditions->size() > 0) { 
 
                for (std::map<std::string, Subcondition*>::iterator it = subConditions-
>begin(); it != subConditions->end(); ++it) { 
                     
                    subConds++; 
 
                    Subcondition *subCondition = it->second; 
 
                    std::map<std::string, Premise*> *premises = subCondition-
>getPremises(); 
                    for (std::map<std::string, Premise*>::iterator it = premises-
>begin(); it != premises->end(); ++it) { 
                     
                        Premise *premise = it->second; 
                        std::string premiseName = premise->getName(); 
                         
                        names_rulesVinculadas.clear(); 
                        names_rulesVinculadas = RetornaRulesVinculadas(premiseName, 
rules); 
                         
                        int premiseNova = VerificaPremiseRepetida(names_premise, 
premiseName); 
                        if(premiseNova != 0){ 
                            generatePremise(fileCPP, fileH, premise, cmpInstName, 
names_rulesVinculadas, subConds, level); 
                            names_premise.push_back(premise->getName()); 
                        } 
 
                    } 
                }     
 
            } else { 
 
                std::map<std::string, Premise*> *premises = condition->getPremises(); 
                for (std::map<std::string, Premise*>::iterator it = premises->begin(); 
it != premises->end(); ++it) { 
                     
                    Premise *premise = it->second; 
                    std::string premiseName = premise->getName(); 
                    //cout<<"Nome da Premise: "<<premiseName<<endl; 
 
                    names_rulesVinculadas.clear(); 
                    names_rulesVinculadas = RetornaRulesVinculadas(premiseName, rules); 
                         
                    int premiseNova = VerificaPremiseRepetida(names_premise, 
premiseName); 
                    if(premiseNova != 0){ 
                        generatePremise(fileCPP, fileH, premise, cmpInstName, 
names_rulesVinculadas, subConds, level); 


230 
 
 
                        names_premise.push_back(premise->getName()); 
                    } 
                } 
 
            } 
 
        } 
 
        level++; 
 
        // loop para serem implementadas as premises das instances 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it != 
otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;      // otherInst -> corresponde a 
"instances das instances" 
 
            if (otherInst->getName() != "this") { 
 
                generateCodePremise(fileCPP, fileH, otherInst, level); 
 
            } 
 
        } 
 
        fileH << tab << "\t}" << std::endl; 
        fileCPP << tab << "\t}" << std::endl; 
 
    } 
 
} 
 
void NamespacesCompiler::generatePremise(ofstream& fileCPP, ofstream& fileH, Premise 
*premise, std::string instName, std::list<std::string> names_rulesVinculadas, int 
subConds, int level) { 
 
 
    //std::cout << "generatePremise: " << premise->getName() << " from " << ruleName << 
std::endl; 
 
    std::string tab = getLevel(level); 
 
    fileCPP << tab << "\t\tnamespace " << premise->getName() << " {" << std::endl; 
    fileH << tab << "\t\tnamespace " << premise->getName() << " {" << std::endl; 
 
 
    std::string methodCallInc = ""; 
    std::string methodCallDec = ""; 
    std::string methodCallEql = ""; 
    std::list<std::string> methodCallIncList; 
    std::list<std::string> methodCallDecList; 
    std::list<std::string> methodCallEqlList; 
     
 
std::string leftValue = ""; 
    std::string rightValue = ""; 
    std::string cmpOp = ""; 
 
 
std::string preLogicalValue = ""; 
 
    std::string cmpAttType = ""; 
    std::string cmp1st_att = ""; 
    std::string cmpInstName = ""; 
 
 
    Expression *expression = premise->getExpression(); 
    Factor *leftFactor = expression->getLeftFactor(); 
 
    bool isUniquePremise = premise->getUnique(); 
 


231 
 
 
    std::list<std::string> attributes_ativar; 
    if (premise->getImpertinent()){ 
        attributes_ativar = RetornaAttributesImpAtivar(premise, instName); 
    } 
 
 
    if (leftFactor->getFactorId() == Factor::ELEMENT_FACTOR) { 
 
        ElementFactor *element = (ElementFactor*)leftFactor; 
 
        cmp1st_att = element->getInstance()->getName();  
 
        cmp1st_att = cmp1st_att + "_"; 
        cmp1st_att = cmp1st_att + element->getAttribute()->getName(); 
        cmpAttType = returnType(element->getAttribute()->getType()->getTypeId()); 
 
 
 
leftValue = element->getAttribute()->getFactor()->getStringValue(); 
 
    } else { 
 
 
 
leftValue = leftFactor->getStringValue(); 
 
 
} 
 
 
Factor *rightFactor = expression->getRightFactor(); 
 
 
if (rightFactor->getFactorId() == Factor::ELEMENT_FACTOR) { 
 
        ElementFactor *element = (ElementFactor*)rightFactor; 
 
 
 
rightValue = element->getAttribute()->getFactor()->getStringValue(); 
 
    } else { 
 
 
 
rightValue = rightFactor->getStringValue(); 
 
 
} 
 
    cmpOp = returnOperation(expression->getSymbol()->getSymbolId()); 
 
 
preLogicalValue = (premise->getInitialLogicalValue() ? "true" : "false"); 
 
    // Construção da chamada do namespace das rules 
    for (std::list<std::string>::iterator itIni = names_rulesVinculadas.begin(); 
itIni!= names_rulesVinculadas.end(); ++itIni) { 
 
        std::string ruleName = itIni->c_str(); 
        methodCallInc = "rule::" + instName + "::" + ruleName + "::inc"; 
        methodCallDec = "rule::" + instName + "::" + ruleName + "::dec"; 
        methodCallEql = "rule::" + instName + "::" + ruleName + "::eql"; 
     
        // quando (subConds != 0) significa que há subConditions: neste caso, para cada 
subCondition é criado um método inc() e dec() 
        // enumerando esses métodos de acordo com o valor do contador subConds 
        // quando (subConds = 0) significa que na estrutura do fbe, sas conditions 
segue direto para as premises... sem subcondition 
        if (subConds != 0) { 
            char buf[3]; 
 
            sprintf(buf, "%i", subConds);  // convertendo o valor de subConds para 
string 
 
            methodCallInc = methodCallInc + buf; 
            methodCallDec = methodCallDec + buf;   
            methodCallEql = methodCallEql + buf; 
        } 
 


232 
 
 
        methodCallInc = methodCallInc + "();"; 
        methodCallIncList.push_back(methodCallInc); 
 
        methodCallDec = methodCallDec + "();"; 
        methodCallDecList.push_back(methodCallDec); 
 
        methodCallEql = methodCallEql + "();"; 
        methodCallEqlList.push_back(methodCallEql); 
 
    } 
     
    //fileH << tab << "\t\t\tint impertinent = " << premise->getImpertinent() << ";" << 
std::endl; 
    fileH << tab << "\t\t\textern bool state;" << std::endl; 
    fileH << tab << "\t\t\textern " << cmpAttType << " cpy1st, cpy2nd;" << std::endl; 
     
    std::string typeMethod = "void"; 
    if(premise->getImpertinent()){ 
        typeMethod = "bool"; 
    } 
     
    fileH << tab << "\t\t\textern " + typeMethod + " compare();" << std::endl; 
    fileH << tab << "\t\t\textern " + typeMethod + " 
notify_"<<cmp1st_att<<"("<<cmpAttType<< " newValue);" << std::endl; 
 
    fileCPP << tab << "\t\t\tint impertinent = " << premise->getImpertinent() << ";" << 
std::endl; 
    fileCPP << tab << "\t\t\tbool state = (" << preLogicalValue << ");" << std::endl; 
     
 
fileCPP << tab << "\t\t\t" << cmpAttType << " cpy1st = " << leftValue << ";" << 
std::endl; 
 
fileCPP << tab << "\t\t\t" << cmpAttType << " cpy2nd = " << rightValue << ";" << 
std::endl; 
     
    fileCPP << tab << "\t\t\t" + typeMethod + " compare() {"<< std::endl; 
    fileCPP << tab << "\t\t\t\tif (cpy1st"<< cmpOp <<"cpy2nd) {"<< std::endl; 
    fileCPP << tab << "\t\t\t\t\tif (state == false) {"<< std::endl; 
    fileCPP << tab << "\t\t\t\t\t\tstate = true;"<< std::endl; 
    //fileCPP << tab << "\t\t\t\t\t\tstd::cout << \""<< methodCallInc << "\" << 
std::endl;" << std::endl; 
 
    int totalRules = methodCallIncList.size(); 
    int rulesCounter = 0; 
    for (std::list<std::string>::iterator itIni = methodCallIncList.begin(); itIni!= 
methodCallIncList.end(); ++itIni) { 
 
        rulesCounter++; 
        fileCPP << tab << "\t\t\t\t\t"; 
        if(isUniquePremise){ 
             
            for(int i = 0; i < rulesCounter; i++){ 
                fileCPP << "\t"; 
            } 
            if(rulesCounter != totalRules){ 
                fileCPP << "if ("<< itIni->c_str() << " != false){" << std::endl; 
            }else{ 
                fileCPP << "bool result" << rulesCounter << " = " << itIni->c_str() << 
";" << std::endl; 
            } 
             
        } 
        else{ 
            fileCPP << "bool result" << rulesCounter << " = " << itIni->c_str() << ";" 
<< std::endl; 
        } 
 


233 
 
 
    } 
 
    if(isUniquePremise){ 
 
        for(int i = rulesCounter; i > 0; i--){ 
            fileCPP << tab << "\t\t\t\t"; 
 
            for(int j = rulesCounter; j > 0; j--){ 
                fileCPP << "\t"; 
                if(j == 1){ 
                    if(i == 1){ 
                       fileCPP << "}else{" << std::endl;  
                    } 
                    else{ 
                        fileCPP << "}" << std::endl; 
                    } 
                } 
            } 
        } 
 
    }else{ 
        fileCPP << tab << "\t\t\t\t\t} else {" << std::endl; 
    } 
     
    rulesCounter = 0; 
    for (std::list<std::string>::iterator itIni = methodCallEqlList.begin(); itIni!= 
methodCallEqlList.end(); ++itIni) { 
 
        rulesCounter++; 
        fileCPP << tab << "\t\t\t\t\t"; 
        if(isUniquePremise){ 
             
            for(int i = 0; i < rulesCounter; i++){ 
                fileCPP << "\t"; 
            } 
            if(rulesCounter != totalRules){ 
                fileCPP << "if ("<< itIni->c_str() << " != false){" << std::endl; 
            }else{ 
                fileCPP << "bool result" << rulesCounter << " = " << itIni->c_str() << 
";" << std::endl; 
            } 
             
        } 
        else{ 
            fileCPP << "bool result" << rulesCounter << " = " << itIni->c_str() << ";" 
<< std::endl; 
        } 
 
    } 
    if(isUniquePremise){ 
 
        for(int i = rulesCounter; i > 0; i--){ 
            fileCPP << tab << "\t\t\t\t"; 
 
            for(int j = rulesCounter; j > 0; j--){ 
                fileCPP << "\t"; 
                if(j == 1){ 
                    fileCPP << "}" << std::endl; 
                } 
            } 
        } 
 
    }else{ 
        fileCPP << tab << "\t\t\t\t\t}" << std::endl; 
    } 
     


234 
 
 
    if (premise->getImpertinent()){ 
 
        if(attributes_ativar.size() > 0){ 
 
            for (std::list<std::string>::iterator itIni = attributes_ativar.begin(); 
itIni!= attributes_ativar.end(); ++itIni) { 
 
                fileCPP << tab << "\t\t\t\t\t" << itIni->c_str() << std::endl; 
 
            } 
        } 
 
        fileCPP << tab << "\t\t\t\t\treturn true;" << std::endl; 
    } 
    fileCPP << tab << "\t\t\t\t} else {" << std::endl; 
    fileCPP << tab << "\t\t\t\t\tif (state == true) {"<< std::endl; 
    fileCPP << tab << "\t\t\t\t\t\tstate = false;"<< std::endl; 
    //fileCPP << tab << "\t\t\t\t\t\tstd::cout << \""<< methodCallDec << "\" << 
std::endl;" << std::endl; 
 
    for (std::list<std::string>::iterator itIni = methodCallDecList.begin(); itIni!= 
methodCallDecList.end(); ++itIni) { 
 
        fileCPP << tab << "\t\t\t\t\t\t"<< itIni->c_str() << std::endl; 
 
    } 
     
    fileCPP << tab << "\t\t\t\t\t}" << std::endl; 
    if (premise->getImpertinent()){ 
        fileCPP << tab << "\t\t\t\t\treturn false;" << std::endl; 
    } 
    fileCPP << tab << "\t\t\t\t}" << std::endl; 
    fileCPP << tab << "\t\t\t}" << std::endl; 
    fileCPP << tab << "\t\t\t" + typeMethod + " notify_"<<cmp1st_att<<"("<<cmpAttType<< 
" newValue) {" << std::endl; 
    fileCPP << tab << "\t\t\t\tcpy1st = newValue;" << std::endl; 
 
    fileCPP << tab << "\t\t\t\t"; 
    if (premise->getImpertinent()) { 
        fileCPP << "return "; 
    } 
    fileCPP << "compare();" << std::endl; 
 
    fileCPP << tab << "\t\t\t}" << std::endl; 
    fileCPP << tab << "\t\t}" << std::endl; 
    fileH << tab << "\t\t}" << std::endl; 
} 
 
void NamespacesCompiler::generateAllMethods(Instance *mainInstance) { 
 
 
    std::cout << "generateAllMethods" << std::endl; 
     
    //creation methods.h file 
    ofstream fileH; 
    std::string filenameH = "Generated/methods.h"; 
    fileH.open(filenameH.c_str(), ios::out); 
    fileH << "#pragma once" << std::endl; 
    fileH << "#include <string>" << std::endl; 
    fileH << "#include <iostream>" << std::endl; 
    fileH << "namespace method {" << std::endl; 
 
    //Creation of methods.cpp file 
    ofstream fileCPP; 
    std::string filenameCPP = "Generated/methods.cpp"; 
    fileCPP.open(filenameCPP.c_str(), ios::out); 
    fileCPP << "#include \"methods.h\"" << std::endl; 


235 
 
 
    fileCPP << "#include \"instances.h\"" << std::endl; 
    fileCPP << "#include <string>" << std::endl; 
    fileCPP << "#include <iostream>" << std::endl; 
 
    fileCPP << getIncludeBlock() << std::endl; 
 
    fileCPP << "namespace method {" << std::endl; 
 
    fileH << "\tnamespace main {" << std::endl; 
 
fileCPP << "\tnamespace main {" << std::endl; 
 
    // implementação dos method do fbe main 
    generateCodeMethod(fileCPP, fileH, mainInstance, 0); 
 
    fileCPP << "\t}"<< std::endl;// end of method 
    fileH << "\t}"<< std::endl;// end of method 
 
    fileH << "}"<< std::endl;// end of mt namespace 
    fileH.close(); 
    fileCPP << "}"<< std::endl;// end of mt namespace 
    fileCPP.close(); 
 
} 
 
void NamespacesCompiler::generateCodeMethod(ofstream& fileCPP, ofstream& fileH, 
Instance *instance, int level) { 
 
 
    std::cout << "generateCodeMethod: " << instance->getName() << std::endl; 
 
 
std::string tab = getLevel(level); 
 
    std::map<std::string, Method*> *methods = instance->getMethods(); 
 
    if (methods->size() > 0) { 
 
 
 
if (instance->getName() != "this") { 
 
 
 
fileH << tab << "\tnamespace " << instance->getName()<<" {" << 
std::endl; 
 
 
 
fileCPP << tab << "\tnamespace " << instance->getName() << " {" << 
std::endl; 
 
 
}/* else { 
 
 
 
fileH << tab << "\tnamespace main {" << std::endl; 
 
 
 
fileCPP << tab << "\tnamespace main {" << std::endl; 
 
 
}*/ 
 
 
 
        for (std::map<std::string, Method*>::iterator it = methods->begin(); it != 
methods->end(); ++it) { 
             
            Method *method = it->second; 
 
 
 
 
fileH << tab << "\t\tnamespace "<< method->getName()<<" {" << 
std::endl; 
 
 
 
fileCPP << tab << "\t\tnamespace " << method->getName() << " {" << 
std::endl; 
 
 
 
 
            std::string paramsCode = ""; 
            int countParams = 0; 
 
            std::map<std::string, Param*> *params = method->getParams(); 
            countParams = params->size(); 
            for (std::map<std::string, Param*>::iterator it = params->begin(); it != 
params->end(); ++it) { 
 
                Param *param = it->second; 
                paramsCode = paramsCode + returnType(param->getType()->getTypeId()) + " 
" + param->getName(); 


236 
 
 
                 
                //*** XXX Alteração methods-params XXX ***// 
                /*if (countParams > 1){ 
                    paramsCode = paramsCode + ", "; 
                } 
                countParams--;*/ 
            }  
 
            std::map<std::string, CodeBlock*> *codeBlocks = method->getCodeBlocks(); 
            for (std::map<std::string, CodeBlock*>::iterator it = codeBlocks->begin(); 
it != codeBlocks->end(); ++it) { 
                 
                CodeBlock *codeBlock = it->second; 
                 
                fileH << tab << "\t\t\tvoid " << method-
>getName()<<"("<<paramsCode<<");" << std::endl; 
                fileCPP << tab << "\t\t\tvoid " << method-
>getName()<<"("<<paramsCode<<") {" << std::endl; 
                 
                fileCPP << tab << "\t\t\t\t" << codeBlock->getCode() << std::endl; 
 
                fileCPP << tab << "\t\t\t}" << std::endl; 
 
            } 
 
            std::map<std::string, Assignment*> *assignments = method->getAssignments(); 
            for (std::map<std::string, Assignment*>::iterator it = assignments-
>begin(); it != assignments->end(); ++it) { 
 
                Assignment *assignment = it->second; 
                Factor *factor = assignment->getFactor(); 
                 
                ElementFactor *element =  assignment->getElement(); 
 
                Attribute *att = element->getAttribute(); 
 
                if(att != 0x0) { 
                    std::string typeName = returnType(att->getType()->getTypeId()); 
 
                    std::string cmpInstName = getInstanceCompleteName(att-
>getParentInstance()); 
 
                    fileCPP << tab << "\t\t\tvoid " << method->getName() << "() {" << 
std::endl; 
 
                    //fileCPP << tab << "\t\t\t\tstd::cout << \"" << method->getName() 
<< "\" << std::endl;" << std::endl; 
                    fileCPP << tab << "\t\t\t\tinstance::" << cmpInstName << "::at::" 
<< element->getAttributeName() << "::setValue(" << factor->getStringValue() << ");" << 
std::endl; 
                    fileCPP << tab << "\t\t\t}" << std::endl; 
 
                    fileH << tab << "\t\t\textern void " << method->getName() << "();" 
<< std::endl; 
                } 
                 
            } 
 
            fileCPP << tab << "\t\t}"<< std::endl;// end of at namespace 
            fileH << tab << "\t\t}"<< std::endl; 
 
        } 
         
        level++; 
 
        // loop para serem implementadas os methods das instances 


237 
 
 
        std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it != 
otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;      // otherInst -> corresponde a 
"instances das instances" 
            if (otherInst->getName() != "this") { 
 
                generateCodeMethod(fileCPP, fileH, otherInst, level); 
 
            } 
 
        } 
 
        if (instance->getName() != "this") { 
 
 
 
fileCPP << tab << "\t}"<< std::endl;// end of method 
            fileH << tab << "\t}"<< std::endl;// end of method 
 
 
} 
 
    }else{ 
        // loop para serem implementadas os methods das instances 
        std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it != 
otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;      // otherInst -> corresponde a 
"instances das instances" 
            if (otherInst->getName() != "this") { 
 
                generateCodeMethod(fileCPP, fileH, otherInst, 1); 
 
            } 
 
        } 
    } 
 
} 
 
void NamespacesCompiler::generateAllRules(Instance *mainInstance) { 
 
    std::cout << "generateAllRules" << std::endl; 
     
    //creation rules.h file 
    ofstream fileH; 
    std::string filenameH = "Generated/rules.h"; 
    fileH.open(filenameH.c_str(), ios::out); 
    fileH << "#pragma once" << std::endl; 
    fileH << "#include <string>" << std::endl; 
    fileH << "#include <iostream>" << std::endl; 
    fileH << "namespace rule {" << std::endl; 
 
    //Creation of rules.cpp file 
    ofstream fileCPP; 
    std::string filenameCPP = "Generated/rules.cpp"; 
    fileCPP.open(filenameCPP.c_str(), ios::out); 
    fileCPP << "#include \"rules.h\"" << std::endl; 
    fileCPP << "#include \"methods.h\"" << std::endl; 
    fileCPP << "#include \"instances.h\"" << std::endl; 
    fileCPP << "#include <string>" << std::endl; 
    fileCPP << "#include <iostream>" << std::endl; 
    fileCPP << getIncludeBlock() << std::endl; 
 
    fileCPP << "namespace rule {" << std::endl; 
 
    fileH << "\tnamespace main {" << std::endl; 
    fileCPP << "\tnamespace main {" << std::endl; 


238 
 
 
 
    // implementação das rules do fbe main 
    generateCodeRule(fileCPP, fileH, mainInstance, 0); 
 
    fileH << "\t}" << std::endl; 
    fileCPP << "\t}" << std::endl; 
 
    fileH << "}"<<std::endl;// end of rl namespace 
    fileH.close(); 
    fileCPP << "}"<<std::endl;// end of rl namespace 
    fileCPP.close(); 
 
} 
 
void NamespacesCompiler::generateCodeRule(ofstream& fileCPP, ofstream& fileH, Instance 
*instance, int level) { 
 
    std::cout << "generateCodeRule: " << instance->getName() << std::endl; 
 
    std::string tab = getLevel(level); 
 
    std::map<std::string, Rule*> *rules = instance->getRules(); 
 
    if (rules->size() > 0) { 
 
        if (instance->getName() != "this") { 
            fileH << tab << "\tnamespace "<< instance->getName()<<" {" << std::endl; 
            fileCPP << tab << "\tnamespace " << instance->getName() << " {" << 
std::endl; 
        } 
        /*else{ 
            fileH << tab << "\tnamespace main {" << std::endl; 
            fileCPP << tab << "\tnamespace main {" << std::endl; 
        }*/ 
 
        for (std::map<std::string, Rule*>::iterator it = rules->begin(); it != rules-
>end(); ++it) {  
 
            Rule *rule = it->second; 
 
            fileH << tab << "\t\tnamespace " << rule->getName() << " {" << std::endl; 
            fileCPP << tab << "\t\tnamespace " << rule->getName() << " {" << std::endl; 
 
            Condition *condition = rule->getCondition(); 
                 
            std::map<std::string, Subcondition*> *subconditions = condition-
>getSubconditions(); 
            if (subconditions->size() > 0) { 
 
                int i = 0; 
                std::vector<std::string> list_exprConjunction; 
                std::vector<int> list_numPremises; 
 
                // declaração das variaveis para cada subcondition 
                for (std::map<std::string, Subcondition*>::iterator it = subconditions-
>begin(); it != subconditions->end(); ++it) { 
 
 
 
 
 
 
Subcondition *subcondition = it->second; 
 
                    i++; 
 
                    fileH << tab << "\t\t\textern int count" << i << ";" << std::endl; 
                    fileH << tab << "\t\t\textern bool status" << i << ";" << 
std::endl; 
                    fileCPP << tab << "\t\t\tint count" << i << " = " << subcondition-
>getNumberApprovedPremises() << ";" << std::endl; 


239 
 
 
                    fileCPP << tab << "\t\t\tbool status" << i << ";" << std::endl; 
 
                    Conjunction* conjunction = subcondition->getConjunction(); 
                    std::string conjunctionName = conjunction->getConjunctionName();  
 
                    std::map<std::string, Premise*> *premises = subcondition-
>getPremises(); 
                    if (conjunctionName == "AND") { 
                        list_exprConjunction.push_back("=="); 
                        list_numPremises.push_back(premises->size()); 
                    } else { 
                        list_exprConjunction.push_back(">="); 
                        list_numPremises.push_back(1); 
                    }  
                } 
 
                //implementação dos métodos para cada subcondition 
                for (int it = 1; it <= subconditions->size(); ++it) { 
                     
                    fileH << tab << "\t\t\textern bool inc" << it << "();" << 
std::endl; 
                    fileH << tab << "\t\t\textern void dec" << it << "();" << 
std::endl;    
                    fileH << tab << "\t\t\textern bool eql" << it << "();" << 
std::endl;              
                     
                    fileCPP << tab << "\t\t\tbool inc" << it << "() {" << std::endl; 
                    fileCPP << tab << "\t\t\t\tcount" << it << "++;" << std::endl; 
                    //fileCPP << tab << "\t\t\t\tstd::cout << count" << it << " << 
std::endl;" << std::endl; 
                    fileCPP << tab << "\t\t\t\tstatus" << it << " = false;" << 
std::endl; 
                    fileCPP << tab << "\t\t\t\tif (count" << it << " " << 
list_exprConjunction[it-1] << " " <<list_numPremises[it-1]<<") {" << std::endl; 
                    fileCPP << tab << "\t\t\t\t\tstatus" << it << " = true;" << 
std::endl; 
                    fileCPP << tab << "\t\t\t\t\treturn compareStatusSubConditions();" 
<< std::endl; 
                    fileCPP << tab << "\t\t\t\t}"<< std::endl; 
                    fileCPP << tab << "\t\t\t\treturn false;"<< std::endl; 
                    fileCPP << tab << "\t\t\t}" << std::endl; 
                    fileCPP << tab << "\t\t\tvoid dec" << it << "() {" << std::endl; 
                    fileCPP << tab << "\t\t\t\tcount" << it << "--;" << std::endl; 
                    //fileCPP << tab << "\t\t\t\tstd::cout << count" << it << " << 
std::endl;" << std::endl; 
                    fileCPP << tab << "\t\t\t}" << std::endl;    
                    fileCPP << tab << "\t\t\tbool eql" << it << "() {" << std::endl; 
                    //fileCPP << tab << "\t\t\t\tstd::cout << count" << it << " << 
std::endl;" << std::endl; 
                    fileCPP << tab << "\t\t\t\tstatus" << it << " = false;" << 
std::endl; 
                    fileCPP << tab << "\t\t\t\tif (count" << it << " " << 
list_exprConjunction[it-1] << " " <<list_numPremises[it-1]<<") {" << std::endl; 
                    fileCPP << tab << "\t\t\t\t\tstatus" << it << " = true;" << 
std::endl; 
                    fileCPP << tab << "\t\t\t\t\treturn compareStatusSubConditions();" 
<< std::endl; 
                    fileCPP << tab << "\t\t\t\t}"<< std::endl; 
                    fileCPP << tab << "\t\t\t\treturn false;"<< std::endl; 
                    fileCPP << tab << "\t\t\t}" << std::endl;             
 
                } 
 
                fileH << tab << "\t\t\textern bool compareStatusSubConditions();" << 
std::endl; 


240 
 
 
                fileCPP << tab << "\t\t\tbool compareStatusSubConditions() {" << 
std::endl;  
                fileCPP << tab << "\t\t\t\tif ("; 
 
                int conjunctionCondId = condition->getConjunction()-
>getConjunctionId(); 
                std::string conjunctionCondValue = ""; 
 
                if (conjunctionCondId == Conjunction::AND_CONJUNCTION) { 
                    conjunctionCondValue = " && "; 
                } else if (conjunctionCondId == Conjunction::OR_CONJUNCTION) { 
                    conjunctionCondValue = " || "; 
                } 
 
                for (int it = 1; it <= subconditions->size(); ++it) { 
                    fileCPP << "(status" << it << " == true)";    
                    if (it != subconditions->size()) { 
                        fileCPP << conjunctionCondValue;  
                    } else { 
                        fileCPP << ") {" << std::endl;     
                    } 
                } 
 
                // Instigations 
                generateInstigation(fileCPP, fileH, instance, rule, level); 
 
                fileCPP << tab << "\t\t\t\t\treturn true;"<< std::endl; 
 
                fileCPP << tab << "\t\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t\t\treturn false;"<< std::endl; 
                fileCPP << tab << "\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t}" << std::endl; 
                fileH << tab << "\t\t}" << std::endl; 
 
            } else {     // não há subconditions 
 
                //Premises 
                std::map<std::string, Premise*> *premises = condition->getPremises(); 
 
                int numPremises = 0; 
                std::string expressionConjunction = ""; 
                std::string subConditionName = ""; 
 
                Conjunction* conjunction = condition->getConjunction(); 
                std::string conjunctionName = conjunction->getConjunctionName(); 
                 
                if (conjunctionName == "AND") { 
                    expressionConjunction = "=="; 
                    numPremises = premises->size(); 
                } else { 
                    expressionConjunction = ">="; 
                    numPremises = 1; 
                }  
                 
                // declaração da variável 
                fileH << tab << "\t\t\textern int count;" << std::endl; 
                fileCPP << tab << "\t\t\tint count = " << condition-
>getNumberApprovedPremises() << ";" << std::endl; 
 
                // implementação dos métodos 
                fileH << tab << "\t\t\textern bool inc();" << std::endl; 
                fileH << tab << "\t\t\textern void dec();" << std::endl; 
                fileH << tab << "\t\t\textern bool eql();" << std::endl; 
                fileCPP << tab << "\t\t\tbool inc() {" << std::endl; 
                fileCPP << tab << "\t\t\t\tcount++;" << std::endl; 


241 
 
 
                //fileCPP << tab << "\t\t\t\tstd::cout << count << std::endl;" << 
std::endl; 
                fileCPP << tab << "\t\t\t\tif (count "<< expressionConjunction << " " 
<< numPremises << ") {" << std::endl; 
 
                //instigations             
                generateInstigation(fileCPP, fileH, instance, rule, level);     
 
                fileCPP << tab << "\t\t\t\t\treturn true;" << std::endl;     
 
                fileCPP << tab << "\t\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t\t\treturn false;" << std::endl;   
                fileCPP << tab << "\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t\tvoid dec() {" << std::endl; 
                fileCPP << tab << "\t\t\t\tcount--;" << std::endl; 
                //fileCPP << tab << "\t\t\t\tstd::cout << \"  [\" << count << \" of " 
<< numPremises << "]\" << std::endl;" << std::endl; 
                fileCPP << tab << "\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t\tbool eql() {" << std::endl; 
                //fileCPP << tab << "\t\t\t\tstd::cout << count << std::endl;" << 
std::endl; 
                fileCPP << tab << "\t\t\t\tif (count "<< expressionConjunction << " " 
<< numPremises << ") {" << std::endl; 
 
                //instigations             
                generateInstigation(fileCPP, fileH, instance, rule, level);    
 
                fileCPP << tab << "\t\t\t\t\treturn true;" << std::endl;      
 
                fileCPP << tab << "\t\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t\t\treturn false;" << std::endl;  
                fileCPP << tab << "\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t}" << std::endl; 
                fileH << tab << "\t\t}" << std::endl; 
 
            } 
             
        } 
 
        level++; 
 
        // loop para serem implementadas os methods das instances 
        std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it != 
otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;      // otherInst -> corresponde a 
"instances das instances" 
            if (otherInst->getName() != "this") { 
 
                generateCodeRule(fileCPP, fileH, otherInst, level); 
 
            } 
 
        } 
 
        if (instance->getName() != "this") { 
            fileH << tab << "\t}" << std::endl; 
            fileCPP << tab << "\t}" << std::endl; 
        } 
         
    }else{ 
        // loop para serem implementadas os methods das instances 
        std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it != 
otherInsts->end(); ++it) { 


242 
 
 
 
            Instance *otherInst = it->second;      // otherInst -> corresponde a 
"instances das instances" 
            if (otherInst->getName() != "this") { 
 
                generateCodeRule(fileCPP, fileH, otherInst, 1); 
 
            } 
 
        } 
    } 
 
} 
 
void NamespacesCompiler::generateInstigation(ofstream& fileCPP, ofstream& fileH, 
Instance *instance, Rule *rule, int level) { 
 
    std::cout << "generateInstigation: " << instance->getName() << std::endl; 
 
    std::string tab = getLevel(level); 
 
std::string methodCall = ""; 
 
int countParams = 0; 
 
    Action *action = rule->getAction();  
 
    std::map<std::string, Instigation*> *instigations = action->getInstigations(); 
    for (std::map<std::string, Instigation*>::iterator it = instigations->begin(); it 
!= instigations->end(); ++it) {       
         
        Instigation *instigation = it->second; 
 
 
 
 
 
std::list<Call*> *calls = instigation->getCalls(); 
 
 
for (std::list<Call*>::iterator it = calls->begin(); it != calls->end(); 
++it) { 
 
 
 
 
Call *call = (*it); 
 
 
 
 
Method *method = call->getMethod(); 
 
            std::string cmpInstName = getInstanceCompleteName(method-
>getParentInstance()); 
 
            std::list<Argument*> *arguments = call->getArguments(); 
 
 
 
 
            //*** XXX Alteração methods-params XXX ***// 
 
 
 
/*methodCall = methodCall + tab + "\t\t\t\t\tmethod::" + 
cmpInstName + "::" + method->getName() + "::" + method->getName() + "("; 
 
 
 
 
 
 
if (arguments->size() > 0) { 
 
 
 
 
 
 
 
 
 
countParams = arguments->size(); 
 
                for (std::list<Argument*>::iterator it = arguments->begin(); it != 
arguments->end(); ++it) { 
 
 
 
 
 
 
Argument *argument = (*it); 
 
                    Factor *factor = argument->getFactor(); 
                     
 
 
 
 
 
//fileCPP << tab << "\t\t\t\t\tstd::cout << \"* 
method::" << cmpInstName << "::" << method->getName() << "::" << method->getName() << 
")\" << std::endl;" << std::endl; 
                    //fileCPP << tab << "\t\t\t\t\tmethod::" << cmpInstName << "::" << 
method->getName() << "::" << method->getName() << "(" << factor->getStringValue() << 
");" << std::endl; 
 
 
 
 
 
methodCall = methodCall + factor->getStringValue(); 


243 
 
 
 
 
 
 
 
 
 
 
 
 
 
if (countParams > 1) { 
 
 
 
 
 
 
methodCall = methodCall + ", "; 
 
 
 
 
 
} 
 
 
 
 
 
countParams--; 
                } 
 
            } 
             
 
 
 
methodCall = methodCall + ");"; 
            fileCPP << methodCall << std::endl;*/ 
 
 
 
 
            if (arguments->size() > 0) { 
 
                for (std::list<Argument*>::iterator it = arguments->begin(); it != 
arguments->end(); ++it) { 
 
 
 
 
 
 
Argument *argument = (*it); 
 
                    Factor *factor = argument->getFactor(); 
                     
 
 
 
 
 
//fileCPP << tab << "\t\t\t\t\tstd::cout << \"* 
method::" << cmpInstName << "::" << method->getName() << "::" << method->getName() << 
")\" << std::endl;" << std::endl; 
                    fileCPP << tab << "\t\t\t\t\tmethod::" << cmpInstName << "::" << 
method->getName() << "::" << method->getName() << "(" << factor->getStringValue() << 
");" << std::endl; 
 
                } 
 
            } else { 
                 
                //fileCPP << tab << "\t\t\t\t\tstd::cout << \"* method::" << 
cmpInstName << "::" << method->getName() << "::" << method->getName() << "()\" << 
std::endl;" << std::endl; 
                fileCPP << tab << "\t\t\t\t\tmethod::" << cmpInstName << "::" << 
method->getName() << "::" << method->getName() << "();" << std::endl; 
 
            }             
        } 
    } 
} 
 
 
void NamespacesCompiler::generateBody() { 
 
    std::cout << "generateBody" << std::endl; 
 
    ofstream file; 
    std::string filename = "Generated/Main.cpp"; 
    file.open(filename.c_str(), ios::out); 
    file << "#include <stdio.h>" << std::endl; 
    file << "#include <sys/time.h>" << std::endl; 
    file << "#include <iostream>" << std::endl; 
    file << "#include \"premises.h\"" << std::endl; 
    file << "#include \"instances.h\"" << std::endl; 
 
    file << std::endl; 
    file << "using namespace std;" << std::endl; 
    file << std::endl; 
 
    file << "int main() {" << std::endl; 
 
 
    /*file << "\tFILE *fp = NULL;" << std::endl; 
    file << "\tfp = fopen(\"Arquivo.txt\", \"w\");" << std::endl; 
    file << "\tif (fp != NULL) {" << std::endl; 


244 
 
 
    file << "\t\tfprintf(fp, \"Resultados eletronicgate:\");" << std::endl; 
    file << "\t}" << std::endl; 
    file << "\tfclose(fp);" << std::endl;*/ 
 
    for (std::list<std::string>::iterator itIni = init_premises.begin(); itIni!= 
init_premises.end(); ++itIni) { 
        file << "\t" << itIni->c_str() << std::endl; 
    } 
 
 
    file << std::endl; 
    file << "\tclock_t begin = clock();" << std::endl; 
     
    file << std::endl; 
 
    file << "\tint iteration = 100;" << std::endl; 
    file << "\twhile(iteration--){" << std:: endl; 
 
 
if (graph->getMainBlock() != 0) { 
 
 
 
std::map<std::string, Assignment*> *assignments = graph->getMainBlock()-
>getAssignments(); 
 
 
for (std::map<std::string, Assignment*>::iterator it = assignments-
>begin(); it != assignments->end(); ++it) { 
 
 
 
 
Assignment *assignment = it->second; 
 
 
 
Factor *factor = assignment->getFactor(); 
 
 
 
 
 
 
 
ElementFactor *element =  assignment->getElement(); 
 
 
 
 
 
 
 
Attribute *att = element->getAttribute(); 
 
 
 
 
 
 
 
Instance *instance = att->getParentInstance(); 
 
 
 
 
 
 
 
std::string typeName = returnType(att->getType()->getTypeId()); 
 
 
 
 
std::string cmpInstName = getInstanceCompleteName(instance); 
 
 
 
 
file << "\t\tinstance::" << cmpInstName << "::at::" << att-
>getName() << "::setValue(" << factor->getStringValue() << ");" << std::endl; 
 
 
 
} 
 
 
} 
 
    file << "\t}" << std::endl; 
 
    file << std::endl; 
 
    file << "\tclock_t end = clock();" << std::endl; 
 
    file << std::endl; 
    file << "\tdouble time_spent = (double)(end - begin);" << std::endl; 
    file << "\ttime_spent /= ((double)CLOCKS_PER_SEC);" << std::endl; 
    file << "\tcout << time_spent << endl;" << std::endl; 
     
    file << "\treturn 0;" << std::endl; 
     
    file << "}" << std::endl; 
 
    file.close();     
} 
void NamespacesCompiler::assemble() { 
    generateCode(); 
} 
Fonte: Autoria própria. 


245 
 
 
APÊNDICE B 
CÓDIGOS FONTE DO PROGRAMA REDE DE SENSORES EM LINGPON 2.0 
 
Este apêndice apresenta os códigos fonte do programa Rede de Sensores 
implementados em LingPON 2.0 e a classe externa SMSSender, apresentado na Seção 3.1.2. 
 
Arquivo Main.nop 
Código 66 - Arquivo Main.nop do programa Rede de Sensores implementado em LingPON 2.0 
fbe Main 
 
    includes NAMESPACES 
        #include "SMSSender.h" 
        #include <iostream> 
        using namespace std; 
    end_includes 
 
    private Sector sectorA 
    private Sector sectorB 
 
    private method mtSendSms 
        params 
            String cellphone 
        end_params 
        code NAMESPACES 
            SMSSender *sender = new SMSSender(); 
            sender->send(cellphone); 
        end_code 
    end_method 
 
    rule rlInvasionDetection 
        condition 
            premise prSectorAInvaded 
                sectorA.atIntruderDetected == true 
            end_premise 
            or 
            premise prSectorBInvaded 
                sectorB.atIntruderDetected == true 
            end_premise 
        end_condition 
        action sequential 
            instigation 
                call this.mtSendSms 
                    params 
                        "41-999999999" 
                    end_params 
                end_call 
 
 
  call this.mtSendSms 
                    params 
                        "47-999999999" 
                    end_params 
                end_call 
 
 
  call sectorA.mtNotifyInvasion 
            end_instigation 
        end_action 
    end_rule 


246 
 
 
 
 
main 
 
 
sectorA.atIntruderDetected = 1 
 
 
sectorB.atIntruderDetected = 1 
 
end_main 
 
    properties 
        strategy PRIORITY 
    end_properties 
 
end_fbe 
Fonte: Autoria própria. 
 
Arquivo Sector.nop 
Código 67 - Arquivo Sector.nop do programa Rede de Sensores implementado em LingPON 2.0 
fbe Sector 
 
    private Boolean atIntruderDetected = false 
 
    private Alarm alarmA 
    private Alarm alarmB 
     
    private Siren sirenA1 
    private Siren sirenA2 
    private Siren sirenB1 
 
    private Sensor sensorA1 
    private Sensor sensorA2 
    private Sensor sensorB1 
 
    private method mtNotifyInvasion 
        assignment 
            this.atIntruderDetected = true 
        end_assignment 
    end_method 
     
    rule rlFireAlarmA 
        condition 
            subcondition 
                premise prSectorInPeaceA 
                    this.atIntruderDetected == false 
                end_premise 
                and 
                premise prAlarmAOn 
                    alarmA.atStatus == true 
                end_premise 
            end_subcondition 
            and 
            subcondition 
                premise prSensorA1State 
                    sensorA1.atState == true 
                end_premise 
                or 
                premise prSensorA2State 
                    sensorA2.atState == true 
                end_premise 
            end_subcondition 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtNotifyInvasion() 
            end_instigation 
        end_action 


247 
 
 
    end_rule 
 
    rule rlFireAlarmB 
        condition 
            premise prSectorInPeaceB 
                this.atIntruderDetected == false 
            end_premise 
            and 
            premise prAlarmBOn 
                alarmB.atStatus == true 
            end_premise 
            and 
            premise prSensorB1State 
                sensorB1.atState == true 
            end_premise 
        end_condition 
        action sequential 
            instigation sequential 
                call this.mtNotifyInvasion() 
            end_instigation 
        end_action 
    end_rule 
 
    properties 
        strategy PRIORITY 
    end_properties 
 
end_fbe 
Fonte: Autoria própria. 
 
Arquivo Alarm.nop 
Código 68 - Arquivo Alarm.nop do programa Rede de Sensores implementado em LingPON 2.0 
fbe Alarm 
    public boolean atStatus = false 
    public boolean atDebug = false 
 
    private method mtDebug 
        assignment 
            this.atDebug = true 
        end_assignment 
    end_method 
 
    rule rlDebug 
        condition 
            premise prDebug 
                this.atStatus == true 
            end_premise 
        end_condition 
        action sequential 
            instigation sequential 
                call this.mtDebug 
            end_instigation 
        end_action 
    end_rule 
end_fbe 
Fonte: Autoria própria. 
 
 
 


248 
 
 
Arquivo Sensor.nop 
Código 69 - Arquivo Sensor.nop do programa Rede de Sensores implementado em LingPON 2.0 
fbe Sensor 
    public boolean atState = false 
end_fbe 
Fonte: Autoria própria. 
 
Arquivo Siren.nop 
Código 70 - Arquivo Siren.nop do programa Rede de Sensores implementado em LingPON 2.0 
fbe Siren 
    public integer atTime = 0 
end_fbe 
Fonte: Autoria própria. 
 
Arquivo SMSSender.h 
Código 71 - Arquivo .h da classe SMSSender utilizada no programa Rede de Sensores 
#pragma once 
#include <string> 
 
class SMSSender { 
 
public: 
 
 
void send(std::string cellphone); 
}; 
Fonte: Autoria própria. 
 
Arquivo SMSSender.cpp 
Código 72 - Arquivo .cpp da classe SMSSender utilizada no programa Rede de Sensores 
#include "SMSSender.h" 
#include <iostream> 
 
void SMSSender::send(std::string cellphone) { 
 
std::cout << "External send: " << cellphone << std::endl; 
} 
Fonte: Autoria própria.


249 
 
 
APÊNDICE C 
CÓDIGOS RESULTANTES DA GERAÇÃO EM C++ NOTIFICANTE ORIENTADO 
A NAMESPACES REFERENTE AO PROGRAMA REDE DE SENSORES 
 
Este apêndice apresenta os códigos gerados em C++ notificante modular orientado a 
namespaces resultantes da compilação do programa Rede de Sensore implementado em 
LingPON 2.0, conforme apresentado na Seção 3.1.2. 
 
Arquivos .h e .cpp do namespace ‘Instances’ 
 
Código 73 - Arquivo Instances.h do programa Rede de Sensores pelo NPCPP 2.0 
#pragma once 
#include <string> 
namespace instance{ 
 
namespace sectorA{ 
 
 
namespace at{ 
 
 
 
namespace atIntruderDetected{ 
 
 
 
 
extern bool value; 
 
 
 
 
extern void setValue(bool newValue); 
 
 
 
} 
 
 
} 
 
 
namespace alarmA{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atStatus{ 
 
 
 
 
 
extern bool value; 
 
 
 
 
 
extern void setValue(bool newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace alarmB{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atStatus{ 
 
 
 
 
 
extern bool value; 
 
 
 
 
 
extern void setValue(bool newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sensorA1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atState{ 
 
 
 
 
 
extern bool value; 
 
 
 
 
 
extern void setValue(bool newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sensorA2{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atState{ 
 
 
 
 
 
extern bool value; 
 
 
 
 
 
extern void setValue(bool newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 


250 
 
 
 
 
namespace sensorB1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atState{ 
 
 
 
 
 
extern bool value; 
 
 
 
 
 
extern void setValue(bool newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sirenA1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atTime{ 
 
 
 
 
 
extern int value; 
 
 
 
 
 
extern void setValue(int newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sirenA2{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atTime{ 
 
 
 
 
 
extern int value; 
 
 
 
 
 
extern void setValue(int newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sirenB1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atTime{ 
 
 
 
 
 
extern int value; 
 
 
 
 
 
extern void setValue(int newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
} 
 
namespace sectorB{ 
 
 
namespace at{ 
 
 
 
namespace atIntruderDetected{ 
 
 
 
 
extern bool value; 
 
 
 
 
extern void setValue(bool newValue); 
 
 
 
} 
 
 
} 
 
 
namespace alarmA{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atStatus{ 
 
 
 
 
 
extern bool value; 
 
 
 
 
 
extern void setValue(bool newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace alarmB{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atStatus{ 
 
 
 
 
 
extern bool value; 
 
 
 
 
 
extern void setValue(bool newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sensorA1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atState{ 
 
 
 
 
 
extern bool value; 
 
 
 
 
 
extern void setValue(bool newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sensorA2{ 
 
 
 
namespace at{ 


251 
 
 
 
 
 
 
namespace atState{ 
 
 
 
 
 
extern bool value; 
 
 
 
 
 
extern void setValue(bool newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sensorB1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atState{ 
 
 
 
 
 
extern bool value; 
 
 
 
 
 
extern void setValue(bool newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sirenA1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atTime{ 
 
 
 
 
 
extern int value; 
 
 
 
 
 
extern void setValue(int newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sirenA2{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atTime{ 
 
 
 
 
 
extern int value; 
 
 
 
 
 
extern void setValue(int newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sirenB1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atTime{ 
 
 
 
 
 
extern int value; 
 
 
 
 
 
extern void setValue(int newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
} 
} 
Fonte: Autoria própria. 
 
Código 74 - Arquivo Instances.cpp do programa Rede de Sensores gerado pelo NPCPP 2.0 
#include "instances.h" 
#include "premises.h" 
#include <string> 
 
        #include "SMSSender.h" 
        #include <iostream> 
        using namespace std; 
     
namespace instance{ 
 
namespace sectorA{ 
 
 
namespace at{ 
 
 
 
namespace atIntruderDetected{ 
 
 
 
 
bool value = 0; 
 
 
 
 
void setValue(bool newValue){ 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
premise::main::prSectorAInvaded::notify_sectorA_atIntruderDetected(newValue); 
 
 
 
 
 
 
premise::sectorA::prSectorInPeaceA::notify_sectorB_atIntruderDetected(newValue); 


252 
 
 
 
 
 
 
 
 
premise::sectorA::prSectorInPeaceB::notify_sectorB_atIntruderDetected(newValue); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace alarmA{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atStatus{ 
 
 
 
 
 
bool value = 0; 
 
 
 
 
 
void setValue(bool newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
 
premise::sectorA::prAlarmAOn::notify_alarmA_atStatus(newValue); 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace alarmB{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atStatus{ 
 
 
 
 
 
bool value = 0; 
 
 
 
 
 
void setValue(bool newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
 
premise::sectorA::prAlarmBOn::notify_alarmB_atStatus(newValue); 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sensorA1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atState{ 
 
 
 
 
 
bool value = 0; 
 
 
 
 
 
void setValue(bool newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
 
premise::sectorA::prSensorA1State::notify_sensorA1_atState(newValue); 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sensorA2{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atState{ 
 
 
 
 
 
bool value = 0; 
 
 
 
 
 
void setValue(bool newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
 
premise::sectorA::prSensorA2State::notify_sensorA2_atState(newValue); 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sensorB1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atState{ 
 
 
 
 
 
bool value = 0; 


253 
 
 
 
 
 
 
 
void setValue(bool newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
 
premise::sectorA::prSensorB1State::notify_sensorB1_atState(newValue); 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sirenA1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atTime{ 
 
 
 
 
 
int value = 0; 
 
 
 
 
 
void setValue(int newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sirenA2{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atTime{ 
 
 
 
 
 
int value = 0; 
 
 
 
 
 
void setValue(int newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sirenB1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atTime{ 
 
 
 
 
 
int value = 0; 
 
 
 
 
 
void setValue(int newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
} 
 
namespace sectorB{ 
 
 
namespace at{ 
 
 
 
namespace atIntruderDetected{ 
 
 
 
 
bool value = 0; 
 
 
 
 
void setValue(bool newValue){ 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
premise::main::prSectorBInvaded::notify_sectorB_atIntruderDetected(newValue); 
 
 
 
 
 
 
premise::sectorB::prSectorInPeaceA::notify_sectorB_atIntruderDetected(newValue); 
 
 
 
 
 
 
premise::sectorB::prSectorInPeaceB::notify_sectorB_atIntruderDetected(newValue); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace alarmA{ 
 
 
 
namespace at{ 


254 
 
 
 
 
 
 
namespace atStatus{ 
 
 
 
 
 
bool value = 0; 
 
 
 
 
 
void setValue(bool newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
 
premise::sectorB::prAlarmAOn::notify_alarmA_atStatus(newValue); 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace alarmB{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atStatus{ 
 
 
 
 
 
bool value = 0; 
 
 
 
 
 
void setValue(bool newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
 
premise::sectorB::prAlarmBOn::notify_alarmB_atStatus(newValue); 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sensorA1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atState{ 
 
 
 
 
 
bool value = 0; 
 
 
 
 
 
void setValue(bool newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
 
premise::sectorB::prSensorA1State::notify_sensorA1_atState(newValue); 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sensorA2{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atState{ 
 
 
 
 
 
bool value = 0; 
 
 
 
 
 
void setValue(bool newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
 
premise::sectorB::prSensorA2State::notify_sensorA2_atState(newValue); 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sensorB1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atState{ 
 
 
 
 
 
bool value = 0; 
 
 
 
 
 
void setValue(bool newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
 
premise::sectorB::prSensorB1State::notify_sensorB1_atState(newValue); 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 


255 
 
 
 
 
 
} 
 
 
} 
 
 
namespace sirenA1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atTime{ 
 
 
 
 
 
int value = 0; 
 
 
 
 
 
void setValue(int newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sirenA2{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atTime{ 
 
 
 
 
 
int value = 0; 
 
 
 
 
 
void setValue(int newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace sirenB1{ 
 
 
 
namespace at{ 
 
 
 
 
namespace atTime{ 
 
 
 
 
 
int value = 0; 
 
 
 
 
 
void setValue(int newValue){ 
 
 
 
 
 
 
if (value != newValue){ 
 
 
 
 
 
 
 
value = newValue; 
 
 
 
 
 
 
} 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
} 
} 
Fonte: Autoria própria. 
 
Arquivos .h e .cpp do namespace ‘Premises’ 
 
Código 75 - Arquivo Premises.h do programa Rede de Sensores gerado pelo NPCPP 2.0 
#pragma once 
#include <string> 
namespace premise{ 
 
namespace sectorA{ 
 
 
namespace prAlarmAOn{ 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_alarmA_atStatus(bool newValue); 
 
 
} 
 
 
namespace prSectorInPeaceA{ 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_sectorB_atIntruderDetected(bool newValue); 
 
 
} 


256 
 
 
 
 
namespace prSensorA1State{ 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_sensorA1_atState(bool newValue); 
 
 
} 
 
 
namespace prSensorA2State{ 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_sensorA2_atState(bool newValue); 
 
 
} 
 
 
namespace prAlarmBOn{ 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_alarmB_atStatus(bool newValue); 
 
 
} 
 
 
namespace prSectorInPeaceB{ 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_sectorB_atIntruderDetected(bool newValue); 
 
 
} 
 
 
namespace prSensorB1State{ 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_sensorB1_atState(bool newValue); 
 
 
} 
 
} 
 
namespace sectorB{ 
 
 
namespace prAlarmAOn{ 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_alarmA_atStatus(bool newValue); 
 
 
} 
 
 
namespace prSectorInPeaceA{ 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_sectorB_atIntruderDetected(bool newValue); 
 
 
} 
 
 
namespace prSensorA1State{ 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_sensorA1_atState(bool newValue); 
 
 
} 
 
 
namespace prSensorA2State{ 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_sensorA2_atState(bool newValue); 
 
 
} 
 
 
namespace prAlarmBOn{ 


257 
 
 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_alarmB_atStatus(bool newValue); 
 
 
} 
 
 
namespace prSectorInPeaceB{ 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_sectorB_atIntruderDetected(bool newValue); 
 
 
} 
 
 
namespace prSensorB1State{ 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_sensorB1_atState(bool newValue); 
 
 
} 
 
} 
 
namespace main{ 
 
 
namespace prSectorAInvaded{ 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_sectorA_atIntruderDetected(bool newValue); 
 
 
} 
 
 
namespace prSectorBInvaded{ 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void init(); 
 
 
 
extern void compare(); 
 
 
 
extern void notify_sectorB_atIntruderDetected(bool newValue); 
 
 
} 
 
} 
} 
Fonte: Autoria própria. 
 
Código 76 - Arquivo Premise.cpp do programa Rede de Sensores gerado pelo NPCPP 2.0 
#include "premises.h" 
#include "rules.h" 
#include <string> 
 
        #include "SMSSender.h" 
        #include <iostream> 
        using namespace std; 
     
namespace premise{ 
 
namespace sectorA{ 
 
 
namespace prAlarmAOn{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 1; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::sectorA::rlFireAlarmA::inc1(); 
 
 
 
 
 
} 


258 
 
 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 
 
 
 
 
 
 
rule::sectorA::rlFireAlarmA::dec1(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
 
void notify_alarmA_atStatus(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 
 
 
namespace prSectorInPeaceA{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 0; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::sectorA::rlFireAlarmA::inc1(); 
 
 
 
 
 
} 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 
 
 
 
 
 
 
rule::sectorA::rlFireAlarmA::dec1(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
 
void notify_sectorB_atIntruderDetected(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 
 
 
namespace prSensorA1State{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 1; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::sectorA::rlFireAlarmA::inc2(); 
 
 
 
 
 
} 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 
 
 
 
 
 
 
rule::sectorA::rlFireAlarmA::dec2(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
 
void notify_sensorA1_atState(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 
 
 
namespace prSensorA2State{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 


259 
 
 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 1; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::sectorA::rlFireAlarmA::inc2(); 
 
 
 
 
 
} 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 
 
 
 
 
 
 
rule::sectorA::rlFireAlarmA::dec2(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
 
void notify_sensorA2_atState(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 
 
 
namespace prAlarmBOn{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 1; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::sectorA::rlFireAlarmB::inc(); 
 
 
 
 
 
} 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 
 
 
 
 
 
 
rule::sectorA::rlFireAlarmB::dec(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
 
void notify_alarmB_atStatus(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 
 
 
namespace prSectorInPeaceB{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 0; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::sectorA::rlFireAlarmB::inc(); 
 
 
 
 
 
} 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 
 
 
 
 
 
 
rule::sectorA::rlFireAlarmB::dec(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 


260 
 
 
 
 
 
void notify_sectorB_atIntruderDetected(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 
 
 
namespace prSensorB1State{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 1; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::sectorA::rlFireAlarmB::inc(); 
 
 
 
 
 
} 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 
 
 
 
 
 
 
rule::sectorA::rlFireAlarmB::dec(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
 
void notify_sensorB1_atState(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 
 
} 
 
namespace sectorB{ 
 
 
namespace prAlarmAOn{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 1; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::sectorB::rlFireAlarmA::inc1(); 
 
 
 
 
 
} 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 
 
 
 
 
 
 
rule::sectorB::rlFireAlarmA::dec1(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
 
void notify_alarmA_atStatus(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 
 
 
namespace prSectorInPeaceA{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 0; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 


261 
 
 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::sectorB::rlFireAlarmA::inc1(); 
 
 
 
 
 
} 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 
 
 
 
 
 
 
rule::sectorB::rlFireAlarmA::dec1(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
 
void notify_sectorB_atIntruderDetected(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 
 
 
namespace prSensorA1State{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 1; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::sectorB::rlFireAlarmA::inc2(); 
 
 
 
 
 
} 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 
 
 
 
 
 
 
rule::sectorB::rlFireAlarmA::dec2(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
 
void notify_sensorA1_atState(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 
 
 
namespace prSensorA2State{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 1; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::sectorB::rlFireAlarmA::inc2(); 
 
 
 
 
 
} 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 
 
 
 
 
 
 
rule::sectorB::rlFireAlarmA::dec2(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
 
void notify_sensorA2_atState(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 


262 
 
 
 
 
namespace prAlarmBOn{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 1; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::sectorB::rlFireAlarmB::inc(); 
 
 
 
 
 
} 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 
 
 
 
 
 
 
rule::sectorB::rlFireAlarmB::dec(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
 
void notify_alarmB_atStatus(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 
 
 
namespace prSectorInPeaceB{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 0; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::sectorB::rlFireAlarmB::inc(); 
 
 
 
 
 
} 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 
 
 
 
 
 
 
rule::sectorB::rlFireAlarmB::dec(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
 
void notify_sectorB_atIntruderDetected(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 
 
 
namespace prSensorB1State{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 1; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::sectorB::rlFireAlarmB::inc(); 
 
 
 
 
 
} 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 


263 
 
 
 
 
 
 
 
 
rule::sectorB::rlFireAlarmB::dec(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
 
void notify_sensorB1_atState(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 
 
} 
 
namespace main{ 
 
 
namespace prSectorAInvaded{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 1; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::main::rlInvasionDetection::inc(); 
 
 
 
 
 
} 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 
 
 
 
 
 
 
rule::main::rlInvasionDetection::dec(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
 
void notify_sectorA_atIntruderDetected(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 
 
 
namespace prSectorBInvaded{ 
 
 
 
bool state = false; 
 
 
 
bool cpy1st, cpy2nd; 
 
 
 
void init(){ 
 
 
 
 
cpy1st = 0; 
 
 
 
 
cpy2nd = 1; 
 
 
 
} 
 
 
 
void compare(){ 
 
 
 
 
if(cpy1st  ==  cpy2nd){ 
 
 
 
 
 
if(state == false){ 
 
 
 
 
 
 
state = true; 
 
 
 
 
 
 
rule::main::rlInvasionDetection::inc(); 
 
 
 
 
 
} 
 
 
 
 
}else{ 
 
 
 
 
 
if(state == true){ 
 
 
 
 
 
 
state = false; 
 
 
 
 
 
 
rule::main::rlInvasionDetection::dec(); 
 
 
 
 
 
} 
 
 
 
 
} 
 
 
 
} 
 
 
 
void notify_sectorB_atIntruderDetected(bool newValue){ 
 
 
 
 
cpy1st = newValue; 
 
 
 
 
compare(); 
 
 
 
} 
 
 
} 
 
} 
} 
Fonte: Autoria própria. 
 


264 
 
 
Arquivos .h e .cpp do namespace ‘Rules’ 
 
Código 77 - Arquivo Rules.h do programa Rede de Sensores gerado pelo NPCPP 2.0 
#pragma once 
#include <string> 
namespace rule{ 
 
namespace main{ 
 
 
namespace rlInvasionDetection{ 
 
 
 
extern int count; 
 
 
 
extern void inc(); 
 
 
 
extern void dec(); 
 
 
} 
 
} 
 
namespace sectorA{ 
 
 
namespace rlFireAlarmA{ 
 
 
 
extern int count1; 
 
 
 
extern bool status1; 
 
 
 
extern int count2; 
 
 
 
extern bool status2; 
 
 
 
extern void inc1(); 
 
 
 
extern void dec1(); 
 
 
 
extern void inc2(); 
 
 
 
extern void dec2(); 
 
 
 
extern void compareStatusSubConditions(); 
 
 
} 
 
 
namespace rlFireAlarmB{ 
 
 
 
extern int count; 
 
 
 
extern void inc(); 
 
 
 
extern void dec(); 
 
 
} 
 
} 
 
namespace sectorB{ 
 
 
namespace rlFireAlarmA{ 
 
 
 
extern int count1; 
 
 
 
extern bool status1; 
 
 
 
extern int count2; 
 
 
 
extern bool status2; 
 
 
 
extern void inc1(); 
 
 
 
extern void dec1(); 
 
 
 
extern void inc2(); 
 
 
 
extern void dec2(); 
 
 
 
extern void compareStatusSubConditions(); 
 
 
} 
 
 
namespace rlFireAlarmB{ 
 
 
 
extern int count; 
 
 
 
extern void inc(); 
 
 
 
extern void dec(); 
 
 
} 
 
} 
} 
Fonte: Autoria própria. 
 
Código 78 - Arquivo Rules.cpp do programa Rede de Sensores gerado pelo NPCPP 2.0 
#include "rules.h" 
#include "methods.h" 
#include <string> 
 
        #include "SMSSender.h" 
        #include <iostream> 
        using namespace std; 
     
namespace rule{ 
 
namespace main{ 


265 
 
 
 
 
namespace rlInvasionDetection{ 
 
 
 
int count = 0; 
 
 
 
void inc(){ 
 
 
 
 
count++; 
 
 
 
 
if (count >= 1){ 
 
 
 
 
 
method::main::mtSendSms::mtSendSms("41-999999999"); 
 
 
 
 
 
method::main::mtSendSms::mtSendSms("47-999999999"); 
 
 
 
 
} 
 
 
 
} 
 
 
 
void dec(){ 
 
 
 
 
count--; 
 
 
 
} 
 
 
} 
 
} 
 
namespace sectorA{ 
 
 
namespace rlFireAlarmA{ 
 
 
 
int count1 = 0; 
 
 
 
bool status1; 
 
 
 
int count2 = 0; 
 
 
 
bool status2; 
 
 
 
void inc1(){ 
 
 
 
 
count1++; 
 
 
 
 
status1 = false; 
 
 
 
 
if (count1 == 2){ 
 
 
 
 
 
status1 = true; 
 
 
 
 
 
compareStatusSubConditions(); 
 
 
 
 
} 
 
 
 
} 
 
 
 
void dec1(){ 
 
 
 
 
count1--; 
 
 
 
} 
 
 
 
void inc2(){ 
 
 
 
 
count2++; 
 
 
 
 
status2 = false; 
 
 
 
 
if (count2 >= 1){ 
 
 
 
 
 
status2 = true; 
 
 
 
 
 
compareStatusSubConditions(); 
 
 
 
 
} 
 
 
 
} 
 
 
 
void dec2(){ 
 
 
 
 
count2--; 
 
 
 
} 
 
 
 
void compareStatusSubConditions(){ 
 
 
 
 
if((status1 == true) && (status2 == true)){ 
 
                          method::sectorA::mtNotifyInvasion::mtNotifyInvasion(); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace rlFireAlarmB{ 
 
 
 
int count = 0; 
 
 
 
void inc(){ 
 
 
 
 
count++; 
 
 
 
 
if (count == 3){ 
 
 
 
 
        
                                 method::sectorA::mtNotifyInvasion::mtNotifyInvasion(); 
 
 
 
 
} 
 
 
 
} 
 
 
 
void dec(){ 
 
 
 
 
count--; 
 
 
 
} 
 
 
} 
 
} 
 
namespace sectorB{ 
 
 
namespace rlFireAlarmA{ 
 
 
 
int count1 = 0; 
 
 
 
bool status1; 
 
 
 
int count2 = 0; 


266 
 
 
 
 
 
bool status2; 
 
 
 
void inc1(){ 
 
 
 
 
count1++; 
 
 
 
 
status1 = false; 
 
 
 
 
if (count1 == 2){ 
 
 
 
 
 
status1 = true; 
 
 
 
 
 
compareStatusSubConditions(); 
 
 
 
 
} 
 
 
 
} 
 
 
 
void dec1(){ 
 
 
 
 
count1--; 
 
 
 
} 
 
 
 
void inc2(){ 
 
 
 
 
count2++; 
 
 
 
 
status2 = false; 
 
 
 
 
if (count2 >= 1){ 
 
 
 
 
 
status2 = true; 
 
 
 
 
 
compareStatusSubConditions(); 
 
 
 
 
} 
 
 
 
} 
 
 
 
void dec2(){ 
 
 
 
 
count2--; 
 
 
 
} 
 
 
 
void compareStatusSubConditions(){ 
 
 
 
 
if((status1 == true) && (status2 == true)){ 
 
 
 
                     method::sectorB::mtNotifyInvasion::mtNotifyInvasion(); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace rlFireAlarmB{ 
 
 
 
int count = 0; 
 
 
 
void inc(){ 
 
 
 
 
count++; 
 
 
 
 
if (count == 3){ 
 
 
 
 
            
                                 method::sectorB::mtNotifyInvasion::mtNotifyInvasion(); 
 
 
 
 
} 
 
 
 
} 
 
 
 
void dec(){ 
 
 
 
 
count--; 
 
 
 
} 
 
 
} 
 
} 
} 
Fonte: Autoria própria. 
 
Arquivos .h e .cpp do namespace ‘Methods’ 
 
Código 79 - Arquivo Methods.h do programa Rede de Sensores gerado pelo NPCPP 2.0 
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
#pragma once 
#include <string> 
namespace method{ 
 
namespace main{ 
 
 
namespace mtSendSms{ 
 
 
 
void mtSendSms(std::string cellphone); 
 
 
} 
 
} 
 
namespace sectorA{ 
 
 
namespace mtNotifyInvasion{ 
 
 
 
extern void mtNotifyInvasion(); 
 
 
} 
 
} 
 
namespace sectorB{ 
 
 
namespace mtNotifyInvasion{ 


267 
 
 
16 
17 
18 
19 
 
 
 
extern void mtNotifyInvasion(); 
 
 
} 
 
} 
} 
Fonte: Autoria própria. 
 
Código 80 - Arquivo Methods.cpp do programa Rede de Sensores gerado pelo NPCPP 2.0 
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
#include "methods.h" 
#include "instances.h" 
#include <string> 
 
        #include "SMSSender.h" 
        #include <iostream> 
        using namespace std; 
     
namespace method{ 
 
namespace main{ 
 
 
namespace mtSendSms{ 
 
 
 
void mtSendSms(std::string cellphone){ 
 
 
 
 
 
            SMSSender *sender = new SMSSender(); 
            sender->send(cellphone); 
         
 
 
 
} 
 
 
} 
 
} 
 
namespace sectorA{ 
 
 
namespace mtNotifyInvasion{ 
 
 
 
void mtNotifyInvasion(){ 
 
 
 
 
instance::sectorA::at::atIntruderDetected::setValue(1); 
 
 
 
} 
 
 
} 
 
} 
 
namespace sectorB{ 
 
 
namespace mtNotifyInvasion{ 
 
 
 
void mtNotifyInvasion(){ 
 
 
 
 
instance::sectorB::at::atIntruderDetected::setValue(1); 
 
 
 
} 
 
 
} 
 
} 
} 
Fonte: Autoria própria. 
 
Arquivo Main.cpp 
 
Código 81 - Arquivo Main.cpp do programa Rede de Sensores gerado pelo NPCPP 2.0 
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
#include <stdio.h> 
#include <sys/time.h> 
#include <iostream> 
#include "premises.h" 
#include "instances.h" 
 
using namespace std; 
 
int main() { 
 
premise::sectorA::prAlarmAOn::init(); 
 
premise::sectorA::prSectorInPeaceA::init(); 
 
premise::sectorA::prSensorA1State::init(); 
 
premise::sectorA::prSensorA2State::init(); 
 
premise::sectorA::prAlarmBOn::init(); 
 
premise::sectorA::prSectorInPeaceB::init(); 


268 
 
 
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
37 
38 
39 
40 
41 
42 
 
premise::sectorA::prSensorB1State::init(); 
 
premise::sectorB::prAlarmAOn::init(); 
 
premise::sectorB::prSectorInPeaceA::init(); 
 
premise::sectorB::prSensorA1State::init(); 
 
premise::sectorB::prSensorA2State::init(); 
 
premise::sectorB::prAlarmBOn::init(); 
 
premise::sectorB::prSectorInPeaceB::init(); 
 
premise::sectorB::prSensorB1State::init(); 
 
premise::main::prSectorAInvaded::init(); 
 
premise::main::prSectorBInvaded::init(); 
 
 
timeval time; 
 
double initial; 
 
double final; 
 
gettimeofday(&time,0); 
 
initial = (time.tv_sec * 1000.0) + (time.tv_usec / 1000.0); 
 
 
instance::sectorB::at::atIntruderDetected::setValue(0); 
 
instance::sectorB::alarmB::at::atStatus::setValue(1); 
 
instance::sectorB::sensorB1::at::atState::setValue(1); 
 
 
gettimeofday(&time,0); 
 
final = (time.tv_sec * 1000.0) + (time.tv_usec / 1000.0); 
 
double resultado = final - initial; 
 
cout << resultado << endl; 
 
return 0; 
} 
Fonte: Autoria própria. 
 


269 
 
 
APÊNDICE D 
DESENVOLVIMENTO DO DESPERTADOR ELETRÔNICO 
 
Nesta seção, será feita a apresentação de uma atividade proposta sobre a 
implementação de uma aplicação simples de despertador eletrônico na disciplina do PON. Esta 
atividade teve como objetivo auxiliar que os alunos se familiarizassem com o desenvolvimento 
em LingPON 2.0, além testar o NPCPP 2.0 e identificar inconsistências e melhorias, as quais 
foram listadas no Quadro 16, da Seção 3.2. 
 
 Atividade Proposta 
Implementar um projeto em lingPon, simulando um a funcionalidade "Soneca" de um 
despertador. O projeto deverá conter um fbe Despertador e um fbe Contador. O fbe 
Despertador poderá ter um atribute que indica se o "soneca" foi ativado ou não, e o fbe 
Contador possuirá um atribute que indicará a contagem de 5 minutos do soneca. O fbe 
Despertador conterá ainda uma rule: se o soneca for ativado, ativará o contador do fbe 
Contador. O fbe Contador possuirá a rule: se o contador for ativado, conta 5 minutos (ou 
segundos) e após, o alarme dispara  (aparecer no console uma mensagem informando o 
disparo do alarme). 
Sugestão: a contagem do soneca e o "disparo do alarme" poderão ser representados 
em um método de uma classe externa (em c++) 
 
 Solução da Implementação em LingPON 2.0 
A solução apresentada a seguir foi desenvolvida pelo aluno Lucas Garcia. 
o FBE Main 
Código 82 - FBE Main da aplicação do Despertador Eletrônico 
fbe Contador 
        includes NAMESPACES 
        #include "ExternalProvider.h" 
        #include <iostream> 
        using namespace std; 
    end_includes 
 
    private boolean cont = false 
 
    private method mt_StartConting 
        code NAMESPACES 
            ExternalProvider *exProvider = new ExternalProvider(); 
            exProvider->printStateCont(true); 
            instance::main::contador::at::cont::setValue(true); 
      end_code 
    end_method 


270 
 
 
 
    private method mt_Count 
        code NAMESPACES 
            ExternalProvider *exProvider = new ExternalProvider(); 
            exProvider->count(); 
            exProvider->printStateCont(false); 
            instance::main::contador::at::cont::setValue(false); 
      end_code 
    end_method 
     
end_fbe 
Fonte: Autoria própria. 
 
o FBE Despertador 
Código 83 - FBE Despertador da aplicação do Despertador Eletrônico 
fbe Despertador 
 
includes NAMESPACES 
        #include "ExternalProvider.h" 
        #include <iostream> 
        using namespace std; 
    end_includes 
 
 
private boolean sonAt = true 
 
    private method mt_DesabNotifSon 
    code NAMESPACES 
            ExternalProvider *exProvider = new ExternalProvider(); 
            exProvider->printStateSoneca(false); 
            instance::main::despertador::at::sonAt::setValue(false); 
        end_code 
    end_method 
 
  
 
private method mt_EscolheSoneca 
        code NAMESPACES 
            ExternalProvider *exProvider = new ExternalProvider(); 
            exProvider->printStateSoneca(true); 
            instance::main::despertador::at::sonAt::setValue(true); 
        end_code 
    end_method 
 
end_fbe 
Fonte: Autoria própria. 
 
o FBE Contador 
Código 84 - FBE Contador da aplicação do Despertador Eletrônico 
fbe Contador 
        includes NAMESPACES 
        #include "ExternalProvider.h" 
        #include <iostream> 
        using namespace std; 
    end_includes 
 
    private boolean cont = false 
 
    private method mt_StartConting 
        code NAMESPACES 
            ExternalProvider *exProvider = new ExternalProvider(); 
            exProvider->printStateCont(true); 
            instance::main::contador::at::cont::setValue(true); 
      end_code 


271 
 
 
    end_method 
 
    private method mt_Count 
        code NAMESPACES 
            ExternalProvider *exProvider = new ExternalProvider(); 
            exProvider->count(); 
            exProvider->printStateCont(false); 
            instance::main::contador::at::cont::setValue(false); 
        end_code 
    end_method 
 
end_fbe 
 
 
Fonte: Autoria própria. 
 
o Arquivos .h e .cpp da Classe ExternalProvider 
Código 85 - Arquivo .h da classe externa utilizada na aplicação do Despertador Eletrônico 
#pragma once 
 
class ExternalProvider{ 
public: 
  ExternalProvider(); 
  ~ExternalProvider(); 
  int getNew(); 
  bool getAt(); 
  void count(); 
 
void printStateSoneca(bool s); 
void printStateCont(bool s); 
} 
Fonte: Autoria própria. 
 
Código 86 - Arquivo .cpp da classe externa utilizada na aplicação do Despertador Eletrônico 
#include "ExternalProvider.h" 
// #include "instantiations.h" 
#include <iostream> 
#include <time.h> 
#include <unistd.h> 
 
ExternalProvider::ExternalProvider() 
{ 
  srand(time(NULL)); 
} 
ExternalProvider::~ExternalProvider() 
{ 
} 
 
bool ExternalProvider::getAt() 
{ 
  srand(time(NULL)); 
  const int newV{rand()%2}; 
  std::cout << "New Val " << newV << std::endl; 
 
  return static_cast<bool>(newV); 
} 
 
void ExternalProvider::count() 
{ 
  std::cout << "Dormindo um tempo" << std::endl; 
  sleep(1); 
  std::cout << "Acordei" << std::endl; 
} 
 


272 
 
 
 
void ExternalProvider::printStateSoneca(bool s) 
{ 
  std::cout << "New state Soneca " << s << std::endl; 
} 
 
void ExternalProvider::printStateCont(bool s) 
{ 
  std::cout << "New state Cont " << s << std::endl; 
} 
Fonte: Autoria própria. 
 
 Implementação gerada pelo NPCPP 2.0 
o Namespaces Instances 
Código 87 - Arquivo .h do namespace Instance gerado para a aplicação Despertador Eletrônico 
#pragma once 
#include <string> 
#include <iostream> 
namespace instance { 
 
namespace main { 
 
 
namespace contador { 
 
 
 
namespace at { 
 
 
 
 
namespace cont { 
 
 
 
 
 
extern bool value; 
 
 
 
 
 
extern void setValue(bool newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
namespace despertador { 
 
 
 
namespace at { 
 
 
 
 
namespace sonAt { 
 
 
 
 
 
extern bool value; 
 
 
 
 
 
extern void setValue(bool newValue); 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
} 
} 
Fonte: Autoria própria. 
 
o Namespaces Premises 
Código 88 - Arquivo .h do namespace Premises gerado para a aplicação Despertador Eletrônico 
#pragma once 
#include <string> 
#include <iostream> 
namespace premise { 
 
namespace main { 
 
 
namespace pr1 { 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void compare(); 
 
 
 
extern void notify_contador_cont(bool newValue); 
 
 
} 
 
 
namespace pr2 { 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void compare(); 
 
 
 
extern void notify_despertador_sonAt(bool newValue); 


273 
 
 
 
 
} 
 
 
namespace pr3 { 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void compare(); 
 
 
 
extern void notify_contador_cont(bool newValue); 
 
 
} 
 
 
namespace pr4 { 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void compare(); 
 
 
 
extern void notify_despertador_sonAt(bool newValue); 
 
 
} 
 
 
namespace pr5 { 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void compare(); 
 
 
 
extern void notify_contador_cont(bool newValue); 
 
 
} 
 
 
namespace pr6 { 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void compare(); 
 
 
 
extern void notify_despertador_sonAt(bool newValue); 
 
 
} 
 
 
namespace pr7 { 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void compare(); 
 
 
 
extern void notify_contador_cont(bool newValue); 
 
 
} 
 
 
namespace pr8 { 
 
 
 
extern bool state; 
 
 
 
extern bool cpy1st, cpy2nd; 
 
 
 
extern void compare(); 
 
 
 
extern void notify_despertador_sonAt(bool newValue); 
 
 
} 
 
} 
} 
Fonte: Autoria própria. 
 
o Namespaces Rules 
Código 89 - Arquivo .h do namespace Rules gerado para a aplicação Despertador Eletrônico 
#pragma once 
#include <string> 
#include <iostream> 
namespace rule { 
 
namespace main { 
 
 
namespace rl1 { 
 
 
 
extern int count; 
 
 
 
extern void inc(); 
 
 
 
extern void dec(); 
 
 
 
extern void tryExec(); 
 
 
} 
 
 
namespace rl2 { 
 
 
 
extern int count; 
 
 
 
extern void inc(); 
 
 
 
extern void dec(); 
 
 
 
extern void tryExec(); 
 
 
} 
 
 
namespace rl3 { 
 
 
 
extern int count; 
 
 
 
extern void inc(); 


274 
 
 
 
 
 
extern void dec(); 
 
 
 
extern void tryExec(); 
 
 
} 
 
 
namespace rl4 { 
 
 
 
extern int count; 
 
 
 
extern void inc(); 
 
 
 
extern void dec(); 
 
 
 
extern void tryExec(); 
 
 
} 
 
} 
} 
Fonte: Autoria própria. 
 
o Namespaces Methods 
Código 90 - Arquivo .h do namespace Methods gerado para a aplicação Despertador Eletrônico 
#pragma once 
#include <string> 
#include <iostream> 
namespace method { 
 
namespace main { 
 
 
namespace contador { 
 
 
 
namespace mt_Count { 
 
 
 
 
void mt_Count(); 
 
 
 
} 
 
 
 
namespace mt_StartConting { 
 
 
 
 
void mt_StartConting(); 
 
 
 
} 
 
 
} 
 
 
namespace despertador { 
 
 
 
namespace mt_DesabNotifSon { 
 
 
 
 
void mt_DesabNotifSon(); 
 
 
 
} 
 
 
 
namespace mt_EscolheSoneca { 
 
 
 
 
void mt_EscolheSoneca(); 
 
 
 
} 
 
 
} 
 
} 
} 
Fonte: Autoria própria.


275 
 
 
APÊNDICE E 
CÓDIGOS FONTE DAS ESTRATÉGIAS DE CONTROLE DO SIMULADOR CTA 
IMPLEMENTADOS EM LINGPON 2.0 
 
Este apêndice apresenta os códigos fonte da estratégia de controle independente e da 
estratégia de controle baseado em congestionamento, implementados em LingPON 2.0, do 
Simulador CTA, conforme apresentado na Seção 3.3.1. Serão apresentados também as classes 
SimuladorNamespacesAPI e SimuladorNamespacesAPI_CBCL, utilizadas para integrar as 
estratégias de controle, implementadas em C++ notificante modular orientado a namespaces, 
com o Simulador CTA, implementado em C++. 
 
 Estratégia de Controle Independente 
 
Arquivo Main.nop 
Código 91 - Arquivo Main.nop da estratégia de controle independente em LingPON 2.0 
fbe Main 
 
    includes NAMESPACES 
        #include <iostream> 
        using namespace std; 
    end_includes 
 
    private Semaphore[10] S1 
 
    properties 
        strategy BREADTH 
    end_properties 
 
    main 
 
 semaphoreS.atSeconds = 2 
    end_main 
 
end_fbe 
Fonte: Autoria própria. 
 
Arquivo Semaphore.nop 
Código 92 - Arquivo Semaphore.nop da estratégia de controle independente em LingPON 2.0 
fbe Semaphore 
 
    private Integer atSemaphoreState = 5 
    private Integer atSeconds = 0 
 
    private method mtResetTimer 
        assignment 
            this.atSeconds = 0 
        end_assignment 


276 
 
 
    end_method 
 
    private method mtHorizontalTrafficLightGREEN 
        assignment 
            this.atSemaphoreState = 0 
        end_assignment 
    end_method 
 
    private method mtHorizontalTrafficLightYELLOW 
        assignment 
            this.atSemaphoreState = 1 
        end_assignment 
    end_method 
 
    private method mtHorizontalTrafficLightRED 
        assignment 
            this.atSemaphoreState = 2 
        end_assignment 
    end_method 
 
    private method mtVerticalTrafficLightGREEN 
        assignment 
            this.atSemaphoreState = 3 
        end_assignment 
    end_method 
 
    private method mtVerticalTrafficLightYELLOW 
        assignment 
            this.atSemaphoreState = 4 
        end_assignment 
    end_method 
 
    private method mtVerticalTrafficLightRED 
        assignment 
            this.atSemaphoreState = 5 
        end_assignment 
    end_method 
 
    rule rlHorizontalTrafficLightGreen 
        condition 
                premise prSeconds 
                    this.atSeconds == 2 
                end_premise 
                and 
                premise prSemaphoreState 
                    this.atSemaphoreState == 5 
                end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtHorizontalTrafficLightGREEN() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlHorizontalTrafficLightYellow 
        condition 
            premise prSeconds2 
                this.atSeconds == 40 
            end_premise 
            and 
            premise prSemaphoreState2 
                this.atSemaphoreState == 0 
            end_premise 
        end_condition 
        action sequential 


277 
 
 
            instigation parallel 
                call this.mtHorizontalTrafficLightYELLOW() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlHorizontalTrafficLightRed 
        condition 
            premise prAtSeconds3 
                this.atSeconds == 45  
            end_premise 
            and 
            premise prSemaphoreState3 
                this.atSemaphoreState == 1  
            end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtHorizontalTrafficLightRED() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlVerticalTrafficLightGreen 
        condition 
            premise prAtSeconds4 
                this.atSeconds == 47 
            end_premise 
            and 
            premise prSemaphoreState4 
                this.atSemaphoreState == 2 
            end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtVerticalTrafficLightGREEN() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlVerticalTrafficLightYellow 
        condition 
            premise prAtSeconds5 
                this.atSeconds == 85 
            end_premise 
            and 
            premise prSemaphoreState5 
                this.atSemaphoreState == 3 
            end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtVerticalTrafficLightYELLOW() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlVerticalTrafficLightRed 
        condition 
            premise prAtSeconds6 
                this.atSeconds == 90 
            end_premise 
            and 
            premise prSemaphoreState6 
                this.atSemaphoreState == 4 
            end_premise 


278 
 
 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtVerticalTrafficLightRED() 
                call this.mtResetTimer() 
            end_instigation 
        end_action 
    end_rule 
 
end_fbe 
 
 
Fonte: Autoria própria. 
 
Arquivos .h e .cpp da Classe SimuladorNamespaceAPI 
Código 93 - Arquivo .h da API SimuladorNamespaceAPI para a  
estratégia de controle independente 
#pragma once 
#include <iostream> 
#include <string> 
#include <list> 
#include "../Semaphore.h" 
 
using namespace std; 
 
class SimuladorNamespaceAPI 
{ 
public: 
    static void addSemaphore(Semaphore* semaphore); 
 
 
static Semaphore* getSemaphoreSim(int id); 
    static void setStateSim(int id, int state); 
    static void setCurrentCycleTimeSim(int id, int sec); 
 
    static void inicializaIdNop(); 
    static void setSemaphoreStateNop(int id, int state); 
    static void setSecondsNop(int id, int sec); 
 
private: 
 
static std::list<Semaphore*> pSemaphores; 
 
}; 
Fonte: Autoria própria. 
 
Código 94 - Arquivo .cpp da API SimuladorNamespaceAPI para a  
estratégia de controle independente 
#include "SimuladorNamespaceAPI.h" 
#include "../Traffic_Light.h" 
#include "instances.h" 
#include <string> 
using namespace std; 
using namespace instance; 
 
void SimuladorNamespaceAPI::addSemaphore(Semaphore* semaphore) 
{ 
 
pSemaphores.push_back(semaphore); 
} 
 
Semaphore* SimuladorNamespaceAPI::getSemaphoreSim(int id) 
{ 
 
std::list<Semaphore*>::const_iterator it; 
 
 
for (it = (&pSemaphores)->begin(); it != (&pSemaphores)->end(); ++it) { 
 
 
Semaphore* semaphore = (*it); 


279 
 
 
 
 
if (semaphore->GetId() == id) 
 
 
{ 
 
 
 
return semaphore; 
 
 
} 
 
} 
} 
 
void SimuladorNamespaceAPI::setStateSim(int id, int state) 
{ 
 
Semaphore *semaphore = getSemaphoreSim(id); 
 
 
switch (state) 
 
{ 
 
case 0: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(GREEN); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(RED); 
 
 
break; 
 
case 1: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(YELLOW); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(RED); 
 
 
break; 
 
case 2: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(RED); 
 
 
break; 
 
case 3: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(GREEN); 
 
 
break; 
 
case 4: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(YELLOW); 
 
 
break; 
 
case 5: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(RED); 
 
 
break; 
 
} 
} 
 
void SimuladorNamespaceAPI::inicializaIdNop() 
{ 
 
instance::main::S1__vector_0::at::atId::setValue(1); 
 
instance::main::S1__vector_1::at::atId::setValue(2); 
 
instance::main::S1__vector_2::at::atId::setValue(3); 
 
instance::main::S1__vector_3::at::atId::setValue(4); 
 
instance::main::S1__vector_4::at::atId::setValue(5); 
 
instance::main::S1__vector_5::at::atId::setValue(6); 
 
instance::main::S1__vector_6::at::atId::setValue(7); 
 
instance::main::S1__vector_7::at::atId::setValue(8); 
 
instance::main::S1__vector_8::at::atId::setValue(9); 
 
instance::main::S1__vector_9::at::atId::setValue(10); 
} 
 
void SimuladorNamespaceAPI::setSemaphoreStateNop(int id, int state) 
{ 
 
switch (id) 
 
{ 
 
case 1: 
 
 
instance::main::S1__vector_0::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 2: 
 
 
instance::main::S1__vector_1::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 3: 
 
 
instance::main::S1__vector_2::at::atSemaphoreState::setValue(state); 


280 
 
 
 
 
break; 
 
case 4: 
 
 
instance::main::S1__vector_3::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 5: 
 
 
instance::main::S1__vector_4::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 6: 
 
 
instance::main::S1__vector_5::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 7: 
 
 
instance::main::S1__vector_6::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 8: 
 
 
instance::main::S1__vector_7::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 9: 
 
 
instance::main::S1__vector_8::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 10: 
 
 
instance::main::S1__vector_9::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
} 
} 
 
void SimuladorNamespaceAPI::setSecondsNop(int id, int sec) 
{ 
 
switch (id) 
 
{ 
 
case 1: 
 
 
instance::main::S1__vector_0::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 2: 
 
 
instance::main::S1__vector_1::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 3: 
 
 
instance::main::S1__vector_2::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 4: 
 
 
instance::main::S1__vector_3::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 5: 
 
 
instance::main::S1__vector_4::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 6: 
 
 
instance::main::S1__vector_5::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 7: 
 
 
instance::main::S1__vector_6::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 8: 
 
 
instance::main::S1__vector_7::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 9: 
 
 
instance::main::S1__vector_8::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 10: 
 
 
instance::main::S1__vector_9::at::atSeconds::setValue(sec); 
 
 
break; 
 
} 
} 
 
void SimuladorNamespaceAPI::setCurrentCycleTimeSim(int id, int sec) 
{ 
 
Semaphore *semaphore = getSemaphoreSim(id); 
 


281 
 
 
 
semaphore->SetCurrentCycleTime(sec); 
} 
Fonte: Autoria própria. 
 
 Estratégia de Controle Baseado em Congestionamento 
 
Arquivo Main.nop 
Código 95 - Arquivo Main.nop da estratégia de controle baseado em  
congestionamento em LingPON 2.0 
fbe Main 
 
    includes NAMESPACES 
        #include <iostream> 
        using namespace std; 
    end_includes 
 
    private Semaphore[10] S1 
 
    properties 
        strategy BREADTH 
    end_properties 
 
    main 
 
     
    end_main 
 
end_fbe 
Fonte: Autoria própria. 
 
Arquivo Semaphore.nop 
Código 96 - Arquivo Semaphore.nop da estratégia baseado em congestionamento em LingPON 2.0 
fbe Semaphore_CBCL 
 
    private Integer atSemaphoreState = 5 
    private Integer atSeconds = 0 
 
private integer atHVSS = 0 
 
private integer atVVSS = 0 
 
    private method mtRT 
        attribution 
            this.atSeconds = 0 
        end_attribution 
    end_method 
 
    private method mtHTLG 
        attribution 
            this.atSemaphoreState = 0 
        end_attribution 
    end_method 
 
    private method mtHTLY 
        attribution 
            this.atSemaphoreState = 1 
        end_attribution 
    end_method 
 
    private method mtHTLR 
        attribution 


282 
 
 
            this.atSemaphoreState = 2 
        end_attribution 
    end_method 
 
    private method mtVTLG 
        attribution 
            this.atSemaphoreState = 3 
        end_attribution 
    end_method 
 
    private method mtVTLY 
        attribution 
            this.atSemaphoreState = 4 
        end_attribution 
    end_method 
 
    private method mtVTLR 
        attribution 
            this.atSemaphoreState = 5 
        end_attribution 
    end_method 
 
 
 
private method mtHTLGCBCL 
        attribution 
            this.atSemaphoreState = 6 
        end_attribution 
    end_method 
 
    private method mtHTLYCBCL 
        attribution 
            this.atSemaphoreState = 7 
        end_attribution 
    end_method 
 
    private method mtVTLGCBCL 
        attribution 
            this.atSemaphoreState = 8 
        end_attribution 
    end_method 
 
    private method mtVTLYCBCL 
        attribution 
            this.atSemaphoreState = 9 
        end_attribution 
    end_method 
 
    rule rlCBCL1 
        condition 
                premise prSeconds 
                    this.atSeconds == 2 
                end_premise 
                and 
                premise prSemaphoreState 
                    this.atSemaphoreState == 5 
                end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtHTLG() 
 
 
  call this.mtRT() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlCBCL2 
        condition 


283 
 
 
            premise prSeconds2 
                this.atSeconds == 38 
            end_premise 
            and 
            premise prSemaphoreState2 
                this.atSemaphoreState == 0 
            end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtHTLY() 
 
 
  call this.mtRT() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlCBCL3 
        condition 
            premise prSecondsCBCL2 
                this.atSeconds == 30  
            end_premise 
            and 
            premise prSemaphoreStateCBCL2 
                this.atSemaphoreState == 6 
            end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtHTLY() 
 
 
 
 
call this.mtRT() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlCBCL4 
        condition 
            premise prSeconds3 
                this.atSeconds == 5 
            end_premise 
            and 
            premise prSemaphoreState3 
                this.atSemaphoreState == 1 
            end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtHTLR() 
 
 
  call this.mtRT() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlCBCL5 
        condition 
            premise prSecondsCBCL3 
                this.atSeconds == 6 
            end_premise 
            and 
            premise prSemaphoreStateCBCL3 
                this.atSemaphoreState == 7 
            end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtHTLR() 
 
 
 
 
call this.mtRT() 


284 
 
 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlCBCL6 
        condition 
            premise prSeconds4 
                this.atSeconds == 2 
            end_premise 
            and 
            premise prSemaphoreState4 
                this.atSemaphoreState == 2 
            end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtVTLG() 
                call this.mtRT() 
            end_instigation 
        end_action 
    end_rule 
 
 
 
rule rlCBCL7 
        condition 
                premise prSeconds5 
                    this.atSeconds == 38 
                end_premise 
                and 
                premise prSemaphoreState5 
                    this.atSemaphoreState == 3 
                end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtVTLY() 
 
 
 
 
call this.mtRT() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlCBCL8 
        condition 
            premise prSecondsCBCL5 
                this.atSeconds == 30 
            end_premise 
            and 
            premise prSemaphoreStateCBCL5 
                this.atSemaphoreState == 8 
            end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtVTLY() 
 
 
  call this.mtRT() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlCBCL9 
        condition 
            premise prSeconds6 
                this.atSeconds == 5 
            end_premise 
            and 
            premise prSemaphoreState6 
                this.atSemaphoreState == 4 


285 
 
 
            end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtVTLR() 
 
 
  call this.mtRT() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlCBCL10 
        condition 
            premise prSecondsCBCL6 
                this.atSeconds == 6 
            end_premise 
            and 
            premise prSemaphoreStateCBCL6 
                this.atSemaphoreState == 9 
            end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtVTLR() 
 
 
  call this.mtRT() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlCBCL11 
        condition 
            premise prSeconds7 
                this.atSeconds <= 17 
            end_premise 
            and 
            premise prSemaphoreState7 
                this.atSemaphoreState == 0 
            end_premise 
 
     and 
 
     premise prVehicleSensorState7  
 
 
  this.atVVSS == 1 
 
         end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtHTLGCBCL() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlCBCL12 
        condition 
            premise prSeconds7Full 
                this.atSeconds <= 17 
            end_premise 
            and 
            premise prSemaphoreState7Full 
                this.atSemaphoreState == 0 
            end_premise 
 
 
 
and 
 
 
 
premise prVehicleSensorState7Full  
 
 
 
 
this.atVVSS == 2 
 
 
 
end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtHTLGCBCL() 


286 
 
 
            end_instigation 
        end_action 
    end_rule 
 
 
 
rule rlCBCL13 
        condition 
            premise prSeconds8 
                this.atSeconds >= 18 
            end_premise 
            and 
 
     premise prSecondsSup8 
                this.atSeconds < 32 
            end_premise 
            and 
            premise prSemaphoreState8 
                this.atSemaphoreState == 0 
            end_premise 
 
    and 
 
    premise prVehicleSensorState8  
 
 
  this.atVVSS == 1 
 
    end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtHTLYCBCL() 
 
 
  call this.mtRT() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlCBCL14 
        condition 
            premise prSeconds8Full 
                this.atSeconds >= 18 
            end_premise 
            and 
 
 
 
premise prSecondsSup8Full 
                this.atSeconds < 32 
            end_premise 
            and 
            premise prSemaphoreState8Full 
                this.atSemaphoreState == 0 
            end_premise 
 
 
 
and 
 
 
 
premise prVehicleSensorState8Full  
 
 
 
 
this.atVVSS == 2 
 
 
 
end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtHTLYCBCL() 
 
 
 
 
call this.mtRT() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlCBCL15 
        condition 
            premise prSeconds9 
                this.atSeconds <= 17 
            end_premise 
            and 
            premise prSemaphoreState9 
                this.atSemaphoreState == 3 
            end_premise 
            and 


287 
 
 
 
     premise prVehicleSensorState9 
                this.atSemaphoreState == 1  
            end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtVTLGCBCL() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlCBCL16 
        condition 
            premise prSeconds9Full 
                this.atSeconds <= 77 
            end_premise 
            and 
            premise prSemaphoreState9Full 
                this.atSemaphoreState == 3 
            end_premise 
            and 
 
     premise prVehicleSensorState9Full 
 
 
  this.atSemaphoreState == 2 
 
     end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtVTLGCBCL() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlCBCL17 
        condition 
            premise prSeconds10 
                this.atSeconds >= 18 
            end_premise 
            and 
            premise prSecondsSup10 
                this.atSeconds < 32 
            end_premise 
            and 
 
     premise prSemaphoreState10 
                this.atSemaphoreState == 3 
            end_premise 
            and 
            premise prVehicleSensorState10 
                this.atHVSS == 1 
            end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtVTLYCBCL() 
 
 
  call this.mtRT() 
            end_instigation 
        end_action 
    end_rule 
 
    rule rlCBCL18 
        condition 
            premise prSeconds10Full 
                this.atSeconds >= 18 
            end_premise 
            and 
            premise prSecondsSup10Full 
                this.atSeconds < 32 


288 
 
 
            end_premise 
            and 
 
     premise prSemaphoreState10Full 
                this.atSemaphoreState == 3 
            end_premise 
            and 
            premise prVehicleSensorState10Full 
                this.atHVSS == 2 
            end_premise 
        end_condition 
        action sequential 
            instigation parallel 
                call this.mtVTLYCBCL() 
                call this.mtRT() 
            end_instigation 
        end_action 
    end_rule 
 
end_fbe 
Fonte: Autoria própria. 
 
Arquivos .h e .cpp da Classe SimuladorNamespaceAPI 
Código 97 - Arquivo .h da API SimuladorNamespaceAPI para a  
estratégia baseado em congestionamento 
#pragma once 
#include <iostream> 
#include <string> 
#include <list> 
#include "../Semaphore.h" 
 
using namespace std; 
 
class SimuladorNamespaceAPI 
{ 
public: 
 
void static addSemaphore(Semaphore* semaphore); 
 
 
static Semaphore* getSemaphoreSim(int id); 
 
void static setStateSim(int id, int state); 
 
void static setCurrentCycleTimeSim(int id, int sec); 
 
 
static void inicializaIdNop(); 
 
static void setSemaphoreStateNop(int id, int state); 
 
static void setSecondsNop(int id, int sec); 
 
static void setHVSSNop(int id, int value); 
 
static void setVVSSNop(int id, int value); 
 
private: 
 
static list<Semaphore*> apiSemaphores; 
 
}; 
Fonte: Autoria própria. 
 
Código 98 - Arquivo .cpp da API SimuladorNamespaceAPI para a  
estratégia baseado em congestionamento 
#include "SimuladorNamespaceAPI.h" 
#include "../Traffic_Light.h" 
#include "instances.h" 
#include <string> 
using namespace std; 
using namespace instance; 


289 
 
 
 
void SimuladorNamespaceAPI::addSemaphore(Semaphore* semaphore) 
{ 
 
apiSemaphores.push_back(semaphore); 
} 
 
Semaphore* SimuladorNamespaceAPI::getSemaphoreSim(int id) 
{ 
 
std::list<Semaphore*>::const_iterator it; 
 
 
for (it = (&apiSemaphores)->begin(); it != (&apiSemaphores)->end(); ++it) { 
 
 
Semaphore* semaphore = (*it); 
 
 
if (semaphore->GetId() == id) 
 
 
{ 
 
 
 
return semaphore; 
 
 
} 
 
} 
} 
 
void SimuladorNamespaceAPI::setStateSim(int id, int state) 
{ 
 
Semaphore* semaphore = getSemaphoreSim(id); 
 
 
switch (state) 
 
{ 
 
case 0: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(GREEN); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(RED); 
 
 
break; 
 
case 1: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(YELLOW); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(RED); 
 
 
break; 
 
case 2: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(RED); 
 
 
break; 
 
case 3: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(GREEN); 
 
 
break; 
 
case 4: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(YELLOW); 
 
 
break; 
 
case 5: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(RED); 
 
 
break; 
 
case 6: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(GREEN); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(RED); 
 
 
break; 
 
case 7: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(YELLOW); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(RED); 
 
 
break; 
 
case 8: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(GREEN); 
 
 
break; 
 
case 9: 
 
 
semaphore->GetHorizontalTrafficLight()->SetState(RED); 
 
 
semaphore->GetVerticalTrafficLight()->SetState(YELLOW); 
 
 
break; 
 
} 


290 
 
 
} 
 
void SimuladorNamespaceAPI::inicializaIdNop() 
{ 
 
instance::main::S1__vector_0::at::atId::setValue(1); 
 
instance::main::S1__vector_1::at::atId::setValue(2); 
 
instance::main::S1__vector_2::at::atId::setValue(3); 
 
instance::main::S1__vector_3::at::atId::setValue(4); 
 
instance::main::S1__vector_4::at::atId::setValue(5); 
 
instance::main::S1__vector_5::at::atId::setValue(6); 
 
instance::main::S1__vector_6::at::atId::setValue(7); 
 
instance::main::S1__vector_7::at::atId::setValue(8); 
 
instance::main::S1__vector_8::at::atId::setValue(9); 
 
instance::main::S1__vector_9::at::atId::setValue(10); 
} 
 
void SimuladorNamespaceAPI::setSemaphoreStateNop(int id, int state) 
{ 
 
switch (id) 
 
{ 
 
case 1: 
 
 
instance::main::S1__vector_0::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 2: 
 
 
instance::main::S1__vector_1::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 3: 
 
 
instance::main::S1__vector_2::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 4: 
 
 
instance::main::S1__vector_3::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 5: 
 
 
instance::main::S1__vector_4::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 6: 
 
 
instance::main::S1__vector_5::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 7: 
 
 
instance::main::S1__vector_6::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 8: 
 
 
instance::main::S1__vector_7::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 9: 
 
 
instance::main::S1__vector_8::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
case 10: 
 
 
instance::main::S1__vector_9::at::atSemaphoreState::setValue(state); 
 
 
break; 
 
} 
} 
 
void SimuladorNamespaceAPI::setSecondsNop(int id, int sec) 
{ 
 
switch (id) 
 
{ 
 
case 1: 
 
 
instance::main::S1__vector_0::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 2: 
 
 
instance::main::S1__vector_1::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 3: 
 
 
instance::main::S1__vector_2::at::atSeconds::setValue(sec); 
 
 
break; 


291 
 
 
 
case 4: 
 
 
instance::main::S1__vector_3::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 5: 
 
 
instance::main::S1__vector_4::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 6: 
 
 
instance::main::S1__vector_5::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 7: 
 
 
instance::main::S1__vector_6::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 8: 
 
 
instance::main::S1__vector_7::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 9: 
 
 
instance::main::S1__vector_8::at::atSeconds::setValue(sec); 
 
 
break; 
 
case 10: 
 
 
instance::main::S1__vector_9::at::atSeconds::setValue(sec); 
 
 
break; 
 
} 
} 
 
void SimuladorNamespaceAPI::setHVSSNop(int id, int value) 
{ 
 
switch (id) 
 
{ 
 
case 1: 
 
 
instance::main::S1__vector_0::at::atHVSS::setValue(value); 
 
 
break; 
 
case 2: 
 
 
instance::main::S1__vector_1::at::atHVSS::setValue(value); 
 
 
break; 
 
case 3: 
 
 
instance::main::S1__vector_2::at::atHVSS::setValue(value); 
 
 
break; 
 
case 4: 
 
 
instance::main::S1__vector_3::at::atHVSS::setValue(value); 
 
 
break; 
 
case 5: 
 
 
instance::main::S1__vector_4::at::atHVSS::setValue(value); 
 
 
break; 
 
case 6: 
 
 
instance::main::S1__vector_5::at::atHVSS::setValue(value); 
 
 
break; 
 
case 7: 
 
 
instance::main::S1__vector_6::at::atHVSS::setValue(value); 
 
 
break; 
 
case 8: 
 
 
instance::main::S1__vector_7::at::atHVSS::setValue(value); 
 
 
break; 
 
case 9: 
 
 
instance::main::S1__vector_8::at::atHVSS::setValue(value); 
 
 
break; 
 
case 10: 
 
 
instance::main::S1__vector_9::at::atHVSS::setValue(value); 
 
 
break; 
 
} 
} 
 
void SimuladorNamespaceAPI::setVVSSNop(int id, int value) 
{ 
 
switch (id) 
 
{ 
 
case 1: 


292 
 
 
 
 
instance::main::S1__vector_0::at::atVVSS::setValue(value); 
 
 
break; 
 
case 2: 
 
 
instance::main::S1__vector_1::at::atVVSS::setValue(value); 
 
 
break; 
 
case 3: 
 
 
instance::main::S1__vector_2::at::atVVSS::setValue(value); 
 
 
break; 
 
case 4: 
 
 
instance::main::S1__vector_3::at::atVVSS::setValue(value); 
 
 
break; 
 
case 5: 
 
 
instance::main::S1__vector_4::at::atVVSS::setValue(value); 
 
 
break; 
 
case 6: 
 
 
instance::main::S1__vector_5::at::atVVSS::setValue(value); 
 
 
break; 
 
case 7: 
 
 
instance::main::S1__vector_6::at::atVVSS::setValue(value); 
 
 
break; 
 
case 8: 
 
 
instance::main::S1__vector_7::at::atVVSS::setValue(value); 
 
 
break; 
 
case 9: 
 
 
instance::main::S1__vector_8::at::atVVSS::setValue(value); 
 
 
break; 
 
case 10: 
 
 
instance::main::S1__vector_9::at::atVVSS::setValue(value); 
 
 
break; 
 
} 
} 
 
void SimuladorNamespaceAPI::setCurrentCycleTimeSim(int id, int sec) 
{ 
 
Semaphore* semaphore = getSemaphoreSim(id); 
 
 
semaphore->SetCurrentCycleTime(sec); 
} 
 
list<Semaphore*> init() 
{ 
 
list<Semaphore*> *tmp = new list<Semaphore*>(); 
 
 
return *tmp; 
} 
 
list<Semaphore*> SimuladorNamespaceAPI::apiSemaphores(init()); 
Fonte: Autoria própria. 


293 
 
 
APÊNDICE F 
CLASSE NAMESPACESPTHREADCOMPILER DO NPCPP 2.0 MULTITHREADING 
 
Este apêndice apresenta os arquivos .h e .cpp da classe NamespacesPThreadCompiler, 
do NPCPP 2.0 multithreading, apresentada na Seção 3.4. 
 
Código 99 - Arquivo .h da classe NamespacesPThreadCompiler 
#ifndef _NAMESPACES_PTHREAD_COMPILER_H_ 
#define _NAMESPACES_PTHREAD_COMPILER_H_ 
 
class Instance; 
class Premise; 
class Attribute; 
class Condition; 
class Rule; 
 
#include "Compiler.h" 
 
#include <string> 
#include <iostream> 
#include <fstream> 
#include <list> 
 
using namespace std; 
 
class NamespacesPThreadCompiler : public Compiler { 
 
public: 
 
 
std::list<std::string> init_premises; 
 
 
std::string getInstanceCompleteName(Instance* instance); 
 
 
std::string getIncludeBlock(); 
 
 
void generateCode(); 
 
void generateCodeInstance(Instance *mainInstance); 
 
void generateAllPremises(Instance *mainInstance); 
 
void generateAllAttributes(Instance *mainInstance); 
 
void generateAllMethods(Instance *mainInstance); 
 
void generateAllRules(Instance *mainInstance); 
 
void generateBody(); 
 
 
void generateCodeAttribute(ofstream& fileH, ofstream& fileCPP, Instance *instance,  
                                  int level); 
 
void generateCodeMethod(ofstream& fileH, ofstream& fileCPP, Instance *instance,  
                               int level); 
 
void generateCodeRule(ofstream& fileH, ofstream& fileCPP, Instance *instance, int  
                             level); 
 
void generateCodePremise(ofstream& fileH, ofstream& fileCPP, Instance *instance,  
                                int level); 
 
 
void generatePremise(ofstream& fileCPP, ofstream& fileH, Premise *premise,          
                            std::string instName, std::string ruleName, int subConds, int  
                            level); 
 
void generateInstigation(ofstream& fileCPP, ofstream& fileH, Instance *instance,  
                                Rule *rule, int level); 


294 
 
 
 
 
 
void assemble(); 
}; 
#endif /* NAMESPACES_2_0_COMPILER_H */ 
Fonte: Autoria própria. 
 
Código 100 - Arquivo .cpp da classe NamespacesPThreadCompiler 
#include "generation/namespaces/NamespacesPThreadCompiler.h" 
 
#include "NOPGraph.h" 
 
#include "elements/Fbe.h" 
#include "elements/Instance.h" 
#include "elements/Attribute.h" 
#include "elements/Method.h" 
#include "elements/Premise.h" 
#include "elements/Subcondition.h" 
#include "elements/Condition.h" 
#include "elements/Rule.h" 
#include "elements/Action.h" 
#include "elements/Instigation.h" 
#include "elements/Expression.h" 
#include "elements/Factor.h" 
#include "elements/ElementFactor.h" 
#include "elements/Symbol.h" 
#include "elements/Type.h" 
#include "elements/Param.h" 
#include "elements/CodeBlock.h" 
#include "elements/Assignment.h" 
#include "elements/Target.h" 
#include "elements/Call.h" 
#include "elements/Conjunction.h" 
#include "elements/Argument.h" 
#include "elements/IncludeBlock.h" 
#include "elements/MainBlock.h" 
 
#include <string> 
#include <iostream> 
#include <fstream> 
#include <vector> 
#include <list> 
#include <map> 
 
// Function that returns the type of the Attribute 
std::string returnTypePThread(int attType) { 
    std::string ret = ""; 
    switch (attType) { 
 
case Type::BOOLEAN_TYPE: 
 
    ret = "bool"; 
            break; 
        case Type::INTEGER_TYPE: 
            ret = "int"; 
            break; 
        case Type::DOUBLE_TYPE: 
            ret = "float"; 
            break; 
        case Type::STRING_TYPE: 
            ret = "std::string"; 
            break; 
        case Type::CHAR_TYPE: 
            ret = "char"; 
            break; 
        default: 
            ret = "undefined"; 


295 
 
 
            break; 
    }//end switch 
    return ret; 
} 
 
// Function that returns the default type of the Attribute 
std::string returnDefaultPThread(short attType) { 
    std::string ret = ""; 
    switch (attType) { 
        case Type::BOOLEAN_TYPE: 
            ret = "false"; 
            break; 
        case Type::INTEGER_TYPE: 
            ret = "0"; 
            break; 
        case Type::DOUBLE_TYPE: 
            ret = "0.0"; 
            break; 
        case Type::STRING_TYPE: 
            ret = "\"\""; 
            break; 
        case Type::CHAR_TYPE: 
            ret = "\" \""; 
            break; 
        default: 
            ret = "null"; 
            break; 
    }//end switch 
    return ret; 
}     
 
// Function that returns the operator 
std::string returnOperationPThread(short attOp) { 
    std::string ret = ""; 
    switch (attOp) { 
        case Symbol::EQUAL_SYMBOL: 
            ret = " == "; 
            break; 
        case Symbol::NOT_EQUAL_SYMBOL: 
            ret = " != "; 
            break; 
        case Symbol::LESSER_THAN_SYMBOL: 
            ret = " < "; 
            break; 
        case Symbol::GREATER_THAN_SYMBOL: 
            ret = " > "; 
            break; 
        case Symbol::LESS_OR_EQUAL_SYMBOL: 
            ret = " <= "; 
            break; 
        case Symbol::GREATER_OR_EQUAL_SYMBOL: 
            ret = " >= "; 
            break; 
        default: 
            ret = "undefined"; 
            break; 
    }//end switch 
    return ret; 
} 
 
std::string NamespacesPThreadCompiler::getInstanceCompleteName(Instance* instance) { 
 
    std::string cmpInstName = instance->getName(); 
 
    if (cmpInstName == "this") { 
         


296 
 
 
        cmpInstName = "main"; 
 
    } else { 
 
        while (instance->getParentInstance() != 0) { 
 
            if (instance->getParentInstance()->getName() == "this") { 
                cmpInstName = "main::" + cmpInstName; 
                break; 
            } 
 
            cmpInstName = instance->getParentInstance()->getName() + "::" +              
                          cmpInstName; 
 
            instance = instance->getParentInstance(); 
        } 
    } 
    return cmpInstName; 
} 
 
std::string NamespacesPThreadCompiler::getIncludeBlock() { 
 
    Fbe *fbe = graph->getFbeMainInstance()->getFbe(); 
 
    std::map<std::string, IncludeBlock*> *includes = fbe->getIncludes(); 
 
    if (includes != 0) { 
 
        for (std::map<std::string, IncludeBlock*>::iterator it = includes->begin(); it  
             != includes->end(); ++it) { 
         
            IncludeBlock *include = it->second; 
 
            if (include->getTarget()->getTargetId() == Target::NAMESPACES_TARGET) { 
 
                return include->getCode(); 
 
            } 
        } 
    } 
 
    return ""; 
} 
 
void NamespacesPThreadCompiler::generateCode() { 
 
    generateCodeInstance(graph->getFbeMainInstance());     
    generateBody(); 
 
} 
 
void NamespacesPThreadCompiler::generateCodeInstance(Instance *mainInstance) { 
 
    // Attributes 
    generateAllAttributes(mainInstance); 
     
    // Methods 
    generateAllMethods(mainInstance); 
     
    // Rules 
    generateAllRules(mainInstance); 
     
    // Premises 
    generateAllPremises(mainInstance); 
 
} 


297 
 
 
 
void NamespacesPThreadCompiler::generateAllAttributes(Instance *mainInstance) { 
 
    std::cout << "generateAllAttributes" << std::endl; 
 
    //creation instances.h file 
    ofstream fileH; 
    std::string filenameH = "Generated/pThread/instances.h"; 
    fileH.open(filenameH.c_str(), ios::out); 
    fileH << "#pragma once" << std::endl; 
    fileH << "#include <string>" << std::endl; 
    fileH << "#include <iostream>" << std::endl; 
    fileH << "namespace instance {" << std::endl; 
 
    //Creation of instances.cpp file 
    ofstream fileCPP; 
    std::string filenameCPP = "Generated/pThread/instances.cpp"; 
    fileCPP.open(filenameCPP.c_str(), ios::out); 
    fileCPP << "#include \"instances.h\"" << std::endl; 
    fileCPP << "#include \"premises.h\"" << std::endl; 
    fileCPP << "#include <string>" << std::endl; 
    fileCPP << "#include <iostream>" << std::endl; 
 
    fileCPP << getIncludeBlock() << std::endl; 
 
    fileCPP << "namespace instance {" << std::endl; 
 
    generateCodeAttribute(fileCPP, fileH, mainInstance, 0); 
     
    fileH << "}"<< std::endl;// end of at namespace 
    fileH.close(); 
    fileCPP << "}"<< std::endl;// end of at namespace 
    fileCPP.close(); 
} 
 
void NamespacesPThreadCompiler::generateCodeAttribute(ofstream& fileCPP, ofstream& 
fileH, Instance *instance, int level) { 
 
    std::cout << "generateCodeAttribute: " << instance->getName() << std::endl; 
 
    std::string tab = getLevel(level); 
 
    std::string instName = ""; 
 
    if (instance->getName() != "this") { 
        instName = instance->getName(); 
    } else { 
        instName = "main";  
    } 
 
    fileH << tab << "\tnamespace "<< instName <<" {" << std::endl; 
    fileCPP << tab << "\tnamespace " << instName << " {" << std::endl; 
 
    std::map<std::string, Attribute*> *attributes = instance->getAttributes(); 
    for (std::map<std::string, Attribute*>::iterator it = attributes->begin(); it !=  
         attributes->end(); ++it) { 
 
        Attribute *attribute = it->second; 
 
        std::cout << "Attribute: " << attribute->getName() << std::endl; 
 
        fileH << tab << "\t\tnamespace at {" << std::endl; 
        fileH << tab << "\t\t\tnamespace "<< attribute->getName() << " {" << std::endl; 
        fileH << tab << "\t\t\t\textern "<< returnTypePThread(attribute->getType()-> 
                 getTypeId()) <<" value;" << std::endl; 
        fileH << tab << "\t\t\t\textern void setValue("<< returnTypePThread(attribute-> 


298 
 
 
                 getType()->getTypeId()) <<" newValue);" << std::endl; 
        fileH << tab << "\t\t\t}"<< std::endl; 
        fileH << tab << "\t\t}"<< std::endl; 
 
        fileCPP << tab << "\t\tnamespace at {" << std::endl; 
        fileCPP << tab << "\t\t\tnamespace " << attribute->getName() << " {" <<  
                   std::endl; 
 
        fileCPP << tab << "\t\t\t\t" << returnTypePThread(attribute->getType()-> 
                   getTypeId()) << " value = " <<  
                   attribute->getFactor()->getStringValue() << ";" << std::endl; 
        fileCPP << tab << "\t\t\t\tvoid setValue("<< returnTypePThread(attribute-> 
                   getType()->getTypeId()) << " newValue) {" << std::endl; 
         
        fileCPP << tab << "\t\t\t\t\tif (value != newValue) {" << std::endl; 
        fileCPP << tab << "\t\t\t\t\t\tvalue = newValue;" << std::endl; 
 
        std::map<std::string, Premise*> *premises = attribute->getPremises(); 
        for (std::map<std::string, Premise*>::iterator it = premises->begin(); it !=  
             premises->end(); ++it) { 
 
            Premise *premise = it->second; 
             
            std::string cmpInstName = getInstanceCompleteName(premise-> 
                                                              getParentInstance()); 
            std::string cmp1st_att = ""; 
 
            Expression *expression = premise->getExpression(); 
            Factor *leftFactor = expression->getLeftFactor(); 
 
            if (leftFactor->getFactorId() == Factor::ELEMENT_FACTOR) { 
 
                ElementFactor *element = (ElementFactor*)leftFactor; 
                cmp1st_att = element->getInstance()->getName(); 
                cmp1st_att = cmp1st_att + "_"; 
                cmp1st_att = cmp1st_att + element->getAttribute()->getName(); 
                 
                fileCPP << tab << "\t\t\t\t\t\tpremise::"<<cmpInstName<<"::"<< 
                           premise->getName()<<"::notify_"<<cmp1st_att<<"(newValue);"<<  
                           std::endl; 
 
            } 
        } 
 
        fileCPP << tab << "\t\t\t\t\t}" << std::endl;//end if 
        fileCPP << tab << "\t\t\t\t}" << std::endl;// end setValue function 
        fileCPP << tab << "\t\t\t}" << std::endl;// end of attribute 
        fileCPP << tab << "\t\t}"<< std::endl;// end of at         
    } 
 
    level++; 
    std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
    if (otherInsts->size() > 0) { 
 
        // loop para serem implementadas as premises das instances 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it !=  
             otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;       
             
            if (otherInst->getName() != "this") { 
                generateCodeAttribute(fileCPP, fileH, otherInst, level); 
            } 
        } 
    } 
 


299 
 
 
    fileH << tab << "\t}"<< std::endl;// end of instance 
    fileCPP << tab << "\t}"<< std::endl;// end of instance     
} 
 
void NamespacesPThreadCompiler::generateAllPremises(Instance *mainInstance) { 
 
    std::cout << "generateAllPremises" << std::endl; 
 
 
    //creation premises.h file 
    ofstream fileH; 
    std::string filenameH = "Generated/pThread/premises.h"; 
    fileH.open(filenameH.c_str(), ios::out); 
    fileH << "#pragma once" << std::endl; 
    fileH << "#include <string>" << std::endl; 
    fileH << "#include <iostream>" << std::endl; 
    fileH << "namespace premise {" << std::endl; 
 
    //Creation of premises.cpp file 
    ofstream fileCPP; 
    std::string filenameCPP = "Generated/pThread/premises.cpp"; 
    fileCPP.open(filenameCPP.c_str(), ios::out); 
    fileCPP << "#include \"premises.h\"" << std::endl; 
    fileCPP << "#include \"rules.h\"" << std::endl; 
    fileCPP << "#include <string>" << std::endl; 
    fileCPP << "#include <pthread.h>" << std::endl; 
    fileCPP << "#include <iostream>" << std::endl; 
    fileCPP << std::endl; 
 
    fileCPP << getIncludeBlock() << std::endl; 
 
    fileCPP << "namespace premise {" << std::endl; 
 
    // implementation of fbe main premises 
    generateCodePremise(fileCPP, fileH, mainInstance, 0); 
     
    fileCPP << "}"<<std::endl; // end of pr namespace 
    fileCPP.close(); 
     
    fileH << "}"<<std::endl; // end of pr namespace 
    fileH.close(); 
 
} 
 
void NamespacesPThreadCompiler::generateCodePremise(ofstream& fileCPP, ofstream& fileH,  
                                                    Instance *instance, int level) { 
 
 
    std::cout << "generateCodePremise: " << instance->getName() << std::endl; 
 
    std::string tab = getLevel(level); 
 
    int subConds = 0; 
    std::string ruleName = ""; 
    std::string instName = ""; 
 
    if (instance->getName() != "this") { 
        instName = instance->getName(); 
    } else { 
        instName = "main";  
    } 
     
    std::map<std::string, Rule*> *rules = instance->getRules(); 
    std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
 
    if (rules->size() > 0 || otherInsts->size() > 0) { 
 
        fileH << tab << "\tnamespace "<< instName <<" {" << std::endl; 


300 
 
 
        fileCPP << tab << "\tnamespace " << instName << " {" << std::endl; 
 
        std::string cmpInstName = getInstanceCompleteName(instance); 
         
        for (std::map<std::string, Rule*>::iterator it = rules->begin(); it != rules-> 
             end(); ++it) { 
 
            Rule *rule = it->second; 
 
            subConds = 0; 
            ruleName = rule->getName(); 
 
            Condition *condition = rule->getCondition(); 
 
            std::map<std::string, Subcondition*> *subConditions = condition-> 
                                                                  getSubconditions(); 
 
            if (subConditions->size() > 0) { 
 
                for (std::map<std::string, Subcondition*>::iterator it=subConditions-> 
                     begin(); it != subConditions->end(); ++it) { 
                     
                    subConds++; 
 
                    Subcondition *subCondition = it->second; 
 
                    std::map<std::string, Premise*> *premises = subCondition-> 
                                                                getPremises(); 
                    for (std::map<std::string, Premise*>::iterator it = premises-> 
                         begin(); it != premises->end(); ++it) { 
                     
                        Premise *premise = it->second; 
 
                        generatePremise(fileCPP, fileH, premise, cmpInstName, ruleName,  
                                        subConds, level); 
 
                    } 
                }     
 
            } else { 
 
                std::map<std::string, Premise*> *premises = condition->getPremises(); 
                for (std::map<std::string, Premise*>::iterator it = premises->begin();  
                     it != premises->end(); ++it) { 
                     
                    Premise *premise = it->second; 
 
                    generatePremise(fileCPP, fileH, premise, cmpInstName, ruleName,  
                                    subConds, level); 
 
                } 
            } 
        } 
 
        level++; 
 
        // loop para serem implementadas as premises das instances 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it !=  
             otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;    
 
            if (otherInst->getName() != "this") { 
                generateCodePremise(fileCPP, fileH, otherInst, level); 
            } 
        } 


301 
 
 
 
        fileH << tab << "\t}" << std::endl; 
        fileCPP << tab << "\t}" << std::endl; 
    } 
} 
 
void NamespacesPThreadCompiler::generatePremise(ofstream& fileCPP, ofstream& fileH,  
                                                Premise *premise, std::string instName,  
                                                std::string ruleName, int subConds, int  
                                                level) { 
 
    std::string tab = getLevel(level); 
 
    fileCPP << tab << "\t\tnamespace " << premise->getName() << " {" << std::endl; 
    fileH << tab << "\t\tnamespace " << premise->getName() << " {" << std::endl; 
 
 
    std::string methodCallInc = ""; 
    std::string methodCallDec = ""; 
     
    std::string leftValue = ""; 
    std::string rightValue = ""; 
    std::string cmpOp = ""; 
 
    std::string preLogicalValue = ""; 
 
    std::string cmpAttType = ""; 
    std::string cmp1st_att = ""; 
    std::string cmpInstName = ""; 
 
 
    Expression *expression = premise->getExpression(); 
    Factor *leftFactor = expression->getLeftFactor(); 
 
 
    if (leftFactor->getFactorId() == Factor::ELEMENT_FACTOR) { 
 
        ElementFactor *element = (ElementFactor*)leftFactor; 
 
        cmp1st_att = element->getInstance()->getName();  
 
        cmp1st_att = cmp1st_att + "_"; 
        cmp1st_att = cmp1st_att + element->getAttribute()->getName(); 
        cmpAttType = returnTypePThread(element->getAttribute()->getType()-> 
                     getTypeId()); 
 
 
 leftValue = element->getAttribute()->getFactor()->getStringValue(); 
 
    } else { 
 
 
 leftValue = leftFactor->getStringValue(); 
 
    } 
 
 
Factor *rightFactor = expression->getRightFactor(); 
 
 
if (rightFactor->getFactorId() == Factor::ELEMENT_FACTOR) { 
 
        ElementFactor *element = (ElementFactor*)rightFactor; 
 
        rightValue = element->getAttribute()->getFactor()->getStringValue(); 
 
    } else { 
 
 
 rightValue = rightFactor->getStringValue(); 
 
    } 
 
    cmpOp = returnOperationPThread(expression->getSymbol()->getSymbolId()); 


302 
 
 
 
    preLogicalValue = (premise->getInitialLogicalValue() ? "true" : "false"); 
 
    // Construção da chamada do namespace das rules 
    /*methodCallInc = methodCallInc + "rule::" + instName + "::" + ruleName + "::inc"; 
    methodCallDec = methodCallDec + "rule::" + instName + "::" + ruleName + "::dec";*/ 
    int subConditionCounter = 0; 
    if (subConds == 0) { 
        if(methodCallInc.compare("") != 0) methodCallInc += "\t\t\t\t\t"; 
        if(methodCallDec.compare("") != 0) methodCallDec += "\t\t\t\t\t"; 
        methodCallInc += "while(rule::" + instName + "::" + ruleName + "::inc_running  
                                == 1) {};\n"; 
        methodCallDec += "while(rule::" + instName + "::" + ruleName + "::dec_running  
                                == 1) {};\n"; 
 
        if(methodCallInc.compare("") != 0) methodCallInc += "\t\t\t\t\t"; 
        if(methodCallDec.compare("") != 0) methodCallDec += "\t\t\t\t\t"; 
        methodCallInc += "pthread_create(&id"+std::to_string(subConditionCounter)+", 
                                         NULL, &rule::" +instName+ "::" +ruleName+ " 
                                         ::inc, NULL);\n"; 
        methodCallDec += "pthread_create(&id"+std::to_string(subConditionCounter+1)+", 
                                         NULL, &rule::" + instName + "::"+ruleName+" 
                                         ::dec, NULL);\n"; 
    } 
    // quando (subConds != 0) significa que há subConditions: neste caso, para cada  
    // subCondition é criado um método inc() e dec() 
    // enumerando esses métodos de acordo com o valor do contador subConds 
    // quando (subConds = 0) significa que na estrutura do fbe, sas conditions segue  
    // direto para as premises... sem subcondition 
    else { 
        char buf[3]; 
 
        sprintf(buf, "%i", subConds);  // convertendo o valor de subConds para string 
 
        /*methodCallInc = methodCallInc + buf; 
        methodCallDec = methodCallDec + buf;*/   
        if(methodCallInc.compare("") != 0) methodCallInc += "\t\t\t\t\t"; 
        if(methodCallDec.compare("") != 0) methodCallDec += "\t\t\t\t\t"; 
        methodCallInc += "while(rule::" + instName + "::" + ruleName + "::inc_running"  
                                + buf + " == 1) {};\n"; 
        methodCallDec += "while(rule::" + instName + "::" + ruleName + "::dec_running"  
                                + buf + " == 1) {};\n"; 
 
        if(methodCallInc.compare("") != 0) methodCallInc += "\t\t\t\t\t"; 
        if(methodCallDec.compare("") != 0) methodCallDec += "\t\t\t\t\t"; 
        methodCallInc += "pthread_create(&id" + std::to_string(subConditionCounter  ) +  
                         ", NULL, &rule::" + instName + "::" + ruleName + "::inc" +  
                         buf + ", NULL);\n"; 
        methodCallDec += "pthread_create(&id" + std::to_string(subConditionCounter+1) +  
                         ", NULL, &rule::" + instName + "::" + ruleName + "::dec" +  
                         buf + ", NULL);\n"; 
    } 
 
    //methodCallInc = methodCallInc + "();"; 
    //methodCallDec = methodCallDec + "();"; 
     
    fileH << tab << "\t\t\textern bool state;" << std::endl; 
    fileH << tab << "\t\t\textern " << cmpAttType << " cpy1st, cpy2nd;" << std::endl; 
     
    fileH << tab << "\t\t\textern void compare();" << std::endl; 
    fileH << tab << "\t\t\textern void notify_"<<cmp1st_att<<"("<<cmpAttType<<  
             " newValue);" << std::endl; 
 
    fileCPP << tab << "\t\t\tbool state = (" << preLogicalValue << ");" << std::endl; 
     
    fileCPP << tab << "\t\t\t" << cmpAttType << " cpy1st = " << leftValue << ";" <<  


303 
 
 
               std::endl; 
    fileCPP << tab << "\t\t\t" << cmpAttType << " cpy2nd = " << rightValue << ";" <<     
               std::endl; 
 
    fileCPP << "\t\t\tpthread_t id0, id1"; 
    for(int i = 2; i < subConditionCounter; i++) fileCPP << ", id" <<  
                                                 std::to_string(i); 
    fileCPP << ";" << std::endl; 
     
    fileCPP << tab << "\t\t\tvoid compare() {"<< std::endl; 
    fileCPP << tab << "\t\t\t\tif (cpy1st"<< cmpOp <<"cpy2nd) {"<< std::endl; 
    fileCPP << tab << "\t\t\t\t\tif (state == false) {"<< std::endl; 
    fileCPP << tab << "\t\t\t\t\t\tstate = true;"<< std::endl; 
    fileCPP << tab << "\t\t\t\t\t\t"<< methodCallInc << std::endl; 
    fileCPP << tab << "\t\t\t\t\t}" << std::endl; 
    fileCPP << tab << "\t\t\t\t} else {" << std::endl; 
    fileCPP << tab << "\t\t\t\t\tif (state == true) {"<< std::endl; 
    fileCPP << tab << "\t\t\t\t\t\tstate = false;"<< std::endl; 
    fileCPP << tab << "\t\t\t\t\t\t"<< methodCallDec << std::endl; 
    fileCPP << tab << "\t\t\t\t\t}" << std::endl; 
    fileCPP << tab << "\t\t\t\t}" << std::endl; 
    fileCPP << tab << "\t\t\t}" << std::endl; 
    fileCPP << tab << "\t\t\tvoid notify_"<<cmp1st_att<<"("<<cmpAttType<< " newValue){"  
            << std::endl; 
    fileCPP << tab << "\t\t\t\tcpy1st = newValue;" << std::endl; 
    fileCPP << tab << "\t\t\t\tcompare();" << std::endl; 
    fileCPP << tab << "\t\t\t}" << std::endl; 
    fileCPP << tab << "\t\t}" << std::endl; 
    fileH << tab << "\t\t}" << std::endl; 
} 
 
void NamespacesPThreadCompiler::generateAllMethods(Instance *mainInstance) { 
 
 
    std::cout << "generateAllMethods" << std::endl; 
     
    //creation methods.h file 
    ofstream fileH; 
    std::string filenameH = "Generated/pThread/methods.h"; 
    fileH.open(filenameH.c_str(), ios::out); 
    fileH << "#pragma once" << std::endl; 
    fileH << "#include <string>" << std::endl; 
    fileH << "#include <iostream>" << std::endl; 
    fileH << "namespace method {" << std::endl; 
 
    //Creation of methods.cpp file 
    ofstream fileCPP; 
    std::string filenameCPP = "Generated/pThread/methods.cpp"; 
    fileCPP.open(filenameCPP.c_str(), ios::out); 
    fileCPP << "#include \"methods.h\"" << std::endl; 
    fileCPP << "#include \"instances.h\"" << std::endl; 
    fileCPP << "#include <string>" << std::endl; 
    fileCPP << "#include <iostream>" << std::endl; 
 
    fileCPP << getIncludeBlock() << std::endl; 
 
    fileCPP << "namespace method {" << std::endl; 
 
    fileH << "\tnamespace main {" << std::endl; 
    fileCPP << "\tnamespace main {" << std::endl; 
 
    // implementação dos method do fbe main 
    generateCodeMethod(fileCPP, fileH, mainInstance, 0); 
 
    fileCPP << "\t}"<< std::endl;// end of method 
    fileH << "\t}"<< std::endl;// end of method 
 


304 
 
 
    fileH << "}"<< std::endl;// end of mt namespace 
    fileH.close(); 
    fileCPP << "}"<< std::endl;// end of mt namespace 
    fileCPP.close(); 
} 
 
void NamespacesPThreadCompiler::generateCodeMethod(ofstream& fileCPP, ofstream& fileH,  
                                                   Instance *instance, int level) { 
 
 
    std::cout << "generateCodeMethod: " << instance->getName() << std::endl; 
 
    std::string tab = getLevel(level); 
 
    std::map<std::string, Method*> *methods = instance->getMethods(); 
 
    if (methods->size() > 0) { 
 
 
 if (instance->getName() != "this") { 
 
        fileH << tab << "\tnamespace " << instance->getName()<<" {" <<  
                        std::endl; 
 
 
 fileCPP << tab << "\tnamespace " << instance->getName() << " {" <<  
                           std::endl; 
 
 }/* else { 
 
 
 fileH << tab << "\tnamespace main {" << std::endl; 
 
 
 fileCPP << tab << "\tnamespace main {" << std::endl; 
 
 }*/ 
 
 
 
        for (std::map<std::string, Method*>::iterator it = methods->begin(); it !=  
             methods->end(); ++it) { 
             
            Method *method = it->second; 
 
 
     fileH << tab << "\t\tnamespace "<< method->getName()<<" {" << std::endl; 
 
     fileCPP << tab << "\t\tnamespace " << method->getName() << " {" <<  
                       std::endl; 
 
 
 
 
            std::string paramsCode = ""; 
 
            std::map<std::string, Param*> *params = method->getParams(); 
            for (std::map<std::string, Param*>::iterator it = params->begin(); it !=  
                 params->end(); ++it) { 
 
                Param *param = it->second; 
                paramsCode = paramsCode + returnTypePThread(param->getType()-> 
                             getTypeId()) + " " + param->getName(); 
                             
            }  
 
            std::map<std::string, CodeBlock*> *codeBlocks = method->getCodeBlocks(); 
            for (std::map<std::string, CodeBlock*>::iterator it = codeBlocks->begin();  
                 it != codeBlocks->end(); ++it) { 
                 
                CodeBlock *codeBlock = it->second; 
                 
                fileH << tab << "\t\t\tvoid " << method-> 
                         getName()<<"("<<paramsCode<<");" << std::endl; 
                fileCPP << tab << "\t\t\tvoid " << method-> 
                           getName()<<"("<<paramsCode<<") {" << std::endl; 
                 
                fileCPP << tab << "\t\t\t\t" << codeBlock->getCode() << std::endl; 
                fileCPP << tab << "\t\t\t}" << std::endl; 
 
            } 
 
            std::map<std::string, Assignment*> *assignments = method->getAssignments(); 
            for (std::map<std::string, Assignment*>::iterator it = assignments-> 


305 
 
 
                 begin(); it != assignments->end(); ++it) { 
 
                Assignment *assignment = it->second; 
                Factor *factor = assignment->getFactor(); 
                 
                ElementFactor *element =  assignment->getElement(); 
 
                Attribute *att = element->getAttribute(); 
 
                std::string typeName = returnTypePThread(att->getType()->getTypeId()); 
 
                std::string cmpInstName = getInstanceCompleteName(att-> 
                                                                  getParentInstance()); 
 
                fileCPP << tab << "\t\t\tvoid " << method->getName() << "() {" <<  
                           std::endl; 
                fileCPP << tab << "\t\t\t\tinstance::" << cmpInstName << "::at::" <<  
                           element->getAttributeName() << "::setValue(" << factor-> 
                           getStringValue() << ");" << std::endl; 
                fileCPP << tab << "\t\t\t}" << std::endl; 
 
                fileH << tab << "\t\t\textern void " << method->getName() << "();" <<  
                         std::endl; 
            } 
 
            fileCPP << tab << "\t\t}"<< std::endl;// end of at namespace 
            fileH << tab << "\t\t}"<< std::endl; 
        } 
         
        level++; 
 
        // loop para serem implementadas os methods das instances 
        std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it !=  
             otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;       
            if (otherInst->getName() != "this") { 
                generateCodeMethod(fileCPP, fileH, otherInst, level); 
            } 
 
        } 
 
        if (instance->getName() != "this") { 
 
 
 
fileCPP << tab << "\t}"<< std::endl;// end of method 
            fileH << tab << "\t}"<< std::endl;// end of method 
 
 
} 
 
    }else{ 
        // loop para serem implementadas os methods das instances 
        std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it !=  
             otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;       
            if (otherInst->getName() != "this") { 
                generateCodeMethod(fileCPP, fileH, otherInst, 1); 
            } 
        } 
    } 
} 
 
void NamespacesPThreadCompiler::generateAllRules(Instance *mainInstance) { 
 
    std::cout << "generateAllRules" << std::endl; 
     


306 
 
 
    //creation rules.h file 
    ofstream fileH; 
    std::string filenameH = "Generated/pThread/rules.h"; 
    fileH.open(filenameH.c_str(), ios::out); 
    fileH << "#pragma once" << std::endl; 
    fileH << "#include <string>" << std::endl; 
    fileH << "#include <iostream>" << std::endl; 
    fileH << "namespace rule {" << std::endl; 
 
    //Creation of rules.cpp file 
    ofstream fileCPP; 
    std::string filenameCPP = "Generated/pThread/rules.cpp"; 
    fileCPP.open(filenameCPP.c_str(), ios::out); 
    fileCPP << "#include \"rules.h\"" << std::endl; 
    fileCPP << "#include \"methods.h\"" << std::endl; 
    fileCPP << "#include \"instances.h\"" << std::endl; 
    fileCPP << "#include <string>" << std::endl; 
    fileCPP << "#include <iostream>" << std::endl; 
    fileCPP << getIncludeBlock() << std::endl; 
 
    fileCPP << "namespace rule {" << std::endl; 
 
    fileH << "\tnamespace main {" << std::endl; 
    fileCPP << "\tnamespace main {" << std::endl; 
 
    // implementação das rules do fbe main 
    generateCodeRule(fileCPP, fileH, mainInstance, 0); 
 
    fileH << "\t}" << std::endl; 
    fileCPP << "\t}" << std::endl; 
 
    fileH << "}"<<std::endl;// end of rl namespace 
    fileH.close(); 
    fileCPP << "}"<<std::endl;// end of rl namespace 
    fileCPP.close(); 
 
} 
 
void NamespacesPThreadCompiler::generateCodeRule(ofstream& fileCPP, ofstream& fileH,  
                                                 Instance *instance, int level) { 
 
    std::cout << "generateCodeRule: " << instance->getName() << std::endl; 
 
    std::string tab = getLevel(level); 
 
    std::map<std::string, Rule*> *rules = instance->getRules(); 
 
    if (rules->size() > 0) { 
 
        if (instance->getName() != "this") { 
            fileH << tab << "\tnamespace "<< instance->getName()<<" {" << std::endl; 
            fileCPP << tab << "\tnamespace " << instance->getName() << " {" <<  
                       std::endl; 
        } 
        /*else{ 
            fileH << tab << "\tnamespace main {" << std::endl; 
            fileCPP << tab << "\tnamespace main {" << std::endl; 
        }*/ 
 
        for (std::map<std::string, Rule*>::iterator it = rules->begin(); it != rules-> 
             end(); ++it) {  
 
            Rule *rule = it->second; 
 
            fileH << tab << "\t\tnamespace " << rule->getName() << " {" << std::endl; 
            fileCPP << tab << "\t\tnamespace " << rule->getName() << " {" << std::endl; 


307 
 
 
 
            Condition *condition = rule->getCondition(); 
                 
            std::map<std::string, Subcondition*> *subconditions = condition-> 
                                                                  getSubconditions(); 
            if (subconditions->size() > 0) { 
 
                int i = 0; 
                std::vector<std::string> list_exprConjunction; 
                std::vector<int> list_numPremises; 
 
                // declaração das variaveis para cada subcondition 
                for (std::map<std::string, Subcondition*>::iterator it=subconditions-> 
                     begin(); it != subconditions->end(); ++it) { 
 
 
 
      Subcondition *subcondition = it->second; 
 
                    i++; 
 
                    fileH << tab << "\t\t\textern int count" << i << ";" << std::endl; 
                    fileH << tab << "\t\t\textern bool status" << i << ";" <<  
                             std::endl; 
                    fileCPP << tab << "\t\t\tint count" << i << " = " << subcondition-> 
                               getNumberApprovedPremises() << ";" << std::endl; 
                    fileCPP << tab << "\t\t\tbool status" << i << ";" << std::endl; 
 
                    Conjunction* conjunction = subcondition->getConjunction(); 
                    std::string conjunctionName = conjunction->getConjunctionName();  
 
                    std::map<std::string, Premise*> *premises = subcondition-> 
                                                                getPremises(); 
                    if (conjunctionName == "AND") { 
                        list_exprConjunction.push_back("=="); 
                        list_numPremises.push_back(premises->size()); 
                    } else { 
                        list_exprConjunction.push_back(">="); 
                        list_numPremises.push_back(1); 
                    }  
                } 
 
                //implementação dos métodos para cada subcondition 
                for (int it = 1; it <= subconditions->size(); ++it) { 
                     
                    fileH << tab << "\t\t\textern bool inc_running" << it << ";" <<  
                             std::endl; 
                    fileH << tab << "\t\t\textern bool dec_running" << it << ";" <<  
                             std::endl; 
                    fileH << tab << "\t\t\textern void* inc" << it << "(void* arg);" <<  
                             std::endl; 
                    fileH << tab << "\t\t\textern void* dec" << it << "(void* arg);" <<  
                             std::endl;                     
                    fileCPP << tab << "\t\t\tbool inc_running" << it << " = 0;" <<  
                               std::endl; 
                    fileCPP << tab << "\t\t\tbool dec_running" << it << " = 0;" <<  
                               std::endl; 
                    fileCPP << tab << "\t\t\tvoid* inc" << it << "(void* arg) {" <<  
                               std::endl; 
                    fileCPP << tab << "\t\t\t\tinc_running" << it << " = 1;" <<  
                               std::endl; 
                    fileCPP << tab << "\t\t\t\tcount" << it << "++;" << std::endl; 
                    fileCPP << tab << "\t\t\t\tstatus" << it << " = false;" <<  
                               std::endl; 
                    fileCPP << tab << "\t\t\t\tif (count" << it << " " <<  
                               list_exprConjunction[it-1] << " " << 
                               list_numPremises[it-1]<<") {" << std::endl; 
                    fileCPP << tab << "\t\t\t\t\tstatus" << it << " = true;" <<  


308 
 
 
                               std::endl; 
                    fileCPP << tab << "\t\t\t\t\tcompareStatusSubConditions();" <<  
                               std::endl; 
                    fileCPP << tab << "\t\t\t\t}"<< std::endl; 
                    fileCPP << tab << "\t\t\t\tinc_running" << it << " = 0;" <<  
                               std::endl; 
                    fileCPP << tab << "\t\t\t}" << std::endl; 
                    fileCPP << tab << "\t\t\tvoid* dec" << it << "(void* arg) {" <<  
                               std::endl; 
                    fileCPP << tab << "\t\t\t\tdec_running" << it << " = 1;" <<  
                               std::endl; 
                    fileCPP << tab << "\t\t\t\tcount" << it << "--;" << std::endl; 
                    fileCPP << tab << "\t\t\t\tdec_running" << it << " = 0;" <<  
                               std::endl; 
                    fileCPP << tab << "\t\t\t}" << std::endl;                
 
                } 
 
                fileH << tab << "\t\t\textern void compareStatusSubConditions();" <<  
                         std::endl; 
                fileCPP << tab << "\t\t\tvoid compareStatusSubConditions() {" <<  
                           std::endl;  
                fileCPP << tab << "\t\t\t\tif ("; 
 
                int conjunctionCondId = condition->getConjunction()-> 
                                                  getConjunctionId(); 
                std::string conjunctionCondValue = ""; 
 
                if (conjunctionCondId == Conjunction::AND_CONJUNCTION) { 
                    conjunctionCondValue = " && "; 
                } else if (conjunctionCondId == Conjunction::OR_CONJUNCTION) { 
                    conjunctionCondValue = " || "; 
                } 
 
                for (int it = 1; it <= subconditions->size(); ++it) { 
                    fileCPP << "(status" << it << " == true)";    
                    if (it != subconditions->size()) { 
                        fileCPP << conjunctionCondValue;  
                    } else { 
                        fileCPP << ") {" << std::endl;     
                    } 
                } 
 
                // Instigations 
                generateInstigation(fileCPP, fileH, instance, rule, level); 
 
                fileCPP << tab << "\t\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t}" << std::endl; 
                fileH << tab << "\t\t}" << std::endl; 
 
            } else {     // não há subconditions 
 
                //Premises 
                std::map<std::string, Premise*> *premises = condition->getPremises(); 
 
                int numPremises = 0; 
                std::string expressionConjunction = ""; 
                std::string subConditionName = ""; 
 
                Conjunction* conjunction = condition->getConjunction(); 
                std::string conjunctionName = conjunction->getConjunctionName(); 
                 
                if (conjunctionName == "AND") { 
                    expressionConjunction = "=="; 
                    numPremises = premises->size(); 


309 
 
 
                } else { 
                    expressionConjunction = ">="; 
                    numPremises = 1; 
                }  
                 
                // declaração da variável 
                fileH << tab << "\t\t\textern int count;" << std::endl; 
                fileCPP << tab << "\t\t\tint count = " << condition-> 
                           getNumberApprovedPremises() << ";" << std::endl; 
 
                // implementação dos métodos 
                fileH << tab << "\t\t\textern bool inc_running;" << std::endl; 
                fileH << tab << "\t\t\textern bool dec_running;" << std::endl; 
                fileH << tab << "\t\t\textern void* inc(void* arg);" << std::endl; 
                fileH << tab << "\t\t\textern void* dec(void* arg);" << std::endl; 
                fileCPP << tab << "\t\t\tbool inc_running = 0;" << std::endl; 
                fileCPP << tab << "\t\t\tbool dec_running = 0;" << std::endl; 
                fileCPP << tab << "\t\t\tvoid* inc(void* arg){" << std::endl; 
                fileCPP << tab << "\t\t\t\tinc_running = 1;" << std::endl; 
                fileCPP << tab << "\t\t\t\tcount++;" << std::endl; 
                 
                fileCPP << tab << "\t\t\t\tif (count "<< expressionConjunction << " "    
                        << numPremises << ") {" << std::endl; 
 
                //instigations             
                generateInstigation(fileCPP, fileH, instance, rule, level);         
 
                fileCPP << tab << "\t\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t\t\tinc_running = 0;" << std::endl; 
                fileCPP << tab << "\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t\tvoid* dec(void* arg){" << std::endl; 
                fileCPP << tab << "\t\t\t\tdec_running = 1;" << std::endl; 
                fileCPP << tab << "\t\t\t\tcount--;" << std::endl; 
                fileCPP << tab << "\t\t\t\tdec_running = 0;" << std::endl; 
                fileCPP << tab << "\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t}" << std::endl; 
                fileH << tab << "\t\t}" << std::endl; 
            }             
        } 
 
        level++; 
 
        // loop para serem implementadas os methods das instances 
        std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it !=  
             otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;       
            if (otherInst->getName() != "this") { 
                generateCodeRule(fileCPP, fileH, otherInst, level); 
            } 
        } 
 
        if (instance->getName() != "this") { 
            fileH << tab << "\t}" << std::endl; 
            fileCPP << tab << "\t}" << std::endl; 
        } 
         
    }else{ 
        // loop para serem implementadas os methods das instances 
        std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it !=  
             otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;      
            if (otherInst->getName() != "this") { 


310 
 
 
                generateCodeRule(fileCPP, fileH, otherInst, 1); 
            } 
        } 
    } 
} 
 
void NamespacesPThreadCompiler::generateInstigation(ofstream& fileCPP, ofstream& fileH, 
Instance *instance, Rule *rule, int level) { 
 
    std::cout << "generateInstigation: " << instance->getName() << std::endl; 
 
    std::string tab = getLevel(level); 
 
    Action *action = rule->getAction();  
 
    std::map<std::string, Instigation*> *instigations = action->getInstigations(); 
    for (std::map<std::string, Instigation*>::iterator it = instigations->begin(); it  
         != instigations->end(); ++it) {       
         
        Instigation *instigation = it->second; 
 
 
 
 
 std::list<Call*> *calls = instigation->getCalls(); 
 
 for (std::list<Call*>::iterator it = calls->begin(); it != calls->end(); ++it){ 
 
 
     Call *call = (*it); 
 
 
     Method *method = call->getMethod(); 
 
            std::string cmpInstName = getInstanceCompleteName(method-> 
                                                              getParentInstance()); 
 
            std::list<Argument*> *arguments = call->getArguments(); 
 
 
 
 
            if (arguments->size() > 0) { 
 
                for (std::list<Argument*>::iterator it = arguments->begin(); it !=  
                     arguments->end(); ++it) { 
 
 
 
      Argument *argument = (*it); 
 
                    Factor *factor = argument->getFactor(); 
 
                    fileCPP << tab << "\t\t\t\t\tmethod::" << cmpInstName << "::" <<  
                               method->getName() << "::" << method->getName() <<  
                               "(" << factor->getStringValue() << ");" << std::endl; 
                } 
 
            } else { 
 
                fileCPP << tab << "\t\t\t\t\tmethod::" << cmpInstName << "::" <<  
                           method->getName() << "::" << method->getName() << "();" <<  
                           std::endl; 
 
            }             
        } 
    } 
} 
 
 
void NamespacesPThreadCompiler::generateBody() { 
 
    std::cout << "generateBody" << std::endl; 
 
    ofstream file; 
    std::string filename = "Generated/pThread/Main.cpp"; 
    file.open(filename.c_str(), ios::out); 


311 
 
 
    file << "#include <stdio.h>" << std::endl; 
    file << "#include <sys/time.h>" << std::endl; 
    file << "#include <iostream>" << std::endl; 
    file << "#include \"premises.h\"" << std::endl; 
    file << "#include \"instances.h\"" << std::endl; 
 
    file << std::endl; 
    file << "using namespace std;" << std::endl; 
    file << std::endl; 
 
    file << "int main() {" << std::endl; 
 
 
    file << "\tFILE *fp = NULL;" << std::endl; 
    file << "\tfp = fopen(\"Arquivo.txt\", \"w\");" << std::endl; 
    file << "\tif (fp != NULL) {" << std::endl; 
    file << "\t\tfprintf(fp, \"Resultados eletronicgate:\");" << std::endl; 
    file << "\t}" << std::endl; 
    file << "\tfclose(fp);" << std::endl; 
 
    file << std::endl; 
    file << "\tclock_t begin = clock();" << std::endl; 
     
    file << std::endl; 
 
    file << "\tint iteration = 100;" << std::endl; 
    file << "\twhile(iteration--){" << std:: endl; 
 
    if (graph->getMainBlock() != 0) { 
 
        std::map<std::string, Assignment*> *assignments = graph->getMainBlock()-> 
                                                                 getAssignments(); 
 
 for (std::map<std::string, Assignment*>::iterator it = assignments->begin(); it  
             != assignments->end(); ++it) { 
 
 
     Assignment *assignment = it->second; 
 
     Factor *factor = assignment->getFactor(); 
 
 
 
 
 
     ElementFactor *element =  assignment->getElement(); 
 
 
 
 
 
     Attribute *att = element->getAttribute(); 
 
 
 
 
 
     Instance *instance = att->getParentInstance(); 
 
 
 
 
 
     std::string typeName = returnTypePThread(att->getType()->getTypeId()); 
 
 
     std::string cmpInstName = getInstanceCompleteName(instance); 
 
 
     file << "\t\tinstance::" << cmpInstName << "::at::" << att->getName()  
                 << "::setValue(" << factor->getStringValue() << ");" << std::endl; 
 
        } 
    } 
     
    file << "\t}" << std::endl; 
 
    file << std::endl; 
 
    file << "\tclock_t end = clock();" << std::endl; 
 
    file << std::endl; 
    file << "\tdouble time_spent = (double)(end - begin);" << std::endl; 
    file << "\ttime_spent /= ((double)CLOCKS_PER_SEC);" << std::endl; 
    file << "\tcout << time_spent << endl;" << std::endl; 
     
    file << "\treturn 0;" << std::endl; 
 


312 
 
 
     
    file << "}" << std::endl; 
 
    file.close();     
} 
 
void NamespacesPThreadCompiler::assemble() { 
    generateCode(); 
} 
Fonte: Autoria própria.


313 
 
 
APÊNDICE G 
CLASSE NAMESPACESPTHREADCOMPILER DO NPCPP 2.0 MULTITHREADING 
 
Este apêndice apresenta os arquivos .h e .cpp da classe NamespacesTPoolCompiler, 
do NPCPP 2.0 multithreading, apresentada na Seção 3.4. 
 
Código 101 - Arquivo .h da classe NamespacesTPoolCompiler 
#ifndef _NAMESPACES_TPOOL_COMPILER_H_ 
#define _NAMESPACES_TPOOL_COMPILER_H_ 
 
class Instance; 
class Premise; 
class Attribute; 
class Condition; 
class Rule; 
 
#include "Compiler.h" 
 
#include <string> 
#include <iostream> 
#include <fstream> 
#include <list> 
 
using namespace std; 
 
class NamespacesTPoolCompiler : public Compiler { 
 
public: 
 
 
std::list<std::string> init_premises; 
 
 
std::string getInstanceCompleteName(Instance* instance); 
 
 
std::string getIncludeBlock(); 
 
 
void generateCode(); 
 
void generateCodeInstance(Instance *mainInstance); 
 
void generateAllPremises(Instance *mainInstance); 
 
void generateAllAttributes(Instance *mainInstance); 
 
void generateAllMethods(Instance *mainInstance); 
 
void generateAllRules(Instance *mainInstance); 
 
void generateBody(); 
 
 
void generateCodeAttribute(ofstream& fileH, ofstream& fileCPP, Instance *instance,  
                                  int level); 
 
void generateCodeMethod(ofstream& fileH, ofstream& fileCPP, Instance *instance,  
                               int level); 
 
void generateCodeRule(ofstream& fileH, ofstream& fileCPP, Instance *instance, int  
                             level); 
 
void generateCodePremise(ofstream& fileH, ofstream& fileCPP, Instance *instance,  
                                int level); 
 
void generatePremise(ofstream& fileCPP, ofstream& fileH, Premise *premise,  
                            std::string instName, std::string ruleName, int subConds,  
                            int level); 
 
void generateInstigation(ofstream& fileCPP, ofstream& fileH, Instance *instance,  
                                Rule *rule, int level); 


314 
 
 
 
 
 
void assemble(); 
}; 
#endif /* NAMESPACES_2_0_COMPILER_H */ 
Fonte: Autoria própria. 
 
Código 102 - Arquivo .cpp da classe NamespacesTPoolCompiler 
#include "generation/namespaces/NamespacesTPoolCompiler.h" 
 
#include "NOPGraph.h" 
 
#include "elements/Fbe.h" 
#include "elements/Instance.h" 
#include "elements/Attribute.h" 
#include "elements/Method.h" 
#include "elements/Premise.h" 
#include "elements/Subcondition.h" 
#include "elements/Condition.h" 
#include "elements/Rule.h" 
#include "elements/Action.h" 
#include "elements/Instigation.h" 
#include "elements/Expression.h" 
#include "elements/Factor.h" 
#include "elements/ElementFactor.h" 
#include "elements/Symbol.h" 
#include "elements/Type.h" 
#include "elements/Param.h" 
#include "elements/CodeBlock.h" 
#include "elements/Assignment.h" 
#include "elements/Target.h" 
#include "elements/Call.h" 
#include "elements/Conjunction.h" 
#include "elements/Argument.h" 
#include "elements/IncludeBlock.h" 
#include "elements/MainBlock.h" 
 
#include <string> 
#include <iostream> 
#include <fstream> 
#include <vector> 
#include <list> 
#include <map> 
 
// Function that returns the type of the Attribute 
std::string returnTypeTPool(int attType) { 
    std::string ret = ""; 
    switch (attType) { 
 
case Type::BOOLEAN_TYPE: 
 
    ret = "bool"; 
            break; 
        case Type::INTEGER_TYPE: 
            ret = "int"; 
            break; 
        case Type::DOUBLE_TYPE: 
            ret = "float"; 
            break; 
        case Type::STRING_TYPE: 
            ret = "std::string"; 
            break; 
        case Type::CHAR_TYPE: 
            ret = "char"; 
            break; 
        default: 
            ret = "undefined"; 


315 
 
 
            break; 
    }//end switch 
    return ret; 
} 
 
// Function that returns the default type of the Attribute 
std::string returnDefaultTPool(short attType) { 
    std::string ret = ""; 
    switch (attType) { 
        case Type::BOOLEAN_TYPE: 
            ret = "false"; 
            break; 
        case Type::INTEGER_TYPE: 
            ret = "0"; 
            break; 
        case Type::DOUBLE_TYPE: 
            ret = "0.0"; 
            break; 
        case Type::STRING_TYPE: 
            ret = "\"\""; 
            break; 
        case Type::CHAR_TYPE: 
            ret = "\" \""; 
            break; 
        default: 
            ret = "null"; 
            break; 
    }//end switch 
    return ret; 
}     
 
// Function that returns the operator 
std::string returnOperationTPool(short attOp) { 
    std::string ret = ""; 
    switch (attOp) { 
        case Symbol::EQUAL_SYMBOL: 
            ret = " == "; 
            break; 
        case Symbol::NOT_EQUAL_SYMBOL: 
            ret = " != "; 
            break; 
        case Symbol::LESSER_THAN_SYMBOL: 
            ret = " < "; 
            break; 
        case Symbol::GREATER_THAN_SYMBOL: 
            ret = " > "; 
            break; 
        case Symbol::LESS_OR_EQUAL_SYMBOL: 
            ret = " <= "; 
            break; 
        case Symbol::GREATER_OR_EQUAL_SYMBOL: 
            ret = " >= "; 
            break; 
        default: 
            ret = "undefined"; 
            break; 
    }//end switch 
    return ret; 
} 
 
std::string NamespacesTPoolCompiler::getInstanceCompleteName(Instance* instance) { 
 
    std::string cmpInstName = instance->getName(); 
 
    if (cmpInstName == "this") { 
         


316 
 
 
        cmpInstName = "main"; 
 
    } else { 
 
        while (instance->getParentInstance() != 0) { 
 
            if (instance->getParentInstance()->getName() == "this") { 
                cmpInstName = "main::" + cmpInstName; 
                break; 
            } 
 
            cmpInstName = instance->getParentInstance()->getName() + "::" +  
                          cmpInstName; 
 
            instance = instance->getParentInstance(); 
        } 
    } 
 
    return cmpInstName; 
} 
 
std::string NamespacesTPoolCompiler::getIncludeBlock() { 
 
    Fbe *fbe = graph->getFbeMainInstance()->getFbe(); 
 
    std::map<std::string, IncludeBlock*> *includes = fbe->getIncludes(); 
 
    if (includes != 0) { 
 
        for (std::map<std::string, IncludeBlock*>::iterator it = includes->begin(); it  
             != includes->end(); ++it) { 
         
            IncludeBlock *include = it->second; 
 
            if (include->getTarget()->getTargetId() == Target::NAMESPACES_TARGET) { 
 
                return include->getCode(); 
 
            } 
        } 
    } 
 
    return ""; 
} 
 
void NamespacesTPoolCompiler::generateCode() { 
 
    generateCodeInstance(graph->getFbeMainInstance());     
    generateBody(); 
 
} 
 
void NamespacesTPoolCompiler::generateCodeInstance(Instance *mainInstance) { 
 
    // Attributes 
    generateAllAttributes(mainInstance); 
     
    // Methods 
    generateAllMethods(mainInstance); 
     
    // Rules 
    generateAllRules(mainInstance); 
     
    // Premises 
    generateAllPremises(mainInstance); 
 


317 
 
 
} 
 
void NamespacesTPoolCompiler::generateAllAttributes(Instance *mainInstance) { 
 
    std::cout << "generateAllAttributes" << std::endl; 
 
    //creation instances.h file 
    ofstream fileH; 
    std::string filenameH = "Generated/tPool/instances.h"; 
    fileH.open(filenameH.c_str(), ios::out); 
    fileH << "#pragma once" << std::endl; 
    fileH << "#include <string>" << std::endl; 
    fileH << "#include <iostream>" << std::endl; 
    fileH << "namespace instance {" << std::endl; 
 
    //Creation of instances.cpp file 
    ofstream fileCPP; 
    std::string filenameCPP = "Generated/tPool/instances.cpp"; 
    fileCPP.open(filenameCPP.c_str(), ios::out); 
    fileCPP << "#include \"instances.h\"" << std::endl; 
    fileCPP << "#include \"premises.h\"" << std::endl; 
    fileCPP << "#include <string>" << std::endl; 
    fileCPP << "#include <iostream>" << std::endl; 
 
    fileCPP << getIncludeBlock() << std::endl; 
 
    fileCPP << "namespace instance {" << std::endl; 
 
    generateCodeAttribute(fileCPP, fileH, mainInstance, 0); 
     
    fileH << "}"<< std::endl;// end of at namespace 
    fileH.close(); 
    fileCPP << "}"<< std::endl;// end of at namespace 
    fileCPP.close(); 
} 
 
void NamespacesTPoolCompiler::generateCodeAttribute(ofstream& fileCPP, ofstream& fileH, 
Instance *instance, int level) { 
 
    std::cout << "generateCodeAttribute: " << instance->getName() << std::endl; 
 
    std::string tab = getLevel(level); 
 
    std::string instName = ""; 
 
    if (instance->getName() != "this") { 
        instName = instance->getName(); 
    } else { 
        instName = "main";  
    } 
 
    fileH << tab << "\tnamespace "<< instName <<" {" << std::endl; 
    fileCPP << tab << "\tnamespace " << instName << " {" << std::endl; 
 
    std::map<std::string, Attribute*> *attributes = instance->getAttributes(); 
    for (std::map<std::string, Attribute*>::iterator it = attributes->begin(); it !=  
         attributes->end(); ++it) { 
 
        Attribute *attribute = it->second; 
 
        std::cout << "Attribute: " << attribute->getName() << std::endl; 
 
        fileH << tab << "\t\tnamespace at {" << std::endl; 
        fileH << tab << "\t\t\tnamespace "<< attribute->getName() << " {" << std::endl; 
        fileH << tab << "\t\t\t\textern "<< returnTypeTPool(attribute->getType()-> 
                 getTypeId()) <<" value;" << std::endl; 


318 
 
 
        fileH << tab << "\t\t\t\textern void setValue("<< returnTypeTPool(attribute-> 
                 getType()->getTypeId()) <<" newValue);" << std::endl; 
        fileH << tab << "\t\t\t}"<< std::endl; 
        fileH << tab << "\t\t}"<< std::endl; 
 
        fileCPP << tab << "\t\tnamespace at {" << std::endl; 
        fileCPP << tab << "\t\t\tnamespace " << attribute->getName() << " {" <<  
                   std::endl; 
 
        fileCPP << tab << "\t\t\t\t" << returnTypeTPool(attribute->getType()-> 
                   getTypeId()) << " value = " << attribute->getFactor()-> 
                   getStringValue() << ";" << std::endl; 
        fileCPP << tab << "\t\t\t\tvoid setValue("<< returnTypeTPool(attribute-> 
                   getType()->getTypeId()) << " newValue) {" << std::endl; 
         
        fileCPP << tab << "\t\t\t\t\tif (value != newValue) {" << std::endl; 
        fileCPP << tab << "\t\t\t\t\t\tvalue = newValue;" << std::endl; 
 
        std::map<std::string, Premise*> *premises = attribute->getPremises(); 
        for (std::map<std::string, Premise*>::iterator it = premises->begin(); it !=  
             premises->end(); ++it) { 
 
            Premise *premise = it->second; 
             
            std::string cmpInstName = getInstanceCompleteName(premise-> 
                                                              getParentInstance()); 
            std::string cmp1st_att = ""; 
 
            Expression *expression = premise->getExpression(); 
            Factor *leftFactor = expression->getLeftFactor(); 
 
            if (leftFactor->getFactorId() == Factor::ELEMENT_FACTOR) { 
 
                ElementFactor *element = (ElementFactor*)leftFactor; 
                cmp1st_att = element->getInstance()->getName(); 
                cmp1st_att = cmp1st_att + "_"; 
                cmp1st_att = cmp1st_att + element->getAttribute()->getName(); 
 
                fileCPP << tab << "\t\t\t\t\t\tpremise::"<<cmpInstName<<"::"<<premise-> 
                           getName()<<"::notify_"<<cmp1st_att<<"(newValue);"<<  
                           std::endl; 
 
            } 
        } 
 
        fileCPP << tab << "\t\t\t\t\t}" << std::endl;//end if 
        fileCPP << tab << "\t\t\t\t}" << std::endl;// end setValue function 
        fileCPP << tab << "\t\t\t}" << std::endl;// end of attribute 
        fileCPP << tab << "\t\t}"<< std::endl;// end of at         
    } 
 
    level++; 
 
    std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
 
    if (otherInsts->size() > 0) { 
 
        // loop para serem implementadas as premises das instances 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it !=  
             otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;      
             
            if (otherInst->getName() != "this") { 
                generateCodeAttribute(fileCPP, fileH, otherInst, level); 
            } 


319 
 
 
        } 
    } 
 
    fileH << tab << "\t}"<< std::endl;// end of instance 
    fileCPP << tab << "\t}"<< std::endl;// end of instance     
} 
 
void NamespacesTPoolCompiler::generateAllPremises(Instance *mainInstance) { 
 
    std::cout << "generateAllPremises" << std::endl; 
 
 
    //creation premises.h file 
    ofstream fileH; 
    std::string filenameH = "Generated/tPool/premises.h"; 
    fileH.open(filenameH.c_str(), ios::out); 
    fileH << "#pragma once" << std::endl; 
    fileH << "#include <string>" << std::endl; 
    fileH << "#include <stdio.h>" << std::endl; 
    fileH << "#include <pthread.h>" << std::endl; 
    fileH << "#include \"thpool.h\"" << std::endl; 
    fileH << "#include <iostream>" << std::endl; 
    fileH << "namespace premise {" << std::endl; 
 
    //Creation of premises.cpp file 
    ofstream fileCPP; 
    std::string filenameCPP = "Generated/tPool/premises.cpp"; 
    fileCPP.open(filenameCPP.c_str(), ios::out); 
    fileCPP << "#include \"premises.h\"" << std::endl; 
    fileCPP << "#include \"rules.h\"" << std::endl; 
    fileCPP << std::endl; 
 
    fileCPP << getIncludeBlock() << std::endl; 
 
    fileCPP << "namespace premise {" << std::endl; 
 
    // implementation of fbe main premises 
    generateCodePremise(fileCPP, fileH, mainInstance, 0); 
     
    fileCPP << "}"<<std::endl; // end of pr namespace 
    fileCPP.close(); 
     
    fileH << "}"<<std::endl; // end of pr namespace 
    fileH.close(); 
 
} 
 
void NamespacesTPoolCompiler::generateCodePremise(ofstream& fileCPP, ofstream& fileH, 
Instance *instance, int level) { 
 
 
    std::cout << "generateCodePremise: " << instance->getName() << std::endl; 
 
    std::string tab = getLevel(level); 
 
    int subConds = 0; 
    std::string ruleName = ""; 
    std::string instName = ""; 
 
    if (instance->getName() != "this") { 
        instName = instance->getName(); 
    } else { 
        instName = "main";  
    } 
     
    std::map<std::string, Rule*> *rules = instance->getRules(); 
    std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
 


320 
 
 
    if (rules->size() > 0 || otherInsts->size() > 0) { 
 
        fileH << tab << "\tnamespace "<< instName <<" {" << std::endl; 
        fileCPP << tab << "\tnamespace " << instName << " {" << std::endl; 
 
        std::string cmpInstName = getInstanceCompleteName(instance); 
         
        for (std::map<std::string, Rule*>::iterator it = rules->begin(); it != rules-> 
             end(); ++it) { 
 
            Rule *rule = it->second; 
 
            subConds = 0; 
            ruleName = rule->getName(); 
 
            Condition *condition = rule->getCondition(); 
 
            std::map<std::string, Subcondition*> *subConditions = condition-> 
                                                                  getSubconditions(); 
 
            if (subConditions->size() > 0) { 
 
                for (std::map<std::string, Subcondition*>::iterator it=subConditions-> 
                     begin(); it != subConditions->end(); ++it) { 
                     
                    subConds++; 
 
                    Subcondition *subCondition = it->second; 
 
                    std::map<std::string, Premise*> *premises = subCondition-> 
                                                                getPremises(); 
                    for (std::map<std::string, Premise*>::iterator it = premises-> 
                         begin(); it != premises->end(); ++it) { 
                     
                        Premise *premise = it->second; 
 
                        generatePremise(fileCPP, fileH, premise, cmpInstName, ruleName,  
                                        subConds, level); 
 
                    } 
                }     
 
            } else { 
 
                std::map<std::string, Premise*> *premises = condition->getPremises(); 
                for (std::map<std::string, Premise*>::iterator it = premises->begin();  
                     it != premises->end(); ++it) { 
                     
                    Premise *premise = it->second; 
 
                    generatePremise(fileCPP, fileH, premise, cmpInstName, ruleName,  
                                    subConds, level); 
 
                } 
            } 
        } 
 
        level++; 
 
        // loop para serem implementadas as premises das instances 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it !=  
             otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;       
 
            if (otherInst->getName() != "this") { 


321 
 
 
                generateCodePremise(fileCPP, fileH, otherInst, level); 
            } 
        } 
 
        fileH << tab << "\t}" << std::endl; 
        fileCPP << tab << "\t}" << std::endl; 
    } 
} 
 
void NamespacesTPoolCompiler::generatePremise(ofstream& fileCPP, ofstream& fileH,  
                                              Premise *premise, std::string instName,  
                                              std::string ruleName, int subConds,  
                                              int level) { 
 
    std::string tab = getLevel(level); 
 
    fileCPP << tab << "\t\tnamespace " << premise->getName() << " {" << std::endl; 
    fileH << tab << "\t\tnamespace " << premise->getName() << " {" << std::endl; 
 
 
    std::string methodCallInc = ""; 
    std::string methodCallDec = ""; 
     
    std::string leftValue = ""; 
    std::string rightValue = ""; 
    std::string cmpOp = ""; 
 
    std::string preLogicalValue = ""; 
 
    std::string cmpAttType = ""; 
    std::string cmp1st_att = ""; 
    std::string cmpInstName = ""; 
 
 
    Expression *expression = premise->getExpression(); 
    Factor *leftFactor = expression->getLeftFactor(); 
 
 
    if (leftFactor->getFactorId() == Factor::ELEMENT_FACTOR) { 
 
        ElementFactor *element = (ElementFactor*)leftFactor; 
 
        cmp1st_att = element->getInstance()->getName();  
 
        cmp1st_att = cmp1st_att + "_"; 
        cmp1st_att = cmp1st_att + element->getAttribute()->getName(); 
        cmpAttType = returnTypeTPool(element->getAttribute()->getType()->getTypeId()); 
 
 
 leftValue = element->getAttribute()->getFactor()->getStringValue(); 
 
    } else { 
 
 
 leftValue = leftFactor->getStringValue(); 
 
    } 
 
    Factor *rightFactor = expression->getRightFactor(); 
 
    if (rightFactor->getFactorId() == Factor::ELEMENT_FACTOR) { 
 
        ElementFactor *element = (ElementFactor*)rightFactor; 
 
        rightValue = element->getAttribute()->getFactor()->getStringValue(); 
 
    } else { 
 
 
 rightValue = rightFactor->getStringValue(); 
 
    } 


322 
 
 
 
    cmpOp = returnOperationTPool(expression->getSymbol()->getSymbolId()); 
 
    preLogicalValue = (premise->getInitialLogicalValue() ? "true" : "false"); 
 
    // Construção da chamada do namespace das rules 
    /*methodCallInc = methodCallInc + "rule::" + instName + "::" + ruleName + "::inc"; 
    methodCallDec = methodCallDec + "rule::" + instName + "::" + ruleName + "::dec";*/ 
    int subConditionCounter = 0; 
    if (subConds == 0) { 
        if(methodCallInc.compare("") != 0) methodCallInc += "\t\t\t\t\t"; 
        if(methodCallDec.compare("") != 0) methodCallDec += "\t\t\t\t\t"; 
        methodCallInc += "thpool_add_work(thpool1, &rule::" + instName + "::" +  
                         ruleName + "::inc, NULL);\n"; 
        methodCallDec += "thpool_add_work(thpool1, &rule::" + instName + "::" +  
                         ruleName + "::dec, NULL);\n"; 
    } 
    // quando (subConds != 0) significa que há subConditions: neste caso, para cada  
    // subCondition é criado um método inc() e dec() 
    // enumerando esses métodos de acordo com o valor do contador subConds 
    // quando (subConds = 0) significa que na estrutura do fbe, sas conditions segue  
    // direto para as premises... sem subcondition 
    else { 
        char buf[3]; 
 
        sprintf(buf, "%i", subConds);  // convertendo o valor de subConds para string 
 
        /*methodCallInc = methodCallInc + buf; 
        methodCallDec = methodCallDec + buf;*/   
 
        if(methodCallInc.compare("") != 0) methodCallInc += "\t\t\t\t\t"; 
        if(methodCallDec.compare("") != 0) methodCallDec += "\t\t\t\t\t"; 
        methodCallInc += "thpool_add_work(thpool1, &rule::" + instName + "::" +  
                         ruleName + "::inc" + buf + ", NULL);\n"; 
        methodCallDec += "thpool_add_work(thpool2, &rule::" + instName + "::" +  
                         ruleName + "::dec" + buf + ", NULL);\n"; 
    } 
 
    //methodCallInc = methodCallInc + "();"; 
    //methodCallDec = methodCallDec + "();"; 
     
    fileH << tab << "\t\t\textern bool state;" << std::endl; 
    fileH << tab << "\t\t\textern " << cmpAttType << " cpy1st, cpy2nd;" << std::endl; 
    fileH << tab << "\t\t\textern threadpool thpool1;" << std::endl; 
     
    fileH << tab << "\t\t\textern void compare();" << std::endl; 
    fileH << tab << "\t\t\textern void notify_"<<cmp1st_att<<"("<<cmpAttType<< "  
             newValue);" << std::endl; 
 
    fileCPP << tab << "\t\t\tbool state = (" << preLogicalValue << ");" << std::endl; 
     
    fileCPP << tab << "\t\t\t" << cmpAttType << " cpy1st = " << leftValue << ";" <<  
               std::endl; 
    fileCPP << tab << "\t\t\t" << cmpAttType << " cpy2nd = " << rightValue << ";" <<  
               std::endl; 
 
    fileCPP << tab << "\t\t\tthreadpool thpool1 = thpool_init(1);" << std::endl; 
     
    fileCPP << tab << "\t\t\tvoid compare() {"<< std::endl; 
    fileCPP << tab << "\t\t\t\tif (cpy1st"<< cmpOp <<"cpy2nd) {"<< std::endl; 
    fileCPP << tab << "\t\t\t\t\tif (state == false) {"<< std::endl; 
    fileCPP << tab << "\t\t\t\t\t\tstate = true;"<< std::endl; 
 
    fileCPP << tab << "\t\t\t\t\t\t"<< methodCallInc << std::endl; 
    fileCPP << tab << "\t\t\t\t\t\tthpool_wait(thpool1);" << std::endl; 
    fileCPP << tab << "\t\t\t\t\t}" << std::endl; 


323 
 
 
    fileCPP << tab << "\t\t\t\t} else {" << std::endl; 
    fileCPP << tab << "\t\t\t\t\tif (state == true) {"<< std::endl; 
    fileCPP << tab << "\t\t\t\t\t\tstate = false;"<< std::endl; 
     
    fileCPP << tab << "\t\t\t\t\t\t"<< methodCallDec << std::endl; 
    fileCPP << tab << "\t\t\t\t\t\tthpool_wait(thpool1);" << std::endl; 
    fileCPP << tab << "\t\t\t\t\t}" << std::endl; 
    fileCPP << tab << "\t\t\t\t}" << std::endl; 
    fileCPP << tab << "\t\t\t}" << std::endl; 
    fileCPP << tab << "\t\t\tvoid notify_"<<cmp1st_att<<"("<<cmpAttType<< " newValue){"  
            << std::endl; 
    fileCPP << tab << "\t\t\t\tcpy1st = newValue;" << std::endl; 
    fileCPP << tab << "\t\t\t\tcompare();" << std::endl; 
    fileCPP << tab << "\t\t\t}" << std::endl; 
    fileCPP << tab << "\t\t}" << std::endl; 
    fileH << tab << "\t\t}" << std::endl; 
} 
 
void NamespacesTPoolCompiler::generateAllMethods(Instance *mainInstance) { 
 
 
    std::cout << "generateAllMethods" << std::endl; 
     
    //creation methods.h file 
    ofstream fileH; 
    std::string filenameH = "Generated/tPool/methods.h"; 
    fileH.open(filenameH.c_str(), ios::out); 
    fileH << "#pragma once" << std::endl; 
    fileH << "#include <string>" << std::endl; 
    fileH << "#include <iostream>" << std::endl; 
    fileH << "namespace method {" << std::endl; 
 
    //Creation of methods.cpp file 
    ofstream fileCPP; 
    std::string filenameCPP = "Generated/tPool/methods.cpp"; 
    fileCPP.open(filenameCPP.c_str(), ios::out); 
    fileCPP << "#include \"methods.h\"" << std::endl; 
    fileCPP << "#include \"instances.h\"" << std::endl; 
    fileCPP << "#include <string>" << std::endl; 
    fileCPP << "#include <iostream>" << std::endl; 
 
    fileCPP << getIncludeBlock() << std::endl; 
 
    fileCPP << "namespace method {" << std::endl; 
 
    fileH << "\tnamespace main {" << std::endl; 
 
fileCPP << "\tnamespace main {" << std::endl; 
 
    // implementação dos method do fbe main 
    generateCodeMethod(fileCPP, fileH, mainInstance, 0); 
 
    fileCPP << "\t}"<< std::endl;// end of method 
    fileH << "\t}"<< std::endl;// end of method 
 
    fileH << "}"<< std::endl;// end of mt namespace 
    fileH.close(); 
    fileCPP << "}"<< std::endl;// end of mt namespace 
    fileCPP.close(); 
} 
 
void NamespacesTPoolCompiler::generateCodeMethod(ofstream& fileCPP, ofstream& fileH,  
                                                 Instance *instance, int level) { 
 
 
    std::cout << "generateCodeMethod: " << instance->getName() << std::endl; 
 
    std::string tab = getLevel(level); 
 


324 
 
 
    std::map<std::string, Method*> *methods = instance->getMethods(); 
 
    if (methods->size() > 0) { 
 
 
 if (instance->getName() != "this") { 
 
     fileH << tab << "\tnamespace " << instance->getName()<<" {" << std::endl; 
 
     fileCPP << tab << "\tnamespace " << instance->getName() << " {" <<  
                       std::endl; 
 
 }/* else { 
 
     fileH << tab << "\tnamespace main {" << std::endl; 
 
     fileCPP << tab << "\tnamespace main {" << std::endl; 
 
 }*/ 
 
 
 
        for (std::map<std::string, Method*>::iterator it = methods->begin(); it !=  
             methods->end(); ++it) { 
             
            Method *method = it->second; 
 
 
    fileH << tab << "\t\tnamespace "<< method->getName()<<" {" << std::endl; 
 
    fileCPP << tab << "\t\tnamespace " << method->getName() << " {" <<  
                      std::endl; 
 
 
 
 
            std::string paramsCode = ""; 
 
            std::map<std::string, Param*> *params = method->getParams(); 
            for (std::map<std::string, Param*>::iterator it = params->begin(); it !=  
                 params->end(); ++it) { 
 
                Param *param = it->second; 
                paramsCode = paramsCode + returnTypeTPool(param->getType()-> 
                             getTypeId()) + " " + param->getName(); 
                             
            }  
 
            std::map<std::string, CodeBlock*> *codeBlocks = method->getCodeBlocks(); 
            for (std::map<std::string, CodeBlock*>::iterator it = codeBlocks->begin();  
                 it != codeBlocks->end(); ++it) { 
                 
                CodeBlock *codeBlock = it->second; 
                 
                fileH << tab << "\t\t\tvoid " << method-> 
                       getName()<<"("<<paramsCode<<");" << std::endl; 
                fileCPP << tab << "\t\t\tvoid " << method-> 
                           getName()<<"("<<paramsCode<<") {" << std::endl; 
                 
                fileCPP << tab << "\t\t\t\t" << codeBlock->getCode() << std::endl; 
 
                fileCPP << tab << "\t\t\t}" << std::endl; 
 
            } 
 
            std::map<std::string, Assignment*> *assignments = method->getAssignments(); 
            for (std::map<std::string, Assignment*>::iterator it = assignments-> 
                 begin(); it != assignments->end(); ++it) { 
 
                Assignment *assignment = it->second; 
                Factor *factor = assignment->getFactor(); 
                 
                ElementFactor *element =  assignment->getElement(); 
 
                Attribute *att = element->getAttribute(); 
 
                std::string typeName = returnTypeTPool(att->getType()->getTypeId()); 
 
                std::string cmpInstName = getInstanceCompleteName(att-> 
                                                                  getParentInstance()); 


325 
 
 
 
                fileCPP << tab << "\t\t\tvoid " << method->getName() << "() {" <<  
                           std::endl; 
 
                fileCPP << tab << "\t\t\t\tinstance::" << cmpInstName << "::at::" <<  
                           element->getAttributeName() << "::setValue(" << factor-> 
                           getStringValue() << ");" << std::endl; 
                fileCPP << tab << "\t\t\t}" << std::endl; 
 
                fileH << tab << "\t\t\textern void " << method->getName() << "();" <<  
                         std::endl; 
                 
            } 
 
            fileCPP << tab << "\t\t}"<< std::endl;// end of at namespace 
            fileH << tab << "\t\t}"<< std::endl; 
        } 
         
        level++; 
 
        // loop para serem implementadas os methods das instances 
        std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it !=  
             otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;       
            if (otherInst->getName() != "this") { 
                generateCodeMethod(fileCPP, fileH, otherInst, level); 
            } 
        } 
 
        if (instance->getName() != "this") { 
 
     fileCPP << tab << "\t}"<< std::endl;// end of method 
            fileH << tab << "\t}"<< std::endl;// end of method 
 
 } 
 
    }else{ 
        // loop para serem implementadas os methods das instances 
        std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it !=  
             otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;       
            if (otherInst->getName() != "this") { 
 
                generateCodeMethod(fileCPP, fileH, otherInst, 1); 
 
            } 
        } 
    } 
} 
 
void NamespacesTPoolCompiler::generateAllRules(Instance *mainInstance) { 
 
    std::cout << "generateAllRules" << std::endl; 
     
    //creation rules.h file 
    ofstream fileH; 
    std::string filenameH = "Generated/tPool/rules.h"; 
    fileH.open(filenameH.c_str(), ios::out); 
    fileH << "#pragma once" << std::endl; 
    fileH << "#include <string>" << std::endl; 
    fileH << "#include <iostream>" << std::endl; 
    fileH << "namespace rule {" << std::endl; 
 
    //Creation of rules.cpp file 


326 
 
 
    ofstream fileCPP; 
    std::string filenameCPP = "Generated/tPool/rules.cpp"; 
    fileCPP.open(filenameCPP.c_str(), ios::out); 
    fileCPP << "#include \"rules.h\"" << std::endl; 
    fileCPP << "#include \"methods.h\"" << std::endl; 
    fileCPP << "#include \"instances.h\"" << std::endl; 
    fileCPP << "#include <string>" << std::endl; 
    fileCPP << "#include <iostream>" << std::endl; 
    fileCPP << getIncludeBlock() << std::endl; 
 
    fileCPP << "namespace rule {" << std::endl; 
 
    fileH << "\tnamespace main {" << std::endl; 
    fileCPP << "\tnamespace main {" << std::endl; 
 
    // implementação das rules do fbe main 
    generateCodeRule(fileCPP, fileH, mainInstance, 0); 
 
    fileH << "\t}" << std::endl; 
    fileCPP << "\t}" << std::endl; 
 
    fileH << "}"<<std::endl;// end of rl namespace 
    fileH.close(); 
    fileCPP << "}"<<std::endl;// end of rl namespace 
    fileCPP.close(); 
 
} 
 
void NamespacesTPoolCompiler::generateCodeRule(ofstream& fileCPP, ofstream& fileH,  
                                               Instance *instance, int level) { 
 
    std::cout << "generateCodeRule: " << instance->getName() << std::endl; 
 
    std::string tab = getLevel(level); 
 
    std::map<std::string, Rule*> *rules = instance->getRules(); 
 
    if (rules->size() > 0) { 
 
        if (instance->getName() != "this") { 
            fileH << tab << "\tnamespace "<< instance->getName()<<" {" << std::endl; 
            fileCPP << tab << "\tnamespace " << instance->getName() << " {" <<  
                       std::endl; 
        } 
        /*else{ 
            fileH << tab << "\tnamespace main {" << std::endl; 
            fileCPP << tab << "\tnamespace main {" << std::endl; 
        }*/ 
 
        for (std::map<std::string, Rule*>::iterator it = rules->begin(); it != rules- 
             >end(); ++it) {  
 
            Rule *rule = it->second; 
 
            fileH << tab << "\t\tnamespace " << rule->getName() << " {" << std::endl; 
            fileCPP << tab << "\t\tnamespace " << rule->getName() << " {" << std::endl; 
 
            Condition *condition = rule->getCondition(); 
                 
            std::map<std::string, Subcondition*> *subconditions = condition-> 
                                                                  getSubconditions(); 
            if (subconditions->size() > 0) { 
 
                int i = 0; 
                std::vector<std::string> list_exprConjunction; 
                std::vector<int> list_numPremises; 


327 
 
 
 
                // declaração das variaveis para cada subcondition 
                for (std::map<std::string, Subcondition*>::iterator it=subconditions-> 
                     begin(); it != subconditions->end(); ++it) { 
 
 
 
      Subcondition *subcondition = it->second; 
 
                    i++; 
 
                    fileH << tab << "\t\t\textern int count" << i << ";" << std::endl; 
                    fileH << tab << "\t\t\textern bool status" << i << ";" <<  
                             std::endl; 
                    fileCPP << tab << "\t\t\tint count" << i << " = " << subcondition-> 
                               getNumberApprovedPremises() << ";" << std::endl; 
                    fileCPP << tab << "\t\t\tbool status" << i << ";" << std::endl; 
 
                    Conjunction* conjunction = subcondition->getConjunction(); 
                    std::string conjunctionName = conjunction->getConjunctionName();  
 
                    std::map<std::string, Premise*> *premises = subcondition-> 
                                                                getPremises(); 
                    if (conjunctionName == "AND") { 
                        list_exprConjunction.push_back("=="); 
                        list_numPremises.push_back(premises->size()); 
                    } else { 
                        list_exprConjunction.push_back(">="); 
                        list_numPremises.push_back(1); 
                    }  
                } 
 
                //implementação dos métodos para cada subcondition 
                for (int it = 1; it <= subconditions->size(); ++it) { 
                     
                    fileH << tab << "\t\t\textern void inc" << it << "(void* arg);" <<  
                             std::endl; 
                    fileH << tab << "\t\t\textern void dec" << it << "(void* arg);" <<  
                             std::endl; 
                     
                    fileCPP << tab << "\t\t\tvoid inc" << it << "(void* arg) {" <<  
                               std::endl; 
                    fileCPP << tab << "\t\t\t\tcount" << it << "++;" << std::endl; 
                     
                    fileCPP << tab << "\t\t\t\tstatus" << it << " = false;" <<  
                               std::endl; 
                    fileCPP << tab << "\t\t\t\tif (count" << it << " " <<  
                               list_exprConjunction[it-1] << " " << 
                               list_numPremises[it-1]<<") {" << std::endl; 
                    fileCPP << tab << "\t\t\t\t\tstatus" << it << " = true;" <<  
                               std::endl; 
                    fileCPP << tab << "\t\t\t\t\tcompareStatusSubConditions();" <<  
                               std::endl; 
                    fileCPP << tab << "\t\t\t\t}"<< std::endl; 
                    fileCPP << tab << "\t\t\t}" << std::endl; 
                    fileCPP << tab << "\t\t\tvoid dec" << it << "(void* arg) {" <<  
                               std::endl; 
                    fileCPP << tab << "\t\t\t\tcount" << it << "--;" << std::endl; 
                     
                    fileCPP << tab << "\t\t\t}" << std::endl;   
                } 
 
                fileH << tab << "\t\t\textern void compareStatusSubConditions();" <<  
                         std::endl; 
                fileCPP << tab << "\t\t\tvoid compareStatusSubConditions() {" <<  
                           std::endl;  
                fileCPP << tab << "\t\t\t\tif ("; 
 


328 
 
 
                int conjunctionCondId = condition->getConjunction()-> 
                                        getConjunctionId(); 
                std::string conjunctionCondValue = ""; 
 
                if (conjunctionCondId == Conjunction::AND_CONJUNCTION) { 
                    conjunctionCondValue = " && "; 
                } else if (conjunctionCondId == Conjunction::OR_CONJUNCTION) { 
                    conjunctionCondValue = " || "; 
                } 
 
                for (int it = 1; it <= subconditions->size(); ++it) { 
                    fileCPP << "(status" << it << " == true)";    
                    if (it != subconditions->size()) { 
                        fileCPP << conjunctionCondValue;  
                    } else { 
                        fileCPP << ") {" << std::endl;     
                    } 
                } 
 
                // Instigations 
                generateInstigation(fileCPP, fileH, instance, rule, level); 
 
                fileCPP << tab << "\t\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t}" << std::endl; 
                fileH << tab << "\t\t}" << std::endl; 
 
            } else {     // não há subconditions 
 
                //Premises 
                std::map<std::string, Premise*> *premises = condition->getPremises(); 
 
                int numPremises = 0; 
                std::string expressionConjunction = ""; 
                std::string subConditionName = ""; 
 
                Conjunction* conjunction = condition->getConjunction(); 
                std::string conjunctionName = conjunction->getConjunctionName(); 
                 
                if (conjunctionName == "AND") { 
                    expressionConjunction = "=="; 
                    numPremises = premises->size(); 
                } else { 
                    expressionConjunction = ">="; 
                    numPremises = 1; 
                }  
                 
                // declaração da variável 
                fileH << tab << "\t\t\textern int count;" << std::endl; 
                fileCPP << tab << "\t\t\tint count = " << condition-> 
                           getNumberApprovedPremises() << ";" << std::endl; 
 
                // implementação dos métodos 
                fileH << tab << "\t\t\textern void inc(void* arg);" << std::endl; 
                fileH << tab << "\t\t\textern void dec(void* arg);" << std::endl; 
                fileCPP << tab << "\t\t\tvoid inc(void* arg){" << std::endl; 
                fileCPP << tab << "\t\t\t\tcount++;" << std::endl; 
                 
                fileCPP << tab << "\t\t\t\tif (count "<< expressionConjunction << " "  
                        << numPremises << ") {" << std::endl; 
 
                //instigations             
                generateInstigation(fileCPP, fileH, instance, rule, level);         
 
                fileCPP << tab << "\t\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t\t}" << std::endl; 


329 
 
 
                fileCPP << tab << "\t\t\tvoid dec(void* arg){" << std::endl; 
                fileCPP << tab << "\t\t\t\tcount--;" << std::endl; 
                 
                fileCPP << tab << "\t\t\t}" << std::endl; 
                fileCPP << tab << "\t\t}" << std::endl; 
                fileH << tab << "\t\t}" << std::endl; 
 
            } 
             
        } 
 
        level++; 
 
        // loop para serem implementadas os methods das instances 
        std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it !=  
             otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;      
            if (otherInst->getName() != "this") { 
                generateCodeRule(fileCPP, fileH, otherInst, level); 
            } 
        } 
 
        if (instance->getName() != "this") { 
            fileH << tab << "\t}" << std::endl; 
            fileCPP << tab << "\t}" << std::endl; 
        } 
         
    }else{ 
        // loop para serem implementadas os methods das instances 
        std::map<std::string, Instance*> *otherInsts = instance->getInstances(); 
        for (std::map<std::string, Instance*>::iterator it = otherInsts->begin(); it !=  
             otherInsts->end(); ++it) { 
 
            Instance *otherInst = it->second;    
            if (otherInst->getName() != "this") { 
 
                generateCodeRule(fileCPP, fileH, otherInst, 1); 
 
            } 
        } 
    } 
} 
 
void NamespacesTPoolCompiler::generateInstigation(ofstream& fileCPP, ofstream& fileH, 
Instance *instance, Rule *rule, int level) { 
 
    std::cout << "generateInstigation: " << instance->getName() << std::endl; 
 
    std::string tab = getLevel(level); 
 
    Action *action = rule->getAction();  
 
    std::map<std::string, Instigation*> *instigations = action->getInstigations(); 
    for (std::map<std::string, Instigation*>::iterator it = instigations->begin();  
         it != instigations->end(); ++it) {       
         
        Instigation *instigation = it->second; 
 
 
 
 
 std::list<Call*> *calls = instigation->getCalls(); 
 
 for (std::list<Call*>::iterator it = calls->begin(); it != calls->end(); ++it){ 
 
 
     Call *call = (*it); 
 
 
     Method *method = call->getMethod(); 


330 
 
 
 
            std::string cmpInstName = getInstanceCompleteName(method-> 
                                                              getParentInstance()); 
 
            std::list<Argument*> *arguments = call->getArguments(); 
 
 
 
 
            if (arguments->size() > 0) { 
 
                for (std::list<Argument*>::iterator it = arguments->begin();  
                     it != arguments->end(); ++it) { 
 
 
 
      Argument *argument = (*it); 
 
                    Factor *factor = argument->getFactor(); 
                     
                    fileCPP << tab << "\t\t\t\t\tmethod::" << cmpInstName << "::"  
                            << method->getName() << "::" << method->getName() << "("  
                            << factor->getStringValue() << ");" << std::endl; 
 
                } 
            } else { 
 
                fileCPP << tab << "\t\t\t\t\tmethod::" << cmpInstName << "::"  
                        << method->getName() << "::" << method->getName() << "();"  
                        << std::endl; 
 
            }             
        } 
    } 
} 
 
void NamespacesTPoolCompiler::generateBody() { 
 
    std::cout << "generateBody" << std::endl; 
 
    ofstream file; 
    std::string filename = "Generated/tPool/Main.cpp"; 
    file.open(filename.c_str(), ios::out); 
    file << "#include <stdio.h>" << std::endl; 
    file << "#include <sys/time.h>" << std::endl; 
    file << "#include <iostream>" << std::endl; 
    file << "#include \"premises.h\"" << std::endl; 
    file << "#include \"instances.h\"" << std::endl; 
 
    file << std::endl; 
    file << "using namespace std;" << std::endl; 
    file << std::endl; 
 
    file << "int main() {" << std::endl; 
 
 
    file << "\tFILE *fp = NULL;" << std::endl; 
    file << "\tfp = fopen(\"Arquivo.txt\", \"w\");" << std::endl; 
    file << "\tif (fp != NULL) {" << std::endl; 
    file << "\t\tfprintf(fp, \"Resultados eletronicgate:\");" << std::endl; 
    file << "\t}" << std::endl; 
    file << "\tfclose(fp);" << std::endl; 
 
    file << std::endl; 
    file << "\tclock_t begin = clock();" << std::endl; 
     
    file << std::endl; 
 
    file << "\tint iteration = 100;" << std::endl; 
    file << "\twhile(iteration--){" << std:: endl; 
 
 
if (graph->getMainBlock() != 0) { 


331 
 
 
 
 
    std::map<std::string, Assignment*> *assignments = graph->getMainBlock()-> 
                                                             getAssignments(); 
 
    for (std::map<std::string, Assignment*>::iterator it = assignments->begin();  
                it != assignments->end(); ++it) { 
 
 
        Assignment *assignment = it->second; 
 
 
 Factor *factor = assignment->getFactor(); 
 
 
 
 
 
 
 ElementFactor *element =  assignment->getElement(); 
 
 
 
 
 
 
 Attribute *att = element->getAttribute(); 
 
 
 
 
 
 
 Instance *instance = att->getParentInstance(); 
 
 
 
 
 
 
 std::string typeName = returnTypeTPool(att->getType()->getTypeId()); 
 
 
 
 std::string cmpInstName = getInstanceCompleteName(instance); 
 
   
 
 file << "\t\tinstance::" << cmpInstName << "::at::" << att->getName()  
                    << "::setValue(" << factor->getStringValue() << ");" << std::endl; 
 
        } 
    } 
     
    file << "\t}" << std::endl; 
 
    file << std::endl; 
 
    file << "\tclock_t end = clock();" << std::endl; 
 
    file << std::endl; 
    file << "\tdouble time_spent = (double)(end - begin);" << std::endl; 
    file << "\ttime_spent /= ((double)CLOCKS_PER_SEC);" << std::endl; 
    file << "\tcout << time_spent << endl;" << std::endl; 
     
    file << "\treturn 0;" << std::endl; 
     
    file << "}" << std::endl; 
 
    file.close(); 
     
} 
 
void NamespacesTPoolCompiler::assemble() { 
    generateCode(); 
} 
Fonte: Autoria própria. 
 
 


332 
 
 
APÊNDICE H 
EXPERIMENTO SUPLEMENTAR COM A APLICAÇÃO BITONIC SORT 
 
Este apêndice apresenta os resultados do experimento com a aplicação Bitonic Sort 
executando sequências com mais de 64 elementos. Da mesma maneira que o experimento 
apresentado na Seção 3.3.3, este experimento suplementar também foi realizado em Python, 
C++ OO, além da implementação em NPCPP 2.0. Foram consideradas sequências com 64, 128, 
256, 512, 1024, 2048 e 4096 elementos. Os testes foram realizados em uma máquina virtual 
EC2 disponibilizada pela AWS (Amazon Web Service) Ubuntu Server 18.04 LTS, com 
processador Intel Xeon E5-2676 v3 @ 2.40GHz. E os resultados foram obtidos em tempo de 
execução, em milissegundos, correspondendo à mediana dos valores obtidos de 20 execuções.  
A Figura 62 apresenta a comparação dos resultados do tempo de execução, em microssegundos.  
 
Figura 62 - Resultado comparativo do Bitonic Sort com mais de 64 elementos 
 
Fonte: Autoria própria 
 
Para todos os casos deste experimento foi calculado o desvio padrão, obtendo um valor 
máximo de 8,2% do valor da mediana (para o cenário com 128 elementos), valor de desvio 
padrão semelhante ao do experimento inicial (com até 64 elementos) realizado no ambiente da 
21
45
106,5000
252
581
1349
3145
7069,5
433
1028
2497,5
6090
14493,5
33470
76178,5
172103
290
648
1426
3263
7290
16174
36046
78555
64
128
256
512
1024
2048
4096
8192
TEMPO DE EXECUÇÃO (MICROSSEGUNDOS)
NÚMERO DE ELEMENTOS DA SEQUÊNCIA BITONIC
COMPARAÇÃO DE DESEMPENHO - BITONIC SORT
C++
Python
NPCPP 2.0


333 
 
 
AWS. Além disso, este teste adicional confirma o desempenho das três implementações ao longo 
do crescimento da quantidade de elementos na sequência, sendo que a implementação em C++ 
OO usual apresenta a melhor performance, seguida do NPCPP 2.0 e, por último, a 
implementação em Python. 
No entanto, no experimento com poucos elementos é mais difícil analisar os resultados, 
conforme apresentado no Capítulo 3. A importância de realizar esse experimento suplementar 
com mais de 64 elementos é a possibilidade de analisar com mais pertinência o comportamento 
do NPCPP 2.0. Este teste permitiu avaliar que à medida que aumenta o número de elementos da 
sequência, o tempo de execução se eleva de maneira levemente logarítmica. Isto é notado 
também nos resultados obtidos pela implementação em Python. Em contrapartida, a aplicação 
em C++ OO apresenta um aumento no tempo de execução de maneira mais escalar. Conforme 
mencionado na Seção 3.5, essa diferença de comportamento entre o NPCPP 2.0 e o C++ OO 
pode ser decorrente pela possibilidade de ainda haver notificações desnecessárias na aplicação 
gerada pelo NPCPP 2.0, o que poderá ser investigado nos trabalhos futuros. 


