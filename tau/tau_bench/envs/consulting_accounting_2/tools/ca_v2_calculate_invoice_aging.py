# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _calculate_aging_days(invoice_date: str, current_date: str = "2024-12-10") -> int:
    """Calculate days between invoice date and current date"""
    try:
        invoice = datetime.fromisoformat(invoice_date.replace('Z', '+00:00') if 'T' in invoice_date else invoice_date + "T00:00:00+00:00")
        current = datetime.fromisoformat(current_date + "T00:00:00+00:00")
        return (current - invoice).days
    except:
        return 0

class CaV2CalculateInvoiceAging(Tool):
    """Calculate aging buckets for unpaid invoices."""

    @staticmethod
    def invoke(data: Dict[str, Any], current_date = "2024-12-10") -> str:

        invoices = data.get("invoices", [])
        unpaid_invoices = [inv for inv in invoices if not inv.get("paid_at")]

        aging_buckets = {
            "current": [],      # 0 to 30 days
            "31_60": [],        # 31 to 60 days
            "61_90": [],        # 61 to 90 days
            "over_90": []       # Over 90 days
        }

        for invoice in unpaid_invoices:
            days_overdue = _calculate_aging_days(invoice.get("invoice_date", ""), current_date)

            aging_info = {
                "invoice_id": invoice.get("invoice_id"),
                "invoice_number": invoice.get("invoice_number"),
                "publisher_id": invoice.get("publisher_id"),
                "total_due": invoice.get("total_due"),
                "invoice_date": invoice.get("invoice_date"),
                "days_overdue": days_overdue
            }

            if days_overdue <= 30:
                aging_buckets["current"].append(aging_info)
            elif days_overdue <= 60:
                aging_buckets["31_60"].append(aging_info)
            elif days_overdue <= 90:
                aging_buckets["61_90"].append(aging_info)
            else:
                aging_buckets["over_90"].append(aging_info)

        return json.dumps(aging_buckets)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_calculate_invoice_aging",
                "description": "Calculate aging buckets for all unpaid invoices.",
                "parameters": {
                    "type": "object",
                    "properties": {"current_date": {"type": "string", "format": "date"}},
                    "required": [],
                },
            },
        }