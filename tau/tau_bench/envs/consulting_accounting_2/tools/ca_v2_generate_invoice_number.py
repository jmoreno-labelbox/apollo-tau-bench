# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2GenerateInvoiceNumber(Tool):
    """Generate next sequential invoice number for a given year."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        year = kwargs.get("year")
        if not year:
            return _error("year is required.")

        invoices = data.get("invoices", [])
        year_invoices = [inv for inv in invoices if inv.get("invoice_date", "").startswith(year)]

        # Determine the maximum value for the year.
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
            year=year
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_generate_invoice_number",
                "description": "Generate the next sequential invoice number for a given year.",
                "parameters": {
                    "type": "object",
                    "properties": {"year": {"type": "string"}},
                    "required": ["year"],
                },
            },
        }
