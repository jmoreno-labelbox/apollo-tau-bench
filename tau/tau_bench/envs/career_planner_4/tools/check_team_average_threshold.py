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

class CheckTeamAverageThreshold(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], team_id: str, threshold: int, comparison: str
    ) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": "Team not found"}
            out = json.dumps(payload, indent=2)
            return out

        members = team.get("team_members", [])
        progress_data = data.get("user_course_progress", [])

        # Compute the average for the team
        total_progress = 0
        member_count = 0

        for member_id in members:
            member_courses = [p for p in progress_data if p.get("user_id") == member_id]
            if member_courses:
                avg_progress = sum(
                    c.get("current_progress_percent", 0) for c in member_courses
                ) / len(member_courses)
                total_progress += avg_progress
                member_count += 1

        team_average = total_progress / member_count if member_count > 0 else 0

        if comparison == "below":
            meets_condition = team_average < threshold
        elif comparison == "above":
            meets_condition = team_average > threshold
        else:
            meets_condition = team_average == threshold
        payload = {
            "team_id": team_id,
            "team_average": team_average,
            "threshold": threshold,
            "comparison": comparison,
            "meets_condition": meets_condition,
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
                "name": "checkTeamAverageThreshold",
                "description": "Check if team average meets threshold",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "threshold": {"type": "integer"},
                        "comparison": {"type": "string"},
                    },
                    "required": ["team_id", "threshold", "comparison"],
                },
            },
        }
