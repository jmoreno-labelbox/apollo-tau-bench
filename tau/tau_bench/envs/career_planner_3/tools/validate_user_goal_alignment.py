# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateUserGoalAlignment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        target_role = kwargs.get("target_role")
        goals = data.get("goals", [])
        user_goals = [g for g in goals if g["user_id"] == user_id]

        if not user_goals:
            return json.dumps(
                {"valid": False, "reason": "No goals found for user"}, indent=2
            )

        for goal_group in user_goals:
            for goal in goal_group.get("goals", []):
                goal_desc = goal.get("goal_description", "").lower()
                goal_target_role = goal.get("target_role", "").lower()

                if (
                    target_role.lower() in goal_desc
                    or target_role.lower() in goal_target_role
                    or goal_target_role == target_role.lower()
                ):
                    return json.dumps(
                        {"valid": True, "goal_id": goal.get("goal_id")}, indent=2
                    )

        return json.dumps(
            {"valid": False, "reason": "No goals found for target role"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_user_goal_alignment",
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
