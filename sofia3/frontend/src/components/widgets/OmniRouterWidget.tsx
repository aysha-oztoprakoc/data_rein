import { ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, Cell } from "recharts";
import { useAppSelector } from "../../store";

export function OmniRouterWidget() {
  const combos = useAppSelector((state) => state.telemetry.combos);
  const tokens = useAppSelector((state) => state.telemetry.tokens);

  // Prepare chart data from token windows if available
  const chartData = tokens?.windows
    ? Object.entries(tokens.windows).map(([windowName, data]) => ({
        name: windowName,
        used: data.used_tokens || 0,
        budget: data.budget_tokens || 100000,
        percent: data.percent || 0,
      }))
    : [
        { name: "5h", used: 12400, budget: 100000, percent: 12.4 },
        { name: "day", used: 45000, budget: 500000, percent: 9.0 },
        { name: "week", used: 180000, budget: 2000000, percent: 9.0 },
      ];

  return (
    <div className="widget-card omnirouter-widget">
      <div className="widget-header">
        <span className="widget-title">OMNIROUTER // MODEL MATRIX & TOKEN BUDGETS</span>
        <span className="badge badge-accent">{combos.length || 11} COMBOS REGISTERED</span>
      </div>

      <div className="widget-body split-sub">
        <div className="sub-pane">
          <div className="sub-title">TOKEN BUDGET UTILIZATION (%)</div>
          <div style={{ width: "100%", height: 140 }}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={chartData} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <XAxis dataKey="name" stroke="#ff4040" fontSize={11} tickLine={false} />
                <YAxis stroke="#888" fontSize={10} domain={[0, 100]} />
                <Tooltip
                  contentStyle={{ backgroundColor: "#200000", borderColor: "#ff4040", color: "#fff" }}
                  formatter={(val: unknown) => [`${val}%`, "Budget Used"]}
                />
                <Bar dataKey="percent" fill="#ff4040" radius={[4, 4, 0, 0]}>
                  {chartData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.percent > 80 ? "#ff0000" : "#ff4040"} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>


        <div className="sub-pane combo-list-pane">
          <div className="sub-title">ACTIVE PROVIDER COMBO TIERS</div>
          <div className="combo-scroll">
            {(combos.length > 0
              ? combos
              : [
                  { id: "ollama/qwen2.5:7b", provider: "ollama", tier: "free", node: "amdy" },
                  { id: "ollama/deepseek-r1:8b", provider: "ollama", tier: "free", node: "tell" },
                  { id: "gemini/gemini-2.5-flash", provider: "gemini", tier: "cloud", node: "cloud" },
                  { id: "claude/claude-3-5-sonnet", provider: "anthropic", tier: "cloud", node: "cloud" },
                ]
            ).map((c) => (
              <div key={c.id} className="combo-row">
                <span className="combo-id">{c.id}</span>
                <span className={`combo-badge ${c.tier === "cloud" ? "badge-cloud" : "badge-local"}`}>
                  {c.tier.toUpperCase()} ({c.node})
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
