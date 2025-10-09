from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class CalculateOptimizationMetrics(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], projects: list = [], metric_type: str = "efficiency_gain") -> str:
        allocations = data.get("allocations", [])
        employees = data.get("employees", [])
        projects_data = data.get("projects", [])

        total_allocated_hours = 0
        total_required_hours = 0
        overallocated_employees = 0
        underutilized_employees = 0
        skill_mismatches = 0
        partial_allocations = 0

        project_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("project_id") in projects and alloc.get("status") == "active"
        ]

        for alloc in project_allocations:
            total_allocated_hours += alloc.get("hours_per_week", 0)

            if alloc.get("hours_per_week", 0) < 20:
                partial_allocations += 1

        for proj_id in projects:
            project = next(
                (p for p in projects_data if p.get("project_id") == proj_id), None
            )
            if project:
                total_required_hours += project.get("required_hours_per_week", 0)

        employee_hours = {}
        for alloc in allocations:
            if alloc.get("status") == "active":
                emp_id = alloc.get("employee_id")
                if emp_id not in employee_hours:
                    employee_hours[emp_id] = 0
                employee_hours[emp_id] += alloc.get("hours_per_week", 0)

        for emp_id, hours in employee_hours.items():
            utilization = (hours / 40) * 100
            if utilization > 100:
                overallocated_employees += 1
            elif utilization < 70:
                underutilized_employees += 1

        for alloc in project_allocations:
            emp_id = alloc.get("employee_id")
            employee = next(
                (e for e in employees if e.get("employee_id") == emp_id), None
            )
            project = next(
                (
                    p
                    for p in projects_data
                    if p.get("project_id") == alloc.get("project_id")
                ),
                None,
            )

            if employee and project:
                role = employee.get("role", "").lower()
                if ("senior" in role or "architect" in role) and project.get(
                    "priority"
                ) in ["low", "medium"]:
                    skill_mismatches += 1

        allocation_efficiency = (
            (total_allocated_hours / total_required_hours * 100)
            if total_required_hours > 0
            else 0
        )

        potential_improvements = (
            (overallocated_employees * 5)
            + (underutilized_employees * 3)
            + (skill_mismatches * 2)
            + (partial_allocations * 1)
        )

        efficiency_gain = min(potential_improvements, 30)

        optimization_complete = efficiency_gain < 5
        payload = {
                "projects_analyzed": len(projects),
                "metric_type": metric_type,
                "efficiency_gain": efficiency_gain,
                "optimization_complete": optimization_complete,
                "metrics": {
                    "allocation_efficiency": round(allocation_efficiency, 1),
                    "overallocated_employees": overallocated_employees,
                    "underutilized_employees": underutilized_employees,
                    "skill_mismatches": skill_mismatches,
                    "partial_allocations": partial_allocations,
                    "total_allocated_hours": total_allocated_hours,
                    "total_required_hours": total_required_hours,
                },
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateOptimizationMetrics",
                "description": "Calculate optimization metrics for projects",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "projects": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of project IDs",
                        },
                        "metric_type": {
                            "type": "string",
                            "description": "Type of metric to calculate",
                        },
                    },
                    "required": ["projects"],
                },
            },
        }
