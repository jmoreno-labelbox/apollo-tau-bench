# Sierra Copyright

import datetime, uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateTeam(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id, team_id, team_name, team_members = []) -> str:

        if not all([team_name, project_id]):
            return json.dumps({"error": "team_name and project_id are required"})

        teams = data.get("teams", [])
        projects = list(data.get("projects", {}).values())
        allocations = data.get("allocations", [])

        project = next((p for p in projects if p.get("project_id") == project_id), None)
        if not project:
            return json.dumps({"error": f"Project {project_id} not found"})

        project_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("project_id") == project_id and alloc.get("status") == "active"
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

        teams.append(new_team)

        return json.dumps(
            {
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
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_team",
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
