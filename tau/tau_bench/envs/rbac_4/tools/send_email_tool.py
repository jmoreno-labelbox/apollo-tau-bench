# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendEmailTool(Tool):
    """Send an email from a deterministic sender to a receiver, logging the event for compliance."""

    @staticmethod
    def invoke(data, **kwargs):
        sender = kwargs["sender"]        # user_id of sender
        receiver = kwargs["receiver"]    # user_id of receiver
        subject = kwargs["subject"]
        body = kwargs["body"]
        timestamp = kwargs["timestamp"]

        # Validate sender exists
        sender_user = next((u for u in list(data.get("users", {}).values()) if u.get("user_id") == sender), None)
        if not sender_user:
            return json.dumps({"error": f"Sender '{sender}' not found in users.json."}, indent=2)

        # Validate receiver exists
        receiver_user = next((u for u in list(data.get("users", {}).values()) if u.get("user_id") == receiver), None)
        if not receiver_user:
            return json.dumps({"error": f"Receiver '{receiver}' not found in users.json."}, indent=2)

        # Receiver must be ACTIVE or PENDING_ACCESS
        if receiver_user.get("status") not in ("ACTIVE", "PENDING_ACCESS"):
            return json.dumps(
                {"error": f"Receiver '{receiver}' has status '{receiver_user.get('status')}', not allowed."},
                indent=2
            )

        # Validate subject/body
        if not isinstance(subject, str) or not subject.strip():
            return json.dumps({"error": "Subject must be a non-empty string."}, indent=2)
        if not isinstance(body, str) or not body.strip():
            return json.dumps({"error": "Body must be a non-empty string."}, indent=2)

        # Append to emails.json
        emails = data.setdefault("emails", [])
        email_id = f"EM-{len(emails) + 1:03d}"
        record = {
            "email_id": email_id,
            "timestamp": timestamp,
            "sender": sender,
            "receiver": receiver,
            "subject": subject,
            "text_content": body
        }
        emails.append(record)

        return json.dumps(
            {
                "success": f"Email {email_id} sent to {receiver}",
                "email_id": email_id
            },
            indent=2
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "send_email",
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
                            "description": "Sender's user_id (must exist in users.json)."
                        },
                        "receiver": {
                            "type": "string",
                            "description": "Receiver's user_id (must be ACTIVE or PENDING_ACCESS)."
                        },
                        "subject": {
                            "type": "string",
                            "description": "Email subject, policy/compliance driven."
                        },
                        "body": {
                            "type": "string",
                            "description": "Email body text, deterministic."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "ISO 8601 UTC timestamp, deterministic."
                        }
                    },
                    "required": ["sender", "receiver", "subject", "body", "timestamp"]
                }
            }
        }
