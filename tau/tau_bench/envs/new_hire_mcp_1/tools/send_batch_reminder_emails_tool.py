from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SendBatchReminderEmailsTool(Tool):
    """Generates several reminder emails from a template and refreshes the related `checklist_items`."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_ids: list = None, days_overdue_threshold: int = 0) -> str:
        if candidate_ids is None:
            candidate_ids = []
        days_overdue_threshold = _as_int(days_overdue_threshold)
        template_name = "overdue_task_reminder"

        if not candidate_ids:
            return _err("candidate_ids array is required.")
        if days_overdue_threshold is None:
            return _err("days_overdue_threshold must be an integer.")

        emails = data.setdefault("emails", [])
        candidates_map = {c.get("candidate_id"): c for c in data.get("candidates", {}).values()}
        all_checklist_items = data.get("checklist_items", {}).values()

        results = []
        for candidate_id in candidate_ids:
            candidate = candidates_map.get(candidate_id)
            if not candidate:
                continue

            overdue_tasks = []
            for item in all_checklist_items.values():
                if str(item.get("candidate_id")) != str(candidate_id):
                    continue
                due_date = item.get("due_date")
                if not due_date or item.get("status") == "Completed":
                    continue
                days_overdue = _days_between(due_date, HARD_TS)
                if days_overdue >= days_overdue_threshold:
                    overdue_tasks.append(item)

            if not overdue_tasks:
                continue

            context = {
                "name": candidate.get("candidate_name"),
                "tasks": ", ".join([t.get("task_name", "") for t in overdue_tasks]),
            }
            rendered = _get_hardcoded_template_and_render(template_name, context)

            # Generate Email
            new_email_id = _next_str_id(emails, "message_id", "msg_")
            new_email = {
                "message_id": new_email_id,
                "subject": rendered["subject"],
                "body": rendered["body"],
                "from_email": "hr@company.com",
                "to_emails": [candidate.get("candidate_email")],
                "cc_emails": (
                    [candidate.get("manager_email_nullable")]
                    if candidate.get("manager_email_nullable")
                    else []
                ),
                "date_ts": HARD_TS,
                "labels_ids": ["label_2"],
                "attachments_ids": [],
                "draft_flag": False,
                "sent_flag": True,
                "candidate_id_nullable": candidate.get("candidate_id"),
                "thread_id_nullable": None,
                "in_reply_to_message_id_nullable": None,
            }
            emails.append(new_email)

            # Refresh checklist items
            updated_items = []
            for item in overdue_tasks:
                item["reminder_sent_flag"] = True
                item["reminder_email_message_id_nullable"] = new_email_id
                item["updated_ts"] = HARD_TS
                updated_items.append(item)

            results.append(
                {
                    "created_email": new_email,
                    "updated_checklist_items": updated_items,
                    "results": {"system_name": "Email", "status": "Success"},
                }
            )
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendBatchReminderEmails",
                "description": "Sends batch reminder emails for overdue tasks.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of candidate IDs to send reminders to.",
                        },
                        "days_overdue_threshold": {
                            "type": "integer",
                            "description": "Minimum days past due date to trigger a reminder.",
                        },
                    },
                    "required": ["candidate_ids", "days_overdue_threshold"],
                },
            },
        }
