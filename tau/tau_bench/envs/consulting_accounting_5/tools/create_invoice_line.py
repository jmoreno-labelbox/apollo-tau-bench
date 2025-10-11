# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateInvoiceLine(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], invoice_id, project_id, hours = 1, hst_rate = 0.13, rate = 1) -> str:
        """
        Insert a new invoice line linked to an existing invoice_id.
        Deterministic: uses provided invoice_id, project_id, isbn, hours, rate, hst_rate.
        Returns created line_id.
        """

        line_id = f"LINE-{len(data['invoice_lines'])+1:04d}"
        line_total = round(hours * rate, 2)
        hst_amount = round(line_total * hst_rate, 2)

        new_line = {
            "line_id": line_id,
            "invoice_id": invoice_id,
            "project_id": project_id,
            "hours": hours,
            "rate": rate,
            "line_total": line_total,
            "hst_amount": hst_amount
        }
        data["invoice_lines"].append(new_line)
        return json.dumps(new_line)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInvoiceLine",
                "description": "Create a line item for an invoice using project time entry details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string", "description": "Publisher ID to filter invoices by"}
                    },
                    "required": ["invoice_id",'project_id'],
                },
            },
        }
