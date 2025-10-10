# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendEmailTool(Tool):
    """send_email: convenience wrapper around upsert for creation-only."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        email_id = kwargs.get("email_id")
        receiver = kwargs.get("receiver")
        user_id = kwargs.get("user_id")
        subject = kwargs.get("subject")
        text_content = kwargs.get("text_content")
        sender = kwargs.get("sender")

        if not email_id or not subject or not text_content:
            return json.dumps(
                {"error": "email_id, subject, and text_content are required"},
                indent=2,
            )

        # If receiver not provided, try to resolve from user_id
        if not receiver and user_id:
            users: List[Dict[str, Any]] = list(data.get("users", {}).values())
            user = next((u for u in users if u.get("user_id") == user_id), None)
            if not user or not user.get("email"):
                return json.dumps(
                    {"error": f"Could not resolve email for user_id {user_id}"},
                    indent=2,
                )
            receiver = user.get("email")

        if not receiver:
            return json.dumps(
                {"error": "receiver or user_id must be provided"}, indent=2
            )

        return UpsertEmailTool.invoke(
            data,
            email_id=email_id,
            receiver=receiver,
            subject=subject,
            text_content=text_content,
            sender=sender,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_email",
                "description": (
                    "Send an email record (deterministic timestamp). Provide receiver or user_id to resolve email."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email_id": {"type": "string"},
                        "user_id": {
                            "type": "string",
                            "description": (
                                "If provided, resolves receiver from users[].email"
                            ),
                        },
                        "receiver": {"type": "string"},
                        "subject": {"type": "string"},
                        "text_content": {"type": "string"},
                        "sender": {"type": "string"},
                    },
                    "required": ["email_id", "subject", "text_content"],
                },
            },
        }
