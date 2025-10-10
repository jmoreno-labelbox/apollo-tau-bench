# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class bulk_update_goals(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], team_id: str, goal_type: str, updates: dict
    ) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": "Team not found"}, indent=2)

        members = team.get("members", [])
        goals_data = data.get("goals", [])

        for member in members:
            user_goals = next(
                (g for g in goals_data if g.get("user_id") == member), None
            )
            if user_goals:
                for goal in user_goals.get("goals", []):
                    if goal_type.lower() in goal.get("title", "").lower():
                        goal.update(updates)

        return json.dumps(
            {"success": f"Bulk updated goals for {len(members)} members"}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "bulk_update_goals",
                "description": "Bulk update goals for team members",
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
