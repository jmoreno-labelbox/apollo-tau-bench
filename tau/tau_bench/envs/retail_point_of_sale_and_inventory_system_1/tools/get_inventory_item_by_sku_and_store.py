from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetInventoryItemBySkuAndStore(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, store_id: str = None) -> str:
        inventory_items = data.get("inventory", [])
        for item in inventory_items:
            if item.get("sku") == sku and item.get("store_id") == store_id:
                payload = item
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryItemBySkuAndStore",
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
