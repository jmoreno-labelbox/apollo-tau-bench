# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteDepartment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name) -> str:
        department_name = name

        if not all([department_name]):
            return json.dumps({"error": "department_name is a required parameters"})

        departments = list(data.get("departments", {}).values())

        for i, department in enumerate(departments):
            if department.get("department_name") == department_name:
                departments.pop(i)
                return json.dumps({"success": True})

        return json.dumps(
            {
                "error": "Department name '{}' does not exist".format(department_name),
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_department",
                "description": "Delete a department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Department name"},
                    },
                    "required": ["name"],
                },
            },
        }
