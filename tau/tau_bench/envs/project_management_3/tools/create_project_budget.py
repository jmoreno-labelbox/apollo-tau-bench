# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateProjectBudget(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        fiscal_year = kwargs.get("fiscal_year")
        total_budget = kwargs.get("total_budget")
        budget_categories = kwargs.get("budget_categories", {})

        if not all([project_id, fiscal_year, total_budget]):
            return json.dumps(
                {"error": "project_id, fiscal_year, and total_budget are required"}
            )

        budgets = data.get("budgets", [])
        projects = list(data.get("projects", {}).values())
        allocations = data.get("allocations", [])
        employees = list(data.get("employees", {}).values())

        project = next((p for p in projects if p.get("project_id") == project_id), None)
        if not project:
            return json.dumps({"error": f"Project {project_id} not found"})

        if project.get("status") not in ["active", "planning"]:
            return json.dumps(
                {
                    "error": f"Cannot create budget for project with status: {project.get('status')}"
                }
            )

        project_allocations = [
            a
            for a in allocations
            if a.get("project_id") == project_id and a.get("status") == "active"
        ]

        total_personnel_cost = 0
        for allocation in project_allocations:
            employee = next(
                (
                    e
                    for e in employees
                    if e.get("employee_id") == allocation.get("employee_id")
                ),
                None,
            )
            if employee:

                hourly_rate = (
                    150 if "senior" in employee.get("role", "").lower() else 100
                )
                weekly_cost = allocation.get("hours_per_week", 0) * hourly_rate

                duration_weeks = 26
                total_personnel_cost += weekly_cost * duration_weeks

        if total_personnel_cost > total_budget * 0.8:
            return json.dumps(
                {
                    "error": f"Personnel costs (${total_personnel_cost}) exceed 80% of total budget. Increase budget or reduce allocations.",
                    "suggested_budget": int(total_personnel_cost / 0.8),
                }
            )

        budget_id = kwargs.get("budget_id", f"budget_{uuid.uuid4().hex[:8]}")

        new_budget = {
            "budget_id": budget_id,
            "project_id": project_id,
            "fiscal_year": fiscal_year,
            "total_budget": total_budget,
            "personnel_budget": total_budget * 0.8,
            "non_personnel_budget": total_budget * 0.2,
            "allocated_personnel_cost": total_personnel_cost,
            "spent_amount": 0,
            "committed_amount": 0,
            "budget_categories": budget_categories,
            "status": "active",
            "created_date": datetime.now().isoformat(),
            "last_modified": datetime.now().isoformat(),
            "project_priority": project.get("priority"),
            "department": project.get("department"),
        }

        budgets.append(new_budget)

        return json.dumps({"success": True, "budget": new_budget})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_project_budget",
                "description": "Create a new budget for a project based on team allocations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "budget_id": {"type": "string", "description": "Budget ID"},
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year",
                        },
                        "total_budget": {
                            "type": "number",
                            "description": "Total budget amount",
                        },
                        "budget_categories": {
                            "type": "object",
                            "description": "Budget breakdown by category",
                        },
                    },
                    "required": ["project_id", "fiscal_year", "total_budget"],
                },
            },
        }
