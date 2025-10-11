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

class LabelEmailByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], label_name, message_id) -> str:
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