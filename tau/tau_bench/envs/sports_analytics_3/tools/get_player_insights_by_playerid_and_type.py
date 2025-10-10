# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPlayerInsightsByPlayeridAndType(Tool):
    """
    Fetch player insights by player_id and type filter.

    Inputs (exact names):
      - player_id (int) [required]
      - type (string)   [required]
          * Use "all" to return all insights for the player
          * Or pass an exact insight_type (e.g., "Performance", "Health", "Development", "Strategic", "Mechanical")

    Behavior:
      - Exact match (case-sensitive) on insight_type when type != "all"
      - Deterministic ordering by insight_id ASC
    """

    @staticmethod
    def invoke(data: Dict[str, Any], player_id, type) -> str:
        type_filter = type

        # 1) Verify
        if player_id is None:
            return json.dumps({"error": "Missing required field: player_id"}, indent=2)
        if not isinstance(type_filter, str) or type_filter == "":
            return json.dumps({"error": "Missing required field: type"}, indent=2)

        # Retrieve database.
        insights: List[Dict[str, Any]] = list(data.get("curated_insights", {}).values())

        # 3) Apply filter based on player_id
        player_insights = [i for i in insights if i.get("player_id") == player_id]

        if not player_insights:
            return json.dumps({"error": f"No insights found for player_id {player_id}"}, indent=2)

        # 4) Implement type filter
        if type_filter != "all":
            player_insights = [i for i in player_insights if i.get("insight_type") == type_filter]
            if not player_insights:
                return json.dumps(
                    {"error": f"No insights found for player_id {player_id} with type '{type_filter}'"},
                    indent=2
                )

        # 5) Fixed sequence
        player_insights.sort(key=lambda i: int(i.get("insight_id", 0)))

        return json.dumps(player_insights, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_player_insights_by_playerid_and_type",
                "description": (
                    "Fetch curated insights for a player. Pass type='All' to get all insights, "
                    "or an exact insight_type (e.g., 'Performance') for a specific subset."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID whose insights to retrieve."
                        },
                        "type": {
                            "type": "string",
                            "description": "Use 'All' or provide an exact insight_type (case-sensitive)."
                        }
                    },
                    "required": ["player_id", "type"]
                }
            }
        }
