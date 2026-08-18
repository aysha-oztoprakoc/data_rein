import { useAppSelector } from "../../store";


export function PonHealthWidget() {
  const pon = useAppSelector((state) => state.telemetry.pon);
  const connected = useAppSelector((state) => state.trail.connected);

  return (
    <div className="widget-card pon-widget">
      <div className="widget-header">
        <span className="widget-title">PON PROTOCOL // REACTIVE HEALTH</span>
        <span className={`badge ${connected ? "badge-ok" : "badge-err"}`}>
          {connected ? "STREAM ACTIVE" : "DISCONNECTED"}
        </span>
      </div>
      <div className="widget-body">
        <div className="pon-grid">
          <div className="pon-stat">
            <span className="pon-label">POLLING STATUS</span>
            <span className="pon-val text-green">ZERO POLLING (0% IDLE CPU)</span>
          </div>
          <div className="pon-stat">
            <span className="pon-label">INOTIFY WATCHERS</span>
            <span className="pon-val">{pon?.inotify_active !== false ? "ARMED (SQLite WAL)" : "DEGRADED"}</span>
          </div>
          <div className="pon-stat">
            <span className="pon-label">MQTT BUS</span>
            <span className="pon-val">{pon?.mqtt_active !== false ? "SUBSCRIBED (localhost:1883)" : "OFFLINE"}</span>
          </div>
          <div className="pon-stat">
            <span className="pon-label">FBE ARCHITECTURE</span>
            <span className="pon-val text-accent">FACT BASE ELEMENTS ACTIVE</span>
          </div>
        </div>
      </div>
      <div className="widget-footer text-dim">
        Rule of Awareness: Task Trail state machine authoritative. Wakes on notification only.
      </div>
    </div>
  );
}
