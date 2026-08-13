### Relatório de Benchmarking Técnico: Avaliação de Variantes LoRA e a Primazia da Taxa de Aprendizado (LR) no Fine-tuning de LLMs

#### 1\. Introdução e Contexto Estratégico

O avanço vertiginoso nas capacidades dos Grandes Modelos de Linguagem (LLMs) é acompanhado por uma barreira de entrada crítica: o custo computacional e de memória do  *Full Fine-tuning* . Com modelos escalando para centenas de bilhões de parâmetros, a adaptação para domínios específicos — como a precisão terminológica na medicina ou a análise de volatilidade nas finanças — exige abordagens de  *Parameter-Efficient Fine-tuning*  (PEFT). Nesse ecossistema, o  **Low-Rank Adaptation (LoRA)**  emergiu como o padrão  *de facto* , prometendo eficiência ao treinar apenas uma fração mínima de pesos. No entanto, o campo de pesquisa atual sofre de uma lacuna metodológica preocupante. Nossa análise de 52 artigos de alto impacto revela que menos de 30% dos trabalhos realizam o ajuste da taxa de aprendizado (LR) e apenas um único trabalho (1 em 52\) considerou simultaneamente o Rank, o Batch Size e a LR.A tese central deste relatório é que o aparente progresso metodológico de variantes "avançadas" do LoRA é frequentemente um artefato de setups subotimizados para o baseline. Demonstramos que a sensibilidade do LoRA à LR é o fator determinante do desempenho; uma vez que este parâmetro é rigorosamente otimizado, observa-se uma paridade de resultados (dentro de uma margem de 1-2%) entre o LoRA original e suas variantes mais complexas. Este fenômeno exige uma reavaliação da taxonomia e do rigor experimental aplicado ao fine-tuning de LLMs.

#### 2\. Taxonomia dos Métodos PEFT Avaliados

A escolha da arquitetura do adaptador é uma decisão técnica fundamental, mas muitas vezes baseada em premissas de inicialização incompletas. Para garantir que o treinamento comece exatamente no checkpoint pré-treinado, as variantes de inicialização utilizam o conceito de  **Matriz Residual (**  **$W\_{res}**$  **)** . Formalmente, a operação de  *forward pass*  é redefinida como:  $$h \= W\_{res}x \+ \\gamma BAx$$  Onde  $W\_{res}$  é configurado para compensar a inicialização não-nula dos adaptadores. Abaixo, detalhamos as cinco metodologias avaliadas:

* **Low-Rank Adaptation (LoRA):**  Utiliza matrizes de  *down-projection*  ( **A** ) e  *up-projection*  ( **B** ). A inicialização padrão emprega Kaiming Uniform para a matriz A e zero para a matriz B, garantindo que o termo de adaptação inicial seja nulo.  
* **Variantes de Inicialização baseadas em SVD:**  
* **PiSSA (Principal Singular values and Singular vectors Adaptation):**  Inicializa as matrizes  $A$  e  $B$  com os componentes principais (maiores valores singulares) da matriz original  $W\_{pre}$ . Aqui,  $W\_{res} \= W\_{pre} \- B\_0 A\_0$ , focando o treinamento nas direções de maior variância.  
* **MiLoRA (Minor Singular components Adaptation):**  Em oposição ao PiSSA, utiliza os componentes menores (menores valores singulares) para inicializar os adaptadores, visando preservar o conhecimento base e mitigar o esquecimento catastrófico.  
* **InitAB:**  Estratégia de inicialização aleatória não-nula para ambas as matrizes (A e B). Assim como no PiSSA, utiliza a matriz residual para manter a fidelidade ao modelo original no tempo zero do fine-tuning.  
* **Modificação Arquitetural (DoRA):**  
* **Weight-Decomposed Low-Rank Adaptation (DoRA):**  Desacopla os pesos pré-treinados em componentes de  **magnitude**  e  **direção** . O LoRA é aplicado apenas para atualizar a direção, buscando uma estabilidade de aprendizado similar ao  *Full Fine-tuning* .

#### 3\. Protocolo Unificado de Benchmarking e Configuração Experimental

A prática comum de herdar hiperparâmetros de trabalhos anteriores sem validação local compromete a integridade científica dos benchmarks PEFT. Diferentes métodos possuem cenários de perda ( *loss landscapes* ) distintos, exigindo um protocolo de avaliação justo e exaustivo.

##### Resumo do Setup Experimental

Para isolar o efeito da taxa de aprendizado, o fator de escala  $\\alpha$  foi mantido igual ao rank  $r$  (resultando em  $\\gamma\_r \= 1$ ), eliminando a redundância entre o escalonamento do adaptador e a LR.| Componente | Especificações Técnicas || \------ | \------ || **Modelos (Base versions)** | Qwen3-0.6B, Gemma-3-1B, Llama-2-7B. || **Datasets e Tarefas** | Matemática (MetaMathQA, GSM8K, MATH) e Código (CodeFeedback, HumanEval, MBPP). || **Rank do Adaptador (r)** | 4, 8, 16, 32, 64, 128, 256\. || **Batch Size (B)** | 16, 64, 128\. || **Busca de LR (**  **$\\eta**$  **)** | Busca logarítmica exaustiva ( $10^{-3}$  a  $10^{-6}$ ), com 4 pontos por ordem de magnitude. |

#### 4\. Análise de Desempenho e o Mito das Variantes Superiores

Os dados obtidos desafiam a narrativa de superioridade intrínseca das variantes. No modelo Qwen3-0.6B, por exemplo, a diferença entre o LoRA original (líder) e o MiLoRA foi de apenas  **0,43%**  após a sintonização da LR.

* **Paridade de Desempenho:**  Uma vez ajustada a LR ideal, o Vanilla LoRA frequentemente iguala ou supera variantes como DoRA e PiSSA. O progresso relatado em outros estudos é, em muitos casos, um reflexo da subotimização do baseline.  
* **Sensibilidade e Robustez do PiSSA:**  O PiSSA exige LRs significativamente menores para convergência inicial devido à sua alta curvatura. No entanto, demonstrou uma robustez única: em LRs extremamente altas (ex:  $1.1 \\times 10^{-3}$ ), onde o LoRA e outros métodos divergem para o colapso (gibberish), o PiSSA manteve acurácias razoáveis (\~27% em Llama-2), sugerindo uma estabilidade estrutural superior em regimes de alto ruído.  
* **A "Scaling Rule":**  Confirmamos que o desempenho não degrada necessariamente com o aumento do  *Batch Size* . A LR ideal escala proporcionalmente com o tamanho do lote; ao ajustar ambos, configurações de  $B=128$  mantêm a eficácia do treinamento.

#### 5\. Análise de Hessian: Fundamentação Matemática da Curvatura

Para fundamentar os achados experimentais, realizamos uma análise de segunda ordem (Hessian) no ponto de inicialização. A estabilidade do treinamento é ditada pela "Sharpness" (nitidez) do cenário de perda. A teoria clássica estabelece que a taxa de aprendizado ideal ( $\\eta^*$ ) é inversamente proporcional ao maior autovalor do Hessian ( $\\lambda\_{max}$ ):  $$\\eta^* \\propto \\frac{1}{\\lambda\_{max}(\\mathbf{H})}$$Nossos dados confirmam que o  **PiSSA apresenta um**  **$\\lambda\_{max}**$  **significativamente maior**  do que o LoRA original. Essa curvatura elevada explica matematicamente por que o PiSSA exige taxas de aprendizado mais baixas: o cenário de otimização é muito mais íngreme, e LRs convencionais causariam o "overshooting" imediato da solução. Variantes como MiLoRA e InitAB apresentam autovalores mais próximos ao do LoRA, justificando suas LRs ideais em ordens de magnitude similares.

#### 6\. Dinâmicas Dependentes de Rank e Comportamento de Borda

A superioridade de um método não é absoluta, mas dependente do espectro de Rank ( $r$ ) utilizado. Observamos comportamentos divergentes nas extremidades do espectro:

* **Baixo Rank (**  **$r \\leq 32**$  **):**  O DoRA e o MiLoRA demonstram ganhos marginais. O PiSSA, curiosamente, tende a  **subperformar**  o LoRA original em ranks baixos no dataset MetaMathQA, revelando que a seleção de componentes principais pode não ser a melhor estratégia quando a capacidade do adaptador é extremamente limitada.  
* **Alto Rank (**  **$r \\geq 128**$  **):**  O PiSSA recupera terreno, superando levemente o baseline. Em contrapartida, o  **MiLoRA perde sua vantagem competitiva** , chegando a performar  **0,63% abaixo do baseline**  em  $r=256$ . Isso reforça que a complexidade da inicialização SVD pode se tornar um detrator de performance se o Rank não for criteriosamente selecionado para a tarefa.

#### 7\. Conclusões e Implicações para Práticas de Fine-tuning

Este relatório demonstra que o rigor no ajuste de hiperparâmetros supera a complexidade arquitetural em valor estratégico. As conclusões críticas para a indústria e academia são:

1. **Suficiência do Vanilla LoRA:**  O método original é um baseline de altíssima robustez. Implementar variantes mais complexas sem antes explorar exaustivamente a LR do LoRA básico é uma ineficiência de engenharia.  
2. **Necessidade de Busca Ampla de LR:**  Pesquisas futuras devem adotar protocolos de busca logarítmica. Conclusões baseadas em um único conjunto de hiperparâmetros são vulneráveis e frequentemente enganosas.  
3. **Cuidado com o "Winner's Curse" em Benchmarks:**  O progresso no campo de PEFT é frequentemente um artefato de setups subotimizados para os baselines. A paridade observada sugere que muitos avanços relatados podem não ser universais.A transparência absoluta no relato de hiperparâmetros é a única via para garantir avanços confiáveis e reprodutíveis no campo da Inteligência Artificial. Antes de adotar novas variantes, a prioridade técnica deve ser a exploração da curvatura e da taxa de aprendizado do modelo base.

