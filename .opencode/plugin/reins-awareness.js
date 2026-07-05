// Passive Task Trail bookkeeping for OpenCode sessions running inside the
// data_rein harness. This is deliberately separate from the `reins` MCP tools
// (mcp_server.py): those are things the agent chooses to call; this plugin
// logs session start/end automatically, so other harness agents
// (data-agy/data-hermes/data-ody) see an OpenCode session in `reins trail list`
// even if the agent itself never touches the trail.
//
// One Task Trail entry per OpenCode session, keyed by sessionID -> task_id.

const sessionTasks = new Map();

const PY = ".venv/bin/python";

async function trailCreate($, directory, sessionID, title) {
  try {
    const result = await $`${PY} -c ${
      "import sys; from reins.services.task_trail import TaskTrail; " +
      "t = TaskTrail(); print(t.create_task('opencode:session', sys.argv[1], 'amdy'))"
    } ${title || sessionID}`.cwd(directory).quiet();
    const taskId = result.stdout.toString().trim();
    if (taskId) sessionTasks.set(sessionID, taskId);
  } catch {
    // Graceful degradation: never let trail bookkeeping break a session.
  }
}

async function trailUpdate($, directory, sessionID, status) {
  const taskId = sessionTasks.get(sessionID);
  if (!taskId) return;
  try {
    await $`${PY} -c ${
      "import sys; from reins.services.task_trail import TaskTrail; " +
      "TaskTrail().update_task(sys.argv[1], sys.argv[2])"
    } ${taskId} ${status}`.cwd(directory).quiet();
  } catch {
    // Graceful degradation.
  }
}

export const ReinsAwarenessPlugin = async ({ $, directory }) => {
  return {
    event: async ({ event }) => {
      if (event.type === "session.created") {
        const { info } = event.properties;
        await trailCreate($, directory, info.id, info.title);
      } else if (event.type === "session.idle") {
        await trailUpdate($, directory, event.properties.sessionID, "success");
      } else if (event.type === "session.error") {
        await trailUpdate($, directory, event.properties.sessionID, "failed");
      } else if (event.type === "session.deleted") {
        sessionTasks.delete(event.properties.info.id);
      }
    },
  };
};
