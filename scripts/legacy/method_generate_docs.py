#!/usr/bin/env python3
import os
import subprocess

MD_CONTENT = """# SISTEMA BAK 1.0 (PON)

## Introdução
O **SISTEMA BAK 1.0** é um motor de backup e validação reativo construído estritamente sob o Paradigma Orientado a Notificações (PON). O sistema não possui *polling* (0% ciclos vazios de CPU) e garante que o hospedeiro (amdy) sincronize suas mudanças com a entidade redundante remota (tell) via publicações e inscrições no protocolo MQTT.

## Arquitetura Causal (PON FBE)
O fluxo causal substitui scripts imperativos pela seguinte sequência de eventos lógicos:
1. **Ativação:** Os aliases do terminal publicam uma mensagem no tópico MQTT `amdy/fbe/attributes/PowerManager/at_ShutdownRequested`. Eles agem modificando um atributo.
2. **Reação a Eventos (Rules):** A notificação de alteração é ouvida passivamente (E/S bloqueante) pela máquina `pon_bak_system.py`. A Rule `rl_RunTests` é notificada.
3. **Instigação:** `rl_RunTests` dispara os métodos (`Method_RunTestSuite`) que testam a integridade. O método atualiza outro atributo: `at_TestsPassed`.
4. **Desfecho:** 
   - Se os testes passarem (`rl_AllowShutdown`), o GitHub é atualizado, a entidade redundante `tell` é notificada via MQTT para auto-atualizar, e a ação final é executada.
   - Se os testes falharem (`rl_PreventShutdown`), o desligamento/reboot é impedido, um backup failsafe é gerado localmente, e o painel `tmux` alerta o erro.

## Comandos (Aliases) Integrados
Estes comandos substituem as chamadas do sistema originais:
- `reboot` : Instiga processo de validação PON, enviando ao GitHub/tell e reiniciando, caso aprovado.
- `shutdown` : Mesmo fluxo de reboot, para desligar.
- `poweroff` : Mesmo fluxo de reboot, para desligar.
- `bak` : Força backup sem desligamento.
- `bak restore` : (via function) Força recuperação passiva se necessário.

## Organização Distribuída
- **amdy (Hospedeiro Primário):** Contém os aliases de escuta e roda o motor PON FBE em background.
- **tell (Redundante via Rede):** Atua como Proxy Remoto. Subscreve ao tópico `tell/fbe/attributes/BackupState/sync`. Assim que o push é feito pelo amdy, o tell recebe notificação passiva para puxar (`git pull`) sem consultar o servidor a todo momento.
"""

def create_fallback_pdf(path):
    # Generates a minimal valid PDF file with a text message
    
    stream_content = b"BT\n/F1 12 Tf\n30 700 Td\n(SISTEMA BAK 1.0 (PON) Documentacao.) Tj\n0 -20 Td\n(Por favor, leia o arquivo 'SISTEMA BAK 1.0.md' para visualizar o manual completo.) Tj\nET\n"
    stream_len = len(stream_content)
    
    objects = []
    
    # Obj 1: Catalog
    objects.append(b"<< /Type /Catalog\n/Outlines 2 0 R\n/Pages 3 0 R\n>>")
    # Obj 2: Outlines
    objects.append(b"<< /Type /Outlines\n/Count 0\n>>")
    # Obj 3: Pages
    objects.append(b"<< /Type /Pages\n/Kids [4 0 R]\n/Count 1\n>>")
    # Obj 4: Page
    objects.append(b"<< /Type /Page\n/Parent 3 0 R\n/MediaBox [0 0 612 792]\n/Contents 5 0 R\n/Resources << /ProcSet 6 0 R\n/Font << /F1 7 0 R >>\n>>\n>>")
    # Obj 5: Contents (stream)
    objects.append(b"<< /Length " + str(stream_len).encode() + b" >>\nstream\n" + stream_content + b"endstream")
    # Obj 6: ProcSet
    objects.append(b"[/PDF /Text]")
    # Obj 7: Font
    objects.append(b"<< /Type /Font\n/Subtype /Type1\n/Name /F1\n/BaseFont /Helvetica\n/Encoding /MacRomanEncoding\n>>")
    
    pdf = bytearray()
    pdf.extend(b"%PDF-1.1\n")
    pdf.extend(b"%\xa7\xa3\xaa\xa9\n") # Proper binary comment marker
    
    offsets = [0]
    
    for i, obj in enumerate(objects):
        offsets.append(len(pdf))
        pdf.extend(f"{i+1} 0 obj\n".encode())
        pdf.extend(obj)
        pdf.extend(b"\nendobj\n")
        
    startxref = len(pdf)
    pdf.extend(b"xref\n")
    pdf.extend(f"0 {len(objects)+1}\n".encode())
    pdf.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        pdf.extend(f"{offset:010d} 00000 n \n".encode())
        
    pdf.extend(b"trailer\n")
    pdf.extend(f"<< /Size {len(objects)+1}\n/Root 1 0 R\n>>\n".encode())
    pdf.extend(b"startxref\n")
    pdf.extend(f"{startxref}\n".encode())
    pdf.extend(b"%%EOF\n")
    
    with open(path, "wb") as f:
        f.write(pdf)

def generate_docs():
    md_path = "/home/amdy/DATA/BAK 1.0/SISTEMA BAK 1.0.md"
    pdf_path = "/home/amdy/DATA/BAK 1.0/SISTEMA BAK 1.0.pdf"
    
    with open(md_path, "w") as f:
        f.write(MD_CONTENT)
        
    print(f"[Method GenerateDocs] Markdown escrito em {md_path}. Iniciando conversão para PDF...")
    try:
        subprocess.run(["pandoc", md_path, "-o", pdf_path], check=True)
        print(f"[Method GenerateDocs] PDF gerado com sucesso via pandoc em {pdf_path}.")
    except Exception as e:
        print(f"[Method GenerateDocs] Falha ao usar pandoc (dependencias ausentes). Criando PDF de fallback nativo...")
        create_fallback_pdf(pdf_path)
        print(f"[Method GenerateDocs] PDF de fallback criado em {pdf_path}.")

if __name__ == "__main__":
    generate_docs()
