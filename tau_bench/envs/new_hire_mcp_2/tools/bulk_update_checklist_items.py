from tau_bench.envs.tool import Tool
import json
from typing import Any

class BulkUpdateChecklistItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_ids: list = None, fields: dict = None) -> str:
        if item_ids is None:
            item_ids = []
        if fields is None:
            fields = {}
        rows = _ensure_list(data, "checklist_items")
        updated = []
        for item_id in item_ids:
            row = _find_by_key(rows, "item_id", item_id)
            if row:
                for k, v in fields.items():
                    row[k] = v
                row["updated_ts"] = NOW_TS
                updated.append(item_id)
        payload = {"updated_item_ids": updated, "count": len(updated)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BulkUpdateChecklistItems",
                "description": "Update multiple checklist items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                        "fields": {"type": "object"},
                    },
                    "required": ["item_ids", "fields"],
                },
            },
        }
