import json
import re
from datetime import datetime, timezone
from typing import Any

from tau_bench.envs.tool import Tool

TEMPLATE_INDEX = {
    "onboarding": "/onboarding/templates/Welcome-Email-Template.md",
}
TASK_TEMPLATES = {
    "orientation_invite": "Day-1 orientation details will be provided at check-in.",
    "manager_intro": "A manager introduction will follow orientation.",
    "access_gaps": "Access checks require attention. Please review.",
    "checklist_reminder": "Please review your pending onboarding tasks.",
    "allocation_confirmation": "Your asset allocation has been recorded.",
    "acknowledge": "Acknowledged. We are proceeding per policy.",
}
TEMPLATE_WELCOME_PATH = "/onboarding/templates/Welcome-Email-Template.md"


def _next_seq(rows, key, prefix):
    pass
    mx = 0
    pat = re.compile(rf"^{re.escape(prefix)}_(\d+)$")
    for r in rows:
        v = r.get(key) or ""
        m = pat.match(v)
        if m:
            mx = max(mx, int(m.group(1)))
    return f"{prefix}_{mx+1}"


def _fill(text, cand):
    pass
    name = (cand or {}).get("candidate_name", "")
    role = (cand or {}).get("role_title", "")
    start = (cand or {}).get("start_date", "")
    text = re.sub(r"\{\{\s*name\s*}}", name, text, flags=re.I)
    text = re.sub(r"\{\{\s*role\s*}}", role, text, flags=re.I)
    text = re.sub(r"\{\{\s*start[_\s]*date\s*}}", start, text, flags=re.I)
    return text


def _ensure_list(v):
    pass
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def _get_or_create_label_id(db: dict[str, Any], name: str) -> str:
    """Provide label_id for `name`; generate the next sequential id (label_1, label_2, ...) if it does not exist."""
    pass
    labels = db.setdefault("email_labels", [])
    for lab in labels:
        if lab.get("name") == name:
            return lab["label_id"]
    max_n = 0
    for lab in labels:
        lid = lab.get("label_id") or ""
        m = re.match(r"^label_(\d+)$", lid)
        if m:
            n = int(m.group(1))
            if n > max_n:
                max_n = n
    new_id = f"label_{max_n + 1}"
    labels.append({"label_id": new_id, "name": name})
    return new_id


def _fixed_ts(ts: str | None) -> str:
    pass
    return ts or "2025-09-01T00:00:00Z"


class ListCandidateEmails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str) -> str:
        cand_id = candidate_id
        rows = [
            e
            for e in data.get("emails", [])
            if e.get("candidate_id_nullable") == cand_id
        ]
        payload = {"emails": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listCandidateEmails",
                "description": "List emails for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }


class MarkChecklistItemsReminded(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_ids: list[str], reminder_email_message_id: str | None = None, updated_ts: Any = None, candidate_id: str = None, status: str = None, due_date_lte: Any = None, subject: str = None) -> str:
        updated_ts = _fixed_ts(updated_ts)

        updated = 0
        for it in data.get("checklist_items", []):
            if it.get("item_id") in item_ids:
                it["status"] = "Reminder Sent"
                it["reminder_sent_flag"] = True
                it["reminder_email_message_id_nullable"] = reminder_email_message_id
                it["updated_ts"] = updated_ts
                updated += 1
        payload = {"updated": updated, "message_id": reminder_email_message_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MarkChecklistItemsReminded",
                "description": "Mark checklist items as reminded, link the reminder email id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                        "reminder_email_message_id": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["item_ids"],
                },
            },
        }


class GetOrCreateEmailLabel(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str) -> str:
        label_id = _get_or_create_label_id(data, name)
        payload = {"label_id": label_id, "name": name}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrCreateEmailLabel",
                "description": "Get or create label by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class SearchAttachmentsByFilename(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], filename: str) -> str:
        matches = [
            a for a in data.get("attachments", []) if a.get("filename") == filename
        ]
        payload = {"matches": matches}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchAttachmentsByFilename",
                "description": "Search attachments (simulated Drive) by exact filename.",
                "parameters": {
                    "type": "object",
                    "properties": {"filename": {"type": "string"}},
                    "required": ["filename"],
                },
            },
        }


class FindCandidateByEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_email: str, start_date: str) -> str:
        row = {}
        for _row in data.get("candidates", []):
            if _row.get("candidate_email") == candidate_email and _row.get("start_date") == start_date:
                row = _row

        if row:
            payload = {"found": True, "candidate_id": row["candidate_id"], "candidate": row}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"found": False, "candidate_id": None, "candidate": None}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCandidateByEmail",
                "description": "Find candidate by (candidate_email, start_date). Returns full candidate row too.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_email": {"type": "string"},
                        "start_date": {"type": "string"},
                    },
                    "required": ["candidate_email", "start_date"],
                },
            },
        }


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


class AllocateFirstAvailableAsset(Tool):
    @staticmethod
    def invoke(db: dict[str, Any], request_id: str, updated_ts: str = None) -> str:
        rid = request_id
        req = next(
            (r for r in db.get("asset_requests", []) if r.get("request_id") == rid),
            None,
        )
        if not req:
            payload = {"error": f"request_id {rid} not found"}
            out = json.dumps(payload, indent=2)
            return out
        cand_id = req.get("candidate_id")
        a_type = req.get("asset_type")
        inv = db.get("inventory_assets", [])

        def is_free(row):
            st = (row.get("status") or "").lower()
            return (
                (row.get("asset_type") == a_type)
                and (row.get("assigned_candidate_id_nullable") in (None, ""))
                and (st in ("available", "avail", "free"))
            )

        free = sorted(
            [r for r in inv if is_free(r)], key=lambda r: (r.get("asset_tag") or "")
        )
        if not free:
            payload = {
                    "request_id": rid,
                    "candidate_id": cand_id,
                    "asset_type": a_type,
                    "asset_tag": None,
                    "status": "none_available",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        chosen = free[0]
        chosen["assigned_candidate_id_nullable"] = cand_id
        chosen["status"] = "allocated"
        for c in db.get("candidates", []):
            if c.get("candidate_id") == cand_id:
                c["allocated_asset_tag_nullable"] = chosen.get("asset_tag")
                break
        req["updated_ts"] = _fixed_ts(updated_ts)
        payload = {
                "request_id": rid,
                "candidate_id": cand_id,
                "asset_type": a_type,
                "asset_tag": chosen.get("asset_tag"),
                "status": "allocated",
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
                "name": "AllocateFirstAvailableAsset",
                "description": "Allocate the first available inventory asset for an existing request_id, and mirror the tag onto the candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["request_id"],
                },
            },
        }


class WriteOnboardingFile(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        candidate_id: str,
        file_path: str,
        content_text: str = "",
        mime_type: str = "text/markdown",
        created_ts: Any = None,
        updated_ts: Any = None
,
    payload: Any = None,
    ) -> str:
        cand_id = candidate_id
        created_ts = _fixed_ts(created_ts)
        updated_ts = _fixed_ts(updated_ts)

        files = data.setdefault("onboarding_files", [])
        for f in files:
            if f.get("file_path") == file_path and f.get("candidate_id") == cand_id:
                f["content_text"] = content_text
                f["mime_type"] = mime_type
                f["updated_ts"] = updated_ts
                payload = {"file_path": file_path, "status": "updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        files.append(
            {
                "file_path": file_path,
                "content_text": content_text,
                "mime_type": mime_type,
                "created_ts": created_ts,
                "updated_ts": updated_ts,
                "candidate_id": cand_id,
            }
        )
        payload = {"file_path": file_path, "status": "created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteOnboardingFile",
                "description": "Create or update an onboarding file record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "file_path": {"type": "string"},
                        "content_text": {"type": "string"},
                        "mime_type": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["candidate_id", "file_path"],
                },
            },
        }


class UpdateCandidateStatusFields(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str, fields: dict[str, Any] = {}, payload: Any = None) -> str:
        cand_id = candidate_id
        for row in data.get("candidates", []):
            if row.get("candidate_id") == cand_id:
                for k, v in fields.items():
                    if v is None:
                        row[k] = None
                    else:
                        row[k] = v
                payload = {"candidate_id": cand_id, "updated_fields": list(fields.keys())}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": f"candidate_id {cand_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCandidateStatusFields",
                "description": "Update selected candidate fields deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "fields": {"type": "object"},
                    },
                    "required": ["candidate_id", "fields"],
                },
            },
        }


class GetCandidateDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str) -> str:
        cand_id = candidate_id
        for row in data.get("candidates", []):
            if row.get("candidate_id") == cand_id:
                payload = {"candidate": row}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"candidate_id {cand_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCandidateDetails",
                "description": "Get candidate row by candidate_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }


class UpdateCandidateInviteTimestamps(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        candidate_id: str, 
        orientation_invite_ts: str = None, 
        manager_intro_invite_ts: str = None
,
    message_id: Any = None,
    ) -> str:
        fields = {}
        if orientation_invite_ts is not None:
            fields["orientation_invite_ts_nullable"] = _fixed_ts(orientation_invite_ts)
        if manager_intro_invite_ts is not None:
            fields["manager_intro_invite_ts_nullable"] = _fixed_ts(manager_intro_invite_ts)
        return UpdateCandidateStatusFields.invoke(
            data, candidate_id=candidate_id, fields=fields
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCandidateInviteTimestamps",
                "description": "Set candidate invite timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "orientation_invite_ts": {"type": "string"},
                        "manager_intro_invite_ts": {"type": "string"},
                    },
                    "required": ["candidate_id"],
                },
            },
        }


class RecordAccessChecksAndNotifyGaps(Tool):
    @staticmethod
    def invoke(
        db, 
        candidate_id: str, 
        checks: list = None, 
        to_emails: list = None, 
        subject: str = "Access Gaps", 
        date_ts: str = "2000-01-01T00:00:00Z", message_id: Any = None) -> str:
        if checks is None:
            checks = []
        if to_emails is None:
            to_emails = ["it-assets@example.com"]

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


class ReplyToEmailThread(Tool):
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
        task: str = None
,
    thread_id: Any = None,
    ) -> str:
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


class WriteAssetRequestFile(Tool):
    @staticmethod
    def invoke(
        db: dict[str, Any],
        candidate_id: str,
        file_path: str = None,
        payload: dict = None,
        created_ts: str = None,
        updated_ts: str = None
    ) -> str:
        file_path = file_path or f"/onboarding/{candidate_id}/asset_request.json"
        payload = payload or {}
        return WriteOnboardingFile.invoke(
            db,
            candidate_id=candidate_id,
            file_path=file_path,
            content_text=json.dumps(payload, sort_keys=True, indent=2),
            mime_type="application/json",
            created_ts=created_ts,
            updated_ts=updated_ts,
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteAssetRequestFile",
                "description": "Store asset_request.json for the candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "file_path": {"type": "string"},
                        "payload": {"type": "object"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["candidate_id", "payload"],
                },
            },
        }


class ReadAssetRequest(Tool):
    @staticmethod
    def invoke(data, request_id: str) -> str:
        row = next(
            (r for r in data.get("asset_requests", []) if r.get("request_id") == request_id),
            None,
        )
        payload = {"asset_request": row} if row else {"error": f"request_id {request_id} not found"}
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
                "name": "ReadAssetRequest",
                "parameters": {
                    "type": "object",
                    "properties": {"request_id": {"type": "string"}},
                    "required": ["request_id"],
                },
            },
        }


class AssignAssetToCandidate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_tag: str, candidate_id: str) -> str:
        inv = data.get("inventory_assets", [])
        row = next((a for a in inv if a.get("asset_tag") == asset_tag), None)
        if not row:
            payload = {"error": f"asset_tag {asset_tag} not found"}
            out = json.dumps(payload, indent=2)
            return out

        row["assigned_candidate_id_nullable"] = candidate_id
        row["status"] = "allocated"
        for c in data.get("candidates", []):
            if c.get("candidate_id") == candidate_id:
                c["allocated_asset_tag_nullable"] = asset_tag
        payload = {"asset_tag": asset_tag, "assigned_to": candidate_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assignAssetToCandidate",
                "description": "Assign inventory asset to candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_tag": {"type": "string"},
                        "candidate_id": {"type": "string"},
                    },
                    "required": ["asset_tag", "candidate_id"],
                },
            },
        }


class RecordAccessChecks(Tool):
    @staticmethod
    def invoke(data, candidate_id: str, checks: list = None) -> str:
        checks = checks or []
        rows = data.setdefault("access_checks", [])
        ids = []
        for i, chk in enumerate(checks):
            payload = {
                "access_check_id": _next_seq(rows, "access_check_id", "acc"),
                "candidate_id": candidate_id,
                "system_name": chk["system_name"],
                "status": chk["status"],
                "note_nullable": chk.get("note"),
                "checked_ts": _fixed_ts(chk.get("checked_ts")),
            }
            rows.append(payload)
            ids.append(payload["access_check_id"])
        payload = {"inserted": len(ids), "access_check_ids": ids}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordAccessChecks",
                "description": "Bulk insert access checks for candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "checks": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "system_name": {"type": "string"},
                                    "status": {"type": "string"},
                                    "note": {"type": "string"},
                                    "checked_ts": {"type": "string"},
                                },
                                "required": ["system_name", "status"],
                            },
                        },
                    },
                    "required": ["candidate_id", "checks"],
                },
            },
        }


class RenderOnboardingWelcome(Tool):
    @staticmethod
    def _candidate_exists(data: dict[str, Any], cand_id: str) -> bool:
        pass
        return any(r.get("candidate_id") == cand_id for r in data.get("candidates", []))

    @staticmethod
    def _get_template_text(data: dict[str, Any]) -> str:
        pass
        for f in data.get("onboarding_files", []):
            if f.get("file_path") == TEMPLATE_WELCOME_PATH:
                return f.get("content_text", "")
        return ""

    @staticmethod
    def _fill(template: str, name: str, role: str, start_date: str) -> str:
        pass
        repls = {
            r"\{\{\s*name\s*\}\}": name,
            r"\{\{\s*role\s*\}\}": role,
            r"\{\{\s*start[_\s]*date\s*\}\}": start_date,
        }
        out = template
        for pat, val in repls.items():
            out = re.sub(pat, val, out, flags=re.IGNORECASE)
        return out

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str, candidate_name: str = "", role_title: str = "", start_date: str = "") -> str:
        cand_id = candidate_id
        name = candidate_name
        role = role_title
        start_date = start_date

        if not RenderOnboardingWelcome._candidate_exists(data, cand_id):
            payload = {"error": f"candidate_id {cand_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        template_text = RenderOnboardingWelcome._get_template_text(data)
        if not template_text:
            payload = {"error": f"template not found at {TEMPLATE_WELCOME_PATH}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        content = RenderOnboardingWelcome._fill(template_text, name, role, start_date)
        payload = {
                "candidate_id": cand_id,
                "file_path": TEMPLATE_WELCOME_PATH,
                "content_text": content,
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
                "name": "RenderOnboardingWelcome",
                "description": "Return onboarding welcome email content from the stored template with placeholders filled.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "candidate_name": {"type": "string"},
                        "role_title": {"type": "string"},
                        "start_date": {"type": "string"},
                    },
                    "required": [
                        "candidate_id",
                        "candidate_name",
                        "role_title",
                        "start_date",
                    ],
                },
            },
        }


class CreateAssetRequest(Tool):
    """Establish or modify an asset request for a candidate (idempotent based on candidate_id and asset_type)."""

    @staticmethod
    def invoke(
        db: dict[str, Any], 
        candidate_id: str, 
        asset_type: str, 
        requested_ts: Any = None, 
        status: str = "Requested"
    ) -> str:
        ts = _fixed_ts(requested_ts)
        reqs = db.setdefault("asset_requests", [])

        row = next(
            (
                r
                for r in reqs
                if r.get("candidate_id") == candidate_id
                and r.get("asset_type") == asset_type
            ),
            None,
        )
        if row:
            row["status"] = status
            row["updated_ts"] = ts
            payload = {"request_id": row["request_id"], "status": "updated"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        request_id = _next_seq(reqs, "request_id", "req")
        reqs.append(
            {
                "request_id": request_id,
                "candidate_id": candidate_id,
                "asset_type": asset_type,
                "status": status,
                "email_message_id_nullable": None,
                "inventory_checked_flag": False,
                "asset_tag_nullable": None,
                "requested_ts": ts,
                "updated_ts": ts,
            }
        )
        payload = {"request_id": request_id, "status": "created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAssetRequest",
                "description": "Create or update an asset request for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "asset_type": {"type": "string"},
                        "status": {"type": "string"},
                        "requested_ts": {"type": "string"},
                    },
                    "required": ["candidate_id", "asset_type"],
                },
            },
        }


class WritePendingTasksFile(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        candidate_id: str,
        content_markdown: str = "# Pending Tasks\n",
        file_path: str = None,
        created_ts: str = None,
        updated_ts: str = None
,
    due_date_lte: Any = None,
    ) -> str:
        file_path = file_path or f"/onboarding/{candidate_id}/pending_tasks.md"
        return WriteOnboardingFile.invoke(
            data,
            candidate_id=candidate_id,
            file_path=file_path,
            content_text=content_markdown,
            mime_type="text/markdown",
            created_ts=created_ts,
            updated_ts=updated_ts,
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WritePendingTasksFile",
                "description": "Write a markdown summary of pending checklist items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "content_markdown": {"type": "string"},
                        "file_path": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["candidate_id"],
                },
            },
        }


class UpsertCandidateRecord(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        candidate_email: str,
        start_date: str,
        candidate_name: str,
        role_title: str = None,
        manager_email: str = None,
        onboarding_status: str = "Created",
        created_ts: Any = None, due_date_lte: Any = None) -> str:
        pass
        email = candidate_email
        start = start_date
        name = candidate_name
        role = role_title
        manager_email = manager_email
        onboarding_status = onboarding_status
        created_ts = _fixed_ts(created_ts)

        candidates = data.setdefault("candidates", [])
        row = {}
        for _row in data.get("candidates", []):
            if _row.get("candidate_email") == email and _row.get("start_date") == start:
                row = _row
        if row:
            row["candidate_name"] = name
            if role is not None:
                row["role_title"] = role
            if manager_email is not None:
                row["manager_email_nullable"] = manager_email
            row["onboarding_status"] = onboarding_status
            payload = {"candidate_id": row["candidate_id"], "status": "updated"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        candidate_id = _get_or_create_label_id(
            "cand", {"email": email, "start": start, "name": name}
        )
        new_row = {
            "candidate_id": candidate_id,
            "candidate_name": name,
            "role_title": role,
            "start_date": start,
            "candidate_email": email,
            "onboarding_status": onboarding_status,
            "asset_request_record_id_nullable": None,
            "checklist_follow_up_ts_nullable": None,
            "created_ts": created_ts,
            "manager_email_nullable": manager_email,
            "orientation_invite_ts_nullable": None,
            "manager_intro_invite_ts_nullable": None,
            "welcome_email_message_id_nullable": None,
        }
        candidates.append(new_row)
        payload = {"candidate_id": candidate_id, "status": "created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsertCandidateRecord",
                "description": "Create/update candidate keyed by (candidate_email, start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_name": {"type": "string"},
                        "role_title": {"type": "string"},
                        "start_date": {"type": "string"},
                        "candidate_email": {"type": "string"},
                        "manager_email": {"type": "string"},
                        "onboarding_status": {"type": "string"},
                        "created_ts": {"type": "string"},
                    },
                    "required": ["candidate_name", "start_date", "candidate_email"],
                },
            },
        }


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


class ReadOnboardingFile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], file_path: str) -> str:
        for f in data.get("onboarding_files", []):
            if f.get("file_path") == file_path:
                payload = {"file": f}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"file_path {file_path} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReadOnboardingFile",
                "description": "Read an onboarding file by file_path.",
                "parameters": {
                    "type": "object",
                    "properties": {"file_path": {"type": "string"}},
                    "required": ["file_path"],
                },
            },
        }


class SearchChecklistItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str, status: str = None, due_date_lte: str = None) -> str:
        rows = []
        for it in data.get("checklist_items", []):
            if it.get("candidate_id") != candidate_id:
                continue
            if status and it.get("status") != status:
                continue
            if due_date_lte and it.get("due_date") and it["due_date"] > due_date_lte:
                continue
            rows.append(it)
        payload = {"items": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchChecklistItems",
                "description": "Search checklist items for a candidate with simple filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "status": {"type": "string"},
                        "due_date_lte": {"type": "string"},
                    },
                    "required": ["candidate_id"],
                },
            },
        }


class ModifyEmailLabels(Tool):
    @staticmethod
    def _find_email_by_keys(
        db: dict[str, Any], candidate_id: str, subject: str, date_ts: str
    ) -> dict[str, Any] | None:
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
        message_id: str = None,
        candidate_id: str = None,
        subject: str = None,
        date_ts: int = None,
        add_names: list[str] = None,
        remove_names: list[str] = None,
        email_id: Any = None
    ) -> str:
        email = None
        if message_id:
            email = next(
                (e for e in db.get("emails", []) if e.get("message_id") == message_id), None
            )
        else:
            date_ts = _fixed_ts(date_ts)
            if candidate_id and subject:
                email = ModifyEmailLabels._find_email_by_keys(
                    db, candidate_id, subject, date_ts
                )

        if not email:
            payload = {
                "message_id": None,
                "labels_ids": [],
                "note": "email not found for labeling",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        add = add_names or []
        remove = remove_names or []

        labels_ids = set(email.get("labels_ids", []))
        for nm in add:
            labels_ids.add(_get_or_create_label_id(db, nm))
        for nm in remove:
            existing = next(
                (
                    lab.get("label_id")
                    for lab in db.get("email_labels", [])
                    if lab.get("name") == nm
                ),
                None,
            )
            if existing and existing in labels_ids:
                labels_ids.remove(existing)

        email["labels_ids"] = list(labels_ids)
        payload = {"message_id": email["message_id"], "labels_ids": email["labels_ids"]}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ModifyEmailLabels",
                "description": "Add or remove labels on an email by message_id or by (candidate_id, subject, date_ts).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string"},
                        "candidate_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "date_ts": {"type": "string"},
                        "add_names": {"type": "array", "items": {"type": "string"}},
                        "remove_names": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [],
                },
            },
        }


class AuditAttachmentsForEmail(Tool):
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
    def invoke(
        db: dict[str, Any], 
        candidate_id: str, 
        subject: str, 
        date_ts: Any = None
    ) -> str:
        cand_id = candidate_id
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


class CloseCompletedChecklistItems(Tool):
    @staticmethod
    def invoke(db: dict[str, Any], candidate_id: str, due_date_lte: str = None) -> str:
        items = db.get("checklist_items", [])
        updated = 0
        for it in items:
            if it.get("candidate_id") != candidate_id:
                continue
            if it.get("status") != "Completed":
                continue
            if it.get("completed_ts"):
                continue
            if due_date_lte and it.get("due_date") and it["due_date"] > due_date_lte:
                continue
            it["completed_ts"] = _fixed_ts(None)
            updated += 1
        payload = {"updated": updated}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CloseCompletedChecklistItems",
                "description": "Backfill completed_ts for completed checklist items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "due_date_lte": {"type": "string"},
                    },
                    "required": ["candidate_id"],
                },
            },
        }


class SummarizeAccessChecks(Tool):
    @staticmethod
    def _safe_name(s: str) -> str:
        pass
        return re.sub(r"[^A-Za-z0-9]+", "_", s or "").strip("_") or "unknown"

    @staticmethod
    def invoke(db: dict[str, Any], candidate_id: str) -> str:
        cand_id = candidate_id
        cand_row = next(
            (r for r in db.get("candidates", []) if r.get("candidate_id") == cand_id),
            None,
        )
        name = cand_row.get("candidate_name") if cand_row else cand_id
        checks = [
            r for r in db.get("access_checks", []) if r.get("candidate_id") == cand_id
        ]
        by_sys: dict[str, dict[str, int]] = {}
        for r in checks:
            sysn = r.get("system_name") or ""
            st = r.get("status") or ""
            by_sys.setdefault(sysn, {}).setdefault(st, 0)
            by_sys[sysn][st] += 1
        summary = {"candidate_id": cand_id, "counts": by_sys, "total": len(checks)}
        file_path = (
            f"/onboarding/{SummarizeAccessChecks._safe_name(name)}/access_summary.json"
        )
        WriteOnboardingFile.invoke(
            db,
            candidate_id=cand_id,
            file_path=file_path,
            content_text=json.dumps(summary, sort_keys=True, indent=2),
            mime_type="application/json",
            updated_ts=_fixed_ts(None),
        )
        payload = {"file_path": file_path, "total_checks": len(checks)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SummarizeAccessChecks",
                "description": "Aggregate access_checks and write an access_summary.json artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }


class CreateCandidate(Tool):
    """Establish or insert a candidate (predictable candidate_id)."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        candidate_id: str = None,
        name: str = None,
        email: str = None,
        start_date: str = None,
        department: str = None,
        manager_email: str = None,
        status: str = "hired"
    ) -> str:
        c = {
            "candidate_id": candidate_id,
            "name": name,
            "email": email,
            "start_date": start_date,
            "department": department,
            "manager_email": manager_email,
            "status": status,
        }
        if not c["candidate_id"]:
            payload = {"error": "missing_candidate_id"}
            out = json.dumps(payload, indent=2)
            return out
        data.setdefault("candidates", [])
        # insert or update using candidate_id
        for i, existing in enumerate(data["candidates"]):
            if existing.get("candidate_id") == c["candidate_id"]:
                updated = dict(existing)
                updated.update({k: v for k, v in c.items() if v is not None})
                data["candidates"][i] = updated
                payload = updated
                out = json.dumps(payload, indent=2)
                return out
        data["candidates"].append(c)
        payload = c
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createCandidate",
                "description": "Create or upsert a candidate by candidate_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "name": {"type": "string"},
                        "email": {"type": "string"},
                        "start_date": {"type": "string"},
                        "department": {"type": "string"},
                        "manager_email": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["candidate_id"],
                },
            },
        }


class AddChecklistItemForCandidate(Tool):
    """Establish or insert a checklist item for a candidate."""

    @staticmethod
    def invoke(data: dict[str, Any], item_id: str = None, candidate_id: str = None, title: str = None, due_date: str = None, status: str = "pending", completed_on: str = None) -> str:
        item = {
            "item_id": item_id,
            "candidate_id": candidate_id,
            "title": title,
            "due_date": due_date,
            "status": status,
            "completed_on": completed_on,
        }
        if not item["item_id"] or not item["candidate_id"]:
            payload = {"error": "missing_required_fields"}
            out = json.dumps(payload, indent=2)
            return out
        data.setdefault("checklist_items", [])
        #insert or update using item_id
        for i, it in enumerate(data["checklist_items"]):
            if it.get("item_id") == item["item_id"]:
                updated = dict(it)
                updated.update({k: v for k, v in item.items() if v is not None})
                data["checklist_items"][i] = updated
                payload = updated
                out = json.dumps(payload, indent=2)
                return out
        data["checklist_items"].append(item)
        payload = item
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addChecklistItemForCandidate",
                "description": "Create or upsert a checklist item for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"},
                        "candidate_id": {"type": "string"},
                        "title": {"type": "string"},
                        "due_date": {"type": "string"},
                        "status": {"type": "string"},
                        "completed_on": {"type": "string"},
                    },
                    "required": ["item_id", "candidate_id"],
                },
            },
        }


class CreateOnboardingFile(Tool):
    """Establish or insert an onboarding document for a candidate."""

    @staticmethod
    def invoke(data: dict[str, Any], file_id: str, candidate_id: str, doc_type: str, status: str = "pending", uploaded_at: str = None) -> str:
        f = {
            "file_id": file_id,
            "candidate_id": candidate_id,
            "doc_type": doc_type,
            "status": status,
            "uploaded_at": uploaded_at,
        }
        if not f["file_id"] or not f["candidate_id"] or not f["doc_type"]:
            payload = {"error": "missing_required_fields"}
            out = json.dumps(payload, indent=2)
            return out
        data.setdefault("onboarding_files", [])
        for i, existing in enumerate(data["onboarding_files"]):
            if existing.get("file_id") == f["file_id"]:
                updated = dict(existing)
                updated.update({k: v for k, v in f.items() if v is not None})
                data["onboarding_files"][i] = updated
                payload = updated
                out = json.dumps(payload, indent=2)
                return out
        data["onboarding_files"].append(f)
        payload = f
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createOnboardingFile",
                "description": "Create or upsert an onboarding file for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_id": {"type": "string"},
                        "candidate_id": {"type": "string"},
                        "doc_type": {"type": "string"},
                        "status": {"type": "string"},
                        "uploaded_at": {"type": "string"},
                    },
                    "required": ["file_id", "candidate_id", "doc_type"],
                },
            },
        }


TOOLS = [
    ListCandidateEmails(),
    MarkChecklistItemsReminded(),
    GetOrCreateEmailLabel(),
    SearchAttachmentsByFilename(),
    FindCandidateByEmail(),
    GenerateAndSendEmail(),
    AllocateFirstAvailableAsset(),
    WriteOnboardingFile(),
    UpdateCandidateStatusFields(),
    GetCandidateDetails(),
    UpdateCandidateInviteTimestamps(),
    RecordAccessChecksAndNotifyGaps(),
    ReplyToEmailThread(),
    WriteAssetRequestFile(),
    ReadAssetRequest(),
    AssignAssetToCandidate(),
    RecordAccessChecks(),
    RenderOnboardingWelcome(),
    CreateAssetRequest(),
    WritePendingTasksFile(),
    UpsertCandidateRecord(),
    UpdateAssetRequestStatus(),
    ReadOnboardingFile(),
    SearchChecklistItems(),
    ModifyEmailLabels(),
    AuditAttachmentsForEmail(),
    CloseCompletedChecklistItems(),
    SummarizeAccessChecks(),
    CreateCandidate(),
    AddChecklistItemForCandidate(),
    CreateOnboardingFile(),
]
