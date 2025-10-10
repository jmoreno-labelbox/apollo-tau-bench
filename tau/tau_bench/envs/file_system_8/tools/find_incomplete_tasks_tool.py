# Copyright Sierra

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

        # Locate first task where completed flag is False
        incomplete_task = next(
            (entry for entry in database if not entry.get("completed", True)),
            None
        )

        if incomplete_task:
            # Provide task details for downstream processing
            return json.dumps({
                "task_id": incomplete_task.get("task_id"),
                "task": incomplete_task
            })

        return json.dumps({
            "task_id": None,
            "message": "No incomplete tasks found."
        })
