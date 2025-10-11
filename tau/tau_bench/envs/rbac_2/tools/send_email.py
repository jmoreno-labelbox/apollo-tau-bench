# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendEmail(Tool):
    """ A tool to send an email by creating a record in the database."""

    @staticmethod
    def invoke(data: Dict[str, Any], receiver, sender, subject, text_content, timestamp) -> str:
        try:
            emails = data.get('emails', [])
        except (KeyError, json.JSONDecodeError):
            emails = []
        existing_ids = [int(email["email_id"].replace("EM-", "")) for email in emails if email.get("email_id", "").startswith("EM-")]
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

        return json.dumps(new_email)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_email",
                "description": "Sends a standard onboarding email by creating a record of it in the database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sender": {
                            "type": "string",
                            "description": "The email address of the sender (e.g., onboarding@taucorp.com)."
                        },
                        "receiver": {
                            "type": "string",
                            "description": "The email address of the recipient."
                        },
                        "subject": {
                            "type": "string",
                            "description": "The subject line of the email."
                        },
                        "text_content": {
                            "type": "string",
                            "description": "The plain text body of the email."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The timestamp of when the email is sent, in ISO 8601 format."
                        },
                    },
                    "required": ["sender", "receiver", "subject", "text_content", "timestamp"]
                }
            }
        }
