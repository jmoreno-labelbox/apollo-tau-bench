from tau_bench.envs.tool import Tool
import json
from typing import Any

class InsertEmail(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        message_id: str,
        subject: str = None,
        body: str = None,
        from_email: str = "hr@company.com",
        to_emails: list = None,
        cc_emails: list = None,
        date_ts: int = NOW_TS,
        labels_ids: list = None,
        attachments_ids: list = None,
        draft_flag: bool = False,
        sent_flag: bool = True,
        candidate_id: str = None,
        thread_id_nullable: str = None,
        in_reply_to_message_id_nullable: str = None
    ) -> str:
        if to_emails is None:
            to_emails = []
        if cc_emails is None:
            cc_emails = []
        if labels_ids is None:
            labels_ids = []
        if attachments_ids is None:
            attachments_ids = []

        rows = _ensure_list(data, "emails")
        if _find_by_key(rows, "message_id", message_id) is None:
            payload = {
                "message_id": message_id,
                "subject": subject,
                "body": body,
                "from_email": from_email,
                "to_emails": to_emails,
                "cc_emails": cc_emails,
                "date_ts": date_ts,
                "labels_ids": labels_ids,
                "attachments_ids": attachments_ids,
                "draft_flag": draft_flag,
                "sent_flag": sent_flag,
                "candidate_id_nullable": candidate_id,
                "thread_id_nullable": thread_id_nullable,
                "in_reply_to_message_id_nullable": in_reply_to_message_id_nullable,
            }
            rows.append(payload)
        payload = {"message_id": message_id, "created": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertEmail",
                "description": "Insert an email row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "body": {"type": "string"},
                        "to_emails": {"type": "array", "items": {"type": "string"}},
                        "candidate_id": {"type": "string"},
                        "draft_flag": {"type": "boolean"},
                        "sent_flag": {"type": "boolean"},
                    },
                    "required": [
                        "message_id",
                        "subject",
                        "body",
                        "to_emails",
                        "candidate_id",
                        "draft_flag",
                        "sent_flag",
                    ],
                },
            },
        }
