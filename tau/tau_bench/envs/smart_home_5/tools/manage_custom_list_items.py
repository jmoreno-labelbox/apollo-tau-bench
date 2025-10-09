from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ManageCustomListItems(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], list_id: str, item: dict[str, Any], action: str
    ) -> str:
        custom_lists = data.get("custom_lists", [])
        list_found = False
        for l in custom_lists:
            if l.get("list_id") == list_id:
                list_found = True
                items = l.setdefault("items", [])
                if action == "add":
                    items.append(item)
                    payload = {"success": f"Item added to list '{list_id}'."}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                elif action == "remove":
                    initial_len = len(items)
                    items[:] = [i for i in items if i.get("item") != item.get("item")]
                    if len(items) < initial_len:
                        payload = {"success": f"Item removed from list '{list_id}'."}
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                    else:
                        payload = {"error": f"Item not found in list '{list_id}'."}
                        out = json.dumps(
                            payload, indent=2
                        )
                        return out
                else:
                    payload = {"error": "Invalid action. Use 'add' or 'remove'."}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out

        if not list_found:
            payload = {"error": f"List with ID '{list_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"error": "An unexpected error occurred."}
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageCustomListItems",
                "description": "Add or remove items from a custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The ID of the list to modify.",
                        },
                        "item": {
                            "type": "object",
                            "description": "The item to add or remove. For removal, only the 'item' name is needed.",
                            "properties": {
                                "item": {"type": "string"},
                                "quantity": {"type": "integer"},
                            },
                            "required": ["item"],
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "remove"],
                            "description": "The action to perform.",
                        },
                    },
                    "required": ["list_id", "item", "action"],
                    "additionalProperties": False,
                },
            },
        }
