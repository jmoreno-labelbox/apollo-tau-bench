# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListRolesTool(Tool):
    """List roles, with optional filter for temporary."""

    @staticmethod
    def invoke(data: Dict[str, Any], is_temporary) -> str:
        temp_flag = is_temporary
        roles = list(data.get("roles", {}).values())
        if temp_flag is None:
            return json.dumps(roles, indent=2)
        return json.dumps([r for r in roles if r["is_temporary"] == temp_flag], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_roles",
                "description": "List all roles optionally filtering by temporary flag",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "is_temporary": {"type": "boolean"}
                    }
                }
            }
        }
