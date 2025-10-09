from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class BulkUpdateGoals(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], team_id: str, goal_type: str, updates: dict
    ) -> str:
        _goal_typeL = goal_type or ''.lower()
        pass
        teams = data.get("teams", {}).values()
        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": "Team not found"}
            out = json.dumps(payload, indent=2)
            return out

        members = team.get("members", [])
        goals_data = data.get("goals", {}).values()

        for member in members:
            user_goals = next(
                (g for g in goals_data.values() if g.get("user_id") == member), None
            )
            if user_goals:
                for goal in user_goals.get("goals", []):
                    if goal_type.lower() in goal.get("title", "").lower():
                        goal.update(updates)
        payload = {"success": f"Bulk updated goals for {len(members)} members"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "bulkUpdateGoals",
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
