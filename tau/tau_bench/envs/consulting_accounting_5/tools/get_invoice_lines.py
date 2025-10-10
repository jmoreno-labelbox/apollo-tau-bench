# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInvoiceLines(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns invoice_line_ids for a given invoice_id.
        """
        invoice_id = kwargs["invoice_id"]
        lines = [ln for ln in data["invoice_lines"] if ln["invoice_id"] == invoice_id]
        return json.dumps([ln["line_id"] for ln in lines])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInvoiceLines",
                "description": "Retrieve all invoice_line_ids for a given invoice_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string", "description": "Invoice ID to fetch line items for"}
                    },
                    "required": ["invoice_id"],
                },
            },
        }
