# NeuroPON: uma abordagem para o desenvolvimento de redes neurais artificiais utilizando o paradigma orientado a notificações.pdf

 
 
UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ 
PROGRAMA DE PÓS-GRADUAÇÃO EM ENGENHARIA ELÉTRICA E 
INFORMÁTICA INDUSTRIAL 
 
 
 
 
 
 
 
 
FERNANDO SCHÜTZ 
 
 
 
 
 
 
 
 
NEURO-PON: UMA ABORDAGEM PARA O DESENVOLVIMENTO DE 
REDES NEURAIS ARTIFICIAIS UTILIZANDO O PARADIGMA 
ORIENTADO A NOTIFICAÇÕES 
 
 
 
 
 
TESE DE DOUTORADO 
 
 
 
 
 
 
 
 
 
 
 
 
CURITIBA 
2019 


 
 
FERNANDO SCHÜTZ 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
NEURO-PON: UMA ABORDAGEM PARA O DESENVOLVIMENTO DE 
REDES NEURAIS ARTIFICIAIS UTILIZANDO O PARADIGMA 
ORIENTADO A NOTIFICAÇÕES 
 
 
 
 
 
Tese de doutorado apresentada ao Programa de Pós-
Graduação em Engenharia Elétrica e Informática 
Industrial da Universidade Tecnológica Federal do 
Paraná como requisito parcial para obtenção do título 
de “Doutor em Ciências” – Área de Concentração: 
Engenharia de Computação. 
 
Orientador: Prof. Dr. Jean Marcelo Simão 
Co-orientador: Prof. Dr. João Alberto Fabro 
 
 
 
 
 
 
CURITIBA 
2019 
 


 
 
 
 
 
 
 
 
 
 
 
 
 
Dados Internacionais de Catalogação na Publicação 
   
  Schütz, Fernando 
       NeuroPON [recurso eletrônico] : uma abordagem  para o desenvolvi- 
  mento de redes neurais artificiais utilizando o paradigma orientado a  
  notificações / Fernando Schütz.-- 2019. 
       1 arquivo eletrônico (277 f.) : PDF ; 7,03 MB. 
 
       Modo de acesso: World Wide Web. 
       Texto em português com resumo em inglês. 
       Tese (Doutorado) - Universidade Tecnológica Federal do Paraná.  
   Programa de Pós-graduação em Engenharia Elétrica e Informática  
   Industrial. Área de Concentração: Engenharia de Computação, Curitiba,  
   2019.  
       Bibliografia: f. 217-230. 
 
       1. Engenharia elétrica - Teses. 2. Paradigma orientado a notificações.  
   3. Redes neurais (Computação). 4.  Inteligência artificial. 5. Arranjos de  
   lógica programável em campo. 6. Processamento paralelo (Computado- 
   res). 7. Software - Desenvolvimento. 8. Métodos de simulação. 9.  
   Engenharia de computador. I. Simão, Jean Marcelo, orient. II. Fabro,  
   João Alberto, coorient. III. Universidade Tecnológica Federal do Paraná.  
   Programa de Pós-graduação em Engenharia Elétrica e Informática  
   Industrial. IV. Título.  
                                                                                    CDD: Ed. 23 -- 621.3 
Biblioteca Central do Câmpus Curitiba - UTFPR 
Bibliotecária: Luiza Aquemi Matsumoto CRB-9/794 
 
 


 
 
 
Ministério da Educação 
Universidade Tecnológica Federal do Paraná 
Diretoria de Pesquisa e Pós-Graduação 
 
 
 
 
TERMO DE APROVAÇÃO DE TESE Nº 195 
 
A Tese de Doutorado intitulada “NEURO-PON: Uma Abordagem para o Desenvolvimento de Redes 
Neurais Artificiais Utilizando o Paradigma Orientado a Notificações”, defendida em sessão pública 
pelo(a) candidato(a) Fernando Schütz, no dia 31 de maio de 2019, foi julgada para a obtenção do 
título de Doutor em Ciências, área de concentração Engenharia de Computação, e aprovada em 
sua forma final, pelo Programa de Pós-Graduação em Engenharia Elétrica e Informática Industrial. 
 
BANCA EXAMINADORA: 
 
Prof.(a) Dr.(a)  Hugo Vieira Neto - Presidente – (UTFPR) 
Prof.(a) Dr.(a)  Julio Cesar Nievola – (PUC-PR) 
Prof.(a) Dr.(a)  Lucas Ferrari de Oliveira – (UFPR) 
Prof.(a) Dr.(a)  Carlos Raimundo Erig Lima – (UTFPR) 
Prof.(a) Dr.(a)  André Eugênio Lazzaretti - (UTFPR) 
Prof.(a) Dr.(a)  Robson Ribeiro Linhares – (UTFPR) 
 
 
A via original deste documento encontra-se arquivada na Secretaria do Programa, contendo a assinatura 
da Coordenação após a entrega da versão corrigida do trabalho. 
 
 
 
 
Curitiba, 31 de maio de 2019. 
 
 
 
 
 
 
 
 
 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Ao Sr. Plínio Ari Schütz (in memoriam) e à Sra. 
Erenita Schütz pela vida. 
À Fabiana, Francisco e Helena pela convivência 
com paciência e amor, pelo incentivo na partida, e 
pelo alento e alegria ao retorno. 
Aos 
Mafic’s 
pelo 
acompanhamento 
sempre 
presente. 


 
 
AGRADECIMENTOS 
 
Certamente estes parágrafos não irão atender a todas as pessoas que fizeram parte dessa importante 
fase de minha vida. Portanto, desde já, peço desculpas àquelas que não estão presentes entre essas 
palavras, mas elas podem estar certas que fazem parte do meu pensamento e de minha gratidão. 
À DEUS e à minha família vão os primeiros agradecimentos. À minha esposa e amiga Fabiana, e aos 
meus filhos Francisco e Helena, pelo amor e paciência. Aos meus pais Plínio (in memoriam) e Erenita, 
que sempre acreditaram no trabalho, honestidade, humildade e perseverança, valores a mim 
repassados, que foram essenciais para a conclusão deste trabalho. Às minhas irmãs Carla Patrícia e 
Fabiane Cristina, bem como os amados que constituem suas novas famílias, pela afetividade constante. 
Em segundo lugar, mas não menos importante, meus agradecimentos ao Professor Dr. Jean Marcelo 
Simão pela dedicação e pela orientação deste trabalho e, por meio dele, eu me reporto a toda a 
comunidade docente e técnico-administrativa da Universidade Tecnológica Federal do Paraná 
(UTFPR) pela educação, apoio e profissionalismo. Agradeço ao Professor Dr. João Alberto Fabro, pela 
(co)orientação nesta pesquisa e pelos muitos momentos de aprendizado, tanto presenciais quanto à 
distância. Saliento, ainda, que o auxílio destes foi veemente, inclusive para se alcançar a redação deste 
presente documento. Meu agradecimento também aos pesquisadores e professores da banca 
examinadora, pela atenção e contribuição dedicadas a este trabalho. Ainda, no âmbito acadêmico-
profissional, agradeço a equipe em torno do Paradigma Orientado a Notificações, cujos esforços e 
resultados de pesquisa permitiram a experimentação e a conclusão deste projeto. À Fundação 
Araucária pelos meses de fomento ao presente trabalho de pesquisa. 
À minha segunda família, de Curitiba, não posso deixar de externar meus agradecimento pelas diversas 
acolhidas em seus lares. Cristiano, Orlando, Fabiane e Neuza sempre terão (e sempre tiveram) um 
lugar especial no meu coração e, pela participação no finalzinho, meu afilhado Daniel. Agradecimentos 
especiais, também, aos amigos Eden Ricardo, Edenilson e Omero, e suas respectivas famílias, o 
agradecimento pela acolhida, e à “família Natec”, nominadamente Danillo, Kleber, Foronda, Talau, 
Joilson, Bruno, Vilmar, Rubão, Euclides, Hermes. Por fim ao amigo Adriano Francisco Ronszcka, que 
trabalhou comigo de forma incondicional em disciplinas do curso, na pesquisa e no desenvolvimento, 
minha eterna gratidão. 
Enfim, tudo isto posto, sinceros e profundos agradecimentos. 
Fernando Schütz. 
 
 
 


 
 
 
RESUMO 
SCHÜTZ, Fernando. NeuroPON: Uma abordagem para o desenvolvimento de 
Redes Neurais Artificiais utilizando o Paradigma Orientado a Notificações. 2019. 
277 f. Texto de tese (Doutorado em Engenharia Elétrica e Informática Industrial). 
Programa de Pós-Graduação em Engenharia Elétrica e Informática Industrial 
(CPGEI). Universidade Tecnológica Federal do Paraná (UTFPR). Curitiba, 2019. 
 
Redes Neurais Artificiais (RNA), que são inspiradas nas naturalmente paralelas Redes 
Neurais Naturais (RNN), são modelos computacionais capazes de auto ajustar seus pesos 
sinápticos a partir de exemplos, sendo assim capazes de aprender e generalizar soluções. 
Grande parte das implementações de RNA teve seu desenvolvimento guiado pelo Paradigma 
Imperativo (PI), geralmente resultando em programas acoplados. Assim, mesmo se inspiradas 
em RNN paralelas, as RNA não têm uma distribuição efetiva de execução, quando 
desenvolvidas sob PI, devido ao seu fator de acoplamento. Como alternativa, o Paradigma 
Orientado a Notificações (PON) surge como uma abordagem de processamento que se 
baseia em entidades colaborativas e notificantes. O PON tende a ser mais eficiente e 
desacoplado quando comparado ao PI, pois permite a exploração de processamento de 
maneira mais simples e eficiente. Tais vantagens se tornam ainda mais relevantes em 
sistemas que devem ter partes desacopladas, a serem executadas em paralelo, como RNA. 
A execução de aplicações PON, entretanto, nem sempre pode ser feita da forma mais eficiente 
pelas arquiteturas de computadores tradicionais, baseados em modelos de execução 
sequencial (tanto monocore como multicore). Neste contexto, a tecnologia de Field 
Programmable Gate Arrays (FPGA) é uma alternativa para o desenvolvimento em PON. Neste 
âmbito surgiu a tecnologia PON-HD, que permite se desenvolver sistemas de forma 
declarativa utilizando a linguagem própria do PON (LingPON) e, por meio de compilador 
específico, gerar código paralelo para execução em dispositivos FPGA. O presente trabalho 
propõe então a especificação e elaboração do modelo computacional NeuroPON, que permite 
a construção de RNA com conceitos do PON, por meio de uma linguagem declarativa de alto 
nível. Este modelo herda do PON a abstração do conhecimento por meio de regras lógico-
causais, utilizando uma linguagem declarativa. Também é foco deste modelo a geração de 
código eficiente para execução em processadores monocore, concorrente para execução em 
processadores multicore e paralelizável para dispositivos FPGA. Tais códigos permitem que 
a RNA criada execute no modo operacional e de treinamento, de forma adaptável e escalável, 
em tais plataformas computacionais. Testes foram realizados utilizando materializações do 
PON em software (Framework PON C++ 2.0, 3.0 e LingPON), bem como em hardware (PON-
HD). Tais testes demonstraram a factibilidade do modelo computacional NeuroPON. Os 
resultados de experimentos com NeuroPON em software monoprocessado, quando 
comparados com equivalentes em PI, apresentaram um alto nível de desacoplamento, 
tornando explícitos os elementos factuais e lógico-causais. Experimentos com o Framework 
PON C++ 3.0 e com o Framework Elixir/Erlang demonstraram a distribuição das entidades 
PON para execução em diferentes núcleos de processamento (multicore). Experimentos 
efetuados em hardware (PON-HD) resultaram na geração de código VHDL paralelo, de forma 
transparente ao usuário. Em suma, o NeuroPON se apresenta de fato como um novo modelo 
computacional para RNA, que apresenta características ausentes em demais abordagens da 
literatura, como treinamento e execução de RNA em plataformas distintas por meio entidades 
neurais efetivas criadas a partir de sua implementação em linguagem descritiva de alto nível. 
 
Palavras-chave: Paradigma Orientado a Notificações, Redes Neurais Artificiais, 
Sistemas Paralelizáveis, Field Programmable Gate Arrays, Paradigmas de Software.  


 
 
ABSTRACT 
SCHÜTZ, Fernando. NeuroPON: An approach to the development of Artificial 
Neural Networks using the Notification Oriented Paradigm. 2019. 277 f. Texto de 
tese (Doutorado em Engenharia Elétrica e Informática Industrial). Programa de Pós-
Graduação em Engenharia Elétrica e Informática Industrial (CPGEI). Universidade 
Tecnológica Federal do Paraná (UTFPR). Curitiba, 2019. 
 
Artificial Neural Networks (ANN), which are inspired by the naturally parallel Natural Neural 
Networks (NNN), are computational models capable of self-adjusting their synaptic weights 
based on examples, thus being able to learn and generalize solutions. Most ANN 
implementations were driven by the Imperative Paradigm (IP), often resulting in coupled 
programs. Thus, even if inspired by parallel NNN, ANN does not have an effective execution 
distribution when developed under IP, due to their coupling factor. Alternatively, the Notification 
Oriented Paradigm (NOP) emerges as a processing approach that relies on collaborative and 
notifying entities. NOP tends to be more efficient and decoupled compared to IP, as it allows 
a simpler and more efficient exploration of processing. Such advantages become even more 
relevant in systems that must have decoupled parts to be executed in parallel, such as ANN. 
The execution of NOP applications, however, cannot always be held most efficiently by 
traditional computer architectures based on sequential execution models (both monocore and 
multicore). In this context, Field Programmable Gate Arrays (FPGA) technology is a great 
alternative to NOP development. In this sense emerged the NOPHD technology, allowing the 
development of systems declaratively using NOP's own language (NOPL) and, through a 
specific compiler, generate parallel code for execution on FPGA devices. The present work 
proposes the specification and elaboration of the computational model NeuroNOP, which 
allows the construction of ANN with NOP concepts through a high-level declarative language. 
This model inherits from NOP the abstraction of knowledge through logical-causal rules using 
a declarative language. The focus of this model is also on efficient code generation for 
execution on monocore processors, concurrent for execution on multicore processors and 
parallel to FPGA devices. Such codes allow the created ANN to run in operational and training 
mode, adaptably and scalably, on such computational platforms. Tests were performed using 
NOP materializations in software (NOP Framework C++ 2.0, 3.0 and NOPL) as well as in 
hardware (NOPHD). Such tests proved the feasibility of the NeuroNOP computational model. 
The results of experiments with NeuroNOP in monoprocessor software, when compared with 
equivalents in IP, revealed a high level of decoupling, making the factual and logical-causal 
elements explicit. Experiments with the Framework NOP C++ 3.0 and the Framework 
Elixir/Erlang have proven the distribution of NOP entities for execution in different cores 
(multicore). Hardware experiments (NOPHD) resulted in the generation of parallel VHDL code, 
in a transparent way to the user. In short, NeuroNOP presents itself as a new computational 
model for ANN, which presents absent characteristics from other approaches in the literature, 
such as ANN execution and training in different computational platforms, through effective 
neural entities created from its descriptive and high-level language implementation. 
 
Keywords: Notification Oriented Paradigm, Artificial Neural Network, Parallel 
Systems, Field Programmable Gate Arrays, Software Paradigms.  
 
 
 


 
 
LISTA DE ILUSTRAÇÕES 
FIGURA 1 – REPRESENTAÇÃO DA ESTRUTURA DE UMA RNA: NEURÔNIOS E CONEXÕES SINÁPTICAS. OS NEURÔNIOS PODEM REALIZAR 
SEU PROCESSAMENTO DE FORMA COMPLETAMENTE PARALELA ................................................................................... 23 
FIGURA 2 - ESQUEMA REPRESENTATIVO DE UM NEURÔNIO ................................................................................................. 24 
FIGURA 3 - EXEMPLO DE ARQUITETURA DE UM SBR (ADAPTADO DE AL-TAANI, 2007) .......................................................... 46 
FIGURA 4 - EXEMPLO DE SBR: (A) 4 REGRAS DO SISTEMA;  (B) FLUXO DO SISTEMA DE PRODUÇÃO APÓS A REGRA 1 SER DISPARADA 
(ADAPTADO DE AL-TAANI, 2007) ...................................................................................................................... 47 
FIGURA 5 - EXEMPLO DE MODELO DE FLUXO DE DADOS NO POD: (A) CÓDIGO SEQUENCIAL; (B) SEU EQUIVALENTE EM MODELO 
DATAFLOW (ADAPTADO DE JOHNSTON ET AL., 2004) ........................................................................................... 48 
FIGURA 6 - ETAPAS E SUB ETAPAS EXECUTADAS EM UM COMPILADOR (ADAPTADO DE FERREIRA, 2015) ................................... 51 
FIGURA 7 - ARQUITETURA DE UM DISPOSITIVO FPGA SRAM (ADAPTADO DE BROWN; VRANESIC, 2008) .............................. 54 
FIGURA 8 - ESTRUTURA INTERNA DE UMA FPGA (ADAPTADO DE BROWN; VRANESIC, 2008) ............................................... 55 
FIGURA 9 - ESTRUTURA DE UMA LUT DE DUAS ENTRADAS: (A) TABELA VERDADE; (B) CIRCUITO REPRESENTATIVO IMPLEMENTADO VIA 
MULTIPLEXADORES (ADAPTADO DE BROWN; VRANESIC, 2008)............................................................................. 56 
FIGURA 10 – DIAGRAMA DE REDE NEURAL ARTIFICIAL (ADAPTADO DE HEATON, 2015) ........................................................ 63 
FIGURA 11 - NEURÔNIO ARTIFICIAL - MODELO DE MCCULLOCH E PITTS (SILVA, 2010A) ........................................................ 64 
FIGURA 12 - ESTRUTURA DE UMA RNA MULTI LAYER PERCEPTRON (SILVA ET AL., 2010A) .................................................... 67 
FIGURA 13 - ALGORITMO DE TREINAMENTO DE UMA RNA MLP UTILIZANDO O MÉTODO BP (SILVA ET AL., 2010A) ................... 72 
FIGURA 14 - ALGORITMO DE OPERAÇÃO DE UMA RNA MLP (SILVA ET AL., 2010) ............................................................... 73 
FIGURA 15 - FLUXO DE TRABALHO DSE DA LINGUAGEM VINNSL (ADAPTADO DE BERAN ET AL., 2008) ..................................... 75 
FIGURA 16 - ESQUEMA DEMONSTRANDO A RNA IMPLEMENTADA EM HARDWARE (ADAPTADO E TRADUZIDO DE ALI E MOHAMMED, 
2010) ............................................................................................................................................................ 84 
FIGURA 17 - ESQUEMA DE CONFIGURAÇÃO DA RNA MLP EM NEDJAH ET AL., 2012 .............................................................. 86 
FIGURA 18 - FLUXO DE DESENVOLVIMENTO DE RNA UTILIZANDO A FERRAMENTA  ANGE (BAPTISTA; MORGADO-DIAS, 2017) 87 
FIGURA 19 - TAXONOMIA DE PARADIGMAS DE PROGRAMAÇÃO INCLUINDO O PON (XAVIER, 2014) ........................................ 92 
FIGURA 20 - ESTRUTURA DO MODELO DE NOTIFICAÇÕES PON (ADAPTADO DE SIMÃO ET AL., 2009B) ...................................... 93 
FIGURA 21 - EXEMPLO DE UM REGRA (RULE) EM PON ..................................................................................................... 93 
FIGURA 22 - COLABORAÇÕES ENTRE ENTIDADES DO MODELO PON (ADAPTADO DE LINHARES ET AL., 2015) ............................ 95 
FIGURA 23 - ESTRUTURA DO FRAMEWORK PON C++ 2.0, DEMONSTRADA POR DIAGRAMA DE CLASSES E PACOTES EM UML 
(RONSZCKA, 2012) ........................................................................................................................................ 98 
FIGURA 24 - ESTRUTURA DO PACOTE CORE, REPRESENTADA POR MEIO DE UM DIAGRAMA DE CLASSES EM UML (RONSZCKA, 
2012) ............................................................................................................................................................ 99 
FIGURA 25 – DIAGRAMA DE ATIVIDADES UML: ETAPAS DA COMPILAÇÃO LINGPON ............................................................. 106 
FIGURA 26 – DIAGRAMA DE PACOTES EM UML DO FRAMEWORK PON C++ 3.0. ................................................................ 109 
FIGURA 27 - DIAGRAMA DE ATIVIDADE UML: FLUXO DE CONTROLE DAS ENTIDADES PON NO  FRAMEWORK PON C++ 3.0 (SCHÜTZ 
ET AL., 2018). ............................................................................................................................................... 111 
FIGURA 28 - MODELAGEM OS ELEMENTOS PON EM POA (NEGRINI ET. AL, 2019) ............................................................ 113 


 
 
FIGURA 29 - ARQUITETURA DA COMPILAÇÃO PARA ERLANG/ELIXIR (NEGRINI ET AL., 2019) ................................................ 114 
FIGURA 30 - MODELO DE EXECUÇÃO DO PON EM HARDWARE .......................................................................................... 115 
FIGURA 31 - DIAGRAMA DE BLOCOS EM SYSML DE ENTIDADES PON EM HARDWARE UTILIZADOS NO FRAMEWORK PON-HD 1.0 
(KERSCHBAUMER, 2018) ............................................................................................................................ 117 
FIGURA 32 -  DIAGRAMA DE ATIVIDADES UML: REPRESENTAÇÃO DO DON POR MEIO DE SUAS ATIVIDADES E CICLOS DE 
DESENVOLVIMENTO (MENDONÇA ET AL, 2015) ................................................................................................ 120 
FIGURA 33 - DIAGRAMA DE COMPONENTE DE UMA RULE (MENDONÇA, 2016) ................................................................ 120 
FIGURA 34 - ELEMENTOS DO DIAGRAMA DE INSTÂNCIAS DO PON (KOSSOSKI, 2015) ......................................................... 121 
FIGURA 35 – DIAGRAMA DE ATIVIDADES EM UML: APRESENTAÇÃO DO PROCESSO DE GERAÇÃO DE RNA  POR MEIO DO MODELO 
COMPUTACIONAL NEUROPON .......................................................................................................................... 126 
FIGURA 36 – DIAGRAMA DE INSTÂNCIAS PON: ESTRUTURA DE UM NEURÔNIO EM NEUROPON .............................................. 131 
FIGURA 37 - ESTRUTURA DE UMA RNA EM NEUROPON: MODO DE OPERAÇÃO ................................................................... 135 
FIGURA 38 - ESTRUTURA DE UMA RNA EM NEUROPON, NO MODO DE TREINAMENTO ......................................................... 136 
FIGURA 39 - DIAGRAMA DE ATIVIDADES EM UML: CADEIA DE NOTIFICAÇÕES DO ALGORITMO DE  TREINAMENTO RNA MLP PELO 
MÉTODO BP, UTILIZANDO PON ......................................................................................................................... 138 
FIGURA 40 - DIAGRAMA DE CLASSES EM UML: RELACIONAMENTO ENTRE AS ENTIDADES FBE PARA A MATERIALIZAÇÃO DO MODELO 
COMPUTACIONAL NEUROPON UTILIZANDO FRAMEWORK PON C++ 2.0. ................................................................. 147 
FIGURA 41 – DIAGRAMA DE OBJETOS EM UML: FLUXO DE EXECUÇÃO CONCORRENTE DAS ENTIDADES PON, NA EXECUÇÃO DE UMA 
RNA MLP, UTILIZANDO FRAMEWORK PON C++ 3.0 ............................................................................................ 159 
FIGURA 42 – TEMPOS DE EXECUÇÃO (EM MILISSEGUNDOS) DO TREINAMENTO DE RNA MLP COM MÉTODO BP, UTILIZANDO O 
MODELO COMPUTACIONAL NEUROPON EM MATERIALIZAÇÕES DE SOFTWARE DO PON, PARA A BASE DE DADOS DA FLOR DE 
IRIS. ............................................................................................................................................................. 160 
FIGURA 43 – CAPTURA DE TELA (SCREENSHOT) DO HISTÓRICO DA CPU, APRESENTANDO O USO DOS NÚCLEOS NA EXECUÇÃO DO 
TREINAMENTO MULTICORE, POR MEIO DO FRAMEWORK PON C++ 3.0: (A) 1 NÚCLEO; (B) 2 NÚCLEOS; (C) 4 NÚCLEOS; (D) 8 
NÚCLEOS. ...................................................................................................................................................... 161 
FIGURA 44 - GRÁFICO DE UTILIZAÇÃO DO USO DE NÚCLEOS DE PROCESSAMENTO POR MEIO DO COMANDO TOP EM LINUX ........... 162 
FIGURA 45 - REPRESENTAÇÃO GRÁFICA DOS TEMPOS MÉDIOS DE EXECUÇÃO NEUROPON DE UMA RNA MLP PARA A FUNÇÃO XOR 
EM ERLANG ................................................................................................................................................... 167 
FIGURA 46 - MODELO DE OBJETOS PON: IMPLEMENTAÇÃO DA RNA MLP PARA O TREINAMENTO IRIS DATASET ...................... 169 
FIGURA 47 - PROCESSO DE QUANTIZAÇÃO EM NEUROPON-HD POR MEIO DE UM DIAGRAMA DE ATIVIDADES UML .................... 177 
FIGURA 48 - DIAGRAMA DE ATIVIDADES UML: DETALHAMENTO DA CADEIA DE NOTIFICAÇÕES, POR MEIO  DA APRESENTAÇÃO DOS 
METHODS PON A SEREM IMPLEMENTADOS EM LINGPON-HD. .............................................................................. 180 
FIGURA 49 - RECORTE DA NETLIST, DO CIRCUITO LINGPON-HD EM VHDL, GERADA SINTETIZADOR DA FERRAMENTA QUARTUS II: 
COMPONENTES SINTETIZADOS QUE IMPLEMENTAM O CÓDIGO 28............................................................................. 189 
 
 


 
 
LISTA DE TABELAS 
 
TABELA 1 - ARQUITETURAS DE RNA............................................................................................................................... 67 
TABELA 2 - COMPARAÇÃO ENTRE LINGUAGENS DECLARATIVAS, BASEADAS EM XML, PARA DEFINIÇÃO DE RNA  (ADAPTADO DE 
UNIVERSITY OF VIENNA, 2008) ........................................................................................................................... 77 
TABELA 3 - COMPARATIVO ENTRE TECNOLOGIAS DE HARDWARE DIGITAL (DEOTALE; DEOLE, 2014) ....................................... 88 
TABELA 4 - COMPARAÇÃO ENTRE TRABALHOS CORRELATOS E A PROPOSTA DO MODELO COMPUTACIONAL NEUROPON:  
CARACTERÍSTICAS PRESENTES E AUSENTES .............................................................................................................. 89 
TABELA 5 - REQUISITOS FUNCIONAIS DO MODELO COMPUTACIONAL NEUROPON ................................................................ 124 
TABELA 6 - REQUISITOS NÃO FUNCIONAIS DO MODELO COMPUTACIONAL NEUROPON ......................................................... 125 
TABELA 7 - DEFINIÇÃO DE UM NEURÔNIO EM NEUROPON - ENTIDADE NEURON ................................................................. 128 
TABELA 8 - DEFINIÇÃO DE UMA RNA EM NEUROPON - ENTIDADE NETWORK ..................................................................... 132 
TABELA 9 - RESUMO DOS EXPERIMENTOS DESENVOLVIDOS ............................................................................................... 144 
TABELA 10 - RESULTADOS DO TREINAMENTO DE RNA MLP COM MÉTODO BP EM  FRAMEWORK PON C++ 2.0 PARA A FUNÇÃO XOR
 ................................................................................................................................................................... 152 
TABELA 11 – RESULTADOS COMPARATIVOS ENTRE O TREINAMENTO BP DE UMA RNA MLP: NEURONOP UTILIZANDO O FRAMEWORK 
PON C++ 2.0 VERSUS LINGUAGEM C PROCEDIMENTAL (CLASSIFICAÇÃO IRIS DATASET) .............................................. 156 
TABELA 12 - RESULTADOS DA EXECUÇÃO DO VALGRIND SOBRE APLICAÇÃO GERADA A PARTIR DO FRAMEWORK PON C++ 3.0 ...... 163 
TABELA 13 - RESULTADOS DA EXECUÇÃO DO EXPERIMENTO NEUROPON DE UMA RNA MLP PARA A FUNÇÃO XOR EM ERLANG ... 166 
TABELA 14 - RESULTADOS DO TREINAMENTO PARA O SISTEMA DE CLASSIFICAÇÃO IRIS DATASET (LINGPON X C) ....................... 173 
TABELA 15 - EXEMPLOS DE QUANTIZAÇÃO DE VALORES REAIS EM INTEIROS .......................................................................... 176 
TABELA 16 – REPRESENTAÇÃO DE VALORES INTEIROS COM DIFERENTES QUANTIDADES DE BITS ................................................ 176 
TABELA 17 – TABELA PRESENTATIVA DE UMA LOOKUP TABLE, IMPLEMENTADA PARA A FUNÇÃO QUE RETORNA  A TANGENTE 
HIPERBÓLICA DE UM VALOR, EM NEUROPON. ..................................................................................................... 178 
TABELA 18 - VALORES UTILIZADOS NO EXPERIMENTO XOR EM NEUROPON-HD .................................................................. 181 
TABELA 19 - RESULTADOS DOS EXPERIMENTOS DE IMPLEMENTAÇÃO DE RNA POR MEIO DE VHDL .......................................... 192 
TABELA 20 - QUANTIDADE DE ELEMENTOS NECESSÁRIOS À RNA, E SEU TAMANHO EM BITS .................................................... 196 
TABELA 21 - RESULTADOS DOS EXPERIMENTOS DE IMPLEMENTAÇÃO DE RNA MLP POR MEIO DO NEUROPON .......................... 200 
TABELA 22 - MODELO COMPUTACIONAL NEUROPON: CARACTERÍSTICAS DE IMPLEMENTAÇÃO DE RNA ................................... 207 
 
 


 
 
LISTA DE CÓDIGOS 
CÓDIGO 1 - PREDICADO UTILIZADO EM MECANISMOS DE BUSCA (EXEMPLO DO IEEE XPLORE) ................................................... 40 
CÓDIGO 2 - EXEMPLO DE REDUNDÂNCIA NO PI ................................................................................................................ 44 
CÓDIGO 3 - ARQUIVO XML CONTENDO O ESQUEMA DE DEFINIÇÃO (DEFINITION SCHEMA) PARA UMA RNA A SER TREINADA COM O 
ALGORITMO DE TREINAMENTO POR BP, COM O EXEMPLO DO XOR (ADAPTADO DE BERAN ET AL., 2008) .......................... 75 
CÓDIGO 4 - CLASSE NETWORKSYSTEM QUE ESTENDE NOPAPPLICATION, CUJA INSTÂNCIA COORDENA TODO O SISTEMA ............... 100 
CÓDIGO 5 - CÓDIGO: ESTRUTURA DE UMA FBE NO FRAMEWORK PON C++ 2.0 .................................................................. 100 
CÓDIGO 6 - CÓDIGO: ESTRUTURA DAS PREMISES PARA O FRAMEWORK PON C++ ................................................................ 101 
CÓDIGO 7 - CONTROLE DE PORTÃO ELETRÔNICO IMPLEMENTADO COM LINGPON 1.0 .......................................................... 103 
CÓDIGO 8 - CÓDIGO DA IMPLEMENTAÇÃO DE UM NEURÔNIO EM NEUROPON: (A) REPRESENTAÇÃO UTILIZANDO LINGPON EM 
SOFTWARE; (B) REPRESENTAÇÃO UTILIZANDO LINGPON-HD EM HARDWARE ............................................................. 130 
CÓDIGO 9 - FBE NEURON EM CÓDIGO FRAMEWORK PON C++ 2.0 .................................................................................. 149 
CÓDIGO 10 - DEFINIÇÃO DA RULE RLESTART EM LINGPON .............................................................................................. 150 
CÓDIGO 11 - CONFIGURAÇÃO DE PREMISES E RULES RELACIONADAS À FBE NETWORK -  FRAMEWORK PON C++ 2.0 - EXEMPLO XOR
 ................................................................................................................................................................... 150 
CÓDIGO 12 - IMPLEMENTAÇÃO DA RULE RLECALCNET, UTILIZANDO LINGPON .................................................................... 151 
CÓDIGO 13 - IMPLEMENTAÇÃO, UTILIZANDO FRAMEWORK PON C++ 2.0, DO METHOD MTHCALCNET() ................................. 151 
CÓDIGO 14 - AJUSTE DO ATTRIBUTE ATTNUMEPOCHS – DISPARA O INÍCIO DA CADEIA DE  NOTIFICAÇÕES – FRAMEWORK PON C++ 
2.0 – EXEMPLO DO XOR .................................................................................................................................. 152 
CÓDIGO 15 - FBE NEURONHIDDEN EM CÓDIGO FRAMEWORK PON C++ 2.0 ..................................................................... 155 
CÓDIGO 16 - IMPLEMENTAÇÃO DA RULE RLECALCHIDDEN, UTILIZANDO FRAMEWORK PON C++ 3.0....................................... 158 
CÓDIGO 17 - DECLARAÇÃO DAS INSTANCIAS DE FBE EM LINGPON, DA RNA MLP, PA RA O IRIS DATASET ................................ 168 
CÓDIGO 18 - REGRA DE FORMAÇÃO NA CONCEPÇÃO DA RULE RLENOCALCOUTPUT ............................................................. 170 
CÓDIGO 19 - RESULTADO DA PRÉ-COMPILAÇÃO - UMA FBE E UMA RULE PARA CADA INSTÂNCIA ............................................. 170 
CÓDIGO 20 - IMPLEMENTAÇÃO DO ATTRIBUTE ATTNUMEPOCHS, FBE NETWORK ................................................................ 171 
CÓDIGO 21 - ARQUIVOS NET_MTHNETSTART.H E NET_MTHNETSTART.CPP IMPLEMENTADOS EM STATICCPP ........................... 172 
CÓDIGO 22 - CÓDIGO EM LINGPON-HD APRESENTANDO O TOKEN PARA A FUNÇÃO DE QUANTIZAÇÃO ..................................... 182 
CÓDIGO 23 - TRECHO DE CÓDIGO VHDL QUE IMPLEMENTA A LUT DA FUNÇÃO DE TRANSFERÊNCIA  TANGENTE HIPERBÓLICA EM 
NEUROPON-HD ............................................................................................................................................ 183 
CÓDIGO 24 - UTILIZAÇÃO DA FUNÇÃO DE TANGENTE HIPERBÓLICA EM LINGPON-HD .......................................................... 184 
CÓDIGO 25 - LINGPON-HD: IMPLEMENTAÇÃO DA FBE NETWORK EM NEUROPON-HD ...................................................... 184 
CÓDIGO 26 - FBE FHIDDENNEURONA, QUE REPRESENTA UM NEURÔNIO DA CAMADA ........................................................... 185 
CÓDIGO 27 – NEURORULE EM LINGPON-HD, PARA O CONTROLE DO  INÍCIO DOS CÁLCULOS DOS NEURÔNIOS ........................... 187 
CÓDIGO 28 - VHDL NEUROPON-HD: IMPLEMENTAÇÃO DOS SINAIS ................................................................................. 188 
CÓDIGO 29 - TRECHO DE CÓDIGO DO ARQUIVO DE DESCRIÇÃO (DESCRIPTION.XML) DE RNA EM NEUROPON ............................ 189 
CÓDIGO 30 - DEFINIÇÃO DOS SINAIS DE ENTRADA E SAÍDA (INTERFACE) DA ENTIDADE NEUROPON, EM VHDL ............................. 196 
CÓDIGO 31 – AJUSTE DAS CONFIGURAÇÕES E DO INÍCIO DA CADEIA DE NOTIFICAÇÕES VIA ARQUIVO DE TESTBENCH EM VHDL ....... 198 


 
 
 LISTA DE ABREVIATURAS 
Abreviaturas 
Latim 
Tradução/Significado 
cf. 
confer 
conforme 
i.e. 
id est 
isto é 
e.g. 
exempli gratia 
por exemplo 
et al. 
et alii ou et aliae 
e outros ou e outras 
 
LISTA DE SIGLAS E ACRÔNIMOS 
SIGLA 
Original 
Tradução 
ALU 
Arithmetic Logical Unit 
Unidade Lógica Aritmética 
ANGE 
Automatic General-purpose Neural 
Hardware Generator 
Gerador Automático de Hardware Neural 
de Propósito Geral 
ARQPON 
Arquitetura de Processador para o 
Paradigma Orientado a Notificações 
Notification-Oriented Computer 
Architecture 
API 
Application Programming Interface 
Interface de Programação de Aplicativos 
BNF 
Backus-Naur Form 
Forma de Backus-Naur 
BP 
Backpropagation 
Retropropagação 
CAD 
Computer-Aided Design 
Projeto Auxiliado por Computador 
CMOS 
Complementary Metal-Oxide 
Semiconductor 
Semicondutor complementar de Metal-
Óxido 
CON 
Controle Orientado a Notificações 
Notification Oriented Control 
COPON 
Coprocessador PON 
NOP Coprocessor 
CPLD 
Complex Programmable Logic Devices 
Dispositivos Complexos de Lógica 
Programável 
CPU 
Central Processing Unit 
Unidade Central de Processamento 
DSE 
Dynamic Service Evolution 
Evolução Dinamica de Serviço 
EDA 
Electronic Design Automation 
Automação de Desenho Eletrônico 
EEPROM 
Electrically-Erasable Programmable 
Read-Only Memory 
Memoria “Somente-Leitura” Programável 
Eletricamente Apagável 


 
 
FBE 
Fact Base Element 
Elemento da Base de Fatos 
FIFO 
First In, First Out 
Primeiro a Entrar, Primeiro a Sair 
FSM 
Finite State Machine 
Máquina de Estados Finita 
FPGA 
Field Programmable Gate Array 
Arranjo de Portas Programável em 
Campo 
FPU 
Floating Point Unit 
Unidade de Ponto Flutuante 
GAL 
Generic Array Logic 
Matriz Lógica Genérica 
GPU 
Graphics Processing Unit 
Unidade de Processamento Gráfico 
GUI 
Graphical User Interfaces 
Interfaces Gráficas de Usuário 
HDL 
Hardware Description Language 
Linguagem de Descrição de Hardware 
IEEE 
Institute of Electrical and Electronics 
Engineers 
Instituto de Engenheiros Eletricistas e 
Eletrônicos 
IP 
Internet Protocol 
Protocolo de Internet 
ISA 
Instruction Set Architecture 
Arquitetura do Conjunto de Instruções 
IDE 
Integrated Development Environment 
Ambiente de Desenvolvimento Integrado 
IA 
Inteligência Artificial 
Artificial Intelligence 
IC 
Inteligência Computacional 
Computational Intelligence 
ION 
Inferência Orientada a Notificações 
Notification Oriented Inference 
iXCSL 
eXtensible Soft Computing Language 
Linguagem Extensível para Soft 
Computing 
LIFO 
Last In, First Out 
Último a Entrar, Primeiro a Sair 
LingPON 
Linguagem PON 
NOP Language 
LUT 
Lookup Tables 
Tabela de Consulta 
MLP 
Multi-Layer Perceptron 
Perceptron de Múltiplas Camadas 
MCPON 
Modelo para Compilação PON 
Compilation Model for NOP 
MOSFET 
Metal Oxide Semiconductor Field Effect 
Transistor 
Transistor de Efeito de Campo Metal-
Óxido-Semicondutor 
MPGA 
Mask Programmed Gate Array 
Arranjo de Portas por Máscara 
Programável 
NOCA 
Notification-Oriented Computer 
Architecture 
Arquitetura de Processador para o 
Paradigma Orientado a Notificações 


 
 
NNDef 
Neural Network Definition Toolkit 
Conjunto de Ferramentas para Definição 
de Rede Neural 
NXML 
Neural XML 
XML Neural 
PC 
Personal Computer 
Computador Pessoal 
PD 
Paradigma Declarativo 
Declarative Paradigm 
PF 
Paradigma Funcional 
Functional Paradigm 
PI 
Paradigma Imperativo 
Imperative Paradigm 
PL 
Paradigma Lógico 
Logical Paradigm 
PLD 
Programmable Logic Device 
Dispositivo Lógico Programável 
PMC 
Perceptron de Múltiplas Camadas 
Multi-Layer Perceptron 
POD 
Paradigma Orientado a Dados 
Data Oriented Paradigm 
POE 
Paradigma Orientado a Eventos 
Event-Driven Paradigm 
PON 
Paradigma Orientado a Notificações 
Notification Oriented Paradigm 
PON-HD 
PON em Hardware Digital 
NOP Digital Hardware 
POO 
Programação Orientada a Objetos 
Object Oriented Programming 
POR 
Paradigma Orientado a Regras 
Rule Oriented Paradigm 
PP 
Paradigma Procedimental 
Procedural Paradigm 
RNA 
Redes Neurais Artificiais 
Artificial Neural Networks 
RNH 
Redes Neurais em Hardware 
Hardware Neural Networks 
SBR 
Sistema Baseado em Regras 
Rule Based Systems 
SoC 
System-on-a-chip 
Sistema em um Chip 
SOM 
Self Organizing Maps 
Mapas Auto-Organizáveis 
SPLD 
Simple Programmable Logic Devices 
Dispositivos Simples de Lógica 
Programável 
SSI 
Small-Scale Integrated 
Integração em Baixa Escala 
STL 
Standard Template Library 
Biblioteca Padrão de Gabaritos 
TCP 
Transmission Control Protocol 
Protocolo de Controle de Transmissão 
UDP 
User Datagram Protocol 
Protocolo de Datagramas de Usuário 
UML 
Unified Modeling Language 
Linguagem de Modelagem Unificada 


 
 
VHDL 
VHSIC Hardware Description Language 
Linguagem de Descrição de Hardware 
VHSIC 
VHSIC 
Very-High-Speed Integrated Circuit 
Circuito Integrado de Velocidade Muito 
Alta 
ViNNSL 
Vienna Neural Network Speciﬁcation 
Language 
Linguagem de Especificação de Rede 
Neural Vienna 
XML 
eXtensible Markup Language 
Linguagem de Marcação Extensível 
XOR 
eXclusive OR 
OU Exclusivo 
YAML 
YAML Ain't Markup Language 
YAML Não é Linguagem de Marcação 
 
 
 


 
 
SUMÁRIO 
1 INTRODUÇÃO ....................................................................................................................... 21 
1.1 FORMULAÇÃO DO PROBLEMA ................................................................................................... 22 
1.2 CONTEXTUALIZAÇÃO ............................................................................................................... 27 
1.3 HIPÓTESE ............................................................................................................................. 29 
1.4 OBJETIVOS ............................................................................................................................ 32 
1.5 JUSTIFICATIVAS ...................................................................................................................... 32 
1.6 MOTIVAÇÕES ........................................................................................................................ 38 
1.7 ORGANIZAÇÃO DO DOCUMENTO ................................................................................................ 39 
2 FUNDAMENTAÇÃO TEÓRICA ................................................................................................. 40 
2.1 PARADIGMAS DE PROGRAMAÇÃO .............................................................................................. 41 
2.1.1 PARADIGMA IMPERATIVO – PI ......................................................................................................... 42 
2.1.2 PARADIGMA DECLARATIVO – PD ...................................................................................................... 45 
2.1.3 PARADIGMA ORIENTADO A DADOS – POD OU DATAFLOW ................................................................... 47 
2.1.4 CONSIDERAÇÕES SOBRE PARADIGMAS DE PROGRAMAÇÃO ................................................................... 49 
2.2 LINGUAGENS E COMPILADORES .................................................................................................. 50 
2.3 HARDWARE E LÓGICA RECONFIGURÁVEL ...................................................................................... 53 
2.3.1 HARDWARE RECONFIGURÁVEL: DISPOSITIVOS FPGA ............................................................................ 54 
2.3.2 PROGRAMAÇÃO DE FPGA ............................................................................................................... 57 
2.3.3 SÍNTESE EM ALTO NÍVEL .................................................................................................................. 58 
2.3.4 CONSIDERAÇÕES SOBRE DISPOSITIVOS FPGA ...................................................................................... 60 
2.4 REDES NEURAIS ARTIFICIAIS ...................................................................................................... 62 
2.4.1 CONCEITOS DE RNA ....................................................................................................................... 62 
2.4.2 NEURÔNIO ARTIFICIAL .................................................................................................................... 64 
2.4.3 ARQUITETURAS DE RNA ................................................................................................................. 66 
2.4.4 PROCESSO DE APRENDIZADO E TREINAMENTO ..................................................................................... 68 
2.4.5 IMPLEMENTAÇÃO DE RNA EM SOFTWARE ......................................................................................... 74 
2.4.6 CONSIDERAÇÕES SOBRE IMPLEMENTAÇÃO DE RNA EM SOFTWARE ........................................................ 76 
2.4.7 IMPLEMENTAÇÃO DE RNA EM HARDWARE (RNH) .............................................................................. 78 
2.4.7.1 Tecnologias para Implementação de RNH ............................................................................. 80 
2.4.7.2 RNH em Hardware Reconfigurável ........................................................................................ 81 


 
 
2.4.7.3 Trabalhos correlatos .............................................................................................................. 83 
2.4.8 CONSIDERAÇÕES FINAIS SOBRE IMPLEMENTAÇÃO DE RNA .................................................................... 87 
2.5 CONSIDERAÇÕES SOBRE A REVISÃO DE LITERATURA ........................................................................ 90 
3 PARADIGMA ORIENTADO A NOTIFICAÇÕES ........................................................................... 91 
3.1 ORIGENS DO PON .................................................................................................................. 91 
3.2 ENTIDADES DO PON ............................................................................................................... 92 
3.3 MATERIALIZAÇÕES DO PON ...................................................................................................... 96 
3.3.1 ARQUÉTIPO OU FRAMEWORK .......................................................................................................... 96 
3.3.2 LINGUAGEM E COMPILADOR PARA O PON ....................................................................................... 102 
3.3.2.1 Linguagem do LingPON 1.0 .................................................................................................. 102 
3.3.2.2 Compilador do LingPON 1.0 ................................................................................................. 105 
3.3.3 PARALELIZAÇÃO E DISTRIBUIÇÃO VIA PON EM SOFTWARE .................................................................. 108 
3.3.4 FRAMEWORK PON ELIXIR/ERLANG ................................................................................................ 113 
3.3.5 PON EM HARDWARE ................................................................................................................... 114 
3.3.6 TECNOLOGIA LINGPON-HD .......................................................................................................... 116 
3.3.7 DESENVOLVIMENTO ORIENTADO A NOTIFICAÇÕES (DON) ................................................................. 119 
3.4 CONSIDERAÇÕES SOBRE O PON ............................................................................................... 122 
4 MODELO COMPUTACIONAL NEUROPON.............................................................................. 124 
4.1 MODELO COMPUTACIONAL NEUROPON: REQUISITOS ................................................................... 124 
4.2 MODELO COMPUTACIONAL NEUROPON: ETAPAS PARA GERAÇÃO DE CÓDIGO ..................................... 125 
4.3 MODELO COMPUTACIONAL NEUROPON: FUNCIONAMENTO ........................................................... 127 
4.3.1 NEURÔNIO EM NEUROPON .......................................................................................................... 127 
4.3.2 RNA EM NEUROPON .................................................................................................................. 132 
4.4 CONSIDERAÇÕES SOBRE O MODELO COMPUTACIONAL NEUROPON ................................................. 141 
5 IMPLEMENTAÇÕES E EXPERIMENTOS DO MODELO COMPUTACIONAL NEUROPON ............... 144 
5.1 RNA MLP COM LINGUAGEM C PROCEDIMENTAL ......................................................................... 145 
5.2 RNA MLP COM FRAMEWORK PON C++ 2.0: TREINAMENTO BP PARA A FUNÇÃO XOR ........................ 146 
5.2.1 DESENVOLVIMENTO DA RNA ......................................................................................................... 147 
5.2.2 CODIFICAÇÃO DA RNA VIA FRAMEWORK PON C++ 2.0 .................................................................... 148 


 
 
5.2.3 RESULTADOS DO EXPERIMENTO ..................................................................................................... 152 
5.2.4 CONSIDERAÇÕES SOBRE O EXPERIMENTO ......................................................................................... 152 
5.3 RNA MLP COM FRAMEWORK PON C++ 2.0: TREINAMENTO BP PARA IRIS DATASET .......................... 154 
5.3.1 DESENVOLVIMENTO DO EXPERIMENTO ............................................................................................ 154 
5.3.2 CODIFICAÇÃO .............................................................................................................................. 154 
5.3.3 RESULTADOS DO EXPERIMENTO ..................................................................................................... 155 
5.3.4 CONSIDERAÇÕES SOBRE O EXPERIMENTO ......................................................................................... 156 
5.4 RNA MLP COM FRAMEWORK PON C++ 3.0: TREINAMENTO BP PARA IRIS DATASET .......................... 157 
5.4.1 DESENVOLVIMENTO E CODIFICAÇÃO ................................................................................................ 157 
5.4.2 RESULTADOS DO EXPERIMENTO ..................................................................................................... 159 
5.4.3 CONSIDERAÇÕES SOBRE O EXPERIMENTO ......................................................................................... 163 
5.5 RNA MLP PARA XOR COM FRAMEWORK ELIXIR/ERLANG ............................................................. 165 
5.6 RNA MLP PARA IRIS DATASET COM LINGPON 1.2 STATICCPP ...................................................... 167 
5.6.1 DESENVOLVIMENTO ..................................................................................................................... 168 
5.6.2 CODIFICAÇÃO .............................................................................................................................. 168 
5.6.3 RESULTADOS DO EXPERIMENTO ..................................................................................................... 172 
5.6.4 CONSIDERAÇÕES .......................................................................................................................... 173 
5.7 RNA MLP PARA XOR COM LINGPON-HD ................................................................................ 174 
5.7.1 DESENVOLVIMENTO ..................................................................................................................... 175 
5.7.2 CODIFICAÇÃO .............................................................................................................................. 181 
5.7.3 RESULTADOS DO EXPERIMENTO ..................................................................................................... 190 
5.7.4 CONSIDERAÇÕES .......................................................................................................................... 193 
5.8 RNA MLP PARA IRIS COM LINGPON-HD ................................................................................. 195 
5.8.1 DESENVOLVIMENTO ..................................................................................................................... 195 
5.8.2 EXECUÇÃO E RESULTADOS DO EXPERIMENTO ................................................................................... 198 
5.8.3 CONSIDERAÇÕES .......................................................................................................................... 201 
5.9 REFLEXÕES SOBRE OS EXPERIMENTOS ........................................................................................ 202 
6 CONCLUSÕES E TRABALHOS FUTUROS ................................................................................. 205 
6.1 CONCLUSÕES ....................................................................................................................... 205 
6.1.1 CONTRIBUIÇÕES .......................................................................................................................... 208 
6.1.2 DISCUSSÃO SOBRE AS CONTRIBUIÇÕES ............................................................................................. 211 
6.1.3 REFLEXÕES FINAIS DA TESE ............................................................................................................ 215 
6.2 TRABALHOS FUTUROS ............................................................................................................ 216 


 
 
REFERÊNCIAS ............................................................................................................................ 217 
APÊNDICE A – IMPLEMENTAÇÃO RNA EM LINGUAGEM C PROCEDIMENTAL ............................... 231 
APÊNDICE B – CÓDIGOS DE EXPERIMENTOS .............................................................................. 236 
APÊNDICE C – CÓDIGO XML – ARQUIVO DESCRIPTION.XML ....................................................... 245 
APÊNDICE D – LINGUAGENS DE DESCRIÇÃO DE RNA .................................................................. 247 
ANEXO A - MANUAL DA LINGUAGEM PON - LINGPON ............................................................... 255 
ANEXO B – RELATÓRIO DE DISCIPLINA SOBRE STATICCPP .......................................................... 269 
 
 


21 
 
 
1 Introdução 
Uma Rede Neural Artificial (RNA) é um modelo computacional simplificado, baseado 
nos conhecimentos atuais a respeito do funcionamento dos neurônios nos sistemas 
nervosos de animais superiores (HAYKIN, 2008). Tais modelos, supostamente 
inerentemente paralelos, são capazes de auto ajustar seus parâmetros, ou pesos, a 
partir de exemplos, tornando-se assim capazes de aprender, a fim de reconhecer 
padrões (HEATON, 2015).  
Muito embora supostamente paralelas em termos de modelo, Krose; Smagt 
(1996) apontam que quando implementações de RNA são executadas em 
computadores convencionais sequenciais, baseados na arquitetura de von Neumann 
ou similares, tais sistemas não atingem todo seu potencial de execução paralela. Neste 
âmbito, Omondi et al. (2006) apontam que a tecnologia de dispositivos do tipo Field 
Programmable Gate Arrays (FPGA) é uma alternativa para o desenvolvimento de RNA 
no tocante a paralelismo. 
Dispositivos 
FPGA 
são 
compostos 
por 
unidades 
programáveis 
e 
reconfiguráveis. Isto dito, com a utilização de tais dispositivos, pode-se elaborar 
circuitos paralelos devido a certo desacoplamento das unidades, e ainda com baixo 
custo de prototipação devido à reconfigurabilidade implícita (COSTA, 2014). Contudo, 
a programação em FPGA, particularmente explorando paralelismo, demanda 
considerável conhecimento técnico de desenvolvimento em baixo nível (TISAN; CHIN, 
2015; WINDH et al., 2015).  
Uma alternativa para o melhor desenvolvimento com FPGA são as linguagens 
de especificação de hardware (tais como VHDL ou Verilog) utilizadas para programação 
e subsequente (re)configuração de tais dispositivos (BAPTISTA; MORGADO-DIAS, 
2017; TISAN; CHIN, 2015). Entretanto, tais linguagens demandam acentuado 
conhecimento e expertise técnicos (KERSCHBAUMER, 2018; LAKSHMI; SUBADRA, 
2013). Neste contexto, outra alternativa são as linguagens utilizadas para Síntese de 
Alto Nível (High-Level Synthesis - HLS). As técnicas e ferramentas de HLS apresentam 
a vantagem de permitir desenvolvimento em mais alto-nível, com menos necessidade 
de conhecimento técnico. Por outro lado, elas tendem a explorar mais pobremente o 
paralelismo permitido por dispositivos FPGA (COUSSY et al., 2009; KERSCHBAUMER, 
2018; MEEUS et al., 2012).  
Efetivamente, linguagens utilizadas em HLS como, por exemplo, Handel-C, 
Hyden-C e SystemC, baseadas nas linguagens C/C++, seguem a lógica baseada em 


22 
 
 
paradigmas de programação tradicionais, principalmente o Paradigma Imperativo (PI), 
o que resulta em aplicações geralmente acopladas e redundantes (DAOUD et al., 2014; 
KERSCHBAUMER, 2018; LAKSHMI; SUBADRA, 2013; PETHICK et al., 2003). O 
exemplo mais veemente de paradigma tradicional é de fato o imperativo que comporta 
linguagens como C e C++, as quais tem sido derivadas para uso em FPGA e que 
apresentam justamente os problemas salientados (BAPTISTA; MORGADO-DIAS, 
2017; KERSCHBAUMER, 2018; TISAN; CHIN, 2015; WINDH et al., 2015). 
Uma exceção parcial a esta problemática posta seria a Programação orientada 
a Fluxo de Dados (dataflow) que lida consideravelmente bem com a distribuição de 
processamento aritmético. Entretanto, ela não lida necessariamente bem com a 
distribuição de processamento lógico causal (JOHNSTON et al., 2004; KAISLER, 
2005). Outra exceção mais efetiva é um paradigma emergente chamado de Paradigma 
Orientado a Notificações (PON) que possui características de tratar desacopladamente 
cada 
entidade 
de 
processamento 
lógico-causal 
e 
facto-execucional 
(KERSCHBAUMER, 2018; SIMÃO, 2005; SIMÃO; STADZISZ, 2008). 
Neste âmbito, o presente trabalho propõe um novo método para a criação de 
RNA utilizando o PON, visando uma nova maneira de compor RNA com paralelismos 
implícitos, sendo apresentadas demonstrações de conceito em software e, 
notadamente, em hardware reconfigurável (nomeadamente em dispositivos FPGA). No 
tocante a esta proposta, o presente capítulo aborda a formulação e a contextualização 
do problema, os objetivos do trabalho e o método utilizado nele. Nos capítulos 
subsequentes, uma revisão dos temas integrantes da pesquisa é apresentada, bem 
como os trabalhos realizados durante o processo de doutoramento. Por fim, são 
apresentadas as conclusões e as propostas de trabalhos futuros. 
1.1 Formulação do Problema 
Pesquisas recentes em Inteligência Artificial (IA) e afins têm apresentado 
soluções mais efetivas em diversas áreas do conhecimento, desde ‘visão 
computacional’ aplicada em segurança de aeroportos até ‘navegação inteligente’ 
aplicada a carros autônomos (BOYD, 2017;GUIZZO, 2011; HIGH, 2012;LEO et al. 
2017). Os avanços tecnológicos dos equipamentos computacionais digitais e mesmo 
alguns aperfeiçoamentos das técnicas de programação têm colaborado para com a 
transição, de fato, da IA da academia para a indústria (FREUND et al., 2017; KRÖSE; 
SMAGT, 2006). 


23 
 
 
Neste contexto, uma técnica de IA que vem se destacando são as RNA, as 
quais são aplicadas em domínios como aproximação de funções, previsão de séries 
temporais, classificações e reconhecimento de padrões (RUSSEL; NORVIG, 2009; 
SILVA et al., 2010a). 
RNA são inspiradas no funcionamento dos sistemas nervosos biológicos ou 
Redes Neurais Naturais (RNN), os quais são formados por um conjunto complexo de 
células interligadas chamadas de neurônios. Segundo Haykin (2008), o neurônio é a 
unidade básica da estrutura do cérebro, sendo responsável pela condução dos 
impulsos nervosos. Tais impulsos são recebidos e transmitidos a outros neurônios, 
formando assim uma rede de transmissão de informações na forma de sinapses. Isto 
dito, as RNN servem de inspiração, até certo ponto, para a composição das RNA. A 
Figura 1 apresenta um exemplo esquemático de uma RNA e suas interconexões. 
Figura 1 – Representação da estrutura de uma RNA: neurônios e conexões sinápticas. Os neurônios 
podem realizar seu processamento de forma completamente paralela 
 
Fonte: Autoria Própria 
Assim como no sistema nervoso biológico, a estrutura de uma RNA é composta 
por múltiplas unidades de processamento supostamente paralelas, chamadas de 
neurônios artificiais. Tais neurônios são interligados entre si por sinapses artificiais, as 
quais são representadas por pesos sinápticos, na forma de valores numéricos, tanto 
reais quanto inteiros. A partir da aplicação de equações matemáticas em seus valores 
de entrada, os neurônios produzem estados de ativação. Tais estados de ativação 
auxiliam na modificação dos pesos sinápticos e diferenciam cada uma das sinapses 


24 
 
 
(HAYKIN, 2008; SILVA, et al., 2010a). A Figura 2 apresenta um esquema de 
representação um neurônio. 
Figura 2 - Esquema representativo de um neurônio 
 
Fonte: Autoria Própria 
Para que o processamento em RNA fosse mais fidedigno ao de um cérebro 
biológico, este deveria ser efetivamente executado de forma paralela. Tal assertiva é 
corroborada pelo trabalho de Volokitin (2014), cujo desenvolvimento de um treinamento 
de RNA com paralelismos, executando em dois núcleos de processamento (cores), 
apontou um ganho de 25% em termos de desempenho relativo ao tempo de 
processamento quando comparado a um treinamento equivalente, porém realizado de 
forma sequencial, em apenas um core (VOLOKITIN, 2014). Porém, o mesmo estudo 
aponta que o aumento de núcleos de processamento (utilizando, e.g. mais de dois 
cores) tornaria o processo mais lento, devido ao gasto com overheads no sistema. Tais 
overheads são causados pelo fato de o algoritmo de treinamento utilizado não ser 
paralelo, exigindo sincronizações após o treinamento de cada camada (VOLOKITIN, 
2014). 
Neste sentido, segundo Souza e Torres (2011), com a tecnologia de hardware 
reconfigurável, principalmente por meio de dispositivos FPGA, pode-se elaborar 
circuitos paralelos, ou seja, circuitos onde uma parte de sua estrutura interna possa 
executar um trabalho de forma independente e paralela de outra parte da mesma 
estrutura. Tal característica é particularmente útil para elaborar RNA. Ainda, Asanovic 
et al. (2006) apontam que os dispositivos FPGA têm avançado constantemente, 
tornando-se importantes ferramentas de prototipação e implementação de mecanismos 
paralelos. Isto ocorre em função do contínuo aumento da capacidade de tais 
dispositivos, a qual já chega a milhões de portas e bits de memória, bem como à 
flexibilidade de reconfiguração, a qual permite inclusive que soluções refinadas e novos 


25 
 
 
testes sejam reformulados após avaliações de testes anteriores (ASANOVIC et al., 
2006; SOUZA; TORRES, 2011). 
Neste contexto, mesmo que o desenvolvimento de sistemas computacionais 
para dispositivos FPGA não seja (ainda) tão usual quanto para dispositivos de 
processamento sequencial baseados em máquinas von Neumann, alguns trabalhos 
têm utilizado tal tecnologia para desenvolver sistemas de diversos tipos (e.g. sistemas 
com cálculos matemáticos paralelizados e soluções de controle contínuo e discreto) 
(CHEN et al., 2006; GOKHALE; GRAHAM, 2005; GREEN, 2009; KILTS, 2007; MA et 
al.,2011), sendo utilizada inclusive no tocante à RNA. Como exemplos, Ali e 
Mohammed (2010), Deotale e Dole (2014), Moukhlis et al. (2014) e Rezvani et al. (2012) 
demonstram a implementação e aplicação paralela de RNA utilizando dispositivos 
FPGA e concluem que tais implementações são, de fato, mais velozes do que quando 
feitas de maneira monoprocessada e sequencial.  
Não obstante, neste âmbito de dispositivos FPGA, os usuários devem conhecer 
técnicas de programação de baixo nível, ou mesmo utilizar linguagens de descrição de 
hardware para alcançar paralelismo, o que exige considerável arcabouço de 
conhecimento técnico (BAPTISTA; MORGADO-DIAS, 2017; TISAN; CHIN, 2015).  
Uma alternativa, neste contexto, são as ferramentas de síntese de alto nível 
(MEEUS et al., 2012). Porém, em tais ferramentas, são utilizadas linguagens 
imperativo-sequenciais derivadas de C/C++ como Impulse-C (utilizada na ferramenta 
CoDeveloper) e Handel-C (utilizada na ferramenta DK Design Suite), ou derivadas de 
linguagens de descrição de hardware como Bluespec System Verilog (utilizada na 
ferramenta Bluespec), as quais, ainda assim, exigem considerável conhecimento 
técnico (KERSCHBAUMER, 2018). 
Na verdade, a problemática de programação paralela vai além do escopo de 
FPGA e afins. Neste sentido, quanto ao desenvolvimento de sistemas paralelos em 
geral via paradigmas vigentes de programação, programadores têm dificuldade de 
abstração na elaboração de software paralelo. Isto se dá pois a distribuição lógica das 
instruções passa a ser não somente temporal (i.e., execução de instruções distribuída 
sequencialmente ao longo do tempo), mas também espacial (i.e., execução de 
instruções distribuída em vários locais ao mesmo tempo) (ASANOVIC et al., 2006; 
BORKAR; CHIEN, 2011; KAISLER, 2005; LINHARES, 2015).  
Neste contexto, Banaszewski et al. (2007) indica que parte da dificuldade de 
paralelismo e distribuição de software em geral, encontra-se nos paradigmas de 
programação vigentes. Dentre eles, pode-se salientar o PI, de maior impacto industrial, 


26 
 
 
que comporta as linguagens mais usuais de programação, como C/C++, Python, C#, 
Java e afins (BANASZEWSKI et al., 2007; BANASZEWSKI, 2009; CASS, 2018; 
RONSZCKA, 2019).  
O PI é baseado em uma organização sequencial de comandos, que quando 
executados, realizam manipulação de dados a partir de variáveis para obter o resultado 
desejado (BROOKSHEAR; BRYLOW, 2014). Na verdade, é natural que PI seja assim 
dado que tal paradigma surgiu com processamento sequencial para as arquiteturas 
computacionais até hoje vigentes, e dado que as linguagens que seguem tal paradigma 
sejam um facilitador na programação de software para tais arquiteturas 
(BROOKSHEAR; BRYLOW, 2014; RONSZCKA, 2018; VAN ROY; HARIDI, 2004). 
Além disso, a tendência ao acoplamento entre partes do software, que seguem 
os preceitos do PI, leva à geração de programas que não aproveitam todo o potencial 
paralelo de um sistema computacional, quando tal potencial está presente na aplicação 
a ser implementada (BELMONTE et al., 2016; RONSZCKA, 2019). 
Gabbrielli e Martini (2010), Kaisler (2005) e Simão e Stadzisz (2009a) destacam 
ainda que o PI, cujas expressões causais e dados são tratados como entidades 
passivas, causa considerável desperdício de processamento. Na verdade, a repetição 
de expressões lógicas e suas reavaliações desnecessárias, bem como o forte 
acoplamento de entidades quanto ao cálculo lógico-causal, são situações causadas 
pela orientação a estruturas de repetição ou busca. Em todo caso, ambas são 
efetivamente apontadas como deficiências no PI (GABBRIELLI; MARTINI, 2010; 
KAISLER, 2005; SIMÃO; STADZISZ, 2009a).  
Neste contexto, uma alternativa ao PI é o Paradigma Declarativo (PD). O PD é 
uma abordagem focada em descrever, em linguagem de alto nível, o que o programa 
deve fazer e não como seus procedimentos devem funcionar (MANZANO, 2013). 
Entretanto, o PD pode ser entendido como uma camada sobre o PI, automatizando e 
generalizando atividades de processamento lógico-causal por meio das chamadas 
máquinas de inferência com o custo de elevação de tempos de processamento 
(RONSZCKA, 2019).  
Em todo caso, o PD não resolve a questão de distribuição. De fato, tanto PI 
quanto PD, foram concebidos para fins de computação monoprocessada sequencial. 
De acordo com Simão e Stadzisz (2009), o problema de acoplamento é agravado pela 
característica de que ambos são orientados a pesquisa em dados, seja por meio de 
laços explícitos (no caso do PI), seja por meio de laços implícitos (no caso de máquinas 
de inferência do PD) (GABBRIELLI E MARTINI, 2010; SIMÃO; STADZISZ, 2009a).  


27 
 
 
Em suma, como apontado por Simão e Stadzisz (2009a), paradigmas de 
programação atuais, nomeadamente PD e PI, não auxiliam efetivamente na exploração 
da capacidade total dos processadores sequenciais e tampouco na execução paralela 
e/ou distribuídas em grupos de processadores sequenciais (BELMONTE et. al., 2016; 
GABBRIELLI E MARTINI, 2010; KAISLER, 2005; LINHARES et al., 2015; SIMÃO E 
STADZISZ, 2009a).  
Partindo deste pressuposto, foi criado o Paradigma Orientado a Notificações 
(PON) (SIMÃO, 2005; SIMÃO; STADZISZ, 2008). Em suma, o PON visa melhorar o 
processo de criação de código coeso e desacoplado, o que resolveria ou, pelo menos, 
atenuaria os problemas de PI e PD conforme considerado na Seção 1.2. 
Por fim, postula-se, portanto, que o problema a ser resolvido pela presente tese 
de doutoramento seja possibilitar o desenvolvimento de RNA paralelizáveis, por meio 
de uma nova proposta de abordagem de RNA baseada em PON, particularmente com 
execução em dispositivos FPGA. Assim, o código de execução dessa nova forma de 
compor e executar RNA deve ser baseado neste novo paradigma, de forma tal que se 
aproveite o potencial de execução paralela destes dispositivos de forma transparente 
ao usuário que compõe ou usa RNA 
1.2 Contextualização 
O Paradigma Orientado a Notificações (PON) foi desenvolvido com base em 
uma solução genérica para controle discreto que habilita, de forma eficiente e intuitiva, 
a organização da colaboração entre entidades controladas (e.g. entidade de 
manufatura). Esta teoria embrionária do PON é atualmente chamada de Controle 
Orientado a Notificações (CON), a qual foi utilizada inicialmente visando agilizar 
sistemas de produção, chamados de Sistemas Inteligentes de Produção (SIMÃO, 2005; 
SIMÃO; STADZISZ, 2008; SIMÃO; STADZISZ, 2009a).  
Atualmente, o PON é tido como uma abordagem para desenvolvimento de 
aplicações (tanto em software quanto em hardware), propondo soluções para reduzir 
os problemas dos atuais paradigmas de programação, de forma que haja um aumento 
no desempenho de execução por meio da diminuição de redundâncias, bem como a 
simplificação de paralelismo e distribuição pela garantia implícita de coesão e 
desacoplamento em entidades granulares (BELMONTE et al., 2016; FERREIRA, 2015; 
KERSCHBAUMER, 2018; LINHARES, 2015; LINHARES et al., 2014; PORDEUS, 2017; 


28 
 
 
RONSZCKA et al., 2015; RONSZCKA, 2019; SANTOS, 2017; SIMÃO; STADZISZ, 
2009a; SIMÃO; STADZISZ, 2010).  
De fato, o PON utiliza evoluções (i. e. adaptações e melhorias) de conceitos de 
PD no tocante a sua expressão, como Elementos da Base de Fatos (Fact Base 
Elements - FBE) e Regras (Rules)1. Assim, no tocante à expressão e na qualidade de 
uma abordagem orientada a regras, o PON permite desenvolvimento em alto nível.  
Outro ponto fundamental e diferencial do PON é que seu mecanismo de 
inferência é inovador e ímpar, pois ocorre por meio da colaboração ativa entre 
entidades computacionais de pequeno porte, reativas e desacopladas, tudo via 
notificações pontuais e precisas. Em tempo, o PON e seu mecanismo de Inferência 
Orientada a Notificações (ION) serão detalhados no Capítulo 4.  
Por ser um paradigma relativamente novo, o PON tem sido assunto de diversas 
pesquisas e esforços de desenvolvimento. Primeiramente, o PON foi materializado na 
forma de um Framework, desenvolvido na linguagem de programação C++, sob o PI/ 
POO tendo três versões – prototipal, 1.0 e 2.0 (BANASZEWSKI, 2009; RONSZCKA, 
2012; RONSZCKA et al., 2015; VALENÇA, 2012). Além disso, versões do Framework 
implementados em C++, Java e C# foram desenvolvidas, inclusive permitindo 
aplicações efetivamente concorrentes, com paralelismos e/ou mesmo distribuídas do 
PON (BARRETO et al.,2018; BELMONTE et. al, 2016; HENZEN, 2015; OLIVEIRA et 
al.,2018; SCHÜTZ et al., 2018).  
Subsequentemente foi desenvolvida uma linguagem e compilador específicos 
para o PON, sendo essa tecnologia chamada de LingPON (FERREIRA, 2015; MELO, 
2016; PORDEUS, 2017; RONSZCKA et al., 2017; SANTOS, 2017; SANTOS et. al., 
2017). Na verdade, foi definido por Ronszcka um método para criação de linguagens e 
compiladores para o PON, atualmente chamado de MCPON, o qual serviu ao longo dos 
últimos anos de guia para a composição destes trabalhos citados no tocante a LingPON 
(RONSZCKA, 2019).  
Neste âmbito, observa-se que os esforços de implementação e de avaliação de 
aplicações PON em software utilizaram plataformas de computação providas de 
processadores sequenciais em sua execução, ou seja, construídos a partir de 
arquitetura sequencial, baseada no modelo de von Neumann, tanto monocore onde o 
PON permite evitar redundâncias de processamento, quanto multicore onde o PON 
permite paralelização de granularidade tão fina quanto possível (BELMONTE et al., 
 
1 Doravante, a nomeação das entidades PON no texto estão escritas em Inglês, visando seguir 
o padrão adotado pelo grupo de pesquisas a ser seguidos em todas as publicações relacionadas a PON 
e suas derivações. 


29 
 
 
2016; NEGRINI et al., 2019). Entretanto, como tal modelo de hardware força a 
sequencialização de todo ou parte do mecanismo de inferência por notificações em 
cada core, a materialização plena dos conceitos do PON é limitada, sendo, portanto, 
impossível implementar soluções de forma puramente paralela (KERSCHBAUMER et 
al., 2015; PORDEUS et al., 2016; SIMÃO et al., 2012b; WITT et al., 2011). 
Para fins de paralelização efetiva, o PON tem sido explorado como uma 
alternativa computacional para paradigmas de hardware, além de software. Neste 
sentido, esforços na aplicação dos conceitos de PON em Hardware têm sido realizados. 
Em suma, o PON em Hardware Digital (PON-HD) é uma implementação em hardware 
das entidades computacionais da cadeia de notificações PON, implementada em 
dispositivos 
de 
hardware 
reconfigurável 
(KERSCHBAUMER 
et 
al., 
2015; 
KERSCHBAUMER, 2018; KERSCHBAUMER et al., 2018; PORDEUS et al., 2016; 
SIMÃO et al., 2012a; WITT et al., 2011).   
Isto posto, além das melhorias conceituais do PON frente ao PI e PD no tocante 
a arquiteturas usuais como von Neumann (principalmente ao uso de entidades reativas 
e desacopladas em seu mecanismo de notificações), as materializações e pesquisas 
efetuadas em hardware específico sobre o PON são fundamentais para o 
desenvolvimento de sistemas efetivamente paralelos. Isto, em suma, é o que as 
materializações e experimentos elencados tem demonstrando ao longo do tempo2. 
1.3 Hipótese 
O PON em hardware (PON-HD), altamente paralelizável, poderia ser aplicado 
ao caso de se desenvolver RNA seguindo os preceitos do PON, sendo possível 
considerar que notificações mimetizam sinapses. Neste processo, determinados 
conjuntos de FBE (i.e., entidades facto-execucionais) associadas a certas Rules (i.e., 
entidades lógico-causais) constituiriam estruturas que mimetizariam, em alguma 
medida, neurônios de Redes Neurais Naturais (RNN) e seus relacionamentos, os quais 
colaborariam por sinapses notificantes, formando a proposição de um modelo 
computacional de RNA chamado NeuroPON. 
A solução NeuroPON poderia ser implementada primeiramente em software via 
materializações do PON em software, e, subsequentemente, feita efetivamente em 
hardware digital, via tecnologia PON-HD. No caso do NeuroPON-HD, as ditas sinapses 
notificantes se dariam explicitamente via sinais elétricos em hardware, o que se 
 
2 Maiores detalhes sobre as materializações e o próprio PON estão descritos no Capítulo 33. 


30 
 
 
aproximaria ainda mais ao que se conhece de RNN. Neste contexto, tal hipótese e 
primeiros ensaios foram trazidos em publicação em evento, bem como em trabalho de 
qualificação de tese, ambos no âmbito deste trabalho de doutoramento (SCHÜTZ, 
2017; SCHÜTZ et al., 2015). 
Corroborando com esse contexto, o trabalho de Omondi et al. (2006) aponta 
que processadores convencionais de uso geral (i.e., sequenciais e baseados na 
máquina de von Neumann) não irão explorar plenamente o paralelismo inerente a 
modelos de RNA, sendo que arquiteturas altamente paralelas são necessárias.  
Ainda, sistemas executados em processadores de propósito geral e baseados 
na máquina de von Neumann serão, por sua natureza, mais lentos do que sistemas 
executados em hardware especificamente projetados para tal função. De fato, um 
sistema gravado diretamente em hardware não necessita de sistemas operacionais, 
traduções e interpretações, além das camadas de software (e. g. APIs e mesmo 
máquinas virtuais) presentes nos computadores modernos (OMONDI et al., 2006).  
Efetivamente, soluções em hardware específico permitem propor novas 
arquiteturas ou soluções distintas do processamento sequencial. Neste contexto, dada 
a necessidade de novas soluções de computação inclusive para RNA e afins, torna-se 
evidente que hardware reconfigurável, destacadamente os dispositivos FPGA, 
apresentam-se como opções altamente úteis inclusive para fins prototipais e 
demonstração de conceito (KERSCHBAUMER; LINHARES; et al.,2018; OMONDI et al., 
2006; PEDRONI, 2010).  
Entretanto, para o desenvolvimento de sistemas paralelos em dispositivos 
FPGA é necessário um conhecimento técnico acentuado (TISAN; CHIN, 2015), sendo 
isso observado inclusive em atuais abordagens paralelas de RNA via implementação 
em dispositivos FPGA (ALI; MOHAMMED, 2010; DEOTALE; DOLE, 2014; MOUKHLIS 
et al., 2014; REZVANI et al., 2012). Outrossim, uma suposta alternativa seria usar 
ferramentas de alto nível que geram código para dispositivos FPGA. Entretanto, em 
geral, tais ferramentas são baseadas nos paradigmas vigentes de programação, 
gerando os problemas de acoplamento e dificuldades de paralelismo já discutidos 
(BANASZEWSKI et al., 2007; GABBRIELLI; MARTINI, 2010; KAISLER, 2005; 
KERSCHBAUMER, 2018; SIMÃO; STADZISZ, 2009a).  
Em suma, como usualmente as RNA são implementadas seguindo os preceitos 
do PI, por vezes de maneira muito técnica, e com as dificuldades inerentes a este 
paradigma, ou de maneira ainda mais técnica quando descritas para executarem 
diretamente em hardware utilizando VHDL, a alternativa da utilização de 


31 
 
 
materializações do PON facilitaria a implementação de RNA, em particular via a 
linguagem própria do PON (LingPON) que é orientada a regras. Neste contexto, a partir 
de linguagem de alto nível, poder-se-ia desenvolver RNA declarativamente em alto 
nível e, ao mesmo tempo, permitir sua execução apropriada para arquiteturas 
sequenciais, suficientemente paralelizadas para multicore e ainda altamente 
paralelizadas em dispositivos FPGA.  
Neste âmbito, a tecnologia PON-HD é efetivamente uma alternativa para 
programar, em alto nível, sistemas paralelos para execução em dispositivos FPGA, 
sobretudo quando aliado à LingPON, constituindo a chamada LingPON-HD 
(KERSCHBAUMER, 
2018; 
KERSCHBAUMER; 
LINHARES; 
et 
al., 
2018; 
KERSCHBAUMER; SIMAO; et al., 2018; PORDEUS et al., 2016; RONSZCKA, 2019). 
Assume-se então que a LingPON-HD poderia facilitar o desenvolvimento de RNA 
efetivamente paralela a partir de uma abordagem declarativa, bem como permitir que 
seja comprovada sua eficácia em aplicações pertinentes.  
Assim, retomando a hipótese trazida no início desta Seção, a tecnologia 
LingPON (i.e., linguagem e compilador para o PON), salientando a LingPON-HD, 
poderia ser utilizada para a criação de um modelo computacional que traga novas 
maneiras de compor, estruturar e executar RNA à luz do PON, denominado NeuroPON. 
O modelo computacional NeuroPON deve, ademais, possuir uma linguagem 
descritiva/declarativa, na qual se parametrizaria o necessário para gerar NeuroPON via 
tecnologia LingPON. Isto posto, postula-se que pode haver ganhos tanto da forma de 
executar RNA por meio de sinapses notificantes, como na forma de desenvolvê-las em 
altíssimo nível orientando-se a regras ou mesmo a descrições. Tal modelo NeuroPON 
seria uma abordagem naturalmente diferenciada das existentes que implementam RNA 
em hardware e software dado sua elaboração à luz dos constituintes do PON. 
Neste âmbito, este trabalho diz respeito à especificação e elaboração de um 
novo modelo computacional, doravante chamado efetivamente de NeuroPON, que 
permite a construção de RNA utilizando os conceitos do PON. Outrossim, este modelo 
deverá permitir a geração de código para plataformas distintas não redundante 
(portanto eficiente) e desacoplado (portanto paralelizável), para definição, treinamento 
e execução de RNA. O objetivo geral e os objetivos específicos encontram-se descritos 
na próxima seção. 


32 
 
 
1.4 Objetivos 
O objetivo geral deste trabalho é propor um modelo computacional para 
implementação e treinamento de Redes Neurais Artificiais (RNA) orientado a 
entidades sináptico-notificantes, à luz do Paradigma Orientado a Notificações 
(PON)  
A partir do objetivo geral estabelecido, faz-se possível propor os objetivos 
específicos pertinentes.  
1) Por meio de revisão de literatura, apresentar pesquisas e discussões acerca 
de aspectos teóricos, técnicos e características outras pertinentes das 
soluções e tecnologias a serem consideradas para estabelecer em termos 
gerais a lacuna de pesquisa ou para o desenvolvimento subsequente do 
NeuroPON visando preencher tal lacuna.  
2) Desenvolver revisão de literatura sobre trabalhos relacionados à arquitetura 
de implementação de RNA, enfatizando trabalhos com implementações 
paralelas e com hardware reconfigurável, a fim de explicitar pontualmente 
lacuna contemplada neste trabalho de pesquisa. 
3) Definir e implementar um novo modelo computacional NeuroPON orientado a 
entidades notificantes, sob a perspectiva do PON, para implementação, 
treinamento e operação de RNA.  
4) Desenvolver aplicações para validação do modelo computacional NeuroPON 
construído, com execuções em software e hardware.  
5) Comparar em termos de propriedades gerais o modelo computacional 
NeuroPON e modelos computacionais vigentes de RNA, identificados via 
revisão de literatura.  
1.5 Justificativas 
Esta seção apresenta as justificativas quanto aos objetivos específicos listados 
na seção anterior. Cada um dos objetivos específicos é aqui repetido somente para fins 
de facilitar a leitura do texto. 
1) Por meio de revisão de literatura, apresentar pesquisas e discussões acerca 
de aspectos teóricos, técnicos e características outras pertinentes das 
soluções e tecnologias a serem consideradas para estabelecer em termos 
gerais a lacuna de pesquisa ou para o desenvolvimento subsequente do 
NeuroPON visando preencher tal lacuna.  
Soluções computacionais inspiradas nas RNN, ou seja, as RNA, têm sido 
apresentadas e empregadas ao longo do tempo. RNA podem ser empregadas em 


33 
 
 
diversas áreas do conhecimento. Potenciais áreas de aplicabilidade concentram-se na 
aproximação de funções, controle de processos, reconhecimento e classificação de 
padrões, agrupamento de dados, sistemas de previsão, otimização de sistemas, 
memórias associativas, dentre outras (SILVA et al., 2010a). 
Desde o primeiro modelamento matemático inspirado em um neurônio 
biológico, apresentado por McCulloch & Pitts (1943), outras soluções foram criadas no 
tocante a RNA, gerando assim uma série de topologias, estruturas e algoritmos de 
aprendizagem (RUSSEL; NORVIG, 2009; HAYKIN, 2008). Grande parte dessas 
soluções, salientando topologias de RNA, foram implementadas de forma sequencial-
imperativa em arquiteturas von Neumann, normalmente orientando-se ao uso de 
matrizes para representar os neurônios e seus pesos sinápticos (COSTA; LUDWIG 
JUNIOR, 2007; GIANNINI et al.,2017; OMONDI et al.,2006; TISAN; CHIN, 2015). 
De fato, as RNA podem ser e usualmente são implementadas utilizando-se 
linguagens de programação de propósito geral, como C, C++ e Java. Entretanto, 
conforme apontado anteriormente, tais linguagens e afins seguem a lógica baseada em 
paradigmas de programação tradicionais, portanto sequenciais, principalmente o 
Paradigma Imperativo (PI), o que resultada em aplicações geralmente acopladas e 
redundantes (KERSCHBAUMER, 2018; LAKSHMI; SUBADRA, 2013; LINHARES et 
al.,2015;PETHICK et al., 2003).  
Alternativamente, não raro RNA são implementadas ainda por meio da 
utilização de aplicativos e plataformas especializados para desenvolvimento destas. 
Tais soluções são empregadas na simulação, pesquisa e desenvolvimento de RNA, 
bem como sua aplicação em diversas áreas do conhecimento. Mesmo que tais 
soluções facilitem o desenvolvimento por meio de interface gráficas ou linguagens 
descritivas prévias, normalmente o código gerado é implementado utilizando os 
conceitos de PI. Assim, tais códigos-fonte geralmente herdam os problemas já citados 
do PI (KAISLER, 2005; LINHARES, 2015; OMONDI et al., 2006).  
Outrossim, mesmo que não tão usual quanto abordagens sequencial-
imperativa em arquiteturas von Neumann e afins, a literatura relata que outras 
implementações foram feitas usando alternativas no tocante a implementações 
paralelas, particularmente em FPGA apesar de ser necessário considerável 
conhecimento técnico para efetivamente alcançar o paralelismo nelas (HARIPRASATH; 
PRABAKAR, 2012; LI; LI, 2012;  NEDJAH et al., 2016). Ainda, mesmo que haja 
linguagens de desenvolvimento para FPGA, elas são em geral derivadas das 
linguagens sequencial-imperativas, advindas da computação sequencial, justamente 


34 
 
 
não aproveitando o paralelismo disponível em dispositivos  FPGA, o que seria uma das 
grandes vantagens desta (COUSSY et al., 2009; MEEUS et al., 2012). Uma alternativa 
neste âmbito é justamente o PON e sua tecnologia LingPON (linguagem e compilador) 
quando aplicada ao âmbito de dispositivos FPGA (KERSCHBAUMER, 2018; 
KERSCHBAUMER; LINHARES; et al.,2018; LINHARES et al., 2015;  PORDEUS, 
2017).  
Isto tudo considerado, apresentar uma revisão de literatura das soluções 
existentes pertinentes é necessária para fundamentar esta tese. Primeiramente, tem-
se que estudar RNA em geral, apresentando mais efetivamente as imperfeições de 
soluções usuais, normalmente matriciais, em ambiente sequencial-imperativo. 
Subsequentemente, é necessário também salientar as dificuldades gerais de 
implementação de RNA em FPGA, seja diretamente ou por meio de suas linguagens 
de desenvolvimento. Ainda, apresenta-se o PON e seu arcabouço técnico como uma 
solução útil inclusive para o desenvolvimento em FPGA, levando a possibilidade de 
propor o modelo computacional NeuroPON. 
Topologias usuais, aplicadas em arquiteturas von Neumann e também em 
soluções para dispositivos FPGA, precisam ser evidenciadas nesta revisão. Isto se dá 
para que tal topologia seja testada e validada no modelo computacional NeuroPON 
proposto. Partindo do pressuposto que uma dada topologia tem sido amplamente 
pesquisada, pretende-se neste objetivo específico, entender e aproveitar, por meio da 
investigação bibliográfica, conceitos e exemplos consolidados de RNA da topologia em 
questão, que é a Perceptron de Múltiplas Camadas (Multi-Layer Perceptron – MLP), 
mas agora em NeuroPON.  
Isto tudo posto, os conteúdos elencados para estudos no objetivo sob 
justificativa tornam-se necessários.  
2) Desenvolver revisão de literatura sobre trabalhos relacionados à arquitetura 
de implementação de RNA, enfatizando trabalhos com implementações 
paralelas e com hardware reconfigurável, a fim de explicitar pontualmente 
lacuna contemplada neste trabalho de pesquisa. 
Partindo-se do pressuposto que as RNA implementadas de forma paralela 
operam em alguma medida de forma mais fidedigna às RNN (Redes Neurais Naturais), 
aplicações que gerem códigos sequenciais não irão explorar plenamente o paralelismo 
que supostamente deveria ser inerente a modelos de RNA (Redes Neurais Artificiais) 
(NEDJAH et al., 2012; OMONDI et al., 2006; VOLOKITIN, 2014). Assim sendo, a 
literatura apresenta alternativas a soluções sequenciais, as quais tem orbitado inclusive 
no tocante a tecnologia de FPGA. 


35 
 
 
Isto dito, o presente objetivo específico engloba a realização de revisão de 
literatura acerca das implementações alternativas de RNA e suas aplicações, 
concentrando tal pesquisa nos temas relevantes para o presente trabalho, incluindo 
particularmente aplicações que envolvam paralelismo e reconfigurabilidade. Assim, 
além do conhecimento das técnicas a serem utilizadas, pretende-se com este objetivo 
conhecer implementações já existentes, para que se possa precisar lacunas à luz do 
estado da arte, o que deve ensejar o modelo proposto NeuroPON. 
Ademais, visando a delimitação das aplicações e experimentos em RNA, as 
pesquisas têm particular atenção em experimentos que utilizem a topologia Perceptron 
de Múltiplas Camadas (Multi-Layer Perceptron – MLP). Neste contexto, a título de prova 
de conceito, o modelo computacional NeuroPON deve permitir a criação de RNA de tal 
topologia.  
3) Definir e implementar um novo modelo computacional NeuroPON orientado a 
entidades notificantes, à luz do PON, para implementação, treinamento e 
operação de RNA.  
O objetivo da tese é propor, modelar e implementar o modelo computacional 
NeuroPON, no qual cada neurônio e cada RNA serão entidades computacionais 
orientadas a notificações, à luz das propriedades do PON. O fato de neurônios serem 
efetivamente entidades computacionais permitiria notificação interneurônio, o que se 
assemelharia a sinapses entre eles, além de permitir manipular cada neurônio 
individualmente ou coleções deles, como eventualmente aplicar diferentes funções de 
ativação em grupo deles. Neste âmbito, o NeuroPON deve explorar características 
pertinentes do PON, como desenvolvimento em alto nível, não redundância de código  
e, particularmente, desacoplamento implícito (portanto neurônios paralelizáveis e 
individualizáveis).  
A viabilização de um modelo computacional que permita a descrição de uma 
RNA em alto nível, sem a necessidade de conhecimento prévio de linguagens de 
programação complexas, é também parte da proposta deste objetivo específico. Tal 
modelo deverá permitir a especificação de RNA em alto nível (de forma declarativa ou 
descritiva), o qual deve gerar automaticamente código PON, para realizar o treinamento 
e operação de cada RNA especificada, de forma eficiente e paralelizável. Neste 
contexto, linguagens de descrição de RNA existentes serão avaliadas, a fim de verificar 
a que melhor se adeque às premissas do modelo computacional NeuroPON.   
O modelo computacional NeuroPON deve ser proposto por meio de linguagem 
de modelagem, nomeadamente a UML e diagrama próprios ao PON (KOSSOSKI, 


36 
 
 
2015; MENDONÇA et al., 2015), onde já se observaria a existência de entidades 
relativas a neurônios desacopladas entre si. Subsequentemente, deve haver a 
implementação do modelo computacional NeuroPON, a qual se dará por meio de 
adaptação e conformação de materializações do PON. Particularmente, serão 
evoluídas e conformadas as materializações do PON que se encontram na forma de 
arquétipos/frameworks (tanto em software e hardware) e, particularmente, a da 
tecnologia LingPON (BELMONTE et al., 2016; KERSCHBAUMER; LINHARES; et al., 
2018; RONSZCKA; FERREIRA; et al., 2017; RONSZCKA; VALENÇA; et al.,  2017; 
SCHÜTZ; RONSZCKA, 2015).  
4) Desenvolver aplicações para validação do modelo computacional NeuroPON 
construído, com execuções em software e hardware.  
Visando apresentar a validade do modelo computacional NeuroPON proposto 
quanto ao desenvolvimento de RNA, algumas aplicações conhecidas da literatura serão 
construídas utilizando a tecnologia NeuroPON. Tais aplicações experimentais serão 
desenvolvidas utilizando os arquétipos do PON conformados para tal, nomeadamente 
os Frameworks PON C++ 2.0, 3.0 e LingPON para software, bem  como LingPON para 
hardware reprogramável. 
Nestes experimentos, busca-se, portanto, verificar a real possibilidade de 
desenvolvimento de RNA composta por entidades neuro-notificantes definidas no 
NeuroPON, as quais remetam a notificações que seriam em alguma medida sinapses 
artificiais.  
Tais aplicações experimentais que implementarão o treinamento e execução 
de RNA MLP serão no tocante a função XOR (eXclusive OR) e a base de dados da flor 
de IRIS (“Iris DataSet”, 2016), as quais são consideradas problemas clássicos na área 
de aprendizado de máquina. Considera-se que tais experimentos sejam suficientes 
para apresentar os conceitos propostos ao modelo computacional NeuroPON. 
5) Comparar em termos de propriedades gerais o modelo computacional 
NeuroPON e modelos computacionais vigentes de RNA, identificados via 
revisão de literatura.  
Primeiramente, tais tabulações visam externar a aplicabilidade e a inovação do 
modelo computacional NeuroPON para a construção de RNA indicando se ele atende 
ou não uma série de características previstas. Neste contexto, os elementos de 
averiguação (e mesmo comparação subsequente) via tabelamento residem em 
algumas características inerentes aos objetivos do NeuroPON: 


37 
 
 
 Especificação em alto nível: a geração de RNA para execução eficiente em 
software, ou eminentemente paralela em hardware, a partir de uma 
especificação de alto nível, facilita a aplicação de RNA em diversas áreas de 
conhecimento.  
 Treinamento no hardware: a grande maioria dos modelos de RNA que 
podem ser executados em dispositivos FPGA, executam o treinamento em 
aplicativos rodando em máquinas sequenciais para depois testar o modelo 
no hardware com os pesos já treinados. Desta forma, o treinamento ou 
“aprendizado” não é executado de forma paralela, diferentemente do 
pressuposto para uma RNA. 
 Possibilidade de customização: tal funcionalidade permite ao usuário do 
modelo informar como será constituída a RNA a ser utilizada. Neste âmbito, 
o presente trabalho pretende criar um modelo a ser utilizado em diversas 
aplicações, não somente em provas de conceito com parâmetros fixos no 
código. Desta forma, uma linguagem padrão para descrição de RNA será 
utilizada na customização, sem a necessidade de fazer modificações 
diretamente no código que implementa a RNA. 
 Geração de código: a fim de permitir ao usuário executar a arquitetura 
construída, o modelo computacional NeuroPON deverá permitir a geração 
automática do código que implementa o treinamento e a operação da RNA.  
 Flexibilidade de plataforma: quanto ao código a ser gerado pelo NeuroPON, 
este deverá estar apto a ser executado tanto em máquinas sequenciais 
(monocore e multicore), quanto em dispositivos FPGA (paralelo). Tal 
característica visa facilitar o trabalho de usuários, pois poderão executar a 
RNA criada a partir de alto nível no dispositivo que lhes estiver disponível ou 
que lhes convier.  
Por fim, após a averiguação sobre o atendimento ou não das características 
visadas, trabalhos como Góes et al. (2002), Guo et al. (2012), Hunter et al. (2012), 
Nedjah et al. (2016), Rezvani et al. (2012) e Silva, et al. (2010b) entre outros, serão 
utilizados como base para comparar essas soluções com NeuroPON por meio de matriz 
indicado qual solução atende qual característica das listadas acima. Isso permitirá, via 
tabelamento de matriz de soluções versus características, entender como o NeuroPON 
se diferencia de soluções pertinentes no estado da arte.  


38 
 
 
Por fim, ressalta-se que não serão refeitas as aplicações utilizadas nos 
trabalhos apontados, mas sim os resultados verificados em termos de taxas de erros e 
suas características gerais pertinentes vis-à-vis ao NeuroPON com meio para saber se 
os códigos gerados executam de forma similar às dos trabalhos considerados. 
1.6 Motivações 
Por ser o PON um paradigma relativamente novo, relevante e promissor para 
o desenvolvimento de sistemas computacionais (SIMÃO, 2005; SIMÃO; STADZISZ, 
2008), torna-se importante aplicá-lo em áreas de desenvolvimento científico e/ou 
tecnológico, a fim de avaliar suas características frente a tais áreas. 
Neste âmbito, é notório que a área de RNA tem se destacado na academia e 
na indústria. Dentre alguns projetos, pode-se destacar o trabalho de Abadi e Andersen 
(2016), desenvolvido no laboratório Google Brain, que demonstra a interação entre três 
RNA, utilizando métodos de criptografia criados por elas mesmas, sem a interação 
humana no processo. Ainda, outro exemplo é do Facebook, o projeto chamado 
DeepText (ABDULKADER et al., 2016), que determina o significado de uma publicação 
ou comentário, e aprende a bloquear mensagens ofensivas.  
Outra questão importante para aplicação do PON em RNA são suas 
características de geração de código desacoplado e, portanto, paralelizável/distribuível, 
vindo de encontro ao paralelismo desejado nas arquiteturas de RNA. Tal característica 
do PON teria potencial para facilitar a implementação destas arquiteturas de RNA de 
forma computacionalmente paralela. Isto seria particularmente factível em ambientes 
computacionais propícios ao paralelismo, como em dispositivos FPGA. 
Neste contexto, Girau (2006) aponta que, além dos dispositivos FPGA serem 
uma escolha mais barata e flexível para implementações em hardware, alguns recursos 
apontam vantagens específicas do seu uso para implementação paralela de RNA: 
 Prototipação por meio de reprogramação; 
 Dispositivos FPGA podem ser usados de forma embarcada, mesmo para 
sistemas com baixa escala de produção. 
 Implementações baseadas em dispositivos FPGA podem ser mapeadas 
para novos dispositivos FPGA. 
Além destas, as já citadas características como reconfigurabilidade, baixo 
consumo de energia e grande capacidade de processamento são pontos que fazem 


39 
 
 
dos FPGAs dispositivos adequados para a implementação de RNA (DEOTALE; DOLE, 
2014; FREUND et al., 2017; GIRAU, 2006; HEMSOTH, 2017; MOHAMAD et al., 2012; 
OMONDI et al., 2006). Ainda, diversas soluções para implementação de RNA em 
hardware reconfigurável têm sido propostas. Exemplos relevantes de aplicações de 
RNA utilizando hardware reconfigurável são apresentados na Seção 2.4.7.  
1.7 Organização do Documento 
Este documento está organizado em 6 Capítulos incluindo o presente capítulo 
de introdução. 
O Capítulo 2 descreve toda a fundamentação teórica pesquisada para 
elaboração deste trabalho, abrangendo conceitos fundamentais de RNA e hardware 
reconfigurável com ênfase em FPGAs, bem como o estado da arte da implementação 
de RNA em dispositivos FPGA. 
O Capítulo 3 apresenta o Paradigma Orientado a Notificações (PON), 
descrevendo sua origem, funcionamento, materializações e o estado da técnica3. 
Ainda, melhoramentos efetuados em materializações do PON, no âmbito desta tese, 
são apresentados.  
O Capítulo 4 contém o desenvolvimento do modelo computacional NeuroPON 
Teórico. Tal desenvolvimento engloba os requisitos, premissas e aspectos relevantes 
para a concepção do modelo computacional NeuroPON Teórico. 
O Capítulo 5 apresenta os experimentos efetuados no âmbito da tese, sendo 
estes implementados tanto com materializações PON para software (Frameworks PON 
C++ 2.0 e 3.0 e LingPON), quanto para hardware (LingPON-HD), bem como o 
desenvolvimento de novos artefatos para o PON, visando a NeuroPON. 
Nomeadamente, tais artefatos são: tradutor da Linguagem de Especificação de RNA 
(baseada em XML) para LingPON, ajustes realizados nos compiladores LingPON para 
software e, principalmente LingPON para hardware (i. e. LingPON-HD para VHDL), 
visando a implementação paralela das RNA MLP em dispositivos FPGA. 
Por fim, o Capítulo 6 apresenta as conclusões desta tese e discussões finais 
acerca do trabalho proposto. 
 
 
 
3 Em tempo, alguns esforços de melhoramento do PON ainda estão em andamento e, portanto, 
serão referenciados por relatórios técnicos (alguns estimulados por disciplinas stricto sensu pertinentes 
ao PON). 


40 
 
 
2 Fundamentação Teórica 
O presente capítulo trata da apresentação dos fundamentos teóricos utilizados 
para o desenvolvimento deste trabalho. Inicialmente são abordados conceitos sobre 
Paradigmas de Programação, abordando os paradigmas significativos para o 
entendimento do Paradigma Orientado a Notificações (PON) Capítulo 3.  
Em seguida, a teoria de linguagens de programação e compiladores é 
abordada, de forma breve, inclusive em função da existência de linguagem de 
programação para o PON (LingPON).  A Seção 2.3 aborda a temática de Hardware 
Reconfigurável, a fim de apresentar a tecnologia de dispositivos FPGA aqui utilizada.   
Na sequência, o tema de Redes Neurais Artificiais (RNA) é considerado. Em 
tempo, ressalta-se que a área de RNA é uma área ampla em termos de ramificações 
de tópicos, à luz das compreensões das pesquisas efetuadas neste trabalho. Neste 
âmbito, percebe-se tópicos de RNA, naturalmente correlacionados, como arquitetura 
topológica, métodos de treinamento, aplicações e modelos de desenvolvimento.  
Neste contexto, a busca por material bibliográfico utilizou critérios como: 
 Busca por palavras-chave em bases de pesquisa relevantes para a área de 
Engenharia ou Ciência da Computação, notadamente em IEEE Explore, 
ACM Library e Google Scholar. 
 Quanto à data de publicação, busca por material bibliográfico relativamente 
recente (mínimo 2007), exceto no caso de material com grande número de 
referências. 
 Utilização de uma lista de predicados, apresentado no Código 1, para um 
refinamento das buscas por material, devido à quantidade de modelos e 
arquiteturas de RNA. Assim, os resultados a uma busca de trabalhos 
relativos a RNA do tipo MLP, com treinamento paralelo, foi efetuado.  
 Por fim, os resultados obtidos foram 
refinados 
considerando-se 
implementações que fossem paralelas ou paralelizáveis, e executadas 
utilizando-se hardware reconfigurável.  
Código 1 - Predicado utilizado em mecanismos de busca (exemplo do IEEE Xplore) 
01 
02 
03 
04 
05 
((("Document Title":Artificial Neural Net*) OR "Document Title":Neuron*) OR 
"Document Title":Synaptic*) AND  
(((((((("Document Title":MLP) OR "Document Title":Perceptron) OR "Document 
Title":SOM) OR "Document Title":Kohonen) NOT "Document Title":Spiking) NOT 


41 
 
 
06 
07 
08 
09 
"Document Title":Recurrent) NOT "Document Title":RBF) NOT "Document 
Title":Chebyshev) AND  
((((("Document Title":Learning) OR "Document Title":Training) OR "Document 
Title":Parallel) NOT "Document Title":Convolutional) NOT "Document 
Title":Reinforcement) 
Fonte: Autoria Própria 
Após tais refinamentos o presente capítulo apresenta discussões acerca de 
pesquisas, em hardware e software, em modificações a arquiteturas topológicas, como 
em Christiaanse et al. (2016), Nedjah et al. (2012, 2016) e Parker; Khan (2016). 
Também há pesquisas direcionadas aos métodos de treinamento, como em Chaturvedi 
et al. (2014), Courbariaux et al. (2015), Courbariaux; Bengio (2016),  Ortega-Zamorano 
et al. (2014) e Popa (2014). Ainda, há pesquisas focadas em áreas de aplicação, como 
em Moukhlis et al. (2014), Rocha (2015), Sridevi et al. (2017) e Vyas; Upadhyay (2014). 
Por fim, há pesquisas mais voltadas a modelos de desenvolvimento computacional, 
como aqueles em dispositivos GPU e FPGA: Abrol; Mahajan (2015), Atibi et al. (2014), 
Deotale; Dole (2014) e Yazdanbakhsh et al. (2015).  
Os tópicos apresentados na revisão de RNA tratam principalmente desses 
modelos de desenvolvimento computacional, tanto em software quanto em hardware. 
Entretanto, naturalmente, revisa-se alguns conceitos pertinentes para aqueles modelos 
como componentes de RNA, funções de ativação (e.g. tangente hiperbólica, sigmoide, 
entre outras), arquiteturas (e.g. Perceptron de Múltiplas Camadas) e certos métodos de 
aprendizado/treinamento (e.g. algoritmo Backpropagation).  
Como o presente capítulo apresenta uma revisão de temas de potencial 
conhecimento comum, o leitor que esteja confortável com algum tema citado poderia 
ignorar a respectiva seção. Entretanto, seria aconselhável a leitura de reflexão final 
pertinente a cada seção, esta na forma de seção de considerações.  
Neste contexto, é possível que se compreenda o restante do trabalho sem uma 
leitura completa deste capítulo. Recomenda-se, entretanto, a leitura das seções a partir 
da Seção 2.4.5 , pois tratam de modelos de desenvolvimento computacional e 
exemplos de RNA, tanto em hardware quanto em software, importantes para a 
compreensão da abordagem proposta. 
2.1 Paradigmas de Programação 
Um paradigma de programação determina como deve ser efetuada a 
programação e execução de uma aplicação, por meio da definição dos conceitos e 
abstrações utilizadas para representar os elementos de um programa (SEBESTA, 


42 
 
 
2010). Assim, um paradigma de programação fornece e determina a visão que o 
programador deve ter sobre a estruturação e execução de uma aplicação. Ainda, 
segundo Peter Van Roy, um paradigma de programação é um sistema formal que 
define como a programação é realizada. Portanto, cada paradigma tem o seu próprio 
conjunto de técnicas para estruturar o pensamento na concepção de soluções em 
software (VAN ROY; HARIDI, 2004). 
Segundo Banaszewski (2009), um modelo de paradigma de programação 
usualmente está disponível na forma de uma linguagem de programação própria para 
ele ou, ainda, na forma de um arquétipo (i.e. Framework) sobre outra linguagem de 
outro paradigma. Neste sentido, as linguagens e arquétipos/frameworks de 
programação são as ferramentas capazes de tornar o paradigma aplicável e permitir 
que artefatos de software possam ser criados para solucionar problemas 
(BANASZEWSKI, 2009). 
Isto posto, para a análise do Paradigma Orientado a Notificações (PON)4 como 
paradigma de programação, é justamente conveniente fazer uma introdução de outros 
paradigmas, com os quais este pode ser comparado. Neste sentido, o PON utiliza e 
aprimora alguns conceitos apresentados pelo Paradigma Imperativo (PI) e pelo 
Paradigma Declarativo (PD), diferenciando-se peculiarmente no processo de 
organização de entidades e, sobretudo, no processo de inferência lógico-causal em 
relação às evoluções factuais. Isto dito, será considerado estes dois paradigmas (PI e 
PD), bem como alguns (sub) paradigmas mais pertinentes, considerando suas 
deficiências quanto à programação de computadores, que levaram à criação do PON. 
2.1.1 Paradigma Imperativo – PI  
O Paradigma Imperativo (PI) é baseado em uma organização sequencial de 
comandos que, quando executados, realizam manipulação de dados a partir de 
variáveis para obter o resultado desejado. Coerentemente com seu nome, tal 
programação “impera” sobre o computador com comandos que executam ações que 
normalmente mudam o estado das variáveis de um programa. A base da programação 
imperativa é o próprio conceito da Máquina de Turing, que, juntamente com os 
conceitos de von Neumann, regem o funcionamento dos computadores até os dias 
atuais (BANASZEWSKI, 2009; BROOKSHEAR; BRYLOW, 2014; WATT, 2004). 
 
4 Por ser o principal paradigma de programação utilizado no trabalho, sendo parte do objetivo 
principal, o Paradigma Orientado a Notificações (PON) será detalhadamente discutido no Capítulo 3 
desta tese.  


43 
 
 
No Paradigma Imperativo (PI), em uma visão simplista-estruturante, pode-se 
considerar como subparadigmas o Paradigma Procedimental (PP) e o Paradigma 
Orientado a Objetos (POO). Isto dito, a utilização do PI se tornou popular entre os 
desenvolvedores ao longo dos anos, primeiramente o PP e subsequentemente o POO 
(VAN ROY;HARIDI, 2004; SEBESTA,  2010; WATT, 2004). Isto, em geral, devido a 
questões como flexibilidade algorítmica e alguma riqueza de abstração, sublinhando 
neste caso o POO (XAVIER, 2014).  
No caso do PP/PI as variáveis e comandos são organizados em funções e 
procedimentos que permitem alcançar um grau significativo de modularidade no código 
implementado, desde que bem projetados e implementados (KAISLER, 2005; VAN 
ROY, 2009). O POO/PI, por sua vez, apresenta um nível de abstração considerado 
mais rico e natural do que o do PP/PI, facilitando em alguma medida o alcançar de 
modularidade (KAISLER, 2005; VAN ROY, 2009). Porém, ressalta-se que em ambos 
os casos exigem profissionais bem treinados e/ou experimentados (BANASZEWSKI, 
2009).  
Os sistemas baseados no POO/PI são compostos por uma coleção de 
entidades modulares denominadas objetos, os quais são abstrações de objetos do 
mundo (concreto ou imaginário), apresentando somente as características pertinentes 
para a implementação em sistemas computacionais. Estas características, em termos 
técnicos, agrupam atributos (“similares” a variáveis do PP) e os métodos (similares a 
funções do PP) relacionados de maneira a estimular coesão e desacoplamento que são 
os fundamentos da modularidade. Neste âmbito, a POO permite aos objetos/módulos 
(inclusive por meio de seus tipos ou classes) estabelecer relacionamentos e sinergia 
entre eles, via dispositivos como associação, agregação, herança e afins (KAISLER, 
2005; VAN ROY, 2009). 
 Entretanto, mesmo com essas pertinentes diferenças estruturais com relação 
ao PP, o POO tende a ter seus estados (dados) de programa alterados de acordo com 
uma organização sequencial de execução do PI (PRESSMAN, 2011; BANASZEWSKI, 
2009; BROOKSHEAR; BRYLOW, 2014; WATT, 2004). Ainda, na forma de 
programação segundo o PI, tanto no PP quanto no POO, induz-se ao uso de linguagens 
de programação com lógicas complexas e detalhamento técnico elevado para a 
construção de sistemas computacionais. Particularmente, quando o objetivo é o de 
obter programas com correto grau de desempenho (i.e. sem desperdício de 
processamento) e correto grau de modularidade (i.e. com o devido grau de coesão e 
desacoplamento), aquilo se torna mais evidente (XAVIER, 2014). 


44 
 
 
Neste âmbito, os programas desenvolvidos segundo o PI têm um acoplamento 
natural devido à mistura do processamento de relações lógico-causais (e.g., “se então”) 
com a execução efetiva que envolve execução de comandos e a atuação propriamente 
dita sobre os dados. Este acoplamento se torna uma deficiência ao PI no que diz 
respeito à possibilidade de obter correta modularização sem grandes esforços. Isto 
afeta questões como o reuso e também a distribuição/paralelização, no sentido de 
permitir que distintos processadores possam executar partes diferentes de um 
programa, de forma simultânea e independente (GABBRIELLI; MARTINI, 2010; 
KAISLER, 2005). 
Outra deficiência presente no PI, correlata à deficiência apontada quanto ao 
acoplamento, diz respeito às avaliações das expressões lógico-causais. Estas 
expressões são frequentemente avaliadas desnecessariamente, mesmo que seus 
respectivos estados não tenham sidos alterados, conforme procura exemplificar o 
Código 2. Tais avaliações repetitivas e desnecessárias causam degradação no 
desempenho do sistema computacional, ocasionando as chamadas redundâncias 
temporais e estruturais (GABBRIELLI; MARTINI, 2010; KAISLER, 2005).  
A redundância temporal consiste na avaliação desnecessária e repetida de 
expressões lógico-causais na presença de estados (de atributos/variáveis) já avaliados 
e inalterados. Por sua vez, a redundância estrutural ocorre quando o conhecimento 
sobre um valor de uma expressão lógica (e.g., comparação de uma variável com uma 
constante) não é compartilhado entre outras expressões causais pertinentes, causando 
reavaliações desnecessárias (BANASZEWSKI, 2009). Neste âmbito, o Código 2 
demonstra, por meio de um código de exemplo, conceitos de redundância temporal e 
estrutural presentes no PI.  
Código 2 - Exemplo de redundância no PI 
01 
02 
03 
04 
05 
06 
07 
08 
09 
10 
11 
while(true){ 
  if(objeto1.atributo1 = 1 && objeto2.atributo1 = 1){ 
    objeto1.método1(); 
    objeto2.método2(); 
  } 
... 
  if(objeto1.atributo1 = 1 && objeto2.atributoN = N){ 
    objeto1.métodoN(); 
    objeto2.métodoN(); 
  } 
} 
Fonte: Autoria Própria 


45 
 
 
Neste exemplo do Código 2, no tocante a redundância temporal, observa-se 
que o laço de repetição força a avaliação de todas as condições lógicas de forma 
sequencial. Porém, grande parte dessas avaliações lógicas é desnecessária, pois os 
valores dos atributos muitas vezes não foram modificados ou não estão com os valores 
apropriados para aprovação de expressão lógico-causal (SIMÃO; STADZISZ, 2008; 
BANASZEWSKI, 2009; SIMÃO et al., 2012a).  
No tocante à redundância estrutural, algumas avaliações lógicas estão 
replicadas no código de exemplo do Código 2, acarretando também em avaliações 
desnecessárias. Assim sendo, a quantidade de avaliações lógicas desnecessárias é 
expandida, sobretudo quando as relações causais (e.g., “se então”) estão dispersas no 
código, acarretando maior degradação de desempenho (SIMÃO; STADZISZ, 2008; 
BANASZEWSKI, 2009; SIMÃO et al., 2012a). 
2.1.2 Paradigma Declarativo – PD  
O Paradigma Declarativo (PD) é uma abordagem focada em descrever o que o 
programa deve fazer e não como seus procedimentos devem funcionar. Assim, é 
considerado um paradigma alternativo ao PI, uma vez que se preocupa com “o que 
deve fazer”, em vez de preocupar-se com “como deve ser feito” (MANZANO, 2013). Em 
tempo, na verdade o PD pode ser entendido como uma automatização sobre o PI, 
permitindo programação em mais alto nível, em camadas mais abstratas. Pode-se 
considerar como subparadigmas, dentro do PD, o Paradigma Lógico (PL) e o 
Paradigma Funcional (PF), sendo este menos distante do PI do que aquele em termos 
de camadas de abstração (MANZANO, 2013).  
Isso dito, o PD exige que o programador descreva as regras lógico-causais que 
tratam do problema, ao invés de escrever um algoritmo com passos para tal como no 
PI. Em geral, o PD faz uso de algoritmos genéricos pré-estabelecidos, a fim de resolver 
problemas (BROOKSHEAR; BRYLOW, 2014;SCOTT, 2015). Isto ocorre mesmo no PF 
quando implementado usando o PD como linha mestra. Entretanto, tal característica 
em questão do PD se acentua no PL, salientando nele os chamados Sistemas 
Baseados em Regras (SBR) (WATT, 2004). 
Um SBR é composto por elementos da base de fatos, os quais podem ser 
tratados como entidades ou instâncias tal qual objetos com atributos e métodos ou, 
senão, ‘quadros’ (frames) com escaninhos (slots) e funcionalidades em uma visão mais 
voltada à Inteligência Artificial (IA), onde PD encontra suas origens. Isto considerado, 
adicionalmente e particularmente, um SBR é também composto com um conjunto de 


46 
 
 
regras lógico-causais. Estes dois conjuntos de elementos, chamados de Base de Fatos 
e Base de Regras, são processados com o uso de uma máquina (ou motor) de 
inferência que compara regras e fatos, gerando novos fatos ou atualizando os 
existentes (ciclo de inferência) (FERREIRA, 2015; LINHARES et al., 2015; SCOTT, 
2015; XAVIER, 2014). A Figura 3 apresenta um diagrama da arquitetura de um SBR. 
Figura 3 - Exemplo de arquitetura de um SBR (adaptado de AL-TAANI, 2007) 
 
Fonte: Autoria Própria 
Neste contexto, na Figura 3, a interface dá ao usuário a possibilidade de efetuar 
as entradas no sistema e obter as saídas. Já o Módulo de Explicação ilustra ao usuário 
como e porque o sistema demonstra determinadas causas referentes ao problema 
explorado. A Base de Conhecimento é coletada a partir de especialistas humanos, 
livros especializados, ou mesmo websites. Por fim, a Máquina de Inferência faz 
inferências na ocorrência de situações derivadas do sistema idealizado, decidindo quais 
regras são satisfeitas pelos fatos existentes, e propõe a correta solução (AL-TAANI, 
2007). A Figura 4 apresenta um exemplo de regras (parte (a)) e o fluxo do sistema de 
produção (parte (b)) para um sistema de diagnóstico de falha em carros. 
Acertadamente, alguns exemplos clássicos de algoritmos otimizados utilizados 
em mecanismos de inferência são o RETE (FORGY, 1982), o TREAT, o LEAPS 
(MIRANKER et al., 1990) e também o HAL (POU-YUNG LEE; CHENG, 2002). Porém, 
mesmo com tais algoritmos de inferência procurem evitar parte das redundâncias 
temporais e estruturais, a programação por meio do PD é computacionalmente cara em 
termos de estruturas de dados a serem processadas, inclusive para viabilizar tais 
algoritmos (RONSZCKA et al., 2015; SCOTT, 2015; SIMÃO; STADZISZ, 2009a).  


47 
 
 
 
Figura 4 - Exemplo de SBR: (a) 4 regras do sistema;  
(b) fluxo do sistema de produção após a Regra 1 ser disparada 
 
Fonte: Adaptado de AL-TAANI, 2007. 
Adicionalmente, o PD pode ser considerado similar ao PI com relação à 
inferência ou cálculo lógico-causal, pois esta normalmente ocorre por entidades 
monolíticas baseadas em algum tipo de pesquisa sobre entidades passivas que 
conduzem a programas com passos de execução interdependentes. A diferença é que 
em PD ela é explícita, automatizando o que é feito implicitamente por laços (ou loops) 
em PI (GABBRIELLI E MARTINI, 2010; SIMÃO; STADZISZ, 2009a; WATT, 2004).  
Em suma, todas essas características negativas aqui elencadas de PI e PD 
contribuem para a existência de um overhead de processamento, além de forte 
acoplamento entre expressões causais e estrutura de fatos/dados, dificultando a 
execução dos programas de maneira não redundante, portanto eficiente, bem com 
processamento desacoplado, portanto potencialmente paralelo ou distribuído 
(BANASZEWSKI, 2009; LINHARES, 2015; XAVIER, 2014; WATT, 2004). 
2.1.3 Paradigma Orientado a Dados – POD ou Dataflow 
Segundo Kaisler (2005), no chamado Paradigma Orientado a Dados (POD), ou 
mais precisamente Modelo de Fluxo de Dados (Dataflow Model), o modelo de 
programação é bem distinto das abordagens de execução tidas como mais tradicionais 
como, por exemplo, o modelo sequencial imperativo, usual para arquitetura de von 
Neumann.  
A exemplo, no modelo sequencial de von Neumann, o processador busca 
instruções e dados de forma sequencial na memória para realizar a execução. Por sua 


48 
 
 
vez, no modelo dataflow, o programa é simplesmente representado por um grafo, no 
qual os nós identificam computações e arcos identificam caminhos de dados entre nós 
produtores e nós consumidores. Desta forma, nos modelos sequenciais, os programas 
executados são direcionados a partir de um contador de programa, enquanto no modelo 
dataflow a execução ocorre de acordo com a disponibilidade dos dados (JOHNSTON 
et al., 2004; KAISLER, 2005; LINHARES, 2015). Neste contexto, o modelo dataflow é 
particularmente útil para tratamento de cálculo aritmético e não necessariamente para 
o cálculo lógico causal que envolve correlação de dados a serem comparados 
(LINHARES, 2015). 
Em tempo, o dataflow seria mais que um paradigma de programação e sim um 
paradigma de computação, demandando arquitetura própria. Entretanto, ele também é 
implementado em arquitetura von Neumann e afins, onde o dataflow pode ser 
considerado como um subparadigma do PD (VAN ROY,2009). No tocante ao 
processamento aritmético, o dataflow em von Neumann se assemelharia a PF, 
enquanto no tocante ao processamento lógico-causal em von Neumann se 
assemelharia a solução de inferência Rete de SBR já discutidos em seção anterior. Isto 
considerado, um exemplo do modelo dataflow comparado a um programa sequencial é 
apresentado na Figura 5. 
Figura 5 - Exemplo de modelo de Fluxo de Dados no POD: 
 (a) código sequencial; (b) seu equivalente em modelo dataflow 
(a)
(b)
a = x + y;
b = y / 6;
f = a * b;
+
/
*
x
y
6
f
 
 Fonte: Adaptado de JOHNSTON et al., 2004 
A Figura 5 (a) mostra um fragmento de um código de programa, enquanto que 
a Figura 5 (b) apresenta como tal código é representado em um grafo no modelo 
dataflow. No grafo, portanto, as setas representam os arcos, os círculos representam 
os nós de instrução, os quadrados os valores, e as letras representam onde os dados 
fluem para dentro ou fora do restante do programa, não mostradas no grafo. Neste 


49 
 
 
contexto, o programa calcula o resultado de uma função com duas variáveis de entrada 
(x e y), uma constante (6) e um resultado de saída (f) (JOHNSTON et al., 2004).  
Na função apresentada na Figura 5, existe uma dependência da disponibilidade 
das entradas x e y para execução do programa no modelo dataflow, porém uma vez 
que x e y estejam disponíveis, os cálculos de (x + y) e (y / 6) são executados e seus 
resultados ficam disponíveis imediatamente para o próximo nó do grafo. Uma vez que 
estes dados estão disponíveis, o cálculo correspondente é realizado e seu resultado é 
disponibilizado automaticamente na variável de saída f. Desta forma, há uma 
colaboração simultânea para o cálculo de f sem uma definição programática de 
sequência de execução entre estas duas operações (JOHNSTON et al., 2004). 
No entanto, Linhares (2015) aponta que, como este modelo apresenta uma 
dependência elevada da disponibilidade dos dados para orientar a sua execução, deve 
ser levada em consideração a complexidade no acesso a dados, devido às hierarquias 
de memórias. Neste âmbito, este modelo possui a desvantagem das latências 
envolvidas para acesso aos dados (LINHARES, 2015). Por fim, Johnston et al. (2004) 
aponta que existem três características chave neste modelo, ainda a serem resolvidas: 
a representação das estruturas de fluxo de controle (o que envolveria cálculo lógico-
causal), a representação das estruturas de dados, a visualização da execução e o não-
determinismo. 
2.1.4 Considerações sobre Paradigmas de Programação 
Em suma, conforme explanado, a programação que segue os paradigmas 
descritos não alcança, de maneira fácil e conjunta, alguns requisitos importantes para 
o aproveitamento total de um sistema computadorizado. Neste contexto, a facilidade de 
obtenção de código não redundante, facilidade de código eficiente, facilidade e 
flexibilidade na composição de programas, divisão de código em módulos 
refinadamente coesos-desacoplados, paralelismo efetivo fino e distribuição finamente 
balanceada são exemplos de tais requisitos. Isto se dá em função de processo de 
inferência orientado a busca (implícito ou explicito) que acopla parte do código e 
sobrecarrega processamento (RONSZCKA, 2012; SIMÃO et al., 2012a). 
Tal questão acima descrita se torna um problema, principalmente quando se 
considera a demanda de mercado por software, no qual facilidade de desenvolvimento, 
código eficiente e processos de paralelização e distribuição são requisitos atuais 
(RONSZCKA, 2012). Na verdade, tal demanda por software estimula novas pesquisas 
e soluções para tornar menos complexa (quiçá mais simples) a tarefa de construir 


50 
 
 
software com tais requisitos (SIMÃO et al., 2012a). Neste âmbito, um novo paradigma 
denominado Paradigma Orientado a Notificações (PON) foi proposto, e é assunto do 
Capítulo 3.  
No presente capítulo, entretanto, ainda há outros assuntos a serem 
considerados. Neste sentido, uma vez que os principais Paradigmas de Programação 
foram descritos, bem como sua taxonomia foi apresentada e considerações foram 
apontadas, a Seção 2.2 aborda, de forma resumida, os conceitos de linguagens e 
compiladores que regem a construção de linguagens de programação. Do ponto de 
vista da teoria de linguagem e compiladores, os paradigmas relatados e suas 
linguagens seriam agrupados em um paradigma maior e regidos pela mesma teoria 
geral. Tal paradigma que seria o paradigma sequencial, à luz da própria arquitetura 
computacional ainda vigente (arquitetura de von Neumann de origem sequencial).  
Tais conceitos têm sido importantes para a criação de diversas linguagens nos 
diversos paradigmas, o que inclui a linguagem/compilador do próprio PON, chamada 
de LingPON. Neste âmbito, dentre os objetivos do presente trabalho de pesquisa, está 
a conformação de materializações existentes do PON, juntamente com o uso de 
linguagem descritiva-declarativa em alto nível, para o desenvolvimento de RNA com 
treinamento e execução a partir de entidades derivadas do PON. 
2.2 Linguagens e compiladores 
Uma linguagem de programação pode ser definida, segundo Gabbrielli e Martini 
(2010), como um formalismo artificial onde algoritmos podem ser expressos, a fim de 
construir soluções computacionais (GABBRIELLI; MARTINI, 2010).  Porém antes dos 
programas escritos em qualquer linguagem serem executados em computadores, estes 
precisam ser traduzidos em uma forma legível à máquina. Neste contexto, os sistemas 
de software que fazem tal tradução são chamados de compiladores (AHO et al., 2006). 
Um compilador é uma aplicação que lê um programa escrito em uma linguagem 
(linguagem fonte) e traduz para um programa equivalente em outra linguagem 
(linguagem alvo), a qual não é necessariamente “linguagem de máquina” (AHO et al., 
2006). Um código pode sofrer, ainda, várias traduções ou compilações até que possa 
ser executado diretamente por uma máquina.  
O processo de compilação é dividido em duas etapas, cada uma responsável 
por transformar o código fonte de uma representação para outra. Dentre essas etapas 
é possível destacar as etapas de análise e de síntese (AHO et al., 2006). A Figura 6 


51 
 
 
apresenta as etapas de análise e síntese, por meio de um diagrama de atividades da 
UML, realizadas em um compilador. 
Figura 6 - Etapas e sub etapas executadas em um compilador 
 
 Fonte: Adaptado de FERREIRA, 2015. 
Na etapa de análise, primeiramente, é feita a coleta de dados sobre o código 
para a criação da tabela de símbolos. Tal tabela contém dados sobre o código e pode 
ser utilizada em todas as etapas do compilador. Entre os dados coletados estão os 
nomes de variáveis e funções, seus tipos, parâmetros, entre outros (AHO et al., 2006).  
Após a construção da tabela de símbolos, o compilador executa três tipos de 
análise diferentes: análise léxica, análise sintática e análise semântica do código. Os 
processos em cada uma das etapas podem ser descritos por:  
 Análise léxica: também conhecida como scanning, tal etapa avalia se todos 
os símbolos que são utilizados no código são válidos. Em caso positivo, os 
caracteres do código são agrupados em sequências significativas chamadas 
de lexemas. Os lexemas são repassados à próxima fase de compilação, a 
análise sintática. 
 Análise sintática: também chamada de parsing, esta fase de compilação 
avalia se os símbolos estão encadeados corretamente de acordo com a 
especificação sintática da linguagem. A saída desta etapa é uma árvore 


52 
 
 
sintática, onde os nós representam uma operação e, seus dependentes 
diretos, os argumentos desta operação. Tal árvore será utilizada em etapas 
posteriores de compilação para auxiliar na geração de código-alvo. 
 Análise semântica: esta etapa utiliza a árvore sintática e a informação da 
tabela de símbolos da linguagem para avaliar se o código tem consistência 
semântica, de acordo com a definição da linguagem. Como exemplo, tem-
se uma análise de atribuições de variáveis, validando sua tipificação 
(operadores e operandos devem seguir o mesmo tipo de dados), no caso de 
linguagens tipadas. 
É importante salientar que, caso sejam encontrados erros, o compilador deve 
apresentar mensagens esclarecedoras ao programador, de modo que ações corretivas 
possam ser efetuadas (AHO et al., 2006).  
Ao final da etapa de análise, uma representação intermediária do código é 
criada. Tal representação é, geralmente, uma estrutura de dados em árvore que 
representa a estrutura sintática do código, denominada usualmente árvore sintática 
(AHO et al., 2006). Tal estrutura serve de base para a realização da etapa de síntese. 
A etapa de síntese, ao seu turno, realiza a conversão da representação 
intermediária em um código alvo desejado, podendo utilizar as informações contidas na 
tabela de símbolos. Nesta etapa pode existir variações de um compilador para outro, 
onde etapas de otimização de código e geração de código final (e.g. código de máquina 
se este for o código alvo) podem ser executadas (AHO et al., 2006).  
Uma observação adicionada ao diagrama da Figura 6 é importante: todas as 
etapas do processo de compilação têm acesso à tabela de símbolos. Tal tabela contém 
cada nome definido pelo usuário no programa, sendo que tais informações são 
inseridas na tabela de símbolos pelos analisadores léxico e sintático, sendo 
subsequentemente consumidas pelo analisador semântico e pelo gerador de código 
(AHO et al., 2006). 
A presente seção visou abordar, de forma simples, o que são linguagens de 
programação e compiladores, pois são temas pertinentes aos objetivos deste trabalho. 
Outrossim, a seção subsequente (seção 2.3) trata de dispositivos de lógica 
reconfigurável, especificamente os dispositivos Field Programmable Gate Array 
(FPGA), partindo-se do pressuposto que esta é uma das tecnologias-alvo do 
desenvolvimento do NeuroPON.  


53 
 
 
2.3 Hardware e Lógica Reconfigurável 
Nas últimas décadas, é notória a evolução dos métodos de elaboração de 
sistemas digitais. Até a década de 60, os sistemas digitais eram construídos a partir de 
componentes discretos, tais como resistores, capacitores e alguns transistores. Com o 
surgimento de circuitos integrados (chips), foi possível integrar muitos transistores 
dentro de uma única pastilha de silício, dando subsídios à criação de uma vasta gama 
de produtos (PEDRONI, 2010). 
Circuitos digitais podem ser implementados a fim de executar diversos tipos de 
aplicações. Entretanto, em suma, existem duas formas usuais para se viabilizar a 
execução de uma aplicação por um circuito eletrônico: (1) por meio do uso de um 
microprocessador, que neste contexto é um hardware com características genéricas; 
ou (2) utilizar circuitos integrados de aplicação específica (ASIC - Application-Specific 
Integrated Circuit) (FERLIN, 2008; PEDRONI, 2010; ). 
O uso de microprocessadores genéricos faz com que se realize, de forma 
eletrônica, a lógica algorítmica da aplicação por meio da execução de um conjunto de 
instruções prevista para aquela arquitetura computacional. Neste caso, a execução das 
instruções causa transições nos estados internos dos circuitos do microprocessador, 
geralmente em função de dados fornecidos como entrada, e gera como resultado os 
dados processados de saída (LINHARES, 2015).   
Outrossim, aplicações de hardware específico utilizam circuitos integrados de 
aplicação específica ou ASIC (Application Specific Integrated Circuit). Projetado para 
um sistema específico, os dispositivos ASIC geralmente possuem um desempenho 
superior e menor consumo de energia do que uma implementação genérica, via 
software, executada em um microprocessador de uso geral (FERLIN, 2008; PEDRONI, 
2010;). Uma desvantagem natural de tal modelo é que, uma vez produzido, tal sistema 
não é passível de modificações. Neste contexto, é necessário que o sistema seja 
projetado todo de uma só vez. 
Outra tecnologia mais recente presente no mercado e muito utilizada para 
prototipação e mesmo efetivação de novas tecnologias é o hardware reconfigurável. O 
hardware reconfigurável agrega o melhor das duas tecnologias (genérica e específica), 
pois pode ser alterado por meio de (re)programação, e adaptado a uma aplicação 
específica, utilizando uma quantidade menor de componentes se comparado a um 
hardware de uso geral (LINHARES, 2015). Neste contexto, o hardware pode ser 
adaptado às necessidades do projetista sem uma gravação permanente, ter a 
disposição considerável poder de processamento com baixos custo de prototipação e 


54 
 
 
gasto energético (COSTA, 2014; PEDRONI, 2010b). A Seção 2.3.1 trata, justamente, 
da tecnologia de hardware reconfigurável. 
2.3.1 Hardware reconfigurável: dispositivos FPGA 
A proposta da computação reconfigurável é disponibilizar uma estrutura de 
“hardware virtual”, podendo emular vários sistemas complexos de forma transparente 
ao usuário. Neste âmbito, o hardware reconfigurável é considerado um hardware de 
propósito geral configurado para realizar uma tarefa específica, mas podendo ser 
reconfigurado sob demanda para realizar outras tarefas específicas (COSTA, 2014; 
PEDRONI, 2010b). 
Costa (2014) define FPGA como um dispositivo de propósito geral, consistindo 
de uma matriz de elementos de circuitos chamado de blocos lógicos e recursos de 
interconexão, com lógica programável multinível, customizável em campo pelo 
usuário5. Ainda, de acordo com Balid e Abdulwahed (2013), os dispositivos FPGA 
podem ser definidos como circuitos integrados programáveis pelo usuário que oferecem 
um nível razoável de integração, baixo custo de prototipagem e uma rápida capacidade 
de produção (BALID; ABDULWAHED, 2013; COSTA, 2014).  
Segundo Pedroni (2010), nos dispositivos FPGA a configuração (ou o arranjo 
dos elementos lógicos) é volátil, implementada em memórias SRAM. Isso requer que 
as FPGA contenham uma memória não volátil extra, embutida no chip, que é utilizada 
para a programação (volátil) da configuração quando da inicialização do dispositivo 
(CHEN et al., 2006; COSTA, 2014; PEDRONI, 2010). A Figura 7 apresenta o esquema 
que reproduz a arquitetura interna de um FPGA SRAM. 
Figura 7 - Arquitetura de um dispositivo FPGA SRAM 
 
Fonte: Adaptado de BROWN; VRANESIC, 2008. 
 
5 Tal usuário seria uma pessoa com domínio técnico no assunto. 


55 
 
 
Costa (2014) afirma que o tamanho, a estrutura e o número de blocos de um 
FPGA, bem como a quantidade e a conectividade de suas interconexões variam 
consideravelmente entre as arquiteturas existentes. Outrossim, os seguintes recursos 
sempre estarão presentes: 
a. Funções lógicas programáveis de n entradas, onde n varia com o 
fabricante de FPGA e com o modelo do mesmo; 
b. Rede de conexão para ligação entre as diferentes portas; 
c. Flip-flops para o armazenamento de informação; 
d. Buffers de entrada e saída. 
A Figura 8 apresenta a estrutura interna, de forma genérica (i. e., não atrelada 
a fabricantes), de uma FPGA.  
Figura 8 - Estrutura interna de uma FPGA 
 
 Fonte: Adaptado de BROWN; VRANESIC, 2008. 
Conforme demonstrado na Figura 8, internamente os FPGA são compostos por 
blocos lógicos, utilizados para a configuração das funções lógicas, bem como as 
interconexões entre estes blocos. Os blocos lógicos, por sua vez, podem ser baseados 
em LUT (lookup tables), as quais são compostas por células de armazenamento 
multiplexáveis que permitem implementar um mapeamento entre os valores binários de 
um conjunto de entradas e o valor binário de saída da função correspondente (i.e., uma 
tabela verdade da função a ser implementada). Tal mapeamento, juntamente com os 
valores binários de entrada e o estado das chaves binárias de interconexão, 
constituem-se portanto nos elementos configuráveis de um dispositivo FPGA (BROWN; 


56 
 
 
VRANESIC, 2008; CARRO, 2001; COSTA, 2014; PEDRONI, 2010b). A Figura 9 
apresenta um esquema de uma LUT. 
Figura 9 - Estrutura de uma LUT de duas entradas: (a) tabela verdade; (b) circuito representativo 
implementado via multiplexadores. 
entrada 
seleção 
Saída 
0 
0 
x2 
x1 
F 
0 
1 
x2 
1 
0 
x2 
x1 
1 
1 
x2 
 
 
(a) 
(b) 
Fonte: Adaptado de BROWN; VRANESIC, 2008. 
A Figura 9 apresenta duas formas de representação de uma LUT: a parte (a) 
apresenta a tabela verdade da função a ser executada na FPGA; (b) apresenta um 
circuito implementando uma LUT via multiplexadores. Neste caso, a LUT é capaz de 
implementar qualquer função lógica que possa ser especificada via tabela verdade. 
Conclui-se, portanto, que os elementos reprogramáveis apresentados possuem, em 
termos, a mesma flexibilidade de software, em um sistema baseado em processadores, 
porém sem a limitação da quantidade núcleos do processador (COSTA, 2014).  
Outrossim, os FPGA são verdadeiramente paralelos por natureza, sendo que 
diferentes operações de processamento não necessariamente competem pelos 
mesmos recursos. Neste contexto, cada tarefa de processamento é enviada para uma 
seção dedicada do dispositivo, podendo ser executada de modo autônomo a outros 
blocos lógicos (COSTA, 2014; FERLIN, 2008). 
Ainda, quanto às vantagens de processamento paralelo utilizando FPGA, Ferlin 
(2008) aponta que, a exploração do paralelismo pela execução simultânea de tarefas 
em sistemas de computação reconfigurável aceleram a execução do programa, 
proporcionando assim uma alternativa de alta performance para soluções que antes 
eram exclusivamente em software (FERLIN, 2008). 
Assim, com a capacidade de implementar milhares de portas lógicas em um 
único circuito integrado e por serem programados pelo usuário no campo, os 
dispositivos FPGA deixaram os projetos de lógica digital mais baratos e rápidos, 
tornando-se muito populares. Atualmente, sistemas embarcados em FPGA são tidos 
como a principal escolha em produtos que necessitam de alto processamento 


57 
 
 
computacional, como em processamento gráfico e codificadores de vídeo. Entretanto, 
a programação de dispositivos FPGA ainda exige considerável conhecimento técnico, 
sendo este diferente de programação de softwares, dado que se trata de construção de 
circuitos (CARRO, 2001; COSTA, 2014; PEDRONI, 2010b). Entretanto, essa 
dificuldade pode ser diminuída um tanto, o que é tema da seção 2.3.2. 
2.3.2 Programação de FPGA 
A computação reconfigurável em FPGA objetiva preencher a lacuna entre 
hardware especifico e software sobre processador de cunho geral, alcançando maior 
desempenho do que o software e mantendo um grau de flexibilidade maior do que o 
hardware específico usual (PEDRONI, 2010a; PETERS et al. , 2012). Apesar da alta 
complexidade dos dispositivos programáveis, nomeadamente FPGA, a programação 
destes é, em termos, facilitada. 
Uma abstração muito utilizada na descrição e programação de FPGA são as 
Linguagens de Descrição de Hardware (HDL – Hardware Description Languages). As 
duas principais HDL, segundo Pedroni (2010a), são Verilog e VHDL sendo que, por 
meio destas, é possível descrever o hardware com arquivos-fonte. Assim, modificando-
se somente tais arquivos há a possibilidade de se atualizar todo o hardware do sistema. 
Esta atualização pode ser feita tanto na inicialização do dispositivo como em tempo de 
execução (PEDRONI, 2010a). 
Ainda, segundo LaMeres (2017), linguagens de descrição de hardware 
permitem, além da descrição do hardware, simulação dos circuitos resultantes em 
diferentes níveis de abstração. A utilização de linguagens de descrição de hardware 
traz a facilidade de trabalhar em um nível mais alto de abstração, sem a dependência 
de uma arquitetura específica (LAMERES, 2017). Também, a utilização das linguagens 
de descrição de hardware pode automatizar o processo de síntese que permite que as 
ferramentas de CAD (Computer-Aided Design) criem automaticamente os circuitos a 
nível de hardware. A utilização de bibliotecas contendo componentes e funções 
predefinidas também é uma característica importante das linguagens de descrição de 
hardware (LAMERES, 2017). 
Outro processo de concepção de circuitos é configurá-lo na forma de diagrama 
esquemático. Segundo Linhares (2015) tal método espera um desenho de circuito no 
qual se explicita os componentes discretos que o compõem (portas lógicas, buffers, 
comparadores, circuitos aritméticos, etc.) e as suas interconexões. Porém, de acordo 
com Ferlin (2008), esta abordagem tende a se tornar impraticável para grandes 


58 
 
 
projetos, pois a dificuldade em se gerenciar a representação gráfica de componentes é 
diretamente proporcional ao tamanho do projeto (FERLIN, 2008; LINHARES, 2015). 
Visando uma alternativa de programação, os fabricantes de hardwares 
reprogramáveis apresentam IDE (Integrated Development Environment ou Ambiente 
de Desenvolvimento Integrado) para manipulação dos mesmos, fazendo com que a 
configuração da arquitetura interna do chip, responsável pela função do mesmo, seja 
transparente ao usuário. Tais IDE, que seguem os padrões de fluxo de projeto de cada 
arquitetura, permitem ainda que o sistema seja simulado e verificado passo-a-passo, 
por meio da geração de arquivos com padrões de testes, onde podem ser colocadas 
todas as características de temporização e debug (CHEN et al., 2006; COSTA, 2014; 
PEDRONI, 2010b). 
 
Atualmente, aplicativos específicos conhecidos como ferramentas de 
Automação de Projeto Eletrônico (EDA – Electronic Design Automation), desenvolvidos 
por fabricantes de FPGA e que acompanham kits de prototipação, permitem a 
realização das etapas de entrada do circuito, bem como automatizam as etapas do 
fluxo de projeto anteriormente listado. Exemplos de ferramentas ou ambientes 
disponíveis para esta finalidade no mercado são Altera Quartus II e Xilinx ISE, ambas 
permitindo todas as funcionalidades do fluxo de projeto (CHEN et al., 2006; COSTA, 
2014; PEDRONI, 2010). 
Não obstante, apesar de todo ferramental aqui apurado no tocante a construção 
de projeto de sistemas em hardware via dispositivos FPGA, Kerschbaumer (2018) 
aponta que compor tais sistemas demanda considerável conhecimento técnico. Ainda, 
observa-se que isso se agrava na concepção de projetos grandes e complexos, 
aumentando o consumo de tempo e recursos Alternativamente, entretanto, uma técnica 
vem ganhando espaço na composição de projetos de hardware, que é a chamada 
síntese em alto nível, abordada na Seção 2.3.3 (COUSSY et al., 2009).  
2.3.3 Síntese em alto nível 
Segundo Coussy et al. (2009), a técnica de Síntese em Alto Nível (High-Level 
Synthesis – HLS) objetiva elevar o nível de abstração do projeto permitindo assim a 
rápida geração de hardware. O resultado desta geração é que o hardware sintetizado 
em alto nível é consideravelmente otimizado, em termos de desempenho, área e 
consumo de energia. Pode se observar, ainda, que HLS é importante na evolução do 
processo de projeto de circuitos de hardware, pois permite que projetistas explorem o 
espaço de projeto de forma eficiente e rápida. 


59 
 
 
A fim de propiciar a síntese em alto nível, ferramentas que permitam tal 
processo são necessárias. De acordo com Meeus et al. (2012), ferramentas de HLS 
visam preencher a lacuna entre a concepção de algoritmos a serem executados 
diretamente em hardware e o projeto do hardware em si. Tais ferramentas otimizam o 
processo, pois automatizam as etapas mais complexas da geração de circuitos digitais 
(MEEUS et al., 2012). Como exemplo, a ferramenta Catapult C, da empresa Calipto 
Design Systems, aceita um subconjunto das linguagens C, C++ e SystemC para síntese 
de alto nível. Outros exemplos são AccelDSP, Agility compiler, AutoPilot e C-to-Silicon 
(MEEUS et al., 2012). 
A implementação direta de sistemas em dispositivos FPGA é considerada mais 
complexa do que em microprocessadores (MEEUS et al., 2012). A função fim de um 
circuito (uma aplicação ou programa) pode ser implementado por meio de linguagens 
como C/C++ em um microprocessador, e geralmente estão alocados em máquinas com 
sistemas operacionais, facilitando assim um tanto a sua programação. Já dispositivos 
FPGA dependem de configurações específicas, pois depois de programados 
funcionarão como hardware específico. 
Isto posto, a principal característica de uma ferramenta de HLS é sua linguagem 
de entrada. A linguagem oferecida pela ferramenta deve ser compatível com as 
linguagens de implementação de algoritmos, facilitando assim a migração dos códigos 
já existentes, vislumbrados inicialmente para software. Uma ferramenta de HLS deveria 
também permitir a captura do projeto com certo nível de abstração. Ainda, é igualmente 
importante que a ferramenta e seus recursos sejam fáceis de usar (MEEUS et al., 
2012). 
Por outro lado,  Simão e Stadzisz (2009a), Tisan e Chin (2015) e Windh et al. 
(2015) apontam que as linguagens de programação tradicionais não são adequadas 
para o desenvolvimento de projetos envolvendo paralelismo. Tisan e Chin (2015) e 
Windh et al. (2015) complementam que, além disso, o uso destas linguagens não 
permite o total aproveitamento das potencialidades de dispositivos como os FPGA. Não 
obstante, grande parte da comunidade desenvolvedora segue usando ferramentas de 
sínteses baseadas em linguagens usuais (TISAN; CHIN, 2015; WINDH et al., 2015). 
Neste contexto, Windh et al. (2015) aponta que linguagens baseadas em C não 
são apropriadas para as ferramentas de síntese de alto nível, devido principalmente à 
falta de informação temporal no código, bem como a ausência de um modelo de 
concorrência e paralelismo apropriado. Não obstante, a adoção de linguagens 
baseadas em C traz um bom nível de abstração, facilitando a adaptação dos algoritmos 


60 
 
 
existentes, possibilitando assim um aprendizado mais veloz por parte do desenvolvedor 
apesar das deficiências apontadas (WINDH et al., 2015). 
Algumas linguagens específicas são muito utilizadas para a implementação de 
sistemas em FPGA. São exemplos de tais linguagens SystemC, Bluespec, 
SystemVerilog e JavaTime (ANTIQUEIRA, 2011; MEEUS et al., 2012)). Apesar disso, 
essas linguagens dificultam a reutilização ou a adaptação de algoritmos originalmente 
escritos em linguagens como C e C++ (WINDH et al., 2015). Ademais, tais linguagens 
obrigam o desenvolvedor a ter um bom conhecimento do hardware e estar ciente do 
paralelismo a ser expressado explicitamente. 
Ainda, Meeus et al. (2012) apontam uma classificação das ferramentas de 
síntese de alto nível. As principais características são: facilidade de implementação, 
nível de abstração, tipos de dados, independência de arquitetura, capacidade de 
verificação, qualidade dos resultados, documentação e curva de aprendizado (MEEUS 
et al., 2012). Entretanto, uma realidade é que a linguagens ou ferramentas de síntese 
de alto nível não contemplam realmente essas características conjuntamente com a 
devida profundidade (KERSCHBAUMER, 2018). 
Isto considerado, ainda é possível ressaltar outro trabalho com relação à 
implementação de hardware reconfigurável por meio de HLS. O trabalho de doutorado 
de Kerschbaumer (2018) objetivou permitir a descrição de sistemas utilizando a 
LingPON e sua tradução automática para a linguagem VHDL. Os resultados deste 
trabalho são animadores, pois permitem a geração de hardware em um nível de 
abstração mais alto do que a geração diretamente por meio de VHDL, em qualidade de 
expressão/abstração considerada superior em relação às abordagens de HLS 
abordadas e, ainda, apresentam os mesmos resultados em termos de desempenho e 
quantidade de elementos lógicos utilizados em tais abordagens (KERSCHBAUMER, 
2018). Tal assunto será naturalmente retomado no capítulo 4, que trata especificamente 
do PON. 
2.3.4 Considerações sobre dispositivos FPGA  
Apresentadas as principais características dos dispositivos FPGA, técnicas de 
projeto e implementação, é importante frisar que o uso de dispositivos reprogramáveis, 
especificamente os FPGA, possibilita a implementação de blocos de hardware paralelo, 
o que aumenta a eficiência computacional de um sistema. Além disso, Costa (2014) e 
Pedroni (2010) apontam que tais dispositivos são componentes muito confiáveis, sendo 


61 
 
 
que a progressiva redução dos custos de produção tem motivado sua utilização 
(COSTA, 2014; PEDRONI, 2010). 
Recursos como rápida prototipação, uso embarcado mesmo em baixa escala 
de produção, baixo consumo de energia e grande capacidade de processamento, 
incentivam a utilização de dispositivos FPGA. De fato, o hardware reconfigurável tem 
se tornado uma importante ferramenta de prototipação e mesmo aplicação, 
principalmente no desenvolvimento de aplicações que buscam paralelismo como, por 
exemplo, RNA (BOHRN et al., 2013; HARIPRASATH; PRABAKAR, 2012; MISRA; 
SAHA, 2010; NEDJAH et al., 2012; e OMONDI et al., 2006) . 
Contudo, o desenvolvimento para dispositivos FPGA, em geral, difere da 
programação de sistemas computacionais baseados em máquinas von Neumann, 
principalmente em sistemas paralelos. Entretanto, os usuários devem conhecer 
técnicas de programação em baixo nível, ou ainda as linguagens de descrição de 
hardware, a fim de refinar a programação de tais dispositivos para atingir todo seu 
potencial paralelo. Em contraponto, algumas linguagens e, até mesmo, ferramentas de 
síntese de alto nível podem ser utilizadas visando facilitar o processo. Porém, conforme 
Kerschbaumer (2018), tais ferramentas geram código não otimizado para hardware, 
principalmente na questão do paralelismo, herdando alguns problemas apontados 
ainda no Paradigma Imperativo (PI). 
Neste âmbito, trabalhos como LingPON-HD 1.0 (KERSCHBAUMER, 2018; 
PORDEUS, 2017) pretendem melhorar a implementação de sistemas paralelos 
utilizando FPGA, pois permitirá a descrição de tais sistemas utilizando linguagem de 
alto nível em estilo declarativo, sendo posteriormente traduzida automaticamente para 
VHDL via compilador elaborado para tal, melhorando a síntese do paralelismo em 
hardware. 
Isto posto, corroborado por trabalhos como os de Ali e Mohammed (2010), 
Deotale e Dole (2014), Moukhlis et al. (2014) e Rezvani et al. (2012), que demonstram 
a implementação e aplicação paralela de RNA utilizando dispositivos FPGA, postula-se 
pertinente a utilização de dispositivos de hardware reprogramáveis na implementação 
de RNA via proposição de um novo modelo de RNA que deve utilizar inclusive os 
fundamentos da tecnologia de LingPON-HD 1.0.  
Em tempo, tais trabalhos de RNA em FPGA, citados no parágrafo justo acima, 
não contemplam as funcionalidades esperadas para o modelo computacional 
NeuroPON, detalhadas no Capítulo 1. Em todo caso os trabalhos citados servem como 
exemplo da viabilidade e mesmo pertinência de implementações de RNA em 


62 
 
 
dispositivos FPGA. Isto dito, a seção 2.4 aborda a temática de RNA dado que ela é uma 
temática cerne desta tese de doutorado. 
2.4 Redes Neurais Artificiais 
Conforme salientado no início do presente capítulo, a revisão de RNA diz 
respeito a modelos de desenvolvimento em software e em hardware. Particularmente, 
considerar-se-á RNA elaboradas de forma declarativa ou em alto nível, e 
implementações visando desacoplamento/paralelismo. 
Entretanto, naturalmente, alguns conceitos de RNA são aqui revisados visando 
suportar tais conteúdos. Isso ocorre nas primeiras subseções que trazem 
respectivamente os conceitos de RNA, neurônios artificiais, arquiteturas, treinamentos 
e afins.  
2.4.1 Conceitos de RNA 
As 
Redes 
Neurais 
Artificiais 
(RNA) 
são 
definidas 
como 
modelos 
computacionais de inferência multidimensionais e não lineares, inspirados no sistema 
nervoso de seres vivos, chamados neste trabalho de Redes Neurais Naturais (RNN). 
Tais modelos possuem a capacidade de aquisição e armazenamento do conhecimento 
em forma de valores numéricos, representando os “pesos” de suas interconexões 
sinápticas (HAYKIN, 2008; HEATON, 2015; RUSSELL; NORVIG, 2009; SILVA et al., 
2010a). 
As RNA possuem um conjunto de unidades de processamento, denominados 
neurônios artificiais, os quais são interligados por um grande número de interconexões 
denominadas sinapses artificiais. Tais sinapses são representadas por vetores e/ou 
matrizes de pesos sinápticos, dependendo da quantidade necessária na representação 
da RNA (HAYKIN, 2008; HEATON, 2015; RUSSELL; NORVIG, 2009; SILVA et al., 
2010a). 
Desde a década de 1940, estudos têm sido desenvolvidos na área de RNA para 
que tais estruturas possam aprender o funcionamento de sistemas, por meio de dados, 
imitando assim o funcionamento de RNN em um ambiente computacional (KURZWEIL, 
2012). Atualmente, as RNA estão sendo aplicadas com sucesso em uma ampla gama 
de domínios de problemas, em áreas como finanças, medicina, engenharias, geologia 
e física (HAYKIN, 2008; HEATON, 2015; RUSSELL; NORVIG, 2009; SILVA et al., 
2010a).  


63 
 
 
Isto dito, no tocante à essência de uma RNA, a Figura 10 apresenta um 
exemplo de RNA utilizando um diagrama simplificado. 
Figura 10 – Diagrama de Rede Neural Artificial 
 
 Fonte: Adaptado de HEATON, 2015. 
Como visto na Figura 10, uma RNA é composta por várias camadas neuronais. 
Tais camadas auxiliam na organização dos neurônios que compõem a RNA, bem como 
nas funções da própria RNA. A função de cada camada, conforme Haykin (2008), pode 
ser descrita como: 
a) Camada de entrada: tal camada é responsável pela aquisição dos dados 
externos, sejam estes de treinamento, teste, validação ou operação. A 
camada de entrada está, portanto, conectada, de um lado à fonte dos dados 
e, de outro lado, à (primeira) camada escondida; 
b) Camada escondida: a quantidade de camadas escondidas depende 
diretamente do modelo a ser utilizado, bem como dos testes efetuados em 
campo. Outrossim, os neurônios desta camada são responsáveis pelos 
cálculos que irão ajustar os pesos sinápticos, os quais atuam na capacidade 
de aprendizado e subsequente reconhecimento de padrões da RNA. Ainda, 
tais pesos pertencem às ligações entre a camada escondida e a camada de 
entrada, bem como à próxima camada, podendo esta ser outra camada 
escondida ou a camada de saída; 
c) Camada de saída: recebe os dados advindos da última camada escondida, 
efetua a última etapa de treinamento e apresenta os resultados da RNA. 
Durante o treinamento, o valor resultante de seus neurônios é utilizado para 
recalcular os valores dos pesos sinápticos em algoritmos de aprendizado 
supervisionado. 


64 
 
 
Na Figura 10, observa-se que todas as camadas possuem uma quantidade de 
neurônios, os quais são representados por círculos. Apesar da estrutura das RNA ter 
sido desenvolvida a partir das RNN, os elementos computacionais ou unidades 
processadoras, denominadas Neurônios Artificiais, são modelos bem simplificados em 
relação aos neurônios biológicos. 
2.4.2 Neurônio Artificial 
Segundo Silva et al. (2010a), neurônios artificiais são estruturas não-lineares, 
que possuem valores de saída contínuos e realizam funções simples, como coletar os 
sinais existentes em suas entradas, agrupá-los conforme sua função operacional, e 
exibir resultados, considerando a função de ativação utilizada (SILVA et al., 2010a). A 
Figura 11 apresenta o modelo do neurônio artificial de McCullock e Pitts, o qual evoluiu 
para modelos e materializações mais contemporâneas. 
Figura 11 - Neurônio Artificial - modelo de McCulloch e Pitts 
 
 Fonte: SILVA et al., 2010a. 
A função básica de um neurônio é somar o produto dos valores de suas 
entradas pelos valores de seus pesos sinápticos (operação denominada combinação 
linear) e aplicar tal resultado a uma função de ativação. O valor resultante desta função 
de ativação é considerado a saída do neurônio e indica seu potencial de ativação, ou 
seja, quanto este é importante para o resultado a ser apresentado. 
Neste contexto, no modelo da Figura 11 os diversos sinais de entrada advindos 
do meio externo (i. e., de uma aplicação) são espelhados pelo conjunto de entradas 
representados por (x1, x2, x3, ..., xn), os quais seriam análogos aos impulsos elétricos 
externos captados pelos dendritos em um neurônio biológico. Neste sentido, a 
representação de quão significativa cada junção sináptica do modelo de neurônio 


65 
 
 
biológico é efetuada por meio do conjunto de pesos sinápticos representados por (w1, 
w2, w3, ..., wn) no neurônio artificial.  
Neste sentido, a importância de cada uma das entradas xi do neurônio é 
descoberta pela a multiplicação de seus valores pelos valores dos respectivos pesos 
sinápticos wi, ponderando-se todos os dados externos que chegam ao neurônio. Assim, 
é possível verificar que a saída do corpo celular (u) do neurônio artificial, é a soma 
ponderada de suas entradas (HAYKIN, 2008; HEATON, 2015; RUSSELL; NORVIG, 
2009; SILVA et al., 2010a). As equações (1) e (2) resumem o processo de obtenção 
dos resultados de um neurônio artificial. 
 
 = ( .  	) − 


 
(1) 
 
 = () 
(2) 
Na Figura 11 e nas equações (1) e (2) apresentadas, tem-se: 
a) Limiar de ativação (θ) ou bias: é a variável que especifica qual será o 
patamar apropriado para que o resultado produzido pelo combinador linear6 
possa gerar um valor de disparo em direção à saída do neurônio. Assim, 
esta entrada especial é usada para permitir uma melhor adaptação ao 
conhecimento a ela fornecido, pois aumenta o grau de liberdade no ajuste 
de pesos sinápticos; 
b) Potencial de ativação (u): resultado produzido pela diferença do valor 
produzido entre o combinador linear e o bias. Se tal valor é positivo, então 
o neurônio é considerado ativo, com grau igual ao valor deste potencial de 
ativação. Caso contrário, o neurônio não está ativo; 
c) Função de ativação (g(u)): limita a saída do neurônio dentro de um intervalo 
de valores razoáveis a serem assumidos pela sua própria imagem funcional. 
As funções de ativação (também chamadas de funções de transferência) 
estabelecem limites para a saída dos neurônios, indicando assim 
determinada classificação.  
d) Sinal de saída (y): é o valor final produzido. Como os neurônios podem ser 
encadeados em camada, tal valor pode ser utilizado por outros neurônios. 
Os neurônios precisam ser treinados com pesos apropriados para executarem 
suas funções de participação no reconhecimento de padrões, por exemplo. Para tal 
 
6 Resultado da soma de produtos dos valores das entradas pelos valores dos pesos sinápticos. 


66 
 
 
utiliza-se padrões de treinamento que permitem parametrizar os pesos sinápticos. 
Assim, um neurônio é capaz de exercer sua função de gerar respostas matemáticas 
em faixas que auxiliem no processo geral de execução da RNA. Outrossim, o 
funcionamento de uma RNA e mesmo seu treinamento dependem de sua arquitetura e 
topologia, os quais são assuntos da Seção 2.4.3. 
2.4.3 Arquiteturas de RNA 
A arquitetura de uma RNA define a forma como os seus diversos neurônios 
estão dispostos ou arranjados uns em relação aos outros. Esses arranjos são 
estruturados pela forma como os neurônios estão conectados, ou seja, por meio do 
direcionamento das conexões sinápticas dos neurônios nas camadas da RNA 
(HAYKIN, 2008; HEATON, 2015; RUSSELL; NORVIG, 2009; SILVA et al., 2010a). 
A topologia de uma RNA, considerando determinada arquitetura, pode ser 
definida como sendo as diferentes formas de composições estruturais que esta poderá 
assumir. Por exemplo, pode-se ter duas topologias pertencentes a uma mesma 
arquitetura, sendo que uma é composta por 10 neurônios e outra por 20 neurônios; ou 
ainda, uma constituída de neurônios com função de ativação logística, ao passo que os 
neurônios da outra assumem a tangente hiperbólica7 como função de ativação 
(HAYKIN, 2008; HEATON, 2015; RUSSELL; NORVIG, 2009; SILVA et al., 2010a). 
Considerando-se a disposição de seus neurônios, bem como as formas de 
interligação entre estes e a constituição de suas camadas, as principais arquiteturas de 
RNA são: redes feedforward (alimentação à frente) de camada simples, redes 
feedforward de camadas múltiplas, redes recorrentes e redes reticuladas (HAYKIN, 
2008; HEATON, 2015; RUSSELL; NORVIG, 2009; SILVA et al., 2010a). 
A arquitetura utilizada neste trabalho foi a de RNA feedforward de camadas 
múltiplas, especificamente a rede Perceptron de Múltiplas Camadas (PMC ou MLP – 
Multi Layer Perceptron). Tendeu-se à escolha desta arquitetura pois são consideradas 
muito versáteis, podendo ser aplicadas em vários tipos de problemas. Assim, possuem 
uma quantidade maior de experimentos e trabalhos disponíveis. A Figura 12 apresenta 
a estrutura de uma RNA de arquitetura MLP. 
Segundo SILVA et al. (2010a), RNA do tipo MLP possuem, no mínimo, uma 
camada intermediária de neurônios, entre a camada de entrada e saída, chamada de 
 
7 Informações detalhadas sobre as funções de ativação, bem como outras funções 
exemplificadas, podem ser encontradas no Apêndice A, bem como nas referências bibliográficas 
pertinentes, utilizadas neste trabalho. 


67 
 
 
camada escondida (hidden layer). Os neurônios das camadas estão conectados 
apenas aos neurônios subsequentes, indicando que sua arquitetura é do tipo 
feedforward. Seu treinamento segue os algoritmos supervisionados (SILVA et al., 
2010a).  
Ainda, segundo SILVA et al. (2010a), as RNA MLP são consideradas muito 
versáteis em relação à sua aplicabilidade, sendo utilizadas em diversos tipos de 
problemas relacionadas com as mais diferentes áreas do conhecimento, como 
reconhecimento de padrões, previsão de séries temporais e otimização de sistemas. 
Figura 12 - Estrutura de uma RNA Multi Layer Perceptron 
 
Fonte: SILVA et al., 2010a. 
A título de informação, uma vez que o modelo computacional NeuroPON prevê, 
como prova de conceito, a utilização apenas de RNNA MLP, a Tabela 1 apresenta 
outras arquiteturas de RNA, além da MLP. 
Tabela 1 - Arquiteturas de RNA 
Denominação 
Representação 
Exemplos de Aplicação 
Perceptron de Múltiplas 
Camadas (Multi Layer 
Perceptron) 
 
Reconhecimento de padrões, previsão de 
séries temporais e otimização de sistemas 
Feedforward de camada 
simples 
 
Problemas envolvendo classificação de 
padrões e filtragem linear. 


68 
 
 
Recorrente ou Realimentada 
 
Sistemas variantes em relação ao tempo, 
como previsão de séries temporais, 
otimização e identificação de sistemas, 
controle de processos. 
Reticulada 
 
Problemas de agrupamento (clustering), 
reconhecimento de padrões, otimização 
de sistemas, grafos, etc. 
Fonte: Autoria Própria 
Enfim, para que uma RNA possa generalizar o funcionamento de um sistema, 
esta precisa ser treinada por meio de algoritmos. Isto se dá a fim de que a RNA aprenda 
o comportamento de determinado sistema. A próxima seção descreve tal procedimento, 
e apresenta um exemplo prático de treinamento. 
2.4.4 Processo de aprendizado e treinamento 
Segundo Haykin (2008), a principal característica das RNA está na sua 
capacidade de aprender e generalizar sistemas. Assim, a partir de amostras (padrões) 
que exprimem o comportamento de determinado sistema, uma RNA aprende como o 
sistema funciona e generaliza soluções, podendo produzir uma saída próxima àquela 
esperada, a partir de dados de entrada (HAYKIN, 2008).  
Neste contexto, o treinamento de uma arquitetura específica consiste na 
aplicação de um conjunto de passos ordenados (algoritmos) para ajustar os pesos 
sinápticos e os limiares de ativação de seus neurônios, fazendo com que as respostas 
da RNA estejam próximas dos valores desejados. Uma vez treinada, os valores de 
pesos sinápticos e limiares de ativação são armazenados para que a RNA possa gerar 
a função esperada (SILVA et al., 2010a). 
Para que a RNA seja ajustada, os algoritmos de treinamento utilizam dados 
relativos ao problema a ser generalizado. Ainda, a fim de validar seu treinamento, testes 
devem ser efetuados na RNA treinada. Assim, o conjunto total das amostras disponíveis 
para um determinado problema é dividido em um subconjunto para realizar o 
treinamento e outro para realizar o teste. O percentual de cada subconjunto depende 
do problema e dos resultados parciais obtidos em cada processo, mas a divisão padrão 
define de 60% a 90% para o conjunto de treinamento (os dados utilizados para o 
aprendizado da rede) e de 40% a 10% para os testes (SILVA et al., 2010a). 


69 
 
 
O treinamento utilizado na concepção do modelo computacional NeuroPON foi 
do tipo supervisionado, que implica na existência de um supervisor (ou ‘professor’ 
externo) o qual é responsável por estimular as entradas da RNA por meio de padrões 
de entrada, observar a saída calculada pela mesma e compará-la com a saída 
desejada. Para cada padrão de entrada, a RNA tem sua saída corrente comparada com 
a saída desejada pelo supervisor, que fornece informações sobre a direção de ajuste 
dos pesos sinápticos entre as camadas da RNA. A minimização de tal diferença é feita 
a cada etapa de treinamento, realizando pequenos ajustes nos pesos, para que estes 
busquem uma solução possível (se houver) (HEATON, 2015; RUSSELL; NORVIG, 
2009; SILVA et al., 2010a). 
Um termo pertinente ao treinamento de uma RNA denomina-se época (ou 
round), que é o processo de execução dos passos de treinamento sobre todas as 
amostras de um padrão utilizado. Tais operações servem para o ajuste dos pesos 
sinápticos e limiares de uma RNA. Outrossim, a aplicação de um passo de treinamento 
para cada amostra denomina-se iteração de treinamento (RUSSEL; NORVIG, 2009). 
A título de exemplo, o treinamento supervisionado por retro-propagação 
(Backpropagation – BP), utilizado na elaboração do modelo computacional NeuroPON, 
é aqui demonstrado. A escolha deste se deu por ser um método amplamente utilizado 
em sistemas de RNA, mesmo em aplicações recentes. Assim, ampla literatura de testes 
e exemplos está disponível para pesquisa (KALBANDE; BAVASKAR, 2013; LI; LI, 2012; 
PARKER; KHAN, 2016; RAIZER et al., 2010; RIOS, 2013; WANG; LIMARE, 2015). 
Também, devido a tal fator, tal treinamento foi utilizado nos estudos e testes para o 
desenvolvimento deste trabalho.  
A primeira fase do método é denominada propagação “a frente” (forward 
propagation), onde os sinais de entrada são inseridos na RNA e propagados camada a 
camada até a produção das saídas. Assim, tal fase busca obter as respostas da RNA 
considerando valores atuais de pesos sinápticos e limiares de seus neurônios. Ao final 
desta etapa, as respostas produzidas são comparadas com as respostas desejadas 
(aprendizado supervisionado), gerando os desvios (erros) por meio da subtração das 
saídas desejadas pelas produzidas no processamento da RNA (HEATON, 2015; SILVA 
et al., 2010a).  
A segunda fase do método, denominada retro-propagação, usa o erro obtido 
previamente para ajustar os pesos sinápticos e limiares da RNA. Em arquiteturas que 
usam camadas escondidas como na MLP, não há acesso direto aos valores dos 
neurônios que pertencem a tais camadas, assim como os valores requeridos por tais 


70 
 
 
neurônios são desconhecidos. Neste caso, o ajuste de seus valores é baseado nos 
pesos sinápticos ajustados nos neurônios da camada de saída da RNA (SILVA et al., 
2010). A equação (3) é um exemplo de modelo de ajuste para o algoritmo BP. 
 

() = 
() +  .
() .
(−1) 
(3) 
Na equação de ajuste (3), 
() é o vetor da camada L, neurônio ;  é a 
constante de ajuste de aprendizado (valor positivo entre 0 e 1); 
() é o valor do 
gradiente local da camada L do -ésimo neurônio; e 
(−1) é o vetor que contém os 
valores das saídas da camada anterior, em relação ao -ésimo neurônio. A equação é 
aplicada a todas as ligações entre as camadas (em ordem – saída com escondida, 
escondida(s), escondida com entrada) até que os pesos estejam ajustados. 
Isto dito, deve-se definir os valores das entradas ponderadas pelos pesos (vetor 
Ij(L)) e as saídas de cada um dos neurônios (vetor Yj(L)), definidas nas equações (4) e 
(5). 
 

() =  
() ∙	

=0
 
(4) 
 

() = (
()) 
 
(5) 
A equação (4) efetua a soma ponderada de todos os pesos sinápticos 
() 
pelas entradas da rede na camada , e este resultado é aplicado à função de ativação, 
conforme a equação (5), que apresenta a saída de cada neurônio  da camada . Este 
processo é repetido em todas as camadas existentes. 
A próxima etapa do algoritmo de treinamento por BP é a definição da função 
que representa o erro de aproximação. Tal função retorna o desvio entre as respostas 
produzidas pela RNA em relação aos respectivos valores desejados (aprendizado 
supervisionado). Considerando-se, portanto, a k-ésima amostra de treinamento, utiliza-
se a função de erro quadrático, expressa na equação (6). 
 
!(") = 1
2 ($(%) −
(&)(%))
2

'
(
 
(6) 
Na equação (6), 
(&)(%) é o valor produzido pelo -ésimo neurônio de saída da 
rede na %-ésima amostra de treinamento, e $(%) é o valor desejado nesta saída 
(treinamento supervisionado). Esta é a representação do erro local ou erro em cada 


71 
 
 
amostra de treinamento, sendo que é necessário calcular o erro quadrático médio, 
definido na equação (7), onde ) é a quantidade de amostras de treinamento utilizadas. 
 
!* = 1
)  !(%)
+
"
 
 
(7) 
 
A partir do cálculo do erro quadrático médio, pode-se efetuar o ajuste de pesos 
das camadas, visando minimizar o erro entre a saída produzida pela RNA em relação 
à respectiva saída desejada. Para a equação de ajuste, é empregada a definição do 
método de Gradiente Descendente ou a Regra Delta. Neste contexto, a equação (8) 
define o gradiente local em relação ao -ésimo neurônio da camada de saída. 
 

(3) = ($ −
(3)) ∙′(
(3)) 
(8) 
Na equação (8) ′(∙) denota a derivada de primeira ordem da função de 
ativação considerada. Assim, o ajuste da matriz de pesos da camada de saída é 
efetuado pela equação (3) com L = 3, pois a camada em questão é a camada de saída 
(3ª camada). 
Esse processo repete-se pelas camadas intermediárias (escondidas), até o 
ajuste dos pesos sinápticos que fazem a ligação entre as entradas e a primeira camada 
escondida da RNA. Ao final do ajuste dos pesos, repete-se o passo forward para ajustar 
a saída da RNA, obtém-se o erro quadrático médio (conforme equação (7)) e atualiza-
se a época (aumenta seu valor em 1 unidade, pois passa à próxima época). O 
treinamento é finalizado quando o algoritmo atingir o ponto de parada, que pode ser 
uma quantidade determinada de épocas, um valor de erro mínimo atingido ou outra 
condição definida pelo desenvolvedor.  
SILVA et al. (2010a) desenvolvem o exemplo por meio de um pseudocódigo, 
demonstrado na Figura 13. O critério de parada deste é estipulado em função do erro 
quadrático médio, levando-se em consideração todas as amostras de treinamento 
disponíveis. Assim, o algoritmo converge quando o erro quadrático médio entre duas 
épocas sucessivas for suficientemente pequeno. 
Após o processo de treinamento, a variável época conterá a quantidade de 
épocas necessárias para o treinamento. Em tempo, época refere-se à quantidade de 
apresentações de amostras do conjunto de treinamento ao algoritmo, até que se 
considere a RNA treinada, ou seja, até que seus pesos sinápticos fossem considerados 
ajustados a fim de generalizar o sistema proposto, sobre qualquer entrada. Isso posto, 


72 
 
 
pode-se utilizar a RNA para estimar as saídas do sistema que foi mapeado frente às 
novas amostras que serão apresentadas em suas entradas. Silva et al. (2010a) 
apresentam um pseudocódigo, descrito na Figura 14, que viabiliza a fase de operação 
da RNA. 
Figura 13 - Algoritmo de treinamento de uma RNA MLP utilizando o método BP 
 
Fonte: SILVA et al., 2010a. 
SILVA et al. (2010a) destacam também que os ajustes das matrizes de pesos 
sinápticos são realizados somente na fase de treinamento, onde a fase backward é 
executada para efetuar correções sinápticas necessárias. Na fase de operação não há 
ajustes nos pesos, ou seja, somente a fase forward é executada com o objetivo de gerar 
as saídas da RNA. 
 
 
 
 


73 
 
 
Figura 14 - Algoritmo de operação de uma RNA MLP 
 
Fonte: SILVA et al., 2010 
O treinamento por BP é muito utilizado desde sua concepção até os dias atuais, 
pois é prático e de fácil implementação em qualquer linguagem de programação, bem 
como considerado eficaz. Não obstante, para que o treinamento por BP seja bem 
sucedido, Fahlman (1988) e Heaton (2015) apontam que uma “afinação” de três 
parâmetros é imprescindível: a taxa de aprendizagem, o termo de momentum, e faixa 
inicial dos pesos aleatórios. Tais parâmetros podem ser definidos como: 
 Taxa de Aprendizagem (learning rate): a taxa de aprendizagem dimensiona 
o gradiente e controla a velocidade de aprendizado. Contudo, taxas muito 
altas fazem com que a RNA não consiga convergir a um valor baixo de erro. 
Normalmente este valor deve ficar na faixa entre 0 e 1.  
 Termo de Impulso (momentum): assim como a taxa de aprendizado, também 
é um fator de escala. Este termo determina a porcentagem de alteração do 
peso da iteração anterior que deve ser aplicado à iteração atual. Tal técnica 
pode ser utilizada para escapar dos mínimos locais, que são pontos baixos 
locais e não mínimos globais. O algoritmo BP tem uma tendência a “ficar 
preso” em tais pontos, e não encontrar o caminho de volta à busca do mínimo 
erro global. 
 Valoração dos pesos: é importante que, a cada treinamento, os pesos iniciais 
possuam valores diferentes dos anteriores, sejam aleatórios e muito 
próximos de zero (0). Tais fatores são importantes para um bom treinamento 
quando se usa o método BP, pois  a otimização pelo método do gradiente 
descendente é utilizada neste método. Portanto, assim como o termo de 


74 
 
 
momentum, a aleatoriedade diminui também a chance de que o algoritmo 
"fique preso" em um mínimo local, aumentando assim as chances de se 
alcançar melhores valores ao final do treinamento.  
Os algoritmos de treinamento, testes e operação de RNA demonstrados nesta 
seção podem ser implementados por meio de diversas linguagens de programação. 
Existe ainda a possibilidade do uso de simuladores, bem como linguagens 
especificamente criadas para a especificação de RNA.  
2.4.5 Implementação de RNA em Software 
As RNA podem ser implementadas utilizando-se linguagens de programação 
de propósito geral do PI, como C, C++ e Java, ou ainda por meio da utilização de 
aplicativos e plataformas especializados para desenvolvimento destas. Algumas 
linguagens de programação possuem bibliotecas e pacotes contendo funções e 
estruturas de dados especializados para a implementação de RNA. A título de exemplo, 
a linguagem Python do PI possui soluções registradas para o desenvolvimento de RNA. 
Dentre estas, pode-se citar as bibliotecas NeuroLab (JOSHI, 2017) e FANN (Fast 
Artificial Neural Network Library) (ATABAY, 2016), que contêm algoritmos de 
treinamento, estruturas de dados, modelos básicos de RNA e um Framework para criar 
e explorar outras RNA Framework. Ainda, alguns aplicativos e plataformas utilizam 
linguagens específicas na implementação de RNA. Na sua maioria, tais linguagens são 
especificações de RNA, feitas em sintaxe própria ou utilizando padrão de linguagens 
de marcação, principalmente eXtensible Markup Language (XML). Neste âmbito, 
apresenta-se aqui a linguagem para especificação ViNNSL, utilizada no presente 
trabalho. 
Criada por Beran et al. (2008), a linguagem Vienna Neural Network 
Speciﬁcation Language (ViNNSL) é uma linguagem aberta, baseada em XML, que 
permite a interação dinâmica de clientes e recursos de serviço, independentemente de 
quaisquer detalhes de implementação (BERAN et al., 2008; SCHIKUTA et al., 2015). 
A linguagem ViNNSL visa servir especificamente o domínio das RNA, 
fornecendo cinco esquemas para gerenciar a interação entre um cliente e um provedor 
de serviços de RNA. Usando estes esquemas é possível descrever as capacidades de 
serviço, a semântica, as funções e os parâmetros em uma maneira que possa ser 
interpretada pelo cliente (BERAN et al., 2008). A Figura 15 demonstra o esquema 


75 
 
 
chamado Evolução Dinamica de Serviço (Dynamic Service Evolution – DSE) utilizada 
pela linguagem. 
Na Figura 15 todo o processo DSE é ilustrado com um cliente e um serviço que 
está fornecendo a implementação de um paradigma de RNA. Assim, o fluxo deve ser 
utilizado quando a linguagem ViNNSL é aplicada aos consumidores de serviços que 
aceitem tal linguagem. Para o bom funcionamento do fluxo, cinco esquemas devem ser 
utilizados para dar suporte à ViNNSL: descrição, definição, dados, instância e resultado.  
Figura 15 - Fluxo de trabalho DSE da linguagem ViNNSL 
 
Fonte: Adaptado de Beran et al., 2008. 
Como exemplo, o esquema de definição (definition) é apresentado. Tal 
esquema é definido pelo usuário, e representa a especificação formal, baseada em 
XML, de uma nova RNA que deve ser treinada. O Código 3 apresenta um arquivo XML 
Definition de uma RNA com treinamento BP, utilizando o exemplo do OU Exclusivo 
(eXclusive OR – XOR). 
Código 3 - Arquivo XML contendo o esquema de definição (definition schema) para uma RNA a ser treinada 
com o algoritmo de treinamento por BP, com o exemplo do XOR (Adaptado de Beran et al., 2008) 
01 
02 
03 
04 
05 
06 
07 
08 
09 
10 
<definition xmlns="http://www.pri.univie.ac.at/../vinnsl"> 
  <identifier>00000000000000000000000000000007</identifier> 
  <structure>  
    <input> 
      <id>Input1</id> 
      <dimension>2</dimension> 
      <size>1</size> 
    </input>  
    <hidden>  
      <id>Hidden1</id> 


76 
 
 
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
      <dimension>5</dimension> 
      <size>1</size> 
    </hidden> 
    <output> 
      <id>Output1</id> 
      <dimension>1</dimension> 
      <size>1</size> 
    </output> 
    <connections> ... </connections>  
  </structure>  
  <parameters>  
    <valueparameter>  
      <name>lrate</name> 
      <label>Learning Rate</label> 
      <value>0.3</value> 
    </valueparameter> 
    <boolparameter> 
      <name>bias</name> 
      <label>Bias</label> 
      <value>true</value> 
    </boolparameter> 
    <comboparameter> 
        <name>afunc</name> 
        <label>Activation Function</label> 
        <value>sigmoid</value> 
    </comboparameter> 
  </parameters>  
</definition> 
Fonte: Autoria Própria 
Assim que definidos, os esquemas podem ser utilizados em simuladores aptos 
a realizar o processamento de RNA a partir da linguagem ViNNSL. A fim de exemplificar 
sua utilização, o artigo de Beran et al. (2008) apresenta a linguagem ViNNSL, bem 
como sua aplicação em um sistema baseado na linguagem Java para simulação de 
RNA distribuídas (BERAN et al., 2008; SCHIKUTA et al., 2015). Ainda em outro 
exemplo, Nussbaum; Schikuta (2018) utilizam a linguagem ViNNSL em um sistema 
para a geração de RNA por meio de arquiteturas de micro serviço baseadas em Java, 
utilizando RESTful Web Services (NUSSBAUM; SCHIKUTA, 2018). 
2.4.6 Considerações sobre Implementação de RNA em software 
As RNA podem ser implementadas utilizando-se linguagens de programação 
de propósito geral do PI, como C, C++ e Java, ou ainda por meio da utilização de 
aplicativos e plataformas especializados para desenvolvimento destas. Algumas 
linguagens de programação possuem bibliotecas e pacotes contendo funções e 
estruturas de dados especializados para a implementação de RNA (Aisa et al., 2008; 
Atabay, 2016; Joshi, 2017; Zell, 2014). As aplicações e modelos considerados incluem 


77 
 
 
aplicativos com interfaces gráficas, frameworks, bibliotecas de linguagens de 
programação e padrões XML para descrição de RNA. De acordo com a Tabela 2, três 
(3) dos modelos estudados permitem especificar teste e treinamento de uma RNA, além 
do tipo de entrada de treinamento. 
A implementação tida como “tradicional” de RNA em software faz a utilização, 
geralmente, de estruturas de dados matriciais no âmbito do PI. Neste contexto, a 
representação das entradas, neurônios de camadas escondidas e de saída, bem como 
dos pesos sinápticos, é feita por meio de matrizes. Exemplos desta prática são os 
projetos Encog (HEATON, 2008), Joone (MARRONE, 2004), FANN (ATABY, 2016), 
OpenNN (LOPEZ, 2014), bem como os exemplos de Costa e Ludwig Junior (2007) e 
McCaffrey (2015). Ainda, implementações (mesmo que algorítmicas) de RNA em livros 
consagrados como Haykin (2008) e Russel e Norvig (2009) seguem o mesmo padrão 
imperativo. Em tempo, tais aplicações em PI por vezes seguem a forma procedimental 
e outras a forma OO. 
Porém, conforme mencionado anteriormente, para que o processamento 
neuronal em RNA fosse mais fidedigno ao de uma RNN, este deveria ser executado de 
forma paralela. Neste contexto, é sabido que implementações feitas em PI tendem a 
ser naturalmente acopladas, o que afeta a distribuição e, consequentemente, a 
possibilidade de paralelização de tais estruturas. Ainda, o uso de estruturas de dados 
matriciais demanda códigos-fonte que envolvam laços de repetição, tornando o código 
ainda mais acoplado, dificultando sua distribuição. 
Outrossim, Apêndice D apresenta alguns exemplos de linguagens de 
especificação de RNA. Tais linguagens permitem especificar uma RNA de forma 
declarativa. Entretanto, ressalta-se que o código gerado, a ser executado, a partir da 
expressão declarativa volta a ser imperativo nos moldes já explicados. A Tabela 2 
apresenta um comparativo entre as linguagens declarativas baseadas em XML. 
Tabela 2 - Comparação entre linguagens declarativas, baseadas em XML, para definição de RNA  
 
ViNNSL 
iXCSL 
NXML 
NNDef 
Tecnologias 
XML Schema 
XML Schema 
XML Schema 
DTD 
Tipo de 
Neurônios 
Artificial, Bias 
Artificial, Bias 
Artificial, Bias 
Artificial, Bias 
Criação 
Sim 
Sim 
Sim 
Sim 
Treinamento 
Sim 
Não 
Sim 
Sim 
Avaliação 
Sim 
Não 
Sim 
Sim 
Tipo de Entrada 
Numérico (double), 
binários 
Não especificado 
Números, 
Caracteres, 
Imagens 
Numérico (real) 


78 
 
 
Tipo de Saídas 
Tabelas, arquivos, 
diagramas 2-D, 
mensagens 
Não especificado 
Números e 
Caracteres 
Numérico (real) 
Sistema 
N2Grid 
Não especificado 
Brainet .Net 
Java 
Paradigma 
Grid/PI 
Não especificado 
PI 
PI 
Fonte: Adaptado de University of Vienna, 2008. 
Neste contexto, é importante ressaltar que, mesmo apresentando a facilidade 
de programação por serem declarativas, a aplicação resultante é executada segundo 
os conceitos do PI, estando sujeita às mesmas deficiências, que levam à geração de 
código acoplado de difícil distribuição, anteriormente apontadas. 
Isto posto, em relevantes trabalhos de pesquisa e no presente universo de 
discurso, não se encontrou uma aplicação que oferecesse a praticidade da 
programação declarativa para a descrição de RNA e que resultasse em um código 
desacoplado e otimizado para arquiteturas von Neumann, bem como paralelizável para 
dispositivos FPGA. Assim, a especificação e elaboração de um modelo que permita a 
construção de RNA utilizando os conceitos do PON torna-se relevante. 
A Seção 2.4.7 apresenta uma revisão quanto aos trabalhos relacionados à 
implementação de RNA em hardware, pois o modelo computacional NeuroPON 
proposto visa a geração de código para execução direta em dispositivos FPGA. 
2.4.7 Implementação de RNA em Hardware (RNH) 
Mesmo que muitas aplicações comerciais existentes para RNA sejam muitas 
vezes desenvolvidas em software, aplicações específicas, como compressão de vídeo 
streaming, exigem características distintas não atingidas por processadores de uso 
genérico. Segundo Abrol e Mahajan (2015), mesmo que a maioria das implementações 
de RNA sejam feitas em software, as implementações em hardware vêm tornando-se 
importantes no meio científico, mesmo que mais difíceis de se desenvolver e 
consumindo maior tempo de desenvolvimento. Algumas características, apontadas por 
Misra e Saha (2010) são: grande volume de processamento adaptativo em tempo real, 
consumo de energia eficiente, e ‘verdadeira’ capacidade de processamento paralelo 
(MISRA; SAHA, 2010). 
Melhoramentos em computadores digitais (i.e., circuitos dedicados de 
processamento específico e processadores multicore) e técnicas de programação (i.e., 
POO, POE e APIs) têm contribuído para a construção de RNA de forma efetiva 
(BAPTISTA et al., 2013; SCHUMAN et al., 2017). Porém, algoritmos que implementem 
RNA executando em máquinas sequenciais (baseadas na arquitetura de von Neumann) 


79 
 
 
não alcançam seu potencial teórico e, supostamente inerente, de execução paralela 
(LAKSHMI; SUBADRA, 2013; PETHICK ET AL., 2003). Por fim, os paradigmas atuais 
não contribuem para execução eficiente, nem mesmo em monoprocessamento, tão 
pouco na questão de geração de código paralelo (BORKAR; CHIEN, 2011; KAISLER, 
2005; LINHARES, 2015). 
Dispositivos de hardware projetados especificamente para executar tanto 
arquiteturas de RNA quanto algoritmos de aprendizado associados a estas aproveitam, 
de certa forma, o paralelismo inerente ao processamento neural. Neste contexto, Misra 
e Saha (2010) apontam três vantagens que hardware especializado em processamento 
de RNA possuem frente a processadores de uso comum: 
 Velocidade: hardware especializado oferece poder computacional elevado a 
um preço limitado, alcançando várias ordens de aceleração. Tal 
característica é importante especialmente em RNA onde o paralelismo e a 
computação distribuída estão inerentemente envolvidos. 
 Custo: por meio da redução da quantidade de componentes ou mesmo 
requisitos energéticos, uma implementação de hardware pode reduzir 
custos. Em aplicações de alto volume, como reconhecimento de padrões em 
tempo real (para sistemas ubíquos por exemplo), que são muito sensíveis a 
custos, tal característica é fundamental 
 Degradação progressiva: sistemas sequenciais com processadores únicos 
ou multicores carecem de mecanismos efetivos de tolerância a falhas. 
Portanto, aplicações baseadas neste tipo de arquitetura podem parar devido 
a falhas de operação (fail-stop operations). Arquiteturas paralelas e 
distribuídas, ao contrário, permitem que as aplicações continuem 
funcionando com um desempenho ligeiramente reduzido (degradação 
progressiva) mesmo na presença de falhas em alguns componentes. Para 
RNA que requerem alta disponibilidade (safety-critical), a tolerância a falhas 
é de extrema importância e, a este respeito, implementações de hardware 
paralelas oferecem vantagens consideráveis. 
 Tais implementações recebem o nome de Redes Neurais em Hardware (RNH 
ou HNN – Hardware Neural Networks) (MISRA; SAHA, 2010). Neste contexto, a 
presente seção aborda por meio de suas subseções o desenvolvimento de RNH em 
dispositivos digitais, especialmente os FPGA. 


80 
 
 
2.4.7.1 Tecnologias para Implementação de RNH 
 A implementação de RNH pode ser realizada utilizando diversas tecnologias. 
Neste contexto, o presente trabalho restringiu a busca por implementações em 
neurochips, que são implementações específicas em pastilhas de silício (microchips). 
Neste âmbito, podem ser utilizadas as tecnologias de neurochips digitais, analógicos e 
híbridos, bem como implementações utilizando FPGA, RAM e memórias associativas. 
Segundo Misra; Saha (2010) RNH contêm um bloco de ativação responsável 
por executar a soma de produtos, ou seja, a multiplicação das entradas pelos pesos 
sinápticos da RNA e a sua soma. Outros blocos envolvendo o estado de um neurônio, 
pesos sinápticos e funções de ativação podem estar ou não dentro do chip, podendo 
tais funções serem executadas por computadores hospedeiros. 
Implementações utilizando circuitos analógicos, ou Neurochips analógicos, 
contém resistores, capacitores e EEPROMs de porta flutuante, podendo ainda utilizar 
circuitos MOSFET (Metal Oxide Semiconductor Field Effect Transistor) e amplificadores 
com saturação. Porém, Kim et al. (2012) afirma que tais circuitos são difíceis de 
reconfigurar e que o uso de capacitores com alto custo de área no chip para manter os 
pesos sinápticos dificulta a integração em larga escala de neurônios (KIM et al., 2012; 
MISRA; SAHA, 2010). Exemplos de trabalhos com RNHs analógicas estão em Mitra et 
al. (2009), Van Schaik (2001), e Wijekoon e Dudek (2008), porém tal assunto não será 
aprofundado, pois esta classe de RNH está fora do escopo do presente trabalho. 
Neurochips digitais podem ser construídos utilizando diversas técnicas. Além 
de dispositivos FPGA (tecnologia de hardware a ser utilizada neste trabalho) outras 
tecnologias de hardware digital podem ser utilizadas para a implementação de RNHs, 
como Arduino (ARDUINOAG, 2017) utilizado no trabalho de Parker; Khan (2016) e 
Memristor utilizado nos trabalhos de Forssell (2014) e de Liu et al. (2017). 
Recentemente as Unidades de Processamento Gráfico (GPU - Graphic 
Processing Unit) despertaram grande interesse no desenvolvimento de RNA, devido ao 
alta performance no processamento de aplicações altamente paralelas. As GPU 
diferem das tradicionais CPU justamente na especialização de circuitos, pois seu 
processamento é focado em circuitos aritméticos, especialmente em Unidades Lógicas 
e Aritméticas (ALU – Arithmetic Logical Units) e Unidades de Ponto Flutuante (FPU – 
Floating Point Unit), caracterizando assim sua especialidade em operações que 
envolvem muitos cálculos (NVIDIA, 2017; SANDERS; KANDROT, 2011). Neste âmbito, 
as GPU são muito utilizadas para aceleração e paralelização do processamento de 


81 
 
 
RNA. Trabalhos como os de  Huqqani et al. (2013), Nguyen et al. (2015), Raizer et al. 
(2010), Veselý et al. (2010) e Yazdanbakhsh et al. (2015) são exemplos da aplicação 
de RNA em GPU. 
A presente seção objetivou listar alguns exemplos de aplicações de RNHs que 
não são implementadas em hardware reconfigurável, sendo este assunto da seção 
2.4.7.2. Não houve aprofundamento em tais tecnologias, pois estas não fazem parte do 
escopo do presente trabalho.  
2.4.7.2 RNH em Hardware Reconfigurável 
Misra; Saha (2010) apontam que dispositivos FPGA fornecem uma 
característica programável eficaz para a implementação de RNHs, pois permitem 
diferentes projetos para comparação e avaliação em curto período de tempo (MISRA; 
SAHA, 2010). Outras vantagens da utilização de FPGA são características como baixo 
consumo de energia e grande capacidade de processamento (tanto serial quanto 
paralelo) (DEOTALE; DOLE, 2014; GIRAU, 2006; HEMSOTH, 2017; MOHAMAD et al., 
2012). Não obstante, os desenvolvedores devem conhecer técnicas de programação 
em baixo nível, ou ainda as linguagens de descrição de hardware, a fim de realizar a 
programação de tais dispositivos.  
De fato, linguagens como C e C++ não são adequadas para descrição de 
hardware, devido às particularidades necessárias à programação de tais dispositivos 
de forma direta (TISAN; CHIN, 2015; WINDH et al., 2015). A aplicabilidade de RNH 
implementadas em FPGA se dá em diversas áreas de conhecimento, por exemplo: (a) 
Krips et al. (2002) apresentam uma implementação em dispositivo FPGA de uma RNA 
destinada a projetar um sistema de detecção e rastreamento de mãos, em tempo real, 
aplicado a imagens de vídeo; e (b) Fan Yang; Paindavoine (2003) apresentam um 
hardware baseado em dispositivo FPGA implementado em um sistema embarcado, 
com a finalidade de rastrear rostos e verificar identidades em filmes (sequências de 
vídeo),  com taxas de acerto de 92% de sucesso (MISRA; SAHA, 2010). 
Além de sistemas de segurança, o reconhecimento de gestos visando a 
comunicação e interação natural com a máquina, sem a interferência de outros 
dispositivos (como controles remotos), é muito utilizado em dispositivos eletrônicos 
inteligentes (smart devices). Neste contexto, Sridevi et al. (2017) propõem a utilização 
de uma RNH implementada em dispositivos FPGA para o reconhecimento de gestos, 
pois afirmam que tais dispositivos precisam de menos espaço, possuindo menor 


82 
 
 
consumo de energia e menor peso em comparação a computadores pessoais, 
geralmente utilizados, frente à necessidade de processamento em tempo real que tais 
sistemas demandam.  
Em aplicações de neurociências, Rice et al. (2009) relatam que uma 
implementação, baseada em dispositivos FPGA, de um modelo cognitivo inspirado em 
neocórtex, pode fornecer um ganho médio de taxa de transferência de 75 vezes sobre 
a implementação em software em um supercomputador Cray XD1 completo. Neste 
estudo foi utilizado o modelo hierárquico Bayesiano de RNA, baseado no neocórtex 
desenvolvido por George; Hawkins (2005). Sua implementação acelerada de hardware 
no Cray XD1 usa o dispositivo FPGA Xilinx Virtex II Pro com memória SRAM off-chip, 
sendo que a implementação em software usa 5 processadores Opteron Dual Core de 
2,0 GHz. Em outro exemplo, Girau; Torres-Huitzil (2007) mapearam o modelo neuronal 
LEGION (Local Excitatory Global Inhibitory Oscillator Network), de RNA do tipo spiking, 
para segmentação de imagens, também implementado em um dispositivo FPGA 
(MISRA; SAHA, 2010). 
Outra importante questão de projeto de RNH em dispositivos FPGA, destacada 
por Misra; Saha (2010), é a operação de multiplicação, que utiliza grande quantidade 
de bits. Como cada conexão sináptica requer um multiplicador único, tal quantidade 
cresce na taxa do quadrado do número de neurônios. Neste âmbito, fabricantes de 
dispositivos FPGA tem produzido dispositivos com centenas de multiplicadores 
dedicados, bem como soluções voltadas para Aprendizagem de Máquina, como os 
dispositivos Virtex UltraScale+, Virtex-7 e Virtex Plus 2, da fabricante Xilinx (FREUND 
et al., 2016, 2017; FU et al., 2017; JENKINS, 2003).  
Os resultados dos estudos acima apontam que dispositivos FPGA são uma boa 
escolha para aplicações em RNA. Além de características da própria tecnologia como 
a reconfiguração em campo e custo relativamente baixo para prototipação, os 
fabricantes têm investido em dispositivos cada vez mais rápidos e robustos, a fim de 
suportar aplicações com grande demanda de processamento e dados. 
Ainda na implementação de RNH em FPGA, outros trabalhos corroboram a 
eficiência e abrangência desta linha de pesquisas. Abrol e Mahajan (2015), Ali e 
Mohammed (2010), Bahoura e Park (2011), Dondon et al. (2014), Gomperts et al. 
(2011), Guo et al. (2012), Nedjah et al. (2012) e Rezvani et al. (2012) demonstram 
diversas técnicas de implementação e aplicação, bem como apresentam comparativos 
entre os resultados obtidos com a execução de RNH em dispositivos FPGA com outro 
hardware e software. Tais trabalhos são abordados na Seção 2.4.7.3. 


83 
 
 
2.4.7.3 Trabalhos correlatos 
A presente seção visa apresentar abordagens correlatas ao presente trabalho, 
para que se possa compreender o estado da arte e da técnica, no âmbito da concepção 
de RNA em hardware. Neste contexto, elaborou-se apenas um resumo de cada 
abordagem, não havendo contraposições às características desejáveis no modelo 
computacional NeuroPON aqui proposto. Uma comparação entre tais trabalhos e o 
NeuroPON, segundo determinadas características, é apresentada na Seção 2.4.8. 
Rezvani et al. (2012) simularam uma RNA MLP usando código VHDL 
sintetizável. Neste modelo, o usuário pode determinar a quantidade de camadas, bem 
como a quantidade de neurônios em cada camada. A fase de treinamento é online e 
feita no hardware, bem como a fase de operação. Outra característica importante é que 
os pesos podem ser declarados na forma de ponto flutuante. Nos experimentos, um 
problema de reconhecimento de padrões (dígitos de 0 a 9) foi utilizado, sendo que 
variou-se parâmetros como a quantidade de camadas e de neurônios em cada camada, 
bem como a quantidade de épocas em cada um dos testes. Os resultados obtidos 
demonstraram que o projeto utilizando dispositivos FPGA é eficaz pois, em comparação 
com o mesmo sistema desenvolvido em software, a execução foi mais rápida, e os 
valores das taxas de erros dentro da mesma faixa (REZVANI et al., 2012). 
Também utilizando RNA MLP com treinamento em BP, Gomperts et al. (2011) 
descrevem uma RNA parametrizável de propósito geral, e afirmam que tal modelo 
explora a área do dispositivo FPGA de uma forma mais eficiente, com prototipação e 
teste rápidos, maximizando o desempenho frente a outras implementações em 
hardware. Quanto à sua confiabilidade, experimentos demonstram que o sistema atinge 
taxas de erro similares à RNA desenvolvida utilizando MATLAB (GOMPERTS et al., 
2011). 
O trabalho de Abrol e Mahajan (2015) apresentou o desenvolvimento de um 
neurônio que pode ser usado em qualquer RNA, utilizando uma função de ativação 
sigmoidal. Utilizando VHDL, o projeto concluiu o desenvolvimento de um componente 
que, a partir de ferramentas disponíveis em editores de esquemático, pode-se utilizar 
tal neurônio. Assim, o projetista pode utilizar quantos neurônios forem necessários ao 
seu projeto, por meio da técnica de arrastar-soltar a partir de uma biblioteca de 
componentes. 
Ali e Mohammed (2010) também apresentam o desenvolvimento de uma RNA 
utilizando FPGA, utilizando a arquitetura MLP feedforward como exemplo. O 


84 
 
 
desenvolvimento de um neurônio foi efetuado utilizando-se a linguagem VHDL. A 
função de ativação sigmoidal foi apresentada, bem como uma simulação de 
encadeamento de neurônios, a fim de produzir as camadas em uma RNA. A Figura 16 
apresenta um esquema demonstrando a RNA implementada. 
Figura 16 - Esquema demonstrando a RNA implementada em hardware 
 
Fonte: Adaptado e traduzido de Ali e Mohammed, 2010. 
Na Figura 16 encontra-se a RNA montada com três neurônios na camada 
intermediária e um neurônio na camada de saída. Assim, o neurônio foi implementado 
por meio de um multiplicador, um acumulador e um bloco que executa a função de 
ativação sigmoidal. A estrutura da RNA montada conta ainda com um circuito 
controlador e um multiplexador (MUX) a fim de controlar o processamento dos 
neurônios intermediários. 
Bahoura e Park (2011) demonstraram a implementação de uma RNA MLP com 
treinamento BP com algumas modificações. No método BP, o trabalho propôs uma 
modificação na atualização os pesos, baseando-se em regras de atualização 
‘atrasadas’. Assim, o erro médio é obtido pela equação (10). 
 
."( −/) = $"( −/) −"( −/) 
(10) 


85 
 
 
Na equação (10), $"( −/) e "( −/) representam as versões atrasadas da 
saída desejada e atual do neurônio, respectivamente. Neste contexto, os resultados da 
implementação em hardware demonstraram ser quatro vezes mais rápidas que as tidas 
como convencionais, no caso de funções não lineares. 
O trabalho de Dondon et al. (2014) apresentou o desenvolvimento de uma RNA 
de arquitetura feed forward simples com apenas uma camada escondida, contendo três 
neurônios, e contendo um neurônio na camada de saída. Ainda, neste trabalho, Dondon 
et al. (2014) decidiram por efetuar o treinamento utilizando as ferramentas da aplicação 
Matlab, devido à restrição de tamanho do dispositivo FPGA.  
Os neurônios foram representados em módulos. Tais módulos contém 
memórias, unidades de cálculo e unidades de tratamento. Como a implementação 
utilizou a linguagem VHDL de forma direta, duas formas foram testadas: um módulo por 
neurônio e um módulo por camada. Na primeira implementação, os neurônios se 
inicializavam um a um e aguardavam uns aos outros a cada passo. Quando todos 
estavam inicializados, havia o cálculo da soma ponderada e, quando prontos, 
escreviam seus resultados na memória. A na segunda implementação utilizava um 
neurônio por camada, adicionando-se um módulo adicional por cada camada. Neste 
caso, era necessário voltar ao módulo neuronal cada vez que um resultado era obtido, 
a fim de informar ao neurônio sua posição na RNA (DONDON et al., 2014). A conclusão 
foi que a primeira implementação foi mais veloz pois permitiu o paralelismo entre os 
neurônios, porém utilizou mais recursos. A segunda implementação consumiu menos 
componentes e recursos, porém cada módulo precisava ser reiniciado novamente a 
cada nova entrada processada (DONDON et al., 2014). Concluiu-se ainda que a 
linguagem VHDL juntamente como FPGA permitiu uma flexibilização do projeto a um 
custo eficiente, mas com grande necessidade de conhecimento técnico na geração de 
circuitos paralelos.   
Ainda, neste contexto, o trabalho de Guo et al. (2012) avaliou uma RNA paralela 
construída sobre várias unidades computacionais, com um sistema em dispositivo 
FPGA e uClinux8. Com a utilização do treinamento pelo método BP, o sistema utilizou 
unidades paralelas de cálculo aritmético. O processo de implementação da RNA incluiu 
a estrutura da rede para computação paralela e o desenvolvimento de um software 
paralelo (GUO et al., 2012). 
 
8 uClinux (µClinux) é uma variação do kernel do S. O. Linux, aplicado em microcontroladores 
sem uma unidade de gerenciamento de memória. Tal sistema operacional disponibiliza ferramental para 
utilizar o sistema operacional Linux em microcontroladores (DIONNE; DURRANT, 2007) 


86 
 
 
Em outro trabalho, Nedjah et al. (2012) propõe uma implementação envolvendo 
hardware e software na concepção de uma RNA. É implementado uma RNA paralela 
em hardware, do tipo MLP, utilizando a linguagem VHDL; e um software utilizando a 
linguagem de programação C.  
A aplicação desenvolvida permite ajustar a topologia da RNA, informando a 
quantidade de camadas, a quantidade de neurônios por camada, bem como a 
quantidade de entradas. Depois deste ajuste, um laço de repetição alimenta o hardware 
por meio de um barramento de dados com as entradas, pesos e valores de bias 
necessários para a computação da RNA. Em tempo, a aplicação criada na linguagem 
C executa no microprocessador MicroBlaze9. A Figura 17 apresenta o esquema da 
disposição dos componentes no sistema. 
Figura 17 - Esquema de configuração da RNA MLP 
 
 
 
 
 
 
 
Fonte: Nedjah et al., 2012. 
Uma característica particular desenvolvida no trabalho de Nedjah et al. (2012) 
é que, a fim de reduzir o tempo de processamento gasto na computação aritmética, um 
número real é representado usando frações de números inteiros. Desta forma, a 
aritmética é limitada a operações inteiras, realizadas por circuitos combinacionais. 
Assim, é necessária uma máquina de estados simples para controlar somas e produtos 
de frações, economizando hardware e diminuindo tempo de processamento (NEDJAH 
et al., 2012). Nos resultados concluiu-se, por meio de comparações, que o projeto 
atingiu o sucesso esperado, tornando-se mais veloz na execução e prototipação, bem 
como no uso da área do dispositivo. 
Visando facilitar a construção de RNA em hardware, Baptista; Morgado-Dias 
(2017) apresentam a implementação de um gerador automático neural de propósito 
 
9 O MicroBlaze é um microprocessador RISC IP da fabricante XILINX, que pode ser sintetizado 
em dispositivos reconfiguráveis (XILINX, 2017) 


87 
 
 
geral (ANGE - Automatic General-purpose Neural Hardware Generator). Tal projeto 
provê uma implementação direta em hardware de uma RNA feed-forward, utilizando-se 
uma interface gráfica. Nesta, o usuário insere a estrutura da RNA, a quantidade de bits 
e o tipo de implementação da função de ativação, e carrega os arquivos com os pesos. 
Após tais processos, o sistema ANGE automaticamente produz o código necessário 
para sintetizar o hardware. A Figura 18 apresenta o fluxo de desenvolvimento de RNA 
utilizando a ferramenta ANGE. 
Figura 18 - Fluxo de desenvolvimento de RNA utilizando a ferramenta ANGE 
 
Fonte: Baptista; Morgado-Dias, 2017. 
Ainda, na ferramenta ANGE, o usuário pode escolher como implementar 
funções de ativação. A tangente hiperbólica, por exemplo, pode ser implementada de 
duas maneiras diferentes: utilizando LUT ou a interpolação de Chebyshev (BAPTISA; 
MORGADO-DIAS, 2017). Os resultados apresentados foram promissores, uma vez que 
a taxa de erros foi próxima à da implementação feita em MATLAB. Em tempo, a 
ferramenta ANGE faz uso das ferramentas e aplicações MATLAB e Simulink, System 
Generator e Xilinx ISE. 
2.4.8 Considerações finais sobre implementação de RNA 
A presente seção apresentou, de forma resumida, um descritivo da tecnologia 
de RNA e sua implementação. Pode observar-se, portanto, que o grande apelo destes 
modelos está em sua capacidade de “aprender” e generalizar sistemas, tendo como 
fonte conjuntos de dados simples ou complexos. Neste contexto, como uma RNA pode 
aceitar diferentes dados de entrada, a utilização desta tecnologia mostra-se adequada 


88 
 
 
para modelagem de várias soluções para problemas reais, principalmente a partir de 
dados coletados em campo (HAYKIN, 2008; HEATON, 2015; RUSSELL; NORVIG, 
2009; SILVA et al., 2010a). 
Tidas como modelos matemáticos, RNA podem ser implementadas por 
circuitos integrados, ou ainda simuladas utilizando-se aplicativos computadorizados. No 
entanto, o paralelismo inerente incorporado à dinâmica de uma RNA só pode ser 
idealmente realizado em implementações feitas por meio de hardware especializado 
(DEOTALE; DEOLE, 2014). Ainda, quando máquinas sequenciais baseadas na 
arquitetura de von Neumann são muito utilizadas para a execução e simulação de RNA, 
a velocidade é limitada, principalmente quando o tamanho da estrutura se torna grande 
(milhares de neurônios).  
As implementações de RNH baseadas em hardware digital tendem a fornecer 
melhores resultados. Recentes avanços em lógica reprogramável permitem a 
implementação de RNA relativamente grandes (com alguns milhares de neurônios) em 
apenas um dispositivo FPGA. A principal razão disto é a tecnologia de miniaturização 
de componentes manufaturados, fazendo com que a capacidade dos componentes 
aumente significativamente (ABROL; MAHAJAN, 2015). De fato, dispositivos FPGA se 
apresentam como boas alternativas para a implementação de RNH. A Tabela 3 
demonstra um comparativo entre quatro tecnologias de hardware.  
Tabela 3 - Comparativo entre tecnologias de hardware digital 
Parâmetro 
ASIC 
Analógico 
ASIC 
 Digital 
FPGA 
Processador 
Área 
+++ 
++ 
+ 
- 
Velocidade 
+++ 
++ 
+ 
- 
Custo 
-- 
-- 
++ 
++ 
Tempo de projeto 
-- 
-- 
+ 
+++ 
Confiabilidade 
-- 
+ 
++ 
++ 
Cada + significa ponto positivo; Cada - significa ponto negativo 
Fonte: Deotale; Deole, 2014. 
A Tabela 3 apresenta que, considerando-se a média entre consumo de área, 
velocidade, custo, tempo de projeto e confiabilidade, dispositivos FPGA se mostram 
como a melhor alternativa de desenvolvimento. Porém, os usuários devem conhecer 
técnicas de programação em baixo nível, ou ainda as linguagens de descrição de 
hardware, a fim de realizar a programação para FPGA. De fato, linguagens como C e 


89 
 
 
C++ não são adequadas para descrição de hardware, devido às particularidades 
necessárias à programação de tais dispositivos de forma direta (TISAN; CHIN, 2015; 
WINDH et al., 2015). 
A fim de resumir algumas características desejáveis na concepção de RNA em 
hardware, os trabalhos correlatos descritos anteriormente estão relacionados na Tabela 
4, e podem ser comparados ao modelo computacional NeuroPON proposto. Neste 
sentido, almeja-se que o NeuroPON tenha conjuntamente as propriedades elencadas. 
Parte destas propriedades são objeto de discussão do Capítulo 4, e outras estão 
previstas nos trabalhos subsequentes. 
 
Tabela 4 - Comparação entre trabalhos correlatos e a proposta do modelo computacional NeuroPON:  
características presentes e ausentes 
Trabalho/proposta 
Programação 
em Alto Nível 
Treinamento no 
hardware 
Customizável 
Geração de 
Código 
Código 
Desacoplado 
Código para 
Plataformas 
Distintas 
Abrol e Mahajan (2015) 
N 
? 
N 
N 
N/A 
N/A 
Ali e Mohammed (2010) 
N 
N 
N 
N 
N/A 
N/A 
Bahoura e Park (2011) 
N 
N 
N 
N 
N/A 
N/A 
Baptista e Morgado-Dias (2017) 
S 
N 
S 
S 
? 
N 
Dondon et al. (2014) 
N 
N 
N 
N 
N/A 
N/A 
Gomperts et al. (2011) 
S1 
S 
S1 
N 
N/A 
N/A 
Guo et al. (2012) 
N 
S 
N 
N 
N/A 
N/A 
Nedjah et al. (2012) 
S2 
N 
S 
S3 
? 
N 
Rezvani et al. (2012) 
N 
S 
N 
N 
N/A 
N/A 
Tisan e Chin (2015) 
S1 
N 
N 
N 
N/A 
N/A 
NeuroPON 
S 
S 
S 
S 
S 
S 
Legenda: S: sim  N: não  ?: informações não disponíveis  N/A: Não se Aplica 
Notas: 1 Utiliza outras ferramentas ou plataformas para a programação/descrição da RNA; 2Programação utilizando linguagem C, 
portanto, não declarativa-descritiva; 3Geração de código feita diretamente no hardware por meio de microprocessador dedicado. 
Fonte: Autoria Própria 
As duas colunas mais à direita da Tabela 4 apresentam características quanto 
ao código a ser gerado: desacoplado e passível de execução em plataformas distintas. 
Um código desacoplado viabiliza a construção de programas com execução paralela 
ou distribuída tão fina quanto a arquitetura computacional permitir; e um código visando 
plataformas distintas é aquele que pode ser executado em diversas  arquiteturas 
computacionais, tanto em software quanto em hardware. 


90 
 
 
Dos trabalhos analisados nesta tese, apenas a solução de Baptista; Morgado-
Dias (2017) apresenta uma geração de código a partir de parametrização, porém tal 
código não apresenta características de desacoplamento, tampouco passíveis de 
execução em plataformas distintas. Isto posto, fica clara a importância do 
desenvolvimento de um modelo que permita a implementação, utilizando linguagem 
declarativa-descritiva de alto nível, de RNA distribuíveis e desacopladas, cujos códigos 
para treinamento e execução possam ser executados em diversos tipos de plataformas. 
2.5 Considerações sobre a Revisão de Literatura 
O presente Capítulo apresentou os conceitos relacionados aos objetivos 
propostos para o presente trabalho, no âmbito do desenvolvimento do modelo 
computacional NeuroPON. Neste contexto, o resultado de uma revisão de literatura, 
bem como a discussão de tais trabalhos frente ao objetivo proposto, foi realizado. 
Ressalta-se que a revisão de literatura englobou apenas o predicado da busca 
descrita no início do presente capítulo. Neste âmbito, é sabido que existem outras 
tecnologias que não estão cobertas no presente capítulo. Por fim, exemplos de 
tecnologias de hardware na implementação de RNA foram apresentadas, bem como 
exemplos de aplicação em diversos trabalhos. O destaque à tecnologia de 
implementação de RNA com hardware reconfigurável se dá pela natureza do trabalho, 
bem como à necessidade de agregar trabalhos importantes para futuras comparações. 
Fica clara a necessidade de um modelo que facilite a criação de RNA mais 
eficazes. Tais RNA devem ser, de fato, implementadas de forma otimizada, e com 
tecnologias que possam realmente aproveitar todo seu potencial paralelo (conforme já 
apresentado). Neste sentido, há uma carência quanto a modelos de programação 
paralela, se comparados com modelos disponíveis para programação sequencial, que 
sejam difundidos e de simples utilização. As dificuldades permanecem no tocante a 
paralelismo e distribuição, pois estão presentes na definição dos paradigmas apontados 
(BORKAR; CHIEN, 2011; KAISLER, 2005; LINHARES, 2015).  
Partindo deste pressuposto, o uso de um paradigma de programação mais 
adequado ao desenvolvimento de aplicações paralelizáveis é proposto. O Capítulo 3 
aborda o PON, que permite construir códigos com o mínimo de redundância estrutural 
e temporal, menor acoplamento entre as entidades, melhorando assim a distribuição e 
paralelização dos processos criados. 
 
 


91 
 
 
3 Paradigma Orientado a Notificações 
As seções a seguir apresentam os conceitos teóricos e mesmo práticos 
fundamentais sobre o Paradigma Orientado a Notificações (PON). Tais seções têm 
seus conteúdos baseados e adaptados dos trabalhos de Linhares (2015), Pordeus 
(2017) e Santos (2017), que sintetizam os trabalhos do grupo de pesquisa do PON 
(SIMÃO, 2017). 
3.1 Origens do PON 
O Paradigma Orientado a Notificações (PON) foi proposto como uma nova 
alternativa de desenvolvimento de sistemas computacionais, inicialmente software mas 
subsequentemente também hardware, visando diminuir problemas existentes nos 
atuais Paradigma Imperativo (PI) e Paradigma Declarativo (PD), já tratados na seção 
2.1. Exemplos de problemas são as redundâncias de execução com o consequente 
mau uso de processamento e o correlato acoplamento excessivo entre entidades 
computacionais com a consequente dificuldade de reaproveitamento delas e de 
paralelização/distribuição de seu processamento (BANASZEWSKI, 2009; PORDEUS, 
2017; SIMÃO; STADZISZ, 2008).  
Não obstante, o PON encontra certas inspirações no PI, como flexibilidade 
algorítmica e abstração em forma de entidades similares a classes/instâncias do POO. 
Tal qual, PON também encontra certas inspirações no PD, como abstração do 
conhecimento em termos de expressão por meio de regras lógico-causais e base de 
fatos dos SBR, as quais são tratadas por entidades outras. Desta forma, o PON 
possibilita o uso simbiótico de ambos os paradigmas de programação em seu modelo, 
mas, contudo, aprimorando o processo de inferência ou cálculo lógico-causal, bem 
como a organização de entidades que permitem inferência diferenciada (SIMÃO; 
STADZISZ, 2008).  
Em PON, justamente, a inferência se dá por notificações pontuais e precisas 
entre entidades pertinentes e colaborativas. Neste âmbito, o PON introduz um novo 
conceito para a concepção, construção e execução de aplicações de software. Essa 
nova maneira de concepção de software tende a proporcionar uma melhora na 
performance das aplicações e, potencialmente, tende a facilitar suas concepções, tanto 
para ambientes não paralelo e distribuídos como para ambientes paralelos e/ou 


92 
 
 
distribuídos (BANASZEWSKI, 2009; LINHARES et al., 2011; RONSZCKA, 2018; 
SIMÃO; STADZISZ, 2008; SIMÃO; STADZISZ, 2009a; SIMÃO et al. 2012a). 
Estas características do PON serão consideradas nas seções subsequentes. 
Entretanto, de antemão, foram essas características que permitiram classificar o PON 
a luz da classificação de paradigmas proposta por Peter Van Roy (XAVIER, 2014; 
XAVIER et al., 2014). Na Figura 19, encontra-se o PON em relação aos demais 
paradigmas, sendo que os detalhes de tal classificação se encontram em Xavier (2014).  
Figura 19 - Taxonomia de paradigmas de programação incluindo o PON 
 
Fonte: XAVIER, 2014. 
3.2 Entidades do PON 
A estrutura de uma aplicação no modelo PON é representada na forma de Base 
de Fatos (FBE – Fact Base Element) e Regras (Rules). As entidades FBE são utilizadas 
para representar entidades do mundo em um sistema computacional, por meio de 
conjuntos de estados mutuamente exclusivos que são tratados por entidades 
chamadas de Atributos (Attributes) e por meio de correlatos serviços tratados por 
entidades chamadas de Métodos (Methods). As entidades Rules, por sua vez, definem 


93 
 
 
o cálculo lógico-causal a ser efetuado sobre os estados dos FBE, controlando a 
execução dos seus serviços, à luz dos Attributes e dos Methods (SIMÃO; STADZISZ, 
2008; SIMÃO et al., 2009b). A Figura 20 apresenta a estrutura do modelo PON. 
Figura 20 - Estrutura do modelo de notificações PON 
<<NOP>>
Action
<<NOP>>
Rule
<<NOP>>
Condition
<<NOP>>
Premise
<<NOP>>
Instigation
<<NOP>>
Attribute
<<NOP>>
Method
<<NOP>>
FBE
1
1
1
1
0..*
1..*
 Activate 
1..*
0..*
Notify
 State
1..2
0..*
Notify
 State
0..*
1..*
 Instigate 
1
0..*
1
1..*
Change 
State
 
Fonte: Adaptado de SIMÃO et al., 2009b. 
A entidade que representa uma Rule é decomposta em uma entidade 
Condition, que representa a avaliação lógico-causal, e uma entidade Action, que 
representa as ações a serem executadas em função da aprovação da respectiva 
Condition. Cada Condition, por sua vez, é relacionada a uma ou mais entidades que 
tratam operações lógicas chamadas Premises, as quais operam sobre valores entre 
dois Attributes, ou entre um Attribute e um valor constante. Ainda, cada entidade Action 
é relacionada a entidades denominadas Instigations, que colaboram com as Actions 
acionando a execução de algum serviço de um objeto FBE por meio de seus Methods. 
Por sua vez, estas chamadas podem mudar os estados dos Attributes. A Figura 21 
apresenta a estrutura de uma Rule (Regra) em PON (SIMÃO; STADZISZ, 2008; SIMÃO 
et al., 2009b). 
Figura 21 - Exemplo de um Regra (Rule) em PON 
 
Fonte: Autoria Própria 


94 
 
 
No exemplo da Figura 21 é apresentada uma Rule (com seus colaboradores 
Condition, Premises, Action e Instigations) no formato usual de regras lógico-causais 
para realizar o controle de um portão simples. Na representação a FBE Gate contém o 
Attribute attGateState, que representa o estado do portão e o Attribute attTimer, que 
representa o tempo decorrido desde a operação (abertura ou fechamento), e um 
Method chamado mthOpening(), utilizado para efetuar a abertura do portão. 
Ainda, na Figura 21, a Rule é formada por duas Premises. A primeira Premise 
valida se o Attribute attGateState é igual à zero, enquanto que a segunda Premise 
também valida se o Attribute attTimeré igual a zero. Quando ocorre a modificação no 
valor de qualquer um dos Attributes envolvidos, as Premises serão notificadas, sendo 
que cada Premise é notificada a partir de seu respectivo Attribute. Subsequentemente, 
se o valor lógico de alguma das Premises notificadas for alterado, cada Premise de 
valor modificado irá notificar sua Condition relacionada (SIMÃO; STADZISZ, 2008; 
SIMÃO et al., 2009b). 
A Condition do exemplo em questão é formada por uma conjunção entre as 
duas Premises. Portanto para a aprovação da mesma, é necessário que as duas 
Premises tenham seu valor lógico verdadeiro. Caso esta Condition seja verdadeira, 
será executada uma Action, que por sua vez, irá realizar a chamada (por meio das 
Instigations) de execução do Method mthOpening  (SIMÃO; STADZISZ, 2008; SIMÃO 
et al., 2009b). 
Outrossim, a colaboração entre estes elementos do PON, i. e. FBE com seus 
Attributes e Methods e Rules com seus colaboradores (Premises, Conditions, Actions 
e Instigations), ocorre por meio de notificações diretas, o que é um processo de 
inferência essencialmente distinto dos processos utilizados em software em PI e em PD 
(SIMÃO; STADZISZ, 2008; SIMÃO et al., 2009b). 
Não obstante, existem casos em que o processo de notificação dos Attributes 
(sua reatividade) encadearia sequências de notificações indesejáveis. Tais casos 
podem ser caracterizados por situações em que um dado Attribute, apesar de não ser 
determinante para a aprovação de uma Rule em um dado contexto, apresenta 
constantes mudanças de estado, disparando o fluxo de notificações a cada variação 
em seu estado. Assim, tais notificações desnecessárias impactariam negativamente no 
desempenho de execução de uma aplicação PON (RONSZCKA, 2012). 
Neste contexto, tais estruturas que possuem um tratamento diferenciado pela 
cadeia de notificações, são chamados de Attributes Impertinentes. Cada Attribute 
impertinente 
em 
dado 
contexto 
tem 
suas 
funções 
reativas 
desabilitadas 


95 
 
 
temporariamente para com as Premises-Conditions-Rules afetadas pela impertinência. 
Uma vez desabilitadas, as variações de estado desse Attribute não impactariam no 
disparo do fluxo de notificações para Premises a ele relacionadas. Neste âmbito, 
quando o conjunto dos Attributes tivesse aprovado ‘suas’ Premises em uma dada 
Condition-Rule, essa deveria solicitar a reativação das notificações para a Premise 
composta pelo Attribute impertinente.  
A Figura 22 apresenta de forma genérica as colaborações entre as entidades 
do modelo PON (LINHARES et al., 2015). Do ponto de vista dinâmico, cada vez que o 
valor de um Attribute é modificado, o próprio Attribute notifica apenas e precisamente 
as Premises que dependem do seu valor. Cada uma destas Premises, por sua vez, tem 
seu valor lógico reavaliado por meio do cálculo relacional, o qual opera sobre o novo 
valor do Attribute que a notificou e também sobre um segundo valor, que pode ser uma 
constante ou outro Attribute (SIMÃO; STADZISZ, 2008; SIMÃO et al., 2009b). 
Figura 22 - Colaborações entre entidades do modelo PON 
 
Fonte: Adaptado de Linhares et al., 2015. 
Cada Premise, cujo resultado lógico tenha sido alterado, notifica precisamente 
apenas um conjunto de entidades Conditions que dela dependem. Em seguida, cada 
uma destas Conditions também tem seu estado lógico reavaliado de acordo com os 
resultados das Premises. Se o valor lógico da entidade Condition é verdadeiro, a Rule 


96 
 
 
é aprovada para execução. Com isso, uma vez resolvido eventuais conflitos, a Action 
agregada a esta Rule notifica as Instigations conectadas, as quais disparam os Methods 
correspondentes. A execução dos Methods gera o processamento factual que pode 
atualizar Attributes dos FBE, reiniciando o ciclo de inferência de notificações (SIMÃO; 
STADZISZ, 2008; SIMÃO et al., 2009b). Estas etapas, portanto, descrevem a cadeia 
de notificação do PON. 
Isto posto, pode-se afirmar que, no PON, a essência da computação está 
organizada e distribuída entre as entidades autônomas e reativas apresentadas, sendo 
que estas colaboram, entre si, por meio de notificações pontuais. Tal arranjo forma o 
mecanismo de notificações, que determina o fluxo de execução das aplicações. Por 
meio desse mecanismo, as responsabilidades de um programa são divididas entre os 
objetos do modelo, o que permite execução otimizada e ‘desacoplada’ (i.e. 
minimamente acoplada) útil para o aproveitamento correto de monoprocessamento, 
bem como para o processamento distribuído (BELMONTE et al., 2016; LINHARES, 
2015; PETERS et al., 2011; RONSZCKA, 2012; SIMÃO et al. 2012a).  
A próxima seção apresenta as materializações do PON, demonstrando como o 
paradigma pode ser utilizado para a criação de artefatos de software e hardware. 
3.3 Materializações do PON 
As subseções que seguem apresentam um resumo do estado da técnica atual 
no tocante ao PON. Em suma, resume-se as materializações ou implementações do 
PON. 
3.3.1 Arquétipo ou Framework  
A primeira implementação dos conceitos do PON foi realizada sobre um 
arquétipo ou Framework desenvolvido em linguagem de programação C++. O objetivo 
deste Framework é oferecer uma interface de programação (API - Application 
Programming Interface) para o desenvolvimento de aplicações seguindo o modelo 
PON, com abstrações necessárias para compor as FBE e Rules (BANASZEWSKI, 
2009; RONSZCKA, 2012; VALENÇA, 2012).  
O Framework PON C++ prototipal (ou referencial) foi proposto por Simão em 
2007 (SIMÃO et al., 2012c; SIMÃO; STADZISZ, 2008), remontando ao Framework que 
implementa o metamodelo do Controle Orientado a Notificações (CON) sobre a 
ferramenta ANALYTICE II (SIMÃO, 2005). Tal Framework prototipal foi refeito no 


97 
 
 
trabalho de Banaszewski (2009) gerando o chamado Framework PON C++ 1.0 (ou 
original) . Subsequentemente, uma nova versão do Framework, otimizada e orientada 
a padrões de projeto, foi elaborada nos trabalhos de Valença (2012) e Ronszcka (2012) 
sendo chamada de Framework PON C++ 2.0 (ou otimizado). Este ainda se constitui na 
principal materialização estável do PON para software (RONSZCKA, 2012; 
RONSZCKA et al., 2015; VALENÇA, 2012). 
O Framework PON C++ é implementado por um conjunto de classes cujos 
métodos são materializados em PI, sendo que sua implementação se baseia em 
percorrer estruturas de dados (originalmente fornecidas pela STL– Standard Template 
Library na versão 1.0 do Framework – e subsequentemente por biblioteca própria na 
versão 2.0 do Framework) para avaliação das relações lógico-causais e fazer o envio 
de notificações na forma de chamada de métodos. Tal abordagem é desvantajosa à 
filosofia do PON em si, pois há uma enorme dependência de estruturas de dados e a 
execução sobre tais estruturas se dá de forma sequencial, decorrendo assim em 
degradação de desempenho (LINHARES, 2015; RONSZCKA, 2012; VALENÇA, 2012). 
Neste âmbito, Valença (2012) e Ronszcka (2012) efetuaram uma série de 
otimizações com objetivo de aprimorar a performance de execução das aplicações 
sobre Framework C++ PON, o que foi chamado de Framework C++ PON 2.0.  
O Framework PON C++ 2.0 é baseado em uma variedade de estruturas de 
dados mais otimizadas do que as equivalentes fornecidas pela STL, por exemplo, 
vetores (PONVECTOR), listas (PONLIST) e tabelas hash (PONHASH). Tais 
otimizações, frente ao Framework PON C++ 1.0, fizeram o Framework PON C++ 2.0 
apresentar ganhos de desempenho em diversas aplicações (RONSZCKA, 2012; 
VALENÇA, 2012). 
Segundo Ronszcka (2012), as entidades do PON, no Framework PON C++ 2.0, 
estão estruturadas na forma de classes/objetos, sendo relacionados por meio de 
estruturas de dados, com referência às entidades que têm interesse em seus estados. 
Para uma melhor visualização de tais relacionamentos, a Figura 23 apresenta um 
diagrama de classes do Framework PON C++ 2.0. Em tempo, esse Framework PON é 
aqui considerado por ter servido como primeira abordagem ou protótipo para 
NeuroPON, a ser explicado subsequentemente neste trabalho (SCHÜTZ et al., 2015). 
De acordo com a Figura 23, o Framework PON C++ 2.0 subdivide-se em três 
pacotes principais. O pacote Application é formado exclusivamente pela classe 
Application, sendo que tal classe representa a ponte de ligação entre uma aplicação 
PON e as demais classes do Framework em questão. O pacote Scheduler, por sua vez, 


98 
 
 
representa as implementações das classes de resolução de conflitos (RONSZCKA, 
2012). Por fim, o pacote Core contém as classes colaboradoras, responsáveis pelo 
processo de notificação do Framework (RONSZCKA, 2012). Em tempo, uma vez que a 
cadeia de notificações é determinante nos conceitos do PON, a Figura 24 apresenta tal 
pacote em detalhes, com o detalhamento de suas entidades componentes. 
Figura 23 - Estrutura do Framework PON C++ 2.0, demonstrada por Diagrama  
de Classes e Pacotes em UML 
 
Fonte: Ronszcka, 2012. 
Neste contexto, é importante destacar o relacionamento entre a estrutura 
apresentada na Figura 24 e a estrutura apresentada na Figura 20, indicando que o 
pacote CORE implementa a estrutura de entidades do PON, adicionando algumas 
particularidades necessárias ao modelo. Como exemplo, as classes Method e Rule, 
que definem as entidades puras do PON, são estendidas de modo a proporcionar 
funcionalidades adicionais (RONSZCKA, 2012).  
Também em conjunto com o pacote CORE, os subpacotes Attributes e 
Conditions podem ser destacados. O subpacote Attribute é formado pelas classes 
responsáveis por encapsular os tipos primitivos da POO. Estas classes (Boolean, Char, 
Double, Integer e String) introduzem reatividade aos tipos primitivos, permitindo que 
estes façam parte de estruturas causais do PON (RONSZCKA, 2012). Por sua vez, o 
subpacote Conditions é formado pelas classes que fazem parte da composição de uma 
respectiva Condition. Particularmente, a classe LogicalOperator e suas derivadas 


99 
 
 
(Conjunction, Disjunction e Single), definem a operação lógica utilizada pela Condition 
de maneira a aprovar uma determinada Rule (RONSZCKA, 2012). 
Figura 24 - Estrutura do pacote CORE, representada por meio de um Diagrama de Classes em UML 
 
Fonte: Ronszcka, 2012. 
Visando demonstrar a utilização do Framework PON C++ 2.0, alguns trechos 
de códigos são aqui apresentados. Quanto à sua codificação, o Framework segue a 
sintaxe da linguagem C++. Para que se possa criar uma aplicação, o desenvolvedor 
precisa estender a classe NOPApplication, cuja instância coordena todo o processo. As 
entidades do PON possuem classes base que o desenvolvedor precisa estender e 
instanciar, como FBE, ou apenas instanciar, como Rule. Ainda, a classe Attribute é 
estendida de acordo com seu tipo: Boolean, Integer, Double, Char ou String. 
Quando uma classe NOPApplication é criada ou instanciada e alguns Attributes 
são ajustados, o núcleo do Framework configura todas as tarefas necessárias, e inicia 
a cadeia de notificações. O Código 4 mostra um trecho de código da declaração da 
classe GateSystem para o controle de um portão eletrônico, a qual estende 
NOPApplication, como um exemplo. 
 
 


100 
 
 
Código 4 - Classe NetworkSystem que estende NOPApplication, cuja instância coordena todo o sistema 
01 
02 
03 
04 
05 
06 
07 
08 
09 
10 
11 
12 
13 
class GateSystem : public NOPApplication { 
    public: 
        Gate *gate; 
        RemoteControl *remoteControl; 
    public: 
        GateSystem(); 
        virtual ~GateSystem(); 
    private: 
        void initStartApplicationComponents(); 
        void initFactBase(); 
        void initSharedEntities(); 
        void initRules(); 
        void codeApplication(); 
}; 
Fonte: Autoria Própria 
A Código 5 apresenta um código que corresponde a um FBE para execução de 
uma aplicação PON por meio do Framework. Este exemplo consiste na definição do 
próprio portão, por meio da FBE Gate.  
Código 5 - Código: estrutura de uma FBE no Framework PON C++ 2.0 
01 
02 
03 
04 
05 
06 
07 
08 
09 
10 
11 
12 
13 
14 
15 
16 
17 
18 
class Gate: public FBE{ 
public: 
 
Integer* attGateState; 
      Integer* attTimer; 
 
public: 
 
Gate(); 
 
void Opened(); 
 
void Closed(); 
 
void Opening(); 
 
void Closing(); 
 
void StopOpening(); 
 
void StopClosing(); 
 
MethodPointer<Gate>* mtStatusOpened; 
 
MethodPointer<Gate>* mtStatusClosed; 
 
MethodPointer<Gate>* mtStatusOpening; 
 
MethodPointer<Gate>* mtStatusClosing; 
 
MethodPointer<Gate>* mtStatusStopOpen; 
 
MethodPointer<Gate>* mtStatusStopClose; 
}; 
Fonte: Autoria Própria 
O Código 5 apresenta a estrutura para a criação de Rules em Framework PON 
C++ 2.0. Neste caso, a Rule controla o processo de abertura do portão a partir de três 
Premises: a primeira verifica se o controle remoto está ativo, a segunda valida se o 
portão está fechado e a terceira verifica o temporizador do portão (indica seu tempo de 


101 
 
 
abertura). Em caso de uma conjunção verdadeira entre as três Premises, o Method 
mthOpening é instigado, e a abertura do portão é iniciada. 
Código 6 - Código: estrutura das Premises para o Framework PON C++ 
01 
02 
03 
04 
05 
06 
07 
08 
09 
10 
11 
12 
RULE(rleOpeningGate, SingletonScheduler::getInstance(), Condition::SINGLE); 
PREMISE(preOpening0, remotecontrol->attRemoteStatus, true, Premise::EQUAL,  
        Premise::STANDARD, false); 
PREMISE(preOpening1, this->attGateState, 0, Premise::EQUAL, Premise::STANDARD,  
        false); 
PREMISE(preOpening2, this->attTimer, 0, Premise::EQUAL, Premise::STANDARD,  
        false); 
mthOpening = new MethodPointer<Gate>(this, &Gate::opening); 
rleOpeningGate->addPremise(preOpening0); 
rleOpeningGate->addPremise(preOpening1); 
rleOpeningGate->addPremise(preOpening2); 
rleOpeningGate->addMethod(mthOpening); 
Fonte: Autoria Própria 
A apresentação dos trechos do Código 5 e do Código 6 visa exemplificar a 
sintaxe do Framework PON C++ 2.0, destacando apenas as definições para execução 
de uma Rule. Informações mais detalhadas estão nos trabalhos de Ronszcka (2012), 
Ronszcka et al. (2017), Valença (2012), e Valença et al. (2011). Ademais, a 
implementação de uma RNA em PON, utilizando o Framework PON C++ 2.0, é descrita 
em Schütz et al. (2015), bem como no Capítulo 4 do presente trabalho. 
Segundo Ronszcka (2012), o Framework PON C++ 2.0 permite uma rápida 
prototipação de aplicações PON para teste sobre plataformas de computação 
convencionais. Entretanto, mesmo após otimizações feitas no âmbito do Framework, 
experimentos foram conduzidos sendo que os resultados ainda não se mostraram 
satisfatórios em termos de desempenho vis-à-vis o cálculo assintótico do PON 
(BANASZEWSKI, 2009; SIMÃO et al, 2012a). Tal degradação se deve principalmente 
ao uso de estruturas de dados custosas à execução do processo de inferência.  
Muito embora efetivamente funcional e com resultados de desempenho 
aceitáveis ainda que aquém do desejado à luz da natureza do PON, o Framework PON 
C++ 2.0 não é concorrente e, portanto, não paralelizável em si. Baseando-se nesta 
característica, uma extensão para o Framework PON C++ 2.0 foi criada a fim de 
executar de forma concorrente e, ademais, sobre processadores multicore. Tal 
extensão é chamada de Framework PON C++ 3.0, e é assunto da seção 3.3.3. 
Ainda que o Framework 3.0 e suas tecnologias associadas permitam 
processamento paralelizado de granularidade fina em ambientes multicore, as 
estruturas de dados que degradam o desempenho ainda estão presentes. Desta forma, 


102 
 
 
motivou-se a criação de uma linguagem e compilador específicos ao modelo PON, com 
o objetivo de eliminar ou minimizar os problemas apresentados nos frameworks quanto 
ao uso de estrutradas de dados (FERREIRA, 2015). Tal linguagem e compilador são 
descritos na seção 3.3.2. 
3.3.2 Linguagem e compilador para o PON 
A primeira versão prototipal da Linguagem e Compilador para o PON surgiram 
como resultado de esforços conjuntos dos integrantes do grupo de pesquisa em PON. 
Assim, a versão prototipal desenvolvida foi uma primeira demonstração sobre a 
viabilidade de se desenvolver uma linguagem e compilador para o PON (RONSZCKA, 
2018)(SANTOS, 2017).  
Na construção da linguagem PON foi definido um conjunto de tokens, sendo 
ainda especificada por meio de formalismo (gramática) segundo Backus-Naur Form 
(BNF) (FERREIRA, 2015). Subsequentemente, por meio de esforços de Ferreira (2015) 
com colaboração de Ronszcka et al. (2017b), esta versão prototipal da LingPON passa 
a ser chamada de Tecnologia LingPON 1.0, nomeando assim o conjunto linguagem e 
compilador para o PON. Na verdade, as tecnologias LingPON em geral, iniciais e 
subsequentes, seguem um método elaborado para a criação de linguagens e 
compiladores para o PON, atualmente chamado de MCPON (RONSCKA, 2018). 
3.3.2.1 Linguagem do LingPON 1.0 
Na tecnologia LingPON 1.0, a sua linguagem em si é chamada naturalmente 
de LingPON 1.0. Isto dito, de modo geral, o código fonte de uma aplicação utilizando a 
LingPON 1.0 segue três etapas específicas. Primeiramente define-se as FBE de seu 
programa, declara-se as instâncias necessárias desses FBE e informa-se a estratégia 
de escalonamento das Rules. Em seguida, é necessário definir as Rules para fins de 
avaliação lógico-causal dos estados das instâncias de cada FBE por meio de 
notificações. Por último, é possível adicionar um código específico da linguagem alvo 
escolhida no processo de compilação (e.g. C ou C++), através da utilização do bloco 
de código main (FERREIRA, 2015). O Código 7 apresenta o código fonte de uma 
aplicação completa em PON, que implementa o comportamento de um portão 
eletrônico simples, controlando apenas a abertura e fechamento do portão. 
 


103 
 
 
Código 7 - Controle de Portão Eletrônico implementado com LingPON 1.0 
01 
02 
03 
04 
05 
06 
07 
08 
09 
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
fbe Gate 
    attributes 
        integer atGateState 0 
    end_attributes    
    methods 
       method mtOpening(atGateState = 1) 
       method mtClosing(atGateState = 0) 
    end_methods 
end_fbe 
fbe RemoteControl 
    attributes 
        integer atRemoteStatus 0 
    end_attributes 
    methods 
        method mtReset(atRemoteStatus = 0)          
    end_methods 
end_fbe 
 
inst 
    Gate gate 
    RemoteControl remote 
end_inst 
strategy 
    no_one 
end_strategy 
 
rule rlOpeningGate 
    condition 
       subcondition subOpening 
              premise prRCOn remote.atRemoteStatus == 1 and 
              premise prGateIsClosed gate.atGateState == 0     
        end_subcondition 
    end_condition 
    action 
        instigation inReset1 remote.mtReset();  
        instigation inOpening gate.mtOpening(); 
    end_action 
end_rule 
rule rlClosingGate 
    condition 
       subcondition subClosing 
              premise prRCOn remote.atRemoteStatus == 1 and 
              premise prGateIsOpened gate.atGateState == 1 
       end_subcondition 
    end_condition 
    action 
        instigation inReset2 remote.mtReset(); 
        instigation inClosing gate.mtClosing();        
    end_action 
end_rule 
 
main { 
       for (int i = 0; i < 1000; i++) { 
              remote_atRemoteStatus::setValue(1); 
              printf("iteração: %05d\n",i);} 
} 
Fonte: Autoria Própria 


104 
 
 
O Código 7 representa, portanto: 
 Da linha 1 até a linha 9 é definida a FBE Gate, que representa a base de 
fatos do portão. Nesta está definido, nas linhas 2 a 4, o Attribute atGateState, 
do tipo inteiro (integer), que conterá o estado atual do portão (1 simboliza o 
portão aberto e 0 simboliza o portão fechado). Nas linhas 5 a 8 estão 
declarados os Methods responsáveis pela ação de abertura e fechamento 
do portão, sendo mtOpening e mtClosing respectivamente.  
 Entre as linhas 11 e 17 está contido o código que define a FBE 
RemoteControl, responsável pelo controle do portão eletrônico. A linha 13 
apresenta a definição do Attribute atRemoteStatus, do tipo inteiro, que simula 
o pressionamento do botão no controle, onde 1 representa “botão 
pressionado” e 0 representa “botão não pressionado”. A linha 16 apresenta 
a definição do Method mtReset, que implementa a ação de zerar o 
pressionamento do botão de controle de abertura. 
 Da linha 19 à 22 são definidas as instâncias de FBE. Neste exemplo apenas 
uma instância de cada FBE é criada.  
 A linha 27 apresenta o código de início da Rule que fará o controle da 
abertura do portão. Internamente são implementadas as entidades ligadas à 
Rule, que são as Conditions e Subconditions, Premises, Actions e 
Instigations. Essencialmente, por meio de Premises, o código da linha 30 
valida o pressionamento do botão do controle e verifica se o portão está 
fechado. Em caso verdadeiro, as Instigations definidas farão a chamada ao 
Method mtReset(), da FBE RemoteControl, e ao Method mtOpening(), da 
FBE Gate.  
 Seguindo os mesmos padrões, a Rule para controle do fechamento do 
portão é implementada entre as linhas 39 a 50. 
 Entre as linhas 52 e 56, o código principal é implementado diretamente na 
linguagem alvo. No exemplo se utilizou a linguagem C++. 
Na LingPON 1.0, uma FBE é composta por duas partes. A primeira parte 
representa a declaração dos Attributes. Tais estrutura possuem uma estrutura formada 
pelo tipo do dado, seguido do nome do Attribute e seu respectivo valor inicial. Os tipos 
de dados disponíveis na LingPON 1.0 são boolean, integer, float, char e string.  


105 
 
 
A segunda parte, por sua vez, representa a declaração dos Methods. Utiliza-se 
a palavra reservada method seguida do nome e sua respectiva funcionalidade. 
Adicionalmente, a LingPON 1.0 abre a possibilidade ao desenvolvedor adicionar código 
nativo da LingPON 1.0 alvo do compilador ao bloco de código do method definido entre 
as palavras reservadas begin_method e end_method. 
A declaração do conhecimento lógico-causal da aplicação se dá por meio de 
Rules, compostas por três partes: Properties (bloco opcional), Condition (expressão 
lógica) e Action (execução). O bloco Properties da Rule pode ser composto por duas 
propriedades, sendo a propriedade Priority e a propriedade Keeper.  
Uma Condition é formada por, no mínimo, uma Subcondition, seguida de um 
identificador (mesmo para a composição de expressões simples). A construção de uma 
Subcondition necessita de ao menos uma Premise. No caso da utilização de mais de 
uma Premise, estas devem ser aninhadas com conjunções (AND). Para utilização de 
disjunções (OR) em uma Rule, é necessária a criação de duas ou mais Subconditions. 
Para a definição de Premises na LingPON 1.0, a palavra reservada premise 
deve ser utilizada, seguida de um nome (opcional) e uma comparação. Ainda, pode ser 
aplicada à Premise a propriedade Attribute Impertinente, adicionando a palavra 
reservada imp após o identificador da Premise. 
O bloco Action, que representa a execução da Rule, é iniciado a partir da 
palavra-chave action. Este bloco consiste no vínculo de instigações aos Methods 
definidos nos FBE. A estrutura da Instigation é composta pela palavra-chave instigation 
seguida de um nome (opcional) e um método de uma instância particular de um FBE. 
3.3.2.2 Compilador do LingPON 1.0 
À luz do discutido sobre a teoria de linguagens e compiladores na seção 2.2, 
após a criação do código duas etapas precisam ser executadas, nomeadamente a 
compilação e síntese, sendo que a compilação envolve a análise léxica e a análise 
sintática. Assim, naturalmente após e criação do código em LingPON 1.0, ocorre a 
respectiva compilação (com suas análises) e síntese (ou geração de código alvo) no 
âmbito da tecnologia LingPON 1.0. 
Na tecnologia LingPON 1.0, à luz do método MCPON, para compor analisador 
léxico na compilação, foi utilizada a ferramenta Flex/Lex. A entrada do programa 
Flex/Lex é um arquivo contendo tokens definidos e reconhecidos com a utilização de 
expressões regulares. Desta forma, esta ferramenta produz um módulo de software de 


106 
 
 
varredura que pode ser compilado e acoplado a outros módulos, como o módulo de 
análise sintática. Ao seu turno, o analisador sintático é feito por meio da ferramenta 
Bison. Tal ferramenta é um programa que, baseado em uma gramática livre de 
contexto, constrói um programa C/C++ que analisa um arquivo de entrada (código) de 
acordo com as regras gramaticais (FERREIRA, 2015). 
A etapa de síntese foi criada a partir de uma aplicação em C++ que incluem os 
códigos gerados através das ferramentas Flex/Lex e Bison. Nesta etapa são utilizadas 
as informações interpretadas e validadas nas etapas anteriores, com o intuito de gerar 
um código alvo que execute a aplicação de acordo com o modelo PON. Tal aplicação 
gera códigos em três alvos: código especifico para Framework PON C++ 2.0, código 
específico PON para a linguagem C++ e código específico PON para a linguagem C 
(FERREIRA, 2015). A Figura 25 apresenta um diagrama de atividades UML, contendo 
as etapas de compilação LingPON. 
Figura 25 – Diagrama de atividades UML: etapas da Compilação LingPON 
Analisador Léxico
Flex/Lex
Analisador Sintático
Bison
Síntese
Componentes 
Compilador PON
Compilador PON
Compilar 
Linguagem C
Compilar
Linguagem C++
Compilar
Framework PON
Entrada de código-
fonte em LingPON 
 
Fonte: Autoria Própria 
A fim de validar a tecnologia LingPON 1.0, Ferreira (2015) realizou 
experimentos com duas aplicações: Mira ao Alvo, que consiste na implementação do 
tradicional jogo de mira ao alvo onde as entidades do tipo mira interagem com as 
entidades do tipo alvo; e Sistema de Vendas, consistindo em uma tradicional aplicação 
CRUD (acrônimo inglês de Create, Read, Update e Delete). Os experimentos 
contemplaram comparações de desempenho, quantidade de linhas do código gerado 
em Assembly (no caso do PON a partir da linguagem alvo C ou C++) e o uso de 
memória. Os códigos-fonte elaborados basearam-se em Framework PON C++ 2.0, 
PON para C++, PON para C e também PI C++. Adicionalmente, analisou-se um tanto 
a facilidade de programação de aplicações PON entre a linguagem PON e o Framework 


107 
 
 
PON C++ 2.0, por meio de experimentos em termos de linhas de códigos, número de 
tokens, além de relatos de desenvolvedores que usaram as duas abordagens 
(FERREIRA, 2015). 
Os resultados de tais experimentos mostraram que, o código gerado pelo 
compilador em PON C apresentou melhores resultados quanto ao seu desempenho, 
fez menos uso de memória e gerou um código Assembly com menor número de linhas 
se comparados às demais implementações PON. Consequentemente, o código gerado 
em PON C apresentou a menor complexidade dentre todos. 
Outrossim, na comparação dos resultados entre às implementações PON com 
as aplicações equivalentes construídas em PI C++, os resultados obtidos com código 
específico PON C foram ainda melhores do que a comparação citada no parágrafo 
anterior, ou pelo menos apresentaram resultados equivalentes ao código específico 
PON C++ (FERREIRA, 2015). 
Uma versão da LingPON denominada LingPON 1.2 StaticCPP, possui 
compilação para a linguagem C++, gerando, porém, código totalmente estático. Nesta 
versão, os elementos PON são implementados em C++ na forma estática (static) e “em 
linha” (inline) (SCHÜTZ; RONSZCKA, 2015). Tal versão apresentou melhor 
desempenho do que a versão PON C++. O relatório completo é apresentado no Anexo 
D do presente trabalho sendo essa versão em questão uma contribuição técnica para 
o grupo no âmbito deste presente esforço de pesquisa. 
Em suma, nesta versão LingPON 1.2 StaticCPP, tais técnicas específicas para 
aceleração do código gerado foram utilizadas: 
 Uso de métodos e funções em-linha (inline): Tais códigos são tratados como 
uma definição de macros para o compilador. Assim, a chamada da função é 
substituída pelo corpo (ou código) da função declarada. É extremamente 
eficiente para funções pequenas, pois evita a geração de código para 
chamada e retorno da função. Todas as funções e métodos são declarados 
e implementados no arquivo .h, ou seja, não há mais o arquivo específico 
.cpp contendo os códigos-fonte da implementação. 
 Todos os elementos são estáticos (static): nesta forma de declaração, todos 
os objetos compartilham um mesmo espaço de armazenamento, tornando 
sua troca de informações mais veloz. Consequentemente, toda a informação 
se tornou global na aplicação. 


108 
 
 
 Cada entidade PON se tornou uma classe: como agora tudo se tornaria 
estático, definiu-se que cada elemento PON seria uma classe específica. 
Este processo não ficou natural, pois implementações com muitos elementos 
geram vários arquivos na mesma pasta, dificultando o processo de busca. 
Porém, visando facilitar qualquer monitoramento, a nomenclatura utilizada 
na nomeação dos arquivos buscou um padrão isonômico e intuitivo. 
Mesmo que os códigos gerados via LingPON 1.2 StaticCPP sejam mais velozes 
do que as versões tradicionais da linguagem, há a limitação de acesso a elementos que 
não sejam estáticos. Assim, as aplicações não têm acesso a métodos e atributos não 
estáticos, inviabilizando alguns modos de programação e integração com códigos ou 
bibliotecas outras em C/C++. Neste contexto, Athayde; Negrini (2016) idealizaram a 
LingPON 1.2 Namespaces, onde a implementação das entidades PON em C++ baseia-
se no conceito de Namespaces. Tal solução possui códigos de alta performance, assim 
como na versão StaticCPP, podendo utilizar código não-estático (ATHAYDE; NEGRINI, 
2016). 
Isto posto, é notável a contribuição da LingPON, bem como das versões de 
Framework apresentadas, para a evolução na implementação de aplicações em 
software segundo os preceitos do PON. Em tempo, Santos (2017) apresenta aplicações 
em software feitas com o PON10, salientando Tecnologia LingPON, com respectivos 
trabalhos, inclusive a sua complexa aplicação de controle de futebol de robôs 
simulados.11  
Entretanto, duas características intrínsecas do PON, decorrentes da sua 
implícita característica de alta coesão e desacoplamento, que são paralelização e 
distribuição, não têm sido contempladas nas materializações já abordadas neste 
documento. Neste contexto, a fim de viabilizar tais elementos do PON, esforços têm 
sido efetuados em nível de software e hardware. As seções 3.3 e 3.4 abordam tais 
materializações.  
3.3.3 Paralelização e Distribuição via PON em Software 
Quanto à paralelização e distribuição via PON em software, alguns esforços 
são apresentados nesta seção. Weber et al. (2010) especializaram o Framework PON 
 
10 Aplicações essas cujos trabalhos estão listados em Simão (2017).  
11 Atualmente, a tecnologia PON 2.0, considerada uma nova versão do MCPON bem como de sua 
linguagem e compilador, são tratados no âmbito da tese de doutorado de Adriano Francisco Ronszcka. 
Como ainda não totalmente conformada, não foi utilizada no âmbito da presente tese. 


109 
 
 
C++ 1.0 (BANASZEWSKI, 2009) por meio da proposta de um ambiente multithread para 
execução concorrente dos elementos presentes no modelo de notificações do CON. 
Nesta as entidades CON (Rule, Condition, Premise etc.) podem executar cada qual em 
uma thread em particular. Contudo, tal solução não foi adicionada nas materializações 
atuais do PON de maneira explicita. Conquanto, Belmonte et al. (2012) utilizaram tal 
ambiente para decisões tomadas em desenvolvimento subsequente.   
Neste trabalho, Belmonte et al. (2012) estenderam a implementação do 
Framework PON C++ 2.0 C++ (RONSZCKA, 2012), incluindo a execução de Rules por 
meio de threads independentes (BELMONTE, 2012). Neste contexto, a extensão do 
Framework PON C++ 2.0 por meio de threads, intitulada de Framework PON C++ 3.0, 
fornece uma maneira (via uma camada adicional) de paralelizar elementos PON em 
múltiplos núcleos, de forma transparente (BELMONTE et al., 2016).  
As principais classes que implementam os elementos PON no Framework PON 
C++ 2.0 foram mantidas, sendo que algumas classes foram criadas para suportar o 
mecanismo multi-threaded quando disponível. A Figura 26 apresenta os pacotes 
adicionais do Framework PON C++ 3.0 e sua relação com os pacotes mantidos da 
versão 2.0. 
Figura 26 – Diagrama de Pacotes em UML do Framework PON C++ 3.0 
 
Fonte: Belmonte et al., 2016. 


110 
 
 
Conforme apresentado, o pacote NOPVectorMulticore contém especializações 
da estrutura NOPVECTOR. Essencialmente, a estrutura NOPVECTOR atua como um 
agente iterativo sobre as entidades PON de uma maneira otimizada, reduzindo o uso 
do cache de dados do aplicativo. As demais classes pertencentes ao pacote Multicore, 
são responsáveis por: 
 SynchronizedQueue: classe que implementa uma estrutura de dados na 
forma de uma fila, onde são armazenadas entidades PON a serem 
executadas, de forma síncrona, em cada um dos núcleos de um 
processador. 
 CoreControllersManager: responsável por criar uma instância da classe 
CoreController para cada núcleo da máquina de destino. Além disso, durante 
a execução do aplicativo, essa classe registra as notificações enviadas para 
cada entidade PON relevante. 
 CoreController: classe responsável por enfileirar entidades do PON quando 
a classe CoreControllerManager registra uma notificação. Também é 
responsável pela execução simultânea das Premises, Conditions, 
Instigations e Methods em cada núcleo de processamento. 
 SleepCondition: tal classe possui métodos que auxiliam no controle da fila 
de execução de entidades PON. São utilizados métodos relevantes da 
classe <pthread> de maneira controlada. 
 Thread: as instâncias dessa classe são usadas como fluxos de execução. 
Nesta classe proprietária, os métodos da exclusão mútua da classe 
<pthread> são usados de maneira controlada. 
 <pthread>: esta classe, pertencente à biblioteca C da linguagem GNU, 
possui todas as primitivas para a criação, controle e destruição de fluxos de 
execução em ambientes multicore, baseados no sistema operacional Linux. 
Conforme já apresentado, os métodos dessa classe são utilizados de forma 
controlada em outras classes do pacote Multicore, visando a correta 
distribuição da execução nos núcleos de processamento da máquina alvo. 
Com relação ao controle de threads e seus respectivos núcleos de execução, 
cada FBE instanciada no aplicativo está relacionada a uma instância da classe 
CoreController. A classe CoreControllerManager, por sua vez, instancia cada uma das 
FBE do aplicativo em um núcleo específico. Assim, as entidades da cadeia de 


111 
 
 
notificação são distribuídas entre os núcleos da máquina de destino de forma 
controlada. 
A fim de respeitar a execução correta das entidades PON em cada núcleo de 
processamento, a classe CoreController possui uma fila de entidades a serem 
executadas. Assim, uma entidade notificada vai para esta fila de execução e, assim que 
um núcleo do processador esteja disponível, uma entidade é removida da fila e 
executada. A Figura 27 apresenta o fluxo de controle de execução no Framework PON 
C++ 3.0, a partir de um diagrama de atividades UML. 
Figura 27 - Diagrama de atividade UML: fluxo de controle das entidades PON no Framework PON C++ 3.0 
 
Fonte: SCHÜTZ et al., 2018. 
Como pode ser visto, o diagrama de atividade da UML na Figura 27 é dividido 
em duas faixas: 
 a primeira faixa mostra a sequência de atividades da thread principal. Nota-
se, portanto, que há a criação das threads e a espera pela sua conclusão 
(join). Quando a thread principal recupera o controle, as threads criadas são 
destruídas. 


112 
 
 
 a segunda faixa representa cada uma das threads criadas no aplicativo, 
dividida em duas partes: 
o Processo de execução da entidade: inicialmente, uma instância da 
classe CoreController verifica se existe alguma entidade na fila. Esse 
processo se repete até que algum elemento seja enfileirado. Se houver 
algum elemento, uma entidade é retirada da fila, e suas ações são 
executadas. Ao final, pode haver o envio de uma notificação a outras 
entidades, ou seu encerramento. 
o Processo 
de 
gerenciamento 
de 
fila: 
conforme 
apresentado 
anteriormente, as entidades reativas do PON notificam-se durante a 
execução do processo de inferência. Nesse contexto, assim que o 
gerenciador de controle de núcleos (CoreControllerManager) recebe 
uma notificação, a entidade-alvo da notificação é adicionada à fila. Ao 
final, um sinal de ativação (wake) é enviado para a instância do 
controlador de núcleo (CoreController) a fim de retirar tal entidade da fila 
e executá-la. 
Como mencionado anteriormente, o Framework PON C++ 3.0 usa uma API que 
implementa o modelo de execução Posix Threads (pthreads), API esta cf. (“IEEE 
(POSIX)”, 2000). Tal API fornece um conjunto de bibliotecas com recursos de controle 
e sincronização de threads, por meio dos conceitos de exclusão mútua (mutex) para 
controlar o acesso e a execução de entidades compartilhadas, entre as múltiplas 
threads criadas (BELMONTE et al., 2016; SCHÜTZ et al., 2018). 
O Framework PON C++ 3.0 possui os métodos necessários, conforme 
apresentado em Belmonte (2012), que visa organizar o balanceamento da execução 
de um software de forma automática, sem a intervenção explícita do desenvolvedor. 
Ainda, o processo de alocação de entidades em múltiplos núcleos é transparente para 
o desenvolvedor. A única mudança no código usado em entidades PON, em relação ao 
código fonte do Framework PON C++ 2.0, é a especificação do núcleo de execução 
para cada entidade a ser utilizada. 
Por fim, resultados obtidos demostraram que há melhora no aproveitamento da 
capacidade de processamento disponível na plataforma estudada que utiliza múltiplos 
núcleos (multicore) (BELMONTE et al., 2016).  


113 
 
 
3.3.4 Framework PON Elixir/Erlang 
Erlang é uma linguagem de programação, em conjunto com um sistema para 
sua execução. Neste contexto, a máquina virtual Erlang permite programação em alto 
nível, compilação e execução concorrente. Tal concorrência ocorre de forma natural, 
tão natural quanto desacoplado forem os módulos visados, devido às características de 
desacoplamento da linguagem Erlang12 que, aliada à arquitetura multicore da máquina 
virtual BEAM disponibilizada pela arquitetura Erlang/OTP, permitem o uso de seus 
métodos de balanceamento  (RONSZCKA, 2019; NEGRINI et al., 2019). 
Isto posto, visando uma execução de programas PON em máquinas multicore, 
com maior qualidade frente ao Framework PON C++ 3.0, foi criado o Framework PON 
Elixir/Erlang (NEGRINI et al., 2019). Tal Framework PON Elixir/Erlang foi construído 
pelo mapeamento de elementos PON para elementos com comportamento de atores, 
uma vez que a linguagem Elixir é baseada no Paradigma Orientado a Atores (NEGRINI 
et al., 2019). 
Quanto ao paradigma, a linguagem Erlang segue os princípios do Paradigma 
Funcional (PF) em conjunto com o Paradigma Orientado a Atores (POA), sendo que o 
POA pode ser visto como um sistema de agentes. Nesse âmbito, Negrini fez uma 
modelagem de cada uma das entidades PON principais na forma de micro atores 
(RONSZCKA, 2019; NEGRINI et al., 2019). A Figura 28 apresenta um diagrama da 
tradução dos elementos PON em atores. 
Figura 28 - Modelagem os elementos PON em POA. 
 
Fonte: Negrini et. al, 2019. 
Para a codificação dos elementos PON mapeados para elementos com 
comportamentos de atores optou-se pela utilização da linguagem Elixir. Tal escolha se 
 
12A linguagem Erlang possui seu próprio heap e pilha, ao invés de fornecer encadeamentos 
que compartilham memória. Assim, cada processo é executado em seu próprio espaço de memória, com 
heap e pilha prórpiios. Ademais, os processos em execução não podem interferir uns com os outros 
inadvertidamente, característica comum em outros modelos de multithreading, que acarretam em 
deadlocks e outros problemas comuns à programação concorrente (NEGRINI et al., 2019). 


114 
 
 
deve à proximidade de tal linguagem à plataforma Erlang, e ainda por disponibilizar 
mecanismos essenciais para a programação estruturada (NEGRINI et al., 2019). A 
Figura 29, ilustra a arquitetura da solução proposta. 
Experimentos foram efetuados e seus resultados são apresentados no trabalho 
de Negrini (NEGRINI et al., 2019). Nestes é possível verificar que, conforme aumenta-
se o número de núcleos para um mesmo programa PON, o tempo de execução é 
reduzido. Ademais, um balanceamento efetivo de carga de processamento, entre os 
núcleos de execução, pode ser verificado durante toda a execução do experimento. 
Neste contexto, o Framework PON Elixir/Erlang permite a paralelização transparente e 
eficiente dentro da arquitetura proposta. 
Figura 29 - Arquitetura da compilação para Erlang/Elixir 
 
Fonte: Negrini et al., 2019. 
3.3.5 PON em Hardware  
Com o intuito de executar aplicações concebidas seguindo o modelo PON de 
maneira mais fidedigna ao paralelismo, vislumbrou-se a materialização do PON em 
hardware. Assim técnicas, modelos de circuitos e estruturas arquiteturais de hardware 
foram propostas, permitindo a construção de ambientes nos quais o mecanismo de 
notificações possa executar, de fato, em paralelo. Tais proposta também objetivam 
minimizar questões de overhead presente nas soluções propostas em software. 
A primeira proposta de materialização de uma aplicação PON em hardware, foi 
feita por Witt et al. (2011), em cujo trabalho foi proposto um conjunto de circuitos 


115 
 
 
sequenciais/combinacionais que implementam as entidades PON em hardware 
(PORDEUS et al., 2016; SIMÃO et al., 2012b; WITT et al., 2011). Tal modelo é 
conhecido como PON-HD prototipal, sendo que tais circuitos podem ter suas 
interconexões sintetizadas em FPGAs, de forma a implementar a cadeia de notificações 
do PON para cada aplicação em específico. Dada a pequena complexidade do 
funcionamento de cada uma das entidades do PON, estas podem ser modeladas em 
hardware como blocos lógicos (AND, OR, NOT) e blocos sequenciais (latches e flip-
flops) (WITT et al., 2011) 
A Figura 30 apresenta os blocos componentes de uma aplicação PON-HD. Tais 
aplicações são implementadas em lógica reconfigurável por meio de mapeamento 
direto dos elementos da cadeia de notificações, e dos Methods do PON em hardware. 
Porém, nesse ambiente há uma dependência de que a aplicação PON seja 
implementada diretamente em linguagem de descrição de hardware (PORDEUS et al., 
2016; SIMÃO et al., 2012b; WITT et al., 2011). 
Figura 30 - Modelo de execução do PON em hardware 
 
Fonte: Autoria Própria 
Segundo tal modelo, a execução da cadeia de notificações depende 
exclusivamente da propagação de sinais digitais entre os circuitos que representam 
cada elemento da cadeia de notificações PON. Esta propagação pode ocorrer de forma 
paralela (depende da quantidade de conexões), portanto permitindo a ocorrência do 
paralelismo intrínseco previsto no PON. Além disso, as propagações das notificações 
ocorrem em um nível de implementação efetivamente baixo (propagação de sinais 
síncronos no circuito gerado), fazendo com que a performance nesta abordagem seja 
superior ao desempenho nas abordagens na forma de software.  
Em um primeiro experimento, Witt et al. (2011) propuseram a comparação de 
dois simuladores de sistema de telefonia, ambos implementados em hardware. Neste 
contexto de experimentos, um dos sistemas criado foi baseado na abordagem da POO 
e outro baseado em PON (LINHARES et al., 2011). Como resultado da comparação 
dos simuladores, quanto aos resultados qualitativos, a solução PON foi mais intuitiva e 
Modelo da Aplicação 
PON
Hardware Description 
Language (VHDL)
Aplicação + 
Componentes PON
Field Programmable 
Gate Array (FPGA)


116 
 
 
fácil de ser composta em hardware do que a solução baseada em POO. Outrossim, a 
performance da solução PON foi melhor do que a solução POO (WITT et al., 2011). 
Neste 
âmbito, 
tais 
resultados 
se 
deram 
pelas 
características 
de 
desacoplamento das entidades do PON, que permitem uma execução paralela, e desta 
forma, a implementação em hardware traz potenciais ganhos de desempenho em 
relação a implementações convencionais realizadas puramente em software (WITT et 
al., 2011).  
Mesmo que veloz, paralela e com potencial descrição em alto nível, a 
abordagem em PON-HD possui certa limitação de escalabilidade, pois mapeia os 
elementos da cadeia de notificações de determinada aplicação para instâncias dos 
circuitos digitais correspondentes em hardware. Assim cada uma dessas instâncias 
consome uma determinada quantidade de elementos lógicos (LE – Logic Elements) 
disponível no dispositivo FPGA, limitando assim a quantidade de instâncias pela 
capacidade de do dispositivo FPGA, em termos de LE (KERSCHBAUMER et al., 2015; 
PORDEUS et al., 2016). Ainda, cada mudança na aplicação requer uma reconfiguração 
do FPGA, o que diminui a flexibilidade no uso desta abordagem em relação ao modelo 
em software (o qual têm seu código binário simplesmente carregado da memória para 
a plataforma em execução) (LINHARES, 2015). 
Visando mitigar tais deficiências, bem como buscar o desenvolvimento de uma 
solução efetiva que explore o potencial do PON diretamente sintetizado em hardware, 
pesquisas com PON-HD foram retomadas conforme trata a seção 3.3.6. 
3.3.6 Tecnologia LingPON-HD  
Para desenvolver uma nova solução em de PON-HD 1.0, foi proposta um 
Framework PON-HD 1.0, no qual as entidades do PON foram implementadas por meio 
de componentes VHDL, diferentemente do PON-HD prototipal, onde eram descritas de 
forma monobloco (KERSCHBAUMER, 2017, 2018).  
Para a implementação das entidades PON em VHDL, criou-se um componente 
VHDL para cada elemento no Framework PON-HD 1.0. Optou-se pela implementação 
dos componentes em VHDL pela grande compatibilidade com as ferramentas de 
síntese existentes no mercado. O modelo teórico-estrutural do PON utiliza entidades 
que devem ser implementadas fisicamente e outras que podem ser classificadas como 
entidades conceituais, não sendo necessária sua implementação de forma ‘física’ no 
Framework PON-HD 1.0. Neste contexto, tanto a entidade FBE quanto a entidade Rule 
não possuem correspondentes físicos nesta materialização.  


117 
 
 
A Figura 31 apresenta o diagrama de blocos em SysML com os elementos do 
PON que não possuem correspondentes físicos no Framework PON-HD 1.0 
diferenciados dos demais por meio de marcações com a palavra “Conceptual”, e com 
as bordas tracejadas. Conforme apresentado na Figura 31, portanto, são fisicamente 
implementadas em VHDL as entidades facto-execucionais Attributes, Methods e 
Actions, bem como as entidades lógico-relacionais Condition e Premises. Tais 
entidades são implementadas como componentes genéricos, podendo ser 
parametrizadas por meio da entidade VHDL generic (KERSCHBAUMER, 2017, 2018). 
Figura 31 - Diagrama de blocos em SysML de entidades PON  
em hardware utilizados no Framework PON-HD 1.0 
 
Fonte: Kerschbaumer, 2018  
Além do Framework PON VHDL 1.0, o trabalho de Kerschbaumer (2018) 
contribuiu para a evolução da LingPON para a LingPON-HD 1.0 (primeiro prototipal e 
depois 1.0) e, particularmente, do compilador PON para geração de código em 
Framework PON VHDL 1.0. Neste âmbito, o compilador recebe como entrada um 
código escrito em linguagem LingPON-HD 1.0 e devolve um código VHDL, à luz do 


118 
 
 
Framework PON-HD 1.0, utilizando seus componentes na descrição do circuito final 
(KERSCHBAUMER, 2018). 
Este conjunto de Framework PON VHDL 1.0, LingPON-HD 1.0, respectivo 
compilador e elementos de suporte foram conjuntamente chamados de Tecnologia 
PON-HD 1.0. A Tecnologia PON-HD 1.0 foi uma nova solução e ferramental 
desenvolvidos, focando também na resolução de conflitos e no desempenho do circuito 
gerado. Como resultado, desenvolveu-se uma solução que permite desenvolver 
hardware digital com de regras em alto nível, utilizando a filosofia do PON, por meio da 
Tecnologia LingPON-HD (KERSCHBAUMER, 2018). 
A fim de verificar as funcionalidades da implementação de hardware digital via 
Tecnologia PON-HD 1.0, experimentos foram conduzidos e apresentados em tese de 
doutoramento de Kerschbaumer (2018). Tais experimentos envolvem um contador 
decimal simples, um contador decimal de três dígitos, um ordenador de dados Odd 
Even Sort, um controlador para robô hexápode e um controlador de esteiras para 
transporte de caixas (KERSCHBAUMER, 2018). Nestes experimentos, a nova 
abordagem PON apresentou desempenho, frequência de clock e quantidade de 
elementos lógicos equivalentes à abordagem puramente em VHDL usando técnicas 
usuais de desenvolvimento. 
Em outros experimentos efetuados, Kerschbaumer (2018) comparou o 
resultado das implementações feitas com LingPON-HD 1.0 com a ferramenta HLS 
Vivado. Neste contexto, houve o desenvolvimento de um driver para display de sete 
segmentos, cálculo de média de valores, e um controlador PID. Com relação aos 
resultados, Kerschbaumer (2018) aponta que: 
O ferramental PON-HD 1.0 tem uma grande vantagem com relação a 
estruturação do algoritmo, pois a linguagem LingPON-HD 1.0 permite uma 
descrição intrinsicamente paralela das aplicações, isso pela própria natureza 
do PON. O Vivado HLS por sua vez, não permite “pensar em paralelo” ou 
“alcançar intrinsicamente paralelismo efetivo”, uma vez que utiliza linguagens 
tradicionais de programação na descrição das aplicações (KERSCHBAUMER, 
2018, p. 167).  
Em tempo, a pesquisa de Kerschbaumer (2018) é aqui destacada pois, dentre 
as metas do modelo computacional NeuroPON está a geração de código VHDL para 
treinamento e operação de RNA em dispositivos FPGA. Ainda, como ferramental de 
alto nível de abstração, o PON-HD 1.0 permite que desenvolvedores com poucos 
conhecimentos sobre hardware reconfigurável, ou mesmo sobre circuitos digitais, 
sintetizem circuitos por meio de regras de alto nível (KERSCHBAUMER, 2018). Enfim, 
o desenvolvimento orientado por componentes, utilizando as premissas do PON, 
apresenta maior nível de abstração em relação à abordagem de desenvolvimento 


119 
 
 
puramente em VHDL. Tais características são de grande valia para a implementação 
do NeuroPON a partir de linguagem descritiva declarativa de alto nível. 
Outrossim, além das materializações do PON em software e em hardware, 
permitindo sua utilização prática, há uma série de outros esforços no tocante ao PON. 
Neste contexto, um ferramental que auxilie do processo de engenharia, tendo artefatos 
de modelagem que permitam chegar melhor aos artefatos de execução, é  tradado na 
seção 3.3.6. 
3.3.7 Desenvolvimento Orientado a Notificações (DON) 
Segundo Wiecheteck (2011), embora o emprego convencional da UML e 
processos conhecidos no desenvolvimento de aplicações PON seja possível, as 
especificidades do PON motivam o uso mais particularizado de linguagens de 
modelagem e processos de software. Neste contexto, o DON (Desenvolvimento 
Orientado a Notificações) objetiva orientar projetistas na construção de projetos de 
software baseados em PON. 
Os modelos desenvolvidos no método são: modelo de classes, modelo de 
estados de alto nível, modelo de componentes, modelo de sequência, modelo de 
comunicação e modelo de Redes de Petri (MENDONÇA, 2015). O diagrama de 
atividades UML da Figura 32 ilustra os oito passos do método DON. 
Destaca-se ainda que o DON foi uma primeira abordagem de engenharia de 
software do tocante ao PON, permitindo algum ganho em termos de modelagem. A 
título de exemplo, a  Figura 33 apresenta um diagrama de componente para uma Rule, 
sendo que, no formato apresentado, o diagrama de componentes é uma contribuição 
pertinente do DON aos processos de desenvolvimento de software. 
 
 
 
 
 
 
 
 
 
 
 


120 
 
 
Figura 32 -  Diagrama de Atividades UML: representação do DON por meio de  
suas atividades e ciclos de desenvolvimento 
 
Fonte: Mendonça et al., 2015. 
Figura 33 - Diagrama de componente de uma Rule 
 
Fonte: Mendonça, 2016. 


121 
 
 
Segundo Mendonça et al. (2015), o método DON abrange atividades 
relacionadas aos requisitos e análise e projeto de softwares em PON, sendo aderente 
aos processos tradicionais de desenvolvimento de software. Neste contexto e 
entretanto, como ainda dependente da UML, a análise realizada com DON não 
beneficia como um todo a descoberta das regras no PON. Assim, o processo de 
identificação de regras torna-se um intenso processo de síntese e requer muito esforço 
do desenvolvedor (MENDONÇA et al., 2015). 
Visando amenizar tais deficiências do DON, Mendonça (2016) propôs uma 
Metodologia de Projeto de Software Orientado a Notificações (NOM). Nesta 
metodologia, a orientação a regras, fatos e notificações considerados desde os 
primeiros níveis de modelagem (MENDONÇA, 2016).  
Ainda, em outro avanço relacionado ao desenvolvimento de aplicativos de 
software em PON, Kossoski (2015) propôs um método de teste para projetos de que 
empregam o PON no seu desenvolvimento. Este método foi desenvolvido para ser 
aplicado nas fases de teste unitário e teste de integração.  Como parte deste método, 
Kossoski (2015) desenvolveu o Diagrama de Instâncias do PON, sendo que tal 
diagrama pode ser utilizado para representar as entidades que compõem o sistema. 
Assim, o desenvolvedor pode ter uma visão gráfica sobre o ciclo de notificações dos 
elementos envolvidos na aplicação. Segundo Kossoski (2015), caso seja necessário, o 
desenvolvedor poderá isolar elementos que realizam determinados processos no 
sistema, com o objetivo de facilitar análises específicas de fluxo de execução. A Figura 
34 apresenta a notação dos elementos da cadeia de notificações PON utilizada no 
diagrama de instâncias PON. 
Figura 34 - Elementos do diagrama de instâncias do PON 
 
Fonte: Kossoski, 2015. 


122 
 
 
A correlação entre os elementos da cadeia de notificações e sua representação 
no diagrama de instâncias é dada por: 
 FBE é representada como um objeto retangular.  
 Attribute é representado como um triângulo.  
 Premise é representada como um losango.  
 Rule é representada com um objeto que desencadeia um fluxo de execução 
em um sentido. Considerou-se Condition como parte integrante da 
respectiva Rule.  
 Method é representado como uma engrenagem. 
 O sentido das notificações é representado como uma seta. 
O diagrama de instâncias do PON foi aqui destacado pois é utilizado no 
Capítulo 4, na própria definição do modelo computacional NeuroPON e mesmo na 
representação dos experimentos decorrentes, apresentando os elementos do modelo 
computacional NeuroPON de uma forma mais fidedigna à cadeia de notificações PON. 
A Seção 3.3, portanto, objetivou a apresentação das materializações e 
processos de desenvolvimento que iniciaram o PON no desenvolvimento de software, 
de hardware, e na própria modelagem de sistemas computacionais. Não obstante, as 
tecnologias abordadas, bem como o próprio PON, vêm sendo evoluídos por diversos 
esforços do grupo de pesquisadores do PON. Ainda que a maioria destas aplicações 
foram desenvolvidas no âmbito acadêmico, algumas têm complexidade razoável 
conforme detalha o trabalho de Santos (2017), e permitiram a aplicação do PON em 
diferentes domínios de aplicação. Isto dito, tais evoluções conceituais são assunto da 
seção 3.4. 
3.4 Considerações sobre o PON 
Como um paradigma relativamente novo, que vem evoluindo desde a tese de 
Simão (2001, 2005), o PON é uma alternativa aos paradigmas de programação 
vigentes (e.g. PI e PD). Com o intuito de resolver algumas das principais deficiências 
dos atuais paradigmas de programação, tais como redundâncias estruturais e 
temporais, bem como os acoplamentos daí decorrentes, o PON apresenta uma nova 
forma de estruturar e executar artefatos de software (SANTOS, 2017). 


123 
 
 
Neste contexto, o PON permite criar aplicações de forma mais natural, em alto 
nível, pois tem inspiração na forma declarativa (e.g. fatos e regras) de programação. 
Ainda, o inovador mecanismo de notificações do PON, permite execução não (estrutural 
e temporalmente) redundante e minimamente acoplada de aplicações. Composto por 
pequenas entidades computacionais reativas, as quais colaboram por meio de 
notificações precisas e pontuais, um código baseado em PON tende a aproveitar 
melhor o sistema hospedeiro. 
Quanto às formas de se utilizar o PON para a construção de sistemas, 
materializações em software e hardware foram produzidas, conforme apontado na 
seção 3.3.   
Particularmente, aprimoramentos realizados na Tecnologia LingPON (i.e., 
LingPON e compilador) foram importantes para os experimentos do presente trabalho. 
A idealização da versão StaticCPP permitiram que uma RNA MLP fosse implementada 
em LingPON, sendo que os detalhes da implementação encontram-se no próximo 
capítulo. Ainda, a já citada Tecnologia LingPON-HD (KERSCHBAUMER, 2018) tem 
fundamental importância para o modelo computacional NeuroPON, conforme será 
tratado no decorrer desse documento de tese. 
A seguir, o Capítulo 4 apresenta o modelo computacional NeuroPON partindo 
de seus requisitos até sua implementação, bem como experimentos realizados a fim de 
demonstrar as hipóteses da presente tese. 
 
 


124 
 
 
4 Modelo Computacional NeuroPON 
Neste capítulo é apresentado o desenvolvimento do modelo computacional 
NeuroPON. Na sequência, são apresentados os primeiros experimentos realizados 
com o Framework PON C++ 2.0 na construção de RNA, seguidos por experimentos 
utilizando a LingPON com compilação específica para StaticCPP. Neste âmbito, os 
primeiros experimentos foram efetuados em materializações voltadas à geração de 
software, com processamento monocore, os quais permitem o vislumbre do 
funcionamento do modelo computacional. 
O presente capítulo também apresenta implementações que visam a execução 
em múltiplos núcleos de processamento (multicore). Neste âmbito, um experimento 
com o Framework PON C++ 3.0 é apresentado. Ademais, o uso da tecnologia PON-HD 
1.0, desenvolvida por Kerschbaumer (2018), é utilizada para o experimento do modelo 
computacional NeuroPON em hardware reconfigurável. 
 Ainda, outras atividades correlatas desenvolvidas durante o período de 
doutoramento, e que se mostraram fundamentais para o desenvolvimento do modelo, 
são apresentadas: modificações na LingPON e Compilador para a geração de código 
específico StaticCPP, bem como ajustes no Framework PON C++ 3.0 e compilador 
LingPON-HD. Tais modificações foram necessárias para acomodar o NeuroPON e, por 
consequência, evoluir tais materializações.  
4.1 Modelo computacional NeuroPON: requisitos 
Com base nos objetivos desta pesquisa de doutoramento, os requisitos 
necessários para a concepção do modelo computacional NeuroPON foram levantados 
e estão descritos na presente seção. A Tabela 5 apresenta os requisitos funcionais do 
NeuroPON, sendo que todos vêm de encontro ao objetivo específico três, que trata do 
desenvolvimento do modelo computacional orientado a notificações para RNA.  
Tabela 5 - Requisitos Funcionais do modelo computacional NeuroPON 
RF-01 
O NeuroPON deve permitir a especificação de uma RNA a partir de uma 
linguagem de alto nível. 
RF-01.1 
A especificação de RNA poderá ser feita via linguagem declarativa descritiva 
baseada em linguagem de especificação de RNA. 


125 
 
 
RF-02 
O NeuroPON deve gerar código para plataforma(s) visada(s) para efetuar o 
treinamento e operação da RNA criada. 
RF-02.1 
O código gerado deve ser não redundante de acordo com o PON. 
RF-02.2 
O código gerado deve  ser desacoplado, permitindo processamento paralelo 
quando a plataforma assim o permitir. 
RF-02.3 
O código gerado deve permitir acesso individual a cada uma das neuro-
entidades implementadas, permitindo que alterações pontuais sejam efetuadas, 
se necessário for. 
RF-03 
O NeuroPON deve possuir um compilador próprio, a fim de gerar código para 
treinamento, teste e execução da RNA gerada em NeuroLingPON para 
plataformas (e.g. linguagens e frameworks)  que venham a ser homologadas. 
RF-04 
O NeuroPON deve gerar arquivos com a parametrização final da RNA.  
Fonte: Autoria Própria 
Por fim, a Tabela 6 apresenta os requisitos não funcionais do modelo 
computacional NeuroPON. 
 Tabela 6 - Requisitos Não Funcionais do modelo computacional NeuroPON 
RNF-01 
O NeuroPON deve ser implementado utilizando os conceitos do PON 
RNF-02 
Os arquivos devem ser importados e exportados no formato XML v.1.0 
RNF-03 
A compilação de Código NeuroPON poderá ser efetuada nas seguintes 
materializações e seus respectivos compiladores: LingPON 1.2 
StaticCPP, LingPON-HD 1.0 VHDL, Framework PON C++ 2.0, e 
Framework PON C++ 3.0. 
Fonte: Autoria Própria 
Tais requisitos foram definidos a partir do contexto deste trabalho, 
principalmente quanto aos objetivos já apontados. Na Seção 4.2, a seguir, são 
apresentadas as etapas do modelo computacional NeuroPON.  
4.2 Modelo computacional NeuroPON: etapas para geração de código 
Para apresentar os processos envolvidos no desenvolvimento de RNA 
utilizando o modelo computacional NeuroPON proposto, a Figura 35 apresenta um 
esquema com as etapas, desde a descrição da RNA por meio de linguagem de 
descrição de RNA, até a geração dos códigos de treinamento e operação na linguagem 
escolhida.  
 


126 
 
 
Figura 35 – Diagrama de Atividades em UML: apresentação do processo de geração de RNA  
por meio do modelo computacional NeuroPON 
 
Fonte: Autoria Própria 
No esquema apresentado na  Figura 35, portanto, as seguintes etapas são 
propostas para o modelo computacional NeuroPON, visando suprir os requisitos 
descritos na Tabela 5: 
1. Especificar a RNA em Linguagem Declarativa Descritiva: na primeira etapa, 
o usuário/desenvolvedor informa os parâmetros da RNA por meio de uma 
Linguagem de Especificação de RNA descritiva, que segue o padrão XML 
.  
2. Verificar opção para geração de código: Nesta atividade há a verificação 
da opção de geração de código para execução direta em hardware 
reconfigurável ou software em máquinas von Neumann. 
2.1. Gerar NeuroLingPON: caso a opção escolhida seja cpp, LingPON 1.2 
StaticCPP será a materialização utilizada como base para a geração 
de código, de acordo com as regras da LingPON e do modelo 
computacional NeuroPON. 
2.2. Gerar NeuroPON-FW: caso a opção escolhida seja fw, haverá o 
processo de geração de código baseado nas regras de Framework 
PON C++ 3.0 multithreads e do modelo computacional NeuroPON. 
3. Gerar NeuroLingPON-HD: caso a opção escolhida seja a de gerar código 
a ser executado diretamente em hardware reconfigurável, a etapa de 
geração de código efetua a compilação dos códigos-fonte para 
implementação da RNA em VHDL, seguindo as regras da tecnologia 
LingPON-HD e NeuroPON, visando a execução em dispositivos FPGA. 


127 
 
 
Uma vez gerados os arquivos com os códigos-fonte para execução e 
treinamento da RNA, basta executar a compilação dos mesmos por meio de 
compiladores apropriados para cada linguagem e plataforma visada. 
A Seção 4.3 apresenta o funcionamento do modelo computacional NeuroPON, 
por meio da descrição das entidades logico-causais e facto-execucionais tanto dos 
neurônios quanto da própria RNA em si. Tais entidades são, a partir deste, nomeadas 
de neuro-entidades.   
4.3 Modelo computacional NeuroPON: funcionamento 
Conforme já apontado, o modelo computacional NeuroPON permite a 
construção de RNA do tipo Multi-Layer Perceptron (MLP) de acordo com as diretrizes 
do PON, utilizando para treinamento o método Backpropagation (BP), porém com 
entidades neurais (neuro-entidades) notificantes. Neste contexto, o modelo 
computacional NeuroPON se propõe justamente a ser uma alternativa computacional 
para o desenvolvimento de RNA.  
Assim, após análises sobre a teoria das RNA, especificamente quanto à 
arquitetura MLP e ao treinamento BP, foram definidos os artefatos necessários para se 
desenvolver a RNA com código notificante, desacoplado e não redundante. 
Inicialmente, duas FBE em PON foram definidas para o desenvolvimento da aplicação, 
com seus Attributes notificantes e seus Methods instigáveis. Essas duas FBE são a 
FBE Network e a FBE Neuron. Subsequentemente foram definidas as Rules, 
Conditions, Premises, Actions e Instigations pertinentes e relacionadas13. Esses 
elementos são apresentados nas subseções que seguem. 
4.3.1 Neurônio em NeuroPON 
Conforme visto na Seção 2.4.2 (página 64), o valor de saída de um neurônio 
deve ser o resultado de cálculos efetuados entre valores de entrada e dos pesos de 
cada ligação sináptica entre este e outros neurônios a ele conectados. Sobre tal 
funcionamento, definiu-se que uma entidade Neuron em PON é composta por uma FBE 
Neuron (com conjunto de Attributes e Methods), por, no mínimo, uma Rule (com sua 
Condition e Actions) com, no mínimo, duas Premises e uma Instigation. Nestes termos, 
 
13 A nomeação das entidades PON no texto estão escritas em Inglês, visando seguir o padrão 
adotado pelo grupo de pesquisas a ser seguido em todas as publicações relacionadas a PON e suas 
derivações. 


128 
 
 
como uma Rule sempre terá tal composição no controle das etapas do modelo 
NeuroPON, tal entidade é nomeada como uma NeuroRule. 
A necessidade de se ter uma Premise específica, contendo um valor booleano 
em todas as Conditions de uma NeuroRule, deve-se ao fato de que, na tecnologia PON-
HD, uma vez que uma Premise for ativada pelo resultado positivo de sua avaliação 
lógico-causal, as Instigations a ela relacionadas em uma Rule serão sempre instigadas, 
devido à sua implementação em VHDL. Neste contexto, devido à lógica de 
implementação do NeuroPON em LingPON, alguns Methods eram executados sem 
necessidade, gerando resultados diferente dos esperados para a RNA. 
 A Tabela 7 apresenta os elementos PON que compõem uma neuro-entidade 
Neuron (neurônio) em NeuroPON. 
Tabela 7 - Definição de um Neurônio em NeuroPON - Entidade Neuron 
Entidade Neuron 
FBE Neuron 
Attributes 
Methods 
<tipo_pon> attOutput  
boolean [attDone] || [atStepN … ] 
<tipo_pon> attWeightNM … 
[mthCalcN()] || 
[mtProdN() … 
mtSumN() … 
mtFuncN()] 
NeuroRule 
rleCalcN … 
Premises 
Instigations 
[Neuron->attDone == <true,false>] 
[Neuron->atStepN == <true, false> …] ||  
[Network->atStepN == <true, false>] 
insXN … 
Fonte: Autoria Própria 
Na notação utilizada para a definição do neurônio na Tabela 7, os três pontos 
(...) logo após a definição da entidade, juntamente com a letra N em sua identificação, 
indica que pode ser necessário uma ou mais delas na definição do neurônio; os 
colchetes ([ ]), juntamente com as barras paralelas (||), indicam que pode aparecer um 
ou outro conjunto de elementos em cada entidade. Tais características dependem da 
quantidade de neurônios necessários, bem como na materialização PON escolhida 
para implementação da RNA. 
Naturalmente, à luz da teoria do PON, a FBE Neuron possui Methods e 
Attributes, sendo que estes últimos notificam Premises relacionadas a Condition de 
uma NeuroRule. Uma NeuroRule aprovada ou ativada em termos neurais, executa sua 
Action, sendo que esta ativa Instigation(s) que, aos seus turnos, instigam Method(s) de 
FBE, executando assim a cadeia de notificações. 


129 
 
 
A neuro-entidade Neuron definida, com seus dados apresentados na Tabela 7, 
é genérica, podendo ser especializada para atuar tanto como um neurônio de uma 
camada escondida quanto um neurônio de uma camada de saída. Neste caso, outros 
Attributes podem ser adicionados, porém os definidos como padrão são: 
 <tipo_pon> attOutput: representa o valor de saída do neurônio. O tipo pode 
variar de acordo com a implementação entre integer e float. 
 <tipo_pon> attWeightN: tais Attributes representam as ligações sinápticas 
entre neurônios, armazenando assim o valor do peso de tal conexão no 
contexto da RNA. A quantidade de tais Attributes é variável, pois devem ser 
definidos quantos forem necessários, a fim de contemplar todas as ligações 
sinápticas necessárias. O tipo pode variar, de acordo com a implementação, 
entre integer e float. 
 boolean [attDone || atStepN]: tais Attributes lógicos são utilizados para a 
sincronização e controle dos cálculos entre os neurônios de uma camada, 
bem como entre as próprias camadas.  
O funcionamento de um neurônio em NeuroPON é baseado em Attributes de 
controle. Tais Attributes são utilizados para controlar a sequência das etapas de cálculo 
intra-neuronais, bem como a sincronização dos cálculos intra e entre camadas. 
Conforme já apontado, tanto na fase de propagação quanto de retro-propagação, em 
RNA MLP com treinamento BP, é necessária uma sincronização entre as camadas, 
pois o valor dos neurônios é cascateado entre elas. Neste sentido, um neurônio da 
camada N necessita, em seus cálculos, o valor de saída dos neurônios da camada N-
1 a ele conectados via sinapses artificiais. 
Devido a tais requisitos de RNA MLP com treinamento BP, as materializações 
em software possuem um Attribute attDone, do próprio neurônio, e um Attribute externo, 
attClock, que pertence à FBE Network, relativo à RNA como um todo, a ser detalhado 
subsequentemente. Assim, quando o Attribute attDone for falso (false) e o Attribute 
attClock for igual a dois (indicando assim que o neurônio não está em processo de 
computação, e que a etapa atual de processamento da RNA é a segunda etapa), uma 
Instigation é ativada, que por sua vez instiga o Method mthCalc(), que executa os 
cálculos do neurônio. O Method mthCalc() ainda atualiza Attributes da própria entidade 
Neuron. 
Na materialização em hardware reconfigurável, que utiliza a tecnologia 
LingPON-HD, permite apenas Methods que implementem uma única operação com, no 


130 
 
 
máximo, dois parâmetros. Neste contexto, as etapas de cálculo são divididas em vários 
Methods, fazendo com que mais entidades PON sejam utilizadas para o 
desenvolvimento NeuroPON em hardware. A fim de exemplificar e comparar os 
cálculos em materializações de software e hardware, o Código 8 apresenta dois 
códigos-fonte de exemplo da implementação dos processos de cálculo de uma neuro-
entidade Neuron, tanto em software quanto em hardware. 
Código 8 - Código da implementação de um neurônio em NeuroPON: (a) representação utilizando LingPON 
em software; (b) representação utilizando LingPON-HD em hardware 
(a) Neurônio em Software (LingPON) 
09 
10 
11 
12 
13 
14 
15 
... 
method mthCalc() begin_method  
    atSumProd = ((net.atI0 * atW00) + (net.atI1 * atW01)); 
    atSumProd = atSumProd + atBias; 
    atOutput = tanh(atSumProd); 
end_method 
... 
 
(b) Neurônio em Hardware (LingPON-HD) 
09 
10 
11 
12 
13 
14 
15 
... 
method mtProdI0(atProdI0 = net.atI0 * atW00) 
method mtProdI1(atProdI1 = net.atI1 * atW01) 
method mtSumProd(atSumProd = atProdI0 + atProdI1) 
method mtSumBias(atSumProd = atSumProd + atBias) 
method mtTanH(atOutput = atSumProd ~ 8) 
... 
Fonte: Autoria Própria 
Pode-se observar, portanto, que no código da parte (a) do Código 8, todo o 
processo de cálculo de um neurônio é efetuado em um Method, sendo que no Código 
8 parte (b) são apresentados cinco Methods para executar tal processo de cálculo. 
Ainda, como a versão em software permite a utilização da linguagem C++ para a 
definição de Methods, o cálculo referente à função de ativação Tangente Hiperbólica 
foi efetuado por meio da função tanh(). Em hardware, porém, a tangente hiperbólica foi 
implementada por meio de quantização e lookup table14. Assim,   diferentemente das 
operações matemáticas convencionais apresentadas nos Methods das linhas 10 a 13, 
o Method mtTanH(), apresentado na linha 14 do Código 8, possui um caractere ‘~’, 
representando a função de ativação tangente hiperbólica. 
Pode-se generalizar uma entidade Neuron com os elementos apresentados na 
Tabela 7, variando-se apenas quantidade de cada elemento, porém mantendo sua 
 
14 Maiores detalhes sobre a implementação da função TanH() em hardware reconfigurável são 
apresentados na Seção 5.7. 


131 
 
 
essência. Neste contexto, a quantidade gerada de tais elementos é diretamente 
proporcional à materialização a ser utilizada, bem como da quantidade de entradas, de 
camadas, e de neurônios por camadas, parametrizados, via linguagem declarativa 
descritiva, no momento da implementação da RNA.  
Por fim, para uma melhor visualização da entidade Neuron, um diagrama é 
apresentado na Figura 36, utilizando os conceitos do diagrama de instâncias do PON. 
Tais conceitos são utilizados pois as entidades PON FBE e NeuroRule, com suas 
subentidades reativas e notificantes, não são idealmente representadas em um 
diagrama de classes da UML. Neste contexto, o trabalho de Kossoski (2015) propôs e 
Mendonça (2016) endossou uma representação gráfica de objetos PON (conforme já 
apresentado na Seção 3.3.7 página 119), demonstrando assim as entidades que 
compõem um sistema. 
Figura 36 – Diagrama de instâncias PON: estrutura de um neurônio em NeuroPON 
 
Fonte: Autoria Própria 
Além de apresentar os objetos PON pertencentes ao modelo, o diagrama da 
Figura 36 apresenta o sentido do fluxo de notificações (representado pelas setas) em 
cada uma das entidades. Neste contexto, a cada modificação nos Attributes 
relacionados à esquerda no modelo, as Premises são notificadas. Em caso de 
aprovação das Premises e, por consequência, das Conditions relacionadas, as 
NeuroRule são ativadas. Por fim, com a notificação de Action e Instigations pertinentes, 
os Methods são executados, modificando assim os Attributes, relacionados à direita no 
modelo. 
Dois novos componentes do diagrama de instâncias PON propostos neste 
presente trabalho são apresentados na Figura 36: a Condition, representada por um 


132 
 
 
hexágono, e a NeuroRule, representada pelo retângulo com cantos arredondados. Tais 
contribuições foram necessárias para acomodar as modificações efetuadas pelo 
modelo 
computacional 
NeuroPON. 
Neste 
contexto, 
conforme 
já 
apontado 
anteriormente, uma NeuroRule apresenta-se como uma Rule diferenciada, contendo os 
elementos necessários à representação, tanto em software quanto em hardware, da 
entidade neurônio. Tais elementos são: 
 Condition contendo uma ou mais Premises com Attributes de controle; e 
 Action contendo uma ou mais Instigations aos Methods pertinentes. 
Por fim, no modelo apresentado na Figura 36, a Premise com contornos 
pontilhados indica que, além das Premises de controle relacionadas à Attributes da FBE 
Neuron, podem haver Premises relacionadas a Attributes da FBE Network no controle 
de cada entidade Neuron.  
4.3.2 RNA em NeuroPON 
Após a definição da entidade Neuron, a devida definição da RNA foi elaborada. 
A Tabela 8 apresenta, portanto, os elementos de tal definição. 
Tabela 8 - Definição de uma RNA em NeuroPON - Entidade Network 
Entidade Network 
FBE Network 
Attributes 
Methods 
integer attNumEpochs 
integer attTotTrainInputs 
integer attReadTrainInputs 
[integer attClock || boolean atStepN] 
<tipo_pon> attLR 
<tipo_pon> attMomentum 
<tipo_pon> attInput … 
<tipo_pon> attOutPred … 
<tipo_pon> attErrorPattern 
<tipo_pon> attErrorEpoch 
mthNetStart() 
[mthGetValues()] 
mthDoneN() 
[mthCalcOverallError()] || 
[mtStepN()] 
mtNextLayer() 
mthRaiseEpoch() 
Rule rleNetStart 
Premises 
Instigations 
Sincronizar e controlar as 
épocas de treinamento. 
attNumEpochs > 0 
insNetStart 
Rule rleNetGetValues 
Premises 
Instigations 
Controlar a leitura dos 
padrões de treinamento. 
attReadTrainInputs < attTotTrainInputs 
insNetGetValues 
Rule rleNetRaiseEpoch 
Premises 
Instigations 
Controlar o processamento de 
camadas.  
attReadTrainInputs >= attTotTrainInputs && 
[attClock || atStepN] 
insNetRaiseEpoch 
Rule rleNetNeuronsDone 
Premises 
Instigations 


133 
 
 
Regrar a sincronização entre 
neurônios de determinada 
camada. 
NeuronN->attDone … && 
[Network->attClock ] ||[Network->atStepM …]  
insNetRNeuronsDone … 
Rule rleNetCalcOverallError 
Premises 
Instigations 
Controlar o ajuste dos pesos 
sinápticos a partir do erro 
calculado. 
[Network->attClock] || [Network->atStepM] 
insNetCalcOverallError … 
inStepMethodM 
Rule rleNetUpdateWeights 
Premises 
Instigations 
Iniciar a atualização de pesos 
sinápticos. 
[Network->attClock] || [Network->atStepM] 
insNetUpdateWeightsNM ... 
Fonte: Autoria Própria 
A estrutura base e o funcionamento de uma RNA em NeuroPON, representada 
pela FBE Network e Rules relacionadas, são os mesmos para qualquer materialização 
do PON. Não obstante, da mesma forma como na descrição de uma entidade Neuron, 
os Attributes de controle de etapas variam entre as implementações em software e 
hardware, devido à forma de operação dos Methods (conforme apresentado 
anteriormente na definição da entidade Neuron).  
Isto dito, uma RNA em NeuroPON a partir das entidades PON apresentadas na 
Tabela 8, possui a seguinte descrição quanto aos seus Attributes: 
 integer attNumEpochs – armazena a quantidade de épocas a serem 
executadas. Tal Attribute, do tipo inteiro (integer), é utilizado para iniciar o 
processamento da cadeia de notificações, além de ser utilizado como 
condição de parada do treinamento; 
 integer attTotTrainInputs – Attribute, do tipo inteiro, que contém a quantidade 
total de entradas de treinamento; 
 integer attReadTrainInputs – Attribute, do tipo inteiro, que contém a 
quantidade de entradas de treinamento já lidas. Ele é utilizado para controlar, 
em conjunto com o Attribute attTotTrainInputs, a leitura de todos os padrões 
de treinamento durante uma época; 
 [integer attClock] || [boolean atStepN] – Attributes utilizados para 
sincronização dos processos da RNA. No caso de materializações que 
geram software, é utilizado o Attribute, do tipo inteiro, attClock, sendo que na 
materialização que gera descrição de hardware reconfigurável, é utilizado 
mais de um Attribute do tipo boolean; 
 <tipo_pon> attLR – taxa de aprendizagem (Learning Rate); 
 <tipo_pon> attMomentum – termo de momentum; 


134 
 
 
 <tipo_pon> attInput – contém o valor da entrada de treinamento. Este 
Attribute pode ser repetido quantas vezes for necessário; 
 <tipo_pon> attOutPred – contém o valor da saída prevista para determinada 
entrada de treinamento. Como o método de treinamento é supervisionado, 
as saídas são conhecidas, e devem ser utilizadas durante o treinamento; 
 <tipo_pon> attErrorPattern – armazena o erro quadrático em cada padrão 
de treinamento; 
 <tipo_pon> attErrorEpoch – armazena o erro médio em cada época de 
treinamento; 
Assim como já apresentado anteriormente (Seção 2.4 página 62), as RNA 
possuem duas fases ou modos de execução, nominadamente, a fase de treinamento e 
a fase de operação. Neste contexto, é importante separar as fases de forma explícita, 
no modelo NeuroPON, visando adaptar cada uma das fases de acordo com suas 
peculiaridades. 
Relativo ao funcionamento da RNA em NeuroPON no modo de operação, o 
processamento da cadeia de notificações é iniciado pelo ajuste do Attribute 
attReadTrainInputs para o valor zero, informando que nenhum padrão ainda foi lido. Tal 
ajuste dispara o processo de leitura do padrão a ser validado. Após a leitura do padrão, 
os processos relativos à propagação à frente (forward) são executados, tanto na 
camada escondida quanto na camada de saída. Por fim, o erro é calculado, frente às 
saídas esperadas, e o valor do Attribute attReadTrainInputs é atualizado, fazendo com 
que a próxima entrada seja lida ou o processo seja encerrado. A Figura 37 apresenta 
a estrutura da RNA em NeuroPON, no modo de operação, utilizando um diagrama de 
instâncias PON. 
No diagrama apresentado na Figura 37, as Conditions cdNetHNDone e 
cdNetONDone recebem linhas no formato de barramentos (linhas duplas), advindas da 
entidade Neuron. Tal diferenciação visa informar que a quantidade de Premises 
declaradas e pertencentes às referidas Conditions, depende diretamente da quantidade 
de instâncias da entidade Neuron conectadas, via sinapses notificantes, tanto à camada 
escondida quanto à camada de saída.  Neste contexto, caso uma RNA possua cinco 
neurônios na camada escondida, por exemplo, serão declaradas cinco Premises de 
controle em Condition e NeuroRule pertinentes. 
Outrossim, além de operacionalizar um RNA, um dos objetivos do modelo 
computacional NeuroPON é a de propor treinamento utilizando PON, tanto em software 


135 
 
 
quanto em hardware. A Figura 38 apresenta a estrutura da RNA em NeuroPON, no 
modo de treinamento, utilizando um diagrama de instâncias PON. 
Figura 37 - Estrutura de uma RNA em NeuroPON: modo de operação 
 
Fonte: Autoria Própria 
 O funcionamento de uma RNA em NeuroPON, no modo de treinamento, é 
baseado no ajuste inicial da quantidade de épocas, ou seja, do Attribute atNumEpochs. 
Assim que tal Attribute é ajustado, os valores do primeiro padrão de treinamento são 
lidos. Após a leitura do padrão, os cálculos dos neurônios da camada escondida e de 
saída são efetuados, tanto na fase de propagação quanto na fase de retro-propagação. 
Na sequência realiza-se a atualização dos pesos sinápticos por meio de valores 
baseados no erro de cada neurônio de saída. Por fim, é efetuado o cálculo do erro 
médio da RNA, e um novo padrão de treinamento é lido e atribuído às entradas da RNA, 
reiniciando assim o processo de treinamento da RNA. No caso de todos os padrões de 
treinamento já terem sido lidos e aplicados, o valor do Attribute atNumEpochs é 
ajustado e, caso atinja o número esperado e inicialmente informado, o treinamento é 
encerrado. Naturalmente, tudo isso guiado por um fluxo de notificações ou, melhor 
dizendo, de sinapses notificantes entre instâncias de entidades Neuron, bem como 
entre tais instâncias de entidades Neuron e Network. 


136 
 
 
Figura 38 - Estrutura de uma RNA em NeuroPON, no modo de Treinamento 
 
Fonte: Autoria Própria 


137 
 
 
Conforme já apontado, a diferença entre o modo de operação e o modo de 
treinamento de uma RNA é que no modo de operação ocorre apenas a primeira fase 
do treinamento pelo método BP, ou seja, a fase de propagação. Assim sendo, as fases 
de retro-propagação e atualização dos pesos são executadas no modo de treinamento 
da RNA. O controle destas fases é realizado pelas NeuroRules rlHNBackCalc e 
rlHNUpdWeights para as neuro-entidades de camadas escondidas, e pelas NeuroRules 
rlONBackCalc e rlONUpdWeights para as neuro-entidades da camada de saída. 
Os diagramas apresentados tanto na Figura 36, Figura 37 e Figura 38 
apresentam uma visão geral das entidades Neuron e Network, no modo de operação e 
no modo de treinamento. Tais diagramas apresentam as entidades separadamente, 
como de fato ocorre, mostrando o desacoplamento entre elas, que é um facilitador 
inclusive de paralelismo/concorrência e mesmo distribuição. Esses diagramas também 
apresentam as interconexões, aqui ditas sináptico-notificantes, entre entidades 
advindas do PON que permitem as notificações e as instigações (um tipo de notificação 
também) pertinentes entre eles.   
Tais diagramas, mesmo que permitam ter a noção da dinâmica que a aplicação 
terá em função de explicitar essas ditas interconexões sinápticas de notificação entre 
os constituintes, ainda assim não trás efetivamente a dinâmica de notificações de 
execução ali existente. Neste contexto, a Figura 39 apresenta a cadeia de notificações 
da aplicação de treinamento desenvolvida, utilizando um Diagrama de Atividades da 
UML como um modelo alternativo. 
A Figura 39 apresenta o funcionamento dinâmico da NeuroPON, por meio da 
cadeia de notificações PON. Neste contexto, o texto que segue descreve tecnicamente 
o exposto no diagrama de atividades em UML: 
1. A cadeia de notificações PON, bem como o treinamento da RNA, são 
iniciados pela mudança no Attribute que representa a quantidade de 
épocas. Assim, quando o valor do Attribute atNumEpochs é modificado, as 
Premises e Conditions pertinentes notificam a NeuroRule pertinente, que 
verifica se a quantidade de épocas é maior do que zero. Se verdadeiro, o 
Atrribute atReadTrainInputs é ajustado para zero, iniciando o processo de 
leitura de padrões de treinamento. Por fim, é verificado se o total de 
entradas lidas é menor que o total de entradas de treinamento. Caso isto 
seja verdadeiro, adquire-se os padrões de entrada por meio de entidades 
Rule-Action-Instigation pertinentes. 


138 
 
 
Figura 39 - Diagrama de Atividades em UML: cadeia de notificações do algoritmo de  
treinamento RNA MLP pelo método BP, utilizando PON 
 
Fonte: Autoria Própria 


139 
 
 
2. Após a leitura do padrão de treinamento e sua correta atribuição às 
entradas da RNA, o processo de cálculo deve ser disparado. Assim, 
Attributes de controle tanto da entidade Network quando das entidades 
HiddenNeuron (pertencentes à camada escondida), são ajustados.  
3. O processo de cálculo lógico-causal (e mesmo a sincronia de 
concorrências) neste contexto dado é regulado pelas NeuroRules 
pertinentes à fase de Forward Propagation (propagação), da entidade 
HiddenNeuron. Ainda, os Methods de cada neurônio serão executados por 
meio de notificações via entidades Condition-NeuroRule-Action-Instigation, 
se a conjunção entre as Premises pertinentes for verdadeira. 
4. Após a execução e todos os cálculos, os Methods pertinentes de cada 
instância da entidade HiddenNeuron modificam seus Attributes de controle, 
notificando 
assim 
as 
Premises 
envolvidas 
na 
NeuroRule 
rleNetNeuronsHDone, diretamente ligada à entidade Network. A conjunção 
verdadeira de tais Premises inicia os processos de cálculo da fase de 
propagação em cada entidade OutputNeuron, tendo como entrada os 
resultados das entidades HiddenNeurons. 
5. Os procedimentos adotados na implementação dos cálculos das entidades 
Neuron de saída são os mesmos dos utilizados na camada escondida 
intermediária. Assim, após os cálculos necessários à fase de propagação, 
bem como os cálculos relacionados à obtenção do erro em cada entidade 
Neuron de saída, iniciam-se os cálculos da fase Backpropagation (retro-
propagação). 
6. Antes de se iniciar o processo de atualização dos pesos sináptico-
notificantes da camada de saída, é necessário armazenar valores auxiliares 
à atualização dos pesos da camada escondida. Neste contexto, um 
controle por parte da própria RNA é requerido e representado pela entidade 
Network, para a execução (via Condition-NeuroRule-Action-Instigation) de 
Methods para tais cálculos.  
7. Na sequência, o processo de atualização dos pesos sináptico-notificantes, 
que ligam as entidades Neuron da camada de saída às entidades Neuron 
da camada escondida, é efetuado. Tais processos de atualização são 
executados de forma concorrente/paralela, sempre que o meio de 
execução assim o permitir.  


140 
 
 
8. Uma vez que os processos da fase de retro-propagação de OutputNeuron 
tenham sido executados, há uma sincronização de todos as entidades 
Neuron na entidade Network. Tal sincronização, via entidades PON 
pertinentes, dispara ainda o processo de notificação às entidades 
HiddenNeuron, visando iniciar a fase de retro-propagação na camada 
escondida intermediária. Neste contexto, assim como efetuado sobre as 
entidades Neuron da camada de saída, os processos de cálculo para 
atualização, e a própria atualização dos pesos sináptico-notificantes, é 
efetuada. 
9. Por fim, o controle é passado à entidade Network, que efetua verificações 
quanto à finalização do treinamento.  
9.1. Quando todas as entidades HiddenNeuron finalizaram seus cálculos, a 
NeuroRule pertinente é notificada e instiga o Method responsável pelo 
cálculo do erro geral da RNA, resultante do padrão de treinamento 
atual. De forma concorrente, inicia-se o processamento da próxima 
entrada de treinamento, por meio do incremento do Attribute 
atReadTrainInputs.  
9.2. Uma vez que o valor do Attribute atReadTrainInputs seja igual ao total 
de entradas de treinamento, o Attribute que contém a quantidade de 
épocas atNumEpoch é incrementado, paralelamente ao cálculo do erro 
médio da RNA e do ajuste do Attribute atReadTrainInputs, cujo valor 
passa a ser zero, reiniciando o treinamento numa nova época a partir 
da primeira entrada de treinamento. Caso contrário, o treinamento é 
reiniciado com a próxima entrada de treinamento. 
A fim de demonstrar o processo de treinamento no diagrama UML, a Figura 39 
não apresenta todos os processos PON executados na cadeia de notificações PON. 
Assim, são apresentados apenas o ajuste dos Attributes reativos por meio de Methods 
(atividades no diagrama). Tais Attributes, ao ter seu valor alterado, notificam as 
entidades pertinentes e, consequentemente, disparam o processo necessário na 
cadeia de notificações. Neste contexto, tais processos estão implícitos e representados 
por cada seta que liga as atividades no diagrama. 
Ainda, no diagrama da Figura 39, a abertura de concorrência nas entidades que 
representam os neurônios da camada escondida e da camada de saída, indica que o 
PON permite concorrência ou paralelismo se a plataforma assim permitir. Isso se dá 


141 
 
 
tanto no modo de treinamento, explicitado no diagrama da Figura 39, quanto no modo 
de operação. 
4.4 Considerações sobre o Modelo Computacional NeuroPON 
O presente Capítulo apresentou o desenvolvimento do modelo computacional 
NeuroPON Teórico, desde sua concepção por meio de seus requisitos até sua 
modelagem apresentadas por diagramas UML e diagramas próprios do PON. O 
NeuroPON surgiu de observações efetuadas sobre as sinapses artificiais de uma RNA, 
comparando-as com as notificações entre as entidades PON. Neste contexto, de forma 
hipotética, as sinapses poderiam ser representadas por notificações, e a cadeia de 
notificações em execução tornar-se-ia o processo de treinamento e operação de uma 
RNA.  
Ao evoluir a reflexão sobre tais hipóteses, aventou-se a possibilidade de que o 
Attribute envolvido em uma Premise poderia conter o valor de ativação de determinada 
ligação sináptica. Ademais, os Methods poderiam executar o processamento neuronal 
necessário para a geração de tal ativação e, por meio do ajuste de determinados 
Attributes pelos Methods, novas regras poderiam ser notificadas e ativadas. 
Por fim, as FBE poderiam representar as entidades neuronais, com seus 
Attributes e Methods pertinentes, sendo que as Rules poderiam reger o caminho de 
treinamento a ser tomado nesta RNA, avaliando quais sinapses seriam reforçadas e 
quais seriam atenuadas. Tudo isso, à luz do próprio PON, poderia ser avaliado e 
executado de forma paralela, caso a plataforma de execução assim o permitisse. 
Subsequentemente, em modo de operação da RNA, tais entidades PON tomariam 
papéis pertinentes para a execução sendo que certos FBE tratariam os dados de 
entradas notificando Rules que, por suas vezes, instigariam mudanças em outras FBE 
e assim por diante, criando algo como uma cadeia sináptica por notificações no seio da 
execução de RNA a luz do NeuroPON. 
A partir de tais hipóteses, o modelo computacional NeuroPON Teórico foi 
concebido, conforme apresentado no presente Capítulo. Neste contexto, observou-se 
a factibilidade do treinamento e da operação de uma RNA, no tocante ao 
desacoplamento implícito de entidades, à luz da teoria do PON. Entretanto, além do 
que já foi considerado até então, outras hipóteses puderam ser levantadas durante o 
processo de desenvolvimento do NeuroPON. Neste âmbito, o neurônio tornou-se uma 
entidade PON completa, com elementos facto-execucionais e lógico-causais 


142 
 
 
independentes, permitindo assim  o acesso singular a cada um dos componentes da 
RNA. 
Outrossim, uma vez que venha a ser implementada, a computação de todas as 
entidades Neuron declaradas poderia ser efetuada de forma concorrente e, até mesmo, 
com paralelismo, a partir de sua implementação por meio das materializações 
Framework PON C++ 3.0 em software, e LingPON-HD para hardware. Como já dito 
anteriormente nesta tese, é sabido que o PON permite o desacoplamento de forma 
implícita das entidades, fazendo com que grande parte do processo execute de forma 
concorrente (em termos do modelo computacional).  
Neste âmbito, almeja-se que a utilização do modelo computacional NeuroPON 
produza códigos que realmente aproveitem o potencial de processamento e, 
particularmente, paralelismo de cada plataforma utilizada: 
 No caso da utilização de máquinas sequenciais baseadas em Von Neumann 
que contenham apenas um núcleo de execução (monocore), haveria uma 
concorrência emulada em software, ou seja, uma sequencialização das 
atividades, sendo que a concorrência ficaria emulada dado ao sincronismo 
subsequente que ocorre no âmbito das NeuroRules. 
 Na utilização de plataformas multicore, ocorreria a distribuição do 
processamento das entidades entre os núcleos de execução deste 
microprocessador multicore, por meio da utilização do Framework PON C++ 
3.0, por exemplo; 
 Pela utilização de dispositivos FPGA, a Tecnologia LingPON-HD permitiria a 
criação de código VHDL totalmente paralelizado a ser executado em tais 
dispositivos. 
Ademais, o uso de uma linguagem descritiva para a parametrização da RNA 
facilitaria o uso do modelo computacional NeuroPON na concepção de RNA MLP. É 
certo que usuários com efetivo conhecimento técnico na descrição de hardware 
conseguiriam criar circuitos que implementem RNA de maneira eficiente e concorrente. 
Porém, no caso de uma mudança na quantidade de entidades neuronais, sejam estas 
de camada escondida ou de saída, todo o processo teria que ser feito manualmente, 
ao contrário da implementação por parametrização que o NeuroPON permitiria.  
Em suma, o modelo computacional NeuroPON proposto e modelado daria 
liberdade ao usuário escolher geração de código não-redundante (portanto eficiente) e 
desacoplado (potencialmente concorrente e paralelo) para software a ser executado 


143 
 
 
em plataformas monocore ou multicore e, particularmente, para dispositivos FPGA que 
seria o seu melhor nicho. Neste âmbito, a fim de demonstrar a implementação do 
modelo computacional NeuroPON Teórico, visando o NeuroPON Prototipal, a geração 
de código para materializações do PON em software e hardware foram efetuadas e 
testadas por meio de experimentos. Tais implementações, bem como seus resultados, 
são apresentados no Capítulo 5. 
 
 


144 
 
 
5 Implementações e Experimentos do modelo computacional 
NeuroPON 
Com o intuito de verificar se a aplicação de RNA em PON é, de fato, um 
processo 
viável, implementações do 
NeuroPON proposto e 
subsequentes 
experimentos foram realizados para tal. Tais implementações e experimentos foram 
efetuados utilizando materializações do PON tanto em software quanto em hardware, 
e são apresentados nas seções do presente Capítulo. A Tabela 9 apresenta, de forma 
resumida, as principais características de cada uma das implementações e dos 
experimentos a serem detalhados. 
Tabela 9 - Resumo dos experimentos desenvolvidos 
Experimento 
Materialização 
PON 
Base de Dados 
Padrões de 
treinamento 
Objetivo 
Estrutura das Camadas da RNA 
Pesos 
Entrada 
Escondida 
Saída 
Qtde 
Tipo de 
Dados 
Qtde 
Tipo de 
Dados 
Qtde 
Tipo de 
Dados 
1 
FW 
2.0 
XOR 
4 
Verificar a plausibilidade de 
se utilizar conceitos do 
PON para o 
desenvolvimento de uma 
RNA de forma declarativa, 
em alto nível, com geração 
de código implicitamente 
desacoplado. 
Real 
3 
Inteiro 
binário 
4 
Real 
1 
Real 
2 
FW 
2.0 
IRIS 
120 
Verificar a escalabilidade 
do algoritmo criado, como 
prova de conceito, no 
experimento 01. 
Real 
4 
Real 
5 
Real 
3 
Real 
3 
FW 
3.0 
IRIS 
120 
Verificar a plausibilidade de 
execução paralela, em 
múltiplos núcleos, das 
entidades do modelo 
Teórico NeuroPON. 
Real 
4 
Real 
5 
Real 
3 
Real 
4 
FW 
Elixir/Erlang 
XOR 
4 
Verificar a plausibilidade da 
implementação do modelo 
Teórico NeuroPON 
utilizando o Framework 
PON Elixir/Erlang. 
Inteiro 
2 
Inteiro 
2 
Inteiro 
1 
Inteiro 
5 
LingPON 
Static CPP 
IRIS 
120 
Verificar a plausibilidade da 
implementação do modelo 
Teórico NeuroPON 
utilizando a Tecnologia 
LingPON. 
Real 
4 
Real 
5 
Real 
3 
Inteiro  
6 
LingPON 
HD 
XOR 
4 
Verificar a plausibilidade da 
implementação do modelo 
Teórico NeuroPON 
utilizando a Tecnologia 
LingPON-HD. 
Inteiro 
2 
Inteiro 
2 
Inteiro 
1 
Inteiro 


145 
 
 
7 
LingPON 
HD 
IRIS 
120 
Verificar a escalabilidade 
do algoritmo criado, como 
prova de conceito, no 
experimento 05. 
Inteiro 
4 
Inteiro 
5 
Inteiro 
3 
Inteiro 
quantiz
ado 
Fonte: Autoria Própria 
Os experimentos aqui apresentados foram executados sobre uma RNA do tipo 
Multi-Layer Perceptron (MLP) com treinamento pelo método Backpropagation (BP). 
Neste contexto, para ilustrar tais processos de treinamento, bem como apresentar o 
código base utilizado para comparação com as implementações PON, o Apêndice B 
provê uma implementação utilizando o PI, e a Seção 5.1  apresenta uma discussão 
sobre tal implementação. O algoritmo desenvolvido é utilizado para o treinamento BP 
de uma RNA MLP tanto sobre a tabela verdade da função XOR, quanto sobre a base 
de dados IRIS Dataset.  
Por fim, os experimentos com materializações em software foram executados 
utilizando um microcomputador com processador baseado na tecnologia de von 
Neumann, Intel Core i5-3317U 1.7GHz 8GB de RAM, utilizando sistema operacional 
Windows, versão 10. A compilação foi efetuada no ambiente do terminal Cygwin versão 
2.5.1 64 bits, com o compilador GCC versão 5.3.0 e G++ 5.3.0. Já os experimentos com 
o LingPON-HD foram efetuados por meio do simulador MultiSim, da ferramenta Quartus 
II v.13 executando no mesmo microcomputador.  
5.1 RNA MLP com Linguagem C procedimental 
Para servir de base de comparação para os experimentos desenvolvidos por 
meio do NeuroPON, uma implementação tradicional, por meio da linguagem C/C++ 
procedimental, do algoritmo de treinamento BP para RNA MLP é apresentado no 
Apêndice A. O código desenvolvido, baseado em implementações tradicionais de RNA, 
utiliza laços de repetição nos cálculos para alcançar todos os valores nas matrizes, 
como é tradicional em abordagens baseadas em sequencialidade e na passividade dos 
elementos nas linguagens do PI. Assim, as linhas de código se tornam 
interdependentes, o que causa problemas de redundâncias temporais e estruturais na 
aplicação, dificultando assim o uso apropriado da capacidade computacional 
disponível.  
Ademais, como foi escrito de forma totalmente sequencial e acoplante, tal 
código não pode ser facilmente paralelizado. Assim, a divisão do código em pequenas 
partes (granularidade fina) para a realização de tarefas paralelas, é um processo 


146 
 
 
moroso e de difícil execução. O fator de (des)acoplamento é de fundamental 
importância no desenvolvimento de uma RNA em software. 
Por fim, mesmo que uma distribuição de código em granularidade fina, visando 
obter todas as vantagens dos recursos de processamento disponíveis, seja efetuada, 
tal tarefa depende do controle explícito do programador, não havendo mecanismos para 
facilitar 
a 
programação 
multiprocessada 
(BANASZEWSKI, 
2009; 
GRUVE, 
2007;SEVILLA et al., 2008). Em suma, uma abordagem matricial em PI para RNA é 
animada por laços de repetição usuais (loops), com as usuais redundâncias e 
acoplamentos inerentes já discutidas neste trabalho. Mesmo que se divida tal matriz 
em N partes e se paralelize (em CUDA15 ou FPGA por exemplo), ainda assim se terá 
laços de repetição com redundâncias e acoplamentos. Neste contexto, pode-se até 
mitigar o problema, porém não o resolver por completo. 
Uma versão modificada do algoritmo de treinamento foi desenvolvida, visando 
o treinamento de RNA restrita ao uso de valores inteiros, tanto nas entradas de 
treinamento, pesos sinápticos e valores de ativação dos neurônios. Os resultados do 
experimento com números inteiros, portanto, serão a base para comparação com 
outros dois experimentos implementados em hardware reconfigurável. 
Isto posto, visando superar as questões observadas em implementações PI, as 
próximas seções descrevem implementações de RNA MLP em PON, utilizando o 
método BP para treinamento. 
5.2 RNA MLP com Framework PON C++ 2.0: treinamento BP para a função 
XOR 
A presente seção apresenta a construção de uma RNA MLP, utilizando PON, 
com um algoritmo de treinamento pelo método BP. Tal implementação do algoritmo foi 
efetuada sobre o Framework PON C++ 2.0, conforme Ronszcka (2012), Valença et al., 
2011 e Ronszcka; Valença; et al. (2017). Neste contexto de Framework PON C++ 2.0, 
objetiva-se demonstrar a aplicabilidade do PON para o desenvolvimento de uma RNA 
declarativamente, em alto nível, permitindo solução implicitamente desacoplada à luz 
da implementação de tal Framework.  
A implementação do experimento segue as regras do modelo computacional 
NeuroPON. Em tempo, neste experimento, o NeuroPON é aplicado à classificação das 
 
15 CUDA é um modelo de programação e computação paralela, desenvolvido pela NVIDIA, para 
computação geral em unidades de processamento gráfico (NVIDIA, 2017). 


147 
 
 
possibilidades da tabela verdade da função XOR. A aplicação de tal função apresenta-
se como um exemplo clássico e simples para RNA do tipo MLP, porém é uma forma 
plausível de avaliar a construção, bem como a execução das fases de treinamento e 
operação de RNA em NeuroPON. 
5.2.1 Desenvolvimento da RNA 
Conforme apresentado na Seção 3.3.1, no Framework PON C++ 2.0 as 
entidades PON estão estruturadas na forma de classes/objetos, sendo relacionadas 
por meio de estruturas de dados.  Neste contexto, o pacote CORE contém tais 
entidades em forma de classes, que devem ser utilizadas na construção de aplicações 
baseadas em tal materialização. 
Assim, duas classes herdadas da classe FBE foram definidas para o 
desenvolvimento da aplicação, nomeadamente a classe Network e a classe Neuron. A 
Figura 40 apresenta um diagrama de classes em UML com o relacionamento entre tais 
entidades (advindas do PON) até então criadas. 
Figura 40 - Diagrama de Classes em UML: relacionamento entre as entidades FBE para a materialização do 
modelo computacional NeuroPON utilizando Framework PON C++ 2.0. 
 
Fonte: Autoria Própria 


148 
 
 
A classe (FBE) Network foi criada para efetuar o controle da RNA propriamente 
dita. Assim, tanto os Attributes quanto os Methods criados são utilizados para este fim. 
Neste âmbito, na classe que representa FBE Network, estão definidos os Attributes 
para controle da quantidade de épocas, de sincronização, do erro médio da RNA e a 
lista de instâncias de neurônios que a RNA pode conter. 
Por sua vez, na classe que representa a FBE Neuron, responsável por tratar 
explicitamente os neurônios da RNA, contendo os Attributes e Methods responsáveis 
por tratar parte das funcionalidades do neurônio. Neste sentido, em Neuron, são 
definidos os Attributes para as duas entradas do XOR, a entrada especial Bias e saída 
após o cálculo. Também são definidos os Attributes que contém os pesos das conexões 
sinápticas, bem como taxas de aprendizagem e erro médio. Ainda, há Attributes de 
controle e sincronização. Em tempo, as instâncias de FBE Neuron seriam 
particularmente interessantes, pois as notificações de seus Attributes que permitirão as 
sinapses neste modelo computacional alternativo, remontando a hipótese inicial desta 
pesquisa sobre o dueto notificação e sinapse. 
Ainda, devido ao uso do Framework NOP C++ 2.0, foi criada uma classe 
herdada da dita classe principal NOPApplication, sendo tal classe derivada aqui 
denominada NetworkSystem. Esta classe NetworkSystem contém os métodos 
necessários para coordenar as entidades constituintes da aplicação proposta de acordo 
com os princípios do PON.  
A estrutura do diagrama proposto na Figura 40 baseia-se na estrutura principal 
do Framework PON C++ 2.0. De fato, a aplicação para treinamento de uma RNA MLP 
com o método BP baseou-se no inter-relacionamento dos modelos do PON e do 
Framework PON C++ 2.0, representados portanto pela Figura 20 (página 93), pela 
Figura 23 (página 98) e pela Figura 40. A Seção 5.2.2 apresenta a codificação da 
aplicação da RNA MLP via Framework PON C++ 2.0. 
5.2.2 Codificação da RNA via Framework PON C++ 2.0 
O processo de codificação de aplicações utilizando o Framework PON C++ 2.0 
utiliza a sintaxe da linguagem C++. Neste contexto, a codificação de aplicações neste 
Framework é conduzida pela instanciação de classes e chamadas de métodos de 
classe, seguindo as restrições impostas pelas super classes do próprio Framework. 
Inicialmente, o Código 9 apresenta a declaração da FBE Neuron. Em tempo, o código 
apresentado representa a FBE como em uma classe na programação POO. Sua 
especialização é realizada na classe NetworkSystem, por meio da criação de instâncias 


149 
 
 
(neste caso, cinco instâncias são consideradas – quatro na camada intermediária e 
uma na camada de saída). 
Código 9 - FBE Neuron em código Framework PON C++ 2.0 
01 
02 
03 
04 
05 
06 
07 
08 
09 
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
class Neuron : public FBE { 
    public: 
        Integer *attInput01;    // entrada 01 
        Integer *attInput02;    // entrada 02 
        Integer *attInput03;    // attBias 
        Integer *attOutput;     // saída 
        Double *attWeightIH01;  // peso sináptico entrada 01 -> camada escondida 
        Double *attWeightIH02;  // peso sináptico entrada 02 -> camada escondida 
        Double *attWeightIH03;  // peso sináptico entrada 03 -> camada escondida 
        Double *attWeightHO;    // peso sináptico camada escondida -> saída 
        Double *attLR_HO;       // taxa de aprendizado de saída 
        Double *attLR_IH;       // taxa de aprendizado de entrada 
        Double *attHiddenVal;   // valor do neurôno na camada escondida 
        Double *attErrThisPat;  // erro no padrão atual 
        Double *attOutPred;     // saída atual de treinamento 
        Integer *attPatNum;     // número do padrão 
        Boolean *attDoCalc;     // controle de cálculo (sincronização) 
        Boolean *attDoWC;       // controle de cálculo de erro (sincronização) 
        Boolean *attDone;       // controle de processamento (sincronização) 
    public: 
        Premise *preCalcNet;          // Declaração de Premise 
        Premise *preWeightsChange;    
        Method *mthCalcNet;           // Declaração de Method 
        Method *mthWeightChanges; 
        RuleObject *rleCalcNet;       // Declaração de Rule 
        RuleObject *rleWeightsChange; 
    private: 
        void calcNet(); 
        void weightChanges(); 
}; 
Fonte: Autoria Própria 
Conforme já apresentado na Seção 3.3.1, tal código não precisa ser escrito de 
forma manual. O desenvolvedor pode utilizar a linguagem declarativa de alto nível 
LingPON e, posteriormente via compilador próprio do PON, fazer a tradução dos 
códigos-fonte da aplicação para o padrão utilizado no Framework PON C++ 2.0. Neste 
contexto, o Código 10 apresenta a codificação da Rule rleStart utilizando a LingPON. 
O Código 11 apresenta a Rule rleStart, responsável por descrever tal processo 
e as entidades PON a ela relacionadas, codificada utilizando a linguagem C++ e as 
regras do Framework PON C++ 2.0.  
 
 
 
 
 
 


150 
 
 
Código 10 - Definição da Rule rleStart em LingPON 
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
rule rleStart 
 
condition 
 
  subcondition sbcNetStart 
 
 
 premise preStart attNumEpochs > 0 and 
 
 
 premise preStartClk attClock == 0 
 
  end_subcondition 
 
end_condition 
 
action 
 
  instigation insNetStart net.mthStart(); 
 
end_action 
end_rule 
Fonte: Autoria Própria 
Código 11 - Configuração de Premises e Rules relacionadas à FBE Network -  
Framework PON C++ 2.0 - exemplo XOR 
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
// Criação da Rule que inicia o processo da cadeia de notificações (rleStart)  
RULE(rleStart, SingletonScheduler::getInstance(), Condition::CONJUNCTION); 
 
// Criação da Premise que verifica o Attribute attClock  
PREMISE(preStartClk, this->attClock, 0, Premise::EQUAL, Premise::STANDARD, false); 
// Criação da Premise que verifica o Attribute attNumEpochs 
PREMISE(preStart, this->attNumEpochs, 0, Premise::GREATERTHAN, Premise::STANDARD, false); 
// Coloca o endereço do método netStart() na entidade que representa o Method mthStart   
mthStart = new MethodPointer<Network>(this, &Network::netstart); 
// Faz o relacionamento entre as Premises e o Method com a Rule  
rleStart->addPremise(preStartClk); 
rleStart->addPremise(preStart); 
rleStart->addMethod(mthStart); 
Fonte: Autoria Própria 
Conforme apresentado no Código 10 e no Código 11, quando o valor do 
Attribute attNumEpochs é modificado, a Rule rleStart verifica, por meio das entidades 
Premise e Condition pertinentes, se o valor do Attribute attNumEpochs é maior do que 
zero, e se o valor do Attribute attClock é igual a zero. Assim, a partir da conjunção 
verdadeira das Premises preStartClk e preStart uma Condition é notificada, a Rule 
rleStart é validada, e, por meio de entidades Rule-Action-Instigation pertinentes, o 
Method mthStart é invocado, executando então as instruções designadas pelo seu 
código fonte.  
 Os códigos que definem as Rules, bem como os componentes necessários 
para o funcionamento da cadeia de notificações relacionadas à FBE Neuron, seguem 
a mesma sintaxe já apresentada no Código 11. Neste contexto, as entidades 
declaradas e apresentadas no diagrama de classes da Figura 40 são codificadas 
seguindo os mesmos conceitos apresentados. O Código 12 apresenta a implementação 
da Rule rleCalcNet, em LingPON.  
 


151 
 
 
Código 12 - Implementação da Rule rleCalcNet, utilizando LingPON 
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
// Rule que representa o comportamento de disparo do cálculo dos neurônios 
rule rleCalcNet 
 
condition 
 
  subcondition sbcCalcNet 
 
 
 premise preCalcNet attDoCalc == true  
 
  end_subcondition 
 
end_condition 
 
action 
 
  instigation insNetStart mthCalcNet(); 
 
end_action 
end_rule 
Fonte: Autoria Própria 
A Rule rleCalcNet envolve a Premise preCalcNet. Tal Premise avalia o Attribute 
attDoCalc que representa o estado da FBE Neuron. O Method mthCalcNet() de cada 
neurônio será executado por meio de notificações via entidades Condition-Rule-Action-
Instigation, se a Premise for verdadeira. O Código 13 apresenta o código do Method 
mthCalcNet(). 
Código 13 - Implementação, utilizando Framework PON C++ 2.0, do Method mthCalcNet() 
43 
44 
45 
46 
47 
48 
49 
50 
51 
void Neuron::calcNet() { 
    attHiddenVal->setValue(tanh(attInput01->getValue()*attWeightIH01->getValue() + 
                                attInput02->getValue()*attWeightIH02->getValue() + 
                                attInput03->getValue()*attWeightIH03->getValue())); 
    attOutPred->setValue(attHiddenVal->getValue()*attWeightHO->getValue()); 
    attErrThisPat->setValue(attOutPred->getValue()-attOutput->getValue()); 
    attDoCalc->setValue(false);     
    attDoWC->setValue(true);     
} 
Fonte: Autoria Própria 
Após a execução e todos os cálculos, o Method mthCalcNet() modifica o 
Attribute attDoCalc para falso (false), e o Attribute attDoWC para verdadeiro (true), 
notificando assim a Premise envolvida na Rule rleWeightsChange. Caso tal Premise se 
torne verdadeira, o processo de cálculo do erro médio e a mudança dos pesos é 
iniciado. 
Por fim, o Código 14 apresenta o código que dispara a cadeia de notificações. 
Segundo os princípios do PON, o processo inicia-se quando um Attribute é modificado, 
notificando assim uma Premise e, sucessivamente, notificando todas as entidades já 
programadas. Neste experimento, o ajuste da quantidade de épocas (Attribute 
attNumEpochs) a serem executadas, durante o treinamento, dispara o processo. 
 
 


152 
 
 
Código 14 - Ajuste do Attribute attNumEpochs – dispara o início da cadeia de  
notificações – Framework PON C++ 2.0 – exemplo do XOR 
42 
43 
44 
45 
46 
// Ajusta o Attribute que representa a quantidade de épocas 
// Inicia o processamento da cadeia de notificações 
void NetworkSystem::codeApplication() { 
    rede->attNumEpochs->setValue(100); 
} 
Fonte: Autoria Própria 
5.2.3 Resultados do Experimento 
Testes foram conduzidos com 1000 épocas de treinamento. A inicialização dos 
pesos sinápticos foi feita de forma aleatória, variando os valores de 0 a 1. Os resultados 
foram equivalentes, tanto na média de erros obtida quanto no tempo de cada execução. 
A Tabela 10 apresenta a média dos resultados de cinco execuções do algoritmo, com 
1000 repetições (épocas) em cada execução (treinamento). 
Tabela 10 - Resultados do treinamento de RNA MLP com método BP em  
Framework PON C++ 2.0 para a função XOR 
Treinamento em PON 
Treinamento em PI 
ORD 
Erro geral 
Tempo (ms) 
 
Erro geral 
Tempo (ms) 
1 
0.0051 
315 
 
0.0009 
136 
2 
0.0017 
163 
 
0.0008 
121 
3 
0.0021 
202 
 
0.0056 
59 
4 
0.0033 
164 
 
0.0008 
66 
5 
0.0013 
161 
 
0.0045 
85 
Média 
0.0027 
201 
 
0.0025 
93.4 
Desvio Padrão 
0.0015 
66.0 
 
0.0023 
33.8 
Fonte: Autoria Própria 
A proximidade nos valores do erro médio geral entre as implementações 
mostrou que o treinamento utilizando o Framework PON C++ 2.0 é plausível. A 
diferença no tempo de execução era esperada, pois a implementação do Framework 
faz uso intenso de técnicas de OO (ainda que sob o viés de notificações) como métodos 
virtuais, polimorfismo e estruturas de dados como listas e filas, o que implicaria em 
tempos de execução maiores, em relação à versão do treinamento utilizando a 
linguagem C. 
5.2.4 Considerações sobre o experimento 
O uso do Framework PON C++ 2.0 para o experimento, ao invés de 
materializações que gerem códigos mais velozes, deu-se pela disponibilidade de uma 


153 
 
 
versão estável à época do início do desenvolvimento. Outras materializações para 
geração de software PON não possuíam versões tão estáveis (i.e. tecnologia LingPON 
e suas variantes) quanto ele ou eram mais lentas (i.e. versões anteriores do framework 
PON), sendo que as materializações para geração de hardware em PON eram muito 
incipientes (e.g. PON-HD prototipal e suas variantes) ou, senão, não tão acessíveis 
(e.g. CoPON).   
A principal contribuição do presente experimento foi a demonstração da 
plausibilidade na construção de uma RNA utilizando PON. Mesmo que os resultados, 
em termos de tempo de execução, não tenham sido positivos, as taxas de erro 
alcançadas foram muito próximas às da implementação em linguagem C 
procedimental. 
Outra vantagem desta solução proposta foi a forma de desenvolvimento, pois 
permitiu a utilização de bibliotecas prontas, baseadas em PON, que permitiram a 
criação de entidades desacopladas. Neste contexto, a visualização do processo de 
execução da RNA no tocante à abstração dos elementos fica mais clara para o 
programador se comparada à solução implementada em Linguagem C procedimental. 
Ainda, pode-se observar que uma vez definidas as FBE e Rules de forma 
correta, a execução da cadeia de notificações não segue um padrão sequencial top-
down como nos códigos criados via PI. Em PON, o mecanismo de inferência define a 
ordem de execução das ações. Tal fato pode ser verificado por meio da necessidade 
de controle sobre o final do processamento dos neurônios de cada camada (via 
Attribute attClock), para então realizar o cálculo do erro médio dos padrões e da própria 
RNA.  
Outrossim, a execução do algoritmo aqui apresentado, mesmo que 
implementado em PON, não ocorre de forma paralela, pois foi utilizado um computador 
de processamento sequencial, monocore e single-thread, baseado na arquitetura de 
von Neumann. Neste contexto, a dinâmica da execução PON não foi realizada de forma 
eficiente pelo hardware utilizado porque ele não o permite. Não obstante, o 
desacoplamento inerente e a potencial natural concorrência/paralelismo das RNA em 
NeuroPON pode ser vislumbrando nas entidades constituintes. 
É sugerido, portanto, que o PON se torne relevante à construção de RNA, pois 
a solução mostrou sua plausibilidade com resultados satisfatórios, nas condições 
dadas, facilitando a descrição de uma RNA desacoplada e, portanto, paralelizável 
(conforme os conceitos do PON). Em tempo, tais esforços de pesquisa e 
desenvolvimento tornaram-se objeto de publicação em Schütz et al. (2015).  


154 
 
 
5.3 RNA MLP com Framework PON C++ 2.0: Treinamento BP para IRIS 
Dataset 
A segunda experiência de implementação de RNA MLP utilizando o Framework 
PON C++ 2.0 visou o treinamento para o reconhecimento dos padrões de classificação 
da Flor Iris (IRIS Dataset). A classificação IRIS Dataset, assim como a função XOR, 
também é um sistema clássico nos trabalhos de RNA. Tal banco de dados consiste em 
cento e cinquenta amostras de dados, com as medidas de comprimento e largura, em 
centímetros, das pétalas e sépalas da flor de IRIS. A partir deste conjunto de dados de 
entrada, é possível classificar os três subtipos de flores de Iris: Setosa, Virginica e 
Versicolor. O conjunto de dados consiste em 150 amostras de cada uma das espécies 
da flor de IRIS (FISCHER, 1926; HEATON, 2015).  
5.3.1 Desenvolvimento do Experimento 
A estrutura principal da aplicação segue a implementação da RNA MLP 
treinada para a função XOR. Para o sistema de classificação IRIS Dataset, aumentou-
se a quantidade de estruturas geradas, bem como algumas funções foram 
especializadas. Neste caso, a configuração utilizada para o sistema foi de quatro 
entradas, cinco neurônios acomodados em uma camada escondida, e três neurônios 
de saída. A função de ativação utilizada foi a tangente hiperbólica.  
5.3.2 Codificação 
O processo de treinamento para a base de dados da flor de Iris é maior do que 
para a função XOR. Consequentemente, a estrutura da RNA criada foi expandida 
perante a estrutura utilizada na função XOR, bem como a própria estrutura de código 
do NeuroPON criado. Assim, um maior controle de processamento entre as camadas 
foi realizado, resultando numa quantidade maior de Premises dentro de cada entidade 
Condition das Rules da aplicação.  
Ainda, conforme exposto na seção 4.4.2, as FBE dos neurônios foram 
especializadas. A título de exemplo, o Código 15 apresenta a FBE que representa um 
neurônio da camada escondida da RNA. 
 
 
 


155 
 
 
Código 15 - FBE NeuronHidden em código Framework PON C++ 2.0 
01 
02 
03 
04 
05 
06 
07 
08 
09 
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
class NeuronHidden : public FBE { 
public: 
    NeuronHidden(Network *netw); 
    virtual ~NeuronHidden(); 
    void createPON(); 
public: 
    Double *attBias;          // entrada de Bias 
    Double *attOutput;        // saida 
    Double *attGradient;      // gradiente para atualização dos pesos 
    Boolean *attDone;         // controle de sincronização de cálculo 
    Double *attDerivative;    // derivada utilizada na função de ativação 
    double i0, i1, i2, i3;    // entradas 
    double w0, w1, w2, w3;    // pesos 
public: 
    Premise *preCalcHidden;   // Premises 
    Premise *preCalcHiddenF; 
    Method *mthCalcHidden;    // Method 
    RuleObject *rleCalcHidden;// Rule 
private: 
    void calcHidden(); 
}; 
Fonte: Autoria Própria 
Nas linhas 12 e 13 do Código 15, pode se notar que as entradas e os pesos, 
respectivamente, não estão sendo declarados como Attributes PON. Isso se dá pois 
tais elementos não serão reativos, ou seja, ao ter seu valor alterado, não notificarão 
nenhuma outra entidade pertinente. Neste contexto, até mesmo a título de 
experimentação, optou-se pela criação de variáveis com tipos “tradicionais”, 
pertencentes à própria linguagem.  
O processo de treinamento da base de dados da flor de Iris é o mesmo efetuado 
para a função XOR, tanto para neurônios da camada escondida intermediária quanto 
para a camada de saída. Isto posto, a seção 5.3.3 apresenta os resultados do 
experimento. 
5.3.3 Resultados do Experimento 
Os testes foram conduzidos com 1000 épocas de treinamento. A inicialização 
dos pesos sinápticos foi aleatória, tanto para a implementação Framework PON C++ 
2.0 quanto para a implementação procedural em Linguagem C com PI, variando os 
valores de 0 a 1. 
Em cada execução do algoritmo de treinamento, tanto na implementação 
procedural PI utilizando a linguagem C quanto na implementação PON utilizando o 
Framework PON C++ 2.0, os resultados obtidos foram equivalentes. Os valores de 


156 
 
 
erros médios foram muito próximos, sendo que o tempo de execução foi (naturalmente) 
maior na versão implementada em PON, com Framework PON C++ 2.0. 
No exemplo do IRIS Dataset, o treinamento foi conduzido utilizando-se 80% 
dos padrões de entrada, aleatoriamente selecionados. Os mesmos dados foram 
utilizados tanto na aplicação PON quanto na aplicação PI. Em cada implementação, tal 
seleção resultou em 120 padrões de treinamento (40 para cada tipo de flor do banco 
de dados), com quatro entradas (comprimento e largura de pétala e sépala), e três 
possibilidades de saída binárias. Os resultados obtidos estão apresentados na Tabela 
11. 
Tabela 11 – Resultados comparativos entre o treinamento BP de uma RNA MLP: NeuroNOP utilizando o 
Framework PON C++ 2.0 versus Linguagem C Procedimental (classificação IRIS Dataset) 
Framework PON C++ 2.0 
 
Linguagem C Procedimental 
ORD 
Erro geral 
Tempo (ms) 
  
Erro geral 
Tempo (ms) 
1 
0.046 
4820 
0.039 
1292 
2 
0.037 
2494 
0.048 
1150 
3 
0.015 
3091 
0.011 
791 
4 
0.031 
2509 
0.019 
913 
5 
0.018 
2463 
0.021 
932 
Média 
0.029 
3075 
  
0.028 
1016 
Desvio Padrão 
0.013 
1010 
  
0.015 
202 
Fonte: Autoria Própria 
As cinco execuções, com 1000 épocas cada, gastaram um tempo médio de, 
aproximadamente 3 segundos na implementação Framework PON C++ 2.0. Neste 
contexto, avaliou-se que o algoritmo que implementou o treinamento pelo método BP 
com PON atingiu bons resultados utilizando 0,1 como taxa de aprendizagem, atingindo 
um erro médio de 0,029. 
Na implementação em PI procedimental utilizando a linguagem C, o tempo 
gasto nas cinco execuções, com mil épocas cada, foi de aproximadamente 1 segundo. 
Também com a taxa de aprendizagem ajustada em 0,1, o erro médio geral por de 0,028. 
Nos testes de classificação utilizando o IRIS Dataset, subsequentemente ao 
processo de treinamento, a solução também mostrou-se plausível pois a RNA MLP 
atingiu resultados em um tempo de execução equivalente aos trabalhos de Swain et al. 
(2012) e Vyas e Upadhyay (2014), por exemplo.  
5.3.4 Considerações sobre o experimento 
Apesar do experimento utilizando a base de dados da flor de IRIS (IRIS 
DataSet) ter uma lógica semelhante ao experimento utilizando o XOR (ambos em 


157 
 
 
Framework PON C++ 2.0), houve uma evolução no processo de implementação. A 
quantidade de padrões de treinamento é maior, a criação de Methods específicos para 
aquisição de dados foi necessária. Além disso, a quantidade de saídas na RNA a ser 
treinada para IRIS DataSet é maior do que para o XOR, que possui apenas um neurônio 
na camada de saída. Tal fator motivou a criação de Methods que permitiram maior 
desacoplamento entre os neurônios de saída, facilitando assim uma futura 
paralelização dos cálculos entre tais entidades. 
Outro conceito importante que pode ser verificado no presente experimento foi 
quanto à escalabilidade. Mesmo que algumas mudanças na codificação do primeiro 
experimento tenham sido efetuadas, a RNA foi treinada pela utilização da mesma 
lógica, em termos de entidades PON, do primeiro experimento.  
Por fim, o modelo computacional NeuroPON também permitiu a criação de 
entidades desacopladas devido à sua natureza notificante, o que facilitaria paralelismo 
e mesmo distribuição. Neste contexto, as dificuldades em se definir estruturas 
desacopladas durante o desenvolvimento de RNA em PI são suprimidas pela utilização 
do NeuroPON. Por meio da utilização de FBE e Rules ao invés de estruturas matriciais 
e laços de repetição, o desacoplamento acontece de forma natural, em tempo de 
construção (SIMÃO; STADZSIZ, 2008; SIMÃO et al, 2012b). 
A Seção 5.4 apresenta um primeiro experimento visando a execução 
concorrente dos neurônios implementados em PON. O desenvolvimento de tal 
experimento foi guiado pelo trabalho de Belmonte et al. (2016), porém com 
modificações na implementação do Framework PON C++ 3.0, a fim de adequar sua 
execução conforme as regras do modelo computacional NeuroPON.  
5.4 RNA MLP com Framework PON C++ 3.0: treinamento BP para IRIS 
Dataset 
Conforme descrito na Seção 3.3.3, o Framework PON C++ 3.0 é uma extensão 
do Framework PON C++ 2.0 por meio de threads, que visa fornecer uma maneira de 
distribuir as entidades do PON em múltiplos núcleos de processamento, de forma 
transparente ao desenvolvedor.  
5.4.1 Desenvolvimento e codificação 
A implementação da RNA MLP com treinamento BP aqui apresentada segue o 
mesmo padrão de implementação do experimento demonstrado na Seção 5.3. A 


158 
 
 
modificação que deve ser feita, no código das estruturas-padrão do Framework, é a 
identificação do núcleo (core) de execução da entidade PON utilizada. O Código 16 
apresenta o código que implementa a Rule rleCalcHidden e seus componentes. 
Código 16 - Implementação da Rule rleCalcHidden, utilizando Framework PON C++ 3.0 
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
// Adjusts the number of epochs (stats the process) 
mthCalcHidden = new MethodPointer<NeuronHidden>(this, &NeuronHidden::calcHidden); 
RULE(rleCalcHidden, SingletonScheduler::getInstance(), Condition::CONJUNCTION, this->core); 
PREMISE(preCalcHidden, this->net->attClock, 2, Premise::EQUAL, Premise::STANDARD, false, 
this->core); 
PREMISE(preCalcHiddenF, this->attDone, false, Premise::EQUAL, Premise::STANDARD, false, 
this->core); 
rleCalcHidden->addPremise(preCalcHidden); 
rleCalcHidden->addPremise(preCalcHiddenF);     
rleCalcHidden->addMethod(mthCalcHidden); 
Fonte: Autoria Própria 
Na declaração da Rule rleCalcHidden e das Premises preCalcHidden e 
preCalcHiddenF, do código apresentado no Código 16, o último parâmetro da macro 
definida é a informação do núcleo de execução. Implicitamente, a execução das ações 
implementadas pelos Methods instigados em determinada Rule (neste caso 
mthCalcHidden), ocorre no núcleo informado na declaração da própria Rule. 
Naturalmente, como a implementação de uma RNA envolve mais de um 
neurônio, o núcleo de execução é definido via um atributo da própria classe que 
implementa a FBE Neuron no Framework. Assim, vinculado à instanciação de um 
neurônio, tanto de camada escondida quanto de saída, é repassada a informação (via 
valoração de parâmetro) de qual núcleo do microprocessador deverá ser utilizado na 
execução das ações pertinentes à entidade notificada. 
Quanto à execução dos elementos, a Figura 41 apresenta um diagrama de 
objetos da UML como um exemplo de concorrência na execução das entidades PON. 
O diagrama de objetos em UML, mostrado na Figura 41, apresenta um exemplo 
de computação concorrente entre dois neurônios de camada oculta em uma RNA. O 
processo de notificação é iniciado quando o valor do Attribute net::attClock é 
modificado. Tal ajuste notifica as Premises hidneu0::preCalc e hidneu1::preCalc. Deste 
ponto em diante, todo o processo de notificação e execução das entidades PON ocorre 
simultaneamente. Por fim, quando os valores dos Attributes hidneu0::attDone e 
hidneu1::attDone são modificados, a Premise net::preCalcDone é notificada. 
 
 


159 
 
 
Figura 41 – Diagrama de objetos em UML: fluxo de execução concorrente das entidades PON, na execução 
de uma RNA MLP, utilizando Framework PON C++ 3.0 
 
Fonte: Autoria Própria 
Além da execução concorrente apresentada na Figura 41, é importante 
observar que as entidades PON que estão em uma thread acessam entidades PON 
que estão em outra thread (na Figura 41 as threads estão representadas pelas pistas 
– lanes). Tal mecanismo é considerado crítico nas execuções em máquinas com 
microprocessadores multicore. Neste contexto, a exclusão mútua ao acesso às 
entidades PON compartilhadas é garantida pelos métodos das classes Thread e 
SleepCondition, pertencentes ao pacote Multicore do Framework PON C++ 3.0 
(apresentado na Seção 3.3.3 Página 108). 
5.4.2 Resultados do Experimento 
Assim como no experimento efetuado com o Framework PON C++ 2.0, os 
testes aqui foram conduzidos com 1000 épocas de treinamento. Porém, neste 
experimento, a inicialização dos pesos sinápticos seguiu os mesmos valores do 
experimento em Framework PON C++ 2.0. Tal processo foi efetuado visando comparar 
os valores e a taxa de acerto do algoritmo de treinamento. Neste sentido, em cada 
execução do algoritmo de treinamento os resultados obtidos foram iguais, em termos 
de valoração de pesos sináptico e taxa de acerto.  


160 
 
 
Referente aos dados de desempenho do presente experimento, a Figura 42 
apresenta um gráfico comparativo entre os experimentos efetuados em software. 
Figura 42 – Tempos de execução (em milissegundos) do treinamento de RNA MLP com método BP, 
utilizando NeuroPON em materializações de software do PON, para a base de dados da flor de Iris. 
 
Fonte: Autoria Própria 
No gráfico da Figura 42, a sigla IP C representa o tempo médio de execução 
do algoritmo em Linguagem C apresentado na Seção 5.1. Ainda, a sigla FANN (Fast 
Artificial Neural Network) é uma implementação alternativa, também baseada no 
Paradigma Imperativo. Conforme apresentado na Figura 42, o tempo médio de 
processamento do treinamento em cem execuções (mil épocas cada) foi de 6987 
milissegundos para a implementação no Framework PON C++ 3.0 utilizando apenas 1 
núcleo, ou seja, aproximadamente 2,34 vezes mais lento que a versão 2.0 monocore 
do Framework. 
Outrossim, a execução em múltiplos núcleos pode ser observada. A Figura 43 
apresenta um screenshot (captura de tela) do histórico da CPU enquanto executando 
o algoritmo de treinamento do presente experimento. 
 
 
 
 


161 
 
 
Figura 43 – Captura de tela (screenshot) do histórico da CPU, apresentando o uso dos núcleos na 
execução do treinamento multicore, por meio do Framework PON C++ 3.0:  
(a) 1 núcleo; (b) 2 núcleos; (c) 4 núcleos; (d) 8 núcleos. 
 
Fonte: Autoria Própria 
A Figura 43 apresenta o comportamento dos núcleos de processamento 
durante a execução do treinamento de uma RNA MLP usando o método BP, por meio 
do Framework PON C++ 3.0. Neste contexto, mesmo que de modo mais lento, o 
processo é conduzido nos múltiplos núcleos de processamento do microprocessado 
utilizado. Tal fator demonstra a plausibilidade da utilização de tal Framework para a 
construção de RNA contendo entidades concorrentes. 
Visando uma análise mais elaborada e precisa do uso dos núcleos de 
processamento para a execução paralela, utilizou-se o comando top no sistema Linux. 
Este comando apresenta as informações do sistema e a lista de processos (threads) 
atualmente gerenciados pelo Kernel do Linux. Para extrair apenas os dados de 
utilização dos quatro núcleos de execução, o comando foi executado com a opção de 
simplificar os dados apresentados, e com o tempo de aferição ajustado para 0,5 
segundo: 
top -b  -d 0,5 | grep Cpu > top_cpu.txt 
O comando grep foi concatenado à linha de execução para que haja, apenas, 
os dados dos cores (no caso do comando apresentado é a palavra Cpu). Por fim, os 
dados são armazenados em arquivo texto para posterior ajustes e tabulação. A Figura 


162 
 
 
44 apresenta os dados de utilização tabulados, juntamente com um gráfico de linhas, a 
partir da execução do treinamento utilizando quatro cores. 
Figura 44 - Gráfico de utilização do uso de núcleos de processamento por meio do comando TOP em Linux 
 
Fonte: Autoria Própria 
Nos dados tabulados e gráfico apresentados na Figura 44, é possível observar 
que há, realmente, a utilização de todos os núcleos de execução (cores) em paralelo. 
A ocupação do primeiro núcleo (cpu0 us, na linha na cor azul), em algumas execuções, 
torna-se muito baixo. Isso se dá pela preempção de processos entre a execução do 
treinamento em PON e o sistema operacional. 
Por fim, visando checar possíveis problemas no uso de recursos do sistema 
pela aplicação PON multicore, utilizou-se o programa Valgrind (SEWARD, 2019). O 
Valgrind é um sistema para depuração e criação de perfil de programas Linux, que roda 
sobre uma licença geral pública (GPL - General Public License). Neste contexto, a 
execução do programa sobre a aplicação PON durou 30 horas. Os resultados 
basearam-se em uma verificação feita sobre o uso de memória, e são apresentados na 
Tabela 12. 
A interpretação destes resultados, por meio da documentação da aplicação 
Valgrind, indica que os erros residem em leituras e escritas inválidas, em 158 diferentes 
áreas de memória, acessadas 16.242 vezes. A indicação de vazamentos 
“possivelmente perdidos” na memória é causada por problemas relacionados a 
referências a ponteiros onde, neste caso, não existe um ponteiro inicial para 
determinada área de memória, mas existe um ponteiro interno naquele espaço de 
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
cpu0 us 3 12 58 96 96 98 63 67 13 94 10 96 94 94 91 70 17 18 7 44 87 39 87 50 96 94 91 37 36 86
cpu1 us 2 20 71 96 92 98 76 98 88 92 10 92 94 92 92 75 63 73 79 85 89 52 91 58 96 95 93 54 49 84
cpu2 us 3 14 71 96 96 94 68 82 88 98 98 96 98 92 90 72 73 72 83 84 89 56 94 73 10 94 91 46 51 86
cpu3 us 4 12 82 98 96 10 89 98 92 94 98 96 98 94 94 90 78 83 90 94 92 78 94 83 10 97 97 82 78 70
0
20
40
60
80
100
120
% de utilização 
Utilização dos núcleos de execução


163 
 
 
memória. Contudo, tal erro pode ser confundido, pelo Valgrind, por códigos válidos que 
não seriam vazamentos de memória. 
Tabela 12 - Resultados da execução do Valgrind sobre aplicação gerada  
a partir do Framework PON C++ 3.0 
Resumo de Vazamento de memória (Leak Summary) 
Dados definitivamente perdidos na memória 
0 bytes em 0 blocos 
Dados indiretamente perdidos na memória 
0 bytes em 0 blocos 
Dados possivelmente perdidos na memória 
1.152 bytes em 4 blocos 
Dados ainda acessíveis 
93.451 bytes em 1.145 blocos 
Resumo de Erros (Error Summary) 
16.242 erros a partir de 158 contextos 
Fonte: Autoria Própria 
Por fim, os vazamentos de memória "ainda acessível" ocorrem quando blocos 
de memória ainda estão acessíveis após o término da execução do processo, ou seja, 
não foram liberados pelo processo. Não obstante, tais vazamentos não são 
considerados prejudiciais ao processo de desenvolvimento de sistemas, pois existem 
bibliotecas estáveis e populares da comunidade de Software Livre (e. g. GLib e GTK+) 
que alocam dinamicamente muita memória heap para dados que devem estar 
disponíveis durante toda a execução do programa; isto é, memória que não deve ser 
desalocada até que o programa esteja prestes a sair (e. g. variáveis globais). Nestes 
caso, ao invés de se liberar explicitamente essa memória antes do retorno da função 
principal, alguns programas deixam esta tarefa para o kernel do sistema. 
5.4.3 Considerações sobre o experimento 
Conforme apresentado, códigos-fonte utilizados no Framework PON C++ 2.0 
podem ser utilizados em sua extensão multicore com threads, nomeadamente o 
Framework PON C++ 3.0, adicionando a informação do núcleo de execução da 
entidade PON. Assim, as vantagens quanto à facilidade na definição de estruturas 
paralelas e desacopladas durante o desenvolvimento, são as mesmas quanto à 
utilização dos dois frameworks. 
Os resultados dos experimentos, referentes ao tempo de execução do 
treinamento de um RNA MLP em PON por meio do Framework PON C++ 3.0, 
demonstraram que o código gerado é mais lento que os códigos gerados nas outras 
materializações em software (na implementação de RNA MLP com treinamento BP 


164 
 
 
conforme experimentos aqui apresentados). Esse resultado é, em parte, um reflexo do 
uso de estruturas computacionais caras na implementação do Framework. 
Outra questão relevante em relação à solução multicore está no modelo de 
execução utilizado. O gerenciamento de memória compartilhada, por exemplo, pode 
ser considerado um gargalo na execução dos experimentos. Como o algoritmo de 
treinamento pelo método BP utiliza o resultado de todos os cálculos de neurônios no 
ajuste dos pesos sinápticos, o processo de exclusão mútua (ou seja, bloqueio e 
desbloqueio de mutex) é amplamente utilizado, fazendo com que tal controle gaste 
tempo de processamento. 
Além disso, o processo de controle da execução de múltiplos núcleos de 
processamento também pode ser considerado um gargalo. Nos experimentos, a 
quantidade de neurônios a ser utilizada é pequena se comparada a grandes RNA, 
fazendo com que o cálculo, a ser realizado em cada neurônio paralelo, seja realizado 
de maneira rápida e simples. Neste contexto, o Sistema Operacional gastou mais tempo 
no controle de threads do que no processamento de cada neurônio, de maneira paralela 
(AKHTER; ROBERTS, 2006; BELMONTE et al., 2016; YUN et al., 2016). 
Este último gargalo é corroborado pelo gráfico de resultados da Figura 42. Os 
tempos de processamento no Framework PON C++ 3.0 são mais altos do que em sua 
versão 2.0, devido ao processo de alocação e controle de threads no processamento 
multicore. Além disso, conforme mostrado no gráfico, o tempo médio de processamento 
é diretamente proporcional à quantidade de núcleos de processamento utilizados. 
Consequentemente, excluindo-se as deficiências técnicas apresentadas na 
implementação do próprio Framework PON C++ 3.0, a transparência na distribuição do 
código gerado é um ponto positivo. Tal processo é fundamental para a avaliação da 
viabilidade de implementação paralela, serve de exemplo para novos experimentos 
especialmente em hardware, onde pode se superar tais deficiências.  
Por fim, duas análises adicionais aos dados publicados no artigo supracitado 
foram efetuadas. O comando top, do S.O. Linux, foi utilizado visando a apresentação 
do uso dos múltiplos cores disponíveis para execução na máquina alvo. Neste contexto, 
uma verificação efetuada a cada 0,5 segundos, demonstrou o uso dos núcleos de 
execução. Outrossim, a aplicação Valgrind apresentou resultados quanto ao uso da 
memória, apontando que erros no uso da memória heap podem estar ocorrendo 
durante a execução da aplicação.  
 Como o presente trabalho visa explorar a implementação, do modelo 
computacional NeuroPON, de forma direta em hardware reconfigurável, não foram 


165 
 
 
feitos novos esforços no melhoramento do próprio Framework PON C++ 3.0 a fim de 
atingir melhores resultados em termos de velocidade, tampouco buscou-se investigar, 
de forma mais veemente, possíveis deficiências em seu código. O experimento aqui 
demonstrado foi utilizado exclusivamente para demonstrar a plausibilidade da 
distribuição dos elementos PON, por meio de uma materialização que permitisse a 
distribuição de processamento em vários núcleos de execução, em um processador 
multicore baseado em Von Neumann. Neste contexto, os esforços efetuados para a 
execução de tal treinamento em Framework PON C++ 3.0 foram direcionados para a 
publicação do artigo Schütz et al. (2018) em revista especializada16. 
A Seção 5.6 apresenta outro experimento efetuado, buscando a execução 
multicore, em máquinas Von Neumann. Tal experimento, por meio da utilização de uma 
nova abordagem chamada Framework PON Elixir/Erlang, apresenta resultados mais 
próximos aos esperados para execução multicore. 
5.5 RNA MLP para XOR com Framework Elixir/Erlang 
O experimento da execução da RNA em NeuroPON no Framework Elixir/Erlang 
foi efetuado visando, novamente, a plausibilidade do modelo em tal materialização. 
Neste contexto, não houve uma formalização e projeto teóricos para a execução, 
mesmo porque, à época da defesa desta tese, o projeto do Framework encontrava-se 
em suas primeiras versões.  
Outrossim, o experimento da execução da RNA em NeuroPON no Framework 
PON Elixir/Erlang foi efetuado visando, novamente, a plausibilidade do modelo em tal 
materialização. Neste contexto, não houve uma formalização e projeto teóricos para a 
execução. Entretanto, algo pertinente a ser relatado é que essa materialização da 
NeuroPON e mesmo experimento com ela foi feito por outrem e não pelo autor dessa 
tese. O autor do experimento se chama Fabio Negrini, principal autor também do 
framework aqui em questão, sendo ele pesquisador do grupo de pesquisa do PON17.   
Isto considerado, o código do experimento feito em Framework PON 
Elixir/Erlang foi de uma RNA MLP para a função XOR. Em bora hora, salienta-se que 
tal código foi escrito espelhando-se em (i.e., traduzindo de) outros códigos em 
NeuroPON previamente elaborados pelo autor desta tese. Após tais traduções e 
 
16 Neural Computing and Applications, ISSN 1433-3058, Springer, Impact Factor 4.213. 
17 O Framework PON Elixir/Erlang e a integração deste com Tecnologia LingPON, são parte 
dos esforços de dissertação do Sr. Fabio Negrini, trabalho a ser defendido em outubro de 2019 
(https://portal.utfpr.edu.br/cursos/coordenacoes/stricto-sensu/cpgei/defesas/mestrado-fabio-negrini) 


166 
 
 
ajustes, quatro diferentes máquinas foram locadas nos servidores da Amazon com, 
respectivamente, um, dois, quatro e oito núcleos de execução (cores). O programa 
resultante da compilação do código NeuroPON adaptado à LingPON 2.0 foi executado 
nas quatro máquinas, e seus resultados estão demonstrados na Tabela 13. 
Tabela 13 - Resultados da execução do experimento NeuroPON: RNA MLP para a função XOR em Erlang 
Quantidade 
de cores 
Média 
Diferença 
Total 
Diferença 
com 
anterior 
Execução 
01 
Execução 
02 
Execução 
03 
Execução 
04 
Execução 
05 
01 
MONO 
CORE 
113360 
0.00% 
  
47300 
59300 
168400 
180400 
111400 
02 
DUAL CORE 
41700 
63.21% 
63.21% 
5000 
61200 
48900 
58000 
35600 
04 
QUAD CORE 
17800 
84.30% 
57.31% 
19000 
16000 
15800 
23500 
14600 
08 
OCTA CORE 
7200 
93.65% 
59.55% 
10300 
3700 
8400 
6200 
7300 
Fonte: Autoria Própria 
Conforme apresentado na Tabela 13, foram efetuadas cinco execuções do 
código, em cada uma das máquinas. A segunda coluna apresenta a média do tempo 
de execução em milissegundos. Pode-se observar, portanto, uma queda de, 
aproximadamente, 63% no tempo de execução entre a máquina monocore e a máquina 
dual core, de aproximadamente 84% entre a máquina dual core e quad core, e de 
aproximadamente 94% entre a máquina quad core e octa core. A Figura 45 apresenta 
o gráfico de tais médias de tempo de processamento. 
Isto posto, é correto afirmar que o Framework PON Erlang é de grande valia 
para a execução da NeuroPON, uma vez que seus resultados foram muito superiores 
aos resultados alcançados via Framework PON C++ 3.0. Na verdade, esse experimento 
permite melhor perceber a valia de NeuroPON já em termos de paralelismo em 
software. Outrossim, para um melhor funcionamento do modelo computacional 
NeuroPON nesses Frameworks, tanto Framework PON C++ 3.0 quanto em Framework 
PON Elixir/Erlang, seria necessário que os seus códigos fossem gerados  a partir de 
tecnologias LingPON 2.0. 
 
 
 
 


167 
 
 
Figura 45 - Representação gráfica dos tempos médios de execução NeuroPON de uma  
RNA MLP para a função XOR em Erlang 
 
Fonte: Autoria Própria 
Ao bem da verdade, atualmente já há compiladores que permitem compilar de 
LingPON para ambos os frameworks citados, nomeadamente Framework PON C++ 3.0 
e Framework PON Elixir/Erlang (MENDES et al., 2019; NEGRINI et al., 2019). Não 
obstante, dado que os testes com multicore serviram ao seu propósito que era testar a 
possibilidade de paralelismo com PON, considerou-se melhor concentrar esforços 
subsequentes ao LingPON em outras implementações, conforme será descrito 
subsequentemente neste presente documento de tese. 
A Seção 5.6 aborda o mais um experimento feito em software, antes da 
elaboração do modelo computacional NeuroPON definitivo e os experimentos de 
hardware reconfigurável. Tal experimento utiliza o IRIS Dataset, porém a RNA é 
descrita utilizando LingPON, sendo compilada para linguagem StaticCPP. 
5.6 RNA MLP para IRIS Dataset com LingPON 1.2 StaticCPP 
O último experimento, visando comprovar a plausibilidade de uma RNA em 
PON via materializações em software, foi implementado utilizando-se diretamente a 
linguagem LingPON. O exemplo utilizado para treinamento foi o banco de dados da flor 
de Iris (Iris Dataset), tendo assim os mesmos parâmetros utilizados no exemplo da 
Seção 5.3: cento e cinquenta amostras com quatro números reais de entrada e três 
binários de saída, sendo que 80% foram utilizadas para o treinamento, e o restante 
para os testes. Ainda, a lógica utilizada para implementar a aplicação em PON foi a 
113360
41700
17800
7200
0
20000
40000
60000
80000
100000
120000
01
MONO CORE
02
DUAL CORE
04
QUAD CORE
08
OCTA CORE
Tempo médio em milissegundos
Ambiente virtual 
Tempo de execução por ambiente virtualizado


168 
 
 
mesma do experimento apresentado na Seção 5.3. Assim, a Figura 39  serve como 
referência para a cadeia de notificações deste experimento. 
5.6.1 Desenvolvimento 
Conforme apontado, o presente experimento utiliza os mesmos parâmetros, em 
termos de modelo, do experimento apresentado na seção 5.3. Assim, os mesmos 
Attributes e FBE são definidas neste experimento, porém utilizando LingPON ao invés 
de Framework PON C++ 2.0.  
A FBE Network, por sua vez, define a RNA em si, a FBE NeuronHidden 
representa cada neurônio da camada escondida, e a FBE NeuronOutput, representa 
cada neurônio da camada de saída. Neste contexto, demonstrar-se-á, em termos de 
diagramas, apenas o diagrama de instâncias PON, expondo a relação das entidades 
envolvidas no processamento da cadeia de notificações. Assim, a Figura 46 apresenta 
tal modelo para a implementação da RNA MLP em LingPON, ligadas à FBE Network.  
5.6.2 Codificação 
Para o treinamento, teste e execução da RNA no exemplo do Iris Dataset, foram 
declaradas cinco instâncias do FBE NeuronHidden, três instâncias do FBE 
NeuronOutput e uma instância do FBE Network. Em tempo, no modelo da Figura 46, 
as instâncias não estão representadas, mas apenas a entidade representando cada 
FBE. A título de exemplo, o Código 17 apresenta a instanciação das FBE. 
Código 17 - Declaração das instancias de FBE em LingPON, da RNA MLP, para o Iris Dataset 
75 
76 
77 
78 
79 
Inst 
 
Network net 
 
NeuronHidden hidneu0, hidneu1, hidneu2, hidneu3, hidneu4 
 
NeuronOutput outneu0, outneu1, outneu2 
end_inst 
Fonte: Autoria Própria 
Em tempo, a fim de diferenciar os Attributes, aqueles que não são reativos 
estão esmaecidos na Figura 46. Neste contexto, os Attributes não reativos 
(attRMSerror, attErrorPattern e attOutputx) são aqueles que não estão ligados a 
nenhuma Premise. Assim, ao ter seu valor alterado, não efetuam notificação às 
entidades pertinentes e, consequentemente, não disparam nenhum processo na cadeia 
de notificações. 


169 
 
 
A implementação das Rules que definem o comportamento das FBE que representam os neurônios, tanto 
os da camada escondida quanto da camada de saída, deve levar em conta todas as instâncias destes 
neurônios. Tal implementação é necessária pois a LingPON trata seus elementos de forma independente, 
não admitindo laços de repetição com índices para o tratamento de várias instâncias. O  
Código 18 apresenta o código da regra de formação para a concepção da Rule 
rleNOCalcOutput. 
Figura 46 - Modelo de Objetos PON: implementação da RNA MLP para o treinamento IRIS Dataset 
Network
attNumEpochs
preNetStart
rleNetStart
mthNetStart
Network
attClock
attReadTrainInputs
attReadTrainInputs
preNetGetValues
rleNetGetValues
mthNetGetValues
preNetRaiseEpoch
rleNetRaiseEpoch
mthNetRaiseEpoch
attNumEpochs
attTotTrainInputs
attClock
preNetRaiseEpochC
NeuronHidden
attDone
preNetNeuronsHDone
rleNeuronsHDone
mthNetNeurons
HDone
NeuronHidden
attDone
preNetSetOutputNeurons
rleNetSetOutputNeurons
mthNetSetOutput
Neurons
attErrorPattern
NeuronOutput
attDone
preNetNeuronsODone
rleNetNeuronsODone
mthNetNeurons
ODone
NeuronOutput
attDone
attOutput(x)
preNetCalcOverallError
rleNetCalcOverallError
mthNetCalc
OverallError
attRMSerror
Legenda
FBE
Premise
Rule
Method
 
Fonte: Autoria Própria 
 


170 
 
 
Código 18 - Regra de Formação na concepção da Rule rleNOCalcOutput 
181 
182 
183 
184 
185 
186 
187 
188 
189 
190 
191 
formRule rleNOCalcOutput 
 
condition 
 
  subcondition sbcNOCalcOutput 
 
 
 premise preNOCalcOutput NeuronOutput.attDone == false and 
 
 
 premise preNOCalcOutputF Network.attClock == 4 
 
  end_subcondition 
 
end_condition 
 
action 
 
  instigation insNOCalcOutput NeuronOutput.mthNOCalcOutput(); 
 
end_action 
end_formRule 
Fonte: Autoria Própria 
Assim, uma pré-compilação no código verifica qual FBE foi utilizada na 
Formation Rule e, a partir da quantidade de instâncias de tal FBE, a quantidade de 
entidades necessárias são criadas (FBE e Rules). O Código 19 apresenta o código da 
instanciação de tais FBE, bem como uma Rule relacionada a uma das instâncias da 
FBE NeuronOutput já modificada pelo processo de pré-compilação. 
Código 19 - Resultado da pré-compilação - uma FBE e uma Rule para cada instância 
181 
182 
183 
184 
185 
186 
187 
 
246 
247 
248 
249 
250 
251 
252 
253 
254 
255 
256 
257 
258 
259 
 
269 
270 
271 
 
281 
inst  
 
… 
 
NeuronOutputoutneu0 outneu0 
 
NeuronOutputoutneu1 outneu1 
 
NeuronOutputoutneu2 outneu2 
end_inst 
 
… 
 
rule rleNOCalcOutput0 
 
condition 
 
 
subcondition sbcNOCalcOutput0 
 
 
 premise preNOCalcOutputF0 net.attClock == 4 and 
 
 
 premise preNOCalcOutput0 outneu0.attDone == false 
 
 
end_subcondition 
 
end_condition 
 
action 
 
 
instigation insNOCalcOutput0 outneu0.mthNOCalcOutput(); 
 
end_action 
end_rule 
 
rule rleNOCalcOutput1 
 
… 
end_rule 
 
rule rleNOCalcOutput2 
 
… 
end_rule 
Fonte: Autoria Própria 
Além do Código 19 é importante ressaltar que o código das FBE também é 
refeito de forma automatizada. Como, em tais códigos estão inseridos os Methods que, 
normalmente, contêm muitas instruções, o processo de construção de código para 


171 
 
 
aplicações PON se torna prático e eficiente. O código completo da aplicação encontra-
se no Apêndice B.2. 
O presente experimento focou na implementação do treinamento da RNA MLP 
com o experimento em IRIS Dataset em LingPON, sendo posteriormente traduzido para 
a linguagem C++ sob o viés da orientação à notificação do respectivo compilador. O 
Código 20 apresenta o código fonte do Attribute attNumEpochs, FBE Network, em 
StaticCPP, para exemplificar os elementos acima listados. 
Código 20 - Implementação do Attribute attNumEpochs, FBE Network 
01 
02 
03 
04 
05 
06 
07 
08 
09 
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
#pragma once 
#include "preNetStart.h" 
#include "_NOPAdds.h" 
 
class net_attNumEpochs { 
public: 
    static int value; 
 
    static inline int setValue(int newValue, int type = _NOPAdds::STANDARD) { 
        if (net_attNumEpochs::value != newValue) { 
            net_attNumEpochs::value = newValue; 
            preNetStart::notify_net_attNumEpochs(newValue, type); 
 
        } else if (type == _NOPAdds::RENOTIFY) { 
            preNetStart::notify_net_attNumEpochs(newValue, type); 
 
        } 
    } 
}; 
Fonte: Autoria Própria 
O Código 20 é a implementação de um Attribute em PON, utilizando StaticCPP. 
Neste contexto, um Attribute é composto por um atributo que representa seu valor, e 
por um método que controle a alteração deste valor, de acordo com as normas do PON. 
No Código 20, portanto: 
 Linha 07: declaração de atributo estático; 
 Linhas 09 a 18: declaração e implementação de método estático. 
Em toda codificação realizada utilizando-se os conceitos do chamado 
StaticCPP, apenas o código do Method foi implementado em um arquivo separado de 
sua declaração, ou seja, em um arquivo .cpp. O Código 21 apresenta o código, gerado 
pelo compilador, dos arquivos .h e .cpp do Method mthNetStart a título de exemplo. 
 
 
 


172 
 
 
Código 21 - Arquivos net_mthNetStart.h e net_mthNetStart.cpp implementados em StaticCPP 
 
01 
02 
03 
04 
05 
06 
07 
 
01 
02 
03 
04 
05 
06 
07 
08 
09 
10 
11 
12 
// net_mthNetStart.h 
#pragma once 
 
class net_mthNetStart{ 
    public:  
 
 static bool run(); 
}; 
 
// net_mthNetStart.cpp 
#include "net_mthNetStart.h" 
#include "_NOPAdds.h" 
#include "net_attClock.h" 
#include "net_attReadTrainInputs.h" 
#include <iostream> 
 
using namespace std; 
inline bool net_mthNetStart::run(){ 
    if (_NOPAdds::log) cout << "NetStart" << endl; 
    net_attClock::setValue(1, _NOPAdds::NO_NOTIFY); 
    net_attReadTrainInputs::setValue(0, _NOPAdds::RENOTIFY); 
   
} 
Fonte: Autoria Própria 
Na primeira parte do Código 21 há apenas a declaração do método run(), no 
arquivo .h, que contém os comandos a serem executados por tal método. Já na 
segunda parte do Código 21, no arquivo .cpp, o código do método run() é apresentado, 
com seus respectivos comandos. 
No processo de codificação, as principais mudanças entre o presente 
experimento e o experimento que utilizou o Framework PON C++ 2.0 foram 
apresentadas. A lógica de execução permanece a mesma, já que ambos foram 
executados em máquinas com processadores sequenciais, baseados em von 
Neumann, e não utilizaram qualquer sistema de concorrência (como threads).  
5.6.3 Resultados do Experimento 
Os testes foram conduzidos com 1000 épocas de treinamento. A inicialização 
dos pesos sinápticos foi aleatória, tanto para a implementação em LingPON para 
StaticCPP quanto para a implementação procedimental em Linguagem C com PI, 
variando os valores de zero a um. 
Em cada execução do algoritmo de treinamento, em ambas as 
implementações, os resultados obtidos foram equivalentes. Os valores de erros médios 
foram muito próximos, sendo que o tempo de execução foi um pouco maior na versão 
implementada em PON. Os resultados obtidos estão apresentados na Tabela 14. 
 


173 
 
 
Tabela 14 - Resultados do treinamento para o sistema de classificação IRIS Dataset (LingPON x C) 
  
PON com LingPON 
PI com Linguagem C 
  
Tempo (ms) 
Erro médio 
Tempo (ms) 
Erro médio 
1 
158 
0.02235 
128 
0.02346 
2 
173 
0.03365 
131 
0.02128 
3 
157 
0.02689 
129 
0.025 
4 
161 
0.02587 
207 
0.02055 
5 
158 
0.02483 
147 
0.02261 
Média 
161 
0.02672 
148 
0.02258 
Desvio Padrão 
6.656 
0.00423 
33.657 
0.00176 
Fonte: Autoria Própria 
As cinco execuções, com 1000 épocas cada, gastaram um tempo médio de, 
aproximadamente, 161 milissegundos na implementação com LingPON em StaticCPP. 
Neste contexto, avaliou-se que o algoritmo que implementou o treinamento pelo método 
BP com PON atingiu bons resultados utilizando 0,1 como taxa de aprendizagem, 
atingindo um erro médio de 0,02672. 
Já na implementação em PI procedimental utilizando a linguagem C, o tempo 
médio nas cinco execuções, com mil épocas cada, foi de aproximadamente 148 
milissegundos. Também com a taxa de aprendizagem ajustada em 0,1, o erro médio 
geral foi de 0,02258.  
Em ambos os testes, a proximidade nos valores médios entre as duas 
implementações comparadas (LingPON com StaticCPP e PI procedimental com 
linguagem C) demonstrou que o treinamento efetuado utilizando-se PON é plausível e, 
uma vez otimizado o código, a diferença de desempenho se torna mínima.  
Por fim, salienta-se que a compilação dos códigos foi efetuada utilizando-se a 
otimização máxima permitida pelo compilador GNU C++ (g++) em sua versão para 
Linux (Cygwin). Neste contexto, o parâmetro -O3 foi utilizado. Tal decisão de projeto foi 
tomada frente aos testes da LingPON 1.2 compilada para StaticCPP, onde o uso desta 
otimização é fundamental para um expressivo aumento na velocidade de execução. 
5.6.4 Considerações 
Relativo à codificação da RNA MLP e de seu treinamento utilizando a LingPON, 
esta linguagem/materialização permite flexibilidade algorítmica na codificação da 
aplicação. Permite, também, um nível de abstração na forma de FBE, herdado da 
programação POO, em um nível ainda mais alto do que no Framework PON C++ 2.0. 
Além disso, uma vez que o PON usa conceitos de PD como a facilidade de 


174 
 
 
programação em alto nível, e a representação do conhecimento via regras como SBR, 
a implementação da RNA MLP tornou-se prática, com um código mais legível, em 
relação às implementações realizadas com as versões 2.0 e 3.0 do Framework PON 
C++. 
Outrossim, como já citado, a utilização das Formation Rules resultou em um 
menor esforço na produção de código, permitindo um alto nível de abstração por meio 
do uso das FBE no lugar de instâncias. Neste contexto, o processo de pré-compilação 
facilita a manutenção do código, uma vez que a transformação ao código final é feita 
de forma automatizada. 
Por fim, a utilização das técnicas de otimização StaticCPP, utilizadas pelo 
compilador, fizeram com que a aplicação resultante tivesse um desempenho superior 
às versões desenvolvidas utilizando Framework PON C++ 2.0, aproximando-se ainda 
mais da versão em linguagem C procedimental. Assim, o treinamento possui a mesma 
eficiência em termos de tempo de execução, porém a implementação apresenta as 
vantagens do modelo computacional NeuroPON18.  
5.7 RNA MLP para XOR com LingPON-HD 
O presente experimento visa a implementação de uma RNA MLP, com 
treinamento por meio do método BP, utilizando a tecnologia LingPON-HD. Assim, 
objetiva-se efetuar a operação e treinamento de tal RNA em dispositivos de hardware 
reconfigurável, notadamente FPGA, a fim de validar os conceitos do modelo 
computacional NeuroPON em uma plataforma onde se possa aproveitar o paralelismo 
estrutural e funcional de uma RNA MLP em sua operação, bem como no uso do método 
BP em seu treinamento. 
A implementação do experimento segue as regras do modelo computacional 
NeuroPON. Neste experimento, o NeuroPON é aplicado à classificação das 
possibilidades da tabela verdade da função XOR, ainda como aplicação de problemas 
clássicos visando a plausibilidade do experimento frente ao modelo. 
 
18 Novas versões de linguagem e compiladores PON vem aprimorando os resultados da própria 
tecnologia PON, e poderiam ser utilizados na implementação do modelo computacional NeuroPON. Não 
obstante, tais versões ainda estão muito incipientes para serem utilizadas na presente tese. 


175 
 
 
5.7.1 Desenvolvimento 
O planejamento para desenvolvimento de um experimento que vise a execução 
da 
RNA 
NeuroPON 
em 
FPGA 
levou 
em 
conta 
a 
tecnologia 
PON-HD 
(KERSCHBAUMER, 2018). Neste contexto, uma das decisões de projeto tomadas foi 
a de se utilizar apenas valores inteiros na tipificação dos Attributes numéricos, uma vez 
que a LingPON-HD não implementa o tipo de dados float, que acomoda os valores reais 
em Attributes PON. Assim, uma representação de valores reais por meio de valores 
inteiros quantizados foi utilizada. 
A utilização de números inteiros em hardware, inclusive com experimentos em 
RNA, é apontada como vantajosa nos trabalhos de Jacob et al. (2018), Nedjah et al. 
(2012) e Wu et al. (2018). Tais vantagens incluem a economia de espaço no chip e 
velocidade de execução. 
Em contraponto, um revés na utilização de inteiros na representação de valores 
reais é a precisão numérica, uma vez que tal transformação acarreta em uma 
aproximação de valores que, nesta tese, foi feita por meio de uma quantização. Porém, 
segundo os trabalhos citados no parágrafo anterior, não há uma interferência 
significativa no uso de valores quantizados no treinamento de RNA, ou seja, que 
desabone sua utilização frente às vantagens apontadas (JACOB et al., 2018; NEDJAH 
et al., 2012; WU et al., 2018). 
O processo de quantização atribui valores discretos para outros que podem 
variar entre infinitos valores. Assim, neste experimento, o processo de quantização foi 
utilizado para a obtenção de valores inteiros para representar os valores resultantes da 
função tangente hiperbólica, entradas, saídas e pesos sinápticos. A Tabela 15 
apresenta três exemplos de quantização. 
A Tabela 15 parte (a) apresenta a quantização de valores reais na faixa de -1.0 
até +1.0, para valores inteiros com 6 bits. Neste caso, o maior valor negativo da faixa 
real é -1.0, e da faixa de inteiros é -32. Ainda, os valores reais da primeira coluna estão 
representados pelos valores inteiros da segunda coluna. A Tabela 15 parte (b) 
apresenta a quantização com inteiros de 8 bits, porém, na segunda coluna, apresenta 
uma mudança nos valores reais, pois estes estão na faixa de -5 até +5.  
 
 
 
 


176 
 
 
Tabela 15 - Exemplos de quantização de valores reais em inteiros 
Valores 
Reais 
Inteiros  
6 bits 
 
Valores 
Reais 
Valores 
Reais 
Inteiros  
8 bits 
Faixa -1 a +1 
-32 a +31 
 
Faixa -1 a +1 
Faixa -5 a +5 
-128 a +127 
-1.00 
-32 
 
-1.00 
-5.00 
-128 
-0.97 
-31 
 
-0.99 
-4.96 
-127 
-0.94 
-30 
 
-0.98 
-4.92 
-126 
... 
... 
 
... 
... 
... 
0.00 
00 
 
0.00 
000 
000 
0.03 
01 
 
0.01 
0.00 
001 
0.06 
02 
 
0.02 
0.04 
002 
... 
... 
 
... 
... 
... 
0.97 
31 
 
0.99 
4.96 
127 
(a) 
 
(b) 
Fonte: Autoria Própria 
Além da quantização de valores reais para inteiros, efetuou-se a quantização 
na transformação de valores inteiros representados em diferentes faixas de bits. Tal 
processo foi necessário pois a multiplicação entre números inteiros, muito utilizada no 
treinamento e operação de uma RNA, gera valores com grande quantidade de bits. 
Neste caso, optou-se pela quantização para reduzir o espaço ocupado pela RNA no 
dispositivo FPGA. A Tabela 16 apresenta um exemplo com valores aleatórios, visando 
a demonstração de tal processo. 
Tabela 16 – Representação de valores inteiros com diferentes quantidades de bits 
Número 
Decimal 
(entre -5.0 e 
5.0) 
Tipo 
Representação em 31 bits 
Representação em 
15 bits 
Representação 
em 10 bits  
0.004  
Decimal 
8.589.935  
131 
4 
Binário 
correspon-
dente 
0000000100000110001001001101111 
000000010000011 
0000000100 
0.035 
Decimal 
15.000.000 
228 
7 
Binário 
correspon-
dente 
0000000111001001110000111000000 
000000011100100 
0000000111 
0.545 
Decimal 
234.123.000 
3572 
111 
Binário 
correspon-
dente 
0001101111101000110111011111000 
0001101111101000 
0001101111 
+5.0 
(+4.9999) 
Decimal 
1.073.741.823 
32767 
511 
Binário 
correspon-
dente 
0111111111111111111111111111111 
0111111111111111 
0111111111 
Fonte: Autoria Própria 
Por fim, quanto ao processo de quantização, utilizou-se operações de 
deslocamento de bits a fim de gerar os valores quantizados. Tal decisão de projeto foi 


177 
 
 
tomada pois as operações de deslocamento de bits utilizam registradores de 
deslocamento, e são considerados processos mais simples e mais rápidos do que 
divisores e multiplicadores, aumentando assim o desempenho de execução da 
quantização (HYDE, 2010). A Figura 47 apresenta um diagrama de atividades em UML 
do processo de quantização implementado. 
Figura 47 - Processo de quantização em NeuroPON-HD por meio de um diagrama de atividades UML 
 
Fonte: Autoria Própria 
O processo de quantização não é um Method LingPON-HD, mas sim uma 
função, escrita em VHDL, para dar suporte à tecnologia PON-HD, nas aplicações de 
RNA e onde quantizações sejam necessárias. Tal função foi incorporada ao código 
padrão de um Method em LingPON-HD. 
Devido à utilização de números inteiros foi necessário, ainda, implementar outra 
forma para o cálculo da função de transferência tangente hiperbólica, que não a 
implementada por números reais. Neste contexto, o trabalho de NAMIN et al. (2009) 
apresenta uma forma eficiente de se programar a tangente hiperbólica em hardware 
reconfigurável: utilizar uma lookup table (LUT) para armazenar os valores de entrada e 
de saída correspondentes, já quantizados. Tais valores são, portanto, calculados em 
software, quantizados e, posteriormente, colocados no dispositivo FPGA de forma fixa 
(hard coded) pelo compilador NeuroPON. Não obstante, a inovação proposta foi a de 
se comparar, via LUT, uma faixa de valores ao invés de apenas um valor de entrada 
com o valor de saída. Um exemplo desta LUT encontra-se na Tabela 17. 
 
 
 


178 
 
 
Tabela 17 – Tabela representativa de uma LookUp Table, implementada para a função que retorna  
a Tangente Hiperbólica de um valor, em NeuroPON. 
Entrada 
Saída 
 
Entrada 
Saída 
< 1344 
Entrada 
Saída 
>= 1216 
45 
>= 1152 
43 
>= 1088 
41 
>= 1024 
38 
>= 960 
36 
>= 896 
34 
>= 832 
31 
>= 768 
29 
>= 704 
27 
>= 640 
24 
>= 576 
22 
... 
... 
>= 64 
2 
else 
0 
 
 
< 2624 
Entrada 
Saída 
>= 2560 
83 
... 
... 
>= 1345 
49 
 
< 3986 
 
Entrada 
Saída 
>= 3904 
106 
... 
... 
>= 2623 
85 
 
senão (nenhum 
caso anterior) 
Entrada 
Saída 
>= 9088 
83 
... 
... 
>= 3985 
107 
 
Fonte: Autoria Própria 
No exemplo da Tabela 17, as entradas estão representadas em 15 bits, sendo 
que a saída está representada em 8 bits, ou seja, há um processo de quantização antes 
da disponibilização destes valores pelo Method. 
O processamento da função via a LUT desenvolvida (no caso a Tabela 17), 
verifica-se, primeiramente, a faixa em que se encontra o valor de entrada, pois a 
comparação de valores de entrada foi dividido em quatro faixas: de 0 a 1344, 1345 a 
2624, 2625 a 3986, e 3985 a 32767. Tal processo visou economizar tanto 
processamento quanto memória do dispositivo FPGA. Nestes termos, uma vez que o 
valor seja validado em uma das quatro faixas, há uma nova rodada de comparações, 
porém agora com 21 possibilidades diferentes em cada nova tabela (LUT). No exemplo 
da Tabela 17, utilizou-se “...” para informar o intervalo entre os valores indicados. Por 
fim, quando há o casamento entre a entrada da função e seu respectivo valor 
aproximado na LUT, a saída será o valor quantizado da função tangente hiperbólica.  
A faixa de valores da primeira coluna da tabela externa varia de 0 a 9088. No 
caso de se colocar todos os valores possíveis de entrada, o valor máximo seria 2n-1, 
sendo n a quantidade de bits do atributo de entrada (no caso, com 15 bits, o valor 
máximo permitido é 32767). Porém, verificou-se que a função tangente hiperbólica gera 


179 
 
 
sempre o valor 1 (neste caso, 127) com valores de entrada acima de 9088. Tal 
validação permitiu também uma economia de recursos do dispositivo FPGA.  
Ainda, valores negativos não possuem entradas na LUT, pois a verificação é 
feita desconsiderando-se o sinal. No caso de um valor de entrada negativo, uma flag é 
ativada, modificando assim o sinal do valor resultante. Tal processo também possibilitou 
a utilização de uma LUT de menor tamanho, consequentemente economizando espaço 
no dispositivo FPGA.  
Por fim, quanto ao fluxo da cadeia de notificações, tanto para execução quanto 
para treinamento, este é o mesmo apresentado na Figura 37 e na Figura 38 (página 
136) respectivamente. A fim de apresentar uma sequência de etapas mais detalhada, 
a Figura 48 apresenta um diagrama de atividades UML contendo, como ações do 
diagrama, os Methods PON a serem implementados. 
As atividades do diagrama da Figura 48 estão devidamente dispostas em pistas 
(lanes), sendo que cada pista representa a neuro-entidade relacionada às atividades. 
Neste âmbito, a pista central representa a entidade Network, a pista da esquerda 
representa as entidades Neuron da camada escondida, e a pista da direita as entidades 
Neuron da camada de saída da RNA. Ainda, a apresentação em cascata na parte 
superior do diagrama, aponta que pode haver mais de uma entidade Neuron em cada 
uma das camadas, e que estão executando suas ações em paralelo. 
O diagrama apresenta áreas pontilhadas, que agrupam os métodos utilizados 
para efetuar a propagação à frente (forward propagation) e a retro-propagação 
(backpropagation), nas entidades Neuron. Ainda, conforme já apontado, o processo é 
iniciado pela mudança no valor do Attribute attNumEpochs, que notifica (via Premise-
Condition) a NeuroRule responsável por verificar o valor de tal Attribute (via Action-
Instigation-Method). Caso a quantidade de épocas seja menor do que o limite 
especificado, a computação das entidades Neuron da camada escondida é iniciada. 
Após o processamento de todas as entidades Neuron da camada escondida, o 
controle volta à entidade Network, que dispara os cálculos para a camada de saída. 
Uma vez encerrado o processo em todas as camadas, a entidade Network (que retoma 
o controle) verifica se há outros padrões a serem utilizados em um treinamento. Caso 
contrário, a entidade verifica se ainda existem épocas a serem processadas. No caso 
de todas as épocas terem sido processadas, o treinamento é encerrado. 
 
 
 


180 
 
 
Figura 48 - Diagrama de Atividades UML: detalhamento da cadeia de notificações, por meio  
da apresentação dos Methods PON a serem implementados em LingPON-HD 
 
Fonte: Autoria Própria. 
 


181 
 
 
5.7.2 Codificação 
Para o treinamento da função XOR em hardware (utilizando PON-HD) foram 
declaradas duas entradas, dois neurônios na camada escondida e um neurônio de 
saída. Conforme apontado, o processamento em LingPON-HD utiliza a quantização 
para a representação de valores reais em valores inteiros quando necessário. Neste 
contexto, Tabela 18 apresenta os valores utilizados no experimento. 
Tabela 18 - Valores utilizados no experimento XOR em NeuroPON-HD 
Attributes 
Medida 
Entradas 
Pesos 
Saída 
i0 
i1 
w00 
w01 
w10 
w11 
o0 
Bits 
6 
6 
10 
10 
10 
10 
6 
Valor Quantizado 
31 
31 
52 
52 
52 
52 
31 
Valor Real 
1 
1 
0.5 
0.5 
0.5 
0.5 
1 
Faixa 
-1 a +1 
-1 a +1 
-5 a +5 
-5 a +5 
-5 a +5 
-5 a +5 
-1 a +1 
Validação 
0.969 
0.969 
0.508 
0.508 
0.508 
0.508 
0.969 
Fonte: Autoria Própria 
Os valores apontados na Tabela 18 são utilizados apenas no experimento, 
visando a comparação de valores com a solução implementada em software, utilizando 
a linguagem C, apresentada na Seção 5.1. Assim, no contexto da tabela, as medidas 
utilizadas são: 
 Bits: tamanho, em bits, do Attribute a ser implementado em VHDL. Tal 
informação também é utilizada no processo de quantização; 
 Valor quantizado: valor do Attribute já quantizado, representado em números 
inteiros. No caso das entradas, na tabela representada, o valor 31 é o maior 
valor positivo que pode ser representado por 6 bits, representando assim o 
maior valor na faixa dos números reais (neste caso o valor é 1); 
 Valor real: valor do Attribute antes da quantização, representado em 
números reais. Neste caso das entradas é representado o valor das entradas 
ajustas em 1; 
 Faixa: limites de representação do valor real. No caso das entradas e saída, 
o valor de cada Attribute por variar de -1 até 1; no caso dos pesos, o valor 
de cada pode variar de -5 até 5. 


182 
 
 
 Validação: tais valores são o resultado da “desquantização”, i. e. o processo 
de transformar o valor inteiro quantizado em um valor real. Tal medida aqui 
é interessante para que se possa verificar a diferença entre o valor real 
original e o calculado. 
O processo de quantização não é efetuado apenas nos valores de entradas, 
pesos sinápticos e de saídas. Devido à restrição de todos os Attributes numéricos 
estarem declarados como valores inteiros, os cálculos efetuados no treinamento, 
principalmente na retro-propagação, geram valores que podem ultrapassar 10 dígitos 
decimais. Neste contexto, a quantização é efetuada nos valores dos Attributes de: 
 saída dos neurônios; 
 produto de derivadas; 
 delta de atualização de pesos sinápticos; 
 controle de erros. 
Devido à sua utilização durante o treinamento, houve a criação de um token 
para informar a quantização durante o processo de análise léxica e sintática na 
compilação do código LingPON-HD para sua transformação em VHDL. Neste contexto, 
utilizou-se o símbolo de dois pontos (:) para sua representação no código. O Código 22 
apresenta um código de exemplo.  
Código 22 - Código em LingPON-HD apresentando o token para a função de quantização 
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
fbe fHiddenNeuron 
    attributes 
 
 
... 
    end_attributes 
    methods 
 
 
... 
 
 
method mtHNbDeltaBias(atHNbDeltaB = atHNbHSignal / net.atLR) 
 
 
method mtHNbDeltaBiasQtz(atHNbDeltaQtzB = atHNbDeltaB : 10) 
 
 
method mtHNbUpdBias(atHNbBias = atHNbBias + atHNbDeltaQtzB) 
 
 
... 
 
end_methods 
end_fbe 
Fonte: Autoria Própria 
Assim, a linha 39 do código do Código 22 apresenta um Method que efetua a 
quantização do Attribute atHNbDeltaB para dez bits, e copia seu valor para o Attribute 
atHNbDeltaQtzB. 
Conforme já apontado, além da quantização foi implementada uma função que 
retorna a tangente hiperbólica de um valor informado. A fim de apresentar um trecho 


183 
 
 
de código que implementa a Tabela 17, o Código 23 apresenta um trecho de código 
demonstrando a LUT desenvolvida. 
Código 23 - Trecho de código VHDL que implementa a LUT da função de transferência  
Tangente Hiperbólica em NeuroPON-HD 
01 
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
 
41 
42 
43 
 
125 
126 
127 
128 
129 
130 
... 
SUBTYPE stIn_a_value IS STD_LOGIC_VECTOR(bits_in_a-1 downto 0); 
SUBTYPE stIn_b_value IS STD_LOGIC_VECTOR(bits_in_b-1 downto 0); 
SUBTYPE stOut_value IS STD_LOGIC_VECTOR(bits_res-1 downto 0); 
 
function hyTan(x : stIn_a_value) return stOut_value is 
 
variable ret : signed(bits_res-1 downto 0); 
 
variable y   : natural range 0 to 2**(bits_in_a-1)-1; 
begin 
 y:=to_integer(abs(signed(x))); 
 
   if (y < 1344) then 
  
  if (y >= 1280) then ret:=to_signed(47, bits_res); 
  
  elsif (y >= 1216) then ret:=to_signed(45, bits_res); 
  
  elsif (y >= 1152) then ret:=to_signed(43, bits_res); 
  
  elsif (y >= 1088) then ret:=to_signed(41, bits_res); 
  
  elsif (y >= 1024) then ret:=to_signed(38, bits_res); 
  
  elsif (y >= 960) then ret:=to_signed(36, bits_res); 
  
  elsif (y >= 896) then ret:=to_signed(34, bits_res); 
...   
  
  else ret:=(others => '0'); 
  
  end if; 
   elsif (y < 2624) then 
... 
 
end if; 
 
if (signed(x) < 0) then 
 
 
ret := resize((-1 * ret),bits_res); 
 
end if; 
 
return std_logic_vector(ret); 
end function hyTan; 
Fonte: Autoria Própria 
O Código 23 apresenta, das linhas 20 a 125, o processo de comparação para 
a sintetização da LUT em hardware19. A fim de se efetuar uma quantidade menor de 
comparações, dividiu-se a faixa de valores em quatro partes, para que dentro desta 
faixa fossem feitas as comparações. Por meio desta codificação, foram sintetizadas 
quatro LUT, porém, na utilização desta função, uma quantidade menor de comparações 
será efetuada. A grande vantagem apontada por esta implementação é a economia de 
área do chip, pois diminui-se as linhas da tabela devido à menor quantidade de 
comparações para a faixa de valores esperada (MUSCEDERE; LEBOEUF, 2008; 
NAMIN et al., 2009). 
Assim como na quantização, um token para a utilização da função que retorna 
a tangente hiperbólica de um valor foi inserido na em LingPON-HD. Neste contexto, 
definiu-se que o caractere til (~) fosse utilizado com a finalidade de retornar a tangente 
 
19 O restante do código apresentado não será aqui explanado por ser código auxiliar ao uso de 
LUT para a representação de função de transferência. 


184 
 
 
hiperbólica quantizada (aproximada) de um valor de entrada. O Código 24 apresenta 
um trecho de código de tal utilização. 
Código 24 - Utilização da função de Tangente Hiperbólica em LingPON-HD 
32 
33 
… 
50 
51 
… 
60 
61 
62 
… 
101 
102 
fbe fHiddenNeuron 
    attributes 
 
 
... 
    end_attributes 
    methods 
 
 
... 
 
 
method mtHNbSumBias(atHNbSumProd = atHNbSumProd + atHNbBias) 
 
 
method mtHNbTanH(atHNbOutput = atHNbSumProd ~ 8) 
 
 
method mtHNbDerSquare(atHNbDerivative = atHNbOutput * atHNbOutput)  
 
 
... 
    end_methods 
end_fbe 
Fonte: Autoria Própria 
Assim, a linha 61 do Código 24 apresenta um Method responsável pelo cálculo 
da função de ativação de um neurônio. Neste caso, o Method efetua a tangente 
hiperbólica sobre o valor do Attribute atHNbSumProd com 8 bits, e copia seu valor para 
o Attribute atHNbOutput. No processo de compilação do código LingPON-HD para 
VHDL, a função que retorna o valor aproximado da tangente hiperbólica é incorporada 
ao código padrão do componente Method em VHDL, no padrão especificado pela 
tecnologia PON-HD. 
Conforme apontado na Seção 4.3, a geração de código NeuroPON para PON-
HD resulta em uma quantidade maior de entidades para controle de processos, devido 
à restrição dos Methods serem implementados com apenas uma operação e com dois 
parâmetros (Attributes e constantes). Tal implementação de controle é feita tanto na 
entidade Network quanto nas entidades Neuron. Nestes termos, a FBE Network é 
apresentada no Código 25. 
Código 25 - LingPON-HD: implementação da FBE Network em NeuroPON-HD 
01 
02 
03 
04 
05 
06 
07 
08 
09 
10 
11 
12 
13 
14 
15 
16 
fbe fNetwork 
    attributes 
 
 
integer atNumEpochs 0 
 
 
integer atTrainInput0 0 
 
 
integer atTrainInput1 0 
 
 
integer atTrainOutput0 0 
 
 
integer atReadTrainInputs 0 
 
 
integer atTotTrainInputs 0 
 
 
integer atNetProdSumON 0 
 
 
integer atLR 0 
 
 
integer atNetError 0 
 
 
boolean atNetStep1_1 false 
 
 
boolean atNetStep2_1a1 false 
 
 
boolean atNetStep2_2a false 
 
 
boolean atNetStep2_3 false 
 
 
boolean atNetStep3_1 false 


185 
 
 
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
 
 
integer atNumberOne 16384 
    end_attributes 
    methods 
 
 
method mtNetStep1_1_Reset(atNetStep1_1 = false) 
 
 
method mtNetStep2_1a1_Reset(atNetStep2_1a1 = false) 
 
 
method mtNetStep2_2a_Reset(atNetStep2_2a = false) 
 
 
method mtNetStep2_3_Reset(atNetStep2_3 = false) 
 
 
method mtNetStep3_1_Reset(atNetStep3_1 = false) 
 
 
method mtNetStep1_1_Set(atNetStep1_1 = true) 
 
 
method mtNetStep2_1a1_Set(atNetStep2_1a1 = true) 
 
 
method mtNetStep2_2a_Set(atNetStep2_2a = true) 
 
 
method mtNetStep2_3_Set(atNetStep2_3 = true) 
 
 
method mtNetStep3_1_Set(atNetStep3_1 = true) 
 
 
method mtNetReadTI_Reset(atReadTrainInputs = 0) 
 
 
method mtNetNextInput(atReadTrainInputs = atReadTrainInputs + 1) 
 
 
method mtNetRaiseEpoch(atNumEpochs = atNumEpochs - 1)  
 
 
method mtNetProdSumONa0(atNetProdSumON = atNetProdSumON + on0.atONaProdSigQtzH0) 
 
 
method mtNetProdSumONa1(atNetProdSumON = atNetProdSumON + on0.atONaProdSigQtzH1) 
 
 
method mtNetONaErrorSum(atNetError = atNetError + on0.atONaError) 
 
 
method mtNetErrorHalf(atNetError = atNetError / 2) 
 
 
method mtNetErrorAvg(atNetError = atNetError / atTotTrainInputs) 
 
end_methods 
end_fbe 
Fonte: Autoria Própria 
As linhas 12 a 16 do Código 25, apresentam a declaração dos Attributes de 
controle e sincronização dos processos de operação e treinamento da RNA, e, da linha 
20 a 30, os Methods para ajuste de tais Attributes. Ressalta-se que tal código é gerado 
de forma automática pelo compilador NeuroPON, sendo que tais Attributes e Methods 
podem variar de acordo com a quantidade de entidades Neuron declaradas para as 
camadas escondidas e de saída da RNA. 
Conforme já apontado na definição do modelo de uma entidade Neuron, esta 
também possui vários Attributes de controle, dependendo para tanto da materialização 
escolhida como alvo para a implementação. Neste contexto, uma entidade Neuron 
(FBE fHiddenNeuronA) é apresentada noCódigo 26.  
Código 26 - FBE fHiddenNeuronA, que representa um neurônio da camada 
01 
02 
03 
04 
05 
06 
07 
08 
09 
10 
11 
12 
13 
14 
15 
16 
17 
18 
fbe fHiddenNeuronA 
 
attributes 
 
 
integer atHNaOutput 0 
 
 
integer atHNaSumProd 0 
 
 
integer atHNaWeightI0 0 
 
 
integer atHNaW0 0 
 
 
integer atHNaWeightI1 0 
 
 
integer atHNaW1 0 
 
 
integer atHNaBias 0 
 
 
integer atHNaB 0 
 
 
integer atHNaProdI0 0 
 
 
integer atHNaProdI1 0 
 
 
integer atHNaDerivative 0 
 
 
integer atHNaHSignal 0 
 
 
integer atHNaDeltaI0 0  
 
 
integer atHNaDeltaQtzI0 0  
 
 
integer atHNaDeltaI1 0  
 
 
integer atHNaDeltaQtzI1 0  


186 
 
 
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
78 
79 
80 
81 
82 
 
 
integer atHNaDeltaB 0  
 
 
integer atHNaDeltaQtzB 0  
// forward steps 
 
 
boolean atHNaStep1_1 false 
 
 
boolean atHNaStep1_2 false 
 
 
boolean atHNaStep1_3 false 
 
 
boolean atHNaStep1_4 false 
 
 
boolean atHNaStep1_5_ONStep false 
// backprop steps 
 
 
boolean atHNaStep2_1 false 
 
 
boolean atHNaStep2_2 false 
 
 
boolean atHNaStep2_3 false 
 
 
boolean atHNaStep2_4 false 
 
 
boolean atHNaStep3_1 false 
 
 
boolean atHNaStep3_2 false 
 
 
boolean atHNaStep3_3 false 
 
 
boolean atHNaStep3_4 false 
 
 
boolean atHNaStep3_5 false 
 
 
boolean atHNaStep3_6 false 
 
 
boolean atHNaStep3_7 false 
 
 
boolean atHNaStep3_8_NetStep false 
 
end_attributes 
 
methods 
// reset control attributes 
 
 
method mtHNaStep1_1_Reset(atHNaStep1_1 = false) 
 
 
method mtHNaStep1_2_Reset(atHNaStep1_2 = false) 
 
 
method mtHNaStep1_3_Reset(atHNaStep1_3 = false) 
 
 
method mtHNaStep1_4_Reset(atHNaStep1_4 = false) 
 
 
method mtHNaStep1_5_Reset(atHNaStep1_5_ONStep = false) 
// reset control attributes 
 
 
method mtHNaStep1_1_Set(atHNaStep1_1 = true) 
 
 
method mtHNaStep1_2_Set(atHNaStep1_2 = true) 
 
 
method mtHNaStep1_3_Set(atHNaStep1_3 = true) 
 
 
method mtHNaStep1_4_Set(atHNaStep1_4 = true) 
 
 
method mtHNaStep1_5_Set(atHNaStep1_5_ONStep = true) 
// Calc Methods 
 
 
method mtHNaSumProd01(atHNaSumProd = atHNaProdI0 + atHNaProdI1) 
 
 
method mtHNaProdI0(atHNaProdI0 = net.atTrainInput0 * atHNaWeightI0) 
 
 
method mtHNaProdI1(atHNaProdI1 = net.atTrainInput1 * atHNaWeightI1) 
 
 
method mtHNaSumBias(atHNaSumProd = atHNaSumProd + atHNaBias) 
 
 
method mtHNaTanH(atHNaOutput = atHNaSumProd ~ 8) 
// Derivative 
 
 
method mtHNaDerSquare(atHNaDerivative = atHNaOutput * atHNaOutput) 
 
 
method mtHNaDerDif(atHNaDerivative = net.atNumberOne - atHNaDerivative) 
 
 
method mtHNaHSigMul(atHNaHSignal = atHNaDerivative * net.atNetProdSumON) 
 
 
method mtHNaHSignal(atHNaHSignal = atHNaHSignal : 8) 
// UpdWeight 
 
 
method mtHNaDeltaSigI0(atHNaDeltaI0 = atHNaHSignal * net.atTrainInput0) 
 
 
method mtHNaDeltaLRI0(atHNaDeltaI0 = atHNaDeltaI0 / net.atLR) 
 
 
method mtHNaDeltaQtzI0(atHNaDeltaQtzI0 = atHNaDeltaI0 : 10) 
 
 
method mtHNaUpdWeightI0(atHNaWeightI0 = atHNaWeightI0 + atHNaDeltaQtzI0) 
 
 
method mtHNaDeltaSigI1(atHNaDeltaI1 = atHNaHSignal * net.atTrainInput1) 
 
 
method mtHNaDeltaLRI1(atHNaDeltaI1 = atHNaDeltaI1 / net.atLR) 
 
 
method mtHNaDeltaQtzI1(atHNaDeltaQtzI1 = atHNaDeltaI1 : 10) 
 
 
method mtHNaUpdWeightI1(atHNaWeightI1 = atHNaWeightI1 + atHNaDeltaQtzI1) 
 
 
method mtHNaDeltaBias(atHNaDeltaB = atHNaHSignal / net.atLR) 
 
 
method mtHNaDeltaBiasQtz(atHNaDeltaQtzB = atHNaDeltaB : 10) 
 
 
method mtHNaUpdBias(atHNaBias = atHNaBias + atHNaDeltaQtzB) 
// output weights 
 
 
method mtHNaSetW0(atHNaW0 = atHNaWeightI0) 
 
 
method mtHNaSetW1(atHNaW1 = atHNaWeightI1) 
 
 
method mtHNaSetB(atHNaB = atHNaBias) 
 
end_methods 
end_fbe 
Fonte: Autoria Própria 


187 
 
 
Conforme apresentado no Código 26, são cinco Attributes para o controle da 
propagação e 12 Attributes para o controle da retro-propagação onde cada um 
representa uma etapa das fases de treinamento. Tais Attributes são utilizados nas 
Premises que compõe uma NeuroRule, juntamente com outras Premises pertinentes. 
O Código 27 apresenta o código da NeuroRule que valida o início do processamento 
da cadeia de notificações. 
Código 27 – NeuroRule em LingPON-HD, para o controle do  
início dos cálculos dos neurônios 
405 
406 
407 
408 
409 
410 
411 
412 
413 
414 
415 
416 
417 
rule rlNetStartCalc 
 
condition 
 
  subcondition cdNetStartCalc 
 
 
 premise prNetStartCalcR net.atReadTrainInputs < net.atTotTrainInputs and 
 
 
 premise prNetStartCalcS21 net.atNetStep3_1 == true 
 
  end_subcondition 
 
end_condition 
 
action 
 
 
instigation inStartCalcS31 net.mtNetStep3_1_Reset(); 
 
 
instigation inStartCalcH0S11 hn0.mtHNaStep1_1_Set(); 
 
 
instigation inStartCalcH1S11 hn1.mtHNbStep1_1_Set(); 
 
end_action 
end_rule 
Fonte: Autoria Própria 
O Código 27 apresenta: 
 Linha 408: Premise para validar se a quantidade de entradas de treinamento 
lidas é menor do que a quantidade total de entradas de treinamento; 
 Linha 409: Premise para validar o Attribute de controle das etapas de 
processamento da RNA em si; 
 Linha 413: Instigation para o Method que torna o Attribute de controle falso. 
Tal procedimento impede que, mesmo que a Premise prNetStartCalcR seja 
verdadeira, os Methods desta Rule não sejam instigados; 
 Linhas 414 e 415: Instigations para os Methods que ajustam os Attributes de 
controle do início dos cálculos no neurônio hn0 e hn1, da camada escondida, 
respectivamente. 
Neste caso a instigação dos Methods e, por consequência, sua execução serão 
efetuadas de forma totalmente paralela no circuito do dispositivo FPGA. Se houver mais 
de uma entidade PON instanciada, com seus Attributes e Methods pertencentes a uma 
NeuroRule, todos serão executados paralelamente. 
Conforme apontado na Seção 3.3.6 (página 116), a tecnologia PON-HD opera 
com componentes já implementados, de forma genérica, que são apenas 


188 
 
 
parametrizados durante a compilação. Assim, o sinal que representa a saída de um 
Attribute, está diretamente ligado ao sinal que informa que as Premises estão 
aprovadas, que está diretamente conectado ao sinal de execução de um Method. Todo 
este processo de notificação é feito por conexões entre componentes no código PON-
HD em VHDL e, posteriormente, sintetizados e gravados no dispositivo FPGA. Neste 
contexto, a fim de exemplificar seu funcionamento, a o Código 28 apresenta o código 
VHDL e a Figura 49 apresenta um diagrama de blocos da Netlist criada pelo sintetizador 
da ferramenta Quartus II da Altera.   
Código 28 - VHDL NeuroPON-HD: implementação dos sinais 
405 
406 
407 
408 
409 
410 
 
432 
433 
434 
435 
436 
437 
... 
net_mtNetStep3_1_Reset_execute <= (prNetRaiseEpoch_result) OR  
                                  (prNetStartCalcS21_result AND prNetStartCalcR_result); 
hn0_mtHNaStep1_1_Set_execute <= (prNetStartCalcS21_result AND prNetStartCalcR_result); 
hn1_mtHNbStep1_1_Set_execute <= (prNetStartCalcS21_result AND prNetStartCalcR_result); 
 
... 
 
net_mtNetStep3_1_Reset: NOP_method  
GENERIC MAP(bits_in_a=> 1, bits_in_b => 1, bits_res => 1, dataType => 1, operation => 0)  
PORT MAP(in_a => net_mtNetStep3_1_Reset_input_a, in_b => net_mtNetStep3_1_Reset_input_b, 
execute => net_mtNetStep3_1_Reset_execute, result => net_mtNetStep3_1_Reset_output, notify 
=> net_mtNetStep3_1_Reset_notify); 
Fonte: Autoria Própria 
Conforme o diagrama da Figura 49, o único componente que opera respeitando 
a sincronia do sistema, via sinal de clock (att_clock), é o componente Attribute 
(NOP_attribute), sendo que o restante dos componentes estão conectados entre si, 
sem receber o sinal de clock. Neste âmbito, assim que houver um sinal de clock 
(respeitando a borda de subida), o valor do Attribute é atualizado, e as entradas das 
Premises 
(NOP_premise) 
a 
ele 
conectadas 
também 
são 
atualizadas. 
Consequentemente, os Methods que possuem os sinais de controle da própria 
execução (execute) conectados às saídas de tais Premises, são ativados, executando 
assim a ação que lhes foi conferida pela parametrização via compilador LingPON-HD. 
Pode-se observar na Figura 49, que os componentes contidos dentro das áreas 
pontilhadas operam em paralelo, pois todos recebem um sinal a partir de uma porta 
lógica OU, que efetua uma disjunção entre a saída das Premises ao mesmo tempo. 
Todo esse processo deve ocorrer em um ciclo de clock, pois os Methods ajustam 
determinados Attributes (saídas notify e result[0]) que devem estar atualizados para 
que, no próximo sinal de sincronismo, possam atualizar seus valores. 
 
 


189 
 
 
Figura 49 - Recorte da Netlist, do circuito LingPON-HD em VHDL, gerada sintetizador da ferramenta 
Quartus II: componentes sintetizados que implementam o Código 28. 
 
Fonte: Autoria Própria. 
Quanto aos códigos escritos em LingPON-HD, apresentados nesta seção, é 
pertinente ressaltar que estes são gerados por meio do compilador NeuroPON. 
Primeiramente, o compilador realiza a validação da estrutura e dos dados do arquivo 
description.xml que contém a parametrização da RNA a ser gerada. Esta validação é 
feita por meio do arquivo definition.xsd, que contém as regras impostas pela linguagem 
ViNNSL. 
Uma vez que o arquivo foi validado, o compilador lê os parâmetros 
especificados no arquivo description.xml. Tais parâmetros, especificados via linguagem 
XML, são elencados em uma estrutura de árvore por meio de uma API do Document 
Object Model (DOM). Neste âmbito, o compilador extrai os dados desta árvore 
hierárquica e, por meio da análise de tais dados, cria os códigos em LingPON para o 
treinamento de uma RNA MLP por meio de BP.  
O Código 29 apresenta um trecho de código do arquivo description.xml, 
utilizado para a descrição de uma RNA em NeuroPON. 
Código 29 - Trecho de código do arquivo de descrição (description.xml) de RNA em NeuroPON 
32 
33 
34 
35 
36 
37 
38 
... 
    <structure> 
      <input> 
 
 
  <ID>Input1</ID> 
 
 
  <dimension> 
 
 
 
<min>2</min> 
 
 
 
<max>2</max> 


190 
 
 
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
 
 
  </dimension> 
 
 
  <size> 
 
 
 
<min>1</min> 
 
 
 
<max>1</max> 
 
 
  </size> 
      </input> 
      <hidden> 
        <ID>Hidden1</ID> 
        <dimension> 
          <min>2</min> 
          <max>2</max> 
        </dimension> 
        <size> 
          <min>1</min> 
          <max>1</max> 
        </size> 
      </hidden> 
      <output> 
        <ID>Output1</ID> 
        <dimension> 
          <min>1</min> 
          <max>1</max> 
        </dimension> 
        <size> 
          <min>1</min> 
          <max>1</max> 
        </size> 
      </output> 
      <connections>fullconnected</connections> 
    </structure> 
... 
Fonte: Autoria Própria 
No Código 29 estão destacados (em negrito) os elementos que informam a 
quantidade de entradas, neurônios escondidos e neurônios de saída, que são 
basicamente as informações lidas pela atual versão do interpretador NeuroPON. A título 
de exemplo, os valores informados no Código 29 são os dados utilizados no presente 
experimento, ou seja, duas entradas, dois neurônios na camada escondida e um 
neurônio de saída. O código completo deste arquivo encontra-se no Apêndice C. 
5.7.3 Resultados do Experimento 
Os testes foram conduzidos no simulador ModelSim, aplicativo integrante da 
ferramenta Quartus v.13 da Altera Corporation. Para a operacionalização dos testes, 
um arquivo de testbench, em VHDL, foi criado. Tal arquivo, instancia um componente 
como sendo a RNA em NeuroPON e, a partir da informação de portas de entrada e 
saída, os valores são inseridos no componente instanciado para testes. 
Na arquitetura desta entidade VHDL testbench, um sinal de clock é gerado, 
permitindo assim o sincronismo na operacionalização dos elementos do circuito. Ainda, 
um processo é criado, a fim de informar os valores dos padrões de treinamento 
(entradas e saídas), total de padrões a serem utilizados, valor de inicialização dos 


191 
 
 
pesos, taxa de aprendizagem, quantidade de épocas de treinamento e o valor do Bias 
em cada camada neuronal. 
Dois laços de repetição também são criados, sendo um para o controle das 
épocas e outro para controle das entradas de treinamento20. Neste caso, a ação de 
disponibilização dos valores de treinamento é feita aos sinais de entrada, de maneira 
aleatória. 
Os resultados deste experimento foram comparados com os resultados de 
outros dois experimentos que implementam uma RNA restrita a valores numéricos 
inteiros. Neste contexto, os experimentos construídos foram uma RNA MLP 
implementada em linguagem C procedimental, e uma RNA MLP implementada em 
VHDL, ambas com processos de treinamento seguindo os conceitos do método 
Backpropagation (BP). 
A implementação em linguagem C procedimental, utilizando apenas valores 
inteiros, serviu como uma referência para o desenvolvimento em hardware. Como todos 
os experimentos anteriores à tese foram efetuados com números reais, não havia um 
parâmetro para que se pudesse comparar os novos experimentos.  
Além deste experimento em software, foi desenvolvido um experimento para 
ser executado diretamente em hardware reconfigurável (FPGA). Tal experimento visou 
comparar seus resultados, tanto estruturais quanto temporais, com o modelo 
computacional NeuroPON implementado via tecnologia PON-HD. Assim, seguindo os 
conceitos do Paradigma Imperativo (PI) utilizados no desenvolvimento da RNA MLP em 
linguagem C procedimental, tal experimento foi implementado diretamente na 
linguagem VHDL. 
Mesmo que o código interno às funções tenha sido implementado seguindo os 
conceitos do PI, a implementação deste experimento levou em conta conceitos de 
paralelismo em hardware, componentização dos neurônios e bibliotecas de funções, 
porém sem seguir os conceitos do modelo computacional NeuroPON. Neste contexto, 
o desenvolvedor possui o conhecimento necessário para se descrever um hardware via 
linguagem VHDL. A Tabela 19 apresenta um comparativo entre tais implementações. 
Em tempo, os três experimentos de implementação da RNA restrita a números 
inteiros, utilizaram a mesma quantidade de entradas, neurônios da camada escondida 
e da camada de saída, bem como a mesma função de transferência. 
 
20 Tais controles são efetuados neste arquivo pois é um arquivo utilizado para testes. Em outros 
casos, o controle é efetuado pelas NeuroRules pertinentes durante o ciclo de notificações do NeuroPON. 


192 
 
 
Tabela 19 - Resultados dos experimentos de implementação de RNA por meio de VHDL 
Parâmetro 
Implementação 
Tradicional 
Implementação 
NeuroPON 
Elementos Lógicos 
5336 
6149 
Funções combinacionais 
5318 
5733 
Registradores lógicos dedicados 
196 
915 
Pinos 
293 
257 
Multiplicadores embarcados 
58 
44 
Frequência máxima de clock 
5.21 MHz (hidden) 
10.61 MHz 
10.94 MHz (output) 
178.57 MHz (clock) 
Dispositivo FPGA 
Cyclone IV E – EP4CE115F29C7 
Ciclos de clock necessários para execução de um 
padrão de treinamento. 
9 
39 
Fonte: Autoria Própria 
Como esperado, a solução implementada via tecnologia PON-HD utiliza uma 
quantidade maior de registradores, uma vez que os Attributes são implementados com 
este tipo de estrutura. Neste caso, como a solução desenvolvida para o treinamento BP 
em uma RNA MLP utiliza Attributes de controle para a sincronização dos processos, 
uma quantidade maior de registradores será utilizada. 
Quanto à frequência de execução (clock) suportada pelo circuito, a diferença 
alcançada entre os experimentos reside na forma de implementação da própria 
tecnologia PON-HD. Em PON-HD, apenas os Attributes possuem sinal de 
sincronização, sendo que tais Attributtes respeitam um ciclo de clock para propagar o 
valor das entradas para as saídas, protegendo o circuito de possíveis condições de 
corrida (Race Conditions) (KERSCHBAUMER, 2018). 
A implementação dita “tradicional” baseada em PI possui três sinais de 
sincronização: 
 Clock: sinal geral, i. e., utilizado para a sincronização do funcionamento de 
toda a RNA, desde os processos de controle de épocas até a aferição dos 
erros gerados durante o treinamento; 
 HiddenBhv: sinal para a sincronização dos neurônios da camada escondida; 
 OutputBhv: sinal para a sincronização dos neurônios da camada de saída; 


193 
 
 
Mesmo que o clock de sincronização geral tenha uma frequência máxima de 
178,57 MHz, o circuito deve respeitar a frequência de operação mais lenta, que, neste 
caso, é do componente que implementa um neurônio da camada escondida, e possui 
uma frequência de 5,21 MHz. Assim, tanto o clock principal quanto o clock do 
componente que implementa os neurônios da camada de saída (que opera numa 
frequência de 10,94 MHz), não executam ações efetivas ao treinamento da RNA em 
todos seus pulsos, pois estas são executadas na menor frequência máxima registrada 
no circuito. 
Outra característica pertinente a ser analisada é a quantidade de ciclos de clock 
necessários para execução de um padrão de treinamento. Pode-se observar que a 
solução NeuroPON utiliza 30 ciclos de clock a mais do que a solução tradicional. Neste 
contexto, seriam necessários 113% mais ciclos de clock na solução NeuroPON em 
comparação à tradicional. Efetuando-se, portanto, regras de três simples, obtém-se a 
proporção entre os experimentos. 
0120%+3
0120%4567
= 10,61
5,21 = 2,04 
(9) 
0012<_0120%+3
>.1?çã2+3
_4567
= 39
2,04 = 19,15 
(10) 
 
0012<_0120%+3
_4567
0012<_0120%4567
= 19,15
9
= 2,13 ∴113% 
(11) 
 
A equação (9) define a proporção entre o clock do circuito em NeuroPON com 
o circuito tradicional. Tal valor é utilizado, na equação (10), para definir quantos ciclos 
de clock seriam necessários na aplicação PON se configurada como a aplicação 
tradicional. E, por fim, a equação (11) apresenta a relação entre a quantidade de ciclos 
de clock, com a mesma parametrização, nos dois experimentos. 
5.7.4 Considerações 
A Tecnologia LingPON-HD 1.0 mostrou-se um ferramental funcional para o 
desenvolvimento da NeuroPON em hardware digital. Particularmente, a codificação em 
alto nível é um facilitador para expressar o arranjo de entidades neurais à luz do PON. 
Entretanto, fez-se necessário alguns ajustes na Tecnologia LingPON-HD 1.0, 
particularmente no componente que implementa os Methods, visando a viabilização do 


194 
 
 
NeuroPON HD. Neste contexto, adicionou-se o processo de quantização de valores 
inteiros, bem como a função Tangente Hiperbólica quantizada (aproximada), utilizando 
apenas números inteiros.  
Uma vez estabelecido o necessário para se ter o NeuroPON HD, foi então feito 
a codificação da NeuroPON HD em si, com topologia RNA MLP, utilizando a LingPON-
HD 1.0. Uma vez que a NeuroPON-HD estava estabelecida, foi possível então realizar 
os testes de treinamento, por meio de compilador e simulador para VHDL.  
No primeiro experimento desenvolvido visando treinamento e operação em 
hardware, a quantidade de ciclos de clock, para a execução de uma época de 
treinamento pelo método BP em NeuroPON-HD, foi maior do que na implementação 
dita “tradicional” no mesmo hardware. Este resultado deve-se ao fato do próprio 
processo de notificações do PON. Conforme apresentado pela equação (1) (página 65), 
o cálculo que gera a saída de um neurônio em RNA possui uma função de somatório 
em seu desenvolvimento. Tal função precisa efetivar diversas somas em sequência, 
por meio de um acumulador, ou separando-se os valores a serem somados em pares. 
Assim, a fim de realizar tal processo via LingPON, é necessário criar vários Methods 
contendo, cada um, a soma de dois valores pertencentes a tal somatório, até atingir o 
último valor da equação. Outrossim, como tais Methods não podem estar agrupados 
numa mesma Action (onde seriam instigados em paralelo), é necessário utilizar um 
Attribute de controle que dispara uma notificação pois toda a cadeia de notificação deve 
ser executada (Attribute – Premise – Condition – Action – Instigation – Method). 
Neste contexto, modificações na própria estrutura da Tecnologia LingPON-HD 
teriam que ser efetuadas, visando a melhoria no NeuroPON-HD. Uma hipótese seria a 
utilização de Methods diferenciados, ou modificações na estrutura de uma Action, onde 
seria possível informar quais instigações são sequenciais e quais são paralelas, 
permitindo uma estratégia diferenciada de instigação. Não obstante, é importante 
lembrar que a tecnologia PON-HD ainda está naturalmente em fase prototipal de 
desenvolvimento, sendo que melhorias devem surgir em futuras versões. 
Por fim, de forma transparente ao usuário, a partir do código gerado foi possível 
alcançar execução  dos neurônios de uma RNA MLP de forma paralela em um 
simulador FPGA. Em tempo, o código declarativo gerado em LingPON para tal ocorre 
de maneira automatizada a partir de uma linguagem descritiva, utilizando o padrão 
ViNNSL, por meio de um interpretador. Neste caso, um usuário NeuroPON sem 
conhecimentos técnicos em descrição de hardware e nem mesmo de LingPON 
(linguagem de regras), pode parametrizar a geração de RNA para treinamento e 


195 
 
 
operação efetuados em FPGA por meio da utilização da linguagem descritiva em 
questão. 
Isto posto, o próximo experimento visa avaliar a escalabilidade do modelo 
computacional NeuroPON Prototipal para hardware reconfigurável. 
5.8 RNA MLP para IRIS com LingPON-HD 
O segundo experimento efetuado por meio da Tecnologia PON-HD trata-se da 
implementação de uma RNA MLP, com treinamento por meio do método BP, sobre a 
base de dados da flor de íris (IRIS DataSet).  
5.8.1 Desenvolvimento 
Para o desenvolvimento deste experimento, utilizou-se, em geral, as mesmas 
prerrogativas do experimento efetuado sobre a função XOR. Neste contexto, utilizou-
se apenas valores com números inteiros, efetuando-se o processo de quantização 
sobre valores reais. O mesmo processo também foi efetuado sobre a função de 
ativação tangente hiperbólica, representada por uma LUT no dispositivo FPGA.  
Uma vez que o modelo computacional NeuroPON propõe que a RNA seja 
implementada via linguagem descritiva/declarativa, ficando a cargo do compilador a 
geração de código para o processo de treinamento e operação da RNA, o planejamento 
do experimento para IRIS DataSet deveria apenas considerar a mudança nas 
quantidade de neurônios em cada camada, a quantidade de padrões de treinamento, e 
os pesos sinápticos. Não obstante, a compilação do código NeuroPON VHDL gerado 
não teve sucesso, pois a quantidade de pinos necessários na interface do dispositivo 
era muito alta, ultrapassando a disponibilidade do dispositivo FPGA.  
No experimento com a função XOR, a valoração, tanto dos pesos sinápticos 
quanto dos padrões de treinamento, foi efetuada utilizando-se a interface do dispositivo, 
por meio de pinos de entrada. Como o IRIS DataSet possui uma quantidade maior de 
entradas e padrões de treinamento, mais pesos sinápticos precisam ser definidos, 
ocupando assim uma quantidade maior de pinos de entrada e saída do dispositivo.  
A fim de demonstrar as diferenças entre os experimentos, no quesito 
quantidade de entradas e saídas, a Tabela 20 apresenta a estrutura da RNA, a 
quantidade de cada elemento, bem como a quantidade de bits a serem ocupados no 
dispositivo FPGA no treinamento da função XOR e IRIS DataSet. 


196 
 
 
Tabela 20 - Quantidade de elementos necessários à RNA, e seu tamanho em bits 
Função 
Entradas 
Pesos 
Neurônios 
Pesos 
Neurônios 
Total de bits 
Qtde 
Bits 
Entrada 
para 
escondida 
Bits 
Camada 
Escondida 
Bits 
Escondida 
para Saída 
Bits 
Camada de 
Saída 
Bits 
XOR 
2 
12 
4 
40 
2 
16 
2 
20 
1 
8 
107 
IRIS 
4 
24 
20 
200 
5 
40 
15 
150 
3 
24 
485 
Fonte: Autoria Própria 
Conforme apresentado na Tabela 20, a quantidade total de pinos necessária 
na interface do dispositivo é, aproximadamente, 4,5 vezes maior na RNA para IRIS 
DataSet em comparação a RNA para a função XOR. Neste contexto, o dispositivo 
utilizado no experimento (Cyclone IV E – EP4CE115F29C7) não comporta a quantidade 
de bits necessária. 
Efetuou-se, portanto, uma pesquisa na busca de dispositivos FPGA que 
tivessem a quantidade de pinos necessária. Os resultados apontaram que dispositivos 
comerciais e, até mesmo, disponíveis para experimentação na ferramenta Quartus II, 
não continham a quantidade de pinos necessária para se executar o experimento.  
Neste contexto, a decisão de projeto tomada foi a de desenvolver processos 
para leitura e escrita dos pesos e padrões de treinamento, utilizando sinais internos ao 
dispositivo FPGA, eliminando tais valores da interface do dispositivo. Assim, a 
quantidade de pinos a serem utilizados independe da quantidade de estruturas criadas 
na RNA, bem como da quantidade de entradas, saídas, e pesos sinápticos necessários. 
Nesta nova proposta, a interface é utilizada somente para o ajuste do Attribute utilizado 
para iniciar o processamento da cadeia de notificações, da quantidade de épocas de 
treinamento, do total de padrões de teste, da taxa de aprendizagem, do sinal de 
sincronismo (clock) e do sinal de configuração. O Código 30 apresenta o código VHDL 
da interface da entidade neuropon. 
Código 30 - Definição dos sinais de entrada e saída (interface) da entidade neuropon, em VHDL 
8 
9 
10 
11 
12 
13 
14 
15 
16 
ENTITY neuropon IS 
    PORT (in_net_atNStep1_1         : in std_logic; 
          in_set_net_atNStep1_1     : in std_logic; 
          in_net_atNumEpochs        : in std_logic_vector(8-1 downto 0); 
          in_set_net_atNumEpochs    : in std_logic; 
          in_net_atTotalTI          : in std_logic_vector(8-1 downto 0); 
          in_set_net_atTotalTI      : in std_logic; 
          in_net_atLR               : in std_logic_vector(10-1 downto 0); 
          in_set_net_atLR           : in std_logic; 


197 
 
 
17 
18 
19 
20 
          out_net_atNErr            : out std_logic_vector(15-1 downto 0); 
          in_cfgStart               : in std_logic; 
          clock                     : in std_logic); 
END neuropon; 
Fonte: Autoria Própria 
Além das entradas, houve mudanças na interface de saída do dispositivo que 
embarca a entidade neuropon, por meio da remoção dos pesos sinápticos. Uma vez 
que o processo de treinamento modifica o valor dos pesos sinápticos, é necessário que 
estes novos valores estejam disponíveis ao final do treinamento. Neste contexto, na 
implementação do NeuroPON no experimento da função XOR, os pesos sinápticos 
ficavam disponíveis na interface de saída do dispositivo. Na implementação da RNA 
para IRIS DataSet, ao final da atualização dos pesos sinápticos, os valores dos pesos 
sinápticos são disponibilizados na memória do dispositivo. Neste experimento, no 
arquivo testbench, a memória secundária foi utilizada por meio de um arquivo texto. 
 Além disso, devido às características específicas da valoração de sinais em 
VHDL, os Attributes que representam os pesos sinápticos foram duplicados, sendo que 
alguns foram utilizados nos Methods próprios para ajuste de seus valores, e outros 
utilizados para a disponibilização dos valores atualizados na interface de saída do 
dispositivo. A implementação do presente experimento eliminou tal duplicação, 
economizando ainda mais espaço na FPGA. 
A partir do desenvolvimento dos processos necessários à leitura e escrita dos 
padrões de treinamento, bem como da valoração inicial dos pesos sinápticos, o 
experimento pode ser executado. Neste contexto, a parametrização da RNA 
implementada para o presente experimento foi efetuada no arquivo description.xml, 
ajustando-se: 
 4 entradas, 6 bits cada. 
 5 neurônios na camada escondida, 8 bits cada. 
 3 neurônios na camada de saída, 8 bits cada. 
 120 padrões de treinamento, 6 bits para entrada e 8 bits para saídas. 
Os pesos das sinapses da RNA gerada, assim como os valores de entrada e 
saída da RNA, são declarados como valores inteiros. Assim, o processo de quantização 
de números reais para inteiros foi realizado antes do treinamento ser efetuado. A 
quantidade de bits utilizada na quantização segue a mesma especificação para a RNA 
XOR, estando ainda listados juntamente com a apresentação dos valores do arquivo 
description.xml.  


198 
 
 
Quanto ao código a ser gerado, a estrutura e a codificação da entidade que 
representa a RNA, FBE Network, e das entidades que representam os neurônios 
escondidos, FBE HiddenNeuron, e os neurônios de saída, FBE OutputNeuron, seguem 
as mesmas regras das estruturas geradas para o experimento com a função XOR. Não 
obstante, a quantidade de tais entidades é modificada, de acordo com a necessidade 
da IRIS DataSet. 
Por fim, pela utilização do compilador próprio, a geração do código VHDL foi 
concluída, e o experimento pode ser executado via simulador ModelSim da ferramenta 
Quartus II. 
5.8.2 Execução e Resultados do Experimento 
Assim como no experimento da RNA para a função XOR, a operacionalização 
do experimento utilizou um arquivo de testbench, em VHDL. Em tal arquivo, a entidade 
neuropon é instanciada por meio da declaração de um componente. Os valores da 
quantidade de épocas, taxa de aprendizagem e o total de entradas de treinamento são 
informados por meio da interface deste componente à entidade neuropon. 
Uma vez que, a partir deste experimento, o processo de valoração das entradas 
de treinamento é feito dentro do próprio componente neuropon, uma etapa anterior ao 
disparo da cadeia de notificações é efetuada. Tal processo de configuração é regido 
pela entrada in_cfgStart. Uma vez que tal sinal é ajustado (valor 1), os processos de 
leitura dos padrões de treinamento e o ajuste inicial dos pesos é efetuado. O circuito, 
então, é configurado para aguardar 2 ciclos de clock para então disparar o 
processamento da cadeia de notificações. O Código 31 apresenta o código VHDL que 
executa tais ajustes. 
Código 31 – Ajuste das configurações e do início da cadeia de notificações via  
arquivo de testbench em VHDL 
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
 
cfgStart <= '1'; 
 
wait for (clk_period * 2); 
 
cfgStart <= '0'; 
 
 
net_atNumEpochs <= std_logic_vector(to_signed(epochs,net_atTotalTI'length)); 
 
net_atTotalTI <= std_logic_vector(to_signed(xmlTI,net_atTotalTI'length)); 
 
net_atLR <= std_logic_vector(to_signed(xmlLR,net_atLR'length)); 
 
net_atNetStep1_1 <= '1'; 
 
 
set_net_atNumEpochs <= '1'; 
 
set_net_atTotalTI <= '1'; 
 
set_net_atLR <= '1'; 
 
set_net_atNetStep1_1 <= '1'; 
 
 
 
 
 
 
wait for (clk_period); 
 


199 
 
 
80 
81 
82 
83 
 
set_net_atNumEpochs <= '0'; 
 
set_net_atTotalTI <= '0'; 
 
set_net_atLR <= '0'; 
 
set_net_atNetStep1_1 <= '0'; 
Fonte: Autoria Própria 
Todos os sinais apresentados no Código 31 são mapeados no componente 
neuropon, correspondendo à interface de entrada do componente. Conforme a 
estrutura apresentada no Código 31, as tarefas de configuração efetuadas pelo arquivo 
de testbench são: 
 Das linhas 64 a 66 é disparado o processo de configuração do dispositivo, 
visando a valoração das entradas de treinamento.  
 Das linhas 68 a 71 os valores da quantidade de épocas de treinamento, total 
de entradas de treinamento, taxa de aprendizagem e o ajuste da flag que 
dispara o processamento da cadeia de notificações NeuroPON, 
respectivamente, são informadas.  
 Das linhas 73 a 76 são ajustadas as flags referentes à valoração dos sinais 
internos ao dispositivo, segundo as regras da LingPON-HD. Neste contexto, 
uma vez que tais flags são ajustadas para o valor ‘1’, os componentes 
Attributes conectados às referidas entradas são valorados pelos sinais de 
entrada informados, na próxima vez que o clock é ativado.  
 A linha 78 aguarda um ciclo de clock, que é o tempo necessário para que os 
componentes Attributes, definidos na entidade neuropon, atualizem seus 
estados de acordo com os valores apresentados via sinais de entrada (linhas 
68 a 71) 
 Por fim, da linha 78 à linha 81, a valoração dos componentes Attributes 
relacionados são ajustados para os valores anteriores (índice zero – ‘0’) aos 
necessários para configuração. 
Após a configuração, a entidade neuropon inicia o processamento da cadeia 
de notificações, efetuando o treinamento da RNA declarada. Tal processamento é 
executado até que a quantidade de épocas, informada na declaração via arquivo xml, 
for atingida. 
Em consequência à não utilização dos pesos sinápticos, das entradas e das 
saídas na interface do dispositivo, não foi necessária sua vinculação a componentes 
que representam Attributes em PON-HD. Tais valores, nesta nova proposta, estão 


200 
 
 
representados por sinais definidos na arquitetura do componente neuropon e possuem 
processos específicos de leitura e escrita, os quais são desvinculados dos Methods em 
PON-HD. Tal decisão de projeto diminuiu, proporcionalmente, o espaço utilizado no 
dispositivo FPGA, uma vez que os Attributes PON utilizam registradores e elementos 
lógicos específicos para o controle das entidades facto-execucionais. A Tabela 21 
apresenta os resultados deste experimento. 
Tabela 21 - Resultados dos experimentos de implementação de RNA MLP por meio do NeuroPON 
Parâmetro 
XOR 
IRIS 
Elementos Lógicos 
6149 
7323 
Funções combinacionais 
5733 
7130 
Registradores lógicos dedicados 
915 
1552 
Pinos 
257 
48 
Multiplicadores embarcados 
44 
42 
Frequência máxima de clock 
10.61 MHz 
65.48 MHz (read t.i.) 
10.49 MHz (clock) 
Dispositivo FPGA 
Cyclone IV E – EP4CE115F29C7 
Ciclos de clock necessários para execução 
de um padrão de treinamento. 
39 
24 
Fonte: Autoria Própria 
Como esperado, a quantidade de elementos lógicos, funções combinacionais 
e registradores dedicados, aumentou no presente experimento, visto que a quantidades 
de entradas, neurônios e pesos sinápticos é necessariamente maior para a IRIS 
DataSet em relação à função XOR. Outrossim, a quantidade de pinos necessários é 
menor, devido ao processo interno de leitura dos dados. Por fim, não houve uma 
mudança significativa na quantidade de multiplicadores embarcados, fato determinado 
pelo próprio compilador do Quartus II no momento da síntese. 
Quanto à escalabilidade do circuito, destaca-se que, mesmo frente a um 
aumento na quantidade de dados, a frequência de clock principal teve uma alteração 
mínima. Tal característica aponta que a escalabilidade do modelo computacional 
NeuroPON é eficaz, uma vez que houve o treinamento de uma quantidade maior de 
neurônios, tanto escondidos quanto de saída, de forma paralela, sem diminuir a 
frequência de processamento.  
Uma das principais mudanças positivas no resultado do experimento foi que a 
quantidade de ciclos de clock necessários para execução de um padrão de treinamento 


201 
 
 
diminuiu de 39 para 24, fazendo com que o processamento neuronal de cada entrada 
de treinamento seja mais veloz e, proporcionalmente à quantidade de dados, uma 
época de treinamento seja executada de forma mais rápida. Tal diminuição de ciclos se 
deve ao fato de que a leitura dos padrões de treinamento não serem mais 
implementadas na cadeia de notificações, mas sim em processos separados e 
dedicados a esta função. Neste contexto, este processo de leitura das entradas de 
treinamento obteve uma avaliação temporal separada do clock principal, conforme 
demonstrado na Tabela 21. 
Uma vez que a frequência de clock do circuito não teve mudanças 
significativas, é necessário efetuar, apenas, uma regra de três simples, a fim de obter-
se a proporção entre os experimentos. 
0012<_0120%5E
0012<_0120%F35
= 24
39 = 0,62 ∴38% 
(12) 
 
Isto posto, a equação (12) apresenta que o experimento da RNA com IRIS 
DataSet é 38% mais veloz frente ao experimento da RNA com a função XOR. Tal taxa 
é, naturalmente, proporcional ao tamanho da RNA, pois a IRIS DataSet possui 150 
padrões de treinamento com quatro entradas e três saídas, frente à quatro padrões com 
duas entradas e uma saída da função XOR. Neste contexto, o treinamento de uma 
época é diretamente proporcional à quantidade de entradas de treinamento. Não 
obstante, o uso de processos específicos para a leitura de padrões de treinamento, 
retirando este processo da cadeia de notificações do NeuroPON, otimizou na 
implementação do modelo computacional NeuroPON Prototipal. 
Por fim, a sintetização do circuito NeuroPON HD para VHDL, via ferramenta 
Quartus II, detectou um sinal de sincronização (clock) relacionado à leitura das entradas 
de treinamento, no valor de 65.48 MHz. A detecção deste sinal era esperada, visto que, 
conforme apontado, o processo de leitura dos valores é efetuado por um processo 
próprio, e não por um Method PON. 
5.8.3 Considerações 
O experimento da implementação IRIS DataSet, via NeuroPON HD, objetivou 
a validação da escalabilidade do modelo. Neste contexto, houve a geração de uma 
RNA com uma quantidade maior de entradas e entidades neuronais de forma 
transparente ao usuário, bastando apenas a mudança do arquivo de descrição da RNA. 


202 
 
 
Ademais, a execução destas entidades neuronais é feita de forma totalmente paralela 
no dispositivo FPGA, executando à uma frequência de clock muito próxima ao 
treinamento da RNA na função XOR. 
Outrossim, a quantidade de ciclos de clock necessários para a execução do 
treinamento de uma entrada de treinamento é menor no experimento IRIS DataSet, 
frente ao experimento com a função XOR. Conforme apontado, a execução do 
treinamento é 38% mais veloz. Em uma RNA com poucas entidades neuronais e 
padrões de treinamento, tal mudança torna-se praticamente imperceptível, visto que, a 
uma frequência de 10,5 MHz, cada etapa leva 22800 ms a menos para ser executada. 
Porém, em RNA maiores (e. g. com uma quantidade maior de entidades neuronais e 
padrões de treinamento), este valor torna-se relevante na execução do treinamento via 
hardware reprogramável. 
A partir de tais resultados, torna-se ainda mais claro que modificações na 
estrutura da Tecnologia LingPON-HD precisam ser efetuadas, visando a melhoria no 
NeuroPON-HD. A necessidade da implementação de Methods específicos para a 
execução de alguns processos referentes à execução de uma RNA, evitando assim a 
necessidade de seguir, em alguns casos, a cadeia de notificações PON. Ademais, a 
utilização de sinais internos ao invés de Attributes para entidades não notificantes 
apresenta-se como outra hipótese válida ao modelo NeuroPON.  
Por fim, uma das considerações apontadas no experimento da RNA com a 
função XOR podem ser apontadas sobre o experimento IRIS DataSet. A transparência 
ao usuário, na criação de uma RNA totalmente paralela, gerada a partir de linguagem 
descritiva/declarativa, é uma vantagem pertinente ao modelo. 
5.9 Reflexões sobre os experimentos 
O conjunto de esforços realizados para a criação do modelo computacional  
NeuroPON, bem como experimentos daí decorrentes, levam a um conjunto de 
reflexões. 
Primeiramente, em termos de tempo de execução, o desempenho dos 
experimentos NeuroPON (no tocante a treinamento) frente a experimentos baseados 
em PI é, ainda, um tanto mais lento em NeuroPON via Framework PON C++ 2.0 e 
ligeiramente mais lento que NeuroPON via LingPON StaticCPP. Entretanto, as 
tecnologias PON para desenvolvimento de software, tem sido alvo de constantes 
melhorias.  


203 
 
 
A título de exemplo de melhorias nas materializações do PON, os trabalhos de 
Martini (2018), Mendes; Ferreira (2019), Negrini et al., (2019) apontam melhorias na 
computação de entidades PON de forma concorrente, tanto para a tecnologia LingPON 
quanto para o Framework PON (como Framework PON C++ 3.0 e o novo Framework 
PON Elixir Erlang). Ademais, o trabalho de Ronszcka (2018) apresenta a Tecnologia 
LingPON 2.0, que tem por objetivo contemplar todas as propriedades elementares do 
PON em plataformas distintas (RONSZCKA, 2018). Enfim, tais evoluções, que 
apresentam algum melhoramento nas materializações do PON, podem ser utilizadas 
para avançar também o NeuroPON no tocante às suas implementações prototipais 
correntes. 
Outrossim, o NeuroPON promove uma melhor organização da solução do que 
RNA em PI, devido ao seu nível de abstração com entidades explícitas. Diferentemente 
de implementação de RNA em PI, o NeuroPON explicita o conhecimento de cada parte 
da RNA, o que melhora a manutenibilidade, incluindo eventuais ajustes no  código 
decorrente. Com uma visão clara de cada elemento da RNA, com um nível apropriado 
de coesão e desacoplamento aproveitado da orientação a notificações, o 
desenvolvedor poderia melhor ajustar os componentes de acordo com a sua 
necessidade. 
Ainda, tais componentes, como entidades Neurons, possuem controle de 
execução independente, pois o escalonamento de tais neuro-entidades é controlado 
pelo mecanismo de inferência que se dá pela cadeia de notificações. Neste contexto, 
todas as neuro-entidades neste processo sináptico notificante podem, portanto, ser 
executados concorrentemente e, se a plataforma computacional permitir, mesmo 
paralelamente. Neste contexto, de execução concorrente, os experimentos com 
Framework PON C++ 3.0, Framework PON Elixir/Erlang, bem como com Tecnologia 
LingPON-HD, apresentaram resultados de processamento realmente paralelo, mesmo 
que com desempenho mais baixo, em termos de tempo de processamento, frente às 
implementações ditas tradicionais, tanto em software quanto em hardware.  
No segundo experimento via tecnologia PON-HD, que é a implementação de 
uma RNA MLP para IRIS DataSet, observou-se que o uso de processos e sinais VHDL, 
ao invés de Methods e Attributes PON, para a implementação de algumas ações 
específicas, fez com que o treinamento utiliza-se uma quantidade menor de ciclos de 
clock. Tais ações demandam procedimentos repetitivos, e não têm a necessidade do 
uso do paralelismo, tampouco o uso de entidades notificantes, a exemplo da leitura dos 
padrões de entrada de treinamento. Nestes casos, os processos poderiam ser 


204 
 
 
executados sem respeitar a cadeia de notificações. Isto posto, observa-se que 
modificações no compilador, visando a criação de processos e sinais específicos para 
a execução de tais ações, são necessários para a evolução do NeuroPON, 
nomeadamente na criação de códigos para hardware reconfigurável. 
Por fim, a possibilidade de se utilizar uma linguagem declarativa descritiva, 
baseada em XML, para a parametrização da RNA a ser implementada, facilita a 
implementação de uma RNA. Ainda, o uso da tecnologia LingPON permite a geração 
de código não redundante (portanto eficiente), desacoplado (portanto passível de 
concorrência ou paralelismo em plataformas pertinentes) e visando as plataformas 
aptas a executarem código PON. Ademais, o usuário não precisa ter conhecimento 
técnico apurado quanto a projeto e desenvolvimento de RNA, tanto em software para 
execução monocore e multicore, quanto em hardware reconfigurável, uma vez que o 
NeuroPON Prototipal cria tais estruturas de execução, de forma transparente ao 
usuário. 
 
 


205 
 
 
6 Conclusões e Trabalhos Futuros 
O presente capítulo apresenta as conclusões acerca deste trabalho, sobretudo 
frente às motivações e aos objetivos apresentados no Capítulo 1, os quais estão 
disponíveis na seção 1.4 (página 32). Outrossim, as principais contribuições desta tese 
são listadas, a fim de pontuar as etapas desenvolvidas à conclusão do modelo 
computacional NeuroPON Teórico e Prototipal. Ainda, visando um constante 
aprimoramento no desenvolvimento do NeuroPON, considerações sobre as atividades 
subsequentes à própria tese são apresentadas. 
6.1 Conclusões 
Este trabalho objetivou o desenvolvimento do modelo computacional 
NeuroPON, tido como uma nova abordagem para o desenvolvimento de RNA utilizando 
o PON. Neste âmbito, uma revisão de literatura sobre os temas pertinentes foi efetuada, 
sendo aqui apresentada nos Capítulos 2 e 3. Tal atividade cobriu os dois primeiros 
objetivos específicos, descritos no Capítulo 1, sendo que o fundamental era localizar 
lacuna existente. 
Algumas pesquisas, já apresentadas nas Subseções 2.4.5 e 2.4.7, apontam 
que as RNA vêm sendo aplicadas na academia e na indústria, em processos como 
reconhecimento de padrões, classificação, previsão de séries temporais, entre outros. 
Neste contexto, tais pesquisas consideram que a eficiência de uma RNA se dá por 
implementações que consigam, de certa forma, efetuar um processamento paralelo de 
seus neurônios.  
Neste 
sentido, 
unidades 
de 
processamento 
singulares 
(i.e., 
monoprocessadores) para a execução de RNA, não executam tais estruturas de forma 
condizente à sua teoria de origem, mimetizante das RNN, devido a limitações de 
paralelismo, por exemplo. Assim, ao bem da verdade, faz-se necessário mudar o modo 
de construção da RNA, passando de unidades de processamento únicas para 
computação que possa ser desacoplada, e assim, paralelizáveis (GUO et al., 2012). 
Após análise de trabalhos que implementaram RNA e seus componentes, ficou 
explícito que neurônios implementados em FPGA possuem alta performance de 
execução, não só por serem implementados diretamente em circuitos, mas também por 
permitirem paralelismo efetivo, granular e escalável (GUO et al., 2012; OMONDI et al., 
2006). Neste sentido, abordagens de implementação apropriadas de RNA em 


206 
 
 
dispositivos FPGA têm maior potencial para efetuar um real processamento paralelo 
que aquelas usuais abordagens procedimentais, usadas em implementações 
imperativas, executadas em plataformas sequenciais baseadas na arquitetura de von 
Neumann (MISRA; SAHA, 2010; OMONDI et al., 2006). 
Não obstante ao potencial das FPGA, para realizar a programação de tais 
dispositivos, os usuários devem conhecer técnicas de desenvolvimento de hardware 
digital (em baixíssimo nível) ou ainda conhecer técnicas para descrição de hardware, 
via linguagens específicas e veementemente técnicas (BAPTISTA; MORGADO-DIAS, 
2017; KERSCHBAUMER, 2018; TISAN; CHIN, 2015). Em tempo, até se pode 
programar FPGA via ferramentas de High-Level Synthesis (HLS), porém tais 
ferramentas seguem características de linguagens usuais de programação para 
arquiteturas baseadas no modelo de von Neumann e, portanto, de seus paradigmas 
sequenciais e acoplantes, dificultando assim exploração efetiva e apropriada do 
paralelismo disponível em dispositivos FPGA. De fato, os códigos gerados por meio 
das premissas do PI são, geralmente, acoplados e de difícil distribuição 
(KERSCHBAUMER, 2018; MEEUS et al., 2012; WINDH et al., 2015).  
Assim, além da geração de código de RNA a ser executado em dispositivos 
FPGA, deveria haver um modelo que permitisse desenvolvimento em alto nível e de 
fácil composição, mas aproveitando o paralelismo inerente de FPGA. Mais do que isso, 
deveria haver um modelo que permitisse a geração de código, tanto para treinamento 
quanto para operação de RNA, com elementos desacoplados, concorrentes (portanto 
paralelizáveis) e não redundantes, podendo ser executado em diferentes plataformas. 
Neste âmbito, caso o usuário disponha de plataforma que não possibilite paralelismo 
de execução (e.g. computadores sequenciais monoprocessados) ou que permitam 
apenas paralelismo parcial (e.g. processadores multicore) ou ainda que permita 
paralelismo mais efetivo (e.g. dispositivos FPGA), as RNA geradas poderiam ser 
executadas de forma eficiente e desacoplada, visando aproveitar o potencial de 
execução possível na plataforma visada. 
Nesse âmbito, durante o processo investigativo realizado nesta tese, 
identificou-se que há uma lacuna apresentada na Tabela 4 (página 89) na qual o modelo 
NeuroPON procura criar meios e caminhos para suprir. Em tempo, propôs-se o modelo 
computacional NeuroPON, a partir do dueto sinapses de RNA & notificações do PON, 
além das características do PON como um todo. Assim, o modelo computacional 
NeuroPON consiste em uma solução que permite desenvolvimento de alto nível, de 
forma descritiva declarativa, gerando código para plataformas distintas. A conclusão do 


207 
 
 
desenvolvimento do NeuroPON cobriu o terceiro objetivo, bem como cumpriu os 
elementos apontados no objetivo geral desta tese. 
No tocante a cumprimento do terceiro objetivo, entretanto, considera-se o 
NeuroPON aqui em dois vieses: um teórico e o outro prototipal. Neste âmbito, o modelo 
computacional NeuroPON é considerado sob duas diferentes visões, nomeadamente 
NeuroPON Teórico e NeuroPON Prototipal, os quais retratam respectivamente o 
modelo teórico proposto e o conjunto ferramental e experimental realizado. Neste 
sentido, a Tabela 22 salienta a solução NeuroPON proposta de forma tal a mostrar 
como o NeuroPON Teórico e o NeuroPON Prototipal existente até então suprem as 
características vislumbradas. 
Tabela 22 - Modelo computacional NeuroPON: características de implementação de RNA 
Trabalho/proposta 
Programação 
em Alto Nível 
Treinamento 
no hardware 
Customizável 
Geração de 
Código 
Código Não-
Redundante 
Código 
Desacoplado 
Código para 
Plataformas 
Distintas 
NeuroPON Teórico 
S 
S 
S 
S 
S 
S 
S 
NeuroPON Prototipal 
S 
S 
P 
S 
S 
S 
P 
Legenda: S: sim  P: parcialmente 
Fonte: Autoria Própria 
 Como trata a Tabela 22, o NeuroPON Teórico permite em tese alcançar todas 
as 
características, 
enquanto 
que 
o 
NeuroPON 
Prototipal 
permite 
indicar 
experimentalmente as factibilidades de se ter as características postas, ainda que com 
alguma imperfeição natural a protótipos que servem para demonstração experimental 
de conceitos. Em termos de NeuroPON Prototipal, uma característica apontada como 
Parcial é a de gerar código para plataformas distintas. Tal consideração foi apontada 
pois o processo não é automático, a partir da descrição em XML, para todas as 
plataformas visadas, sendo funcional apenas para a geração de LingPON-HD. Não 
obstante, a partir de código NeuroLingPON é possível compilar, de forma individual e 
semiautomática, gerando código para Framework PON C++ 2.0 e 3.0, StaticCPP e 
VHDL. Ainda, a característica de customização é tida como parcial no NeuroPON 
Prototipal pois ainda não é possível parametrizar a função de transferência por meio da 
descrição em ViNNSL, mesmo que viável via LingPON e afins.  
Outrossim, a construção do NeuroPON Teórico e, particularmente, do 
NeuroPON Prototipal, dependeu de um conjunto de trabalhos desenvolvidos sendo 
alguns deles no âmbito estrito e oriundos dos esforços de pesquisa desta presente tese. 
Estes últimos são considerados como contribuições deste trabalho, havendo 
contribuições tanto para a área de RNA em si quanto para a evolução do próprio PON 


208 
 
 
e suas materializações com contribuições naturais ao grupo de pesquisa pertinente. 
Isto posto, a Seção 6.1.1 aborda tais contribuições e a Seção 6.1.2 faz reflexões sobre 
o que foi alcançado com elas. 
6.1.1 Contribuições 
Durante o período de doutoramento, no âmbito desta tese, algumas atividades 
de ordem inventivo-propositivas e de desenvolvimento foram elaboradas, visando a 
criação do modelo computacional NeuroPON Teórico e Prototipal, bem como o 
correlato aprimoramento de algumas materializações do PON para tal.  
 Desenvolvimento 
do 
modelo 
computacional 
NeuroPON 
Teórico: 
Primeiramente houve a questão inventiva de elaborar um novo modelo 
estrutural e com dinâmica de notificações para RNA, buscando relacionar 
componentes de uma RNA com seus correspondentes em PON. 
Posteriormente a esta atividades inventivas, houve a utilização de um 
Diagrama de Instâncias do PON visando a conformação do modelo com o 
próprio PON, que permitiu a definição efetiva de novas neuro-entidades 
orientadas a notificação (e.g. NeuroRules). Subsequentemente, também 
houve a construção de diagramas em UML para descrever os elementos 
estruturais do NeuroPON por meio de diagramas de classe, bem como o seu 
funcionamento dinâmico, por meio de diagramas de atividades. Neste 
contexto, as neuro-entidades sináptico-notificantes do NeuroPON proposto 
mostraram-se desacopladas e notificantes, permitindo assim, em termos de 
modelo, vislumbrar a execução concorrente e paralelizável. Por fim, a 
evolução da modelagem permitiu a definição das características desejáveis 
do modelo NeuroPON, apontadas na Tabela 22. 
 Implementação da estrutura de operação e treinamento de RNA MLP, por 
meio do método BP, nas seguintes materializações do PON permitindo a 
proposição e validações do NeuroPON Prototipal naturalmente à luz do 
NeuroPON Teórico: 
o Framework PON C++ 2.0: como um primeiro experimento, demonstra-
se experimentalmente a factibilidade do NeuroPON, utilizando a 
generalização da função XOR. Tal experimento e seus resultados foram 
publicados em Schütz et al. (2015) . 


209 
 
 
o Framework PON C++ 3.0: a partir de tal experimento, com a base de 
dados da flor de Iris, demonstra-se experimentalmente a transparência 
de execução de forma concorrente do NeuroPON. Este experimento e 
seus resultados foram publicados em Schütz et al. (2018). 
o Framework Elixir/Erlang: por meio do ajuste do código NeuroLingPON, 
da versão 1.0 para a versão 2.0, o experimento da RNA para a função 
XOR foi executado em quatro máquinas, com diferentes quantidades de 
cores, por meio do Framework Elixir/Erlang. Os resultados obtidos 
demonstraram a factibilidade da execução do NeuroPON em multicore, 
de uma maneira mais refinada e efetiva, uma vez que a velocidade de 
processamento aumenta proporcionalmente à quantidade de cores. 
o LingPON com compilador para StaticCPP: neste experimento, com a 
base de dados da flor de Iris, demonstra-se experimentalmente que é 
possível acelerar o processo de treinamento da RNA em NeuroPON, 
pois os resultados obtidos pelos frameworks PON, em termos de tempo 
de processamento, estavam muito aquém do esperado. Ainda, tal 
experimento mostrou a implementação do modelo NeuroPON Teórico 
por meio de tecnologia LingPON em software. 
o LingPON-HD: no experimento, com a função XOR, demonstra-se 
experimentalmente que há de fato execução paralela das neuro-
entidades do modelo computacional NeuroPON em dispositivo FPGA, 
chamado de NeuroPON-HD. Posteriormente, no experimento com IRIS 
DataSet, com novos processos para leitura dos dados de treinamento e 
pesos sinápticos iniciais, bem como para disponibilização dos pesos 
sinápticos treinados, o processo de treinamento da RNA tornou-se mais 
veloz, diminuindo a quantidade de ciclos de execução em hardware. 
Ademais, como uma quantidade maior de entidades neuronais foi 
automaticamente criada, frente à necessidade da IRIS DataSet, a 
escalabilidade do NeuroPON Prototipal pode ser experimentalmente 
demonstrada. Por fim, tais experimentos mostraram a construção de 
código NeuroPON a partir da definição de RNA em ViNNSL, gerando 
RNA em NeuroPON-HD (hardware) via tecnologia LingPON. 
 Construção de um gerador de código a partir da linguagem LingPON, 
gerando código StaticCPP: este trabalho foi realizado visando acelerar a 


210 
 
 
execução de aplicativos PON em uma linguagem baseada no POO. Os 
resultados foram expressivos, na questão de diminuição de tempo de 
execução frente a todas as materializações do PON em software 
implementadas até então. Primeiramente houve experimentos puramente 
em PON21. Subsequentemente, esta nova materialização PON foi usada 
para implementar NeuroPON em software.  
 Adequação do Framework PON C++ 3.0: foi efetuada uma correção desta 
materialização pois experimentos iniciais apresentaram problemas na 
execução de entidades do modelo NeuroPON. Neste contexto, parte da 
implementação desta versão do Framework PON C++ precisou ser refeita. 
Ademais, houve a subsequente adequação para a execução das neuro-
entidades, do modelo computacional NeuroPON, de forma concorrente em 
diversos núcleos de processamento.  
 Adequação da Tecnologia LingPON-HD: o compilador desenvolvido por 
Kerschbaumer (2018), principalmente na descrição de Methods, não 
englobava a execução de funções de Tangente Hiperbólica e Quantização. 
Neste contexto, foram adicionados novos tokens à LingPON em questão e, 
consequentemente, 
implementou-se 
no 
compilador 
pertinente 
funcionalidades para suas identificações, bem como todos os ajustes para a 
subsequente geração de código em VHDL. Ainda, neste âmbito também 
houve toda uma preocupação de tratar números reais por representações 
inteiras. Tal adequação permitiu enfim a geração de código VHDL apropriado 
ao modelo computacional NeuroPON para síntese em dispositivos FPGA. 
 Construção de um interpretador XML e compilador para gerar código em 
LingPON: o interpretador efetua a leitura da parametrização da RNA, a partir 
de um arquivo de descrição escrito em XML. Tal XML segue o padrão da 
linguagem ViNNSL, especialmente criada para a descrição de RNA (BERAN 
et al., 2008). A partir dos dados lidos, o compilador desenvolvido constrói a 
estrutura de código em LingPON necessária para a operação e treinamento 
da RNA, na plataforma especificada, e seguindo os conceitos do modelo 
computacional NeuroPON.  
 
21 Tais experimentos e seus resultados, são parte de artigo enviado à revista IEEE América 
Latina em agosto de 2018. 


211 
 
 
 Avaliação das diversas implementações do NeuroPON, as quais constituem 
o aqui chamado NeuroPON Prototipal. Neste contexto, implementações de 
RNA em PI foram desenvolvidas, sendo registrados e analisados os 
resultados inclusive à luz de literatura pertinente. Subsequentemente, os 
mesmos experimentos foram refeitos com NeuroPON confirmando que os 
algoritmos 
implementados 
funcionam 
(realizando 
os 
treinamentos/produções) vis-à-vis à obtenção de resultados similares as 
soluções tradicionais implementadas em PI.  
Além dos artefatos de software e hardware, bem como da modelagem Teórica 
do NeuroPON aqui descritas, uma faceta peculiar do PON pode ser observada ao final 
da construção de tal modelo. Neste contexto, a utilização dos conceitos teóricos do 
PON na implementação de RNA se deu muito mais pelo seu viés de desacoplamento 
do que pelo seu viés de não redundância. Tal contribuição, portanto, mostra 
efetivamente que o PON torna-se útil não somente para a solução de problemas que 
possuem um alto índice de redundância, mas também em sistemas nos quais a 
necessidade da criação de entidades desacopladas, reativas e funcionais é vantajoso. 
6.1.2 Discussão sobre as contribuições 
Visando validar as implementações dos códigos para operação e treinamento 
de RNA MLP pelo método BP em NeuroPON Prototipal alguns experimentos foram 
efetuados e relatados neste trabalho. Ainda, tais experimentos visaram a própria 
confirmação do NeuroPON Prototipal, criado à luz do NeuroPON Teórico, como um 
novo modelo computacional para o desenvolvimento de RNA.  
Tais experimentos cobrem o quarto objetivo específico, apresentado no 
Capítulo 1. Por meio de tais experimentos concluiu-se que o treinamento de RNA 
utilizando PON no arranjo proposto no seio da NeuroPON é de todo factível. No caso 
da NeuroPON SW (em software), particularmente no caso do experimento com IRIS 
DataSet gerando código escrito na Tecnologia LingPON SW com StaticCPP, houve um 
desempenho, tanto em acurácia de classificação quanto em tempo de execução muito 
próximos aos de uma RNA implementada em linguagem C procedimental (Tabela 14). 
Além dos experimentos em materializações ditas “monocore”, experimentos 
foram conduzidos por meio de materializações que permitem a execução de código 
concorrente e paralelo de forma efetiva a partir do NeuroPON. Neste âmbito, o 
experimento com o NeuroPON implementado via o (corrigido) Framework PON C++ 


212 
 
 
3.0, distribuiu as neuro-entidades nos múltiplos núcleos de um processador. Entretanto, 
os resultados em relação ao desempenho deste experimento ficaram aquém do 
desejado vis-à-vis aos resultados com a Tecnologia LingPON SW em StaticCPP. Neste 
contexto, tal resultado é, em parte, um reflexo do uso de estruturas computacionais 
caras na implementação do Framework. Ainda, o gerenciamento de memória 
compartilhada é ainda um ponto negativo na execução do experimento pois, como o 
algoritmo BP necessita de muito acesso a áreas compartilhadas, a exclusão mútua é 
amplamente utilizada gastando assim tempo de processamento. 
Outro experimento dito “multicore”, envolveu o Framework Elixir/Erlang. Tal 
experimento, mesmo que executado com uma tradução entre a LingPON 1.0 e a 
LingPON 2.0 feita por meio de ajustes, comprovou a plausibilidade da execução do 
NeuroPON em tal plataforma. Ademais, os resultados da execução da RNA MLP para 
a função XOR foram muito superiores aos dados resultantes do experimento com 
Framework PON C++ 3.0, indicando experimentalmente que a velocidade do 
treinamento é diretamente proporcional à quantidade de núcleos de execução (cores).  
Outrossim, também houve a materialização do NeuroPON em Hardware Digital 
(HD) via Tecnologia LingPON-HD. Neste âmbito, a partir dos experimentos, decorrentes 
com código VHDL gerado por meio da aplicação da tecnologia NeuroPON-HD para a 
implementação da RNA, houve execução de forma paralela das neuro-entidades 
alocadas em um dispositivo FPGA tanto quanto previsto no NeuroPON Teórico, i.e. 
tanto quanto modelado em Diagramas de Instâncias do PON e em UML por diagramas 
de atividades. Em suma, o paralelismo foi alcançado graças ao desacoplamento entre 
as entidades, denotado pelo NeuroPON nas chamadas neuro-entidades do modelo 
dado. 
Ainda, os resultados dos experimentos XOR e IRIS com a Tecnologia PON-HD, 
quanto à quantidade de ciclos de clock necessários para uma época de treinamento 
serem bons, mas não extraordinários, recai no fato da tecnologia LingPON-HD ser uma 
solução genérica na criação de circuitos digitais. Como há a necessidade de uma alta 
quantidade de cálculo pelo treinamento BP em RNA MLP, muitos Methods 
sequencializados precisam ser instigados e, consequentemente, toda a cadeia de 
notificações precisa também ser executada. Neste sentido, a quantidade de ciclos de 
clock foi menor no experimento com IRIS DataSet frente ao experimento XOR, devido 
ao uso de processos específicos para a implementação de atividades que demandem 
um processamento repetitivo e que não envolvam entidades notificantes (e. g. leitura 
de dados de treinamento). Neste caso, ao utilizar-se Methods PON para a leitura de 


213 
 
 
padrões de treinamento, toda a cadeia de notificações precisaria ser ativada na leitura 
de cada padrão, sendo que nesta nova proposta a alimentação dos padrões de entrada 
e dos pesos iniciais é feita por meio de memória RAM, utilizando sinais internos ao 
circuito. Deste modo, o uso de técnicas como Attributes impertinentes (definidos na 
Seção 3.2) poderia ser uma solução, visando o aprimoramento do NeuroPON. 
Outra reflexão pertinente em relação aos experimentos, foi quanto à forma de 
desenvolvimento. O NeuroPON permite, por meio da integração de linguagem de alto 
nível e descritiva que gera declarativa, a criação implícita de entidades não redundantes 
e desacopladas à luz do PON. Assim, tal nível de desacoplamento implícito permite 
paralelismo de granularidade fina em ambiente apropriado, nomeadamente em 
dispositivos FPGA, sem ônus ao usuário da solução proposta, ou seja, sem as 
dificuldades existentes em programação utilizando RNA via PI para se definir estruturas 
desacopladas, visando concorrência ou paralelismo. Neste contexto, tais dificuldades 
são suprimidas pela utilização do NeuroPON, via sua linguagem descritiva para 
definição de RNA. 
Ademais, a geração de código desacoplado em NeuroPON permitiu uma 
melhor visualização da estrutura da RNA e seus componentes. Diferentemente de 
implementações matriciais de neurônios, que utilizam laços de repetição para um 
acesso generalizado a tais entidades, o modelo computacional NeuroPON facilita um 
tratamento único a cada elemento. Tal processo abre novas possibilidades para 
experimentos, como a aplicação de diferentes funções de ativação por neurônio, a 
criação de camadas especializadas e mesmo podas sinápticas, os quais são temas 
discutidos nos trabalhos futuros. 
Por fim, buscando cobrir o quinto objetivo específico, os experimentos 
efetuados confirmaram as características almejadas pelo modelo computacional 
NeuroPON. Tais características, bem como os trabalhos relacionados para 
comparação, estão listados na Tabela 4 (página 89), sendo aqui elencados para 
validação vis-à-vis aos resultados alcançados: 
 Programação em Alto Nível: a programação por meio de regras permitida 
pela Tecnologia LingPON é caracterizada como uma programação em alto 
nível sendo que o arranjo que permite o NeuroPON foi expresso inclusive 
por esse meio. Ademais, a utilização de linguagem declarativa descritiva na 
parametrização da RNA, tende a elevar ainda mais o nível de programação 
quando permite gerar automaticamente o arranjo em LingPON que expressa 
o NeuroPON. 


214 
 
 
 Treinamento no Hardware: o código gerado em VHDL, por meio da 
tecnologia LingPON-HD, foi executado em simulador homologado pela 
fabricante altera. Os valores resultantes de tal treinamento coincidiram com 
os treinamentos efetuados em software (Tecnologia LingPON e Frameworks 
PON). 
Ainda 
houve 
também 
confrontação 
com 
implementações 
funcionalmente equivalentes em PI sendo que os resultados são muito 
similares. Assim, confirma-se o sucesso no processo de aprendizado. 
 Customização: tal característica foi coberta na sua totalidade em NeuroPON 
Teórico e parcialmente no NeuroPON Prototipal. Neste âmbito, é possível 
informar a quantidade de entradas e camadas, bem como a quantidade de 
entidades neuronais em cada camada. Porém, a função de transferência 
(ainda) não é parametrizada via linguagem ViNNSL, mas já o sendo nas 
demais etapas do processo de geração de RNA pela abordagem NeuroPON. 
 Geração de Código: os experimentos demonstraram que, a partir da 
especificação em NeuroLingPON, compiladores específicos geram códigos 
para operacionalização e treinamento de RNA tanto em software quanto 
hardware. Tais experimentos, portanto, concluíram os testes nas linguagens 
StaticCPP, Framework PON C++ 2.0 e 3.0, bem como em VHDL.  
 Código Desacoplado e não-redundante:  frente aos resultados obtidos nos 
experimentos, o NeuroPON se mostrou plausível na geração de código não-
redundante (i.e. eficiente à luz do PON) e desacoplado, portanto, 
concorrente, de forma transparente ao desenvolvedor, a partir da 
parametrização da RNA por meio de linguagem declarativa descritiva 
baseada em XML, e posterior geração de código NeuroLingPON. 
 Código adequado a execução em plataformas distintas: tal característica foi 
coberta na sua totalidade, pelo NeuroPON Teórico, e parcialmente pelo 
NeuroPON Prototipal. Neste contexto, o código gerado no processo de 
compilação a partir da linguagem ViNNSL para LingPON é adequado à 
Tecnologia LingPON-HD. Não obstante, códigos escritos em NeuroLingPON 
podem ser compilados para StaticCPP e para as versões do Framework, 
porém de forma semiautomática.  
Enfim, além da confirmação das características almejadas pelo modelo 
computacional NeuroPON, observa-se que novas possibilidades de pesquisa, na área 
de RNA a partir desse modelo. 


215 
 
 
6.1.3 Reflexões finais da tese 
Mesmo que tido como um modelo embrionário quanto à aplicação de RNA em 
PON, a construção do modelo computacional NeuroPON permitiu expandir um tanto a 
fronteira do conhecimento, a partir de percepções iniciais sobre um possível dueto entre 
sinapses neurais e notificações PON. Ademais, os resultados são interessantes do 
ponto de vista do estado da arte e mesmo tido com apropriados para uma tecnologia 
prototipal do ponto de vista do estado da técnica. 
Neste contexto, o modelo computacional NeuroPON inovou na questão de criar 
entidades neuronais (neuro-entidades) independentes e notificantes, que mimetizam 
sinapses artificiais. Por meio da criação de tais neuro-entidades, uma gama de novas 
possibilidades de aplicação e pesquisas foi aberta: 
 Podas sinápticas: no NeuroPON, uma entidade Neuron possui NeuroRules, 
cujas Conditions obrigatoriamente contém uma Premise para o controle de 
execução e sincronismo. Neste contexto, tal Premise pode facilmente ser 
utilizada para se efetuar uma Poda Darwiniana, na qual as ligações 
sinápticas mais fracas (i.e. com menor peso) sejam eliminadas. Segundo 
Frankle; Carbin (2018), a abordagem de poda (prunning) permite diminuir em 
até 90% a quantidade de neuro-entidades de uma RNA treinada, obtendo 
praticamente os mesmos resultados de precisão de treinamento. Ainda, em 
se tratando da implementação em hardware, esta abordagem poderia gerar 
menor gasto de energia, e ocupar menos espaço nos circuitos da FPGA. 
 Acesso singular a cada neuro-entidade: o NeuroPON trabalha com 
entidades autônomas, reativas e desacopladas. Assim, um experimento a 
ser testado é a utilização de uma função de ativação diferente por neurônio, 
não somente por camada. Segundo Heaton (2015), pesquisas recentes 
apontam que RNA devem utilizar funções como ReLU (Rectified Linear Unit) 
em camadas ocultas, e softmax ou funções lineares em camadas de saída. 
Neste contexto, a experimentação de diferentes funções por neurônio se 
mostra uma hipótese digna de avaliação.  


216 
 
 
6.2 Trabalhos futuros 
Visando explorar, ainda mais, a fronteira do conhecimento quanto ao 
desenvolvimento do modelo computacional NeuroPON, sugere-se atividades futuras 
que poderão ser desenvolvidas a partir deste trabalho. 
Conforme apresentado no Capítulo 3, as materializações do PON estão em 
constante evolução, buscando principalmente avanços quanto à execução concorrente 
dos elementos de sua cadeia de notificações. Neste sentido, uma relação simbiótica 
entre tais avanços e pesquisas/experimentos envolvendo o NeuroPON deve acontecer, 
salientando como exemplo o Framework Elixir/Erlang que se mostrou eficiente na 
execução multicore, ainda que tenha surgido como um experimento tardio no âmbito 
desta tese de doutorado. 
Sugere-se também uma evolução com relação ao próprio modelo 
computacional NeuroPON Prototipal quanto ao uso de novas arquiteturas, topologias e 
funções de treinamento de RNA, como em aprendizado profundo (deep learning) e, até 
mesmo, em RNA com camadas convolucionais.  
Neste contexto, experimentos com arquiteturas recorrentes e reticuladas, com 
treinamento não supervisionado, por exemplo, seriam de grande valia para sua 
evolução. Ainda, a implementação de neuro-entidades que computem camadas 
convolucionais, visando aprendizado profundo, aumentaria ainda mais a gama de 
aplicações das RNA geradas pelo NeuroPON. 
 
 


217 
 
 
 
Referências 
Este capítulo apresenta as referências bibliográficas utilizadas no presente 
documento de tese de doutorado. No tocante ao PON, os trabalhos estão listados e 
não raro disponibilizados em página própria do paradigma. Isso é particularmente 
pertinente para os Relatórios Técnicos do grupo de pesquisa do PON. Neste âmbito, 
as páginas pertinentes a esta consideração feita são as que seguem: 
 http://www.dainf.ct.utfpr.edu.br/~jeansimao/PON/PON.htm 
 http://www.dainf.ct.utfpr.edu.br/~jeansimao/PON/PON_RelatTecnicos.htm 
 
ABADI, M.; ANDERSEN, D. G. Learning to Protect Communications with Adversarial Neural 
Cryptography. , 2016. Disponível em: <http://arxiv.org/abs/1610.06918>. . 
ABDULKADER, A.; LAKSHMIRATAN, A.; ZHANG, J. Introducing DeepText: Facebook’s text 
understanding 
engine. 
Disponível 
em: 
<https://code.facebook.com/posts/181565595577955/introducing-deeptext-facebook-s-text-
understanding-engine/>. Acesso em: 7/6/2017. 
ABROL, S.; MAHAJAN, R. Artificial Neural Network Implementation on FPGA Chip. 
International Journal of Computer Science and Information Technology Research, v. 3, n. 
1, p. 11–18, 2015. 
AISA, B.; MINGUS, B.; O’REILLY, R. The Emergent neural modeling system. Neural Networks, 
v. 
21, 
n. 
8, 
p. 
1146–1152, 
2008. 
Disponível 
em: 
<http://linkinghub.elsevier.com/retrieve/pii/S0893608008001287>. . 
AKHTER, S.; ROBERTS, J. Multi-core programming: Increasing Performance through 
Software Multi-threading. USA: Intel press, 2006. 
ALI, H. K.; MOHAMMED, E. Z. Design Artificial Neural Network Using FPGA. IJCSNS 
International Journal of Computer Science and Network Security, v. 10, n. 8, p. 88–92, 
2010. 
ANTIQUEIRA, P. A. Implementação de Modelos de Redes de Petri em Hardware de Lógica 
Reconfigurável, 2011. UTFPR. 
ARDUINOAG. Getting Started with Arduino and Genuino products. Disponível em: 
<https://www.arduino.cc/en/Guide/HomePage>. Acesso em: 11/4/2017. 
ASANOVIC, K.; BODIK, R.; CATANZARO, B. C.; et al. The Landscape of Parallel Computing 
Research: A View from Berkeley. Berkeley, 2006. 
ATABAY, 
D. 
Python 
For 
Artificial 
Intelligence. 
Disponível 
em: 
<https://wiki.python.org/moin/PythonForArtificialIntelligence>. Acesso em: 2/4/2017. 
ATHAYDE, E. B. DE; NEGRINI, F. Implementação de Compilação para C++ Namespaces 


218 
 
 
para a LingPON e Otimizações no Tratamento de Premissas. Curitiba/PR, 2016. 
ATIBI, M.; ATOUF, I.; BOUSSAA, M.; BENNIS, A. Parallel and mixed hardware implementation 
of artificial neuron network on the FPGA platform. International Journal of Engineering and 
Technology, v. 6, n. 5, p. 2008–2016, 2014. 
BALID, W.; ABDULWAHED, M. A novel FPGA educational paradigm using the next generation 
programming languages case of an embedded FPGA system course. 2013 IEEE Global 
Engineering Education Conference (EDUCON).  Anais... . p.23–31, 2013. Berlin, Germany: 
IEEE. Disponível em: <http://ieeexplore.ieee.org/document/6530082>. . 
BANASZEWSKI, R. F. Paradigma Orientado a Notificações: Avanços e Comparações, 
2009. Curitiba/PR: Dissertação (Mestrado em Engenharia) - Programa de Pós-Graduação em 
Engenharia Elétrica e Informática Industrial (CPGEI/UTFPR), Curitiba. 
BANASZEWSKI, R. F.; STADZISZ, P. C.; TACLA, C. A.; SIMÃO, J. M. Notification Oriented 
Paradigm (NOP): A Software Development Approach based on Artificial Intelligence Concepts. 
Logic Applied To Technology.  Anais... , 2007. Santos/SP. 
BAPTISTA, D.; ABREU, S.; FREITAS, F.; VASCONCELOS, R.; MORGADO-DIAS, F. A survey 
of software and hardware use in artificial neural networks. Neural Computing and 
Applications, 
v. 
23, 
n. 
3–4, 
p. 
591–599, 
2013. 
Disponível 
em: 
<http://link.springer.com/10.1007/s00521-013-1406-y>. . 
BAPTISTA, F. D.; MORGADO-DIAS, F. Automatic general-purpose neural hardware generator. 
Neural Computing and Applications, v. 28, n. 1, p. 25–36, 2017. Disponível em: 
<http://link.springer.com/10.1007/s00521-015-2034-5>. . 
BARRETO, W. R. M.; VENDRAMI, A. C. B. K.; SIMÃO, J. M. Notification Oriented Paradigm for 
Distributed Systems. Anais do Computer on the Beach.  Anais... , 2018. Florianópolis/SC. 
BELMONTE, D. L. Método para Distribuição da Carga de Trabalho dos Softwares PON em 
Multicore, 2012. Qualificação (Doutorado em Engenharia) - Programa de Pós-Graduação em 
Engenharia Elétrica e Informática Industrial (CPGEI/UTFPR), Curitiba. 
BELMONTE, D. L.; LINHARES, R. R.; STADZISZ, P. C.; SIMÃO, J. M. A new Method for 
Dynamic Balancing of Workload and Scalability in Multicore Systems. IEEE Latin America 
Transactions, 
v. 
14, 
n. 
7, 
p. 
3335–3344, 
2016. 
Disponível 
em: 
<http://ieeexplore.ieee.org/document/7587639/>. . 
BELMONTE, D. L.; SIMÃO, J. M.; STADZISZ, P. C. Proposta de um Método para Distribuição 
da Carga de Trabalho usando o Paradigma Orientado a Notificações (PON). Sodebras, v. 7, n. 
84, p. 10–18, 2012. 
BERAN, P. P.; VINEK, E.; SCHIKUTA, E.; WEISHAUPL, T. ViNNSL-the Vienna Neural Network 
Specification Language. IEEE International Joint Conference on Neural Networks, 2008. 
IJCNN 2008. (IEEE World Congress on Computational Intelligence)., p. 1872–1879, 2008. 
Disponível em: <http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4634053>. . 
BOHRN, M.; FUJCIK, L.; VRBA, R. Field programmable neural array for feed-forward neural 
networks. 2013 36th International Conference on Telecommunications and Signal 
Processing, TSP 2013, p. 727–731, 2013. 
BORKAR, S.; CHIEN, A. A. The future of microprocessors. Communications of the ACM, v. 
54, 
n. 
5, 
p. 
67, 
2011. 
Disponível 
em: 
<nhttp://portal.acm.org/citation.cfm?doid=1941487.1941507>. . 
BOYD, J. Renesas Unveils Its Open Autonomous Vehicle Platform. . 


219 
 
 
BROOKSHEAR, J. G.; BRYLOW, D. Computer Science: An overview. Pearson, 2014. 
BROWN, S.; VRANESIC, Z. Fundamentals of Digital Logic with VHDL Design. 3rd ed. 
McGraw-Hill Education, 2008. 
BULLINARIA, J. A. Step by Step Guido to IMplementing a Neural Network in C. Disponível em: 
<http://www.cs.bham.ac.uk/~jxb/INC/nn.html>. Acesso em: 21/8/2017. 
CARRO, L. Projeto e Prototipação de Sistemas Digitais. Porto Alegre/RS: Editora 
Universidade/UFRGS, 2001. 
CHATURVEDI, S.; TITRE, R. N.; SONDHIYA, N. Review of handwritten pattern recognition of 
digits and special characters using feed forward neural network and izhikevich neural model. 
Proceedings - International Conference on Electronic Systems, Signal Processing, and 
Computing Technologies, ICESC 2014, p. 425–428, 2014. 
CHEN, D.; CONG, J.; PAN, P. FPGA Design Automation: A Survey. Hanover/MA: Now 
Publishers Inc., 2006. 
CHRISTIAANSE, G. J.; ZJAJO, A.; GALUZZI, C.; VAN LEUKEN, R. A real-time hybrid neuron 
network for highly parallel cognitive systems. 2016 38th Annual International Conference of the 
IEEE Engineering in Medicine and Biology Society (EMBC).  Anais... . p.792–795, 2016. IEEE. 
Disponível em: <http://ieeexplore.ieee.org/document/7590820/>. . 
COSTA, C. DA. Projetos de Circuitos Digitais com FPGA. 3o ed. São Paulo/SP: Editora Érica, 
2014. 
COSTA, E. M. M.; LUDWIG JUNIOR, O. Redes Neurais - Fundamentos e Aplicações com 
Programas em C. 1o ed. Rio de Janeiro/RJ: Ciência Moderna, 2007. 
COURBARIAUX, M.; BENGIO, Y. BinaryNet: Training Deep Neural Networks with Weights and 
Activations Constrained to +1 or -1. 30th Annual Conference on Neural Information Processing 
Systems 2016.  Anais... . p.9, 2016. Disponível em: <http://arxiv.org/abs/1602.02830>. . 
COURBARIAUX, M.; BENGIO, Y.; DAVID, J.-P. BinaryConnect: Training Deep Neural Networks 
with binary weights during propagations. 29th Annual Conference on Neural Information 
Processing Systems.  Anais... . p.3123–3131, 2015. Montreal, Canada: Curran Associates, Inc. 
Disponível em: <http://arxiv.org/abs/1511.00363>. . 
COUSSY, P.; GAJSKI, D. D.; MEREDITH, M.; TAKACH, A. An Introduction to High-Level 
Synthesis. IEEE Design & Test of Computers, v. 26, n. 4, p. 8–17, 2009. Disponível em: 
<http://ieeexplore.ieee.org/document/5209958/>. . 
DAOUD, L.; ZYDEK, D.; SELVARAJ, H. A Survey of High Level Synthesis Languages, Tools, 
and Compilers for Reconfigurable High Performance Computing. In: J. Swiątek; A. Grzech; P. 
Swiątek; J. M. Tomczak (Orgs.); Advances in Systems Science, Advances in Intelligent 
Systems and Computing. v. 240, p.653–669, 2014. Cham: Springer International Publishing. 
Disponível em: <http://link.springer.com/10.1007/978-3-319-01857-7>. . 
DEOTALE, P. D.; DOLE, L. Design of FPGA based general purpose neural network. 
International Conference on Information Communication and Embedded Systems 
(ICICES2014), 
, 
n. 
978, 
p. 
1–5, 
2014. 
Disponível 
em: 
<http://ieeexplore.ieee.org/lpdocs/epic03/wrapper.htm?arnumber=7033843>. . 
DIONNE, 
J.; 
DURRANT, 
M. 
Documentation 
- 
uClinux 
Project. 
Disponível 
em: 
<http://www.uclinux.org/description/>. Acesso em: 18/8/2017. 
FAHLMAN, S. E. An empirical study of learning speed in back-propagation networks. Neural 


220 
 
 
Networks, 
v. 
6, 
n. 
3, 
p. 
1–19, 
1988. 
Disponível 
em: 
<http://scholar.google.com/scholar?cluster=3383018529262918047&hl=en>. . 
FAN YANG; PAINDAVOINE, M. Implementation of an RBF Neural Network on Ebedded 
Systems: real-time face tracking and identity verification. IEEE Transactions on Neural 
Networks, 
v. 
14, 
n. 
5, 
p. 
1162–1175, 
2003. 
Disponível 
em: 
<http://ieeexplore.ieee.org/document/1243718/>. . 
FERLIN, E. P. Arquitetura paralela reconfigurável baseada em fluxo de dados implementada 
em FPGA. , p. 159, 2008. 
FERREIRA, C. A. Linguagem e compilador para o Paradigma Orientado a Notificações 
(PON): avanços e comparações, 2015. Dissertação (Mestrado em Engenharia) - Programa 
de Pós-Graduação em Engenharia Elétrica e Informática Industrial (CPGEI/UTFPR), Curitiba. 
FORGY, C. RETE: A Fast Algorithm for the Many Pattern/Many Object Pattern Match Problem. 
Artificial Intelligence, v. 19, n. 1, p. 17–37, 1982. 
FORSSELL, M. Hardware Implementation of Artificial Neural Networks. Pittsburgh, PA, 
2014. 
FRANKLE, J.; CARBIN, M. The Lottery Ticket Hypothesis: Training Pruned Neural Networks. 
CoRR, v. abs/1803.0, 2018. Disponível em: <http://arxiv.org/abs/1803.03635>. . 
FREUND, K.; MOORHEAD, P.; MCCUTCHEON, S. Xilinx Reconfigurable Acceleration Stack 
Targets Machine Learning, Data Analytics, & Video Streaming. , 2016. Moor Insight and 
Strategy. Disponível em: <http://www.moorinsightsstrategy.com/research-paper-a-machine-
learning-application-landscape/>. . 
FREUND, K.; MOORHEAD, P.; MCCUTCHEON, S. A Machine Learning Application 
Landscape. 
, 
2017. 
Moor 
Insights 
and 
Strategy. 
Disponível 
em: 
<https://www.xilinx.com/support/documentation/backgrounders/Machine-Learning-Application-
Landscape.pdf>. . 
FU, Y.; WU, E.; SANTHASEELAN, V.; et al. Embedded Vision with INT8 Optimization on Xilinx 
Devices. 
, 
2017. 
Xilinx. 
Disponível 
em: 
<https://www.xilinx.com/support/documentation/white_papers/wp486-deep-learning-int8.pdf>. . 
GABBRIELLI, M.; MARTINI, S. Programming Languages: Principles and Paradigms. 1st ed. 
London: Springer-Verlag London, 2010. 
GEORGE, D.; HAWKINS, J. A hierarchical bayesian model of invariant pattern recognition in 
the visual cortex. Proceedings. 2005 IEEE International Joint Conference on Neural Networks, 
2005. 
 
Anais... 
. 
v. 
3, 
p.1812–1817, 
2005. 
IEEE. 
Disponível 
em: 
<http://ieeexplore.ieee.org/document/1556155/>. . 
GIANNINI, F.; LAVEGLIA, V.; ROSSI, A.; ZANCA, D.; ZUGARINI, A. Neural Networks for 
Beginners. A fast implemention in Matlab, Torch, TensorFlow. Arxiv, p. 1–48, 2017. Disponível 
em: <http://arxiv.org/abs/1703.05298>. . 
GIRAU, B. FPNA: Concepts and Properties. In: A. R. Omondi; J. C. Rajapakse (Orgs.); FPGA 
Implementations of Neural Networks. p.363, 2006. Nancy/FR: Springer. 
GIRAU, B.; TORRES-HUITZIL, C. Massively distributed digital implementation of an integrate-
and-fire LEGION network for visual scene segmentation. Neurocomputing, v. 70, n. 7–9, p. 
1186–1197, 
2007. 
Disponível 
em: 
<http://linkinghub.elsevier.com/retrieve/pii/S0925231206004711>. . 


221 
 
 
GÓES, L. F. W.; ROULIN, F.; RAMOS, L. E. S.; ZÁRATE, L. E.; MARTINS, C. A. P. S. Análise 
do Desempenho de uma Implementação Paralela da Rede Neural Perceptron Multicamadas 
Utilizando Variável Compartilhada. Conferencia Iberoamericana en Sistemas, Cibernética e 
Informática.  Anais... , 2002. 
GOKHALE, M.; GRAHAM, P. S. Reconfigurable Computing: Accelerating Computation 
with Field-Programmable Gate Arrays. Springer, 2005. 
GOMPERTS, A.; UKIL, A.; ZURFLUH, F. Development and implementation of parameterized 
FPGA-based general purpose neural networks for online applications. IEEE Transactions on 
Industrial Informatics, v. 7, n. 1, p. 78–89, 2011. 
GREEN, S. B. FPGA Coprocessing for Computational Mathematics, 2009. University of 
Central Arkansas. 
GRUVE, W. A. Distributed Intelligence Systems: A new Paradigm for System Integration. IEEE 
Int. Conference on Information Reuse and Integration (IRI).  Anais... . p.14–16, 2007. 
GUIZZO, 
E. 
How 
Google’s 
Self-Driving 
Car 
Works. 
Disponível 
em: 
<http://spectrum.ieee.org/automaton/robotics/artificial-intelligence/how-google-self-driving-car-
works>. Acesso em: 15/2/2017. 
GUO, Y. H.; ZHOU, D. T.; QIAN, X. P.; ZENG, X. Q. A Parallel BP Neural Network Based on 
the FPGA. Applied Mechanics and Materials, v. 239–240, p. 1541–1545, 2012. Disponível 
em: <http://www.scientific.net/AMM.239-240.1541>. . 
GUPTA, G.; SOHI, G. S. Dataflow execution of sequential imperative programs on multicore 
architectures. Proceedings of the 44th Annual IEEE/ACM International Symposium on 
Microarchitecture.  Anais... . p.59–70, 2011. 
HARIPRASATH, S.; PRABAKAR, T. N. FPGA Implementation of Multilayer Feed Forward 
Neural Network Architecture using VHDL. International Conference on Computing, 
Communication and Applications (ICCCA)2012, p. 1–6, 2012. 
HAYKIN, S. Neural Networks and Learning Machines. 2o ed. Porto Alegre/RS: Pearson, 
2008. 
HEATON, J. Artificial Intelligence for Humans, Volume 3: Deep Learning and Neural 
Networks. First ed ed. Chesterfield, MO: Heaton Research, Inc., 2015. 
HECHT-NIELSEN, R. Theory of the Backpropagation Neural Network. Proceedings Of The 
International Joint Conference On Neural Networks.  Anais... . v. 1, p.593–605, 1989. 
HEMSOTH, N. Escher Erases Batching Lines for Efficient FPGA Deep Learning. Disponível em: 
<https://www.nextplatform.com/2017/04/25/escher-erases-batching-lines-efficient-fpga-deep-
learning/>. Acesso em: 26/4/2017. 
HENZEN, A. F. Portabilidade do Framework PON de C++ Standard para C# e Java. 
Curitiba/PR, 2015. 
HIGH, R. The Era of Cognitive Systems: An Inside Look at IBM Watson and How it Works. , 
2012. 
IBM Digital Services Group, Technical Content Services. Disponível em: 
<http://www.redbooks.ibm.com/redpapers/pdfs/redp4955.pdf>. . 
HUNTER, D.; YU, H.; PUKISH, M. S.; KOLBUSZ, J.; WILAMOWSKI, B. M. Selection of Proper 
Neural Network Sizes and Architectures — A Comparative Study. IEEE Transactions on 
Industrial Informatics, v. 8, n. 2, p. 228–240, 2012. 


222 
 
 
HUQQANI, A. A.; SCHIKUTA, E.; YE, S.; CHEN, P. Multicore and GPU parallelization of neural 
networks for face recognition. Procedia Computer Science, v. 18, p. 349–358, 2013. Elsevier 
B.V. Disponível em: <http://dx.doi.org/10.1016/j.procs.2013.05.198>. . 
HYDE, R. The Art of Assembly Language. 2nd. ed. São Francisco, CA: No Starch Press, 
2010. 
IEEE Standard for Information Technology- Portable Operating System Interface (POSIX)- Part 
1: System Application Program Interface (API)-Amendment J: Advanced Real-time Extensions 
[C Language]. .IEEE Std 1003.1j-2000, p. 0_1-88, 2000. 
Iris DataSet. .Disponível em: <https://archive.ics.uci.edu/ml/datasets/Iris>. Acesso em: 
15/2/2016. 
JACOB, B.; KLIGYS, S.; CHEN, B.; et al. Quantization and Training of Neural Networks for 
Efficient Integer-Arithmetic-Only Inference. Proceedings of the IEEE Computer Society 
Conference on Computer Vision and Pattern Recognition, p. 2704–2713, 2018. 
JENKINS, J. CipherStream Protocol: How CoolRunner-II CPLDs Protect FPGA IP. , 2003. Xilinx. 
Disponível em: <https://www.xilinx.com/support/documentation/white_papers/wp197.pdf>. . 
JOHNSTON, W. M.; HANNA, J. R. P.; MILLAR, R. J. Advances in dataflow programming 
languages. ACM Computing Surveys, v. 36, n. 1, p. 1–34, 2004. Disponível em: 
<http://portal.acm.org/citation.cfm?doid=1013208.1013209>. . 
JOSHI, P. Artificial Intelligence with Python. Birmingham, Mumbai: Packt Publishing, 2017. 
KAISLER, S. H. Software Paradigms. 1st ed. John Wiley & Sons, 2005. 
KALBANDE, C.; BAVASKAR, A. Implementation of FPGA-Based General Purpose Artificial 
Neural Network. ITSI Transactions on Electrical and Electronics Engineering, v. 1, n. 3, p. 
99–103, 2013. 
KERSCHBAUMER, R. Paradigma Orientado A Notificações Para Síntese De Lógica 
Reconfigurável, 2017. Qualificação (Doutorado em Engenharia) - Programa de Pós-
Graduação em Engenharia Elétrica e Informática Industrial (CPGEI/UTFPR), Curitiba. 
KERSCHBAUMER, R. Proposição do paradigma orientado a notificações no 
desenvolvimento de circuitos lógico-digitais reconfiguráveis., 2018. Tese (Doutorado em 
Engenharia) - Programa de Pós-Graduação em Engenharia Elétrica e Informática Industrial 
(CPGEI/UTFPR), Curitiba. Disponível em: <http://repositorio.utfpr.edu.br/jspui/handle/1/3811>. 
. 
KERSCHBAUMER, R.; LINHARES, R. R.; SIMÃO, J. M.; STADZISZ, P. C.; ERIG LIMA, C. R. 
Notification-Oriented Paradigm to Implement Digital Hardware. Journal of Circuits, Systems 
and 
Computers, 
v. 
27, 
n. 
08, 
2018. 
Disponível 
em: 
<https://www.worldscientific.com/doi/abs/10.1142/S0218126618501244>. . 
KERSCHBAUMER, R.; SIMAO, J. M.; FABRO, J. A.; ERIG LIMA, C. R.; RIBEIRO LINHARES, 
R. A Tool for Digital Circuits Synthesis Based on Notification Oriented Paradigm. IEEE Latin 
America 
Transactions, 
v. 
16, 
n. 
6, 
p. 
1574–1586, 
2018. 
Disponível 
em: 
<https://ieeexplore.ieee.org/document/8444152/>. . 
KERSCHBAUMER, R.; SIMÃO, J. M.; LINHARES, R. R.; STADZISZ, P. C.; LIMA, C. R. E. 
Paradigma Orientado a Notificações para a Síntese de Lógica Reconfigurável. Congresso 
Brasileiro em Inteligência Artificial.  Anais... , 2015. Curitiba/PR. 
KILTS, S. Advanced FPGA Design Architecture , Implementation , and Optimization. 1st 


223 
 
 
ed. Wiley-IEEE Press, 2007. 
KIM, Y.; ZHANG, Y.; LI, P. A digital neuromorphic VLSI architecture with memristor crossbar 
synaptic array for machine learning. 2012 IEEE International SOC Conference.  Anais... . 
p.328–333, 2012. IEEE. Disponível em: <http://ieeexplore.ieee.org/document/6398336/>. . 
KOSSOSKI, C. Proposta de um Método de Teste para Processos de Desenvolvimento de 
Software Usando o Paradigma Orientado a Notificações, 2015. Dissertação (Mestrado em 
Engenharia) - Programa de Pós-Graduação em Engenharia Elétrica e Informática Industrial 
(CPGEI/UTFPR), Curitiba. 
KRIPS, M.; LAMMERT, T.; KUMMERT, A. FPGA implementation of a neural network for a real-
time hand tracking system. Proceedings First IEEE International Workshop on Electronic 
Design, Test and Applications ’2002.  Anais... . p.313–317, 2002. IEEE Comput. Soc. 
Disponível em: <http://ieeexplore.ieee.org/document/994637/>. . 
KROSE, B.; SMAGT, P. VAN DER. An introduction to Neural Networks. Eighth ed. 
Amsterdam: University of Amsterdan, 1996. 
KURZWEIL, R. How to Create a Mind: The Secret of Human Thought Revealed. 1st ed. 
Viking Penguin, 2012. 
LAKSHMI, K. P.; SUBADRA, M. A survey on FPGA based MLP realization for on-chip learning. 
International Journal of Scientific & Engineering Research, v. 4, n. 1, p. 1–9, 2013. 
Disponível em: <http://www.ijser.org>. . 
LAMERES, B. J. Introduction to Logic Circuits and Logic Design with VHDL. 1o ed. Springer 
International Publishing, 2017. 
LEO, M.; MEDIONI, G.; TRIVEDI, M.; KANADE, T.; FARINELLA, G. M. Computer vision for 
assistive technologies. Computer Vision and Image Understanding, v. 154, p. 1–15, 2017. 
Disponível em: <http://linkinghub.elsevier.com/retrieve/pii/S1077314216301357>. . 
LI, X. J.; LI, L. IP Core Based Hardware Implementation of Multi-Layer Perceptrons on FPGAs: 
A Parallel Approach. Advanced Materials Research, v. 433–440, p. 5647–5653, 2012. 
Disponível em: <http://www.scientific.net/AMR.433-440.5647>. . 
LINHARES, R. R. Contribuição para o desenvolvimento de uma arquitetura de 
computação própria ao paradigma orientado a notificações, 2015. Tese (Doutorado em 
Engenharia) - Programa de Pós-Graduação em Engenharia Elétrica e Informática Industrial 
(CPGEI/UTFPR), Curitiba. 
LINHARES, R. R.; RENAUX, D. P. B.; STADZISZ, P. C.; SIMÃO, J. M. Evaluation of the 
Notification Oriented Paradigm applied to Real-Time Systems. Brazilian Symposium on 
Computing Systems Engineering (SBESC).  Anais... , 2014. Manaus/AM. 
LINHARES, R. R.; SIMÃO, J. M.; STADZISZ, P. C. NOCA: A notification-oriented computer 
architecture. IEEE Latin America Transactions, v. 13, n. 5, p. 1593–1604, 2015. 
LIU, C.; YANG, Q.; ZHANG, C.; et al. A memristor-based neuromorphic engine with a current 
sensing scheme for artificial neural network applications. 2017 22nd Asia and South Pacific 
Design Automation Conference (ASP-DAC).  Anais... . p.647–652, 2017. IEEE. Disponível em: 
<http://ieeexplore.ieee.org/document/7858397/>. . 
LOPEZ, R. Open NN: An Open Source Neural Networks C++ Library. , 2014. CIMNE - 
International 
Center 
for 
Numerical 
Methods 
in 
Engineering. 
Disponível 
em: 
<www.cimne.com/flood>. . 


224 
 
 
MA, Y.; XIONG, R.; ZHANG, F. Design of a FPGA-Based Multiple Motors Control System. 
Lecture Notes in Electrical Engineering, vol 133. p.557–567, 2011. Berlin, Heidelberg: 
Springer. Disponível em: <http://link.springer.com/10.1007/978-3-642-25992-0_76>. . 
MARTINI, G. H. K. NOPL & Compiler to NOP C++ Namespace Multi-Threading Oriented 
Solution: Studies of Capabilities for the X86-64 Architecture. 2018. 
MCCAFFREY, 
J. 
How 
To 
Reuse 
Neural 
Network 
Models. 
Disponível 
em: 
<https://visualstudiomagazine.com/articles/2015/09/01/how-to-reuse-neural-network-
models.aspx>. Acesso em: 22/5/2016. 
MEEUS, W.; VAN BEECK, K.; GOEDEMÉ, T.; MEEL, J.; STROOBANDT, D. An overview of 
today’s high-level synthesis tools. Design Automation for Embedded Systems, v. 16, n. 3, p. 
31–51, 2012. Disponível em: <http://link.springer.com/10.1007/s10617-012-9096-8>. . 
MELO, L. C. V. Adaptação do Paradigma Orientado a Notificações para desenvolvimento 
de Sistemas Fuzzy, 2016. Dissertação (Mestrado em Ciências) - Programa de Pós-Graduação 
em Computação Aplicada (PPGCA/UTFPR), Curitiba. 
MENDES, C. C. S.; FERREIRA, C. A.; RONSZCKA, A. F.; FABRO, J. A.; SIMÃO, J. M. 
LingPON 2.0 & Compilador para Framework PON C++ 3.0 & PON-IP. Disciplina EE2261 - 
Estudos Especiais Em Paradigmas de Programação. CPGEI/UTFPR/Curitiba, PR. 2019/01, 
2019. 
MENDONÇA, I. T. M. Metodologia De Projeto De Software Orientado A Notificações, 2016. 
Qualificação (Doutorado em Engenharia) - Programa de Pós-Graduação em Engenharia 
Elétrica e Informática Industrial (CPGEI/UTFPR), Curitiba. 
MENDONÇA, I. T. M.; SIMÃO, J. M.; WIECHETECK, L. V. B.; STADZISZ, P. C. Método para 
Desenvolvimento de Sistemas Orientados a Regras utilizando o Paradigma Orientado a 
Notificações. 12th Congresso Brasileiro de Inteligencia Computacional - CBIC.  Anais... , 2015. 
Curitiba, Paraná, Brazil. 
MIRANKER, D. P.; BRANT, D. A.; LOFASO, B.; GADBOIS, D. On the Performance of Lazy 
Matching in Production System. 8th National Conference on Artificial Intelligence AAAI.  Anais... 
. p.685–692, 1990. AAAI Press / The MIT Press. 
MISRA, J.; SAHA, I. Artificial neural networks in hardware: A survey of two decades of progress. 
Neurocomputing, 
v. 
74, 
n. 
1–3, 
p. 
239–255, 
2010. 
Elsevier. 
Disponível 
em: 
<http://dx.doi.org/10.1016/j.neucom.2010.03.021>. . 
MITRA, S.; FUSI, S.; INDIVERI, G. Real-Time Classification of Complex Patterns Using Spike-
Based Learning in Neuromorphic VLSI. IEEE Transactions on Biomedical Circuits and 
Systems, 
v. 
3, 
n. 
1, 
p. 
32–42, 
2009. 
Disponível 
em: 
<http://ieeexplore.ieee.org/document/4693998/>. . 
MOUKHLIS, S. EL; ELRHARRAS, A.; HAMDOUN, A. FPGA Implementation of Artificial Neural 
Networks. IJCSI Internationl Journal of Computer Science Issues, v. 11, n. 2, p. 237–239, 
2014. Disponível em: <http://ethesis.nitrkl.ac.in/4217/>. . 
MUSCEDERE, R.; LEBOEUF, K. A dynamic address decode circuit for implementing range 
addressable look-up tables. Proceedings - IEEE International Symposium on Circuits and 
Systems, , n. m, p. 3326–3329, 2008. 
NAMIN, A. H.; LEBOEUF, K.; MUSCEDERE, R.; WU, H.; AHMADI, M. Efficient hardware 
implementation of the hyperbolic tangent sigmoid function. Proceedings - IEEE International 
Symposium on Circuits and Systems, , n. June, p. 2117–2120, 2009. 


225 
 
 
NEDJAH, N.; SILVA, F. P. DA; SÁ, A. O. DE; MOURELLE, L. M.; BONILLA, D. A. A massively 
parallel pipelined reconfigurable design for M-PLN based neural networks for efficient image 
classification. Neurocomputing, v. 183, p. 39–55, 2016. 
NEDJAH, N.; DA SILVA, R. M.; DE MACEDO MOURELLE, L. Compact yet efficient hardware 
implementation of artificial neural networks with customized topology. Expert Systems with 
Applications, v. 39, n. 10, p. 9191–9206, 2012. Elsevier Ltd. Disponível em: 
<http://dx.doi.org/10.1016/j.eswa.2012.02.085>. . 
NEGRINI, F. LingPON 2.0 & Compilador para Framework Erlang: Programação Multicore 
Transparente já é uma Realidade. Curitiba/PR, 2019. 
NEGRINI, F.; RONSZCKA, A. F.; LINHARES, R. R.; FABRO, J. A.; STADZISZ, P. C. NOPL-
Erlang: Programação multicore transparente em linguagem de alto nível. V Escola Regional de 
Alto Desempenho do Rio de Janeiro (ERAD-RJ 2019).  Anais... , 2019. Rio de Janeiro/RJ: 
CEFET/RJ. 
NGUYEN, H. A. DU; AL-ARS, Z.; SMARAGDOS, G.; STRYDIS, C. Accelerating Complex Brain-
Model Simulations on GPU Platforms. Design, Automation & Test in Europe Conference & 
Exhibition (DATE), 2015.  Anais... . p.974–979, 2015. New Jersey: IEEE Conference 
Publications. 
Disponível 
em: 
<http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=7092530>. . 
NUSSBAUM, B.; SCHIKUTA, E. A Lightweight Cloud Execution Stack for Neural Network 
Simulation. In: Cheng L., Leung A., Ozawa S. (eds) Neural Information Processing. ICONIP 
2018. Lecture Notes in Computer Science, vol 11306. p.181–192, 2018. Springer, Cham. 
Disponível em: <http://link.springer.com/10.1007/978-3-030-04224-0_16>. . 
NVIDIA. 
CUDA 
Toolkit 
Documentation. 
Disponível 
em: 
<http://docs.nvidia.com/cuda/index.html>. Acesso em: 5/4/2017. 
OLIVEIRA, R. N.; ROTH, V.; HENZEN, A. F.; et al. Notification Oriented Paradigm Applied to 
Ambient Assisted Living Tool. IEEE Latin America Transactions, v. 16, n. 2, p. 7, 2018. 
OMONDI, A. R.; RAJAPAKSE, J. C.; BAJGER, M. FPGA Implementations of Neural 
Networks. Dordrecht/NED: Springer US, 2006. 
ORTEGA-ZAMORANO, F.; JEREZ, J. M.; JUÁREZ, G.; PÉREZ, J. O.; FRANCO, L. High 
precision FPGA implementation of neural network activation functions. IEEE Symposium on 
Intelligent Embedded Systems (IES).  Anais... . p.55–60, 2014. Orlando/FL. 
PARKER, G.; KHAN, M. Distributed neural network: Dynamic learning via backpropagation with 
hardware neurons using arduino chips. 2016 International Joint Conference on Neural Networks 
(IJCNN). 
 
Anais... 
. 
p.206–212, 
2016. 
IEEE. 
Disponível 
em: 
<http://ieeexplore.ieee.org/document/7727200/>. . 
PEDRONI, V. A. Circuit Design and Simulation with VHDL. Second ed. The MIT Press, 
2010a. 
PEDRONI, V. A. Eletrônica Digital Moderna com VHDL. Elsevier, 2010b. 
PETERS, E.; JASINSKI, R. P.; PEDRONI, V. A.; SIMÃO, J. M. A new hardware coprocessor for 
accelerating notification-oriented applications. FPT 2012 - 2012 International Conference on 
Field-Programmable Technology.  Anais... . p.257–260, 2012. Seoul, Korea: IEEE Comput. 
Soc. 
PETHICK, M.; LIDDLE, M.; WERSTEIN, P.; HUANG, Z. Parallelization of a backpropagation 
neural network on a cluster computer. 15th IASTED International Conference on Parallel and 


226 
 
 
Distributed Computing and Systems.  Anais... . p.574–582, 2003. Marina Del Rey, California: 
IASTED/ACTA Press. 
POPA, C.-A. Enhanced Gradient Descent Algorithms for Complex-Valued Neural Networks. 
2014 16th International Symposium on Symbolic and Numeric Algorithms for Scientific 
Computing. 
 
Anais... 
. 
p.272–279, 
2014. 
IEEE. 
Disponível 
em: 
<http://ieeexplore.ieee.org/document/7034694/>. . 
PORDEUS, L. F. Contribuição para o desenvolvimento de uma arquitetura de computação 
própria ao paradigma orientado a notificações, 2017. Dissertação (Mestrado em 
Engenharia) - Programa de Pós-Graduação em Engenharia Elétrica e Informática Industrial 
(CPGEI/UTFPR), Curitiba. 
PORDEUS, L. F.; KERSCHBAUMER, R.; LINHARES, R. R.; et al. Notification Oriented 
Paradigm To Digital Hardware. Sodebras, v. 11, n. 128, p. 116–122, 2016. 
POU-YUNG LEE; CHENG, A. M. K. HAL: a faster match algorithm. IEEE Transactions on 
Knowledge and Data Engineering, v. 14, n. 5, p. 1047–1058, 2002. Disponível em: 
<http://ieeexplore.ieee.org/document/1033773/>. . 
PRESSMAN, R. S. Engenharia de Software. 7o ed. Porto Alegre/RS: AMGH Editora Ltda., 
2011. 
RAIZER, K.; IDAGAWA, H. S.; NÓBREGA, E. G. O.; FERREIRA, L. O. S. Performance 
comparison of training methods for mlp neural networks in gpu. Proc. of the CONEM 2010, 
2010. 
REZVANI, R.; KATIRAEE, M.; JAMALIAN, A. H.; MEHRABI, S. H.; VEZVAEI, A. A New Method 
for Hardware Design of Multi-Layer Perceptron Neural Networks with Online Training. 
Proceedings of the 11th Conference on Cognition Informatics&Cognitive Computing 
(ICCI’CC), p. 527–534, 2012. 
RICE, K. L.; TAHA, T. M.; VUTSINAS, C. N. Scaling analysis of a neocortex inspired cognitive 
model on the Cray XD1. The Journal of Supercomputing, v. 47, n. 1, p. 21–43, 2009. 
Disponível em: <http://link.springer.com/10.1007/s11227-008-0195-z>. . 
RIOS, D. Writing the Backpropagation Algorithm into C++ Source Code. Disponível em: 
<http://www.learnartificialneuralnetworks.com/neural-network-software/backpropagation-
source-code/>. Acesso em: 21/8/2017. 
ROCHA, R. H. S. Reconhecimento de Objetos por Redes Neurais Convolutivas. , p. 49, 2015. 
RONSZCKA, A. F. Contribuição para a concepção de aplicações no paradigma orientado 
a notificações (PON) sob o viés de padrões, 2012. Dissertação (Mestrado em Engenharia) - 
Programa de Pós-Graduação em Engenharia Elétrica e Informática Industrial (CPGEI/UTFPR), 
Curitiba. 
RONSZCKA, A. F. LINGPON - Linguagem de Programação e Compilador para o 
Paradigma Orientado a Notificações (PON) – Uma Materialização Efetiva para a Validação 
das Propriedades Elementares do PON., 2018. Qualificação (Doutorado em Engenharia) - 
Programa de Pós-Graduação em Engenharia Elétrica e Informática Industrial (CPGEI/UTFPR), 
Curitiba. 
RONSZCKA, A. F. Método para a criação de linguagens de programação e compiladores 
para o paradigma orientado a notificações em plataformas distintas, 2019. Tese 
(Doutorado em Engenharia) - Programa de Pós-Graduação em Engenharia Elétrica e 
Informática Industrial (CPGEI/UTFPR), Curitiba. 


227 
 
 
RONSZCKA, A. F.; BANASZEWSKI, R. F.; LINHARES, R. R.; et al. Notification-Oriented and 
Rete Network Inference: A Comparative Study. Proceedings - 2015 IEEE International 
Conference on Systems, Man, and Cybernetics, SMC 2015.  Anais... . p.807–814, 2015. Hong-
Kong, China: IEEE. 
RONSZCKA, A. F.; FERREIRA, C. A.; STADZISZ, P. C.; FABRO, J. A.; SIMÃO, J. M. 
Notification-Oriented Programming Language and Compiler. 2017 VII Brazilian Symposium on 
Computing Systems Engineering (SBESC).  Anais... . p.125–131, 2017. Curitiba/PR: IEEE. 
Disponível em: <http://ieeexplore.ieee.org/document/8116569/>. . 
RONSZCKA, A. F.; VALENÇA, G. Z.; LINHARES, R. R.; et al. Notification-Oriented Paradigm 
Framework 2.0: An Implementation Based On Design Patterns. IEEE Latin America 
Transactions, v. 15, n. 11, p. 2220–2231, 2017. 
VAN ROY, P. Programming paradigms for dummies: What every programmer should know. 
New computational paradigms for computer music. p.198, 2009. IRCAM/Delatour France. 
VAN ROY, P.; HARIDI, S. Concepts, Techniques, and Models of Computer Programming. 
1st ed. The MIT Press, 2004. 
RUSSEL, S.; NORVIG, P. Artificial Intelligence: A modern approach. 3o ed. Prentice-Hall, 
2009. 
SANDERS, J.; KANDROT, D. CUDA by Example: An Introduction to General-Purpose GPU 
Programming. Addison-Wesley Publishing Company, 2011. 
SANTOS, L. A. Linguagem e Compilador para o Paradigma Orientado A Notificações: 
Avanços para Facilitar a Codificação e sua Validação em uma Aplicação de Controle de 
Futebol de Robôs, 2017. Dissertação (Mestrado em Engenharia) - Programa de Pós-
Graduação em Engenharia Elétrica e Informática Industrial (CPGEI/UTFPR), Curitiba. 
VAN SCHAIK, A. Building blocks for electronic spiking neural networks. Neural Networks, v. 
14, 
n. 
6–7, 
p. 
617–628, 
2001. 
Disponível 
em: 
<http://linkinghub.elsevier.com/retrieve/pii/S0893608001000673>. . 
SCHIKUTA, E.; HUQQANI, A.; KOPICA, T. Semantic extensions to the Vienna Neural Network 
Specification Language. 2015 International Joint Conference on Neural Networks (IJCNN).  
Anais... . p.1–8, 2015. IEEE. Disponível em: <http://ieeexplore.ieee.org/document/7280667/>. . 
SCHIKUTA, E.; WEISHÄUPL, T. Artificial Neural Networks and the Grid. International 
Conference on Computational Science ICCS 2004.  Anais... . p.486–489, 2004. Kraków, 
Poland: 
Springer-Verlag 
Berlin 
Heidelberg. 
Disponível 
em: 
<http://link.springer.com/10.1007/978-3-540-24685-5_72>. . 
SCHUMAN, C. D.; POTOK, T. E.; PATTON, R. M.; et al. A Survey of Neuromorphic Computing 
and 
Neural 
Networks 
in 
Hardware. 
arXiv, 
p. 
1–88, 
2017. 
Disponível 
em: 
<http://arxiv.org/abs/1705.06963>. . 
SCHÜTZ, F. Estudo de FPGAs. Monografia de Graduação (Curso de Bacharelado em 
Informática) - UNIOESTE Campus Cascavel, PR, 2000. 
SCHÜTZ, F.; FABRO, J. A.; LIMA, C. R. E.; et al. Training of an Artificial Neural Network with 
Backpropagation algorithm using notification oriented paradigm. 2015 Latin-America Congress 
on Computational Intelligence, LA-CCI 2015.  Anais... . p.1–6, 2015. Curitiba, Paraná, Brazil: 
IEEE Comput. Soc. 
SCHÜTZ, F.; FABRO, J. A.; RONSZCKA, A. F.; STADZISZ, P. C.; SIMÃO, J. M. Proposal of a 
declarative and parallelizable artificial neural network using the notification-oriented paradigm. 


228 
 
 
Neural Computing and Applications, v. 30, n. 6, p. 1715–1731, 2018. 
SCHÜTZ, F.; RONSZCKA, A. F. Compilador LingPON para StaticCPP. Relatório Técnico 
apresentado à disciplina de doutorado - CPGEI/UTFPR - Curitiba/PR, 2015. 
SCOTT, M. L. Programming Language Pragmatics. 4th ed. Morgan Kaufmann, 2015. 
SEBESTA, R. W. Conceitos de Linguagens de Progamação. 9o ed. Porto Alegre/RS: 
Bookman, 2010. 
SEVILLA, D.; GARCÍA, J. M.; GÓMEZ, A. Using AOP to Automatically Provide Distribution, Fault 
Tolerance, and Load Balancing to the CORBA–LC Component Model. In: C. Bischof; M. Bücker; 
P. Gibbon; et al. (Orgs.); Parallel Computing: Architectures, Algorithms and Applications. 
v. 15, p.347–354, 2008. IOS Press Ebooks. 
SEWARD, J. Valgrind Distribution Documents. Disponível em: <http://www.valgrind.org/docs/>. 
Acesso em: 15/7/2019. 
SILVA, I. N.; SPATTI, D. H.; FLAUZINO, R. A. Redes Neurais Artificiais: para engenharia e 
ciências aplicadas. First ed. São Paulo/SP: Artliber, 2010. 
SILVA, R. M. DA; NEDJAH, N.; MOURELLE, L. DE M. Arquitetura de Hardware Compacta e 
Eficiente para Redes Neurais Artificiais do tipo Múltiplas Camadas. XVIII Congresso Brasileiro 
de Automática.  Anais... . p.2838–2845, 2010. 
SIMÃO, J. M. A Contribution to the Development of a HMS Simulation Tool and 
Proposition of a Meta-Model for Holonic Control, 2005. Ph. D. Thesis. CPGEI at UTFPR, 
Curitiba, PR, Brazil and CRAN at UHP, France. 
SIMÃO, 
J. 
M. 
Paradigma 
Orientado 
a 
Notificações. 
Disponível 
em: 
<http://www.dainf.ct.utfpr.edu.br/~jeansimao/PON/PON.htm>. Acesso em: 5/4/2017. 
SIMÃO, J. M.; BANASZEWSKI, R. F.; TACLA, C. A.; STADZISZ, P. C. Notification Oriented 
Paradigm (NOP) and Imperative Paradigm: A Comparative Study. Journal of Software 
Engineering and Applications, v. 05, n. 06, p. 402–416, 2012. Disponível em: 
<http://search.proquest.com/docview/1024420637?accountid=10344>. . 
SIMÃO, J. M.; LINHARES, R. R.; WITT, F. A.; LIMA, C. R. E.; STADZISZ, P. C. Paradigma 
Orientado a Notificações em Hardware Digital. , 2012. Patent number BR 10 2012 026429 3, 
INPI, Brazil. 
SIMÃO, J. M.; STADZISZ, P. C. Notification Oriented Paradigm (NOP) - A Notification Oriented 
Technique to Software Composition and Execution. , 2008. Patent number: PI0805518-1, INPI, 
Brazil. 
SIMÃO, JEAN MARCELO; STADZISZ, P. C. Paradigma Orientado a Notificações (PON) Uma 
Técnica de Composição e Execução de Software Orientada a Notificações. , 2008. Brasil. 
Disponível em: <http://nitpar.pr.gov.br/catalogo-de-patentes/patente/paradigma-orientado-a-
notificacoes-pon-uma-tecnica-de-composicao-e-execucao-de-software-orientada-a-
notificacoes/>. . 
SIMÃO, J. M.; STADZISZ, P. C. Inference Based on Notifications: A Holonic Metamodel Applied 
to Control Issues. IEEE Transactions on Systems, Man, and Cybernetics - Part A: Systems 
and 
Humans, 
v. 
39, 
n. 
1, 
p. 
238–250, 
2009. 
Disponível 
em: 
<http://ieeexplore.ieee.org/document/4689369/>. . 
SIMÃO, J. M.; STADZISZ, P. C. Mecanismo de Resolução de Conflito e Garantia de 
Determinismo para o Paradigma Orientado a Notificações (PON). , 2010. Pedido de Patente 


229 
 
 
PI0805518-1. Brasil. 
SRIDEVI, K.; SUNDARAMBAL, M.; MURALIDHARAN, K.; JOSEPHINE, R. L. FPGA 
implementation of hand gesture recognition system using neural networks. 2017 11th 
International Conference on Intelligent Systems and Control (ISCO).  Anais... . p.34–39, 2017. 
IEEE. Disponível em: <http://ieeexplore.ieee.org/document/7856017/>. . 
SWAIN, M.; DASH, S. K.; DASH, S.; MOHAPATRA, A. An Approach for IRIS Plant Classification 
using Neural Network. International Journal on Soft Computing - IJSC, v. 3, n. 1, p. 79–89, 
2012. 
TISAN, A.; CHIN, J. An end user platform for implementing Artificial Neutron Networks on FPGA. 
Proceeding - 2015 IEEE International Conference on Industrial Informatics, INDIN 2015, 
p. 856–859, 2015. 
UNIVERSITY OF VIENNA. Comparision of presented approaches. Disponível em: 
<http://www.wst.univie.ac.at/workgroups/veloci/index.php?m=D&t=resources&c=show&CEWe
bS_what=Comparison>. Acesso em: 22/5/2016. 
VALENÇA, G. Z. Contribuição para a materialização do paradigma orientado a 
notificações (PON) via framework e wizard, 2012. Dissertação (Mestrado em Engenharia) - 
Programa de Pós-Graduação em Computação Aplicada (PPGCA/UTFPR), Curitiba. 
VALENÇA, G. Z.; BANASZEWSKI, R. F.; RONSZCKA, A. F.; et al. Framework PON, Avanços 
e Comparações. III Simpósio de Computação Aplicada.  Anais... , 2011. Passo Fundo/RS. 
VESELÝ, K.; BURGET, L.; GRÉZL, F. Parallel Training of Neural Networks for Speech 
Recognition. Proceedings of the 11th Annual Conference of the International Speech 
Communication Association (INTERSPEECH 2010). p.439–446, 2010. Makuhari,Chiba/JP: 
International 
Speech 
Communication 
Association. 
Disponível 
em: 
<http://link.springer.com/10.1007/978-3-642-15760-8_56>. . 
VOLOKITIN, S. Parallel Implementation of a Neural Network Learning Algorithm. International 
Journal of Computer Applications, v. 85, n. 3, p. 8–11, 2014. 
VYAS, S.; UPADHYAY, D. Identification of Iris Plant using Feed Forward Neural Network on the 
Basis of Floral Dimensions. International Journal of Innovative Research in Science, 
Engineering and Technology - IJIRSET, v. 3, n. 12, p. 18200–18204, 2014. 
WANG, Y.-Q.; LIMARE, N. AFast C++ Implementation of Neural Network Backpropagation 
Training Algorithm: Application to Bayesian Optimal Image Demosaicing. Image Processing 
On 
Line, 
v. 
5, 
p. 
257–266, 
2015. 
Disponível 
em: 
<http://www.ipol.im/pub/art/2015/137/?utm_source=doi>. . 
WATT, D. A. Programming Language Design Concepts. 1o ed. Chichester/UK: John Wiley & 
Sons, Ltd, 2004. 
WIJEKOON, J. H. B.; DUDEK, P. Compact silicon neuron circuit with spiking and bursting 
behaviour. Neural Networks, v. 21, n. 2–3, p. 524–534, 2008. Disponível em: 
<http://linkinghub.elsevier.com/retrieve/pii/S0893608007002705>. . 
WINDH, S.; MA, X.; HALSTEAD, R. J.; et al. High-Level Language Tools for Reconfigurable 
Computing. Proceedings of the IEEE, v. 103, n. 3, p. 390–408, 2015. Disponível em: 
<http://ieeexplore.ieee.org/document/7086410/>. . 
WITT, F. A.; SIMÃO, J. M.; LINHARES, R. R.; STADZISZ, P. C.; LIMA, C. R. E. Comparação 
entre o Paradigma Orientado A Objetos (POO) e o Paradigma Orientado a Notificações (PON) 
em um Controle Discreto em Lógica Reconfigurável. XVI SICITE - Seminário de Iniciação 


230 
 
 
Científica e Tecnológica da UTFPR.  Anais... . p.4, 2011. Ponta Grossa/PR: UTFPR. 
WU, S.; LI, G.; CHEN, F.; SHI, L. Training and Inference with Integers in Deep Neural Networks. 
Sixth International Conference on Learning Representations.  Anais... . p.1–14, 2018. 
Vancouver, CANADA. Disponível em: <https://openreview.net/forum?id=HJGXzmspb>. . 
XAVIER, R. D. Paradigmas de Desenvolvimneto de Software: Comparação ente 
abordagens Orientada a Eventos e Orientada a Notificações, 2014. Dissertação (Mestrado 
em Engenharia) - Programa de Pós-Graduação em Computação Aplicada (PPGCA/UTFPR), 
Curitiba. 
XILINX. MicroBlaze Processor Reference Guide. 2017. 
YAZDANBAKHSH, A.; PARK, J.; SHARMA, H.; LOTFI-KAMRAN, P.; ESMAEILZADEH, H. 
Neural acceleration for GPU throughput processors. Proceedings of the 48th International 
Symposium on Microarchitecture - MICRO-48, p. 482–493, 2015. Disponível em: 
<http://dl.acm.org/citation.cfm?doid=2830772.2830810>. . 
YUN, H.; GONDI, S.; BISWAS, S.; CORPORATION, B. BWLOCK : A Dynamic Memory Access 
Control Framework for Soft Real-Time Applications on Multicore Platforms. Transactions on 
Computers, 
v. 
66, 
n. 
7, 
p. 
1247–1252, 
2016. 
Disponível 
em: 
<http://ieeexplore.ieee.org/document/7784697/>. . 
YURIY, 
C. 
Backpropagation 
Artificial 
Neural 
Network 
in 
C++. 
Disponível 
em: 
<https://www.codeproject.com/Articles/21171/Backpropagation-Artificial-Neural-Network-in-
C>. Acesso em: 21/8/2017. 
ZELL, A. JavaNNS: Java Neural Network Simulator. Disponível em: <http://www.ra.cs.uni-
tuebingen.de/software/JavaNNS/>. Acesso em: 26/2/2016. 
 
 
 


231 
 
 
 
Apêndice A – Implementação RNA em Linguagem C 
Procedimental 
Inicialmente, a fim de apresentar os dados que foram utilizados nos testes de 
uma RNA MLP com treinamento via método BP, desenvolvida com linguagem C 
procedimental, a Tabela 1 apresenta os parâmetros da aplicação, bem como alguns 
exemplos de padrões de treinamento em cada uma das bases de dados utilizadas. 
Tabela 1- Parâmetros da RNA implementada na Linguagem C com PI Procedimental 
Função de 
Ativação 
Entradas 
Neurônios 
Learning 
Rate 
Padrões de 
treinamento 
Camada Escondida 
Camada de 
Saída 
Tangente 
Hiperbólica 
4 
5 
3 
0,1 
120 
Exemplo de padrão de treinamento (IRIS DataSet) 
Tabela verdade (XOR) 
H = I ⊕K 
Comprimento 
Sépala 
Largura 
Sépala 
Comprimento 
Pétala 
Largura 
Pétala 
Saída binária 
Espécie 
5,1 
3,5 
1,4 
0,2 
0 
0 
1 
Setosa 
7,0 
3,2 
4,7 
1,4 
0 
1 
0 
Versicolor 
6,3 
3,3 
6,0 
2,5 
1 
0 
0 
Virginica 
 
A 
B 
S 
0 
0 
-1 
0 
1 
1 
1 
0 
1 
1 
1 
-1 
 
 
A implementação apresentada nesta seção é baseada no trabalho de Costa e 
Ludwig Junior (2007). Tal implementação do algoritmo de treinamento BP de uma RNA 
MLP em von Neumann, escrito na linguagem C a partir de uma usual abordagem 
procedimental do PI utilizando matrizes para a representação dos neurônios. Exemplos 
desta usual abordagem computacional baseada em PI matricial  podem ser 
encontradas em trabalhos como (BULLINARIA, 2009; RIOS, 2013; WANG; LIMARE, 
2015; YURIY, 2008).  
De fato, o desenvolvimento de RNA utilizando matrizes é tida como uma 
abordagem tradicional e muito utilizada. Tal fato é corroborado por bibliografias 
tradicionais de RNA como Silva et al. (2010a) e Haykin (2008) que apresentam 
equações, funções e algoritmos imperativos na demonstração de métodos de 
treinamento e execução de RNA, sugerindo a utilização de matrizes para a 
representação de pesos sinápticos e neurônios. Neste contexto, o presente exemplo 
baseou-se em uma implementação matricial como exemplo base de comparação com 
as implementações em PON, apresentadas nas próximas seções. A fim de apresentar 
a implementação, inicialmente a Figura 1 lista algumas variáveis utilizadas no algoritmo. 


232 
 
 
09 
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
40 
41 
42 
//// definição das variáveis da aplicação //// 
#define numInputs 5              // Quantidade de entradas 
#define numHidden 5              // Quantidade de neurônios escondidos 
#define numOutputs 3             // Quantidade de neurônios de saída 
#define numPatterns 120          // Quantidade de padrões de treinamento 
 
const int numEpochs = 10000;     // qtde de épocas 
const float minError = 0.009;    // erro mínimo aceito no treinamento 
const float LR = 0.1;            // learning rate – taxa de aprendizagem 
const float alpha = 1;           // termos de momentum  
const float smallWT = 0.05;      // valor absoluto máximo inicial de peso 
 
float randPatterns[numPatterns];  // matriz de índice de padrões aleatórios 
float weightsIH[numInputs][numHidden];  // matriz de pesos entrada->escondida 
float weightsHO[numHidden][numOutputs]; // matriz de pesos escondida->saída 
float hiddenVal[numHidden];             // matriz de neurônios escondidos 
float outputVal[numOutputs];            // matriz de neurônios de saída 
... 
float trainInputs[numPatterns][numInputs]; // matriz padrões de treinamento 
int trainOutputs[numPatterns][numOutputs]; // matriz saídas esperadas de 
                                           // treinamento 
Figura 1 - Trecho de código: algumas variáveis utilizadas no algoritmo de treinamento pelo  
método BP de uma RNA MLP com Linguagem C procedimental 
O exemplo aqui apresentado permite o treinamento de uma RNA MLP tanto 
para o reconhecimento da função XOR quanto o reconhecimento da base de dados da 
flor de Iris. Porém, os padrões de configuração da estrutura da RNA estão ajustados 
para o treinamento quanto ao reconhecimento da base dados da flor de Iris (Iris 
DataSet). Neste contexto, os identificadores apresentados na Figura  representam, 
respectivamente: 
Linha 10: quantidade de entradas da RNA; 
Linha 11: quantidade de neurônios da camada escondida; 
Linha 12: quantidade de neurônios da camada de saída; 
Linha 13: quantidade de padrões de treinamento; 
Linha 15: quantidade de épocas de treinamento (critério de parada); 
Linha 16: erro mínimo (critério de parada); 
Linha 17: Learning Rate (taxa de aprendizagem); 
Linha 18: termo de momentum; 
Linha 19: valor obsoluto inicial máximo admitido nos pesos sinápticos. É 
utilizado na função de inicialização dos pesos sinápticos; 


233 
 
 
Linha 21: vetor que contém a sequência de padrões para treinamento, em 
ordem aleatória. A cada etapa de treinamento lê-se uma posição do vetor, 
indicando qual padrão de treinamento deve ser lido e utilizado na RNA; 
 Linha 22: matriz contento os valores dos pesos de cada sinapse entre a 
camada de entrada e a camada escondida; 
Linha 23: matriz contendo os valores dos pesos de cada sinapse entre a 
camada escondida e a camada de saída; 
Linha 24: vetor que armazenará os valores dos neurônios da camada 
escondida; 
Linha 25:  vetor que armazenará os valores dos neurônios da camada de saída; 
Linha 40: vetor que armazenará os valores da entrada (de treinamento); 
Linha 41: vetor que armazenará os valores da saída prevista. Como o método 
de treinamento é supervisionado, as saídas são conhecidas, e devem ser 
utilizadas durante o treinamento. 
Tais variáveis são definidas de forma global pois são utilizadas em várias 
funções no algoritmo. Na sequência, a fim de apresentar o exemplo de implementação, 
as funções que executam os processos necessários ao treinamento serão 
apresentadas. Todo algoritmo foi escrito no arquivo main.c da aplicação, sendo que a 
função principal é apresentada na Figura 2. 
240 
241 
242 
243 
244 
245 
246 
247 
248 
249 
 
250 
 
251 
252 
 
 
253 
254 
 
 
 
255 
256 
257 
int main(int argc, char** argv) { 
    int contEpochs = 0;       // variável auxiliar para contagem de épocas 
    float overallError = 0.0; // variável auxiliar para o erro geral da RNA 
    srand(time(NULL));        // inicialização do gerador de num. aleatórios 
    initializeWeights();      // função de inicialização dos pesos 
    getPattern(numPatterns);  // função para aquisição dos padrões de treinamento 
    do { 
        randomPatterns();     // aleatorização dos padrões de treinamento 
        for (int contPattern = 0;contPattern < numPatterns;contPattern++){ 
            calcNet(randPatterns[contPattern]);     // função de cálculo dos 
                                                           // neurônios 
            updateValues(randPatterns[contPattern]); // função para atualização  
                                                            // dos pesos sinápticos  
        } 
        overallError = msePattern / (double)numPatterns;  // cálculo do erro  
                                                                 // geral da RNA em 
                                                                 // determinada época 
        msePattern = 0.0;     // zera o erro médio quadrático   
        contEpochs++;         // incrementa o contador de épocas 
      // condições de parada 
       // encerra quando a quantidade de épocas for maior do que a quantidade definida 
       // ou quando o erro geral na época for menor ou igual ao erro mínimo definido 
    } while ((contEpochs <= numEpochs) && (overallError > minError)); 
    saveData(contEpochs,overallError); // função para salvar os dados 
    return (EXIT_SUCCESS); 


234 
 
 
258 } 
Figura 2 - Algoritmo de treinamento BP utilizando a linguagem de programação C. Trecho de código da função 
principal (main(void)) da aplicação (adaptado de Costa; Ludwig Junior (2007)) 
A Figura 2 apresenta o código do programa principal, com os ajustes iniciais, 
laços de repetição (loops) e chamadas de função que executam as funções necessárias 
ao treinamento da RNA MLP via método BP. Alguns códigos são destacados: 
Linha 244: função de inicialização dos pesos sinápticos. A inicialização dos 
pesos leva em consideração o parâmetro de tamanho máximo permitido. 
Ainda, há a aleatorização de valores entre 0 e 1. 
Linha 245: função de aquisição de padrões de treinamento. A matriz que 
armazena os padrões de treinamento é preenchida por esta função, a partir 
de um arquivo texto informado. 
Linha 247: aleatorização dos padrões de treinamento: a cada época a 
sequência de treinamento é alterada. 
Linha 249: processo de cálculo dos valores dos neurônios da RNA. Nesta 
função são aplicadas as equações de funcionamento dos neurônios, tanto 
da camada escondida quanto da camada de saída. Ao final, tem-se os 
valores de tais neurônios, frente aos pesos sinápticos atuais. Tal processo é 
repetido para cada padrão de treinamento (loop). 
Linha 250: processo de atualização dos pesos sinápticos. Nesta função ocorre 
o processo de treinamento propriamente dito, onde há o ajuste dos pesos 
sinápticos frente aos valores encontrados na etapa anterior. Aqui são 
realizadas as etapas de propagação e retro-propagação do algoritmo de 
treinamento por BP. Tal processo é repetido para cada padrão de 
treinamento (loop). 
Linha 252: obtenção do erro médio da RNA, por meio da divisão da soma dos 
erros quadráticos médios, obtidos na computação de cada padrão de 
treinamento, pela quantidade de padrões de treinamento. 
Linha 255: critérios de parada do treinamento. Caso a quantidade de épocas 
processadas atingiu a quantidade parametrizada inicialmente, ou ainda o 
valor do erro médio da RNA se tornou menor ou igual ao erro mínimo 
parametrizado, o treinamento é encerrado. 


235 
 
 
Linha 256: função que grava os dados em arquivo. Por fim, uma vez que o 
treinamento foi encerrado, os valores atuais de pesos sinápticos e erro médio 
da RNA são armazenados, para que possam ser utilizados para teste e 
execução da RNA. 
As épocas são controladas por um laço de repetição simples, enquanto que 
outro laço de repetição aninhado controla a leitura de cada padrão de leitura. Os pesos 
sinápticos são iniciados com valores aleatórios pequenos, entre 0,0 e 1,0. Todos os 
cálculos nas funções seguem as equações apresentadas para o método BP. A função 
de ativação utilizada, no presente exemplo, é a tangente hiperbólica. Tal função foi 
utilizada no algoritmo original, e mostrou-se adequada ao exemplo da função XOR, pois 
é indicada para funções de classificação com resultados entre -1 e 1. Assim, para fins 
de comparação, continuou sendo utilizada em todos os exemplos, até mesmo com o 
IRIS DataSet. 
Todo o código desta implementação própria, porém baseadas nas 
implementações de Bullinaria (2009), Costa e Ludwig Junior (2007), Rios (2013), Wang 
e Limare (2015), e Yuriy (2008) é apresentado no Apêndice B. Em tempo, resalienta-se 
que esse modelo computacional é, em suma, uma implementação PI matricial utilizando 
a linguagem C procedimental.  
 
 


236 
 
 
Apêndice B – Códigos de experimentos  
B. Códigos-fonte de experimentos 
B.1. Implementação do treinamento IRIS MLP em linguagem C 
01 
02 
03 
04 
05 
06 
07 
08 
09 
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
#include <stdio.h> 
#include <stdlib.h> 
#include <math.h> 
#include <string.h> 
#include <sys/time.h> 
 
#define numInputs 5 
#define numHidden 5 
#define numOutputs 3 
#define numPatterns 120 
 
const int numEpochs = 10000; 
const float minError = 0.009; 
const float LR = 0.1; 
const float alpha = 1; // momentum  
const float smallWT = 0.05; 
 
float randPatterns[numPatterns]; 
float weightsIH[numInputs][numHidden]; 
float weightsHO[numHidden][numOutputs]; 
float hiddenVal[numHidden]; 
float outputVal[numOutputs]; 
 
float hBiases[numHidden]; 
float oBiases[numOutputs]; 
float hSignals[numHidden]; 
float oSignals[numOutputs]; 
float hoGrads[numHidden][numOutputs]; 
float ihGrads[numInputs][numHidden]; 
float obGrads[numOutputs]; 
float hbGrads[numHidden]; 
float ihPrevWeightsDelta[numInputs][numHidden]; 
float hoPrevWeightsDelta[numHidden][numOutputs]; 
float hPrevBiasesDelta[numHidden]; 
float oPrevBiasesDelta[numOutputs]; 
 
float trainInputs[numPatterns][numInputs]; 
int trainOutputs[numPatterns][numOutputs]; 
 
float msePattern = 0.0; 
 
float hyperTan(float x){ 
    if (x < -20.0) { 
        return -1.0; 
    } else { 
        if (x > 20.0) { 
            return 1.0; 
        } else { 
            return tanh(x); 
        } 
    } 
} 


237 
 
 
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
 
void calcNet(int patNum){               // compute outputs 
    float hSums[numHidden]; 
    float oSums[numOutputs]; 
    float softSum = 0.0; 
    float errSum = 0.0; 
     
    for (int i = 0;i < numHidden;i++) hSums[i] = 0.0; 
    for (int i = 0;i < numOutputs;i++) oSums[i] = 0.0; 
     
    for (int j = 0;j < numHidden; j++){ 
        for (int i = 0;i < numInputs;i++){ 
            hSums[j] += trainInputs[patNum][i] * weightsIH[i][j]; 
        } 
        hSums[j] += hBiases[j];  
        hiddenVal[j] = hyperTan(hSums[j]); 
    } 
     
    for (int k = 0;k < numOutputs; k++){ 
        for (int j = 0;j < numHidden;j++){ 
            oSums[k] += hiddenVal[j] * weightsHO[j][k]; 
        } 
        oSums[k] += oBiases[k];  
        softSum += exp(oSums[k]);    // utilizado para a função softmax 
    } 
 
    // softmax and error 
    for (int k = 0;k < numOutputs;k++){ 
        outputVal[k] = exp(oSums[k]) / softSum; 
        errSum += (trainOutputs[patNum][k] - outputVal[k]) * 
(trainOutputs[patNum][k] - outputVal[k]); 
    } 
    msePattern += (0.5 * errSum); 
} 
 
void updateValues(int patNum){ 
    double delta = 0.0; 
     
    for (int k = 0;k < numOutputs;k++){ 
        oSignals[k] = (trainOutputs[patNum][k] - outputVal[k]) * (1 - 
outputVal[k]) * outputVal[k]; 
        for (int j = 0;j < numHidden;j++){ 
            hoGrads[j][k] = oSignals[k] * hiddenVal[j]; 
        } 
        obGrads[k] = oSignals[k] * 1.0; 
    } 
     
    for (int j = 0;j < numHidden;j++){ 
        float sum = 0.0; 
        for (int k = 0;k < numOutputs;k++){ 
            sum += oSignals[k] * weightsHO[j][k]; 
        } 
        hSignals[j] = (1 + hiddenVal[j]) * (1 - hiddenVal[j]) * sum; 
        for (int i = 0;i < numInputs;i++){ 
            ihGrads[i][j] = hSignals[j] * trainInputs[patNum][i]; 
        } 
        hbGrads[j] = hSignals[j] * 1.0; 
    } 
 
    for (int j = 0;j < numHidden;j++){ 


238 
 
 
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
123 
124 
125 
126 
127 
128 
129 
130 
131 
132 
133 
134 
135 
136 
137 
138 
139 
140 
141 
142 
143 
144 
145 
146 
147 
148 
149 
150 
151 
152 
153 
154 
155 
156 
157 
158 
159 
160 
161 
162 
163 
164 
165 
166 
167 
168 
169 
170 
171 
172 
        for (int i = 0;i < numInputs;i++){ 
            delta = ihGrads[i][j] * LR; 
            weightsIH[i][j] += delta; 
            weightsIH[i][j] += ihPrevWeightsDelta[i][j] * alpha; 
            ihPrevWeightsDelta[i][j] = delta; 
        } 
        delta = hbGrads[j] * LR; 
        hBiases[j] += delta; 
        hBiases[j] += hPrevBiasesDelta[j] * alpha; 
        hPrevBiasesDelta[j] = delta; 
    } 
     
    for (int k = 0;k < numOutputs;k++){ 
        for (int j = 0;j < numHidden;j++){ 
            delta = hoGrads[j][k] * LR; 
            weightsHO[j][k] += delta; 
            weightsHO[j][k] += hoPrevWeightsDelta[j][k] * alpha; 
            hoPrevWeightsDelta[j][k] = delta; 
        } 
        delta = obGrads[k] * LR; 
        oBiases[k] += delta; 
        oBiases[k] += oPrevBiasesDelta[k] * alpha; 
        oPrevBiasesDelta[k] = delta; 
    }     
} 
 
void initializeWeights(void){ 
    printf("Weights input-hidden: \n");     
    for (int j = 0;j < numHidden;j++){ 
        for (int i = 0;i < numInputs;i++){ 
            weightsIH[i][j] = smallWT * ((float)rand()/RAND_MAX) + 0.0001; 
            printf("%8.5f;",weightsIH[i][j]); 
        } 
        hBiases[j] = smallWT * ((float)rand()/RAND_MAX) + 0.0001; 
    } 
    printf("\nWeights hidden-output: \n"); 
    for (int k = 0;k < numOutputs;k++){ 
        for (int j = 0;j < numHidden;j++){ 
            weightsHO[j][k] = smallWT * ((float)rand()/RAND_MAX) + 0.0001; 
            printf("%8.5f;",weightsHO[j][k]); 
        } 
        oBiases[k] = smallWT * ((float)rand()/RAND_MAX) + 0.0001; 
    } 
    printf("\n"); 
} 
 
void randomPatterns(void){ 
    int aux = 0; 
    struct timeval tv; 
    gettimeofday(&tv, NULL); 
    int usec = tv.tv_usec; 
    srand48(usec); 
    for (int p = 0;p < numPatterns;p++){ 
        randPatterns[p] = p; 
    } 
    size_t p; 
    for (p = numPatterns - 1;p > 0;p--){ 
        size_t np = (unsigned int)(drand48()*(p+1)); 
        aux = randPatterns[np]; 
        randPatterns[np] = randPatterns[p]; 


239 
 
 
173 
174 
175 
176 
177 
178 
179 
180 
181 
182 
183 
184 
185 
186 
187 
188 
189 
190 
191 
192 
193 
194 
195 
196 
197 
198 
199 
200 
201 
202 
203 
204 
205 
206 
207 
208 
209 
210 
211 
212 
213 
214 
215 
216 
217 
218 
219 
220 
221 
222 
223 
224 
225 
226 
227 
228 
229 
230 
231 
232 
        randPatterns[p] = aux; 
    } 
} 
 
int getPattern(int totPat){ 
    printf("Training patterns: \n"); 
    FILE *file; 
    char text[40] = ""; 
    char *slice; 
    file = fopen("IrisData.txt","r"); 
    if (file == NULL){ 
        return 1; 
    } else { 
        for (int np = 0;np < totPat;np++){ 
            fscanf(file,"%s\n",&text); 
            slice = strtok(text,","); 
            for (int pos = 0;pos < (numInputs+numOutputs);pos++){ 
                if (pos < numInputs) {  
                    trainInputs[np][pos] = atof(slice); 
                    printf("%8.5f; ",trainInputs[np][pos]); 
                } else { 
                    trainOutputs[np][pos-numInputs] = atoi(slice); 
                    printf("%d; ",trainOutputs[np][pos-numInputs]); 
                } 
                slice = strtok(NULL,","); 
            } 
            printf("\n"); 
        } 
        fclose(file); 
    } 
    return 0; 
} 
 
int saveData(int ne, float oe) {     // ne - numEpochs; oe - OverallError 
    FILE *file; 
    char text[40] = ""; 
    char *slice; 
    file = fopen("ResData.txt","w+"); 
    if (file == NULL){ 
        return 1; 
    } else { 
        fprintf(file,"Epochs: %d; Overall Error: %f;\n",ne,oe); 
        fprintf(file,"Weights Input-Hidden (i,h) - (%d,%d): 
\n",numInputs,numHidden); 
        for (int j = 0;j < numHidden;j++) 
            for (int i = 0;i < numInputs;i++) 
                fprintf(file,"%f;",weightsIH[i][j]); 
 
        fprintf(file,"\nWeights Hidden Biases (%d): \n",numHidden); 
        for (int j = 0;j < numHidden;j++) 
            fprintf(file,"%f;",hBiases[j]); 
 
        fprintf(file,"\nWeights Hidden-Output (h,o) - (%d,%d): 
\n",numHidden,numOutputs); 
        for (int k = 0;k < numOutputs;k++) 
            for (int j = 0;j < numHidden;j++) 
                fprintf(file,"%f;",weightsHO[j][k]); 
 
        fprintf(file,"\nWeights Output Biases (%d): \n",numOutputs); 
        for (int k = 0;k < numOutputs;k++) 


240 
 
 
233 
234 
235 
236 
237 
238 
239 
240 
241 
242 
243 
244 
245 
246 
247 
248 
249 
250 
251 
252 
253 
254 
255 
            fprintf(file,"%f;",oBiases[k]); 
 
        fclose(file); 
    } 
    return 0;     
} 
 
int main(int argc, char** argv) { 
    int contEpochs = 0; 
    float overallError = 0.0; 
    srand(time(NULL)); 
    initializeWeights(); 
    getPattern(numPatterns); 
    do { 
        randomPatterns(); 
        for (int contPattern = 0;contPattern < numPatterns;contPattern++){ 
            calcNet(randPatterns[contPattern]); 
            updateValues(randPatterns[contPattern]); 
        } 
        overallError = msePattern / (double)numPatterns; 
        msePattern = 0.0; 
        contEpochs++; 
        printf("Overall error in epoch %5d: %10.5f;\n",contEpochs,overallError); 
    } while ((contEpochs <= numEpochs) && (overallError > minError)); 
    saveData(contEpochs,overallError); 
    return (EXIT_SUCCESS); 
}  
B.2. Implementação do treinamento IRIS MLP em LingPON 
01 
02 
03 
04 
05 
06 
07 
08 
09 
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
fbe Network 
    attributes 
       integer attNumEpochs 0 
 
 
integer attTotTrainInputs 0 
 
 
integer attReadTrainInputs 0 
 
 
integer attClock 0 
 
 
pfloat attRMSerror 0 
 
 
pfloat attLR 0.1 
       pfloat attInput0 0.0 
       pfloat attInput1 0.0 
       pfloat attInput2 0.0 
       pfloat attInput3 0.0 
        
        // saídas esperadas pela rede 
       pfloat attOutPred0 0.0 
       pfloat attOutPred1 0.0 
       pfloat attOutPred2 0.0 
         
        // valores reais de cada neurônio de saída 
       pfloat attOutput0 0.0 
       pfloat attOutput1 0.0 
       pfloat attOutput2 0.0 
 
 
 
 
 
pfloat attErrorPattern 0.0 
 
 
pfloat attErrorEpoch 0.0 
    end_attributes  
 
    methods 


241 
 
 
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
88 
89 
90 
       method mthNetStart() begin_method #include <iostream> <def>using 
namespace std;</def> cout << "mth Net Start" << endl; attClock = 1<N>; 
attReadTrainInputs = 0<R>; end_method 
 
 
method mthNetGetValues() begin_method #include <iostream> <def>using 
namespace std;</def> cout << "mth Net GetValues" << endl; attClock = 2; 
end_method 
 
 
method mthNetRaiseEpoch() begin_method #include <iostream> <def>using 
namespace std;</def> cout << "mth Net RaiseEpochs" << endl; attNumEpochs = 
attNumEpochs-1; end_method 
 
 
method mthNetNeuronsHDone() begin_method #include <iostream> <def>using 
namespace std;</def> cout << "mth Net NHDone" << endl; attClock = 10; 
hidneu0.attDone = false; hidneu1.attDone = false; hidneu2.attDone = false; 
hidneu3.attDone = false; hidneu4.attDone = false; attClock = 3; end_method 
 
 
method mthNetSetOutputNeurons() begin_method #include <iostream> <def>using 
namespace std;</def> cout << "mth Net Setout" << endl; attErrorPattern = 0.0; 
attClock = 4; end_method 
 
 
method mthNetNeuronsODone() begin_method #include <iostream> <def>using 
namespace std;</def> cout << "mth Net NODone" << endl; attClock = 10; 
outneu0.attDone = false; outneu1.attDone = false; outneu2.attDone = false; 
attOutput0 = outneu0.attNOOutput; attOutput1 = outneu1.attNOOutput; attOutput2 = 
outneu2.attNOOutput; attClock = 5; end_method 
 
 
method mthNetCalcOverallError() begin_method #include <iostream> <def>using 
namespace std;</def> cout << "mth Net CalcError" << endl; attReadTrainInputs = 
attReadTrainInputs + 1; end_method 
    end_methods 
end_fbe 
 
fbe NeuronHidden 
 
attributes 
 
 
pfloat attBias 0.0 
 
 
pfloat attNHOutput 0.0 
 
 
pfloat attDerivative 0.0  
 
 
boolean attDone false 
       pfloat attIHWeight0 0.0  // entrada 0 escondida 0 
       pfloat attIHWeight1 0.0  // entrada 1 escondida 0 
       pfloat attIHWeight2 0.0  // entrada 2 escondida 0 
       pfloat attIHWeight3 0.0  // .... 
 
end_attributes 
 
methods 
 
 
method mthNHCalcHidden() begin_method  
 
 
#include <math.h>  
 
 
#include <iostream>  
 
 
<def>using namespace std;</def>  
 
 
cout << "mth Neuhidcalc" << endl;  
 
 
double sumOfProducts = 0.0;  
 
 
sumOfProducts = 
(net.attInput0*attIHWeight0)+(net.attInput1*attIHWeight1)+(net.attInput2*attIHWe
ight2)+(net.attInput3*attIHWeight3);  
 
 
attNHOutput = tanh(sumOfProducts);  
 
 
attDerivative = 1.0 - (attNHOutput * attNHOutput); attDone = true; 
end_method 
 
end_methods 
end_fbe 
 
fbe NeuronOutput 
 
attributes 
 
 
pfloat attBias 0.0 
 
 
pfloat attNOOutput 0.0 
 
 
pfloat attLocalError 0.0 
 
 
pfloat attGradient 0.0 


242 
 
 
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
123 
124 
125 
126 
127 
128 
129 
130 
131 
132 
133 
134 
135 
136 
137 
138 
139 
140 
141 
142 
143 
144 
145 
146 
147 
148 
149 
150 
 
 
pfloat attOutPred 0.0  
 
 
boolean attDone false 
       pfloat attHOWeight0 0.0 // escodida 0 saída 0 
       pfloat attHOWeight1 0.0 // escodida 1 saída 0 
       pfloat attHOWeight2 0.0 // escodida 2 saída 0 
       pfloat attHOWeight3 0.0 // ...  
 
       pfloat attHOWeight4 0.0 
 
end_attributes 
 
 
 
methods 
 
 
method mthNOCalcOutput() begin_method #include <math.h> #include <iostream> 
<def>using namespace std;</def> cout << "mth Neuoutcalc" << endl; double 
sumOfProducts = 0.0; double derivative = 0.0; sumOfProducts = 
(hidneu0.attNHOutput*attHOWeight0)+(hidneu1.attNHOutput*attHOWeight1)+(hidneu2.a
ttNHOutput*attHOWeight2)+(hidneu3.attNHOutput*attHOWeight3)+(hidneu4.attNHOutput
*attHOWeight4); attNOOutput = tanh(sumOfProducts); attLocalError = attOutPred - 
attNOOutput; derivative = 1.0 - (attNOOutput * attNOOutput); attGradient = 
derivative * attLocalError; net.attErrorPattern += fabs(attLocalError); attDone 
= true; end_method 
 
end_methods 
end_fbe 
 
inst 
 
Network net 
 
NeuronHidden hidneu0, hidneu1, hidneu2, hidneu3, hidneu4 
 
NeuronOutput outneu0, outneu1, outneu2 
end_inst 
 
strategy 
 
no_one 
end_strategy 
 
rule rleNetStart 
 
condition 
 
  subcondition sbcNetStart 
 
 
 premise preNetStart net.attNumEpochs > 0 
 
  end_subcondition 
 
end_condition 
 
action 
 
  instigation insNetStart net.mthNetStart(); 
 
end_action 
end_rule 
 
rule rleNetGetValues 
 
condition 
 
  subcondition sbcNetGetValues 
 
 
 premise preNetGetValues net.attReadTrainInputs < net.attTotTrainInputs 
 
  end_subcondition 
 
end_condition 
 
action 
 
  instigation insNetGetValues net.mthNetGetValues(); 
 
end_action 
end_rule 
 
rule rleNetRaiseEpoch 
 
condition 
 
  subcondition sbcNetRaiseEpoch 
 
 
 premise preNetRaiseEpoch net.attReadTrainInputs >= net.attTotTrainInputs 
and 
 
 
 premise preNetRaiseEpochC net.attClock == 5 


243 
 
 
151 
152 
153 
154 
155 
156 
157 
158 
159 
160 
161 
162 
163 
164 
165 
166 
167 
168 
169 
170 
171 
172 
173 
174 
175 
176 
177 
178 
179 
180 
181 
182 
183 
184 
185 
186 
187 
188 
189 
190 
191 
192 
193 
194 
195 
196 
197 
198 
199 
200 
201 
202 
203 
204 
205 
206 
207 
208 
209 
210 
 
  end_subcondition 
 
end_condition 
 
action 
 
  instigation insNetRaiseEpoch net.mthNetRaiseEpoch(); 
 
end_action 
end_rule 
 
rule rleNetNeuronsHDone 
 
condition 
 
  subcondition sbcNetNeuronsHDone 
 
 
 premise preNetNeuronsHDone0 hidneu0.attDone == true and  
 
 
 premise preNetNeuronsHDone1 hidneu1.attDone == true and 
 
 
 premise preNetNeuronsHDone2 hidneu2.attDone == true and 
 
 
 premise preNetNeuronsHDone3 hidneu3.attDone == true and 
 
 
 premise preNetNeuronsHDone4 hidneu4.attDone == true 
 
  end_subcondition 
 
end_condition 
 
action 
 
  instigation insNetNeuronsHDone net.mthNetNeuronsHDone(); 
 
end_action 
end_rule 
 
rule rleNetSetOutputNeurons 
 
condition 
 
  subcondition sbcNetSetOutputNeurons 
 
 
 premise preNetSetOutputNeurons net.attClock == 3 
 
  end_subcondition 
 
end_condition 
 
action 
 
  instigation insNetSetOutputNeurons net.mthNetSetOutputNeurons(); 
 
end_action 
end_rule 
 
rule rleNetNeuronsODone 
 
condition 
 
  subcondition sbcNetNeuronsODone 
 
 
 premise preNetNeuronsODone0 outneu0.attDone == true and  
 
 
 premise preNetNeuronsODone1 outneu1.attDone == true and 
 
 
 premise preNetNeuronsODone2 outneu2.attDone == true 
 
  end_subcondition 
 
end_condition 
 
action 
 
  instigation insNetNeuronsODone net.mthNetNeuronsODone(); 
 
end_action 
end_rule 
 
rule rleNetCalcOverallError 
 
condition 
 
  subcondition sbcNetCalcOverallError 
 
 
 premise preNetCalcOverallError net.attClock == 5 
 
  end_subcondition 
 
end_condition 
 
action 
 
  instigation insNetCalcOverallError net.mthNetCalcOverallError(); 
 
end_action 
end_rule 
 
formRule rleNHCalcHidden 
 
condition 
 
  subcondition sbcNHCalcHidden 


244 
 
 
211 
212 
213 
214 
215 
216 
217 
218 
219 
220 
221 
222 
223 
224 
225 
226 
227 
228 
229 
230 
231 
232 
233 
234 
235 
236 
237 
238 
239 
240 
241 
242 
243 
244 
245 
246 
247 
248 
 
 
 premise preNHCalcHidden NeuronHidden.attDone == false and 
 
 
 premise preNHCalcHiddenF Network.attClock == 2 
 
  end_subcondition 
 
end_condition 
 
action 
 
  instigation insNHCalcHidden NeuronHidden.mthNHCalcHidden(); 
 
end_action 
end_formRule 
 
formRule rleNOCalcOutput 
 
condition 
 
  subcondition sbcNOCalcOutput 
 
 
 premise preNOCalcOutput NeuronOutput.attDone == false and 
 
 
 premise preNOCalcOutputF Network.attClock == 4 
 
  end_subcondition 
 
end_condition 
 
action 
 
  instigation insNOCalcOutput NeuronOutput.mthNOCalcOutput(); 
 
end_action 
end_formRule 
 
main {  
 
hidneu0_attDone::setValue(false, _NOPAdds::RENOTIFY); 
 
hidneu1_attDone::setValue(false, _NOPAdds::RENOTIFY); 
 
hidneu2_attDone::setValue(false, _NOPAdds::RENOTIFY); 
 
hidneu3_attDone::setValue(false, _NOPAdds::RENOTIFY); 
 
hidneu4_attDone::setValue(false, _NOPAdds::RENOTIFY); 
 
outneu0_attDone::setValue(false, _NOPAdds::RENOTIFY); 
 
outneu1_attDone::setValue(false, _NOPAdds::RENOTIFY); 
 
outneu2_attDone::setValue(false, _NOPAdds::RENOTIFY); 
 
net_attReadTrainInputs::setValue(0, _NOPAdds::NO_NOTIFY); 
 
net_attTotTrainInputs::setValue(1, _NOPAdds::NO_NOTIFY); 
 
 
 
for (int i = 0; i < 2; i++) { 
 
 
net_attNumEpochs::setValue(1); 
 
 
printf("iteração: %05d\n",i); 
 
} 
} 
 
 


245 
 
 
Apêndice C – Código XML – arquivo description.xml 
<?xml version="1.0" encoding="UTF-8"?> 
  <description xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xsi:noNamespaceSchemaLocation="file:///C:/Users/FernandoSchutz/Dropbox/progc/XMLRead
er/description.xsd"> 
    <identifier></identifier> 
    <metadata> 
      <paradigm>classification</paradigm> 
      <name>Backpropagation Classification</name> 
      <description>Iris Classfication Example</description> 
    </metadata> 
    <creator> 
      <name>Schutz</name> 
      <contact>fernando@utfpr.edu.br</contact> 
    </creator> 
    <problemDomain> 
      <propagationType type="feedforward"> 
      <learningType>supervised</learningType> 
      </propagationType> 
      <applicationField>Classification</applicationField> 
      <networkType>Backpropagation</networkType> 
      <problemType>Classifiers</problemType> 
    </problemDomain> 
    <endpoints> 
      <train>true</train> 
      <retrain>true</retrain> 
      <evaluate>true</evaluate> 
    </endpoints> 
    <executionEnvironment> 
      <parallel> 
        <hardware> 
          <special /> 
        </hardware> 
      </parallel>  
    </executionEnvironment> 
    <structure> 
      <input> 
 
 
  <ID>Input1</ID> 
 
 
  <dimension> 
 
 
 
<min>2</min> 
 
 
 
<max>2</max> 
 
 
  </dimension> 
 
 
  <size> 
 
 
 
<min>1</min> 
 
 
 
<max>1</max> 
 
 
  </size> 
      </input> 
      <hidden> 
        <ID>Hidden1</ID> 
        <dimension> 
          <min>2</min> 
          <max>2</max> 
        </dimension> 
        <size> 
          <min>1</min> 
          <max>1</max> 
        </size> 


246 
 
 
      </hidden> 
      <output> 
        <ID>Output1</ID> 
        <dimension> 
          <min>1</min> 
          <max>1</max> 
        </dimension> 
        <size> 
          <min>1</min> 
          <max>1</max> 
        </size> 
      </output> 
      <connections>fullconnected</connections> 
    </structure> 
    <parameters> 
      <valueparameter name="learningrate">10</valueparameter> 
      <comboparameter name="activationfunction">tanh</comboparameter> 
      <valueparameter name="epochs">500</valueparameter> 
      <valueparameter name="seed">6</valueparameter> 
    </parameters> 
    <data> 
      <description>iris file, 3 classes, 4 inputs</description> 
      <filedescription>name/iris.txt</filedescription> 
    </data> 
  </description> 
 
 
 


247 
 
 
 
Apêndice D – Linguagens de Descrição de RNA 
 


#Net para Microsoft Azure 
Com o intuito de permitir o desenvolvimento de RNA, a empresa Microsoft criou 
a linguagem #Net que é uma linguagem utilizada para definir arquiteturas de RNA para 
módulos de RNA em Aprendizado de Máquina do Microsoft Azure (TAKAKI, 2016). 
Microsoft Azure é uma plataforma destinada à execução de aplicativos e serviços, 
baseada nos conceitos da computação em nuvem, lançada em 2008 pela empresa.  
De acordo com Takaki (2016), alguns requisitos básicos devem ser cumpridos 
para que se possa utilizar tal linguagem: 
• A RNA deve ter uma camada de saída, pelo menos uma camada de entrada, 
sendo as camadas ocultas opcionais; 
• Em cada camada deve se definir um número fixo de nós (neurônios), 
arranjados em uma matriz retangular de dimensões arbitrárias; 
• Camadas ocultas (se houverem) e de saída têm parâmetros treinados 
associados, sendo estes os pesos sinápticos e bias; 
• A origem de um neurônio deve ser diferente do seu destino, sendo que 
conexões são acíclicas, ou seja, não pode haver conexões onde o destino é 
o neurônio de origem (inicial); 
Na linguagem #Net, a especificação de estrutura de uma RNA é composta por 
três seções: a declaração de constantes, a declaração de camada e a declaração de 
conexão. A seção de declaração de constantes é opcional, porém as de declaração de 
camadas e de conexões são seções necessárias para a especificação da RNA. A Figura 
1 apresenta um exemplo simples para a criação de uma RNA em #Net. 
01 
02 
03 
04 
  Const { bInput = 200; bOutput = 4; }   
  input Data auto; 
  hidden H [bInput] from Data all; 
  output Out [bOutput] tanh from H all;   
Figura 1 - Azure #Net: modelo de RNA com uma camada oculta (Adaptado de Takaki, 2016) 
O exemplo da Figura 1 define, na sua linha 01, duas constantes, bInput e 
bOutput, utilizadas para informar o tamanho das camadas de entrada e saída 
respectivamente. Na linha 02 é definida a camada de entrada denominada Data, sendo 


que a palavra chave auto indica que a quantidade de neurônios é a mesma que 
quantidade de dados disponíveis para a RNA, ou seja, depende direta e 
automaticamente dos padrões de entrada informados. Na linha 03, é definida a camada 
oculta chamada H, contendo duzentos (200) neurônios, totalmente conectada à camada 
de entrada. Já na quarta linha, a camada de saída, denominada O, é definida, e contém 
quatro (4) neurônios de saída (uma camada de saída por classe). A palavra-chave tanh 
indica a função de ativação que será aplicada aos neurônios da camada de saída, sendo 
neste caso a função tangente hiperbólica.  
O exemplo da Figura 2 apresenta um modelo de RNA com múltiplas camadas. 
01 
02 
03 
04 
05 
06 
07 
08 
09 
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
  // Define as camadas de entrada 
  input Pixels [10, 20]; 
  input MetaData [7]; 
 
  // Define as primeiras duas camadas escondidas, usando apenas dados da entrada Pixels 
  hidden ByRow [10, 12] from Pixels where (s,d) => s[0] == d[0]; 
  hidden ByCol [5, 20] from Pixels where (s,d) => abs(s[1] - d[1]) <= 1; 
 
  // Define a terceira camada escondida, usando os dados das camadas ByRow e ByCol 
  hidden Gather [100]  
  { 
    from ByRow all; 
    from ByCol all; 
  } 
 
  // Define a camada de saída e suas fontes de dados 
  output Result [10]   
  { 
    from Gather all; 
    from MetaData all; 
  }    
Figura 2 - Azure #Net: modelo de RNA com várias camadas (Adaptado de Takaki, 2016) 
Na Figura 2, o modelo de RNA apresenta seis camadas: duas camadas de 
entrada (input – linhas 02 e 03), três camadas escondidas (hidden - da linha 06 à 14), e 
uma camada de saída (output - linha 17).  
Nos dois exemplos, tanto da Figura 1 quanto da Figura 2, os pesos sinápticos 
não foram definidos, pois são gerados automaticamente, de forma aleatória. 
Opcionalmente, a especificação de um conjunto de pesos pode ser realizada. utilizando 
o atributo Weights, cuja valoração deve ser uma tupla de valores de pontos flutuantes 
com um comprimento correspondente ao número de conexões definidas no algoritmo.  


Isto posto, tem se que, mesmo utilizada pela Microsoft para projetos de 
aprendizado de máquina e aplicativos que vão de reconhecimento de imagem a análise 
de texto, a linguagem Net# para personalizar a arquitetura de RNA apresenta-se como 
um exemplo plausível para a descrição de RNA, podendo ser utilizada como base para 
este trabalho.  
iXCSL (eXtensible Soft Computing Language) 
O iXSCL (eXtensible Soft Computing Language) é um vocabulário, especificado 
no padrão de linguagem de marcação extensível (eXtensible Markup Language - XML), 
para a especificação de objetos comuns na área de Inteligência Computacional (união 
de sistemas Fuzzy e sistemas baseados em RNA) (BERAN et al., 2008). Assim, tal 
vocabulário descreve a arquitetura como um conjunto de camadas interconectadas, onde 
cada camada é um conjunto de nós de processamento interconectados que podem ser 
neurônios artificiais e nós de polarização (bias).  
Para definição de uma RNA, deve-se informar as camadas, parâmetros, fluxos 
de sinais dentro e entre as camadas, e um critério de parada especificando o término do 
cálculo. A Figura 3 demonstra o esquema para a descrição de uma RNA do tipo Hopfield, 
utilizando o vocabulário iXSCL. 
 
01 
02 
03 
04 
05 
06 
07 
08 
09 
10 
11 
12 
13 
14 
15 
16 
17 
// Definição de uma RNA 
<neuralNetwork name=" "> Hopﬁeld 
  <parameters> 
    <input name="input-vector" type="/sensors/NoiseSample"/> 
    <output name="output-vector" type="/levels/NoiseLevel"/> 
  </parameters> 
  <networkLayers> 
    <layer id="lattice" nInputs="3" nOutputs="3">  
      <!-- deﬁnition of this layer --> 
    </layer> 
  </networkLayers> 
  <signalFlow> 
    <inputs node="lattice">i1 i2 i3</inputs> 
    <outputs>lattice:o1 lattice:o2 lattice:o3</outputs> 
  </signalFlow> 
  <stopCriterion xsi:type="stability"/> 
</neuralNetwork> 
Figura 3 - Vocabulário iXSCL: definição de uma RNA (Adaptado de Souto, 2003) 


Quanto à definição de neurônios, o esquema iXSCL define dois tipos de nó de 
processamento: o neurônio artificial clássico e um nó de bias. O node (nó) do tipo 
nonLinearNeuronNode possui uma função de ativação, pesos e tags nomeadas 
opcionais que podem ser usados para associar atributos ao neurônio. Os nós de 
polarização (bias), por sua vez, fornecem uma saída constante de um determinado valor 
real. Os nós são definidos dentro de uma camada, que também descreve o conjunto de 
conexões entre eles. A Figura 4 apresenta o vocabulário para a definição de uma 
camada. 
01 
02 
03 
04 
05 
06 
07 
08 
09 
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
// Definição de uma camada 
<layer id="lattice" nInputs="3" nOutputs="3" model="asynchronous">  
  <processingNodes> 
    <node id="n1" xsi:type="nonLinearNeuronNode" nInputs="5"> 
      <activationFunction xsi:type="thresholdActivationFunction"> 
        <min>0.0</min> 
        <max>1.0</max> 
      </activationFunction> 
      <weights> 
        0.123124124 0.259528285 0.87721231 0.1928123 0.12938241 
      </weights> 
      <tags> 
        <tag name="label">Class A1</tag> 
      </tags> 
    </node>  
    <!-- other nodes: n2, n3 -->  
  </processingNodes> 
  <signalFlow> 
    <inputs node="n1">i1 i2 i3 n2 n3</inputs> 
    <inputs node="n2">i1 i2 i3 n1 n3</inputs> 
    <inputs node="n3">i1 i2 i3 n1 n2</inputs> 
    <outputs>o1 o2 o3</outputs> 
  </signalFlow> 
</layer> 
Figura 4 - Vocabulário iXSCL: definição de uma camada de RNA (Adaptado de Souto, 2003) 
A Figura 4 demonstra a definição de uma camada em iXSCL. Os nós são 
definidos dentro de uma camada por meio do elemento node (linha 04), declarando a 
função de ativação (linha 05), os pesos (linha 09) e possíveis tags (linha 12). O elemento 
signalFlow (linha 18) declara onde estão as entradas de cada nó e quais nós fornecem 
as saídas da camada. Para definição das entradas, in representa a n-ésima entrada da 
camada, on a n-ésima saída e id a identificação de um nó de saída. 


Pode-se concluir, portanto, que o vocabulário iXSCL é útil para definir uma RNA. 
No entanto, este modelo não possui suporte às operações de treinamento ou teste de 
uma RNA: apenas fornece as informações necessárias para permitir o processamento 
de saídas, dado um conjunto de entradas (SOUTO, 2003). 
NXML (Neural XML) 
Neural XML (NXML) é uma linguagem baseada em XML para criar, treinar e 
executar RNA. Incorporada em uma biblioteca da linguagem .NET chamada BrainNet, a 
linguagem NXML permite gerar, salvar e carregar RNA de e para arquivos XML 
(Madhusudanan, 2016). Por meio do uso do arquivo do esquema XML da rede 
(network.xsd) pode se descrever uma RNA fornecendo o número de neurônios por 
camada, número de camadas, conexões, entradas e pesos sinápticos. A definição de 
tipos de dados, fontes e o local de armazenamento dos dados deve ser efetuada no 
esquema XML neural (NeuraIXML.xsd). 
Para utilizar adequadamente a linguagem NXML na construção da estrutura de 
uma RNA todos os neurônios devem ser definidos. Assim, visando facilitar o processo 
de criação de tal descrição, o projeto em código binário é disponibilizado em 
Madhusudanan (2016) para a geração automática de RNA e seu treinamento. A Figura 
5 demonstra o comando para a geração de uma RNA com três camadas, contendo dois 
neurônios na primeira camada, dois neurônios na segunda e um neurônio da terceira 
camada, sendo que o resultado será gravado no arquivo gate.xml. 
 
 C:\BrainNet\Nxml\Bin>nxml -gen 2,2,1 gate.xml 
Figura 5 - Linguagem NXML: comando para criação de RNA (Adaptado de Madhusudanan, 2016) 
Seguindo a estrutura do esquema XML network.xsd, a RNA gerada pelo 
comando demonstrado na Figura 5 é apresentada na Figura 6. 
01 
02 
03 
04 
05 
06 
<code><?xml version="1.0" encoding="utf-8"?> 
<Network> 
  <Layer Name="Layer0"> 
    <Neuron Name="L0N0"> 
      <Bias>0.7982105016708374</Bias> 
      <Output>0</Output> 


07 
08 
09 
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
      <Delta>0</Delta> 
    </Neuron> 
    <Neuron Name="L0N1"> 
      <Bias>-0.3051917552947998</Bias> 
      <Output>0</Output> 
      <Delta>0</Delta> 
    </Neuron> 
  </Layer> 
  <Layer Name="Layer1"> 
    <Neuron Name="L1N0"> 
      <Bias>-0.74571740627288818</Bias> 
      <Output>0</Output> 
      <Delta>0</Delta> 
      <Connections> 
        <Input Layer="0" Neuron="1" Weight="0.25023746490478516" /> 
        <Input Layer="0" Neuron="0" Weight="-0.68162941932678223" /> 
      </Connections> 
    </Neuron> 
    <Neuron Name="L1N1"> 
      <Bias>0.044701099395751953</Bias> 
      <Output>0</Output> 
      <Delta>0</Delta> 
      <Connections> 
        <Input Layer="0" Neuron="1" Weight="-0.41200506687164307" /> 
        <Input Layer="0" Neuron="0" Weight="-0.14756286144256592" /> 
      </Connections> 
    </Neuron> 
  </Layer> 
  <Layer Name="Layer2"> 
    <Neuron Name="L2N0"> 
      <Bias>-0.32655441761016846</Bias> 
      <Output>0</Output> 
      <Delta>0</Delta> 
      <Connections> 
        <Input Layer="1" Neuron="1" Weight="-0.9166187047958374" /> 
        <Input Layer="1" Neuron="0" Weight="-0.4252774715423584" /> 
      </Connections> 
    </Neuron> 
  </Layer> 
</Network> 
Figura 6 - Linguagem NXML: arquivo de descrição da RNA de exemplo gate.xml (Adaptado de Madhusudanan, 2016) 
Na Figura 6, sob a tag raiz Network, são definidas as camadas da RNA, por meio 
de tags Layer. Assim, observa-se que a RNA ilustrada consiste em três camadas, Layer0, 
Layer1 e Layer2. Dentro de cada dos elementos que representam a camada, são 
declarados os neurônios, contendo valores de bias, saída e delta, bem como suas 
conexões de entrada com a camada anterior. Em cada entrada são especificados os 


pesos sinápticos, por meio do atributo Weight. No exemplo ilustrado, todos os valores 
são gerados aleatoriamente. 
No esquema XML NeuraIXML.xsd os valores para o treinamento podem ser 
definidos. Além disso, parâmetros informados definem se a rede deve ser treinada 
(atributo Type = “Train”) ou executada (atributo Type = “Run”). No caso da execução de 
um treinamento, o número de iterações pode ser especificado no atributo TrainCount. 
Quanto aos dados, a linguagem NXML suporta padrões, números, matrizes e caracteres 
como tipos de entrada e saída, devendo estes serem especificados no parâmetro 
PatternData. Pode se especificar um arquivo de imagem por meio do parâmetro 
ImageData, tendo como entrada suas dimensões (largura x altura), bem como o tipo de 
saída de dados a ser gerada. 


255 
 
 
 
Anexo A - Manual da Linguagem PON - LINGPON 
A. Manual 
 
Este anexo apresenta o relatório final para a disciplina de Linguagens e 
Compiladores do programa de Pós-Graduação em Computação Aplicada da 
Universidade Tecnológica Federal do Paraná, no ano de 2015 e ministrada por Prof. 
Dr. João Alberto Fabro e Prof. Dr. Jean Marcelo Simão. 
 Este trabalho corresponde às adaptações a respeito da linguagem e 
compilador PON na versão 1.2 e foi desenvolvido pelos alunos: 
Fernando Schütz 
Leonardo Araujo Santos 
Leonardo Faix Pordeus 
Luís Guilherme Bergamini Mendes 
Ricardo Kerschbaumer 
Com o auxílio de Adriano Francisco Ronszcka 
 
 
 


256 
 
 
A.1. Introdução 
 
O Paradigma Orientado a Notificações (PON) é uma nova abordagem para o 
desenvolvimento de sistemas computacionais de maneira mais eficiente quando 
comparado a sistemas baseados em paradigmas tradicionais, como a Programação 
Procedimental e a Programação Orientada a Objetos (POO) do Paradigma Imperativo 
(PI), assim como os Sistemas baseados em Regras (SBR) do paradigma declarativo 
(PD) (SIMÃO; STADZISZ, 2008) (BANASZEWSKI, 2009). 
O PON propõe uma solução para os problemas destes paradigmas, que 
apresentam deficiências com relação a redundâncias estruturais, temporais e forte 
acoplamento entre suas entidades, diminuindo o desempenho e gerando maior 
dificuldade de paralelização e distribuição. Tais vantagens são constituídas por uma 
maior facilidade na concepção de sistemas que apresentem paralelismo ou distribuição, 
além da redução ou eliminação de alguns dos problemas clássicos de software PI e 
PD, tais como redundâncias de execução e acoplamento excessivo entre entidades 
computacionais (SIMÃO; STADZISZ, 2008) (BANASZEWSKI, 2009). 
Para o desenvolvimento de softwares fazendo uso do PON, primeiramente 
foram realizadas pesquisas com Framework C++ (BANASZEWSKI, 2009) e uma 
segunda versão otimizada do Framework C++ (RONSZCKA, 2012), permitindo a 
criação de softwares PON sob abordagem de POO. Porém nessas abordagens há um 
elevado uso de estruturas de dados, como lists, vectors, hashs, entre outras, que 
degradam o desempenho das aplicações construídas sobre o conceito do PON. Assim, 
observou-se a necessidade de desenvolvimento de um compilador e de uma linguagem 
específica para o PON, denominada LingPon. 
Outras pesquisas também exploraram a implementação do PON em hardware 
com uso de lógica reconfigurável (SIMÃO et al, 2012b) seguindo os conceitos do PON. 
Peters (2012) propôs a implementação em lógica reconfigurável de um co-processador 
PON (CoPON), uma solução híbrida, na qual a parte da aplicação responsável pelo 
processamento factual é executada em um núcleo von Neumann e a parte da aplicação 
responsável pelo cálculo lógico-causal e propagação de notificações é executada por 
meio de um co-processador baseado nos princípios do PON. Outrossim, uma 
arquitetura de processador foi desenvolvida de acordo com o modelo do PON, sendo 
denominada Notification-Oriented Computer Architecture (NOCA) (LINHARES,2015). 
O trabalho da disciplina de linguagens e compiladores teve como objetivo dar 
continuidade a linguagem LingPon. A primeira versão do LingPon foi materializada na 
disciplina Linguagens e Compiladores no ano de 2014 e aprimorada por (FERREIRA, 


257 
 
 
2015) em sua dissertação de mestrado. Em sua primeira versão foi concebida uma 
gramática própria, definida por uma BNF (Backus Normal Form) e com as ferramentas 
flex e bison. A Figura 1 apresenta um diagrama de blocos da estrutura da primeira 
versão do compilador. Na qual, é composto por um código escrito na linguagem 
LingPon, que representa a aplicação, o compilador e três possíveis códigos 
intermediários (C, C++ e Framework ). 
 
 
Figura 1 - Diagrama de Blocos LingPon 
 
Para a disciplina Linguagens e Compiladores de 2015 foram acrescentadas 
novas funcionalidades à linguagem, como regras de formação, compilação para 
Notification Oriented Computer Architecture (NOCA) (LINHARES, 2015), VHDL e uma 
nova versão C++, na qual é gerado um código seguindo os conceitos do PON de forma 
estática. 
 
 
A.2. Linguagem Atual 
A.2.1. 
Pré Requisitos e Instalação 
Para o desenvolvimento do compilador é necessário instalar previamente os 
analisadores léxicos e semânticos, que são as ferramentas Flex/Lex e Bison. Para a 


258 
 
 
sua compilação também é necessário configurar o compilador g++. No Windows o 
compilador 
pode 
ser 
configurado 
através 
da 
ferramenta 
cygwin 
(https://cygwin.com/install.html) 
(Tutorial 
de 
instalação 
do 
cygwin: 
http://cs.calvin.edu/curriculum/cs/112/resources/installingEclipse/cygwin/ 
Marcar 
a 
opção de instalação do Flex e Bison). 
Não existe no momento um instalador do compilador. Para sua utilização é 
necessário primeiramente, realizar o check-out do projeto no servidor svn disponível no 
seguinte 
endereço 
(https://200.134.17.9/svn/NOP/NOP_Compilador/NOP_v2015/). 
Após realizar o check-out do projeto é necessário seguir o processo abaixo (no 
Windows, através do cygwin) para realizar a sua compilação. 
 
flex lex_pon.l 
bison -d bison_pon.y 
g++ lex.yy.c bison_pon.tab.c *.cpp -o pon 
 
A.2.2. 
Linguagem PON 
A linguagem PON pode ser dividida em cinco partes, sendo: 
 Declaração de FBE´s; 
 Instâncias dos FBE´s; 
 Estratégias de escalonamento; 
 Definição das Rules; 
 Definição da função Main do programa. 
O Algoritmo a seguir apresenta o código referente a estrutura básica de um 
programa escrito na linguagem PON. 
 
 
 
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
fbe Apple 
   . . . 
end_fbe 
 
fbe Archer 
   . . . 
end_fbe 
 
---------------- 
 
inst 


259 
 
 
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
 
O Algoritmo a seguir apresenta o exemplo de código para criação de um FBE. 
 
 
Algoritmo 2: Exemplo de criação de FBE 
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
fbe Archer 
    Attributes 
        boolean atHasFired false 
    end_Attributes 
 
 
    Methods 
        method mtFire(atHasFired = true) 
        method mtInnerCode() begin_method cout << "" << endl; 
end_method 
    end_Methods 
end_fbe 
 
O Algoritmo a seguir demonstra como declarar instâncias dos FBE’s. 
 
 
Algoritmo 3: Exemplo de instanciações de FBE 
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
 
 


260 
 
 
 
 
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
 
A.2.3 Tipos de atributos do PON 
Os tipos de atributos permitidos na linguagem PON são: 
 boolean 
 integer 
 string 
 


261 
 
 
 char 
 pfloat 
Além desses tipos atributos, é possível realizar a composição de um FBE. O 
algoritmo a seguir apresenta como realizar a composição em um FBE. 
 
A.2.3. 
Compilando 
Para compilar e executar um programa utilizando o compilador PON é 
necessário executar os seguintes passos: 
 
1. Crie o programa PON conforme exemplificado anteriormente e salve em um arquivo 
de código fonte preferencialmente com a extensão .pon; 
2. Execute o processo de criação do compilador PON (pon em Linux e pon.exe em 
Windows). Veja etapa de geração do compilador. 
3. Execute o comando abaixo: 
./pon 1 < nome_do_programa.pon (Linux) 
./pon.exe 1 < nome_do_programa.pon (Windows) 
 
O comando descrito no passo três é composto pela chamada de execução do 
compilador PON criado com o nome pon. São necessários dois argumentos para 
executar o processo de compilação. O primeiro argumento é a opção de geração de 
código intermediário que varia de 1 a 7.  
1. C; 
2. C++; 
3. Framework ; 
4. Pré-Compilador; 
5. NOCA; 
6. Static C++; 
7. VHDL; 
Já o segundo argumento atribui o código fonte inserido no arquivo 
nome_do_programa.pon e irá criar o código intermediário PON conforme opção 
selecionada. 


262 
 
 
Obs: vale ressaltar que o código intermediário gerado será criado na pasta 
compiladosc para o código intermediário em C, cppcompilados para o código 
intermediário em C++ ou Static C++, compilados para código intermediário em 
Framework, nopcompilados para a opção do pré-compilador, nocacompilados para 
código NOCA e VHDLcompilados para código intermediário VHDL. 
 
A.2.4. 
Regras de Formação 
O conceito de Regras de Formação ou Formation Rules foi proposto por 
(SIMÃO, 2001; SIMÃO, STADZISZ e KÜNZLE,2003) para permitir a criação de Rules 
específicas, a partir da representação genérica de uma Rule. Este conceito é bastante 
útil quando o conhecimento causal de uma Rule é comum para diferentes conjuntos de 
instâncias de FBE, ou seja, um conjunto de Rules específicas se diferencia apenas nas 
instâncias referenciadas.  
Um exemplo do uso das Regras de Formação é em cenário de simulação de 
um conjunto de semáforos. Cada semáforo da simulação possui o mesmo conjunto de 
regras, se diferenciando apenas na instância declarada. Caso ocorra uma simulação 
com um número elevado de semáforos, seria necessário replicar as regras 
manualmente para cada instância declarada. Tornando o processo de desenvolvimento 
muito trabalhoso. Com o uso de regras de formação, o conhecimento das Rules é 
genérico para todas as instâncias de semáforos. Assim, para cada instância declarada, 
esta regra genérica é replicada para as instâncias específicas.  
No trabalho realizado na disciplina, foi adicionado a BNF os tokens formRule e 
end_formRule para diferenciar de uma Rule comum. O Algoritmo abaixo apresenta a 
estrutura sintática de uma regra de formação na linguagem PON. Quando o 
conhecimento é genérico em uma regra, é feita referencia ao nome do FBE, ao invés 
do nome de uma instância específica. 
 
 
Algoritmo 8: Exemplo do código FormRule 
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


263 
 
 
13 
14 
15 
16 
17 
18 
19 
 
   action 
      instigation inArcherFire1 Archer.mtFire 
      instigation inAppleCrossed1 Apple.mtExplode 
   end_action 
 
end_formRule 
 
O processo de regras de formação se encontra na opção quatro, ou seja, pré-
compilação. Na qual cada regra de formação é replicada na forma de combinação dos 
FBE que a compõem, na forma de regras tradicionais. 
 
A.2.5. 
Regras de FBE 
O conceito de Regras de FBE ou FBE Rules foi criado de forma a facilitar o 
desenvolvimento de aplicações PON que necessitam aplicar um conjunto de regras à 
todas as instâncias de um determinado FBE. Utilizando FBE Rules, torna-se possível a 
criação de FBE como entidades computacionais autônomas, ou seja, que apresentam 
Rules intrínsecas à sua instanciação. Trata-se de um caso particular de Regra de 
Formação, na qual a Rule está relacionada apenas a um determinado tipo de FBE. 
No trabalho realizado na disciplina, foi adicionado a BNF os tokens fbeRule e 
end_fbeRule para diferenciar de uma Form Rule e de uma Rule comum. O Algoritmo 
abaixo apresenta a estrutura sintática de um FBE Rule na linguagem PON.  
 
 
Algoritmo 9: Exemplo do código FbeRule 
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
 
O processo de compilação de FBE Rules se encontra na opção quatro, ou seja, 
pré-compilação. Cada FBE Rule é replicada para cada uma das instâncias da FBE que 
as compõem, na forma de regras tradicionais. 
Importante: Para que a regra seja aplicada a toda nova instância de um 
determinado FBE é necessário que as Premises e Instigations façam referência ao 
nome do FBE e não à sua instância. No exemplo acima, a Premise “PrHasFired2” 
possui como primeiro parâmetro “Robot.hasKicked”. Nesse caso, “Robot” é o nome de 


264 
 
 
um FBE e, portanto, essa regra será aplicada a todas as instâncias de “Robot” que 
forem criadas, independentemente de quantas sejam. 
 
A.2.6. 
Ponteiros 
Para permitir a utilização inicial de ponteiros na LingPON, uma série de 
alterações foram feitas no código do compilador para C++. 
Primeiramente, foram criados dois novos tokens no interpretador léxico (Lex): 
NEW e PTR. O token NEW reconhece a sequência “new”, enquanto PTR reconhece 
“^”, que é o caractere especial que designa ponteiros nessa proposta. Dessa forma, 
sequências desse tipo podem ser reconhecidas: 
Archer^ archer = new Archer 
A próxima alteração foi feita no parser Bison. Foi criada uma estrutura do tipo 
list da Standard Library para armazenar todos os IDs de ponteiros que são 
reconhecidos, e essa estrutura será utilizada posteriormente na geração de código C++. 
A alteração feita no Bison permite reconhecer sequências do tipo em declarações de 
Insts: 
Archer^ archer 
Archer^ acher1, ^archer2, ^archer3 
Também permite a utilização dos ponteiros dentro de métodos, em construções 
do tipo: 
method mtNewArcher(archer1 = new Archer) 
 A próxima alteração foi feita na parte de geração de código C++. Para que não 
fosse necessário fazer uma alteração muito grande nesse trecho de código, foi criado 
um novo tipo de entidade dentro da classe Attribute, chamado A_PTR, juntamente com 
os tipos antigos A_BOOLEAN, A_INTEGER e assim por diante. O atributo do tipo 
A_PTR é utilizado dentro da classe CPPCompiler para fazer a geração de código do 
ponteiro. Para isso, um método auxiliar foi criado dentro da classe Compiler, que serve 
de base para CPPCompiler. O método createInstantiationPtr varre a lista de 
identificadores e cria atributos do tipo A_PTR, que posteriormente são lidos para 
imprimir código em C++ utilizando a sintaxe de ponteiros. 
 
A.2.7. 
NOCA 
O NOCA é uma arquitetura de computador alternativa às arquiteturas de 
computadores tradicionais, tais como von Neumann e fluxo de dados. Essa arquitetura 


265 
 
 
foi desenvolvida de acordo com o modelo de execução PON, permitindo a execução de 
aplicações desenvolvidas segundo este paradigma. 
Para isso, Linhares (2015) listou os requisitos abaixo: 
A NOCA deve ser capaz de executar software composto unicamente de 
elementos do PON e, opcionalmente, também de funções sequênciais de acordo com 
o modelo von Neumann. 
 A NOCA deve ser genérica, no sentido de que qualquer alteração na aplicação 
PON sendo executada, dependa somente de alterações de software, portanto 
não requerendo qualquer reconfiguração de hardware. 
 A NOCA deve definir uma arquitetura de conjunto de instruções (Instruction Set 
Architecture, ou ISA) que implemente as funcionalidades dos elementos da 
cadeia de notificações do PON. 
 A NOCA deve definir unidades de processamento que sejam capazes de 
executar as instruções da ISA e o fluxo de notificações de forma paralela. 
 A NOCA deve ser capaz de executar uma aplicação PON mesmo que esta seja 
composta de mais elementos notificantes do que o número de unidades de 
processamento disponíveis para sua execução. Isto viabiliza a escalabilidade, 
no sentido de que o tamanho de uma aplicação PON a ser executada é limitado 
somente pela quantidade de memória disponível para armazenamento do 
respectivo software. 
Com base nesses requisitos, alguns elementos do metamodelo do PON, são 
mapeados para a ISA do NOCA (Attribute, Premise, Condition, Method e Method von 
Neumann). Do ponto de vista da linguagem PON, a compilação usando a opção seis, 
gera um código intermediário que contém a aplicação desenvolvida, formada apenas 
pelas instruções da ISA. 
A.2.8. 
Compilando para VHDL 
 
É possível compilar as aplicações escritas em PON diretamente para VHDL, de 
forma que o código gerado possa ser compilado e executado em uma FPGA. Como a 
cadeia de notificações do PON é executada de forma diferenciada no hardware da 
FPGA nem todos os elementos do PON tem seu paralelo no código VHDL. Os principais 
elementos são: O Attribute que armazena os dados, as Premises que realizam as 
avaliações sobre os dados e os Methods que alteram os dados dos Attributes. As 


266 
 
 
Conditions são apenas operações AND sobre as saídas das Premises, as Instigations 
são apenas ligações e assim por diante. A seguir serão detalhados os procedimentos 
necessários para que se possa executar a aplicação PON em uma FPGA. 
Para que uma aplicação PON possa ser compilada para uma FPGA são 
necessários além do arquivo VHDL gerado na compilação, os seguintes arquivos: 
 data_type_pkg.vhd 
 NOP_attribute.vhd 
 NOP_method.vhd 
 NOP_premise.vhd 
A seguir será feita uma breve descrição de cada um deles. 
O arquivo data_type_pkg.vhd contém a declaração genérica dos dados a serem 
armazenados no atributo, assim qualquer número de bits de qualquer tipo de dado pode 
ser armazenado em um atributo. Além disso, é possível concatenar um número variável 
de entradas em um atributo, resolvendo os conflitos por ordem de precedência. 
O arquivo NOP_attribute.vhd contém a declaração dos registradores que 
armazenam de forma genérica os dados dos attributes notificando as premises quando 
alguma alteração ocorre. 
O arquivo NOP_method.vhd contém o código das operações realizadas sobre 
os attributes e a lógica para fazer a atualização dos mesmos. 
O arquivo NOP_premise.vhd contém o código que realiza os testes sobre os 
valores dos Attributes determinando assim se a condição é verdadeira ou não. 
A atual implementação do compilador PON para VHDL possui algumas 
limitações. A principal delas é que apenas os tipos de dados boolean e integer estão 
implementados. Os Methods são capazes de realizar apenas as quatro operações 
básicas, soma, subtração, multiplicação e divisão, além da atribuição de valores. Os 
dados do tipo integer são interpretados como inteiros com sinal de 32 bits e o resultado 
da multiplicação é truncado em 32 bits. 
A resolução de conflitos é automática no código gerado, assim se dois ou mais 
methods tentarem atualizar o valor de um Attribute ao mesmo tempo o Attribute vai 
receber o valor do method que aparecer primeiro no código. 
Como não existe a estrutura “main” no VHDL, o bloco main do programa PON 
foi utilizado para determinar as entradas, as saídas, o nome da entidade e o nome do 
arquivo para o VHDL gerado. Para declarar um Attribute como entrada é necessário 
adicionar a seguinte linha ao bloco main no PON. 
in <nome_fbe>.<nome_attribute> 


267 
 
 
ex: in controlador.liga 
Para declarar um Attribute como saída é necessário adicionar a seguinte linha 
ao bloco main no PON. 
out <nome_fbe>.<nome_attribute> 
ex: out controlador.contador 
Para determinar o nome da entidade e consequentemente o nome do arquivo 
VHDL gerado é necessário adicionar a seguinte linha ao bloco main no PON. 
entity <nome_entidade> 
ex: entity controlaRobo 
Assim a entidade no código gerado vai receber o nome <nome_entidade> e o 
arquivo VHDL gerado vai receber o nome <nome_entidade>.vhd. 
Se o compilados não encontrar a palavra “entity” no bloco main o nome adotado 
é “NOPHD”. 
Como o bloco main não é interpretado pelo flex/bison não é possível adicionar 
comentários ou realizar a verificação de erros, assim deve-se tomar cuidado com a 
sintaxe. 
Para que se possa realizar a compilação do código gerado devem ser 
realizadas algumas configurações no compilador VHDL. Inicialmente é necessário 
adicionar todos os arquivos ao projeto, o código gerado e os arquivos apresentados 
anteriormente. A seguir é necessário configurar a ferramenta para interpretar o VHDL 
como VHDL 2008. A versão 2008 não é padrão e é necessária para compilar os tipos 
de dados utilizados. 
Uma característica importante do código VHDL gerado é que os elementos do 
PON são componentes independentes, assim é possível utilizar o visualizador RTL para 
encontrar erros nas aplicações. 
A.2.9. 
Integração 
Cada funcionalidade nova na linguagem foi implementada de maneira 
individual, sendo necessário realizar a integração de cada uma das partes. Para isso 
foram realizadas reuniões no laboratório LSIP, afim de resolver eventuais conflitos em 
arquivos fontes comuns do compilador. Como resultado, foram acrescentadas novas 
funcionalidades a linguagem e compiladores, com o objetivo de desenvolver o estado 
da técnica do compilador. A Figura 2 mostra o diagrama de blocos do compilador PON, 
após a realização das integrações dos trabalhos individuais da disciplina. 
 


268 
 
 
 
Figura 2 - Diagrama de Blocos após Integração. 
 
 


269 
 
 
Anexo B – Relatório de Disciplina sobre StaticCPP 
 


Universidade Tecnológica Federal do Paraná – Câmpus Curitiba 
Relatório para Disciplina Linguagens e Compiladores PON 
Profs. João Alberto Fabro e Jean Marcelo Simão 
Disciplina conjunta entre PPGCA e CPGEI 
 
Compilação C++ Estático 
StaticCPPCompiler.cpp 
Fernando Schutz e Adriano F. Ronszcka 
fschutz@gmail.com, ronszcka@gmail.com 
1. Introdução 
O projeto do compilador para C++ já existia nas versões anteriores do compilador PON, porém 
para a versão de C++ Estático (Static C++), o projeto foi reiniciado do zero, não aproveitando o que já havia 
sido feito. Tal decisão de projeto foi tomada justamente para não haver legados, bem como reforçar o 
aprendizado nas técnicas do PON. 
 
2. Processo de construção 
Após reuniões, algumas ideias foram propostas: 
 
Uso de métodos e funções INLINE 
o Tais códigos são tratados como uma definição de macros para o compilador. 
Assim, a chamada da função é substituída pelo corpo (ou código-fonte) da função 
declarada.  
o É extremamente eficiente para funções pequenas (caso do PON que tem poucos 
códigos nativos), pois evita a geração de código para chamada e retorno da 
função. 
o Todas as funções e métodos são declarados e implementações no arquivo .h, ou 
seja, não há mais o arquivo específico .cpp contendo os códigos-fonte da 
implementação. 
 
Todos os elementos deveriam ser STATIC 
o Existe uma porção de armazenamento específica e singular para tais elementos, 
não importando sua quantidade. Todos os objetos compartilham este mesmo 
espaço de armazenamento. Assim, o compartilhamento de “informações” entre 
estes se torna mais próximo e, consequentemente, mais rápido. 
 
Cada entidade PON se tornou uma classe 
o Como agora tudo se tornaria estático, definiu-se que cada elemento PON seria 
uma classe específica. 
o Este processo não ficou natural, pois em implementações com muitos elementos, 
geram vários arquivos na mesma pasta, dificultando o processo de busca. Porém, 
visando facilitar qualquer monitoramento, a nomenclatura utilizada na 
nomeação dos arquivos buscou um padrão isonômico e intuitivo. 
Assim, sobre a cadeia de notificação PON, quatro elementos foram construídos: 


 
Attributes: definiu-se que os Attributes teriam um atributo de valor e um método para 
ajustar seu valor (setValue()).  
 
Premise: possui um método que controla o processo de notificação, e um método que 
controla a inicialização da Premise. Uma questão importante foi realizar a cópia dos 
valores dos atributos durante a inicialização. Isso faz com que os valores possam ser 
comparados fidedignamente, sendo estes outros atributos ou valores. 
 
Subcondition: congrega os médotos para incrementar e decrementar a quantidade de 
Premises verdadeiras durante o processo de inferência.  
 
Methods: Neste não foi gerado apenas o arquivo .h mas também o arquivo .cpp, que 
contém a implementação do método. 
A Figura 1 demonstra o fluxo de execução da cadeia de notificações PON em StaticCPP. 
 
Figura 1: Fluxo de execução da cadeia de notificações PON em StaticCPP 
O processo de criação, portanto, seguiu a ordem dos métodos predeterminados pelo Compilador 
existente. Em todos os métodos a árvore de elementos do PON já está devidamente construída, sendo 
necessário apenas o mapeamento destes para uma estrutura legível na linguagem C++. Assim, a seguinte 
sequencia foi utilização 
 
createAllRules(mapRules): neste método é feita a iteração entre todas as Rules do código 
PON. Assim é possível construir as Conditions e Subconditions. Dentro destas é feita uma 
varredura na Instigations relacionadas, visando inserir a chamada dos Methods 
relacionados a cada Condition no método que incrementa a quantidade de Premises 
verdadeiras. A Figura 2 apresenta um código-fonte de uma subcondition. 
 
createAllPremises(mapPremises): este método faz a iteração em todas as Premises e 
valida a qual conditions e subconditions que as mesmas pertencem para incluir em seu 
arquivo (#include). São criados os métodos de inicialização e comparação entre os valores 
dos atributos. 
 
createAllInstantiations(mapInstantiations): itera-se entre todas as Instantiations afim de 
localizar os métodos e os atributos relacionados. Também é feita a varreduras nas 
Premises para que se possa realizar a inclusão destas. 
 
Attribute
•setValue()
Premise
•notify()
Subcondition
•inc()
•dec()
Method
•run()


 
Figura 2: Exemplo de Subcondition - "subClosing.h" 
 
Figura 3: Exemplo de Premise – “prGateIsClosed.h” 
 
Figura 4: Exemplo de Attribute - "gate_atGateState.h" 
 


 
(a)
(b)
 
Figura 5: Exemplo de Method – (a)"gate_mtClosing.h" e (b) "gate_mtClosing.cpp" 
No programa principal (main.cpp) devem ser feitas as inicializações de todos os atributos 
estáticos, bem como a execução dos métodos de inicialização das Premises. A Figura 6 apresenta um trecho 
de código exemplificando o processo de inclusão de todos os elementos PON, bem como a inicialização de 
seus atritubos. 
 
Figura 6: Snapshot de código-fonte do programa principal - "main.cpp" 
 
Testes foram efetuados utilizando o exemplo do portão eletrônico. Em uma máquina comum do 
laboratório L204 configurou-se o sistema operacional para trabalhar no modo monotarefa e monousuário, 
minimizando assim a influência do Sistema Operacional sobre o processo de testes. 
O sistema a ser testado deveria fazer 1.000.000 (um milhão) de mudanças do portão de aberto – 
fechado – aberto. Os resultados foram: 
 
Na compilação normal (sem otimização): 
o PON em linguagem C: 32000 milissegundos 
o PON em linguagem C++: 82000 milissegundos 
o PON em linguagem C++ estática: 52000 milissegundos 
Os primeiros resultados atingiram o esperado, ou seja, possivelmente não teria uma performance 
melhor que a linguagem C “pura” porém melhor que a linguagem C++ não estática. Porém um dos objetivos 
do projeto era o teste com a compilação otimizada, utilizando-se o parâmetro –O3 durante a compilação. Os 
resultados foram: 
 
Na compilação otimizada (-O3): 


o PON em linguagem C: 21000 milissegundos 
o PON em linguagem C++: 19000 milissegundos 
o PON em linguagem C++ estática: 9000 milissegundos 
Ou seja, na versão com otimização de código, a nova versão proposta era de duas a três vezes 
mais rápida que as versões existentes de compilação do código PON. A Figura 7 apresenta tais resultados. 
 
Figura 7: Resultado dos testes 
 
Assim, pode-se concluir que a utilização de construções de códigos INLINE e elementos STATIC, 
juntamente com a compilação otimizada, resultou num código veloz e eficiente. 
 
3. Modificações em 2016 
Após a utilização do sistema StaticCPP em problemas mais complexos do que o portão eletrônico, 
tradicionalmente implementado nas disciplinas, percebeu-se algumas falhas no código, bem como a falta de 
recursos para especificar situações pertinentes ao PON. As seguintes seções visam detalhar tais modificações. 
3.1. Valor inicial de Attributes e Premises 
Na primeira versão do C++ estático, ao se iniciar as Premises, era feita a verificação de sua 
validação, ou seja, caso o valor padrão se encaixasse expressão lógico-causal tornando a Premise verdadeira, 
o valor desta se tornava verdadeiro, e contava na validação da Subcondition e na Rule. Este processo foi 
retirado, pois estava causando problemas na lógica de alguns algoritmos, pois fazia com que, ao se ajustar o 
valor padrão inicial, o Method relacionado à Action era disparado, invalidando a cadeia de notificações inicial. 
O programador é forçado, agora, a tecer a lógica do algoritmo de acordo com o que deve ser ou 
não notificado ao ajustar os valores iniciais dos Attributes. Isso faz com que o desenvolvedor tenha consciência 
da lógica aplicada à cadeia de notificações. 
Average
0
10000
20000
30000
40000
50000
60000
70000
80000
90000
C
Old C++
New C++
C
Old C++
New C++
Linux Mono
Linux Mono -O3
Average
One Milion Gate Changes 
(Open to Close to Open)


 
No exemplo acima há o ajuste inicial de oito Attributes booleanos com valores false, sendo que 
tal valor já deve ser contado na Rule relacionada (RENOTIFY). Posteriormente, nas linhas 416 e 417, dois 
Attributes inteiros são valorados, porém tal processo não deve ser levado em consideração pela Rule, ou seja, 
não será avaliado na Premise durante sua atribuição. 
 
3.2. Notificação de Atributos 
A valoração de Attributes é realizada por meio do método setValue, que passa agora a ter dois 
parâmetros: valor e tipo de notificação. 
3.2.1. Tipo de Notificação 
 
_NOPAdds::STANDARD: comportamento padrão de notificações, ou seja, caso haja mudança no 
valor é notificado, caso contrário não há notificação. Caso seja deixado em branco, o algoritmo assume 
tal comportamento. 
 
_NOPAdds::RENOTIFY: faz com que haja notificação mesmo sem a mudança no valor do atributo. 
 
_NOPAdds::NO_NOTIFY: não há notificação mesmo com a mudança no valor do atributo. 
 
 
3.3. Interpretação de Métodos 
Todo método declarado na FBE deve ser escrito em uma linha, sendo que cada linha de comando 
deve ser separada por ponto e vírgula (;). Assim, optava-se por escrever os métodos após a compilação de 
tradução do algoritmo PON para a linguagem alvo. O grande problema é quando tem-se Regras de Formação, 
pois na pré-compilação cada uma das formRules será dividida em várias, de acordo com a quantidade de 
instancias da mesma. Assim, algumas novas interpretações foram realizadas nos métodos. 
3.3.1. Inclusão de bibliotecas 
Caso o programador necessite de alguma biblioteca, esta poderá ser declarada no início do corpo 
do método. 
 


3.3.2. Comandos e definições 
Caso seja necessário inserir uma configuração ou definição que deva aparecer antes do corpo do 
método e depois das includes iniciais da classe, basta colocar o código entre as palavras-chave <def> e </def> 
 
3.4. Tipo de Atribuição/Notificação 
Logo após a valoração do atributo, insere-se um valor entre os caracteres <> para definir o tipo 
de notificação: 
 
<S>: _NOPAdds::STANDARD 
 
<R>: _NOPAdds::RENOTIFY 
 
<N>: _NOPAdds::NO-NOTIFY 
 
 
3.5. Adequação no ajuste (set) e obtenção dos valores de Attributes 
Por padrão, a compilação insere os comandos para a modificação e obtenção dos valores dos 
Attrbitues, conforme a sintaxe padrão para o C++ Estático. O método da figura abaixo é resultante da 
compilação do método PON utilizado nos exemplos anteriores. 
 
 
4. Classe padrão _NOPAdds.h 
A cada compilação, será criada uma classe padrão a ser utilizada em todas as classes geradas na 
compilação. Até o presente, tal classe possui apenas a definição das constantes utilizadas na valoração de 
Attributes em seus tipos, conforme apresentado anteriormente. 


 
 
Referências 
RONSZCKA, A. F. Contribuição para a concepção de aplicações no paradigma orientado a 
notificações (PON) sob o viés de padrões, 2012. UTFPR. 
FERREIRA, C. A. Linguagem e compilador para o Paradigma Orientado a Notificações (PON): 
avanços e comparações, 2015. UTFPR. 
VALENÇA, G. Z.; BANASZEWSKI, R. F.; RONSZCKA, A. F.; et al. Framework PON, Avanços e 
Comparações. III Simpósio de Computação Aplicada. Anais... , 2011. Passo Fundo/RS. 
BANASZEWSKI, R. F. Paradigma Orientado a Notificações: Avanços e Comparações, Dissertação 
de Mestrado (CPGEI/UTFR). 2009. Curitiba/PR: UTFPR. 


