# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_compensation_records(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id) -> str:
        if not find_employee(list(data.get("employees", {}).values()), employee_id):
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        records = [
            c
            for c in data.get("compensation_records", [])
            if c.get("employee_id") == employee_id
        ]
        return json.dumps(records, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_compensation_records",
                "description": "Retrieve all historical compensation records for an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }
