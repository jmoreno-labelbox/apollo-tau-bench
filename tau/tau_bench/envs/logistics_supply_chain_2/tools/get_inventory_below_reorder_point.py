from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetInventoryBelowReorderPoint(Tool):
    """Utility for fetching inventory items that fall below the reorder threshold."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_ids: list[str] = None) -> str:
        inventories = data.get("inventory", [])
        low_stock = [
            item["inventory_id"]
            for item in inventories
            if item["quantity_available"] < item["reorder_point"]
        ]
        if list_of_ids:
            low_stock = [ls for ls in low_stock if ls in list_of_ids]
        payload = low_stock
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryBelowReorderPoint",
                "description": "Retrieve inventory items where available quantity is below reorder point.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of inventories to choose from.",
                        }
                    },
                },
            },
        }
