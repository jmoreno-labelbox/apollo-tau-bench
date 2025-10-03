from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2GetInvoiceLinesForInvoice(Tool):
    """Retrieve all line items for a specific invoice."""

    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None) -> str:
        if not invoice_id:
            return _error("invoice_id is required.")

        invoice_lines = data.get("invoice_lines", [])
        lines = _find_all(invoice_lines, "invoice_id", invoice_id)
        payload = lines
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetInvoiceLinesForInvoice",
                "description": "Get all line items for a specific invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {"invoice_id": {"type": "string"}},
                    "required": ["invoice_id"],
                },
            },
        }
