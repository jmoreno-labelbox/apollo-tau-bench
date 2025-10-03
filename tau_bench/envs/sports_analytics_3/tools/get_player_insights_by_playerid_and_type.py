from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetPlayerInsightsByPlayeridAndType(Tool):
    """
    Retrieve player insights using player_id and type filter.

    Inputs (exact names):
      - player_id (int) [required]
      - type (string)   [required]
          * Use "all" to return all insights for the player
          * Or provide an exact insight_type (e.g., "Performance", "Health", "Development", "Strategic", "Mechanical")

    Behavior:
      - Exact match (case-sensitive) on insight_type when type is not "all"
      - Deterministic ordering by insight_id in ascending order
    """

    @staticmethod
    def invoke(data: dict[str, Any], player_id: str = None, type_filter: str = None) -> str:
        #1) Confirm validity
        if player_id is None:
            payload = {"error": "Missing required field: player_id"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(type_filter, str) or type_filter == "":
            payload = {"error": "Missing required field: type"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        insights: list[dict[str, Any]] = data.get("curated_insights", [])

        #3) Filter based on player_id
        player_insights = [i for i in insights if i.get("player_id") == player_id]

        if not player_insights:
            payload = {"error": f"No insights found for player_id {player_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Implement type filter
        if type_filter != "all":
            player_insights = [
                i for i in player_insights if i.get("insight_type") == type_filter
            ]
            if not player_insights:
                payload = {
                        "error": f"No insights found for player_id {player_id} with type '{type_filter}'"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

        #5) Order deterministically
        player_insights.sort(key=lambda i: int(i.get("insight_id", 0)))
        payload = player_insights
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPlayerInsightsByPlayeridAndType",
                "description": (
                    "Fetch curated insights for a player. Pass type='All' to get all insights, "
                    "or an exact insight_type (e.g., 'Performance') for a specific subset."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID whose insights to retrieve.",
                        },
                        "type": {
                            "type": "string",
                            "description": "Use 'All' or provide an exact insight_type (case-sensitive).",
                        },
                    },
                    "required": ["player_id", "type"],
                },
            },
        }
