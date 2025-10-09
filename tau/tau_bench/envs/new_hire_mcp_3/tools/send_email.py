from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class SendEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], email: dict = None, email_id: Any = None,
    updates: Any = None,
    ) -> str:
        new_email = email or {}
        emails = data.get("emails", [])
        emails.append(new_email)
        data["emails"] = emails
        payload = {"sent_email": new_email}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
                "description": "Send a new email and add it to the record.",
                "parameters": {
                    "type": "object",
                    "properties": {"email": {"type": "object"}},
                    "required": ["email"],
                },
            },
        }
