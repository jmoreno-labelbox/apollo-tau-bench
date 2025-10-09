from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CaV2ForecastCashFlow(Tool):
    """Predict cash flow considering outstanding invoices and payment patterns."""

    @staticmethod
    def invoke(data: dict[str, Any], forecast_months: int = 3, current_date: str = "2024-12-10") -> str:
        # Retrieve outstanding invoices
        invoices = data.get("invoices", {}).values()
        unpaid_invoices = [inv for inv in invoices.values() if not inv.get("paid_at")]

        # Retrieve payment patterns
        payment_behaviors = data.get("payment_behavior", {}).values()

        # Predict collections
        forecasted_collections = []
        for invoice in unpaid_invoices:
            publisher_id = invoice.get("publisher_id")
            behavior = _find_one(list(payment_behaviors.values()), "publisher_id", publisher_id)

            avg_days = behavior.get("avg_days_to_pay", 30) if behavior else 30
            invoice_date = datetime.fromisoformat(
                invoice.get("invoice_date") + "T00:00:00"
            )
            expected_payment = invoice_date + timedelta(days=avg_days)

            forecasted_collections.append(
                {
                    "invoice_id": invoice.get("invoice_id"),
                    "invoice_number": invoice.get("invoice_number"),
                    "amount": invoice.get("total_due"),
                    "expected_payment_date": expected_payment.strftime("%Y-%m-%d"),
                    "confidence": (
                        behavior.get("payment_consistency", "moderate")
                        if behavior
                        else "moderate"
                    ),
                }
            )

        # Retrieve regular expenses
        recurring_schedules = data.get("recurring_schedules", {}).values()
        active_schedules = [sch for sch in recurring_schedules.values() if sch.get("is_active")]

        # Condense data monthly
        monthly_summary = {}
        for i in range(forecast_months):
            month_start = datetime.fromisoformat(
                current_date + "T00:00:00"
            ) + timedelta(days=30 * i)
            month_key = month_start.strftime("%Y-%m")
            monthly_summary[month_key] = {
                "expected_collections": 0,
                "scheduled_expenses": 0,
                "net_flow": 0,
            }

        # Include collections in summary
        for collection in forecasted_collections:
            payment_month = collection["expected_payment_date"][:7]
            if payment_month in monthly_summary:
                monthly_summary[payment_month]["expected_collections"] += collection[
                    "amount"
                ]

        # Include expenses in summary
        for schedule in active_schedules:
            monthly_amount = schedule.get("amount", 0)
            for month_key in monthly_summary.keys():
                if schedule.get("frequency") == "monthly":
                    monthly_summary[month_key]["scheduled_expenses"] += monthly_amount

        # Compute net cash flow
        for month_data in monthly_summary.values():
            month_data["net_flow"] = (
                month_data["expected_collections"] - month_data["scheduled_expenses"]
            )

        return _ok(
            forecast_period_months=forecast_months,
            forecasted_collections=forecasted_collections,
            monthly_summary=monthly_summary,
            total_expected_collections=sum(c["amount"] for c in forecasted_collections.values()),
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2ForecastCashFlow",
                "description": "Forecast cash flow based on unpaid invoices, payment behavior, and recurring expenses.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "forecast_months": {"type": "integer", "default": 3},
                        "current_date": {"type": "string", "format": "date"},
                    },
                    "required": [],
                },
            },
        }
