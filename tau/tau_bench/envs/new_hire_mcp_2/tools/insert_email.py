# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsertEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], body, candidate_id, in_reply_to_message_id_nullable, message_id, subject, thread_id_nullable, attachments_ids = [], cc_emails = [], date_ts = NOW_TS, draft_flag = False, from_email = "hr@company.com", labels_ids = [], sent_flag = True, to_emails = []) -> str:
        rows = _ensure_list(data, "emails")
        if _find_by_key(rows, "message_id", message_id) is None:
            payload = {"message_id": message_id, "subject": subject, "body": body,
                       "from_email": from_email,
                       "to_emails": to_emails, "cc_emails": cc_emails,
                       "date_ts": date_ts, "labels_ids": labels_ids,
                       "attachments_ids": attachments_ids,
                       "draft_flag": draft_flag, "sent_flag": sent_flag,
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
