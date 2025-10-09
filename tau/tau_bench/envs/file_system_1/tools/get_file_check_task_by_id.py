from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetFileCheckTaskByID(Tool):
    """Fetches a specific file check task using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None) -> str:
        for task in data.get("file_check_db", {}).values():
            if task.get("task_id") == task_id:
                payload = task
                out = json.dumps(payload)
                return out
        payload = {"error": f"File check task with ID '{task_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFileCheckTaskById",
                "description": "Fetches the full details and parsed instructions for a file check task by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The unique ID of the file check task (e.g., 'fc_task_001').",
                        }
                    },
                    "required": ["task_id"],
                },
            },
        }
