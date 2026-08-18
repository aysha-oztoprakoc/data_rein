/**
 * data_rein — Cyberpunk 2077 Netrunner Deck & Audio HUD Engine
 */

class CyberpunkHUD {
  constructor() {
    this.audioEnabled = true;
    this.scanlinesEnabled = true;
    this.audioCtx = null;
    this.cmdHistory = [];
    this.historyIndex = -1;
    
    this.initAudio();
    this.initControls();
    this.initTerminal();
    this.initQCRatchet();
    this.initClusterProbe();
  }

  initAudio() {
    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) {
        this.audioCtx = new AudioContext();
      }
    } catch (e) {
      console.warn("Web Audio API not supported", e);
    }
  }

  playSound(type = 'click') {
    if (!this.audioEnabled || !this.audioCtx) return;
    
    if (this.audioCtx.state === 'suspended') {
      this.audioCtx.resume();
    }

    const osc = this.audioCtx.createOscillator();
    const gain = this.audioCtx.createGain();
    const now = this.audioCtx.currentTime;

    if (type === 'keystroke') {
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(800, now);
      osc.frequency.exponentialRampToValueAtTime(300, now + 0.03);
      gain.gain.setValueAtTime(0.04, now);
      gain.gain.linearRampToValueAtTime(0.001, now + 0.03);
      osc.connect(gain);
      gain.connect(this.audioCtx.destination);
      osc.start(now);
      osc.stop(now + 0.03);
    } else if (type === 'execute') {
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(440, now);
      osc.frequency.exponentialRampToValueAtTime(880, now + 0.08);
      gain.gain.setValueAtTime(0.06, now);
      gain.gain.linearRampToValueAtTime(0.001, now + 0.08);
      osc.connect(gain);
      gain.connect(this.audioCtx.destination);
      osc.start(now);
      osc.stop(now + 0.08);
    } else if (type === 'success') {
      osc.type = 'sine';
      osc.frequency.setValueAtTime(587.33, now); // D5
      osc.frequency.setValueAtTime(880, now + 0.06);   // A5
      gain.gain.setValueAtTime(0.08, now);
      gain.gain.linearRampToValueAtTime(0.001, now + 0.16);
      osc.connect(gain);
      gain.connect(this.audioCtx.destination);
      osc.start(now);
      osc.stop(now + 0.16);
    } else if (type === 'warn') {
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(220, now);
      osc.frequency.setValueAtTime(180, now + 0.1);
      gain.gain.setValueAtTime(0.1, now);
      gain.gain.linearRampToValueAtTime(0.001, now + 0.2);
      osc.connect(gain);
      gain.connect(this.audioCtx.destination);
      osc.start(now);
      osc.stop(now + 0.2);
    }
  }

  initControls() {
    const audioBtn = document.getElementById('btn-toggle-audio');
    const scanlinesBtn = document.getElementById('btn-toggle-scanlines');

    if (audioBtn) {
      audioBtn.addEventListener('click', () => {
        this.audioEnabled = !this.audioEnabled;
        audioBtn.classList.toggle('active', this.audioEnabled);
        audioBtn.textContent = this.audioEnabled ? '🔊 AUDIO: ON' : '🔇 AUDIO: MUTED';
        if (this.audioEnabled) this.playSound('execute');
      });
    }

    if (scanlinesBtn) {
      scanlinesBtn.addEventListener('click', () => {
        this.scanlinesEnabled = !this.scanlinesEnabled;
        document.body.classList.toggle('scanlines', this.scanlinesEnabled);
        scanlinesBtn.classList.toggle('active', this.scanlinesEnabled);
        scanlinesBtn.textContent = this.scanlinesEnabled ? '📺 CRT: ON' : '📺 CRT: OFF';
        this.playSound('click');
      });
    }
  }

  initTerminal() {
    const input = document.getElementById('term-input');
    const history = document.getElementById('term-history');
    const quickBtns = document.querySelectorAll('.quick-cmd-btn');

    if (!input || !history) return;

    input.addEventListener('keydown', (e) => {
      this.playSound('keystroke');
      if (e.key === 'Enter') {
        const rawCmd = input.value.trim();
        if (rawCmd) {
          this.executeCommand(rawCmd);
          this.cmdHistory.push(rawCmd);
          this.historyIndex = this.cmdHistory.length;
          input.value = '';
        }
      }
    });

    quickBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const cmd = btn.getAttribute('data-cmd');
        if (cmd) {
          input.value = cmd;
          this.executeCommand(cmd);
          this.playSound('execute');
        }
      });
    });

    // Initial boot print
    this.printToTerm(`// CYBERPUNK 2077 NETRUNNER TERMINAL DECK [data_rein v0.2.0]
// PON PROTOCOL KAD 1.1: ZERO POLLING ACTIVE | NODE AMDY LINKED
// Type 'help' or click quick commands above to initiate cyber-deck routines.\n`);
  }

  executeCommand(cmd) {
    const history = document.getElementById('term-history');
    this.printToTerm(`<span style="color: #fcee09;">netrunner@amdy:~$</span> ${cmd}`);
    this.playSound('execute');

    const clean = cmd.toLowerCase().trim();

    if (clean === 'help') {
      this.printToTerm(`AVAILABLE HARNESS CYBER-ROUTINES:
  reins run <cat> <prompt>    - Dispatch prompt to local Ollama / Kùzu RAG
  reins wiki search <query>   - Full-text BM25 & graph neighborhood search
  reins tokens status         - Rolling token consumption & budget metrics
  reins qc eval               - Run Radon cyclomatic complexity & coverage ratchet
  reins cluster probe         - Handshake ping amdy (192.168.0.3) <-> tell (192.168.0.4)
  reins paths                 - Print canonical harness system paths
  clear                       - Clear terminal buffer`);
    } else if (clean.startsWith('reins run')) {
      this.printToTerm(`[0.01s] [FBE:TASK_CREATED] ModelRouter selected tier: LOCAL (Ollama / Qwen2.5-Coder-7B)
[0.04s] [ContextBuilder] Kùzu graph query returned 2 related wiki nodes (sim=0.94)
[0.08s] [amdy:RX 9060 XT] Executing with 8GB VRAM allocation...
[0.19s] [ValidatorNode] Judge (Archimedes & Sofia) passed with score 0.98.
<span style="color: #00ff66;">[OK] Execution complete in 210ms. Response grounded in Fact Base.</span>`);
      this.playSound('success');
    } else if (clean.startsWith('reins wiki')) {
      this.printToTerm(`[WikiDB] Querying SQLite FTS5 index & Kùzu ContextGraph...
  1. [PAGE] PRIME_DIRECTIVE.md (rank: 0.982) - PON architecture & zero polling laws
  2. [MEMORY] KAD 1.1 Cluster State (rank: 0.941) - amdy (methods) / tell (facts)
  3. [CHUNK] ModelCoordinator LRU (rank: 0.915) - Entropy eviction heuristics
<span style="color: #00ffff;">[3 results found in 4.2ms]</span>`);
      this.playSound('success');
    } else if (clean.startsWith('reins tokens')) {
      this.printToTerm(`[TOKEN USAGE TRACKER] Rolling Window Consumption vs Hard Budgets:
  5-Hour Window:  [████░░░░░░░░░░░░░░░░]  21.4% (107k / 500k tokens)
  24-Hour Day:    [████████░░░░░░░░░░░░]  40.2% (804k / 2.0M tokens)
  30-Day Month:   [███░░░░░░░░░░░░░░░░░]  16.8% (8.4M / 50.0M tokens)
<span style="color: #00ff66;">[STATUS: GREEN] All operations operating strictly within budget ceilings.</span>`);
      this.playSound('success');
    } else if (clean.startsWith('reins qc')) {
      this.printToTerm(`[QC META-HARNESS] Analyzing recent commit changeset...
  * Radon Cyclomatic Max: 4 (Hotspot ceiling: 20) -> PASS
  * Pytest-Cov Differential: +3.2% (Regressions: 0) -> PASS
  * Risk Score: LOW (Formatting & Utility Layer) -> PASS
<span style="color: #fcee09;">[RATCRAFT RECOMMENDATION: AUTO_MERGE] Autonomous merge authorized.</span>`);
      this.playSound('success');
    } else if (clean.startsWith('reins cluster') || clean.startsWith('reins probe')) {
      this.printToTerm(`[MESH DIAGNOSTIC] Initiating cross-node UDP/MQTT handshake...
  [NODE: amdy] 192.168.0.3 (Stateless Methods Node) -> 0.0% CPU Idle | ONLINE
  [NODE: tell] 192.168.0.4 (NixOS Central Fact Base) -> MQTT v2 Port 1883 | ONLINE
  [CUDA PLANE] NVIDIA GTX 1060 6GB (Ollama JIT) -> Port 11434 | ONLINE
<span style="color: #00ff66;">[MESH INTEGRITY: 100%] Sub-millisecond reactive bus confirmed.</span>`);
      this.playSound('success');
    } else if (clean.startsWith('reins paths')) {
      this.printToTerm(`[CANONICAL PATHS]
  HARNESS_ROOT: /home/amdy/data_rein
  WIKI_DB:      /home/amdy/data_rein/knowledge_base/wiki.db
  KUZU_GRAPH:   /home/amdy/data_rein/DATA/kuzu_db
  TASK_TRAIL:   /home/amdy/data_rein/knowledge_base/task_trail.json
  SKILLS_DIR:   /home/amdy/data_rein/skills`);
    } else if (clean === 'clear') {
      history.innerHTML = '';
      return;
    } else {
      this.printToTerm(`<span style="color: #ff003c;">[COMMAND UNRECOGNIZED: '${cmd}'] Type 'help' for command manual.</span>`);
      this.playSound('warn');
    }

    history.scrollTop = history.scrollHeight;
  }

  printToTerm(html) {
    const history = document.getElementById('term-history');
    if (history) {
      history.innerHTML += `<div style="margin-bottom: 0.35rem;">${html}</div>`;
      history.scrollTop = history.scrollHeight;
    }
  }

  initQCRatchet() {
    const ccInput = document.getElementById('qc-cc-slider');
    const ccVal = document.getElementById('qc-cc-val');
    const covInput = document.getElementById('qc-cov-slider');
    const covVal = document.getElementById('qc-cov-val');
    const riskSelect = document.getElementById('qc-risk-select');
    const monitorBox = document.getElementById('qc-monitor-box');

    const update = () => {
      if (!ccInput || !covInput || !riskSelect || !monitorBox) return;

      const cc = parseInt(ccInput.value, 10);
      const covDelta = parseFloat(covInput.value);
      const risk = riskSelect.value;

      if (ccVal) ccVal.textContent = cc;
      if (covVal) covVal.textContent = (covDelta >= 0 ? '+' : '') + covDelta + '%';

      let statusBadge = '<span class="hud-card-badge badge-cyan" style="font-size: 1rem; border-color: #00ff66; color: #00ff66; background: rgba(0,255,102,0.1);">// DISPOSITION: AUTO_MERGE</span>';
      let reason = 'All ratchet constraints satisfied. Code complexity within bounds & zero coverage regression.';

      if (cc > 20) {
        statusBadge = '<span class="hud-card-badge badge-red" style="font-size: 1rem;">// DISPOSITION: BLOCK</span>';
        reason = `CRITICAL VIOLATION: Function cyclomatic complexity (${cc}) exceeds ceiling of 20.`;
        this.playSound('warn');
      } else if (covDelta < 0) {
        statusBadge = '<span class="hud-card-badge badge-red" style="font-size: 1rem;">// DISPOSITION: BLOCK</span>';
        reason = `RATCHET VIOLATION: Test coverage regressed by ${covDelta}%. Negative coverage strictly prohibited.`;
        this.playSound('warn');
      } else if (risk === 'HIGH') {
        statusBadge = '<span class="hud-card-badge badge-yellow" style="font-size: 1rem;">// DISPOSITION: HUMAN_SIGN_OFF</span>';
        reason = 'High-risk security/storage change detected. Autonomous merge blocked pending operator approval.';
      }

      monitorBox.innerHTML = `
        <div style="margin-bottom: 1rem;">${statusBadge}</div>
        <div style="font-family: var(--font-mono); font-size: 0.85rem; color: #cbd5e1; margin-bottom: 0.5rem;">
          Complexity Hotspot: <span style="color: ${cc > 20 ? '#ff003c' : '#00ffff'}">${cc} / 20</span> | 
          Cov Delta: <span style="color: ${covDelta < 0 ? '#ff003c' : '#00ff66'}">${covDelta}%</span>
        </div>
        <p style="font-size: 0.82rem; color: var(--text-dim); margin-top: 0.5rem;">${reason}</p>
      `;
    };

    if (ccInput) ccInput.addEventListener('input', update);
    if (covInput) covInput.addEventListener('input', update);
    if (riskSelect) riskSelect.addEventListener('change', update);
    update();
  }

  initClusterProbe() {
    const probeBtn = document.getElementById('btn-probe-matrix');
    const logBox = document.getElementById('matrix-probe-log');

    if (probeBtn && logBox) {
      probeBtn.addEventListener('click', () => {
        this.playSound('execute');
        logBox.innerHTML = '<span style="color: #fcee09;">[PINGING 192.168.0.4:1883] Probing Mosquitto MQTT & CUDA Ollama...</span>';
        setTimeout(() => {
          logBox.innerHTML = '<span style="color: #00ff66;">[HANDSHAKE OK] amdy (Methods) <---> tell (Facts) linked over reactive zero-polling bus.</span>';
          this.playSound('success');
        }, 350);
      });
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  document.body.classList.add('scanlines');
  window.cyberHUD = new CyberpunkHUD();
});
