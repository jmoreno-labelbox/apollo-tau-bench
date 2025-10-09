from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class find_gmail_threads(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], label_contains: str = None, subject_contains: str = None, participant_email: str = None) -> str:
        p = _params(data, {
            "label_contains": label_contains,
            "subject_contains": subject_contains,
            "participant_email": participant_email
        })
        rows = []
        threads = _ensure(data, "gmail_threads", [])
        label_q = p.get("label_contains")
        subj_q = p.get("subject_contains")
        party_q = p.get("participant_email")

        for t in threads:
            ok = True
            if label_q:
                labels = t.get("labels", [])
                ok &= any(label_q.lower() in (lab or "").lower() for lab in labels.values()
            if subj_q:
                ok &= subj_q.lower() in (t.get("subject", "").lower())
            if party_q:
                parts = set(t.get("participants", []))
                ok &= party_q in parts
            if ok:
                rows.append(
                    {
                        "thread_id": t.get("thread_id"),
                        "subject": t.get("subject"),
                        "participants": t.get("participants", []),
                        "current_labels": t.get("labels", []),
                    }
                )
        return _ok({"rows": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindGmailThreads",
                "description": "Search Gmail threads by label, subject, or participant.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "label_contains": {"type": "string"},
                        "subject_contains": {"type": "string"},
                        "participant_email": {"type": "string"},
                    },
                },
            },
        }
