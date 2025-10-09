from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class CreateOrientationInvitationEmailsTool(Tool):
    """Generates orientation and manager introduction emails for candidates using templates."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        orientation_details: dict[str, Any] = None, 
        ready_candidate_ids: list[str] = None
    ) -> str:
        pass
        candidates_map = {c.get("candidate_id"): c for c in data.get("candidates", [])}
        emails = data.setdefault("emails", [])
        results = []

        orientation_details = orientation_details or {}

        for candidate_id in ready_candidate_ids or []:
            candidate = candidates_map.get(candidate_id)
            if not candidate:
                continue

            context = candidate.copy()
            context.update(orientation_details)

            #Orientation Message
            rendered_orient = _get_hardcoded_template_and_render(
                "orientation_invitation", context
            )
            orient_email_id = _next_str_id(emails, "message_id", "msg_")
            orient_email = {
                "message_id": orient_email_id,
                "subject": rendered_orient["subject"],
                "body": rendered_orient["body"],
                "from_email": "hr@company.com",
                "to_emails": [candidate.get("candidate_email")],
                "cc_emails": (
                    [candidate.get("manager_email_nullable")]
                    if candidate.get("manager_email_nullable")
                    else []
                ),
                "date_ts": HARD_TS,
                "labels_ids": ["label_4"],
                "attachments_ids": [],
                "draft_flag": False,
                "sent_flag": True,
                "candidate_id_nullable": candidate_id,
                "thread_id_nullable": None,
                "in_reply_to_message_id_nullable": None,
            }
            emails.append(orient_email)

            #Manager Introduction Message
            rendered_intro = _get_hardcoded_template_and_render(
                "manager_introduction", context
            )
            intro_email_id = _next_str_id(emails, "message_id", "msg_")
            intro_email = {
                "message_id": intro_email_id,
                "subject": rendered_intro["subject"],
                "body": rendered_intro["body"],
                "from_email": "hr@company.com",
                "to_emails": [candidate.get("manager_email_nullable")],
                "cc_emails": [candidate.get("candidate_email")],
                "date_ts": HARD_TS,
                "labels_ids": ["label_5"],
                "attachments_ids": [],
                "draft_flag": False,
                "sent_flag": True,
                "candidate_id_nullable": candidate_id,
                "thread_id_nullable": None,
                "in_reply_to_message_id_nullable": None,
            }
            emails.append(intro_email)

            candidate["orientation_invite_ts_nullable"] = HARD_TS
            candidate["manager_intro_invite_ts_nullable"] = HARD_TS

            results.append(
                {
                    "candidate_id": candidate_id,
                    "orientation_email": orient_email,
                    "manager_intro_email": intro_email,
                    "updated_candidate": candidate,
                    "results": {"system_name": "Email", "status": "Success"},
                    "email_type": "orientation invitation",
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
                "name": "CreateOrientationInvitationEmails",
                "description": "Creates orientation and manager introduction emails.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ready_candidate_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "orientation_details": {
                            "type": "object",
                            "description": "e.g., meeting_time, meeting_location",
                        },
                        "orientation_template_name": {
                            "type": "string",
                            "description": "Template name for orientation email",
                        },
                        "manager_intro_template_name": {
                            "type": "string",
                            "description": "Template name for manager introduction email",
                        },
                    },
                    "required": [
                        "ready_candidate_ids",
                        "orientation_template_name",
                        "manager_intro_template_name",
                    ],
                },
            },
        }
