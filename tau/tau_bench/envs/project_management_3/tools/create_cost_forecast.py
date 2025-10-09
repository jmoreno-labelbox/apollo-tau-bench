from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateCostForecast(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        forecast_months: int = 3,
        include_contingency: bool = True,
        fiscal_year: int = datetime.now().year,
    ) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", [])
        allocations = data.get("allocations", [])
        employees = data.get("employees", [])
        budgets = data.get("budgets", [])
        cost_forecasts = data.get("cost_forecasts", [])

        project = next((p for p in projects if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project {project_id} not found"}
            out = json.dumps(payload)
            return out

        project_allocations = [
            a
            for a in allocations
            if a.get("project_id") == project_id and a.get("status") == "active"
        ]

        monthly_personnel_cost = 0
        for alloc in project_allocations:
            employee = next(
                (e for e in employees if e.get("employee_id") == alloc["employee_id"]),
                None,
            )
            if employee:
                hourly_rate = (
                    150 if "senior" in employee.get("role", "").lower() else 100
                )
                monthly_personnel_cost += (
                    alloc.get("hours_per_week", 0) * hourly_rate * 4.33
                )

        monthly_non_personnel = monthly_personnel_cost * 0.2
        monthly_total = monthly_personnel_cost + monthly_non_personnel

        forecast_data = []
        cumulative_cost = 0

        for month in range(1, forecast_months + 1):
            if include_contingency:
                month_cost = monthly_total * (1 + 0.1 * month / forecast_months)
            else:
                month_cost = monthly_total

            cumulative_cost += month_cost

            forecast_data.append(
                {
                    "month": month,
                    "personnel_cost": (
                        monthly_personnel_cost * (1 + 0.1 * month / forecast_months)
                        if include_contingency
                        else monthly_personnel_cost
                    ),
                    "non_personnel_cost": (
                        monthly_non_personnel * (1 + 0.1 * month / forecast_months)
                        if include_contingency
                        else monthly_non_personnel
                    ),
                    "total_cost": month_cost,
                    "cumulative_cost": cumulative_cost,
                }
            )

        current_budget = next(
            (
                b
                for b in budgets
                if b.get("project_id") == project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        budget_exhaustion_month = None
        if current_budget:
            remaining_budget = current_budget["total_budget"] - current_budget.get(
                "spent_amount", 0
            )
            for i, month_data in enumerate(forecast_data):
                if month_data["cumulative_cost"] > remaining_budget:
                    budget_exhaustion_month = i + 1
                    break

        forecast_id = f"forecast_{uuid.uuid4().hex[:8]}"

        new_forecast = {
            "budget_exhaustion_month": budget_exhaustion_month,
            "forecast_id": forecast_id,
            "project_id": project_id,
            "forecast_months": forecast_months,
            "monthly_burn_rate": monthly_total,
            "forecast_data": forecast_data,
            "total_forecasted_cost": cumulative_cost,
            "includes_contingency": include_contingency,
            "created_date": datetime.now().isoformat(),
        }

        cost_forecasts.append(new_forecast)
        payload = {"success": True, "forecast": new_forecast}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCostForecast",
                "description": "Create a cost forecast for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "forecast_months": {
                            "type": "integer",
                            "description": "Number of months to forecast",
                        },
                        "include_contingency": {
                            "type": "boolean",
                            "description": "Include contingency in forecast",
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
