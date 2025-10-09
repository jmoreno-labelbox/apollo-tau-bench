from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class NotifyManagerTool(Tool):
    """Dispatches a standardized notification email to the manager of a candidate."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, notification_type: str = None) -> str:
        if not candidate_id or not notification_type:
            return _err("candidate_id and notification_type are required.")

        candidate = next(
            (
                c
                for c in data.get("candidates", [])
                if str(c.get("candidate_id")) == str(candidate_id)
            ),
            None,
        )
        if not candidate:
            return _err(f"Candidate '{candidate_id}' not found.", code="not_found")

        manager_email = candidate.get("manager_email_nullable")
        if not manager_email:
            return _err(f"Manager not found for candidate '{candidate_id}'.")

        template_name = f"manager_{notification_type}_notification"

        context = candidate.copy()
        context["manager_name"] = manager_email.split("@")[0]

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
            "draft_flag": False,
            "sent_flag": True,
            "candidate_id_nullable": candidate_id,
            "thread_id_nullable": _generate_new_thread_id(emails),
            "in_reply_to_message_id_nullable": None,
        }
        emails.append(new_email)
        payload = new_email
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NotifyManager",
                "description": "Sends a standardized notification email to a candidate's manager.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "notification_type": {
                            "type": "string",
                            "description": "e.g., 'access_issue', 'overdue_escalation'",
                        },
                    },
                    "required": ["candidate_id", "notification_type"],
                },
            },
        }
