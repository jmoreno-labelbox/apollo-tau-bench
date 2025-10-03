from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetDepartmentDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        if not name:
            payload = {"error": "name is a required parameter"}
            out = json.dumps(payload)
            return out

        departments = data.get("departments", [])

        for department in departments:
            if department.get("department_name") == name:
                payload = {"success": True, "details": department}
                out = json.dumps(payload)
                return out
        payload = {
                "error": "name or department is not found",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDepartmentDetails",
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
