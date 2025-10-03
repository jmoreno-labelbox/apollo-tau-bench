from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2GenerateInvoiceNumber(Tool):
    """Create the next sequential invoice number for a specified year."""

    @staticmethod
    def invoke(data: dict[str, Any], year: str = None) -> str:
        if not year:
            return _error("year is required.")

        invoices = data.get("invoices", [])
        year_invoices = [
            inv for inv in invoices if inv.get("invoice_date", "").startswith(year)
        ]

        # Identify the maximum value for the year
        max_number = 0
        for invoice in year_invoices:
            invoice_number = invoice.get("invoice_number", "")
            if invoice_number.startswith(f"{year}-"):
                try:
                    number = int(invoice_number.split("-")[1])
                    max_number = max(max_number, number)
                except:
                    continue

        next_number = max_number + 1
        next_invoice_number = f"{year}-{next_number:03d}"

        return _ok(
            next_invoice_number=next_invoice_number,
            sequence_number=next_number,
            year=year,
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GenerateInvoiceNumber",
                "description": "Generate the next sequential invoice number for a given year.",
                "parameters": {
                    "type": "object",
                    "properties": {"year": {"type": "string"}},
                    "required": ["year"],
                },
            },
        }
