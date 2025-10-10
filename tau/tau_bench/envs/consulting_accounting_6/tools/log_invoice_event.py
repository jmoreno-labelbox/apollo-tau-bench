# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogInvoiceEvent(Tool):
    """Append an audit event for an invoice (generated, emailed…)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        audits = data.get("invoice_audit", [])
        # New audit_id like AUD001, AUD002 ...
        prefix, max_num = "AUD", 0
        for a in audits:
            s = str(a.get("audit_id", ""))
            if s.startswith(prefix):
                try:
                    max_num = max(max_num, int(s[len(prefix):]))
                except ValueError:
                    pass
        new_id = f"{prefix}{max_num + 1:03d}"
        row = {
            "audit_id": new_id,
            "invoice_id": kwargs.get("invoice_id"),
            "invoice_number": kwargs.get("invoice_number"),
            "event_type": kwargs.get("event_type"),
            "event_timestamp": _now_iso(),
            "notes": kwargs.get("notes")
        }
        audits.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "log_invoice_event",
            "description": "Record an audit event for an invoice.",
            "parameters": {"type": "object", "properties": {
                "invoice_id": {"type": "string"},
                "invoice_number": {"type": "string"},
                "event_type": {"type": "string"},
                "notes": {"type": "string"}
            }, "required": ["event_type"]}
        }}
