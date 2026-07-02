# A Bíblia do Projeto Sofia: Manual de Reconstrução Mestre

Este documento (KAD 1.1) é a diretriz mestre inalterável para a orquestração do ecossistema de dados distribuídos. A arquitetura obedece rigorosamente ao **Paradigma Orientado a Notificações (PON)**.

## 1. Diretiva de Execução: Graceful Degradation (Degradação Graciosa)
A integridade da inteligência nunca deve cessar, mesmo mediante exaustão de hardware (RAM/VRAM no nó `Amdy` ou quebra de cluster no `Tell`). 
Se o sistema detectar carga excessiva via MQTT (`data_rein/hardware/stress`), os agentes mudarão instantaneamente o modelo orquestrador de uma arquitetura pesada (*Mixture of Experts* / 70B) para um modelo quantizado local de sobrevivência (Llama 3 8B 4-bit) usando chunking em modo *low-overhead*.

## 2. Topologia de Extração RAG (Amdy -> Tell)
### Nó Amdy (NVIDIA GPU / Computação):
Hospeda o `sofia_ingestor.py`. Quatro agentes *daemon threads* são despachados para analisar os dados brutos:
- `Agent Text`: Faz o chunking semântico respeitando a taxonomia Markdown e executa a busca híbrida (BM25 + Vector).
- `Agent Audio`: Usa inferência otimizada local (como *Whisper*) na NVIDIA GPU para compilar logs transcritos.
- `Agent Vision`: Executa LLaVA (quantizado) para descrever imagens e extrair intenção.
- `Agent Metadata`: Extrai tabelas hash e cronologia, blindando a integridade original dos arquivos.

### Nó Tell (Memória Mestre / ChromaDB):
As *threads* no `Amdy` jamais guardam estado (cumprindo a Lei do PON). Cada embedding vetorial mastigado na placa de vídeo do `Amdy` é disparado em rede para o `Tell`, onde o **ChromaDB** os abriga permanentemente na coleção `sofia_knowledge`.

## 3. Orquestração de Acesso (KAT 11)
A orquestração não tolera loops infinitos. Os prompts de cada agente são governados pela hierarquia KAT 11 (Know-All-Topology 11).

### System Prompt Padronizado dos Agentes:
> "Você é uma entidade passiva operando sob o Protocolo Sofia (Acesso KAT 11). Sua diretiva principal é a extração cirúrgica dos Fatos Baseados em Elementos (FBEs) contidos no payload da notificação. Respeite os limites do Graceful Degradation; se o estado apontar `Degraded`, resuma o dado usando chunking genérico e abstenha-se de inferências elaboradas (como re-ranking BGE pesado). O destino final das suas deduções é unicamente a base de dados do nó Tell."
