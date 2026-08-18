import { useState } from "react";
import GridLayout, { useContainerWidth, type Layout, type LayoutItem } from "react-grid-layout";
import "react-grid-layout/css/styles.css";
import { useAppDispatch, useAppSelector, useLiveBridge } from "./store";
import { setNav, setSelected, toggleWidget, NavTab } from "./store/uiSlice";
import { GraphView } from "./views/Graph";
import { DetailPanel } from "./components/DetailPanel";
import { HardwareWidget } from "./components/widgets/HardwareWidget";
import { OmniRouterWidget } from "./components/widgets/OmniRouterWidget";
import { PonHealthWidget } from "./components/widgets/PonHealthWidget";
import { CoordWidget } from "./components/widgets/CoordWidget";
import { TasksWidget } from "./components/widgets/TasksWidget";

const defaultLayouts: LayoutItem[] = [
  { i: "graph", x: 0, y: 0, w: 7, h: 10, minW: 4, minH: 6 },
  { i: "detail", x: 7, y: 0, w: 5, h: 10, minW: 3, minH: 6 },
  { i: "tasks", x: 0, y: 10, w: 6, h: 8, minW: 3, minH: 4 },
  { i: "hardware", x: 6, y: 10, w: 6, h: 8, minW: 3, minH: 4 },
  { i: "routing", x: 0, y: 18, w: 6, h: 8, minW: 3, minH: 4 },
  { i: "pon", x: 6, y: 18, w: 3, h: 8, minW: 2, minH: 4 },
  { i: "coord", x: 9, y: 18, w: 3, h: 8, minW: 2, minH: 4 },
];

export default function App() {
  const dispatch = useAppDispatch();
  const { connected } = useLiveBridge();
  const { width, containerRef } = useContainerWidth();
  const trail = useAppSelector((state) => state.trail);
  const health = useAppSelector((state) => state.ui.health);
  const nav = useAppSelector((state) => state.ui.nav);
  const selected = useAppSelector((state) => state.ui.selected);
  const visibleWidgets = useAppSelector((state) => state.ui.visibleWidgets);

  const [layout, setLayout] = useState<Layout>(() => {
    try {
      const saved = localStorage.getItem("sofia3_grid_layout");
      return saved ? JSON.parse(saved) : defaultLayouts;
    } catch {
      return defaultLayouts;
    }
  });

  const onLayoutChange = (newLayout: Layout) => {
    setLayout(newLayout);
    try {
      localStorage.setItem("sofia3_grid_layout", JSON.stringify(newLayout));
    } catch {
      /* ignore */
    }
  };


  const live = connected && trail.lastUpdated !== null;

  return (
    <div className="app-shell">
      <header className="topbar">
        <div className="brand">
          SOFIA<span className="slash">³</span> // KERNEL MONITOR
        </div>
        <div className="widget-toggles">
          <button
            className={`btn-toggle ${visibleWidgets.graph ? "active" : ""}`}
            onClick={() => dispatch(toggleWidget("graph"))}
          >
            [+ GRAPH]
          </button>
          <button
            className={`btn-toggle ${visibleWidgets.tasks ? "active" : ""}`}
            onClick={() => dispatch(toggleWidget("tasks"))}
          >
            [+ TASKS]
          </button>
          <button
            className={`btn-toggle ${visibleWidgets.hardware ? "active" : ""}`}
            onClick={() => dispatch(toggleWidget("hardware"))}
          >
            [+ HARDWARE]
          </button>
          <button
            className={`btn-toggle ${visibleWidgets.routing ? "active" : ""}`}
            onClick={() => dispatch(toggleWidget("routing"))}
          >
            [+ ROUTER]
          </button>
          <button
            className={`btn-toggle ${visibleWidgets.pon ? "active" : ""}`}
            onClick={() => dispatch(toggleWidget("pon"))}
          >
            [+ PON]
          </button>
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
            ["hardware", "HARDWARE"],
            ["routing", "ROUTER MATRIX"],
            ["pon", "PON HEALTH"],
          ] as const
        ).map(([id, label]) => (
          <button
            key={id}
            className={`nav-tab${nav === id ? " active" : ""}`}
            onClick={() => dispatch(setNav(id as NavTab))}
          >
            {label}
          </button>
        ))}
      </nav>

      <div className="main grid-main" ref={containerRef as any}>
        {width > 0 && (
          <GridLayout
            className="layout"
            layout={layout}
            gridConfig={{ cols: 12, rowHeight: 30 }}
            dragConfig={{ handle: ".widget-header, .panel-title", enabled: true }}
            resizeConfig={{ enabled: true }}
            width={width}
            onLayoutChange={onLayoutChange}
          >

            {visibleWidgets.graph && (
              <div key="graph" className="grid-item">
                <GraphView
                  trail={trail.tasks.length ? { kind: "trail", tasks: trail.tasks, summary: trail.summary, total: trail.total } : null}
                  onSelect={(node) => dispatch(setSelected(node))}
                  nav={nav === "hardware" || nav === "routing" || nav === "pon" ? "unified" : nav}
                />
              </div>
            )}

            {visibleWidgets.detail && (
              <div key="detail" className="grid-item">
                <DetailPanel selected={selected} />
              </div>
            )}

            {visibleWidgets.tasks && (
              <div key="tasks" className="grid-item">
                <TasksWidget />
              </div>
            )}

            {visibleWidgets.hardware && (
              <div key="hardware" className="grid-item">
                <HardwareWidget />
              </div>
            )}

            {visibleWidgets.routing && (
              <div key="routing" className="grid-item">
                <OmniRouterWidget />
              </div>
            )}

            {visibleWidgets.pon && (
              <div key="pon" className="grid-item">
                <PonHealthWidget />
              </div>
            )}

            {visibleWidgets.coord && (
              <div key="coord" className="grid-item">
                <CoordWidget />
              </div>
            )}
          </GridLayout>
        )}
      </div>
    </div>
  );
}


