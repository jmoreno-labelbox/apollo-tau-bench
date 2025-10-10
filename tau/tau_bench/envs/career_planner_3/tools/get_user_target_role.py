# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserTargetRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        goals_data = data.get("goals", [])

        user_goals = [g for g in goals_data if g.get("user_id") == user_id]

        if not user_goals:
            return json.dumps({"error": f"No goals found for user {user_id}."})

        # Find the first goal with the type "Role Transition"
        for goal in user_goals[0].get("goals", []):
            if goal.get("goal_type") == "Role Transition" and "target_role" in goal:
                return json.dumps({"target_role": goal.get("target_role")})

        return json.dumps(
            {"error": f"No 'Role Transition' goal found for user {user_id}."}
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_target_role",
                "description": "Retrieves the formal target role from a user's 'Role Transition' career goal.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
