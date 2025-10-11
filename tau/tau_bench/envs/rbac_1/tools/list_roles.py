# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListRoles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        roles = list(data.get('roles', {}).values())
        return json.dumps({"roles": roles})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "list_roles",
                        "description": "Lists all available roles in the system.",
                        "parameters": {
                                "type": "object",
                                "properties": {},
                                "required": []
                        }
                }
        }
