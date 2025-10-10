# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ManageListItems(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], list_id: str, action: str, items: List[str], quantities: Dict[str, int]) -> str:
        target = next((l for l in list(data.get("custom_lists", {}).values()) if l["list_id"] == list_id), None)
        if not target:
            return json.dumps({"error": "List not found"}, indent=2)
        if action == "list":
            return json.dumps({"items": target["items"]}, indent=2)
        if action == "add_items":
            if not items:
                return json.dumps({"error": "items array required"}, indent=2)
            target["items"].extend([{"item": item, "quantity": 1} for item in items])
        elif action == "remove_items":
            if not items:
                return json.dumps({"error": "items array required"}, indent=2)
            target["items"] = [itm for itm in target["items"] if itm["item"] not in items]
        elif action == "set_quantity":
            updates: Dict[str, int] = quantities
            for itm in target["items"]:
                if itm["item"] in updates:
                    itm["quantity"] = updates[itm["item"]]
        else:
            return json.dumps({"error": "Unsupported action"}, indent=2)
        target["updated_at"] = _now_iso()
        return json.dumps({"success": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_list_items",
                "description": "Add, remove, list, or update quantities of items in a custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {"type": "string", "description": "List identifier."},
                        "action": {"type": "string", "enum": ["list", "add_items (requires items) (default quantity 1)", "remove_items (requires items)", "set_quantity (requires quantities)"]},
                        "items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "For add/remove actions: array of item names",
                        },
                        "quantities": {"type": "object", "description": "Mapping of item name → new quantity for set_quantity."},
                    },
                    "required": ["list_id", "action"],
                    "additionalProperties": False,
                },
            },
        }
