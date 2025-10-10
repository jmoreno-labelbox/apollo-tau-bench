# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchProductsByFilter(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], category: str = None, min_price: float = None, max_price: float = None, available_only: bool = True, options: Dict[str, Any] = None, **kwargs) -> str:
        """
        Search products by category, price range, and availability status

        Data Sources: products.json (product_id, name, variants with price/available fields)
        """
        products = list(data.get("products", {}).values())
        matching_products = []
        show_all = kwargs.get("show_all", False)

        # Condition: Verify item availability prior to allocation - do not allocate items that are out of stock.
        for product in products:
            product_name = product.get("name", "").lower()
            product_id = product.get("product_id")
            variants = product.get("variants", {})
            limit = kwargs.get("limit", None)

            # Apply category filtering if provided.
            if category and category.lower() not in product_name:
                continue

            # Verify options for filtering by price and availability.
            valid_variants = []
            for variant_id, variant in variants.items():
                variant_price = variant.get("price", 0)
                variant_available = variant.get("available", False)
                variant_options = variant.get("options", {})

                # Guideline: Verify product availability prior to distribution.
                if not show_all:
                    if available_only and not variant_available:
                        continue

                # Implement price filtering.
                if min_price is not None and variant_price < min_price:
                    continue
                if max_price is not None and variant_price > max_price:
                    continue

                # Implement the options filter if it exists.
                if options:
                    # Verify that all designated options correspond with the variant options.
                    options_match = True
                    for option_key, option_value in options.items():
                        variant_option_value = variant_options.get(option_key)

                        if variant_option_value is None:
                            options_match = False
                            break

                        # Support multiple entries for a single option (e.g., color: ["red", "blue"])
                        if isinstance(option_value, list):
                            # Verify if the variant's option value aligns with any of the specified values.
                            variant_value_str = str(variant_option_value).lower().strip()
                            value_matches = any(
                                variant_value_str == str(val).lower().strip()
                                for val in option_value
                            )
                            if not value_matches:
                                options_match = False
                                break
                        else:
                            # Individual value evaluation (current implementation)
                            variant_value_str = str(variant_option_value).lower().strip()
                            search_value_str = str(option_value).lower().strip()

                            if variant_value_str != search_value_str:
                                options_match = False
                                break

                    if not options_match:
                        continue

                valid_variants.append({
                    "item_id": variant_id,
                    "price": variant_price,
                    "available": variant_available,
                    "options": variant_options
                })

            if valid_variants:
                matching_products.append({
                    "product_id": product_id,
                    "name": product.get("name"),
                    "variants_count": len(valid_variants),
                    "price_range": {
                        "min": min(v["price"] for v in valid_variants),
                        "max": max(v["price"] for v in valid_variants)
                    },
                    "sample_variants": valid_variants
                })

        # Filter by the price flag if available and return just one product.
        price_flag = kwargs.get("price_flag")

        if price_flag == "cheapest":
            # Organize sample_variants by price for each product.
            for product in matching_products:
                if "sample_variants" in product:
                    product["sample_variants"].sort(key=lambda v: v["price"])
                    product["sample_variants"] = product["sample_variants"][:limit]  # Restrict to the least expensive option.

        elif price_flag == "expensive":
            # Arrange sample_variants for each product in descending order based on price.
            for product in matching_products:
                if "sample_variants" in product:
                    product["sample_variants"].sort(key=lambda v: v["price"], reverse=True)
                    product["sample_variants"] = product["sample_variants"][:limit]

        result = {
            "status": "success",
            "search_criteria": {
                "category": category,
                "min_price": min_price,
                "max_price": max_price,
                "available_only": available_only,
                "options_filter": options
            },
            "total_products_found": len(matching_products),
            "products": matching_products[:10]
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_products_by_filter",
                "description": "Search products by category, price range, availability, and specific variant options from product catalog",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {"type": "string", "description": "Product category filter (e.g., 'laptop', 't-shirt', 'bluetooth speaker')"},
                        "min_price": {"type": "number", "description": "Minimum price filter"},
                        "max_price": {"type": "number", "description": "Maximum price filter"},
                        "available_only": {"type": "boolean", "description": "Show only available products", "default": True},
                        "options": {
                            "type": "object",
                            "description": "Filter by specific variant options. Values can be strings or arrays for multiple options (e.g., {'color': ['red', 'blue'], 'battery life': '20 hours', 'size': ['large', 'medium']})",
                            "additionalProperties": {
                                "oneOf": [
                                    {"type": "string"},
                                    {"type": "array", "items": {"type": "string"}}
                                ]
                            }
                        },
                        "price_flag": {"type": "string", "description": "Flag to indicate price preference (e.g., 'cheapest', 'expensive')"},
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of variants to return per product",
                            "default": 1
                        },
                        "show_all": {
                            "type": "boolean",
                            "description": "Flag to indicate if all matching products should be returned",
                            "default": False
                        }
                    }
                }
            }
        }
