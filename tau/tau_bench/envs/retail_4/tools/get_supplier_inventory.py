# © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSupplierInventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str, product_types: List[str] = None, item_ids: List[str] = None, stock_available: bool = None, stock_level: int = None, stock_level_comparison: str = None) -> str:
        """
        Get supplier inventory filtered by product types, item IDs, stock availability, and stock level with comparison options
        """
        # Locate vendor
        suppliers = data.get("suppliers", [])
        target_supplier = next((s for s in suppliers if s.get("supplier_id") == supplier_id), None)

        if not target_supplier:
            return json.dumps({"error": f"Supplier {supplier_id} not found", "status": "failed"})

        # Check the stock_level parameter for validity.
        if stock_level is not None and stock_level < 0:
            return json.dumps({"error": "Stock level filter must be non-negative", "status": "failed"})

        # Check the stock_level_comparison parameter for validity.
        valid_comparisons = ["above", "below", "equal"]
        if stock_level_comparison and stock_level_comparison not in valid_comparisons:
            return json.dumps({
                "error": f"Invalid stock_level_comparison '{stock_level_comparison}'. Valid options: {', '.join(valid_comparisons)}",
                "status": "failed"
            })

        # If stock_level_comparison is supplied, stock_level must be included as well.
        if stock_level_comparison and stock_level is None:
            return json.dumps({
                "error": "stock_level must be provided when using stock_level_comparison",
                "status": "failed"
            })

        # Retrieve product mapping.
        products = list(data.get("products", {}).values())
        item_to_product_map = {}
        product_details_map = {}

        for product in products:
            product_id = product.get("product_id")
            product_name = product.get("name", "").lower()
            variants = product.get("variants", {})

            if product_id:
                product_details_map[product_id] = {
                    "product_id": product_id,
                    "product_name": product.get("name"),
                    "product_category": product.get("category", "")
                }

                for item_id in variants.keys():
                    item_to_product_map[item_id] = product_id

        # Refine supplier stock list.
        supplier_item_stock = target_supplier.get("item_stock", {})
        matching_items = []

        for item_id, stock_level_value in supplier_item_stock.items():
            # Implement stock_available filter if provided.
            if stock_available is not None:
                if stock_available:
                    # Filter to include only items with stock quantity greater than zero.
                    if not (isinstance(stock_level_value, (int, str)) and str(stock_level_value).isdigit() and int(stock_level_value) > 0):
                        continue
                else:
                    # Include only items that are out of stock or no longer available.
                    if stock_level_value not in ["out_of_stock", "discontinued"]:
                        continue

            # Implement stock_level filter with comparison if provided.
            if stock_level is not None:
                # Verify only the numeric stock levels against the specified threshold.
                if isinstance(stock_level_value, (int, str)) and str(stock_level_value).isdigit():
                    numeric_stock = int(stock_level_value)

                    if stock_level_comparison:
                        if stock_level_comparison == "above" and numeric_stock <= stock_level:
                            continue
                        elif stock_level_comparison == "below" and numeric_stock >= stock_level:
                            continue
                        elif stock_level_comparison == "equal" and numeric_stock != stock_level:
                            continue
                    else:
                        # Standard operation (greater than or equal to)
                        if numeric_stock < stock_level:
                            continue
                else:
                    # Non-numeric inventory statuses (out_of_stock, discontinued) fail to satisfy numeric criteria.
                    continue

            # Use item_ids filter when provided.
            if item_ids and item_id not in item_ids:
                continue

            # Implement the product_types filter when provided.
            product_id = item_to_product_map.get(item_id)
            if product_types and product_id:
                product_name = product_details_map.get(product_id, {}).get("product_name", "").lower()
                type_matches = any(ptype.lower() in product_name for ptype in product_types)
                if not type_matches:
                    continue

            # Retrieve details for the product and its variants.
            if product_id and product_id in product_details_map:
                product_info = product_details_map[product_id]

                # Retrieve variant information
                product_variants = next((p.get("variants", {}) for p in products if p.get("product_id") == product_id), {})
                variant_info = product_variants.get(item_id, {})

                matching_items.append({
                    "item_id": item_id,
                    "product_id": product_id,
                    "product_name": product_info["product_name"],
                    "product_category": product_info["product_category"],
                    "stock_level": stock_level_value,
                    "numeric_stock_level": int(stock_level_value) if isinstance(stock_level_value, (int, str)) and str(stock_level_value).isdigit() else 0,
                    "price": variant_info.get("price", 0),
                    "available": variant_info.get("available", False),
                    "options": variant_info.get("options", {})
                })

        result = {
            "status": "success",
            "supplier_id": supplier_id,
            "filters_applied": {
                "product_types": product_types,
                "item_ids": item_ids,
                "stock_available": stock_available,
                "stock_level_threshold": stock_level,
                "stock_level_comparison": stock_level_comparison if stock_level_comparison else "greater_than_or_equal"
            },
            "items": matching_items,
            "total_items": len(matching_items)
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_supplier_inventory",
                "description": "Get supplier inventory filtered by product types, item IDs, stock availability, and stock level with comparison options (above, below, equal)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier identifier (e.g., '#SUP0001')"
                        },
                        "product_types": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of product types to filter by (e.g., ['laptop', 'smartphone', 't-shirt']). Matches product names containing these terms (case-insensitive)."
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of specific item IDs to include in results. Only these specific items will be returned if they exist in supplier's inventory."
                        },
                        "stock_available": {
                            "type": "boolean",
                            "description": "Optional stock availability filter: true = only items with stock available, false = only out_of_stock/discontinued items, null/undefined = all items regardless of stock status"
                        },
                        "stock_level": {
                            "type": "integer",
                            "description": "Optional stock level threshold for filtering. Works with stock_level_comparison parameter.",
                            "minimum": 0
                        },
                        "stock_level_comparison": {
                            "type": "string",
                            "description": "Optional comparison operator for stock level filtering. Requires stock_level to be specified. 'above' = greater than threshold, 'below' = less than threshold, 'equal' = exactly equal to threshold. If not specified, defaults to greater than or equal (>=).",
                            "enum": ["above", "below", "equal"]
                        }
                    },
                    "required": ["supplier_id"]
                }
            }
        }
