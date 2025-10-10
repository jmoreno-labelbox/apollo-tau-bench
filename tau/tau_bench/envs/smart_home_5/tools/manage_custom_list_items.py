# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ManageCustomListItems(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id: str, item: Dict[str, Any], action: str) -> str:
        custom_lists = data.get('custom_lists', [])
        list_found = False
        for l in custom_lists:
            if l.get('list_id') == list_id:
                list_found = True
                items = l.setdefault('items', [])
                if action == 'add':
                    items.append(item)
                    return json.dumps({"success": f"Item added to list '{list_id}'."}, indent=2)
                elif action == 'remove':
                    initial_len = len(items)
                    items[:] = [i for i in items if i.get('item') != item.get('item')]
                    if len(items) < initial_len:
                        return json.dumps({"success": f"Item removed from list '{list_id}'."}, indent=2)
                    else:
                        return json.dumps({"error": f"Item not found in list '{list_id}'."}, indent=2)
                else:
                    return json.dumps({"error": "Invalid action. Use 'add' or 'remove'."}, indent=2)

        if not list_found:
            return json.dumps({"error": f"List with ID '{list_id}' not found."}, indent=2)
        return json.dumps({"error": "An unexpected error occurred."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_custom_list_items",
                "description": "Add or remove items from a custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "The ID of the list to modify."
                        },
                        "item": {
                            "type": "object",
                            "description": "The item to add or remove. For removal, only the 'item' name is needed.",
                             "properties": {
                                "item": {"type": "string"},
                                "quantity": {"type": "integer"}
                            },
                            "required": ["item"]
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "remove"],
                            "description": "The action to perform."
                        }
                    },
                    "required": ["list_id", "item", "action"],
                    "additionalProperties": False
                }
            }
        }
