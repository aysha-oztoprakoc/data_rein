### Bíblia Arquitetural: Projeto Sovereign e Paradigma Orientado a Notificações (PON)
Este documento estabelece as diretrizes canônicas e as normas técnicas para o desenvolvimento do Projeto Sovereign. Como Arquiteto de Sistemas Sênior, exijo o cumprimento rigoroso destas definições para garantir a transição da computação passiva (polling) para a colaboração reativa acelerada em hardware.
#### 1\. Visão Geral e Escopo do Projeto Sovereign
O Projeto Sovereign redefine a eficiência computacional em sistemas críticos, operando em duas fases estratégicas que convergem na eliminação do processamento redundante:
* **Fase 1: RPG C++ IoT:** Desenvolvimento de sistemas embarcados de alta performance em C++. O foco reside na aplicação do PON para o gerenciamento de estados granulares e interações complexas entre sensores e entidades, eliminando ciclos de CPU gastos em verificações de estado inalterado. 
* **Fase 2: RAG Dinâmico para LLM Local:** Implementação de Geração Aumentada por Recuperação (RAG) reativa. A arquitetura utiliza as "Notificações de Atributo" como gatilhos determinísticos para a re-indexação de vetores de contexto. **É terminantemente proibido o polling em bases de dados vetoriais** ; a busca de contexto deve ser instanciada apenas quando a base de conhecimento notifica uma alteração real em seus atributos.
#### 2\. Fundamentos Técnicos do PON (Estado da Arte)
O Paradigma Orientado a Notificações (PON) não é apenas um modelo de eventos, mas uma filosofia de influência causal:"A essência do PON constitui-se em uma nova forma de influência causal baseada na colaboração pontual entre entidades granulares e notificantes." (Peters, 2012\)
##### Vantagens Arquiteturais
* **Eliminação do Polling:** Fim do desperdício de processamento em expressões causais (se-então) que consultam dados passivos. 
* **União Paradigmática:** Integra as vantagens da programação baseada em eventos com a clareza da programação declarativa. 
* **Mimetismo Cognitivo:** Representação do c

