# Copyright Sierra

import re
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _fixed_ts(ts: Optional[str]) -> str:
    return ts or "2025-09-01T00:00:00Z"

class WriteOnboardingFile(Tool):
    """Insert/update onboarding_files entry for candidate_id + file_path."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        file_path = kwargs["file_path"]
        content_text = kwargs.get("content_text", "")
        mime_type = kwargs.get("mime_type", "text/markdown")
        created_ts = _fixed_ts(kwargs.get("created_ts"))
        updated_ts = _fixed_ts(kwargs.get("updated_ts"))

        files = data.setdefault("onboarding_files", [])
        for f in files:
            if f.get("file_path") == file_path and f.get("candidate_id") == cand_id:
                f["content_text"] = content_text
                f["mime_type"] = mime_type
                f["updated_ts"] = updated_ts
                return json.dumps({"file_path": file_path, "status": "updated"}, indent=2)

        files.append({
            "file_path": file_path,
            "content_text": content_text,
            "mime_type": mime_type,
            "created_ts": created_ts,
            "updated_ts": updated_ts,
            "candidate_id": cand_id
        })
        return json.dumps({"file_path": file_path, "status": "created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "write_onboarding_file",
                "description": "Create or update an onboarding file record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "file_path": {"type": "string"},
                        "content_text": {"type": "string"},
                        "mime_type": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"}
                    },
                    "required": ["candidate_id", "file_path"]
                }
            }
        }

class AuditAttachmentsForEmail(Tool):
    """
    Write an attachments audit for a specific email (candidate_id, subject, date_ts) to /onboarding/<Name>/attachments_audit.json.
    If the email or attachments are missing, still writes an empty audit for determinism.
    """
    @staticmethod
    def _safe_name(s: str) -> str:
        return re.sub(r"[^A-Za-z0-9]+", "_", s or "").strip("_") or "unknown"

    @staticmethod
    def _find_email_by_keys(db, candidate_id, subject, date_ts):
        emails = db.get("emails", [])
        return next((e for e in emails if e.get("candidate_id_nullable")==candidate_id and e.get("subject")==subject and e.get("date_ts")==date_ts), None)

    @staticmethod
    def invoke(db: Dict[str, Any], candidate_id, date_ts, subject) -> str:
        cand_id = candidate_id; date_ts = _fixed_ts(date_ts)
        cand_row = next((r for r in db.get("candidates", []) if r.get("candidate_id")==cand_id), None)
        name = cand_row.get("candidate_name") if cand_row else cand_id

        email = AuditAttachmentsForEmail._find_email_by_keys(db, cand_id, subject, date_ts)
        att_rows = db.get("attachments", [])
        items = []
        if email:
            for att_id in email.get("attachments_ids", []):
                a = next((x for x in att_rows if x.get("attachment_id")==att_id), None)
                if a:
                    items.append({"attachment_id": a.get("attachment_id"), "filename": a.get("filename"), "mime_type": a.get("mime_type"), "file_path": a.get("file_path"), "size_bytes": a.get("size_bytes")})

        audit = {"candidate_id": cand_id, "subject": subject, "date_ts": date_ts, "attachments": items, "count": len(items)}
        file_path = f"/onboarding/{AuditAttachmentsForEmail._safe_name(name)}/attachments_audit.json"
        WriteOnboardingFile.invoke(db, candidate_id=cand_id, file_path=file_path, content_text=json.dumps(audit, sort_keys=True, indent=2), mime_type="application/json", updated_ts=_fixed_ts(None))
        return json.dumps({"file_path": file_path, "count": len(items)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"audit_attachments_for_email",
            "description":"Write an attachments audit for (candidate_id, subject, date_ts).",
            "parameters":{"type":"object","properties":{
                "candidate_id":{"type":"string"},
                "subject":{"type":"string"},
                "date_ts":{"type":"string"}
            },"required":["candidate_id","subject","date_ts"]}
        }}