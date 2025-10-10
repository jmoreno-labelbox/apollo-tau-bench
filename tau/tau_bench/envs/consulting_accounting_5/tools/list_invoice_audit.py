# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListInvoiceAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], audit_id, invoice_id) -> str:
        results = []
        if audit_id:
            results = [a for a in data["invoice_audit"] if a["audit_id"] == audit_id]
        if invoice_id:
            results = [a for a in data["invoice_audit"] if a["invoice_id"] == invoice_id]

        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListInvoiceAudit",
                "description": "List invoice audit from invoice_audit.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                    },
                    "required": ["audit_id" ],
                },
            },
        }
