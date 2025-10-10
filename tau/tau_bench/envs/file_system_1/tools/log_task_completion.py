# Sierra copyright notice.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogTaskCompletion(Tool):
    """Creates a log entry for a successfully completed task."""
    @staticmethod
    def invoke(data: Dict[str, Any], task_id, task_type, user_id) -> str:
        task_logs = data.get('task_logs', [])

        if task_type == "archive":
            notes = f"Archive task {task_id} completed successfully"
        elif task_type == "file_check":
            notes = f"File check task {task_id} completed successfully"
        elif task_type == "file_organization":
            notes = f"File organization task {task_id} completed successfully"
        else:
            notes = f"{task_type.title()} task {task_id} completed successfully"

        new_log = {
            "task_id": task_id, "task_type": task_type, "user_id": user_id, "result": "success", "completed_at": "2024-01-20T13:00:00Z", "notes": notes}
        task_logs.append(new_log)
        data['task_logs'] = task_logs
        return json.dumps(new_log)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "log_task_completion", "description": "Writes a record to the main task log for a successfully completed task.", "parameters": {"type": "object", "properties": {"task_id": {"type": "string"}, "task_type": {"type": "string"}, "user_id": {"type": "string"}}, "required": ["task_id", "task_type", "user_id"]}}}
