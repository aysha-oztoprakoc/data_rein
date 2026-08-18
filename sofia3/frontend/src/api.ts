/* Shared API types for the Sofia³ frontend. */

export interface TaskRecord {
  task_id: string;
  status: string;
  title?: string;
  target_node?: string;
  timestamp?: number;
  task_type?: string;
  prompt?: string;
  attempts?: number | string;
  breaker_state?: string;
  parent_task_id?: string | null;
  is_archived?: boolean;
  [key: string]: unknown;
}

export interface HardwareNode {
  gpu?: string;
  vram_gb?: number;
  ram_gb?: number;
  cpu?: string;
  cores?: number;
  [key: string]: unknown;
}

export interface ClusterProfile {
  nodes?: Record<string, HardwareNode>;
  summary?: Record<string, unknown>;
  [key: string]: unknown;
}

export interface ComboItem {
  id: string;
  provider: string;
  model: string;
  tier: string;
  node: string;
}

export interface ModelCategoryItem {
  description?: string;
  amdy: string[];
  tell: string[];
  cloud: string[];
}

export interface TokenWindowUsage {
  used_tokens?: number;
  budget_tokens?: number;
  percent?: number;
  call_count?: number;
}

export interface TokenBudgetReport {
  windows?: Record<string, TokenWindowUsage>;
  providers?: Record<string, Record<string, number>>;
  total_calls?: number;
  [key: string]: unknown;
}

export interface CoordinatorStatus {
  active_model?: string | null;
  busy?: boolean;
  vram_allocated_mb?: number;
  loaded_models?: string[];
  [key: string]: unknown;
}

export interface PonHealth {
  zero_polling: boolean;
  inotify_active: boolean;
  mqtt_active: boolean;
  timestamp: number;
}

export interface TelemetrySnapshot {
  hardware?: ClusterProfile;
  hardware_gaps?: Record<string, unknown>;
  combos?: ComboItem[];
  categories?: Record<string, ModelCategoryItem>;
  tokens?: TokenBudgetReport;
  coord?: CoordinatorStatus;
  agent_budgets?: Record<string, unknown>;
  training?: Record<string, unknown>;
  pon?: PonHealth;
}

export interface TrailSnapshot {
  kind: "trail" | "heartbeat";
  tasks?: TaskRecord[];
  summary?: Record<string, number>;
  total?: number;
  telemetry?: TelemetrySnapshot;
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