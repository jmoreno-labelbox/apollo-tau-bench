from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class GenerateAndSendEmail(Tool):
    @staticmethod
    def invoke(
        db,
        to_emails,
        subject,
        body="",
        cc_emails=None,
        candidate_id=None,
        thread_id=None,
        in_reply_to=None,
        label_names=None,
        attach_paths=None,
        date_ts=None,
        task: Any = None,
        attachment_file_paths: Any = None,
        add_names: Any = None,
    ) -> str:
        if not to_emails or not subject:
            payload = {"error": "to_emails and subject are required"}
            out = json.dumps(payload, indent=2)
            return out

        label_names = label_names or []
        attach_paths = attach_paths or []

        try:
            dts = _fixed_ts(date_ts)
        except Exception:
            dts = date_ts or datetime.now(timezone.utc).isoformat()

        emails = db.setdefault("emails", [])
        attachments = db.setdefault("attachments", [])
        labels_tbl = db.setdefault("email_labels", [])
        files_tbl = db.setdefault("onboarding_files", [])

        def _ensure_list(x):
            return x if isinstance(x, list) else ([] if x is None else [x])

        def _next_id(rows, key, prefix):
            mx = 0
            pat = re.compile(rf"^{re.escape(prefix)}_(\d+)$")
            for r in rows:
                v = r.get(key) or ""
                m = pat.match(v)
                if m:
                    mx = max(mx, int(m.group(1)))
            return f"{prefix}_{mx+1}"

        message_id = _next_id(emails, "message_id", "msg")
        email_row = {
            "message_id": message_id,
            "subject": subject or "",
            "body": body or "",
            "from_email": "hr@example.com",
            "to_emails": _ensure_list(to_emails),
            "cc_emails": _ensure_list(cc_emails),
            "date_ts": dts,
            "draft_flag": True,
            "sent_flag": False,
            "labels_ids": [],
            "attachments_ids": [],
            "candidate_id_nullable": candidate_id,
            "thread_id_nullable": thread_id,
            "in_reply_to_message_id_nullable": in_reply_to,
        }
        emails.append(email_row)

        for path in _ensure_list(attach_paths):
            file_row = next((f for f in files_tbl if f.get("file_path") == path), None)
            att_id = _next_id(attachments, "attachment_id", "att")
            attachments.append(
                {
                    "attachment_id": att_id,
                    "message_id": message_id,
                    "filename": (
                        file_row["file_path"].split("/")[-1]
                        if file_row
                        else (path.split("/")[-1] or "attachment")
                    ),
                    "mime_type": (
                        file_row.get("mime_type")
                        if file_row
                        else "application/octet-stream"
                    ),
                    "file_path": (file_row.get("file_path") if file_row else path),
                    "size_bytes": 0,
                    "stored_ts": dts,
                }
            )
            email_row["attachments_ids"].append(att_id)

        label_ids = []
        for name in _ensure_list(label_names):
            if not name:
                continue
            lab = next((l for l in labels_tbl if l.get("name") == name), None)
            if not lab:
                lid = _next_id(labels_tbl, "label_id", "label")
                lab = {"label_id": lid, "name": name}
                labels_tbl.append(lab)
            if lab["label_id"] not in email_row["labels_ids"]:
                email_row["labels_ids"].append(lab["label_id"])
            label_ids.append(lab["label_id"])

        email_row["draft_flag"] = False
        email_row["sent_flag"] = True
        email_row["date_ts"] = dts
        payload = {"message_id": message_id, "status": "sent", "label_ids": label_ids}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GenerateAndSendEmail",
                "description": "Draft, optionally label, and send an email in a single step. No nested tool calls.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "to_emails": {"type": "array", "items": {"type": "string"}},
                        "subject": {"type": "string"},
                        "body": {"type": "string"},
                        "label_names": {"type": "array", "items": {"type": "string"}},
                        "attachment_file_paths": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "cc_emails": {"type": "array", "items": {"type": "string"}},
                        "candidate_id": {"type": "string"},
                        "thread_id": {"type": "string"},
                        "in_reply_to_message_id": {"type": "string"},
                        "date_ts": {"type": "string"},
                    },
                    "required": ["to_emails", "subject"],
                },
            },
        }
