from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetUsersWithLeadershipGoals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_ids: list[int] = None) -> str:
        if user_ids is None:
            user_ids = []
        goals = data.get("goals", [])
        leadership_users = []

        for g in goals:
            if g["user_id"] in user_ids:
                for goal in g.get("goals", []):
                    goal_desc = goal.get("goal_description", "").lower()
                    goal_type = goal.get("goal_type", "").lower()
                    target_role = goal.get("target_role", "").lower()

                    # Look for signs of leadership
                    leadership_indicators = [
                        "leadership",
                        "lead",
                        "manager",
                        "director",
                        "senior",
                        "principal",
                        "staff",
                    ]
                    if (
                        any(
                            indicator in goal_desc
                            for indicator in leadership_indicators
                        )
                        or any(
                            indicator in goal_type
                            for indicator in leadership_indicators
                        )
                        or any(
                            indicator in target_role
                            for indicator in leadership_indicators
                        )
                    ):
                        if g["user_id"] not in leadership_users:
                            leadership_users.append(g["user_id"])
                        break
        payload = leadership_users
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUsersWithLeadershipGoals",
                "description": "Filters users by whether they have a leadership-oriented goal.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of user IDs to evaluate.",
                        }
                    },
                    "required": ["user_ids"],
                },
            },
        }
