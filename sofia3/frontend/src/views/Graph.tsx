import { useEffect, useMemo, useRef, useState } from "react";

interface GraphNode {
  id: string;
  type: string;
  content?: string;
  properties?: Record<string, unknown>;
}
interface GraphEdge {
  id?: string;
  source: string;
  target: string;
  type: string;
  weight?: number;
}
interface GraphPayload {
  nodes: GraphNode[];
  edges: GraphEdge[];
}
interface ApiGraphResponse {
  graph?: GraphPayload;
  stats?: {
    node_types?: Record<string, number>;
    edge_types?: Record<string, number>;
    node_count?: number;
    edge_count?: number;
  };
  notes?: { pages?: number; memories?: number; tasks?: number; models?: number; centrality?: string };
  degraded?: boolean;
}

const NODE_COLORS: Record<string, string> = {
  Page: "#ff4040",
  Memory: "#ff3c3c",
  Task: "#ffcf3d",
  Agent: "#26bdfd",
  Model: "#5c5855",
  Owner: "#b06a6a",
  Category: "#7a3a3a",
  Session: "#9b4d4d",
};

function nodeColor(type: string): string {
  return NODE_COLORS[type] ?? "#8a5c5c";
}

// Minimal structural type for the lazily-imported force-graph instance.
interface ForceGraphHandle {
  graphData: (d: unknown) => ForceGraphHandle;
  nodeId: (k: string) => ForceGraphHandle;
  nodeLabel: (f: (n: GraphNode) => string) => ForceGraphHandle;
  nodeColor: (f: (n: GraphNode) => string) => ForceGraphHandle;
  nodeVal: (f: (n: GraphNode) => number) => ForceGraphHandle;
  linkColor: (f: () => string) => ForceGraphHandle;
  backgroundColor: (c: string) => ForceGraphHandle;
  width: (w: number) => ForceGraphHandle;
  height: (h: number) => ForceGraphHandle;
  onNodeClick: (f: (n: GraphNode) => void) => ForceGraphHandle;
  d3Force: (name: string) => { strength: (v: number) => unknown };
}

export function GraphView() {
  const [data, setData] = useState<ApiGraphResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [filter, setFilter] = useState<string>("all");
  const [activeNode, setActiveNode] = useState<GraphNode | null>(null);
  const [forceGraph, setForceGraph] = useState<((el: HTMLElement) => ForceGraphHandle) | null>(null);

  useEffect(() => {
    fetch("/api/graph")
      .then((r) => r.json())
      .then((d: ApiGraphResponse) => {
        const detail = (d as unknown as { detail?: { degraded?: boolean; error?: string } }).detail;
        if (detail?.degraded) setError(detail.error ?? "degraded");
        else setData(d);
      })
      .catch(() => setError("graph bridge unreachable"));
  }, []);

  // Lazy-load the force-graph module (avoids bloating initial bundle).
  useEffect(() => {
    import("react-force-graph-2d")
      .then((m) =>
        setForceGraph(() => (m.default as unknown) as (el: HTMLElement) => ForceGraphHandle),
      )
      .catch(() => setError("force-graph module failed to load"));
  }, []);

  const graph = data?.graph;
  const nodeTypes = useMemo(() => {
    const map: Record<string, number> = {};
    (graph?.nodes ?? []).forEach((n) => {
      map[n.type] = (map[n.type] ?? 0) + 1;
    });
    return map;
  }, [graph]);

  const fgData = useMemo(() => {
    const nodes = graph?.nodes ?? [];
    const ids = new Set(nodes.map((n) => n.id));
    const links = (graph?.edges ?? [])
      .filter((e) => ids.has(e.source) && ids.has(e.target))
      .map((e) => ({ source: e.source, target: e.target }));
    return { nodes, links };
  }, [graph]);

  const renderRef = useRef<HTMLDivElement>(null);
  const graphInstance = useRef<ForceGraphHandle | null>(null);

  useEffect(() => {
    if (!forceGraph || !fgData.nodes.length || !renderRef.current) return;
    if (graphInstance.current) {
      graphInstance.current.graphData(fgData);
      return;
    }
    const g = forceGraph(renderRef.current)
      .graphData(fgData)
      .nodeId("id")
      .nodeLabel((n) => `${n.content ?? n.id} [${n.type}]`)
      .nodeColor((n) => nodeColor(n.type))
      .nodeVal((n) => (n.type === "Page" || n.type === "Memory" ? 4 : 3))
      .linkColor(() => "rgba(255,64,64,0.35)")
      .backgroundColor("#090300")
      .width(910)
      .height(540)
      .onNodeClick((n) => setActiveNode(n));
    g.d3Force("charge").strength(-90);
    graphInstance.current = g;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [forceGraph, fgData]);

  const types = Object.keys(nodeTypes);
  useEffect(() => {
    if (filter === "all" || !graphInstance.current) return;
    const filtered = fgData.nodes.filter((n) => n.type === filter);
    graphInstance.current.graphData({ nodes: filtered, links: fgData.links });
  }, [filter, fgData, graph]);

  if (error) {
    return (
      <div className="panel">
        <div className="panel-title">UNIFIED KNOWLEDGE GRAPH</div>
        <div className="error-banner">GRAPH DEGRADED: {error}</div>
      </div>
    );
  }
  if (!graph) return <div className="panel"><div className="empty">LOADING GRAPH…</div></div>;

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
      <div className="panel">
        <div className="panel-title">
          UNIFIED KNOWLEDGE GRAPH — {graph.nodes.length} NODES / {graph.edges.length} EDGES
        </div>
        <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginBottom: 12 }}>
          {["all", ...types].map((t) => (
            <button
              key={t}
              className={`nav-tab${filter === t ? " active" : ""}`}
              onClick={() => setFilter(t)}
            >
              {t} ({t === "all" ? graph.nodes.length : (nodeTypes[t] ?? 0)})
            </button>
          ))}
        </div>
        <div ref={renderRef} />
        <div style={{ marginTop: 8, display: "flex", gap: 14, flexWrap: "wrap", fontSize: 11, color: "var(--text-dim)" }}>
          {Object.entries(nodeTypes).map(([t, c]) => (
            <span key={t}>
              <span style={{ color: nodeColor(t), fontWeight: 700 }}>▮ {t}</span> {c}
            </span>
          ))}
        </div>
      </div>

      {activeNode && (
        <div className="panel">
          <div className="panel-title">SELECTED NODE</div>
          <div style={{ fontSize: 12, lineHeight: 1.8 }}>
            <div><strong>{activeNode.content ?? activeNode.id}</strong></div>
            <div style={{ color: "var(--text-dim)" }}>
              id: {activeNode.id} · type: {activeNode.type}
            </div>
            {activeNode.properties &&
              Object.entries(activeNode.properties)
                .filter(([, v]) => v)
                .slice(0, 6)
                .map(([k, v]) => (
                  <div key={k} style={{ color: "var(--text-dim)" }}>
                    {k}: {String(v)}
                  </div>
                ))}
          </div>
        </div>
      )}

      {data?.notes && (
        <div className="panel">
          <div className="panel-title">GRAPH NOTES</div>
          <div style={{ fontSize: 11, color: "var(--text-dim)", lineHeight: 1.8 }}>
            pages: {data.notes.pages} · memories: {data.notes.memories} · tasks: {data.notes.tasks} · models: {data.notes.models}
            {(data.notes.centrality ?? "").startsWith("unavailable") && (
              <div style={{ marginTop: 6 }}>
                centrality/communities require the heavy semantica `kg` subpackage (not vendored — see third_party/semantica/README.md).
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}