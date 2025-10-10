# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMe(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        existing = data.get("_me")
        if isinstance(existing, dict) and "username" in existing and not kwargs:
            return json.dumps(existing, indent=2)

        username = kwargs.get("username")
        if username:
            auth_list = data.get("authentication") or []
            match = next((a for a in auth_list if a.get("username") == username), None)
            if not match:
                return json.dumps({"error": f"Unknown username: {username}"}, indent=2)
            me = {"username": match.get("username"), "email": match.get("email")}
            data["_me"] = me
            return json.dumps(me, indent=2)

        return json.dumps({"error": "No acting identity set. Provide username to get_me."}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_me",
                "description": "Gets/sets the acting identity.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"}
                    },
                    "required": ["username"]
                }
            }
        }
