from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class FindIncompleteTasksTool(Tool):
    """Tool for identifying pending tasks in the file_check_db."""

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
    def invoke(data: dict[str, Any], file_check_db: list = None) -> str:
        database = file_check_db if file_check_db is not None else []

        # Find the initial task with a completed flag set to False
        incomplete_task = next(
            (entry for entry in database if not entry.get("completed", True)), None
        )

        if incomplete_task:
            payload = {"task_id": incomplete_task.get("task_id"), "task": incomplete_task}
            out = json.dumps(payload)
            return out
        payload = {"task_id": None, "message": "No incomplete tasks found."}
        out = json.dumps(payload)
        return out
