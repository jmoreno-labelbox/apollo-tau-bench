from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListInvoiceLines(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, invoice_number: str = None) -> str:
        invs = data.get("invoices", [])
        if invoice_id is None and invoice_number:
            inv = next(
                (i for i in invs if i.get("invoice_number") == invoice_number), None
            )
            if inv:
                invoice_id = inv.get("invoice_id")
        rows = (
            [
                l
                for l in data.get("invoice_lines", [])
                if str(l.get("invoice_id")) == str(invoice_id)
            ]
            if invoice_id
            else []
        )
        payload = {"invoice_id": invoice_id, "lines": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListInvoiceLines",
                "description": "List lines for an invoice by id or number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
