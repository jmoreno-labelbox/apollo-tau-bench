# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListInvoiceLines(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoice_id = kwargs.get("invoice_id")
        invoice_number = kwargs.get("invoice_number")
        invs = data.get("invoices", [])
        if invoice_id is None and invoice_number:
            inv = next((i for i in invs if i.get("invoice_number")==invoice_number), None)
            if inv: invoice_id = inv.get("invoice_id")
        rows = [l for l in data.get("invoice_lines", []) if str(l.get("invoice_id")) == str(invoice_id)] if invoice_id else []
        return json.dumps({"invoice_id": invoice_id, "lines": rows}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_invoice_lines",
            "description":"List lines for an invoice by id or number.",
            "parameters":{"type":"object","properties":{"invoice_id":{"type":"string"},"invoice_number":{"type":"string"}},"required":[]}
        }}
