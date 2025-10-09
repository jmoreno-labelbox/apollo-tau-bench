from tau_bench.envs.tool import Tool
import json
from typing import Any

class ManageListItems(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        list_id: str,
        action: str,
        items: list[str],
        quantities: dict[str, int]
    ) -> str:
        target = next(
            (l for l in data.get("custom_lists", []) if l["list_id"] == list_id), None
        )
        if not target:
            payload = {"error": "List not found"}
            out = json.dumps(payload, indent=2)
            return out
        if action == "list":
            payload = {"items": target["items"]}
            out = json.dumps(payload, indent=2)
            return out
        if action == "add_items":
            if not items:
                payload = {"error": "items array required"}
                out = json.dumps(payload, indent=2)
                return out
            target["items"].extend([{"item": item, "quantity": 1} for item in items])
        elif action == "remove_items":
            if not items:
                payload = {"error": "items array required"}
                out = json.dumps(payload, indent=2)
                return out
            target["items"] = [
                itm for itm in target["items"] if itm["item"] not in items
            ]
        elif action == "set_quantity":
            updates: dict[str, int] = quantities
            for itm in target["items"]:
                if itm["item"] in updates:
                    itm["quantity"] = updates[itm["item"]]
        else:
            payload = {"error": "Unsupported action"}
            out = json.dumps(payload, indent=2)
            return out
        target["updated_at"] = _now_iso()
        payload = {"success": True}
        out = json.dumps(payload, indent=2)
        return out
        pass
        target = next(
            (l for l in data.get("custom_lists", []) if l["list_id"] == list_id), None
        )
        if not target:
            payload = {"error": "List not found"}
            out = json.dumps(payload, indent=2)
            return out
        if action == "list":
            payload = {"items": target["items"]}
            out = json.dumps(payload, indent=2)
            return out
        if action == "add_items":
            if not items:
                payload = {"error": "items array required"}
                out = json.dumps(payload, indent=2)
                return out
            target["items"].extend([{"item": item, "quantity": 1} for item in items])
        elif action == "remove_items":
            if not items:
                payload = {"error": "items array required"}
                out = json.dumps(payload, indent=2)
                return out
            target["items"] = [
                itm for itm in target["items"] if itm["item"] not in items
            ]
        elif action == "set_quantity":
            updates: dict[str, int] = quantities
            for itm in target["items"]:
                if itm["item"] in updates:
                    itm["quantity"] = updates[itm["item"]]
        else:
            payload = {"error": "Unsupported action"}
            out = json.dumps(payload, indent=2)
            return out
        target["updated_at"] = _now_iso()
        payload = {"success": True}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manageListItems",
                "description": "Add, remove, list, or update quantities of items in a custom list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_id": {
                            "type": "string",
                            "description": "List identifier.",
                        },
                        "action": {
                            "type": "string",
                            "enum": [
                                "list",
                                "add_items (requires items) (default quantity 1)",
                                "remove_items (requires items)",
                                "set_quantity (requires quantities)",
                            ],
                        },
                        "items": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "For add/remove actions: array of item names",
                        },
                        "quantities": {
                            "type": "object",
                            "description": "Mapping of item name → new quantity for set_quantity.",
                        },
                    },
                    "required": ["list_id", "action"],
                    "additionalProperties": False,
                },
            },
        }
