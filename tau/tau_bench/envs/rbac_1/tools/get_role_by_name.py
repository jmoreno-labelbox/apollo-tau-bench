# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRoleByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], role_name) -> str:
        for role in list(data.get('roles', {}).values()):
            if role.get('role_name') == role_name:
                return json.dumps(role)
        return json.dumps({"error": "Role not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_role_by_name",
                        "description": "Retrieves role details based on the role name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_name": {
                                                "type": "string",
                                                "description": "The name of the role to search for."
                                        }
                                },
                                "required": ["role_name"]
                        }
                }
        }
