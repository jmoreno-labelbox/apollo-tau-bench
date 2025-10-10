# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAllocation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], allocation_id, employee_id, project_id, role, cross_department = False, end_date = "", hours_per_week = 0, start_date = "", status = "active") -> str:

        if not all([employee_id, project_id, role]):
            return json.dumps(
                {
                    "error": "employee_id, project_id, hours_per_week, and role are required"
                }
            )

        allocations = data.get("allocations", [])
        projects = list(data.get("projects", {}).values())
        skill_requirements = data.get("skill_requirements", [])

        is_temporary = any(
            term in role.lower()
            for term in ["consultant", "emergency", "temporary", "interim"]
        )

        project = next((p for p in projects if p.get("project_id") == project_id), None)

        skill_gap_filled = 0
        if project:

            project_requirements = next(
                (
                    req
                    for req in skill_requirements
                    if req.get("project_id") == project_id
                ),
                None,
            )

            if project_requirements:

                current_allocations = [
                    alloc
                    for alloc in allocations
                    if alloc.get("project_id") == project_id
                    and alloc.get("status") == "active"
                ]
                current_hours = sum(
                    alloc.get("hours_per_week", 0) for alloc in current_allocations
                )

                total_hours_needed = sum(
                    skill.get("hours_needed", 0)
                    for skill in project_requirements.get("required_skills", [])
                )

                previous_gap = max(0, total_hours_needed - current_hours)
                new_gap = max(0, total_hours_needed - (current_hours + hours_per_week))
                skill_gap_filled = previous_gap - new_gap

        allocation_id = allocation_id or f"alloc_{uuid.uuid4().hex[:8]}"

        new_allocation = {
            "allocation_id": allocation_id,
            "employee_id": employee_id,
            "project_id": project_id,
            "hours_per_week": hours_per_week,
            "role": role,
            "start_date": start_date,
            "end_date": end_date,
            "status": status,
            "cross_department": cross_department,
        }

        allocations.append(new_allocation)

        result = {
            "success": True,
            "allocation": new_allocation,
            "is_temporary": is_temporary,
        }

        if is_temporary:
            result["temporary_coverage"] = hours_per_week

        if skill_gap_filled > 0:
            result["skill_gap_filled"] = skill_gap_filled

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_allocation",
                "description": "Create a new resource allocation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "allocation_id": {
                            "type": "string",
                            "description": "Optional custom allocation ID",
                        },
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        },
                        "hours_per_week": {
                            "type": "number",
                            "description": "Hours allocated per week",
                        },
                        "role": {
                            "type": "string",
                            "description": "Role in the project",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date (YYYY-MM-DD)",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date (YYYY-MM-DD)",
                        },
                        "status": {
                            "type": "string",
                            "description": "Status: active, completed, cancelled",
                        },
                        "cross_department": {
                            "type": "boolean",
                            "description": "Is this a cross-department allocation",
                        },
                    },
                    "required": ["employee_id", "project_id", "hours_per_week", "role"],
                },
            },
        }
