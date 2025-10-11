# Copyright Sierra

from datetime import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterInvoices(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], end_date, invoice_date, invoice_number, max_amount, min_amount, publisher_id, start_date, unpaid_only) -> str:
        """
        Filter invoices by conditions such as invoice_number, date range, amount, or paid/unpaid status.
        Returns a list of matching invoice_ids.
        """
        invoices = data["invoices"]
        results = invoices

        # Filter based on invoice_number.
        if "publisher_id" in kwargs:
            results = [inv for inv in results if inv["publisher_id"] == publisher_id]

        # Filter based on invoice_number.
        if "invoice_number" in kwargs:
            results = [inv for inv in results if inv["invoice_number"] == invoice_number]

        if "invoice_date" in kwargs:
            results = [inv for inv in results if inv["invoice_date"] == invoice_date]

        # Restrict by date interval
        if "start_date" in kwargs and "end_date" in kwargs:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            results = [
                inv for inv in results
                if start <= datetime.strptime(inv["invoice_date"], "%Y-%m-%d") <= end
            ]

        # Select only invoices that are unpaid.
        if unpaid_only:
            results = [inv for inv in results if inv.get("paid_at") is None]

        # Filter based on the specified minimum and maximum values.
        if "min_amount" in kwargs:
            results = [inv for inv in results if float(inv["total_due"]) >= min_amount]
        if "max_amount" in kwargs:
            results = [inv for inv in results if float(inv["total_due"]) <= max_amount]

        return json.dumps([inv["invoice_id"] for inv in results])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterInvoices",
                "description": "Filter publisher invoices by invoice_number, date range, unpaid_only, or amount thresholds.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_number": {"type": "string"},
                        "start_date": {"type": "string", "description": "Start of invoice_date range (YYYY-MM-DD)"},
                        "end_date": {"type": "string", "description": "End of invoice_date range (YYYY-MM-DD)"},
                        "unpaid_only": {"type": "boolean", "description": "Filter only unpaid invoices"},
                        "min_amount": {"type": "number", "description": "Minimum invoice total_due"},
                        "max_amount": {"type": "number", "description": "Maximum invoice total_due"}
                    },
                    "required": [],
                },
            },
        }
