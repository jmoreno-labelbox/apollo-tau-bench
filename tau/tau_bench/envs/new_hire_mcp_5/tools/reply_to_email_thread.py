# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReplyToEmailThread(Tool):
    """
    Reply in the same thread to an existing email identified by (candidate_id, subject, date_ts).
    - Subject becomes 'Re: <subject>'
    - Body comes from TASK_TEMPLATES[task] (deterministic), optionally filled with {{name}}/{{role}}/{{start_date}}
    - Reuses original to/cc if not provided
    - Writes a new emails row with a new msg_N and a deterministic thread_id (uses the original's message_id as thread_id)
    """
    @staticmethod
    def _find_email_by_keys(db, candidate_id, subject, date_ts):
        emails = db.get("emails", [])
        matches = [e for e in emails
                   if e.get("candidate_id_nullable") == candidate_id
                   and e.get("subject") == subject
                   and e.get("date_ts") == date_ts]
        if not matches:
            return None
        def msg_seq(e):
            m = re.match(r"^msg_(\d+)$", e.get("message_id",""))
            return int(m.group(1)) if m else 0
        matches.sort(key=lambda e: (e.get("sent_flag") is True, msg_seq(e)), reverse=True)
        return matches[0]

    @staticmethod
    def invoke(db: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]; subject = kwargs["subject"]; date_ts = _fixed_ts(kwargs.get("date_ts"))
        base = ReplyToEmailThread._find_email_by_keys(db, cand_id, subject, date_ts)
        cand_row = next((r for r in db.get("candidates", []) if r.get("candidate_id") == cand_id), None)
        to_emails = kwargs.get("to_emails") or (base.get("to_emails") if base else [])
        cc_emails = kwargs.get("cc_emails") or (base.get("cc_emails") if base else [])
        body = kwargs.get("body", "")
        task = kwargs.get("task")
        if not body and task in TASK_TEMPLATES:
            body = _fill(TASK_TEMPLATES[task], cand_row)

        emails = db.setdefault("emails", [])
        msg_id = _next_seq(emails, "message_id", "msg")
        thread_id = (base.get("thread_id_nullable") or base.get("message_id")) if base else None

        emails.append({
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
            "candidate_id_nullable": cand_id,
            "thread_id_nullable": thread_id,
            "in_reply_to_message_id_nullable": base.get("message_id") if base else None
        })
        if base and not base.get("thread_id_nullable"):
            base["thread_id_nullable"] = thread_id

        return json.dumps({"message_id": msg_id, "thread_id": thread_id, "status": "sent", "note": "reply appended"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"reply_to_email_thread",
            "description":"Reply to an existing email thread identified by (candidate_id, subject, date_ts).",
            "parameters":{"type":"object","properties":{
                "candidate_id":{"type":"string"},
                "subject":{"type":"string"},
                "date_ts":{"type":"string"},
                "task":{"type":"string"},
                "to_emails":{"type":"array","items":{"type":"string"}},
                "cc_emails":{"type":"array","items":{"type":"string"}},
                "body":{"type":"string"}
            },"required":["candidate_id","subject","date_ts"]}
        }}
