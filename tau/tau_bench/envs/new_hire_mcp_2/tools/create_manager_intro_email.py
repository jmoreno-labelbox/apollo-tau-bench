# Sierra Copyright

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

class CreateManagerIntroEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], body, candidate_id, message_id, subject, to_emails = []) -> str:
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