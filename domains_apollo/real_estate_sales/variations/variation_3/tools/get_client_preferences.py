from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetClientPreferences(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None) -> str:
        if client_id is None:
            payload = {"error": "client_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        prefs = next(
            (
                p
                for p in data.get("client_preferences", [])
                if p.get("client_id") == client_id
            ),
            None,
        )
        if not prefs:
            payload = {"error": f"No preferences found for client_id={client_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = prefs
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetClientPreferences",
                "description": "Get preferences for a specific client.",
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }
