# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogTaskCompletionTool(Tool):
    """Logs the completion details of a task to a central log."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_task_completion",
                "description": "Logs the result and notes of a completed task to the task_log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "task_name": {"type": "string"},
                        "result": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["task_id", "task_name", "result"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if "task_log" not in data:
            data["task_log"] = []
        log = {**kwargs}
        data["task_log"].append(log)
        return json.dumps({"status": "logged", "entry": log})
