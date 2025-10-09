from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class FilterInvoices(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        publisher_id: str = None,
        invoice_number: str = None,
        invoice_date: str = None,
        start_date: str = None,
        end_date: str = None,
        unpaid_only: bool = False,
        min_amount: float = None,
        max_amount: float = None
    ) -> str:
        """
        Filter invoices by conditions such as invoice_number, date range, amount, or paid/unpaid status.
        Returns a list of matching invoice_ids.
        """
        invoices = data["invoices"]
        results = invoices

        if publisher_id is not None:
            results = [inv for inv in results.values() if inv["publisher_id"] == publisher_id]

        if invoice_number is not None:
            results = [inv for inv in results.values() if inv["invoice_number"] == invoice_number]

        if invoice_date is not None:
            results = [inv for inv in results.values() if inv["invoice_date"] == invoice_date]

        if start_date is not None and end_date is not None:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            results = [
                inv for inv in results
                if start <= datetime.strptime(inv["invoice_date"], "%Y-%m-%d") <= end
            ]

        if unpaid_only:
            results = [inv for inv in results.values() if inv.get("paid_at") is None]

        if min_amount is not None:
            results = [inv for inv in results.values() if float(inv["total_due"]) >= min_amount]
        if max_amount is not None:
            results = [inv for inv in results.values() if float(inv["total_due"]) <= max_amount]

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
