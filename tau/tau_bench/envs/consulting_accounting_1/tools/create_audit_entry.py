from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateAuditEntry(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, event_type: str = None, notes: str = "") -> str:
        import datetime as _dt

        if not invoice_id or not event_type:
            payload = {"error": "invoice_id and event_type are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        audit = data.setdefault("invoice_audit", [])
        new_id = f"AUTO-AUD-{len(audit)+1:04d}"
        ts = _dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
        record = {
            "audit_id": new_id,
            "invoice_id": invoice_id,
            "event_type": event_type,
            "event_timestamp": ts,
            "notes": notes,
        }
        audit.append(record)
        payload = record
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAuditEntry",
                "description": "Create an audit event for an invoice (reminder, second_notice, escalation, etc).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["invoice_id", "event_type"],
                },
            },
        }
