import { useEffect, useState } from "react";
import type { Health, TrailSnapshot, View } from "./api";
import { TasksView } from "./views/Tasks";
import { WikiView } from "./views/Wiki";
import { GraphView } from "./views/Graph";

const VIEWS: { id: View; label: string }[] = [
  { id: "tasks", label: "TASKS" },
  { id: "wiki", label: "WIKI" },
  { id: "graph", label: "GRAPH" },
];

function useLiveTrail(): TrailSnapshot | null {
  const [snap, setSnap] = useState<TrailSnapshot | null>(null);
  useEffect(() => {
    let ws: WebSocket | null = null;
    let retry: number | undefined;

    const connect = () => {
      const proto = location.protocol === "https:" ? "wss" : "ws";
      ws = new WebSocket(`${proto}://${location.host}/ws`);
      ws.onmessage = (ev) => {
        try {
          const data = JSON.parse(ev.data) as TrailSnapshot;
          if (data.kind === "trail") setSnap(data);
        } catch {
          /* non-JSON keepalive — ignore */
        }
      };
      ws.onclose = () => {
        // Reactive reconnect (event-driven, never a busy loop).
        retry = window.setTimeout(connect, 3000);
      };
    };
    connect();
    return () => {
      if (retry) window.clearTimeout(retry);
      ws?.close();
    };
  }, []);
  return snap;
}

function useHealth(): Health | null {
  const [health, setHealth] = useState<Health | null>(null);
  useEffect(() => {
    fetch("/api/health")
      .then((r) => r.json())
      .then(setHealth)
      .catch(() => setHealth(null));
  }, []);
  return health;
}

export default function App() {
  const [view, setView] = useState<View>("tasks");
  const trail = useLiveTrail();
  const health = useHealth();
  const live = trail !== null;

  return (
    <div className="app-shell">
      <header className="topbar">
        <div className="brand">
          SOFIA<span className="slash">³</span> // KERNEL
        </div>
        <div className="spacer" />
        <span className="live-dot" style={live ? {} : { animation: "none" }} />
        <span className="status-label">{live ? "LIVE" : "SYNCING…"}</span>
        <span className="status-label">v{health?.version ?? "3.0.0"}</span>
      </header>

      <nav className="nav-tabs">
        {VIEWS.map((v) => (
          <button
            key={v.id}
            className={`nav-tab${view === v.id ? " active" : ""}`}
            onClick={() => setView(v.id)}
          >
            {v.label}
          </button>
        ))}
      </nav>

      <main className="main">
        {view === "tasks" && <TasksView trail={trail} />}
        {view === "wiki" && <WikiView />}
        {view === "graph" && <GraphView />}
      </main>
    </div>
  );
}
