import { useAppSelector } from "../../store";


export function CoordWidget() {
  const coord = useAppSelector((state) => state.telemetry.coord);
  const agentBudgets = useAppSelector((state) => state.telemetry.agentBudgets);

  return (
    <div className="widget-card coord-widget">
      <div className="widget-header">
        <span className="widget-title">COORDINATOR // MODEL RESIDENCY & AGENT BUDGETS</span>
        <span className="badge badge-accent">
          {coord?.busy ? "LOCK ACQUIRED (BUSY)" : "IDLE / READY"}
        </span>
      </div>
      <div className="widget-body split-sub">
        <div className="sub-pane">
          <div className="sub-title">RESIDENT MODEL SLOT</div>
          <div className="stat-row">
            <span className="stat-label">LOADED MODEL</span>
            <span className="stat-val highlight">{coord?.active_model || "None (JIT Evicted)"}</span>
          </div>
          <div className="stat-row">
            <span className="stat-label">VRAM ALLOCATED</span>
            <span className="stat-val">{coord?.vram_allocated_mb ? `${coord.vram_allocated_mb} MB` : "0 MB"}</span>
          </div>
        </div>
        <div className="sub-pane">
          <div className="sub-title">AGENT RESOURCE ENVELOPES</div>
          <div className="budget-list">
            {agentBudgets && Object.keys(agentBudgets).length > 0 ? (
              Object.entries(agentBudgets).map(([agent, b]) => (
                <div key={agent} className="budget-row">
                  <span className="agent-tag">{agent}</span>
                  <span className="text-dim">{JSON.stringify(b)}</span>
                </div>
              ))
            ) : (
              <div className="text-dim">Standard 8GB VRAM cap across amdy / tell slots.</div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
