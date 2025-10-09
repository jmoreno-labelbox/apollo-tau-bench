from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class LogInvoiceEvent(Tool):
    """Add an audit record for an invoice (generated, emailed, etc.)."""
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, invoice_number: str = None, event_type: str = None, notes: str = None) -> str:
        audits = data.get("invoice_audit", {}).values()
        # Generate new audit IDs like AUD001, AUD002 ...
        prefix, max_num = "AUD", 0
        for a in audits:
            s = str(a.get("audit_id", ""))
            if s.startswith(prefix):
                try:
                    max_num = max(max_num, int(s[len(prefix) :]))
                except ValueError:
                    pass
        new_id = f"{prefix}{max_num + 1:03d}"
        row = {
            "audit_id": new_id,
            "invoice_id": invoice_id,
            "invoice_number": invoice_number,
            "event_type": event_type,
            "event_timestamp": _now_iso(),
            "notes": notes,
        }
        data["invoice_audit"][row["invoice_audit_id"]] = row
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogInvoiceEvent",
                "description": "Record an audit event for an invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "invoice_number": {"type": "string"},
                        "event_type": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["event_type"],
                },
            },
        }
