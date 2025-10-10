# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComposeInvoicePdf(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoice_id = kwargs.get("invoice_id")
        publisher_id = kwargs.get("publisher_id")
        if not invoice_id or not publisher_id:
            return json.dumps({"error": "invoice_id and publisher_id are required"}, indent=2)
        path = f"/invoices/auto/{invoice_id}.pdf"
        return json.dumps({"invoice_id": invoice_id,"publisher_id": publisher_id,"pdf_path": path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "compose_invoice_pdf","description": "Generate a PDF artifact path for the invoice.","parameters": {"type": "object","properties": {"invoice_id": {"type": "string"},"publisher_id": {"type": "string"}},"required": ["invoice_id","publisher_id"]}}}
