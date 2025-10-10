# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetErrorLogDetails(Tool):
    """Retrieves the detailed step-by-step log for a specific failed task."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_id = kwargs.get("task_id")
        for log in data.get('error_logs', []):
            if log.get('task_id') == task_id:
                return json.dumps(log)
        return json.dumps({"error": f"No detailed error log found for task ID '{task_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_error_log_details", "description": "Fetches the detailed step-by-step trace for a failed task to aid in debugging.", "parameters": {"type": "object", "properties": {"task_id": {"type": "string"}}, "required": ["task_id"]}}}
