# Sierra copyright reserved.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class QueryInvoices(Tool):
    """Filter invoices by status/publisher/date range."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = data.get("invoices", []) or []
        status = kwargs.get("status")
        pid = kwargs.get("publisher_id")
        start = kwargs.get("date_from")
        end = kwargs.get("date_to")
        out = []
        for r in rows:
            if status == "open" and r.get("paid_at") is not None:
                continue
            if pid and r.get("publisher_id") != pid:
                continue
            if start and r.get("invoice_date", "") < start:
                continue
            if end and r.get("invoice_date", "") > end:
                continue
            out.append(r)
        return json.dumps({"invoices": out}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "query_invoices",
            "description": "Fetch invoices with filters.",
            "parameters": {"type": "object", "properties": {
                "status": {"type": "string"},
                "publisher_id": {"type": "string"},
                "date_from": {"type": "string"},
                "date_to": {"type": "string"}
            }, "required": []}
        }}
