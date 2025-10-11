# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRoleRequirements(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], role_name) -> str:
        role_catalog = data.get("role_skill_catalog", [])
        result = [r for r in role_catalog if r["role"] == role_name]

        if not result:
            return json.dumps(
                {
                    "error": "Role not found",
                    "role_name": role_name,
                    "available_roles": [r["role"] for r in role_catalog],
                },
                indent=2,
            )

        return json.dumps(result[0], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_requirements",
                "description": "Retrieves the required skills and certifications for a given role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {
                            "type": "string",
                            "description": "The name of the target role.",
                        }
                    },
                    "required": ["role_name"],
                },
            },
        }
