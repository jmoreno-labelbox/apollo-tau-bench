from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class AnalyzeAllocationEfficiency(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        projects: list = None,
        check_partial_allocations: bool = False,
        check_skill_mismatch: bool = False
    ) -> str:
        if projects is None:
            projects = []

        allocations = data.get("allocations", [])
        employees = data.get("employees", [])
        projects_data = data.get("projects", [])

        partial_allocations_found = 0
        skill_mismatches_found = 0
        recommendations = []

        if check_partial_allocations:

            employee_allocations = {}
            for alloc in allocations:
                if (
                    alloc.get("project_id") in projects
                    and alloc.get("status") == "active"
                ):
                    emp_id = alloc.get("employee_id")
                    if emp_id not in employee_allocations:
                        employee_allocations[emp_id] = []
                    employee_allocations[emp_id].append(alloc)

            for emp_id, emp_allocations in employee_allocations.items():
                for alloc in emp_allocations:
                    if alloc.get("hours_per_week", 0) < 20:
                        partial_allocations_found += 1

            if partial_allocations_found > 0:
                recommendations.append("Consider consolidating partial allocations")

        if check_skill_mismatch:

            for alloc in allocations:
                if (
                    alloc.get("project_id") in projects
                    and alloc.get("status") == "active"
                ):
                    emp_id = alloc.get("employee_id")
                    employee = next(
                        (e for e in employees if e.get("employee_id") == emp_id), None
                    )

                    if employee:
                        role = employee.get("role", "").lower()
                        project = next(
                            (
                                p
                                for p in projects_data
                                if p.get("project_id") == alloc.get("project_id")
                            ),
                            None,
                        )

                        if ("senior" in role or "architect" in role) and project:
                            if (
                                project.get("priority") == "medium"
                                or project.get("priority") == "low"
                            ):
                                skill_mismatches_found += 1

            if skill_mismatches_found > 0:
                recommendations.append("Review skill assignments")
        payload = {
                "projects_analyzed": len(projects),
                "partial_allocations_found": partial_allocations_found,
                "skill_mismatches_found": skill_mismatches_found,
                "recommendations": recommendations,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyzeAllocationEfficiency",
                "description": "Analyze allocation efficiency across projects",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "projects": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of project IDs to analyze",
                        },
                        "check_partial_allocations": {
                            "type": "boolean",
                            "description": "Check for partial allocations",
                        },
                        "check_skill_mismatch": {
                            "type": "boolean",
                            "description": "Check for skill mismatches",
                        },
                    },
                    "required": ["projects"],
                },
            },
        }
