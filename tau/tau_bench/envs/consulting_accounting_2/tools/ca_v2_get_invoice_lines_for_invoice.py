# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _find_all(lst: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    return [x for x in lst or [] if x.get(key) == value]

def _error(msg: str) -> str:
    return json.dumps({"error": msg})

class CaV2GetInvoiceLinesForInvoice(Tool):
    """Get all invoice lines for a specific invoice."""

    @staticmethod
    def invoke(data: Dict[str, Any], invoice_id) -> str:
        if not invoice_id:
            return _error("invoice_id is required.")

        invoice_lines = data.get("invoice_lines", [])
        lines = _find_all(invoice_lines, "invoice_id", invoice_id)
        return json.dumps(lines)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_invoice_lines_for_invoice",
                "description": "Get all line items for a specific invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {"invoice_id": {"type": "string"}},
                    "required": ["invoice_id"],
                },
            },
        }