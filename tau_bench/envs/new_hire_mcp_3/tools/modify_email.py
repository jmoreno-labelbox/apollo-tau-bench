from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ModifyEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict = None, message_id: str = None, email_id: str = None) -> str:
        updates = updates or {}
        emails = data.get("emails", [])
        for e in emails:
            if e.get("message_id") == message_id:
                e.update(updates)
                e["updated_at"] = _fixed_now_iso()
        payload = {"updated_message_id": message_id, "updates": updates}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmail",
                "description": "Update an email record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["message_id", "updates"],
                },
            },
        }
