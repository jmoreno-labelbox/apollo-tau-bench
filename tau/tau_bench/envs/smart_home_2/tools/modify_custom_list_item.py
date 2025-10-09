from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ModifyCustomListItem(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], list_id: str, item: dict[str, Any], action: str = "add"
    ) -> str:
        lists = data.get("custom_lists", {}).values()
        _, lst = _find(lists, list_id)
        if not lst:
            payload = {"error": f"list '{list_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        items = lst.setdefault("items", [])
        # find an existing item using its name
        idx = next(
            (i for i, it in enumerate(items) if it["item"] == item.get("item")), None
        )
        if action == "add":
            if idx is not None:
                payload = {"error": "item already exists"}
                out = json.dumps(payload, indent=2)
                return out
            items.append(item)
        elif action == "update":
            if idx is None:
                payload = {"error": "item not found"}
                out = json.dumps(payload, indent=2)
                return out
            items[idx].update(item)
        elif action == "remove":
            if idx is None:
                payload = {"error": "item not found"}
                out = json.dumps(payload, indent=2)
                return out
            items.pop(idx)
        else:
            payload = {"error": "invalid action"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"success": f"item {action}ed", "items": items}
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ModifyCustomListItem",
                "description": "Add, update, or remove a single item in a custom list by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "string", "description": "Target list id"},
                        "item": {
                            "type": "object",
                            "description": "Item object with 'item' (name) and optional 'quantity'.",
                            "additionalProperties": True,
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "update", "remove"],
                            "description": "Operation to perform",
                        },
                    },
                    "required": ["list_id", "item", "action"],
                    "additionalProperties": False,
                },
            },
        }
