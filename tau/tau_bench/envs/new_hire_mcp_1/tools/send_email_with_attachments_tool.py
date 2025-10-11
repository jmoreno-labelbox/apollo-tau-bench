# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendEmailWithAttachmentsTool(Tool):
    """Creates a new email record from a template, with attachments."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, template_name, to_emails, attachment_file_paths = [], cc_emails = [], from_email = "hr@company.com", label_ids = [], template_context = {}) -> str:

        if not candidate_id or not template_name:
            return _err("candidate_id and template_name are required.")

        candidate = next((c for c in data.get("candidates", []) if str(c.get("candidate_id")) == str(candidate_id)), None)
        if not candidate:
            return _err(f"Candidate '{candidate_id}' not found.", code="not_found")

        # Dynamic creation of context for particular templates.
        if template_name == "it_support_request" and "failure_notes" in template_context:
            # Process the dictionary from analyze_system_access_failures.
            if isinstance(template_context['failure_notes'], dict):
                failures = template_context['failure_notes']
                failure_notes_str = "\n".join([f"- {sys}: {', '.join(details.get('failure_notes', []))}" for sys, details in failures.items()])
                template_context['failure_notes'] = failure_notes_str

            # Standard recipient for IT assistance inquiries
            kwargs.setdefault('to_emails', ['it-support@example.com'])

        if template_name == "asset_fulfillment_notification":
            # Verify that asset_name and asset_tag are present in the context.
            if "asset_name" not in template_context or "asset_tag" not in template_context:
                return _err("asset_fulfillment_notification template requires asset_name and asset_tag in template_context.")

        if not to_emails:
            return _err("to_emails is required for this template.")

        context = candidate.copy()
        context.update(template_context)
        rendered_content = _get_hardcoded_template_and_render(template_name, context)

        emails = data.setdefault("emails", [])
        attachments = data.setdefault("attachments", [])
        onboarding_files = data.get("onboarding_files", [])

        new_email = {
            "message_id": _next_str_id(emails, "message_id", "msg_"),
            "subject": rendered_content["subject"],
            "body": rendered_content["body"],
            "from_email": from_email,
            "to_emails": to_emails,
            "cc_emails": cc_emails,
            "date_ts": HARD_TS,
            "labels_ids": label_ids,
            "attachments_ids": [],
            "draft_flag": False, "sent_flag": True,
            "candidate_id_nullable": candidate_id,
            "thread_id_nullable": None, "in_reply_to_message_id_nullable": None
        }

        attachment_paths = attachment_file_paths
        if template_name == "welcome":
            welcome_packet_path = f"/onboarding/{candidate_id}/welcome_packet.md"
            if any(f.get("file_path") == welcome_packet_path for f in onboarding_files):
                attachment_paths.append(welcome_packet_path)

        for file_path in attachment_paths:
            source_file = next((f for f in onboarding_files if f.get("file_path") == file_path), None)
            if source_file:
                new_attachment_id = _next_str_id(attachments, "attachment_id", "attach_")
                new_attachment = {
                    "attachment_id": new_attachment_id,
                    "message_id": new_email["message_id"],
                    "filename": file_path.split('/')[-1],
                    "mime_type": source_file.get("mime_type"),
                    "file_path": file_path,
                    "size_bytes": source_file.get("size_bytes", 1024),
                    "stored_ts": HARD_TS
                }
                attachments.append(new_attachment)
                new_email["attachments_ids"].append(new_attachment_id)

        emails.append(new_email)

        result = {
            "email": new_email,
            "results": {'system_name': 'Email', 'status': 'Success'}
        }
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_email_with_attachments",
                "description": "Creates a new email from a template, with attachments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "template_name": {"type": "string"},
                        "to_emails": {"type": "array", "items": {"type": "string"}, "description": "Required. List of recipient email addresses."},
                        "from_email": {"type": "string", "description": "Optional: Defaults to hr@company.com"},
                        "cc_emails": {"type": "array", "items": {"type": "string"}},
                        "attachment_file_paths": {"type": "array", "items": {"type": "string"}, "description": "Optional: paths to attach. Welcome packet is auto-attached for 'welcome' template."},
                        "label_ids": {"type": "array", "items": {"type": "string"}},
                        "template_context": {"type": "object", "description": "Optional: context for templates. For IT support, failure notes are auto-generated. For asset_fulfillment_notification, requires asset_name and asset_tag."}
                    },
                    "required": ["candidate_id", "template_name", "to_emails"],
                },
            },
        }
