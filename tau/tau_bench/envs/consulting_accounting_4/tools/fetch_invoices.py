# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchInvoices(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], date_from, date_to, publisher_id, status) -> str:
        rows = data.get("invoices", []) or []
        pid = publisher_id
        start = date_from
        end = date_to
        out = []
        for r in rows:
            if status == "open" and r.get("paid_at") is not None:
                continue
            if pid and r.get("publisher_id") != pid:
                continue
            if start and r.get("invoice_date","") < start:
                continue
            if end and r.get("invoice_date","") > end:
                continue
            out.append(r)
        return json.dumps({"invoices": out}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"fetch_invoices",
            "description":"Fetch invoices with optional filters (status/open, publisher, date range).",
            "parameters":{"type":"object","properties":{
                "status":{"type":"string"},
                "publisher_id":{"type":"string"},
                "date_from":{"type":"string"},"date_to":{"type":"string"}
            },"required":[]}
        }}
