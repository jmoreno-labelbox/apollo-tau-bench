# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTaskHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_id = kwargs.get("task_id")

        if not task_id:
            return json.dumps({"error": "task_id is required"})

        task_history = data.get("task_history", [])

        history_entries = [h for h in task_history if h.get("task_id") == task_id]

        history_entries.sort(key=lambda x: x.get("timestamp", ""))

        return json.dumps(
            {
                "task_id": task_id,
                "history_count": len(history_entries),
                "history": history_entries,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_task_history",
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
