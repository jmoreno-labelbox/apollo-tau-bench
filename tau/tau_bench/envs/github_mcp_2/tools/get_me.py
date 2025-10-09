from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetMe(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], username: str = None) -> str:
        existing = data.get("_me")
        if isinstance(existing, dict) and "username" in existing and not username:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out

        if username:
            auth_list = data.get("authentication") or []
            match = next((a for a in auth_list.values() if a.get("username") == username), None)
            if not match:
                payload = {"error": f"Unknown username: {username}"}
                out = json.dumps(payload, indent=2)
                return out
            me = {"username": match.get("username"), "email": match.get("email")}
            data["_me"] = me
            payload = me
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "No acting identity set. Provide username to get_me."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetMe",
                "description": "Gets/sets the acting identity.",
                "parameters": {
                    "type": "object",
                    "properties": {"username": {"type": "string"}},
                    "required": ["username"],
                },
            },
        }
