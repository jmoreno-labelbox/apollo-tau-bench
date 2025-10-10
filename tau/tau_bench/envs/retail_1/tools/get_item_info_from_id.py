# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetItemInfoFromId(Tool): # READ
    @staticmethod
    def invoke(data: Dict[str, Any], item_id: str) -> str:
        products = list(data.get("products", {}).values())
        for product in products:
            if item_id in product["variants"]:
                return json.dumps(product["variants"][item_id])
        return json.dumps({"error": "Item not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_item_info_from_id",
                "description": "Retrieve item information by item ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string", "description": "The ID of the item to retrieve information for."}
                    },
                    "required": ["item_id"]
                }
            }
        }
