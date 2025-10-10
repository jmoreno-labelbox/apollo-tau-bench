# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateEmailMetadata(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], message_id, fields = {}) -> str:
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
