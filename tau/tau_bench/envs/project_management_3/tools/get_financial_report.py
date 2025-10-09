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

class GetFinancialReport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], report_type: str, entity_id: str, fiscal_year: int = datetime.now().year) -> str:
        if not all([report_type, entity_id]):
            payload = {"error": "report_type and entity_id are required"}
            out = json.dumps(payload)
            return out

        budgets = data.get("budgets", {}).values()
        expenses = data.get("expenses", {}).values()
        purchase_orders = data.get("purchase_orders", {}).values()

        if report_type == "project":
            budget = next(
                (
                    b
                    for b in budgets.values() if b.get("project_id") == entity_id
                    and b.get("fiscal_year") == fiscal_year
                ),
                None,
            )

            if not budget:
                payload = {"error": f"No budget found for project {entity_id}"}
                out = json.dumps(payload)
                return out

            project_expenses = [
                e
                for e in expenses.values() if e.get("project_id") == entity_id
                and e.get("fiscal_year") == fiscal_year
                and e.get("status") == "approved"
            ]

            expenses_by_category = {}
            for exp in project_expenses:
                cat = exp.get("category", "Other")
                expenses_by_category[cat] = (
                    expenses_by_category.get(cat, 0) + exp["amount"]
                )

            report = {
                "report_type": "project_financial",
                "project_id": entity_id,
                "fiscal_year": fiscal_year,
                "budget_summary": {
                    "total_budget": budget["total_budget"],
                    "spent": budget.get("spent_amount", 0),
                    "committed": budget.get("committed_amount", 0),
                    "available": budget["total_budget"]
                    - budget.get("spent_amount", 0)
                    - budget.get("committed_amount", 0),
                    "utilization_rate": round(
                        (budget.get("spent_amount", 0) / budget["total_budget"] * 100),
                        2,
                    ),
                },
                "expenses_by_category": expenses_by_category,
                "total_expenses": sum(expenses_by_category.values()),
                "purchase_orders": {
                    "pending": len(
                        [
                            po
                            for po in purchase_orders.values() if po.get("project_id") == entity_id
                            and po.get("status") == "pending_approval"
                        ]
                    ),
                    "approved": len(
                        [
                            po
                            for po in purchase_orders.values() if po.get("project_id") == entity_id
                            and po.get("status") == "approved"
                        ]
                    ),
                },
                "compliance": {
                    "budget_health": (
                        "critical"
                        if budget.get("spent_amount", 0) > budget["total_budget"] * 0.9
                        else (
                            "warning"
                            if budget.get("spent_amount", 0)
                            > budget["total_budget"] * 0.8
                            else "healthy"
                        )
                    ),
                    "requires_review": budget.get("spent_amount", 0)
                    < budget["total_budget"] * 0.3,
                },
            }
            payload = report
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"Report type '{report_type}' not implemented"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFinancialReport",
                "description": "Generate financial reports for projects, departments, or vendors",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_type": {
                            "type": "string",
                            "description": "Type of report: project, department, vendor",
                        },
                        "entity_id": {
                            "type": "string",
                            "description": "ID of the entity to report on",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year",
                        },
                        "quarter": {
                            "type": "integer",
                            "description": "Quarter (1-4, optional)",
                        },
                    },
                    "required": ["report_type", "entity_id"],
                },
            },
        }
