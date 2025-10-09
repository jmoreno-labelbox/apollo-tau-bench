from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CheckLowStockItems(Tool):
    """Tool for reordering items with low stock, capable of ordering for specific stores and items or all at once."""

    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None, sku: str = None) -> str:
        inventory = data.get("inventory", [])

        out = []

        for item in inventory:
            # When filtering by store or sku
            if ((store_id is None) or (item["store_id"] == store_id)) and (
                (sku is None) or (item["sku"] == sku)
            ):
                # Verify if the item requires reordering
                if item["status"] in ["low_stock", "critical"]:
                    out.append(
                        {
                            k: item[k]
                            for k in [
                                "store_id",
                                "sku",
                                "status",
                                "safety_stock",
                                "reorder_level",
                                "quantity",
                            ]
                        }
                    )
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckLowStockItems",
                "description": "Checks if items are low stock and need to be reordered. Returns a list of items that are low stock",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "OPTIONAL. The specific ID of the store to reorder items for. If not sent, every store will be checked.",
                        },
                        "sku": {
                            "type": "string",
                            "description": "OPTIONAL. The specific sku for the item to reorder. If not sent, every item will be checked",
                        },
                    },
                },
            },
        }
