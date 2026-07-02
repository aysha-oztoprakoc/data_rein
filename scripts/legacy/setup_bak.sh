#!/bin/bash
set -euo pipefail

# Setup Git repository
cd "/home/amdy/DATA/BAK 1.0"
if [ ! -d .git ]; then
    git init
fi
git add pon_bak_system.py method_generate_docs.py ui_test_runner.sh setup_bak.sh

# Generate PDF document
python3 method_generate_docs.py
if [ -f "SISTEMA BAK 1.0.pdf" ]; then
    git add "SISTEMA BAK 1.0.md" "SISTEMA BAK 1.0.pdf"
fi

git commit -m "Initial commit: SISTEMA BAK 1.0 PON Architecture" || true

# Add aliases to .bashrc
BASHRC="/home/amdy/.bashrc"
if ! grep -q "SISTEMA BAK 1.0 (PON) Aliases" "$BASHRC"; then
    echo "" >> "$BASHRC"
    echo "# SISTEMA BAK 1.0 (PON) Aliases" >> "$BASHRC"
    # Proper quoting without literal backslashes in JSON
    echo 'pon_reboot() { mosquitto_pub -h localhost -t "amdy/fbe/attributes/PowerManager/at_ShutdownRequested" -m "{\"action\":\"reboot\"}" || /usr/bin/sudo /usr/sbin/reboot; }' >> "$BASHRC"
    echo 'alias reboot=pon_reboot' >> "$BASHRC"
    
    echo 'pon_shutdown() { mosquitto_pub -h localhost -t "amdy/fbe/attributes/PowerManager/at_ShutdownRequested" -m "{\"action\":\"shutdown\"}" || /usr/bin/sudo /usr/sbin/shutdown -h now; }' >> "$BASHRC"
    echo 'alias shutdown=pon_shutdown' >> "$BASHRC"
    
    echo 'pon_poweroff() { mosquitto_pub -h localhost -t "amdy/fbe/attributes/PowerManager/at_ShutdownRequested" -m "{\"action\":\"poweroff\"}" || /usr/bin/sudo /usr/sbin/poweroff; }' >> "$BASHRC"
    echo 'alias poweroff=pon_poweroff' >> "$BASHRC"

    echo "" >> "$BASHRC"
    echo "bak() {" >> "$BASHRC"
    echo '    if [ "$1" = "restore" ]; then' >> "$BASHRC"
    echo '        mosquitto_pub -h localhost -t "amdy/fbe/attributes/PowerManager/at_ShutdownRequested" -m "{\"action\":\"bak_restore\"}"' >> "$BASHRC"
    echo '    else' >> "$BASHRC"
    echo '        mosquitto_pub -h localhost -t "amdy/fbe/attributes/PowerManager/at_ShutdownRequested" -m "{\"action\":\"bak\"}"' >> "$BASHRC"
    echo '    fi' >> "$BASHRC"
    echo "}" >> "$BASHRC"
    echo "Added aliases to .bashrc"
fi
