# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_leave_records(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        records = list(data.get("leave_records", {}).values())
        filtered = [r for r in records if r.get("employee_id") == employee_id]
        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_leave_records",
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
