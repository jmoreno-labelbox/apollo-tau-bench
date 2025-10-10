# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterInventory(Tool):
    """Tool to retrieve inventory items by key and value."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventories = list(data.get("inventory", {}).values())
        key = kwargs.get("key")
        value = kwargs.get("value")
        list_of_inventories = kwargs.get("list_of_ids", None)
        result = [item['inventory_id'] for item in inventories if item[key].lower() == value.lower()]
        if list_of_inventories:
            result = [r for r in result if r in list_of_inventories]
        if result:
            return json.dumps({key: value, 'result': result}, indent=2)
        return json.dumps({"error": f"No matching inventories found for {key} {value}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filter_inventory",
                "description": "Retrieve inventory items based on key and value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of inventories to choose from."
                        },
                        "key": {
                            "type": "string",
                            "description": "Key to consider like warehouse_id and sku."
                        },
                        "value": {
                            "type": "string",
                            "description": "Value to consider for this skey."
                        }
                    }
                }
            }
        }
