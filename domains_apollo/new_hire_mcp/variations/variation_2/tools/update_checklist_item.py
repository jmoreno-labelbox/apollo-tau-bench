from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateChecklistItem(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_id: str = None, fields: dict[str, Any] = None) -> str:
        if fields is None:
            fields = {}
        rows = _ensure_list(data, "checklist_items")
        row = _find_by_key(rows, "item_id", item_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            row["updated_ts"] = NOW_TS
            payload = {"item_id": item_id, "updated": True, "fields": fields}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"item_id": item_id, "updated": False, "reason": "not_found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateChecklistItem",
                "description": "Update a checklist item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"},
                        "fields": {"type": "object"},
                    },
                    "required": ["item_id", "fields"],
                },
            },
        }
