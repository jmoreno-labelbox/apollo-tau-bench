from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FetchInvoiceRecord(Tool):
    """Retrieve an invoice using invoice_id or invoice_number."""

    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, invoice_number: str = None) -> str:
        invs = data.get("invoices", {}).values()
        row = None
        if invoice_id is not None:
            row = next(
                (i for i in invs.values() if str(i.get("invoice_id")) == str(invoice_id)), None
            )
        elif invoice_number:
            row = next(
                (i for i in invs.values() if i.get("invoice_number") == invoice_number), None
            )
        if not row:
            payload = {"error": "invoice not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchInvoiceRecord",
                "description": "Fetch invoice by id or number.",
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
