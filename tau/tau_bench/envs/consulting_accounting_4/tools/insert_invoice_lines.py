from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class InsertInvoiceLines(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: int = None, invoice_number: str = None, lines: list = None) -> str:
        invoice_lines = data.get("invoice_lines", [])
        invs = data.get("invoices", [])
        if invoice_id is None and invoice_number:
            inv = next(
                (i for i in invs if i.get("invoice_number") == invoice_number), None
            )
            if inv:
                invoice_id = inv.get("invoice_id")
        if invoice_id is None:
            payload = {"error": "invoice_id or invoice_number required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        lines = lines or []
        new_ids = []

        max_line_id = 0
        for line in invoice_lines:
            try:
                line_id_val = int(line.get("invoice_line_id", 0))
                if line_id_val > max_line_id:
                    max_line_id = line_id_val
            except (ValueError, TypeError):
                continue

        for ln in lines:
            max_line_id += 1
            lid = max_line_id
            invoice_lines.append(
                {
                    "invoice_line_id": lid,
                    "invoice_id": invoice_id,
                    "project_id": ln.get("project_id"),
                    "isbn": ln.get("isbn"),
                    "hours_billed": ln.get("hours"),
                    "hourly_rate": ln.get("rate"),
                    "line_amount": round(
                        float(ln.get("hours", 0)) * float(ln.get("rate", 0)), 2
                    ),
                }
            )
            new_ids.append(lid)
        payload = {"invoice_id": invoice_id, "inserted_line_ids": new_ids}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertInvoiceLines",
                "description": "Insert invoice lines for an invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                        "lines": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["lines"],
                },
            },
        }
