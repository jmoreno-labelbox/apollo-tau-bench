# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2GetInvoiceById(Tool):
    """Get specific invoice by ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoice_id = kwargs.get("invoice_id")
        if not invoice_id:
            return _error("invoice_id is required.")

        invoices = data.get("invoices", [])
        invoice = _find_one(invoices, "invoice_id", invoice_id)
        return json.dumps(invoice) if invoice else _error(f"Invoice '{invoice_id}' not found.")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_invoice_by_id",
                "description": "Get a specific invoice by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"invoice_id": {"type": "string"}},
                    "required": ["invoice_id"],
                },
            },
        }
