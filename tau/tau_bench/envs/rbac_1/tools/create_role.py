# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], description, role_name, is_temporary = False) -> str:
        roles = list(data.get('roles', {}).values())
        new_id_num = max((int(r['role_id'][4:]) for r in roles), default=0) + 1
        new_role_id = f"ROL-{new_id_num:03d}"
        new_role = {
                "role_id": new_role_id,
                "role_name": role_name,
                "description": description,
                "is_temporary": is_temporary,
        }
        roles.append(new_role)
        data['roles'] = roles
        return json.dumps(new_role)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_role",
                        "description": "Creates a new role.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_name": {"type": "string"},
                                        "description": {"type": "string"},
                                        "temporary": {"type": "bool"}
                                },
                                "required": ["role_name", "description"]
                        }
                }
        }
