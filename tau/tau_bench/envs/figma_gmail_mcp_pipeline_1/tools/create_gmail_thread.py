# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateGmailThread(Tool):  # WRITE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        sender_email: str,
        recipients_emails: List[str],
        workflow_type: str,
        current_labels: List[str]
    ) -> str:
        # Validate input
        if not isinstance(sender_email, str) or not sender_email:
            return json.dumps({"error": "sender_email must be a non-empty string"})
        if not isinstance(recipients_emails, list) or not all(isinstance(e, str) for e in recipients_emails):
            return json.dumps({"error": "recipients_emails must be a list of strings"})
        if not isinstance(workflow_type, str) or not workflow_type or workflow_type not in ['review', 'release']:
            return json.dumps({"error": "workflow_type must be a non-empty string"})
        if not isinstance(current_labels, list) or not all(isinstance(l, str) for l in current_labels):
            return json.dumps({"error": "current_labels must be a list of strings"})
        gmail_labels = get_config_options(data, "gmail_labels")
        invalid_labels = [l for l in current_labels if l not in gmail_labels]
        if invalid_labels:
            return json.dumps({"error": f"Invalid labels: {invalid_labels}. Allowed: {gmail_labels}"})
        gmail_threads = data.get("gmail_threads", [])
        next_num = len(gmail_threads) + 1
        thread_id = f"thread_{next_num:03d}"
        created_ts = "2025-08-26T12:00:00Z"  # Use current date/time in production
        if workflow_type == "review":
            subject = f"Review designs for {sender_email}"
        elif workflow_type == "release":
            subject = f"Release designs for {sender_email}"
        new_thread = {
            "thread_id": thread_id,
            "sender_email": sender_email,
            "recipients_emails": recipients_emails,
            "subject": subject,
            "current_labels": current_labels,
            "created_ts": created_ts
        }
        gmail_threads.append(new_thread)
        return json.dumps({"new_thread": new_thread})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_gmail_thread",
                "description": "Create a new Gmail thread.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sender_email": {"type": "string", "description": "Sender's email address."},
                        "recipients_emails": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of recipient email addresses."
                        },
                        "subject": {"type": "string", "description": "Subject of the thread."},
                        "current_labels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Current labels for the thread."
                        }
                    },
                    "required": ["sender_email", "recipients_emails", "subject", "current_labels"]
                }
            }
        }
