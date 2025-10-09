from tau_bench.envs.tool import Tool
import json
from typing import Any

class NotifyStakeholders(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        plan_id: str,
        stakeholder_emails: list[str],
        audit_id: str,
        status: str,
        owner_email: str,
    ) -> str:
        pass
        #Check the input for validity
        if not isinstance(plan_id, str) or not plan_id:
            payload = {"error": "plan_id must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if not isinstance(stakeholder_emails, list) or not all(
            isinstance(e, str) for e in stakeholder_emails
        ):
            payload = {"error": "stakeholder_emails must be a list of strings"}
            out = json.dumps(payload)
            return out
        if not isinstance(audit_id, str) or not audit_id:
            payload = {"error": "audit_id must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if not isinstance(status, str) or not status:
            payload = {"error": "status must be a non-empty string"}
            out = json.dumps(payload)
            return out
        if not isinstance(owner_email, str) or not owner_email:
            payload = {"error": "owner_email must be a non-empty string"}
            out = json.dumps(payload)
            return out

        #Retrieve valid Gmail labels for the notification workflow
        gmail_labels = get_config_options(data, "gmail_labels")
        notification_labels = ["fix-plan", "audit", "notification"]
        valid_labels = [label for label in notification_labels if label in gmail_labels]
        if not valid_labels:
            #Revert to available labels
            valid_labels = gmail_labels[:2] if len(gmail_labels) >= 2 else gmail_labels

        #Initiate the Gmail thread first
        gmail_threads = data.get("gmail_threads", [])
        next_thread_num = len(gmail_threads) + 1
        thread_id = f"thread_{next_thread_num:03d}"
        created_ts = "2025-08-29T12:00:00Z"

        subject = f"Fix Plan Notification - {status} - {plan_id}"

        new_thread = {
            "thread_id": thread_id,
            "sender_email": owner_email,
            "recipients_emails": stakeholder_emails,
            "subject": subject,
            "current_labels": valid_labels,
            "created_ts": created_ts,
        }
        gmail_threads.append(new_thread)

        #Compose a Gmail message within the thread
        gmail_messages = data.get("gmail_messages", [])
        next_msg_num = len(gmail_messages) + 1
        message_id = f"msg_{next_msg_num:03d}"
        sent_ts = created_ts

        #Generate the content for the notification message
        body_text_stripped = f"Hello, this is a notification regarding fix plan {plan_id} for audit {audit_id}. Current status: {status}. Please review the attached fix plan details."

        new_message = {
            "message_id": message_id,
            "thread_id": thread_id,
            "sender_email": owner_email,
            "body_html": f"<p>{body_text_stripped}</p>",
            "body_text_stripped": body_text_stripped,
            "sent_ts": sent_ts,
            "attachments_asset_ids": [],
        }
        gmail_messages.append(new_message)
        payload = {
                "thread_created": new_thread,
                "message_created": new_message,
                "notification_sent": True,
                "stakeholders_notified": len(stakeholder_emails),
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NotifyStakeholders",
                "description": "Notify stakeholders about fix plan status by creating a Gmail thread and message.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The fix plan ID to notify about.",
                        },
                        "stakeholder_emails": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of stakeholder email addresses to notify.",
                        },
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID associated with the fix plan.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the fix plan.",
                        },
                        "owner_email": {
                            "type": "string",
                            "description": "The email address of the fix plan owner (sender).",
                        },
                    },
                    "required": [
                        "plan_id",
                        "stakeholder_emails",
                        "audit_id",
                        "status",
                        "owner_email",
                    ],
                },
            },
        }
