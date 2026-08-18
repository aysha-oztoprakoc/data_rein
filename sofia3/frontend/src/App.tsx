import { useEffect, useState } from "react";
import type { Health, SelectedNode, TrailSnapshot } from "./api";
import { GraphView } from "./views/Graph";
import { DetailPanel } from "./components/DetailPanel";

function useLiveTrail(): { trail: TrailSnapshot | null; connected: boolean } {
  const [snap, setSnap] = useState<TrailSnapshot | null>(null);
  const [connected, setConnected] = useState(false);

  useEffect(() => {
    let ws: WebSocket | null = null;
    let retry: number | undefined;
    let disposed = false;

    const connect = () => {
      if (disposed) return;
      const proto = location.protocol === "https:" ? "wss" : "ws";
      ws = new WebSocket(`${proto}://${location.host}/ws`);
      ws.onopen = () => {
        if (!disposed) setConnected(true);
      };
      ws.onmessage = (ev) => {
        try {
          const data = JSON.parse(ev.data) as TrailSnapshot;
          if (data.kind === "trail") setSnap(data);
        } catch {
          /* non-JSON keepalive — ignore */
        }
      };
      ws.onclose = () => {
        if (!disposed) {
          setConnected(false);
          setSnap(null);
          // Reactive reconnect (event-driven, never a busy loop).
          retry = window.setTimeout(connect, 3000);
        }
      };
    };
    connect();
    return () => {
      disposed = true;
      if (retry) window.clearTimeout(retry);
      ws?.close();
    };
  }, []);
  return { trail: snap, connected };
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

/**
 * Graph-first interface (refactor plan Ticket 1): a 60/40 horizontal split.
 * Left 60% = interactive unified Semantica graph; right 40% = scrollable
 * detail panel showing the full body of the selected node.
 */
export default function App() {
  const { trail, connected } = useLiveTrail();
  const health = useHealth();
  const live = connected && trail !== null;
  const [selected, setSelected] = useState<SelectedNode | null>(null);
  const [nav, setNav] = useState<"unified" | "tasks" | "wiki">("unified");

  return (
    <div className="app-shell">
      <header className="topbar">
        <div className="brand">
          SOFIA<span className="slash">³</span> // KERNEL
        </div>
        <div className="spacer" />
        <span className="live-dot" style={live ? {} : { animation: "none" }} />
        <span className="status-label">{live ? "LIVE" : !connected ? "RECONNECTING…" : "SYNCING…"}</span>
        <span className="status-label">v{health?.version ?? "3.0.0"}</span>
      </header>

      <nav className="nav-tabs">
        {(
          [
            ["unified", "UNIFIED GRAPH"],
            ["tasks", "TASKS"],
            ["wiki", "WIKI"],
          ] as const
        ).map(([id, label]) => (
          <button
            key={id}
            className={`nav-tab${nav === id ? " active" : ""}`}
            onClick={() => setNav(id)}
          >
            {label}
          </button>
        ))}
      </nav>

      <main className="main split">
        <GraphView trail={trail} onSelect={setSelected} nav={nav} />
        <DetailPanel selected={selected} />
      </main>
    </div>
  );
}
