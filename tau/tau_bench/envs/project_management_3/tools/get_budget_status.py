from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetBudgetStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str, fiscal_year: int = datetime.now().year) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        budgets = data.get("budgets", {}).values()
        expenses = data.get("expenses", {}).values()
        purchase_orders = data.get("purchase_orders", {}).values()

        budget = next(
            (
                b
                for b in budgets.values() if b.get("project_id") == project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        if not budget:
            payload = {
                    "error": f"No budget found for project {project_id} in fiscal year {fiscal_year}"
                }
            out = json.dumps(
                payload)
            return out

        pending_expenses = sum(
            e.get("amount", 0)
            for e in expenses.values() if e.get("project_id") == project_id
            and e.get("status") == "pending_approval"
            and e.get("fiscal_year") == fiscal_year
        )

        pending_pos = sum(
            po.get("total_amount", 0)
            for po in purchase_orders.values() if po.get("project_id") == project_id
            and po.get("status") == "pending_approval"
        )

        total_budget = budget["total_budget"]
        spent = budget.get("spent_amount", 0)
        committed = budget.get("committed_amount", 0)
        available = total_budget - spent - committed

        utilization_rate = (spent / total_budget * 100) if total_budget > 0 else 0
        burn_rate = (
            ((spent + committed) / total_budget * 100) if total_budget > 0 else 0
        )

        status = {
            "project_id": project_id,
            "fiscal_year": fiscal_year,
            "total_budget": total_budget,
            "spent_amount": spent,
            "committed_amount": committed,
            "available_amount": available,
            "pending_expenses": pending_expenses,
            "pending_purchase_orders": pending_pos,
            "utilization_rate": round(utilization_rate, 2),
            "burn_rate": round(burn_rate, 2),
            "budget_health": (
                "critical"
                if burn_rate > 90
                else "warning" if burn_rate > 80 else "healthy"
            ),
            "requires_modification": burn_rate > 110,
        }
        payload = status
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBudgetStatus",
                "description": "Get current budget status and utilization for a project",
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
