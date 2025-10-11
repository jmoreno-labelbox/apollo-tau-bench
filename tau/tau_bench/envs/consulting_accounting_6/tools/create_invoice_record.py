# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateInvoiceRecord(Tool):
    """Insert a new invoice row and return its id and number."""
    @staticmethod
    def invoke(data: Dict[str, Any], hst_amount, invoice_date, invoice_number, pdf_path, period_end, period_start, publisher_id, subtotal, total_due) -> str:
        invoices = data.get("invoices", [])
        # Create invoice IDs in a sequential format such as INV001, INV002, and so on.
        prefix, max_num = "INV", 0
        for inv in invoices:
            s = str(inv.get("invoice_id", ""))
            if s.startswith(prefix):
                try:
                    max_num = max(max_num, int(s[len(prefix):]))
                except ValueError:
                    pass
        new_id = f"{prefix}{max_num + 1:03d}"

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
            "created_at": _now_iso()
        }
        invoices.append(row)
        return json.dumps({"invoice_id": new_id, "invoice_number": row["invoice_number"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "create_invoice_record",
            "description": "Insert a new invoice row.",
            "parameters": {"type": "object", "properties": {
                "invoice_number": {"type": "string"},
                "publisher_id": {"type": "string"},
                "invoice_date": {"type": "string"},
                "period_start": {"type": "string"},
                "period_end": {"type": "string"},
                "subtotal": {"type": "number"},
                "hst_amount": {"type": "number"},
                "total_due": {"type": "number"},
                "pdf_path": {"type": "string"}
            }, "required": ["invoice_number", "publisher_id", "invoice_date",
                            "period_start", "period_end", "subtotal", "hst_amount", "total_due", "pdf_path"]}
        }}
