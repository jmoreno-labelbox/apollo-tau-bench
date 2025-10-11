# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTeamUtilization(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id) -> str:
        if not team_id:
            return json.dumps({"error": "team_id is required"})

        teams = data.get("teams", [])
        allocations = data.get("allocations", [])

        team = None
        for t in teams:
            if t.get("team_id") == team_id:
                team = t
                break

        if not team:
            return json.dumps({"error": f"Team with ID '{team_id}' not found"})

        team_members = team.get("members", [])
        total_capacity = len(team_members) * 40
        total_allocated = 0
        member_utilizations = []

        for member_id in team_members:
            member_allocations = [
                alloc
                for alloc in allocations
                if alloc.get("employee_id") == member_id
                and alloc.get("status") == "active"
            ]
            member_hours = sum(
                alloc.get("hours_per_week", 0) for alloc in member_allocations
            )
            total_allocated += member_hours
            member_utilizations.append(
                {
                    "employee_id": member_id,
                    "hours": member_hours,
                    "utilization": round((member_hours / 40) * 100, 1),
                }
            )

        team_utilization = (
            (total_allocated / total_capacity * 100) if total_capacity > 0 else 0
        )

        return json.dumps(
            {
                "team_id": team_id,
                "team_name": team.get("team_name"),
                "total_capacity": total_capacity,
                "total_allocated": total_allocated,
                "team_utilization": round(team_utilization, 1),
                "member_utilizations": member_utilizations,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_utilization",
                "description": "Get utilization metrics for a team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string", "description": "The team ID"}
                    },
                    "required": ["team_id"],
                },
            },
        }
