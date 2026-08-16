import hashlib
import time
from typing import Optional

from reins.services.task_trail import TaskTrail

class RLMHandle:
    def __init__(self, task_id: str, tier: str, background: bool):
        self.task_id = task_id
        self.tier = tier
        self.background = background
        self.status = "queued"

    def __repr__(self):
        return f"<RLMHandle task_id='{self.task_id}' tier='{self.tier}' status='{self.status}'>"

def rlm(prompt: str, tier: str = "rlm-worker-fast", background: bool = True, name: Optional[str] = None) -> RLMHandle:
    """
    Programmatic subagent delegation using the Prime Agent RLM paradigm.
    Instead of relying on an orchestrator LLM to write text commands, 
    this function injects a subagent task directly into the TaskTrail.
    
    Args:
        prompt: The task instruction for the subagent.
        tier: The capability tier to route to (e.g. rlm-worker-fast, rlm-worker-heavy)
        background: If True, returns immediately without waiting for completion.
        name: Optional custom name for the task.
        
    Returns:
        RLMHandle representing the background task.
    """
    task_id = name or f"rlm-{hashlib.sha256(prompt.encode()).hexdigest()[:8]}-{int(time.time())}"
    
    trail = TaskTrail()
    trail.upsert_task(
        task_id=task_id,
        task_type=tier,
        prompt=prompt,
        status="pending"
    )
    
    return RLMHandle(task_id, tier, background)
