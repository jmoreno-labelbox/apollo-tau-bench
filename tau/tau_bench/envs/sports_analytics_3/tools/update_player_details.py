from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdatePlayerDetails(Tool):
    """Modify a player's information: primary_position, current_team_id, and/or roster_status."""

    @staticmethod
    def invoke(data: dict[str, Any], player_id: str = None, primary_position: str = None, current_team_id: str = None, roster_status: str = None) -> str:
        #1) Confirm validity: player_id is required
        if player_id is None:
            payload = {"error": "Missing required field: player_id"}
            out = json.dumps(payload, indent=2)
            return out

        #At least one optional field must be included
        if all(v is None for v in [primary_position, current_team_id, roster_status]):
            payload = {
                    "error": "At least one of primary_position, current_team_id, or roster_status must be provided"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #2) Retrieve DB using provided data
        players = data.get("players", {}).values()

        #3) Locate and modify player
        for player in players.values():
            if player.get("player_id") == player_id:
                if primary_position is not None:
                    player["primary_position"] = primary_position
                if current_team_id is not None:
                    player["current_team_id"] = current_team_id
                if roster_status is not None:
                    player["roster_status"] = roster_status
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
                "name": "updatePlayerDetails",
                "description": (
                    "Update a player's primary_position, current_team_id, and/or roster_status. "
                    "At least one of these optional fields must be provided."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to update.",
                        },
                        "primary_position": {
                            "type": "string",
                            "description": "New primary position of the player.",
                        },
                        "current_team_id": {
                            "type": "integer",
                            "description": "New team ID for the player.",
                        },
                        "roster_status": {
                            "type": "string",
                            "description": "New roster status for the player.",
                        },
                    },
                    "required": ["player_id"],
                },
            },
        }
