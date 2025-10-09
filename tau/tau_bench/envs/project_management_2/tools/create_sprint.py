from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateSprint(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sprint_id: str = None, sprint_name: str = None, start_date: str = None, end_date: str = None, sprint_goal: str = None, team_id: str = None) -> str:
        if not all([sprint_name, start_date, end_date, team_id]):
            payload = {"error": "sprint_name, start_date, end_date, and team_id are required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", [])
        teams = data.get("teams", [])

        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": f"Team '{team_id}' not found"}
            out = json.dumps(payload)
            return out

        for s in sprints:
            if s.get("sprint_id") == sprint_id:
                payload = {
                    "error": f"sprint_id {sprint_id} exists. Please enter a unique sprint_id.",
                }
                out = json.dumps(payload)
                return out

        new_sprint = {
            "sprint_id": sprint_id,
            "sprint_name": sprint_name,
            "start_date": start_date,
            "end_date": end_date,
            "sprint_goal": sprint_goal,
            "team_id": team_id,
            "status": "planning",
            "planned_story_points": 0,
            "completed_story_points": 0,
            "velocity": 0,
        }

        sprints.append(new_sprint)
        payload = {"success": True, "sprint": new_sprint}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSprint",
                "description": "Create a new sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_name": {
                            "type": "string",
                            "description": "Name of the sprint",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Sprint start date (YYYY-MM-DD)",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "Sprint end date (YYYY-MM-DD)",
                        },
                        "sprint_goal": {
                            "type": "string",
                            "description": "Main goal for the sprint",
                        },
                        "team_id": {
                            "type": "string",
                            "description": "Team assigned to this sprint",
                        },
                    },
                    "required": ["sprint_name", "start_date", "end_date", "team_id"],
                },
            },
        }
