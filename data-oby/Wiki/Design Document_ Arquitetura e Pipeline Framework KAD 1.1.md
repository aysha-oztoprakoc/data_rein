### Design Document: Arquitetura e Pipeline Framework KAD 1.1
#### 1\. Visão Geral e Objetivos da Evolução KAD 1.1
A transição da versão KAD 1.0 para a 1.1 representa uma ruptura definitiva com o processamento passivo baseado em *polling* , migrando para uma arquitetura puramente reativa fundamentada no Paradigma Orientado a Notificações (PON). O objetivo mandatório é a eliminação da latência computacional e do processamento redundante, mimetizando a eficiência de interrupções de hardware em nível de aplicação.**Pilares Centrais da Atualização:**
1. **Migração para Fact Base Elements (FBE):** Transição do processamento de arquivos estáticos ( *File Binary Extraction* ) para a manipulação de fatos dinâmicos em memória. 
2. **Reatividade de Hardware e OS:** Integração profunda com o kernel Arch Linux (Omarchy), tratando estados de RAM e VRAM como entidades notificantes. 
3. **Orquestração Distribuída via MQTT/Docker:** Execução de lógica pesada (IA) em containers disparados exclusivamente por eventos validados.
#### 2\. Fundamentação do Paradigma Orientado a Notificações (PON)
Baseado na tese de Peters (2012), o PON é definido como uma "colaboração pontual entre entidades granulares e notificantes". Diferente do paradigma imperativo, onde o fluxo de execução "pergunta" pelo estado do dado, no KAD 1.1 o dado possui a incumbência de notificar as entidades dependentes apenas quando ocorre uma alteração relevante.**Glossário Técnico KAD 1.1:**
* **Atributos:** Entidades que representam dados brutos. No KAD 1.1, são mapeados diretamente para endereços de memória. 
* **Premissas:** Unidades de teste comparativo. Realizam operações lógicas/aritméticas sobre os Atributos no instante da notificação. 
* **Condições:** Agrupadores lógicos de Premissas que definem estados complexos do sistema. 
* **Regras:** Entidades decisórias. Quando as Condições são satisfeitas, a Regra é aprovada e encaminhada para o pipeline de execução. 
* **Métodos (Instigações):** No KAD 1.1, os Métodos 

