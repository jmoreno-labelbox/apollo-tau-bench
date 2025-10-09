from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateGmailThread(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sender_email: str,
        recipients_emails: list[str],
        workflow_type: str,
        current_labels: list[str],
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(sender_email, str) or not sender_email:
            payload = {"error": "sender_email must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if not isinstance(recipients_emails, list) or not all(
            isinstance(e, str) for e in recipients_emails
        ):
            payload = {"error": "recipients_emails must be a list of strings"}
            out = json.dumps(payload)
            return out
        if (
            not isinstance(workflow_type, str)
            or not workflow_type
            or workflow_type not in ["review", "release"]
        ):
            payload = {"error": "workflow_type must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if not isinstance(current_labels, list) or not all(
            isinstance(l, str) for l in current_labels
        ):
            payload = {"error": "current_labels must be a list of strings"}
            out = json.dumps(payload)
            return out
        gmail_labels = get_config_options(data, "gmail_labels")
        invalid_labels = [l for l in current_labels if l not in gmail_labels]
        if invalid_labels:
            payload = {"error": f"Invalid labels: {invalid_labels}. Allowed: {gmail_labels}"}
            out = json.dumps(
                payload)
            return out
        gmail_threads = data.get("gmail_threads", [])
        next_num = len(gmail_threads) + 1
        thread_id = f"thread_{next_num:03d}"
        created_ts = "2025-08-26T12:00:00Z"  #Utilize the current date/time in production
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
            "created_ts": created_ts,
        }
        gmail_threads.append(new_thread)
        payload = {"new_thread": new_thread}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateGmailThread",
                "description": "Create a new Gmail thread.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sender_email": {
                            "type": "string",
                            "description": "Sender's email address.",
                        },
                        "recipients_emails": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of recipient email addresses.",
                        },
                        "subject": {
                            "type": "string",
                            "description": "Subject of the thread.",
                        },
                        "current_labels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Current labels for the thread.",
                        },
                    },
                    "required": [
                        "sender_email",
                        "recipients_emails",
                        "subject",
                        "current_labels",
                    ],
                },
            },
        }
