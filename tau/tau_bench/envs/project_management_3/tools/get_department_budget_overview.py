from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone
from typing import Any

class GetDepartmentBudgetOverview(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_name: str, fiscal_year: int = datetime.now().year) -> str:
        if not department_name:
            payload = {"error": "department_name is required"}
            out = json.dumps(payload)
            return out

        departments = data.get("departments", [])
        projects = data.get("projects", [])
        budgets = data.get("budgets", [])

        department = next(
            (d for d in departments if d.get("department_name") == department_name),
            None,
        )
        if not department:
            payload = {"error": f"Department {department_name} not found"}
            out = json.dumps(payload)
            return out

        dept_projects = [p for p in projects if p.get("department") == department_name]

        total_budget = 0
        total_spent = 0
        project_budgets = []

        for project in dept_projects:
            project_budget = next(
                (
                    b
                    for b in budgets
                    if b.get("project_id") == project["project_id"]
                    and b.get("fiscal_year") == fiscal_year
                ),
                None,
            )
            if project_budget:
                total_budget += project_budget["total_budget"]
                total_spent += project_budget.get("spent_amount", 0)

                project_budgets.append(
                    {
                        "project_id": project["project_id"],
                        "project_name": project["name"],
                        "priority": project["priority"],
                        "budget": project_budget["total_budget"],
                        "spent": project_budget.get("spent_amount", 0),
                        "remaining": project_budget["total_budget"]
                        - project_budget.get("spent_amount", 0),
                    }
                )

        project_budgets.sort(key=lambda x: x["budget"], reverse=True)

        overview = {
            "department": department_name,
            "budget_overview": {
                "total_department_budget": total_budget,
                "total_spent": total_spent,
                "total_remaining": total_budget - total_spent,
                "utilization_percentage": (
                    round((total_spent / total_budget * 100), 2)
                    if total_budget > 0
                    else 0
                ),
                "project_count": len(dept_projects),
                "projects_with_budget": len(project_budgets),
            },
            "top_projects_by_budget": project_budgets[:5],
            "capacity_metrics": {
                "total_employees": department.get("employee_count", 0),
                "total_capacity_hours": department.get("total_capacity_hours", 0),
                "allocated_hours": department.get("allocated_hours", 0),
                "available_hours": department.get("available_hours", 0),
            },
        }
        payload = overview
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDepartmentBudgetOverview",
                "description": "Get budget overview for all projects in a department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_name": {
                            "type": "string",
                            "description": "Department name",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": ["department_name"],
                },
            },
        }
