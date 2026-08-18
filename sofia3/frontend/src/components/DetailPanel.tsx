import React, { useEffect, useState } from "react";
import type { MemoryDetail, PageDetail, SelectedNode, TaskRecord } from "../api";

interface Props {
  selected: SelectedNode | null;
}

interface TaskFetch {
  task: TaskRecord;
}

/**
 * Detail pane: Fetches full content for pages, memories, tasks, and renders
 * structured JSON viewers and metadata for complex node types.
 */
export function DetailPanel({ selected }: Props) {
  const [page, setPage] = useState<PageDetail | null>(null);
  const [memory, setMemory] = useState<MemoryDetail | null>(null);
  const [task, setTask] = useState<TaskRecord | null>(null);
  const [loading, setLoading] = useState(false);

  const key = selected ? `${selected.type}:${selected.id}` : "none";

  useEffect(() => {
    setPage(null);
    setMemory(null);
    setTask(null);
    setLoading(false);
    if (!selected) return;

    if (selected.type === "Page") {
      const slug = selected.id.replace(/^page:/, "");
      setLoading(true);
      fetch(`/api/wiki/page/${encodeURIComponent(slug)}`)
        .then((r) => r.json())
        .then((d) => setPage(d.page ?? null))
        .catch(() => setPage(null))
        .finally(() => setLoading(false));
    } else if (selected.type === "Memory") {
      const uid = selected.id.replace(/^memory:/, "");
      setLoading(true);
      fetch(`/api/wiki/memory/${encodeURIComponent(uid)}`)
        .then((r) => r.json())
        .then((d) => setMemory(d.memory ?? null))
        .catch(() => setMemory(null))
        .finally(() => setLoading(false));
    } else if (selected.type === "Task") {
      const tid = selected.id.replace(/^task:/, "");
      const stream = (selected.properties?.status as string | undefined) ?? "pending";
      setTask({
        task_id: tid,
        status: stream,
        target_node: (selected.properties?.target_node as string | undefined) ?? "?",
        timestamp: Number(selected.properties?.timestamp ?? 0),
        prompt: selected.content,
      });
      fetch(`/api/tasks/${encodeURIComponent(tid)}`)
        .then((r) => (r.ok ? r.json() : null))
        .then((d: TaskFetch | null) => d && setTask(d.task))
        .catch(() => {});
    }
  }, [key, selected]);

  if (!selected) {
    return (
      <div className="detail-pane">
        <div className="panel-title">DETAIL // NO SELECTION</div>
        <div className="empty">SELECT A NODE OR TASK TO INSPECT FULL METADATA</div>
      </div>
    );
  }

  const props = selected.properties ?? {};
  const metaRows = Object.entries(props).filter(([, v]) => v !== "" && v != null);

  let editCommand = "";
  if (selected.type === "Page") {
    editCommand = `reins wiki edit ${selected.id.replace(/^page:/, "")}`;
  } else if (selected.type === "Memory") {
    editCommand = `reins wiki edit ${selected.id.replace(/^memory:/, "")}`;
  } else if (selected.type === "Task") {
    editCommand = `reins trail update ${selected.id.replace(/^task:/, "")} --status success`;
  } else if (selected.type === "Skill" && props.path) {
    editCommand = `vim ${props.path}`;
  }

  const editBlock = editCommand ? (
    <div className="edit-helper">
      <div className="text-dim text-xs">EDIT VIA CLI</div>
      <code className="text-accent">{editCommand}</code>
    </div>
  ) : null;

  let body: React.ReactNode = null;
  if (selected.type === "Page") {
    body = loading ? (
      <div className="empty">LOADING PAGE…</div>
    ) : page ? (
      <pre className="markdown-body">{page.content}</pre>
    ) : (
      <div className="empty">PAGE NOT FOUND</div>
    );
  } else if (selected.type === "Memory") {
    body = loading ? (
      <div className="empty">LOADING MEMORY…</div>
    ) : memory ? (
      <pre className="markdown-body">{memory.text}</pre>
    ) : (
      <div className="empty">MEMORY NOT FOUND</div>
    );
  } else if (selected.type === "Task") {
    body = task ? <TaskDetail task={task} props={props} /> : <div className="empty">LOADING TASK…</div>;
  } else {
    body = (
      <div>
        <div className="meta-grid">
          {metaRows.map(([k, v]) => (
            <div key={k} className="meta-row">
              <span className="meta-key">{k}</span>
              <span className="meta-val">
                {typeof v === "object" ? JSON.stringify(v, null, 2) : String(v)}
              </span>
            </div>
          ))}
        </div>
        {metaRows.some(([, v]) => typeof v === "object") && (
          <div className="json-tree-container">
            <div className="panel-title" style={{ marginTop: 14 }}>RAW JSON TELEMETRY</div>
            <pre className="json-block">{JSON.stringify(props, null, 2)}</pre>
          </div>
        )}
      </div>
    );
  }

  return (
    <div className="detail-pane">
      <div className="panel-title detail-title">
        <span>{selected.type.toUpperCase()} // {selected.content ?? selected.id}</span>
      </div>
      <div className="detail-meta">
        <span className="status-chip">{selected.type}</span>
        {metaRows.slice(0, 3).map(([k, v]) => (
          <span key={k} className="meta-inline">
            {k}={typeof v === "object" ? "{…}" : String(v)}
          </span>
        ))}
      </div>
      <div className="scroll-body">
        {editBlock}
        {body}
      </div>
    </div>
  );
}

function formatTime(ts: number | undefined): string {
  if (!ts) return "—";
  return new Date(ts * 1000).toLocaleString([], { hour12: false });
}

function TaskDetail({ task, props }: { task: TaskRecord; props: Record<string, unknown> }) {
  const rows: [string, string][] = [
    ["status", task.status ?? "—"],
    ["node", task.target_node ?? "—"],
    ["time", formatTime(task.timestamp)],
    ["type", (task.task_type as string | undefined) ?? (props.task_type as string | undefined) ?? "—"],
    ["attempts", (task.attempts as string | number | undefined)?.toString() ?? "—"],
    ["breaker", (task.breaker_state as string | undefined) ?? "—"],
  ];
  return (
    <div>
      <div className="meta-grid">
        {rows.map(([k, v]) => (
          <div key={k} className="meta-row">
            <span className="meta-key">{k}</span>
            <span className={`meta-val${k === "status" ? ` status-chip ${String(v).toLowerCase()}` : ""}`}>{v}</span>
          </div>
        ))}
      </div>
      <div className="panel-title" style={{ marginTop: 18 }}>PROMPT</div>
      <pre className="markdown-body prompt-body">{(task.prompt as string | undefined) ?? "—"}</pre>
    </div>
  );
}
