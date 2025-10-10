from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
import json, re
from domains.dto import Tool

TEMPLATE_INDEX = {
    "onboarding": "/onboarding/templates/Welcome-Email-Template.md",
}
TASK_TEMPLATES = {
    "orientation_invite": "Day-1 orientation details will be provided at check-in.",
    "manager_intro":      "A manager introduction will follow orientation.",
    "access_gaps":        "Access checks require attention. Please review.",
    "checklist_reminder": "Please review your pending onboarding tasks.",
    "allocation_confirmation": "Your asset allocation has been recorded.",
    "acknowledge": "Acknowledged. We are proceeding per policy."
}
TEMPLATE_WELCOME_PATH = "/onboarding/templates/Welcome-Email-Template.md"

def _fixed_ts(ts: Optional[str]) -> str:
    return ts or "2025-09-01T00:00:00Z"

def _get_or_create_label_id(db: Dict[str, Any], name: str) -> str:
    """Return label_id for `name`; create next sequential id (label_1, label_2, ...) if missing."""
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
            if n > max_n: max_n = n
    new_id = f"label_{max_n + 1}"
    labels.append({"label_id": new_id, "name": name})
    return new_id

def _ensure_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]

def _fill(text, cand):
    name  = (cand or {}).get("candidate_name", "")
    role  = (cand or {}).get("role_title", "")
    start = (cand or {}).get("start_date", "")
    text = re.sub(r"\{\{\s*name\s*}}", name,  text, flags=re.I)
    text = re.sub(r"\{\{\s*role\s*}}", role,  text, flags=re.I)
    text = re.sub(r"\{\{\s*start[_\s]*date\s*}}", start, text, flags=re.I)
    return text

def _next_seq(rows, key, prefix):
    mx = 0
    pat = re.compile(rf"^{re.escape(prefix)}_(\d+)$")
    for r in rows:
        v = (r.get(key) or "")
        m = pat.match(v)
        if m:
            mx = max(mx, int(m.group(1)))
    return f"{prefix}_{mx+1}"


class FindCandidateByEmail(Tool):
    """
    Look up a candidate by (candidate_email, start_date).
    Returns: {"found": bool, "candidate_id": str|None, "candidate": dict|None}
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        email = kwargs["candidate_email"]
        start = kwargs["start_date"]
        row = {}
        for _row in data.get("candidates", []):
            if _row.get("candidate_email") == email and _row.get("start_date") == start:
                row = _row

        if row:
            return json.dumps({
                "found": True,
                "candidate_id": row["candidate_id"],
                "candidate": row
            }, indent=2)
        return json.dumps({"found": False, "candidate_id": None, "candidate": None}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_candidate_by_email",
                "description": "Find candidate by (candidate_email, start_date). Returns full candidate row too.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_email": {"type": "string"},
                        "start_date": {"type": "string"}
                    },
                    "required": ["candidate_email", "start_date"]
                }
            }
        }


class ReadAssetRequest(Tool):
    @staticmethod
    def invoke(data, **kwargs) -> str:
        rid = kwargs["request_id"]
        row = next((r for r in data.get("asset_requests", []) if r.get("request_id") == rid), None)
        return json.dumps({"asset_request": row} if row else {"error": f"request_id {rid} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{
            "name":"read_asset_request",
            "parameters":{"type":"object","properties":{"request_id":{"type":"string"}}, "required":["request_id"]}
        }}


class UpsertCandidateRecord(Tool):
    """
    Idempotent create/update of candidate row keyed by (candidate_email, start_date).
    Deterministic candidate_id based on inputs.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        email = kwargs["candidate_email"]
        start = kwargs["start_date"]
        name = kwargs["candidate_name"]
        role = kwargs.get("role_title")
        manager_email = kwargs.get("manager_email")
        onboarding_status = kwargs.get("onboarding_status", "Created")
        created_ts = _fixed_ts(kwargs.get("created_ts"))

        candidates = data.setdefault("candidates", [])
        row = {}
        for _row in data.get("candidates", []):
            if _row.get("candidate_email") == email and _row.get("start_date") == start:
                row = _row
        if row:
            row["candidate_name"] = name
            if role is not None: row["role_title"] = role
            if manager_email is not None: row["manager_email_nullable"] = manager_email
            row["onboarding_status"] = onboarding_status
            return json.dumps({"candidate_id": row["candidate_id"], "status": "updated"}, indent=2)

        candidate_id = _get_or_create_label_id("cand", {"email": email, "start": start, "name": name})
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
            "welcome_email_message_id_nullable": None
        }
        candidates.append(new_row)
        return json.dumps({"candidate_id": candidate_id, "status": "created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_candidate_record",
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
                        "created_ts": {"type": "string"}
                    },
                    "required": ["candidate_name", "start_date", "candidate_email"]
                }
            }
        }


class GetCandidateDetails(Tool):
    """Return the full candidate row by candidate_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        for row in data.get("candidates", []):
            if row.get("candidate_id") == cand_id:
                return json.dumps({"candidate": row}, indent=2)
        return json.dumps({"error": f"candidate_id {cand_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_candidate_details",
                "description": "Get candidate row by candidate_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"}
                    },
                    "required": ["candidate_id"]
                }
            }
        }


class UpdateCandidateStatusFields(Tool):
    """Patch allowed candidate fields (status, invite timestamps, welcome msg id, asset tag link, follow-up ts, etc.)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        fields: Dict[str, Any] = kwargs.get("fields", {})
        for row in data.get("candidates", []):
            if row.get("candidate_id") == cand_id:
                for k, v in fields.items():
                    if v is None:
                        row[k] = None
                    else:
                        row[k] = v
                return json.dumps({"candidate_id": cand_id, "updated_fields": list(fields.keys())}, indent=2)
        return json.dumps({"error": f"candidate_id {cand_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_candidate_status_fields",
                "description": "Update selected candidate fields deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "fields": {"type": "object"}
                    },
                    "required": ["candidate_id", "fields"]
                }
            }
        }


class SearchAttachmentsByFilename(Tool):
    """Pretend gdrive search: return any attachments with matching filename, else empty list."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        filename = kwargs["filename"]
        matches = [a for a in data.get("attachments", []) if a.get("filename") == filename]
        return json.dumps({"matches": matches}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_attachments_by_filename",
                "description": "Search attachments (simulated Drive) by exact filename.",
                "parameters": {
                    "type": "object",
                    "properties": {"filename": {"type": "string"}},
                    "required": ["filename"]
                }
            }
        }


class ReadOnboardingFile(Tool):
    """Read a file from onboarding_files by file_path."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        file_path = kwargs["file_path"]
        for f in data.get("onboarding_files", []):
            if f.get("file_path") == file_path:
                return json.dumps({"file": f}, indent=2)
        return json.dumps({"error": f"file_path {file_path} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "read_onboarding_file",
                "description": "Read an onboarding file by file_path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {"type": "string"}
                    },
                    "required": ["file_path"]
                }
            }
        }


class RenderOnboardingWelcome(Tool):
    """
    Render onboarding welcome email content by:
      - confirming candidate_id exists (candidates.json)
      - reading template from /onboarding/templates/Welcome-Email-Template.md (onboarding_files)
      - replacing {{name}}, {{role}}, {{start_date}} (case-insensitive)
    Returns: {candidate_id, file_path, content_text}
    """

    @staticmethod
    def _candidate_exists(data: Dict[str, Any], cand_id: str) -> bool:
        return any(r.get("candidate_id") == cand_id for r in data.get("candidates", []))

    @staticmethod
    def _get_template_text(data: Dict[str, Any]) -> str:
        for f in data.get("onboarding_files", []):
            if f.get("file_path") == TEMPLATE_WELCOME_PATH:
                return f.get("content_text", "")
        return ""

    @staticmethod
    def _fill(template: str, name: str, role: str, start_date: str) -> str:
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        name = kwargs.get("candidate_name", "")
        role = kwargs.get("role_title", "")
        start_date = kwargs.get("start_date", "")

        if not RenderOnboardingWelcome._candidate_exists(data, cand_id):
            return json.dumps({"error": f"candidate_id {cand_id} not found"}, indent=2)

        template_text = RenderOnboardingWelcome._get_template_text(data)
        if not template_text:
            return json.dumps({"error": f"template not found at {TEMPLATE_WELCOME_PATH}"}, indent=2)

        content = RenderOnboardingWelcome._fill(template_text, name, role, start_date)
        return json.dumps({
            "candidate_id": cand_id,
            "file_path": TEMPLATE_WELCOME_PATH,
            "content_text": content
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "render_onboarding_welcome",
                "description": "Return onboarding welcome email content from the stored template with placeholders filled.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "candidate_name": {"type": "string"},
                        "role_title": {"type": "string"},
                        "start_date": {"type": "string"}
                    },
                    "required": ["candidate_id", "candidate_name", "role_title", "start_date"]
                }
            }
        }


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


class GenerateAndSendEmail(Tool):
    """
    Draft + (optionally) label + send an email in one call.
    - Does not call other tools.
    - Touches: emails, attachments, email_labels, onboarding_files
    Returns: {"message_id","status":"sent","label_ids":[...]}
    """
    @staticmethod
    def invoke(db, **kw) -> str:
        to_emails = kw.get("to_emails")
        subject   = kw.get("subject")
        if not to_emails or not subject:
            return json.dumps({"error": "to_emails and subject are required"}, indent=2)

        body      = kw.get("body", "")
        cc_emails = kw.get("cc_emails")
        candidate_id = kw.get("candidate_id")
        thread_id    = kw.get("thread_id")
        in_reply_to  = kw.get("in_reply_to_message_id")
        label_names  = kw.get("label_names") or []
        attach_paths = kw.get("attachment_file_paths") or []
        date_ts_in   = kw.get("date_ts")

        try:
            dts = _fixed_ts(date_ts_in)
        except Exception:
            dts = date_ts_in or datetime.now(timezone.utc).isoformat()

        emails      = db.setdefault("emails", [])
        attachments = db.setdefault("attachments", [])
        labels_tbl  = db.setdefault("email_labels", [])
        files_tbl   = db.setdefault("onboarding_files", [])

        def _ensure_list(x):
            return x if isinstance(x, list) else ([] if x is None else [x])

        def _next_id(rows, key, prefix):
            mx = 0
            pat = re.compile(rf"^{re.escape(prefix)}_(\d+)$")
            for r in rows:
                v = (r.get(key) or "")
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
            file_row = next((f for f in files_tbl if f.get("file_path")==path), None)
            att_id = _next_id(attachments, "attachment_id", "att")
            attachments.append({
                "attachment_id": att_id,
                "message_id": message_id,
                "filename": (file_row["file_path"].split("/")[-1] if file_row else (path.split("/")[-1] or "attachment")),
                "mime_type": (file_row.get("mime_type") if file_row else "application/octet-stream"),
                "file_path": (file_row.get("file_path") if file_row else path),
                "size_bytes": 0,
                "stored_ts": dts
            })
            email_row["attachments_ids"].append(att_id)

        label_ids = []
        for name in _ensure_list(label_names):
            if not name:
                continue
            lab = next((l for l in labels_tbl if l.get("name")==name), None)
            if not lab:
                lid = _next_id(labels_tbl, "label_id", "label")
                lab = {"label_id": lid, "name": name}
                labels_tbl.append(lab)
            if lab["label_id"] not in email_row["labels_ids"]:
                email_row["labels_ids"].append(lab["label_id"])
            label_ids.append(lab["label_id"])

        email_row["draft_flag"] = False
        email_row["sent_flag"]  = True
        email_row["date_ts"]    = dts

        return json.dumps({"message_id": message_id, "status": "sent", "label_ids": label_ids}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "generate_and_send_email",
                "description": "Draft, optionally label, and send an email in a single step. No nested tool calls.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "to_emails": {"type": "array", "items": {"type": "string"}},
                        "subject": {"type": "string"},
                        "body": {"type": "string"},
                        "label_names": {"type": "array", "items": {"type": "string"}},
                        "attachment_file_paths": {"type": "array", "items": {"type": "string"}},
                        "cc_emails": {"type": "array", "items": {"type": "string"}},
                        "candidate_id": {"type": "string"},
                        "thread_id": {"type": "string"},
                        "in_reply_to_message_id": {"type": "string"},
                        "date_ts": {"type": "string"}
                    },
                    "required": ["to_emails", "subject"]
                }
            }
        }


class GetOrCreateEmailLabel(Tool):
    """Return label_id for name, creating deterministically if missing."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs["name"]
        label_id = _get_or_create_label_id(data, name)
        return json.dumps({"label_id": label_id, "name": name}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_or_create_email_label",
                "description": "Get or create label by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"]
                }
            }
        }


class ModifyEmailLabels(Tool):
    """
    Add/remove labels on an email.
    Accepts EITHER:
      - message_id
      - OR (candidate_id + subject + date_ts) to resolve the email deterministically.
    """

    @staticmethod
    def _find_email_by_keys(db: Dict[str, Any], candidate_id: str, subject: str, date_ts: str) -> Optional[Dict[str, Any]]:
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
        email = None
        msg_id = kwargs.get("message_id")
        if msg_id:
            email = next((e for e in db.get("emails", []) if e.get("message_id") == msg_id), None)
        else:
            cand_id = kwargs.get("candidate_id"); subject = kwargs.get("subject"); date_ts = _fixed_ts(kwargs.get("date_ts"))
            if cand_id and subject:
                email = ModifyEmailLabels._find_email_by_keys(db, cand_id, subject, date_ts)

        if not email:
            return json.dumps({"message_id": None, "labels_ids": [], "note": "email not found for labeling"}, indent=2)

        add = kwargs.get("add_names") or []
        remove = kwargs.get("remove_names") or []

        labels_ids = set(email.get("labels_ids", []))
        for nm in add:
            labels_ids.add(_get_or_create_label_id(db, nm))
        for nm in remove:
            existing = next((lab.get("label_id") for lab in db.get("email_labels", []) if lab.get("name") == nm), None)
            if existing and existing in labels_ids:
                labels_ids.remove(existing)

        email["labels_ids"] = list(labels_ids)
        return json.dumps({"message_id": email["message_id"], "labels_ids": email["labels_ids"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_email_labels",
                "description": "Add or remove labels on an email by message_id or by (candidate_id, subject, date_ts).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string"},
                        "candidate_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "date_ts": {"type": "string"},
                        "add_names": {"type": "array", "items": {"type": "string"}},
                        "remove_names": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": []
                }
            }
        }


class ListCandidateEmails(Tool):
    """List emails linked to a candidate_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        rows = [e for e in data.get("emails", []) if e.get("candidate_id_nullable") == cand_id]
        return json.dumps({"emails": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_candidate_emails",
                "description": "List emails for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"]
                }
            }
        }


class CreateAssetRequest(Tool):
    """Create or update an asset request for a candidate (idempotent by candidate_id+asset_type)."""
    @staticmethod
    def invoke(db: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        asset_type = kwargs["asset_type"]
        status = kwargs.get("status", "Requested")
        ts = _fixed_ts(kwargs.get("requested_ts"))
        reqs = db.setdefault("asset_requests", [])

        row = next((r for r in reqs if r.get("candidate_id") == cand_id and r.get("asset_type") == asset_type), None)
        if row:
            row["status"] = status
            row["updated_ts"] = ts
            return json.dumps({"request_id": row["request_id"], "status": "updated"}, indent=2)

        request_id = _next_seq(reqs, "request_id", "req")
        reqs.append({
            "request_id": request_id,
            "candidate_id": cand_id,
            "asset_type": asset_type,
            "status": status,
            "email_message_id_nullable": None,
            "inventory_checked_flag": False,
            "asset_tag_nullable": None,
            "requested_ts": ts,
            "updated_ts": ts
        })
        return json.dumps({"request_id": request_id, "status": "created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_asset_request",
                "description": "Create or update an asset request for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "asset_type": {"type": "string"},
                        "status": {"type": "string"},
                        "requested_ts": {"type": "string"}
                    },
                    "required": ["candidate_id", "asset_type"]
                }
            }
        }


class WriteAssetRequestFile(Tool):
    """Write /onboarding/<candidate>/asset_request.json into onboarding_files."""
    @staticmethod
    def invoke(db: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        file_path = kwargs.get("file_path") or f"/onboarding/{cand_id}/asset_request.json"
        payload = kwargs.get("payload", {})
        return WriteOnboardingFile.invoke(
            db,
            candidate_id=cand_id,
            file_path=file_path,
            content_text=json.dumps(payload, sort_keys=True, indent=2),
            mime_type="application/json",
            created_ts=kwargs.get("created_ts"),
            updated_ts=kwargs.get("updated_ts"),
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "write_asset_request_file",
                "description": "Store asset_request.json for the candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "file_path": {"type": "string"},
                        "payload": {"type": "object"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"}
                    },
                    "required": ["candidate_id", "payload"]
                }
            }
        }


class AssignAssetToCandidate(Tool):
    """
    Assign an asset_tag to a candidate:
    - inventory_assets.assigned_candidate_id_nullable = candidate_id and status='allocated'
    - candidates updated with asset_tag (optional via fields)
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_tag = kwargs["asset_tag"]
        cand_id = kwargs["candidate_id"]

        inv = data.get("inventory_assets", [])
        row = next((a for a in inv if a.get("asset_tag") == asset_tag), None)
        if not row:
            return json.dumps({"error": f"asset_tag {asset_tag} not found"}, indent=2)

        row["assigned_candidate_id_nullable"] = cand_id
        row["status"] = "allocated"
        for c in data.get("candidates", []):
            if c.get("candidate_id") == cand_id:
                c["allocated_asset_tag_nullable"] = asset_tag
        return json.dumps({"asset_tag": asset_tag, "assigned_to": cand_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_asset_to_candidate",
                "description": "Assign inventory asset to candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_tag": {"type": "string"},
                        "candidate_id": {"type": "string"}
                    },
                    "required": ["asset_tag", "candidate_id"]
                }
            }
        }


class RecordAccessChecks(Tool):
    @staticmethod
    def invoke(data, **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        checks = kwargs.get("checks", [])
        rows = data.setdefault("access_checks", [])
        ids = []
        for i, chk in enumerate(checks):
            payload = {
                "access_check_id": _next_seq(rows, "access_check_id", "acc"),
                "candidate_id": cand_id,
                "system_name": chk["system_name"],
                "status": chk["status"],
                "note_nullable": chk.get("note"),
                "checked_ts": _fixed_ts(chk.get("checked_ts")),
            }
            rows.append(payload)
            ids.append(payload["access_check_id"])
        return json.dumps({"inserted": len(ids), "access_check_ids": ids}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_access_checks",
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
                                    "checked_ts": {"type": "string"}
                                },
                                "required": ["system_name", "status"]
                            }
                        }
                    },
                    "required": ["candidate_id", "checks"]
                }
            }
        }


class UpdateCandidateInviteTimestamps(Tool):
    """Copy invite timestamps (orientation, manager intro) into candidate row."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        fields = {}
        if "orientation_invite_ts" in kwargs:
            fields["orientation_invite_ts_nullable"] = _fixed_ts(kwargs["orientation_invite_ts"])
        if "manager_intro_invite_ts" in kwargs:
            fields["manager_intro_invite_ts_nullable"] = _fixed_ts(kwargs["manager_intro_invite_ts"])
        return UpdateCandidateStatusFields.invoke(data, candidate_id=cand_id, fields=fields)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_candidate_invite_timestamps",
                "description": "Set candidate invite timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "orientation_invite_ts": {"type": "string"},
                        "manager_intro_invite_ts": {"type": "string"}
                    },
                    "required": ["candidate_id"]
                }
            }
        }


class SearchChecklistItems(Tool):
    """Filter checklist_items by candidate_id, optional status, optional due_date_lte."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        status = kwargs.get("status")
        due_lte = kwargs.get("due_date_lte")
        rows = []
        for it in data.get("checklist_items", []):
            if it.get("candidate_id") != cand_id:
                continue
            if status and it.get("status") != status:
                continue
            if due_lte and it.get("due_date") and it["due_date"] > due_lte:
                continue
            rows.append(it)
        return json.dumps({"items": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_checklist_items",
                "description": "Search checklist items for a candidate with simple filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "status": {"type": "string"},
                        "due_date_lte": {"type": "string"}
                    },
                    "required": ["candidate_id"]
                }
            }
        }


class WritePendingTasksFile(Tool):
    """Write pending_tasks.md under /onboarding/<candidate>/, content provided by caller."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        content_md = kwargs.get("content_markdown", "# Pending Tasks\n")
        file_path = kwargs.get("file_path") or f"/onboarding/{cand_id}/pending_tasks.md"
        return WriteOnboardingFile.invoke(
            data,
            candidate_id=cand_id,
            file_path=file_path,
            content_text=content_md,
            mime_type="text/markdown",
            created_ts=kwargs.get("created_ts"),
            updated_ts=kwargs.get("updated_ts"),
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "write_pending_tasks_file",
                "description": "Write a markdown summary of pending checklist items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "content_markdown": {"type": "string"},
                        "file_path": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"}
                    },
                    "required": ["candidate_id"]
                }
            }
        }


class MarkChecklistItemsReminded(Tool):
    """Set status='Reminder Sent', reminder_sent_flag=true, reminder_email_message_id_nullable, updated_ts."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        item_ids: List[str] = kwargs["item_ids"]
        msg_id: Optional[str] = kwargs.get("reminder_email_message_id")
        updated_ts = _fixed_ts(kwargs.get("updated_ts"))

        updated = 0
        for it in data.get("checklist_items", []):
            if it.get("item_id") in item_ids:
                it["status"] = "Reminder Sent"
                it["reminder_sent_flag"] = True
                it["reminder_email_message_id_nullable"] = msg_id
                it["updated_ts"] = updated_ts
                updated += 1
        return json.dumps({"updated": updated, "message_id": msg_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "mark_checklist_items_reminded",
                "description": "Mark checklist items as reminded, link the reminder email id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                        "reminder_email_message_id": {"type": "string"},
                        "updated_ts": {"type": "string"}
                    },
                    "required": ["item_ids"]
                }
            }
        }


class UpdateAssetRequestStatus(Tool):
    @staticmethod
    def _find_email(db, candidate_id: str, subject: str, date_ts: str):
        emails = db.get("emails", [])
        matches = [e for e in emails
                   if e.get("candidate_id_nullable") == candidate_id
                   and e.get("subject") == subject
                   and e.get("date_ts") == date_ts]
        if not matches: return None
        def seq(e):
            m = re.match(r"^msg_(\d+)$", e.get("message_id",""))
            return int(m.group(1) or 0) if m else 0
        matches.sort(key=lambda e: (e.get("sent_flag") is True, seq(e)), reverse=True)
        return matches[0]

    @staticmethod
    def invoke(db, **kwargs) -> str:
        reqs = db.setdefault("asset_requests", [])
        row = None
        if "request_id" in kwargs:
            row = next((r for r in reqs if r.get("request_id") == kwargs["request_id"]), None)
        else:
            row = next((r for r in reqs if r.get("candidate_id") == kwargs["candidate_id"] and r.get("asset_type") == kwargs["asset_type"]), None)
        if not row:
            return json.dumps({"error": "asset request not found"}, indent=2)
        email_id = kwargs.get("email_message_id")
        if not email_id:
            cand_id = kwargs.get("candidate_id")
            subj    = kwargs.get("subject")
            dts     = _fixed_ts(kwargs.get("date_ts"))
            if cand_id and subj:
                em = UpdateAssetRequestStatus._find_email(db, cand_id, subj, dts)
                if em: email_id = em.get("message_id")
        row["status"] = kwargs.get("status", row.get("status"))
        if email_id is not None:
            row["email_message_id_nullable"] = email_id
        row["updated_ts"] = _fixed_ts(kwargs.get("updated_ts"))
        return json.dumps({"request_id": row["request_id"], "status": row["status"], "email_message_id": row.get("email_message_id_nullable")}, indent=2)


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_asset_request_status",
                "description": "Update asset request status and optional email message id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "asset_type": {"type": "string"},
                        "status": {"type": "string"},
                        "email_message_id": {"type": "string"},
                        "updated_ts": {"type": "string"}
                    },
                    "required": ["candidate_id", "asset_type"]
                }
            }
        }


class AllocateFirstAvailableAsset(Tool):
    """
    Allocate the first available inventory asset for a given request_id.
    - Reads asset_requests[request_id] to get (candidate_id, asset_type)
    - Picks the lexicographically smallest inventory_assets row where:
        status in {'available','Available'} (case-insensitive OK) and assigned_candidate_id_nullable is null
        and asset_type matches the request's asset_type
    - Writes:
        inventory_assets.assigned_candidate_id_nullable = candidate_id
        inventory_assets.status = 'allocated'
        candidates[candidate_id].allocated_asset_tag_nullable = asset_tag
        asset_requests[request_id].updated_ts = FIXED_TS
    Returns: {"request_id", "candidate_id", "asset_type", "asset_tag", "status":"allocated"}
    """
    @staticmethod
    def invoke(db: Dict[str, Any], **kwargs) -> str:
        rid = kwargs["request_id"]
        req = next((r for r in db.get("asset_requests", []) if r.get("request_id") == rid), None)
        if not req:
            return json.dumps({"error": f"request_id {rid} not found"}, indent=2)
        cand_id = req.get("candidate_id"); a_type = req.get("asset_type")
        inv = db.get("inventory_assets", [])
        def is_free(row):
            st = (row.get("status") or "").lower()
            return (row.get("asset_type") == a_type) and (row.get("assigned_candidate_id_nullable") in (None, "")) and (st in ("available","avail","free"))
        free = sorted([r for r in inv if is_free(r)], key=lambda r: (r.get("asset_tag") or ""))
        if not free:
            return json.dumps({"request_id": rid, "candidate_id": cand_id, "asset_type": a_type, "asset_tag": None, "status": "none_available"}, indent=2)
        chosen = free[0]
        chosen["assigned_candidate_id_nullable"] = cand_id
        chosen["status"] = "allocated"
        for c in db.get("candidates", []):
            if c.get("candidate_id") == cand_id:
                c["allocated_asset_tag_nullable"] = chosen.get("asset_tag")
                break
        req["updated_ts"] = _fixed_ts(kwargs.get("updated_ts"))
        return json.dumps({
            "request_id": rid,
            "candidate_id": cand_id,
            "asset_type": a_type,
            "asset_tag": chosen.get("asset_tag"),
            "status": "allocated"
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"allocate_first_available_asset",
            "description":"Allocate the first available inventory asset for an existing request_id, and mirror the tag onto the candidate.",
            "parameters":{"type":"object","properties":{"request_id":{"type":"string"}, "updated_ts":{"type":"string"}}, "required":["request_id"]}
        }}


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


class SummarizeAccessChecks(Tool):
    """
    Aggregate access_checks for a candidate and write /onboarding/<Name>/access_summary.json.
    Always writes the file (even if zero rows), returns file_path and counts.
    """
    @staticmethod
    def _safe_name(s: str) -> str:
        return re.sub(r"[^A-Za-z0-9]+", "_", s or "").strip("_") or "unknown"

    @staticmethod
    def invoke(db: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        cand_row = next((r for r in db.get("candidates", []) if r.get("candidate_id") == cand_id), None)
        name = cand_row.get("candidate_name") if cand_row else cand_id
        checks = [r for r in db.get("access_checks", []) if r.get("candidate_id") == cand_id]
        by_sys: Dict[str, Dict[str, int]] = {}
        for r in checks:
            sysn = r.get("system_name") or ""
            st = r.get("status") or ""
            by_sys.setdefault(sysn, {}).setdefault(st, 0)
            by_sys[sysn][st] += 1
        summary = {"candidate_id": cand_id, "counts": by_sys, "total": len(checks)}
        file_path = f"/onboarding/{SummarizeAccessChecks._safe_name(name)}/access_summary.json"
        WriteOnboardingFile.invoke(db, candidate_id=cand_id, file_path=file_path, content_text=json.dumps(summary, sort_keys=True, indent=2), mime_type="application/json", updated_ts=_fixed_ts(None))
        return json.dumps({"file_path": file_path, "total_checks": len(checks)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"summarize_access_checks",
            "description":"Aggregate access_checks and write an access_summary.json artifact.",
            "parameters":{"type":"object","properties":{"candidate_id":{"type":"string"}},"required":["candidate_id"]}
        }}


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
    def invoke(db: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]; subject = kwargs["subject"]; date_ts = _fixed_ts(kwargs.get("date_ts"))
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


class CloseCompletedChecklistItems(Tool):
    """
    Set completed_ts for any 'Completed' checklist items missing a timestamp (optionally up to due_date_lte).
    Returns count updated.
    """
    @staticmethod
    def invoke(db: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]; due_lte = kwargs.get("due_date_lte")
        items = db.get("checklist_items", [])
        updated = 0
        for it in items:
            if it.get("candidate_id") != cand_id: continue
            if it.get("status") != "Completed": continue
            if it.get("completed_ts"): continue
            if due_lte and it.get("due_date") and it["due_date"] > due_lte: continue
            it["completed_ts"] = _fixed_ts(None); updated += 1
        return json.dumps({"updated": updated}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"close_completed_checklist_items",
            "description":"Backfill completed_ts for completed checklist items.",
            "parameters":{"type":"object","properties":{
                "candidate_id":{"type":"string"},
                "due_date_lte":{"type":"string"}
            },"required":["candidate_id"]}
        }}


class RecordAccessChecksAndNotifyGaps(Tool):
    """
    Record access checks for a candidate and send an 'Access Gaps' email in one step.
    Touches: access_checks (append), emails (create+send)
    Returns: {"message_id": "...", "checks_recorded": N}
    """
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


TOOLS = [
    FindCandidateByEmail(),
    UpsertCandidateRecord(),
    GetCandidateDetails(),
    UpdateCandidateStatusFields(),
    SearchAttachmentsByFilename(),
    ReadOnboardingFile(),
    RenderOnboardingWelcome(),
    WriteOnboardingFile(),
    GenerateAndSendEmail(),
    GetOrCreateEmailLabel(),
    ModifyEmailLabels(),
    ListCandidateEmails(),
    CreateAssetRequest(),
    WriteAssetRequestFile(),
    AssignAssetToCandidate(),
    UpdateAssetRequestStatus(),
    RecordAccessChecks(),
    UpdateCandidateInviteTimestamps(),
    SearchChecklistItems(),
    WritePendingTasksFile(),
    MarkChecklistItemsReminded(),
    ReadAssetRequest(),
    AllocateFirstAvailableAsset(),
    ReplyToEmailThread(),
    SummarizeAccessChecks(),
    AuditAttachmentsForEmail(),
    CloseCompletedChecklistItems(),
    RecordAccessChecksAndNotifyGaps(),

]
