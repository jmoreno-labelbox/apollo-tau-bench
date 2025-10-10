# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
