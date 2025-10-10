# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WhoAmI(Tool):
    """Return the current user (from authentication)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        auth = data.get("authentication") or [{}]
        user = auth[0]
        return json.dumps({
            "username": user.get("username"),
            "email": user.get("email")
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "who_am_i",
                "description": "Return the authenticated username and email.",
                "parameters": {"type": "object", "properties": {}}
            },
        }
