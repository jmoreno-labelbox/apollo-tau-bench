from domains.dto import Tool
from typing import Dict, Any, List
import json

TODAY = "2025-01-01"
NOW_TS = "2025-01-01T09:00:00Z"


def _slug(s: str) -> str:
    return "" if s is None else "".join(ch.lower() if ch.isalnum() else "_" for ch in s).strip("_")


def _ensure_list(d: Dict[str, Any], key: str) -> List[Any]:
    if key not in d or not isinstance(d[key], list):
        d[key] = []
    return d[key]


def _find_by_key(rows: List[Dict[str, Any]], key: str, val: Any) -> Dict[str, Any]:
    for r in rows:
        if r.get(key) == val:
            return r
    return None


def _next_seq_id(rows: List[Dict[str, Any]], key: str, width: int = 4) -> str:
    mx = 0
    for r in rows:
        v = r.get(key)
        if isinstance(v, str) and v.isdigit():
            mx = max(mx, int(v))
    return str(mx + 1).zfill(width)


class SetCandidateFields(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        fields = kwargs.get("fields", {})
        rows = _ensure_list(data, "candidates")
        row = _find_by_key(rows, "candidate_id", candidate_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"candidate_id": candidate_id, "updated": True, "fields": fields}, indent=2)
        return json.dumps({"candidate_id": candidate_id, "updated": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "set_candidate_fields",
                                                 "description": "Update fields on an existing candidate. No-op if not found.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"candidate_id": {"type": "string"},
                                                                               "fields": {"type": "object"}},
                                                                "required": ["candidate_id", "fields"]}}}


class UpdateAssetRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        fields = kwargs.get("fields", {})
        rows = _ensure_list(data, "asset_requests")
        row = _find_by_key(rows, "request_id", request_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"request_id": request_id, "updated": True, "fields": fields}, indent=2)
        return json.dumps({"request_id": request_id, "updated": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_asset_request",
                                                 "description": "Update existing asset_requests row. No-op if not found.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"request_id": {"type": "string"},
                                                                               "fields": {"type": "object"}},
                                                                "required": ["request_id", "fields"]}}}


class AssignInventoryAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_tag = kwargs.get("asset_tag")
        candidate_id = kwargs.get("candidate_id")
        rows = _ensure_list(data, "inventory_assets")
        row = _find_by_key(rows, "asset_tag", asset_tag)
        if row:
            row["assigned_candidate_id_nullable"] = candidate_id
            row["status"] = "Assigned"
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"asset_tag": asset_tag, "assigned": True, "candidate_id": candidate_id}, indent=2)
        return json.dumps({"asset_tag": asset_tag, "assigned": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "assign_inventory_asset",
                                                 "description": "Assign an inventory asset. No-op if not found.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"asset_tag": {"type": "string"},
                                                                               "candidate_id": {"type": "string"}},
                                                                "required": ["asset_tag", "candidate_id"]}}}


class ReleaseInventoryAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_tag = kwargs.get("asset_tag")
        rows = _ensure_list(data, "inventory_assets")
        row = _find_by_key(rows, "asset_tag", asset_tag)
        if row:
            row["assigned_candidate_id_nullable"] = None
            row["status"] = "Available"
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"asset_tag": asset_tag, "released": True}, indent=2)
        return json.dumps({"asset_tag": asset_tag, "released": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "release_inventory_asset",
                                                 "description": "Release an inventory asset. No-op if not found.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"asset_tag": {"type": "string"}},
                                                                "required": ["asset_tag"]}}}


class UpsertOnboardingFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        file_path = kwargs.get("file_path")
        content_text = kwargs.get("content_text", "")
        mime_type = kwargs.get("mime_type", "text/plain")
        candidate_id = kwargs.get("candidate_id")
        rows = _ensure_list(data, "onboarding_files")
        row = _find_by_key(rows, "file_path", file_path)
        created = False
        if row is None:
            row = {"file_path": file_path, "content_text": content_text, "mime_type": mime_type, "created_ts": NOW_TS,
                   "updated_ts": NOW_TS, "candidate_id": candidate_id}
            rows.append(row)
            created = True
        else:
            row["content_text"] = content_text
            row["mime_type"] = mime_type
            row["candidate_id"] = candidate_id
            row["updated_ts"] = NOW_TS
        return json.dumps({"file_path": file_path, "created": created}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "upsert_onboarding_file",
                                                 "description": "Create or update an onboarding_files row.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"file_path": {"type": "string"},
                                                                               "content_text": {"type": "string"},
                                                                               "mime_type": {"type": "string"},
                                                                               "candidate_id": {"type": "string"}},
                                                                "required": ["file_path", "content_text", "mime_type",
                                                                             "candidate_id"]}}}


class CreateOrGetEmailLabel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")
        rows = _ensure_list(data, "email_labels")
        for r in rows:
            if r.get("name") == name:
                return json.dumps({"label_id": r.get("label_id"), "created": False}, indent=2)
        new_id = f"lbl_{_slug(name)}"
        rows.append({"label_id": new_id, "name": name})
        return json.dumps({"label_id": new_id, "created": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_or_get_email_label",
                                                 "description": "Return existing label_id by name or create deterministically.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"name": {"type": "string"}},
                                                                "required": ["name"]}}}


class InsertEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        message_id = kwargs.get("message_id")
        rows = _ensure_list(data, "emails")
        if _find_by_key(rows, "message_id", message_id) is None:
            payload = {"message_id": message_id, "subject": kwargs.get("subject"), "body": kwargs.get("body"),
                       "from_email": kwargs.get("from_email", "hr@company.com"),
                       "to_emails": kwargs.get("to_emails", []), "cc_emails": kwargs.get("cc_emails", []),
                       "date_ts": kwargs.get("date_ts", NOW_TS), "labels_ids": kwargs.get("labels_ids", []),
                       "attachments_ids": kwargs.get("attachments_ids", []),
                       "draft_flag": kwargs.get("draft_flag", False), "sent_flag": kwargs.get("sent_flag", True),
                       "candidate_id_nullable": kwargs.get("candidate_id"),
                       "thread_id_nullable": kwargs.get("thread_id_nullable"),
                       "in_reply_to_message_id_nullable": kwargs.get("in_reply_to_message_id_nullable")}
            rows.append(payload)
        return json.dumps({"message_id": message_id, "created": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "insert_email", "description": "Insert an email row.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"message_id": {"type": "string"},
                                                                               "subject": {"type": "string"},
                                                                               "body": {"type": "string"},
                                                                               "to_emails": {"type": "array", "items": {
                                                                                   "type": "string"}},
                                                                               "candidate_id": {"type": "string"},
                                                                               "draft_flag": {"type": "boolean"},
                                                                               "sent_flag": {"type": "boolean"}},
                                                                "required": ["message_id", "subject", "body",
                                                                             "to_emails", "candidate_id", "draft_flag",
                                                                             "sent_flag"]}}}


class AddLabelsToEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        message_id = kwargs.get("message_id")
        label_ids = kwargs.get("label_ids", [])
        rows = _ensure_list(data, "emails")
        row = _find_by_key(rows, "message_id", message_id)
        if row is None:
            return json.dumps({"message_id": message_id, "updated": False, "reason": "email_not_found"}, indent=2)
        dst = row.setdefault("labels_ids", [])
        for lid in label_ids:
            if lid not in dst:
                dst.append(lid)
        return json.dumps({"message_id": message_id, "labels_ids": dst}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "add_labels_to_email", "description": "Union-add label_ids onto an email.",
                             "parameters": {"type": "object", "properties": {"message_id": {"type": "string"},
                                                                             "label_ids": {"type": "array", "items": {
                                                                                 "type": "string"}}},
                                            "required": ["message_id", "label_ids"]}}}


class InsertAccessCheck(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = _ensure_list(data, "access_checks")
        payload = {"candidate_id": kwargs.get("candidate_id"), "system_name": kwargs.get("system_name"),
                   "status": kwargs.get("status"), "note_nullable": kwargs.get("note_nullable"),
                   "checked_ts": kwargs.get("checked_ts", NOW_TS)}
        rows.append(payload)
        return json.dumps({"inserted": payload}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "insert_access_check", "description": "Append a pass/fail access check.",
                             "parameters": {"type": "object", "properties": {"candidate_id": {"type": "string"},
                                                                             "system_name": {"type": "string"},
                                                                             "status": {"type": "string"},
                                                                             "note_nullable": {"type": "string"}},
                                            "required": ["candidate_id", "system_name", "status"]}}}


class UpdateChecklistItem(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        item_id = kwargs.get("item_id")
        fields = kwargs.get("fields", {})
        rows = _ensure_list(data, "checklist_items")
        row = _find_by_key(rows, "item_id", item_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            row["updated_ts"] = NOW_TS
            return json.dumps({"item_id": item_id, "updated": True, "fields": fields}, indent=2)
        return json.dumps({"item_id": item_id, "updated": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "update_checklist_item", "description": "Update a checklist item.",
                             "parameters": {"type": "object",
                                            "properties": {"item_id": {"type": "string"}, "fields": {"type": "object"}},
                                            "required": ["item_id", "fields"]}}}


class InsertTerminalLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = _ensure_list(data, "terminal_log")
        new_id = _next_seq_id(rows, "entry_id")
        payload = {"entry_id": new_id, "message_text": kwargs.get("message_text"), "printed_ts": NOW_TS}
        rows.append(payload)
        return json.dumps({"entry_id": new_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "insert_terminal_log", "description": "Append an audit line to terminal_log.",
                             "parameters": {"type": "object", "properties": {"message_text": {"type": "string"}},
                                            "required": ["message_text"]}}}


class RecordMcpToolCall(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = _ensure_list(data, "mcp_tool_calls")
        new_id = _next_seq_id(rows, "call_id")
        payload = {"call_id": new_id, "server_name": kwargs.get("server_name"), "tool_name": kwargs.get("tool_name"),
                   "params_json": kwargs.get("params_json", {}), "result_meta_json": kwargs.get("result_meta_json", {}),
                   "call_ts": NOW_TS}
        rows.append(payload)
        return json.dumps({"call_id": new_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "record_mcp_tool_call", "description": "Insert an audit row for an MCP tool call.",
                             "parameters": {"type": "object", "properties": {"server_name": {"type": "string"},
                                                                             "tool_name": {"type": "string"},
                                                                             "params_json": {"type": "object"},
                                                                             "result_meta_json": {"type": "object"}},
                                            "required": ["server_name", "tool_name", "params_json"]}}}


class InsertAttachmentRecord(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = _ensure_list(data, "attachments")
        payload = {"attachment_id": kwargs.get("attachment_id"), "message_id": kwargs.get("message_id"),
                   "filename": kwargs.get("filename"), "mime_type": kwargs.get("mime_type"),
                   "file_path": kwargs.get("file_path"), "size_bytes": kwargs.get("size_bytes", 0),
                   "stored_ts": kwargs.get("stored_ts", NOW_TS)}
        rows.append(payload)
        return json.dumps({"attachment_id": payload["attachment_id"], "created": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "insert_attachment_record",
                                                 "description": "Insert a new attachment row bound to a message_id.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"attachment_id": {"type": "string"},
                                                                               "message_id": {"type": "string"},
                                                                               "filename": {"type": "string"},
                                                                               "mime_type": {"type": "string"},
                                                                               "file_path": {"type": "string"},
                                                                               "size_bytes": {"type": "integer"}},
                                                                "required": ["attachment_id", "message_id", "filename",
                                                                             "mime_type", "file_path"]}}}


class LabelEmailByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        message_id = kwargs.get("message_id")
        label_name = kwargs.get("label_name")
        el = CreateOrGetEmailLabel.invoke
        label_info = json.loads(el(data, name=label_name))
        lid = label_info.get("label_id")
        ae = AddLabelsToEmail.invoke
        res = json.loads(ae(data, message_id=message_id, label_ids=[lid]))
        return json.dumps({"message_id": message_id, "label_id": lid, "labels_ids": res.get("labels_ids", [])},
                          indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "label_email_by_name",
                                                 "description": "Ensure a label by name exists and apply it to an email.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"message_id": {"type": "string"},
                                                                               "label_name": {"type": "string"}},
                                                                "required": ["message_id", "label_name"]}}}


class UpdateEmailMetadata(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        message_id = kwargs.get("message_id")
        fields = kwargs.get("fields", {})
        rows = _ensure_list(data, "emails")
        row = _find_by_key(rows, "message_id", message_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            return json.dumps({"message_id": message_id, "updated": True, "fields": fields}, indent=2)
        return json.dumps({"message_id": message_id, "updated": False, "reason": "email_not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "update_email_metadata", "description": "Update email metadata fields.",
                             "parameters": {"type": "object", "properties": {"message_id": {"type": "string"},
                                                                             "fields": {"type": "object"}},
                                            "required": ["message_id", "fields"]}}}


class ReserveInventoryAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_tag = kwargs.get("asset_tag")
        candidate_id = kwargs.get("candidate_id")
        rows = _ensure_list(data, "inventory_assets")
        row = _find_by_key(rows, "asset_tag", asset_tag)
        if row:
            row["assigned_candidate_id_nullable"] = candidate_id
            row["status"] = "Reserved"
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"asset_tag": asset_tag, "reserved": True, "candidate_id": candidate_id}, indent=2)
        return json.dumps({"asset_tag": asset_tag, "reserved": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "reserve_inventory_asset",
                                                 "description": "Reserve an inventory asset for a candidate.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"asset_tag": {"type": "string"},
                                                                               "candidate_id": {"type": "string"}},
                                                                "required": ["asset_tag", "candidate_id"]}}}


class SetInventoryAssetFields(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_tag = kwargs.get("asset_tag")
        fields = kwargs.get("fields", {})
        rows = _ensure_list(data, "inventory_assets")
        row = _find_by_key(rows, "asset_tag", asset_tag)
        if row:
            for k, v in fields.items():
                row[k] = v
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"asset_tag": asset_tag, "updated": True, "fields": fields}, indent=2)
        return json.dumps({"asset_tag": asset_tag, "updated": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "set_inventory_asset_fields",
                                                 "description": "Update fields on an inventory asset.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"asset_tag": {"type": "string"},
                                                                               "fields": {"type": "object"}},
                                                                "required": ["asset_tag", "fields"]}}}


class LinkAssetRequestToCandidate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        request_id = kwargs.get("request_id")
        crows = _ensure_list(data, "candidates")
        cand = _find_by_key(crows, "candidate_id", candidate_id)
        if cand:
            cand["asset_request_record_id_nullable"] = request_id
            cand.setdefault("updated_ts", NOW_TS)
            return json.dumps({"candidate_id": candidate_id, "linked_request_id": request_id}, indent=2)
        return json.dumps(
            {"candidate_id": candidate_id, "linked_request_id": request_id, "updated": False, "reason": "not_found"},
            indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "link_asset_request_to_candidate",
                                                 "description": "Set candidate.asset_request_record_id_nullable.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"candidate_id": {"type": "string"},
                                                                               "request_id": {"type": "string"}},
                                                                "required": ["candidate_id", "request_id"]}}}


class BulkUpdateChecklistItems(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        item_ids = kwargs.get("item_ids", [])
        fields = kwargs.get("fields", {})
        rows = _ensure_list(data, "checklist_items")
        updated = []
        for item_id in item_ids:
            row = _find_by_key(rows, "item_id", item_id)
            if row:
                for k, v in fields.items():
                    row[k] = v
                row["updated_ts"] = NOW_TS
                updated.append(item_id)
        return json.dumps({"updated_item_ids": updated, "count": len(updated)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "bulk_update_checklist_items", "description": "Update multiple checklist items.",
                             "parameters": {"type": "object",
                                            "properties": {"item_ids": {"type": "array", "items": {"type": "string"}},
                                                           "fields": {"type": "object"}},
                                            "required": ["item_ids", "fields"]}}}


class CreateOrientationInviteEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        message_id = kwargs.get("message_id")
        subject = kwargs.get("subject")
        body = kwargs.get("body")
        to_emails = kwargs.get("to_emails", [])
        candidate_id = kwargs.get("candidate_id")
        InsertEmail.invoke(data, message_id=message_id, subject=subject, body=body, to_emails=to_emails,
                           candidate_id=candidate_id, draft_flag=False, sent_flag=True)
        le = CreateOrGetEmailLabel.invoke
        info = json.loads(le(data, name="Orientation-Invite"))
        lid = info.get("label_id")
        AddLabelsToEmail.invoke(data, message_id=message_id, label_ids=[lid])
        return json.dumps({"message_id": message_id, "label_id": lid}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_orientation_invite_email",
                                                 "description": "Create an orientation invite email and label it.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"message_id": {"type": "string"},
                                                                               "subject": {"type": "string"},
                                                                               "body": {"type": "string"},
                                                                               "to_emails": {"type": "array", "items": {
                                                                                   "type": "string"}},
                                                                               "candidate_id": {"type": "string"}},
                                                                "required": ["message_id", "subject", "body",
                                                                             "to_emails", "candidate_id"]}}}


class CreateManagerIntroEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        message_id = kwargs.get("message_id")
        subject = kwargs.get("subject")
        body = kwargs.get("body")
        to_emails = kwargs.get("to_emails", [])
        candidate_id = kwargs.get("candidate_id")
        InsertEmail.invoke(data, message_id=message_id, subject=subject, body=body, to_emails=to_emails,
                           candidate_id=candidate_id, draft_flag=False, sent_flag=True)
        le = CreateOrGetEmailLabel.invoke
        info = json.loads(le(data, name="Manager-Intro"))
        lid = info.get("label_id")
        AddLabelsToEmail.invoke(data, message_id=message_id, label_ids=[lid])
        return json.dumps({"message_id": message_id, "label_id": lid}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_manager_intro_email",
                                                 "description": "Create a manager intro email and label it.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"message_id": {"type": "string"},
                                                                               "subject": {"type": "string"},
                                                                               "body": {"type": "string"},
                                                                               "to_emails": {"type": "array", "items": {
                                                                                   "type": "string"}},
                                                                               "candidate_id": {"type": "string"}},
                                                                "required": ["message_id", "subject", "body",
                                                                             "to_emails", "candidate_id"]}}}


class UpsertJsonArtifact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        file_path = kwargs.get("file_path")
        content_obj = kwargs.get("content_obj", {})
        candidate_id = kwargs.get("candidate_id")
        text = json.dumps(content_obj, sort_keys=True)
        res = json.loads(
            UpsertOnboardingFile.invoke(data, file_path=file_path, content_text=text, mime_type="application/json",
                                        candidate_id=candidate_id))
        return json.dumps({"file_path": file_path, "created": res.get("created", False)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "upsert_json_artifact",
                                                 "description": "Create or update a JSON artifact file under onboarding_files.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"file_path": {"type": "string"},
                                                                               "content_obj": {"type": "object"},
                                                                               "candidate_id": {"type": "string"}},
                                                                "required": ["file_path", "content_obj",
                                                                             "candidate_id"]}}}


class CreateAccessGapSummaryFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        file_path = kwargs.get("file_path")
        lines = kwargs.get("content_lines", [])
        candidate_id = kwargs.get("candidate_id")
        content_text = "\n".join(lines) + ("\n" if lines else "")
        res = json.loads(
            UpsertOnboardingFile.invoke(data, file_path=file_path, content_text=content_text, mime_type="text/markdown",
                                        candidate_id=candidate_id))
        return json.dumps({"file_path": file_path, "created": res.get("created", False)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_access_gap_summary_file",
                                                 "description": "Create a markdown summary file from lines.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"file_path": {"type": "string"},
                                                                               "content_lines": {"type": "array",
                                                                                                 "items": {
                                                                                                     "type": "string"}},
                                                                               "candidate_id": {"type": "string"}},
                                                                "required": ["file_path", "content_lines",
                                                                             "candidate_id"]}}}


class SetCandidateTimestamps(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        fields = kwargs.get("fields", {})
        rows = _ensure_list(data, "candidates")
        row = _find_by_key(rows, "candidate_id", candidate_id)
        if row:
            for k, v in fields.items():
                row[k] = v if v is not None else NOW_TS
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"candidate_id": candidate_id, "updated": True, "fields": fields}, indent=2)
        return json.dumps({"candidate_id": candidate_id, "updated": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "set_candidate_timestamps",
                                                 "description": "Set timestamp fields on candidate to provided values or NOW_TS.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"candidate_id": {"type": "string"},
                                                                               "fields": {"type": "object"}},
                                                                "required": ["candidate_id", "fields"]}}}


class UpdateCandidateEmailPointers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        message_field = kwargs.get("message_field")
        message_id = kwargs.get("message_id")
        rows = _ensure_list(data, "candidates")
        row = _find_by_key(rows, "candidate_id", candidate_id)
        if row:
            row[message_field] = message_id
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"candidate_id": candidate_id, "field": message_field, "value": message_id}, indent=2)
        return json.dumps({"candidate_id": candidate_id, "field": message_field, "value": message_id, "updated": False,
                           "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_candidate_email_pointers",
                                                 "description": "Set a candidate message pointer field to a message_id.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"candidate_id": {"type": "string"},
                                                                               "message_field": {"type": "string"},
                                                                               "message_id": {"type": "string"}},
                                                                "required": ["candidate_id", "message_field",
                                                                             "message_id"]}}}


class BulkAddLabelsToEmails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        message_ids = kwargs.get("message_ids", [])
        label_ids = kwargs.get("label_ids", [])
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
        return json.dumps({"message_ids": updated, "count": len(updated), "labels_applied": label_ids}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "bulk_add_labels_to_emails", "description": "Apply label_ids to multiple emails.",
                             "parameters": {"type": "object", "properties": {
                                 "message_ids": {"type": "array", "items": {"type": "string"}},
                                 "label_ids": {"type": "array", "items": {"type": "string"}}},
                                            "required": ["message_ids", "label_ids"]}}}


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
