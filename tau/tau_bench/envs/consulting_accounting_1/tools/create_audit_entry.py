# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAuditEntry(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        import datetime as _dt
        inv_id = kwargs.get("invoice_id")
        event_type = kwargs.get("event_type")
        notes = kwargs.get("notes", "")
        if not inv_id or not event_type:
            return json.dumps({"error": "invoice_id and event_type are required"}, indent=2)
        audit = data.setdefault("invoice_audit", [])
        new_id = f"AUTO-AUD-{len(audit)+1:04d}"
        ts = _dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
        record = {"audit_id": new_id,"invoice_id": inv_id,"event_type": event_type,"event_timestamp": ts,"notes": notes}
        audit.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "create_audit_entry","description": "Create an audit event for an invoice (reminder, second_notice, escalation, etc).","parameters": {"type": "object","properties": {"invoice_id": {"type": "string"},"event_type": {"type": "string"},"notes": {"type": "string"}},"required": ["invoice_id","event_type"]}}}
