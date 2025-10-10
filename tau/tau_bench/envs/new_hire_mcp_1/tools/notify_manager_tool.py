# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class NotifyManagerTool(Tool):
    """Sends a standardized notification email to a candidate's manager."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        notification_type = kwargs.get("notification_type")

        if not candidate_id or not notification_type:
            return _err("candidate_id and notification_type are required.")

        candidate = next((c for c in data.get("candidates", []) if str(c.get("candidate_id")) == str(candidate_id)), None)
        if not candidate:
            return _err(f"Candidate '{candidate_id}' not found.", code="not_found")

        manager_email = candidate.get("manager_email_nullable")
        if not manager_email:
            return _err(f"Manager not found for candidate '{candidate_id}'.")

        template_name = f"manager_{notification_type}_notification"

        context = candidate.copy()
        context["manager_name"] = manager_email.split('@')[0]

        rendered = _get_hardcoded_template_and_render(template_name, context)

        emails = data.setdefault("emails", [])
        new_email = {
            "message_id": _next_str_id(emails, "message_id", "msg_"),
            "subject": rendered["subject"],
            "body": rendered["body"],
            "from_email": "hr@company.com",
            "to_emails": [manager_email],
            "cc_emails": [],
            "date_ts": HARD_TS,
            "labels_ids": [],
            "attachments_ids": [],
            "draft_flag": False, "sent_flag": True,
            "candidate_id_nullable": candidate_id,
            "thread_id_nullable": _generate_new_thread_id(emails),
            "in_reply_to_message_id_nullable": None
        }
        emails.append(new_email)

        return json.dumps(new_email, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "notify_manager",
                "description": "Sends a standardized notification email to a candidate's manager.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "notification_type": {"type": "string", "description": "e.g., 'access_issue', 'overdue_escalation'"}
                    },
                    "required": ["candidate_id", "notification_type"],
                },
            },
        }
