# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLastSuccessfulTaskRun(Tool):
    """Finds the log of the last time a task of a certain type completed successfully."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_type = kwargs.get("task_type")
        successful_runs = [log for log in data.get('task_logs', []) if log.get('task_type') == task_type and log.get('result') == 'success']
        if not successful_runs:
            return json.dumps({"error": f"No successful run found for type '{task_type}'."})
        last_run = max(successful_runs, key=lambda x: x['completed_at'])
        return json.dumps(last_run)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_last_successful_task_run", "description": "Finds when a specific type of task last completed successfully.", "parameters": {"type": "object", "properties": {"task_type": {"type": "string", "enum": ["archive", "file_check", "file_organization"]}}, "required": ["task_type"]}}}
