# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProjectFinancialSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        fiscal_year = kwargs.get("fiscal_year", datetime.now().year)

        if not project_id:
            return json.dumps({"error": "project_id is required"})

        projects = list(data.get("projects", {}).values())
        budgets = data.get("budgets", [])
        expenses = data.get("expenses", [])
        allocations = data.get("allocations", [])
        employees = list(data.get("employees", {}).values())

        project = next((p for p in projects if p.get("project_id") == project_id), None)
        if not project:
            return json.dumps({"error": f"Project {project_id} not found"})

        current_budget = next(
            (
                b
                for b in budgets
                if b.get("project_id") == project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        project_allocations = [
            a
            for a in allocations
            if a.get("project_id") == project_id and a.get("status") == "active"
        ]

        weekly_resource_cost = 0
        for alloc in project_allocations:
            employee = next(
                (e for e in employees if e.get("employee_id") == alloc["employee_id"]),
                None,
            )
            if employee:
                hourly_rate = (
                    150 if "senior" in employee.get("role", "").lower() else 100
                )
                weekly_resource_cost += alloc.get("hours_per_week", 0) * hourly_rate

        approved_expenses = sum(
            e.get("amount", 0)
            for e in expenses
            if e.get("project_id") == project_id and e.get("status") == "approved"
        )

        summary = {
            "project_id": project_id,
            "project_name": project["name"],
            "project_status": project["status"],
            "financial_summary": {
                "budget_allocated": current_budget["total_budget"]
                if current_budget
                else 0,
                "budget_spent": current_budget.get("spent_amount", 0)
                if current_budget
                else 0,
                "weekly_burn_rate": weekly_resource_cost,
                "monthly_burn_rate": weekly_resource_cost * 4.33,
                "total_expenses": approved_expenses,
                "remaining_budget": (
                    current_budget["total_budget"]
                    - current_budget.get("spent_amount", 0)
                )
                if current_budget
                else 0,
            },
            "resource_allocation": {
                "active_allocations": len(project_allocations),
                "weekly_resource_hours": sum(
                    a.get("hours_per_week", 0) for a in project_allocations
                ),
                "weekly_resource_cost": weekly_resource_cost,
            },
        }

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_project_financial_summary",
                "description": "Get comprehensive financial summary for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }
