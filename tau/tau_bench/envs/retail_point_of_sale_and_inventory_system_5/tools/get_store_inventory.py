# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetStoreInventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku, store_id) -> str:
        inventory = list(data.get("inventory", {}).values())
        result = [item for item in inventory if item["store_id"] == store_id and item["sku"] == sku]
        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", 
            "function": {
                "name": "get_store_inventory",
                "description": "Get inventory for a specific store and SKU",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "string"}, 
                        "sku": {"type": "string"}
                    }, 
                    "required": ["store_id", "sku"]
                }
            }
        }
