from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddLabelsToEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message_id: str, label_ids: list[str] = []) -> str:
        rows = _ensure_list(data, "emails")
        row = _find_by_key(rows, "message_id", message_id)
        if row is None:
            payload = {
                "message_id": message_id,
                "updated": False,
                "reason": "email_not_found",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        dst = row.setdefault("labels_ids", [])
        for lid in label_ids:
            if lid not in dst:
                dst.append(lid)
        payload = {"message_id": message_id, "labels_ids": dst}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddLabelsToEmail",
                "description": "Union-add label_ids onto an email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string"},
                        "label_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["message_id", "label_ids"],
                },
            },
        }
