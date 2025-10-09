from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class AuditAttachmentsForEmail(Tool):
    """
    Create an attachments audit for a specific email (candidate_id, subject, date_ts) in /onboarding/<Name>/attachments_audit.json.
    If the email or attachments are absent, still generates an empty audit for consistency.
    """

    @staticmethod
    def _safe_name(s: str) -> str:
        pass
        return re.sub(r"[^A-Za-z0-9]+", "_", s or "").strip("_") or "unknown"

    @staticmethod
    def _find_email_by_keys(db, candidate_id, subject, date_ts):
        pass
        emails = db.get("emails", [])
        return next(
            (
                e
                for e in emails
                if e.get("candidate_id_nullable") == candidate_id
                and e.get("subject") == subject
                and e.get("date_ts") == date_ts
            ),
            None,
        )

    @staticmethod
    def invoke(db: dict[str, Any], candidate_id: str, subject: str, date_ts: Any = None) -> str:
        cand_id = candidate_id
        subject = subject
        date_ts = _fixed_ts(date_ts)
        cand_row = next(
            (r for r in db.get("candidates", []) if r.get("candidate_id") == cand_id),
            None,
        )
        name = cand_row.get("candidate_name") if cand_row else cand_id

        email = AuditAttachmentsForEmail._find_email_by_keys(
            db, cand_id, subject, date_ts
        )
        att_rows = db.get("attachments", [])
        items = []
        if email:
            for att_id in email.get("attachments_ids", []):
                a = next(
                    (x for x in att_rows if x.get("attachment_id") == att_id), None
                )
                if a:
                    items.append(
                        {
                            "attachment_id": a.get("attachment_id"),
                            "filename": a.get("filename"),
                            "mime_type": a.get("mime_type"),
                            "file_path": a.get("file_path"),
                            "size_bytes": a.get("size_bytes"),
                        }
                    )

        audit = {
            "candidate_id": cand_id,
            "subject": subject,
            "date_ts": date_ts,
            "attachments": items,
            "count": len(items),
        }
        file_path = f"/onboarding/{AuditAttachmentsForEmail._safe_name(name)}/attachments_audit.json"
        WriteOnboardingFile.invoke(
            db,
            candidate_id=cand_id,
            file_path=file_path,
            content_text=json.dumps(audit, sort_keys=True, indent=2),
            mime_type="application/json",
            updated_ts=_fixed_ts(None),
        )
        payload = {"file_path": file_path, "count": len(items)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AuditAttachmentsForEmail",
                "description": "Write an attachments audit for (candidate_id, subject, date_ts).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "date_ts": {"type": "string"},
                    },
                    "required": ["candidate_id", "subject", "date_ts"],
                },
            },
        }
