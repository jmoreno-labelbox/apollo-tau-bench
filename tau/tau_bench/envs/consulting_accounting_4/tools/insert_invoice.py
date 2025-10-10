# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsertInvoice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoices = data.get("invoices", [])
        
        prefix = "INV"
        max_num = 0
        for inv in invoices:
            inv_id_str = str(inv.get("invoice_id", ""))
            if inv_id_str.startswith(prefix):
                numeric_part = inv_id_str[len(prefix):]
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
            "invoice_number": kwargs.get("invoice_number"),
            "publisher_id": kwargs.get("publisher_id"),
            "invoice_date": kwargs.get("invoice_date"),
            "period_start": kwargs.get("period_start"),
            "period_end": kwargs.get("period_end"),
            "subtotal": kwargs.get("subtotal"),
            "hst_amount": kwargs.get("hst_amount"),
            "total_due": kwargs.get("total_due"),
            "pdf_path": kwargs.get("pdf_path"),
            "sent_at": None,
            "paid_at": None,
            "created_at": _fixed_now_iso()
        }
        invoices.append(row)
        return json.dumps({"invoice_id": new_id, "invoice_number": row["invoice_number"]}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"insert_invoice",
            "description":"Insert a new invoice row.",
            "parameters":{"type":"object","properties":{
                "invoice_number":{"type":"string"},"publisher_id":{"type":"string"},
                "invoice_date":{"type":"string"},"period_start":{"type":"string"},"period_end":{"type":"string"},
                "subtotal":{"type":"number"},"hst_amount":{"type":"number"},"total_due":{"type":"number"},
                "pdf_path":{"type":"string"}
            },"required":["invoice_number","publisher_id","invoice_date","period_start","period_end","subtotal","hst_amount","total_due","pdf_path"]}
        }}
