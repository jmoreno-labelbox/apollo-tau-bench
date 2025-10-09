from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetErrorLogDetails(Tool):
    """Fetches the comprehensive step-by-step log for a particular failed task."""

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None) -> str:
        for log in data.get("error_logs", []):
            if log.get("task_id") == task_id:
                payload = log
                out = json.dumps(payload)
                return out
        payload = {"error": f"No detailed error log found for task ID '{task_id}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetErrorLogDetails",
                "description": "Fetches the detailed step-by-step trace for a failed task to aid in debugging.",
                "parameters": {
                    "type": "object",
                    "properties": {"task_id": {"type": "string"}},
                    "required": ["task_id"],
                },
            },
        }
