# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class check_low_stock_items(Tool):
    """
    Tool that will reorder low stock items. Can order for specific stores and items, or everything all at once.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], sku, store_id) -> str:

        inventory = list(data.get("inventory", {}).values())

        out = []

        for item in inventory:
            # When applying a filter for store or SKU
            if ((store_id is None) or (item["store_id"] == store_id)) and (
                (sku is None) or (item["sku"] == sku)
            ):
                # Verify if the item requires reordering.
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

        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_low_stock_items",
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
