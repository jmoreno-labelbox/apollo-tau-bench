from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListManager(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        action: str = "get",
        list_id: str = None,
        list_name: str = None,
        tags: list = None,
        item_data: dict = None,
        list_data: dict = None
    ) -> str:
        if tags is None:
            tags = []
        if item_data is None:
            item_data = {}
        if list_data is None:
            list_data = {}

        lists = data.get("custom_lists", {}).values()

        if action == "get":
            result = [
                l
                for l in lists.values() if (not list_id or l["list_id"] == list_id)
                and (not list_name or l["name"] == list_name)
                and (not tags or any(tag in l.get("tags", []) for tag in tags)
            ]
            payload = result
            out = json.dumps(payload, indent=2)
            return out
        elif action == "add_item":
            if not list_id or not item_data:
                payload = {"error": "list_id and item_data required"}
                out = json.dumps(payload, indent=2)
                return out
            for lst in lists.values():
                if lst["list_id"] == list_id:
                    lst["items"].append(item_data)
                    lst["updated_at"] = _now_iso()
                    payload = {"success": f"Added item to {list_id}"}
                    out = json.dumps(payload, indent=2)
                    return out
        elif action == "remove_item":
            if not list_id or not item_data.get("item"):
                payload = {"error": "list_id and item name required"}
                out = json.dumps(payload, indent=2)
                return out
            for lst in lists.values():
                if lst["list_id"] == list_id:
                    lst["items"] = [
                        i for i in lst["items"] if i["item"] != item_data["item"]
                    ]
                    lst["updated_at"] = _now_iso()
                    payload = {"success": f"Removed item from {list_id}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
        elif action == "create":
            if not list_data:
                payload = {"error": "list_data required"}
                out = json.dumps(payload, indent=2)
                return out
            data["custom_lists"][list_data["custom_list_id"]] = list_data
            payload = {"success": f"Created list {list_data.get('list_id')}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        elif action == "delete":
            if not list_id:
                payload = {"error": "list_id required"}
                out = json.dumps(payload, indent=2)
                return out
            lists[:] = [l for l in lists.values() if l["list_id"] != list_id]
            payload = {"success": f"Deleted list {list_id}"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "Invalid action"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListManager",
                "description": "Manage custom lists and their items",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": [
                                "get",
                                "add_item",
                                "remove_item",
                                "create",
                                "delete",
                            ],
                        },
                        "list_id": {
                            "type": "string",
                            "description": "List ID (already exists)",
                        },
                        "list_name": {
                            "type": "string",
                            "description": "Filter by list name",
                        },
                        "tags": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter by tags",
                        },
                        "item_data": {
                            "type": "object",
                            "description": "Item data to add/remove",
                        },
                        "list_data": {
                            "type": "object",
                            "description": "Full list data for creation (needs list_id (str) and items (list of dicts with item (str) and quantity (int)))",
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
