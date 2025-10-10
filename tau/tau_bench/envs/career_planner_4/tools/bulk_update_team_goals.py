# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class bulk_update_team_goals(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], team_id: str, goal_type: str, updates: dict
    ) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": "Team not found"}, indent=2)

        members = team.get("team_members", [])
        goals_data = data.get("goals", [])
        updated_goals = []

        for member_id in members:
            user_goals = next(
                (g for g in goals_data if g.get("user_id") == member_id), None
            )
            if user_goals:
                goals = user_goals.get("goals", [])
                for goal in goals:
                    if goal_type.lower() in goal.get("goal_name", "").lower():
                        goal.update(updates)
                        updated_goals.append(
                            {"user_id": member_id, "goal_id": goal.get("goal_id")}
                        )

        return json.dumps(
            {
                "success": f"Team {team_id} goals updated",
                "updated_goals": updated_goals,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "bulk_update_team_goals",
                "description": "Update goals for all team members",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "goal_type": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["team_id", "goal_type", "updates"],
                },
            },
        }
