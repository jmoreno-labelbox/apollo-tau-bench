# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateSprint(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sprint_id = kwargs.get("sprint_id")
        sprint_name = kwargs.get("sprint_name")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")
        sprint_goal = kwargs.get("sprint_goal")
        team_id = kwargs.get("team_id")

        if not all([sprint_name, start_date, end_date, team_id]):
            return json.dumps(
                {"error": "sprint_name, start_date, end_date, and team_id are required"}
            )

        sprints = list(data.get("sprints", {}).values())
        teams = list(data.get("teams", {}).values())

        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": f"Team '{team_id}' not found"})

        for s in sprints:
            if s.get("sprint_id") == sprint_id:
                return json.dumps(
                    {
                        "error": f"sprint_id {sprint_id} exists. Please enter a unique sprint_id.",
                    }
                )

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

        return json.dumps({"success": True, "sprint": new_sprint})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_sprint",
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
