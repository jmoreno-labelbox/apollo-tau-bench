# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInvoiceDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], invoice_id, invoice_number) -> str:
        invs = data.get("invoices", [])
        row = None
        if invoice_id is not None:
            row = next((i for i in invs if str(i.get("invoice_id")) == str(invoice_id)), None)
        elif invoice_number:
            row = next((i for i in invs if i.get("invoice_number") == invoice_number), None)
        if not row:
            return json.dumps({"error":"Invoice not found"}, indent=2)
        return json.dumps(row, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_invoice_details",
            "description":"Read an invoice by id or invoice_number.",
            "parameters":{"type":"object","properties":{
                "invoice_id":{"type":"string"},"invoice_number":{"type":"string"}
            },"required":[]}
        }}
