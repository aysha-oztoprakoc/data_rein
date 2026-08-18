import { useCallback, useEffect, useMemo, useState } from "react";
import Graph from "graphology";
import { SigmaContainer, useLoadGraph, useRegisterEvents, useSigma } from "@react-sigma/core";
import "@react-sigma/core/lib/style.css";

import type { ApiGraphResponse, SelectedNode, TrailSnapshot } from "../api";
import { useGraphLayout } from "../layout";

interface Props {
  trail: TrailSnapshot | null;
  onSelect: (node: SelectedNode | null) => void;
  /** top-level nav filter: unified (all) or source-scoped view */
  nav?: "unified" | "tasks" | "wiki";
}

const EMPTY: ApiGraphResponse = {};

interface TooltipData {
  x: number;
  y: number;
  id: string;
  label: string;
  type: string;
  category?: string;
  domain?: string;
  degree: number;
  status?: string;
}

/**
 * High-performance Sigma Controller:
 * Configures zero-cost WebGL node/edge reducers and smooth camera animations.
 * Eliminates graph rebuilds during hover/selection.
 */
function SigmaController({
  hoveredNode,
  selectedNodeId,
  connectedNodes,
  onNodeClick,
  onStageClick,
  onHover,
  onContextMenu,
}: {
  hoveredNode: string | null;
  selectedNodeId: string | null;
  connectedNodes: Set<string>;
  onNodeClick: (node: string) => void;
  onStageClick: () => void;
  onHover: (node: string | null, clientX?: number, clientY?: number) => void;
  onContextMenu: (e: MouseEvent, node: string) => void;
}) {
  const sigma = useSigma();
  const registerEvents = useRegisterEvents();

  // Register interactive events
  useEffect(() => {
    registerEvents({
      clickNode: (event: any) => {
        onNodeClick(event.node);
        if (event.node !== selectedNodeId) {
          const nodeDisplay = sigma.getNodeDisplayData(event.node);
          if (nodeDisplay) {
            sigma.getCamera().animate(
              { x: nodeDisplay.x, y: nodeDisplay.y, ratio: Math.min(sigma.getCamera().ratio, 0.6) },
              { duration: 350 }
            );
          }
        }
      },
      clickStage: () => {
        onStageClick();
      },
      enterNode: (event: any) => {
        const orig = event.event?.original;
        onHover(event.node, orig?.clientX, orig?.clientY);
      },
      leaveNode: () => onHover(null),
      rightClickNode: (event: any) => {
        event.event.original.preventDefault();
        onContextMenu(event.event.original as MouseEvent, event.node);
      },
    });
  }, [registerEvents, onNodeClick, onStageClick, onHover, onContextMenu, sigma, selectedNodeId]);

  // Set up 60fps WebGL Reducers for zero-allocation hover & highlight effects
  useEffect(() => {
    const activeTarget = hoveredNode || selectedNodeId;

    sigma.setSetting("nodeReducer", (node: string, data: any) => {
      const res = { ...data };

      if (activeTarget) {
        if (node === activeTarget) {
          res.highlighted = true;
          res.zIndex = 20;
          res.size = (data.baseSize || data.size || 1.2) * 1.6;
          res.forceLabel = true;
        } else if (connectedNodes.has(node)) {
          res.highlighted = true;
          res.zIndex = 10;
          res.size = (data.baseSize || data.size || 1.2) * 1.25;
          res.forceLabel = true;
        } else {
          res.color = "#1f1f22";
          res.label = "";
          res.zIndex = 1;
        }
      } else {
        res.highlighted = false;
        res.zIndex = 1;
      }
      return res;
    });

    sigma.setSetting("edgeReducer", (edge: string, data: any) => {
      const res = { ...data };
      const graph = sigma.getGraph();

      if (activeTarget && graph.hasEdge(edge)) {
        const source = graph.source(edge);
        const target = graph.target(edge);
        if (source === activeTarget || target === activeTarget) {
          res.color = "#00ffff";
          res.size = 1.2;
          res.zIndex = 10;
        } else {
          res.hidden = true;
        }
      } else {
        res.hidden = false;
        res.color = data.baseColor || "rgba(0,255,255,0.07)";
        res.size = data.baseSize || 0.12;
      }
      return res;
    });

    sigma.refresh();
  }, [sigma, hoveredNode, selectedNodeId, connectedNodes]);

  return null;
}

/**
 * Loads graph topology into Graphology ONLY when dataset, layout, or filters change.
 */
function GraphLoader({
  nodes,
  edges,
  layout,
  filter,
  isInNav,
  nodeDegrees,
  liveStatus,
}: any) {
  const loadGraph = useLoadGraph();

  useEffect(() => {
    const graph = new Graph();
    const filteredNodes = nodes.filter(
      (nd: any) => isInNav(nd.type) && (filter === "all" || nd.type === filter)
    );

    filteredNodes.forEach((nd: any) => {
      const pos = layout.positions[nd.id] ?? {
        x: Math.random() * 1000,
        y: Math.random() * 1000,
      };

      const taskId = nd.type === "Task" ? nd.id.replace(/^task:/, "") : undefined;
      const status =
        (taskId && liveStatus[taskId]) ||
        (nd.properties?.status as string | undefined) ||
        (nd.metadata?.status as string | undefined);

      let color = "#aaaaaa";
      if (nd.type === "Task")
        color =
          status === "pending"
            ? "#e6a23c"
            : status === "completed"
            ? "#67c23a"
            : "#f56c6c";
      if (nd.type === "Memory") color = "#c785c8";
      if (nd.type === "Page") color = "#409eff";
      if (nd.type === "Skill") color = "#e6a23c";
      if (nd.type === "Chunk") color = "#666666";

      const degree = nodeDegrees[nd.id] || 0;
      // Sleek logarithmic degree scaling: base 0.9px up to 3.6px for major hubs
      const baseSize = Math.max(0.9, Math.min(3.6, 0.9 + Math.log2(degree + 1) * 0.45));

      const category =
        (nd.properties?.category as string | undefined) ||
        (nd.metadata?.category as string | undefined) ||
        "general";

      const domain =
        (nd.properties?.domain as string | undefined) ||
        (nd.metadata?.domain as string | undefined);

      graph.addNode(nd.id, {
        x: pos.x,
        y: pos.y,
        size: baseSize,
        baseSize,
        label: nd.content ?? nd.id,
        color: color,
        baseColor: color,
        nodeType: nd.type,
        category,
        domain,
        degree,
      });
    });

    edges.forEach((e: any) => {
      if (graph.hasNode(e.source) && graph.hasNode(e.target)) {
        graph.addEdge(e.source, e.target, {
          size: 0.12,
          baseSize: 0.12,
          color: "rgba(0,255,255,0.07)",
          baseColor: "rgba(0,255,255,0.07)",
        });
      }
    });

    loadGraph(graph);
  }, [loadGraph, nodes, edges, layout, filter, isInNav, nodeDegrees, liveStatus]);

  return null;
}

export function GraphView({ trail, onSelect, nav = "unified" }: Props) {
  const [data, setData] = useState<ApiGraphResponse>(EMPTY);
  const [error, setError] = useState<string | null>(null);
  const [filter, setFilter] = useState<string>("all");
  const [selectedNodeId, setSelectedNodeId] = useState<string | null>(null);
  const [hoveredNode, setHoveredNode] = useState<string | null>(null);
  const [tooltip, setTooltip] = useState<TooltipData | null>(null);

  // Context Menu State
  const [contextMenu, setContextMenu] = useState<{
    x: number;
    y: number;
    nodeId: string;
  } | null>(null);

  useEffect(() => {
    setFilter("all");
  }, [nav]);

  const fetchGraph = useCallback(() => {
    fetch("/api/graph")
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then(
        (
          d: ApiGraphResponse & { detail?: { degraded?: boolean; error?: string } }
        ) => {
          if (d.detail?.degraded) setError(d.detail.error ?? "degraded");
          else setData(d);
        }
      )
      .catch((err) => setError(err?.message ?? "graph bridge unreachable"));
  }, []);

  useEffect(() => {
    fetchGraph();
  }, [fetchGraph]);

  const graph = data?.graph;
  const nodes = graph?.nodes ?? [];
  const edges = graph?.edges ?? [];

  const nodeTypesSet = useMemo(() => {
    const map: Record<string, number> = {};
    nodes.forEach((nd: any) => {
      map[nd.type] = (map[nd.type] ?? 0) + 1;
    });
    return map;
  }, [nodes]);

  const familyForNav: Record<string, string[]> = useMemo(
    () => ({
      tasks: ["Task", "Agent", "Owner"],
      wiki: ["Page", "Memory", "Skill", "Category", "Domain", "Owner", "Session"],
      unified: ["all"],
    }),
    []
  );
  const families = familyForNav[nav] ?? ["all"];
  const isInNav = useCallback(
    (t: string) =>
      nav === "unified" || (families.length === 1 && families[0] === "all")
        ? true
        : families.includes(t),
    [nav, families]
  );

  const liveStatus = useMemo(() => {
    const map: Record<string, string> = {};
    for (const t of trail?.tasks ?? []) map[t.task_id] = t.status ?? "pending";
    return map;
  }, [trail]);

  const nodeDegrees = useMemo(() => {
    const map: Record<string, number> = {};
    for (const e of edges) {
      map[e.source] = (map[e.source] || 0) + 1;
      map[e.target] = (map[e.target] || 0) + 1;
    }
    return map;
  }, [edges]);

  const activeFocusNode = hoveredNode || selectedNodeId;

  const connectedNodes = useMemo(() => {
    if (!activeFocusNode) return new Set<string>();
    const set = new Set<string>();
    for (const e of edges) {
      if (e.source === activeFocusNode) set.add(e.target);
      if (e.target === activeFocusNode) set.add(e.source);
    }
    return set;
  }, [activeFocusNode, edges]);

  const layout = useGraphLayout(graph);

  const visibleCount = nodes.filter((nd: any) => isInNav(nd.type)).length;
  const types = Object.keys(nodeTypesSet).filter((t) => isInNav(t));

  const handleSelect = useCallback(
    (nodeId: string) => {
      if (selectedNodeId === nodeId) {
        // Toggle off selection
        setSelectedNodeId(null);
        onSelect(null);
        return;
      }
      setSelectedNodeId(nodeId);
      const nd = nodes.find((x: any) => x.id === nodeId);
      if (!nd) return;
      onSelect({
        id: nd.id,
        type: nd.type,
        content: nd.content ?? nd.id,
        properties: nd.properties ?? nd.metadata,
      });
    },
    [nodes, onSelect, selectedNodeId]
  );

  const handleStageClick = useCallback(() => {
    setSelectedNodeId(null);
    onSelect(null);
    setContextMenu(null);
  }, [onSelect]);

  // Pressing Escape deselects the current node and dismisses context menu
  useEffect(() => {
    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        setSelectedNodeId(null);
        onSelect(null);
        setContextMenu(null);
      }
    };
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [onSelect]);

  const handleHover = useCallback(
    (nodeId: string | null, clientX?: number, clientY?: number) => {
      setHoveredNode(nodeId);
      if (!nodeId || clientX === undefined || clientY === undefined) {
        setTooltip(null);
        return;
      }
      const nd = nodes.find((x: any) => x.id === nodeId);
      if (!nd) {
        setTooltip(null);
        return;
      }

      const degree = nodeDegrees[nodeId] || 0;
      const category =
        (nd.properties?.category as string | undefined) ||
        (nd.metadata?.category as string | undefined);
      const domain =
        (nd.properties?.domain as string | undefined) ||
        (nd.metadata?.domain as string | undefined);
      const taskId = nd.type === "Task" ? nd.id.replace(/^task:/, "") : undefined;
      const status = taskId ? liveStatus[taskId] : undefined;

      setTooltip({
        x: clientX,
        y: clientY,
        id: nd.id,
        label: nd.content ?? nd.id,
        type: nd.type,
        category,
        domain,
        degree,
        status,
      });
    },
    [nodes, nodeDegrees, liveStatus]
  );

  const handleContextMenu = useCallback((e: MouseEvent, nodeId: string) => {
    setContextMenu({ x: e.clientX, y: e.clientY, nodeId });
  }, []);

  const handleCloseContextMenu = useCallback(() => {
    setContextMenu(null);
  }, []);

  const selectedContextNode = useMemo(() => {
    if (!contextMenu) return null;
    return nodes.find((x: any) => x.id === contextMenu.nodeId) || null;
  }, [contextMenu, nodes]);

  const isCoreNode = useMemo(() => {
    if (!selectedContextNode) return false;
    const cat = (
      (selectedContextNode.properties?.category as string) ||
      (selectedContextNode.metadata?.category as string) ||
      ""
    )
      .trim()
      .toLowerCase();
    return (
      cat === "sys" ||
      cat === "core" ||
      selectedContextNode.id.startsWith("page:prime_directive") ||
      selectedContextNode.id.startsWith("page:architecture")
    );
  }, [selectedContextNode]);

  const handleDeleteNode = useCallback(() => {
    if (!contextMenu || isCoreNode) return;
    const nd = selectedContextNode;
    if (!nd) return;

    let endpoint = "";
    if (nd.type === "Page") {
      endpoint = `/api/wiki/page/${nd.id.replace(/^page:/, "")}`;
    } else if (nd.type === "Memory") {
      endpoint = `/api/wiki/memory/${nd.id.replace(/^memory:/, "")}`;
    }

    if (endpoint) {
      fetch(endpoint, { method: "DELETE" })
        .then((res) => {
          if (!res.ok) {
            return res.json().then((d) => {
              alert(d.detail || "Deletion failed");
            });
          }
          setContextMenu(null);
          setTimeout(fetchGraph, 1000);
        })
        .catch((err) => console.error("Delete failed:", err));
    }
  }, [contextMenu, isCoreNode, selectedContextNode, fetchGraph]);

  // Progressive Level of Detail (LOD) Sigma Settings
  const sigmaSettings = useMemo(
    () => ({
      allowInvalidContainer: true,
      labelRenderedSizeThreshold: 14, // Labels appear only when zoomed in close
      enableEdgeEvents: false, // Performance boost: skip edge raycasting
      zIndex: true, // Enable hardware z-indexing for focused nodes
      renderLabels: true,
      defaultNodeColor: "#888888",
      defaultEdgeColor: "rgba(0,255,255,0.07)",
      stagePadding: 30,
    }),
    []
  );

  if (error) {
    return (
      <div className="panel">
        <div className="panel-title">UNIFIED KNOWLEDGE GRAPH</div>
        <div className="error-banner">GRAPH DEGRADED: {error}</div>
      </div>
    );
  }
  if (!graph)
    return (
      <div className="panel">
        <div className="empty">LOADING GRAPH…</div>
      </div>
    );

  return (
    <div className="graph-view graph-pane-60" onClick={handleCloseContextMenu}>
      <div className="panel-title graph-title">
        UNIFIED GRAPH — {visibleCount} VISIBLE / {nodes.length} NODES ·{" "}
        {edges.length} EDGES
      </div>
      <div className="graph-filters">
        {["all", ...types].map((t) => (
          <button
            key={t}
            className={`nav-tab${filter === t ? " active" : ""}`}
            onClick={() => setFilter(t)}
          >
            {t} ({t === "all" ? visibleCount : nodeTypesSet[t] ?? 0})
          </button>
        ))}
      </div>

      <div className="reactflow-wrap" style={{ position: "relative" }}>
        <SigmaContainer
          style={{ width: "100%", height: "100%", background: "#110b0b" }}
          settings={sigmaSettings}
        >
          <GraphLoader
            nodes={nodes}
            edges={edges}
            layout={layout}
            filter={filter}
            isInNav={isInNav}
            nodeDegrees={nodeDegrees}
            liveStatus={liveStatus}
          />
          <SigmaController
            hoveredNode={hoveredNode}
            selectedNodeId={selectedNodeId}
            connectedNodes={connectedNodes}
            onNodeClick={handleSelect}
            onStageClick={handleStageClick}
            onHover={handleHover}
            onContextMenu={handleContextMenu}
          />
        </SigmaContainer>

        {/* Rich HTML Tooltip Overlay on Node Hover */}
        {tooltip && (
          <div
            className="graph-tooltip"
            style={{
              position: "fixed",
              top: tooltip.y + 14,
              left: tooltip.x + 14,
              pointerEvents: "none",
              zIndex: 9999,
              background: "rgba(18, 18, 22, 0.94)",
              backdropFilter: "blur(8px)",
              border: "1px solid #3b82f6",
              borderRadius: "6px",
              padding: "8px 12px",
              boxShadow: "0 8px 24px rgba(0,0,0,0.65), 0 0 10px rgba(59,130,246,0.25)",
              maxWidth: "320px",
              fontFamily: "var(--font-sans, system-ui, sans-serif)",
            }}
          >
            <div
              style={{
                display: "flex",
                alignItems: "center",
                gap: "6px",
                marginBottom: "4px",
              }}
            >
              <span
                style={{
                  fontSize: "9px",
                  textTransform: "uppercase",
                  fontWeight: 700,
                  letterSpacing: "0.5px",
                  padding: "2px 6px",
                  borderRadius: "3px",
                  background:
                    tooltip.type === "Page"
                      ? "rgba(64, 158, 255, 0.25)"
                      : tooltip.type === "Memory"
                      ? "rgba(199, 133, 200, 0.25)"
                      : tooltip.type === "Task"
                      ? "rgba(230, 162, 60, 0.25)"
                      : "rgba(255, 255, 255, 0.15)",
                  color:
                    tooltip.type === "Page"
                      ? "#60a5fa"
                      : tooltip.type === "Memory"
                      ? "#e879f9"
                      : tooltip.type === "Task"
                      ? "#fbbf24"
                      : "#e4e4e7",
                }}
              >
                {tooltip.type}
              </span>
              {tooltip.category && (
                <span
                  style={{
                    fontSize: "10px",
                    color: "#a1a1aa",
                    fontFamily: "monospace",
                  }}
                >
                  [{tooltip.category}]
                </span>
              )}
            </div>
            <div
              style={{
                fontSize: "12px",
                fontWeight: 600,
                color: "#f4f4f5",
                lineHeight: "1.35",
                wordBreak: "break-word",
                marginBottom: "4px",
              }}
            >
              {tooltip.label}
            </div>
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                fontSize: "10px",
                color: "#71717a",
                borderTop: "1px solid rgba(255,255,255,0.08)",
                paddingTop: "4px",
                marginTop: "4px",
              }}
            >
              <span>{tooltip.degree} connected edges</span>
              {tooltip.domain && <span>{tooltip.domain}</span>}
              {tooltip.status && (
                <span
                  style={{
                    color:
                      tooltip.status === "completed"
                        ? "#4ade80"
                        : tooltip.status === "pending"
                        ? "#facc15"
                        : "#f87171",
                  }}
                >
                  {tooltip.status}
                </span>
              )}
            </div>
          </div>
        )}

        {/* Context Menu with Core Protection */}
        {contextMenu && (
          <div
            className="context-menu"
            style={{
              position: "fixed",
              top: contextMenu.y,
              left: contextMenu.x,
              background: "#1c1c1f",
              border: "1px solid #3f3f46",
              borderRadius: "6px",
              padding: "6px",
              zIndex: 1000,
              boxShadow: "0 8px 24px rgba(0,0,0,0.6)",
              minWidth: "160px",
            }}
          >
            <div
              style={{
                padding: "4px 8px",
                fontSize: "11px",
                fontFamily: "monospace",
                borderBottom: "1px solid #333",
                color: "#888",
                marginBottom: "4px",
                wordBreak: "break-all",
              }}
            >
              {contextMenu.nodeId}
            </div>

            {isCoreNode ? (
              <div
                style={{
                  padding: "6px 8px",
                  fontSize: "11px",
                  color: "#facc15",
                  background: "rgba(250, 204, 21, 0.1)",
                  borderRadius: "4px",
                  display: "flex",
                  alignItems: "center",
                  gap: "6px",
                }}
              >
                <span>🔒</span>
                <span>Protected Core Node</span>
              </div>
            ) : (
              <button
                onClick={handleDeleteNode}
                style={{
                  display: "block",
                  width: "100%",
                  textAlign: "left",
                  padding: "6px 10px",
                  background: "none",
                  border: "none",
                  borderRadius: "4px",
                  color: "#f87171",
                  cursor: "pointer",
                  fontSize: "12px",
                  transition: "background 0.15s ease",
                }}
                onMouseEnter={(e) =>
                  (e.currentTarget.style.background = "rgba(248, 113, 113, 0.15)")
                }
                onMouseLeave={(e) =>
                  (e.currentTarget.style.background = "none")
                }
              >
                Archive / Delete Node
              </button>
            )}
          </div>
        )}
      </div>

      <div className="graph-legend">
        {Object.entries(nodeTypesSet).map(([t, c]) => (
          <span key={t} className={`legend-item legend-${t.toLowerCase()}`}>
            <span className="legend-swatch">▮</span> {t} {c}
          </span>
        ))}
        {data?.notes?.centrality?.startsWith("unavailable") && (
          <span className="legend-note">
            centrality unavailable (kg subpackage not vendored)
          </span>
        )}
      </div>
    </div>
  );
}

