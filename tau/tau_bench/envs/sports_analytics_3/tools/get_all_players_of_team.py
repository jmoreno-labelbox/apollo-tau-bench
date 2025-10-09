from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAllPlayersOfTeam(Tool):
    """Retrieve all players associated with a specific team_id."""

    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None) -> str:
        #1) Confirm validity
        if team_id is None:
            payload = {"error": "Missing required field: team_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        players: list[dict[str, Any]] = data.get("players", {}).values()

        #3) Filter players based on exact team_id
        matching_players = [
            player for player in players if player.get("current_team_id") == team_id
        ]

        if not matching_players:
            payload = {"error": f"No players found for team_id {team_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = matching_players
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllPlayersOfTeam",
                "description": "Fetch all player records belonging to the specified team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {
                            "type": "integer",
                            "description": "Exact team ID whose players should be retrieved.",
                        }
                    },
                    "required": ["team_id"],
                },
            },
        }
