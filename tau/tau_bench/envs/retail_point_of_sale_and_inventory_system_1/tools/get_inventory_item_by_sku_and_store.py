# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryItemBySkuAndStore(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get('sku')
        store_id = kwargs.get('store_id')
        inventory_items = list(data.get("inventory", {}).values())
        for item in inventory_items:
            if item.get("sku") == sku and item.get("store_id") == store_id:
                return json.dumps(item)
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_item_by_sku_and_store",
                "description": "Retrieves detailed information for a specific inventory item by its SKU and store ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The ID of the store where the inventory is located.",
                        },
                    },
                    "required": ["sku", "store_id"],
                },
            },
        }
