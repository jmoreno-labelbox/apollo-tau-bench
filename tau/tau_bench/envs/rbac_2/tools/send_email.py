from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SendEmail(Tool):
    """A utility for sending an email by generating a record in the database."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        sender: str = None,
        receiver: str = None,
        subject: str = None,
        text_content: str = None,
        timestamp: str = None
    ) -> str:
        try:
            emails = data.get("emails", [])
        except (KeyError, json.JSONDecodeError):
            emails = []
        existing_ids = [
            int(email["email_id"].replace("EM-", ""))
            for email in emails
            if email.get("email_id", "").startswith("EM-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        email_id = f"EM-{next_id_num:03d}"

        new_email = {
            "email_id": email_id,
            "sender": sender,
            "receiver": receiver,
            "subject": subject,
            "text_content": text_content,
            "timestamp": timestamp,
        }

        emails.append(new_email)
        data["emails.json"] = json.dumps(emails, indent=4)
        payload = new_email
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
                "description": "Sends a standard onboarding email by creating a record of it in the database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sender": {
                            "type": "string",
                            "description": "The email address of the sender (e.g., onboarding@taucorp.com).",
                        },
                        "receiver": {
                            "type": "string",
                            "description": "The email address of the recipient.",
                        },
                        "subject": {
                            "type": "string",
                            "description": "The subject line of the email.",
                        },
                        "text_content": {
                            "type": "string",
                            "description": "The plain text body of the email.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The timestamp of when the email is sent, in ISO 8601 format.",
                        },
                    },
                    "required": [
                        "sender",
                        "receiver",
                        "subject",
                        "text_content",
                        "timestamp",
                    ],
                },
            },
        }
