from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchProductsByFilter(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        category: str = None,
        min_price: float = None,
        max_price: float = None,
        available_only: bool = True,
        options: dict[str, Any] = None,
        show_all: bool = False,
        limit: int = None,
        price_flag: str = None,
    ) -> str:
        """
        Search products by category, price range, and availability status

        Data Sources: products.json (product_id, name, variants with price/available fields)
        """
        _categoryL = (category or '').lower()
        products = data.get("products", {}).values()
        matching_products = []

        # Rule: Check product availability status before allocation - never allocate unavailable items
        for product in products.values():
            product_name = product.get("name", "").lower()
            product_id = product.get("product_id")
            variants = product.get("variants", {}).values()

            # Filter by category if specified
            if category and category.lower() not in product_name:
                continue

            # Check variants for price and availability filtering
            valid_variants = []
            for variant_id, variant in variants.items():
                variant_price = variant.get("price", 0)
                variant_available = variant.get("available", False)
                variant_options = variant.get("options", {}).values()

                # Rule: Check product availability status before allocation
                if not show_all:
                    if available_only and not variant_available:
                        continue

                # Apply price filters
                if min_price is not None and variant_price < min_price:
                    continue
                if max_price is not None and variant_price > max_price:
                    continue

                # Apply options filter if provided
                if options:
                    # Check if all specified options match the variant options
                    options_match = True
                    for option_key, option_value in options.items():
                        variant_option_value = variant_options.get(option_key)

                        if variant_option_value is None:
                            options_match = False
                            break

                        # Handle multiple values for the same option (e.g., color: ["red", "blue"])
                        if isinstance(option_value, list):
                            # Check if variant's option value matches any of the provided values
                            variant_value_str = (
                                str(variant_option_value).lower().strip()
                            )
                            value_matches = any(
                                variant_value_str == str(val).lower().strip()
                                for val in option_value
                            )
                            if not value_matches:
                                options_match = False
                                break
                        else:
                            # Single value comparison (existing logic)
                            variant_value_str = (
                                str(variant_option_value).lower().strip()
                            )
                            search_value_str = str(option_value).lower().strip()

                            if variant_value_str != search_value_str:
                                options_match = False
                                break

                    if not options_match:
                        continue

                valid_variants.append(
                    {
                        "item_id": variant_id,
                        "price": variant_price,
                        "available": variant_available,
                        "options": variant_options,
                    }
                )

            if valid_variants:
                matching_products.append(
                    {
                        "product_id": product_id,
                        "name": product.get("name"),
                        "variants_count": len(valid_variants),
                        "price_range": {
                            "min": min(v["price"] for v in valid_variants.values()),
                            "max": max(v["price"] for v in valid_variants.values()),
                        },
                        "sample_variants": valid_variants,
                    }
                )

        # Filter based on price flag if provided and return only a single product
        if price_flag == "cheapest":
            # Sort sample_variants within each product by price
            for product in matching_products:
                if "sample_variants" in product:
                    product["sample_variants"].sort(key=lambda v: v["price"])
                    product["sample_variants"] = product["sample_variants"][
                        :limit
                    ]  # Limit to cheapest variant

        elif price_flag == "expensive":
            # Sort sample_variants within each product by price in descending order
            for product in matching_products:
                if "sample_variants" in product:
                    product["sample_variants"].sort(
                        key=lambda v: v["price"], reverse=True
                    )
                    product["sample_variants"] = product["sample_variants"][:limit]

        result = {
            "status": "success",
            "search_criteria": {
                "category": category,
                "min_price": min_price,
                "max_price": max_price,
                "available_only": available_only,
                "options_filter": options,
            },
            "total_products_found": len(matching_products),
            "products": matching_products[:10],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchProductsByFilter",
                "description": "Search products by category, price range, availability, and specific variant options from product catalog",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "Product category filter (e.g., 'laptop', 't-shirt', 'bluetooth speaker')",
                        },
                        "min_price": {
                            "type": "number",
                            "description": "Minimum price filter",
                        },
                        "max_price": {
                            "type": "number",
                            "description": "Maximum price filter",
                        },
                        "available_only": {
                            "type": "boolean",
                            "description": "Show only available products",
                            "default": True,
                        },
                        "options": {
                            "type": "object",
                            "description": "Filter by specific variant options. Values can be strings or arrays for multiple options (e.g., {'color': ['red', 'blue'], 'battery life': '20 hours', 'size': ['large', 'medium']})",
                            "additionalProperties": {
},
                        },
                        "price_flag": {
                            "type": "string",
                            "description": "Flag to indicate price preference (e.g., 'cheapest', 'expensive')",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of variants to return per product",
                            "default": 1,
                        },
                        "show_all": {
                            "type": "boolean",
                            "description": "Flag to indicate if all matching products should be returned",
                            "default": False,
                        },
                    },
                },
            },
        }
