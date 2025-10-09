from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SendEmailTool(Tool):
    """Dispatch an email from a predictable sender to a receiver, recording the event for compliance."""

    @staticmethod
    def invoke(data, sender, receiver, subject, body, timestamp):
        # Confirm sender's existence
        sender_user = next(
            (u for u in data.get("users", []) if u.get("user_id") == sender), None
        )
        if not sender_user:
            payload = {"error": f"Sender '{sender}' not found in users.json."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Confirm receiver's existence
        receiver_user = next(
            (u for u in data.get("users", []) if u.get("user_id") == receiver), None
        )
        if not receiver_user:
            payload = {"error": f"Receiver '{receiver}' not found in users.json."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Receiver should be ACTIVE or PENDING_ACCESS
        if receiver_user.get("status") not in ("ACTIVE", "PENDING_ACCESS"):
            payload = {
                    "error": f"Receiver '{receiver}' has status '{receiver_user.get('status')}', not allowed."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Check subject/body for validity
        if not isinstance(subject, str) or not subject.strip():
            payload = {"error": "Subject must be a non-empty string."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if not isinstance(body, str) or not body.strip():
            payload = {"error": "Body must be a non-empty string."}
            out = json.dumps(payload, indent=2)
            return out

        # Add to emails.json
        emails = data.setdefault("emails", [])
        email_id = f"EM-{len(emails) + 1:03d}"
        record = {
            "email_id": email_id,
            "timestamp": timestamp,
            "sender": sender,
            "receiver": receiver,
            "subject": subject,
            "text_content": body,
        }
        emails.append(record)
        payload = {"success": f"Email {email_id} sent to {receiver}", "email_id": email_id}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
                "description": (
                    "Send an email from sender user_id to receiver user_id with deterministic subject, "
                    "body, and timestamp. Appends a new record to emails.json. "
                    "Sender and receiver must exist in users.json, and receiver must be ACTIVE or PENDING_ACCESS."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sender": {
                            "type": "string",
                            "description": "Sender's user_id (must exist in users.json).",
                        },
                        "receiver": {
                            "type": "string",
                            "description": "Receiver's user_id (must be ACTIVE or PENDING_ACCESS).",
                        },
                        "subject": {
                            "type": "string",
                            "description": "Email subject, policy/compliance driven.",
                        },
                        "body": {
                            "type": "string",
                            "description": "Email body text, deterministic.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "ISO 8601 UTC timestamp, deterministic.",
                        },
                    },
                    "required": ["sender", "receiver", "subject", "body", "timestamp"],
                },
            },
        }
