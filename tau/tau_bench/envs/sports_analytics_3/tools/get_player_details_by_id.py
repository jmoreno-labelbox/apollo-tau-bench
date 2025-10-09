from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPlayerDetailsById(Tool):
    """Retrieve a player record using its player_id."""

    @staticmethod
    def invoke(data: dict[str, Any], player_id: str = None) -> str:
        #1) Confirm validity
        if player_id is None:
            payload = {"error": "Missing required field: player_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        players = data.get("players", [])

        #3) Lookup for exact matches
        for player in players:
            if player.get("player_id") == player_id:
                payload = player
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No player found with ID {player_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPlayerDetailsById",
                "description": "Fetch a single player's full details by their player_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to retrieve.",
                        }
                    },
                    "required": ["player_id"],
                },
            },
        }
