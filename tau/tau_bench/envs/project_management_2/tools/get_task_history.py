from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetTaskHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None) -> str:
        if not task_id:
            payload = {"error": "task_id is required"}
            out = json.dumps(payload)
            return out

        task_history = data.get("task_history", [])

        history_entries = [h for h in task_history if h.get("task_id") == task_id]

        history_entries.sort(key=lambda x: x.get("timestamp", ""))
        payload = {
                "task_id": task_id,
                "history_count": len(history_entries),
                "history": history_entries,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTaskHistory",
                "description": "Get the history of changes for a task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to get history for",
                        }
                    },
                    "required": ["task_id"],
                },
            },
        }
