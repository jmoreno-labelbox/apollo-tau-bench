# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class create_new_employee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee: Dict[str, Any]) -> str:
        new_emp = employee
        if not new_emp:
            return json.dumps({"error": "employee payload required"}, indent=2)

        employees = list(data.get("employees", {}).values())
        if any(e["employee_id"] == new_emp["employee_id"] for e in employees):
            return json.dumps({"error": "employee_id already exists"}, indent=2)

        employees.append(new_emp)
        data["employees"] = employees
        return json.dumps(
            {"success": f'employee {new_emp["employee_id"]} created'}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_employee",
                "description": "Insert a completely new employee record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee": {
                            "type": "object",
                            "description": "Full employee JSON object conforming to employees.json schema",
                        }
                    },
                    "required": ["employee"],
                    "additionalProperties": False,
                },
            },
        }
