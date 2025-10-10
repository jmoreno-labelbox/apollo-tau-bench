# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogInvoiceAuditEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], event_type, invoice_id, notes = "") -> str:
        """
        Logs an audit event for an invoice.
        """
        new_event = {
            "audit_id": f"AUD_{invoice_id}",
            "invoice_id": invoice_id,
            "event_type": event_type  , # for example, "notification_dispatched", "escalation"
            "notes": notes
        }
        data["invoice_audit"].append(new_event)
        return json.dumps(new_event["audit_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogInvoiceAuditEvent",
                "description": "Log an audit event (reminder, escalation, etc.) for a given invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "invoice_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "event_date": {"type": "string"},
                        "notes": {"type": "string"}
                    },
                    "required": ["audit_id", "invoice_id", "event_type"],
                },
            },
        }
