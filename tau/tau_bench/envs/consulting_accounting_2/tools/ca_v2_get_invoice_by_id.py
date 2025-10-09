from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2GetInvoiceById(Tool):
    """Retrieve a specific invoice using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None) -> str:
        if not invoice_id:
            return _error("invoice_id is required.")

        invoices = data.get("invoices", [])
        invoice = _find_one(invoices, "invoice_id", invoice_id)
        return (
            json.dumps(invoice)
            if invoice
            else _error(f"Invoice '{invoice_id}' not found.")
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetInvoiceById",
                "description": "Get a specific invoice by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"invoice_id": {"type": "string"}},
                    "required": ["invoice_id"],
                },
            },
        }
