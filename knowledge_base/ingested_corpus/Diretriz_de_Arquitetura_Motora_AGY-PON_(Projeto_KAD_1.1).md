### Diretriz de Arquitetura Motora AGY-PON (Projeto KAD 1.1)

##### 1\. Visão Geral e Alinhamento Arquitetural

**1.1. Objetivo do Documento**  Esta diretriz estabelece o protocolo técnico para a migração do motor Antigravity (AGY) para o Paradigma Orientado a Notificações (PON), integrando os componentes Amdy (Hardware) e Tell (Software) no contexto do Projeto KAD 1.1. O objetivo é converter a lógica de execução passiva em uma infraestrutura reativa de alto desempenho fundamentada na dissertação de Peters (2012).**1.2. Fundamentação do Paradigma**  O PON baseia-se na influência causal exercida através da colaboração pontual entre entidades granulares e notificantes. Diferente dos paradigmas procedimentais ou orientados a objetos, onde dados e expressões são passivos e dependem de pesquisa (polling), o PON transforma estas entidades em agentes ativos. Esta mudança arquitetural elimina as "verificações redundantes" inerentes aos modelos tradicionais (BANASZEWSKI, 2009), onde o fluxo de execução consome ciclos de clock processando dados que não sofreram alteração.**1.3. Vantagens Comparativas**

* **Eficiência de Ciclos de Clock:**  Redução de até 96% nos ciclos de clock se comparada a uma implementação puramente em software da mesma aplicação (PETERS, 2012, p. 5).  
* **Desenvolvimento de Alto Nível:**  Representação do conhecimento em forma de regras, alinhada à forma cognitiva humana e facilitando esforços mínimos de codificação.  
* **Reuso de Código:**  Estrutura granular que permite a independência e portabilidade de Elementos da Base de Fatos (FBEs).  
* **Otimização Energética:**  Alta performance que permite a operação em frequências de clock reduzidas sem perda de vazão lógica.

##### 2\. Estrutura de Entidades da Base de Fatos (FBE)

**2.1. Definição de Elementos da Base de Fatos (FBEs)**  As entidades devem ser organizadas de forma que cada alteração de estado propague notificações pela cadeia causal:

* **Atributos:**  Representam os fatos brutos. Possuem a função ativa de notificar mudanças aos seus dependentes.  
* **Premissas:**  Avaliam o estado dos atributos via operações relacionais (==, \!=, \>, \<, \>=, \<=).  
* **Condições:**  Agrupam logicamente as premissas, consolidando o estado de verdade para a ativação de regras.  
* **Regras:**  Instâncias lógicas finais. No motor AGY, as regras aprovadas não aguardam pesquisa; elas são encaminhadas para uma  **FIFO de armazenamento de regras aprovadas**  (PETERS, 2012, p. 63), garantindo a ordem de execução.  
* **Ações e Instigações:**  Gatilhos procedimentais disparados imediatamente após a aprovação da regra na base de fatos.**2.2. Mapeamento de Memória para FBEs**  A integração entre o software (Tell) e o hardware acelerador (Amdy) deve seguir rigorosamente o mapeamento de memória via interface Avalon MM, conforme os Quadros 1 a 5 da fonte:| Endereço (Offset) | Campo | Descrição Técnica || \------ | \------ | \------ || **Atributo**  (0x00) | Valor / Notif. Addr | Armazena o dado e o endereço da entidade a ser notificada. || **Atributo**  (0x08) | Controle / Status | Registrador de status de prontidão e controle de escrita. || **Premissa**  (0x10) | Operandos / Tipo Op. | Define os valores comparativos e o tipo de relação (ex: \==, \>=). || **Condição**  (0x20) | Máscara / Estado | Vetor de bits das premissas e registrador de estado lógico. || **Periférico**  (0x40) | Registrador Global | Configuração geral do motor AGY e gerenciamento de interrupções. || **FIFO Regras**  (0x60) | Saída de Regras | Ponteiro para a próxima regra aprovada pronta para execução. |

##### 3\. Diretriz de Operação: Eliminação de Polling e Fluxo Reativo

**3.1. Extinção do Polling**   **É terminantemente proibida a implementação de loops de verificação de estado (polling) para monitoramento de variáveis na camada AGY-PON.**  No paradigma PON, os dados são entidades ativas que "conhecem" seus dependentes (PETERS, 2012, p. 14). A CPU não deve perguntar se um valor mudou; ela deve aguardar a notificação passiva gerada pela mudança do fato.**3.2. Mecanismo de Notificação e RTL**  A causalidade deve ser tratada em nível de  **Transferência de Registro (RTL)** . Cada mudança de bit em um Atributo deve disparar um sinal físico de notificação para as Premissas vinculadas via barramento local.**3.3. Integração Distribuída via MQTT**  Enquanto a lógica reativa central ocorre em hardware (RTL), a comunicação entre dispositivos distintos no Projeto KAD 1.1 deve utilizar o protocolo MQTT como camada de transporte distribuído. O motor AGY deve publicar mudanças de fatos e assinar instigações, mantendo a semântica de "notificação por evento" mesmo em ambiente de rede.

##### 4\. Metadados de Hardware e Software (Amdy e Tell)

**4.1. Configuração de Hardware (Amdy)**  O motor AGY deve ser sintetizado em FPGAs (como a família Cyclone IV) utilizando Unidades Lógicas (LU) e Tabelas de Busca (LUT). A arquitetura deve prever o uso do processador  **Nios II**  atuando como mestre no barramento, comunicando-se com o acelerador AGY via interface  **Avalon MM**  para garantir baixa latência.**4.2. Interface de Software (Tell)**  A interface Tell deve gerenciar a configuração dinâmica de Atributos e Regras diretamente nos endereços mapeados em memória (Seção 3.4.5, Peters 2012). O software deve ser capaz de inicializar a Base de Fatos (FBE) e, em seguida, entrar em estado de espera, reagindo apenas às interrupções geradas pelo hardware acelerador.

##### 5\. Diretrizes de Implementação e Performance

**5.1. Uso de Coprocessamento**  O motor AGY deve atuar como um  **Hardware Acelerador** . Toda a carga de processamento de regras, condições e premissas deve ser delegada à lógica programável da FPGA. A CPU principal deve ser liberada para tarefas de coordenação e interface, operando em modo "slave" em relação à cadeia de notificações do PON.**5.2. Métricas de Sucesso e Desempenho**  A implementação será validada pelos seguintes critérios documentados:

* **Latência de Transição:**  Redução drástica de aproximadamente  **521 ciclos de clock (em software)**  para apenas  **20 ciclos de clock (em hardware)**  por transição de estado (PETERS, 2012, Tabela 1, p. 80).  
* **Frequência de Operação (**  **$f\_{MAX}**$  **):**  A implementação deve buscar a frequência máxima estável conforme a Figura 32 do contexto, garantindo que o tempo de propagação da notificação seja minimizado.

##### 6\. Glossário Técnico Operacional

* **FPGA (Field Programmable Gate Array):**  Dispositivo que permite a implementação de funções lógicas definidas pelo usuário através de matrizes de memória programáveis.  
* **VHDL (VHSIC Hardware Description Language):**  Linguagem de descrição de hardware utilizada para o desenvolvimento e síntese do coprocessador.  
* **RTL (Register Transfer Level):**  Nível de codificação que descreve a transferência de registros no hardware.  
* **FBE (Elemento da Base de Fatos):**  Componente atômico que compõe a lógica de conhecimento do PON (Atributos, Premissas, etc.).  
* **PON (Paradigma Orientado a Notificações):**  Modelo de programação baseado na colaboração entre entidades notificantes para reduzir desperdício de processamento.

