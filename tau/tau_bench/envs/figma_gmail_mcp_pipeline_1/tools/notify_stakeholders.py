# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class NotifyStakeholders(Tool):  # WRITE
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        plan_id: str,
        stakeholder_emails: List[str],
        audit_id: str,
        status: str,
        owner_email: str
    ) -> str:
        # Validate input
        if not isinstance(plan_id, str) or not plan_id:
            return json.dumps({"error": "plan_id must be a non-empty string"})
        if not isinstance(stakeholder_emails, list) or not all(isinstance(e, str) for e in stakeholder_emails):
            return json.dumps({"error": "stakeholder_emails must be a list of strings"})
        if not isinstance(audit_id, str) or not audit_id:
            return json.dumps({"error": "audit_id must be a non-empty string"})
        if not isinstance(status, str) or not status:
            return json.dumps({"error": "status must be a non-empty string"})
        if not isinstance(owner_email, str) or not owner_email:
            return json.dumps({"error": "owner_email must be a non-empty string"})

        # Get valid Gmail labels for notification workflow
        gmail_labels = get_config_options(data, "gmail_labels")
        notification_labels = ["fix-plan", "audit", "notification"]
        valid_labels = [label for label in notification_labels if label in gmail_labels]
        if not valid_labels:
            # Fallback to available labels
            valid_labels = gmail_labels[:2] if len(gmail_labels) >= 2 else gmail_labels

        # Create Gmail thread first
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
            "created_ts": created_ts
        }
        gmail_threads.append(new_thread)

        # Create Gmail message in the thread
        gmail_messages = data.get("gmail_messages", [])
        next_msg_num = len(gmail_messages) + 1
        message_id = f"msg_{next_msg_num:03d}"
        sent_ts = created_ts

        # Create notification message content
        body_text_stripped = f"Hello, this is a notification regarding fix plan {plan_id} for audit {audit_id}. Current status: {status}. Please review the attached fix plan details."

        new_message = {
            "message_id": message_id,
            "thread_id": thread_id,
            "sender_email": owner_email,
            "body_html": f"<p>{body_text_stripped}</p>",
            "body_text_stripped": body_text_stripped,
            "sent_ts": sent_ts,
            "attachments_asset_ids": []
        }
        gmail_messages.append(new_message)

        return json.dumps({
            "thread_created": new_thread,
            "message_created": new_message,
            "notification_sent": True,
            "stakeholders_notified": len(stakeholder_emails)
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "notify_stakeholders",
                "description": "Notify stakeholders about fix plan status by creating a Gmail thread and message.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The fix plan ID to notify about."
                        },
                        "stakeholder_emails": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of stakeholder email addresses to notify."
                        },
                        "audit_id": {
                            "type": "string",
                            "description": "The audit ID associated with the fix plan."
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the fix plan."
                        },
                        "owner_email": {
                            "type": "string",
                            "description": "The email address of the fix plan owner (sender)."
                        }
                    },
                    "required": ["plan_id", "stakeholder_emails", "audit_id", "status", "owner_email"]
                }
            }
        }
