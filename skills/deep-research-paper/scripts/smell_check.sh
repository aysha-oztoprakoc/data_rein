#!/usr/bin/env bash
# smell_check.sh — Machine-executable LLM writing smell detector
#
# Scans markdown files for banned academic-writing anti-patterns:
# flowery adjectives, absolute claims, and marketing language.
#
# Usage:
#   bash skills/deep-research-paper/scripts/smell_check.sh scratch/chunks/*.md
#   bash skills/deep-research-paper/scripts/smell_check.sh merged_paper.md
#
# Exit codes:
#   0 — no smells found
#   1 — smells detected (count printed)
#   2 — no files given

set -euo pipefail

if [ $# -eq 0 ]; then
    echo "Usage: $0 <file1.md> [file2.md ...]" >&2
    exit 2
fi

# Banned words/phrases from the deep-research-paper skill.
# Case-insensitive, word-boundary-aware where practical.
BANNED='seamless|elegant|vivid|colossal|masterpiece|violently|undeniably|crucially|paradigm.shifting|groundbreaking|exhaustive|comprehensive|incontrovertible|inherently resolves'

# Additional overclaim patterns found in previous audits.
OVERCLAIM='zero cpu|zero.memory.leak|proves? incontrovertib|absolute(ly)?|resolves? inerente|integra[çc][ãa]o perfeita|sem falhas'

# Humanities LLM jargon and cliché metaphors (Portuguese).
HUMANITIES='intrincad[oa]s?|multifacetad[oa]s?|lançar luz|tecer( reflexões| considerações)?|mergulho profundo|divisor de águas|mosaico( social| cultural| histórico)?|teia( social| de relações)?|inegavelmente|ponto de virada|nuances?|olhar atento|desvendar'

total=0
for f in "$@"; do
    if [ ! -f "$f" ]; then
        echo "WARN: $f not found, skipping" >&2
        continue
    fi

    count_banned=$(grep -ciE "$BANNED" "$f" 2>/dev/null || true)
    count_overclaim=$(grep -ciE "$OVERCLAIM" "$f" 2>/dev/null || true)
    count_humanities=$(grep -ciE "$HUMANITIES" "$f" 2>/dev/null || true)
    file_total=$((count_banned + count_overclaim + count_humanities))

    if [ "$file_total" -gt 0 ]; then
        echo "// $f — $file_total smell(s):"
        grep -inE "$BANNED" "$f" 2>/dev/null | sed 's/^/  [banned]      /' || true
        grep -inE "$OVERCLAIM" "$f" 2>/dev/null | sed 's/^/  [overclaim]   /' || true
        grep -inE "$HUMANITIES" "$f" 2>/dev/null | sed 's/^/  [humanities]  /' || true
        echo
    fi
    total=$((total + file_total))
done

if [ "$total" -eq 0 ]; then
    echo "// clean — 0 LLM writing smells detected"
    exit 0
else
    echo "// TOTAL: $total smell(s) across $# file(s)"
    exit 1
fi
