# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOrientationInvitationEmailsTool(Tool):
    """Creates orientation and manager intro emails for candidates from templates."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidates_map = {c.get("candidate_id"): c for c in data.get("candidates", [])}
        emails = data.setdefault("emails", [])
        results = []

        orientation_details = kwargs.get("orientation_details", {})

        for candidate_id in kwargs.get("ready_candidate_ids", []):
            candidate = candidates_map.get(candidate_id)
            if not candidate: continue

            context = candidate.copy()
            context.update(orientation_details)

            # Orientation Email
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

            # Manager Intro Email
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
