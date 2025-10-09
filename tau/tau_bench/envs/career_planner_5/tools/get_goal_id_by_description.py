from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetGoalIdByDescription(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, keyword: str) -> str:
        _keywordL = keyword or ''.lower()
        pass
        goals_data = data.get("goals", {}).values()
        user_goals_obj = next(
            (g for g in goals_data.values() if g.get("user_id") == user_id), None
        )
        if user_goals_obj:
            # Identify a goal with a description that includes the keyword (case-insensitive)
            goal = next(
                (
                    g
                    for g in user_goals_obj.get("goals", [])
                    if keyword.lower() in g.get("goal_description", "").lower()
                ),
                None,
            )
            if goal:
                payload = {"goal_id": goal["goal_id"]}
                out = json.dumps(payload, indent=2)
                return out
        payload = {
            "error": f"Goal for user {user_id} containing keyword '{keyword}' not found"
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getGoalIdByDescription",
                "description": "Find a user's goal ID by searching for a keyword in the goal's description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "keyword": {
                            "type": "string",
                            "description": "A keyword to search for in the goal descriptions.",
                        },
                    },
                    "required": ["user_id", "keyword"],
                },
            },
        }
