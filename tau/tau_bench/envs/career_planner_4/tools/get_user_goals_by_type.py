from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetUserGoalsByType(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        goal_type: str = "",
        goal_description_keywords: str = ""
    ) -> str:
        _goal_typeL = goal_type or ''.lower()
        _goal_description_keywordsL = goal_description_keywords or ''.lower()
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), {})
        goals = user_goals.get("goals", [])

        filtered_goals = goals

        # Filter based on goal type if specified
        if goal_type:
            filtered_goals = [
                g
                for g in filtered_goals
                if g.get("goal_type", "").lower() == goal_type.lower()
            ]

        # Filter using keywords in the goal description if specified
        if goal_description_keywords:
            keywords = goal_description_keywords.lower().split()
            filtered_goals = [
                g
                for g in filtered_goals
                if any(
                    keyword in g.get("goal_description", "").lower()
                    for keyword in keywords
                )
            ]
        payload = {
            "user_id": user_id,
            "matching_goals": filtered_goals,
            "total_goals_found": len(filtered_goals),
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
                "name": "getUserGoalsByType",
                "description": "Get user goals filtered by type and/or description keywords",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "goal_type": {
                            "type": "string",
                            "description": "Goal type to filter by (e.g., 'Role Transition', 'Skill Mastery', 'Certification')",
                        },
                        "goal_description_keywords": {
                            "type": "string",
                            "description": "Keywords to search in goal description (space-separated)",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }
