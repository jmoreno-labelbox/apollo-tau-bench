# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class remove_inventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], inv_id) -> str:
        inventory = list(data.get("inventory", {}).values())

        if inv_id is None:
            return json.dumps({"error": "inv_id must be sent"}, indent=2)

        for item in inventory:
            if item["id"] == inv_id:
                del item

                return json.dumps(
                    {"success": "Removed item: {}".format(inv_id)}, indent=2
                )

        return json.dumps({"error": "No item found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_inventory",
                "description": "Removes an item from the store. This is for completely removing an item, to set to 0, use update_stock_quantity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inv_id": {
                            "type": "string",
                            "description": "The id of the item to remove",
                        },
                    },
                },
            },
        }
