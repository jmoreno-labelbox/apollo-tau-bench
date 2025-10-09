from tau_bench.envs.tool import Tool
import json
from itertools import islice
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FetchClientPrefs(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None) -> str:
        if client_id is None:
            payload = {"error": "client_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        prefs = next(
            (
                p
                for p in data.get("client_preferences", {}).values()
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
                "name": "FetchClientPrefs",
                "description": "Get preferences for a specific client.",
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }
