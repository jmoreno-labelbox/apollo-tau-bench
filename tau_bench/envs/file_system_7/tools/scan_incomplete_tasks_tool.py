from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

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
        db = data.get("file_check_db", [])
        for task in db:
            if not task.get("completed", True):
                payload = {"task_id": task.get("task_id"), "task": task}
                out = json.dumps(payload)
                return out
        payload = {"task_id": None, "message": "No incomplete tasks found."}
        out = json.dumps(payload)
        return out
