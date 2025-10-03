from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateEmailMetadata(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message_id: str = None, fields: dict[str, Any] = None) -> str:
        if fields is None:
            fields = {}
        rows = _ensure_list(data, "emails")
        row = _find_by_key(rows, "message_id", message_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            payload = {"message_id": message_id, "updated": True, "fields": fields}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"message_id": message_id, "updated": False, "reason": "email_not_found"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmailMetadata",
                "description": "Update email metadata fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {"type": "string"},
                        "fields": {"type": "object"},
                    },
                    "required": ["message_id", "fields"],
                },
            },
        }
