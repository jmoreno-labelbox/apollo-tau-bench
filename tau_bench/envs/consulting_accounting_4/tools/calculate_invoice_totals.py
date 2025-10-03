from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class CalculateInvoiceTotals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], lines: list = None, hst_rate: float = 0.13) -> str:
        lines = lines or []
        hst = float(hst_rate)
        subtotal = sum(
            float(l.get("hours", 0)) * float(l.get("rate", 0)) for l in lines
        )
        hst_amount = round(subtotal * hst, 2)
        total_due = round(subtotal + hst_amount, 2)
        payload = {
                "subtotal": round(subtotal, 2),
                "hst_amount": hst_amount,
                "total_due": total_due,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateInvoiceTotals",
                "description": "Compute subtotal, HST, and total_due for invoice lines.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lines": {"type": "array", "items": {"type": "object"}},
                        "hst_rate": {"type": "number"},
                    },
                    "required": ["lines"],
                },
            },
        }
