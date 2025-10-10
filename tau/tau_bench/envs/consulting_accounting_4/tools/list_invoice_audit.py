# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListInvoiceAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inv_id = kwargs.get("invoice_id")
        inv_num = kwargs.get("invoice_number")
        rows = []
        for a in data.get("invoice_audit", []) or []:
            if inv_id and str(a.get("invoice_id")) == str(inv_id):
                rows.append(a)
            elif inv_num and a.get("invoice_number")==inv_num:
                rows.append(a)
        return json.dumps({"events": rows}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_invoice_audit",
            "description":"List audit events for an invoice by id or number.",
            "parameters":{"type":"object","properties":{"invoice_id":{"type":"string"},"invoice_number":{"type":"string"}},"required":[]}
        }}
