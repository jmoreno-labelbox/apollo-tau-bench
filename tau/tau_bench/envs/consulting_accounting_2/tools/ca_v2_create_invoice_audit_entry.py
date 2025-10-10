# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2CreateInvoiceAuditEntry(Tool):
    """Create an audit trail entry for invoice actions."""

    @staticmethod
    def invoke(data: Dict[str, Any], audit_id, event_timestamp, event_type, invoice_id, notes = "") -> str:

        if not all([audit_id, invoice_id, event_type, event_timestamp]):
            return _error("audit_id, invoice_id, event_type, and event_timestamp are required.")

        audit_entry = {
            "audit_id": audit_id,
            "invoice_id": invoice_id,
            "event_type": event_type,
            "event_timestamp": event_timestamp,
            "notes": notes
        }

        data.setdefault("invoice_audit", []).append(audit_entry)

        return _ok(audit_id=audit_id, event_type=event_type)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_invoice_audit_entry",
                "description": "Create an audit trail entry for invoice actions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "invoice_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "event_timestamp": {"type": "string"},
                        "notes": {"type": "string"}
                    },
                    "required": ["audit_id", "invoice_id", "event_type", "event_timestamp"],
                },
            },
        }
