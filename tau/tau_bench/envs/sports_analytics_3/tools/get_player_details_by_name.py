# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPlayerDetailsByName(Tool):
    """Fetch a player record by its full_name (exact match, case-sensitive)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        full_name = kwargs.get("full_name")

        # 1) Validate
        if not full_name:
            return json.dumps({"error": "Missing required field: full_name"}, indent=2)

        # 2) Get DB from passed-in data
        players = data.get("players", [])

        # 3) Exact match lookup (no normalization)
        for player in players:
            if player.get("full_name") == full_name:
                return json.dumps(player, indent=2)

        return json.dumps({"error": f"No player found with full_name {full_name}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_player_details_by_name",
                "description": "Fetch a single player's full details by exact full_name (case-sensitive, no normalization).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "full_name": {
                            "type": "string",
                            "description": "Exact player full name to retrieve (e.g., 'Jennifer Roberts')."
                        }
                    },
                    "required": ["full_name"]
                }
            }
        }    
