from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class UpdateAssetRequestStatus(Tool):
    @staticmethod
    def _find_email(db, candidate_id: str, subject: str, date_ts: str):
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

        def seq(e):
            pass
            m = re.match(r"^msg_(\d+)$", e.get("message_id", ""))
            return int(m.group(1) or 0) if m else 0

        matches.sort(key=lambda e: (e.get("sent_flag") is True, seq(e)), reverse=True)
        return matches[0]

    @staticmethod
    def invoke(
        db,
        request_id: str = None,
        candidate_id: str = None,
        asset_type: str = None,
        email_message_id: str = None,
        subject: str = None,
        date_ts: str = None,
        status: str = None,
        updated_ts: str = None,
    ) -> str:
        reqs = db.setdefault("asset_requests", [])
        row = None
        if request_id:
            row = next(
                (r for r in reqs if r.get("request_id") == request_id), None
            )
        else:
            row = next(
                (
                    r
                    for r in reqs
                    if r.get("candidate_id") == candidate_id
                    and r.get("asset_type") == asset_type
                ),
                None,
            )
        if not row:
            payload = {"error": "asset request not found"}
            out = json.dumps(payload, indent=2)
            return out
        if not email_message_id:
            if candidate_id and subject:
                em = UpdateAssetRequestStatus._find_email(db, candidate_id, subject, _fixed_ts(date_ts))
                if em:
                    email_id = em.get("message_id")
        else:
            email_id = email_message_id
        row["status"] = status if status is not None else row.get("status")
        if email_id is not None:
            row["email_message_id_nullable"] = email_id
        row["updated_ts"] = _fixed_ts(updated_ts)
        payload = {
            "request_id": row["request_id"],
            "status": row["status"],
            "email_message_id": row.get("email_message_id_nullable"),
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
                "name": "UpdateAssetRequestStatus",
                "description": "Update asset request status and optional email message id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "asset_type": {"type": "string"},
                        "status": {"type": "string"},
                        "email_message_id": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["candidate_id", "asset_type"],
                },
            },
        }
