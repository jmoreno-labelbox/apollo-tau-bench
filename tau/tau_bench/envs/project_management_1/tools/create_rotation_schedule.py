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

class CreateRotationSchedule(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str = None,
        from_project: str = None,
        to_project: str = None,
        rotation_date: str = None,
        hours_to_rotate: int = None,
        holiday_coverage: str = "false",
        skill_development_rotation: str = "false"
    ) -> str:
        if not all(
            [employee_id, from_project, to_project, rotation_date, hours_to_rotate]
        ):
            payload = {
                "error": "The fields employee_id, from_project, to_project, rotation_date, hours_to_rotate are required"
            }
            out = json.dumps(payload)
            return out

        rotation_schedules = data.get("rotation_schedules", {}).values()
        allocations = data.get("allocations", {}).values()
        projects = data.get("projects", {}).values()

        from_project_allocations = [
            alloc
            for alloc in allocations.values() if alloc.get("project_id") == from_project
            and alloc.get("status") == "active"
        ]

        employee_from_allocation = next(
            (
                alloc
                for alloc in from_project_allocations
                if alloc.get("employee_id") == employee_id
            ),
            None,
        )

        if not employee_from_allocation:
            payload = {"error": f"Employee {employee_id} not found on project {from_project}"}
            out = json.dumps(payload)
            return out

        from_project_data = next(
            (p for p in projects.values() if p.get("project_id") == from_project), None
        )
        if from_project_data:
            required_hours = from_project_data.get("required_hours_per_week", 0)
            current_total_hours = sum(
                alloc.get("hours_per_week", 0) for alloc in from_project_allocations
            )
            hours_after_rotation = current_total_hours - hours_to_rotate

            coverage_percentage = (
                (hours_after_rotation / required_hours * 100)
                if required_hours > 0
                else 0
            )
            other_team_members = len(from_project_allocations) - 1

            if holiday_coverage.lower() == "true":
                coverage_maintained = (
                    hours_after_rotation >= required_hours * 0.3
                    or other_team_members > 0
                    or hours_to_rotate <= 25
                )
            else:
                coverage_maintained = coverage_percentage >= 80 or (
                    other_team_members > 0
                    and hours_after_rotation >= required_hours * 0.5
                )
        else:
            if holiday_coverage.lower() == "true":
                coverage_maintained = True
            else:
                coverage_maintained = (
                    len(from_project_allocations) > 1 or hours_to_rotate < 20
                )

        rotation_id = f"rot_{uuid.uuid4().hex[:8]}"

        new_rotation = {
            "rotation_id": rotation_id,
            "employee_id": employee_id,
            "from_project": from_project,
            "to_project": to_project,
            "rotation_date": rotation_date,
            "hours_to_rotate": hours_to_rotate,
            "holiday_coverage": holiday_coverage,
            "skill_development_rotation": skill_development_rotation,
            "status": "scheduled",
        }

        data["rotation_schedules"][new_rotation["rotation_schedule_id"]] = new_rotation

        existing_rotations = [
            rot
            for rot in rotation_schedules.values() if rot.get("status") == "scheduled"
            and skill_development_rotation.lower() == "true"
        ]

        developers_in_rotation = len(existing_rotations)
        skill_development_hours = hours_to_rotate
        payload = {
            "success": True,
            "rotation": new_rotation,
            "rotation_created": True,
            "coverage_maintained": coverage_maintained,
            "developers_in_rotation": developers_in_rotation,
            "skill_development_hours": skill_development_hours,
            "coverage_details": {
                "from_project_allocations": len(from_project_allocations),
                "other_team_members": (
                    other_team_members if "other_team_members" in locals() else 0
                ),
                "coverage_percentage": (
                    round(coverage_percentage, 1)
                    if "coverage_percentage" in locals()
                    else 0
                ),
            },
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRotationSchedule",
                "description": "Create a rotation schedule for an employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "from_project": {
                            "type": "string",
                            "description": "Current project ID",
                        },
                        "to_project": {
                            "type": "string",
                            "description": "New project ID",
                        },
                        "rotation_date": {
                            "type": "string",
                            "description": "Date of rotation (YYYY-MM-DD)",
                        },
                        "hours_to_rotate": {
                            "type": "number",
                            "description": "Hours to rotate",
                        },
                        "holiday_coverage": {
                            "type": "boolean",
                            "description": "Flag if the rotation is holiday coverage",
                        },
                        "skill_development_rotation": {
                            "type": "boolean",
                            "description": "Flag if the rotation is skill development rotation",
                        },
                    },
                    "required": [
                        "employee_id",
                        "from_project",
                        "to_project",
                        "rotation_date",
                        "hours_to_rotate",
                    ],
                },
            },
        }
