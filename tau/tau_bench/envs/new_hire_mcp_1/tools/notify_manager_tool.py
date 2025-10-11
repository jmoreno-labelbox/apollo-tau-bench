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

def _generate_new_thread_id(emails: List[Dict[str, Any]]) -> str:
    """Generates a new sequential thread ID."""
    max_id = 0
    for email in emails:
        thread_id = email.get("thread_id_nullable")
        if thread_id and thread_id.startswith("thread_"):
            try:
                num_part = int(thread_id.split('_')[1])
                if num_part > max_id:
                    max_id = num_part
            except (ValueError, IndexError):
                continue
    return f"thread_{max_id + 1}"

def _err(msg: str, code: str = "bad_request", ) -> str:
    """Creates a JSON error message."""
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

class NotifyManagerTool(Tool):
    """Sends a standardized notification email to a candidate's manager."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, notification_type) -> str:

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