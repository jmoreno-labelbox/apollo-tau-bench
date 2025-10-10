# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendEmail(Tool):
    """
    Send an email with deterministic ID and timestamp.

    kwargs:
      sender: str (required)
      receiver: str (required)
      subject: str (required)
      text_content: str (required)
      timestamp: str ISO (optional; defaults to current timestamp)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sender = kwargs.get("sender", "")
        receiver = kwargs.get("receiver", "")
        subject = kwargs.get("subject", "")
        text_content = kwargs.get("text_content", "")
        timestamp = kwargs.get("timestamp") or get_current_timestamp()

        if not sender or not receiver or not subject or not text_content:
            return json.dumps({"error": "sender, receiver, subject, and text_content are required"})

        # Create email record
        email = {
            "email_id": _next_id(data, "emails", "EM"),
            "timestamp": timestamp,
            "sender": sender,
            "receiver": receiver,
            "subject": subject,
            "text_content": text_content
        }

        data.setdefault("emails", []).append(email)
        return json.dumps({"ok": True, "email": email})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_email",
                "description": "Send an email with deterministic ID and timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sender": {"type": "string", "description": "Sender email address."},
                        "receiver": {"type": "string", "description": "Receiver email address."},
                        "subject": {"type": "string", "description": "Email subject."},
                        "text_content": {"type": "string", "description": "Email body text."},
                        "timestamp": {"type": "string", "description": "ISO timestamp (optional)."}
                    },
                    "required": ["sender", "receiver", "subject", "text_content"],
                    "additionalProperties": False
                }
            }
        }
