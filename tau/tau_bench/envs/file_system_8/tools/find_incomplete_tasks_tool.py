# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindIncompleteTasksTool(Tool):
    """Utility for discovering pending tasks within the file_check_db."""

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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        database = data.get("file_check_db", [])

        # Find the initial task with the completed flag set to False.
        incomplete_task = next(
            (entry for entry in database if not entry.get("completed", True)),
            None
        )

        if incomplete_task:
            # Supply task specifications for subsequent processing.
            return json.dumps({
                "task_id": incomplete_task.get("task_id"),
                "task": incomplete_task
            })

        return json.dumps({
            "task_id": None,
            "message": "No incomplete tasks found."
        })
