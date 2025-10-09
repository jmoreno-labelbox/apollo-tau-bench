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

class CreateProjectBudget(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str = None,
        fiscal_year: int = None,
        total_budget: float = None,
        budget_categories: dict = None,
        budget_id: str = None
    ) -> str:
        if budget_categories is None:
            budget_categories = {}

        if not all([project_id, fiscal_year, total_budget]):
            payload = {"error": "project_id, fiscal_year, and total_budget are required"}
            out = json.dumps(payload)
            return out

        budgets = data.get("budgets", [])
        projects = data.get("projects", [])
        allocations = data.get("allocations", [])
        employees = data.get("employees", [])

        project = next((p for p in projects if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project {project_id} not found"}
            out = json.dumps(payload)
            return out

        if project.get("status") not in ["active", "planning"]:
            payload = {
                "error": f"Cannot create budget for project with status: {project.get('status')}"
            }
            out = json.dumps(payload)
            return out

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
            payload = {
                "error": f"Personnel costs (${total_personnel_cost}) exceed 80% of total budget. Increase budget or reduce allocations.",
                "suggested_budget": int(total_personnel_cost / 0.8),
            }
            out = json.dumps(payload)
            return out

        if budget_id is None:
            budget_id = f"budget_{uuid.uuid4().hex[:8]}"

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
        payload = {"success": True, "budget": new_budget}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateProjectBudget",
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
