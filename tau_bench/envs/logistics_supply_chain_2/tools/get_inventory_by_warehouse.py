from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetInventoryByWarehouse(Tool):
    """Utility for obtaining inventory items located in a designated warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str, list_of_ids: list[str] = None) -> str:
        inventories = data.get("inventory", [])
        filtered = [
            item["inventory_id"]
            for item in inventories
            if item["warehouse_id"] == warehouse_id
        ]
        if list_of_ids:
            filtered = [f for f in filtered if f in list_of_ids]
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryByWarehouse",
                "description": "Retrieve inventory items from a specific warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "Warehouse ID (e.g., 'WH-10').",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of inventories to choose from.",
                        },
                    },
                    "required": ["warehouse_id"],
                },
            },
        }
