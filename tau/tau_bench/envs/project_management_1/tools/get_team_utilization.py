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

class GetTeamUtilization(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None) -> str:
        if not team_id:
            payload = {"error": "team_id is required"}
            out = json.dumps(payload)
            return out

        teams = data.get("teams", [])
        allocations = data.get("allocations", [])

        team = None
        for t in teams:
            if t.get("team_id") == team_id:
                team = t
                break

        if not team:
            payload = {"error": f"Team with ID '{team_id}' not found"}
            out = json.dumps(payload)
            return out

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
        payload = {
                "team_id": team_id,
                "team_name": team.get("team_name"),
                "total_capacity": total_capacity,
                "total_allocated": total_allocated,
                "team_utilization": round(team_utilization, 1),
                "member_utilizations": member_utilizations,
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
                "name": "getTeamUtilization",
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
