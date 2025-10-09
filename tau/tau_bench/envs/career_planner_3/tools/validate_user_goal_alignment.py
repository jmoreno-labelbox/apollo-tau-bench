from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ValidateUserGoalAlignment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, target_role: str = None) -> str:
        goals = data.get("goals", {}).values()
        user_goals = [g for g in goals.values() if g["user_id"] == user_id]

        if not user_goals:
            payload = {"valid": False, "reason": "No goals found for user"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        for goal_group in user_goals:
            for goal in goal_group.get("goals", []):
                goal_desc = goal.get("goal_description", "").lower()
                goal_target_role = goal.get("target_role", "").lower()

                if (
                    target_role.lower() in goal_desc
                    or target_role.lower() in goal_target_role
                    or goal_target_role == target_role.lower()
                ):
                    payload = {"valid": True, "goal_id": goal.get("goal_id")}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
        payload = {"valid": False, "reason": "No goals found for target role"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateUserGoalAlignment",
                "description": "Validates that a user has goals aligned with a target role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user to validate.",
                        },
                        "target_role": {
                            "type": "string",
                            "description": "The target role to check alignment with.",
                        },
                    },
                    "required": ["user_id", "target_role"],
                },
            },
        }
