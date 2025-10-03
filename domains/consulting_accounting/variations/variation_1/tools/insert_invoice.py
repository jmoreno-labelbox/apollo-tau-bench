from tau_bench.envs.tool import Tool
import json
from typing import Any

class InsertInvoice(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        invoice_id: str,
        publisher_id: str,
        subtotal: float,
        hst_amount: float,
        total_due: float,
        invoice_number: str = None,
        invoice_date: str = None,
        period_start: str = None,
        period_end: str = None,
        pdf_path: str = None,
        sent_at: str = None,
        paid_at: str = None,
        created_at: str = None
    ) -> str:
        required = ["invoice_id", "publisher_id", "subtotal", "hst_amount", "total_due"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}
        for k in required:
            if params_dict.get(k) is None:
                payload = {"error": f"{k} is required"}
                out = json.dumps(payload, indent=2)
                return out
        invs = data.setdefault("invoices", [])
        record = {
            "invoice_id": invoice_id,
            "invoice_number": invoice_number,
            "publisher_id": publisher_id,
            "invoice_date": invoice_date,
            "period_start": period_start,
            "period_end": period_end,
            "subtotal": subtotal,
            "hst_amount": hst_amount,
            "total_due": total_due,
            "pdf_path": pdf_path,
            "sent_at": sent_at,
            "paid_at": paid_at,
            "created_at": created_at,
        }
        invs.append(record)
        payload = record
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertInvoice",
                "description": "Insert a new invoice header into the dataset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "publisher_id": {"type": "string"},
                        "subtotal": {"type": "number"},
                        "hst_amount": {"type": "number"},
                        "total_due": {"type": "number"},
                        "invoice_number": {"type": "string"},
                        "invoice_date": {"type": "string"},
                        "period_start": {"type": "string"},
                        "period_end": {"type": "string"},
                        "pdf_path": {"type": "string"},
                        "sent_at": {"type": "string"},
                        "paid_at": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "invoice_id",
                        "publisher_id",
                        "subtotal",
                        "hst_amount",
                        "total_due",
                    ],
                },
            },
        }
