from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2CalculateInvoiceAging(Tool):
    """Determine aging categories for outstanding invoices."""

    @staticmethod
    def invoke(data: dict[str, Any], current_date: str = "2024-12-10") -> str:
        invoices = data.get("invoices", [])
        unpaid_invoices = [inv for inv in invoices if not inv.get("paid_at")]

        aging_buckets = {
            "current": [],  # 0 to 30 days
            "31_60": [],  # 31 to 60 days
            "61_90": [],  # 61 to 90 days
            "over_90": [],  # More than 90 days
        }

        for invoice in unpaid_invoices:
            days_overdue = _calculate_aging_days(
                invoice.get("invoice_date", ""), current_date
            )

            aging_info = {
                "invoice_id": invoice.get("invoice_id"),
                "invoice_number": invoice.get("invoice_number"),
                "publisher_id": invoice.get("publisher_id"),
                "total_due": invoice.get("total_due"),
                "invoice_date": invoice.get("invoice_date"),
                "days_overdue": days_overdue,
            }

            if days_overdue <= 30:
                aging_buckets["current"].append(aging_info)
            elif days_overdue <= 60:
                aging_buckets["31_60"].append(aging_info)
            elif days_overdue <= 90:
                aging_buckets["61_90"].append(aging_info)
            else:
                aging_buckets["over_90"].append(aging_info)
        payload = aging_buckets
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CalculateInvoiceAging",
                "description": "Calculate aging buckets for all unpaid invoices.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_date": {"type": "string", "format": "date"}
                    },
                    "required": [],
                },
            },
        }
