from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetUserTargetRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        goals_data = data.get("goals", [])

        user_goals = [g for g in goals_data if g.get("user_id") == user_id]

        if not user_goals:
            payload = {"error": f"No goals found for user {user_id}."}
            out = json.dumps(payload)
            return out

        # Locate the initial goal categorized as "Role Transition"
        for goal in user_goals[0].get("goals", []):
            if goal.get("goal_type") == "Role Transition" and "target_role" in goal:
                payload = {"target_role": goal.get("target_role")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"No 'Role Transition' goal found for user {user_id}."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserTargetRole",
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
