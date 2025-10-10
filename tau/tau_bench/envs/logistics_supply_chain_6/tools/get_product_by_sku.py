# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductBySku(Tool):
    """Tool to get product details by SKU."""

    @staticmethod
    def invoke(data: Dict[str, Any], sku: str) -> str:
        """Execute the tool with given parameters."""
        products = data.get("product_master", [])
        for product in products:
            if product.get("sku") == sku:
                return json.dumps(product, indent=2)
        return json.dumps({"error": f"Product with SKU {sku} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_product_by_sku",
                "description": "Retrieves detailed information about a specific product using its SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The Stock Keeping Unit (SKU) of the product to find.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }
