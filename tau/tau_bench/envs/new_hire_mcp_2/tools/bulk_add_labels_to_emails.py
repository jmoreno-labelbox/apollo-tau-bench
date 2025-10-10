# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
