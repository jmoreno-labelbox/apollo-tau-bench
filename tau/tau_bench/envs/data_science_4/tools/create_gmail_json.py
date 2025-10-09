from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateGmailJson(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        to: list[str] = None,
        cc: list[str] = None,
        bcc: list[str] = None,
        subject: str = None,
        body_text: str = "",
        body: str = None,
        body_html_nullable: str = None,
        attachments_paths: list[str] = None
    ) -> str:
        # Accept either body or body_text
        if body is not None:
            body_text = body
        """Generates a Gmail-like JSON draft (without sending email). Helpful for compiling evaluation results and deliverables into an email artifact."""
        to = to if to is not None else []
        cc = cc if cc is not None else []
        bcc = bcc if bcc is not None else []
        attachments_paths = attachments_paths if attachments_paths is not None else []

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
        payload = {"message_id": message_id, "json_path": json_path}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createGmailJson",
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
