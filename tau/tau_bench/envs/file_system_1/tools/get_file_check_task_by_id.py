# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFileCheckTaskByID(Tool):
    """Retrieves a specific file check task by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], task_id) -> str:
        for task in data.get('file_check_db', []):
            if task.get('task_id') == task_id:
                return json.dumps(task)
        return json.dumps({"error": f"File check task with ID '{task_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_file_check_task_by_id", "description": "Fetches the full details and parsed instructions for a file check task by its ID.", "parameters": {"type": "object", "properties": {"task_id": {"type": "string", "description": "The unique ID of the file check task (e.g., 'fc_task_001')."}}, "required": ["task_id"]}}}
