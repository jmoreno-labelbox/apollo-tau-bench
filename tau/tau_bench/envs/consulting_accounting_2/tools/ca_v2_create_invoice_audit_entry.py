from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2CreateInvoiceAuditEntry(Tool):
    """Generate an audit log entry for invoice activities."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str = None,
        event_timestamp: str = None,
        event_type: str = None,
        invoice_id: str = None,
        notes: str = ""
    ) -> str:
        if not all([audit_id, invoice_id, event_type, event_timestamp]):
            return _error(
                "audit_id, invoice_id, event_type, and event_timestamp are required."
            )

        audit_entry = {
            "audit_id": audit_id,
            "invoice_id": invoice_id,
            "event_type": event_type,
            "event_timestamp": event_timestamp,
            "notes": notes,
        }

        data.setdefault("invoice_audit", []).append(audit_entry)

        return _ok(audit_id=audit_id, event_type=event_type)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateInvoiceAuditEntry",
                "description": "Create an audit trail entry for invoice actions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "invoice_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "event_timestamp": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": [
                        "audit_id",
                        "invoice_id",
                        "event_type",
                        "event_timestamp",
                    ],
                },
            },
        }
