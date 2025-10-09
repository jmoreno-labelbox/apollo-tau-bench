from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class SearchProductsByCategory(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        category: str,
        available_only: bool = True,
        max_price: float = None,
        min_price: float = None,
        min_stock: int = 1,
        max_stock: int = None
    ) -> str:
        if not category:
            payload = {"error": "category is required"}
            out = json.dumps(payload)
            return out

        # Check the validity of stock range
        if min_stock is not None and max_stock is not None and min_stock > max_stock:
            payload = {"error": "min_stock cannot be greater than max_stock"}
            out = json.dumps(payload)
            return out

        products = data["products"]
        suppliers = data["suppliers"]
        results = []

        # Establish a mapping from item_id to stock level for fast retrieval
        item_stock_map = {}
        for supplier in suppliers:
            for item_id, stock in supplier.get("item_stock", {}).items():
                # Take into account only numeric stock levels
                if isinstance(stock, (int, float)) and stock >= 0:
                    item_stock_map[item_id] = stock

        for product in products:
            if category.lower() in product["name"].lower():
                for variant_id, variant in product["variants"].items():
                    if available_only and not variant.get("available", False):
                        continue
                    if max_price and variant["price"] > max_price:
                        continue
                    if min_price and variant["price"] < min_price:
                        continue

                    # Verify stock levels when stock filters are available
                    item_id = variant.get("item_id", variant_id)
                    stock_level = item_stock_map.get(item_id, 0)

                    if min_stock is not None and stock_level < min_stock:
                        continue
                    if max_stock is not None and stock_level > max_stock:
                        continue

                    results.append(
                        {
                            "product_id": product["product_id"],
                            "name": product["name"],
                            "item_id": variant.get("item_id", variant_id),
                            "price": variant["price"],
                            "stock_level": stock_level,
                            "options": variant["options"],
                            "available": variant["available"],
                        }
                    )

        results.sort(key=lambda x: x["price"])
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchProductsByCategory",
                "description": "Search for products by category name with optional price, availability, and stock filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "Product category to search for",
                        },
                        "available_only": {
                            "type": "boolean",
                            "description": "Only return available products",
                            "default": True,
                        },
                        "max_price": {
                            "type": "number",
                            "description": "Maximum price filter",
                        },
                        "min_price": {
                            "type": "number",
                            "description": "Minimum price filter",
                        },
                        "min_stock": {
                            "type": "integer",
                            "description": "Minimum stock level filter",
                        },
                        "max_stock": {
                            "type": "integer",
                            "description": "Maximum stock level filter",
                        },
                    },
                    "required": ["category"],
                },
            },
        }
