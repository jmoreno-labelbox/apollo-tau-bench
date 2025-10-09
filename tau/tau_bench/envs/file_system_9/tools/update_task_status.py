from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateTaskStatus(Tool):
    """Modifies the status of a task across different logs."""

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, new_status: str = None) -> str:
        for task in data.get("task_logs", []):
            if task.get("task_id") == task_id:
                task["result"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Task {task_id} status updated to {new_status}.",
                }
                out = json.dumps(payload)
                return out
        for task in data.get("archive_instructions", []):
            if task.get("archive_id") == task_id:
                task["status"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Task {task_id} status updated to {new_status}.",
                }
                out = json.dumps(payload)
                return out
        for task in data.get("directories", []):
            if task.get("operation_id") == task_id:
                payload = {
                    "status": "success",
                    "message": f"Task {task_id} status noted as {new_status}.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Task not found: {task_id}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTaskStatus",
                "description": "Updates the status of a task in various logs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["task_id", "new_status"],
                },
            },
        }
