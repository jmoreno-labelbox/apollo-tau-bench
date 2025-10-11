# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsertInvoice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], created_at, hst_amount, invoice_date, invoice_id, invoice_number, paid_at, pdf_path, period_end, period_start, publisher_id, sent_at, subtotal, total_due) -> str:
        required = ["invoice_id","publisher_id","subtotal","hst_amount","total_due"]
        for k in required:
            if kwargs.get(k) is None:
                return json.dumps({"error": f"{k} is required"}, indent=2)
        invs = data.setdefault("invoices", [])
        record = {"invoice_id": invoice_id,"invoice_number": invoice_number,"publisher_id": publisher_id,"invoice_date": invoice_date,"period_start": period_start,"period_end": period_end,"subtotal": subtotal,"hst_amount": hst_amount,"total_due": total_due,"pdf_path": pdf_path,"sent_at": sent_at,"paid_at": paid_at,"created_at": created_at}
        invs.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "insert_invoice","description": "Insert a new invoice header into the dataset.","parameters": {"type": "object","properties": {"invoice_id": {"type": "string"},"publisher_id": {"type": "string"},"subtotal": {"type": "number"},"hst_amount": {"type": "number"},"total_due": {"type": "number"},"invoice_number": {"type": "string"},"invoice_date": {"type": "string"},"period_start": {"type": "string"},"period_end": {"type": "string"},"pdf_path": {"type": "string"},"sent_at": {"type": "string"},"paid_at": {"type": "string"},"created_at": {"type": "string"}},"required": ["invoice_id","publisher_id","subtotal","hst_amount","total_due"]}}}
