# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogCollectionAction(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Logs a new collection action into invoice_audit.json.
        """
        new_action = {
            "audit_id": kwargs["audit_id"],
            "invoice_id": kwargs["invoice_id"],
            "event_type": kwargs["event_type"],   # for example, "reminder_delivered", "telephone_contact"
            "event_date": kwargs["event_date"],
            "outcome": kwargs.get("outcome", ""),
            "notes": kwargs.get("notes", "")
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
