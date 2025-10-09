from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class CalculateInvoiceTotals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], lines: list = None, hst_rate: float = 0.13) -> str:
        """
        Calculates subtotal, hst, and total for a list of line items.
        """
        if lines is None:
            lines = []
        subtotal = sum(line.get("hours", 0) * line.get("rate", 0) for line in lines.values())
        hst_amount = round(subtotal * hst_rate, 2)
        total_due = round(subtotal + hst_amount, 2)
        return json.dumps({"subtotal": subtotal, "hst_amount": hst_amount, "total_due": total_due})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "CalculateInvoiceTotals",
                "description": "A simple calculator to compute invoice totals from line items.",
                "parameters": {
                    "type": "object", "properties": {
                        "lines": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {"hours": {"type": "number"}, "rate": {"type": "number"}}
                            }
                        },
                        "hst_rate": {"type": "number", "description": "The HST rate to apply, e.g., 0.13 for 13%"}
                    },
                    "required": ["lines", "hst_rate"],
                },
            },
        }
