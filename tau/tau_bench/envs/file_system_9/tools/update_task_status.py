# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTaskStatus(Tool):
    """Updates the status of a task in various logs."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_id = kwargs.get("task_id")
        new_status = kwargs.get("new_status")
        for task in data.get("task_logs", []):
            if task.get("task_id") == task_id:
                task["result"] = new_status
                return json.dumps({"status": "success", "message": f"Task {task_id} status updated to {new_status}."})
        for task in data.get("archive_instructions", []):
            if task.get("archive_id") == task_id:
                task["status"] = new_status
                return json.dumps({"status": "success", "message": f"Task {task_id} status updated to {new_status}."})
        for task in data.get("directories", []):
             if task.get("operation_id") == task_id:
                return json.dumps({"status": "success", "message": f"Task {task_id} status noted as {new_status}."})
        return json.dumps({"error": f"Task not found: {task_id}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_task_status",
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
