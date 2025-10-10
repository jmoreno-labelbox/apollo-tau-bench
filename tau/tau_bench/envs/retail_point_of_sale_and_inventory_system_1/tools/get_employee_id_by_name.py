# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetEmployeeIdByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_name = kwargs.get("employee_name")
        employees = list(data.get("employees", {}).values())

        for employee in employees:
            if employee.get("name") == employee_name:
                return json.dumps({"employee_id": employee.get("employee_id")})

        return json.dumps({"employee_id": None})


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_id_by_name",
                "description": "Retrieves the employee ID for a given employee's full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_name": {
                            "type": "string",
                            "description": "The full name of the employee.",
                        },
                    },
                    "required": ["employee_name"],
                },
            },
        }
