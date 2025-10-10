# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeInvoiceAging(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        import datetime as _dt
        invoice_id = kwargs.get("invoice_id")
        today_str = kwargs.get("today")
        if not invoice_id or not today_str:
            return json.dumps({"error": "invoice_id and today are required"}, indent=2)
        invoices = list(data.get("invoices", {}).values())
        inv = next((i for i in invoices if i.get("invoice_id") == invoice_id), None)
        if not inv:
            return json.dumps({"error": f"Invoice {invoice_id} not found"}, indent=2)
        if inv.get("paid_at"):
            return json.dumps({"invoice_id": invoice_id,"status": "paid","days_overdue": 0,"bucket": "current"}, indent=2)
        inv_date = _dt.datetime.fromisoformat(inv["invoice_date"])
        today = _dt.datetime.fromisoformat(today_str)
        days = (today - inv_date).days
        bucket = "0-30" if days <= 30 else "31-60" if days <= 60 else "61-90" if days <= 90 else "90+"
        return json.dumps({"invoice_id": invoice_id,"status": "unpaid","days_overdue": days,"bucket": bucket}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "compute_invoice_aging","description": "Compute days overdue and aging bucket for a given invoice.","parameters": {"type": "object","properties": {"invoice_id": {"type": "string"},"today": {"type": "string","description": "YYYY-MM-DD reference date"}},"required": ["invoice_id","today"]}}}
