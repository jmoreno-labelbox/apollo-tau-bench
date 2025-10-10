# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EnableUserMFATool(Tool):
    """Enable MFA for a given user (write operation)."""

    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        users = list(data.get("users", {}).values())

        if not isinstance(user_id, str):
            return json.dumps({"error": "user_id must be provided"}, indent=2)

        for u in users:
            if u.get("user_id") == user_id:
                u["mfa_enabled"] = True
                return json.dumps({"success": f"MFA enabled for {user_id}", "user": u}, indent=2)

        return json.dumps({"error": f"User {user_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "enable_user_mfa",
                "description": "Enable MFA for a given user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to enable MFA for"}
                    },
                    "required": ["user_id"]
                }
            }
        }
