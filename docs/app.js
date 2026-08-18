// data_rein interactive documentation & simulator

document.addEventListener('DOMContentLoaded', () => {
  initClusterStatus();
  initSimTabs();
  initQCRatchetSimulator();
  initFBESimulator();
  initCopyButtons();
});

// Cluster status data
function initClusterStatus() {
  const pingTellBtn = document.getElementById('btn-ping-tell');
  const pingOutput = document.getElementById('ping-tell-status');
  
  if (pingTellBtn && pingOutput) {
    pingTellBtn.addEventListener('click', () => {
      pingOutput.textContent = 'Probing 192.168.0.4:1883 (MQTT) & :11434 (Ollama)...';
      setTimeout(() => {
        pingOutput.innerHTML = '<span style="color: #10b981;">● Online: 192.168.0.4 [tell] — Mosquitto MQTT v2 & Ollama CUDA (GTX 1060 6GB) active. Zero polling event loop active.</span>';
      }, 400);
    });
  }
}

// Simulator Tabs
function initSimTabs() {
  const tabs = document.querySelectorAll('.sim-tab-btn');
  const panels = {
    fbe: document.getElementById('sim-panel-fbe'),
    qc: document.getElementById('sim-panel-qc'),
    graph: document.getElementById('sim-panel-graph'),
  };

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      const target = tab.getAttribute('data-tab');
      Object.keys(panels).forEach(key => {
        if (panels[key]) {
          panels[key].style.display = key === target ? 'grid' : 'none';
        }
      });
    });
  });
}

// Interactive FBE Pipeline Simulator
function initFBESimulator() {
  const triggerBtn = document.getElementById('btn-run-fbe-sim');
  const logOutput = document.getElementById('fbe-log-output');
  const promptInput = document.getElementById('sim-prompt-input');

  if (!triggerBtn || !logOutput) return;

  triggerBtn.addEventListener('click', () => {
    const prompt = promptInput ? promptInput.value : "Refactor parser utility";
    logOutput.textContent = '';
    
    const steps = [
      { delay: 100, text: `[0.00s] [INOTIFY] Raw file drop detected -> Emitting RAW_DATA_AVAILABLE` },
      { delay: 400, text: `[0.03s] [IngestionNode] Parsing content -> Syncing chunks to Kùzu Graph & ChromaDB` },
      { delay: 800, text: `[0.08s] [IngestionNode] Emitting TASK_CREATED { task_id: "fbe-78a2", category: "code" }` },
      { delay: 1200, text: `[0.12s] [ContextBuilderNode] Traversed Kùzu neighborhood -> Injected 2 RAG wiki chunks` },
      { delay: 1600, text: `[0.17s] [ContextBuilderNode] Emitting TASK_READY_FOR_EXECUTION` },
      { delay: 2100, text: `[0.22s] [LocalNode] Dispatched to Ollama on amdy (RX 9060 XT 8GB VRAM) -> Success` },
      { delay: 2600, text: `[0.29s] [ValidatorNode] Archimedes & Sofia Judge check passed -> Emitting QC_REQUEST` },
      { delay: 3100, text: `[0.35s] [QualityControlNode] Radon CC=3, Cov Delta=+3.2%, Risk=LOW -> AUTO_MERGE` },
      { delay: 3500, text: `[0.41s] [qc_action] Executed git apply & commit autonomously -> Pipeline Complete (0% CPU Idle restored)` },
    ];

    steps.forEach(({ delay, text }) => {
      setTimeout(() => {
        logOutput.textContent += text + '\n';
        logOutput.scrollTop = logOutput.scrollHeight;
      }, delay);
    });
  });
}

// Interactive Quality Control Ratchet Simulator
function initQCRatchetSimulator() {
  const ccInput = document.getElementById('qc-cc-input');
  const ccVal = document.getElementById('qc-cc-val');
  const covInput = document.getElementById('qc-cov-input');
  const covVal = document.getElementById('qc-cov-val');
  const riskSelect = document.getElementById('qc-risk-select');
  const resultBox = document.getElementById('qc-result-box');

  function update() {
    if (!ccInput || !covInput || !riskSelect || !resultBox) return;

    const cc = parseInt(ccInput.value, 10);
    const covDelta = parseFloat(covInput.value);
    const risk = riskSelect.value;

    if (ccVal) ccVal.textContent = cc;
    if (covVal) covVal.textContent = (covDelta >= 0 ? '+' : '') + covDelta + '%';

    let passed = true;
    let recommendation = 'AUTO_MERGE';
    let badgeColor = '#10b981';
    let reason = 'All deterministic ratchet quality gates passed.';

    if (cc > 20) {
      passed = false;
      recommendation = 'BLOCK';
      badgeColor = '#f43f5e';
      reason = `Cyclomatic complexity (${cc}) exceeds ratchet maximum ceiling of 20.`;
    } else if (covDelta < 0) {
      passed = false;
      recommendation = 'BLOCK';
      badgeColor = '#f43f5e';
      reason = `Test coverage regressed by ${covDelta}%. Negative coverage deltas are strictly forbidden.`;
    } else if (risk === 'HIGH') {
      recommendation = 'HUMAN_REVIEW_REQUIRED';
      badgeColor = '#f59e0b';
      reason = 'High-risk security/database modification requires explicit sign-off; autonomous merge disabled.';
    } else if (risk === 'MEDIUM') {
      recommendation = 'MERGE_WITH_AI_APPROVAL';
      badgeColor = '#38bdf8';
      reason = 'Medium-risk module logic validated; sampling review enabled.';
    }

    resultBox.innerHTML = `
      <div style="margin-bottom: 0.75rem;">
        <span style="font-weight: 700; font-size: 1.1rem; color: ${badgeColor}; padding: 0.2rem 0.6rem; background: rgba(255,255,255,0.06); border-radius: 4px; border: 1px solid ${badgeColor};">
          ${recommendation}
        </span>
      </div>
      <p style="font-size: 0.9rem; color: #cbd5e1; margin-bottom: 0.5rem;"><strong>Status:</strong> ${passed ? '✅ PASSED GATES' : '❌ REJECTED'}</p>
      <p style="font-size: 0.85rem; color: #94a3b8;">${reason}</p>
    `;
  }

  if (ccInput) ccInput.addEventListener('input', update);
  if (covInput) covInput.addEventListener('input', update);
  if (riskSelect) riskSelect.addEventListener('change', update);
  update();
}

// Copy Code Snippets
function initCopyButtons() {
  document.querySelectorAll('.btn-copy').forEach(btn => {
    btn.addEventListener('click', () => {
      const code = btn.getAttribute('data-copy');
      if (code) {
        navigator.clipboard.writeText(code).then(() => {
          const orig = btn.textContent;
          btn.textContent = 'Copied!';
          setTimeout(() => btn.textContent = orig, 1500);
        });
      }
    });
  });
}
