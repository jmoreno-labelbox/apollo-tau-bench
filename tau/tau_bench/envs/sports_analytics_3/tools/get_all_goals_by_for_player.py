# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllGoalsByForPlayer(Tool):
    """Fetch all development goals for a given player_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        player_id = kwargs.get("player_id")

        # 1) Validate
        if player_id is None:
            return json.dumps({"error": "Missing required field: player_id"}, indent=2)

        # 2) Get DB
        goals: List[Dict[str, Any]] = list(data.get("player_dev_goals", {}).values())

        # 3) Filter goals for player
        matching = [g for g in goals if g.get("player_id") == player_id]

        if not matching:
            return json.dumps({"error": f"No goals found for player_id {player_id}"}, indent=2)

        return json.dumps(matching, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_goals_by_for_player",
                "description": "Fetch all development goals for a given player_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to retrieve goals for."
                        }
                    },
                    "required": ["player_id"]
                }
            }
        }
