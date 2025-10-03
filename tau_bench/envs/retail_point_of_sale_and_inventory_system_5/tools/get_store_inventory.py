from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class GetStoreInventory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None, sku: str = None) -> str:
        inventory = data.get("inventory", [])
        result = [
            item
            for item in inventory
            if item["store_id"] == store_id and item["sku"] == sku
        ]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetStoreInventory",
                "parameters": {
                    "store_id": {"type": "string"},
                    "sku": {"type": "string"},
                },
                "required": ["store_id", "sku"],
            },
        }
