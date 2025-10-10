# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeInvoiceTotals(Tool):
    """Compute subtotal, HST, and total for invoice lines."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        lines = kwargs.get("lines") or []
        hst = float(kwargs.get("hst_rate", 0.13))
        subtotal = sum(float(l.get("hours", 0)) * float(l.get("rate", 0)) for l in lines)
        hst_amount = round(subtotal * hst, 2)
        total_due = round(subtotal + hst_amount, 2)
        return json.dumps({"subtotal": round(subtotal, 2),
                           "hst_amount": hst_amount,
                           "total_due": total_due}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "compute_invoice_totals",
            "description": "Compute invoice totals.",
            "parameters": {"type": "object", "properties": {
                "lines": {"type": "array", "items": {"type": "object"}},
                "hst_rate": {"type": "number"}
            }, "required": ["lines"]}
        }}
