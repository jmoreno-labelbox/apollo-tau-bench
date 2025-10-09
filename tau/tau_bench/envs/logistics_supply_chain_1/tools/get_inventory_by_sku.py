from tau_bench.envs.tool import Tool
import json
import random
from typing import Any

class GetInventoryBySku(Tool):
    """A utility to obtain all inventory records for a specified SKU across all warehouses."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None) -> str:
        if not sku:
            payload = {"error": "sku is a required argument."}
            out = json.dumps(payload, indent=2)
            return out
        inventory = data.get("inventory", [])
        sku_inventory = [item for item in inventory if item.get("sku") == sku]
        payload = sku_inventory
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryBySku",
                "description": "Retrieves all inventory records for a specific SKU across all warehouses.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU to search for inventory records of.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }
