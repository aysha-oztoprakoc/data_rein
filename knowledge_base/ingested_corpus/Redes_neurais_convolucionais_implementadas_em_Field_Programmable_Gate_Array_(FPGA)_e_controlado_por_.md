# Redes neurais convolucionais implementadas em Field Programmable Gate Array (FPGA) e controlado por Paradigma Orientado a Notificações (PON).pdf

UNIVERSIDADE TECNOLÓGICA FEDERAL DO PARANÁ
GABRIEL REQUIÃO
REDES NEURAIS CONVOLUCIONAIS IMPLEMENTADAS EM FIELD
PROGRAMMABLE GATE ARRAY (FPGA) E CONTROLADO POR
PARADIGMA ORIENTADO A NOTIFICAÇÕES (PON)
CURITIBA
2025


GABRIEL REQUIÃO
REDES NEURAIS CONVOLUCIONAIS IMPLEMENTADAS EM FIELD
PROGRAMMABLE GATE ARRAY (FPGA) E CONTROLADO POR
PARADIGMA ORIENTADO A NOTIFICAÇÕES (PON)
Convolutional Neural Network implemented in Field Programmable Gate
Array (FPGA) and controlled by Notiﬁcation Oriented Paradigm (NOP)
Trabalho de Conclusão de Curso de Graduação
apresentado como requisito para obtenção
do
título
de
Bacharel
em
Engenharia
da
Computação
do
Curso
de
Engenharia
da
Computação
da
Universidade
Tecnológica
Federal do Paraná.
Orientador: Prof. João Alberto Fabro
Coorientador: Prof. Jean Marcelo Simão
CURITIBA
2025
Esta licença permite compartilhamento, remixe, adaptação e criação a partir do traba-
lho, mesmo para ﬁns comerciais, desde que sejam atribuídos créditos ao(s) autor(es).
Conteúdos elaborados por terceiros, citados e referenciados nesta obra não são co-
bertos pela licença.
4.0 Internacional


GABRIEL REQUIÃO
REDES NEURAIS CONVOLUCIONAIS IMPLEMENTADAS EM FIELD
PROGRAMMABLE GATE ARRAY (FPGA) E CONTROLADO POR
PARADIGMA ORIENTADO A NOTIFICAÇÕES (PON)
Trabalho de Conclusão de Curso de Graduação
apresentado como requisito para obtenção
do
título
de
Bacharel
em
Engenharia
da
Computação
do
Curso
de
Engenharia
da
Computação
da
Universidade
Tecnológica
Federal do Paraná.
Data de aprovação: 12/fevereiro/2025
João Alberto Fabro
Doutorado
Universidade Tecnológica Federal do Paraná
Robson Ribeiro Linhares
Doutorado
Universidade Tecnológica Federal do Paraná
Fernando Schütz
Doutorado
Universidade Tecnológica Federal do Paraná
Ricardo Kerschbaumer
Doutorado
Instituto Federal de Educação Ciência e Tecnologia Catarinense
CURITIBA
2025


AGRADECIMENTOS
Gostaria de expressar minha sincera gratidão a todas as pessoas que me apoiaram ao
longo desta importante jornada.
Agradeço primeiramente aos meus pais, Renata Requião e Carlos Felipe Requião, pelo
amor incondicional, apoio incansável e presença constante em minha vida. Sem vocês, essa
conquista não teria sido possível.
Estendo meus agradecimentos ao meu orientador, Prof. Dr. João Alberto Fabro, e ao
meu coorientador, Prof. Dr. Jean Marcelo Simão, por sua orientação, paciência e contribuições
valiosas ao longo de toda a trajetória deste trabalho. Suas orientações foram essenciais para
meu crescimento acadêmico e proﬁssional.
Aos meus colegas de curso, que compartilharam comigo momentos desaﬁadores e ale-
gres durante essa caminhada. Em especial, agradeço ao Gustavo Leardini Montanheiro, por
sua disposição e apoio constante.
Não poderia deixar de agradecer à Secretaria do Curso, pela cooperação e suporte
administrativo, que tornaram o caminho mais organizado e ﬂuido.
Por ﬁm, meu agradecimento a todos que, de alguma forma, contribuíram para a realiza-
ção desta pesquisa, seja com palavras de incentivo, orientações ou simples gestos de apoio.
A todos vocês, meu mais sincero obrigado.


RESUMO
Inteligência Artiﬁcial é um domínio que recentemente tem tido avanços rápidos, impulsionado
novas aplicações e casos de usos em muitas áreas como Visão Computacional, Processamento
de Áudio, Ciências de Dados e Processamento de Linguagem Natural, alcançando resultados
comparáveis à capacidade humana e/ou algoritmos manualmente desenvolvidos por humanos.
Uma das técnicas mais utilizadas é a de Rede Neurais Convolucionais que tem grande aplica-
ção em processamento de imagens, áudio, detecção de objeto e até mesmo em sistemas de
carros autônomos. Devido a esta grande utilização, surge a necessidade de realizar execução
eﬁciente dessas redes, tanto em velocidade quanto em gasto energético. Uma alternativa para
a execução de operações computacional com eﬁciência energética é a sua implementação
direta em dispositivos de hardware reconﬁgurável, utilizando as FPGAs (Field Programmable
Gate Arrays). Uma característica das FPGAs que as tornam interessantes para aplicações
tais como a execução de redes neurais é sua inerente implementação paralela das operações
computacionais. Uma das grandes diﬁculdades na programação/conﬁguração das FPGAs é a
complexidade de sincronização das operações, a nível de hardware. O Paradigma Orientado
Notiﬁcações (PON) é um novo paradigma de desenvolvimento de software, de forma coesa
e desacoplada, que provê vantagens principalmente quando a aplicação possui paralelismo.
Desta forma, este trabalho propõe o desenvolvimento de uma arquitetura dedicada a Redes
Neurais Convolucionais em FPGAs, usando o Paradigma Orientado a Notiﬁcações para realizar
a coordenação de controle dos componentes do sistema.
Palavras-chave: fpga; redes neurais convolucionais; paradigma orientado a notiﬁcação; quan-
tização.


ABSTRACT
Artiﬁcial Intelligence is an upcoming paradigm that recently has made rapid advances, creating
new aplications and use cases in several areas such as Computational Vision, Audio Proces-
sing, Data Science and Natural Language Processing, achieving results that are equal or better
than human capability and/or algorithms manually designed by humans. One of the techniques
which has seen wide spread adoption is that of Convolutional Neural Network, which has many
applications in image and audio processing, objection detecting and even in self-driving cars.
Due to this adoption, there is a new need of the efﬁcient execution of those networks, both in
speed and in energy efﬁciency, with one of the potential alternative to the traditional paradigms
utilized by such networks being the Notiﬁcation Oriented Paradigm which has advantages in
parallel processing due to it’s cohesive and decoupled nature. In a similar manner, as a platform
Field Programmable Gate Array(FPGA) demonstrate potential due to it’s reconﬁgurability at
the hardware level and the possible paralelism, which is synergestic with NOP. This works
implements an architecture as a proof of concept, dedicated to Convolutional Neural Networks
in FPGA, using the Notiﬁcation Oriented Paradigm in a hybrid model.
Keywords: fpga; convolutional neural networks; notiﬁcation oriented paradigm; quantization.


LISTA DE FIGURAS
Figura 1 –
Exemplo genérico do relacionamento das entidades em PON.
. . . . .
17
Figura 2 –
Exemplo de funcionamento do ﬂuxo de notiﬁcações.
. . . . . . . . . .
18
Figura 3 –
Exemplo de uma estrutura de Rede Neural Artiﬁcial. . . . . . . . . . . .
20
Figura 4 –
Estrutura de um Neurônio.
. . . . . . . . . . . . . . . . . . . . . . . . .
20
Figura 5 –
Operações de uma Rede Neural Convolucional. . . . . . . . . . . . . . .
22
Figura 6 –
Arquitetura de uma Rede Neural Convolucional.
. . . . . . . . . . . . .
22
Figura 7 –
Exemplo de uma Rede Neural Convolucional. . . . . . . . . . . . . . . .
23
Figura 8 –
Aplicação de um Filtro na operação de convolução . . . . . . . . . . . .
24
Figura 9 –
Gráﬁco da função ReLU . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
Figura 10 – Gráﬁco da função Sigmoide . . . . . . . . . . . . . . . . . . . . . . . . .
26
Figura 11 – Layout da Memória Física. . . . . . . . . . . . . . . . . . . . . . . . . . .
27
Figura 12 – Paralelismo da Operação de Convolução. . . . . . . . . . . . . . . . . .
29
Figura 13 – Arquitetura Convencional de uma FPGA.
. . . . . . . . . . . . . . . . .
31
Figura 14 – Visão de uma implementação de FPGA. . . . . . . . . . . . . . . . . . .
32
Figura 15 – Implementação de um CLB na Arquitetura Cyclone V.
. . . . . . . . . .
33
Figura 16 – Implementação de um bloco DSP na Arquitetura Cyclone V. . . . . . . .
35
Figura 17 – Modos possíveis do bloco M10K. . . . . . . . . . . . . . . . . . . . . . .
36
Figura 18 – Comparação das faixas diferentes de ﬂoat32 e int8 . . . . . . . . . . . .
40
Figura 19 – Quantização de [-1, 1) de ﬂoat32 a int8 . . . . . . . . . . . . . . . . . . .
41
Figura 20 – Exemplo de aplicações de esquema de quantização. . . . . . . . . . . .
45
Figura 21 – Estrutura da Rede Neural Convolucional utilizada. . . . . . . . . . . . .
50
Figura 22 – Diagrama de Blocos da Arquitetura do Trabalho Desenvolvido. Dia-
grama criado na ferramenta Astah SysML . . . . . . . . . . . . . . . . .
51
Figura 23 – Exemplo do processo de pipeline
. . . . . . . . . . . . . . . . . . . . .
53
Figura 24 – Diagrama de Atividade da Unidade de Rede Neural. Diagrama criado na
ferramenta Astah SysML
. . . . . . . . . . . . . . . . . . . . . . . . . .
54
Figura 25 – Diagrama Paramétrico da Unidade de Rede Neural. Diagrama criado na
ferramenta Astah SysML
. . . . . . . . . . . . . . . . . . . . . . . . . .
56
Figura 26 – Diagrama de Atividade da Árvore de Adição.
. . . . . . . . . . . . . . .
57
Figura 27 – Exemplo de pipeline no Bloco de Operação . . . . . . . . . . . . . . . .
58


Figura 28 – Diagrama de Atividade do Bloco de Conversão. Diagrama criado na fer-
ramenta Astah SysML . . . . . . . . . . . . . . . . . . . . . . . . . . . .
61
Figura 29 – Diagrama de Atividade da Função ReLU. Diagrama criado na ferramenta
Astah SysML . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
62
Figura 30 – Diagrama de Atividade da Função Sigmoide. Diagrama criado na ferra-
menta Astah SysML . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
63
Figura 31 – Diagrama de Atividade da operação de MaxPooling. Diagrama criado na
ferramenta Astah SysML
. . . . . . . . . . . . . . . . . . . . . . . . . .
64
Figura 32 – Diagrama de Atividade Simpliﬁcado. . . . . . . . . . . . . . . . . . . . .
68
Figura 33 – Diagrama de Componentes em UML. Diagrama criado com a ferramenta
Astah UML. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
68
Figura 34 – Diagrama de Estado de Maquina. . . . . . . . . . . . . . . . . . . . . . .
69
Figura 35 – Diagrama de Classe representando as entidades PON. Diagrama criado
com a ferramenta Astah UML. . . . . . . . . . . . . . . . . . . . . . . . .
70
Figura 36 – Diagrama de Componente DON - Canto Superior Esquerdo. Diagrama
criado com a ferramenta Astah UML. . . . . . . . . . . . . . . . . . . . .
71
Figura 37 – Diagrama de Componente DON - Canto Superior Direito. Diagrama cri-
ado com a ferramenta Astah UML. . . . . . . . . . . . . . . . . . . . . .
72
Figura 38 – Diagrama de Componente DON - Canto Inferior Esquerdo. Diagrama cri-
ado com a ferramenta Astah UML. . . . . . . . . . . . . . . . . . . . . .
73
Figura 39 – Diagrama de Componente DON - Canto Inferior Direito. Diagrama criado
com a ferramenta Astah UML. . . . . . . . . . . . . . . . . . . . . . . . .
74
Figura 40 – Diagrama de Componente sobre partes das FBEs que se comunicam no
caso de carregamento de uma janela de convolução. Diagrama criado
com a ferramenta Astah UML. . . . . . . . . . . . . . . . . . . . . . . . .
84
Figura 41 – Diagrama de Atividade do SysML - Parte 1. Diagrama criado com a fer-
ramenta Astah UML. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
85
Figura 42 – Diagrama de Atividade do SysML - Parte 2. Diagrama criado com a fer-
ramenta Astah UML. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
85
Figura 43 – Diagrama de Atividade do SysML - Parte 3. Diagrama criado com a fer-
ramenta Astah UML. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
86


Figura 44 – Diagrama de Atividade do SysML - Parte 4. Diagrama criado com a fer-
ramenta Astah UML. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
86
Figura 45 – Imagem classiﬁcada como o dígito 2, oriunda do Dataset MNIST. . . . .
88
Figura 46 – Variante do Modelo com 2 Camadas Convolucionais. . . . . . . . . . . .
90
Figura 47 – Variante do Modelo com 4 Camadas Convolucionais. . . . . . . . . . . .
90


LISTA DE TABELAS
Tabela 1 –
Eﬁciência energética de operações sobre processo de fabricação de
45nm, em pJ (pico Joules)
. . . . . . . . . . . . . . . . . . . . . . . . .
40
Tabela 2 –
Comparação de modelos de Quantização utilizadas em Trabalhos
. . .
46
Tabela 3 –
Recursos utilizados na Implementação da Rede Neural
. . . . . . . . .
89
Tabela 4 –
Resultados de Experimento sobre acurácia dos modelos obtidos
. . .
90
Tabela 5 –
Resultados de Experimento sobre tempo de execução obtidos . . . . .
91


LISTA DE ABREVIATURAS E SIGLAS
Siglas
ASIC
Circuitos Integrados de Aplicação Especíﬁca, do inglês Application Speciﬁc Inte-
grated Circuit
CLB
Blocos Lógicos Conﬁguráveis ou Conﬁgurable Logic Blocks
CNN
Redes Neurais Convolucionais, do inglês Convolutional Neural Networks
DSP
Processador de Sinais Digitais, do inglês Digital Signal Processor
FBE
Fact Base Element (Elemento de Base de Fatos)
FPGA
Arranjo de porta programável em campo ou Field Programmable Gate Array
MLP
Multi Layer Perceptron (Perceptron de múltiplas camadas)
PON
Paradigma Orientado a Notiﬁcações
ReLU
Unidades Lineares Retiﬁcadas, do inglês Rectiﬁed Linear Unit
RNA
Redes Neurais Artiﬁciais


SUMÁRIO
1
INTRODUÇÃO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
1.1
Contextualização . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
1.2
Motivações
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
1.3
Objetivos
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
1.3.1
Objetivo Geral
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
1.3.2
Objetivos Especíﬁcos
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
1.4
Estrutura do trabalho . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
2
REFERENCIAL TEÓRICO . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
2.1
Paradigma Orientado a Notiﬁcações
. . . . . . . . . . . . . . . . . . . .
15
2.2
Redes Neurais Convolucionais
. . . . . . . . . . . . . . . . . . . . . . .
19
2.2.1
Descrição Geral
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
2.2.2
Representação Matemática
. . . . . . . . . . . . . . . . . . . . . . . . . .
23
2.2.3
Representação Computacional
. . . . . . . . . . . . . . . . . . . . . . . .
26
2.2.4
Paralelismo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
2.3
Field Programmable Gate Array . . . . . . . . . . . . . . . . . . . . . . .
29
2.3.1
Introdução Geral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
2.3.2
Bloco Lógico Reconﬁgurável . . . . . . . . . . . . . . . . . . . . . . . . . .
32
2.3.3
Bloco DSP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
2.3.4
Elemento de Memória . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
36
2.4
Quantização de Redes Neurais
. . . . . . . . . . . . . . . . . . . . . . .
37
2.4.1
Formatos Numéricos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
2.4.2
Esquema de Quantização . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
2.4.3
Erro por operação em Quantização . . . . . . . . . . . . . . . . . . . . . .
41
2.4.4
Quantização em Redes Neurais Artiﬁciais . . . . . . . . . . . . . . . . . . .
43
2.4.5
Aplicação de Esquemas de Quantização
. . . . . . . . . . . . . . . . . . .
46
2.5
Considerações sobre a Revisão da Literatura . . . . . . . . . . . . . . .
46
3
REDE NEURAL CONVOLUCIONAL EM FPGA CONTROLADA VIA PON
.
48
3.1
Modelo de Rede Neural Convolucional . . . . . . . . . . . . . . . . . . .
48
3.2
Visão Geral da Arquitetura da Solução . . . . . . . . . . . . . . . . . . .
50
3.3
Unidade Rede Neural . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
53


3.3.1
Visão Geral da Unidade Rede Neural . . . . . . . . . . . . . . . . . . . . .
54
3.3.2
Bloco de Operação . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
56
3.3.3
Bloco de Conversão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
58
3.3.4
Bloco de Ativação
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
61
3.4
Unidade MaxPooling . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
63
3.5
Controlador PON . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
65
3.5.1
Justiﬁcativa da utilização do PON . . . . . . . . . . . . . . . . . . . . . . .
65
3.5.2
Visão Geral do Controlador
. . . . . . . . . . . . . . . . . . . . . . . . . .
66
3.5.3
Modelagem de Máquina em Estados em PON
. . . . . . . . . . . . . . . .
75
3.5.4
Controlador em Operação . . . . . . . . . . . . . . . . . . . . . . . . . . .
84
3.6
Considerações sobre o Trabalho Realizado
. . . . . . . . . . . . . . . .
86
4
RESULTADOS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
88
5
CONCLUSÃO E TRABALHOS FUTUROS . . . . . . . . . . . . . . . . . .
92
5.1
Conclusão . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
92
5.2
Trabalhos Futuros
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
92
REFERÊNCIAS
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
94
APÊNDICE A
MODELAGEM EM LINGPON . . . . . . . . . . . . . . . .
101
APÊNDICE B
CÓDIGO EM VHDL . . . . . . . . . . . . . . . . . . . . .
112


12
1 INTRODUÇÃO
Este capítulo introduz o trabalho, fornecendo as informações necessárias para a com-
preensão do restante do documento.
A seção 1.1 apresenta o contexto sobre a qual este trabalho se baseia, a seção 1.2
apresenta as motivações e justiﬁcativas, e a seção 1.3 apresenta os objetivos que esse trabalho
pretende atingir. A seção 1.4 mostra a estrutura dos capítulos seguintes.
1.1
Contextualização
Redes Neurais Artiﬁciais (RNA) são uma técnica de aprendizagem de máquina que apre-
sentou grande avanço recente, permitindo a solução de muitos problemas com eﬁciência e, em
alguns casos, com precisão superior à humana (TULI et al., 2021; WU; FENG, 2018). Essas
técnicas foram inicialmente concebidas na década de 1940, inspiradas em redes neurais bioló-
gicas. No entanto, devido às limitações computacionais da época, poucos avanços ocorreram
até a década de 1980, quando os progressos na computação digital abriram novas possibilida-
des. Em especial, as Redes Neurais Convolucionais, do inglês Convolutional Neural Networks
(CNN) foram desenvolvidas para resolver problemas encontrados nas Redes Neurais Artiﬁci-
ais tradicionais, alcançando grande sucesso em diversas aplicações (SURYADEVARA; YANA-
MALA, 2021).
Atualmente, as Redes Neurais Convolucionais são muito utilizadas em diversas tarefas,
desde processamento de imagem (SRIVASTAVA et al., 2021) ou áudio (MICHELSANTI et al.,
2021) até a classiﬁcação de objetos e pessoas (DHRUV; NASKAR, 2020). Consequentemente,
o uso crescente das CNNs levanta discussões sobre como desenvolver arquiteturas de hard-
ware eﬁcientes para executá-las.
Devido à utilidade das Redes Neurais Convolucionais, atualmente muitas empresas de
tecnologia buscam desenvolver hardware especializado para a execução de Redes Neurais Ar-
tiﬁciais e Convolucionais, como Google (GOOGLE, 2019; GOOGLE, 2022), Intel (OPENVINO,
2022) ou Qualcomm (QUALCOMM, 2022). Essa abordagem de utilização de hardware dedi-
cado a execução de Redes Neurais Artiﬁciais e Convolucionais já está presente em muitos
dispositivos como smartphones e notebooks (IGNATOV et al., 2019).
O uso de em problemas cada vez mais complexos demanda avanços em relação às
implementações tradicionais, de modo a viabilizar sua aplicação em uma ampla variedade de
sistemas, desde pequenos dispositivos embarcados até agentes autônomos.


13
1.2
Motivações
Embora a Inteligência Artiﬁcial tenham diversas aplicações, enfrenta desaﬁos relaciona-
dos à execução eﬁciente, especialmente em termos de processamento, velocidade e consumo
energético o que diﬁculta a sua utilização em grande quantidade de dispositivos como smart
watches, telefone celulares, drones entre outros (SZE et al., 2017; TAO et al., 2020).
Desta maneira, existe a exploração de metodologias diferentes para execução eﬁciente
e aceleração dessas ferramentas, com o interesse maior sendo sobre o processo de inferência,
já que o treinamento de redes neurais requer muito mais recursos e tempo, sendo que muitas
redes neurais necessitam de grandes clusters de GPUs para que sejam treinadas.
Uma alternativa às metodologias atuais é o Paradigma Orientado a Notiﬁcações (PON),
que proporciona modelagem lógica-causal explicitamente paralela devido ao seu desacopla-
mento de componentes, e como redes neurais são formadas primariamente de operações de
multiplicação e adição em paralelo, o PON pode oferecer uma solução eﬁciente. Já existe uma
implementação de treinamento e inferência de rede neural artiﬁcial totalmente conectada, Multi
Layer Perceptron (Perceptron de múltiplas camadas) (MLP), no paradigma chamado de Neuro-
PON (SCHÜTZ et al., 2019), com bons resultados iniciais.
Como alternativa de plataforma para a execução temos as Arranjo de porta programável
em campo ou Field Programmable Gate Array (FPGA), que se apresentam como uma pla-
taforma interessante para a aceleração dessas redes neurais em Hardware, possuindo uma
eﬁciência energética maior do que GPUs e CPUs convencionais e oferecendo um desempenho
maior do que CPUs (MITTAL, 2020). O trabalho do Schütz et al. (2019) já apresenta implemen-
tação em FPGA, utilizando ferramentas para desenvolvimento de PON em hardware (KERSCH-
BAUMER et al., 2018). Entretanto, o trabalho de Schütz et al. (2019) realiza uma implementação
mais simples, apenas sendo implementadas RNAs, porém realizando também o processo de
treinamento.
Este trabalho então explora a implementação de uma Rede Neural Convolucional utili-
zando a controle de componentes complexos e coordenação entre eles por meio do Paradigma
Orientado a Notiﬁcações (PON). O PON se mostra apropriado para essa aplicação devido à sua
capacidade de desacoplar componentes em relações lógicas causais, permitindo a exploração
eﬁciente do paralelismo granular entre as entidades de processamento.
O trabalho busca demonstrar a viabilidade do uso do PON em conjunto com FPGAs
para aplicações em inteligência artiﬁcial, servindo como uma prova de conceito. Apesar das
limitações impostas pelo escopo deste estudo, espera-se que a proposta contribua para futuras
evoluções no desempenho da execução de CNNs e na adoção do PON e suas tecnologias.


14
1.3
Objetivos
Esta seção apresenta os objetivos deste trabalho, separados em objetivos geral e obje-
tivos especíﬁcos.
1.3.1
Objetivo Geral
O objetivo geral deste trabalho é realizar o processo de inferência de Redes Neurais
Convolucionais (CNNs) em plataforma de FPGAs, usando o Paradigma Orientado a Notiﬁca-
ções (PON) para a realizar a coordenação de controle dos diversos componentes implementa-
dos.
1.3.2
Objetivos Especíﬁcos
À luz do objetivo geral, os objetivos especíﬁcos são:
• Implementar o processo de inferência de Rede Neural Convolucional em FPGA. Para
isso, implementar e testar as seguintes operações: Camada Convolucional, Camada
Fully Connected e Camada MaxPool, funções de ativações ReLU (Rectiﬁed Linear
Unit) e Sigmoidal (Sigmoid).
• Avaliar característica de frequência do circuito implementado, visando que seja possí-
vel usar um clock de 200 MHz em uma FPGA Cyclone V.
• Avaliar os ganhos de desempenho em relação à execução em processadores tradicio-
nais
1.4
Estrutura do trabalho
Nesta seção inicial foi apresentada uma breve introdução a este presente trabalho.
No capítulo 2, são apresentados o Referencial Teórico e a revisão bibliográﬁca necessá-
rios para o desenvolvimento do trabalho, com a explicação dos conceitos fundamentais.
O capítulo 3 descreve o desenvolvimento do trabalho, detalhando a arquitetura criada e
as decisões técnicas tomadas ao longo do processo.
No capítulo 4, são apresentados os resultados obtidos com o trabalho desenvolvido.
Por ﬁm, o capítulo 5 traz as conclusões e considerações ﬁnais deste estudo.


15
2 REFERENCIAL TEÓRICO
Esse capítulo apresenta a base teórica para a construção do presente trabalho. Pri-
meiramente será apresentada na seção 2.1 uma breve descrição do Paradigma Orientado a
Notiﬁcações, seguida pela seção 2.2, que apresenta uma introdução a Redes Neurais Convo-
lucionais. A Seção 2.3, traz uma visão geral sobre os dispositivos de Field Programmable Gate
Array (FPGA) e, por último, com o intuito de explicar conceitos relacionados às tecnologias
mencionadas em seções anteriores, a Seção 2.4 apresenta o conceito de quantização e outros
conceitos relacionados.
2.1
Paradigma Orientado a Notiﬁcações
O Paradigma Orientado a Notiﬁcações (PON) é um paradigma que permite uma nova
maneira de implementar e estruturar software e hardware. Esta seção apresenta o paradigma
de uma maneira introdutória, começando com as bases teóricas e seguindo com as implemen-
tações e trabalhos existentes sobre este paradigma.
A origem do PON foi inicialmente uma proposta de solução de controle discreto para
sistema inteligentes de manufatura (SIMÃO, 2001; SIMÃO, 2005), proposta a qual permitiu uma
maneira de orquestrar controle ágil, i.e. com tempo de resposta curto na sua adaptação, através
de notiﬁcações entre entidades relacionadas em um sistema de regras (SIMÃO; TACLA; STAD-
ZISZ, 2009), com o nome original sendo Controle Orientado a Notiﬁcações (CON). Essa solução
evoluiu, posteriormente, para cobrir casos genéricos de inferência de software (RONSZCKA et
al., 2015; SIMÃO; TACLA; STADZISZ, 2009).
No entanto, foi percebido que o desacoplamento e o paralelismo da solução proposta
apresentam um grande potencial para serem aplicados de diversas outras maneiras quando
comparados aos paradigmas de programação atual. Sendo agrupado estes paradigmas em
duas categorias principais, nomeadamente o Paradigma Imperativo (PI) e o Paradigma Decla-
rativo (PD) (GABBRIELLI; MARTINI, 2010).
O PI é o paradigma clássico sequencial, sendo relativamente similar ao paradigma do
próprio código de máquina presente em computadores modernos. Com isso, é presente nele
um alto grau de diﬁculdade tanto para a produção de códigos desacoplados, sem redundância,
quanto para a utilização de processamento paralelo/distribuído (BANASZEWSKI et al., 2009;
KAISLER, 2005).
O PD, em seu turno, se baseia em uma camada de abstração mais alta, na qual os
programadores deﬁnem outras estruturas de dados como regras e bases de fatos, não se pre-
ocupando com detalhes de implementação, mas no que deve ser feito. Isto foi tornado possível
através do desenvolvimento de um sistema de inferência para tal, baseado em pesquisas e
casamento entre bases de fatos e de regras. Entretanto, ele ainda assim encontra problemas


16
similares de acoplamento, e problemas em distribuição (BANASZEWSKI et al., 2009; GABBRI-
ELLI; MARTINI, 2010).
Dados os problemas encontrados nos atuais paradigmas, largamente discutidos em tra-
balhos (do grupo de pesquisa no qual este trabalho se encontra) como (BANASZEWSKI et al.,
2009; VALENÇA, 2012; WIECHETECK, 2011; XAVIER, 2014; NEGRINI et al., 2019; SCHÜTZ
et al., 2019; KERSCHBAUMER et al., 2018; LINHARES, 2015), foi então concebido e elaborado
o Paradigma Orientado as Notiﬁcações (PON), que visa solucioná-los (SIMÃO, 2001; SIMÃO,
2005; SIMÃO; TACLA; STADZISZ, 2009).
O paradigma nascente foi utilizado inicialmente para implementações de software (BA-
NASZEWSKI et al., 2009; VALENÇA, 2012; WIECHETECK, 2011; XAVIER, 2014; NEGRINI et
al., 2019), mas evoluindo também para modelagem (NOVAES, 2019; MENDONCA, 2020), e por
ﬁm, também para o desenvolvimento de sistemas genéricos e sistemas de hardware (KERS-
CHBAUMER et al., 2018; SCHÜTZ et al., 2019; PORDEUS et al., 2023).
O PON é estruturalmente formado por dois tipos de entidades computacionais, nomea-
damente Fact Base Element (Elemento de Base de Fatos) (FBE) e Rules (Regras). Os FBEs
são entidades facto-execucionais que representam elementos do mundo, sejam esses físicos ou
abstratos, de maneira análoga a objetos em Paradigma Orientado a Objetos, formadas por ele-
mentos chamados de Attributes (Atributos) que codiﬁcam o estado de cada entidade e por ele-
mentos nomeados de Methods (Métodos) que realizam as mudança sobre os estados (SIMÃO;
TACLA; STADZISZ, 2009; BANASZEWSKI et al., 2009; RONSZCKA et al., 2017; PORDEUS et
al., 2023; OSHIRO, 2021).
O segundo tipo de entidade, as Rules (Regras), são, em suma, entidades lógico-causais,
compostas por entidades de dois tipos distintos: Conditions (Condições) e Actions (Ações). As
Conditions são associadas a sub-elementos do tipo Premise (Premissa), e determinam a ló-
gica de acionamento das Rules. Já as Actions (Ações) são associadas a sub-elementos do
tipo Instigation (Instigação), que determinam os efeitos de cada Rule quando acionadas (SI-
MÃO; TACLA; STADZISZ, 2009; BANASZEWSKI et al., 2009; OSHIRO, 2021; NEVES, 2021;
RONSZCKA et al., 2015).
A Figura 1 mostra um exemplo de como as entidades e os seus elementos constituintes
se relacionam em um sistema completo. Como pode ser visto, os FBEs e seus elementos podem
ser representados via instâncias de objetos e Rules e seus elementos podem ser representados
por instâncias de objetos, porém na prática, essas entidades e seus elementos são atômicas e
desacopladas, tendo a comunicação através de notiﬁcações (OSHIRO, 2021).
A Figura 2 mostra um exemplo de um ﬂuxo de notiﬁcações, começando primeiro por um
Attributes de uma instância de um FBE mudar o seu estado, ocasionando notiﬁcações para a
suas Premises associadas, que individualmente recalculam as suas expressões lógicas boo-
leanas. Se tiver alguma mudança de estado na Premise, essa irá propagar a notiﬁcação para
as Conditions pertinentes, que da mesma maneira refazem o cálculo da expressão e caso seja
verdadeira, a sua Rule é notiﬁcada, a qual terá a ação de notiﬁcar as Actions referenciadas


17
Figura 1 – Exemplo genérico do relacionamento das entidades em PON.
Fonte: (OSHIRO, 2021).
e que irão propagar para as notiﬁcações para a lista de Instigation, e estas por suas vez irão
acionar os Methods dos FBEs especíﬁcas, possivelmente causando mudanças nos Attributes e
ativando outro ciclo de notiﬁcações.
Atualmente existem uma ampla gama de materializações do PON, devido a ser um alvo
de pesquisas em diversas áreas como engenharia de software, redes neurais, lógica fuzzy,
hardware reconﬁgurável e entre outas. As primeiras materializações foram em software com
aplicações em hardware surgindo posteriormente (BANASZEWSKI et al., 2009; PORDEUS,
2017; RONSZCKA, 2019; PORDEUS et al., 2023; OSHIRO, 2021).


18
Figura 2 – Exemplo de funcionamento do ﬂuxo de notiﬁcações.
Fonte: (NEVES, 2021).
O desenvolvimento inicial do PON foi um framework para desenvolvimento de software
chamado de Framework PON C++ Prototipal (versão 0.5), que surgiu pela pesquisa de mes-
trado e de doutorado do Prof. Jean Marcelo Simão, com evolução posterior para o Framework
PON C++ (versão 1.0) (BANASZEWSKI et al., 2009; SIMÃO et al., 2012).
Esses frameworks tiveram evolução gradual com uma versão otimizada (Framework
PON C++ 2.0), multicore (Framework PON C++ 3.0) que permitem utilizar a linguagem C++
com o seu Paradigma Orientado a Objeto e Paradigma Imperativo aplicando a abordagem de
notiﬁcações sobre essas. Adicionalmente foram criadas versões do frameworks em outras lin-
guagens diferentes como C#, Java e Erlang (VALENÇA, 2012; PORDEUS, 2017; PORDEUS et
al., 2023; OLIVEIRA, 2019; BARRETTO; VENDRAMIN; SIMÃO, 2018; OSHIRO, 2021).
Conforme mencionado, o PON também foi aplicado em implementações de hardware,
com a primeira pesquisa e projetos sendo o PON em Hardware Digital (PON-HD), que explora
as vantagens do PON em seu paralelismo explícito para plataformas de lógica reconﬁgurável
(WITT et al., 2011; SIMÃO et al., 2012; KERSCHBAUMER et al., 2018; PORDEUS, 2017).
Esta abordagem evoluiu por novas pesquisas para alcançar uma solução mais efetiva usando
o PON-HD com a Tecnologia LingPON para geração de circuitos a partir de uma linguagem de
alto nível (i.e. também chamado de High Level Synthesis, sintése de alto nível) o que é chamado
de LingPON-HD (KERSCHBAUMER et al., 2018; KERSCHBAUMER et al., 2021; PORDEUS et
al., 2023; PORDEUS, 2017).
Essas tecnologias já foram utilizadas com sucesso em aplicações, com a principal rele-
vante para este trabalho sendo a NeuroPON do Prof. Schutz (SCHÜTZ et al., 2019) que utiliza
das tecnologias citadas para a implementação completa de uma Rede Neural Artiﬁcial, que


19
pode ser utilizada em diversas plataformas como processadores monocore, multicore e disposi-
tivos de lógica reconﬁgurável enquanto abstrai os conhecimentos especíﬁcos necessários para
o usuário, apresentando uma maneira altamente eﬁciente e agnóstica.
Em suma, o Paradigma Orientado a Notiﬁcações é um paradigma com diversas pesqui-
sas sendo realizadas sobre, e consistentemente demonstrando a capacidade para ser usado
em casos onde paralelismo é necessário, como por exemplo redes neurais artiﬁciais ou convo-
lucionais (SCHÜTZ et al., 2019; LI et al., 2021).
2.2
Redes Neurais Convolucionais
Nesta seção serão explorados os conceitos fundamentais de Rede Neurais Artiﬁciais
e Convolucionais, começando na seção 2.2.1 com uma introdução de alto nível das referidas
redes e na seção 2.2.2 será explorada a matemática por trás delas, porém limitado apenas ao
processo de inferência, i.e. execução, dessas, e ﬁnalmente a seção 2.2.4 tem explicações de
como essas operações podem ser paralelizadas.
2.2.1
Descrição Geral
Redes Neurais Artiﬁciais (Artiﬁcial Neural Networks - ANN), também chamadas de RNA,
são sistemas computacionais inspirados por sistemas neuro-biológicos que formam a inteligên-
cia natural (WU; FENG, 2018).
Para a generalização de Redes Neurais Artiﬁciais, são mencionados tensores, que em
suma são objetos algébricos que mapeiam relações multilineares, isto é relações lineares com
múltiplas variáveis separadas, o que em suma pode ser representado como matrizes de várias
dimensões.
A estrutura básica de uma RNA pode ser vista na Figura 3, que consiste em uma camada
de entrada, uma ou mais camadas escondidas e uma camada de saída. A camada de entrada
não existe ﬁsicamente na implementação mas apenas na modelagem, servindo para conectar
os dados de entrada com as camadas subsequentes. O resultado ﬁnal de uma RNA é o resul-
tado obtido na última camada, que é nomeada como ’camada de saída’ como consequência.
Uma arquitetura onde não há nenhuma camada escondida é denominada Perceptron. Quando
a RNA possui então, uma ou mais camadas escondidas, a rede neural passa a ser denominada
Multi-Layer Perceptron (MLP).


20
Figura 3 – Exemplo de uma estrutura de Rede Neural Artiﬁcial.
Fonte: (SCHÜTZ et al., 2019).
Cada camada é composta por uma determinada quantidade de neurônios. Um diagrama
representando um neurônio pode ser visualizado na Figura 3. Enquanto que um neurônio pode
ser visto conforme a Figura 4. Neste diagrama, é esquematizada a multiplicação das entra-
das (xi) do neurônio por números ditos pesos (weights, wi), que em suma são parâmetros
aprendidos durante o treinamento da rede. Em seguida, o diagrama representa o somatório dos
resultados dessas multiplicações, e a soma do mesmo por uma constante nomeada de bias.
A partir disso, é aplicada uma "função de ativação", que deﬁne a saída do neurônio partir do
soma obtida anteriormente. Uma função de ativação deve ser uma função não linear, isso é,
uma função cujo gráﬁco não seja uma reta. Nas RNAs tradicionais, as funções de ativação mais
comumente utilizadas são a tangente hiperbólica e a sigmoide (SHAH; YOUNGBLOOD, 2024).
Figura 4 – Estrutura de um Neurônio.
Fonte: (SILVA; SPATTI; FLAUZINO, 2010).
Uma das grandes limitações dos primeiros modelos de RNAs simples/tradicionais (tam-
bém denominados fully connected) se deve à grande quantidades de pesos e neurônios neces-


21
sários para a utilização dessas em imagens. Por exemplo, um único neurônio em uma imagem
colorida RGB de 128 × 128 pixels terá 49.152 pesos (128 x 128 x 3), o que acaba tornando in-
viável a implementação de redes neurais artiﬁcial tradicionais utilizando apenas RNAs (ZHANG
et al., 2021).
Dessa maneira visando principalmente o processamento de imagens, surgiram as Re-
des Neurais Convolucionais (Convolutional Neural Network - CNN), as quais são um caso es-
pecíﬁco de RNAs, na quais utilizam-se da operação matemática de convolução para cálculo de
próximas camadas, com ﬁltros (i.e. sequência de números usados na operação) sendo aplicado
a imagem por um mecanismo de ’janela deslizante’, onde o ﬁltro aplica operações sobre os pi-
xels as quais estão sobrepostos, ou seja, formam uma janela e este, após realizar a operação,
é deslizada para a próxima posição na imagem, gerando um pixel resultante por cada aplicação
do ﬁltro.
Uma das principais vantagens das CNNs em relação às RNAs no processamento de
imagens é a capacidade de aplicar os mesmos ﬁltros em diferentes regiões, permitindo a detec-
ção de padrões recorrentes ao longo da imagem. Isso é essencial, pois características visuais,
como bordas e texturas, podem aparecer em várias partes da imagem. Por exemplo, um ﬁl-
tro especíﬁco pode detectar linhas verticais independentemente de sua posição, o que torna a
extração de características mais eﬁciente e robusta (GOODFELLOW; BENGIO; COURVILLE,
2016; ALBAWI; MOHAMMED; AL-ZAWI, 2017).
A operação básica de convolução implementada por essas redes pode ser vista na Fi-
gura 5, onde vemos a ação do ﬁltro de convolução sobre as várias janelas. O padding referido
na Figura é o preenchimento de zeros na borda da imagem, com neste caso incluindo uma linha
acima, abaixo, uma à direita e uma à esquerda da matriz que representa a imagem. Sendo esse
apenas realizado como preparação a realização das operações subsequentes de Convolução. A
aplicação da convolução é realizada multiplicando cada valor da entrada com o elemento equi-
valente do Kernel da convolução e somando os produtos resultantes. A convolução tem uma
operação de "janela deslizante" conforme o passo (stride), com o caso da Figura 5 sendo um
passo de dois, resultando em um "pulo" de 2 em 2 pixels. Assim, o resultado da aplicação das
convoluções nas janelas é uma matriz 4 × 4. Em seguida, é realizado a operação de redução
de dimensionalidade MaxPool, que pega o maior elemento de cada sub-matriz 2 × 2, levando a
um resultado numa matriz de tamanho 2 × 2 (LI et al., 2021).


22
Figura 5 – Operações de uma Rede Neural Convolucional.
Fonte: (LI et al., 2021).
A Figura 6 mostra uma implementação convencional de uma CNN para o reconheci-
mento de dígitos manuscritos, com as suas diversas camadas de processamento, sendo que a
última camada é geralmente composta de uma rede fully connected. Cada camada de convo-
lução utiliza-se de uma função de ativação Unidades Lineares Retiﬁcadas, do inglês Rectiﬁed
Linear Unit (ReLU), que tem o funcionamento de passar os valores positivos sem transformação
e transformar os valores negativos para zero. A CNN recebe uma imagem na entrada e após
a última camada, apresenta o reconhecimento do caractere presente na imagem (O’SHEA;
NASH, 2015).
Figura 6 – Arquitetura de uma Rede Neural Convolucional.
Fonte: (O’SHEA; NASH, 2015).
A Figura 7 apresenta outro exemplo de uma CNN, desta vez aplicada à classiﬁcação
de objetos. Nela, é possível observar a realização das operações de convolução e pooling,
que processam os dados por meio de operações matemáticas realizadas sobre uma "janela"de
pixels.


23
Figura 7 – Exemplo de uma Rede Neural Convolucional.
Fonte: (ÇEVIK; BO˘gA, 2019).
As CNNs tem uma grande quantidade de aplicação, já sendo uma das rede neurais
artiﬁciais mais utilizadas atualmente, principalmente no campo de visão computacional, mas
com potencial de outras aplicações. Essas redes tem permitido resolver problemas não triviais
como reconhecimento facial e de objetos como alguns exemplos. Dessa maneira, as CNNs se
encontram em uma posição importante com utilização crescente (LI et al., 2021).
Para facilitar a utilização de Rede Neurais Artiﬁcias em diversos desses problemas, exis-
tem frameworks de inteligencia artiﬁcial que implementam uma grande variedade de recursos
utilizados em seu treinamento e utilização, exemplos incluem as bibliotecas tensorﬂow, pytorch,
caffe entre outras. Este trabalho utiliza a biblioteca Tensorﬂow como padrão de referencia para
as operações (DEVELOPERS, 2022).
Como as Redes Neurais Artiﬁciais são estruturas matemáticas, é necessário entender
as operações que são realizadas e a matemática envolvida.
2.2.2
Representação Matemática
Deﬁne-se, inicialmente, uma rede neural artiﬁcial convencional de múltiplas camadas, i.e.
contendo pelo menos uma camada oculta. Considera-se um vetor de entrada X de dimensão n,
que, conforme Seção anterior, é representado por uma série de neurônios (sem operação) e ca-
madas sucessivas H1, H2 . . . Hs com seus neurônios associados. Para cada neurônio em uma
camada subsequente, existem n pesos associados, que compõem um vetor W . O resultado
para esse neurônio é calculado conforme descrito na Equação 1.
Neurônio =
n
X
i=o
Wi · Xi
(1)
Perceba que uma camada inteira pode ser representada por uma multiplicação matricial
se representarmos o vetor de entradas X como uma matriz 1xn e o vetor de pesos W como uma
matriz nxm com cada coluna sendo o neurônio da camada escondida, conforme a Equação 2.
H = W · X
(2)


24
Dessa forma, se usarmos uma função de ativação σ, matematicamente a rede inteira
pode ser representada pela Equação 3.
O = σ(. . . · σ(W2 · σ(W1 · X)))
(3)
Dessa maneira, pode-se entender melhor a operação de convolução, supondo que te-
mos uma matriz de entradas X, com três dimensões que digamos sejam A×B×C, uma matriz
de pesos W com quatro dimensões que sejam F × D × E × C onde A e B são o tamanho da
imagem, C é a sua quantidade de canais (i.e. uma imagem RGB teria 3 canais, um para cada
cor), D e E são o tamanho do ﬁltro convolucional e F é a quantidade de ﬁltros. Fazendo a con-
volução X com W teria um resultado uma matriz H, essa operação seria conforme a Equação
4.
Percebe-se que de maneira equivalente, está se realizando a mesma operação que a
rede neural de perceptron de múltiplas camadas, porém cada neurônio está limitado a janela de
convolução.
Hi,j,f =
D
X
d=0
E
X
e=0
C
X
c=0
Wf,d,e,cXi+d,j+e,c
(4)
Uma visualização da operação pode ser vista na Figura 8 com um Tensor de Entrada
de tamanho N × M × K com a convolução de um Tensor de Filtros (i.e. Kernel) de tamanho
I × J × K resultando em uma imagem de tamanho (N −I + 1) × (M −J + 1) × 1. São
aplicados vários Filtros sobre a imagem e o resultado de cada um desses são conectados na
ultima dimensão, que é também chamado na literatura como a dimensão de canais ou features
map.
Figura 8 – Aplicação de um Filtro na operação de convolução
Fonte: Autoria própria (2025).


25
Funções de ativações não lineares são também uma parte fundamental a serem uti-
lizadas nas Redes Neurais Artiﬁcias em geral. Temos então a deﬁnição de duas funções de
ativação comuns que são a ReLU na Equação 5 e função Sigmoide (σ) na Equação 6.
ReLU(x) =





x se x > 0
0 caso contrário
(5)
σ(x) =
1
1 + e−x
(6)
As Figuras 9 e 10 mostram respectivamente os gráﬁcos resultantes das equações acima
dessas funções.
Figura 9 – Gráﬁco da função ReLU
Fonte: Autoria própria (2025).


26
Figura 10 – Gráﬁco da função Sigmoide
Fonte: Autoria própria (2025).
A operação de redução de dimensionalidade max pooling pode ser descrita conforme a
Equação 7, onde a matriz X é a matriz de entrada (i.e. a imagem original), a matriz P é a janela
de onde será aplicado a operação e a matriz H sendo a matriz com o resultado. Observe que
essa operação seleciona o elemento/neurônio que está mais ’ativo’, i.e. valor mais alto.
H(i, j) = maxm,n em Pi,jXm,n
(7)
Essas são as operações básicas para a implementação do processo de inferência. Este
trabalho não aborda o processo de treinamento porém esse em suma consiste em primeira-
mente calcular uma função de erro com os valores reais conhecidos, em seguida calcula-se os
gradientes, i.e. vetor das derivadas parciais, das camadas sobre a função de erro e então esses
gradientes são utilizados em algoritmos de otimização para atualização dos pesos.
Conforme explicado, as ANNs tem alta complexidade computacional, envolvendo ope-
rações matemáticas complexas. Para garantir a execução rápida e eﬁcaz dessas, é necessário
que essas estruturas matemáticas sejam representadas por estruturas computacionais adequa-
das.
2.2.3
Representação Computacional
Para que sejam implementada as redes neurais em sistemas computacionais, é neces-
sário ter uma maneira de representar Tensores computacionalmente. Tensores são generaliza-
dos como matrizes de várias dimensões, porém em sistemas reais não é possível utilizar essa


27
representação diretamente devido a limitação do espaço de endereçamento ser apenas de uma
dimensão, i.e. uma ﬁta.
Em suma, existem duas implementações usuais de representação dos tensores em me-
mória que são o Channel First e Channel Last, na qual se tem tensores respectivamente com
Dimensões Channel × Height × Width e Height × Width × Channel. Essas representações
podem ser vistas na Figura 11 que mostra as duas organizações de memória de uma ima-
gem RGB com quatro pixels coloridos (três valores por pixel, R, G e B) (MAI; FEDYUNIN; WEI,
2022). Cada uma dessas tem as suas próprias vantagens e desvantagens relativo a arquiteturas
de cada dispositivo como CPU e GPU e as necessidades das operações envolvidas. Um exem-
plo simples da representação mudar a eﬁciência computacional, seria a contagem do número
de pixels em uma imagem RGB que tem a sua cor vermelha acima de um nível, neste caso
a representação de Channel First é uma escolha melhor como o acesso se torna sequencial,
simpliﬁcando as computações realizadas e possibilitando paralelismo.
Figura 11 – Layout da Memória Física.
Fonte: (MAI; FEDYUNIN; WEI, 2022).
Conforme pode ser visto, a escolha de representação traz consequências de como o
paralelismo pode ser realizado pelas operações da Rede Neural Artiﬁcial.
2.2.4
Paralelismo
A operação de convolução é uma operação altamente paralelizável, com a literatura
referenciada classiﬁcando o paralelismo da convolução em três tipos principais. Esses podem
ser vistos na Figura 12, que são Input Channel Parallelism, Output Channel Parallelism e
Pixel Parallelism (YANG et al., 2023).
As deﬁnições desses tipos de paralelismo são:
• Input Channel Parallelism (ICP): Paralelismo sobre o produto do Tensor de entrada
com os ﬁltros nas dimensões dos canais (última dimensão).
• Output Channel Parallelism (OCP): Paralelismo de operações de convoluções de
ﬁltros diferentes sobre a entrada.
• Pixel Parallelism (PP): Paralelismo sobre diferentes elementos do tensor de Entrada.


28
Na Figura 12 temos um exemplo com uma imagem (topo superior esquerdo) 4 × 4 × 3
com uma matriz de ﬁltros (topo superior direito) 2 × 2 × 3 × 2, sendo que a última dimensão
representa que são dois ﬁltros de 2 × 2 × 3 concatenados.
No ICP (Input Channel Paralelism) para este caso, são feitas 3 multiplicações escalares
simultaneamente (pontilhados em verde), percebendo-se que está sendo aplicado sobre os três
canais da imagem ao mesmo tempo, paralelamente.
No OCP (Output Channel Paralelism) para este caso, os dois ﬁltros estão sendo aplica-
dos simultaneamente, fazendo com que se tenha 6 multiplicações escalares, isto é 3 multiplica-
ções (oriundas do ICP) para cada ﬁltro ao mesmo tempo/paralelamente.
No PP (Pixel Parallelism) para este caso, é aplicado sobre a janela de convolução 2 × 2
com cada pixel sendo multiplicado em paralelo, resultando em 24 multiplicações simultâneas,
isto é 3 (ICP) · 2(OCP) · 4(PP).
No exemplo da Figura 12, ao utilizar o ICP, são realizadas 3 operações de multiplicação
simultâneas. Ao utilizar o OCP são realizadas 2 operações de convoluções em paralelo. E ao
utilizar o PP, são realizadas as operações anteriores em 4 pixels simultaneamente.
Perceba-se que há reutilização de dados, sendo que os mesmos dados usados no ICP,
podem ser usados para alimentar vários ﬁltros. Essa reutilização de dados é importante para
que as operações paralelas sejam implementadas com eﬁciência computacional, tendo em vista
que não há a necessidade de recarregar esses dados da memória do sistema.


29
Figura 12 – Paralelismo da Operação de Convolução.
Fonte: (YANG et al., 2023).
Quando ICP ou OCP implementados forem maiores do que a CNN tem disponível em
canais ou ﬁltros respectivamente, é utilizado zero padding, isto é a inserção de zeros nos veto-
res, para manter o tamanho necessário. Por exemplo, para uma implementação com ICP igual
a 4 e a entrada da rede só possuir 3 canais, i.e. imagem RGB, em uma camada, será utilizado
um vetor [R, G, B, 0] para cada pixel ao invés de utilizar o vetor real do pixel [R, G, B].
Para a utilização apropriada desses paralelismos, é necessário plataforma de execução
apropriada visto que nem todas tem a habilidade de aplicar esses paralelismos na execução de
uma CNN. Uma plataforma que tem sido bastante explorada para execução de redes neurais ar-
tiﬁciais é a FPGA, devido a sua reconﬁgurabilidade permitir que sejam deﬁnidos os paralelismo
desejados (SCHÜTZ et al., 2019).
2.3
Field Programmable Gate Array
Esta seção apresenta os conceitos teóricos sobre os dispositivos de FPGA, começando
pela seção 2.3.1 que apresenta uma introdução geral sobre estes dispositivos e as suas utili-


30
zações enquanto que as seções 2.3.2, 2.3.3 e 2.3.4 apresentam respectivamente sobre com-
ponentes especíﬁcos de Blocos de Lógica Reconﬁguráveis, Processadores de Sinais Digitais e
Elementos de Memória da arquitetura Cyclone V (Intel Corporation, 2023; TERASIC, 2018), que
foi o modelo de FPGA escolhido para realizar as simulações/design das redes neurais artiﬁciais
neste trabalho.
2.3.1
Introdução Geral
FPGA são dispositivos de circuito lógicos reconﬁguráveis, cujas características permi-
tem que se consiga cobrir as mais diversas aplicações como roteadores, instrumentos especi-
alizados, etc (GANDHARE; KARTHIKEYAN, 2019). Uma vez que é implementado ao nível de
hardware reconﬁgurável, permite alto desempenho, baixa latência e baixo uso de energia em
comparação a um software implementado em um processador genérico. A grande vantagem da
FPGA é a sua mudança de conﬁguração ’em campo’, permitindo com que seja implementado
qualquer circuito após a fabricação do circuito integrado. Comparativamente, tem-se os Circui-
tos Integrados de Aplicação Especíﬁca, do inglês Application Speciﬁc Integrated Circuit (ASIC)
nos quais o circuito integrado é ﬁxo a partir da fabricação (FAROOQ et al., 2012).
Devido a essa ﬂexibilidade, existe potencial de otimização a problemas que podem ser
especíﬁcos demais para ter um mercado se implementados com ASIC. Isso pode ser demons-
trado com um exemplo de bloco aceleradores de criptograﬁa, se no ASIC for implementado um
circuito que implementa o algoritmo AES-128 e houver necessidade de troca para o algoritmo
SHA-256 devido a mudança de mercados, o circuito não pode mais ser utilizado, tendo que a
computação deve ser realizada em um processador por exemplo. No caso da FPGA, bastaria
reconﬁgurar ela com um circuito para SHA-256 (SKAHILL, 1996).
A Figura 13 mostra como uma FPGA é estruturada de maneira teórica, constituindo
principalmente de Blocos Lógicos Conﬁguráveis ou Conﬁgurable Logic Blocks (CLB) conecta-
dos em uma rede de roteamento formada por Caixas de Conexões (Connection Box) e Caixas
de Roteamento (Switch Box). A implementação do roteamento depende muito do fabricante e
da arquitetura. Os CLBs são responsáveis pela implementação de pequenos circuitos combi-
nacionais e sequenciais como por exemplo portas lógicas ou registradores, enquanto que os
elementos de roteamento permitem que esses pequenos elementos sejam combinados em cir-
cuitos maiores (Intel Corporation, 2023).


31
Figura 13 – Arquitetura Convencional de uma FPGA.
Fonte: (GANDHARE; KARTHIKEYAN, 2019).
A Figura 14 apresenta uma visão de uma seção de uma arquitetura de FPGA da fabri-
cante Intel chamada de Cyclone V. No caso, pode ser visto que a organização é consistente com
a teórica, apresentada com CLBs e elementos de roteamento entre elas. Porém, é perceptível
que nesta arquitetura as CLBs são organizadas em colunas verticais chamadas de Arranjo de
Blocos Lógicos (Logic Array Blocks - LAB). Adicionalmente, os elementos de roteamento são
separados em roteamento global, para conectar um CLB com qualquer outro do dispositivo, e
roteamento local, para conectar um CLB com os seus vizinhos. Isto é necessário conforme os
recursos de roteamento globais são limitados e mais custosos na sua utilização devido a sinais
físicos terem que viajar distâncias maiores.


32
Figura 14 – Visão de uma implementação de FPGA.
Fonte: (Intel Corporation, 2023).
Em suma, FPGAs são dispositivos que utilizam de Blocos Conﬁguráveis que implemen-
tam circuitos booleanos, as quais são roteadas entre si por uma grande rede conﬁgurável. Cada
fabricante deste dispositivos implementa esses componentes de maneira diferente, necessi-
tando que seja estudado cada implementação para utilizar os recursos dos componentes ou
utilizar componentes implementados além dos convencionais.
2.3.2
Bloco Lógico Reconﬁgurável
O componente de Bloco Lógico Reconﬁgurável é o principal componente a ser utilizado
quando se cria circuitos para FPGAs, não sendo instanciado diretamente pelo engenheiro que
está criando o circuito mas pela ferramenta de compilação especíﬁca para FPGAs chamado de
Fitter que é responsável por traduzir as expressões lógicas booleanas do circuito descrito em
componentes de FPGA e rotear estes. A Figura 15 mostra os principais componentes enume-
rados de um CLB (AMD Xilinx, 2010; AMD Xilinx, 2023).


33
Figura 15 – Implementação de um CLB na Arquitetura Cyclone V.
Fonte: Adaptado de Intel Corporation (2023).
Os componentes enumerados na Figura 15 são conforme a descrição abaixo.
1. Entradas do circuito combinacional alimentado a Tabelas de Consultas (Lookup Tables
- LUT) que consistem em pequenos elementos de memória com o resultado da expres-
são lógica embutida, de forma que as entradas servem para selecionar o resultado.
Existem diversas LUTs que podem ser conﬁguradas para implementar LUTs com mais
entradas ou ter funcionamento independente entre si, por exemplo sendo possível con-
ﬁgurar duas LUT de 4 entrada totalmente independente ou duas LUT de 6 entradas
com duas entradas compartilhadas. Essa grande versatilidade de conﬁguração, per-
mite que se tenha alocação eﬁciente dos recursos pelas diversas expressões lógicas
com diferente números existentes no circuito.
2. Circuitos dedicados para implementar adição, com sinais especíﬁcos a roteamento ver-
tical a bloco adjacentes, permitindo que a operação de adição seja eﬁcientemente im-
plementada em colunas de CLBs.
3. Consiste em registradores que servem como elemento de armazenamento para a im-
plementação de circuitos sequenciais, com a sua utilização sendo opcional e imple-
mentados por ﬂip ﬂops D. Os valores armazenados destes, podem servir como entrada
nos circuitos combinacionais implementado pelas LUTs.


34
4. Sinais de controle oriundos por coluna vertical de CLBs que consiste em três sinais
clock e seus respectivos sinais de clock enable e sinais de controle de registradores de
load e reset síncronos e assíncronos. Isto permite que em determinada circunstâncias
seja transferida lógica combinacional que seria implementada por LUTs para dentro
dos registradores.
As conﬁgurações e a utilização diferentes dos recursos ocorrem devido aos diversos
multiplexadores dentro da CLB, que podem ser visto na Figura 15, representados como multi-
plexadores sem sinal de seleção aparente.
Conforme visto os CLBs são blocos muito versáteis que podem ser conﬁgurados para
realizar uma grande quantidade de operações, mas existem operações como por exemplo mul-
tiplicação que não se mapeia de maneira eﬁcientemente a estes blocos, a qual ocasiona em
grande utilização de recursos de baixa frequência dos circuitos resultantes. Consequentemente,
fabricantes de FPGAs adicionam blocos especíﬁcos que são eﬁcientes para estas operações
(BRAVO-MUÑOZ; GARDEL-VICENTE; LÁZARO-GALILEA, 2020), apresentado a seguir.
2.3.3
Bloco DSP
FPGAs são muito utilizadas para aplicações de controle e processamento de sinais digi-
tais onde se é necessário realizar muitas operações matemáticas no menor tempo possível, de
tal maneira que os fabricantes deste dispositivos implementam blocos especiais de Processa-
dor de Sinais Digitais, do inglês Digital Signal Processor (DSP) para facilitar essas aplicações
(BUENO et al., 2008). A Figura 16 mostra o bloco de DSP da arquitetura Cyclone V com os
principais elementos deste bloco destacados.


35
Figura 16 – Implementação de um bloco DSP na Arquitetura Cyclone V.
Fonte: Adaptado de Intel Corporation (2023).
Com os componentes enumerados sendo:
1. Banco de registradores de entrada do bloco, que tem utilização opcional. Algumas
entradas tem registradores de atraso que podem alimentar outras entradas com um
atraso de um ciclo de clock.
2. Circuito de multiplicação implementado diretamente. Cada bloco possui dois multipli-
cadores, estes podendo ser conﬁgurados de diversas maneiras conforme as neces-
sidades de usos, se tendo três casos principais. O primeiro caso sendo multiplicação
de números de 9 bits por 9 bits tendo 3 multiplicações por bloco no total. O segundo
caso sendo multiplicação de números de 18 bits por 19 bits tendo uma multiplicação
por multiplicador, ou seja duas multiplicações no total. E o último caso é a multiplicação
de números de 27 bits por 27 bits tendo uma multiplicação no total (sendo necessário
adicionar o resultado dos dois multiplicadores para realizar esta operação).
3. Circuitos de adição pós multiplicação que consiste em dois circuitos separados que
primeiro realizam a adição do produto e depois realiza adição com um acumulador ou
entrada externa. A utilização desses dois circuitos é conﬁgurável.
4. Registrador de saída que pode ser utilizado como acumulador. Assim como os outros
registradores, o seu uso é opcional. O tamanho desses registradores são de 64-bit,
necessário para que possa realizar acumulação de produtos.


36
Além dos elementos citados existem outros que podem ser conﬁgurados de diversas
maneiras porém não são de uso comum, com a conﬁguração mais comum sendo para que
realize operações de multiplicação e adição.
Como estes componentes são eﬁcientes em processamento de dados matemáticos e
conﬁguráveis para implementação de diversas operações matemáticas complexas como multi-
plicação de matrizes é necessário ter muitos dados armazenados, poderia se armazenar estes
dados em registradores dos CLBs porém não é uma maneira eﬁciente e rápida. Devido a isto,
se tem componentes especíﬁcos para armazenamento de memória maiores distribuídos no dis-
positivo da FPGA, para que se possa alimentar dados para os resto dos circuitos.
2.3.4
Elemento de Memória
Para diversas aplicações em computação, existe a necessidade de ter armazenamento
de valores em memórias como por exemplo na realização de operações matemáticas complexas
com muitas constantes como ﬁltros convolucionais ou Redes Neurais Artiﬁcias ou até mesmo
para aplicações de Redes, conforme é necessário ter o pacote inteiro em memória. Devido a
isto, fabricantes de FPGA implementam blocos distribuídos na FPGA para suprir essa demanda
de maneira eﬁciente.
Na arquitetura Cyclone V este bloco é chamado de M10K que é um bloco de memória,
organizado em colunas conforme os outros componentes apresentados, contendo 10240 bits
(desta maneira tendo o nome de 10K) sendo conﬁgurável de tamanho de palavras em bits e
quantidade de palavras com limite de 40 bits para o tamanho de palavra. Para casos onde
for necessário mais espaço de memória ou palavras maiores, pode juntar vários blocos M10K
aﬁm de ser realizada a conﬁguração desejada. Além dessas conﬁgurações, existem modos de
operação em relação a portas de entrada e escrita, que podem ser visualizadas na Figura 17.
Figura 17 – Modos possíveis do bloco M10K.
Fonte: Adaptado de Intel Corporation (2023).
Os três diferentes modos mostradas pela Figura são:


37
(a) Modo de uma porta compartilhada para leitura e escrita. O barramento address especí-
ﬁca o endereço onde será realizada a operação e o sinal wren para que seja realizado
uma escrita ou leitura, no caso de escrita o valor do barramento data é transferido
para o endereço especiﬁcado e no caso de leitura, o resultado estará disponível no
barramento Q.
(b) Modo de duas portas simples com uma porta de escrita e uma porta de leitura. Neste
modo o barramento address é divido em dois, sendo wraddress para o endereço de
escrita e rdaddress para o endereço de leitura, desta maneira permitindo com que
operações de leitura e escrita sejam realizadas ao mesmo tempo em locais diferentes
da memória.
(c) Modo de duas portas verdadeiro, com cada uma tendo a mesma capacidade de leitura
e escrita conforme o modo de uma porta compartilhada.
Enquanto estes componentes contém grande quantidade de memória, existem aplica-
ções como Redes Neurais Artiﬁciais que tem necessidade de memória além da providenciada
pelo dispositivo de FPGA para que sejam armazenados os pesos e resultados das camadas
intermediárias destas redes. Devido a isto, existe a necessidade de técnicas para a utilização
eﬁciente do espaço em memória. Para isso, é necessário utilizar técnicas de quantização, que
permitem a representação de números de ponto ﬂutuante através da utilização de menos bits
por valor. Técnicas de quantização são discutidas na próxima sessão.
2.4
Quantização de Redes Neurais
Nesta seção será apresentada a fundamentação teórica e aplicação da técnica de quan-
tização sobre Redes Neurais Artiﬁciais, com a seção 2.4.1 sendo uma breve introdução a for-
mato numéricos usados por computadores e os desaﬁos associados a esses. Em seguinte,
na Seção 2.4.2 é abordada a técnica de quantização e como ela é aplicada. A seção 2.4.3
apresenta uma breve explicação sobre propagação de erros introduzidos pela metodologia de
quantização. A seção 2.4.4 apresenta os efeitos da técnica de quantização a modelagem ma-
temática das Redes Neurais Artiﬁciais. A seção 2.4.5 realiza uma comparação de técnicas de
quantização utilizadas em alguns trabalhos estudados.
2.4.1
Formatos Numéricos
Sistemas computacionais operam sobre palavras de símbolos de um alfabeto, os quais
não tem um signiﬁcado inerente, a maneira que é adicionado o signiﬁcado a essas palavras
para que representem números é por formatos numéricos que consistem em sistemas de repre-
sentação de números pelas diferentes palavras possíveis. Em computadores binários modernos


38
são utilizados dois formatos principais que são integer (inteiros) e ﬂoating point (ponto ﬂutuante)
representado por símbolos binários (STOKES, 2007).
O formato numérico integer é o mais utilizado, que representa números do Conjunto
de Inteiros, as quais chamamos de signed integer. em um formato numérico que representa
ambos os inteiros positivos e negativos e unsigned integer que apenas representam inteiros
positivos. A terminologia encontrada na literatura é de que signed integer é denominado como
int e unsigned integer como uint e em ambos os casos adicionando a quantidade de bits da
representação especíﬁca no ﬁnal. Por exemplo, int16 signiﬁca um signed integer de 16 bits e
uint32 signiﬁca um unsigned integer de 32 bits.
Porém, é notável que não se pode representar números racionais ou reais com o formato
de inteiro, para isso são usados os formatos numéricos denominados de ﬂoating point, que
transformam números reais em uma representação aproximada. Esse processo é chamado de
quantização, oriundo do campo de conhecimento de processamento de sinais digitais, onde
é utilizado na etapa de conversão de analógico para digital (GRAY; NEUHOFF, 1998). Neste
trabalho, se utiliza a quantização em relação a mudança de representação numérica.
Para os formatos numéricos ﬂoat, existe uma grande variedade de nomenclatura dife-
rente para descrever as diversas variações existentes, neste trabalho é usado o termo ﬂoat
seguido pelo número de bits para denominar pontos ﬂutuantes do padrão IEEE 754 (LIANG et
al., 2021; LIU et al., 2021; IEEE. . . , 2019).
A deﬁnição de uma representação matemática em ﬂoating point é dada pela Equação
8 para um número com exponente e e tamanho s de bits em sua mantissa. Percebe-se que
enquanto é possível representar exatamente uma grande quantidade de valores reais, devido a
sua natureza discreta não é possível representar todos os valores contínuos, caracterizando se
de uma quantização (GOLDBERG, 1991).
 s−1
X
n=0
bitn · 2−n
!
· 2e
(8)
Para exempliﬁcar a representação matemática em ﬂoating point melhor, será utilizado
exemplos com base 10, conforme M ·10e onde M é a mantissa e e é o exponente, por exemplo,
1.15 · 102 para representar o número 115, tendo M = 1.15 e e = 2. A Mantissa para o exemplo
em base 10 deve ser um número entre [1, 10), para mantissa menores que 1, o número é
chamada de subnormal e é uma exceção ao caso geral. Pertinente observar que é necessário
que esse seja uma exceção como 0.115 · 103 = 1.150 · 102, o que signiﬁcaria que um número
poderia ter várias representações nesse formato (MULLER et al., 2018; GOLDBERG, 1991).
Tendo em vista a representação, é perceptível que as operações de ﬂoating point são
mais complexas do que operações com números inteiros. A operação de multiplicação, em suma
consiste em primeiro multiplicar as mantissas e somar os exponentes, em seguida será neces-
sário normalizar o número e arrendondar ele para a quantidade de dígitos desejada (MULLER
et al., 2018; GOLDBERG, 1991).


39
A Equação 9 exempliﬁca o processo de multiplicação de dois números representados
em ﬂoating point (base 10), cada um com três dígitos signiﬁcativos: 981 e 5020. O número
981 é representado por sua mantissa (9.81) e seu expoente (2), ou seja, 9.81 · 102 = 981. De
maneira análoga, o número 5020 é representado por sua mantissa (5.02) e seu expoente (3).
Após a multiplicação das mantissas, e a soma dos expoentes, o número resultante (49.2462·105
é novamente convertido para o formato de mantissa com três dígitos signiﬁcativos: 4.92 · 106.
(9.81 · 102) · (5.02 · 103) = (9.81 · 5.02) · 102+3
= 49.2462 · 105
= 4.92 · 106
(9)
A operação de adição é ainda mais complicada dado que os números que queremos
realizar a operação sobre, não necessariamente tem o mesmo exponente. Primeiramente é
necessário transformar o número com menor exponente para um número subnormal com ex-
ponente igual ao maior expoente. Em seguida adicionamos as mantissas, e ﬁnalmente norma-
lizamos e arrendondamos para a quantidade de dígitos do modelo de representação (MULLER
et al., 2018; GOLDBERG, 1991). A Equação 10 demonstra o processo.
(9.81 · 102) + (9.5 · 103) = (0.981 · 103) + (9.5 · 103)
= (0.981 + 9.5) · 103
= 10.481 · 103
= 1.05 · 104
(10)
Conforme apresentado, o formato de ﬂoating point apresenta diversos desaﬁos, devido
a sua complexidade de implementação e altos custos energéticos e dessa maneira não se
demonstra adequado para toda aplicação. O primeiro ponto é importante para a utilização em
dispositivos de FPGAs a sistemas embarcados, no qual não se tem uma implementação nativa
em hardware dessa representação numérica (LIBANO et al., 2020).
Ao segundo ponto, pode-se ver pela Tabela 1, uma comparação em diversas tipos de
operações com diferentes formatos numéricos, na qual se pode perceber que as operações com
ﬂoating points são mais custosas à eﬁciência energética e computacional em relação a outros
formatos numéricos. Consequentemente teve-se a necessidade de usar técnicas alternativas
para representação numéricas, principalmente para Rede Neurais Artiﬁciais, na qual se tem
grande quantidade de operações de soma e multiplicação (WU et al., 2020).


40
Tabela 1 – Eﬁciência energética de operações sobre processo de fabricação de 45nm, em pJ (pico
Joules)
Formato
Gasto de Energia com Adição (pJ)
Gasto de Energia com Multiplicação (pJ)
int8
0.03
0.2
int32
0.1
3.1
ﬂoat16
0.4
1.1
ﬂoat32
0.9
3.7
Fonte: (HOROWITZ, 2014).
Devido a esses problemas, existem metodologias alternativas em utilização de formatos
numéricos diferentes para representar números reais, em especial utilizando o formato de intei-
ros como base, já conforme constatado são os mais utilizados na computação. A metodologia
utilizada para essa quantização é chamada de esquema de quantização na literatura (GERSHO,
1978).
2.4.2
Esquema de Quantização
Existem diversos esquemas de quantização encontrados na literatura, com a utilização
da quantização aﬁm por int8 como esquema de quantização neste trabalho. Conforme o nome,
este esquema utiliza o formato numérico de int8 como base, o que traz diversos benefícios,
como a eﬁciência computacional sobre as operações do formato numérico e o menor tamanho
utilizado do formato na memória. Este último ponto porém é um compromisso em relação a
utilização eﬁciente da memória em relação com a precisão do formato, pois conforme aumenta
a quantidade de bits a precisão aumenta mas a utilização de memória se torna menos eﬁciente,
a Figura 18 apresenta a diferença na faixa de valores dos formatos ﬂoat32 e int8. Consequen-
temente, é importante utilizar um esquema de quantização adequado ao problema em questão
para minimizar perdas em precisão.
Figura 18 – Comparação das faixas diferentes de ﬂoat32 e int8
Fonte: Autoria própria (2025).
A deﬁnição do esquema de quantização aﬁm é dado pela Equação 11, para um número
real X, e parâmetros de escala S e ponto zero Z para obter-se um valor quantizado Q, tal que
Q ∈Z. Tendo a representação Q do valor real, podem ser realizadas operações de inteiros


41
sobre ele e obter o resultado correto (JACOB et al., 2017). Pode se perceber que não é possível
representar todos os valores reais utilizando essa técnica, com a diferença do valor real ao valor
quantizado sendo denominada de erro de quantização.
X = S · (Q + Z)
(11)
Os parâmetros de escala S e o ponto zero Z determinam a faixa de valores que pode ser
representada pela quantização. Pode se obter uma faixa ao realizar operações reais e observar
em qual faixa que os valores estão contidos, e ao ter essa faixa de valores [A, B] os parâmetros
S e Z podem ser calculados respectivamente pelas Equações 12 e 13 onde bits se refere a
quantidade de bits do formato numérico utilizado. A utilização do parâmetro Z é opcional, e
quando ele é utilizado com valor zero a quantização é chamada de simétrica e para qualquer
valor diferente de zero é chamada de assimétrica.
S = (B −A)
2bits −1
(12)
Z = −round(A · S) −2bits−1
(13)
A Figura 19 mostra um exemplo de mapeamento da quantização por ﬂoat32 e quantiza-
ção aﬁm simétrica de int8.
Figura 19 – Quantização de [-1, 1) de ﬂoat32 a int8
Fonte: Autoria própria (2025).
Conforme visto técnicas de quantização apresentam erros intrínsecos a modelagem, e
quando são realizadas operações sobre os números quantizados, os erros se propagam, o que
causa uma necessidade de reduzir os erros em sequência principalmente nas Redes Neurais
Artiﬁciais, que necessitam realizar muitas operações.
2.4.3
Erro por operação em Quantização
A propagação de erros é uma análise estática para veriﬁcar a conﬁabilidade dos dados,
representada por uma incerteza. No caso da quantização, se tem erros introduzido pela técnica
em si, por exemplo ao utilizar uma metodologia de quantização com base 10 e três dígitos
para representar o número real 1634, se obterá o número quantizado 1.63 · 103 com o erro de


42
quantização sendo ±0.01. Porém, além desses erros intrínsecos, em quantização pode se ter
erros adicionais ao realizar operações matemáticas, i.e. além da propagação de erros.
Isto pode ser exempliﬁcado ao calcular a oitava potência do número 1.21, deve-se elevar
o número ao quadrado, por três vezes consecutivas. Este cálculo pode ser visto na Equação 14
onde round é a operação de arrendondamento, necessária para que seja preservado o formato
numérico e se terá um erro de 0.05 sobre o resultado real 4.59. Perceba que o arrendondamento
é uma operação que realiza uma quantização e dessa maneira se está introduzindo novamente
erros de quantização.
(1.21 · 100)2 = round(1.4641 · 100) = 1.46 · 100
(1.46 · 100)2 = round(2.1316 · 100) = 2.13 · 100
(2.13 · 100)2 = round(4.5369 · 100) = 4.54 · 100
(14)
Porém, existe outra abordagem que é de apenas utilizar o arrendondamento na opera-
ção ﬁnal realizada sobre o número quantizado, a Equação 15 demonstra o processo. O erro
é reduzido consideravelmente sobre a metodologia anterior, porém precisa realizar operações
com números quantizados com mais dígitos sendo retornado ao formato inicial. Esta melhoria
na acurácia da modelagem traz um ganho maior do que o aumento da complexidade computa-
cional no caso de Redes Neurais Artiﬁciais, devido a grande quantidade de operações de soma
e multiplicação envolvidas.
(1.21 · 100)2 = 1.4641 · 100
(1.4641 · 100)2 = 2.14358881 · 100
(2.14358881 · 100)2 = round(4.59497298636 · 100) = 4.59 · 100
(15)
Realizar essas operações com número maior de dígitos pode implicar em maior utiliza-
ção de recursos de hardware, porém em muitos sistemas como FPGAs, esse custo é pequeno
em comparação ao ganho de precisão, conforme esse dispositivo já foi implementado com es-
sas aplicações em mente até determinadas quantidade de dígitos mas isso não é verdade
em todos os sistemas de hardware. Dessa maneira, essa metodologia de manter a precisão o
máximo possível irá variar de dispositivo a dispositivo veriﬁcado, por exemplo em um microcon-
trolador pode ser avaliado que dados os recursos de hardware implementados, realizar todos
os cálculos com precisão não é possível de realizar eﬁcientemente mas se pode calcular a se-
gunda multiplicação ainda com certa eﬁciência e ao aplicar o arrendondamento no resultado
dessa segunda multiplicação se terá 2.14 e utilizando esse número para a multiplicação ﬁnal, o
resultado irá ser 4.58, o que tem apenas um erro de 0.01 sobre o resultado real de 4.59.


43
Sistemas reais utilizam essa metodologia com números quantizados binários, no qual
para ser representado o resultado das operações, no caso da multiplicação o número resultante
terá quantidade de bits iguais a soma dos termos do produto e na adição o número resultante
terá bits iguais ao maior dos termos mais um.
Conforme visto, esta técnica é particularmente útil para implementação de Rede Neu-
rais Artiﬁcias, porém existem peculiaridades desta aplicação de quantização. Notando que esta
abordagem é a mesma utilizado por instruções denominadas de Fused Multiply Add que exe-
cutam a = b + (c · d) como uma única operação (QUINNELL; SWARTZLANDER; LEMONDS,
2007).
2.4.4
Quantização em Redes Neurais Artiﬁciais
Como Redes Neurais Artiﬁciais realizam operações sobre tensores, é necessário con-
siderar duas peculiaridades que são os efeitos da quantização sobre as operações e sobre os
tensores em si. As operações principais de Redes Neurais Artiﬁciais sejam de neurônio tradicio-
nal ou convolução podem ser representadas por uma soma de produto conforme a Equação 16,
com o neurônio tradicional sendo mapeado diretamente para isto e a convolução necessitando
de combinar os somatórios (KLUSKA; ZI ˛EBA, 2020; JACOB et al., 2017; PERI; PATEL; PARK,
2020).
Yj =
X
i
(Xi · Wi,j)
(16)
Quando essas operações são utilizadas sobre números quantizados, tem-se a Equação
17. É notável que a quantidade de computação necessária aumentou em comparação com a
equação não utilizando valores quantizados.
Sy · (Yj −Zy) =
X
i
(Sx · (Xi −Zx) · Sw · (Wi,j −Zw))
(17)
Porém a equação pode ser simpliﬁcada em relação a Yj, o valor desejado, conforme
demonstrada pela Equação 18. Perceba que dos quatro somatórios, o terceiro e quarto são
constantes e podem ser pre-calculados como os pesos e parâmetros de quantização não mu-
dam durante o processo de inferência, com o primeiro somatório sendo o cálculo da operação
desejada em si mas ainda se tem um segundo somatório a mais a ser calculado. Um método
utilizado é aplicar a quantização simétrica sobre os pesos, isto é Zw = 0 o que eliminará o
segundo somatório.


44
Sy · (Yj −Zy) =
X
i
(Sx · (Xi −Zx) · Sw · (Wi,j −Zw))
Yj = Zy + Sx · Sw
Sy
 X
i
(Xi · Wi,j) −
X
i
(Xi · Zw) −
X
i
(Wi · Zx) +
X
i
(Zx · Zw)
!
(18)
Sendo deﬁnido para os pesos W a usarem a quantização simétrica e substituindo os
valores constantes por K, obtem-se a Equação 19 onde a complexidade computacional dos
somatórios se reduz a apenas uma adição de uma constante a mais em termos de quantidade
de operações.
Yj = Zy + Sx · Sw
Sy
 X
i
(Xi · Wi,j) + K
!
(19)
Observe que na Equação 19 se tem o termo Sx·Sw
Sy
que é um número real multiplicando
o resultado da operação quantizado, porém essa multiplicação e divisão de números real é
contra o objetivo de se utilizar apenas operações de inteiros na quantização. Para resolver
este problema, este termo pode ser representado conforme a Equação 20 onde o termo M é
representado como 2−n · M0 com a escolha do número inteiro n tal que 2−n > M e M ≥
2−(n−1), consequentemente o termo M0 será um número real que vai estar no intervalo [0.5, 1],
e esse número então será quantizado para um inteiro na faixa [-1, 1). Fazendo uma analogia, é
equivalente a extrair a mantissa e expoente de um número em ponto ﬂutuante. Dessa maneira
se pode reduzir a multiplicação e divisão de valores reais para uma multiplicação de inteiros e
operação de deslocamento (JACOB et al., 2017).
M := Sx · Sw
Sy
= 2−n · M0
(20)
Substituindo a Equação 20 na Equação 19 se terá a Equação 21.
Yj = Zy + 2−n · M0
 X
i
(Xi · Wi,j) + K
!
(21)
É notável que na Equação 21 estão sendo realizado dois processos, o primeiro sendo a
operação da Rede Neural Artiﬁcial em si conforme a Equação 22 que resultará em um número
quantizado com escala S = Sx · Sw e ponto zero Z = −P
i(Wi · Zx) e o segundo processo
é a conversão deste valor para a representação ﬁnal quantizada com escala S = Sy e ponto
zero Z = Zy. Esta separação é necessária para que o processo de operação seja calculado


45
com a quantidade de bits necessária para reduzir os erros como descrito na subseção 2.4.3
enquanto que o processo de conversão transforme o valor quantizado para o formato original,
o que é análogo a função de arrendondamento na seção anterior. As Equações 22, 23 e 24
mostra como obter a Equação 21 a partir das anteriores.
O(X, W) =
X
i
(Xi · Wi,j) + K
(22)
C(X) = Zy + 2−n · M0 · X
(23)
Yj = C(O(X, W))
(24)
Portanto, há uma maneira eﬁciente de realizar operações sobre valores quantizados,
porém não foi visto como a quantização é aplicada sobre os tensores. Existem duas maneiras
típicas que são a quantização por tensor (per tensor quantization em inglês), na qual a mesma
quantização é aplicada sobre o tensor inteiro, e quantização por eixo (per axis quantization), que
consiste da quantização ser diferente sobre elementos de um eixo escolhido. A Figura 20 ilustra
isso com o tensor de duas dimensões a esquerda, sendo aplicado a quantização por tensor e
o tensor a direita sendo aplicada a quantização por eixo com as linhas sendo escolhidas como
eixo a serem aplicada a quantização.
Figura 20 – Exemplo de aplicações de esquema de quantização.
Fonte: Autoria própria (2025).
A escolha da quantização por eixo possui vantagem em termo de precisão, pois os
parâmetros de escala e ponto zero podem ser calculados a partir de distribuições com menor
variância. Porém é notável que esta escolha pode afetar a Equação 17 e consequentemente
toda a lógica desenvolvida sobre esta, pois dividiria o somatório em diversas partes, um exemplo
pode ser visto na Equação 25 ao aplicar quantização por eixo sobre a entrada X.
Sy(Yj −Zy) =
k
X
i
(Sx,1(Xi−Zx,1)Sw(Wi,j −Sw))+
n
X
k
(Sx,2(Xk−Zx,2)Sw(Wk,j −Sw)) (25)
Por consequência, a quantização por eixo deve ser escolhida de tal maneira que não
afete o somatório, é notável que devido a isso não se pode aplicar este tipo de quantização
sobre a entrada. Porém se pode aplicar sobre os pesos W , com a Equação 26 sendo um
exemplo. A aplicação disto irá depender da camada da Rede Neural Artiﬁcial em especíﬁca, as


46
Camadas Convolucionais tem o eixo de escolha sendo o de ﬁltros como cada um é aplicado de
maneira independente sobre a mesma entrada, e as Camadas de Neurônio será aplicado sobre
cada neurônio pela mesma lógica.
Sy · (Yj −Zy) =
X
i
(Sx · (Xi −Zx) · Sw,j · (Wi,j −Zw,j))
(26)
Em suma, estes são os principais pontos a serem observados para a implementação
das Redes Neurais Artiﬁciais, porém existem diversas implementações diferentes dos mesmos
princípios apresentados.
2.4.5
Aplicação de Esquemas de Quantização
Na literatura existem muitas aplicações diferentes de esquemas de quantização de Re-
des Neurais Artiﬁciais. A Tabela 2 apresenta alguns trabalhos da literatura e suas diferentes
formas de lidar com o mesmo problema. O trabalho de Schütz et al. (2019) utiliza uma metodo-
logia similar a apresentada neste trabalho, porém com diferenças sobre tipos de quantização,
tamanho de entradas e pesos e várias decisões de projetos, porém a base teórica é a quanti-
zação simétrica similar a este trabalho. Outras alternativas de quantização são apresentada por
trabalhos como Korol (2019), na qual teve preferência sobre utilizar um formato menor de ﬂoa-
ting point como alternativa, enquanto o trabalho Lo, Lau e Sham (2018) utiliza uma metodologia
de quantização completamente diferente usando ponto ﬁxo com bits explicitamente deﬁnidos
para parte inteira e fracionária, no caso 2 bits para parte inteira e 6 para fracionária.
Tabela 2 – Comparação de modelos de Quantização utilizadas em Trabalhos
Trabalho
Metodologia de Quantização
Formato
Linguangem
(SCHÜTZ et al., 2019)
Quantização Simétrica (escala ﬁxa)
int6 (entradas) e int10 (pesos)
LingPON-HD
(KOROL, 2019)
Ponto Flutuante
ﬂoat24
VHDL
(LO; LAU; SHAM, 2018)
Ponto Fixo com 8 bits
Q2.6
VHDL
Este Trabalho
Quantização Aﬁm
int8
Híbrido(VHDL e LingPON)
Em suma, este trabalho utiliza uma evolução da metodologia de quantização apresen-
tada por Schütz et al. (2019), com algumas melhorias para eﬁciência computacional e precisão.
2.5
Considerações sobre a Revisão da Literatura
O presente capítulo apresentou o referencial teórico dos conceitos necessários para que
sejam alcançados os objetivos do presente trabalho, sendo realizada uma busca na literatura e
discussão do relacionamento dos conceitos com os objetivos propostos. Nota-se que a revisão
bibliográﬁca foi limitada aos conceitos relevantes e fundamentais para este trabalho, existindo
uma grande variedade de tecnologias, técnicas e outros conceitos existentes porém não cober-


47
tos por este capítulo. O foco principal foi nas tecnologias necessárias para implementação das
Redes Neurais Convolucionais e tecnologias complementares.
Conforme já ilustrado, existe uma grande necessidade de explorar alternativas ao pro-
cesso de execução de Redes Neurais Artiﬁciais, para que essas tecnologias possam ser aplica-
das em mais cenários. O Paradigma Orientado a Notiﬁcações teve sua aplicabilidade e efetivi-
dade na implementação de Redes Neurais Artiﬁciais no trabalho de Schütz et al. (2019), devido
a ser um paradigma adequado a problemas paralelizáveis como estes. Pela mesma lógica se
aplica a plataforma de FPGAs, onde o dispositivo é também adequado para estes problemas
por trazer possibilidades de implementar blocos de hardware paralelos.
Porém a implementação de Rede Neurais Convolucionais em FPGAs traz diversas diﬁ-
culdades no paralelismo e na complexidade da operação de convolução, necessitando de téc-
nicas como quantização para resolver estes problemas.


48
3 REDE NEURAL CONVOLUCIONAL EM FPGA CONTROLADA VIA PON
Neste capítulo será abordado o processo de desenvolvimento do trabalho, com os deta-
lhes de implementação dos circuitos em FPGA conforme necessários. Começando pela seção
3.1 que apresenta o modelo de Rede Neural Convolucional de referência criado para a imple-
mentação do presente trabalho, seguido pela seção 3.2 que apresenta uma visão de alto nível
da arquitetura utilizada. A seção 3.3 apresenta os componentes responsáveis diretamente pe-
las operações matemáticas ﬁxas de Convolução, redução de dimensionalidade, conversão de
faixa de valores e aplicação da função de ativação necessárias para a implementação de uma
Rede Neural Convolucional. A seção 3.5 apresenta a modelagem em PON e funcionamento
do circuito que controla os componentes desenvolvidos com o intuito de sequenciar as opera-
ções para que se tenha o resultado correto. Por ﬁm, a Seção 3.6 apresenta as considerações e
reﬂexões sobre o trabalho e arquitetura apresentada.
3.1
Modelo de Rede Neural Convolucional
Modelos de Redes Neurais Convolucionais podem utilizar uma grande variedade de
operações matemáticas, devido a isto é necessário para a implementação deste trabalho que se
tenha um modelo com as operações simples apresentadas. Justamente, a necessidade também
se estende para que se tenha controle sobre o processo de quantização exato. Para isso se
viu a necessidade de criar um modelo de Rede Neural Convolucional baseado em modelos
encontrados na literatura (CHOLLET, 2021) mas modiﬁcados para que se enquadre nos limites
de memória da plataforma de FPGA e a ﬁm de servir como referência as operações que devem
ser implementadas e o sequenciamento necessário dessas.
Este modelo foi criado e treinado para identiﬁcação de dígitos escritos a mão do MNIST
(LECUN, 1998), que contém imagens de tamanho 28 × 28 em escala de tons de cinza (gray-
scale), ou seja, cada píxel é representado por um número entre 0 a 255 com a cor preta sendo
o número 0 e a cor branca sendo o número 255, e os tons de cinza sendo os valores entre
estas duas tonalidades. Este problema de classiﬁcação de dígitos escritos a mão é amplamente
utilizado pela literatura para testes e provas de conceitos em aprendizagem de máquina devido
a sua simplicidade (DENG, 2012).
Dessa maneira foi criado o modelo que pode ser visto na Figura 21, utilizando o fra-
mework Tensorﬂow que providencia ferramentas para deﬁnição, treinamento e quantização
do modelo. O treinamento inicial foi realizado em ﬂoat32, com a quantização sendo realizada
usando o framework Tensorﬂow Lite para int8 (JACOB et al., 2017), este processo de quantiza-
ção sendo de realizar inferências em ﬂoat32 sobre base de dados de referências, observando
os valores mínimos e máximos e a partir desses, calcular os parâmetros de quantização. Desta
maneira foi seguido o procedimento para treinamento e execução da rede:


49
• Deﬁnição e treinamento da rede no framework Tensorﬂow usando ﬂoat32.
• Quantização usando o framework Tensorﬂow Lite para int8.
• A rede é salva em um arquivo .h5
• Com base nesse arquivo são extraídos os pesos, bias e parâmetros de quantização de
escala e ponto zero.
• Conversão de pesos, bias e parâmetros de quantização para o formato desejado de
agrupamento de oito valores e armazenado em arquivos de inicialização de memória
(memory initialization ﬁle). Nesta etapa são gerados os parâmetros M0 e 2−n da Seção
2.4.4, conforme eles não são informados diretamente.
• Arquivos de inicialização de memória são associados os seus respectivos blocos de
memórias.
• Imagem da base de dados do MNIST é transformado também em um arquivo de inici-
alização de memória para servir como entrada.
• Execução do circuito pelo simulador.
A ﬁm de poder testar esse modelo em diferentes tamanhos, foi colocada uma camada
de convolução sem a operação de redução de dimensionalidade logo na entrada, sendo esta
camada removida para testes com 3 camadas ou duplicada para testes com 5 camadas. Os
números entre cada par de camadas indica a dimensionalidade dos tensores. A entrada da
primeira camada convolucional é um tensor 28 × 28 × 1, isto é uma matriz de 28 linhas, 28
colunas e 1 canal, que representa o dígito escrito a mão da base do MNIST em tons de cinza.
Na primeira camada convolucional, são aplicados 32 ﬁltros de tamanho 3 × 3 × 1, re-
sultando em um tensor de dimensionalidade de 26 × 26 × 32 com a última dimensão sendo
o resultado de cada ﬁltro concatenado. Para a camada sucessora, são aplicados 32 ﬁltros de
tamanho 3 × 3 × 32, fazendo com que a dimensionalidade caia para 24 × 24 × 32. Em seguida
é aplicado o operador de redução de dimensionalidade pelo valor máximo, isto é a operação
MaxPool de dimensão 2 × 2, fazendo com que a dimensionalidade seja 12 × 12 × 32. A terceira
camada convolucional, aplica novamente 32 ﬁltros de tamanho 3 × 3 × 32 e reduz a dimensi-
onalidade para 10 × 10 × 32, com o segundo MaxPool de dimensão 2x2 reduzindo o tensor
para 5 × 5 × 32 que então é "linearizado"pela camada Reshape, i.e. visto como um tensor de
dimensionalidade 1×800 que é alimentado para a camada totalmente conectada, i.e. FullyCon-
nected cujo resultado são as dez classes possíveis dos caracteres a serem reconhecidos, com
a classe que possui maior valor representando o dígito reconhecido.
A função de transferência mais tradicional de realizar classiﬁcação de diversas classes é
a função softmax mas conforme a implementação dessa tem alto grau de complexidade, devido
a operação de divisão envolvida nesta. Neste problema de classiﬁcação em especíﬁco, a função


50
softmax não vantajem em termos de acurácia sobre a função Sigmoide, consequentemente foi
implementado a Sigmoide devido a ser mais simples.
Figura 21 – Estrutura da Rede Neural Convolucional utilizada.
Fonte: Autoria própria (2025).
Com o modelo e as operações envolvidas deﬁnidas, se tem as informações necessárias
para a criação do desenho da arquitetura para ser executado esse modelo de forma eﬁciente.
3.2
Visão Geral da Arquitetura da Solução
Conforme visto, Redes Neurais são compostas, em essência, por grandes equações
matemáticas, as quais passam por um processo de treinamento de modo que sejam ajustadas
para minimizar o erro em um conjunto de dados. Devido ao seu tamanho, não é trivial mapear
estas para dispositivos de FPGAs, sendo necessária uma maneira eﬁciente para a criação do
circuito que irá realizar este trabalho. Desta maneira, este problema foi dividido em dois sub-
problemas que são a execução das operações elementares necessárias para executar a Rede
Neural, e o controle destas operações a ﬁm de que se tenha o resultado correto, realizando as
operações sequencialmente por uma camada da Rede de cada vez1.
Para o primeiro subproblema, conforme este tem caráter puramente matemático, se vê
a necessidade de se utilizar circuitos ﬁxos otimizados para realizar estas operações, com a uti-
lização dos mecanismos de paralelismo conforme já visto, porém isto pode resultar em circuitos
complexos com várias etapas de execução, com cada operação tomando muitos ciclos para
a execução. A ﬁm de que se tenha eﬁciência, é necessário utilizar a técnica de pipeline que
permite que operações em etapas diferentes, e desta maneira não necessitando dos mesmos
recursos, sejam executadas ao mesmo tempo.
Enquanto no segundo subproblema, a solução consiste em realizar o controle por uma
máquina de estados responsável por gerar sinais de controles sobre os circuitos ﬁxos. Porém,
conforme mencionado, estes circuitos se utilizam da técnica de pipeline, a qual se tem como
consequência o aumento de complexidade da máquina de estados pela necessidade de ge-
renciar múltiplas operações em paralelo. A vista disso, é lógico que se aplique um paradigma
adequado a modelagem deste problema de controle, com o Paradigma Orientado a Notiﬁcações
1
A implementação da arquitetura em VHDL está no Apêndice B


51
sendo o mais apropriado a esta aplicação devido ao mecanismo de notiﬁcações permitir que se
tenha múltiplas máquinas de estados implementadas por FBEs em paralelo. A Figura 22 mostra
o Diagrama de Bloco de Alto Nível do sistema proposto.
Figura 22 – Diagrama de Blocos da Arquitetura do Trabalho Desenvolvido. Diagrama criado na
ferramenta Astah SysML
Fonte: Autoria própria (2025).
Pela Figura 22, os blocos Unidade Rede Neural e Unidade MaxPooling consistem nos
circuitos ﬁxos mencionados no primeiro subproblema, em seguida se tem os dois blocos de me-
mória com o bloco de Memória do Modelo consistindo nos pesos e parâmetros de quantização
que deﬁnem o modelo, com cada Unidade Rede Neural tendo por composição, uma instância
desse bloco e o Bloco Memória que contem a entrada inicial e é utilizado para armazenar os es-
tados das camadas escondidas e o resultado ﬁnal da rede convolucional, é notável que ambos
os blocos de memória consistem inteiramente em elementos de memória da FPGA (conforme
Seção 2.3.4). O bloco de Controlador PON são as máquinas de estados modelados pelo PON,
conforme o segundo subproblema, sendo que estas controlam os blocos ﬁxos por sinais de
controle e pelo ﬂuxo de dados oriundos das memórias.


52
Conforme discutido, a utilização da técnica de pipeline é essencial para alcançar eﬁci-
ência computacional. Em uma arquitetura de pipeline, cada componente processa seus dados
de forma independente e paralela aos demais, repassando-os ao próximo estágio assim que o
processamento atual é concluído. Na Figura 23, é ilustrado um exemplo do pipeline em opera-
ção. Cada Xi representa um dado sendo processado sequencialmente por cada componente.
Observa-se que, enquanto a Unidade Rede Neural realiza cálculos matemáticos em um dado
especíﬁco, o bloco de memória já está fornecendo novos dados por meio dos endereços de lei-
tura. Isso garante que o ﬂuxo de processamento não seja interrompido e que diferentes estágios
estejam sempre ocupados.
Outro aspecto importante demonstrado é que a escrita na memória ocorre apenas após
o processamento completo dos dados. Isso signiﬁca que são necessários múltiplos ciclos para
que o dado ﬁnal seja armazenado, já que o pipeline gera resultados parciais à medida que os
componentes enviam saídas intermediárias ao próximo estágio. No exemplo, observa-se que o
dado X2 é efetivamente escrito apenas no terceiro ciclo, conforme controlado pelo sinal Write
Enable (habilitar escrita).


53
Figura 23 – Exemplo do processo de pipeline
Fonte: Autoria própria (2025).
Em suma, se tem uma arquitetura relativamente simples que é capaz de realizar as ope-
rações sequencialmente por camada de Rede, porém com paralelismo e utilização eﬁciente dos
recursos providenciados pelo dispositivo de FPGA. Nas próximas subseções a implementação
de cada um destes blocos será detalhada e explicada.
3.3
Unidade Rede Neural
O componente de Unidade Rede Neural realiza as três partes matemáticas necessárias
para implementação das camadas de Convolução e Fully Connected, que são as operações de
soma e multiplicação (multiply and accumulate), a conversão entre as faixas de valores e a ati-
vação com funções não lineares. A Seção 3.3.1 mostra a visão de alto nível do bloco, enquanto
na Seção 3.3.2 é abordada a implementação das operações de soma e multiplicação envolvi-
das, em seguida a Seção 3.3.3 explica a conversão do resultado ao esquema de quantização da


54
camada e ﬁnalmente a Seção 3.3.4 que descreve como as funções de ativação são aplicadas
sobre os resultados dos componentes anteriores.
3.3.1
Visão Geral da Unidade Rede Neural
A Unidade Rede Neural é responsável pela realização de funções ﬁxas matemáticas
que são necessárias para a implementação de uma Rede Neural, separando estas operações
em três blocos diferentes que consiste no Bloco de Operação, que implementa as operações de
soma e multiplicação e redução de dimensionalidade, o Bloco de Conversão que implementa
a conversão de faixa de valores da Quantização (conforme visto na Seção 2.4.4) e o Bloco de
Ativação, que implementa as funções de ativações.
A Figura 24 mostra o diagrama de atividades do componente de Unidade de Rede Neu-
ral, na qual podem ser vistos os três blocos mencionados e os seus ﬂuxos, iniciando com o
Bloco de Operação, que consiste da multiplicação, árvore de adição e acumulação. Os dados
provenientes deste bloco são então enviados para o Bloco de Conversão que realiza o processo
de conversão da quantização, e o resultado destas operações são passadas para o Bloco de
Ativação que consiste das duas funções de ativações vistas, sendo qual função a ser utilizada
conﬁgurável por um multiplexador, e este gerando o resultado ﬁnal. As subseções a seguir de-
talham o funcionamento de cada um destes blocos.
Figura 24 – Diagrama de Atividade da Unidade de Rede Neural. Diagrama criado na ferramenta
Astah SysML
Fonte: Autoria própria (2025).


55
A Figura 25 mostra o diagrama paramétrico de uma instância da Unidade de Rede Neu-
ral, a qual existem oito dessas no sistema, permitindo a visualização à visão de operações
matemáticas e o ﬂuxo entre estas. Cada neurônio artiﬁcial desse possui 8 entradas, cada uma
recebendo um número como entrada externa (x1 até x8), utilizando representação quantizada
de inteiro de 8 bits (int8), e multiplicando estes números por pesos (w1 até w8), utilizando os
blocos de multiplicação da FPGA.
Cada unidade de multiplicação gera um número codiﬁcado em int16. O módulo "árvore
de adição"então soma todos estes 8 resultados, gerando um número inteiro representado em
19 bits (int19). Essa mudança de formato é necessária para que não seja introduzido erros
nessas operações intermediarias (conforme visto na seção 2.4.2. Esses números são somados
e acumulados no bloco ’Acumulador’, cujo valor inicial é o bias do ﬁltro que está sendo aplicado,
este valor é armazenado em um número codiﬁcado em int32. O número em formato de int19 é
convertido para int32 antes de ser realizado a operação de acumulação, usando o método de
extensão de sinal, a qual consiste em concatenar uma string de bits que tem o valor deﬁnido
pelo bit mais signiﬁcativo do número com o número original.
Quando todas as operações de soma e multiplicação do ﬁltro são terminadas, o valor é
repassado para o módulo de "Conversão"realiza a conversão entre faixa de valores da quanti-
zação (conforme Seção 2.4.4 e Equação 23), o resultado sendo um número inteiro no formato
de int32. Esse número em outra faixa de valor é passado para os módulos de "RELU"e "SIG-
MOID"em paralelo, que implementam as suas respectiva função de ativação, apenas o resultado
da função de ativação especiﬁcada na conﬁguração da camada é utilizada, através do multiple-
xador. O resultado desses módulos é um número no formato de inteiro de 8 bits, conforme as
operações do bloco fornecem garantia que o resultado estará na faixa de valor desse formato e
é selecionado os 8 bits menos signiﬁcativos.
Desta maneira, uma instância da Unidade Rede Neural processa oito números de entra-
das e pesos em paralelo, equivalendo ao paralelismo ICP igual a oito. Isto é realizado por canal
e não por píxel, com a operação sendo realizada apenas em um píxel ou uma parte desse. Caso
a entrada não possua esses canais, como, por exemplo ,em uma imagem colorida possuindo
três canais (x1 até x3), cada um correspondendo a cor azul, vermelha e verde, os outros cinco
outros canais (x4 até x8) na Unidade Rede Neural serão preenchidos com zero.


56
Figura 25 – Diagrama Paramétrico da Unidade de Rede Neural. Diagrama criado na ferramenta
Astah SysML
Fonte: Autoria própria (2025).
Tendo em vista a maneira de como a Unidade Rede Neural implementa as operações, se
pode perceber que várias Unidades Rede Neural podem operar em paralelo, se equivalendo ao
paralelismo de OCP conforme visto na Seção 2.2.4, onde cada uma destas unidades individuais
será responsável pela execução de um ou mais ﬁltros em paralelo. Para este presente trabalho
foram utilizadas oito Unidades de Rede Neural trabalhando em paralelo, equivalendo a OCP
igual a oito.
3.3.2
Bloco de Operação
Conforme visto, para o processamento da Unidade Rede Neural é necessário que sejam
feitas as operações matemáticas necessárias, as quais consistem em uma soma de produtos
conforme P
i XiWi + K. Isto pode ser visto na Figura 24 que detalha a Unidade inteira e a
Figura 26 mostra o componente de árvore de adição.
Como a plataforma de escolha para este presente trabalho é uma FPGA, a implementa-
ção das multiplicações precisa ser realizada dentro de blocos de DSP por não serem operações
eﬁcientes de ser implementadas em blocos lógicos, como explicado na Seção 2.3.3. Desta
forma, foram conﬁgurados os blocos DSPs para realizarem a multiplicação de dois números
inteiros e soma deles dentro dos DSP a tal maneira com que a multiplicação e o primeiro es-
tágio de adição vista na Figura 26 sejam realizadas no mesmo bloco, não utilizando recursos
adicionais de CLB.


57
Figura 26 – Diagrama de Atividade da Árvore de Adição.
Fonte: Autoria própria (2025).
A partir do segundo estágio de adições, essas operações e a operação de acumula-
ção são realizadas dentro dos CLBs usando os circuitos dedicados a adição e os registradores
dentro de cada, conforme visto na seção 2.3.2. Com o acumulador, adicionalmente, tendo cir-
cuito implementado a mais para carregamento do valor do bias como valor inicial, este sendo
armazenado em um circuito externo de registrador shift circular. Lembrando que a acumulação
é deﬁnida conforme a equação de recorrência a[t] = a[t −1] + b e a[0] = K com K sendo o
valor do bias, isto é o valor b é adicionado em a e guardado no registrador para ser realizada a
mesma operação no próximo ciclo.
A Figura 27 demonstra como funciona o pipeline sobre um exemplo contendo duas mul-
tiplicações, uma adição e um acumulador em três ciclos. A cada ciclo, os registradores arma-
zenam os valores que estão nas suas entradas e fornecem esse para as próximas operações,
que são realizadas sobre esses novos valores.


58
Figura 27 – Exemplo de pipeline no Bloco de Operação
Fonte: Autoria própria (2025).
Em síntese, este bloco realiza as operações inerente a Rede Neurais, alimentando os
blocos subsequentes responsáveis para o tratamento sobre a quantização e aplicação das fun-
ções de ativação no caso de operações de multiplicação e adição ou escrevendo o resultado na
memória no caso de operação de redução de dimensionalidade.
3.3.3
Bloco de Conversão
Conforme visto na Seção 2.4.4, após realizar as operações de multiplicação e acumu-
lação das Redes Neurais é necessário um tratamento sobre a quantização utilizada. Relem-
brando que as operações foram realizadas com a precisão arbitrária de modo a não propagar
erros conforme discutido na Seção 2.4.3, porém é necessário com que seja feito o processo de
arredondamento aﬁm de que os resultados possam ser utilizados pelas próximas operações.


59
A operação geral utilizada neste bloco pode ser vista na Equação 27 com a parte de
P
i Xi · Wi,j sendo realizada no Bloco de Operação. A utilização de 2−n · M0 sendo necessária
devido ao requerimento da plataforma de FPGA em não utilizar operações com ﬂoat com M0
sendo um número inteiro representando um número na faixa [0.5, 1) e desta maneira podendo
ser realizada uma multiplicação de inteiros com este e uma potência de dois, 2−n, a qual pode
ser realizada por uma operação de deslocamento (shift) conforme explicado a fundo na Seção
2.4.4.
Yj = 2−n · M0 (X + K)
(27)
Nota-se que para esta operação de deslocamento é necessário com que se tenha um
arredondamento apropriado na operação aﬁm de que não seja adicionado um viés devido a
truncamento, esta necessidade pode ser vista com um exemplo em base 10. Suponha que se
tem X = 15 com apenas dois dígitos, sem decimais e se quer realizar uma operação de deslo-
camento a direita (divisão por dez) sobre este número resultando em X = 1 pelo truncamento
da casa decimal, ao qual se tem um erro maior e um viés negativo devido ao comportamento
sempre de descartar o decimal. Este viés pode ser observado ao realizar a operação sobre 15
e 25 e somar estes, o resultado será (15 >> 1) + (25 >> 1) = 1 + 2 = 3 o que se tem um
viés negativo de 1 independente do erro.
Existem diversos métodos de arredondamento, o mais comum é chamado de rounding
up (arredondamento para cima) a qual o número a partir do ponto médio (0.5) é arrendondado
sempre para cima, esse método apesar de ser muito utilizado pode adicionar um viés devido
ao seu tratamento não igual dos pontos médio. Uma alternativa utilizada em áreas como esta-
tística é o rounding to nearest even (arredondamento para o número par mais próximo), onde o
arredondamento do ponto médio é sempre na direção do par mais próximo, por exemplo, 6.5 irá
arrendondar para 6 e 7.5 irá arrendondar para 8, esse método é utilizado no padrão IEEE 754
como arredondamento padrão para números de ponto ﬂutuante (MAXFIELD, 2006). Conforme
redes neurais são treinadas em ponto ﬂutuantes, este trabalho utiliza o arredondamento para o
número par mais próximo.
O mesmo problema constatado anteriormente pode ser visto ao pensar em umas amos-
tragens aleatórias A sobre uma distribuição uniforme na faixa [0, 2), ao realizar um somatório
sobre estas após realizar o truncamento teremos que P
i⌊Ai⌋= P
i(Ai −Di) onde é sa-
bido que a função de ﬂoor é equivalente a escrever K = A −D sobre um número real A
tal que 0 < D < 1 e K seja o maior número inteiro menor que A. Para o caso de uma
distribuição uniforme, pode se simpliﬁcar para P
i⌊Ai⌋= P(Ai) −|A|
2 onde |A|
2 é o viés ne-
gativo. Para evitar esse comportamento, percebe-se que se utilizar arredondamento ao invés
de truncamento P
i round(Ai) = P
i(Ai ± Ei) onde Ei é o erro de arredondamento, ao usar
o fato de que a distribuição é uniforme e aleatória, se tem que os erros se cancelam e se tem


60
que P
i round(Ai) = round (P
i Ai), ou seja não se tem nenhum viés com o resultado apenas
sendo afetado pelo próprio erro de arredondamento.
Consequentemente se tem a necessidade de realizar a operação de deslocamento com
arredondamento para o número par mais próximo e para isto não se foi encontrado um algoritmo
de arredondamento na literatura revisada, o que causou com que este trabalho implemente o
seu próprio que pode ser visto no Código 1. O Algoritmo se baseia primariamente na soma
do último bit descartado pela operação de deslocamento, por exemplo, a representação binaria
do número 54 é 00110110 e se deseja realizar a operação 54 >> 3, perceba que o terceiro
bit menos signiﬁcativo é 1, e ao realizar a operação (54 >> 3) + 1 = 7, se obtêm o resultado
correto (00110+1 = 00111 equivalendo a 7 em decimal) ao comparar com o valor real 54
8 = 6.75
e arrendondando este para sete.
Porém, essa adição não é verdade para todos os casos, tendo em consideração o pa-
drão de arredondamento com valores exatos com decimal .5. Continuando com o exemplo, para
o número 52 ao ser realizada a mesma operação de deslocamento por três, e quando aredon-
dado, este deve ser igual a 6, porém como a sua representação binária é 00110100 a operação
então traria o resultado (52 >> 3) + 1 = 7, que evidentemente não é o resultado desejado.
Isso é verdade para metade de todos os casos conforme a regra de arredondamento
para o número par mais próximo, de que para casos com números pares devem ser arrendon-
dados para baixo e números impares devem ser arrendondados para cima.
Desta maneira, a linha 1 do Algoritmo detecta se o número é um desses casos especiais
e a linha 2 detecta se é par ou impar. Em todos os casos, com exceção de números pares que
tenham ﬁnal .5, é realizada a soma do último bit, conforme a linha 5.
Algoritmo 1 – Algoritmo para right shift com arredondamento para número par mais próximo
inserir X, EXP
1: Condição1 = X&(2EXP−1 −1)
2: Condição2 = X >> EXP&1
3: Y = X >> EXP
4: se Condição1! = 0 and Condição2! = 0 então
5:
Y = Y + (X >> (EXP −1)&1)
6: ﬁnaliza se
7: retorna Y
Fonte: Autoria própria (2025).
Em vista disto, a Figura 28 mostra o Diagrama de Atividade do Bloco em questão. Por
simplicidade, este é implementado para realizar a operação sobre a saída do acumulador a
cada ciclo em pipeline, dessa maneira utilizando resultados acumulados não ﬁnais da opera-
ção. Consequentemente, é necessário um circuito externo para controlar o momento exato em
quando se tem o resultado ﬁnal das operações.


61
Figura 28 – Diagrama de Atividade do Bloco de Conversão. Diagrama criado na ferramenta Astah
SysML
Fonte: Autoria própria (2025).
Em suma, este bloco realiza as operações para transformar números quantizados de um
esquema de quantização para outro, aﬁm de que se possa ser usado em operações sucessivas
em Redes Neurais Artiﬁciais. Essa operação é análoga à operação de arredondamento e como
transforma entre esquemas, foi denominada de ’conversão’. Com esta operação realizada, os
resultados podem ser usados para alimentar as funções de ativação.
3.3.4
Bloco de Ativação
Funções de ativações são funções cuja responsabilidade em uma Rede Neural é de
adicionar não linearidade, de maneira que a Rede Neural possa representar e aprender uma
gama mais diversa de distribuições, conforme visto na Seção 2.2.2. Duas principais funções
que foram implementadas neste presente trabalho são a função ReLU e a função Sigmoide.
A função ReLU é deﬁnida conforme a Equação 28, onde se nota que é equivalente
a escrever ReLU(x) = min(x, 0). Esta é uma função amplamente utilizada por ser possível
implementar esta de maneira eﬁciente computacionalmente.
ReLU(x) =





x se x > 0
0 c.c.
(28)
A Figura 29 mostra o Diagrama de Atividade da Função ReLU. A primeira etapa que
é aplicar min(X, 255), com em seguida se aplicando a função max(X, 0), a qual é a própria
função ReLU. Existe a necessidade deste procedimento, pois não se tem garantia sobre a faixa
de valores recebidos dos blocos antecedentes a este, logo se deve garantir que os números
estejam na faixa representável por 8 bits aﬁm de que não tenha erros quando este for transfor-
mado para um int8. Em seguida, é subtraído 128 deste número conforme a faixa das operações
anteriores é [0, 256] a transformar para [-128, 127] que é exatamente a faixa representável para
int8, com a operação sucessiva sendo apenas selecionar estes bits menos signiﬁcativos. Após
realizar a operação, o ponto zero do número quantizado será igual a -128, a qual terá efeito de


62
que apenas números positivos serão representados, pois conforme a Equação 28, não é pos-
sível se ter inteiros negativos na operação de ReLU e consequentemente não se é necessário
utilizar bits para representar estes.
Figura 29 – Diagrama de Atividade da Função ReLU. Diagrama criado na ferramenta Astah SysML
Fonte: Autoria própria (2025).
As Equações 29 e 30 mostram dois exemplos para o funcionamento para números -10
e 270 respectivamente.
ReLU(−10) = max(min(−10, 255), 0) −128
= max(−10, 0) −128
= 0 −128
= −128
(29)
ReLU(270) = max(min(270, 255), 0) −128
= max(255, 0) −128
= 255 −128
= 127
(30)
A função Sigmoide é deﬁnida conforme a Equação 31, é notável que não é uma função
trivial de implementar computacionalmente, mesmo ao utilizar pontos ﬂutuantes. Devido a isto,
existem diversas maneiras de implementar a função Sigmoide em hardware, como a utiliza-
ção de várias funções lineares ou uma função quadrática (TSMOTS; SKOROKHODA; RABYK,
2019). Neste presente trabalho, se utiliza a abordagem de se usar uma tabela de valores pré-
calculadas e utilizar o valor para realizar a seleção sobre esta tabela, o que é conhecido como
Look-Up Table (LUT). Esta escolha teve como o objetivo minimizar erros, devido a capacidade
de se poder calcular exatamente o valor real e utilizar este na tabela.


63
σ(x) =
1
1 + e−x
(31)
A Figura 30 mostra o Diagrama de Atividades dessa função a qual é implementada por
uma LUT de 1024 entradas de 8 bits, com tal escolha devido ao elemento de memória da FPGA
que é o M10K conforme explicado na Seção 2.3.4. Dessa maneira se tem que restringir os
valores recebidos da conversão para a faixa [-512, 511] de maneira a certiﬁcar com que estes
estejam dentro da tabela e dessa maneira não seja selecionada o valor pré-calculado errado.
Com essa garantia, pode se selecionar os dez bits menos signiﬁcativos e utilizar desses para
selecionar o valor da tabela e se obtêm o resultado ﬁnal.
Figura 30 – Diagrama de Atividade da Função Sigmoide. Diagrama criado na ferramenta Astah
SysML
Fonte: Autoria própria (2025).
Em suma, este bloco realiza as operações matemáticas das funções de ativação deste
presente trabalho visando a implementação em FPGA. Porém, esse bloco, assim como os an-
tecessores, são responsáveis apenas pelas equações, sendo necessário que se tenha circuito
externos para controlar as operações realizadas por estas e o sincronismo entre elas.
3.4
Unidade MaxPooling
A Unidade MaxPooling é responsável por realizar a operação de redução de dimensio-
nalidade do mesmo nome. Este componente funciona em paralelo com a Unidade Rede Neural,
com a saída sendo escolhida pela conﬁguração da camada, isto é se é uma camada convoluci-
onal/linear ou de redução de dimensionalidade, em um multiplexador no bloco de Memória.
A operação de MaxPooling, utiliza a Equação 7, aplicada sobre uma janela assim como
operação de convolução, o que em suma resulta com que a operação selecione o elemento
dentro da janela com o maior valor, isso pode ser visto na Equação 33 que demonstra está
sendo aplicada para uma janela dois por dois. Um exemplo concreto desta operação pode ser
visto na Equação 34 sobre um tensor X = [[2, 0], [1, 4]].


64
max(x, y) =





y se y > x
x c.c.
(32)
MaxPooling(X) = max(max(X0,0, X0,1), max(X1,0, X1,1)
(33)
MaxPooling(X) = max(max(X0,0, X0,1), max(X1,0, X1,1)
= max(max(2, 0), max(1, 4))
= max(2, 4)
= 4
(34)
Á vista disso, a Figura 31 mostra o Diagrama de Atividade do bloco utilizado neste tra-
balho, onde em suma este realiza uma operação de max por ciclo, com estas sendo realizadas
sequencialmente sobre a janela a qual pode ser representado pela equação de recorrência
a[t] = max(a[t −1], b) com a[0] = −128 devido a -128 ser o menor número representável.
O sinal de Reset é responsável por reiniciar a relação para o estado inicial. Para esta opera-
ção, é perceptível que pode ter paralelismo entre os canais, com a Unidade MaxPooling tendo
oito blocos que funcionam conforme a Figura 31 operando em paralelo, a qual se equivale ao
paralelismo ICP.
Figura 31 – Diagrama de Atividade da operação de MaxPooling. Diagrama criado na ferramenta
Astah SysML
Fonte: Autoria própria (2025).


65
Em suma, este bloco realiza as operações de redução de dimensionalidade, as quais
são necessárias para implementação de Rede Neurais Artiﬁciais. Os resultados produzidos são
alimentados em camadas convolucionais ou lineares subsequentes.
3.5
Controlador PON
O componente de Controlador PON é responsável pelo controle das execuções dos blo-
cos que realizam as equações implementadas nos circuitos do componente Unidade Rede Neu-
ral, utilizando máquinas de estados modeladas no Paradigma Orientado a Notiﬁcações (PON).
A Seção 3.5.1 apresenta a justiﬁcativa para a utilização do PON neste trabalho. Em seguida,
a Seção 3.5.2 fornece uma visão de alto nível do controlador, destacando suas associações
com os demais blocos. Já na Seção 3.5.3, é detalhada a modelagem das máquinas de estados.
Por ﬁm, a Seção 3.5.4 discute a sequência de operações realizadas pelo controlador e suas
interações com os demais componentes do sistema.
3.5.1
Justiﬁcativa da utilização do PON
Conforme apresentado, o Controlador PON implementa o controle das operações de
Redes Neurais por meio de Máquinas de Estados modeladas no Paradigma Orientado a No-
tiﬁcações (PON). A Seção 2.2 descreve as operações em sua forma puramente matemática,
mas há várias maneiras de implementá-las computacionalmente. Uma dessas maneiras é ilus-
trada no Algoritmo 2, que deﬁne o processo geral de convolução, enquanto a função de janela
da convolução está detalhada no Algoritmo 3. Além disso, a função de Quantização, usada no
processo, é discutida na Seção 2.4.4.
Observa-se que o algoritmo contém partes sequenciais, como as linhas 5 a 7 no Al-
goritmo 2 e a linha 5 no Algoritmo 3, que dependem dos resultados das etapas anteriores.
Por outro lado, há paralelismo disponível dentro dos laços de repetição, conforme discutido na
Seção 2.2.4.
Embora o comportamento sequencial descrito seja funcional, ele não é ideal para plata-
formas FPGA, pois estas não possuem a mesma eﬁciência computacional que as CPUs para
execução sequencial. Nessas plataformas, é comum utilizar o mecanismo de pipeline, onde o
algoritmo é dividido em estágios executados em paralelo para diferentes dados. Por exemplo,
enquanto um píxel P da Imagem está na etapa de Quantização após ser aplicado o ﬁltro F
sobre este, a Convolução pode estar sendo aplicada ao ﬁltro sucessor F + 1, otimizando a
eﬁciência computacional.
Implementar pipeline, entretanto, é mais complexo do que simplesmente utilizar o algo-
ritmo de forma sequencial. É necessário gerenciar os estados de execução, garantir o sincro-
nismo adequado e evitar conﬂitos. Para isso, é essencial um controle eﬁciente e bem modelado.


66
Algoritmo 2 – Algoritmo Geral de Convolução
inserir Imagem, Filtro, Bias, ParQuantização, Resultado
1: para cada linha i de Imagem faça
2:
para cada coluna j de Imagem faça
3:
para cada ﬁltro F em Filtro com índice f faça
4:
op = Convolução(Imagem, F, Bias[f], i, j)
5:
op = Quantização(op, ParQuantização[f])
6:
op = Ativação(op)
7:
Resultado[i][j][f] = op
8:
ﬁnaliza para
9:
ﬁnaliza para
10: ﬁnaliza para
11: retorna Resultado
Fonte: Autoria própria (2025).
Algoritmo 3 – Algoritmo de Janela da Convolução
inserir Imagem, Filtro, Bias, i, j
1: acc = Bias
2: para cada linha k de Filtro faça
3:
para cada coluna l de Filtro faça
4:
para cada canal m de Imagem faça
5:
acc + = Imagem[i+k][j+l][m] · Filtro[k][l][m]
6:
ﬁnaliza para
7:
ﬁnaliza para
8: ﬁnaliza para
9: retorna acc
Fonte: Autoria própria (2025).
O Paradigma Orientado a Notiﬁcações (PON) se destaca como uma solução apropriada, pois
permite o desacoplamento das Máquinas de Estado em FBEs, que operam em paralelo. Esse
desacoplamento facilita a implementação do pipeline, proporcionando uma execução otimizada.
Em resumo, o PON é utilizado neste trabalho para implementar as Máquinas de Estado
de forma a garantir eﬁciência computacional, possibilitada pelo uso do mecanismo de pipeline,
na implementação de Redes Neurais Artiﬁciais em hardware.
3.5.2
Visão Geral do Controlador
Para muitos projeto de hardware, é necessário ter uma ou mais Máquinas de Estados
para que seja controlado o comportamento do circuito desejado, com o controlador PON servido
a este papel neste presente trabalho, pelo seu controle direto e indireto sobre a Unidade Rede
Neural e demais circuitos. Ou seja, o PON irá realizar a coordenação de controle sobre os
diversos pipelines.
O comportamento geral desejado pode ser visto no Algoritmo 4 onde as operações
discutidas devem ser repetidas conforme as camadas da Rede conﬁgurada no Sistema. Para a
implementação deste processo, foi separado este em cinco partes, detalhadas a seguir:


67
• O laço de repetição por camada da Rede Neural, correspondendo as linhas 1 e 2 do
algoritmo, e este sendo encapsulado dentro de uma FBE do PON chamada de NOP_-
Main.
• O carregamento de parâmetros de quantização e bias da camada em execução, equi-
valendo a linha 3 do algoritmo, e é implementada em outra FBE denominada de NOP_-
Parametros.
• O controle sobre o laço de repetição e operações das linhas 4 a 6, na qual se controla
as entradas para a função de Convolução que está sendo chamada. Isto é encapsulado
em uma NOP_Input.
• O controle sobre os parâmetros de quantização e bias, consistindo das linhas 6 e 7 e
sendo realizado pela FBE NOP_Control.
• A escrita do resultado realizada na linha 9, onde isto é feito pela FBE NOP_Output.
Cada uma dessas FBEs é implementadas como uma máquina de Estado que se comu-
nicam com as demais por notiﬁcações para que se tenha sincronismo no pipeline e permitindo
com que se tenha um paralelismo no controle. Essa abordagem simpliﬁca o problema de con-
trole em pipeline ao utilizar o conceito de notiﬁcações do Paradigma Orientado a Notiﬁcações.
Vale relembrar que o controlador apenas realiza o ﬂuxo de controle das operações, com
as funções sendo realizadas pelos circuitos ﬁxos implementados pela Unidade Rede Neural.
Algoritmo 4 – Algoritmo Geral de Convolução
inserir Rede, Imagem, Resultado
1: para cada camada da Rede faça
2:
Carregar informações da Camada
3:
Carregar Bias e ParQuantização da Camada
4:
para cada píxel da Imagem com índice i, j faça
5:
para cada Filtro F da Camada com índice f faça
6:
op = Convolução(Imagem, F, Bias[f], i, j)
7:
op = Quantização(op, ParQuantização[f])
8:
op = Ativação(op)
9:
Resultado[i][j][f]= op
10:
ﬁnaliza para
11:
ﬁnaliza para
12:
Imagem = Resultado
13: ﬁnaliza para
14: retorna Resultado
Fonte: Autoria própria (2025).
A Figura 32 demonstra o funcionamento simpliﬁcado do Controlador. Pode ser vista a
associação de cada FBE com as funcionalidades necessárias vistas no Algoritmo 4, conforme
já visto.


68
Figura 32 – Diagrama de Atividade Simpliﬁcado.
Fonte: Autoria própria (2025).
A Figura 33 mostra um diagrama de componentes do Sistema em completo, mostrando
os componentes citados e as suas ações sobre os outros componentes do sistema, onde é
perceptível que o Controlador PON tem ação direta com sinais de controles e indiretas pelo
acesso e escrita em memória sobre a Unidade Rede Neural.
Figura 33 – Diagrama de Componentes em UML. Diagrama criado com a ferramenta Astah UML.
Fonte: Autoria própria (2025).
A Figura 34 apresenta as máquinas de estados modeladas com LingPON, cada uma
correspondendo a uma FBE. A FBE NOP_Main possui um número maior de estados devido à
necessidade de sequenciamento das operações dentro de uma camada. Para as demais, foram
modelados apenas dois estados, uma vez que as notiﬁcações desempenham parte da lógica de
controle. Na implementação em VHDL, foi necessário adicionar alguns estados extras às FBEs


69
NOP_Main e NOP_Control para garantir a sincronização com os outros circuitos, enquanto as
demais mantiveram uma implementação idêntica à especiﬁcação em LingPON.
Figura 34 – Diagrama de Estado de Maquina.
Fonte: Autoria própria (2025).
A Figura 35 apresenta a organização interna do Controlador PON com as cinco FBEs
citadas anteriormente e as suas relações entre si.


70
Figura 35 – Diagrama de Classe representando as entidades PON. Diagrama criado com a ferra-
menta Astah UML.
Fonte: Autoria própria (2025).
A visão completa do Controlador pode ser vista nas Figuras ilustrativas 36, 37, 38 e
39 que juntas são um Diagrama de Componente do DON que apresentam todos os FBEs,
atributos, regras e ações que formam a modelagem do Controlador PON. Em resumo, cada
FBE implementa uma máquina de estado e responsável por uma parte do algoritmo com as
notiﬁcações entre essas consistindo em inicialização, realização de uma etapa e término.


71
Figura 36 – Diagrama de Componente DON - Canto Superior Esquerdo. Diagrama criado com a
ferramenta Astah UML.
Fonte: Autoria própria (2025).


72
Figura 37 – Diagrama de Componente DON - Canto Superior Direito. Diagrama criado com a ferra-
menta Astah UML.
Fonte: Autoria própria (2025).


73
Figura 38 – Diagrama de Componente DON - Canto Inferior Esquerdo. Diagrama criado com a fer-
ramenta Astah UML.
Fonte: Autoria própria (2025).


74
Figura 39 – Diagrama de Componente DON - Canto Inferior Direito. Diagrama criado com a ferra-
menta Astah UML.
Fonte: Autoria própria (2025).


75
Em suma, o Controlador são máquina de estados modeladas pelo Paradigma Orientado
a Notiﬁcações, cuja responsabilidade é a realização de sincronia e controle dos circuitos imple-
mentados na Unidade Rede Neural, de maneira com que a Rede Neural Artiﬁcial seja executada
na ordem correta.
3.5.3
Modelagem de Máquina em Estados em PON
Conforme visto, o componente de Controlador PON foi modelado no Paradigma Orien-
tado a Notiﬁcação, em cinco diferentes máquinas de estados, cada uma sendo representada
por uma FBE e responsável por uma etapa no controle da Unidade Rede Neural. Sendo estas
NOP_Main, NOP_Parametros, NOP_Input, NOP_Control e NOP_Output.
A FBE NOP_Main é responsável pelo carregamento das informações sobre a Camada,
como tipo de operação, tamanho de ﬁltros e imagens, tipo de ativação e etc e o sequenciamento
da inicialização das outras máquinas de estados, devido à necessidade de executar a NOP_-
Parametros antes das demais. A Listagem 1 mostra partes da modelagem deste componente
em linguagem LingPON 3.0, onde se utiliza o preﬁxo reg para indicar atributos do hardware
utilizados dentro da FBE.
A execução da NOP_Main é relativamente simples, tendo o método de carregamento
das informações da camada da linha 10, onde a função lerCamada da linha 11, realiza a leitura
das informações em um formato binário de 102 bits. O controle da inicialização é feito pelo
atributo de estado atual da máquina de estado atMainStart, com as outras FBEs tendo as suas
premissas e regras para inicializar por este atributo.


76
Listagem 1 – Modelagem da FBE NOP Main
1
fbe NOP_Main
2
a t t r i b u t e
atMainStart
:
v o l a t i l e
boolean = false
3
a t t r i b u t e atCamada :
integer = 0
4
a t t r i b u t e
atMainState
:
integer = 0
5
a t t r i b u t e
atLastLayer
:
boolean = false
6
a t t r i b u t e
regRunning
:
boolean = false
7
a t t r i b u t e regDadosCamada :
integer = 0
8
a t t r i b u t e
regCamadas :
constant
integer [ ]
9
. . .
10
method mtCarregarCamada :
( )
11
atMainState = 1;
12
regDadosCamadas = lerCamada ( regCamadas [ atCamada ] ) ;
13
atCamada = atCamada + 1;
14
i f ( atCamada == length ( lerCamada ) )
15
{
16
atLastLayer = true ;
17
}
18
end
19
20
method mtCarregarParametros :
( )
21
atMainState = 2;
22
end
23
24
method mtExecutar :
( )
25
atMainState = 3;
26
end
27
. . .
28
method mtAvancar :
( )
29
atCamada = atCamada + 1;
30
end
31
. . .
32
premise prEqTwoMainState :
atMainState == 2
33
premise prEqParFinish :
parametros . atParFinished == true
34
35
rule
rlTerminoParametros :
prEqTwoMainState and prEqParFinish
36
mtExecutar ( ) ;
37
end
38
. . .
Fonte: Autoria própria (2025).
Por sua vez, a FBE NOP_Parametros tem como função carregar os parâmetros de quan-
tização e bias de cada camada antes de começar a execução em si. A modelagem pode ser
vista na Listagem 2, com o método mtParExecute da linha 17, onde se carrega os parâmetros
citados na linha 18 por acesso à memória, e sendo necessário informar para qual instância da
Unidade Rede Neural, este dado é destinado, fazendo isto pelo atributo regParWrite que é um
byte, com a posição do bit ’1’ indicando o destinatário, desta maneira a operação de desloca-
mento da linha 19 deve ser o deslocamento lógico.


77
Listagem 2 – Modelagem da FBE NOP Parametros
1
fbe NOP_Parametros
2
a t t r i b u t e
atParState :
integer = 0
3
a t t r i b u t e
atCurrentPar :
v o l a t i l e
integer = 0
4
a t t r i b u t e
atParFinished :
boolean = false
5
a t t r i b u t e
regParWrite :
char = 0
6
a t t r i b u t e
regParData :
integer ;
7
a t t r i b u t e
regParArray :
const
integer [ ]
8
a t t r i b u t e
regParOffset :
v o l a t i l e
integer = 0
9
10
method mtParIncia liza r :
( )
11
atParState = 1;
12
atCurrentPar = 0;
13
atParFinished = false ;
14
regParWrite = 1;
15
end
16
17
method mtParExecute ( )
18
regParData = regParArray [ atCurrentPar + regParOffset ] ;
19
regParWrite = regParWrite << 1;
20
atCurrentPar = atCurrentPar + 1;
21
end
22
. . .
23
premise prEqTwoMainState :
main_controller . atMainState == 2
24
premise prEqParStart :
atParState == 0
25
26
rule
r l P a r S t a r t :
prEqTwoMainState and prEqParStart
27
mtParIncia liza r ( ) ;
28
end
29
30
premise prNeqCurrentPar :
atCurrentPar
!= 32
31
premise prEqCurrentPar :
atCurrentPar == 32
32
premise prEqOneParState :
atParState == 1
33
34
rule
rlParExecute :
prEqOneParState and prNeqCurrentPar
35
mtParExecute ( ) ;
36
end
37
38
rule
r l P a r F i n i s h :
prEqOneParState and prEqCurrentPar
39
mtParFinish ( ) ;
40
end
41
end
Fonte: Autoria própria (2025).
O componente NOP_Input é a máquina de estado mais complexa deste projeto, sendo
responsável pela implementação da leitura da memória por janelas conforme visto na Seção
2.2.2.
Os atributos principais relacionados a realização da operação da Janela pela imagem
inteira pode ser vista na Listagem 3, com os atributos atCurrentX, atCurrentY e atCurrentChan-


78
nel se referindo a posição real do píxel a qual a operação está sendo realizada e os atributos
atWindowX e atWindowY a posição relativa dentro da Janela.
Listagem 3 – Atributos Principais da FBE NOP Input
1
fbe NOP_Input
2
a t t r i b u t e
atCurrentX :
integer = 0
3
a t t r i b u t e
atCurrentY :
integer = 0
4
a t t r i b u t e
atCurrentChannel :
integer = 0
5
a t t r i b u t e
a t C u r r e n t F i l t e r :
integer = 0
6
a t t r i b u t e
atWindowX :
integer = 0
7
a t t r i b u t e
atWindowY :
integer = 0
8
. . .
Fonte: Autoria própria (2025).
Conforme estes atributos são mudados, os endereços referentes a este dados são cria-
dos e mandados para as Memórias a ﬁm de que sejam realizadas as operações. Isto pode ser
visto na Listagem 4, com as linhas 10-14 sendo a representação dessas ações com as variáveis
de regDados e regPesos representando os blocos de memória do hardware.
Listagem 4 – Criação de Endereço da FBE NOP Input
1
a t t r i b u t e
atPrevWindowX :
integer = 0
2
a t t r i b u t e
atPrevWindowY :
integer = 0
3
a t t r i b u t e
atPrevCurrentChannel :
integer = 0
4
. . .
5
method mtMandarDados :
( )
6
atPrevWindowX = atWindowX ;
7
atPrevWindowY = atWindowY ;
8
atPrevCurrentChannel = atCurrentChannel ;
9
regDadosEntrada = regDados [ atCurrentY+atWindowY ]
10
[ atCurrentX+atWindowX ] [ atCurrentChannel ] ;
11
regPesosEntrada = regPesos [ a t C u r r e n t F i l t e r ] [ atWindowX ]
12
[ atWindowY ] [ atCurrentChannel ] ;
13
end
14
. . .
15
premise prChangedWindowX :
atPrevWindowX != atWindowX
16
premise prChangedWindowY :
atPrevWindowY != atWindowY
17
premise prChangedCurrentChannel :
atPrevCurrentChannel
!=
atCurrentChannel
18
rule
rlDados :
prEqOneInputState and ( prChangedWindowX or
19
prChangedWindowY or prChangedCurrentChannel )
20
mtMandarDados ( ) ;
21
end
Fonte: Autoria própria (2025).
Enquanto que o Laço de Repetição em si, que realiza a operação de Janelamento sobre
estes atributos, pode ser visto na Listagem 5, onde as regras rlCol e rlLinha são acionadas,
estas avançam a janela conforme o algoritmo, com também tendo regra rlChannel para os
demais casos e realiza o mesmo tipo de ação conforme as anteriores.


79
Listagem 5 – Laço de Repetição de Janela da FBE NOP Input
1
. . .
2
a t t r i b u t e
regQtdFilter :
v o l a t i l e
integer = 0
3
a t t r i b u t e
regWindowSizeX :
v o l a t i l e
integer = 0
4
a t t r i b u t e
regWindowSizeY :
v o l a t i l e
integer = 0
5
a t t r i b u t e
regQtdChannel :
v o l a t i l e
integer = 0
6
a t t r i b u t e
regImageSizeX :
v o l a t i l e
integer = 0
7
a t t r i b u t e
regImageSizeY :
v o l a t i l e
integer = 0
8
. . .
9
method mtProximaCol :
( )
10
atWindowX += 1
11
end
12
13
method mtProximaLinha :
( )
14
atWindowX = 0;
15
atWindowY += 1
16
end
17
. . .
18
premise prEqOneInputState :
atInputState == 1
19
premise prNeqWindowX : atWindowX != regWindowSizeX
20
rule
r l C o l :
prEqOneInputState and prNeqWindowX
21
mtProximaCol ( ) ;
22
end
23
premise prEqWindowX : atWindowX == regWindowSizeX
24
premise prNeqWindowY : atWindowY != regWindowSizeY
25
rule
r lL i n h a :
prEqOneInputState and prEqWindowX and prNeqWindowY
26
mtProximaLinha ( ) ;
27
end
28
. . .
Fonte: Autoria própria (2025).
Quando a operação de um ﬁltro sobre uma janela de convolução chega ao seu ﬁm, a re-
gra rlFiltro é acionada, a qual instiga o método mtProximoFiltro irá notiﬁcar a FBE NOP_Control
pelo atributo atInputNewWindow na linha 5 e avançar a operação para o próximo ﬁltro, e no-
tando o caso onde todos os ﬁltros já realizaram as suas operações sobre esta janela especíﬁca,
este irá avançar a janela de convolução conforme as linhas 7-16. Da mesma maneira, caso o
avanço da Janela resulte em que esta esteja fora da imagem, é acionada a regra rlTermino que
realiza o retorno para o estado inicial da máquina de estado e notiﬁca a FBE NOP_Control que
esta terminou o seu processamento. Desta maneira, a máquina de estado implementada pela
FBE NOP_Input consegue realizar o seu processamento e notiﬁcar as outras FBEs sobre a sua
situação atual.
Sendo necessário repetir a operação da janela de convolução para cada grupo de oito
ﬁltro, devido ao número de Unidade Rede Neural, envolvido na camada da Rede Neural, com
a variação dos pesos enviados para a Unidade Rede Neural conforme pode ser visto na linha
11-12 da Listagem 4.


80
Listagem 6 – Notiﬁcações para outras entidades na FBE NOP Input
1
method mtProximoFiltro :
( )
2
atWindowX = 0;
3
atWindowY = 0;
4
atCurrentChannel = 0;
5
atInputNewWindow = true ;
6
a t C u r r e n t F i l t e r += 1
7
i f ( a t C u r r e n t F i l t e r == regQtdFilter )
8
{
9
a t C u r r e n t F i l t e r = 0;
10
atCurrentX += 1;
11
i f
( atCurrentX == regImageSizeX )
12
{
13
atCurrentX = 0;
14
atCurrentY += regStrideY ;
15
}
16
}
17
end
18
method mtFinishInput :
( )
19
atInputState = 0;
20
atInputFinished = true
21
end
22
. . .
23
premise prEqChannel :
atCurrentChannel == regQtdChannel
24
rule
r l F i l t r o :
prEqOneInputState and prEqWindowX and
25
prEqWindowY and prEqChannel
26
mtProximoFiltro ( ) ;
27
end
28
29
premise prEqCurrentY :
atCurrentY == regTamanhoImagemY
30
rule
rlTermino :
prEqOneInputState and prEqCurrentY
31
mtFinishInput ( ) ;
32
end
Fonte: Autoria própria (2025).
A máquina de estado da FBE NOP_Control pode ser vista na Listagem 7, com o seu
funcionamento sendo similar as demais apresentadas, com regras para inicialização, execução
quando receber uma notiﬁcação da NOP_Input que terminou de realizar o carregamento de
uma janela de dados e o mesmo para a notiﬁcação de término.
A função principal dessa máquina de estado é de sincronização em sinais de controle
devido ao fato de que as operações da NOP_Input e Unidade Rede Neural demoram diversos
ciclos, devido ao endereço efetivos terem que serem calculado, realizar a leitura na memória
e passar pela multiplicação e árvore de adição da Unidade Rede Neural, com a função de
delay das linhas 14, 19 e 26 realizando este papel. Com as operações realizadas por este
sincronismo sendo de carregar os próximos valores dos parâmetros de quantização e bias pelo
atributo regLoad e de o bloco de acumulador começar de fato acumular valores originários da
árvore de adição, isto é realizar ACC = X + ACC ao invés de ACC = ACC.


81
Listagem 7 – Modelagem da FBE NOP Control
1
fbe NOP_Control
2
a t t r i b u t e
atControlState :
integer = 0
3
a t t r i b u t e
atControlNewWindow :
v o l a t i l e
boolean = false
4
a t t r i b u t e
atControlFinished :
boolean = false
5
a t t r i b u t e
regLoad :
v o l a t i l e
boolean = false
6
a t t r i b u t e
regOperation :
v o l a t i l e
boolean = false
7
8
method
m t C o n t r o l I n i c i a l i z a r :
( )
9
atControlState = 1;
10
regLoad = false ;
11
regLoad = true ;
12
atControlFinished = false ;
13
regOperation = false ;
14
delay ( ) ;
15
regOperation = true ;
16
end
17
method mtProximoParametro ( )
18
input . atInputNewWindow = false ;
19
delay ( ) ;
20
regLoad = true ;
21
regLoad = false ;
22
atControlNewWindow = true ;
23
end
24
method mtFinishControl ( )
25
input . atInputFinished = false ;
26
delay ( ) ;
27
atControlState = 0;
28
atControlFinished = true
29
regOperation = false ;
30
end
31
32
premise prEqThreeMainState :
main_controller . atMainState == 3
33
premise prEqZeroControlState :
atControlState == 0
34
rule
r l C o n t r o l S t a r t :
prEqThreeMainState and prEqZeroControlState
35
m t C o n t r o l I n i c i a l i z a r ( ) ;
36
end
37
38
premise prEqOneControlState :
atControlState == 1
39
premise prEqInputNewWindow :
input . atInputNewWindow == true
40
41
rule
rlLoad :
prEqOneControlState and prEqInputNewWindow
42
mtProximoParametro ( ) ;
43
end
44
45
premise prEqInputFinished :
input . atInputFinished == true
46
47
rule
r l F i n i s h C o n t r o l :
prEqOneControlState and prEqInputFinished
48
mtFinishControl ( ) ;
49
end
50
end
Fonte: Autoria própria (2025).


82
A FBE NOP_Output possui a mesma motivação que a NOP_Control, devido a latência
da passagem dos dados pelos blocos de conversão e ativação da Unidade Rede Neural demo-
rarem diversos ciclos. Consequentemente, este componente tem responsabilidade de calcular
o endereço do píxel da imagem resultante e sincronizar o envio deste para a memória quando
os dados ﬁnais estiverem prontos. Isto é realizado no método mtEscrever através de um delay
na linha 8 da Listagem 8, na linha 9 da mesma Listagem, onde se tem o cálculo do endereço
de escrita e a linha seguinte é acionado o sinal de controle de escrita da memória, indicando a
esta para escrever o valor dado no endereço fornecido. Adicionalmente, se tem o método mt-
FinishOutput utilizado para o último valor da camada a ser escrito na memória, que chama o
método mtEscrever e realiza o retorno para o estado inicial.
Esses métodos são ativados através de notiﬁcações de execução e término da NOP_-
Control. No caso de término, a máquina de estado realiza o processo normal e quando terminar,
passa esta notiﬁcação de término para a NOP_Main. As Listagens 8 e 9 mostram a modelagem
deste componente.
Listagem 8 – Modelagem da FBE NOP Output - Parte 1
1
fbe NOP_Output
2
a t t r i b u t e
atOutputState :
integer = 0
3
a t t r i b u t e
atOutputFinished :
boolean = false
4
a t t r i b u t e
regWriteEn :
v o l a t i l e
boolean = false
5
. . .
6
method mtEscrever :
( )
7
con tr o l . atControlNewWindow = false ;
8
delay ( ) ;
9
regOutput [ regCurrentX ] [ regCurrentY ] [ regCurrentChannel ] = regSaidaURN
;
10
regWriteEn = true ;
11
regCurrentChannel += 1;
12
i f ( regCurrentChannel == regQtdFilter )
13
{
14
regCurrentChannel = 0;
15
regCurrentX += 1;
16
i f ( regCurrentX == regImageSizeX )
17
{
18
regCurrentX = 0;
19
regCurrentY += 1;
20
}
21
}
22
regWriteEn = false ;
23
end
24
. . .
Fonte: Autoria própria (2025).


83
Listagem 9 – Modelagem da FBE NOP Output - Parte 2
1
. . .
2
method mtFinishOutput :
( )
3
con tr o l . atControlFinished = false ;
4
mtEscrever ( ) ;
5
atOutputState = 0;
6
atOutputFinished = true
7
end
8
. . .
9
premise prEqOneOutputState :
atOutputState == 1
10
premise prEqControlNewWindow :
co ntr o l . atControlNewWindow == true
11
rule
r l W r i t e :
prEqOneOutputState and prEqControlNewWindow
12
mtEscrever ( ) ;
13
end
14
premise prEqControlFinished :
co ntr o l . atControlFinished == true
15
rule
r l F i n i s h :
prEqOneOutputState and prEqControlFinished
16
mtFinishOutput ( ) ;
17
end_rule
18
end
Fonte: Autoria própria (2025).
A Figura 40 mostra os componentes que estão atuando sobre o ﬂuxo de notiﬁcação de
término de carregamento de uma janela de convolução para a Unidade Rede Neural, onde a
entidade NOP_Input realiza uma operação de um ﬁltro sobre uma janela de convolução, com
a última etapa sendo o acionamento da regra rlFiltro, com o método desta regra notiﬁcando
a regrarlLoad da entidade NOP_Control para que seja carregado os parâmetros do próximo
ﬁltro e de maneira similar o método da rlLoad passa uma notiﬁcação para a regra rlWrite da
FBE NOP_Output para que seja escrito o resultado ﬁnal da saída da Unidade Rede Neural em
memória.


84
Figura 40 – Diagrama de Componente sobre partes das FBEs que se comunicam no caso de car-
regamento de uma janela de convolução. Diagrama criado com a ferramenta Astah
UML.
Fonte: Autoria própria (2025).
Desta maneira, este trabalho utilizou o Paradigma Orientado a Notiﬁcações para mo-
delar as máquinas de estados responsáveis por controlar os sinais de controle e endereço de
memória para o funcionamento efetivo dos outros blocos de hardware.
3.5.4
Controlador em Operação
Tendo em vista a modelagem do controlador, é necessário que se demonstre a sequên-
cia de operações e notiﬁcações a serem tomadas por este, devido a ter partes onde se tem
execução concorrente entre as diversas FBEs.
As primeiras etapas que o controlador executa podem ser vistas no Diagrama de Ativi-
dade, separado em quatro partes para melhor visualização, e com a primeira parte na Figura
41, por onde se começa com uma sequência simples. Primeiramente, a máquina de estado da
NOP_Main inicializa conforme a notiﬁcação de executar a rede e começa a executar a partir
da primeira camada da rede, carregando as suas informações. Em seguida, a FBE NOP_Para-
metros é notiﬁcada e começa a carregar os parâmetros de quantização e bias para a Unidade
Rede Neural e quando esta etapa é terminada, notiﬁcando a NOP_Main e com esta gerando no-
tiﬁcações para as FBEs NOP_Input, NOP_Control e NOP_Output a inicializarem e executarem
a camada da Rede Neural em si enquanto que a mesma ﬁca em espera até que seja terminado
este processo.


85
Figura 41 – Diagrama de Atividade do SysML - Parte 1. Diagrama criado com a ferramenta Astah
UML.
Fonte: Autoria própria (2025).
A Figura 42 e 43 são a continuação do Diagrama de Atividade apresentado na Figura
41, mostrando a sequência de operações e paralelismo entre as FBEs NOP_Input, NOP_Con-
trol e NOP_Output. Assim que estas recebem a notiﬁcação de início, elas se inicializam e no
primeiro instante apenas a NOP_Input executa, realizando o seu papel de carregar a janela de
convolução conforme descrito na Seção 3.5.3 e quando a NOP_Input termina de realizar este
carregamento notiﬁca a NOP_Control e pode voltar a carregar a mesma janela caso ainda tenha
ﬁltros que não executaram sobre esta ou avançar a janela.
Ao receber esta notiﬁcação, a FBE NOP_Control em paralelo começa a executar, re-
alizando o carregamento dos parâmetros de quantização e bias no momento correto, isto é
quando a Unidade Rede Neural termina de passar os dados pelo Bloco de Operação e aciona a
FBE NOP_Output. Essa FBE por sua vez, escreve o resultado no momento correto levando em
conta as latências envolvidas nos blocos de Conversão e Ativação da Unidade Rede Neural.
Este mesmo ﬂuxo se repete quando a máquina de estado da NOP_Input termina de
carregar todas as janelas da imagem, tendo acionamento para o NOP_Control e este irá notiﬁ-
car o NOP_Output, porém com a diferença de que o estado desses componentes é inicializado
para inativo novamente. Quando for escrito o último resultado pela NOP_Output é gerada uma
notiﬁcação para a NOP_Main.
Figura 42 – Diagrama de Atividade do SysML - Parte 2. Diagrama criado com a ferramenta Astah
UML.
Fonte: Autoria própria (2025).


86
Figura 43 – Diagrama de Atividade do SysML - Parte 3. Diagrama criado com a ferramenta Astah
UML.
Fonte: Autoria própria (2025).
Finalmente, a Figura 44 é a continuação ﬁnal das duas ﬁguras anteriores. O ﬂuxo desta
etapa é o mais simples, com a entidade NOP_Main recebendo a notiﬁcação de término da
execução da camada, e apenas realiza a decisão se ainda existem camadas para continuar e
dessa maneira voltando para o ﬂuxo da Figura 41 ou se todas as camadas da Rede Neural já
foram executadas, ﬁnaliza a execução.
Figura 44 – Diagrama de Atividade do SysML - Parte 4. Diagrama criado com a ferramenta Astah
UML.
Fonte: Autoria própria (2025).
Em resumo, o Controlador modelado em Paradigma Orientado a Notiﬁcações tem uma
sequência de operações que consegue suprir o objetivo de controlar o ﬂuxo das operações na
Unidade Rede Neural a ﬁm de ter eﬁciência computacional pela implementação de pipeline.
3.6
Considerações sobre o Trabalho Realizado
Este capítulo apresentou a metodologia de desenvolvimento, considerando os objetivos
deﬁnidos para este trabalho. Foi destacada a complexidade envolvida na implementação de
uma Rede Neural Artiﬁcial em hardware, bem como as soluções propostas para superar tais
desaﬁos.
Conforme discutido anteriormente, Redes Neurais Artiﬁciais são estruturas essencial-
mente matemáticas. Assim, qualquer solução que as implemente deve priorizar a otimização


87
das operações matemáticas envolvidas. Nesse contexto, foi desenvolvida a Unidade de Rede
Neural, que emprega diversas técnicas de otimização matemática para garantir maior eﬁciência.
Entretanto, essa abordagem resulta em maior complexidade no controle de hardware, além de
exigir o uso de pipelines para melhorar o desempenho computacional, o que demanda sincroni-
zação e comunicação eﬁcaz entre os componentes.
Para viabilizar o controle necessário e a implementação do pipeline, este trabalho utiliza
a modelagem baseada no Paradigma Orientado a Notiﬁcações (PON) nas máquinas de esta-
dos. Tal escolha se justiﬁca pelo desacoplamento proporcionado pelo paradigma, que facilita o
gerenciamento e a interação entre os componentes do sistema.


88
4 RESULTADOS
A solução proposta por este trabalho para Rede Neural Convolucional foi implementada
com sucesso, com testes no modelo de CNN mencionado na Seção 3.1 tendo obtido os mesmos
resultados matemáticos que implementações de referência do framework tensorﬂow utilizado
neste presente trabalho, conforme explicado na Seção 3.1 e utilizando o procedimento deta-
lhado nesta Seção. Todos os resultados da FPGA foram simulados no software ModelSim do
ambiente Quartus Prime 17.1, usando como base a FPGA Cyclone V da placa DE-10 Standard
da empresa Terasic (TERASIC, 2018).
A base de dados do MNIST foi utilizada para validação o problema de classiﬁcação de
dígitos. A Figura 45 é um exemplo de imagem usada para validação, onde foi obtido na saída
do modelo o tensor quantizado [3, 5, 255, 0, 0, 0, 4, 0, 0, 0], percebendo-se que o terceiro dígito
é o maior entre todos os elementos do tensor, consequentemente a Rede Neural detectou que
é mais provável que esta imagem seja de um dígito do número dois. Para esta Figura se tem
que a cor preta representa um píxel de valor ’0’ (zero), e quanto mais clara a cor, maior o valor
do píxel, sendo que a cor ’amarela’ representa o valor 255,
Figura 45 – Imagem classiﬁcada como o dígito 2, oriunda do Dataset MNIST.
Fonte: Autoria própria (2025).
A implementação em FPGA teve sucesso, utilizando a arquitetura especiﬁcada na Seção
3.2 utilizando-se de 8 instâncias de Unidade Rede Neurais, e conseguiu alcançar o objetivo
de frequência de 200 MHz sendo validado utilizando a ferramenta TimeQuest Timing Analyzer
(INTEL, 2022) da fabricante Intel no perﬁl Slow 1100mV 85C, que é o pior caso em execução.
De maneira similar, foram obtidos os recursos de hardware, CLBs e DSPs utilizados na solução,
que podem ser vistos na Tabela 3, onde pode ser percebido que o principal recurso utilizado
foram os blocos de DSP, com a utilização de um pouco mais da metade disponível neste modelo
de FPGA.


89
Este resultado apresenta pontos positivos e negativos, notando-se principalmente que o
tamanho da solução não pode ser dobrado para que se aproveite mais do paralelismo, apesar
de que a FPGA ainda tenha bastantes recursos de DSPs, sendo este o principal ponto nega-
tivo. Porém, um ponto positivo é que os recursos gerais da FPGAs não foram muito utilizados,
permitindo com que esta implementação seja utilizada juntamente a outros softcores como por
exemplo processadores, periféricos, interfaces de rede, etc.
Consequentemente, este resultado é positivo, ainda tendo diversos pontos a melhorar
como, por exemplo, o desacoplamento dos Blocos de Conversão e Ativação da Unidade Rede
Neural permitindo com que sejam utilizados menos recursos de DSPs e desta maneira aumentar
as instâncias possíveis de Unidades Rede Neural na solução.
Tabela 3 – Recursos utilizados na Implementação da Rede Neural
Recurso
Utilizado
Total
%
CLBs
3492
41910
8
Registradores
10174
167640
6
M10K (Memórias)
128
553
23
DSP
59
112
53
Frequência (max)
204.21 MHz
-
-
Fonte: Autoria própria (2025).
O esquema de quantização utilizado neste presente trabalho também foi validado, con-
forme pode ser visto na Tabela 4 comparando a acurácia, isto é a porcentagem em que o modelo
inferiu o dígito correto comparado ao total dos testes, do modelo em seu formato ﬂoat32 original
e depois em seu formato quantizado em int8.
Para esses teste, foi utilizado o modelo original da Seção 3.1, que é o modelo com três
camadas de convolução e duas variantes com duas camadas convolucionais e quatro cama-
das convolucionais, que podem ser visto nas Figuras 46 e 47 respectivamente e com pesos se
referindo a quantidade total de parâmetros da rede para demonstrar o tamanho desses mode-
los. É notável que apesar de se ter degradação na acurácia, o efeito é muito pequeno e desta
maneira validando que a quantização apresenta os mesmos resultados, apenas com uma mar-
gem de erro um pouco maior. Além disso, é possível perceber que a quantização tem o mesmo
comportamento com Redes Neurais Convolucionais maiores ou menores, ou seja, aparenta ser
independente do tamanho.


90
Figura 46 – Variante do Modelo com 2 Camadas Convolucionais.
Fonte: Autoria própria (2025).
Figura 47 – Variante do Modelo com 4 Camadas Convolucionais.
Fonte: Autoria própria (2025).
Tabela 4 – Resultados de Experimento sobre acurácia dos modelos obtidos
Modelo
Acurácia (ﬂoat32)
Acurácia (int8)
Modelo com 2 Camadas (17578 pesos)
99.16%
98.27%
Modelo com 3 Camadas (26826 pesos)
99.3%
98.55%
Modelo com 4 Camadas (33194 pesos)
99.39%
98.49%
Fonte: Autoria própria (2025).
Finalmente, foi realizada comparação do desempenho da implementação realizada
neste trabalho com uma implementação do modelo na linguagem C, criada para este trabalho,
sobre os três modelos de duas, três e quatro camadas convolucionais utilizados no experimento
anterior e plataformas de hardware: ARM Cortex A53 com frequência de clock de 1.2 GHz em
um Raspberry Pi 3B, simulação da FPGA Cyclone V em uma frequência de clock de 200 Mhz
e um computador desktop com processador AMD Ryzen 7 3700X, com frequência de clock de
4.4 GHz. O teste foi realizado sobre a execução dos modelos em uma mesma imagem cem ve-
zes e se obtendo a média aritmética, com exceção do FPGA, onde por ser simulação o tempo
de execução é determinístico. Em todos os casos, a implementação deste trabalho obteve um
speedup sobre as alternativas, porém é notável que o grau de speedup é maior conforme o
tamanho do modelo aumenta, chegando a ser 155 vezes mais rápido que o Raspberry Pi 3B e
6.6 vezes mais rápido que o Ryzen 7 3700X.


91
Tabela 5 – Resultados de Experimento sobre tempo de execução obtidos
Modelo
ARM Cortex A53
Cyclone V
Speedup sobre ARM
Ryzen 7 3700X
Speedup sobre Ryzen
Modelo com 2 Camadas
16.9 ms
0.201 ms
x84.08
0.615 ms
3.05x
Modelo com 3 Camadas
93.2 ms
0.624 ms
x149.35
3.6 ms
5.77x
Modelo com 4 Camadas
151.4 ms
0.973 ms
x155.60
6.45 ms
6.63x
Fonte: Autoria própria (2025).
Desta forma, foram realizados diversos experimentos sobre a implementação do pre-
sente trabalho, a qual obteve resultados interessantes, mesmo quando se comparando a pro-
cessadores mais modernos do que a FPGA em questão. Enquanto que apesar da utilização de
formatos numéricos menos precisos, foi capaz de manter a acurácia.


92
5 CONCLUSÃO E TRABALHOS FUTUROS
5.1
Conclusão
Este trabalho visou a implementação de uma solução de inferências de Redes Neurais
Convolucionais (Convolutional Neural Networks) em FPGA com um Controlador modelado em
PON.
A implementação foi realizada com um modelo híbrido, utilizando o PON como ferra-
menta de modelagem lógica-causal para os processos paralelos das máquinas de estados, e
usando a linguagem de VHDL para a síntese dos circuitos para a FPGA.
Foi possível alcançar os objetivos propostos, tendo sido obtidos resultados de speed up
mesmo sobre processadores mais modernos (em relação ao chip da FPGA) e preservando a
acurácia com o esquema de quantização utilizado.
O Paradigma Orientado a Notiﬁcações (PON) demonstrou alto potencial para aplicação
na modelagem de projetos de hardware, especialmente devido às suas características que fa-
vorecem a modelagem de máquinas de estados. No entanto, este trabalho ainda não explora o
PON em sua totalidade, o que seria viável com a utilização de ferramentas como o PON-HD.
A escolha por não utilizar o PON-HD decorreu de algumas limitações da ferramenta, tais como
a impossibilidade de instanciar blocos de memória, a ausência de suporte para tipos de dados
especíﬁcos, como int19, e a falta de controle sobre a quantidade de ciclos necessários para
determinadas operações.
Os objetivos gerais, que eram de executar uma arquitetura de inferência de Rede Neural
Convolucional em FPGA e utilizando a modelagem do PON, foram alcançados, assim como os
objetivos especíﬁcos.
• Implementar o processo de inferência de Rede Neural Convolucional em FPGA. Para
isso, implementar e testar as seguintes operações: Camada Convolucional, Camada
Fully Connected e Camada MaxPool, funções de ativações ReLU (Rectiﬁed Linear
Unit) e Sigmoidal (Sigmoid).
• Avaliar característica de frequência do circuito implementado, visando que seja possí-
vel usar um clock de 200 MHz para este.
• Avaliar os ganhos de desempenho em relação à execução em processadores tradicio-
nais
5.2
Trabalhos Futuros
Conforme visto, enquanto o trabalho teve sucesso, ainda há diversas possibilidades de
melhorias para trabalhos futuros. Primariamente, como o foco da implementação foi em desen-


93
volver uma prova de conceito, ainda existem diversas possibilidades de otimização sobre a sua
arquitetura.
Um exemplo consiste nos circuitos de conversão que acabaram sendo acoplados as
Unidades de Rede Neural, mas como essas demoram vários ciclos para calcular um resultado,
esses circuitos acabam sendo pouco utilizados. Como esses circuitos necessitam de multiplica-
dores de 32-bits, eles são grandes consumidores de DSPs. Ao desacoplar eles da Unidade de
Rede Neural, podemos implementar uma quantidade menor desses circuitos, permitindo com
que DSPs sejam liberados para serem usados em outras Unidades de Rede Neural.
Porém, essas otimizações requerem circuitos de controle mais avançados, com lógica
de bloqueios sendo necessária.
Um outro avanço é sobre a questão da maneira como é utilizado o PON no hardware,
que neste trabalho foi limitada, porém, com evoluções nos frameworks do PON e mais trabalhos
utilizando este em hardware, podem surgir novas possibilidades de modelagem e implementa-
ção a serem exploradas. Um exemplo séria uma implementação totalmente em PON-HD.
Um próximo passo direto que decorre do presente trabalho, é realizar um estudo de
escalabilidade deste, pois só foram realizados testes com redes relativamente pequenas e em
simulação. Para isso seria provavelmente necessário implementar portas de barramento mestre,
por exemplo, AXI Mestre, para se poder utilizar memória externa da FPGA, com a memória
interna sendo utilizada para outros ﬁns do que o armazenamento total da rede.


94
REFERÊNCIAS
ALBAWI, S.; MOHAMMED, T. A.; AL-ZAWI, S. Understanding of a convolutional neural network.
In: IEEE. 2017 international conference on engineering and technology (ICET). [S.l.], 2017.
p. 1–6.
AMD Xilinx. UG384 - Spartan-6 FPGA Conﬁgurable Logic Block User Guide. Santa Clara,
California, USA, 2010. Disponível em: https://docs.amd.com/v/u/en-US/ug384.
AMD Xilinx. Versal ACAP Conﬁgurable Logic Block Architecture Manual (AM005). Santa
Clara, California, USA, 2023. Disponível em: https://docs.amd.com/r/en-US/am005-versal-clb/
Overview.
BANASZEWSKI, R. F. et al. Paradigma orientado a notiﬁcações: avanços e comparações.
2009. Tese (Doutorado) — Dissertação de Mestrado, CPGEI/UTFPR, Curitiba, 2009.
BARRETTO, W. R.; VENDRAMIN, A. C. B. K.; SIMÃO, J. M. Notiﬁcation oriented paradigm for
distributed systems. Anais do Computer on the Beach, v. 9, p. 110–119, 2018.
BRAVO-MUÑOZ, I.; GARDEL-VICENTE, A.; LÁZARO-GALILEA, J. L. New Applications and
Architectures Based on FPGA/SoC. [S.l.]: MDPI, 2020. 1789 p.
BUENO, E. J. et al. A dsp-and fpga-based industrial control with high-speed communication
interfaces for grid converters applied to distributed power generation systems. IEEE
transactions on industrial electronics, IEEE, v. 56, n. 3, p. 654–669, 2008.
CHOLLET, F. Simple MNIST convnet. 2021. https://keras.io/examples/vision/mnist_convnet//.
Disponível em: https://keras.io/examples/vision/mnist_convnet//.
DENG, L. The mnist database of handwritten digit images for machine learning research [best
of the web]. IEEE signal processing magazine, IEEE, v. 29, n. 6, p. 141–142, 2012.
DEVELOPERS, T. Tensorﬂow. Zenodo, 2022.
DHRUV, P.; NASKAR, S. Image classiﬁcation using convolutional neural network (cnn) and
recurrent neural network (rnn): A review. Machine learning and information processing:
proceedings of ICMLIP 2019, Springer, p. 367–381, 2020.
FAROOQ, U. et al. Fpga architectures: An overview. Tree-Based Heterogeneous FPGA
Architectures: Application Speciﬁc Exploration and Optimization, Springer, p. 7–48, 2012.
GABBRIELLI, M.; MARTINI, S. Programming languages: principles and paradigms. [S.l.]:
Springer Science & Business Media, 2010.
GANDHARE, S.; KARTHIKEYAN, B. Survey on fpga architecture and recent applications.
In: IEEE. 2019 International Conference on Vision Towards Emerging Trends in
Communication and Networking (ViTECoN). [S.l.], 2019. p. 1–4.
GERSHO, A. Principles of quantization. IEEE Transactions on circuits and systems, IEEE,
v. 25, n. 7, p. 427–436, 1978.
GOLDBERG, D. What every computer scientist should know about ﬂoating-point arithmetic.
ACM computing surveys (CSUR), ACM New York, NY, USA, v. 23, n. 1, p. 5–48, 1991.
GOODFELLOW, I.; BENGIO, Y.; COURVILLE, A. Deep Learning. [S.l.]: MIT Press, 2016.
http://www.deeplearningbook.org.


95
GOOGLE. Google Coral. 2019. https://coral.ai/. Disponível em: https://coral.ai/.
GOOGLE. Google TPU - System Architecture. 2022. https://cloud.google.com/tpu/
docs/system-architecture-tpu-vm/. Disponível em: https://cloud.google.com/tpu/docs/
system-architecture-tpu-vm/.
GRAY, R. M.; NEUHOFF, D. L. Quantization. IEEE transactions on information theory, IEEE,
v. 44, n. 6, p. 2325–2383, 1998.
HOROWITZ, M. 1.1 computing’s energy problem (and what we can do about it). In: 2014 IEEE
International Solid-State Circuits Conference Digest of Technical Papers (ISSCC). [S.l.:
s.n.], 2014. p. 10–14.
IEEE Standard for Floating-Point Arithmetic. IEEE Std 754-2019 (Revision of IEEE 754-2008),
p. 1–84, 2019.
IGNATOV, A. et al. Ai benchmark: All about deep learning on smartphones in 2019. In: IEEE.
2019 IEEE/CVF International Conference on Computer Vision Workshop (ICCVW). [S.l.],
2019. p. 3617–3635.
INTEL. Intel Quartus Prime Pro Edition User Guide: Timing Analyzer. 2022.
Intel Corporation. Cyclone V Device Handbook Volume 1. San Jose, California, USA, 2023.
JACOB, B. et al. Quantization and training of neural networks for efﬁcient integer-arithmetic-only
inference. CoRR, abs/1712.05877, 2017. Disponível em: http://arxiv.org/abs/1712.05877.
KAISLER, S. H. Software paradigms. [S.l.]: John Wiley & Sons, 2005.
KERSCHBAUMER, R. et al. The notiﬁcation oriented paradigm language to digital hardware as
an intuitive high-level synthesis tool. Revista de Informática Teórica e Aplicada, v. 28, n. 2, p.
90–106, 2021.
KERSCHBAUMER, R. et al. Proposição do paradigma orientado a notiﬁcações no
desenvolvimento de circuitos lógico-digitais reconﬁguráveis. Universidade Tecnológica Federal
do Paraná, 2018.
KLUSKA, P.; ZI ˛EBA, M. Post-training quantization methods for deep learning models. In:
SPRINGER. Intelligent Information and Database Systems: 12th Asian Conference,
ACIIDS 2020, Phuket, Thailand, March 23–26, 2020, Proceedings, Part I 12. [S.l.], 2020. p.
467–479.
KOROL, G. An fpga implementation for convolutional neural network. In: Pontiﬁcal Catholic
University of Rio Grande Do Sul. [S.l.: s.n.], 2019.
LECUN, Y. The mnist database of handwritten digits. http://yann.lecun.com/exdb/mnist/,
1998. Disponível em: https://cir.nii.ac.jp/crid/1571417126193283840.
LI, Z. et al. A survey of convolutional neural networks: analysis, applications, and prospects.
IEEE transactions on neural networks and learning systems, IEEE, v. 33, n. 12, p.
6999–7019, 2021. Disponível em: https://ieeexplore.ieee.org/abstract/document/9451544.
LIANG, T. et al. Pruning and quantization for deep neural network acceleration: A survey.
Neurocomputing, Elsevier, v. 461, p. 370–403, 2021.
LIBANO, F. et al. Understanding the impact of quantization, accuracy, and radiation on the
reliability of convolutional neural networks on fpgas. IEEE Transactions on Nuclear Science,
IEEE, v. 67, n. 7, p. 1478–1484, 2020.


96
LINHARES, R. R. Contribuição para o desenvolvimento de uma arquitetura de computação
própria ao paradigma orientado a notiﬁcações. Tese de Doutorado, CPGEI, UTFPR, 2015.
LIU, F. et al. Improving neural network efﬁciency via post-training quantization with adaptive
ﬂoating-point. In: Proceedings of the IEEE/CVF international conference on computer
vision. [S.l.: s.n.], 2021. p. 5281–5290.
LO, C. Y.; LAU, F. C.; SHAM, C.-W. Fixed-point implementation of convolutional neural networks
for image classiﬁcation. In: IEEE. 2018 International Conference on Advanced Technologies
for Communications (ATC). [S.l.], 2018. p. 105–109.
MAI, M.; FEDYUNIN, V.; WEI, W. Accelerating PyTorch Vision Mo-
dels with Channels Last on CPU. 2022. https://pytorch.org/blog/
accelerating-pytorch-vision-models-with-channels-last-on-cpu/. Disponível em:
https://pytorch.org/blog/accelerating-pytorch-vision-models-with-channels-last-on-cpu/.
MAXFIELD, C. An introduction to different rounding algorithms. Programmable Logic Design
Line, p. 1–15, 2006.
MENDONCA, I. T. M. Metodologia de projeto de software orientado a notiﬁcações. Tese de
Doutorado, CPGEI, UTFPR, 2020.
MICHELSANTI, D. et al. An overview of deep-learning-based audio-visual speech enhancement
and separation. IEEE/ACM Transactions on Audio, Speech, and Language Processing,
IEEE, v. 29, p. 1368–1396, 2021.
MITTAL, S. A survey of fpga-based accelerators for convolutional neural networks. Neural
computing and applications, Springer, v. 32, n. 4, p. 1109–1139, 2020.
MULLER, J.-M. et al. Handbook of ﬂoating-point arithmetic. [S.l.]: Springer, 2018. v. 1.
NEGRINI, F. et al. Nopl-erlang: Programação multicore transparente em linguagem de alto
nível. Cadernos do IME-Série Informática, v. 43, p. 70–74, 2019.
NEVES, F. d. S. Framework pon c++ 4.0: contribuição para a concepção de aplicações
no paradigma orientado a notiﬁcações por meio de programação genérica. Disertaçã de
Mestrado, CPGEI, UTFPR, 2021.
NOVAES, P. J. D. Método e linguagem para modelagem gráﬁca de requisitos de software e
sistemas. Disertaçã de Mestrado, CPGEI, UTFPR, 2019.
OLIVEIRA, R. N. Assistência à autonomia domiciliar empregando paradigma orientado a
notiﬁcações. Disertaçã de Mestrado, CPGEI, UTFPR, 2019.
OPENVINO. GNA device. 2022. https://docs.openvino.ai/latest/openvino_docs_OV_UG_
supported_plugins_GNA.html/. Disponível em: https://docs.openvino.ai/latest/openvino_docs_
OV_UG_supported_plugins_GNA.html/.
O’SHEA, K.; NASH, R. An introduction to convolutional neural networks. arXiv preprint
arXiv:1511.08458, 2015.
OSHIRO, L. K. Contribuição em paradigma orientado a notiﬁcações: evolução da tecnologia
lingpon 2.0 via aprimoramento da linguagem e compilador para código notiﬁcante modular em
c++. Disertaçã de Mestrado, CPGEI, UTFPR, 2021.
PERI, D.; PATEL, J.; PARK, J. Deploying quantization-aware trained networks using tensorrt. In:
GPU Technology Conference. [S.l.: s.n.], 2020.


97
PORDEUS, L. F. Simulação de uma arquitetura de computação própria ao paradigma orientado
a notiﬁcações. Disertaçã de Mestrado, CPGEI, UTFPR, 2017.
PORDEUS, L. F. et al. Notiﬁcation oriented paradigm to digital hardware—a benchmark
evaluation with random forest algorithm. Microprocessors and Microsystems, Elsevier, v. 103,
p. 104951, 2023.
QUALCOMM. Hexagon DSP SDK. 2022. https://developer.qualcomm.com/software/
hexagon-dsp-sdk/dsp-processor/. Disponível em: https://developer.qualcomm.com/software/
hexagon-dsp-sdk/dsp-processor/.
QUINNELL, E.; SWARTZLANDER, E. E.; LEMONDS, C. Floating-point fused multiply-add
architectures. In: IEEE. 2007 Conference Record of the Forty-First Asilomar Conference on
Signals, Systems and Computers. [S.l.], 2007. p. 331–337.
RONSZCKA, A. F. Método para a criação de linguagens de programação e compiladores para
o paradigma orientado a notiﬁcações em plataformas distintas. Tese de Doutorado, CPGEI,
UTFPR, 2019.
RONSZCKA, A. F. et al. Notiﬁcation-oriented and rete network inference: A comparative study.
In: IEEE. 2015 IEEE International Conference on Systems, Man, and Cybernetics. [S.l.],
2015. p. 807–814.
RONSZCKA, A. F. et al. Notiﬁcation-oriented programming language and compiler. In: IEEE.
2017 VII Brazilian Symposium on Computing Systems Engineering (SBESC). [S.l.], 2017.
p. 125–131.
SCHÜTZ, F. et al. Neuropon: uma abordagem para o desenvolvimento de redes neurais
artiﬁciais utilizando o paradigma orientado a notiﬁcações. Universidade Tecnológica Federal do
Paraná, 2019.
SHAH, V.; YOUNGBLOOD, N. Leveraging continuously differentiable activation functions for
learning in quantized noisy environments. arXiv preprint arXiv:2402.02593, 2024.
SILVA, I. N. d.; SPATTI, D. H.; FLAUZINO, R. A. Redes neurais artiﬁciais para engenharia e
ciências aplicadas. [S.l.]: Artliber Editora, 2010.
SIMÃO, J. M. Proposta de uma arquitetura de controle para sistemas ﬂexíveis
de manufatura baseada em regras e agentes. [S.l.]: Master in Science Thesis,
CPGEI/CEFETPR. Curitiba-PR–Brazil, 2001.
SIMÃO, J. M. A Contribution to the Development of a HMS simulation tool and
Proposition of a Meta-Model for Holonic Control. 2005. Tese (Doutorado) — Université Henri
Poincaré-Nancy 1; Universidade Tecnológica Federal do . . . , 2005.
SIMÃO, J. M. et al. Comparações entre duas materializações do paradigma orientado a
notiﬁcações (pon): Framework pon prototipal versus framework pon primário. IV Congreso
Internacional de Computación y Telecomunicaciones, Universidad Inca Garcilaso de la
Vega, 2012.
SIMÃO, J. M.; TACLA, C. A.; STADZISZ, P. C. Holonic control metamodel. IEEE Transactions
on Systems, Man, and Cybernetics-Part A: Systems and Humans, IEEE, v. 39, n. 5, p.
1126–1139, 2009.
SKAHILL, K. VHDL for programmable logic. [S.l.]: Addison-Wesley Longman Publishing Co.,
Inc., 1996.


98
SRIVASTAVA, S. et al. Comparative analysis of deep learning image detection algorithms.
Journal of Big Data, SpringerOpen, v. 8, n. 1, p. 1–27, 2021.
STOKES, J. Inside the machine: an illustrated introduction to microprocessors and
computer architecture. [S.l.]: No starch press, 2007.
SURYADEVARA, S.; YANAMALA, A. K. Y. A comprehensive overview of artiﬁcial neural
networks: Evolution, architectures, and applications. Revista de Inteligencia Artiﬁcial en
Medicina, v. 12, n. 1, p. 51–76, 2021.
SZE, V. et al. Efﬁcient processing of deep neural networks: A tutorial and survey. Proceedings
of the IEEE, Ieee, v. 105, n. 12, p. 2295–2329, 2017.
TAO, Y. et al. Challenges in energy-efﬁcient deep neural network training with fpga. In:
Proceedings of the IEEE/CVF conference on computer vision and pattern recognition
workshops. [S.l.: s.n.], 2020. p. 400–401.
TERASIC. Terasic DE-10 Standard Overview. 2018. https://www.terasic.com.tw/cgi-bin/
page/archive.pl?Language=English&CategoryNo=165&No=1081&PartNo=1. Disponível em:
https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&CategoryNo=165&No=
1081&PartNo=1.
TSMOTS, I.; SKOROKHODA, O.; RABYK, V. Hardware implementation of sigmoid activation
functions using fpga. In: IEEE. 2019 IEEE 15th International Conference on the Experience
of Designing and Application of CAD Systems (CADSM). [S.l.], 2019. p. 34–38.
TULI, S. et al. Are convolutional neural networks or transformers more like human vision? arXiv
preprint arXiv:2105.07197, 2021.
VALENÇA, G. Z. Contribuição para materialização do paradigma orientado a notiﬁcações
(PON) via framework e wizard. 2012. Dissertação (Mestrado) — Universidade Tecnológica
Federal do Paraná, 2012.
WIECHETECK, L. Software design method using notiﬁcation oriented paradigm—nop. Master’s
Thesis, Graduate School in Electrical Engineering and Industrial Computer Science
(CPGEI) at the Federal University of Technology-Paraná (UTFPR), Curitiba, Brazil, 2011.
WITT, F. D. et al. Comparação entre o paradigma orientado a objetos (poo) e o paradigma
orientado a notiﬁcações (pon) em um controle discreto em lógica reconﬁgurável. XVI Seminário
de Iniciação Cientíﬁca e Tecnológica da UTFPR. Ponta Grossa-PR Brasil, Setembro, 2011.
WU, H. et al. Integer quantization for deep learning inference: Principles and empirical
evaluation. CoRR, abs/2004.09602, 2020. Disponível em: https://arxiv.org/abs/2004.09602.
WU, Y.-c.; FENG, J.-w. Development and application of artiﬁcial neural network. Wireless
Personal Communications, Springer, v. 102, p. 1645–1656, 2018.
XAVIER, R. D. Paradigmas de desenvolvimento de software: comparação entre abordagens
orientada a eventos e orientada a notiﬁcações. Master in Science Thesis at the Federal
University of Technology–Paraná (UTFPR). Curitiba–Paraná (PR), Brazil, 2014.
YANG, X. et al. Fpga implementation of a deep learning acceleration core architecture for image
target detection. Applied Sciences, MDPI, v. 13, n. 7, p. 4144, 2023.
ZHANG, A. et al. Dive into deep learning. arXiv preprint arXiv:2106.11342, 2021.


99
ÇEVIK, K.; BO˘gA, M. Body condition score (bcs) segmentation and classiﬁcation in dairy cows
using r-cnn deep learning architecture r-cnn. European Journal of Science and Technology,
p. 1248–1255, 12 2019.


100
APÊNDICE A – Modelagem em LingPON


101
Este apêndice apresenta o código-fonte em LingPON 3.0 utilizado na implementação do
Controlador PON, conforme descrito na Seção 3.5.
Listagem 10 – Parte 1 - Modelagem em LingPON
1
fbe NOP_Main
2
a t t r i b u t e
atMainStart
:
v o l a t i l e
boolean = false
3
a t t r i b u t e atCamada :
integer = 0
4
a t t r i b u t e
atMainState
:
integer = 0
5
a t t r i b u t e
atLastLayer
:
boolean = false
6
a t t r i b u t e
regRunning
:
boolean = false
7
a t t r i b u t e regDadosCamada :
integer = 0
8
a t t r i b u t e
regCamadas :
constant
integer [ ]
9
10
method m t M a i n I n i c i a l i z a r :
( )
11
atCamada = 0;
12
atRunning = true ;
13
atMainStart = false ;
14
atLastLayer = false ;
15
end
16
17
method mtCarregarCamada :
( )
18
regDadosCamadas = lerCamada ( regCamadas [ atCamada ] ) ;
19
atCamada = atCamada + 1;
20
i f ( atCamada == length ( lerCamada ) )
21
{
22
atLastLayer = true ;
23
}
24
atMainState = 1;
25
end
26
27
method mtCarregarParametros :
( )
28
atMainState = 2;
29
end
30
31
method mtExecutar :
( )
32
atMainState = 3;
33
end
34
35
method mtFinish :
( )
36
atMainState = 0;
37
regRunning = false ;
38
end
39
40
premise prEqZMainState :
atMainState == 0
41
premise prEqMainStart :
atMainStart == true
Fonte: Autoria própria (2025).


102
Listagem 11 – Parte 2 - Modelagem em LingPON
1
rule
rlMainStart :
prEqZMainState and prEqMainStart
2
m t M a i n I n i c i a l i z a r ( ) ;
3
mtCarregarCamada ( ) ;
4
end
5
6
premise prEqOneMainState :
atMainState == 1
7
8
rule
rlParametros :
prEqOneMainState
9
mtCarregarParametros ( ) ;
10
end
11
12
premise prEqTwoMainState :
atMainState == 2
13
premise prEqParFinish :
parametros . atParFinished == true
14
15
rule
rlTerminoParametros :
prEqTwoMainState and prEqParFinish
16
mtExecutar ( ) ;
17
end
18
19
premise prEqThreeMainState :
atMainState == 3
20
premise prEqOutFinish :
output . atOutputFinished == true
21
premise prNeqMainLast :
atLastLayer == false
22
23
rule
rlTerminoExecutar :
prEqThreeMainState and prEqOutFinish
24
and prNeqMainLast
25
mtCarregarCamada ( ) ;
26
end
27
28
premise prEqMainLast :
atLastLayer == true
29
30
rule
rlTerminoRede :
prEqThreeMainState and prEqOutFinish
31
and prEqMainLast
32
mtFinish ( ) ;
33
end
34
35
end
36
37
fbe NOP_Parametros
38
39
a t t r i b u t e
atParState :
integer = 0
40
a t t r i b u t e
atCurrentPar :
v o l a t i l e
integer = 0
41
a t t r i b u t e
atParFinished :
boolean = false
42
a t t r i b u t e
regParWrite :
char = 0
43
a t t r i b u t e
regParData :
integer ;
44
a t t r i b u t e
regParArray :
const
integer [ ]
45
a t t r i b u t e
regParOffset :
v o l a t i l e
integer = 0
Fonte: Autoria própria (2025).


103
Listagem 12 – Parte 3 - Modelagem em LingPON
1
method mtParIncia liza r :
( )
2
atParState = 1;
3
atCurrentPar = 0;
4
atParFinished = false ;
5
regParWrite = 1;
6
end
7
8
method mtParExecute ( )
9
regParData = regParArray [ atCurrentPar + regParOffset ] ;
10
regParWrite = regParWrite << 1;
11
atCurrentPar = atCurrentPar + 1;
12
end
13
14
method mtParFinish ( )
15
atParState = 0;
16
atParFinished = true
17
regParWrite = 0;
18
end
19
20
premise prEqTwoMainState :
main_controller . atMainState == 2
21
premise prEqParStart :
atParState == 0
22
23
rule
r l P a r S t a r t :
prEqTwoMainState and prEqParStart
24
mtParIncia liza r ( ) ;
25
end
26
27
premise prNeqCurrentPar :
atCurrentPar
!= 32
28
premise prEqCurrentPar :
atCurrentPar == 32
29
premise prEqOneParState :
atParState == 1
30
31
rule
rlParExecute :
prEqOneParState and prNeqCurrentPar
32
mtParExecute ( ) ;
33
end
34
35
rule
r l P a r F i n i s h :
prEqOneParState and prEqCurrentPar
36
mtParFinish ( ) ;
37
end
38
end
39
40
41
fbe NOP_Input
42
a t t r i b u t e
atInputState :
integer = 0
43
a t t r i b u t e
atCurrentX :
integer = 0
Fonte: Autoria própria (2025).


104
Listagem 13 – Parte 4 - Modelagem em LingPON
1
a t t r i b u t e
atCurrentY :
integer = 0
2
a t t r i b u t e
atCurrentChannel :
integer = 0
3
a t t r i b u t e
a t C u r r e n t F i l t e r :
integer = 0
4
a t t r i b u t e
atWindowX :
integer = 0
5
a t t r i b u t e
atWindowY :
integer = 0
6
a t t r i b u t e
atPrevWindowX :
integer = 0
7
a t t r i b u t e
atPrevWindowY :
integer = 0
8
a t t r i b u t e
atPrevCurrentChannel :
integer = 0
9
a t t r i b u t e
atInputNewWindow :
v o l a t i l e
boolean = false
10
a t t r i b u t e
atInputFinished :
boolean = false
11
a t t r i b u t e
regQtdFilter :
v o l a t i l e
integer = 0
12
a t t r i b u t e
regWindowSizeX :
v o l a t i l e
integer = 0
13
a t t r i b u t e
regWindowSizeY :
v o l a t i l e
integer = 0
14
a t t r i b u t e
regQtdChannel :
v o l a t i l e
integer = 0
15
a t t r i b u t e
regImageSizeX :
v o l a t i l e
integer = 0
16
a t t r i b u t e
regImageSizeY :
v o l a t i l e
integer = 0
17
a t t r i b u t e
regStrideX :
v o l a t i l e
integer = 0
18
a t t r i b u t e
regStrideY :
v o l a t i l e
integer = 0
19
a t t r i b u t e
regDadosEntrada :
v o l a t i l e
integer = 0
20
a t t r i b u t e
regPesosEntrada :
v o l a t i l e
integer = 0
21
a t t r i b u t e
regDados :
v o l a t i l e
integer [ ] [ ] [ ]
22
a t t r i b u t e
regPesos :
v o l a t i l e
integer [ ] [ ] [ ] [ ]
23
24
method
m t I n p u t I n i c i a l i z a r :
( )
25
atInputState = 1;
26
atCurrentX = 0;
27
atCurrentY = 0;
28
atCurrentChannel = 0;
29
a t C u r r e n t F i l t e r = 0;
30
atWindowX = 0;
31
atWindowY = 0;
32
atPrevWindowX = 0;
33
atPrevWindowY = 0;
34
atPrevCurrentChannel = 0;
35
atInputNewWindow = false ;
36
atInputFinished = false ;
37
end
38
39
method mtMandarDados :
( )
40
atPrevWindowX = atWindowX ;
41
atPrevWindowY = atWindowY ;
42
atPrevCurrentChannel = atCurrentChannel ;
43
regDadosEntrada = regDados [ atCurrentY + atWindowY ]
44
[ atCurrentX + atWindowX ] [ atCurrentChannel ]
Fonte: Autoria própria (2025).


105
Listagem 14 – Parte 5 - Modelagem em LingPON
1
regPesosEntrada = regPesos [ a t C u r r e n t F i l t e r ]
2
[ atWindowX ] [ atWindowY ] [ atCurrentChannel ] ;
3
end
4
5
method mtProximaCol :
( )
6
atWindowX += 1
7
end
8
9
method mtProximaLinha :
( )
10
atWindowX = 0;
11
atWindowY += 1
12
end
13
14
method mtProximoChannel :
( )
15
atWindowX = 0;
16
atWindowY = 0;
17
atCurrentChannel += 1
18
end
19
20
method mtProximoFiltro :
( )
21
atWindowX = 0;
22
atWindowY = 0;
23
atCurrentChannel = 0;
24
atInputNewWindow = true ;
25
a t C u r r e n t F i l t e r += 1;
26
i f ( a t C u r r e n t F i l t e r == regQtdFilter )
27
{
28
a t C u r r e n t F i l t e r = 0;
29
atCurrentX += 1;
30
i f
( atCurrentX == regImageSizeX )
31
{
32
atCurrentX = 0;
33
atCurrentY += regStrideY ;
34
}
35
}
36
end
37
38
method mtFinishInput :
( )
39
atInputState = 0;
40
atInputFinished = true
41
end
42
43
premise prEqThreeMainState :
main_controller . atMainState == 3
44
premise prEqZeroInputState :
== 0
Fonte: Autoria própria (2025).


106
Listagem 15 – Parte 6 - Modelagem em LingPON
1
rule
r l I n p u t S t a r t :
prEqThreeMainState and prEqZeroInputState
2
m t I n p u t I n i c i a l i z a r ( ) ;
3
end
4
5
premise prChangedWindowX :
atPrevWindowX != atWindowX
6
premise prChangedWindowY :
atPrevWindowY != atWindowY
7
premise prChangedCurrentChannel :
atPrevCurrentChannel
!=
atCurrentChannel
8
9
rule
rlDados :
prEqOneInputState and ( prChangedWindowX
10
or prChangedWindowY or prChangedCurrentChannel )
11
mtMandarDados ( ) ;
12
end
13
14
premise prEqOneInputState :
atInputState == 1
15
premise prNeqWindowX : atWindowX != regWindowSizeX
16
17
rule
r l C o l :
prEqOneInputState and prNeqWindowX
18
mtProximaCol ( ) ;
19
end
20
21
premise prEqWindowX : atWindowX == regWindowSizeX
22
premise prNeqWindowY : atWindowY != regWindowSizeY
23
24
rule
r lL i n h a :
prEqOneInputState and prEqWindowX and prNeqWindowY
25
mtProximaLinha ( ) ;
26
end
27
28
premise prEqWindowY : atWindowY == regWindowSizeY
29
premise prNeqChannel :
atCurrentChannel
!= regQtdChannel
30
31
32
rule
rlChannel :
prEqOneInputState and prEqWindowX
33
and prEqWindowY and prNeqChannel
34
mtProximoChannel ( ) ;
35
end_rule
36
37
premise prEqChannel :
atCurrentChannel == regQtdChannel
38
39
rule
r l F i l t r o :
prEqOneInputState and prEqWindowX
40
and prEqWindowY and prEqChannel
41
mtProximoFiltro ( ) ;
42
end
43
44
premise prEqCurrentY :
atCurrentY == regTamanhoImagemY
45
46
rule
rlTermino :
prEqOneInputState and prEqCurrentY
Fonte: Autoria própria (2025).


107
Listagem 16 – Parte 7 - Modelagem em LingPON
1
mtFinishInput ( ) ;
2
end
3
end
4
5
fbe NOP_Control
6
a t t r i b u t e
atControlState :
integer = 0
7
a t t r i b u t e
atControlNewWindow :
v o l a t i l e
boolean = false
8
a t t r i b u t e
atControlFinished :
boolean = false
9
a t t r i b u t e
regLoad :
v o l a t i l e
boolean = false
10
a t t r i b u t e
regOperation :
v o l a t i l e
boolean = false
11
12
method
m t C o n t r o l I n i c i a l i z a r :
( )
13
atControlState = 1;
14
regLoad = false ;
15
regLoad = true ;
16
atControlFinished = false ;
17
regOperation = false ;
18
delay ( ) ;
19
regOperation = true ;
20
end
21
22
method mtProximoParametro ( )
23
input . atInputNewWindow = false ;
24
delay ( ) ;
25
regLoad = true ;
26
regLoad = false ;
27
atControlNewWindow = true ;
28
end
29
30
method mtFinishControl ( )
31
input . atInputFinished = false ;
32
delay ( ) ;
33
atControlState = 0;
34
atControlFinished = true
35
regOperation = false ;
36
end
37
38
premise prEqThreeMainState :
main_controller . atMainState == 3
39
premise prEqZeroControlState :
atControlState == 0
40
41
rule
r l C o n t r o l S t a r t :
prEqThreeMainState and prEqZeroControlState
42
m t C o n t r o l I n i c i a l i z a r ( ) ;
43
end
Fonte: Autoria própria (2025).


108
Listagem 17 – Parte 8 - Modelagem em LingPON
1
premise prEqOneControlState :
atControlState == 1
2
premise prEqInputNewWindow :
input . atInputNewWindow == true
3
4
rule
rlLoad :
prEqOneControlState and prEqInputNewWindow
5
mtProximoParametro ( ) ;
6
end
7
8
premise prEqInputFinished :
input . atInputFinished == true
9
10
rule
r l F i n i s h C o n t r o l :
prEqOneControlState and prEqInputFinished
11
mtFinishControl ( ) ;
12
end
13
end
14
15
fbe NOP_Output
16
a t t r i b u t e
atOutputState :
integer = 0
17
a t t r i b u t e
atOutputFinished :
boolean = false
18
a t t r i b u t e
regWriteEn :
v o l a t i l e
boolean = false
19
a t t r i b u t e
regCurrentX :
v o l a t i l e
integer = 0
20
a t t r i b u t e
regCurrentY :
v o l a t i l e
integer = 0
21
a t t r i b u t e
regCurrentChannel :
v o l a t i l e
integer = 0
22
a t t r i b u t e
regQtdFilter :
v o l a t i l e
integer = 0
23
a t t r i b u t e
regImageSizeX :
v o l a t i l e
integer = 0
24
a t t r i b u t e
regImageSizeY :
v o l a t i l e
integer = 0
25
a t t r i b u t e
regOutput :
v o l a t i l e
integer [ ] [ ] [ ]
26
a t t r i b u t e
regSaidaURN :
v o l a t i l e
integer
27
28
method m t O u t p u t I n i c i a l i z a r :
( )
29
atOutputState = 1;
30
regLoad = false ;
31
atOutputFinished = false ;
32
regCurrentX = 0;
33
regCurrentY = 0;
34
regCurrentChannel = 0;
35
end
36
37
method mtEscrever :
( )
38
con tr o l . atControlNewWindow = false ;
39
delay ( ) ;
40
regOutput [ regCurrentX ] [ regCurrentY ] [ regCurrentChannel ] = regSaidaURN
;
41
regWriteEn = true ;
42
regCurrentChannel += 1;
Fonte: Autoria própria (2025).


109
Listagem 18 – Parte 9 - Modelagem em LingPON
1
i f ( regCurrentChannel == regQtdFilter )
2
{
3
regCurrentChannel = 0;
4
regCurrentX += 1;
5
i f ( regCurrentX == regImageSizeX )
6
{
7
regCurrentX = 0;
8
regCurrentY += 1;
9
}
10
}
11
regWriteEn = false ;
12
end
13
14
method mtFinishOutput :
( )
15
mtEscrever ( ) ;
16
atOutputState = 0;
17
atOutputFinished = true
18
end
19
20
premise prEqThreeMainState :
main_controller . atMainState == 3 and
21
premise prEqZeroOutputState :
atOutputState == 0
22
23
24
rule
r l O u t p u t S t a r t :
prEqThreeMainState and prEqZeroOutputState
25
m t O u t p u t I n i c i a l i z a r ( ) ;
26
end
27
28
premise prEqOneOutputState :
atOutputState == 1
29
premise prEqControlNewWindow :
co ntr o l . atControlNewWindow == true
30
31
rule
r l W r i t e :
prEqOneOutputState and prEqControlNewWindow
32
mtEscrever ( ) ;
33
end
34
35
premise prEqControlFinished :
co ntr o l . atControlFinished == true
36
37
rule
r l F i n i s h :
prEqOneOutputState and prEqControlFinished
38
mtFinishOutput ( ) ;
39
end_rule
40
41
end
Fonte: Autoria própria (2025).


110
Listagem 19 – Parte 10 - Modelagem em LingPON
1
i n s t
2
NOP_Main main_controller
3
NOP_Parametros parametros
4
NOP_Input input
5
NOP_Control
con tr o l
6
NOP_Output output
7
end_inst
8
9
strategy
10
no_one
11
end_strategy
Fonte: Autoria própria (2025).


111
APÊNDICE B – Código em VHDL


112
Este apêndice apresenta todos os códigos-fonte VHDL utilizados na implementação da
solução proposta na Seção 3, com exceção dos componentes provenientes do PON-HD (em-
pregados no componente FSM_NOP_Input) e dos componentes da FPGA instanciados a partir
das funções da ferramenta Quartus.
Listagem 20 – Parte 1 do arquivo Full_Module.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
5
entity Full_Module is
6
port(clk: in std_logic;
7
start: in std_logic;
8
running: out std_logic;
9
OutputDebug: out std_logic_vector(63 downto 0)
10
);
11
end entity;
12
13
architecture rtl of Full_Module is
14
component convolution is
15
port(clk: in std_logic;
16
rd_en: in std_logic_vector (7 downto 0);
17
activation: in std_logic;
18
load: in std_logic;
19
accumulate: in std_logic;
20
channels: in std_logic_vector (63 downto 0);
21
weight_address: in std_logic_vector (9 downto 0);
22
parameters_adress: in std_logic_vector (7 downto 0);
23
output: out std_logic_vector (63 downto 0));
24
end component;
25
26
27
component data_ram IS
28
PORT
29
(
30
clock
: IN STD_LOGIC
:= ’1’;
31
data
: IN STD_LOGIC_VECTOR (63 DOWNTO 0);
32
rdaddress
: IN STD_LOGIC_VECTOR (12 DOWNTO 0);
33
wraddress
: IN STD_LOGIC_VECTOR (12 DOWNTO 0);
34
wren
: IN STD_LOGIC
:= ’0’;
35
q
: OUT STD_LOGIC_VECTOR (63 DOWNTO 0)
36
);
37
end component;
38
39
component pool_unit is
40
port(clk: in std_logic;
Fonte: Autoria própria (2025).


113
Listagem 21 – Parte 2 do arquivo Full_Module.vhd
1
rst: in std_logic;
2
en: in std_logic;
3
channels: in std_logic_vector (63 downto 0);
4
output: out std_logic_vector (63 downto 0));
5
end component;
6
7
component FSM_NOP_Controlador is
8
port(clk: in std_logic;
9
start: in std_logic;
10
running: out std_logic;
11
poolOrConv: out std_logic;
12
activation: out std_logic;
13
OutputWren : out std_logic;
14
selectModule: out std_logic_vector (7 downto 0);
15
load_shift: out std_logic;
16
accumulate: out std_logic;
17
newPool: out std_logic;
18
DataAddress: out std_logic_vector(12 downto 0);
19
ParameterAddress: out std_logic_vector(7 downto 0);
20
WeightAddress: out std_logic_vector(9 downto 0);
21
OutputAddress: out std_logic_vector(12 downto 0)
22
);
23
end component;
24
25
26
-- Signals
27
signal output: std_logic_vector (63 downto 0);
28
29
-- Conv
30
signal activation: std_logic;
31
signal accumulate: std_logic;
32
signal channels: std_logic_vector (63 downto 0);
33
signal ConvOutput: std_logic_vector (63 downto 0);
34
35
36
-- Pool
37
signal pool_en: std_logic;
38
signal PoolOutput: std_logic_vector (63 downto 0);
39
40
Fonte: Autoria própria (2025).


114
Listagem 22 – Parte 3 do arquivo Full_Module.vhd
1
-- Controlador
2
signal poolOrConv: std_logic;
3
signal OutputWren : std_logic;
4
signal selectModule: std_logic_vector (7 downto 0);
5
signal load_shift: std_logic;
6
signal newPool: std_logic;
7
signal DataAddress: std_logic_vector(12 downto 0);
8
signal ParameterAddress: std_logic_vector(7 downto 0);
9
signal WeightAddress: std_logic_vector(9 downto 0);
10
signal OutputAddress: std_logic_vector(12 downto 0);
11
12
begin
13
14
output <=
ConvOutput when poolOrConv = ’0’ else
15
PoolOutput;
16
17
OutputDebug <= output;
18
19
conv : convolution port map(clk => clk,
20
rd_en => selectModule,
21
activation => activation,
22
load => load_shift,
23
accumulate => accumulate,
24
channels => channels,
25
weight_address => WeightAddress,
26
parameters_adress => ParameterAddress,
27
output => ConvOutput);
28
29
pool : pool_unit port map(clk => clk,
30
rst => newPool,
31
en => ’1’,
-- sempre 1
32
channels => channels,
33
output => PoolOutput);
34
35
controlador : FSM_NOP_Controlador port map(clk => clk,
36
start => start,
37
running => running,
38
poolOrConv => poolOrConv,
39
activation => activation,
40
OutputWren => OutputWren,
Fonte: Autoria própria (2025).


115
Listagem 23 – Parte 4 do arquivo Full_Module.vhd
1
selectModule => selectModule,
2
load_shift => load_shift,
3
accumulate => accumulate,
4
newPool => newPool,
5
DataAddress => DataAddress,
6
ParameterAddress =>
ParameterAddress,
7
WeightAddress => WeightAddress,
8
OutputAddress => OutputAddress);
9
10
ram : data_ram port map(clock => clk,
11
data => output,
12
rdaddress => DataAddress,
13
wraddress => OutputAddress,
14
wren => OutputWren,
15
q => channels);
16
17
18
end architecture;
Fonte: Autoria própria (2025).


116
Listagem 24 – Parte 1 do arquivo convolution.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
5
entity convolution is
6
port(clk: in std_logic;
7
rd_en: in std_logic_vector (7 downto 0);
8
activation: in std_logic;
9
load: in std_logic;
10
accumulate: in std_logic;
11
channels: in std_logic_vector (63 downto 0);
12
weight_address: in std_logic_vector (9 downto 0);
13
parameters_adress: in std_logic_vector (7 downto 0);
14
output: out std_logic_vector (63 downto 0));
15
end entity;
16
17
architecture rtl of convolution is
18
component convolution_module_v3_ring is
19
port(clk: in std_logic;
20
rd_en: in std_logic;
21
activation: in std_logic;
22
load: in std_logic;
23
accumulate: in std_logic;
24
channels: in std_logic_vector (63 downto 0);
25
weights: in std_logic_vector (63 downto 0);
26
bias: in std_logic_vector (31 downto 0);
27
zero_point: in std_logic_vector (31 downto 0);
28
multiplier: in std_logic_vector (31 downto 0);
29
shift: in std_logic_vector (4 downto 0);
30
output: out std_logic_vector (7 downto 0));
31
end component;
32
33
component weight_rom IS
34
GENERIC
35
(
36
file_path : string
37
);
38
PORT
39
(
40
address
: IN STD_LOGIC_VECTOR (9 DOWNTO 0);
Fonte: Autoria própria (2025).


117
Listagem 25 – Parte 2 do arquivo convolution.vhd
1
clock
: IN STD_LOGIC;
2
q
: OUT STD_LOGIC_VECTOR (63 DOWNTO 0)
3
);
4
END component;
5
6
component generic32_rom IS
7
GENERIC
8
(
9
file_path : string
10
);
11
PORT
12
(
13
address
: IN STD_LOGIC_VECTOR (7 DOWNTO 0);
14
clock
: IN STD_LOGIC
:= ’1’;
15
q
: OUT STD_LOGIC_VECTOR (31 DOWNTO 0)
16
);
17
END component;
18
19
component generic5_rom IS
20
GENERIC
21
(
22
file_path : string
23
);
24
PORT
25
(
26
address
: IN STD_LOGIC_VECTOR (7 DOWNTO 0);
27
clock
: IN STD_LOGIC
:= ’1’;
28
q
: OUT STD_LOGIC_VECTOR (4 DOWNTO 0)
29
);
30
END component;
31
32
type array_output is array (natural range <>) of
std_logic_vector (7 downto 0);
33
type array_weights is array (natural range <>) of
std_logic_vector (63 downto 0);
34
35
signal aggregate_output: array_output(7 downto 0);
36
signal weights: array_weights(7 downto 0);
37
38
signal bias, zero_point, multiplier: std_logic_vector (31
downto 0);
39
signal shift:
std_logic_vector (4 downto 0);
40
Fonte: Autoria própria (2025).


118
Listagem 26 – Parte 3 do arquivo convolution.vhd
1
begin
2
3
cmod_0 : convolution_module_v3_ring port map(clk => clk,
4
rd_en => rd_en(0),
5
activation => activation,
6
load => load,
7
accumulate => accumulate,
8
channels => channels,
9
weights => weights(0),
10
bias => bias,
11
zero_point => zero_point,
12
multiplier => multiplier,
13
shift => shift,
14
output => aggregate_output(0));
15
16
17
wrom_0 : weight_rom
generic map(file_path => "./rom_files/
weight_rom_0.mif")
18
port map(clock => clk,
19
address => weight_address,
20
q => weights(0));
21
22
23
cmod_1 : convolution_module_v3_ring port map(clk => clk,
24
rd_en => rd_en(1),
25
activation => activation,
26
load => load,
27
accumulate => accumulate,
28
channels => channels,
29
weights => weights(1),
30
bias => bias,
31
zero_point => zero_point,
32
multiplier => multiplier,
33
shift => shift,
34
output => aggregate_output(1));
35
36
37
wrom_1 : weight_rom
generic map(file_path => "./rom_files/
weight_rom_1.mif")
38
port map(clock => clk,
39
address => weight_address,
40
q => weights(1));
Fonte: Autoria própria (2025).


119
Listagem 27 – Parte 4 do arquivo convolution.vhd
1
2
cmod_2 : convolution_module_v3_ring port map(clk => clk,
3
rd_en => rd_en(2),
4
activation => activation,
5
load => load,
6
accumulate => accumulate,
7
channels => channels,
8
weights => weights(2),
9
bias => bias,
10
zero_point => zero_point,
11
multiplier => multiplier,
12
shift => shift,
13
output => aggregate_output(2));
14
15
16
wrom_2 : weight_rom
generic map(file_path => "./rom_files/
weight_rom_2.mif")
17
port map(clock => clk,
18
address => weight_address,
19
q => weights(2));
20
21
cmod_3 : convolution_module_v3_ring port map(clk => clk,
22
rd_en => rd_en(3),
23
activation => activation,
24
load => load,
25
accumulate => accumulate,
26
channels => channels,
27
weights => weights(3),
28
bias => bias,
29
zero_point => zero_point,
30
multiplier => multiplier,
31
shift => shift,
32
output => aggregate_output(3));
33
34
35
wrom_3 : weight_rom
generic map(file_path => "./rom_files/
weight_rom_3.mif")
36
port map(clock => clk,
37
address => weight_address,
38
q => weights(3));
39
40
cmod_4 : convolution_module_v3_ring port map(clk => clk,
Fonte: Autoria própria (2025).


120
Listagem 28 – Parte 5 do arquivo convolution.vhd
1
rd_en => rd_en(4),
2
activation => activation,
3
load => load,
4
accumulate => accumulate,
5
channels => channels,
6
weights => weights(4),
7
bias => bias,
8
zero_point => zero_point,
9
multiplier => multiplier,
10
shift => shift,
11
output => aggregate_output(4));
12
13
14
wrom_4 : weight_rom
generic map(file_path => "./rom_files/
weight_rom_4.mif")
15
port map(clock => clk,
16
address => weight_address,
17
q => weights(4));
18
19
20
cmod_5 : convolution_module_v3_ring port map(clk => clk,
21
rd_en => rd_en(5),
22
activation => activation,
23
load => load,
24
accumulate => accumulate,
25
channels => channels,
26
weights => weights(5),
27
bias => bias,
28
zero_point => zero_point,
29
multiplier => multiplier,
30
shift => shift,
31
output => aggregate_output(5));
32
33
34
wrom_5 : weight_rom
generic map(file_path => "./rom_files/
weight_rom_5.mif")
35
port map(clock => clk,
36
address => weight_address,
37
q => weights(5));
38
39
40
cmod_6 : convolution_module_v3_ring port map(clk => clk,
Fonte: Autoria própria (2025).


121
Listagem 29 – Parte 6 do arquivo convolution.vhd
1
rd_en => rd_en(6),
2
activation => activation,
3
load => load,
4
accumulate => accumulate,
5
channels => channels,
6
weights => weights(6),
7
bias => bias,
8
zero_point => zero_point,
9
multiplier => multiplier,
10
shift => shift,
11
output => aggregate_output(6));
12
13
14
wrom_6 : weight_rom
generic map(file_path => "./rom_files/
weight_rom_6.mif")
15
port map(clock => clk,
16
address => weight_address,
17
q => weights(6));
18
19
20
cmod_7 : convolution_module_v3_ring port map(clk => clk,
21
rd_en => rd_en(7),
22
activation => activation,
23
load => load,
24
accumulate => accumulate,
25
channels => channels,
26
weights => weights(7),
27
bias => bias,
28
zero_point => zero_point,
29
multiplier => multiplier,
30
shift => shift,
31
output => aggregate_output(7));
32
33
34
wrom_7 : weight_rom
generic map(file_path => "./rom_files/
weight_rom_7.mif")
35
port map(clock => clk,
36
address => weight_address,
37
q => weights(7));
38
39
bias_rom : generic32_rom
generic map(file_path => "./
rom_files/bias.mif")
40
port map(clock => clk,
Fonte: Autoria própria (2025).


122
Listagem 30 – Parte 7 do arquivo convolution.vhd
1
address => parameters_adress,
2
q => bias);
3
4
zp_rom : generic32_rom
generic map(file_path => "./rom_files
/zeropoint.mif")
5
port map(clock => clk,
6
address => parameters_adress,
7
q => zero_point);
8
9
mult_rom : generic32_rom
generic map(file_path => "./
rom_files/mult.mif")
10
port map(clock => clk,
11
address => parameters_adress,
12
q => multiplier);
13
14
shift_rom : generic5_rom
generic map(file_path => "./
rom_files/shift.mif")
15
port map(clock => clk,
16
address => parameters_adress,
17
q => shift);
18
19
20
21
generate_assigment: for i in 0 to 7 generate
22
output((i*8)+7 downto i*8) <= aggregate_output(i);
23
end generate generate_assigment;
24
25
26
end architecture;
Fonte: Autoria própria (2025).


123
Listagem 31 – Parte 1 do arquivo convolution_module_v3_ring.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
5
-- activation = ’0’ RELU, ’1’ SIGMOID
6
7
entity convolution_module_v3_ring is
8
port(clk: in std_logic;
9
rd_en: in std_logic;
10
activation: in std_logic; -- ’0’ RELU, ’1’ SIGMOID
11
load: in std_logic;
12
accumulate: in std_logic;
13
channels: in std_logic_vector (63 downto 0);
14
weights: in std_logic_vector (63 downto 0);
15
bias: in std_logic_vector (31 downto 0);
16
zero_point: in std_logic_vector (31 downto 0);
17
multiplier: in std_logic_vector (31 downto 0);
18
shift: in std_logic_vector (4 downto 0);
19
output: out std_logic_vector (7 downto 0));
20
end entity;
21
22
architecture rtl of convolution_module_v3_ring is
23
component mac_unit is
24
port(clk: in std_logic;
25
channels: in std_logic_vector (63 downto 0);
26
weights: in std_logic_vector (63 downto 0);
27
output: out std_logic_vector(18 downto 0));
28
end component;
29
30
component accumulator_ring is
31
port(clk: in std_logic;
32
load: in std_logic;
33
rd_en: in std_logic;
34
accumulate: in std_logic;
35
input: in signed (18 downto 0);
36
data: in signed(31 downto 0);
37
output: out signed(31 downto 0));
38
end component;
39
40
component converter_v3_ring is
Fonte: Autoria própria (2025).


124
Listagem 32 – Parte 2 do arquivo convolution_module_v3_ring.vhd
1
port(clk: in std_logic;
2
convert: in signed (31 downto 0);
3
offset: in signed (31 downto 0);
4
multiplier: in signed(31 downto 0);
5
shiftamount: in std_logic_vector (4 downto 0);
6
rd_en: in std_logic;
7
shift: in std_logic;
8
output: out signed(31 downto 0));
9
end component;
10
11
component relu_unit_v2 is
12
port(clk: in std_logic;
13
input: in signed(31 downto 0);
14
output: out signed (7 downto 0));
15
end component;
16
17
component activation_unit_8bit_v2 is
18
port(clk: in std_logic;
19
input: in
signed (31 downto 0);
20
output: out signed (7 downto 0));
21
end component;
22
23
24
25
signal mac_result: std_logic_vector(18 downto 0);
26
signal acc_result: signed(31 downto 0);
27
signal cov_result: signed(31 downto 0);
28
signal relu_result:signed(7 downto 0);
29
signal act_result: signed(7 downto 0);
30
31
32
signal mux_output: signed(7 downto 0);
33
34
begin
35
36
mac : mac_unit port map(clk => clk,
37
channels => channels,
38
weights => weights,
39
output => mac_result);
40
Fonte: Autoria própria (2025).


125
Listagem 33 – Parte 3 do arquivo convolution_module_v3_ring.vhd
1
2
acc : accumulator_ring port map(clk => clk,
3
load
=> load,
4
rd_en => rd_en,
5
accumulate => accumulate,
6
input => signed(mac_result),
7
data => signed(bias),
8
output => acc_result);
9
10
cov : converter_v3_ring port map(clk => clk,
11
convert
=> acc_result,
12
offset => signed(zero_point),
13
multiplier => signed(multiplier),
14
shiftamount => shift,
15
rd_en => rd_en,
16
shift => load,
17
output => cov_result);
18
19
relu: relu_unit_v2 port map(clk => clk,
20
input
=> cov_result,
21
output => relu_result);
22
23
24
act: activation_unit_8bit_v2 port map(clk => clk,
25
input
=> cov_result,
26
output => act_result);
27
28
29
-- Select para output
30
mux_output <= relu_result when activation = ’0’ else
31
act_result;
32
--act_result(31 downto 24);
33
34
output <= std_logic_vector(mux_output);
35
end architecture;
Fonte: Autoria própria (2025).


126
Listagem 34 – Parte 1 do arquivo accumulator_ring.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
5
entity accumulator_ring is
6
port(clk: in std_logic;
7
load: in std_logic;
8
rd_en: in std_logic;
9
accumulate: in std_logic;
10
input: in signed (18 downto 0);
11
data: in signed(31 downto 0);
12
output: out signed(31 downto 0));
13
end entity;
14
15
architecture rtl of accumulator_ring is
16
17
signal acc: signed (31 downto 0) := (others => ’0’);
18
19
type t_data is array (3 downto 0) of signed (31 downto 0);
20
signal data_reg: t_data := (others => (others => ’0’));
21
22
begin
23
24
process(clk)
25
variable op1, op2: signed (31 downto 0) := (others => ’0’);
26
begin
27
if rising_edge(clk) then
28
if load = ’1’ then
29
op1 := data_reg(0);
30
else
31
op1 := acc;
32
end if;
33
34
if accumulate = ’1’ then
35
op2 := resize(input, 32);
36
else
37
op2 := (others => ’0’);
38
end if;
39
40
acc <= op1 + op2;
Fonte: Autoria própria (2025).


127
Listagem 35 – Parte 2 do arquivo accumulator_ring.vhd
1
if rd_en = ’1’ then
2
data_reg(3) <= data;
3
l_data: for i in 0 to 2 loop
4
data_reg(i) <= data_reg(i+1);
5
end loop l_data;
6
elsif load = ’1’ then
7
l_shift: for i in 0 to 3 loop
8
data_reg(i) <= data_reg((i+1) mod 4);
9
end loop l_shift;
10
end if;
11
end if;
12
end process;
13
14
output <= acc;
15
16
end architecture;
Fonte: Autoria própria (2025).


128
Listagem 36 – Parte 1 do arquivo activation_unit_8bit_v2.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
5
entity activation_unit_8bit_v2 is
6
port(clk: in std_logic;
7
input: in
signed (31 downto 0);
8
output: out signed (7 downto 0));
9
end entity;
10
11
architecture rtl of activation_unit_8bit_v2 is
12
13
component activation_lut_8bit_v2
14
PORT
15
(
16
address
: IN STD_LOGIC_VECTOR (9 DOWNTO 0);
17
clock
: IN STD_LOGIC
:= ’1’;
18
q
: OUT STD_LOGIC_VECTOR (7 DOWNTO 0)
19
);
20
end component;
21
22
signal addition, clamped: signed (31 downto 0) := (others =>
’0’);
23
signal address: std_logic_vector(9 downto 0);
24
signal o: std_logic_vector(7 downto 0);
25
constant Z3: signed(31 downto 0) := x"0000009C";
26
27
constant max_value: signed(31 downto 0) :=
"00000000000000000000000111111111";
28
constant min_value: signed(31 downto 0) :=
"11111111111111111111111000000000";
29
begin
30
31
-- adicionar o z3
32
process(clk)
33
begin
34
if rising_edge(clk) then
35
addition <= input + Z3;
36
end if;
37
end process;
38
39
-- Realizar clamping
40
process(clk)
Fonte: Autoria própria (2025).


129
Listagem 37 – Parte 2 do arquivo activation_unit_8bit_v2.vhd
1
variable multMem: signed(31 downto 0) ;
2
begin
3
if rising_edge(clk) then
4
multMem := addition;
5
if multMem > max_value then
6
multMem := max_value;
7
elsif multMem < min_value then
8
multMem := min_value;
9
end if;
10
clamped <= multMem;
11
end if;
12
end process;
13
14
address <= std_logic_vector(clamped(9 downto 0));
15
16
ROM : activation_lut_8bit_v2 port map(clock => clk,
17
address => address,
18
q => o);
19
20
21
output <= signed(o);
22
23
end architecture;
Fonte: Autoria própria (2025).


130
Listagem 38 – Parte 1 do arquivo converter_v3_ring.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
5
entity converter_v3_ring is
6
port(clk: in std_logic;
7
convert: in signed (31 downto 0);
8
offset: in signed (31 downto 0);
9
multiplier: in signed(31 downto 0);
10
shiftamount: in std_logic_vector (4 downto 0);
11
rd_en: in std_logic;
12
shift: in std_logic;
13
output: out signed(31 downto 0));
14
end entity;
15
16
-- Realiza (X - Z) * S * 2^-M
17
18
architecture rtl of converter_v3_ring is
19
20
component arith_shifter_barrel_v4 is
21
port (
22
clk
: in
std_logic;
23
Input
: in
signed(31 downto 0);
24
ShiftAmount
: in
std_logic_vector(4 downto 0);
25
Round
: out std_logic;
26
Output
: out signed(31 downto 0)
27
);
28
end component;
29
30
signal input_reg : signed (31 downto 0) := (others=>’0’);
31
signal offset_op : signed (32 downto 0) := (others=>’0’);
32
signal offset_op_2: signed(32 downto 0) := (others=>’0’);
33
signal multiplier_reg_logic: std_logic_vector(31 downto 0) :=
(others=>’0’);
34
signal mult_op, mult_op2, mult_op3, mult_op4 : signed(33
downto 0) := (others=>’0’);
35
signal mult_op_result : signed(31 downto 0) := (others=>’0’);
36
signal shift_op: signed(31 downto 0) := (others=>’0’);
37
38
signal mult_intermediate: signed(64 downto 0) := (others
=>’0’);
39
signal mult_intermediate_logic: std_logic_vector(64 downto 0)
:= (others=>’0’);
40
Fonte: Autoria própria (2025).


131
Listagem 39 – Parte 2 do arquivo converter_v3_ring.vhd
1
signal mul_reg_pipe : signed (31 downto 0) := (others=>’0’);
2
3
constant max_value: signed(33 downto 0) :=
"0001111111111111111111111111111111";
4
constant min_value: signed(33 downto 0) :=
"1110000000000000000000000000000000";
5
6
signal Round: std_logic;
7
type t_data is array (3 downto 0) of signed (31 downto 0);
8
type t_data_shift is array (3 downto 0) of std_logic_vector
(4 downto 0);
9
signal multiplier_array, offset_array : t_data := (others =>
(others => ’0’));
10
signal shiftamount_array : t_data_shift := (others => (others
=> ’0’));
11
signal shiftamount_reg : std_logic_vector (4 downto 0) := (
others=>’0’);
12
signal offset_reg, multiplier_reg : signed (31 downto 0) := (
others=>’0’);
13
begin
14
-- registrar as entradas
15
process(clk)
16
variable shift_reg : std_logic := ’0’;
17
18
variable delay_mult_1, delay_mult_2: signed (31 downto 0)
:= (others=>’0’);
19
variable delay_shiftammount_1, delay_shiftammount_2,
delay_shiftammount_3, delay_shiftammount_4 :
std_logic_vector (4 downto 0) := (others=>’0’);
20
variable delay_shiftammount_5, delay_shiftammount_6 :
std_logic_vector (4 downto 0) := (others=>’0’);
21
begin
22
if rising_edge(clk) then
23
input_reg <= convert;
24
25
shiftamount_reg <= delay_shiftammount_6;
26
delay_shiftammount_6 := delay_shiftammount_5;
27
delay_shiftammount_5 := delay_shiftammount_4;
28
delay_shiftammount_4 := delay_shiftammount_3;
29
delay_shiftammount_3 := delay_shiftammount_2;
30
delay_shiftammount_2 := delay_shiftammount_1;
31
32
multiplier_reg <= delay_mult_2;
33
delay_mult_2 := delay_mult_1;
34
if rd_en = ’1’ then
35
shiftamount_array(3) <= shiftamount;
Fonte: Autoria própria (2025).


132
Listagem 40 – Parte 3 do arquivo converter_v3_ring.vhd
1
offset_array(3) <= offset;
2
multiplier_array(3) <= multiplier;
3
l_data: for i in 0 to 2 loop
4
shiftamount_array(i) <= shiftamount_array(i+1);
5
offset_array(i) <= offset_array(i+1);
6
multiplier_array(i) <= multiplier_array(i+1);
7
end loop l_data;
8
elsif shift_reg = ’1’ then
9
l_shift: for i in 0 to 3 loop
10
shiftamount_array(i) <= shiftamount_array((i+1) mod
4);
11
offset_array(i) <= offset_array((i+1) mod 4);
12
multiplier_array(i) <= multiplier_array((i+1) mod 4);
13
end loop l_shift;
14
15
offset_reg <= offset_array(0);
16
delay_mult_1 := multiplier_array(0);
17
delay_shiftammount_1 := shiftamount_array(0);
18
end if;
19
20
shift_reg := shift;
21
22
end if;
23
end process;
24
25
26
-- operacao
27
process(clk)
28
begin
29
if rising_edge(clk) then
30
offset_op <= resize(input_reg, 33) + resize(offset_reg,
33);
-- registrador da LUT/LAB
31
offset_op_2 <= offset_op;
32
end if;
33
end process;
34
35
mult_intermediate <= offset_op_2 * multiplier_reg;
36
37
process(clk)
38
variable multMem: signed(33 downto 0);
39
begin
40
if rising_edge(clk) then
Fonte: Autoria própria (2025).


133
Listagem 41 – Parte 4 do arquivo converter_v3_ring.vhd
1
--multMem := mult_intermediate(64 downto 31);
2
multMem := mult_op3;
3
if multMem > max_value then
4
multMem := max_value;
5
elsif multMem < min_value then
6
multMem := min_value;
7
end if;
8
9
mult_op <= mult_intermediate(64 downto 31);
10
mult_op2 <= mult_op;
11
mult_op3 <= mult_op2;
12
mult_op_result <= multMem(31 downto 0);
13
end if;
14
end process;
15
16
17
shifter : arith_shifter_barrel_v4 port map(clk => clk,
18
Input => mult_op_result,
19
ShiftAmount => shiftamount_reg,
20
Round => Round,
21
output => shift_op);
22
23
-- output <= shift_op;
24
-- Processo de arredondar
25
process(clk)
26
variable round_number: signed(31 downto 0) := (others =>
’0’);
27
begin
28
if rising_edge(clk) then
29
round_number := shift_op;
30
if Round = ’1’ then
31
round_number := round_number + 1;
32
end if;
33
output <= round_number;
34
end if;
35
end process;
36
37
end architecture;
Fonte: Autoria própria (2025).


134
Listagem 42 – Parte 1 do arquivo arith_shifter_barrel_v4.vhd
1
library IEEE;
2
use
IEEE.STD_LOGIC_1164.all;
3
use
IEEE.NUMERIC_STD.all;
4
5
6
entity arith_shifter_barrel_v4 is
7
port (
8
clk
: in
std_logic;
9
Input
: in
signed(31 downto 0);
10
ShiftAmount
: in
std_logic_vector(4 downto 0);
11
Round
: out std_logic;
12
Output
: out signed(31 downto 0)
13
);
14
end entity;
15
16
17
architecture rtl of arith_shifter_barrel_v4 is
18
constant STAGES
: positive
:= 5;
19
20
subtype T_INTERMEDIATE_RESULT is std_logic_vector(31 downto
0);
21
type
T_INTERMEDIATE_VECTOR is array (natural range <>) of
T_INTERMEDIATE_RESULT;
22
23
signal IntermediateResults
: T_INTERMEDIATE_VECTOR(2 downto
0);
24
signal IntermediateResults_pipeline : T_INTERMEDIATE_VECTOR(3
downto 0);
25
signal input_reg, output_reg, pipeline_reg : std_logic_vector
(31 downto 0) := (others=>’0’);
26
signal ShiftAmount_reg, ShiftAmount_reg_pipe :
std_logic_vector(4 downto 0) := (others=>’0’);
27
signal RorL: std_logic;
28
signal discarded_bit, discarded_bit_pipe :std_logic := ’0’;
29
signal index: integer range 0 to 31;
30
begin
31
32
process(clk)
33
begin
34
if rising_edge(clk) then
35
input_reg <= std_logic_vector(Input);
36
output_reg <= IntermediateResults_pipeline(3);
37
ShiftAmount_reg <= ShiftAmount;
38
RorL <= ’0’;
39
end if;
40
end process;
Fonte: Autoria própria (2025).


135
Listagem 43 – Parte 2 do arquivo arith_shifter_barrel_v4.vhd
1
2
IntermediateResults(0)
<= input_reg;
3
Output
<= signed(output_reg);
4
5
6
-- Adicionar pipeline para aumentar a frequencia
7
genStage : for i in 0 to 1 generate
8
process(IntermediateResults(i), ShiftAmount_reg)
9
begin
10
if ShiftAmount_reg(i) = ’0’ then
11
IntermediateResults(i + 1) <= IntermediateResults(i) ;
12
else
13
if RorL = ’0’ then -- 0 = Right, 1 = Left
14
IntermediateResults(i + 1) <= ((2**i - 1) downto 0 =>
IntermediateResults(i)(31)) & IntermediateResults(i)(31
downto 2**i);
15
else
16
IntermediateResults(i + 1) <= IntermediateResults(i)
((32 - 2**i - 1) downto 0) & ((2**i - 1) downto 0 => ’0’);
17
end if;
18
end if;
19
end process;
20
end generate;
21
22
process(clk)
23
variable mask: std_logic_vector(30 downto 0) := (others =>
’0’);
24
variable ANDResult: std_logic_vector(30 downto 0) := (
others => ’0’);
25
variable ORTest :std_logic := ’0’;
26
begin
27
if rising_edge(clk) then
28
29
ORTest := ’0’;
30
for i in 0 to 30 loop
31
ORTest := ORTest or ANDResult(i);
32
end loop;
33
34
pipeline_reg <= IntermediateResults(2);
35
ShiftAmount_reg_pipe <= ShiftAmount_reg;
36
37
discarded_bit <= input_reg(to_integer(unsigned(
ShiftAmount_reg) - 1));
38
Round <= discarded_bit and (ORTest or
IntermediateResults_pipeline(3)(0));
39
40
for i in 0 to 30 loop
Fonte: Autoria própria (2025).


136
Listagem 44 – Parte 3 do arquivo arith_shifter_barrel_v4.vhd
1
if i < to_integer(unsigned(ShiftAmount_reg)-1) then
2
mask(i) := ’1’;
3
else
4
mask(i) := ’0’;
5
end if;
6
end loop;
7
8
ANDResult := mask and input_reg(30 downto 0);
9
10
end if;
11
end process;
12
13
IntermediateResults_pipeline(0) <= pipeline_reg;
14
15
genStage_2 : for i in 2 to 4 generate
16
process(IntermediateResults_pipeline(i-2),
ShiftAmount_reg_pipe)
17
begin
18
if ShiftAmount_reg_pipe(i) = ’0’ then
19
IntermediateResults_pipeline(i-1) <=
IntermediateResults_pipeline(i-2) ;
20
else
21
if RorL = ’0’ then -- 0 = Right, 1 = Left
22
IntermediateResults_pipeline(i-1) <= ((2**i - 1)
downto 0 => IntermediateResults_pipeline(i-2)(31)) &
IntermediateResults_pipeline(i-2)(31 downto 2**i);
23
else
24
IntermediateResults_pipeline(i-1) <=
IntermediateResults_pipeline(i-2)((32 - 2**(i-2) - 1) downto
0) & ((2**(i-2) - 1) downto 0 => ’0’);
25
end if;
26
end if;
27
end process;
28
end generate;
29
end;
Fonte: Autoria própria (2025).


137
Listagem 45 – Parte 1 do arquivo mac_unit.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
5
entity mac_unit is
6
port(clk: in std_logic;
7
channels: in std_logic_vector (63 downto 0);
8
weights: in std_logic_vector (63 downto 0);
9
output: out std_logic_vector(18 downto 0));
10
end entity;
11
12
architecture rtl of mac_unit is
13
14
15
type vector_stage_0 is array (natural range <>) of signed(7
downto 0);
16
type vector_stage_1 is array (natural range <>) of signed(15
downto 0);
17
type vector_stage_2 is array (natural range <>) of signed(16
downto 0);
18
type vector_stage_3 is array (natural range <>) of signed(17
downto 0);
19
20
signal channels_reg, weights_reg: std_logic_vector (63 downto
0) := (others => ’0’);
21
signal stage_0 : vector_stage_0(15 downto 0) := (others => (
others => ’0’));
22
signal stage_1 : vector_stage_1(7 downto 0) := (others => (
others => ’0’));
23
signal stage_2 : vector_stage_2(3 downto 0) := (others => (
others => ’0’));
24
signal stage_3 : vector_stage_3(1 downto 0) := (others => (
others => ’0’));
25
signal stage_4 : signed(18 downto 0) := (others => ’0’);
26
27
begin
28
29
-- registrar as entradas
30
process(clk)
31
begin
32
if rising_edge(clk) then
33
channels_reg <= channels;
34
weights_reg <= weights;
35
end if;
36
end process;
37
38
-- reajustar os sinais para ser mais facíl
39
generate_assigment: for i in 0 to 7 generate
40
stage_0(i)
<= signed(channels_reg((i*8)+7 downto i*8));
Fonte: Autoria própria (2025).


138
Listagem 46 – Parte 2 do arquivo mac_unit.vhd
1
stage_0(i+8) <= signed(weights_reg((i*8)+7 downto i*8));
2
end generate generate_assigment;
3
4
5
generate_multiplication: for i in 0 to 7 generate
6
process(clk)
7
begin
8
if rising_edge(clk) then
9
stage_1(i)
<= stage_0(i) * stage_0(i+8);
10
end if;
11
end process;
12
end generate generate_multiplication;
13
14
generate_add_1: for i in 0 to 3 generate
15
process(clk)
16
begin
17
if rising_edge(clk) then
18
stage_2(i)
<= resize(stage_1(i),17) + resize(stage_1(i
+4),17);
19
end if;
20
end process;
21
end generate generate_add_1;
22
23
generate_add_2: for i in 0 to 1 generate
24
process(clk)
25
begin
26
if rising_edge(clk) then
27
stage_3(i)
<= resize(stage_2(i),18) + resize(stage_2(i
+2),18);
28
end if;
29
end process;
30
end generate generate_add_2;
31
32
process(clk)
33
begin
34
if rising_edge(clk) then
35
stage_4
<= resize(stage_3(0),19) + resize(stage_3(1)
,19);
36
end if;
37
end process;
38
39
output <= std_logic_vector(stage_4);
40
end architecture;
Fonte: Autoria própria (2025).


139
Listagem 47 – Parte 1 do arquivo relu_unit_v2.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
5
entity relu_unit_v2 is
6
port(clk: in std_logic;
7
input: in signed(31 downto 0);
8
output: out signed (7 downto 0));
9
end entity;
10
11
architecture rtl of relu_unit_v2 is
12
13
signal relu_reg, input_reg: signed(31 downto 0) := (others =>
’0’);
14
signal relu_zp_reg: signed(7 downto 0) := (others => ’0’);
15
16
-- ZP fixo para -128
17
constant fixed_zp: signed(7 downto 0) := x"80";
18
19
constant min_value: signed(31 downto 0) := x"00000000";
20
constant max_value: signed(31 downto 0) := x"000000FF";
21
22
begin
23
24
-- registrar as entradas
25
process(clk)
26
begin
27
if rising_edge(clk) then
28
input_reg <= input;
29
end if;
30
end process;
31
32
-- max(0, min(255, x))
33
process(clk)
34
variable multMem: signed(31 downto 0);
35
begin
36
if rising_edge(clk) then
37
multMem := input_reg;
38
if multMem > max_value then
39
multMem := max_value;
40
elsif multMem < min_value then
Fonte: Autoria própria (2025).


140
Listagem 48 – Parte 2 do arquivo relu_unit_v2.vhd
1
multMem := min_value;
2
end if;
3
relu_reg <= multMem;
4
end if;
5
end process;
6
7
-- relu_reg + zp(i.e. -128)
8
process(clk)
9
begin
10
if rising_edge(clk) then
11
relu_zp_reg <= relu_reg(7 downto 0) + fixed_zp;
12
end if;
13
end process;
14
15
16
output <= relu_zp_reg;
17
18
end architecture;
Fonte: Autoria própria (2025).


141
Listagem 49 – Parte 1 do arquivo pool_unit.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
5
entity pool_unit is
6
port(clk: in std_logic;
7
rst: in std_logic;
8
en: in std_logic;
9
channels: in std_logic_vector (63 downto 0);
10
output: out std_logic_vector (63 downto 0));
11
end entity;
12
13
architecture rtl of pool_unit is
14
15
16
type vector is array (natural range <>) of signed(7 downto 0)
;
17
18
signal incoming_value: vector(7 downto 0);
19
signal vector_reg : vector(7 downto 0) := (others => (x"80"))
;
20
signal intermediary : std_logic_vector (63 downto 0);
21
22
begin
23
24
-- não registrar as entradas
25
-- reajustar os sinais para ser mais facíl
26
generate_assigment: for i in 0 to 7 generate
27
incoming_value(i)
<= signed(channels((i*8)+7 downto i*8))
;
28
intermediary((i*8)+7 downto i*8) <= std_logic_vector(
vector_reg(i));
29
end generate generate_assigment;
30
31
32
generate_max: for i in 0 to 7 generate
33
process(clk)
34
variable var_vector_reg : signed(7 downto 0) := x"80";
35
begin
36
if rising_edge(clk) then
37
if rst = ’1’ then
38
var_vector_reg := x"80"; -- Setar para valor mínimo
-> -128
39
end if;
40
Fonte: Autoria própria (2025).


142
Listagem 50 – Parte 2 do arquivo pool_unit.vhd
1
if incoming_value(i) > var_vector_reg then
2
var_vector_reg := incoming_value(i);
3
end if;
4
5
vector_reg(i) <= var_vector_reg;
6
7
end if;
8
end process;
9
end generate generate_max;
10
11
12
output <= intermediary when en = ’1’ else
13
(others => ’Z’);
14
15
end architecture;
Fonte: Autoria própria (2025).


143
Listagem 51 – Parte 1 do arquivo FSM_NOP_Controlador.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
5
entity FSM_NOP_Controlador is
6
port(clk: in std_logic;
7
start: in std_logic;
8
running: out std_logic;
9
poolOrConv: out std_logic;
10
activation: out std_logic;
11
OutputWren : out std_logic;
12
selectModule: out std_logic_vector (7 downto 0);
13
load_shift: out std_logic;
14
accumulate: out std_logic;
15
newPool: out std_logic;
16
DataAddress: out std_logic_vector(12 downto 0);
17
ParameterAddress: out std_logic_vector(7 downto 0);
18
WeightAddress: out std_logic_vector(9 downto 0);
19
OutputAddress: out std_logic_vector(12 downto 0)
20
);
21
end entity;
22
23
architecture rtl of FSM_NOP_Controlador is
24
component FSM_NOP_Main is
25
port(clk: in std_logic;
26
start: in std_logic;
27
donePar: in std_logic;
28
doneMath: in std_logic;
29
running: out std_logic;
30
parameterStart: out std_logic;
31
convStart: out std_logic;
32
poolOrConv: out std_logic;
33
activation: out std_logic;
34
fcOrConv: out std_logic;
35
lineSize: out std_logic_vector (4 downto 0);
36
columnSize: out std_logic_vector (4 downto 0);
37
channelSize: out std_logic_vector (1 downto 0);
38
kernelSize: out std_logic_vector (6 downto 0);
39
filterQtd: out std_logic_vector (1 downto 0);
40
windowHeight: out std_logic_vector (2 downto 0);
Fonte: Autoria própria (2025).


144
Listagem 52 – Parte 2 do arquivo FSM_NOP_Controlador.vhd
1
windowWidth: out std_logic_vector (2 downto 0);
2
strideHeight: out std_logic_vector (1 downto 0);
3
strideWidth: out std_logic_vector (1 downto 0);
4
pBaseAdress: out std_logic_vector (7 downto 0);
5
dBaseAdress: out std_logic_vector (12 downto 0);
6
wBaseAdress: out std_logic_vector (9 downto 0);
7
oBaseAdress: out std_logic_vector (12 downto 0);
8
ChannelColumnSize: out std_logic_vector (6 downto 0);
9
OutputLineSize: out std_logic_vector (4 downto 0);
10
OutputColumnSize: out std_logic_vector (4 downto 0);
11
OutputChannelColumnSize: out std_logic_vector (6 downto
0)
12
);
13
end component;
14
15
component agu_v2 is
16
port(clk: in std_logic;
17
baseAdress: in std_logic_vector (12 downto 0);
18
currentLine: in std_logic_vector(4 downto 0);
19
columnSize: in std_logic_vector (6 downto 0);
20
currentColumn: in std_logic_vector (4 downto 0);
21
channelSize: in std_logic_vector (1 downto 0);
22
currentChannel: in std_logic_vector (1 downto 0);
23
address: out std_logic_vector(12 downto 0));
24
end component;
25
26
component agu_weights is
27
port(clk: in std_logic;
28
baseAdress: in std_logic_vector (9 downto 0);
29
currentFilter: in std_logic_vector(1 downto 0);
30
kernelSize: in std_logic_vector(6 downto 0);
31
positionKernel: in std_logic_vector(6 downto 0);
32
address: out std_logic_vector(9 downto 0));
33
end component;
34
35
36
component FSM_Input is
37
port(clk: in std_logic;
38
rst: in std_logic;
39
lineSize: in std_logic_vector (4 downto 0);
40
columnSize: in std_logic_vector (4 downto 0);
Fonte: Autoria própria (2025).


145
Listagem 53 – Parte 3 do arquivo FSM_NOP_Controlador.vhd
1
channelSize: in std_logic_vector (1 downto 0);
2
kernelSize: in std_logic_vector (6 downto 0);
3
filterQtd: in std_logic_vector (1 downto 0);
4
windowHeight: in std_logic_vector (2 downto 0);
5
windowWidth: in std_logic_vector (2 downto 0);
6
strideHeight: in std_logic_vector (1 downto 0);
7
strideWidth: in std_logic_vector (1 downto 0);
8
cLine: out std_logic_vector(4 downto 0);
9
cCol: out std_logic_vector(4 downto 0);
10
cChan: out std_logic_vector(1 downto 0);
11
cFilter: out std_logic_vector(1 downto 0);
12
cKernel: out std_logic_vector(6 downto 0);
13
done: out std_logic;
14
newPool: out std_logic;
15
newFilter: out std_logic);
16
end component;
17
18
component FSM_NOP_Input is
19
port(clk: in std_logic;
20
start: in std_logic;
21
finished: in std_logic;
22
rst: out std_logic);
23
end component;
24
25
component FSM_NOP_Control is
26
port(clk: in std_logic;
27
kernelSize: in std_logic_vector (6 downto 0);
28
start: in std_logic;
29
finished: in std_logic;
30
poolOrConv: in std_logic;
31
fcOrConv: in std_logic;
32
NewFilter: out std_logic;
33
load_shift: out std_logic;
34
accumulate: out std_logic;
35
forceStep: out std_logic;
36
done: out std_logic);
37
end component;
38
39
component FSM_NOP_Parameters is
40
port(clk: in std_logic;
Fonte: Autoria própria (2025).


146
Listagem 54 – Parte 4 do arquivo FSM_NOP_Controlador.vhd
1
baseAdress: in std_logic_vector (7 downto 0);
2
filterQtd: in std_logic_vector (1 downto 0);
3
start: in std_logic;
4
parametersAdress: out std_logic_vector (7 downto 0);
5
selectModule: out std_logic_vector (7 downto 0);
6
wr_en: out std_logic;
7
done: out std_logic);
8
end component;
9
10
component FSM_NOP_Output is
11
port(clk: in std_logic;
12
activation: in std_logic;
13
start: in std_logic;
14
newFilter: in std_logic;
15
finished: in std_logic;
16
poolOrConv: in std_logic;
17
forceStep: in std_logic;
18
rst: out std_logic;
19
step: out std_logic;
20
wr_en: out std_logic;
21
done: out std_logic);
22
end component;
23
24
component FSM_Output is
25
port(clk: in std_logic;
26
rst: in std_logic;
27
step: in std_logic;
28
lineSize: in std_logic_vector (4 downto 0);
29
columnSize: in std_logic_vector (4 downto 0);
30
channelSize: in std_logic_vector (1 downto 0);
31
cLine: out std_logic_vector(4 downto 0);
32
cCol: out std_logic_vector(4 downto 0);
33
cChan: out std_logic_vector(1 downto 0));
34
end component;
35
36
37
-- FSM_NOP_Main
38
signal donePar: std_logic;
39
signal doneMath: std_logic;
40
signal parameterStart: std_logic;
Fonte: Autoria própria (2025).


147
Listagem 55 – Parte 5 do arquivo FSM_NOP_Controlador.vhd
1
signal convStart: std_logic;
2
signal sPoolOrConv: std_logic;
3
signal sActivation: std_logic;
4
signal fcOrConv: std_logic;
5
6
signal lineSize: std_logic_vector (4 downto 0);
7
signal columnSize: std_logic_vector (4 downto 0);
8
signal channelSize: std_logic_vector (1 downto 0);
9
signal kernelSize: std_logic_vector (6 downto 0);
10
signal filterQtd: std_logic_vector (1 downto 0);
11
signal windowHeight: std_logic_vector (2 downto 0);
12
signal windowWidth: std_logic_vector (2 downto 0);
13
signal strideHeight: std_logic_vector (1 downto 0);
14
signal strideWidth: std_logic_vector (1 downto 0);
15
signal pBaseAdress: std_logic_vector (7 downto 0);
16
signal dBaseAdress: std_logic_vector (12 downto 0)
17
signal wBaseAdress: std_logic_vector (9 downto 0);
18
signal oBaseAdress: std_logic_vector (12 downto 0)
19
signal ChannelColumnSize: std_logic_vector (6 downto 0);
20
signal OutputLineSize: std_logic_vector (4 downto 0);
21
signal OutputColumnSize: std_logic_vector (4 downto 0);
22
signal OutputChannelColumnSize: std_logic_vector (6 downto 0)
;
23
24
-- FSM_Input
25
signal InputCurrentLine: std_logic_vector(4 downto 0);
26
signal InputCurrentCol: std_logic_vector(4 downto 0);
27
signal InputCurrentChan: std_logic_vector(1 downto 0);
28
signal InputCurrentFilter: std_logic_vector(1 downto 0);
29
signal InputCurrentKernel: std_logic_vector(6 downto 0);
30
signal InputReset: std_logic;
31
signal InputDone: std_logic;
32
signal InputNewPool: std_logic;
33
signal InputNewFilter: std_logic;
34
35
-- FSM_NOP_Input
36
37
-- FSM_NOP_Control
38
signal ControlDone: std_logic;
39
signal ControlNewFilter : std_logic;
40
signal ControlLoadShift : std_logic;
Fonte: Autoria própria (2025).


148
Listagem 56 – Parte 6 do arquivo FSM_NOP_Controlador.vhd
1
signal ControlForceStep: std_logic;
2
3
-- FSM_NOP_Parameters
4
signal wr_en : std_logic;
5
6
-- FSM_NOP_Output
7
signal OutputRST : std_logic;
8
signal OutputStep : std_logic;
9
10
-- FSM_Output
11
signal OutputCurrentLine: std_logic_vector(4 downto 0);
12
signal OutputCurrentCol: std_logic_vector(4 downto 0);
13
signal OutputCurrentChan: std_logic_vector(1 downto 0);
14
begin
15
16
poolOrConv <= sPoolOrConv;
17
activation <= sActivation;
18
newPool <= ControlNewFilter or donePar;
19
load_shift <= ControlLoadShift or convStart;
20
21
NOP_Main : FSM_NOP_Main port map(clk => clk,
22
start => start,
23
donePar => donePar,
24
doneMath => doneMath,
25
running => running,
26
parameterStart => parameterStart,
27
convStart => convStart,
28
PoolOrConv => sPoolOrConv,
29
Activation => sActivation,
30
fcOrConv => fcOrConv,
31
lineSize => lineSize,
32
columnSize => columnSize,
33
channelSize => channelSize,
34
kernelSize => kernelSize,
35
filterQtd => filterQtd,
36
windowHeight => windowHeight,
37
windowWidth => windowWidth,
38
strideHeight => strideHeight,
39
strideWidth => strideWidth,
40
pBaseAdress => pBaseAdress,
Fonte: Autoria própria (2025).


149
Listagem 57 – Parte 7 do arquivo FSM_NOP_Controlador.vhd
1
dBaseAdress => dBaseAdress,
2
wBaseAdress => wBaseAdress,
3
oBaseAdress => oBaseAdress,
4
ChannelColumnSize => ChannelColumnSize,
5
OutputLineSize => OutputLineSize,
6
OutputColumnSize => OutputColumnSize,
7
OutputChannelColumnSize =>
OutputChannelColumnSize);
8
9
Machine_Input : FSM_Input port map(clk => clk,
10
rst => InputReset,
11
lineSize => lineSize,
12
columnSize => columnSize,
13
channelSize => channelSize,
14
kernelSize => kernelSize,
15
filterQtd => filterQtd,
16
windowHeight => windowHeight,
17
windowWidth => windowWidth,
18
strideHeight => strideHeight,
19
strideWidth => strideWidth,
20
cLine => InputCurrentLine,
21
cCol => InputCurrentCol,
22
cChan => InputCurrentChan,
23
cFilter => InputCurrentFilter,
24
cKernel => InputCurrentKernel,
25
done => InputDone,
26
newPool => InputNewPool,
27
newFilter => InputNewFilter);
28
29
NOP_Input : FSM_NOP_Input port map (clk => clk,
30
start => convStart,
31
finished => InputDone,
32
rst => InputReset);
33
34
Input_AGU : agu_v2 port map(clk => clk,
35
baseAdress => dBaseAdress,
36
currentLine => InputCurrentLine,
37
columnSize => ChannelColumnSize,
38
currentColumn => InputCurrentCol,
39
channelSize => channelSize,
40
currentChannel => InputCurrentChan,
Fonte: Autoria própria (2025).


150
Listagem 58 – Parte 8 do arquivo FSM_NOP_Controlador.vhd
1
address => DataAddress);
2
3
4
Weight_AGU :
agu_weights port map(clk => clk,
5
baseAdress => wBaseAdress,
6
currentFilter => InputCurrentFilter,
7
kernelSize => kernelSize,
8
positionKernel => InputCurrentKernel,
9
address => WeightAddress);
10
11
12
NOP_Control : FSM_NOP_Control port map(clk => clk,
13
kernelSize => kernelSize,
14
start => convStart,
15
finished => InputDone,
16
poolOrConv => sPoolOrConv,
17
fcOrConv => fcOrConv,
18
NewFilter => ControlNewFilter,
19
load_shift => ControlLoadShift,
20
accumulate => accumulate,
21
forceStep => ControlForceStep,
22
done => ControlDone);
23
24
NOP_Parameters : FSM_NOP_Parameters port map(clk => clk,
25
baseAdress => pBaseAdress,
26
filterQtd => filterQtd,
27
start => parameterStart,
28
parametersAdress =>
ParameterAddress,
29
selectModule => selectModule,
30
wr_en => wr_en, -- Goes nowhere
for now
31
done => donePar);
32
33
34
NOP_Output : FSM_NOP_Output port map(clk => clk,
35
activation => sActivation,
36
start => convStart,
37
newFilter => ControlNewFilter,
38
finished => ControlDone,
39
poolOrConv => sPoolOrConv,
40
forceStep => ControlForceStep,
Fonte: Autoria própria (2025).


151
Listagem 59 – Parte 9 do arquivo FSM_NOP_Controlador.vhd
1
rst => OutputRST,
2
step => OutputStep,
3
wr_en => OutputWren,
4
done => doneMath);
5
6
7
Machine_Output : FSM_Output port map(clk => clk,
8
rst => OutputRST,
9
step => OutputStep,
10
lineSize => OutputLineSize,
11
columnSize => OutputColumnSize,
12
channelSize => filterQtd,
13
cLine => OutputCurrentLine,
14
cCol => OutputCurrentCol,
15
cChan => OutputCurrentChan);
16
17
Output_AGU : agu_v2 port map(clk => clk,
18
baseAdress => oBaseAdress,
19
currentLine => OutputCurrentLine,
20
columnSize => OutputChannelColumnSize,
21
currentColumn => OutputCurrentCol,
22
channelSize => filterQtd,
23
currentChannel => OutputCurrentChan,
24
address => OutputAddress);
25
end architecture;
Fonte: Autoria própria (2025).


152
Listagem 60 – Parte 1 do arquivo agu_v2.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
5
-- AGU -> Address Generation Unit
6
entity agu_v2 is
7
port(clk: in std_logic;
8
baseAdress: in std_logic_vector (12 downto 0);
9
currentLine: in std_logic_vector(4 downto 0);
10
columnSize: in std_logic_vector (6 downto 0);
11
currentColumn: in std_logic_vector (4 downto 0);
12
--channelSize: in std_logic_vector (1 downto 0);
13
channelSize: in std_logic_vector (1 downto 0);
14
currentChannel: in std_logic_vector (1 downto 0);
15
address: out std_logic_vector(12 downto 0));
16
end entity;
17
18
-- Realizar a conta
19
-- baseAdress + currentLine * columnSize + currentColumn *
channelSize + currentChannel
20
-- ColumnSize = Numero de Colunas * numero de Canais -> Pre
calculado
21
22
architecture rtl of agu_v2 is
23
24
25
signal base_reg : unsigned (12 downto 0) := (others => ’0’);
26
signal cl_reg : unsigned (4 downto 0) := (others => ’0’);
-- currentline
27
signal cms_reg: unsigned (6 downto 0) := (others => ’0’);
-- columnsize
28
signal cc_reg: unsigned (4 downto 0) := (others => ’0’);
-- currentcolumn
29
signal chs_reg: unsigned (2 downto 0) := (others => ’0’);
-- channelSize
30
signal cch_reg, cch_reg_1, cch_reg_2: unsigned (1 downto 0)
:= (others => ’0’);
-- currentchannel
31
32
signal mult_line: unsigned(11 downto 0) := (others => ’0’);
33
signal mult_column: unsigned(7 downto 0) := (others => ’0’);
34
35
signal add_lc: unsigned(11 downto 0) := (others => ’0’);
36
37
begin
38
39
-- registrar as entradas
40
process(clk)
Fonte: Autoria própria (2025).


153
Listagem 61 – Parte 2 do arquivo agu_v2.vhd
1
begin
2
if rising_edge(clk) then
3
base_reg <= unsigned(baseAdress);
4
cl_reg <= unsigned(currentLine);
5
cms_reg <= unsigned(columnSize);
6
cc_reg <= unsigned(currentColumn);
7
chs_reg <= resize(unsigned(channelSize),3) + 1;
8
cch_reg <= unsigned(currentChannel);
9
end if;
10
end process;
11
12
13
-- realizar calculo
14
process(clk)
15
variable address_reg: unsigned (12 downto 0);
16
begin
17
if rising_edge(clk) then
18
address_reg := base_reg + add_lc + cch_reg_2;
19
mult_line <= cl_reg * cms_reg;
20
mult_column <= cc_reg * chs_reg;
21
22
add_lc <= mult_line + mult_column;
23
24
address <= std_logic_vector(address_reg);
25
26
-- Registradores pipelines
27
cch_reg_1 <= cch_reg;
--mult_line/mult_column
28
cch_reg_2 <= cch_reg_1;
--add_lc
29
end if;
30
end process;
31
32
end architecture;
Fonte: Autoria própria (2025).


154
Listagem 62 – Parte 1 do arquivo agu_weights.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
5
-- AGU -> Address Generation Unit
6
entity agu_weights is
7
port(clk: in std_logic;
8
baseAdress: in std_logic_vector (9 downto 0);
9
currentFilter: in std_logic_vector(1 downto 0);
10
kernelSize: in std_logic_vector(6 downto 0);
11
positionKernel: in std_logic_vector(6 downto 0);
12
address: out std_logic_vector(9 downto 0));
13
end entity;
14
15
-- Realizar a conta
16
-- baseAdress + currentFilter * kernelSize + positionKernel
17
18
architecture rtl of agu_weights is
19
20
21
signal base_reg : unsigned (9 downto 0) := (others => ’0’);
22
signal cf_reg : unsigned (1 downto 0) := (others => ’0’);
-- currentFilter
23
signal ks_reg: unsigned (6 downto 0) := (others => ’0’);
-- kernelSize
24
signal pk_reg, pk_reg_1: unsigned (6 downto 0) := (others =>
’0’);
-- positionKernel
25
signal address_reg: unsigned (9 downto 0) := (others => ’0’);
26
27
signal mult_add: unsigned (9 downto 0) := (others => ’0’);
28
29
begin
30
31
-- registrar as entradas
32
process(clk)
33
begin
34
if rising_edge(clk) then
35
base_reg <= unsigned(baseAdress);
36
cf_reg <= unsigned(currentFilter);
37
ks_reg <= unsigned(kernelSize)+1;
38
pk_reg <= unsigned(positionKernel);
39
end if;
40
end process;
Fonte: Autoria própria (2025).


155
Listagem 63 – Parte 2 do arquivo agu_weights.vhd
1
2
3
-- realizar calculo
4
process(clk)
5
begin
6
if rising_edge(clk) then
7
address_reg <= mult_add + pk_reg_1;
8
mult_add <= base_reg + cf_reg * ks_reg;
9
10
pk_reg_1 <= pk_reg;
11
12
address <= std_logic_vector(address_reg);
13
end if;
14
end process;
15
16
end architecture;
Fonte: Autoria própria (2025).


156
Listagem 64 – Parte 1 do arquivo FSM_Input.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
5
entity FSM_Input is
6
port(clk: in std_logic;
7
rst: in std_logic;
8
lineSize: in std_logic_vector (4 downto 0);
9
columnSize: in std_logic_vector (4 downto 0);
10
channelSize: in std_logic_vector (1 downto 0);
11
kernelSize: in std_logic_vector (6 downto 0);
12
filterQtd: in std_logic_vector (1 downto 0);
13
windowHeight: in std_logic_vector (2 downto 0);
14
windowWidth: in std_logic_vector (2 downto 0);
15
strideHeight: in std_logic_vector (1 downto 0);
16
strideWidth: in std_logic_vector (1 downto 0);
17
cLine: out std_logic_vector(4 downto 0);
18
cCol: out std_logic_vector(4 downto 0);
19
cChan: out std_logic_vector(1 downto 0);
20
cFilter: out std_logic_vector(1 downto 0);
21
cKernel: out std_logic_vector(6 downto 0);
22
done: out std_logic;
23
newPool: out std_logic;
24
newFilter: out std_logic);
25
end entity;
26
27
28
architecture rtl of FSM_Input is
29
30
signal currentLine, currentColumn: std_logic_vector(4 downto
0) := "00000";
31
signal currentChannel, currentFilter: std_logic_vector(1
downto 0) := "00";
32
signal currentKernel: std_logic_vector(6 downto 0) :=
"0000000";
33
34
signal size_channel: integer range 0 to 4 := 0;
35
signal size_column: integer range 0 to 32 := 0;
36
signal size_line: integer range 0 to 32 := 0;
37
38
signal size_filter: integer range 0 to 128 := 0;
39
signal qtd_filter: integer range 0 to 4 := 0;
40
Fonte: Autoria própria (2025).


157
Listagem 65 – Parte 2 do arquivo FSM_Input.vhd
1
signal size_x: integer range 0 to 8 := 0;
2
signal size_y: integer range 0 to 8 := 0;
3
4
signal stride_x: integer range 0 to 4 := 0;
5
signal stride_y: integer range 0 to 4 := 0;
6
7
signal kernel_size: integer range 0 to 128 := 0;
8
9
begin
10
11
-- registrar as entradas
12
process(clk)
13
begin
14
if rising_edge(clk) then
15
size_channel <= to_integer(unsigned(channelSize));
16
size_column <= to_integer(unsigned(columnSize));
17
size_line <= to_integer(unsigned(lineSize));
18
19
qtd_filter <= to_integer(unsigned(filterQtd));
20
21
size_x <= to_integer(unsigned(windowWidth));
22
size_y <= to_integer(unsigned(windowHeight));
23
--filterSize
24
25
stride_x <= to_integer(unsigned(strideHeight));
26
stride_y <= to_integer(unsigned(strideWidth));
27
28
kernel_size <= to_integer(unsigned(kernelSize));
29
end if;
30
end process;
31
32
33
process(clk)
34
variable channel_counter: integer range 0 to 4 := 0;
35
variable column_counter: integer range 0 to 32 := 0;
36
variable line_counter: integer range 0 to 32 := 0;
37
variable filter_qtd_counter: integer range 0 to 4 := 0;
38
39
variable w_x: integer range 0 to 7 := 0;
40
variable w_y: integer range 0 to 7 := 0;
Fonte: Autoria própria (2025).


158
Listagem 66 – Parte 3 do arquivo FSM_Input.vhd
1
2
variable current_x: integer range 0 to 32 := 0;
3
variable current_y: integer range 0 to 32 := 0;
4
5
variable finished_filter: std_logic := ’0’;
6
7
variable nFilter: std_logic := ’0’;
8
variable nPool: std_logic := ’0’;
9
variable finished: std_logic := ’0’;
10
11
variable current_kernel: integer range 0 to 128 := 0;
12
13
begin
14
if rising_edge(clk) then
15
nFilter := ’0’;
16
nPool := ’0’;
17
if rst = ’1’ then
18
channel_counter := 0;
19
column_counter := 0;
20
line_counter := 0;
21
filter_qtd_counter := 0;
22
w_x := 0;
23
w_y := 0;
24
current_x := 0;
25
current_y := 0;
26
finished := ’0’;
27
28
current_kernel := 0;
29
30
else
31
if w_x = size_x then
32
w_x := 0;
33
column_counter := current_x;
34
if w_y = size_y then
35
w_y := 0;
36
line_counter := current_y;
37
finished_filter := ’1’;
38
else
39
line_counter := line_counter + 1;
40
w_y := w_y + 1;
Fonte: Autoria própria (2025).


159
Listagem 67 – Parte 4 do arquivo FSM_Input.vhd
1
end if;
2
else
3
w_x := w_x + 1;
4
column_counter := column_counter + 1;
5
end if;
6
7
if current_kernel = kernel_size then
8
current_kernel := 0;
9
else
10
current_kernel := current_kernel + 1;
11
end if;
12
13
14
if finished_filter = ’1’ then
15
finished_filter := ’0’;
16
nPool := ’1’;
17
18
if filter_qtd_counter = qtd_filter and
channel_counter = size_channel then
19
filter_qtd_counter := 0;
20
channel_counter := 0;
21
if current_x = size_column then
22
current_x := 0;
23
if current_y = size_line then
24
current_y := 0;
25
finished := ’1’;
26
else
27
current_y := current_y + stride_y;
28
end if;
29
line_counter := current_y;
30
else
31
current_x := current_x + stride_x;
32
end if;
33
column_counter := current_x;
34
nFilter := ’1’;
35
elsif channel_counter = size_channel then
36
filter_qtd_counter := filter_qtd_counter + 1;
37
channel_counter := 0;
38
nFilter := ’1’;
39
else
40
channel_counter := channel_counter + 1;
Fonte: Autoria própria (2025).


160
Listagem 68 – Parte 5 do arquivo FSM_Input.vhd
1
end if;
2
3
end if;
4
end if;
5
6
currentChannel <= std_logic_vector(to_unsigned(
channel_counter, currentChannel’length));
7
currentColumn <= std_logic_vector(to_unsigned(
column_counter, currentColumn’length));
8
currentLine <= std_logic_vector(to_unsigned(line_counter,
currentLine’length));
9
currentFilter <= std_logic_vector(to_unsigned(
filter_qtd_counter, currentFilter’length));
10
11
currentKernel <= std_logic_vector(to_unsigned(
current_kernel, currentKernel’length));
12
13
done <= finished;
14
newFilter <= nFilter;
15
newPool <= nPool;
16
end if;
17
end process;
18
19
cLine <= currentLine;
20
cCol <= currentColumn;
21
cChan <= currentChannel;
22
cFilter <= currentFilter;
23
24
cKernel <= currentKernel;
25
end architecture;
Fonte: Autoria própria (2025).


161
Listagem 69 – Parte 1 do arquivo FSM_NOP_Input.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
USE work.data_type_pkg.all;
5
6
entity FSM_NOP_Input is
7
port(clk: in std_logic;
8
start: in std_logic;
9
finished: in std_logic;
10
rst: out std_logic);
11
end entity;
12
13
14
architecture rtl of FSM_NOP_Input is
15
16
----------------- COMPONENTS ---------------------
17
COMPONENT NOP_attribute
18
GENERIC (
19
N_bits: INTEGER;
20
N_new_values: INTEGER;
21
initial_value: STD_LOGIC_VECTOR
22
);
23
PORT(
24
att_clock :IN STD_LOGIC;
25
att_new_value :IN data(0 TO N_new_values-1)(N_bits-1
downto 0);
26
att_set_value :IN STD_LOGIC_VECTOR(N_new_values-1 downto
0);
27
att_value :OUT STD_LOGIC_VECTOR(N_bits-1 downto 0)
28
);
29
END COMPONENT;
30
COMPONENT NOP_premise
31
GENERIC (
32
N_bits: INTEGER:=1;
33
dataType: INTEGER:=0;
34
operation: INTEGER:=1 --EQUAL 1; DIFFERENT 2; LESS_THAN
3; GREATER_THAN 4; LESS_EQUAL 5; GREATER_EQUAL 6;
35
);
36
PORT(
37
att_value_a :IN STD_LOGIC_VECTOR(N_bits-1 downto 0);
38
att_value_b :IN STD_LOGIC_VECTOR(N_bits-1 downto 0);
39
pre_result :OUT STD_LOGIC
40
);
Fonte: Autoria própria (2025).


162
Listagem 70 – Parte 2 do arquivo FSM_NOP_Input.vhd
1
END COMPONENT;
2
COMPONENT NOP_method
3
GENERIC (
4
N_bits: INTEGER:=1;
5
dataType: INTEGER:=1;
6
operation: INTEGER:=1
7
);
8
PORT(
9
in_a :IN STD_LOGIC_VECTOR(N_bits-1 downto 0);
10
in_b :IN STD_LOGIC_VECTOR(N_bits-1 downto 0);
11
execute :IN STD_LOGIC;
12
result :OUT STD_LOGIC_VECTOR(N_bits-1 downto 0);
13
notify :OUT STD_LOGIC
14
);
15
END COMPONENT;
16
17
----------------- SIGNALS ---------------------
18
SIGNAL cInput_atState_new_value: data(0 TO 2-1)(0 downto 0);
19
SIGNAL cInput_atState_set: STD_LOGIC_VECTOR(2-1 downto 0);
20
SIGNAL cInput_atState_value: STD_LOGIC_VECTOR(0 downto 0) :=
"0";
21
22
SIGNAL prStart_result: STD_LOGIC;
23
SIGNAL prReset_result: STD_LOGIC;
24
25
SIGNAL prStart_input_a: STD_LOGIC_VECTOR(1-1 downto 0);
26
SIGNAL prReset_input_a: STD_LOGIC_VECTOR(1-1 downto 0);
27
28
29
constant prConstOne: STD_LOGIC_VECTOR(1-1 downto 0) := "1";
30
31
begin
32
cInput_atState: NOP_attribute GENERIC MAP(N_bits => 1,
N_new_values => 2, initial_value => "0") PORT MAP(att_clock
=> clk, att_new_value => cInput_atState_new_value,
att_set_value => cInput_atState_set, att_value =>
cInput_atState_value);
33
34
prStart_EQUAL: NOP_premise GENERIC MAP(N_bits => 1, dataType
=> 0, operation => 1) PORT MAP(att_value_a =>
prStart_input_a, att_value_b => prConstOne, pre_result =>
prStart_result);
35
prReset_EQUAL: NOP_premise GENERIC MAP(N_bits => 1, dataType
=> 0, operation => 1) PORT MAP(att_value_a =>
prReset_input_a, att_value_b => prConstOne, pre_result =>
prReset_result);
36
37
-- Inputs
38
prStart_input_a(0) <= start;
39
prReset_input_a(0) <= finished;
40
--


163
Listagem 71 – Parte 3 do arquivo FSM_NOP_Input.vhd
1
2
-- Methods
3
cInput_atState_new_value(0)(0) <= prStart_result;
4
cInput_atState_new_value(1)(0) <= not prReset_result;
5
6
cInput_atState_set(0) <= prStart_result;
7
cInput_atState_set(1) <= prReset_result;
8
9
rst <= not cInput_atState_value(0);
10
11
end architecture;
Fonte: Autoria própria (2025).


164
Listagem 72 – Parte 1 do arquivo FSM_Output.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
5
entity FSM_Output is
6
port(clk: in std_logic;
7
rst: in std_logic;
8
step: in std_logic;
9
lineSize: in std_logic_vector (4 downto 0);
10
columnSize: in std_logic_vector (4 downto 0);
11
channelSize: in std_logic_vector (1 downto 0);
12
cLine: out std_logic_vector(4 downto 0);
13
cCol: out std_logic_vector(4 downto 0);
14
cChan: out std_logic_vector(1 downto 0));
15
end entity;
16
17
18
architecture rtl of FSM_Output is
19
20
signal currentLine, currentColumn: std_logic_vector(4 downto
0) := "00000";
21
signal currentChannel, currentFilter: std_logic_vector(1
downto 0) := "00";
22
signal currentKernel: std_logic_vector(6 downto 0) :=
"0000000";
23
24
signal size_channel: integer range 0 to 4 := 0;
25
signal size_column: integer range 0 to 32 := 0;
26
signal size_line: integer range 0 to 32 := 0;
27
28
signal size_filter: integer range 0 to 128 := 0;
29
signal qtd_filter: integer range 0 to 4 := 0;
30
31
signal size_x: integer range 0 to 4 := 0;
32
signal size_y: integer range 0 to 4 := 0;
33
34
begin
35
36
-- registrar as entradas
37
process(clk)
38
begin
39
if rising_edge(clk) then
40
size_channel <= to_integer(unsigned(channelSize));
Fonte: Autoria própria (2025).


165
Listagem 73 – Parte 2 do arquivo FSM_Output.vhd
1
size_column <= to_integer(unsigned(columnSize));
2
size_line <= to_integer(unsigned(lineSize));
3
end if;
4
end process;
5
6
7
process(clk)
8
variable current_x: integer range 0 to 32 := 0;
9
variable current_y: integer range 0 to 32 := 0;
10
variable current_channel: integer range 0 to 4 := 0;
11
begin
12
if rising_edge(clk) then
13
if rst = ’1’ then
14
current_channel := 0;
15
current_x := 0;
16
current_y := 0;
17
18
elsif step = ’1’ then
19
if current_channel = size_channel then
20
current_channel := 0;
21
if current_x = size_column then
22
current_x := 0;
23
if current_y = size_line then
24
current_y := 0;
25
else
26
current_y := current_y + 1;
27
end if;
28
else
29
current_x := current_x + 1;
30
end if;
31
else
32
current_channel := current_channel + 1;
33
end if;
34
end if;
35
36
currentChannel <= std_logic_vector(to_unsigned(
current_channel, currentChannel’length));
37
currentColumn <= std_logic_vector(to_unsigned(current_x,
currentColumn’length));
38
currentLine <= std_logic_vector(to_unsigned(current_y,
currentLine’length));
39
end if;
40
end process;
Fonte: Autoria própria (2025).


166
Listagem 74 – Parte 3 do arquivo FSM_Output.vhd
1
2
cLine <= currentLine;
3
cCol <= currentColumn;
4
cChan <= currentChannel;
5
6
end architecture;
Fonte: Autoria própria (2025).


167
Listagem 75 – Parte 1 do arquivo FSM_NOP_Output.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
USE work.data_type_pkg.all;
5
6
entity FSM_NOP_Output is
7
generic(delay : integer := 15);
8
port(clk: in std_logic;
9
activation: in std_logic;
10
start: in std_logic;
11
newFilter: in std_logic;
12
finished: in std_logic;
13
poolOrConv: in std_logic;
14
forceStep: in std_logic;
15
rst: out std_logic;
16
step: out std_logic;
17
wr_en: out std_logic;
18
done: out std_logic);
19
end entity;
20
21
22
architecture rtl of FSM_NOP_Output is
23
24
constant memory_delay : integer range 0 to 1024 := 3;
25
26
signal wr_en_array : std_logic_vector(delay - 1 downto 0) :=
(others => ’0’);
27
signal finished_array : std_logic_vector(delay - 1 downto 0)
:= (others => ’0’);
28
signal state, finished_var : std_logic := ’0’;
29
30
begin
31
32
33
process(clk)
34
variable rst_var: std_logic := ’1’;
35
begin
36
37
if rising_edge(clk) then
38
if state = ’1’ then
39
rst_var := ’0’;
40
if poolOrConv = ’0’ then
Fonte: Autoria própria (2025).


168
Listagem 76 – Parte 2 do arquivo FSM_NOP_Output.vhd
1
-- Caso RELU
2
-- Delay - 2
3
if activation = ’0’ and finished_array(1) = ’1’ then
4
state <= ’0’;
5
rst_var := ’1’;
6
-- Caso Sigmoid
7
-- Delay - 1
8
elsif activation = ’1’ and finished_array(0) = ’1’
then
9
state <= ’0’;
10
rst_var := ’1’;
11
end if;
12
else
13
if poolOrConv = ’0’ then
14
if finished_array(DELAY - memory_delay - 1) = ’1’
then
15
state <= ’0’;
16
rst_var := ’1’;
17
end if;
18
else
19
if finished = ’1’ then
20
state <= ’0’;
21
rst_var := ’1’;
22
end if;
23
end if;
24
end if;
25
26
end if;
27
28
finished_array(DELAY -1) <= finished;
29
wr_en_array(DELAY -1) <= newFilter;
30
31
32
shift: for i in 0 to DELAY -2 loop
33
finished_array(i) <= finished_array(i+1);
34
wr_en_array(i) <= wr_en_array(i+1);
35
end loop shift;
36
37
if start = ’1’ then
38
rst_var := ’1’;
39
state <= ’1’;
40
finished_array <= (others => ’0’);
Fonte: Autoria própria (2025).


169
Listagem 77 – Parte 3 do arquivo FSM_NOP_Output.vhd
1
wr_en_array <= (others => ’0’);
2
end if;
3
4
rst <= rst_var;
5
6
end if;
7
end process;
8
9
-- Usando state como enable
10
wr_en <= wr_en_array(1) and state when activation = ’0’ and
poolOrConv = ’0’ else
11
wr_en_array(0) and state when activation = ’1’ and
poolOrConv = ’0’ else
12
newFilter and state; -- bypass
13
14
step <=
wr_en_array(1 + memory_delay) and state when
activation = ’0’ and poolOrConv = ’0’ else
15
wr_en_array(0 + memory_delay) and state when activation
= ’1’ and poolOrConv = ’0’ else
16
(wr_en_array(DELAY - 1) or forceStep) and state;
17
18
done <=
finished_array(1) and state when activation = ’0’
and poolOrConv = ’0’ else
19
finished_array(0) and state when activation = ’1’ and
poolOrConv = ’0’ else
20
finished and state; -- bypass
21
22
23
end architecture;
Fonte: Autoria própria (2025).


170
Listagem 78 – Parte 1 do arquivo FSM_NOP_Control.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
USE work.data_type_pkg.all;
5
6
entity FSM_NOP_Control is
7
port(clk: in std_logic;
8
kernelSize: in std_logic_vector (6 downto 0);
9
start: in std_logic;
10
finished: in std_logic;
11
poolOrConv: in std_logic;
12
fcOrConv: in std_logic;
13
NewFilter: out std_logic;
14
load_shift: out std_logic;
15
accumulate: out std_logic;
16
forceStep: out std_logic;
17
done: out std_logic);
18
end entity;
19
20
21
architecture rtl of FSM_NOP_Control is
22
23
24
begin
25
26
27
process(clk)
28
variable state : integer range 0 to 3 := 0;
29
variable mac_counter: integer range 0 to 16 := 0;
30
variable load_shift_counter : integer range 0 to 128 := 0;
31
32
variable load_shift_var, accumulate_var : std_logic := ’0’;
33
variable finished_notification : std_logic := ’0’;
34
variable done_var, NewFilter_var: std_logic := ’0’;
35
variable force_step_var: std_logic := ’0’;
36
begin
37
if rising_edge(clk) then
38
39
if finished = ’1’ and state = 2 then
40
finished_notification := ’1’;
Fonte: Autoria própria (2025).


171
Listagem 79 – Parte 2 do arquivo FSM_NOP_Control.vhd
1
end if;
2
3
load_shift_var := ’0’; -- Por padrão 0
4
force_step_var := ’0’;
5
6
if state = 1 then
7
-- Espera o delay até chegar o primeiro valor
8
-- 11 delays para modo Conv
9
-- 9 delays para modo pool
10
if poolOrConv = ’0’ then
11
if mac_counter /= 10 then
12
mac_counter := mac_counter + 1;
13
else
14
mac_counter := 0;
15
accumulate_var := ’1’;
16
state := 2;
17
end if;
18
else
19
if mac_counter = 5 then
20
mac_counter := mac_counter + 1;
21
force_step_var := ’1’;
22
elsif mac_counter /= 9 then
23
mac_counter := mac_counter + 1;
24
else
25
mac_counter := 0;
26
state := 2;
27
load_shift_var := ’1’;
28
end if;
29
end if;
30
elsif state = 2 then
31
if load_shift_counter = to_integer(unsigned(kernelSize)
) then
32
load_shift_counter := 0;
33
load_shift_var := ’1’;
34
if finished_notification = ’1’ then
35
state := 3;
36
finished_notification := ’0’;
37
load_shift_var := ’1’;
38
if fcOrConv = ’1’ or to_integer(unsigned(kernelSize
)) > 15 then
39
state := 0;
40
done_var := ’1’;
Fonte: Autoria própria (2025).


172
Listagem 80 – Parte 3 do arquivo FSM_NOP_Control.vhd
1
accumulate_var := ’0’;
2
end if;
3
end if;
4
else
5
load_shift_counter := load_shift_counter + 1;
6
end if;
7
-- ciclos adicionais para flush dos dados
8
elsif state = 3 then
9
if poolOrConv = ’0’ then
10
if mac_counter /= 8 then
11
mac_counter := mac_counter + 1;
12
else
13
mac_counter := 0;
14
accumulate_var := ’0’;
15
load_shift_var := ’1’;
16
done_var := ’1’;
17
state := 0;
18
end if;
19
else
20
if mac_counter /= 3 then
21
mac_counter := mac_counter + 1;
22
else
23
mac_counter := 0;
24
load_shift_var := ’1’;
25
done_var := ’1’;
26
state := 0;
27
end if;
28
end if;
29
end if;
30
31
32
if start = ’1’ then
33
state := 1;
34
mac_counter := 0;
35
load_shift_counter := 0;
36
37
accumulate_var := ’0’;
38
done_var := ’0’;
39
end if;
40
Fonte: Autoria própria (2025).


173
Listagem 81 – Parte 4 do arquivo FSM_NOP_Control.vhd
1
2
accumulate <= accumulate_var;
3
load_shift <= load_shift_var;
4
done <= done_var;
5
NewFilter <= load_shift_var;
6
7
forceStep <= force_step_var;
8
end if;
9
end process;
10
11
end architecture;
Fonte: Autoria própria (2025).


174
Listagem 82 – Parte 1 do arquivo FSM_NOP_Parameters.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
USE work.data_type_pkg.all;
5
6
entity FSM_NOP_Parameters is
7
port(clk: in std_logic;
8
baseAdress: in std_logic_vector (7 downto 0);
9
filterQtd: in std_logic_vector (1 downto 0);
10
start: in std_logic;
11
parametersAdress: out std_logic_vector (7 downto 0);
12
selectModule: out std_logic_vector (7 downto 0);
13
wr_en: out std_logic;
14
done: out std_logic);
15
end entity;
16
17
18
architecture rtl of FSM_NOP_Parameters is
19
20
signal muxSelect: std_logic_vector(7 downto 0) := "00000000";
21
22
signal delay_finished_1, delay_finished_2 : std_logic := ’0’;
23
signal delay_muxSelect_1, delay_muxSelect_2: std_logic_vector
(7 downto 0) := "00000000";
24
25
26
begin
27
28
29
process(clk)
30
variable state : std_logic := ’0’;
31
variable counter : integer range 0 to 8 := 0;
32
variable filter_counter : integer range 0 to 4 := 0;
33
variable current_address : unsigned(7 downto 0) := (others
=> ’0’);
34
variable loop_counter : integer range 0 to 4 := 0;
35
36
variable wr_en_var, finished : std_logic := ’0’;
37
begin
38
finished := ’0’;
39
40
if rising_edge(clk) then
Fonte: Autoria própria (2025).


175
Listagem 83 – Parte 2 do arquivo FSM_NOP_Parameters.vhd
1
-- Carregar os parametros
2
if state = ’1’ then
3
-- Registrador Shift
4
l_shift: for i in 0 to 7 loop
5
muxSelect((i+1) mod 8) <= muxSelect(i);
6
end loop l_shift;
7
8
wr_en_var := ’1’;
9
-- Carrega 8 valores
10
-- Contando a partir do 0
11
if counter /= 7 then
12
counter := counter + 1;
13
current_address := current_address + 1;
14
else
15
counter := 0;
16
if filter_counter = to_integer(unsigned(filterQtd))
then
17
-- Reseta o endereço
18
current_address := unsigned(baseAdress);
19
filter_counter := 0;
20
else
21
-- Continuar incrementando o endereço
22
current_address := current_address + 1;
23
filter_counter := filter_counter + 1;
24
end if;
25
26
-- Condicao para terminio
27
-- Quatro loops, a partir do 0
28
if loop_counter = 3 then
29
-- Reseta o estado
30
state := ’0’;
31
finished := ’1’;
32
wr_en_var := ’0’;
33
muxSelect <= (others => ’0’);
34
else
35
loop_counter := loop_counter + 1;
36
end if;
37
end if;
38
else
39
wr_en_var := ’0’;
40
end if;
Fonte: Autoria própria (2025).


176
Listagem 84 – Parte 3 do arquivo FSM_NOP_Parameters.vhd
1
2
if start = ’1’ then
3
state := ’1’;
4
counter := 0;
5
filter_counter := 0;
6
loop_counter := 0;
7
wr_en_var := ’1’;
8
current_address :=
unsigned(baseAdress);
9
muxSelect <= "00000001";
10
end if;
11
12
13
parametersAdress <= std_logic_vector(current_address);
14
wr_en <= wr_en_var;
15
16
done <= delay_finished_1;
17
delay_finished_2 <= delay_finished_1;
18
delay_finished_1 <= finished;
19
20
selectModule <= delay_muxSelect_1;
21
delay_muxSelect_2 <= delay_muxSelect_1;
22
delay_muxSelect_1 <= muxSelect;
23
end if;
24
end process;
25
26
end architecture;
Fonte: Autoria própria (2025).


177
Listagem 85 – Parte 1 do arquivo FSM_NOP_Main.vhd
1
library ieee;
2
use ieee.std_logic_1164.all;
3
use ieee.numeric_std.all;
4
USE work.data_type_pkg.all;
5
6
entity FSM_NOP_Main is
7
port(clk: in std_logic;
8
start: in std_logic;
9
donePar: in std_logic;
10
doneMath: in std_logic;
11
running: out std_logic;
12
parameterStart: out std_logic;
13
convStart: out std_logic;
14
poolOrConv: out std_logic;
15
fcOrConv: out std_logic;
16
activation: out std_logic;
17
18
lineSize: out std_logic_vector (4 downto 0);
19
columnSize: out std_logic_vector (4 downto 0);
20
channelSize: out std_logic_vector (1 downto 0);
21
kernelSize: out std_logic_vector (6 downto 0);
22
filterQtd: out std_logic_vector (1 downto 0);
23
windowHeight: out std_logic_vector (2 downto 0);
24
windowWidth: out std_logic_vector (2 downto 0);
25
strideHeight: out std_logic_vector (1 downto 0);
26
strideWidth: out std_logic_vector (1 downto 0);
27
pBaseAdress: out std_logic_vector (7 downto 0);
--
Parameters
28
dBaseAdress: out std_logic_vector (12 downto 0);
-- Data
29
wBaseAdress: out std_logic_vector (9 downto 0);
--
Weight
30
oBaseAdress: out std_logic_vector (12 downto 0);
-- Output Data
31
ChannelColumnSize: out std_logic_vector (6 downto 0);
32
OutputLineSize: out std_logic_vector (4 downto 0);
33
OutputColumnSize: out std_logic_vector (4 downto 0);
34
OutputChannelColumnSize: out std_logic_vector (6 downto
0)
35
);
36
end entity;
37
38
39
architecture rtl of FSM_NOP_Main is
40
Fonte: Autoria própria (2025).


178
Listagem 86 – Parte 2 do arquivo FSM_NOP_Main.vhd
1
-- Formato de memoria
2
-- (0) -> Tipo de ativação -> 0 = Relu e 1 = Sigmoid
3
-- (1) -> Tipo de operacao -> 0 = Conv/Fullyconnected e 1 =
Pool
4
-- (2) -> FC ou Conv -> 0 = Conv c.c. FC.
5
-- (15-3) -> Endereço base dos dados
6
-- (25-16) -> Endereço base dos pesos
7
-- (33-26) -> Endereço base dos parametros
8
-- (35-34) -> Stride X
9
-- (37-36) -> Stride Y
10
-- (40-38) -> Janela X
11
-- (43-41) -> Janela Y
12
-- (45-44) -> Quantidade de Filtros
13
-- (52-46) -> Tamanho do Kernel
14
-- (54-53) -> Quantidade de Canais
15
-- (59-55) -> Tamanho da Coluna
16
-- (64-60) -> Tamanho da Linha
17
-- (71-65) -> Canais * Coluna -> precalculado
18
-- (84-74) -> Endereço base dos resultados
19
-- (89-85) -> Tamanho da Linha da Saida
20
-- (94-90) -> Tamanho da Coluna da Saida
21
-- (101-95) -> Canais * Coluna -> precalculado da Saida
22
23
24
type mem is array (0 to 16) of std_logic_vector(101 downto 0);
25
constant instr : mem := (
26
0 => "110100011001110011000000000000001110011001110010000
27
010001101001001010000000000000000000000000000000000",
28
1 => "1100000101111011100000000000001101000101111011111010
29
00111101001001010010000000001001001000000000000000",
30
2 => "001100010111101111000000000000110000010110101101100
31
000110000100110100000000000000000000000000000000010",
32
3 => "010100001001010010000000000000011000001001010011101
33
000111101001001010100000000101101001000000000000000",
34
4 => "0001010010010100110000000000000101000010000100011000
35
00110000100110100000000000000000000000000000000010",
36
5 => "00000000000000000000000000000000101000000000000111100
37
0110110010001010110000001010001001000000000000101",
38
others => (others=>’0’)
39
);
40
41
signal current_instr: std_logic_vector(101 downto 0) := (
others => ’0’);
42
43
begin
44
45
46
process(clk)
Fonte: Autoria própria (2025).


179
Listagem 87 – Parte 3 do arquivo FSM_NOP_Main.vhd
1
variable state: integer range 0 to 6 := 0;
2
variable instr_counter: integer range 0 to 16 := 0;
3
4
variable pStart, cStart: std_logic := ’0’;
5
6
begin
7
if rising_edge(clk) then
8
9
pStart := ’0’;
10
cStart := ’0’;
11
-- Começar a carregar os parametros
12
if state = 1 then
13
pStart := ’1’;
14
state := 2;
15
-- Sincronizar
16
elsif state = 2 then
17
if donePar = ’1’ then
18
state := 3;
19
end if;
20
-- Começa a executar a rede
21
elsif state = 3 then
22
cStart := ’1’;
23
state := 4;
24
-- Sincronizar
25
elsif state = 4 then
26
if doneMath = ’1’ then
27
state := 5;
28
end if;
29
-- Carrega a proxima instr ou termina
30
elsif state = 5 then
31
if current_instr(2) = ’1’ then
32
state := 0;
33
else
34
state := 1;
35
current_instr <= instr(instr_counter);
36
instr_counter := instr_counter + 1;
37
end if;
38
elsif state = 6 then
39
-- Estado a mais só para realizar sincronismo.
40
state := 6;
Fonte: Autoria própria (2025).


180
Listagem 88 – Parte 4 do arquivo FSM_NOP_Main.vhd
1
end if;
2
3
if start = ’1’ then
4
state := 1;
5
instr_counter := 1;
6
current_instr <= instr(0);
7
end if;
8
9
10
if state /= 0 then
11
running <= ’1’;
12
else
13
running <= ’0’;
14
end if;
15
16
parameterStart <= pStart;
17
convStart <= cStart;
18
end if;
19
end process;
20
21
activation <= current_instr(0);
22
poolOrConv <= current_instr(1);
23
fcOrConv <= current_instr(2);
24
dBaseAdress <= current_instr(15 downto 3);
25
wBaseAdress <= current_instr(25 downto 16);
26
pBaseAdress <= current_instr(33 downto 26);
27
strideWidth <= current_instr(35 downto 34);
28
strideHeight <= current_instr(37 downto 36);
29
windowWidth <= current_instr(40 downto 38);
30
windowHeight <= current_instr(43 downto 41);
31
filterQtd <= current_instr(45 downto 44);
32
kernelSize <= current_instr(52 downto 46);
33
channelSize <= current_instr(54 downto 53);
34
columnSize <= current_instr(59 downto 55);
35
lineSize <= current_instr(64 downto 60);
36
ChannelColumnSize <= current_instr(71 downto 65);
37
oBaseAdress <= current_instr(84 downto 72);
38
OutputLineSize <= current_instr(89 downto 85);
39
OutputColumnSize <= current_instr(94 downto 90);
40
OutputChannelColumnSize <= current_instr(101 downto 95);
41
end architecture;
Fonte: Autoria própria (2025).


