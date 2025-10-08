from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2CreateInvoiceLine(Tool):
    """Generate a line item for an invoice."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        invoice_line_id: str = None,
        invoice_id: str = None,
        project_id: str = None,
        isbn: str = None,
        hours_billed: float = None,
        hourly_rate: float = None
    ) -> str:
        # Necessary parameters

        if not all(
            [invoice_line_id, invoice_id, project_id, isbn, hours_billed, hourly_rate]
        ):
            return _error(
                "All line item fields are required: invoice_line_id, invoice_id, project_id, isbn, hours_billed, hourly_rate"
            )

        line_amount = round(hours_billed * hourly_rate, 2)

        new_line = {
            "invoice_line_id": invoice_line_id,
            "invoice_id": invoice_id,
            "project_id": project_id,
            "isbn": isbn,
            "hours_billed": hours_billed,
            "hourly_rate": hourly_rate,
            "line_amount": line_amount,
        }

        # Insert into data
        data.setdefault("invoice_lines", []).append(new_line)

        return _ok(invoice_line_id=invoice_line_id, line_amount=line_amount)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateInvoiceLine",
                "description": "Create an invoice line item with automatic amount calculation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_line_id": {"type": "string"},
                        "invoice_id": {"type": "string"},
                        "project_id": {"type": "string"},
                        "isbn": {"type": "string"},
                        "hours_billed": {"type": "number"},
                        "hourly_rate": {"type": "number"},
                    },
                    "required": [
                        "invoice_line_id",
                        "invoice_id",
                        "project_id",
                        "isbn",
                        "hours_billed",
                        "hourly_rate",
                    ],
                },
            },
        }
