# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _ok() -> str:
    out = {"status": "success"}
    out.update(payload)
    return json.dumps(out)

def _error(msg: str) -> str:
    return json.dumps({"error": msg})

class CaV2CreateInvoiceLine(Tool):
    """Create an invoice line item."""

    @staticmethod
    def invoke(data: Dict[str, Any], hourly_rate, hours_billed, invoice_id, invoice_line_id, isbn, project_id) -> str:

        if not all([invoice_line_id, invoice_id, project_id, isbn, hours_billed, hourly_rate]):
            return _error("All line item fields are required: invoice_line_id, invoice_id, project_id, isbn, hours_billed, hourly_rate")

        line_amount = round(hours_billed * hourly_rate, 2)

        new_line = {
            "invoice_line_id": invoice_line_id,
            "invoice_id": invoice_id,
            "project_id": project_id,
            "isbn": isbn,
            "hours_billed": hours_billed,
            "hourly_rate": hourly_rate,
            "line_amount": line_amount
        }

        # Incorporate additional data.
        data.setdefault("invoice_lines", []).append(new_line)

        return _ok(
            invoice_line_id=invoice_line_id,
            line_amount=line_amount
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_invoice_line",
                "description": "Create an invoice line item with automatic amount calculation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_line_id": {"type": "string"},
                        "invoice_id": {"type": "string"},
                        "project_id": {"type": "string"},
                        "isbn": {"type": "string"},
                        "hours_billed": {"type": "number"},
                        "hourly_rate": {"type": "number"}
                    },
                    "required": ["invoice_line_id", "invoice_id", "project_id", "isbn", "hours_billed", "hourly_rate"],
                },
            },
        }