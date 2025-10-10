# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryWithDamage(Tool):
    """Tool to retrieve inventory items with quantity_damaged > 0."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventories = list(data.get("inventory", {}).values())
        threshold = kwargs.get("threshold", None)
        less_than_threshold = kwargs.get("less_than_threshold", "False")
        list_of_inventories = kwargs.get("list_of_ids", None)
        if threshold:
            if less_than_threshold == "True":
                damaged = [[item['inventory_id'], item['quantity_damaged']] for item in inventories if item["quantity_damaged"] < threshold]
            else:
                damaged = [[item['inventory_id'], item['quantity_damaged']] for item in inventories if
                           item["quantity_damaged"] > threshold]
        else:
            if less_than_threshold == "True":
                damaged = [[item['inventory_id'], item['quantity_damaged']] for item in inventories if item["quantity_damaged"] < 0]
            else:
                damaged = [[item['inventory_id'], item['quantity_damaged']] for item in inventories if item["quantity_damaged"] > 0]
        if list_of_inventories:
            damaged = [d for d in damaged if d[0] in list_of_inventories]
        return json.dumps(damaged, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_with_damage",
                "description": "Retrieve inventory items that have damaged stock.",
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
                        "threshold": {
                            "type": "number",
                            "description": "Threshold value of quantity damaged."
                        },
                        "less_than_threshold": {
                            "type": "string",
                            "description": "'True' means value compared less than threshold."
                        }
                    }
                }
            }
        }
