# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ScanIncompleteTasksTool(Tool):
    """Tool to scan the file_check_db for tasks that are not yet completed."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "scan_incomplete_tasks",
                "description": "Scans the file_check_db for the first task with 'completed' status set to False.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        db = data.get("file_check_db", [])
        for task in db:
            if not task.get("completed", True):
                # return the task identifier and information for the caller to determine whether to continue or cancel
                return json.dumps({"task_id": task.get("task_id"), "task": task})
        return json.dumps({"task_id": None, "message": "No incomplete tasks found."})
