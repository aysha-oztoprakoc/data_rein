### Design Document: Arquitetura e Pipeline Framework KAD 1.1

#### 1\. Visão Geral e Objetivos da Evolução KAD 1.1

A transição da versão KAD 1.0 para a 1.1 representa uma ruptura definitiva com o processamento passivo baseado em  *polling* , migrando para uma arquitetura puramente reativa fundamentada no Paradigma Orientado a Notificações (PON). O objetivo mandatório é a eliminação da latência computacional e do processamento redundante, mimetizando a eficiência de interrupções de hardware em nível de aplicação.**Pilares Centrais da Atualização:**

1. **Migração para Fact Base Elements (FBE):**  Transição do processamento de arquivos estáticos ( *File Binary Extraction* ) para a manipulação de fatos dinâmicos em memória.  
2. **Reatividade de Hardware e OS:**  Integração profunda com o kernel Arch Linux (Omarchy), tratando estados de RAM e VRAM como entidades notificantes.  
3. **Orquestração Distribuída via MQTT/Docker:**  Execução de lógica pesada (IA) em containers disparados exclusivamente por eventos validados.

#### 2\. Fundamentação do Paradigma Orientado a Notificações (PON)

Baseado na tese de Peters (2012), o PON é definido como uma "colaboração pontual entre entidades granulares e notificantes". Diferente do paradigma imperativo, onde o fluxo de execução "pergunta" pelo estado do dado, no KAD 1.1 o dado possui a incumbência de notificar as entidades dependentes apenas quando ocorre uma alteração relevante.**Glossário Técnico KAD 1.1:**

* **Atributos:**  Entidades que representam dados brutos. No KAD 1.1, são mapeados diretamente para endereços de memória.  
* **Premissas:**  Unidades de teste comparativo. Realizam operações lógicas/aritméticas sobre os Atributos no instante da notificação.  
* **Condições:**  Agrupadores lógicos de Premissas que definem estados complexos do sistema.  
* **Regras:**  Entidades decisórias. Quando as Condições são satisfeitas, a Regra é aprovada e encaminhada para o pipeline de execução.  
* **Métodos (Instigações):**  No KAD 1.1, os Métodos são tratados estritamente como  **Instigações**  (chamadas externas via MQTT para containers Docker), distinguindo-se das  **Ações** , que são alterações de estado internas à base de fatos.

#### 3\. Reengenharia Conceitual: De FBE (Binário) para FBE (Fato)

O KAD 1.1 reinterpreta o acrônimo FBE. Abandonamos o  *File Binary Extraction*  (processamento de arquivos em disco) para adotar o  **Fact Base Element**  (Elemento da Base de Fatos). Esta mudança elimina o gargalo de I/O de disco e a necessidade de buffers de leitura.| Característica | KAD 1.0 (File Binary Extraction) | KAD 1.1 (Fact Base Element) || \------ | \------ | \------ || **Persistência** | Arquivos físicos em disco (Latência de I/O). | Estados voláteis em RAM/VRAM (Tempo Real). || **Mecanismo de Acesso** | Buffers de leitura e busca (Polling). | **Memory Mapped I/O (MMIO)**  conforme Peters (2012). || **Uso de Memória** | Alta redundância (Cópia de buffers). | Mínimo (Mapeamento direto de Atributos). || **Processamento** | Ciclos de CPU desperdiçados em verificações. | Notificações orientadas a eventos de hardware. |

#### 4\. Modelagem Reativa do Hardware e OS (Arch Linux/Omarchy)

A arquitetura KAD 1.1 utiliza a lógica de interface  **Avalon MM (Memory Mapped)**  para integrar o hardware como um FBE nativo. O sistema operacional Omarchy mapeia endereços específicos de VRAM (GPU) e RAM como  *Atributos*  do PON.Diferente de sistemas tradicionais, uma escrita de dado pelo hardware em um endereço mapeado não requer interrupção de software para verificação; o próprio mapeamento dispara a cadeia de notificações.**Fluxo Lógico Determinístico:**  Alteração no Hardware (Escrita VRAM) \-\> Notificação Automática do Atributo \-\> Avaliação RTL de Premissas \-\> Aprovação de Regras \-\> Trigger de Instigação (Docker via MQTT).

#### 5\. Pipeline de Execução e Orquestração

A integração entre o  **Framework PON C++ 4.0 IoT**  e o protocolo  **MQTT**  utiliza  **QoS 0**  para garantir a menor latência possível, priorizando a velocidade de notificação sobre a confirmação de entrega em rede local.**Sequência de Execução do Pipeline:**

1. **Captura de Fato:**  O hardware altera um estado mapeado no Mapa de Memória do Periférico (Quadro 5, Peters).  
2. **Avaliação Granular:**  O motor C++ avalia a lógica de Premissas e Condições.  
3. **FIFO de Regras:**  Regras aprovadas são inseridas em uma  **FIFO de armazenamento**  (Figura 25, Peters), garantindo que nenhuma notificação seja perdida durante picos de carga.  
4. **Despacho MQTT:**  O broker encaminha a notificação para os motores  **agy**  ou  **Odysseus AI** .  
5. **Instigação Docker:**  O container alvo executa o  *Method*  (inferência de IA ou lógica de controle) de forma isolada e escalável.

#### 6\. Eficiência e Performance: Eliminação de Polling

A arquitetura KAD 1.1 busca replicar em software o desempenho obtido pelo  **CoPON (Coprocessador PON)**  documentado por Peters (2012). Em testes de hardware, a migração de PON em software para aceleração direta resultou em um  **decréscimo de 96% nos ciclos de clock** . Ao tratar o hardware como FBE e eliminar o polling, o KAD 1.1 elimina a redundância temporal.**Comparativo de Carga Computacional:**  
// ABORDAGEM TRADICIONAL (KAD 1.0 \- Polling Ineficiente)  
while(true) {  
    if (read\_memory(VRAM\_ADDR) \== TRIGGER\_VALUE) {  
        execute\_task(); // Desperdício massivo de ciclos de clock em idle  
    }  
}

// ABORDAGEM REATIVA (KAD 1.1 \- PON / Latência Zero)  
// O processador permanece em estado de espera ou executando outras tarefas.  
// A execução é disparada via callback de notificação de hardware.  
on\_attribute\_change(VRAM\_ADDR, \[\](auto value) {  
    evaluate\_rules(value); // Execução estritamente sob demanda (Event-Driven)  
});

#### 7\. Especificações de Implementação Técnica

Para garantir o determinismo e a performance de "Zero-Polling", os seguintes requisitos são mandatórios:

* **C++ 4.0 IoT:**  Uso obrigatório de aritmética de ponto fixo e alinhamento estrito de memória para compatibilidade com os Mapas de Memória PON (Quadros 1 e 2, Peters, p. 57-58).  
* **Mapeamento de Memória:**  Implementação via  **Register Transfer Level (RTL)**  para garantir que a notificação ocorra no ciclo de clock subsequente à alteração do Atributo.  
* **Protocolo de Mensageria:**  Uso de MQTT com Broker local (ex: Mosquitto) configurado para latência ultra-baixa.  
* **Proibição de Bloqueio:**  É estritamente proibido o uso de sleep(), usleep(), ou loops while(true) de monitoramento. O sistema deve ser 100% orientado a interrupções e notificações de estado.

#### 8\. Considerações de Escalabilidade e Trabalhos Futuros

A arquitetura baseada em instigações externas permite que o  **Odysseus AI**  escale horizontalmente; múltiplos containers podem assinar diferentes tópicos de "Regras Aprovadas", permitindo processamento paralelo massivo sem sobrecarregar o núcleo reativo.O KAD 1.1 atua como a ponte crítica de software para a futura integração de  **aceleração via FPGA (VHDL)** . Seguindo a arquitetura  **SOPC (System on a Programmable Chip)**  de Peters (2012), a versão 1.2 moverá os blocos de Premissas e Condições para lógica programável, atingindo o limite físico de redução de ciclos de clock e consolidando a reatividade absoluta do ecossistema KAD.  
