import json
import os
import threading
import time
import chromadb
from pathlib import Path

try:
    from paho.mqtt.client import CallbackAPIVersion
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

# Configurações de Estado PON e Graceful Degradation
graceful_degradation_event = threading.Event()
BROKER_ADDRESS = "localhost" # Amdy broker
CHROMA_DB_HOST = "tell.local"
CHROMA_DB_PORT = 8000

TRAINING_DATA_PATH = Path("/home/amdy/data_rein/training_data")

def extract_and_embed_worker(subfolder_name: str, chroma_collection):
    """
    Agente especializado que roda em Daemon Thread.
    Aplica Chunking e processamento de RAG de acordo com a regra de Graceful Degradation.
    """
    target_path = TRAINING_DATA_PATH / subfolder_name
    if not target_path.exists():
        return
        
    for filepath in target_path.rglob('*.*'):
        if filepath.is_file():
            # Ação de degradação: se o hardware estiver sob estresse, aplica chunking menos custoso.
            if graceful_degradation_event.is_set():
                chunk_size = 2000 # Menor overhead de reranking
                model_directive = "llama-3-8b-4bit"
            else:
                chunk_size = 500  # Granularidade fina, ideal para Busca Híbrida de precisão
                model_directive = "llama-3-70b-moe" # MoE pesado
            
            # Aqui ocorreria a lógica pesada em NVIDIA (LlamaParse, BGE Reranker)
            # Como placeholder (para não travar sem a biblioteca LlamaIndex):
            metadata = {
                "source": str(filepath),
                "model_directive": model_directive,
                "agent": f"{subfolder_name}_specialist"
            }
            
            try:
                # O nó Amdy orquestra a adição remota na collection que vive no nó Tell
                chroma_collection.add(
                    documents=["[CONTENT EXTRACTED & SEMANTICALLY CHUNKED]"],
                    metadatas=[metadata],
                    ids=[f"{subfolder_name}_{filepath.name}_{time.time()}"]
                )
            except Exception as e:
                pass # Em caso de falha de rede do Tell, o loop não é afetado (desacoplamento)
                
            # Semáforo implícito pela DB, removido o sleep artificial (PON idiomatic)

def on_connect(client, userdata, flags, rc, *args):
    if rc == 0:
        client.subscribe("data_rein/hardware/stress")
        client.subscribe("data_rein/sofia/trigger_ingest")
        print("Sofia Ingestor Online [Amdy]. Conectado ao PON.")

def on_message(client, userdata, msg):
    if msg.topic == "data_rein/hardware/stress":
        try:
            payload = json.loads(msg.payload.decode())
            if payload.get("vram_usage", 0) > 90:
                graceful_degradation_event.set()
                print("Hardware Stress: Graceful Degradation ATIVADO. Reduzindo complexidade MoE para 4-bit Llama.")
            else:
                graceful_degradation_event.clear()
        except:
            pass
            
    elif msg.topic == "data_rein/sofia/trigger_ingest":
        print("Sinal KAT 11 recebido. Iniciando agentes de extração em threads isoladas.")
        
        # Conexão HTTP direta com o nó Tell, garantindo a integridade dos arquivos (ChromaDB Persistente)
        try:
            chroma_client = chromadb.HttpClient(host=CHROMA_DB_HOST, port=CHROMA_DB_PORT)
            collection = chroma_client.get_or_create_collection(name="sofia_knowledge")
        except Exception:
            print("Falha ao contatar ChromaDB no nó Tell. Abortando extração (Regra de Estabilidade).")
            return
            
        # Orquestração dos Agentes Especializados baseados nas subpastas
        subfolders = ["text", "audio_transcripts", "image_descriptions", "metadata"]
        for sf in subfolders:
            t = threading.Thread(target=extract_and_embed_worker, args=(sf, collection), daemon=True)
            t.start()

def main():
    if PAHO_V2:
        client = mqtt.Client(CallbackAPIVersion.VERSION1, client_id="sofia_ingestor_amdy")
    else:
        client = mqtt.Client(client_id="sofia_ingestor_amdy")
        
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect(BROKER_ADDRESS, 1883, 300)
        client.loop_forever() # Loop bloqueante do Daemon (Uso de CPU = 0%)
    except KeyboardInterrupt:
        client.disconnect()

if __name__ == "__main__":
    main()
