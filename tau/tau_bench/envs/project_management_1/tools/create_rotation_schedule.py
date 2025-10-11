# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateRotationSchedule(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id, from_project, hours_to_rotate, rotation_date, to_project, holiday_coverage = "false", skill_development_rotation = "false") -> str:

        if not all(
            [employee_id, from_project, to_project, rotation_date, hours_to_rotate]
        ):
            return json.dumps({"error": "The fields employee_id, from_project, to_project, rotation_date, hours_to_rotate are required"})

        rotation_schedules = data.get("rotation_schedules", [])
        allocations = data.get("allocations", [])
        projects = list(data.get("projects", {}).values())

        from_project_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("project_id") == from_project
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
            return json.dumps(
                {"error": f"Employee {employee_id} not found on project {from_project}"}
            )

        from_project_data = next(
            (p for p in projects if p.get("project_id") == from_project), None
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

        rotation_schedules.append(new_rotation)

        existing_rotations = [
            rot
            for rot in rotation_schedules
            if rot.get("status") == "scheduled"
            and skill_development_rotation.lower() == "true"
        ]

        developers_in_rotation = len(existing_rotations)
        skill_development_hours = hours_to_rotate

        return json.dumps(
            {
                "success": True,
                "rotation": new_rotation,
                "rotation_created": True,
                "coverage_maintained": coverage_maintained,
                "developers_in_rotation": developers_in_rotation,
                "skill_development_hours": skill_development_hours,
                "coverage_details": {
                    "from_project_allocations": len(from_project_allocations),
                    "other_team_members": other_team_members
                    if "other_team_members" in locals()
                    else 0,
                    "coverage_percentage": round(coverage_percentage, 1)
                    if "coverage_percentage" in locals()
                    else 0,
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_rotation_schedule",
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
