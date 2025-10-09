from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FilterInventory(Tool):
    """Utility for fetching inventory items based on specific key-value criteria."""

    @staticmethod
    def invoke(data: dict[str, Any], key: str, value: str, list_of_ids: list[str] = None) -> str:
        inventories = data.get("inventory", [])
        result = [
            item["inventory_id"]
            for item in inventories
            if item[key].lower() == value.lower()
        ]
        if list_of_ids:
            result = [r for r in result if r in list_of_ids]
        if result:
            payload = {key: value, "result": result}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"No matching inventories found for {key} {value}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterInventory",
                "description": "Retrieve inventory items based on key and value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of inventories to choose from.",
                        },
                        "key": {
                            "type": "string",
                            "description": "Key to consider like warehouse_id and sku.",
                        },
                        "value": {
                            "type": "string",
                            "description": "Value to consider for this skey.",
                        },
                    },
                },
            },
        }
