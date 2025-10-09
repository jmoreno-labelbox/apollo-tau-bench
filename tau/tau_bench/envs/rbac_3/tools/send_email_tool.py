from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SendEmailTool(Tool):
    """send_email: convenient wrapper around upsert for creation purposes only."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        email_id: str = None, 
        receiver: str = None, 
        user_id: str = None, 
        subject: str = None, 
        text_content: str = None, 
        sender: str = None
    ) -> str:
        if not email_id or not subject or not text_content:
            payload = {"error": "email_id, subject, and text_content are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # If the receiver is not specified, attempt to determine it from user_id
        if not receiver and user_id:
            users: list[dict[str, Any]] = data.get("users", {}).values()
            user = next((u for u in users if u.get("user_id") == user_id), None)
            if not user or not user.get("email"):
                payload = {"error": f"Could not resolve email for user_id {user_id}"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            receiver = user.get("email")

        if not receiver:
            payload = {"error": "receiver or user_id must be provided"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        return UpsertEmailTool.invoke(
            data,
            email_id=email_id,
            receiver=receiver,
            subject=subject,
            text_content=text_content,
            sender=sender,
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
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
