# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRolePermissionsAliasTool(Tool):
    """get_role_permissions: alias for list_role_permissions."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return ListRolePermissionsTool.invoke(data, **kwargs)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_permissions",
                "description": "Return permissions for a role.",
                "parameters": {
                    "type": "object",
                    "properties": {"role_id": {"type": "string"}},
                    "required": ["role_id"],
                },
            },
        }
