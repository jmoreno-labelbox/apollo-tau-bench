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

class CreateTeam(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        team_name: str = None,
        project_id: str = None,
        team_members: list = None,
        team_id: str = None
    ) -> str:
        if team_members is None:
            team_members = []

        if not all([team_name, project_id]):
            payload = {"error": "team_name and project_id are required"}
            out = json.dumps(payload)
            return out

        teams = data.get("teams", {}).values()
        projects = data.get("projects", {}).values()
        allocations = data.get("allocations", {}).values()

        project = next((p for p in projects.values() if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project {project_id} not found"}
            out = json.dumps(payload)
            return out

        project_allocations = [
            alloc
            for alloc in allocations.values() if alloc.get("project_id") == project_id and alloc.get("status") == "active"
        ]

        total_allocated_hours = sum(
            alloc.get("hours_per_week", 0) for alloc in project_allocations
        )
        required_hours = project.get("required_hours_per_week", 0)

        staffing_percentage = (
            (total_allocated_hours / required_hours * 100) if required_hours > 0 else 0
        )
        project_staffed = staffing_percentage >= 80

        team_formed = True
        members_on_project = 0
        for member_id in team_members:
            member_allocation = next(
                (
                    alloc
                    for alloc in project_allocations
                    if alloc.get("employee_id") == member_id
                ),
                None,
            )
            if member_allocation:
                members_on_project += 1
            else:
                team_formed = False

        team_id = team_id or f"team_{uuid.uuid4().hex[:8]}"

        new_team = {
            "team_id": team_id,
            "team_name": team_name,
            "project_id": project_id,
            "members": team_members,
            "created_date": datetime.now().isoformat(),
            "status": "active",
        }

        data["teams"][team_id] = new_team
        payload = {
                "success": True,
                "team": new_team,
                "team_formed": team_formed,
                "project_staffed": project_staffed,
                "staffing_details": {
                    "allocated_hours": total_allocated_hours,
                    "required_hours": required_hours,
                    "staffing_percentage": round(staffing_percentage, 1),
                    "members_on_project": members_on_project,
                    "total_members": len(team_members),
                },
            }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTeam",
                "description": "Create a new team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_name": {"type": "string", "description": "Team name"},
                        "project_id": {
                            "type": "string",
                            "description": "Associated project ID",
                        },
                        "team_members": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee IDs",
                        },
                        "team_id": {
                            "type": "string",
                            "description": "Optional custom team ID",
                        },
                    },
                    "required": ["team_name", "project_id"],
                },
            },
        }
