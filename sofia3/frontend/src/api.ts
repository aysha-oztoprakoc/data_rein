/* Shared API types for the Sofia³ frontend. */

export interface TaskRecord {
  task_id: string;
  status: string;
  target_node: string;
  timestamp: number;
  task_type?: string;
  prompt?: string;
  attempts?: number | string;
  breaker_state?: string;
  [key: string]: unknown;
}

export interface TrailSnapshot {
  kind: "trail" | "heartbeat";
  tasks?: TaskRecord[];
  summary?: Record<string, number>;
  total?: number;
}

export interface Health {
  status: string;
  service: string;
  version: string;
  degraded: boolean;
}

/* ------------------------------------------------------------------ graph */
export interface GraphNode {
  id: string;
  type: string;
  /** display title / short content */
  content?: string;
  properties?: Record<string, unknown>;
  metadata?: Record<string, unknown>;
}

export interface GraphEdge {
  id?: string;
  source: string;
  target: string;
  type: string;
  weight?: number;
}

export interface GraphData {
  nodes: GraphNode[];
  edges: GraphEdge[];
}

export interface GraphStats {
  node_count?: number;
  edge_count?: number;
  node_types?: Record<string, number>;
  edge_types?: Record<string, number>;
  density?: number;
}

export interface GraphNotes {
  pages?: number;
  memories?: number;
  tasks?: number;
  models?: number;
  centrality?: string;
  communities?: string;
}

export interface ApiGraphResponse {
  graph?: GraphData;
  stats?: GraphStats;
  notes?: GraphNotes;
  degraded?: boolean;
  built_at?: number;
  ttl?: number;
}

/* ---------------------------------------------------- detail (full bodies) */
export interface PageDetail {
  slug: string;
  title: string;
  content: string;
  category: string;
  owner: string;
  source_path?: string;
  metadata_json?: string;
  updated_at?: string;
}

export interface MemoryDetail {
  uid: string;
  text: string;
  category: string;
  owner: string;
  source?: string;
  session_id?: string;
  timestamp?: string;
}

export type SelectedKind = "Page" | "Memory" | "Task" | "Agent" | "Owner" | "Category" | "Model" | "Session";

export interface SelectedNode {
  id: string;
  type: string;
  content?: string;
  properties?: Record<string, unknown>;
}