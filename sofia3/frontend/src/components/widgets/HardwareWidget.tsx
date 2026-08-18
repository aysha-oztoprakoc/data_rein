import { useAppSelector } from "../../store";


export function HardwareWidget() {
  const hardware = useAppSelector((state) => state.telemetry.hardware);
  const gaps = useAppSelector((state) => state.telemetry.hardwareGaps);

  const nodes = hardware?.nodes || {
    amdy: { gpu: "AMD RX 9060 XT", vram_gb: 8, ram_gb: 16, cpu: "Ryzen 7 7700 (8c/16t)" },
    tell: { gpu: "NVIDIA GTX 1060", vram_gb: 6, ram_gb: 16, cpu: "Intel i5 7th-gen (4c/4t)" },
  };

  return (
    <div className="widget-card hardware-widget">
      <div className="widget-header">
        <span className="widget-title">CLUSTER HARDWARE // MANIFEST</span>
        <span className="badge badge-accent">ZERO-POLL SYNC</span>
      </div>
      <div className="widget-body grid-nodes">
        {Object.entries(nodes).map(([nodeName, info]) => {
          const vram = typeof info?.vram_gb === "number" ? info.vram_gb : 8;
          const ram = typeof info?.ram_gb === "number" ? info.ram_gb : 16;
          return (
            <div key={nodeName} className="node-box">
              <div className="node-title">
                <span className="node-tag">NODE</span> {nodeName.toUpperCase()}
              </div>
              <div className="stat-row">
                <span className="stat-label">GPU</span>
                <span className="stat-val">{String(info?.gpu || "Integrated / Shared")}</span>
              </div>
              <div className="stat-row">
                <span className="stat-label">VRAM</span>
                <span className="stat-val highlight">{vram} GB</span>
              </div>
              <div className="meter-bar">
                <div className="meter-fill" style={{ width: `${Math.min(100, (vram / 16) * 100)}%` }} />
              </div>
              <div className="stat-row">
                <span className="stat-label">RAM</span>
                <span className="stat-val">{ram} GB</span>
              </div>
              <div className="stat-row">
                <span className="stat-label">CPU</span>
                <span className="stat-val text-dim">{String(info?.cpu || "Multi-core")}</span>
              </div>
            </div>
          );
        })}
      </div>
      {gaps && (
        <div className="widget-footer gap-info">
          <span className="text-dim">CAPABILITY: </span>
          <span className="badge badge-ok">QLoRA / LoRA ADMITTED</span>
        </div>
      )}
    </div>
  );
}
