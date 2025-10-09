from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class UpsertEmailTool(Tool):
    """upsert_email
    Create or update an email record in a deterministic manner with only exclusive fields.
    - Create when email_id is absent; sets timestamp to HARD_TS.
    - Update when email_id is present; alters only specified fields (no updated_at).
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        email_id: str = None,
        sender: str = None,
        receiver: str = None,
        subject: str = None,
        text_content: str = None
    ) -> str:
        if not email_id:
            payload = {"error": "email_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        emails: list[dict[str, Any]] = data.setdefault("emails", [])
        rec = next((e for e in emails if e.get("email_id") == email_id), None)

        if rec is None:
            if not receiver or not subject or not text_content:
                payload = {
                    "error": (
                        "receiver, subject, and text_content are required for creation"
                    )
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            rec = {
                "email_id": email_id,
                "timestamp": _HARD_TS,
                "sender": sender or "rbac-bot@sigmatech.com",
                "receiver": receiver,
                "subject": subject,
                "text_content": text_content,
            }
            emails.append(rec)
            payload = rec
            out = json.dumps(payload, indent=2)
            return out

        # UPDATE (only exclusive fields)
        if sender is not None:
            rec["sender"] = sender
        if receiver is not None:
            rec["receiver"] = receiver
        if subject is not None:
            rec["subject"] = subject
        if text_content is not None:
            rec["text_content"] = text_content
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsertEmail",
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
