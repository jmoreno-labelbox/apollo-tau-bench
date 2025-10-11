# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
def _render_template(template_content: str, context: Dict[str, Any]) -> str:
    """Performs simple string replacement on a template."""
    for key, value in context.items():
        template_content = template_content.replace(f"{{{{{key}}}}}", str(value))
    return template_content

def _next_str_id(rows: List[Dict[str, Any]], key: str, prefix: str) -> str:
    """Generates the next string ID in a sequence (e.g., CAND-001)."""
    if not rows:
        return f"{prefix}1"

    max_id = 0
    for r in rows:
        id_val = r.get(key)
        if id_val and isinstance(id_val, str) and id_val.startswith(prefix):
            try:
                num_part = int(id_val[len(prefix):])
                if num_part > max_id:
                    max_id = num_part
            except ValueError:
                continue

    return f"{prefix}{max_id + 1:03d}"

def _get_hardcoded_template_and_render(template_name: str, context: Dict[str, Any]) -> Dict[str, str]:
    """
    Retrieves a hardcoded template by name and renders it with the given context.
    """
    templates = {
        "welcome": {
            "subject": "Welcome to the Team, {{candidate_name}}!",
            "body": "Dear {{candidate_name}},\n\nWelcome to our team! We're thrilled to have you join us as our new {{role_title}} starting {{start_date}}.\n\nAttached you'll find your personalized welcome packet.\n\nPlease review these documents before your first day. If you have any questions, don't hesitate to reach out.\n\nBest regards,\nHR Team"
        },
        "asset_request_notification": {
            "subject": "Asset Provisioning Request - {{candidate_name}}",
            "body": "A new asset request has been submitted for {{candidate_name}}.\n\nUrgency: {{urgency_level}}\nSpecifications: {{specifications}}\n\nPlease review and process this request."
        },
        "overdue_task_reminder": {
            "subject": "Onboarding Reminder for {{name}}",
            "body": "Hi {{name}},\n\nThis is a friendly reminder to complete the following overdue onboarding tasks:\n\n{{tasks}}\n\nThanks,\nHR Team"
        },
        "orientation_invitation": {
            "subject": "Orientation Invitation for {{candidate_name}}",
            "body": "Hi {{candidate_name}},\n\nPlease join us for your new hire orientation at {{meeting_time}} in {{meeting_location}}.\n\nWe look forward to seeing you there!"
        },
        "manager_introduction": {
            "subject": "Introduction: {{candidate_name}}",
            "body": "Hi {{manager_email_nullable}},\n\nThis is an introduction to your new team member, {{candidate_name}}, who will be starting on {{start_date}}.\n\nBest regards,\nHR Team"
        },
        "it_support_request": {
            "subject": "URGENT: System Access Failure for {{candidate_name}}",
            "body": "Hi IT Support,\n\nPlease investigate and resolve the following system access failures for candidate {{candidate_name}} ({{candidate_email}}):\n\n{{failure_notes}}\n\nThank you,\nHR Onboarding"
        },
        "manager_access_issue_notification": {
            "subject": "Action Required: System Access Issues for {{candidate_name}}",
            "body": "Hi {{manager_name}},\n\nThis is an alert that your new hire, {{candidate_name}}, is experiencing system access issues that may delay their onboarding. Our IT team has been notified.\n\nThanks,\nHR Onboarding"
        },
        "manager_overdue_escalation": {
            "subject": "Escalation: Overdue Onboarding Tasks for {{candidate_name}}",
            "body": "Hi {{manager_name}},\n\nThis is an escalation regarding overdue onboarding tasks for your new hire, {{candidate_name}}. Please follow up with them to ensure their onboarding stays on track.\n\nThanks,\nHR Onboarding"
        }
    }

    template = templates.get(template_name)
    if not template:
        return {"subject": "", "body": ""} # Return empty strings if template not found

    subject = _render_template(template["subject"], context)
    body = _render_template(template["body"], context)

    return {"subject": subject, "body": body}

def _err(msg: str, code: str = "bad_request", **extra) -> str:
    """Creates a JSON error message."""
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

def _days_between(d1_str: str, d2_str: str) -> int:
    """A deterministic way to calculate days between two ISO date strings."""
    try:
        # Assumes ISO format with 'Z' for UTC
        d1 = datetime.fromisoformat(d1_str.replace("Z", "+00:00"))
        d2 = datetime.fromisoformat(d2_str.replace("Z", "+00:00"))
        return abs((d2 - d1).days)
    except (ValueError, TypeError):
        return 9999  # Return a large number for invalid formats

def _as_int(x: Any) -> Optional[int]:
    """Safely converts a value to an integer."""
    try:
        return int(x)
    except (ValueError, TypeError):
        return None

class SendBatchReminderEmailsTool(Tool):
    """Creates multiple reminder emails from a template and updates corresponding `checklist_items`."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_ids = [], days_overdue_threshold = 0) -> str:
        days_overdue_threshold = _as_int(days_overdue_threshold)
        template_name = "overdue_task_reminder"

        if not candidate_ids:
            return _err("candidate_ids array is required.")
        if days_overdue_threshold is None:
            return _err("days_overdue_threshold must be an integer.")

        emails = data.setdefault("emails", [])
        candidates_map = {c.get("candidate_id"): c for c in data.get("candidates", [])}
        all_checklist_items = data.get("checklist_items", [])

        results = []
        for candidate_id in candidate_ids:
            candidate = candidates_map.get(candidate_id)
            if not candidate: continue

            overdue_tasks = []
            for item in all_checklist_items:
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

            context = { "name": candidate.get("candidate_name"), "tasks": ", ".join([t.get("task_name", "") for t in overdue_tasks]) }
            rendered = _get_hardcoded_template_and_render(template_name, context)

            # Generate Email
            new_email_id = _next_str_id(emails, "message_id", "msg_")
            new_email = {
                "message_id": new_email_id,
                "subject": rendered["subject"],
                "body": rendered["body"],
                "from_email": "hr@company.com",
                "to_emails": [candidate.get("candidate_email")],
                "cc_emails": [candidate.get("manager_email_nullable")] if candidate.get("manager_email_nullable") else [],
                "date_ts": HARD_TS, "labels_ids": ["label_2"], "attachments_ids": [],
                "draft_flag": False, "sent_flag": True,
                "candidate_id_nullable": candidate.get("candidate_id"),
                "thread_id_nullable": None, "in_reply_to_message_id_nullable": None
            }
            emails.append(new_email)

            # Revise checklist entries
            updated_items = []
            for item in overdue_tasks:
                item["reminder_sent_flag"] = True
                item["reminder_email_message_id_nullable"] = new_email_id
                item["updated_ts"] = HARD_TS
                updated_items.append(item)

            results.append({"created_email": new_email, "updated_checklist_items": updated_items, "results": {'system_name': 'Email', 'status': 'Success'}})

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {"name": "send_batch_reminder_emails",
            "description": "Sends batch reminder emails for overdue tasks.",
            "parameters": {"type": "object", "properties": {
                "candidate_ids": {"type": "array", "items": {"type": "string"}, "description": "List of candidate IDs to send reminders to."},
                "days_overdue_threshold": {"type": "integer", "description": "Minimum days past due date to trigger a reminder."}
            }, "required": ["candidate_ids", "days_overdue_threshold"]}}}