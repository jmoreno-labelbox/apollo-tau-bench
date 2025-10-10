# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPlayerDetailsById(Tool):
    """Fetch a player record by its player_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        player_id = kwargs.get("player_id")

        # 1) Validate
        if player_id is None:
            return json.dumps({"error": "Missing required field: player_id"}, indent=2)

        # 2) Get DB from passed-in data
        players = data.get("players", [])

        # 3) Exact match lookup
        for player in players:
            if player.get("player_id") == player_id:
                return json.dumps(player, indent=2)

        return json.dumps({"error": f"No player found with ID {player_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_player_details_by_id",
                "description": "Fetch a single player's full details by their player_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to retrieve."
                        }
                    },
                    "required": ["player_id"]
                }
            }
        }
