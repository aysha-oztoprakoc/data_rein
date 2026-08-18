---
name: pon-testing-suite
description: "Executa testes de segurança, estabilidade e verificação estrita das regras do PON (Paradigma Orientado a Notificações). Obrigatório antes de qualquer push ao GitHub, backup ou grande modificação arquitetural."
tags: "security, stability, pon, testing, gate"
---

# PON Testing Suite (KAD 1.1)

Você tem à sua disposição a suíte de testes de validação PON, de segurança e de estabilidade. 
Sempre que fizer grandes modificações ou antes de enviar qualquer backup para o GitHub ou para o servidor redundante, você **DEVE** invocar o script de validação para comprovar a robustez e integridade do código.

## Como Usar
Execute o comando abaixo no terminal passando o arquivo ou diretório a ser analisado:
```bash
python3 ~/.agents/skills/pon_testing_suite/scripts/pon_tester.py <caminho_do_alvo>
```

O script executará 3 baterias de testes rigorosas:
1. **Testes de Segurança:** Busca por credenciais expostas no código (senhas, chaves privadas, tokens de API) e vulnerabilidades grosseiras.
2. **Testes de Estabilidade:** Realiza checagem de sintaxe pré-runtime e analisa possíveis travamentos, garantindo que a sintaxe seja válida antes de qualquer deploy em produção.
3. **Verificação das Regras PON:** Escaneia o código fonte em busca de antipadrões PON terminantemente proibidos, tais como:
   - `while True` ou `while 1` (Falsa Reatividade/Polling ativo) em qualquer linguagem.
   - Uso de timers síncronos de bloqueio ativo (`time.sleep` em Python ou `Sleep` em C++).
   - Garante a presença de paradigmas de I/O bloqueante passivo, `threading.Event`, callbacks, e/ou `paho-mqtt` (`loop_forever` ou assíncrono).

**DIRETRIZ DE BLOQUEIO:** Se qualquer um dos testes falhar, o processo de commit, backup ou upload **DEVE SER ABORTADO IMEDIATAMENTE**. Você deve refatorar o código, sanar as violações PON/Segurança/Estabilidade e re-executar a ferramenta até obter 100% de sucesso.
