# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class remove_product(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku) -> str:
        products = list(data.get("products", {}).values())

        if sku is None:
            return json.dumps({"error": "sku must be sent"}, indent=2)

        for product in products:
            if product["sku"] == sku:
                del product

                return json.dumps(
                    {"success": "Removed product: {}".format(sku)}, indent=2
                )

        return json.dumps({"error": "No sku found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_product",
                "description": "Removes a product from the products table. This means that the supplier no longer offers it. Use remove_inventory if it is only being removed from a single store.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The sku of the product to remove",
                        },
                    },
                },
            },
        }
