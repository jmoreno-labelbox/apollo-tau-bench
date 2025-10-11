# All rights reserved by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






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

class CreateOrientationInvitationEmailsTool(Tool):
    """Creates orientation and manager intro emails for candidates from templates."""

    @staticmethod
    def invoke(data: Dict[str, Any], orientation_details = {}, ready_candidate_ids = []) -> str:
        candidates_map = {c.get("candidate_id"): c for c in data.get("candidates", [])}
        emails = data.setdefault("emails", [])
        results = []

        for candidate_id in ready_candidate_ids:
            candidate = candidates_map.get(candidate_id)
            if not candidate: continue

            context = candidate.copy()
            context.update(orientation_details)

            # Welcome Email
            rendered_orient = _get_hardcoded_template_and_render("orientation_invitation", context)
            orient_email_id = _next_str_id(emails, "message_id", "msg_")
            orient_email = {
                "message_id": orient_email_id,
                "subject": rendered_orient["subject"],
                "body": rendered_orient["body"],
                "from_email": "hr@company.com", "to_emails": [candidate.get("candidate_email")],
                "cc_emails": [candidate.get("manager_email_nullable")] if candidate.get("manager_email_nullable") else [],
                "date_ts": HARD_TS, "labels_ids": ["label_4"], "attachments_ids": [],
                "draft_flag": False, "sent_flag": True, "candidate_id_nullable": candidate_id,
                "thread_id_nullable": None, "in_reply_to_message_id_nullable": None
            }
            emails.append(orient_email)

            # Email to introduce the manager
            rendered_intro = _get_hardcoded_template_and_render("manager_introduction", context)
            intro_email_id = _next_str_id(emails, "message_id", "msg_")
            intro_email = {
                "message_id": intro_email_id,
                "subject": rendered_intro["subject"],
                "body": rendered_intro["body"],
                "from_email": "hr@company.com", "to_emails": [candidate.get("manager_email_nullable")],
                "cc_emails": [candidate.get("candidate_email")],
                "date_ts": HARD_TS, "labels_ids": ["label_5"], "attachments_ids": [],
                "draft_flag": False, "sent_flag": True, "candidate_id_nullable": candidate_id,
                "thread_id_nullable": None, "in_reply_to_message_id_nullable": None
            }
            emails.append(intro_email)

            candidate["orientation_invite_ts_nullable"] = HARD_TS
            candidate["manager_intro_invite_ts_nullable"] = HARD_TS

            results.append({"candidate_id": candidate_id, "orientation_email": orient_email, "manager_intro_email": intro_email, "updated_candidate": candidate, "results": {'system_name': 'Email', 'status': 'Success'}, "email_type": "orientation invitation"})

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {"name": "create_orientation_invitation_emails",
            "description": "Creates orientation and manager introduction emails.",
            "parameters": {"type": "object", "properties": {
                "ready_candidate_ids": {"type": "array", "items": {"type": "string"}},
                "orientation_details": {"type": "object", "description": "e.g., meeting_time, meeting_location"},
                "orientation_template_name": {"type": "string", "description": "Template name for orientation email"},
                "manager_intro_template_name": {"type": "string", "description": "Template name for manager introduction email"}
            }, "required": ["ready_candidate_ids", "orientation_template_name", "manager_intro_template_name"]}}}