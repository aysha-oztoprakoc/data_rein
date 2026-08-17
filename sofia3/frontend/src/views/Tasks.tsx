import { useEffect, useMemo, useState } from "react";
import type { TaskRecord, TrailSnapshot } from "../api";

/* ------------------------------------------------------------------ helpers */

/* Named aliases (TSX parses arrow functions inside nested generics poorly). */
interface OwnerStats {
  by_owner: Record<string, Record<string, number>>;
  total_tasks: number;
}
interface BudgetsPayload {
  budgets: Record<string, { cpu_pct: number; gpu_vram_gb: number }>;
}
interface CoordPayload {
  coordinator: { vram_budget_gb?: number; used_gb?: number; slots?: Record<string, unknown> };
}
interface ModelsPayload {
  categories: Record<string, { description: string; amdy: string[]; tell: string[]; cloud: string[] }>;
}
interface CombosPayload {
  combos: { id: string; provider: string; model: string; tier: string }[];
}
interface TokensPayload {
  report: Record<string, { day?: { total_tokens?: number } }>;
}
interface HardwarePayload {
  profile: {
    amdy?: { reachable?: boolean; hardware?: { vram_gb?: number; ram_gb?: number; cpu?: { model?: string; threads?: string } } };
  };
}
interface TrainPayload {
  train: { mode?: string; device?: string; base_model_key?: string; reason?: string };
}

function formatTime(ts: number | undefined): string {
  if (!ts) return "—";
  const d = new Date(ts * 1000);
  return d.toLocaleTimeString([], { hour12: false });
}

function truncate(s: string | undefined, n = 64): string {
  if (!s) return "";
  const clean = s.replace(/\s+/g, " ").trim();
  return clean.length > n ? `${clean.slice(0, n)}…` : clean;
}

function useApi<T>(path: string): { data: T | null; error: string | null } {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch(path)
      .then((r) => {
        if (!r.ok) throw new Error(`${path} ${r.status}`);
        return r.json();
      })
      .then(setData)
      .catch((e) => setError(String(e)));
  }, [path]);

  return { data, error };
}

/* ------------------------------------------------------------------ sections */

function StatCards({ trail }: { trail: TrailSnapshot | null }) {
  const summary = trail?.summary ?? {};
  const total = trail?.total ?? 0;
  const items = [
    { label: "RUNNING", value: (summary.running ?? 0) + (summary.active ?? 0) },
    { label: "PENDING", value: (summary.pending ?? 0) + (summary.queued ?? 0) },
    { label: "SUCCESS", value: summary.success ?? 0 },
    { label: "FAILED", value: summary.failed ?? 0 },
    { label: "TRAIL TOTAL", value: total },
  ];
  return (
    <div className="grid three">
      {items.map((it) => (
        <div key={it.label} className="panel">
          <div className="panel-title">{it.label}</div>
          <div style={{ fontSize: 34, fontWeight: 700, color: "var(--red-primary)" }}>
            {it.value}
          </div>
        </div>
      ))}
    </div>
  );
}

function LiveStream({ trail }: { trail: TrailSnapshot | null }) {
  const tasks: TaskRecord[] = trail?.tasks ?? [];
  return (
    <div className="panel">
      <div className="panel-title">LIVE TRAIL STREAM</div>
      {tasks.length === 0 ? (
        <div className="empty">NO SIGNAL — AWAITING TRAIL EVENTS</div>
      ) : (
        <div className="task-list">
          {tasks.slice(0, 40).map((t) => (
            <div key={t.task_id} className="task-row" title={truncate(t.prompt, 200)}>
              <span className="task-id">{truncate(t.prompt, 80) || t.task_id}</span>
              <span>
                <span className={`status-chip ${t.status}`}>{t.status}</span>
              </span>
              <span className="task-node">{t.target_node ?? "?"}</span>
              <span className="task-meta">{formatTime(t.timestamp)}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function AgentStatusPanel() {
  const { data } = useApi<OwnerStats>(
    "/api/agents/status",
  );
  if (!data) return null;
  const owners = Object.entries(data.by_owner ?? {}).sort((a, b) => {
    const sa = Object.values(a[1]).reduce((x, y) => x + y, 0);
    const sb = Object.values(b[1]).reduce((x, y) => x + y, 0);
    return sb - sa;
  });
  return (
    <div className="panel">
      <div className="panel-title">AGENT ACTIVITY — {data.total_tasks ?? 0} TASKS</div>
      <div className="task-list">
        {owners.map(([owner, statuses]) => (
          <div key={owner} className="task-row" style={{ gridTemplateColumns: "1.2fr 2fr" }}>
            <span className="task-node">{owner}</span>
            <span style={{ display: "flex", gap: 6, flexWrap: "wrap" }}>
              {Object.entries(statuses).map(([st, count]) => (
                <span key={st} className={`status-chip ${st}`}>
                  {st}:{count}
                </span>
              ))}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}

function BudgetsPanel() {
  const { data } = useApi<BudgetsPayload>(
    "/api/agents/budgets",
  );
  if (!data) return null;
  const entries = Object.entries(data.budgets ?? {});
  return (
    <div className="panel">
      <div className="panel-title">RESOURCE BUDGETS — CPU% / VRAM GB</div>
      <div className="task-list">
        {entries.map(([agent, b]) => (
          <div key={agent} className="task-row" style={{ gridTemplateColumns: "1.2fr 1fr 1fr" }}>
            <span className="task-node">{agent}</span>
            <span className="task-meta" style={{ textAlign: "left" }}>
              {b.cpu_pct}%
            </span>
            <span className="task-meta" style={{ textAlign: "left" }}>
              {b.gpu_vram_gb} GB
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}

function CoordinatorPanel() {
  const { data } = useApi<CoordPayload>(
    "/api/coord",
  );
  if (!data) return null;
  const c = data.coordinator ?? {};
  const slots = Object.entries(c.slots ?? {});
  return (
    <div className="panel">
      <div className="panel-title">MODEL COORDINATOR — VRAM {c.used_gb ?? 0}/{c.vram_budget_gb ?? "?"} GB</div>
      {slots.length === 0 ? (
        <div className="empty">NO RESIDENT MODELS</div>
      ) : (
        <div className="task-list">
          {slots.map(([model, state]) => (
            <div key={model} className="task-row" style={{ gridTemplateColumns: "2fr 1fr" }}>
              <span className="task-id">{model}</span>
              <span className="task-meta">{JSON.stringify(state)}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function ModelsPanel() {
  const { data } = useApi<ModelsPayload>(
    "/api/models",
  );
  if (!data) return null;
  const cats = Object.entries(data.categories ?? {}).slice(0, 6);
  return (
    <div className="panel">
      <div className="panel-title">ROUTING CATEGORIES → COMBO CHAINS</div>
      <div className="task-list">
        {cats.map(([cat, v]) => (
          <div key={cat} className="panel" style={{ padding: 10, background: "rgba(9,3,0,0.4)" }}>
            <div style={{ color: "var(--red-primary)", marginBottom: 6 }}>{cat}</div>
            <div style={{ fontSize: 11, color: "var(--text-dim)", lineHeight: 1.7 }}>
              <div>amdy: {v.amdy.slice(0, 3).join(" · ") || "—"}</div>
              {v.cloud.length > 0 && <div>cloud: {v.cloud.slice(0, 3).join(" · ")}</div>}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function CombosPanel() {
  const { data } = useApi<CombosPayload>(
    "/api/combos",
  );
  if (!data) return null;
  const combos = data.combos ?? [];
  return (
    <div className="panel">
      <div className="panel-title">COMBOS — {combos.length}</div>
      <div className="task-list">
        {combos.slice(0, 12).map((c) => (
          <div key={c.id} className="task-row" style={{ gridTemplateColumns: "1.6fr 1fr 1fr" }}>
            <span className="task-id" title={c.id}>{c.model}</span>
            <span className="task-meta">{c.provider}</span>
            <span className={`status-chip ${c.tier}`}>{c.tier}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

function TokensPanel() {
  const { data } = useApi<TokensPayload>("/api/tokens");
  if (!data) return null;
  const rows = Object.entries(data.report ?? {});
  if (rows.length === 0) return null;
  return (
    <div className="panel">
      <div className="panel-title">CLOUD TOKEN USAGE (24H)</div>
      <div className="task-list">
        {rows.map(([provider, usage]) => (
          <div key={provider} className="task-row" style={{ gridTemplateColumns: "1.2fr 1.5fr" }}>
            <span className="task-node">{provider}</span>
            <span className="task-meta">
              {usage.day?.total_tokens?.toLocaleString() ?? 0} tokens
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}

function HardwarePanel() {
  const { data } = useApi<HardwarePayload>(
    "/api/hardware",
  );
  if (!data) return null;
  const hw = data.profile?.amdy;
  return (
    <div className="panel">
      <div className="panel-title">HARDWARE — NODE AMDY {hw?.reachable ? "ONLINE" : "OFFLINE"}</div>
      {hw && (
        <div className="task-list">
          <div className="task-row" style={{ gridTemplateColumns: "1fr 1fr" }}>
            <span className="task-meta">CPU</span>
            <span className="task-id">{hw.hardware?.cpu?.model ?? "?"}</span>
          </div>
          <div className="task-row" style={{ gridTemplateColumns: "1fr 1fr" }}>
            <span className="task-meta">VRAM</span>
            <span className="task-id">{hw.hardware?.vram_gb ?? "?"} GB</span>
          </div>
          <div className="task-row" style={{ gridTemplateColumns: "1fr 1fr" }}>
            <span className="task-meta">RAM</span>
            <span className="task-id">{hw.hardware?.ram_gb ?? "?"} GB</span>
          </div>
        </div>
      )}
    </div>
  );
}

function TrainPanel() {
  const { data } = useApi<TrainPayload>(
    "/api/train",
  );
  if (!data) return null;
  const t = data.train ?? {};
  return (
    <div className="panel">
      <div className="panel-title">TRAINING CAPABILITY</div>
      <div className="task-list">
        <div className="task-row" style={{ gridTemplateColumns: "1fr 2fr" }}>
          <span className="task-meta">mode</span>
          <span className="task-id">{t.mode ?? "?"}</span>
        </div>
        <div className="task-row" style={{ gridTemplateColumns: "1fr 2fr" }}>
          <span className="task-meta">device</span>
          <span className="task-id">{t.device ?? "?"}</span>
        </div>
        {t.reason && (
          <div className="task-row" style={{ gridTemplateColumns: "1fr 2fr" }}>
            <span className="task-meta">reason</span>
            <span className="task-id">{truncate(t.reason, 80)}</span>
          </div>
        )}
      </div>
    </div>
  );
}

/* -------------------------------------------------------------------- view */

export function TasksView({ trail }: { trail: TrailSnapshot | null }) {
  const summary = useMemo(() => trail?.summary ?? {}, [trail]);
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
      <StatCards trail={trail} />
      <div className="grid two">
        <AgentStatusPanel />
        <BudgetsPanel />
        <CoordinatorPanel />
        <TokensPanel />
      </div>
      <LiveStream trail={trail} />
      <div className="grid two">
        <ModelsPanel />
        <CombosPanel />
        <HardwarePanel />
        <TrainPanel />
      </div>
      <div style={{ color: "var(--dim)", fontSize: 11, textAlign: "right" }}>
        live summary: {Object.entries(summary).map(([k, v]) => `${k}=${v}`).join(" · ")}
      </div>
    </div>
  );
}
