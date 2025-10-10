# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddLabelsToEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], message_id, label_ids = []) -> str:
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
