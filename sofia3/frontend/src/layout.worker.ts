import { computeLayout } from "./layout";
import type { GraphData } from "./api";

self.onmessage = (e: MessageEvent<{ graph: GraphData; width?: number; height?: number; existingPositions?: Record<string, { x: number; y: number }> }>) => {
  const { graph, width, height, existingPositions } = e.data;
  const result = computeLayout(graph, width, height, existingPositions);
  self.postMessage(result);
};
