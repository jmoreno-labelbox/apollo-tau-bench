# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ModifyCustomListItem(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: str, item: Dict[str, Any], action: str = "add") -> str:
        lists = data.get("custom_lists", [])
        _, lst = _find(lists, list_id)
        if not lst:
            return json.dumps({"error": f"list '{list_id}' not found"}, indent=2)
        items = lst.setdefault("items", [])
        # locate existing item by name
        idx = next((i for i, it in enumerate(items) if it["item"] == item.get("item")), None)
        if action == "add":
            if idx is not None:
                return json.dumps({"error": "item already exists"}, indent=2)
            items.append(item)
        elif action == "update":
            if idx is None:
                return json.dumps({"error": "item not found"}, indent=2)
            items[idx].update(item)
        elif action == "remove":
            if idx is None:
                return json.dumps({"error": "item not found"}, indent=2)
            items.pop(idx)
        else:
            return json.dumps({"error": "invalid action"}, indent=2)
        return json.dumps({"success": f"item {action}ed", "items": items}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_custom_list_item",
                "description": "Add, update, or remove a single item in a custom list by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "string", "description": "Target list id"},
                        "item": {
                            "type": "object",
                            "description": "Item object with 'item' (name) and optional 'quantity'.",
                            "additionalProperties": True
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "update", "remove"],
                            "description": "Operation to perform"
                        }
                    },
                    "required": ["list_id", "item", "action"],
                    "additionalProperties": False
                }
            }
        }
