# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInvoiceDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoice_id = kwargs.get("invoice_id")
        if not invoice_id:
            return json.dumps({"error": "invoice_id is required"}, indent=2)
        invoices = list(data.get("invoices", {}).values())
        inv = next((i for i in invoices if i.get("invoice_id") == invoice_id), None)
        return json.dumps(inv or {"error": f"Invoice {invoice_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "get_invoice_details","description": "Retrieve all data for a specific invoice.","parameters": {"type": "object","properties": {"invoice_id": {"type": "string","description": "The ID of the invoice."}},"required": ["invoice_id"]}}}
