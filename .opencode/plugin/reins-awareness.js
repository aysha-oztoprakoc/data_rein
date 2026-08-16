// Passive Task Trail bookkeeping for OpenCode sessions running inside the
// data_rein harness. This is deliberately separate from the `reins` MCP tools
// (mcp_server.py): those are things the agent chooses to call; this plugin
// logs session start/end AND each session's executed changes automatically, so
// the Task Trail stays the authoritative record of what agents did even if the
// agent itself never touches the trail.
//
// This is the harness's PERMANENT trail enforcement for plans/executions:
// on session start we snapshot the git HEAD; on session idle we diff that range
// and append the executed commits/files as a step, then mark the session done.
//
// One Task Trail entry per OpenCode session, keyed by sessionID -> task_id.

const sessionTasks = new Map();

const PY = ".venv/bin/python";

function recCall(expr) {
  return (
    "import sys; from reins.services.trail_recorder import TrailRecorder; " +
    "rec = TrailRecorder(); " + expr
  );
}

async function trailCreate($, directory, sessionID, title) {
  try {
    // Non-blocking fire-and-forget execution to preserve PON zero-polling principles
    $`${PY} -c ${
      "import sys; from reins.services.task_trail import TaskTrail; " +
      "t = TaskTrail(); print(t.create_task('opencode:session', sys.argv[1], 'amdy'))"
    } ${title || sessionID}`.cwd(directory).quiet().then(result => {
      const taskId = result.stdout.toString().trim();
      if (taskId) {
        sessionTasks.set(sessionID, { taskId, startCommit: null, startPinned: false });
        // Snapshot git HEAD now so we can attribute commits to THIS session later.
        $`git rev-parse HEAD`.cwd(directory).quiet().then(hr => {
          const entry = sessionTasks.get(sessionID);
          if (entry) { entry.startCommit = hr.stdout.toString().trim() || null; entry.startPinned = true; }
        }).catch(() => {});
      }
    }).catch(() => {});
  } catch {
    // Graceful degradation
  }
}

async function trailRecordExecution($, directory, sessionID) {
  const entry = sessionTasks.get(sessionID);
  const taskId = entry?.taskId;
  if (!taskId) return;
  if (!entry.startPinned) return; // git HEAD snapshot not ready yet; skip gracefully
  try {
    const commits = [];
    if (entry.startCommit) {
      // commits made within this session (start..HEAD); empty if none/new repo
      const logs = await $`git log --oneline ${entry.startCommit}..HEAD`.cwd(directory).quiet()
        .catch(() => { stdout: "" });
      const text = (logs?.stdout || "").toString();
      commits.push(...text.split("\n").map(l => l.trim()).filter(Boolean));
    }
    if (commits.length === 0) return; // nothing executed worth a step
    const summary = `executed ${commits.length} commit(s) this session`;
    $`${PY} -c ${
      recCall(
        "import sys,json; argv=json.loads(sys.argv[1]); " +
        "rec.append_step(argv['task_id'], argv['summary'], commits=argv['commits']); " +
        "print('step recorded')"
      )
    } ${JSON.stringify({ task_id: taskId, summary, commits })}`.cwd(directory).quiet().catch(() => {});
  } catch {
    // Graceful degradation
  }
}

async function trailUpdate($, directory, sessionID, status) {
  const entry = sessionTasks.get(sessionID);
  const taskId = entry?.taskId;
  if (!taskId) return;
  try {
    $`${PY} -c ${
      "import sys; from reins.services.task_trail import TaskTrail; " +
      "TaskTrail().update_task(sys.argv[1], sys.argv[2])"
    } ${taskId} ${status}`.cwd(directory).quiet().catch(() => {});
  } catch {
    // Graceful degradation
  }
}

export const ReinsAwarenessPlugin = async ({ $, directory }) => {
  return {
    event: async ({ event }) => {
      try {
        if (event.type === "session.created") {
          const { info } = event.properties;
          trailCreate($, directory, info.id, info.title);
        } else if (event.type === "session.idle") {
          // record this session's executed commits onto the trail, then mark done
          await trailRecordExecution($, directory, event.properties.sessionID);
          trailUpdate($, directory, event.properties.sessionID, "success");
        } else if (event.type === "session.error") {
          trailUpdate($, directory, event.properties.sessionID, "failed");
        } else if (event.type === "session.deleted") {
          sessionTasks.delete(event.properties.info?.id);
        }
      } catch {
        // Prevent plugin errors from crashing OpenCode event loop
      }
    },
  };
};