from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AddChecklistItem(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item: dict = None) -> str:
        new_item = item or {}
        items = data.get("checklist_items", [])
        items.append(new_item)
        data["checklist_items"] = items
        payload = {"added_item": new_item}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addChecklistItem",
                "description": "Add a new checklist item.",
                "parameters": {
                    "type": "object",
                    "properties": {"item": {"type": "object"}},
                    "required": ["item"],
                },
            },
        }
