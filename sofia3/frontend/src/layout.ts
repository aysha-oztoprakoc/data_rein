import { useEffect, useState } from "react";
import {
  forceCenter,
  forceCollide,
  forceLink,
  forceManyBody,
  forceSimulation,
} from "d3-force";
import type { GraphData } from "./api";

export interface LayoutResult {
  positions: Record<string, { x: number; y: number }>;
  width: number;
  height: number;
}

/**
 * Compute a force-directed layout.
 * Seeds existing positions to prevent visual jumping and unnecessary re-calculation.
 */
export function computeLayout(
  data: GraphData,
  width = 1600,
  height = 1000,
  existingPositions?: Record<string, { x: number; y: number }>
): LayoutResult {
  const nodes = data.nodes ?? [];
  const edges = data.edges ?? [];

  if (nodes.length === 0) {
    return { positions: {}, width, height };
  }

  // Check if all nodes already have positions
  if (existingPositions && Object.keys(existingPositions).length > 0) {
    const missingNodes = nodes.filter((n) => !existingPositions[n.id]);
    if (missingNodes.length === 0) {
      return { positions: existingPositions, width, height };
    }
  }

  interface SimNode {
    id: string;
    x: number;
    y: number;
    fx?: number;
    fy?: number;
  }

  const simulationNodes: SimNode[] = nodes.map((nd, i) => {
    if (existingPositions && existingPositions[nd.id]) {
      return {
        id: nd.id,
        x: existingPositions[nd.id].x,
        y: existingPositions[nd.id].y,
        // Pin existing nodes so they don't jump around
        fx: existingPositions[nd.id].x,
        fy: existingPositions[nd.id].y,
      };
    }
    // Stable spiral seed for new nodes
    const angle = i * 2.399963;
    const radius = Math.sqrt(i) * 22;
    return {
      id: nd.id,
      x: width / 2 + Math.cos(angle) * radius,
      y: height / 2 + Math.sin(angle) * radius,
    };
  });

  const nodeById = new Map(simulationNodes.map((s) => [s.id, s]));

  const links: { source: string; target: string }[] = edges
    .filter((e) => nodeById.has(e.source) && nodeById.has(e.target))
    .map((e) => ({ source: e.source, target: e.target }));

  const hasNewNodes = existingPositions && Object.keys(existingPositions).length > 0;
  const tickCount = hasNewNodes ? 30 : 80;

  const simulation = forceSimulation(simulationNodes)
    .force("charge", forceManyBody().strength(-55))
    .force(
      "link",
      forceLink<SimNode, { source: string; target: string }>(links)
        .id((d) => d.id)
        .distance(70)
        .strength(0.4)
    )
    .force("collide", forceCollide(24))
    .force("center", forceCenter(width / 2, height / 2));

  for (let tick = 0; tick < tickCount; tick++) simulation.tick();
  simulation.stop();

  const positions: Record<string, { x: number; y: number }> = {};
  for (const s of simulationNodes) positions[s.id] = { x: s.x, y: s.y };

  return { positions, width, height };
}

/**
 * Hook to compute layout in a background Web Worker,
 * keeping the main thread responsive with incremental caching.
 */
export function useGraphLayout(graph: GraphData | undefined, width = 1600, height = 1000): LayoutResult {
  const [layout, setLayout] = useState<LayoutResult>(() => ({
    positions: {},
    width,
    height,
  }));

  useEffect(() => {
    if (!graph || (graph.nodes.length === 0 && graph.edges.length === 0)) {
      setLayout({ positions: {}, width, height });
      return;
    }

    // Check if we already have positions for all nodes
    const currentPositions = layout.positions;
    if (currentPositions && graph.nodes.length > 0) {
      const allPresent = graph.nodes.every((n) => currentPositions[n.id] !== undefined);
      if (allPresent && Object.keys(currentPositions).length === graph.nodes.length) {
        return;
      }
    }

    if (typeof Worker === "undefined") {
      setLayout((prev) => computeLayout(graph, width, height, prev.positions));
      return;
    }

    let cancelled = false;
    let worker: Worker | null = null;

    try {
      worker = new Worker(new URL("./layout.worker.ts", import.meta.url), { type: "module" });
      worker.onmessage = (e: MessageEvent<LayoutResult>) => {
        if (!cancelled) {
          setLayout(e.data);
        }
      };
      worker.onerror = () => {
        if (!cancelled) {
          setLayout((prev) => computeLayout(graph, width, height, prev.positions));
        }
      };
      worker.postMessage({ graph, width, height, existingPositions: currentPositions });
    } catch {
      setLayout((prev) => computeLayout(graph, width, height, prev.positions));
    }

    return () => {
      cancelled = true;
      worker?.terminate();
    };
  }, [graph, width, height]);

  return layout;
}
