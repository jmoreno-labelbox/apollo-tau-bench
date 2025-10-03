from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class LogCollectionAction(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        audit_id: str,
        event_date: str = None,
        event_type: str = None,
        invoice_id: str = None,
        notes: str = "",
        outcome: str = ""
    ) -> str:
        """
        Logs a new collection action into invoice_audit.json.
        """
        new_action = {
            "audit_id": audit_id,
            "invoice_id": invoice_id,
            "event_type": event_type,
            "event_date": event_date,
            "outcome": outcome,
            "notes": notes
        }
        data["invoice_audit"].append(new_action)
        return json.dumps(new_action["audit_id"])
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogCollectionAction",
                "description": "Log a new collection event (reminder, call, escalation) for a given invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "invoice_id": {"type": "string"},
                        "event_type": {"type": "string"},
                        "event_date": {"type": "string"},
                        "outcome": {"type": "string"},
                        "notes": {"type": "string"}
                    },
                    "required": ["audit_id", "invoice_id", "event_type", "event_date"],
                },
            },
        }
