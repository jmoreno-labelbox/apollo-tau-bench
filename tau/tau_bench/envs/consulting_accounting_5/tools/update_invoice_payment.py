# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInvoicePayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], invoice_id, paid_at) -> str:
        """
        Marks an invoice as paid by updating paid_at field.
        """
        updated = None
        for inv in data["invoices"]:
            if inv["invoice_id"] == invoice_id:
                inv["paid_at"] = paid_at
                updated = inv
                break
        return json.dumps(updated if updated else {})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInvoicePayment",
                "description": "Update the paid_at timestamp for a given invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "paid_at": {"type": "string", "description": "Datetime string for payment confirmation"}
                    },
                    "required": ["invoice_id", "paid_at"],
                },
            },
        }
