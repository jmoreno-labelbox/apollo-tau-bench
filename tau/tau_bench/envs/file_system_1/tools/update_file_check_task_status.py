from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateFileCheckTaskStatus(Tool):
    """Modifies the status of a file check task."""

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, completed: bool = None) -> str:
        for task in data.get("file_check_db", {}).values():
            if task.get("task_id") == task_id:
                task["completed"] = completed
                payload = {"status": "success", "updated_task": task}
                out = json.dumps(payload)
                return out
        payload = {"status": "failure", "error": f"File check task ID '{task_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFileCheckTaskStatus",
                "description": "Updates the completion status of a file check task.",
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
