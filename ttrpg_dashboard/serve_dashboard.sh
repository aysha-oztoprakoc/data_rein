#!/bin/bash
# serve_dashboard.sh
# Script para iniciar o servidor local da TTRPG Dashboard
# Obedece à arquitetura DYSKORDIA (Integração de status via MQTT)

WIKI_DIR="/home/amdy/data_rein/data-oby"
PORT=8080
BROKER="localhost"

echo "[DYSKORDIA] Inicializando o servidor local da TTRPG Dashboard na porta $PORT..."

# Notifica a rede PON que o servidor está inicializando
if command -v mosquitto_pub &> /dev/null; then
    mosquitto_pub -h "$BROKER" -t "data_rein/ttrpg_dashboard/status" -m "{\"status\": \"starting\", \"port\": $PORT}"
fi

# Verifica se o diretório existe
if [ ! -d "$WIKI_DIR" ]; then
    echo "[ERRO] Diretório da Wiki não encontrado em $WIKI_DIR"
    exit 1
fi

# Levanta um servidor Python HTTP em background
cd "$WIKI_DIR" || exit
python3 -m http.server $PORT &
SERVER_PID=$!

echo "[DYSKORDIA] Servidor rodando no PID $SERVER_PID"

if command -v mosquitto_pub &> /dev/null; then
    mosquitto_pub -h "$BROKER" -t "data_rein/ttrpg_dashboard/status" -m "{\"status\": \"online\", \"pid\": $SERVER_PID}"
fi

echo "Para derrubar o servidor, execute: kill $SERVER_PID"
wait $SERVER_PID
