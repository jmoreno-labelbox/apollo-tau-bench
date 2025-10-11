# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInvoiceAuditTrail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], invoice_id) -> str:
        """
        Returns audit_ids for all audit events tied to a given invoice_id.
        """
        audit_ids = [a["audit_id"] for a in data["invoice_audit"] if a["invoice_id"] == invoice_id]
        return json.dumps(audit_ids)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInvoiceAuditTrail",
                "description": "Retrieve audit_ids of all audit events tied to a specific invoice_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string", "description": "Invoice ID to fetch audit trail"}
                    },
                    "required": ["invoice_id"],
                },
            },
        }
