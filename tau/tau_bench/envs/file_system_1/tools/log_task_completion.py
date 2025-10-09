from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LogTaskCompletion(Tool):
    """Generates a log entry for a task that has been successfully completed."""

    @staticmethod
    def invoke(data: dict[str, Any], task_type: str = None, task_id: str = None, user_id: str = None) -> str:
        task_logs = data.get("task_logs", [])

        # Automatically create notes according to the type of task
        if task_type == "archive":
            notes = f"Archive task {task_id} completed successfully"
        elif task_type == "file_check":
            notes = f"File check task {task_id} completed successfully"
        elif task_type == "file_organization":
            notes = f"File organization task {task_id} completed successfully"
        else:
            notes = f"{task_type.title()} task {task_id} completed successfully"

        new_log = {
            "task_id": task_id,
            "task_type": task_type,
            "user_id": user_id,
            "result": "success",
            "completed_at": "2024-01-20T13:00:00Z",
            "notes": notes,
        }
        task_logs.append(new_log)
        data["task_logs"] = task_logs
        payload = new_log
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogTaskCompletion",
                "description": "Writes a record to the main task log for a successfully completed task.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "task_type": {"type": "string"},
                        "user_id": {"type": "string"},
                    },
                    "required": ["task_id", "task_type", "user_id"],
                },
            },
        }
