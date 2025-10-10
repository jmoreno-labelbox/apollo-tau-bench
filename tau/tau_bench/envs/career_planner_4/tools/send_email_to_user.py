# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class send_email_to_user(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, subject: str, body: str) -> str:
        email = {
            "user_id": user_id,
            "subject": subject,
            "body": body,
            "timestamp": "2025-07-04",
        }
        data.setdefault("emails_sent", []).append(email)
        return json.dumps({"success": f"Email sent to user {user_id}"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "send_email_to_user",
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
