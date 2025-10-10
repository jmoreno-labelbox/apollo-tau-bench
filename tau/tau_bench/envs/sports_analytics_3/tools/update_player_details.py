# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdatePlayerDetails(Tool):

    """Update a player's details: primary_position, current_team_id, and/or roster_status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        player_id = kwargs.get("player_id")
        primary_position = kwargs.get("primary_position")
        current_team_id = kwargs.get("current_team_id")
        roster_status = kwargs.get("roster_status")

        # 1) Validate: player_id must be provided
        if player_id is None:
            return json.dumps({"error": "Missing required field: player_id"}, indent=2)

        # At least one of the optional fields should be present
        if all(v is None for v in [primary_position, current_team_id, roster_status]):
            return json.dumps({"error": "At least one of primary_position, current_team_id, or roster_status must be provided"}, indent=2)

        # 2) Get DB from passed-in data
        players = list(data.get("players", {}).values())

        # 3) Find and update player
        for player in players:
            if player.get("player_id") == player_id:
                if primary_position is not None:
                    player["primary_position"] = primary_position
                if current_team_id is not None:
                    player["current_team_id"] = current_team_id
                if roster_status is not None:
                    player["roster_status"] = roster_status
                return json.dumps(player, indent=2)

        return json.dumps({"error": f"No player found with ID {player_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_player_details",
                "description": (
                    "Update a player's primary_position, current_team_id, and/or roster_status. "
                    "At least one of these optional fields must be provided."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to update."
                        },
                        "primary_position": {
                            "type": "string",
                            "description": "New primary position of the player."
                        },
                        "current_team_id": {
                            "type": "integer",
                            "description": "New team ID for the player."
                        },
                        "roster_status": {
                            "type": "string",
                            "description": "New roster status for the player."
                        }
                    },
                    "required": ["player_id"]
                }
            }
        }
