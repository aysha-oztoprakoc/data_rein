#!/bin/bash
# ui_test_runner.sh
# Runs PON tests in a decoupled UI window, waits 10s, and publishes the result back to MQTT.

ACTION=$1
if [ -z "$ACTION" ]; then
    ACTION="reboot"
fi

# Sanitize ACTION: remove any characters that could break JSON
ACTION=$(echo "$ACTION" | tr -cd 'a-zA-Z0-9_-')

echo -e "\e[1;36m=== EXECUTANDO VALIDAÇÃO PON (KAD 1.1) ===\e[0m"

# Path to the tester (bash array to avoid word-splitting issues)
TESTER=(python3 /home/amdy/.agents/skills/pon_testing_suite/scripts/pon_tester.py)

# Targets
TARGET_DATA="/home/amdy/DATA"
TARGET_REATIVIDADE="/home/amdy/teste_reatividade_pon.py"

TESTS_PASSED=true

# Run test on DATA
"${TESTER[@]}" "$TARGET_DATA"
if [ "$?" -ne 0 ]; then
    TESTS_PASSED=false
fi

# Run test on teste_reatividade_pon.py (only if file exists)
if [ -f "$TARGET_REATIVIDADE" ]; then
    "${TESTER[@]}" "$TARGET_REATIVIDADE"
    if [ "$?" -ne 0 ]; then
        TESTS_PASSED=false
    fi
else
    echo "[AVISO] Arquivo $TARGET_REATIVIDADE não encontrado, pulando teste."
fi

echo ""
if [ "$TESTS_PASSED" = true ]; then
    echo -e "\e[1;32mTODOS OS TESTES APROVADOS.\e[0m"
else
    echo -e "\e[1;31mFALHA NOS TESTES. O BACKUP SERÁ BLOQUEADO.\e[0m"
fi

echo ""
# The 10-second timer to continue the process (PON compliant as it's just bash read, not Python blocking loop)
read -t 10 -p "O processo continuará em 10 segundos..."
echo ""

# Publish the result back to the PON engine via MQTT
# Topic: amdy/fbe/attributes/BackupConfig/at_TestsPassed
# Payload: {"passed": true|false, "action": "reboot|bak|..."}

if [ "$TESTS_PASSED" = true ]; then
    mosquitto_pub -h localhost -t "amdy/fbe/attributes/BackupConfig/at_TestsPassed" -m "{\"passed\": true, \"action\": \"$ACTION\"}"
    if [ "$?" -ne 0 ]; then
        echo -e "\e[1;33m[AVISO] Falha ao publicar no broker MQTT. Verifique se o mosquitto está rodando.\e[0m"
    fi
    # A janela do tmux fechará naturalmente ao fim do script; não é necessário sleep.
else
    mosquitto_pub -h localhost -t "amdy/fbe/attributes/BackupConfig/at_TestsPassed" -m "{\"passed\": false, \"action\": \"$ACTION\"}"
    if [ "$?" -ne 0 ]; then
        echo -e "\e[1;33m[AVISO] Falha ao publicar no broker MQTT. Verifique se o mosquitto está rodando.\e[0m"
    fi
    # Se falhou, segura a tela para o usuário ver
    read -p "Pressione ENTER para fechar esta janela..."
fi
