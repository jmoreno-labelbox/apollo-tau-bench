# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeriveDaysOutstanding(Tool):
    """Compute days outstanding for each invoice given an as-of date."""
    @staticmethod
    def invoke(data: Dict[str, Any], invoices, today) -> str:
        today = today or "2025-08-20"
        invs = invoices or []
        out = []
        for r in invs:
            due = r.get("period_end") or r.get("invoice_date")
            due_iso = (due[:10] if isinstance(due, str) and len(due) > 10 else due)
            ds = (datetime.fromisoformat(today) - datetime.fromisoformat(due_iso)).days
            out.append({"invoice_number": r.get("invoice_number"), "days_outstanding": ds})
        return json.dumps({"aging": out}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "derive_days_outstanding",
            "description": "Compute days outstanding as of a given date.",
            "parameters": {"type": "object", "properties": {
                "invoices": {"type": "array", "items": {"type": "object"}},
                "today": {"type": "string"}
            }, "required": ["invoices"]}
        }}
