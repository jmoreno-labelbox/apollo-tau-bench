# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class compute_team_average_progress(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": "Team not found"}, indent=2)

        members = team.get("members", [])
        if not members:
            return json.dumps({"average_progress": 0}, indent=2)

        total_progress = 0
        for member in members:
            user_progress = data.get("user_course_progress", [])
            user_courses = [p for p in user_progress if p.get("user_id") == member]
            if user_courses:
                avg_progress = sum(
                    p.get("current_progress_percent", 0) for p in user_courses
                ) / len(user_courses)
                total_progress += avg_progress

        team_average = total_progress / len(members) if members else 0
        return json.dumps(
            {"team_average_progress": team_average, "team_id": team_id}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "compute_team_average_progress",
                "description": "Compute average course progress for a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
