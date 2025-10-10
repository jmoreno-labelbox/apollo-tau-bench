# Sierra copyright information.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDepartmentBudgetOverview(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department_name, fiscal_year = datetime.now().year) -> str:

        if not department_name:
            return json.dumps({"error": "department_name is required"})

        departments = list(data.get("departments", {}).values())
        projects = list(data.get("projects", {}).values())
        budgets = data.get("budgets", [])

        department = next(
            (d for d in departments if d.get("department_name") == department_name),
            None,
        )
        if not department:
            return json.dumps({"error": f"Department {department_name} not found"})

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
                "utilization_percentage": round((total_spent / total_budget * 100), 2)
                if total_budget > 0
                else 0,
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

        return json.dumps(overview, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_department_budget_overview",
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
