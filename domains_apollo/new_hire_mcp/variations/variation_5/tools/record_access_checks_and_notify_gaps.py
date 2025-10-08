from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class RecordAccessChecksAndNotifyGaps(Tool):
    """
    Log access checks for a candidate and dispatch an 'Access Gaps' email in a single action.
    Affects: access_checks (append), emails (create+send)
    Returns: {"message_id": "...", "checks_recorded": N}
    """

    @staticmethod
    def invoke(
        db, 
        candidate_id: str, 
        checks: list = None, 
        to_emails: list = None, 
        subject: str = "Access Gaps", 
        date_ts: str = "2000-01-01T00:00:00Z"
    ) -> str:
        checks = checks or []
        to_emails = to_emails or ["it-assets@example.com"]

        rows = db.setdefault("access_checks", [])
        rows.append(
            {"candidate_id": candidate_id, "checks": checks, "recorded_ts": date_ts}
        )
        emails = db.setdefault("emails", [])

        def _next_id(rows, key, prefix):
            mx = 0
            for r in rows:
                v = r.get(key) or ""
                if v.startswith(prefix + "_"):
                    try:
                        mx = max(mx, int(v.split("_")[-1]))
                    except Exception:
                        pass
            return f"{prefix}_{mx+1}"

        msg_id = _next_id(emails, "message_id", "msg")
        emails.append(
            {
                "message_id": msg_id,
                "subject": subject,
                "body": "",
                "from_email": "hr@example.com",
                "to_emails": to_emails,
                "cc_emails": [],
                "date_ts": date_ts,
                "draft_flag": False,
                "sent_flag": True,
                "labels_ids": [],
                "attachments_ids": [],
                "candidate_id_nullable": candidate_id,
                "thread_id_nullable": None,
                "in_reply_to_message_id_nullable": None,
            }
        )
        payload = {"message_id": msg_id, "checks_recorded": len(checks)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "recordAccessChecksAndNotifyGaps",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "checks": {"type": "array", "items": {"type": "object"}},
                        "to_emails": {"type": "array", "items": {"type": "string"}},
                        "subject": {"type": "string"},
                        "date_ts": {"type": "string"},
                    },
                    "required": ["candidate_id", "checks"],
                },
            },
        }
