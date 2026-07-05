#!/usr/bin/env python3
import os
import sys
import re
import ast

def scan_file(filepath):
    results = {
        "security": [],
        "stability": [],
        "pon_rules": []
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            content = "".join(lines)
    except Exception as e:
        results["stability"].append(f"Erro ao abrir arquivo: {e}")
        return results
    
    # 1. SECURITY TESTS
    forbidden_security_patterns = [
        (r'aws_access_key_id\s*=\s*[\'"][A-Z0-9]{20}[\'"]', "Chave AWS exposta encontrada."),
        (r'github_token\s*=\s*[\'"][A-Za-z0-9_]{40}[\'"]', "GitHub Token exposto encontrado."),
        (r'(?i)password\s*=\s*[\'"][^\'"]+[\'"]', "Possível senha hardcoded encontrada.")
    ]
    
    for i, line in enumerate(lines):
        for pattern, msg in forbidden_security_patterns:
            if re.search(pattern, line):
                results["security"].append(f"Linha {i+1}: {msg}")

    # 2. STABILITY TESTS
    if filepath.endswith(".py"):
        try:
            ast.parse(content)
        except SyntaxError as e:
            results["stability"].append(f"Erro de Sintaxe Python: {e}")

    # 3. PON RULES VERIFICATION
    pon_violations = [
        (r'while\s+True\s*:', "Uso de 'while True' detectado. Violência direta da Falsa Reatividade PON (Polling Ativo)."),
        (r'while\s+1\s*:', "Uso de 'while 1' detectado. Violência da Falsa Reatividade PON."),
        (r'time\.sleep\(', "Uso de temporizador de bloqueio ativo (sleep síncrono) detectado. Proibido no PON.")
    ]
    
    for i, line in enumerate(lines):
        for pattern, msg in pon_violations:
            if re.search(pattern, line):
                results["pon_rules"].append(f"Linha {i+1}: {msg}")
                
    # `paho.mqtt.publish.single()/multiple()` is a one-shot fire-and-forget publish -
    # it connects, publishes, and disconnects internally with no persistent loop to
    # drive, so it is not held to the loop_forever()/loop_start() requirement below.
    uses_persistent_client = "mqtt.Client(" in content or re.search(r'\bClient\s*\(', content)
    if "paho.mqtt" in content and uses_persistent_client and "loop_forever()" not in content and "loop_start()" not in content:
         results["pon_rules"].append("Arquivo importa paho.mqtt mas não utiliza loop_forever() ou loop_start() adequadamente para E/S Bloqueante.")

    return results

def run_tests(target_path):
    all_files = []
    if os.path.isfile(target_path):
        all_files.append(target_path)
    elif os.path.isdir(target_path):
        for root, dirs, files in os.walk(target_path):
            # Ignora pastas de ambiente virtual, cache, repositório local e third-party/legacy
            dirs[:] = [d for d in dirs if d not in ['.git', 'venv', '.venv', '__pycache__', 'node_modules', '.cache', 'ComfyUI', 'comfyui', 'odysseus']]
            for file in files:
                if file.endswith((".py", ".sh", ".bash", ".js", ".c", ".cpp")):
                    all_files.append(os.path.join(root, file))
    
    total_errors = 0
    
    print(f"=== INICIANDO SUÍTE DE TESTES PON (KAD 1.1) ===")
    print(f"Alvo: {target_path}\n")
    
    for file in all_files:
        res = scan_file(file)
        file_errors = len(res["security"]) + len(res["stability"]) + len(res["pon_rules"])
        
        if file_errors > 0:
            print(f"❌ FALHA no arquivo: {file}")
            if res["security"]:
                print("  [TESTE DE SEGURANÇA]")
                for e in res["security"]: print(f"    -> {e}")
            if res["stability"]:
                print("  [TESTE DE ESTABILIDADE]")
                for e in res["stability"]: print(f"    -> {e}")
            if res["pon_rules"]:
                print("  [VERIFICAÇÃO DE REGRAS PON]")
                for e in res["pon_rules"]: print(f"    -> {e}")
            print("")
            total_errors += file_errors
        else:
            print(f"✅ PASSED: {file}")

    print("===============================================")
    if total_errors == 0:
        print("RESULTADO FINAL: ✅ APROVADO! O código atende à diretriz PON.")
        print("Você está autorizado a prosseguir com o push ao GitHub ou gerar o backup.")
        sys.exit(0)
    else:
        print(f"RESULTADO FINAL: ❌ REPROVADO! Foram encontradas {total_errors} violações.")
        print("BLOQUEIO ATIVADO: Não faça deploy, push ou backup. Corrija o código imediatamente e re-execute a suíte.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 pon_tester.py <caminho_do_arquivo_ou_diretorio>")
        sys.exit(1)
    run_tests(sys.argv[1])
