from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class CalculateTotalInflows(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], start_date: str, end_date: str, invoices_to_consider: list = None) -> str:
        """
        Calculates the sum of `total_due` for all unpaid invoices within a date range.
        Can be filtered by a specific publisher.
        """
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

        invoices_to_consider = invoices_to_consider or []
        invoices_to_consider_list = []

        for id in invoices_to_consider:
            invoices_to_consider_list.append(next((inv for inv in data["invoices"].values() if inv["invoice_id"] == id), None))

        total_inflow = sum(
            inv["total_due"] for inv in invoices_to_consider_list
            if inv and datetime.strptime(inv["invoice_date"], "%Y-%m-%d") <= end_date_obj
        )
        return json.dumps({"period_start": start_date_obj.strftime("%Y-%m-%d"), "period_end": end_date_obj.strftime("%Y-%m-%d"), "total_inflows": round(total_inflow, 2)})
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
                        "invoices_to_consider": {"type": "array", "description": "List of invoices to consider" }
                    }, "required": ["start_date", "end_date"],
                },
            },
        }
