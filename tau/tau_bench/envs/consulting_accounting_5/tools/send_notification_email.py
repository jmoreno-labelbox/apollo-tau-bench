# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendNotificationEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], consultant_id, publisher_id, subject) -> str:
        """
        Simulates sending a general notification email. Does not require an invoice.
        """
        return json.dumps({
            "status": "success",
            "message": "Notification email sent.",
            "recipient_publisher_id": publisher_id,
            "sender_consultant_id": consultant_id,
            "subject": subject
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendNotificationEmail",
                "description": "Sends a general, non-invoice-related email notification.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string", "description": "ID of the publisher contact to send the email to."},
                        "consultant_id": {"type": "string", "description": "ID of the consultant sending the email."},
                        "subject": {"type": "string", "description": "The subject line of the email."},
                        "body_text": {"type": "string", "description": "The body content of the email."}
                    },
                    "required": ["publisher_id", "consultant_id", "subject", "body_text"],
                },
            },
        }
