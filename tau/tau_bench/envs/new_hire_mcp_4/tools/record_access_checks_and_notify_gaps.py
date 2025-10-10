# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordAccessChecksAndNotifyGaps(Tool):
    @staticmethod
    def invoke(db, **kw) -> str:
        candidate_id = kw["candidate_id"]
        checks = kw.get("checks") or []
        to_emails = kw.get("to_emails") or ["it-assets@example.com"]
        subject = kw.get("subject") or "Access Gaps"
        date_ts = kw.get("date_ts") or "2000-01-01T00:00:00Z"

        rows = db.setdefault("access_checks", [])
        rows.append({"candidate_id": candidate_id, "checks": checks, "recorded_ts": date_ts})
        emails = db.setdefault("emails", [])
        def _next_id(rows, key, prefix):
            mx = 0
            for r in rows:
                v = (r.get(key) or "")
                if v.startswith(prefix + "_"):
                    try:
                        mx = max(mx, int(v.split("_")[-1]))
                    except Exception:
                        pass
            return f"{prefix}_{mx+1}"

        msg_id = _next_id(emails, "message_id", "msg")
        emails.append({
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
        })

        return json.dumps({"message_id": msg_id, "checks_recorded": len(checks)}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{
            "name":"record_access_checks_and_notify_gaps",
            "parameters":{"type":"object","properties":{
                "candidate_id":{"type":"string"},
                "checks":{"type":"array","items":{"type":"object"}},
                "to_emails":{"type":"array","items":{"type":"string"}},
                "subject":{"type":"string"},
                "date_ts":{"type":"string"}
            },"required":["candidate_id","checks"]}
        }}
