from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetItemIdByProduct:
    @staticmethod
    def invoke(
        data: dict[str, Any],
        product_ids: list[str],
        product_type: list[str] = None,
        show_available: bool = None,
        exclude_no_stock: bool = True,
    ) -> str:
        """
        Get list of item IDs (variants) from specified product IDs, optionally filtered by product type and availability
        Excludes items with no stock (out_of_stock, discontinued) by default

        Data Sources: products.json (product_id, name, variants), suppliers.json (item_stock for stock validation)
        """
        if not product_ids:
            payload = {"error": "Product IDs list cannot be empty", "status": "failed"}
            out = json.dumps(payload)
            return out

        products = data.get("products", [])
        suppliers = data.get("suppliers", [])

        # Build stock information map from all suppliers
        stock_info_map = {}
        for supplier in suppliers:
            item_stock = supplier.get("item_stock", {})
            for item_id, stock_level in item_stock.items():
                # Track all suppliers that have this item and their stock levels
                if item_id not in stock_info_map:
                    stock_info_map[item_id] = []
                stock_info_map[item_id].append(
                    {
                        "supplier_id": supplier.get("supplier_id"),
                        "stock_level": stock_level,
                    }
                )

        # Convert product_type to lowercase for case-insensitive matching
        product_type_lower = []
        if product_type:
            product_type_lower = [ptype.lower() for ptype in product_type]

        matching_items = []
        product_item_map = {}
        total_variants_found = 0
        total_available_variants = 0
        total_unavailable_variants = 0
        total_excluded_no_stock = 0
        products_not_found = []

        for requested_product_id in product_ids:
            product_found = False

            for product in products:
                product_id = product.get("product_id")
                product_name = product.get("name", "").lower()
                variants = product.get("variants", {})

                if product_id == requested_product_id:
                    product_found = True

                    # Apply product type filter if specified
                    if product_type_lower:
                        # Check if product name contains any of the specified types
                        type_matches = any(
                            ptype in product_name for ptype in product_type_lower
                        )

                        if not type_matches:
                            # Product doesn't match type filter, skip it
                            continue

                    # Extract all item IDs (variant IDs) for this product with availability and stock filtering
                    product_items = []
                    for item_id, variant_info in variants.items():
                        is_available = variant_info.get("available", False)

                        # Check stock status across all suppliers
                        item_stock_info = stock_info_map.get(item_id, [])
                        has_stock = False
                        best_stock_level = "not_in_inventory"
                        supplier_count = 0

                        # Check if any supplier has this item with actual stock
                        for supplier_stock in item_stock_info:
                            stock_level = supplier_stock["stock_level"]
                            supplier_count += 1

                            # Consider item as having stock if any supplier has numeric stock > 0
                            if (
                                isinstance(stock_level, (int, str))
                                and str(stock_level).isdigit()
                                and int(stock_level) > 0
                            ):
                                has_stock = True
                                if best_stock_level == "not_in_inventory" or (
                                    isinstance(best_stock_level, (int, str))
                                    and int(stock_level) > int(best_stock_level)
                                ):
                                    best_stock_level = stock_level
                            elif not has_stock:
                                if best_stock_level == "not_in_inventory":
                                    best_stock_level = stock_level

                        # Apply stock exclusion filter if enabled
                        if exclude_no_stock and not has_stock:
                            # Item has no stock or is out_of_stock/discontinued across all suppliers
                            total_excluded_no_stock += 1
                            continue

                        # Apply availability filter if show_available is specified
                        if show_available is not None:
                            if show_available and not is_available:
                                # Want available items only, but this item is not available
                                total_unavailable_variants += 1
                                continue
                            elif not show_available and is_available:
                                # Want unavailable items only, but this item is available
                                total_available_variants += 1
                                continue

                        # Track totals for summary
                        if is_available:
                            total_available_variants += 1
                        else:
                            total_unavailable_variants += 1

                        # Determine stock status description
                        stock_status = "not_in_inventory"
                        total_stock_across_suppliers = 0

                        if has_stock:
                            stock_status = "in_stock"
                            # Calculate total stock across all suppliers
                            for supplier_stock in item_stock_info:
                                stock_level = supplier_stock["stock_level"]
                                if (
                                    isinstance(stock_level, (int, str))
                                    and str(stock_level).isdigit()
                                ):
                                    total_stock_across_suppliers += int(stock_level)
                        elif item_stock_info:
                            # Has stock entries but no actual stock
                            stock_statuses = [s["stock_level"] for s in item_stock_info]
                            if all(
                                status == "out_of_stock" for status in stock_statuses
                            ):
                                stock_status = "out_of_stock"
                            elif all(
                                status == "discontinued" for status in stock_statuses
                            ):
                                stock_status = "discontinued"
                            elif any(
                                status in ["out_of_stock", "discontinued"]
                                for status in stock_statuses
                            ):
                                stock_status = "mixed_no_stock"

                        item_detail = {
                            "item_id": item_id,
                            "price": variant_info.get("price", 0),
                            "available": is_available,
                            "options": variant_info.get("options", {}),
                            "stock_info": {
                                "stock_status": stock_status,
                                "total_stock_across_suppliers": total_stock_across_suppliers,
                                "suppliers_with_item": supplier_count,
                                "best_stock_level": best_stock_level,
                                "supplier_stock_details": item_stock_info,
                            },
                        }
                        product_items.append(item_detail)
                        total_variants_found += 1

                    if product_items:
                        product_info = {
                            "product_id": product_id,
                            "product_name": product.get("name"),
                            "total_variants": len(product_items),
                            "available_variants": len(
                                [item for item in product_items if item["available"]]
                            ),
                            "unavailable_variants": len(
                                [
                                    item
                                    for item in product_items
                                    if not item["available"]
                                ]
                            ),
                            "in_stock_variants": len(
                                [
                                    item
                                    for item in product_items
                                    if item["stock_info"]["stock_status"] == "in_stock"
                                ]
                            ),
                            "out_of_stock_variants": len(
                                [
                                    item
                                    for item in product_items
                                    if item["stock_info"]["stock_status"]
                                    in [
                                        "out_of_stock",
                                        "discontinued",
                                        "mixed_no_stock",
                                    ]
                                ]
                            ),
                            "item_ids": product_items,
                        }
                        matching_items.append(product_info)
                        product_item_map[product_id] = [
                            item["item_id"] for item in product_items
                        ]

                    break

            if not product_found:
                products_not_found.append(requested_product_id)

        # Create a flat list of all item IDs for easy access
        all_item_ids = []
        for product_info in matching_items:
            all_item_ids.extend([item["item_id"] for item in product_info["item_ids"]])

        # Determine filter description for response
        availability_filter_description = "all items"
        if show_available is True:
            availability_filter_description = "available items only"
        elif show_available is False:
            availability_filter_description = "unavailable items only"

        stock_filter_description = (
            "items with stock only"
            if exclude_no_stock
            else "all items regardless of stock"
        )

        result = {
            "status": "success",
            "search_criteria": {
                "requested_product_ids": product_ids,
                "product_type_filter": product_type,
                "show_available": show_available,
                "exclude_no_stock": exclude_no_stock,
                "filter_applied": product_type is not None
                or show_available is not None
                or exclude_no_stock,
                "availability_filter": availability_filter_description,
                "stock_filter": stock_filter_description,
            },
            "summary": {
                "products_found": len(matching_items),
                "products_not_found": len(products_not_found),
                "total_variants_found": total_variants_found,
                "total_available_variants": total_available_variants,
                "total_unavailable_variants": total_unavailable_variants,
                "total_excluded_no_stock": total_excluded_no_stock,
                "availability_breakdown": {
                    "available_percentage": (
                        round(
                            (
                                total_available_variants
                                / (
                                    total_available_variants
                                    + total_unavailable_variants
                                )
                                * 100
                            ),
                            1,
                        )
                        if (total_available_variants + total_unavailable_variants) > 0
                        else 0
                    ),
                    "unavailable_percentage": (
                        round(
                            (
                                total_unavailable_variants
                                / (
                                    total_available_variants
                                    + total_unavailable_variants
                                )
                                * 100
                            ),
                            1,
                        )
                        if (total_available_variants + total_unavailable_variants) > 0
                        else 0
                    ),
                },
                "stock_filtering": {
                    "items_excluded_no_stock": total_excluded_no_stock,
                    "items_with_stock": len(
                        [
                            item
                            for product in matching_items
                            for item in product["item_ids"]
                            if item["stock_info"]["stock_status"] == "in_stock"
                        ]
                    ),
                    "exclusion_rate_percent": (
                        round(
                            (
                                total_excluded_no_stock
                                / (total_variants_found + total_excluded_no_stock)
                                * 100
                            ),
                            1,
                        )
                        if (total_variants_found + total_excluded_no_stock) > 0
                        else 0
                    ),
                },
            },
            "item_ids": {
                "all_item_ids": all_item_ids,
                "products_with_items": matching_items,
            },
            "product_item_mapping": product_item_map,
            "products_not_found": products_not_found,
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetItemIdsByProduct",
                "description": "Get list of item IDs (variants) from specified product IDs, optionally filtered by product type and availability status. Excludes items with no stock (out_of_stock, discontinued) by default.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of product identifiers to get item IDs from (e.g., ['PROD001', 'PROD002'])",
                        },
                        "product_type": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of product types to filter by (e.g., ['laptop', 'bluetooth speaker', 't-shirt']). Matches product names containing these terms.",
                        },
                        "show_available": {
                            "type": "boolean",
                            "description": "Optional availability filter: true = only available items, false = only unavailable/out-of-stock items, null/undefined = all items regardless of availability",
                        },
                        "exclude_no_stock": {
                            "type": "boolean",
                            "description": "Optional stock filter: true = exclude items with no stock (out_of_stock, discontinued), false = include all items regardless of stock status",
                            "default": True,
                        },
                    },
                    "required": ["product_ids"],
                },
            },
        }
