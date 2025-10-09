from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class SendEmailToUser(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, subject: str, body: str) -> str:
        email = {
            "user_id": user_id,
            "subject": subject,
            "body": body,
            "timestamp": "2025-07-04",
        }
        data.setdefault("emails_sent", []).append(email)
        payload = {"success": f"Email sent to user {user_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "sendEmailToUser",
                "description": "Send an email to a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "body": {"type": "string"},
                    },
                    "required": ["user_id", "subject", "body"],
                },
            },
        }
