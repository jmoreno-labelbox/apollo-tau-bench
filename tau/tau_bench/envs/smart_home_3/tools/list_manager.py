# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], list_id, list_name, action = 'get', item_data = {}, list_data = {}, tags = []) -> str:
        lists = list(data.get('custom_lists', {}).values())

        if action == 'get':
            result = [l for l in lists if (not list_id or l['list_id'] == list_id) and
                     (not list_name or l['name'] == list_name) and
                     (not tags or any(tag in l.get('tags', []) for tag in tags))]
            return json.dumps(result, indent=2)
        elif action == 'add_item':
            if not list_id or not item_data:
                return json.dumps({"error": "list_id and item_data required"}, indent=2)
            for lst in lists:
                if lst['list_id'] == list_id:
                    lst['items'].append(item_data)
                    lst['updated_at'] = _now_iso()
                    return json.dumps({"success": f"Added item to {list_id}"}, indent=2)
        elif action == 'remove_item':
            if not list_id or not item_data.get('item'):
                return json.dumps({"error": "list_id and item name required"}, indent=2)
            for lst in lists:
                if lst['list_id'] == list_id:
                    lst['items'] = [i for i in lst['items'] if i['item'] != item_data['item']]
                    lst['updated_at'] = _now_iso()
                    return json.dumps({"success": f"Removed item from {list_id}"}, indent=2)
        elif action == 'create':
            if not list_data:
                return json.dumps({"error": "list_data required"}, indent=2)
            lists.append(list_data)
            return json.dumps({"success": f"Created list {list_data.get('list_id')}"}, indent=2)
        elif action == 'delete':
            if not list_id:
                return json.dumps({"error": "list_id required"}, indent=2)
            lists[:] = [l for l in lists if l['list_id'] != list_id]
            return json.dumps({"success": f"Deleted list {list_id}"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_manager",
                "description": "Manage custom lists and their items",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "add_item", "remove_item", "create", "delete"]},
                        "list_id": {"type": "string", "description": "List ID (already exists)"},
                        "list_name": {"type": "string", "description": "Filter by list name"},
                        "tags": {"type": "array", "items": {"type": "string"}, "description": "Filter by tags"},
                        "item_data": {"type": "object", "description": "Item data to add/remove"},
                        "list_data": {"type": "object", "description": "Full list data for creation (needs list_id (str) and items (list of dicts with item (str) and quantity (int)))"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }
