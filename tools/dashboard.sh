#!/bin/bash

ollama_log=$(grep -l "ollama pull" /home/amdy/.gemini/antigravity-cli/brain/6046bb2e-91d9-4407-8ffb-d1b5e87b7171/.system_generated/tasks/task-*.log | xargs ls -tr | tail -n 1)
curl_log="/home/amdy/.gemini/antigravity-cli/brain/6046bb2e-91d9-4407-8ffb-d1b5e87b7171/.system_generated/tasks/task-1763.log"

get_pids() {
    ollama_pids=$(pgrep -f "ollama serve" || true)
    curl_pids=$(pgrep -f "curl.*sd_xl_turbo|curl.*flux1-schnell" || true)
}

pause_downloads() {
    get_pids
    for pid in $ollama_pids $curl_pids; do
        if [ -n "$pid" ]; then sudo kill -STOP "$pid" 2>/dev/null; fi
    done
    paused="SIM"
}

resume_downloads() {
    get_pids
    for pid in $ollama_pids $curl_pids; do
        if [ -n "$pid" ]; then sudo kill -CONT "$pid" 2>/dev/null; fi
    done
    paused="NÃO"
}

paused="NÃO"

tput civis
trap "tput cnorm; exit" INT TERM EXIT

while true; do
    ollama_log=$(grep -l "ollama pull" /home/amdy/.gemini/antigravity-cli/brain/6046bb2e-91d9-4407-8ffb-d1b5e87b7171/.system_generated/tasks/task-*.log | xargs ls -tr | tail -n 1)
    clear
    echo -e "\e[1;36m========================================================\e[0m"
    echo -e "\e[1;36m      ⚡ DASHBOARD INTERATIVO: NOVOS MODELOS ⚡        \e[0m"
    echo -e "\e[1;36m========================================================\e[0m"
    
    if [ "$paused" == "SIM" ]; then
        echo -e "\e[1;31;5m  >>> DOWNLOADS EM PAUSA <<<\e[0m"
    else
        echo ""
    fi

    echo -e "\e[1;33m[ 1. MOTOR DE TEXTO (Ollama) ]\e[0m"
    if [ -f "$ollama_log" ]; then
        tail -c 500 "$ollama_log" 2>/dev/null | tr '\r' '\n' | grep "%" | tail -n 1 | sed 's/^pulling [a-z0-9]*:/▶ Modelo Atual:/'
    else
        echo "A aguardar início..."
    fi
    echo ""

    echo -e "\e[1;35m[ 2. MOTOR DE IMAGEM (ComfyUI / HuggingFace) ]\e[0m"
    if [ -f "$curl_log" ]; then
        latest_curl=$(tail -c 500 "$curl_log" 2>/dev/null | tr '\r' '\n' | grep -E "^ *[0-9]+" | tail -n 1)
        if [ -n "$latest_curl" ]; then
            percent=$(echo "$latest_curl" | awk '{print $1}')
            total=$(echo "$latest_curl" | awk '{print $2}')
            dl=$(echo "$latest_curl" | awk '{print $4}')
            speed=$(echo "$latest_curl" | awk '{print $8}')
            eta=$(echo "$latest_curl" | awk '{print $11}')
            echo "▶ Progresso: $percent%"
            echo "  Descarregado: $dl / $total"
            echo "  Velocidade: $speed/s"
            echo "  Tempo Restante: $eta"
        else
            echo "A preparar transferência..."
        fi
    else
        echo "A aguardar início..."
    fi
    echo ""
    echo -e "\e[1;30m--------------------------------------------------------\e[0m"
    echo -e "\e[1;32mOpções: [p] Pausar | [r] Retomar | [q] Sair do Dashboard\e[0m"
    
    if read -r -t 1 -s -n 1 input; then
        case $input in
            p|P) pause_downloads ;;
            r|R) resume_downloads ;;
            q|Q) break ;;
        esac
    fi
done

tput cnorm
echo ""
