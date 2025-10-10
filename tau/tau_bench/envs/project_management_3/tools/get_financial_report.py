# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFinancialReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        report_type = kwargs.get("report_type")
        entity_id = kwargs.get("entity_id")
        fiscal_year = kwargs.get("fiscal_year", datetime.now().year)
        quarter = kwargs.get("quarter")

        if not all([report_type, entity_id]):
            return json.dumps({"error": "report_type and entity_id are required"})

        budgets = data.get("budgets", [])
        expenses = data.get("expenses", [])
        purchase_orders = data.get("purchase_orders", [])

        if report_type == "project":
            budget = next(
                (
                    b
                    for b in budgets
                    if b.get("project_id") == entity_id
                    and b.get("fiscal_year") == fiscal_year
                ),
                None,
            )

            if not budget:
                return json.dumps({"error": f"No budget found for project {entity_id}"})

            project_expenses = [
                e
                for e in expenses
                if e.get("project_id") == entity_id
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
                            for po in purchase_orders
                            if po.get("project_id") == entity_id
                            and po.get("status") == "pending_approval"
                        ]
                    ),
                    "approved": len(
                        [
                            po
                            for po in purchase_orders
                            if po.get("project_id") == entity_id
                            and po.get("status") == "approved"
                        ]
                    ),
                },
                "compliance": {
                    "budget_health": "critical"
                    if budget.get("spent_amount", 0) > budget["total_budget"] * 0.9
                    else "warning"
                    if budget.get("spent_amount", 0) > budget["total_budget"] * 0.8
                    else "healthy",
                    "requires_review": budget.get("spent_amount", 0)
                    < budget["total_budget"] * 0.3,
                },
            }

            return json.dumps(report, indent=2)

        return json.dumps({"error": f"Report type '{report_type}' not implemented"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_financial_report",
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
