# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListInvoiceEvents(Tool):
    """List all audit events for an invoice."""
    @staticmethod
    def invoke(data: Dict[str, Any], invoice_id, invoice_number) -> str:
        inv_id = invoice_id
        inv_no = invoice_number
        events = []
        for a in data.get("invoice_audit", []) or []:
            if inv_id and str(a.get("invoice_id")) == str(inv_id):
                events.append(a)
            elif inv_no and a.get("invoice_number") == inv_no:
                events.append(a)
        return json.dumps({"events": events}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "list_invoice_events",
            "description": "List audit events by invoice id or number.",
            "parameters": {"type": "object", "properties": {
                "invoice_id": {"type": "string"},
                "invoice_number": {"type": "string"}
            }, "required": []}
        }}
