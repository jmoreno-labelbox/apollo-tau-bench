# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTaskCompletionStatusTool(Tool):
    """Updates existing records in `checklist_items` array by setting status to 'Completed'."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        item_ids = kwargs.get("item_ids", [])
        if not item_ids:
            return _err("item_ids array is required.")

        checklist_items = data.get("checklist_items", [])
        updated_items = []

        for item_id in item_ids:
            item = next((i for i in checklist_items if i.get("item_id") == item_id), None)
            if item:
                item["status"] = "Completed"
                item["updated_ts"] = HARD_TS
                item["reminder_sent_flag"] = False
                updated_items.append(item)

        return json.dumps(updated_items, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_task_completion_status",
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
