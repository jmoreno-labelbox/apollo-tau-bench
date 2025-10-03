from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any

class SendEmail(Tool):
    """
    Dispatch an email with consistent ID and timestamp.

    kwargs:
      sender: str (mandatory)
      receiver: str (mandatory)
      subject: str (mandatory)
      text_content: str (mandatory)
      timestamp: str ISO (optional; defaults to the current timestamp)
    """

    @staticmethod
    def invoke(data: dict[str, Any], sender: str = "", receiver: str = "", subject: str = "", text_content: str = "", timestamp: str = None) -> str:
        if timestamp is None:
            timestamp = get_current_timestamp()

        if not sender or not receiver or not subject or not text_content:
            payload = {"error": "sender, receiver, subject, and text_content are required"}
            out = json.dumps(payload)
            return out

        # Establish an email record
        email = {
            "email_id": _next_id(data, "emails", "EM"),
            "timestamp": timestamp,
            "sender": sender,
            "receiver": receiver,
            "subject": subject,
            "text_content": text_content,
        }

        data.setdefault("emails", []).append(email)
        payload = {"ok": True, "email": email}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
                "description": "Send an email with deterministic ID and timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sender": {
                            "type": "string",
                            "description": "Sender email address.",
                        },
                        "receiver": {
                            "type": "string",
                            "description": "Receiver email address.",
                        },
                        "subject": {"type": "string", "description": "Email subject."},
                        "text_content": {
                            "type": "string",
                            "description": "Email body text.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "ISO timestamp (optional).",
                        },
                    },
                    "required": ["sender", "receiver", "subject", "text_content"],
                    "additionalProperties": False,
                },
            },
        }
