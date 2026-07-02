import paho.mqtt.client as mqtt
import json

# FBE Abstraction: amdy acts as a Method node, it does NOT hold state.
# It subscribes to FBE Instigations triggered by Rules on the 'tell' server.

TELL_BROKER = "localhost" # Servidor 'tell' onde reside a Base de Atributos
FBE_INSTIGATION_TOPIC = "amdy/fbe/methods/execute"

def on_connect(client, userdata, flags, rc):
    print(f"[Amdy Node] Conectado ao servidor Tell (Broker MQTT) com código: {rc}")
    # Inscreve-se nas instigações, zero polling.
    client.subscribe(FBE_INSTIGATION_TOPIC)
    print(f"[Amdy Node] Inscrito no tópico: {FBE_INSTIGATION_TOPIC}.")
    print(f"[Amdy Node] Aguardando notificações (0% CPU - E/S Bloqueante)...")

def on_message(client, userdata, msg):
    # Desperta APENAS sob notificação (Reatividade Genuína PON)
    payload = msg.payload.decode()
    print(f"\n[Amdy Node] -> Notificação recebida em {msg.topic}")
    
    try:
        instigation = json.loads(payload)
        method_name = instigation.get("method")
        fbe_params = instigation.get("params", {})
        
        print(f"[Amdy Node] Executando Ação/Método FBE: {method_name}")
        print(f"[Amdy Node] Parâmetros da Base de Fatos: {fbe_params}")
        
        # O amdy não guarda o resultado localmente, ele altera um Atributo FBE no Tell
        result_topic = f"tell/fbe/attributes/{method_name}/status"
        result_payload = json.dumps({"status": "concluido", "node": "amdy"})
        
        print(f"[Amdy Node] Notificando Base de Atributos Tell em: {result_topic}")
        client.publish(result_topic, result_payload)
        
    except json.JSONDecodeError:
        print("[Amdy Node] Erro: Estrutura de instigação FBE inválida.")

if __name__ == "__main__":
    # O nó amdy atua exclusivamente como Nó de Execução
    client = mqtt.Client(client_id="amdy_execution_node")
    client.on_connect = on_connect
    client.on_message = on_message
    
    print("[Amdy Node] Iniciando arquitetura reativa PON...")
    try:
        client.connect(TELL_BROKER, 1883, 60)
        # loop_forever() garante bloqueio nativo via select/poll no SO. Nenhuma varredura manual é feita.
        client.loop_forever()
    except Exception as e:
        print(f"[Amdy Node] Erro de conexão com o Tell: {e}. (O broker MQTT local precisa estar rodando)")
