import json
from typing import Any

from tau_bench.envs.tool import Tool

TODAY = "2025-01-01"
NOW_TS = "2025-01-01T09:00:00Z"




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def _find_by_key(rows: list[dict[str, Any]], key: str, val: Any) -> dict[str, Any]:
    pass
    for r in rows:
        if r.get(key) == val:
            return r
    return None


def _slug(s: str) -> str:
    pass
    return (
        ""
        if s is None
        else "".join(ch.lower() if ch.isalnum() else "_" for ch in s.values().strip("_")
    )


def _next_seq_id(rows: list[dict[str, Any]], key: str, width: int = 4) -> str:
    pass
    mx = 0
    for r in rows:
        v = r.get(key)
        if isinstance(v, str) and v.isdigit():
            mx = max(mx, int(v))
    return str(mx + 1).zfill(width)


def _ensure_list(d: dict[str, Any], key: str) -> list[Any]:
    pass
    if key not in d or not isinstance(d[key], list):
        d[key] = []
    return d[key]


class SetCandidateFields(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, fields: dict = None) -> str:
        if fields is None:
            fields = {}
        rows = _ensure_list(data, "candidates")
        row = _find_by_key(rows, "candidate_id", candidate_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            row.setdefault("updated_ts", NOW_TS)
            payload = {"candidate_id": candidate_id, "updated": True, "fields": fields}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"candidate_id": candidate_id, "updated": False, "reason": "not_found"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetCandidateFields",
                "description": "Update fields on an existing candidate. No-op if not found.",
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


class UpdateAssetRequest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], request_id: str, fields: dict = {}) -> str:
        rows = _ensure_list(data, "asset_requests")
        row = _find_by_key(rows, "request_id", request_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            row.setdefault("updated_ts", NOW_TS)
            payload = {"request_id": request_id, "updated": True, "fields": fields}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"request_id": request_id, "updated": False, "reason": "not_found"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAssetRequest",
                "description": "Update existing asset_requests row. No-op if not found.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "fields": {"type": "object"},
                    },
                    "required": ["request_id", "fields"],
                },
            },
        }


class AssignInventoryAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_tag: str = None, candidate_id: str = None) -> str:
        rows = _ensure_list(data, "inventory_assets")
        row = _find_by_key(rows, "asset_tag", asset_tag)
        if row:
            row["assigned_candidate_id_nullable"] = candidate_id
            row["status"] = "Assigned"
            row.setdefault("updated_ts", NOW_TS)
            payload = {
                "asset_tag": asset_tag,
                "assigned": True,
                "candidate_id": candidate_id,
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"asset_tag": asset_tag, "assigned": False, "reason": "not_found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignInventoryAsset",
                "description": "Assign an inventory asset. No-op if not found.",
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


class ReleaseInventoryAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_tag: str = None) -> str:
        rows = _ensure_list(data, "inventory_assets")
        row = _find_by_key(rows, "asset_tag", asset_tag)
        if row:
            row["assigned_candidate_id_nullable"] = None
            row["status"] = "Available"
            row.setdefault("updated_ts", NOW_TS)
            payload = {"asset_tag": asset_tag, "released": True}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"asset_tag": asset_tag, "released": False, "reason": "not_found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReleaseInventoryAsset",
                "description": "Release an inventory asset. No-op if not found.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_tag": {"type": "string"}},
                    "required": ["asset_tag"],
                },
            },
        }


class UpsertOnboardingFile(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        file_path: str,
        content_text: str = "",
        mime_type: str = "text/plain",
        candidate_id: str = None
    ) -> str:
        rows = _ensure_list(data, "onboarding_files")
        row = _find_by_key(rows, "file_path", file_path)
        created = False
        if row is None:
            row = {
                "file_path": file_path,
                "content_text": content_text,
                "mime_type": mime_type,
                "created_ts": NOW_TS,
                "updated_ts": NOW_TS,
                "candidate_id": candidate_id,
            }
            rows.append(row)
            created = True
        else:
            row["content_text"] = content_text
            row["mime_type"] = mime_type
            row["candidate_id"] = candidate_id
            row["updated_ts"] = NOW_TS
        payload = {"file_path": file_path, "created": created}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertOnboardingFile",
                "description": "Create or update an onboarding_files row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {"type": "string"},
                        "content_text": {"type": "string"},
                        "mime_type": {"type": "string"},
                        "candidate_id": {"type": "string"},
                    },
                    "required": [
                        "file_path",
                        "content_text",
                        "mime_type",
                        "candidate_id",
                    ],
                },
            },
        }


class CreateOrGetEmailLabel(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str) -> str:
        rows = _ensure_list(data, "email_labels")
        for r in rows:
            if r.get("name") == name:
                payload = {"label_id": r.get("label_id"), "created": False}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        new_id = f"lbl_{_slug(name)}"
        rows.append({"label_id": new_id, "name": name})
        payload = {"label_id": new_id, "created": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOrGetEmailLabel",
                "description": "Return existing label_id by name or create deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class InsertEmail(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        message_id: str,
        subject: str = None,
        body: str = None,
        from_email: str = "hr@company.com",
        to_emails: list = None,
        cc_emails: list = None,
        date_ts: int = NOW_TS,
        labels_ids: list = None,
        attachments_ids: list = None,
        draft_flag: bool = False,
        sent_flag: bool = True,
        candidate_id: str = None,
        thread_id_nullable: str = None,
        in_reply_to_message_id_nullable: str = None
    ) -> str:
        if to_emails is None:
            to_emails = []
        if cc_emails is None:
            cc_emails = []
        if labels_ids is None:
            labels_ids = []
        if attachments_ids is None:
            attachments_ids = []

        rows = _ensure_list(data, "emails")
        if _find_by_key(rows, "message_id", message_id) is None:
            payload = {
                "message_id": message_id,
                "subject": subject,
                "body": body,
                "from_email": from_email,
                "to_emails": to_emails,
                "cc_emails": cc_emails,
                "date_ts": date_ts,
                "labels_ids": labels_ids,
                "attachments_ids": attachments_ids,
                "draft_flag": draft_flag,
                "sent_flag": sent_flag,
                "candidate_id_nullable": candidate_id,
                "thread_id_nullable": thread_id_nullable,
                "in_reply_to_message_id_nullable": in_reply_to_message_id_nullable,
            }
            rows.append(payload)
        payload = {"message_id": message_id, "created": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertEmail",
                "description": "Insert an email row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "body": {"type": "string"},
                        "to_emails": {"type": "array", "items": {"type": "string"}},
                        "candidate_id": {"type": "string"},
                        "draft_flag": {"type": "boolean"},
                        "sent_flag": {"type": "boolean"},
                    },
                    "required": [
                        "message_id",
                        "subject",
                        "body",
                        "to_emails",
                        "candidate_id",
                        "draft_flag",
                        "sent_flag",
                    ],
                },
            },
        }


class AddLabelsToEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message_id: str, label_ids: list[str] = []) -> str:
        rows = _ensure_list(data, "emails")
        row = _find_by_key(rows, "message_id", message_id)
        if row is None:
            payload = {
                "message_id": message_id,
                "updated": False,
                "reason": "email_not_found",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        dst = row.setdefault("labels_ids", [])
        for lid in label_ids:
            if lid not in dst:
                dst.append(lid)
        payload = {"message_id": message_id, "labels_ids": dst}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddLabelsToEmail",
                "description": "Union-add label_ids onto an email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string"},
                        "label_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["message_id", "label_ids"],
                },
            },
        }


class InsertAccessCheck(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, system_name: str = None, status: str = None, note_nullable: str = None, checked_ts: str = NOW_TS) -> str:
        rows = _ensure_list(data, "access_checks")
        payload = {
            "candidate_id": candidate_id,
            "system_name": system_name,
            "status": status,
            "note_nullable": note_nullable,
            "checked_ts": checked_ts,
        }
        rows.append(payload)
        payload = {"inserted": payload}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertAccessCheck",
                "description": "Append a pass/fail access check.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "system_name": {"type": "string"},
                        "status": {"type": "string"},
                        "note_nullable": {"type": "string"},
                    },
                    "required": ["candidate_id", "system_name", "status"],
                },
            },
        }


class UpdateChecklistItem(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_id: str = None, fields: dict[str, Any] = None) -> str:
        if fields is None:
            fields = {}
        rows = _ensure_list(data, "checklist_items")
        row = _find_by_key(rows, "item_id", item_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            row["updated_ts"] = NOW_TS
            payload = {"item_id": item_id, "updated": True, "fields": fields}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"item_id": item_id, "updated": False, "reason": "not_found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateChecklistItem",
                "description": "Update a checklist item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"},
                        "fields": {"type": "object"},
                    },
                    "required": ["item_id", "fields"],
                },
            },
        }


class InsertTerminalLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message_text: str = None) -> str:
        rows = _ensure_list(data, "terminal_log")
        new_id = _next_seq_id(rows, "entry_id")
        payload = {
            "entry_id": new_id,
            "message_text": message_text,
            "printed_ts": NOW_TS,
        }
        rows.append(payload)
        payload = {"entry_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertTerminalLog",
                "description": "Append an audit line to terminal_log.",
                "parameters": {
                    "type": "object",
                    "properties": {"message_text": {"type": "string"}},
                    "required": ["message_text"],
                },
            },
        }


class RecordMcpToolCall(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], server_name: str = None, tool_name: str = None, params_json: dict = {}, result_meta_json: dict = {}) -> str:
        rows = _ensure_list(data, "mcp_tool_calls")
        new_id = _next_seq_id(rows, "call_id")
        payload = {
            "call_id": new_id,
            "server_name": server_name,
            "tool_name": tool_name,
            "params_json": params_json,
            "result_meta_json": result_meta_json,
            "call_ts": NOW_TS,
        }
        rows.append(payload)
        payload = {"call_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordMcpToolCall",
                "description": "Insert an audit row for an MCP tool call.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_name": {"type": "string"},
                        "tool_name": {"type": "string"},
                        "params_json": {"type": "object"},
                        "result_meta_json": {"type": "object"},
                    },
                    "required": ["server_name", "tool_name", "params_json"],
                },
            },
        }


class InsertAttachmentRecord(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        attachment_id: str,
        message_id: str,
        filename: str,
        mime_type: str,
        file_path: str,
        size_bytes: int = 0,
        stored_ts: str = NOW_TS
    ) -> str:
        pass
        rows = _ensure_list(data, "attachments")
        payload = {
            "attachment_id": attachment_id,
            "message_id": message_id,
            "filename": filename,
            "mime_type": mime_type,
            "file_path": file_path,
            "size_bytes": size_bytes,
            "stored_ts": stored_ts,
        }
        rows.append(payload)
        payload = {"attachment_id": payload["attachment_id"], "created": True}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertAttachmentRecord",
                "description": "Insert a new attachment row bound to a message_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "attachment_id": {"type": "string"},
                        "message_id": {"type": "string"},
                        "filename": {"type": "string"},
                        "mime_type": {"type": "string"},
                        "file_path": {"type": "string"},
                        "size_bytes": {"type": "integer"},
                    },
                    "required": [
                        "attachment_id",
                        "message_id",
                        "filename",
                        "mime_type",
                        "file_path",
                    ],
                },
            },
        }


class LabelEmailByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message_id: str = None, label_name: str = None) -> str:
        el = CreateOrGetEmailLabel.invoke
        label_info = json.loads(el(data, name=label_name))
        lid = label_info.get("label_id")
        ae = AddLabelsToEmail.invoke
        res = json.loads(ae(data, message_id=message_id, label_ids=[lid]))
        payload = {
                "message_id": message_id,
                "label_id": lid,
                "labels_ids": res.get("labels_ids", []),
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
                "name": "labelEmailByName",
                "description": "Ensure a label by name exists and apply it to an email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string"},
                        "label_name": {"type": "string"},
                    },
                    "required": ["message_id", "label_name"],
                },
            },
        }


class UpdateEmailMetadata(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message_id: str = None, fields: dict[str, Any] = None) -> str:
        if fields is None:
            fields = {}
        rows = _ensure_list(data, "emails")
        row = _find_by_key(rows, "message_id", message_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            payload = {"message_id": message_id, "updated": True, "fields": fields}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"message_id": message_id, "updated": False, "reason": "email_not_found"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmailMetadata",
                "description": "Update email metadata fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string"},
                        "fields": {"type": "object"},
                    },
                    "required": ["message_id", "fields"],
                },
            },
        }


class ReserveInventoryAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_tag: str = None, candidate_id: str = None) -> str:
        rows = _ensure_list(data, "inventory_assets")
        row = _find_by_key(rows, "asset_tag", asset_tag)
        if row:
            row["assigned_candidate_id_nullable"] = candidate_id
            row["status"] = "Reserved"
            row.setdefault("updated_ts", NOW_TS)
            payload = {
                "asset_tag": asset_tag,
                "reserved": True,
                "candidate_id": candidate_id,
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"asset_tag": asset_tag, "reserved": False, "reason": "not_found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reserveInventoryAsset",
                "description": "Reserve an inventory asset for a candidate.",
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


class SetInventoryAssetFields(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_tag: str, fields: dict[str, Any] = {}) -> str:
        rows = _ensure_list(data, "inventory_assets")
        row = _find_by_key(rows, "asset_tag", asset_tag)
        if row:
            for k, v in fields.items():
                row[k] = v
            row.setdefault("updated_ts", NOW_TS)
            payload = {"asset_tag": asset_tag, "updated": True, "fields": fields}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"asset_tag": asset_tag, "updated": False, "reason": "not_found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setInventoryAssetFields",
                "description": "Update fields on an inventory asset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_tag": {"type": "string"},
                        "fields": {"type": "object"},
                    },
                    "required": ["asset_tag", "fields"],
                },
            },
        }


class LinkAssetRequestToCandidate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, request_id: str = None) -> str:
        crows = _ensure_list(data, "candidates")
        cand = _find_by_key(crows, "candidate_id", candidate_id)
        if cand:
            cand["asset_request_record_id_nullable"] = request_id
            cand.setdefault("updated_ts", NOW_TS)
            payload = {"candidate_id": candidate_id, "linked_request_id": request_id}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {
                "candidate_id": candidate_id,
                "linked_request_id": request_id,
                "updated": False,
                "reason": "not_found",
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
                "name": "LinkAssetRequestToCandidate",
                "description": "Set candidate.asset_request_record_id_nullable.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["candidate_id", "request_id"],
                },
            },
        }


class BulkUpdateChecklistItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_ids: list = None, fields: dict = None) -> str:
        if item_ids is None:
            item_ids = []
        if fields is None:
            fields = {}
        rows = _ensure_list(data, "checklist_items")
        updated = []
        for item_id in item_ids:
            row = _find_by_key(rows, "item_id", item_id)
            if row:
                for k, v in fields.items():
                    row[k] = v
                row["updated_ts"] = NOW_TS
                updated.append(item_id)
        payload = {"updated_item_ids": updated, "count": len(updated)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BulkUpdateChecklistItems",
                "description": "Update multiple checklist items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                        "fields": {"type": "object"},
                    },
                    "required": ["item_ids", "fields"],
                },
            },
        }


class CreateOrientationInviteEmail(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        message_id: str = None,
        subject: str = None,
        body: str = None,
        to_emails: list[str] = None,
        candidate_id: str = None
    ) -> str:
        if to_emails is None:
            to_emails = []
        InsertEmail.invoke(
            data,
            message_id=message_id,
            subject=subject,
            body=body,
            to_emails=to_emails,
            candidate_id=candidate_id,
            draft_flag=False,
            sent_flag=True,
        )
        le = CreateOrGetEmailLabel.invoke
        info = json.loads(le(data, name="Orientation-Invite"))
        lid = info.get("label_id")
        AddLabelsToEmail.invoke(data, message_id=message_id, label_ids=[lid])
        payload = {"message_id": message_id, "label_id": lid}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createOrientationInviteEmail",
                "description": "Create an orientation invite email and label it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "body": {"type": "string"},
                        "to_emails": {"type": "array", "items": {"type": "string"}},
                        "candidate_id": {"type": "string"},
                    },
                    "required": [
                        "message_id",
                        "subject",
                        "body",
                        "to_emails",
                        "candidate_id",
                    ],
                },
            },
        }


class CreateManagerIntroEmail(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        message_id: str = None,
        subject: str = None,
        body: str = None,
        to_emails: list = None,
        candidate_id: str = None
    ) -> str:
        if to_emails is None:
            to_emails = []
        InsertEmail.invoke(
            data,
            message_id=message_id,
            subject=subject,
            body=body,
            to_emails=to_emails,
            candidate_id=candidate_id,
            draft_flag=False,
            sent_flag=True,
        )
        le = CreateOrGetEmailLabel.invoke
        info = json.loads(le(data, name="Manager-Intro"))
        lid = info.get("label_id")
        AddLabelsToEmail.invoke(data, message_id=message_id, label_ids=[lid])
        payload = {"message_id": message_id, "label_id": lid}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createManagerIntroEmail",
                "description": "Create a manager intro email and label it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "body": {"type": "string"},
                        "to_emails": {"type": "array", "items": {"type": "string"}},
                        "candidate_id": {"type": "string"},
                    },
                    "required": [
                        "message_id",
                        "subject",
                        "body",
                        "to_emails",
                        "candidate_id",
                    ],
                },
            },
        }


class UpsertJsonArtifact(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], file_path: str = None, content_obj: dict = None, candidate_id: str = None) -> str:
        if content_obj is None:
            content_obj = {}
        text = json.dumps(content_obj, sort_keys=True)
        res = json.loads(
            UpsertOnboardingFile.invoke(
                data,
                file_path=file_path,
                content_text=text,
                mime_type="application/json",
                candidate_id=candidate_id,
            )
        )
        payload = {"file_path": file_path, "created": res.get("created", False)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertJsonArtifact",
                "description": "Create or update a JSON artifact file under onboarding_files.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {"type": "string"},
                        "content_obj": {"type": "object"},
                        "candidate_id": {"type": "string"},
                    },
                    "required": ["file_path", "content_obj", "candidate_id"],
                },
            },
        }


class CreateAccessGapSummaryFile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], file_path: str = None, content_lines: list[str] = None, candidate_id: str = None) -> str:
        if content_lines is None:
            content_lines = []
        content_text = "\n".join(content_lines) + ("\n" if content_lines else "")
        res = json.loads(
            UpsertOnboardingFile.invoke(
                data,
                file_path=file_path,
                content_text=content_text,
                mime_type="text/markdown",
                candidate_id=candidate_id,
            )
        )
        payload = {"file_path": file_path, "created": res.get("created", False)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAccessGapSummaryFile",
                "description": "Create a markdown summary file from lines.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {"type": "string"},
                        "content_lines": {"type": "array", "items": {"type": "string"}},
                        "candidate_id": {"type": "string"},
                    },
                    "required": ["file_path", "content_lines", "candidate_id"],
                },
            },
        }


class SetCandidateTimestamps(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str, fields: dict = None) -> str:
        fields = fields or {}
        rows = _ensure_list(data, "candidates")
        row = _find_by_key(rows, "candidate_id", candidate_id)
        if row:
            for k, v in fields.items():
                row[k] = v if v is not None else NOW_TS
            row.setdefault("updated_ts", NOW_TS)
            payload = {"candidate_id": candidate_id, "updated": True, "fields": fields}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"candidate_id": candidate_id, "updated": False, "reason": "not_found"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetCandidateTimestamps",
                "description": "Set timestamp fields on candidate to provided values or NOW_TS.",
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


class UpdateCandidateEmailPointers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, message_field: str = None, message_id: str = None) -> str:
        rows = _ensure_list(data, "candidates")
        row = _find_by_key(rows, "candidate_id", candidate_id)
        if row:
            row[message_field] = message_id
            row.setdefault("updated_ts", NOW_TS)
            payload = {
                "candidate_id": candidate_id,
                "field": message_field,
                "value": message_id,
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {
            "candidate_id": candidate_id,
            "field": message_field,
            "value": message_id,
            "updated": False,
            "reason": "not_found",
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
                "name": "updateCandidateEmailPointers",
                "description": "Set a candidate message pointer field to a message_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "message_field": {"type": "string"},
                        "message_id": {"type": "string"},
                    },
                    "required": ["candidate_id", "message_field", "message_id"],
                },
            },
        }


class BulkAddLabelsToEmails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message_ids: list[str] = None, label_ids: list[str] = None) -> str:
        if message_ids is None:
            message_ids = []
        if label_ids is None:
            label_ids = []
        rows = _ensure_list(data, "emails")
        updated = []
        for mid in message_ids:
            row = _find_by_key(rows, "message_id", mid)
            if row:
                dst = row.setdefault("labels_ids", [])
                for lid in label_ids:
                    if lid not in dst:
                        dst.append(lid)
                updated.append(mid)
        payload = {
                "message_ids": updated,
                "count": len(updated),
                "labels_applied": label_ids,
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
                "name": "bulkAddLabelsToEmails",
                "description": "Apply label_ids to multiple emails.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_ids": {"type": "array", "items": {"type": "string"}},
                        "label_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["message_ids", "label_ids"],
                },
            },
        }


TOOLS = [
    SetCandidateFields(),
    UpdateAssetRequest(),
    AssignInventoryAsset(),
    ReleaseInventoryAsset(),
    UpsertOnboardingFile(),
    CreateOrGetEmailLabel(),
    InsertEmail(),
    AddLabelsToEmail(),
    InsertAccessCheck(),
    UpdateChecklistItem(),
    InsertTerminalLog(),
    RecordMcpToolCall(),
    InsertAttachmentRecord(),
    LabelEmailByName(),
    UpdateEmailMetadata(),
    ReserveInventoryAsset(),
    SetInventoryAssetFields(),
    LinkAssetRequestToCandidate(),
    BulkUpdateChecklistItems(),
    CreateOrientationInviteEmail(),
    CreateManagerIntroEmail(),
    UpsertJsonArtifact(),
    CreateAccessGapSummaryFile(),
    SetCandidateTimestamps(),
    UpdateCandidateEmailPointers(),
    BulkAddLabelsToEmails(),
]
