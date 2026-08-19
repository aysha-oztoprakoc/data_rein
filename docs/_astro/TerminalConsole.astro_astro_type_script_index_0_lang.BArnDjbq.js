class s{input;history;cmdHistory=[];historyIndex=-1;constructor(){this.input=document.getElementById("term-input"),this.history=document.getElementById("term-history"),this.init()}init(){if(!this.input||!this.history)return;const e=document.querySelectorAll(".quick-cmd-btn");this.input.addEventListener("keydown",t=>{if(t.key==="Enter"){const i=this.input.value.trim();i&&(this.execute(i),this.cmdHistory.push(i),this.historyIndex=this.cmdHistory.length,this.input.value="")}}),e.forEach(t=>{t.addEventListener("click",()=>{const i=t.getAttribute("data-cmd");i&&this.input&&(this.input.value=i,this.execute(i))})}),this.print(`// data_rein Universal Agent Harness Console [v0.2.0]
// PON Protocol Active | Node: amdy (Execution) | tell: linked (Fact Base)
// Type 'help' or click quick command buttons above to test system routines.
`)}execute(e){this.print(`<span style="color: var(--color-text-highlight); font-weight: 700;">amdy@data_rein:~$</span> ${e}`);const t=e.toLowerCase().trim();if(t==="help")this.print(`AVAILABLE HARNESS COMMANDS:
  reins run <cat> <prompt>    - Dispatch prompt to local Ollama / Kùzu RAG
  reins wiki search <query>   - Full-text BM25 & graph neighborhood search
  reins tokens status         - Rolling token consumption & budget metrics
  reins qc eval               - Run Radon cyclomatic complexity & coverage ratchet
  reins cluster probe         - Handshake ping amdy (192.168.0.3) <-> tell (192.168.0.4)
  reins paths                 - Print canonical harness system paths
  clear                       - Clear terminal buffer`);else if(t.startsWith("reins run"))this.print(`[0.01s] [FBE:TASK_CREATED] ModelRouter selected tier: LOCAL (Ollama / Qwen2.5-Coder-7B)
[0.04s] [ContextBuilder] Kùzu graph query returned 2 related wiki nodes (sim=0.94)
[0.08s] [amdy:RX 9060 XT] Executing with 8GB VRAM allocation...
[0.19s] [ValidatorNode] Judge (Archimedes & Sofia) passed with score 0.98.
<span style="color: #00FF66;">[OK] Execution complete in 210ms. Response grounded in Fact Base.</span>`);else if(t.startsWith("reins wiki"))this.print(`[WikiDB] Querying Kùzu Graph & ChromaDB Vector Embeddings...
  1. [PAGE] PRIME_DIRECTIVE.md (rank: 0.982) - PON architecture & zero polling laws
  2. [MEMORY] KAD 1.1 Cluster State (rank: 0.941) - amdy (methods) / tell (facts)
  3. [CHUNK] ModelCoordinator LRU (rank: 0.915) - Entropy eviction heuristics
<span style="color: #00FFFF;">[3 results found in 4.2ms]</span>`);else if(t.startsWith("reins tokens"))this.print(`[TOKEN USAGE TRACKER] Rolling Window Consumption vs Hard Budgets:
  5-Hour Window:  [████░░░░░░░░░░░░░░░░]  21.4% (107k / 500k tokens)
  24-Hour Day:    [████████░░░░░░░░░░░░]  40.2% (804k / 2.0M tokens)
  30-Day Month:   [███░░░░░░░░░░░░░░░░░]  16.8% (8.4M / 50.0M tokens)
<span style="color: #00FF66;">[STATUS: GREEN] All operations operating strictly within budget ceilings.</span>`);else if(t.startsWith("reins qc"))this.print(`[QC META-HARNESS] Analyzing recent commit changeset...
  * Radon Cyclomatic Max: 4 (Hotspot ceiling: 20) -> PASS
  * Pytest-Cov Differential: +3.2% (Regressions: 0) -> PASS
  * Risk Score: LOW (Formatting & Utility Layer) -> PASS
<span style="color: #00FF66;">[RECOMMENDATION: AUTO_MERGE] Autonomous merge authorized.</span>`);else if(t.startsWith("reins cluster")||t.startsWith("reins probe"))this.print(`[MESH DIAGNOSTIC] Initiating cross-node UDP/MQTT handshake...
  [NODE: amdy] 192.168.0.3 (Stateless Methods Node) -> 0.0% CPU Idle | ONLINE
  [NODE: tell] 192.168.0.4 (NixOS Central Fact Base) -> MQTT v2 Port 1883 | ONLINE
  [CUDA PLANE] NVIDIA GTX 1060 6GB (Ollama JIT) -> Port 11434 | ONLINE
<span style="color: #00FF66;">[MESH INTEGRITY: 100%] Sub-millisecond reactive bus confirmed.</span>`);else if(t.startsWith("reins paths"))this.print(`[CANONICAL PATHS]
  HARNESS_ROOT: /home/amdy/data_rein
  WIKI_DB:      /home/amdy/data_rein/knowledge_base/wiki.db
  KUZU_GRAPH:   /home/amdy/data_rein/DATA/kuzu_db
  TASK_TRAIL:   /home/amdy/data_rein/knowledge_base/task_trail.json
  SKILLS_DIR:   /home/amdy/data_rein/skills`);else if(t==="clear"){this.history&&(this.history.innerHTML="");return}else this.print(`<span style="color: var(--color-danger);">[COMMAND UNRECOGNIZED: '${e}'] Type 'help' for command manual.</span>`);this.history&&(this.history.scrollTop=this.history.scrollHeight)}print(e){this.history&&(this.history.innerHTML+=`<div style="margin-bottom: 0.4rem;">${e}</div>`,this.history.scrollTop=this.history.scrollHeight)}}document.addEventListener("DOMContentLoaded",()=>{new s});
