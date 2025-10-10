# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDepartmentDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")

        if not name:
            return json.dumps({"error": "name is a required parameter"})

        departments = list(data.get("departments", {}).values())

        for department in departments:
            if department.get("department_name") == name:
                return json.dumps({"success": True, "details": department})

        return json.dumps(
            {
                "error": "name or department is not found",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_department_details",
                "description": "Get department details",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Name of the department",
                        },
                    },
                    "required": ["name"],
                },
            },
        }
