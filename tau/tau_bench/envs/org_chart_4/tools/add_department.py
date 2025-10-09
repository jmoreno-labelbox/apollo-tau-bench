from tau_bench.envs.tool import Tool
import json
from typing import Any

class add_department(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_id: str) -> str:
        departments = data.setdefault("departments", [])
        department = {"department_id": department_id}
        data["departments"][department_id] = department
        payload = {"success": True, "department_id": department_id}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addDepartment",
                "description": "Add a new department record. The department object must contain all required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "object",
                            "description": "Department record to add",
                        }
                    },
                    "required": ["department"],
                    "additionalProperties": False,
                },
            },
        }
