# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




class UpsertEmailTool(Tool):
    """upsert_email
    Create or update an email record deterministically with exclusive fields only.
    - Create when email_id not present; sets timestamp to HARD_TS.
    - Update when email_id exists; modifies only provided fields (no updated_at).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        email_id = kwargs.get("email_id")
        if not email_id:
            return json.dumps({"error": "email_id is required"}, indent=2)

        emails: List[Dict[str, Any]] = data.setdefault("emails", [])
        rec = next((e for e in emails if e.get("email_id") == email_id), None)

        sender = kwargs.get("sender")
        receiver = kwargs.get("receiver")
        subject = kwargs.get("subject")
        text_content = kwargs.get("text_content")

        if rec is None:
            if not receiver or not subject or not text_content:
                return json.dumps(
                    {
                        "error": (
                            "receiver, subject, and text_content are required for creation"
                        )
                    },
                    indent=2,
                )
            rec = {
                "email_id": email_id,
                "timestamp": _HARD_TS,
                "sender": sender or "rbac-bot@taucorp.com",
                "receiver": receiver,
                "subject": subject,
                "text_content": text_content,
            }
            emails.append(rec)
            return json.dumps(rec, indent=2)

        # UPDATE (exclusive fields only)
        if sender is not None:
            rec["sender"] = sender
        if receiver is not None:
            rec["receiver"] = receiver
        if subject is not None:
            rec["subject"] = subject
        if text_content is not None:
            rec["text_content"] = text_content

        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_email",
                "description": (
                    "Create or update an email record deterministically (exclusive fields only)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email_id": {"type": "string"},
                        "sender": {"type": "string"},
                        "receiver": {"type": "string"},
                        "subject": {"type": "string"},
                        "text_content": {"type": "string"},
                    },
                    "required": ["email_id"],
                },
            },
        }

class SendEmailTool(Tool):
    """send_email: convenience wrapper around upsert for creation-only."""

    @staticmethod
    def invoke(data: Dict[str, Any], email_id, receiver, sender, subject, text_content, user_id) -> str:

        if not email_id or not subject or not text_content:
            return json.dumps(
                {"error": "email_id, subject, and text_content are required"},
                indent=2,
            )

        # If a receiver is not specified, attempt to determine it using user_id.
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