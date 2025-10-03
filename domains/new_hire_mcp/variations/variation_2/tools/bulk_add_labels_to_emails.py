from tau_bench.envs.tool import Tool
import json
from typing import Any

class BulkAddLabelsToEmails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message_ids: list[str] = None, label_ids: list[str] = None) -> str:
        if message_ids is None:
            message_ids = []
        if label_ids is None:
            label_ids = []
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
        payload = {
                "message_ids": updated,
                "count": len(updated),
                "labels_applied": label_ids,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "bulkAddLabelsToEmails",
                "description": "Apply label_ids to multiple emails.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_ids": {"type": "array", "items": {"type": "string"}},
                        "label_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["message_ids", "label_ids"],
                },
            },
        }
