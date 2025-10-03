from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any

class remove_product(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None) -> str:
        products = data.get("products", [])

        if sku is None:
            payload = {"error": "sku must be sent"}
            out = json.dumps(payload, indent=2)
            return out

        for product in products:
            if product["sku"] == sku:
                del product
                payload = {"success": f"Removed product: {sku}"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "No sku found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveProduct",
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
