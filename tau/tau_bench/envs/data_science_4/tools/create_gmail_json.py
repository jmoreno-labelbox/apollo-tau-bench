# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateGmailJson(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Creates a Gmail-style JSON draft (not sending email). Useful for packaging
        evaluation results and deliverables into an email artifact.
        """
        to = kwargs.get("to", [])
        cc = kwargs.get("cc", [])
        bcc = kwargs.get("bcc", [])
        subject = kwargs.get("subject")
        body_text = kwargs.get("body_text", "")
        body_html_nullable = kwargs.get("body_html_nullable")
        attachments_paths = kwargs.get("attachments_paths", [])

        message_id = "GMAIL_MSG_001"
        json_path = f"/gmail/outbox/{message_id}.json"

        msg_entry = {
            "message_id": message_id,
            "to": to if isinstance(to, list) else [to],
            "cc": cc if isinstance(cc, list) else ([cc] if cc else []),
            "bcc": bcc if isinstance(bcc, list) else ([bcc] if bcc else []),
            "subject": subject,
            "body_text": body_text,
            "body_html_path_nullable": body_html_nullable,
            "attachments_paths": attachments_paths,
            "json_path": json_path,
            "status": "draft",
        }

        data.setdefault("gmail_outbox.json", []).append(msg_entry)
        return json.dumps({"message_id": message_id, "json_path": json_path})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateGmailJson",
                "description": "Creates a Gmail-style JSON draft with recipients, subject, body, and attachments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "to": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Recipient emails",
                        },
                        "cc": {"type": "array", "items": {"type": "string"}},
                        "bcc": {"type": "array", "items": {"type": "string"}},
                        "subject": {"type": "string"},
                        "body_text": {"type": "string"},
                        "body_html_nullable": {
                            "type": "string",
                            "description": "Optional path to HTML body",
                        },
                        "attachments_paths": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "File paths to attach",
                        },
                    },
                    "required": ["to"],
                },
            },
        }
