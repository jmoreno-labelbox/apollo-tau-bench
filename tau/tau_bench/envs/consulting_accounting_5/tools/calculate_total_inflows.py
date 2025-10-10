# Copyright Sierra

from datetime import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateTotalInflows(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Calculates the sum of `total_due` for all unpaid invoices within a date range.
        Can be filtered by a specific publisher.
        """
        start_date = datetime.strptime(kwargs["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(kwargs["end_date"], "%Y-%m-%d")

        invoices_ids = kwargs.get("invoices_to_consider", None)
        invoices_to_consider = []

        for id in invoices_ids:
            invoices_to_consider.append(next((inv for inv in data["invoices"] if inv["invoice_id"] == id), None))

        # Considers past-due invoices as immediately receivable within the window.
        total_inflow = sum(
            inv["total_due"] for inv in invoices_to_consider
            if datetime.strptime(inv["invoice_date"], "%Y-%m-%d") <= end_date
        )
        return json.dumps({"period_start": kwargs["start_date"], "period_end": kwargs["end_date"], "total_inflows": round(total_inflow, 2)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "CalculateTotalInflows",
                "description": "Calculates the sum of all unpaid invoices expected within a date range, optionally for a specific publisher.",
                "parameters": {
                    "type": "object", "properties": {
                        "start_date": {"type": "string", "description": "Start of the forecast period (YYYY-MM-DD)"},
                        "end_date": {"type": "string", "description": "End of the forecast period (YYYY-MM-DD)"},
                        "invoices_to_consider": {"type": "object", "description": "List of invoices to consider" }
                    }, "required": ["start_date", "end_date"],
                },
            },
        }
