# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_user_goals_by_type(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_id: str,
        goal_type: str = "",
        goal_description_keywords: str = "",
    ) -> str:
        goals_data = data.get("goals", [])
        user_goals = next((g for g in goals_data if g.get("user_id") == user_id), {})
        goals = user_goals.get("goals", [])

        filtered_goals = goals

        # Apply a filter based on the specified goal type, if available.
        if goal_type:
            filtered_goals = [
                g
                for g in filtered_goals
                if g.get("goal_type", "").lower() == goal_type.lower()
            ]

        # Apply filters based on keywords in the goal description if available.
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

        return json.dumps(
            {
                "user_id": user_id,
                "matching_goals": filtered_goals,
                "total_goals_found": len(filtered_goals),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_user_goals_by_type",
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
