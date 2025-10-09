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

class CalculateTeamCapacity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None, sprint_id: str = None) -> str:
        if not team_id:
            payload = {"error": "team_id is required"}
            out = json.dumps(payload)
            return out

        teams = data.get("teams", {}).values()
        data.get("employees", {}).values()
        tasks = data.get("tasks", {}).values()

        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": f"Team '{team_id}' not found"}
            out = json.dumps(payload)
            return out

        team_members = team.get("members", [])

        total_capacity_hours = len(team_members) * 6 * 10

        if sprint_id:
            sprint_tasks = [
                t
                for t in tasks.values() if t.get("sprint_id") == sprint_id
                and t.get("assignee_id") in team_members
            ]

            member_loads = {}
            for member_id in team_members:
                member_tasks = [
                    t for t in sprint_tasks if t.get("assignee_id") == member_id
                ]
                member_points = sum(t.get("story_points", 0) for t in member_tasks.values())
                member_loads[member_id] = {
                    "story_points": member_points,
                    "task_count": len(member_tasks),
                    "utilization": round((member_points / 20) * 100, 1),
                }

            total_assigned_points = sum(
                m["story_points"] for m in member_loads.values()
            )
            payload = {
                    "team_id": team_id,
                    "sprint_id": sprint_id,
                    "team_utilization": round(
                        (total_assigned_points / (len(team_members) * 20)) * 100, 1
                    ),
                    "total_capacity_hours": total_capacity_hours,
                    "total_capacity_points": len(team_members) * 20,
                    "assigned_story_points": total_assigned_points,
                    "available_story_points": (len(team_members) * 20)
                    - total_assigned_points,
                    "member_loads": member_loads,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {
                "team_id": team_id,
                "total_capacity_hours": total_capacity_hours,
                "total_capacity_points": len(team_members) * 20,
                "team_size": len(team_members),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTeamCapacity",
                "description": "Calculate team capacity for sprint planning",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string", "description": "The team ID"},
                        "sprint_id": {
                            "type": "string",
                            "description": "Optional sprint ID to check current load",
                        },
                    },
                    "required": ["team_id"],
                },
            },
        }
