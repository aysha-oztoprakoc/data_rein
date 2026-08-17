/* Shared API types for the Sofia³ frontend. */

export interface TaskRecord {
  task_id: string;
  status: string;
  target_node: string;
  timestamp: number;
  task_type?: string;
  prompt?: string;
  record_json?: string;
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

export type View = "tasks" | "wiki" | "graph";