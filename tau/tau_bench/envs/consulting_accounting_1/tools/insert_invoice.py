# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsertInvoice(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["invoice_id","publisher_id","subtotal","hst_amount","total_due"]
        for k in required:
            if kwargs.get(k) is None:
                return json.dumps({"error": f"{k} is required"}, indent=2)
        invs = data.setdefault("invoices", [])
        record = {"invoice_id": kwargs["invoice_id"],"invoice_number": kwargs.get("invoice_number"),"publisher_id": kwargs["publisher_id"],"invoice_date": kwargs.get("invoice_date"),"period_start": kwargs.get("period_start"),"period_end": kwargs.get("period_end"),"subtotal": kwargs["subtotal"],"hst_amount": kwargs["hst_amount"],"total_due": kwargs["total_due"],"pdf_path": kwargs.get("pdf_path"),"sent_at": kwargs.get("sent_at"),"paid_at": kwargs.get("paid_at"),"created_at": kwargs.get("created_at")}
        invs.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "insert_invoice","description": "Insert a new invoice header into the dataset.","parameters": {"type": "object","properties": {"invoice_id": {"type": "string"},"publisher_id": {"type": "string"},"subtotal": {"type": "number"},"hst_amount": {"type": "number"},"total_due": {"type": "number"},"invoice_number": {"type": "string"},"invoice_date": {"type": "string"},"period_start": {"type": "string"},"period_end": {"type": "string"},"pdf_path": {"type": "string"},"sent_at": {"type": "string"},"paid_at": {"type": "string"},"created_at": {"type": "string"}},"required": ["invoice_id","publisher_id","subtotal","hst_amount","total_due"]}}}
