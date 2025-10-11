# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
def _ensure_list(d: Dict[str, Any], key: str) -> List[Any]:
    if key not in d or not isinstance(d[key], list):
        d[key] = []
    return d[key]


def _slug(s: str) -> str:
    return "" if s is None else "".join(ch.lower() if ch.isalnum() else "_" for ch in s).strip("_")


def _find_by_key(rows: List[Dict[str, Any]], key: str, val: Any) -> Dict[str, Any]:
    for r in rows:
        if r.get(key) == val:
            return r
    return None


class InsertEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], attachments_ids=None, body=None, candidate_id=None, cc_emails=None, date_ts=None, draft_flag=None, from_email=None, in_reply_to_message_id_nullable=None, label_ids=None, labels_ids=None, message_id=None, name=None, sent_flag=None, subject=None, thread_id_nullable=None, to_emails=None) -> str:
        message_id = message_id
        rows = _ensure_list(data, "emails")
        if _find_by_key(rows, "message_id", message_id) is None:
            payload = {"message_id": message_id, "subject": subject, "body": body,
                       "from_email": (from_email if from_email is not None else "hr@company.com"),
                       "to_emails": (to_emails if to_emails is not None else []), "cc_emails": (cc_emails if cc_emails is not None else []),
                       "date_ts": (date_ts if date_ts is not None else NOW_TS), "labels_ids": (labels_ids if labels_ids is not None else []),
                       "attachments_ids": (attachments_ids if attachments_ids is not None else []),
                       "draft_flag": (draft_flag if draft_flag is not None else False), "sent_flag": (sent_flag if sent_flag is not None else True),
                       "candidate_id_nullable": candidate_id,
                       "thread_id_nullable": thread_id_nullable,
                       "in_reply_to_message_id_nullable": in_reply_to_message_id_nullable}
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

class CreateOrGetEmailLabel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        name = name
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

class AddLabelsToEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        message_id = message_id
        label_ids = (label_ids if label_ids is not None else [])
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

class CreateOrientationInviteEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], body, candidate_id, message_id, subject, to_emails = []) -> str:
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