# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateFileCheckTaskStatus(Tool):
    """Updates the status of a file check task."""
    @staticmethod
    def invoke(data: Dict[str, Any], completed, task_id) -> str:
        is_completed = completed
        for task in data.get('file_check_db', []):
            if task.get('task_id') == task_id:
                task['completed'] = is_completed
                return json.dumps({"status": "success", "updated_task": task})
        return json.dumps({"status": "failure", "error": f"File check task ID '{task_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_file_check_task_status", "description": "Updates the completion status of a file check task.", "parameters": {"type": "object", "properties": {"task_id": {"type": "string"}, "completed": {"type": "boolean"}}, "required": ["task_id", "completed"]}}}
