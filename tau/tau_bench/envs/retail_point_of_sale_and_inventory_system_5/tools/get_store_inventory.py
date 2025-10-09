from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetStoreInventory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None, sku: str = None) -> str:
        inventory = data.get("inventory", {}).values()
        result = [
            item
            for item in inventory.values() if item["store_id"] == store_id and item["sku"] == sku
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
