from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateTaskCompletionStatusTool(Tool):
    """Refreshes existing records in the `checklist_items` array by marking status as 'Completed'."""

    @staticmethod
    def invoke(data: dict[str, Any], item_ids: list = None) -> str:
        if item_ids is None:
            item_ids = []
        if not item_ids:
            return _err("item_ids array is required.")

        checklist_items = data.get("checklist_items", [])
        updated_items = []

        for item_id in item_ids:
            item = next(
                (i for i in checklist_items if i.get("item_id") == item_id), None
            )
            if item:
                item["status"] = "Completed"
                item["updated_ts"] = HARD_TS
                item["reminder_sent_flag"] = False
                updated_items.append(item)
        payload = updated_items
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTaskCompletionStatus",
                "description": "Updates `checklist_items` to mark tasks as 'Completed'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["item_ids"],
                },
            },
        }
