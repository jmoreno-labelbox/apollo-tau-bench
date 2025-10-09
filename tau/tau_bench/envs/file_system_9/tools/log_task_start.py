from tau_bench.envs.tool import Tool
import json
from typing import Any

class LogTaskStart(Tool):
    """Records the initiation of a new task in task_logs.json."""

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, user_id: str = None, task_type: str = None) -> str:
        new_task_log = {
            "task_id": task_id,
            "task_type": task_type,
            "user_id": user_id,
            "result": "in_progress",
            "started_at": "2025-08-13T01:01:01Z",  # Emulated timestamp
            "notes": "Task initiated by agent.",
        }
        data["task_logs"].append(new_task_log)
        payload = {"status": "success", "message": f"Task {task_id} logged as in_progress."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogTaskStart",
                "description": "Logs the start of a new task in task_logs.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "task_type": {"type": "string"},
                    },
                    "required": ["task_id", "user_id", "task_type"],
                },
            },
        }
