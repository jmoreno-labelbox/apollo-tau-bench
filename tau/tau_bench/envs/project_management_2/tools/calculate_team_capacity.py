# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateTeamCapacity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("team_id")

        if not team_id:
            return json.dumps({"error": "team_id is required"})

        teams = list(data.get("teams", {}).values())
        employees = list(data.get("employees", {}).values())
        tasks = list(data.get("tasks", {}).values())

        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": f"Team '{team_id}' not found"})

        team_members = team.get("members", [])

        total_capacity_hours = len(team_members) * 6 * 10

        if sprint_id := kwargs.get("sprint_id"):
            sprint_tasks = [
                t
                for t in tasks
                if t.get("sprint_id") == sprint_id
                and t.get("assignee_id") in team_members
            ]

            member_loads = {}
            for member_id in team_members:
                member_tasks = [
                    t for t in sprint_tasks if t.get("assignee_id") == member_id
                ]
                member_points = sum(t.get("story_points", 0) for t in member_tasks)
                member_loads[member_id] = {
                    "story_points": member_points,
                    "task_count": len(member_tasks),
                    "utilization": round((member_points / 20) * 100, 1),
                }

            total_assigned_points = sum(
                m["story_points"] for m in member_loads.values()
            )

            return json.dumps(
                {
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
                },
                indent=2,
            )

        return json.dumps(
            {
                "team_id": team_id,
                "total_capacity_hours": total_capacity_hours,
                "total_capacity_points": len(team_members) * 20,
                "team_size": len(team_members),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_team_capacity",
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
