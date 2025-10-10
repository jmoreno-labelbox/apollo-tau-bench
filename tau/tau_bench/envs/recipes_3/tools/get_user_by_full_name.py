# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserByFullName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], full_name: str) -> str:
        user = next(
            (u for u in list(data.get("users", {}).values()) if str(u.get("full_name")) == str(full_name)), None
        )
        return _json({"user": user})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_by_full_name",
                "description": "Retrieve a user by exact full_name.",
                "parameters": {
                    "type": "object",
                    "properties": {"full_name": {"type": "string"}},
                    "required": ["full_name"],
                },
            },
        }
