from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class LogTaskCompletionTool(Tool):
    """Records the completion details of a task in a central log."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogTaskCompletion",
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
    def invoke(
        data: dict[str, Any],
        log_entry: dict[str, Any] = None,
        task_id: Any = None,
        task_name: str = None,
        result: str = None,
        timestamp: str = None,
        notes: str = None, timestamp_format: Any = None, severity: Any = None, include_stack_trace: Any = None) -> str:
        if "task_log" not in data:
            data["task_log"] = []
        log = log_entry
        data["task_log"].append(log)
        payload = {"status": "logged", "entry": log}
        out = json.dumps(payload)
        return out
