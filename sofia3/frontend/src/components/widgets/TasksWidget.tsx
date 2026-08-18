import { useState } from "react";

import { useAppDispatch, useAppSelector } from "../../store";
import { setSelected } from "../../store/uiSlice";
import type { TaskRecord } from "../../api";

export function TasksWidget() {
  const dispatch = useAppDispatch();
  const tasks = useAppSelector((state) => state.trail.tasks);
  const summary = useAppSelector((state) => state.trail.summary);
  const [filter, setFilter] = useState<string>("all");

  const filteredTasks = tasks.filter((t) => {
    if (filter === "all") return true;
    return String(t.status).toLowerCase() === filter.toLowerCase();
  });

  const handleSelectTask = (task: TaskRecord) => {
    dispatch(
      setSelected({
        id: task.task_id,
        type: "Task",
        content: task.title || task.prompt || task.task_type || task.task_id,
        properties: task,
      })
    );
  };

  return (
    <div className="widget-card tasks-widget">
      <div className="widget-header">
        <span className="widget-title">UNIVERSAL TASK TRAIL // LIVE FEED</span>
        <div className="task-summary-badges">
          <span
            className={`pill ${filter === "all" ? "pill-active" : ""}`}
            onClick={() => setFilter("all")}
          >
            ALL ({tasks.length})
          </span>
          {Object.entries(summary).map(([st, cnt]) => (
            <span
              key={st}
              className={`pill pill-${st} ${filter === st ? "pill-active" : ""}`}
              onClick={() => setFilter(st)}
            >
              {st.toUpperCase()} ({cnt})
            </span>
          ))}
        </div>
      </div>
      <div className="widget-body task-list-scroll">
        {filteredTasks.length === 0 ? (
          <div className="text-dim empty-msg">No tasks matching active filter.</div>
        ) : (
          filteredTasks.slice(0, 50).map((task) => (
            <div
              key={task.task_id}
              className={`task-row status-${String(task.status).toLowerCase()}`}
              onClick={() => handleSelectTask(task)}
            >
              <div className="task-left">
                <span className={`task-badge badge-${String(task.status).toLowerCase()}`}>
                  {String(task.status).toUpperCase()}
                </span>
                <span className="task-type">{task.task_type || "task"}</span>
              </div>
              <div className="task-center">
                <span className="task-prompt">{task.title || task.prompt || task.task_id}</span>
              </div>
              <div className="task-right">
                <span className="task-node">{task.target_node || "amdy"}</span>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
