# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2ForecastCashFlow(Tool):
    """Forecast cash flow based on unpaid invoices and payment behavior."""

    @staticmethod
    def invoke(data: Dict[str, Any], current_date = "2024-12-10", forecast_months = 3) -> str:

        # Retrieve outstanding invoices
        invoices = data.get("invoices", [])
        unpaid_invoices = [inv for inv in invoices if not inv.get("paid_at")]

        # Retrieve payment patterns.
        payment_behaviors = data.get("payment_behavior", [])

        # Predict revenue collections
        forecasted_collections = []
        for invoice in unpaid_invoices:
            publisher_id = invoice.get("publisher_id")
            behavior = _find_one(payment_behaviors, "publisher_id", publisher_id)

            avg_days = behavior.get("avg_days_to_pay", 30) if behavior else 30
            invoice_date = datetime.fromisoformat(invoice.get("invoice_date") + "T00:00:00")
            expected_payment = invoice_date + timedelta(days=avg_days)

            forecasted_collections.append({
                "invoice_id": invoice.get("invoice_id"),
                "invoice_number": invoice.get("invoice_number"),
                "amount": invoice.get("total_due"),
                "expected_payment_date": expected_payment.strftime("%Y-%m-%d"),
                "confidence": behavior.get("payment_consistency", "moderate") if behavior else "moderate"
            })

        # Retrieve periodic expenditures.
        recurring_schedules = data.get("recurring_schedules", [])
        active_schedules = [sch for sch in recurring_schedules if sch.get("is_active")]

        # Aggregate data on a monthly basis.
        monthly_summary = {}
        for i in range(forecast_months):
            month_start = datetime.fromisoformat(current_date + "T00:00:00") + timedelta(days=30*i)
            month_key = month_start.strftime("%Y-%m")
            monthly_summary[month_key] = {
                "expected_collections": 0,
                "scheduled_expenses": 0,
                "net_flow": 0
            }

        # Incorporate collections into the summary.
        for collection in forecasted_collections:
            payment_month = collection["expected_payment_date"][:7]
            if payment_month in monthly_summary:
                monthly_summary[payment_month]["expected_collections"] += collection["amount"]

        # Incorporate costs into the summary.
        for schedule in active_schedules:
            monthly_amount = schedule.get("amount", 0)
            for month_key in monthly_summary.keys():
                if schedule.get("frequency") == "monthly":
                    monthly_summary[month_key]["scheduled_expenses"] += monthly_amount

        # Determine the net flow.
        for month_data in monthly_summary.values():
            month_data["net_flow"] = month_data["expected_collections"] - month_data["scheduled_expenses"]

        return _ok(
            forecast_period_months=forecast_months,
            forecasted_collections=forecasted_collections,
            monthly_summary=monthly_summary,
            total_expected_collections=sum(c["amount"] for c in forecasted_collections)
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_forecast_cash_flow",
                "description": "Forecast cash flow based on unpaid invoices, payment behavior, and recurring expenses.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "forecast_months": {"type": "integer", "default": 3},
                        "current_date": {"type": "string", "format": "date"}
                    },
                    "required": [],
                },
            },
        }
