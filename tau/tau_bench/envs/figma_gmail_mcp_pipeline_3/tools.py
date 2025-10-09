import json
import re
from datetime import datetime

#Automatically created tools.py (revised by assistant)
from typing import Any

from tau_bench.envs.tool import Tool

_ISO8601Z = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


def _get_table(data: dict[str, Any], name: str) -> list[dict[str, Any]]:
    """Get table from data and convert from dict to list if needed."""
    table = data.get(name, [])
    return _convert_db_to_list(table)


def _export_ext_from_format(fmt: str) -> str:
    s = (fmt or "").lower()
    if "pdf" in s:
        return "pdf"
    if "png" in s:
        return "png"
    if "jpg" in s or "jpeg" in s:
        return "jpg"
    return "pdf"


def _ok(x):
    return _j(x)


def _export_ext_from_profile(profile: str) -> str:
    s = (profile or "").lower()
    if "png" in s:
        return "png"
    if "jpg" in s or "jpeg" in s:
        return "jpg"
    if "pdf" in s:
        return "pdf"
    return "png"


def _params(data: dict[str, Any], kwargs: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in (kwargs or {}).items() if v is not None}


def _j(x):
    payload = x
    out = json.dumps(payload, ensure_ascii=False)
    return out


def _err(code, extra=None):
    payload = {"error": code}
    if isinstance(extra, dict):
        payload.update(extra)
    return _j(payload)


def _ensure(data: dict[str, Any], key: str, default):
    if key not in data or data[key] is None:
        data[key] = default
    return data[key]


def _ymd(ts: str) -> str:
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).strftime("%Y%m%d")
    except Exception:
        return datetime.utcnow().strftime("%Y%m%d")


def _require_write(p: dict[str, Any]):
    miss = _require(p, ["timestamp", "request_id"])
    if miss:
        return miss
    ts = p.get("timestamp")
    if not isinstance(ts, str) or not _ISO8601Z.match(ts):
        return _err("invalid_timestamp_format")
    rid = p.get("request_id")
    if not isinstance(rid, str) or not rid:
        return _err("invalid_request_id")
    return None


def _require(p: dict[str, Any], req: list[str]):
    missing = [k for k in req.values() if p.get(k) in (None, "")]
    if missing:
        return _err("missing_params", {"missing": missing})
    return None


class find_gmail_threads(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], label_contains: str = None, subject_contains: str = None, participant_email: str = None) -> str:
        p = _params(data, {
            "label_contains": label_contains,
            "subject_contains": subject_contains,
            "participant_email": participant_email
        })
        rows = []
        threads = _get_table(data, "gmail_threads")
        label_q = p.get("label_contains")
        subj_q = p.get("subject_contains")
        party_q = p.get("participant_email")

        for t in threads:
            ok = True
            if label_q:
                labels = t.get("labels", [])
                ok &= any(label_q.lower() in (lab or "").lower() for lab in labels)
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


class get_gmail_thread(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None, request_id: str = None, timestamp: str = None) -> str:
        p = _params(data, {"thread_id": thread_id})
        miss = _require(p, ["thread_id"])
        if miss:
            return miss
        threads = _ensure(data, "gmail_threads", [])
        for t in threads:
            if t.get("thread_id") == p["thread_id"]:
                return _ok(
                    {"thread_id": t["thread_id"], "current_labels": t.get("labels", [])}
                )
        return _ok({"thread_id": p["thread_id"], "current_labels": []})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGmailThread",
                "description": "Fetch a Gmail thread metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {"thread_id": {"type": "string"}},
                    "required": ["thread_id"],
                },
            },
        }


class list_gmail_messages(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None, request_id: str = None, timestamp: str = None) -> str:
        p = _params(data, {"thread_id": thread_id})
        miss = _require(p, ["thread_id"])
        if miss:
            return miss
        rows = []
        messages = _ensure(data, "gmail_messages", [])
        for m in messages:
            if m.get("thread_id") == p["thread_id"]:
                rows.append(
                    {
                        "message_id": m.get("message_id"),
                        "sender_email": m.get("sender_email"),
                        "recipients": m.get("recipients", []),
                        "body_html": m.get("body_html"),
                        "timestamp": m.get("timestamp"),
                    }
                )
                break
        return _ok({"rows": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListGmailMessages",
                "description": "List messages for a Gmail thread.",
                "parameters": {
                    "type": "object",
                    "properties": {"thread_id": {"type": "string"}},
                },
            },
        }


class create_gmail_thread(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject: str = None, sender_email: str = None, recipients: list = None, request_id: str = None, timestamp: str = None, initial_labels: list = None) -> str:
        p = _params(data, {
            "subject": subject,
            "sender_email": sender_email,
            "recipients": recipients,
            "request_id": request_id
        })
        miss = _require(p, ["subject", "sender_email", "recipients", "request_id"])
        if miss:
            return miss
        threads = _ensure(data, "gmail_threads", [])
        thread_id = f"thr_{p['request_id']}"
        thread = {
            "thread_id": thread_id,
            "subject": p.get("subject", ""),
            "participants": list({p["sender_email"], *p.get("recipients", [])}),
            "labels": [],
            "messages": [],
        }
        thre_get_table(data, "ads")[ad_id] = thread
        return _ok({"thread_id": thread_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateGmailThread",
                "description": "Create a new Gmail thread.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "sender_email": {"type": "string"},
                        "recipients": {"type": "array", "items": {"type": "string"}},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["subject", "sender_email", "recipients", "request_id"],
                },
            },
        }


class append_gmail_message(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        body_html: str = None,
        recipients: list = None,
        request_id: str = None,
        sender_email: str = None,
        thread_id: str = None,
        timestamp: Any = None,
        attachments_asset_ids: list = None
    ) -> str:
        p = {
            "thread_id": thread_id,
            "sender_email": sender_email,
            "body_html": body_html,
            "request_id": request_id,
            "recipients": recipients or [],
            "timestamp": timestamp
        }
        miss = _require(p, ["thread_id", "sender_email", "body_html", "request_id"])
        if miss:
            return miss
        threads = _ensure(data, "gmail_threads", [])
        for t in threads:
            if t.get("thread_id") == p["thread_id"]:
                msg_id = f"msg_{p['request_id']}"
                msg = {
                    "message_id": msg_id,
                    "sender_email": p["sender_email"],
                    "recipients": p["recipients"],
                    "body_html": p["body_html"],
                    "timestamp": p["timestamp"],
                }
                t.setdefault("gmail_messages", []).append(msg)
                new_parts = set(t.get("participants", []))
                new_parts.add(p["sender_email"])
                for r in p["recipients"]:
                    new_parts.add(r)
                t["participants"] = list(new_parts)
                return _ok({"message_id": msg_id})
        return _err("thread_not_found", {"thread_id": p["thread_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendGmailMessage",
                "description": "Append a message to an existing Gmail thread.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "sender_email": {"type": "string"},
                        "recipients": {"type": "array", "items": {"type": "string"}},
                        "body_html": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "thread_id",
                        "sender_email",
                        "body_html",
                        "request_id",
                    ],
                },
            },
        }


class apply_gmail_labels(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None, add_labels: list = None, remove_labels: list = None, request_id: str = None, timestamp: str = None) -> str:
        p = _params(data, {"thread_id": thread_id, "add_labels": add_labels, "request_id": request_id})
        miss = _require(p, ["thread_id", "add_labels", "request_id"])
        if miss:
            return miss
        threads = _ensure(data, "gmail_threads", [])
        for t in threads:
            if t.get("thread_id") == p["thread_id"]:
                labels = set(t.get("labels", []))
                for lab in p.get("add_labels", []):
                    labels.add(lab)
                t["labels"] = list(labels)
                return _ok({"labels": t["labels"]})
        return _err("thread_not_found", {"thread_id": p["thread_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyGmailLabels",
                "description": "Apply one or more labels to a Gmail thread.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "add_labels": {"type": "array", "items": {"type": "string"}},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["thread_id", "add_labels", "request_id"],
                },
            },
        }


class list_artifacts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_type: str = None, owner_email: str = None, figma_file_id: str = None, tag: str = None) -> str:
        p = {
            "artifact_type": artifact_type,
            "owner_email": owner_email,
            "figma_file_id": figma_file_id,
            "tag": tag
        }
        rows = []
        for a in _ensure(data, "figma_artifacts", []):
            if p.get("artifact_type") and a.get("artifact_type") != p["artifact_type"]:
                continue
            if p.get("owner_email") and a.get("owner_email") != p["owner_email"]:
                continue
            if p.get("figma_file_id") and a.get("figma_file_id") != p["figma_file_id"]:
                continue
            if p.get("tag"):
                tags = a.get("tags", [])
                if p["tag"] not in tags:
                    continue
            rows.append(a)
        return _ok({"rows": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listArtifacts",
                "description": "List Figma artifacts (files/pages/frames) with optional filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_type": {"type": "string"},
                        "owner_email": {"type": "string"},
                        "figma_file_id": {"type": "string"},
                        "tag": {"type": "string"},
                    },
                },
            },
        }


class list_assets(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        rows = list(_ensure(data, "assets", []))
        return _ok({"rows": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listAssets",
                "description": "List exported assets and reports.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class export_assets(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str = None,
        export_profile: str = None,
        request_id: str = None,
        timestamp: str = None
    ) -> str:
        p = _params(data, {
            "artifact_id": artifact_id,
            "export_profile": export_profile,
            "request_id": request_id,
            "timestamp": timestamp
        })
        miss = _require(p, ["artifact_id", "export_profile", "request_id", "timestamp"])
        if miss:
            return miss
        ext = _export_ext_from_profile(p["export_profile"])
        ymd = _ymd(p["timestamp"])
        export_id = f"exp-{p['artifact_id']}-{ymd}-{ext}-001"
        asset_id = f"asset_{p['request_id']}"
        asset = {
            "asset_id": asset_id,
            "export_id": export_id,
            "artifact_id": p["artifact_id"],
        }
        _ensure(data, "assets", []).append(asset)
        return _ok({"asset_id": asset_id, "export_id": export_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportAssets",
                "description": "Export assets for an artifact using an export profile.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "export_profile": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "artifact_id",
                        "export_profile",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }


class list_figma_comments(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None, resolved_flag: bool = None) -> str:
        p = _params(data, {"artifact_id": artifact_id, "resolved_flag": resolved_flag})
        rows = []
        for c in _ensure(data, "figma_comments", []):
            if p.get("artifact_id") and c.get("artifact_id") != p["artifact_id"]:
                continue
            if "resolved_flag" in p and bool(c.get("resolved_flag", False)) != bool(
                p["resolved_flag"]
            ):
                continue
            rows.append(c)
        return _ok({"rows": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listFigmaComments",
                "description": "List comments for a Figma artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "resolved_flag": {"type": "boolean"},
                    },
                },
            },
        }


class create_figma_comment(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str = None,
        author_email: str = None,
        content: str = None,
        request_id: str = None,
        timestamp: str = None,
        source_message_id_nullable: str = None
    ) -> str:
        p = {
            "artifact_id": artifact_id,
            "author_email": author_email,
            "content": content,
            "request_id": request_id,
            "timestamp": timestamp
        }
        miss = _require(p, ["artifact_id", "author_email", "content", "request_id"])
        if miss:
            return miss
        comment_id = f"comment_{p['request_id']}"
        c = {
            "comment_id": comment_id,
            "artifact_id": p["artifact_id"],
            "author_email": p["author_email"],
            "content": p["content"],
            "timestamp": p.get("timestamp"),
            "resolved_flag": False,
        }
        _ensure(data, "figma_comments", []).append(c)
        return _ok({"comment_id": comment_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFigmaComment",
                "description": "Create a new comment on a Figma artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "author_email": {"type": "string"},
                        "content": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "artifact_id",
                        "author_email",
                        "content",
                        "request_id",
                    ],
                },
            },
        }


class list_audit_findings_ds(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, finding_type: str = None) -> str:
        p = _params(data, {"audit_id": audit_id, "finding_type": finding_type})
        miss = _require(p, ["audit_id", "finding_type"])
        if miss:
            return miss
        rows = []
        for a in _ensure(data, "audits", []):
            if a.get("audit_id") == p["audit_id"]:
                for f in a.get("ds_findings", []):
                    if f.get("finding_type") == p["finding_type"]:
                        rows.append(f)
                break
        return _ok({"rows": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAuditFindingsDs",
                "description": "List design-system findings for an audit by type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "finding_type": {"type": "string"},
                    },
                    "required": ["audit_id", "finding_type"],
                },
            },
        }


class list_audit_findings_a11y(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None, violation_type: str = None) -> str:
        p = _params(data, {"audit_id": audit_id, "violation_type": violation_type})
        miss = _require(p, ["audit_id", "violation_type"])
        if miss:
            return miss
        rows = []
        for a in _ensure(data, "audits", []):
            if a.get("audit_id") == p["audit_id"]:
                for f in a.get("a11y_findings", []):
                    if f.get("violation_type") == p["violation_type"]:
                        rows.append(f)
                break
        return _ok({"rows": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAuditFindingsA11y",
                "description": "List accessibility findings for an audit by violation type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "violation_type": {"type": "string"},
                    },
                    "required": ["audit_id", "violation_type"],
                },
            },
        }


class GenerateAuditReport(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str = None,
        audit_id: str = None,
        format: str = None,
        request_id: str = None,
        timestamp: str = None
    ) -> str:
        p = _params(data, {
            "artifact_id": artifact_id,
            "audit_id": audit_id,
            "format": format,
            "timestamp": timestamp,
            "request_id": request_id
        })
        miss = _require(
            p, ["artifact_id", "audit_id", "format", "timestamp", "request_id"]
        )
        if miss:
            return miss
        ext = _export_ext_from_format(p["format"])
        ymd = _ymd(p["timestamp"])
        asset_id = f"exp-{p['artifact_id']}-{ymd}-{ext}-001"
        _ensure(data, "assets", []).append(
            {
                "asset_id": asset_id,
                "artifact_id": p["artifact_id"],
                "audit_id": p["audit_id"],
                "kind": "audit_report",
            }
        )
        return _ok({"asset_id": asset_id})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateAuditReport",
                "description": "Generate an audit report asset for an artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "audit_id": {"type": "string"},
                        "format": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "artifact_id",
                        "audit_id",
                        "format",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }


class update_audit_status(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str = None,
        request_id: str = None,
        status: str = None,
        updated_at: str = None,
        timestamp: str = None
    ) -> str:
        p = {
            "audit_id": audit_id,
            "status": status,
            "request_id": request_id,
            "updated_at": updated_at
        }
        miss = _require(p, ["audit_id", "status", "request_id"])
        if miss:
            return miss
        for a in _ensure(data, "audits", []):
            if a.get("audit_id") == p["audit_id"]:
                a["status"] = p["status"]
                a["updated_at"] = p.get("updated_at")
                return _ok({"audit_id": a["audit_id"], "status": a["status"]})
        return _err("audit_not_found", {"audit_id": p["audit_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAuditStatus",
                "description": "Update an audit's status deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "status": {"type": "string"},
                        "updated_at": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["audit_id", "status", "request_id"],
                },
            },
        }


class get_audit(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None) -> str:
        p = _params(data, {"audit_id": audit_id})
        miss = _require(p, ["audit_id"])
        if miss:
            return miss
        for a in _ensure(data, "audits", []):
            if a.get("audit_id") == p["audit_id"]:
                return _ok(a)
        return _err("audit_not_found", {"audit_id": p["audit_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAudit",
                "description": "Fetch a single audit by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"audit_id": {"type": "string"}},
                    "required": ["audit_id"],
                },
            },
        }


class list_review_cycles(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        pass
        return _ok({"rows": list(_ensure(data, "review_cycles", []))})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListReviewCycles",
                "description": "List review cycles.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class create_review_cycle(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        artifact_id: str = None,
        cycle_id: str = None,
        request_id: str = None,
        started_at: str = None,
        timestamp: str = None
    ) -> str:
        p = _params(data, {
            "cycle_id": cycle_id,
            "artifact_id": artifact_id,
            "started_at": started_at,
            "timestamp": timestamp,
            "request_id": request_id
        })

        #mandatory fields
        miss = _require(
            p, ["cycle_id", "artifact_id", "started_at", "timestamp", "request_id"]
        )
        if miss:
            return miss
        w = _require_write(p)
        if w:
            return w

        #ID_RULE: review_cycle_id — rev-<artifact_id>-<YYYYMMDD>-<seq>
        m = re.match(
            r"^rev-(?P<art>[^-]+)-(?P<date>\d{8})-(?P<seq>\d+)$", p["cycle_id"]
        )
        if not m:
            return _err("invalid_cycle_id_format")

        art_from_id = m.group("art")
        date_from_id = m.group("date")
        ts_date = p["timestamp"][0:10].replace("-", "")

        if art_from_id != p["artifact_id"]:
            return _err("cycle_id_artifact_mismatch")
        if date_from_id != ts_date:
            return _err("cycle_id_date_mismatch")

        #consistent output; no thread linked at the time of creation
        c = {
            "cycle_id": p["cycle_id"],
            "artifact_id": p["artifact_id"],
            "status": "IN_FLIGHT",
            "started_at": p["started_at"],
            "created_ts": p["timestamp"],
            "thread_id_nullable": None,
        }
        _ensure(data, "review_cycles", []).append(c)
        return _ok(c)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReviewCycle",
                "description": "Create a review cycle with deterministic ID validation per ID_RULE.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "artifact_id": {"type": "string"},
                        "started_at": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "cycle_id",
                        "artifact_id",
                        "started_at",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }


class get_review_cycle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str = None) -> str:
        p = _params(data, {"cycle_id": cycle_id})
        miss = _require(p, ["cycle_id"])
        if miss:
            return miss
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                return _ok(c)
        return _ok(
            {"cycle_id": p["cycle_id"], "status": "", "thread_id_nullable": None}
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReviewCycle",
                "description": "Fetch a review cycle summary.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["cycle_id"],
                },
            },
        }


class list_review_approvals(Tool):
    def invoke(data: dict[str, Any], cycle_id: str = None) -> str:
        p = _params(data, {"cycle_id": cycle_id})
        miss = _require(p, ["cycle_id"])
        if miss:
            return miss
        rows = []
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                for email, ts in c.get("approvals", {}).values().items():
                    rows.append({"approver_email": email, "approved_ts_nullable": ts})
                break
        return _ok({"rows": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listReviewApprovals",
                "description": "List approvals for a review cycle.",
                "parameters": {
                    "type": "object",
                    "properties": {"cycle_id": {"type": "string"}},
                    "required": ["cycle_id"],
                },
            },
        }


class update_review_approval(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        approved_ts_nullable: str = None,
        approver_email: str = None,
        cycle_id: str = None,
        request_id: str = None,
        timestamp: str = None
    ) -> str:
        p = {
            "cycle_id": cycle_id,
            "approver_email": approver_email,
            "approved_ts_nullable": approved_ts_nullable,
            "request_id": request_id,
            "timestamp": timestamp
        }
        miss = _require(
            p, ["cycle_id", "approver_email", "approved_ts_nullable", "request_id"]
        )
        if miss:
            return miss
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                c.setdefault("approvals", {}).values()[p["approver_email"]] = p[
                    "approved_ts_nullable"
                ]
                return _ok(
                    {
                        "cycle_id": p["cycle_id"],
                        "approver_email": p["approver_email"],
                        "approved_ts_nullable": p["approved_ts_nullable"],
                        "approval_comment_ref_nullable": None,
                        "updated_ts": p.get("timestamp"),
                    }
                )
        return _err("cycle_not_found", {"cycle_id": p["cycle_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReviewApproval",
                "description": "Set/Update approval timestamp for a reviewer in a cycle.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "approver_email": {"type": "string"},
                        "approved_ts_nullable": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "cycle_id",
                        "approver_email",
                        "approved_ts_nullable",
                        "request_id",
                    ],
                },
            },
        }


class attach_thread_to_review_cycle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str = None, thread_id: str = None, updated_at: str = None, timestamp: str = None, request_id: str = None) -> str:
        p = _params(data, {"cycle_id": cycle_id, "thread_id": thread_id})
        miss = _require(p, ["cycle_id", "thread_id"])
        if miss:
            return miss
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                c["thread_id_nullable"] = p["thread_id"]
                return _ok({"cycle_id": c["cycle_id"], "thread_id": p["thread_id"]})
        return _err("cycle_not_found", {"cycle_id": p["cycle_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AttachThreadToReviewCycle",
                "description": "Attach an email thread to a review cycle.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "thread_id": {"type": "string"},
                    },
                    "required": ["cycle_id", "thread_id"],
                },
            },
        }


class update_review_cycle_status(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cycle_id: str = None,
        request_id: str = None,
        status: str = None,
        updated_at: str = None,
        timestamp: str = None
    ) -> str:
        p = _params(data, {"cycle_id": cycle_id, "status": status, "request_id": request_id, "updated_at": updated_at})
        miss = _require(p, ["cycle_id", "status", "request_id"])
        if miss:
            return miss
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                c["status"] = p["status"]
                c["updated_at"] = p.get("updated_at")
                return _ok(
                    {
                        "cycle_id": c["cycle_id"],
                        "status": c["status"],
                        "updated_at": c.get("updated_at"),
                    }
                )
        return _err("cycle_not_found", {"cycle_id": p["cycle_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReviewCycleStatus",
                "description": "Update the status of a review cycle.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "status": {"type": "string"},
                        "updated_at": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["cycle_id", "status", "request_id"],
                },
            },
        }


class verify_single_thread_per_cycle(Tool):
    def invoke(data: dict[str, Any], cycle_id: str = None) -> str:
        p = _params(data, {"cycle_id": cycle_id})
        miss = _require(p, ["cycle_id"])
        if miss:
            return miss
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                ok = c.get("thread_id_nullable") is not None
                return _ok({"ok": ok, "cycle_id": c["cycle_id"]})
        return _ok({"ok": False, "cycle_id": p["cycle_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verifySingleThreadPerCycle",
                "description": "Verify each cycle has exactly one attached thread (simplified).",
                "parameters": {
                    "type": "object",
                    "properties": {"cycle_id": {"type": "string"}},
                    "required": ["cycle_id"],
                },
            },
        }


class list_releases(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        pass
        return _ok({"rows": list(_ensure(data, "releases", []))})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listReleases",
                "description": "List releases.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class get_release_diff(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], release_id: str = None) -> str:
        p = _params(data, {"release_id": release_id})
        miss = _require(p, ["release_id"])
        if miss:
            return miss
        for r in _ensure(data, "releases", []):
            if r.get("release_id") == p["release_id"]:
                return _ok({"release_id": r["release_id"], "diff": r.get("diff", {}).values()})
        return _err("release_not_found", {"release_id": p["release_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReleaseDiff",
                "description": "Fetch a release diff summary.",
                "parameters": {
                    "type": "object",
                    "properties": {"release_id": {"type": "string"}},
                    "required": ["release_id"],
                },
            },
        }


class create_fix_plan(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        audit_id: str = None,
        delivery_method: str = None,
        owner_email: str = None,
        request_id: str = None,
        timestamp: str = None
    ) -> str:
        p = _params(data, {
            "audit_id": audit_id,
            "owner_email": owner_email,
            "delivery_method": delivery_method,
            "timestamp": timestamp,
            "request_id": request_id
        })
        miss = _require(
            p, ["audit_id", "owner_email", "delivery_method", "timestamp", "request_id"]
        )
        if miss:
            return miss
        w = _require_write(p)
        if w:
            return w

        # Obtain artifact_id from audit_id "aud-<artifact_id>-<YYYYMMDD>-<seq>"
        audit_id = p["audit_id"]
        m = re.match(r"^aud-(?P<art>[^-]+)-(?P<date>\d{8})-(?P<seq>\d+)$", audit_id)
        if not m:
            return _err("invalid_audit_id_format")
        artifact_id = m.group("art")

        # According to ID_RULE: date is based on timestamp
        yyyymmdd = p["timestamp"][0:10].replace("-", "")
        plan_id = f"fp-{artifact_id}-{yyyymmdd}-001"
        plan = {
            "plan_id": plan_id,
            "audit_id": audit_id,
            "owner_email": p["owner_email"],
            "delivery_method": p["delivery_method"],
            "status": "DRAFTED",
            "created_ts": p["timestamp"],
        }
        _ensure(data, "fix_plans", []).append(plan)
        return _ok(plan)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFixPlan",
                "description": "Create a fix plan for an audit (deterministic id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "audit_id": {"type": "string"},
                        "owner_email": {"type": "string"},
                        "delivery_method": {
                            "type": "string",
                            "enum": ["COMMENTS", "TICKETS", "PDF", "EMAIL"],
                        },
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": [
                        "audit_id",
                        "owner_email",
                        "delivery_method",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }


class deliver_fix_plan(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, request_id: str = None, method: str = None, timestamp: str = None, recipients: list = None) -> str:
        p = _params(data, {"plan_id": plan_id, "request_id": request_id})
        miss = _require(p, ["plan_id", "request_id"])
        if miss:
            return miss
        for pl in _ensure(data, "fix_plans", []):
            if pl.get("plan_id") == p["plan_id"]:
                pl["status"] = "DELIVERED"
                return _ok({"plan_id": pl["plan_id"], "status": pl["status"]})
        return _err("plan_not_found", {"plan_id": p["plan_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeliverFixPlan",
                "description": "Mark a fix plan as delivered.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["plan_id", "request_id"],
                },
            },
        }


class upsert_fix_items(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, items: list = None, timestamp: str = None, request_id: str = None) -> str:
        p = _params(data, {"plan_id": plan_id, "items": items})
        miss = _require(p, ["plan_id", "items"])
        if miss:
            return miss
        for pl in _ensure(data, "fix_plans", []):
            if pl.get("plan_id") == p["plan_id"]:
                by_id = {i["item_id"]: i for i in pl.get("items", []) if "item_id" in i}
                for i in p.get("items", []):
                    iid = i.get("item_id") or f"item_{len(by_id)+1:03d}"
                    i["item_id"] = iid
                    by_id[iid] = i
                pl["items"] = list(by_id)
                return _ok({"plan_id": pl["plan_id"], "items": pl["items"]})
        return _err("plan_not_found", {"plan_id": p["plan_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertFixItems",
                "description": "Insert or update fix items on a plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["plan_id", "items"],
                },
            },
        }


class update_fix_item_status(Tool):
    def invoke(
        data: dict[str, Any],
        item_id: str = None,
        plan_id: str = None,
        status: str = None
    ) -> str:
        p = {"plan_id": plan_id, "item_id": item_id, "status": status}
        miss = _require(p, ["plan_id", "item_id", "status"])
        if miss:
            return miss
        for pl in _ensure(data, "fix_plans", []):
            if pl.get("plan_id") == p["plan_id"]:
                for it in pl.get("items", []):
                    if it.get("item_id") == p["item_id"]:
                        it["status"] = p["status"]
                        return _ok(
                            {
                                "plan_id": pl["plan_id"],
                                "item_id": p["item_id"],
                                "status": p["status"],
                            }
                        )
        return _err(
            "item_not_found", {"plan_id": p.get("plan_id"), "item_id": p.get("item_id")}
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateFixItemStatus",
                "description": "Update the status of a single fix item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["plan_id", "item_id", "status"],
                },
            },
        }


class governance_update(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None, request_id: str = None, add_tags: list = None, remove_tags: list = None, timestamp: str = None) -> str:
        p = _params(data, {
            "artifact_id": artifact_id,
            "request_id": request_id,
            "add_tags": add_tags,
            "remove_tags": remove_tags
        })
        miss = _require(p, ["artifact_id", "request_id"])
        if miss:
            return miss
        add = p.get("add_tags", [])
        rem = p.get("remove_tags", [])
        for a in _ensure(data, "figma_artifacts", []):
            if a.get("artifact_id") == p["artifact_id"]:
                tags = set(a.get("current_tags", []))
                for t in add:
                    tags.add(t)
                for t in rem:
                    if t in tags:
                        tags.remove(t)
                a["current_tags"] = list(tags)
                return _ok({"artifact_id": a["artifact_id"], "tags": a["current_tags"]})
        return _err("artifact_not_found", {"artifact_id": p["artifact_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GovernanceUpdate",
                "description": "Add/remove tags on an artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "add_tags": {"type": "array", "items": {"type": "string"}},
                        "remove_tags": {"type": "array", "items": {"type": "string"}},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["artifact_id", "request_id"],
                },
            },
        }


class record_automation_run(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        ended_at: str = None,
        request_id: str = None,
        started_at: str = None,
        status: str = None,
        task_name: str = None,
        timestamp: str = None
    ) -> str:
        p = _params(data, {
            "task_name": task_name,
            "status": status,
            "request_id": request_id,
            "started_at": started_at,
            "ended_at": ended_at,
            "timestamp": timestamp
        })
        miss = _require(p, ["task_name", "status", "request_id"])
        if miss:
            return miss
        run_id = f"run_{p['request_id']}"
        _ensure(data, "automation_runs", []).append(
            {
                "run_id": run_id,
                "task_name": p["task_name"],
                "status": p["status"],
                "started_at": p.get("started_at"),
                "ended_at": p.get("ended_at"),
                "timestamp": p.get("timestamp"),
            }
        )
        return _ok({"run_id": run_id, "status": p["status"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordAutomationRun",
                "description": "Record a deterministic automation run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_name": {"type": "string"},
                        "status": {"type": "string"},
                        "started_at": {"type": "string"},
                        "ended_at": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["task_name", "status", "request_id"],
                },
            },
        }


TOOLS = [
    #Items & Resources
    list_artifacts(),
    export_assets(),
    #Comments from Figma
    list_figma_comments(),
    create_figma_comment(),
    #Evaluation cycles & authorizations
    list_review_cycles(),
    get_review_cycle(),
    list_review_approvals(),
    update_review_approval(),
    attach_thread_to_review_cycle(),
    update_review_cycle_status(),
    #Deployments
    get_release_diff(),
    #Google Mail
    find_gmail_threads(),
    get_gmail_thread(),
    list_gmail_messages(),
    create_gmail_thread(),
    append_gmail_message(),
    apply_gmail_labels(),
    #Examinations
    get_audit(),
    list_audit_findings_ds(),
    list_audit_findings_a11y(),
    GenerateAuditReport(),
    update_audit_status(),
    #Repair strategies & elements
    create_fix_plan(),
    upsert_fix_items(),
    update_fix_item_status(),
    deliver_fix_plan(),
    #Validation & executions
    verify_single_thread_per_cycle(),
    record_automation_run(),
    governance_update(),
    create_review_cycle(),
]
