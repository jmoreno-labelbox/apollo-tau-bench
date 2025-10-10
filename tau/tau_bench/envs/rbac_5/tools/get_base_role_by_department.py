# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBaseRoleByDepartment(Tool):
    """
    Get the base role ID for a given department.

    kwargs:
      department: str (required)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department = (kwargs.get("department", "") or "").strip().lower()

        # Associate departments with core role identifiers.
        department_role_map = {
            "engineering": "engineering-base",
            "marketing": "marketing-base",
            "sales": "sales-base",
            "human resources": "hr-base",
            "operations": "operations-base",
            "finance": "finance-base"
        }

        role_name = department_role_map.get(department)
        if not role_name:
            return json.dumps({"error": f"No base role found for department '{department}'"})

        # Identify the function.
        roles = list(data.get("roles", {}).values())
        for role in roles:
            if role.get("role_name") == role_name:
                return json.dumps({"role": role})

        return json.dumps({"error": f"Base role '{role_name}' not found in roles"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_base_role_by_department",
                "description": "Get the base role for a given department.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {"type": "string", "description": "Department name."}
                    },
                    "required": ["department"],
                    "additionalProperties": False
                }
            }
        }
