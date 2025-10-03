from tau_bench.envs.tool import Tool
import json
from typing import Any

class get_leave_records(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        records = data.get("leave_records", [])
        filtered = [r for r in records if r.get("employee_id") == employee_id]
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLeaveRecords",
                "description": "Return all leave records for the given employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Employee ID to fetch leave records for",
                        }
                    },
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }
