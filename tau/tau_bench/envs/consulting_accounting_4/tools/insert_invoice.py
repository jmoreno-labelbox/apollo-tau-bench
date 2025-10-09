from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class InsertInvoice(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        invoice_number: str = None,
        publisher_id: str = None,
        invoice_date: str = None,
        period_start: str = None,
        period_end: str = None,
        subtotal: float = None,
        hst_amount: float = None,
        total_due: float = None,
        pdf_path: str = None
    ) -> str:
        invoices = data.get("invoices", {}).values()

        prefix = "INV"
        max_num = 0
        for inv in invoices.values():
            inv_id_str = str(inv.get("invoice_id", ""))
            if inv_id_str.startswith(prefix):
                numeric_part = inv_id_str[len(prefix) :]
                try:
                    num = int(numeric_part)
                    if num > max_num:
                        max_num = num
                except ValueError:
                    continue
        new_number = max_num + 1
        new_id = f"{prefix}{new_number:03d}"

        row = {
            "invoice_id": new_id,
            "invoice_number": invoice_number,
            "publisher_id": publisher_id,
            "invoice_date": invoice_date,
            "period_start": period_start,
            "period_end": period_end,
            "subtotal": subtotal,
            "hst_amount": hst_amount,
            "total_due": total_due,
            "pdf_path": pdf_path,
            "sent_at": None,
            "paid_at": None,
            "created_at": _fixed_now_iso(),
        }
        data["invoices"][invoice_id] = row
        payload = {"invoice_id": new_id, "invoice_number": row["invoice_number"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertInvoice",
                "description": "Insert a new invoice row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_number": {"type": "string"},
                        "publisher_id": {"type": "string"},
                        "invoice_date": {"type": "string"},
                        "period_start": {"type": "string"},
                        "period_end": {"type": "string"},
                        "subtotal": {"type": "number"},
                        "hst_amount": {"type": "number"},
                        "total_due": {"type": "number"},
                        "pdf_path": {"type": "string"},
                    },
                    "required": [
                        "invoice_number",
                        "publisher_id",
                        "invoice_date",
                        "period_start",
                        "period_end",
                        "subtotal",
                        "hst_amount",
                        "total_due",
                        "pdf_path",
                    ],
                },
            },
        }
