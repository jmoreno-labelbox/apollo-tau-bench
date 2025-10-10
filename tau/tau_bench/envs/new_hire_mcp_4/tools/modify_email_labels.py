# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ModifyEmailLabels(Tool):
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
