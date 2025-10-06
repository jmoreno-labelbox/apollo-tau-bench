from tau_bench.envs.tool import Tool
import json
from typing import Any

class CalculateTotals(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], hst_rate: float = 0.13, invoice_lines: list = None) -> str:
        if invoice_lines is None:
            invoice_lines = []
        if (
            isinstance(invoice_lines, list)
            and invoice_lines
            and isinstance(invoice_lines[0], dict)
        ):
            subtotal = sum(float(l.get("line_amount", 0.0)) for l in invoice_lines)
        else:
            subtotal = 0.0
            lines_index = {
                l["invoice_line_id"]: l for l in data.get("invoice_lines", [])
            }
            for lid in invoice_lines:
                line = lines_index.get(lid)
                if line:
                    subtotal += float(line.get("line_amount", 0.0))
        hst_amount = round(subtotal * hst_rate, 2)
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
                "name": "CalculateTotals",
                "description": "Calculate subtotal, HST and total due based on provided invoice lines.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_lines": {
                            "type": "array",
                            "items": {
},
                        },
                        "hst_rate": {"type": "number"},
                    },
                    "required": ["invoice_lines"],
                },
            },
        }
