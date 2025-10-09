from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPlayerDetailsByName(Tool):
    """Retrieve a player record using its full_name (exact match, case-sensitive)."""

    @staticmethod
    def invoke(data: dict[str, Any], full_name: str = None) -> str:
        #1) Confirm validity
        if not full_name:
            payload = {"error": "Missing required field: full_name"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        players = data.get("players", [])

        #3) Lookup for exact matches (without normalization)
        for player in players:
            if player.get("full_name") == full_name:
                payload = player
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No player found with full_name {full_name}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPlayerDetailsByName",
                "description": "Fetch a single player's full details by exact full_name (case-sensitive, no normalization).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "full_name": {
                            "type": "string",
                            "description": "Exact player full name to retrieve (e.g., 'Evelyn Martin').",
                        }
                    },
                    "required": ["full_name"],
                },
            },
        }
