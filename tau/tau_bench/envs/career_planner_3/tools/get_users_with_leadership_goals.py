# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUsersWithLeadershipGoals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_ids = []) -> str:
        goals = data.get("goals", [])
        leadership_users = []

        for g in goals:
            if g["user_id"] in user_ids:
                for goal in g.get("goals", []):
                    goal_desc = goal.get("goal_description", "").lower()
                    goal_type = goal.get("goal_type", "").lower()
                    target_role = goal.get("target_role", "").lower()

                    # Verify leadership metrics.
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

        return json.dumps(leadership_users, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_users_with_leadership_goals",
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
