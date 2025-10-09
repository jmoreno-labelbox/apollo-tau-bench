from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class SendEmail(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sender: str = None,
        receiver: str = None,
        subject: str = None,
        text_content: str = None,
        timestamp: str = None
    ) -> str:
        emails = data.get("emails", [])
        new_id_num = max((int(e["email_id"][3:]) for e in emails), default=0) + 1
        new_email_id = f"EM-{new_id_num:03d}"
        new_email = {
            "email_id": new_email_id,
            "sender": sender,
            "receiver": receiver,
            "subject": subject,
            "text_content": text_content,
            "timestamp": timestamp,
        }
        emails.append(new_email)
        data["emails"] = emails
        payload = new_email
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
                "description": "Sends an email to a specified recipient.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "receiver": {"type": "string"},
                        "sender": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "subject": {"type": "string"},
                        "text_content": {"type": "string"},
                    },
                    "required": [
                        "receiver",
                        "sender",
                        "timestamp",
                        "subject",
                        "text_content",
                    ],
                },
            },
        }
