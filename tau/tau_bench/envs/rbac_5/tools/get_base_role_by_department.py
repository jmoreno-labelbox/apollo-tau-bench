from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any

class GetBaseRoleByDepartment(Tool):
    """
    Retrieve the foundational role ID for a specified department.

    kwargs:
      department: str (mandatory)
    """

    @staticmethod
    def invoke(data: dict[str, Any], department: str = "") -> str:
        department = department.strip().lower()

        # Associate departments with foundational role names
        department_role_map = {
            "engineering": "engineering-base",
            "marketing": "marketing-base",
            "sales": "sales-base",
            "human resources": "hr-base",
            "operations": "operations-base",
            "finance": "finance-base",
        }

        role_name = department_role_map.get(department)
        if not role_name:
            payload = {"error": f"No base role found for department '{department}'"}
            out = json.dumps(payload)
            return out

        # Identify the role
        roles = data.get("roles", [])
        for role in roles:
            if role.get("role_name") == role_name:
                payload = {"role": role}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Base role '{role_name}' not found in roles"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBaseRoleByDepartment",
                "description": "Get the base role for a given department.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "string",
                            "description": "Department name.",
                        }
                    },
                    "required": ["department"],
                    "additionalProperties": False,
                },
            },
        }
