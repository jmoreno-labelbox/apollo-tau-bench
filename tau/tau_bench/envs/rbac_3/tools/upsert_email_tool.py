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
    def invoke(data: Dict[str, Any], email_id, receiver, sender, subject, text_content) -> str:
        if not email_id:
            return json.dumps({"error": "email_id is required"}, indent=2)

        emails: List[Dict[str, Any]] = data.setdefault("emails", [])
        rec = next((e for e in emails if e.get("email_id") == email_id), None)

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

        # MODIFY (exclusive attributes only)
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
