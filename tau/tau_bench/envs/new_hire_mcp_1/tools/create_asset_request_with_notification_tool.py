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

def _err(msg: str, code: str = "bad_request", ) -> str:
    """Creates a JSON error message."""
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

class CreateAssetRequestWithNotificationTool(Tool):
    """Creates asset requests and corresponding IT notification emails for one or more candidates."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, candidate_ids, asset_type = defaults["asset_type"], specifications = defaults["specifications"], urgency_level = defaults["urgency_level"]) -> str:

        ids_to_process = []
        if candidate_ids:
            ids_to_process.extend(candidate_ids)
        if candidate_id:
            ids_to_process.append(candidate_id)

        if not ids_to_process:
            return _err("candidate_id or candidate_ids is required.")

        candidates_map = {str(c.get("candidate_id")): c for c in data.get("candidates", [])}
        asset_requests = data.setdefault("asset_requests", [])
        emails = data.setdefault("emails", [])
        all_results = []

        for cid in ids_to_process:
            candidate = candidates_map.get(cid)
            if not candidate:
                if len(ids_to_process) == 1:
                    return _err(f"Candidate '{cid}' not found.", code="not_found")
                continue

            role_title = candidate.get("role_title", "")
            urgency = urgency_level
            specs = specifications

            context = {
                "candidate_name": candidate.get("candidate_name", ""),
                "urgency_level": urgency,
                "specifications": specs
            }
            rendered = _get_hardcoded_template_and_render("asset_request_notification", context)

            new_email_id = _next_str_id(emails, "message_id", "msg_")
            new_email = {
                "message_id": new_email_id,
                "subject": rendered["subject"],
                "body": rendered["body"],
                "from_email": "hr@company.com",
                "to_emails": ["it-assets@company.com"],
                "cc_emails": [candidate.get("manager_email_nullable")] if candidate.get("manager_email_nullable") else [],
                "date_ts": HARD_TS, "labels_ids": ["label_1"], "attachments_ids": [],
                "draft_flag": False, "sent_flag": True,
                "candidate_id_nullable": cid,
                "thread_id_nullable": None, "in_reply_to_message_id_nullable": None
            }
            emails.append(new_email)

            new_request = {
                "request_id": _next_str_id(asset_requests, "request_id", "asset_req_"),
                "candidate_id": cid,
                "asset_type": asset_type,
                "status": "Pending",
                "email_message_id_nullable": new_email_id,
                "inventory_checked_flag": False,
                "asset_tag_nullable": None,
                "requested_ts": HARD_TS,
                "updated_ts": HARD_TS
            }
            asset_requests.append(new_request)

            result = {
                "asset_request": new_request,
                "email": new_email,
                "results": {'system_name': 'Email', 'status': 'Success'}
            }
            all_results.append(result)

        return json.dumps(all_results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_asset_request_with_notification",
                "description": "Creates asset requests and corresponding IT notification emails for one or more candidates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "A single target candidate identifier."},
                        "candidate_ids": {"type": "array", "items": {"type": "string"}, "description": "A list of target candidate identifiers."},
                        "asset_type": {"type": "string", "description": "Optional: Defaults based on role."},
                        "urgency_level": {"type": "string", "description": "Optional: Defaults based on role."},
                        "specifications": {"type": "string", "description": "Optional: Defaults based on role."}
                    },
                },
            },
        }