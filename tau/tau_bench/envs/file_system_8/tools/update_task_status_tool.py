from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class UpdateTaskStatusTool(Tool):
    """Modifies the status of a task in the file_check_db."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTaskStatus",
                "description": "Updates the 'completed' field for a task in the file_check_db.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "completed": {"type": "boolean"},
                    },
                    "required": ["task_id", "completed"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str, completed: bool) -> str:
        task = next(
            (t for t in data.get("file_check_db", []) if t["task_id"] == task_id), None
        )
        if task:
            task["completed"] = completed
            payload = {"status": "success", "task_id": task_id, "completed": completed}
            out = json.dumps(payload)
            return out
        payload = {"error": f"Task ID {task_id} not found."}
        out = json.dumps(payload)
        return out
