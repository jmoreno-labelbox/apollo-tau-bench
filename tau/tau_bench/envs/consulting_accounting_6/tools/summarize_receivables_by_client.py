# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SummarizeReceivablesByClient(Tool):
    """Summarize Accounts Receivable by client and bucket."""
    @staticmethod
    def invoke(data: Dict[str, Any], invoices) -> str:
        invoices = invoices or []
        summary: Dict[str, Dict[str, float]] = {}
        for inv in invoices:
            pid = inv.get("publisher_id")
            bucket = inv.get("aging_bucket", "0-30")
            amt = float(inv.get("total_due", 0))
            summary.setdefault(pid, {})
            summary[pid][bucket] = summary[pid].get(bucket, 0.0) + amt
        return json.dumps({"summary_by_publisher": summary}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "summarize_receivables_by_client",
            "description": "Summarize receivables by publisher and aging bucket.",
            "parameters": {"type": "object", "properties": {
                "invoices": {"type": "array", "items": {"type": "object"}}
            }, "required": ["invoices"]}
        }}
