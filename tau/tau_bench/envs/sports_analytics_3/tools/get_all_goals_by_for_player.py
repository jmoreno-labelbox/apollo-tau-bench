from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAllGoalsByForPlayer(Tool):
    """Retrieve all development goals associated with a specific player_id."""

    @staticmethod
    def invoke(data: dict[str, Any], player_id: str = None) -> str:
        #1) Confirm validity
        if player_id is None:
            payload = {"error": "Missing required field: player_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        goals: list[dict[str, Any]] = data.get("player_dev_goals", {}).values()

        #3) Filter goals related to player
        matching = [g for g in goals.values() if g.get("player_id") == player_id]

        if not matching:
            payload = {"error": f"No goals found for player_id {player_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = matching
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAllGoalsByForPlayer",
                "description": "Fetch all development goals for a given player_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {
                            "type": "integer",
                            "description": "Exact player ID to retrieve goals for.",
                        }
                    },
                    "required": ["player_id"],
                },
            },
        }
