#!/usr/bin/env bash

# PON Compliant Monitor: Utiliza E/S bloqueante (tail -f) sobre SSH. 
# Sem laços de varredura ativa.

echo "============================================================"
echo "    [ TELL NODE ] - NixOS Infection Progress Monitor        "
echo "============================================================"
echo "Conectando ao nó remoto (192.168.0.2) via SSH..."
echo "Aguardando fluxo de dados do log de infecção..."
echo "------------------------------------------------------------"

# E/S bloqueante: a conexão SSH será mantida aberta e o tail -f enviará 
# os dados de forma reativa assim que forem escritos no disco remoto.
ssh -o BatchMode=yes -o ServerAliveInterval=10 -o ServerAliveCountMax=3 tell@192.168.0.2 'tail -f /tmp/nixos_infect.log'

SSH_EXIT_CODE=$?

echo "------------------------------------------------------------"
if [ $SSH_EXIT_CODE -eq 255 ]; then
    echo "[!] A conexão SSH foi encerrada."
    echo "[*] O nó 'tell' iniciou a transmutação final (kexec) e está reiniciando!"
    echo "[*] Aguarde alguns minutos. O sistema retornará como NixOS."
else
    echo "[!] O monitoramento foi interrompido (Código: $SSH_EXIT_CODE)."
fi
echo "============================================================"
