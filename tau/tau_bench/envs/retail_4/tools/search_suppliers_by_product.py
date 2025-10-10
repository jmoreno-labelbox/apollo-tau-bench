# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchSuppliersByProduct(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], product_id: str = None, item_id: str = None, min_stock_level: int = 0, exclude_statuses: List[str] = None, supplier_id: str = None, product_type: List[str] = None, stock_level_preference: str = None, available_only: bool = False) -> str:
        """
        Search suppliers by product availability and stock levels with optional product type filtering, stock level preference, and availability filtering

        Data Sources: suppliers.json (supplier_id, name, products, item_stock), products.json (product names for filtering and availability status)
        """
        if exclude_statuses is None:
            exclude_statuses = ["discontinued", "out_of_stock"]

        # Check the stock_level_preference parameter for validity.
        if stock_level_preference and stock_level_preference not in ["highest", "lowest"]:
            return json.dumps({
                "error": "Invalid stock_level_preference. Valid options: 'highest', 'lowest'",
                "status": "failed"
            })

        # Retrieve product details for type filtering and availability verification.
        products = list(data.get("products", {}).values())
        product_name_map = {}
        item_availability_map = {}

        for product in products:
            product_id_key = product.get("product_id")
            product_name = product.get("name", "").lower()
            variants = product.get("variants", {})

            if product_id_key:
                product_name_map[product_id_key] = product_name

                # Associate product variants with their availability status.
                for variant_id, variant_info in variants.items():
                    item_availability_map[variant_id] = variant_info.get("available", False)

        # Transform product_type to lowercase for uniform matching regardless of case.
        product_type_lower = []
        if product_type:
            product_type_lower = [ptype.lower() for ptype in product_type]

        # Filter the product_id based on the specified product type if applicable.
        if product_id and product_type_lower:
            product_name = product_name_map.get(product_id, "")
            if product_name:
                type_matches = any(
                    ptype in product_name
                    for ptype in product_type_lower
                )
                if not type_matches:
                    return json.dumps({
                        "status": "success",
                        "search_criteria": {
                            "product_id": product_id,
                            "item_id": item_id,
                            "min_stock_level": min_stock_level,
                            "excluded_statuses": exclude_statuses,
                            "supplier_id_filter": supplier_id,
                            "product_type_filter": product_type,
                            "stock_level_preference": stock_level_preference,
                            "available_only": available_only,
                            "filter_applied": True
                        },
                        "total_suppliers_found": 0,
                        "suppliers": [],
                        "message": f"Product {product_id} does not match the specified product type filter"
                    })

        suppliers = data.get("suppliers", [])
        matching_suppliers = []

        for supplier in suppliers:
            current_supplier_id = supplier.get("supplier_id")
            supplier_name = supplier.get("name")
            supplier_products = supplier.get("products", [])
            item_stock = supplier.get("item_stock", {})

            # Apply filter based on supplier_id if available.
            if supplier_id and current_supplier_id != supplier_id:
                continue

            # Verify if the supplier stocks the product.
            if product_id and product_id not in supplier_products:
                continue

            # Verify item inventory when item_id is supplied.
            supplier_match = {
                "supplier_id": current_supplier_id,
                "supplier_name": supplier_name,
                "contact_info": supplier.get("contact_info", {}),
                "matching_items": []
            }

            if item_id:
                # Targeted item retrieval
                if item_id in item_stock:
                    stock_level = item_stock[item_id]

                    # Ignore if the status is excluded.
                    if stock_level in exclude_statuses:
                        continue

                    # Evaluate the availability filter solely when available_only is set to True.
                    if available_only:
                        item_is_available = item_availability_map.get(item_id, False)
                        if not item_is_available:
                            continue

                    # Verify the lowest stock threshold.
                    if isinstance(stock_level, (int, str)) and str(stock_level).isdigit():
                        if int(stock_level) >= min_stock_level:
                            # Implement filtering by product type for item_id queries.
                            item_matches_type = True
                            if product_type_lower:
                                # Retrieve the associated product for this item.
                                item_product_id = None
                                for prod in products:
                                    if item_id in prod.get("variants", {}):
                                        item_product_id = prod.get("product_id")
                                        break

                                if item_product_id:
                                    item_product_name = product_name_map.get(item_product_id, "")
                                    item_matches_type = any(
                                        ptype in item_product_name
                                        for ptype in product_type_lower
                                    )

                            if item_matches_type:
                                supplier_match["matching_items"].append({
                                    "item_id": item_id,
                                    "stock_level": stock_level,
                                    "numeric_stock_level": int(stock_level),
                                    "status": "available",
                                    "product_available": item_availability_map.get(item_id, False)
                                })

                    if supplier_match["matching_items"]:
                        matching_suppliers.append(supplier_match)
            else:
                # Product-specific search - retrieve all items associated with this product.
                candidate_items = []

                for stock_item_id, stock_level in item_stock.items():
                    # Bypass if the status is not included.
                    if stock_level in exclude_statuses:
                        continue

                    # Evaluate the availability filter exclusively when available_only is set to True.
                    if available_only:
                        item_is_available = item_availability_map.get(stock_item_id, False)
                        if not item_is_available:
                            continue

                    # Verify minimum inventory level.
                    if isinstance(stock_level, (int, str)) and str(stock_level).isdigit():
                        if int(stock_level) >= min_stock_level:
                            # Implement filtering by product type for each item.
                            item_matches_type = True
                            if product_type_lower:
                                # Identify the product associated with this item.
                                item_product_id = None
                                for prod in products:
                                    if stock_item_id in prod.get("variants", {}):
                                        item_product_id = prod.get("product_id")
                                        break

                                if item_product_id:
                                    item_product_name = product_name_map.get(item_product_id, "")
                                    item_matches_type = any(
                                        ptype in item_product_name
                                        for ptype in product_type_lower
                                    )

                            if item_matches_type:
                                candidate_items.append({
                                    "item_id": stock_item_id,
                                    "stock_level": stock_level,
                                    "numeric_stock_level": int(stock_level),
                                    "status": "available",
                                    "product_available": item_availability_map.get(stock_item_id, False)
                                })

                # Implement filtering based on stock level preferences.
                if candidate_items and stock_level_preference:
                    if stock_level_preference == "highest":
                        # Determine the highest inventory level.
                        max_stock = max(item["numeric_stock_level"] for item in candidate_items)
                        candidate_items = [item for item in candidate_items if item["numeric_stock_level"] == max_stock]
                    elif stock_level_preference == "lowest":
                        # Determine the lowest stock threshold.
                        min_stock = min(item["numeric_stock_level"] for item in candidate_items)
                        candidate_items = [item for item in candidate_items if item["numeric_stock_level"] == min_stock]

                supplier_match["matching_items"] = candidate_items

                if supplier_match["matching_items"]:
                    matching_suppliers.append(supplier_match)

        # Order by total available stock in descending order.
        for supplier in matching_suppliers:
            total_stock = sum(
                item["numeric_stock_level"] for item in supplier["matching_items"]
            )
            supplier["total_available_stock"] = total_stock

        matching_suppliers.sort(key=lambda x: x["total_available_stock"], reverse=True)

        result = {
            "status": "success",
            "search_criteria": {
                "product_id": product_id,
                "item_id": item_id,
                "min_stock_level": min_stock_level,
                "supplier_id_filter": supplier_id,
                "product_type_filter": product_type,
                "available_only": available_only,
                "filter_applied": product_type is not None or stock_level_preference is not None or available_only
            },
            "total_suppliers_found": len(matching_suppliers),
            "suppliers": matching_suppliers[:3] if not supplier_id else matching_suppliers  # Display all outcomes when filtering based on a particular supplier.
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_suppliers_by_product",
                "description": "Search suppliers by product availability and stock levels with optional supplier, product type filtering, stock level preference, and availability filtering",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string", "description": "Product identifier to search for"},
                        "item_id": {"type": "string", "description": "Specific item identifier to search for"},
                        "min_stock_level": {"type": "integer", "description": "Minimum stock level required", "default": 0},
                        "exclude_statuses": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Stock statuses to exclude from results",
                            "default": ["discontinued", "out_of_stock"]
                        },
                        "supplier_id": {"type": "string", "description": "Optional specific supplier ID to filter results (e.g., '#SUP0001')"},
                        "product_type": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of product types to filter by (e.g., ['laptop', 'bluetooth speaker', 't-shirt']). Matches product names containing these terms."
                        },
                        "stock_level_preference": {
                            "type": "string",
                            "description": "Optional preference for stock levels: 'highest' returns items with maximum stock, 'lowest' returns items with minimum stock",
                            "enum": ["highest", "lowest"]
                        },
                        "available_only": {
                            "type": "boolean",
                            "description": "Optional filter to show only items that are marked as available in the product catalog. When not specified, includes all items regardless of availability status.",
                            "default": False
                        }
                    }
                }
            }
        }
