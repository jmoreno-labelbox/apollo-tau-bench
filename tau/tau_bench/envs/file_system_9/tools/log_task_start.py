# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogTaskStart(Tool):
    """Logs the start of a new task in task_logs.json."""
    @staticmethod
    def invoke(data: Dict[str, Any], task_id, task_type, user_id) -> str:

        new_task_log = {
            "task_id": task_id,
            "task_type": task_type,
            "user_id": user_id,
            "result": "in_progress",
            "started_at": "2025-08-13T01:01:01Z", # Emulated timestamp
            "notes": "Task initiated by agent."
        }
        data["task_logs"].append(new_task_log)
        return json.dumps({"status": "success", "message": f"Task {task_id} logged as in_progress."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_task_start",
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
