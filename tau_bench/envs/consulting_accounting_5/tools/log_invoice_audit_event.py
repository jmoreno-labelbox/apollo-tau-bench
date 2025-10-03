from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class LogInvoiceAuditEvent(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        event_type: str = None,
        invoice_id: str = None,
        notes: str = ""
    ) -> str:
        """
        Logs an audit event for an invoice.
        """
        new_event = {
            "audit_id": f"AUD_{invoice_id}",
            "invoice_id": invoice_id,
            "event_type": event_type,
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
                        "invoice_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "notes": {"type": "string"}
                    },
                    "required": ["invoice_id", "event_type"],
                },
            },
        }
