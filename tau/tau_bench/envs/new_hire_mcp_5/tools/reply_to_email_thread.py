from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class ReplyToEmailThread(Tool):
    """
    Respond in the same thread to a previously existing email identified by (candidate_id, subject, date_ts).
    - Subject changes to 'Re: <subject>'
    - Body is sourced from TASK_TEMPLATES[task] (deterministic), optionally populated with {{name}}/{{role}}/{{start_date}}
    - Reuses the original to/cc if not specified
    - Creates a new emails entry with a new msg_N and a deterministic thread_id (utilizes the original's message_id as thread_id)
    """

    @staticmethod
    def _find_email_by_keys(db, candidate_id, subject, date_ts):
        pass
        emails = db.get("emails", [])
        matches = [
            e
            for e in emails
            if e.get("candidate_id_nullable") == candidate_id
            and e.get("subject") == subject
            and e.get("date_ts") == date_ts
        ]
        if not matches:
            return None

        def msg_seq(e):
            pass
            m = re.match(r"^msg_(\d+)$", e.get("message_id", ""))
            return int(m.group(1)) if m else 0

        matches.sort(
            key=lambda e: (e.get("sent_flag") is True, msg_seq(e)), reverse=True
        )
        return matches[0]

    @staticmethod
    def invoke(
        db: dict[str, Any],
        candidate_id: str,
        subject: str,
        date_ts: str = None,
        to_emails: list[str] = None,
        cc_emails: list[str] = None,
        body: str = "",
        task: str = None, thread_id: Any = None) -> str:
        date_ts = _fixed_ts(date_ts)
        base = ReplyToEmailThread._find_email_by_keys(db, candidate_id, subject, date_ts)
        cand_row = next(
            (r for r in db.get("candidates", []) if r.get("candidate_id") == candidate_id),
            None,
        )
        to_emails = to_emails or (base.get("to_emails") if base else [])
        cc_emails = cc_emails or (base.get("cc_emails") if base else [])
        if not body and task in TASK_TEMPLATES:
            body = _fill(TASK_TEMPLATES[task], cand_row)

        emails = db.setdefault("emails", [])
        msg_id = _next_seq(emails, "message_id", "msg")
        thread_id = (
            (base.get("thread_id_nullable") or base.get("message_id")) if base else None
        )

        emails.append(
            {
                "message_id": msg_id,
                "subject": f"Re: {subject}",
                "body": body or "",
                "from_email": "hr@example.com",
                "to_emails": to_emails,
                "cc_emails": cc_emails,
                "date_ts": date_ts,
                "labels_ids": [],
                "attachments_ids": [],
                "draft_flag": False,
                "sent_flag": True,
                "candidate_id_nullable": candidate_id,
                "thread_id_nullable": thread_id,
                "in_reply_to_message_id_nullable": (
                    base.get("message_id") if base else None
                ),
            }
        )
        if base and not base.get("thread_id_nullable"):
            base["thread_id_nullable"] = thread_id
        payload = {
                "message_id": msg_id,
                "thread_id": thread_id,
                "status": "sent",
                "note": "reply appended",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReplyToEmailThread",
                "description": "Reply to an existing email thread identified by (candidate_id, subject, date_ts).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "date_ts": {"type": "string"},
                        "task": {"type": "string"},
                        "to_emails": {"type": "array", "items": {"type": "string"}},
                        "cc_emails": {"type": "array", "items": {"type": "string"}},
                        "body": {"type": "string"},
                    },
                    "required": ["candidate_id", "subject", "date_ts"],
                },
            },
        }
