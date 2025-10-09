from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ScanIncompleteTasksTool(Tool):
    """Utility to examine the file_check_db for unfinished tasks."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ScanIncompleteTasks",
                "description": "Scans the file_check_db for the first task with 'completed' status set to False.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], file_list_directory: Any = None) -> str:
        db = _convert_db_to_list(data.get("file_check_db", {}).values()
        for task in db:
            if not task.get("completed", True):
                payload = {"task_id": task.get("task_id"), "task": task}
                out = json.dumps(payload)
                return out
        payload = {"task_id": None, "message": "No incomplete tasks found."}
        out = json.dumps(payload)
        return out
