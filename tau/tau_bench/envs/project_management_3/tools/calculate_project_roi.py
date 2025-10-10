# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateProjectROI(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        revenue_generated = kwargs.get("revenue_generated", 0)
        cost_savings = kwargs.get("cost_savings", 0)
        fiscal_year = kwargs.get("fiscal_year", datetime.now().year)

        if not project_id:
            return json.dumps({"error": "project_id is required"})

        projects = list(data.get("projects", {}).values())
        budgets = data.get("budgets", [])
        expenses = data.get("expenses", [])
        allocations = data.get("allocations", [])
        employees = list(data.get("employees", {}).values())
        task_logs = data.get("task_logs", [])
        tasks = list(data.get("tasks", {}).values())

        project = next((p for p in projects if p.get("project_id") == project_id), None)
        if not project:
            return json.dumps({"error": f"Project {project_id} not found"})

        project_budget = next(
            (
                b
                for b in budgets
                if b.get("project_id") == project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        budgeted_amount = project_budget["total_budget"] if project_budget else 0
        spent_amount = project_budget.get("spent_amount", 0) if project_budget else 0

        project_tasks = [
            t
            for t in tasks
            if any(
                a.get("project_id") == project_id
                for a in allocations
                if a.get("employee_id") == t.get("assignee_id")
            )
        ]

        actual_personnel_cost = 0
        for task in project_tasks:
            task_time_logs = [
                log for log in task_logs if log.get("task_id") == task["task_id"]
            ]

            for log in task_time_logs:
                employee_id = log.get("employee_id")
                hours = log.get("hours", 0)

                employee = next(
                    (e for e in employees if e.get("employee_id") == employee_id), None
                )
                if employee:
                    hourly_rate = (
                        150 if "senior" in employee.get("role", "").lower() else 100
                    )
                    actual_personnel_cost += hours * hourly_rate

        project_expenses = [
            e
            for e in expenses
            if e.get("project_id") == project_id and e.get("status") == "approved"
        ]

        total_expense_cost = sum(e.get("amount", 0) for e in project_expenses)

        total_actual_cost = actual_personnel_cost + total_expense_cost

        total_benefit = revenue_generated + cost_savings
        roi_percentage = (
            ((total_benefit - total_actual_cost) / total_actual_cost * 100)
            if total_actual_cost > 0
            else 0
        )

        monthly_benefit = total_benefit / 12
        payback_months = (
            total_actual_cost / monthly_benefit if monthly_benefit > 0 else float("inf")
        )

        roi_analysis = {
            "roi_percentage": round(roi_percentage, 2),
            "project_id": project_id,
            "project_name": project["name"],
            "project_status": project["status"],
            "financial_metrics": {
                "budgeted_cost": budgeted_amount,
                "actual_cost": total_actual_cost,
                "personnel_cost": actual_personnel_cost,
                "expense_cost": total_expense_cost,
                "budget_variance": budgeted_amount - total_actual_cost,
            },
            "benefit_metrics": {
                "revenue_generated": revenue_generated,
                "cost_savings": cost_savings,
                "total_benefit": total_benefit,
            },
            "roi_calculations": {
                "roi_percentage": round(roi_percentage, 2),
                "net_benefit": total_benefit - total_actual_cost,
                "benefit_cost_ratio": round(total_benefit / total_actual_cost, 2)
                if total_actual_cost > 0
                else 0,
                "payback_period_months": round(payback_months, 1)
                if payback_months != float("inf")
                else "N/A",
            },
            "roi_status": "positive" if roi_percentage > 0 else "negative",
            "meets_target": roi_percentage >= 15,
        }

        return json.dumps(roi_analysis, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_project_roi",
                "description": "Calculate return on investment (ROI) for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "revenue_generated": {
                            "type": "number",
                            "description": "Revenue generated by project",
                        },
                        "cost_savings": {
                            "type": "number",
                            "description": "Cost savings achieved",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }
