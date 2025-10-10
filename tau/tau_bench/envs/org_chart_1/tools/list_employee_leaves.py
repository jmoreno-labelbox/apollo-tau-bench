# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_employee_leaves(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        lv = [
            leave_record
            for leave_record in data.get("leave_records", [])
            if leave_record["employee_id"] == employee_id
        ]
        return json.dumps(lv, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_employee_leaves",
                "description": "Return all leave records for the employee (any status).",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }
