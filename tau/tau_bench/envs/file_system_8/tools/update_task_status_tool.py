# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTaskStatusTool(Tool):
    """Updates the status of a task in the file_check_db."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_task_status",
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
    def invoke(data: Dict[str, Any], completed, task_id) -> str:
        task_id, completed = task_id, completed
        task = next(
            (t for t in data.get("file_check_db", []) if t["task_id"] == task_id), None
        )
        if task:
            task["completed"] = completed
            return json.dumps(
                {"status": "success", "task_id": task_id, "completed": completed}
            )
        return json.dumps({"error": f"Task ID {task_id} not found."})
