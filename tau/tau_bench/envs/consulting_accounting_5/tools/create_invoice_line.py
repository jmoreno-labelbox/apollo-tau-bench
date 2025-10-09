from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class CreateInvoiceLine(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], invoice_id: str, project_id: str, hours: int = 1, rate: float = 1.0, hst_rate: float = 0.13) -> str:
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
                        "invoice_id": {"type": "string", "description": "Invoice ID to add line to"},
                        "project_id": {"type": "string", "description": "Project ID for the line item"}
                    },
                    "required": ["invoice_id", "project_id"],
                },
            },
        }
