# Copyright Sierra Inc.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllPlayersOfTeam(Tool):
    """Fetch all players belonging to a given team_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("team_id")

        # 1) Verify
        if team_id is None:
            return json.dumps({"error": "Missing required field: team_id"}, indent=2)

        # Retrieve the database from the provided input data.
        players: List[Dict[str, Any]] = list(data.get("players", {}).values())

        # 3) Select players based on the specific team_id.
        matching_players = [
            player for player in players
            if player.get("current_team_id") == team_id
        ]

        if not matching_players:
            return json.dumps({"error": f"No players found for team_id {team_id}"}, indent=2)

        return json.dumps(matching_players, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_players_of_team",
                "description": "Fetch all player records belonging to the specified team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {
                            "type": "integer",
                            "description": "Exact team ID whose players should be retrieved."
                        }
                    },
                    "required": ["team_id"]
                }
            }
        }
