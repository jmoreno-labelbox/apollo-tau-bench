# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductItemsPerSupplier(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str, stock_available: bool = None, product_type = None) -> str:
        """
        Get products and items for a specific supplier with optional stock filtering and product type filtering
        Maps each item to its corresponding product

        Data Sources: suppliers.json (supplier_id, products, item_stock), products.json (product details, variants)
        """
        # Find the specified supplier
        suppliers = data.get("suppliers", [])
        target_supplier = None

        for supplier in suppliers:
            if supplier.get("supplier_id") == supplier_id:
                target_supplier = supplier
                break

        if not target_supplier:
            return json.dumps({
                "error": f"Supplier {supplier_id} not found",
                "status": "failed"
            })

        # Get product information for mapping items to products
        products = list(data.get("products", {}).values())
        product_details_map = {}
        item_to_product_map = {}

        # Handle product_type parameter - convert string to list if needed
        product_type_list = []
        if product_type is not None:
            if isinstance(product_type, str):
                product_type_list = [product_type]
            elif isinstance(product_type, list):
                product_type_list = product_type
            else:
                return json.dumps({
                    "error": "product_type must be a string or list of strings",
                    "status": "failed"
                })

        # Convert product_type to lowercase for case-insensitive matching
        product_type_lower = []
        if product_type_list:
            product_type_lower = [ptype.lower() for ptype in product_type_list]

        for product in products:
            product_id = product.get("product_id")
            product_name = product.get("name", "").lower()

            if product_id:
                # Apply product type filter if specified
                if product_type_lower:
                    type_matches = any(
                        ptype in product_name
                        for ptype in product_type_lower
                    )
                    if not type_matches:
                        continue  # Skip this product if it doesn't match the type filter

                product_details_map[product_id] = {
                    "product_id": product_id,
                    "name": product.get("name"),
                    "category": product.get("category"),
                    "variants": product.get("variants", {})
                }

                # Map each item to its product
                variants = product.get("variants", {})
                for item_id in variants.keys():
                    item_to_product_map[item_id] = product_id

        # Get supplier information
        supplier_products = target_supplier.get("products", [])
        supplier_item_stock = target_supplier.get("item_stock", {})

        # Process items based on stock_available filter and product type filter
        filtered_items = {}
        stock_summary = {
            "total_items": len(supplier_item_stock),
            "available_items": 0,
            "out_of_stock_items": 0,
            "discontinued_items": 0,
            "unmapped_items": 0,
            "filtered_out_items": 0
        }

        for item_id, stock_level in supplier_item_stock.items():
            # Apply stock filter
            include_item = True

            if stock_available is True:
                # Only include items with numeric stock levels
                include_item = isinstance(stock_level, (int, str)) and str(stock_level).isdigit() and int(stock_level) > 0
            elif stock_available is False:
                # Only include out_of_stock or discontinued items
                include_item = stock_level in ["out_of_stock", "discontinued"]
            # If stock_available is None, include all items

            # Update stock summary
            if stock_level == "out_of_stock":
                stock_summary["out_of_stock_items"] += 1
            elif stock_level == "discontinued":
                stock_summary["discontinued_items"] += 1
            elif isinstance(stock_level, (int, str)) and str(stock_level).isdigit():
                stock_summary["available_items"] += 1

            if include_item:
                # Find which product this item belongs to
                product_id = item_to_product_map.get(item_id)

                if product_id:
                    # Check if product passes the type filter (it should already be in product_details_map if it passes)
                    if product_id in product_details_map:
                        if product_id not in filtered_items:
                            filtered_items[product_id] = []

                        # Get item details from product variants
                        product_info = product_details_map.get(product_id, {})
                        variants = product_info.get("variants", {})
                        item_variant_info = variants.get(item_id, {})

                        filtered_items[product_id].append({
                            "item_id": item_id,
                            "stock_level": stock_level,
                            "numeric_stock_level": int(stock_level) if isinstance(stock_level, (int, str)) and str(stock_level).isdigit() else 0,
                            "stock_status": "available" if isinstance(stock_level, (int, str)) and str(stock_level).isdigit() and int(stock_level) > 0 else stock_level,
                            "variant_info": {
                                "price": item_variant_info.get("price", 0),
                                "available": item_variant_info.get("available", False),
                                "options": item_variant_info.get("options", {})
                            }
                        })
                    else:
                        # Item belongs to a product that was filtered out by product type
                        stock_summary["filtered_out_items"] += 1
                else:
                    # Item not mapped to any product
                    stock_summary["unmapped_items"] += 1
                    if "unmapped_items" not in filtered_items:
                        filtered_items["unmapped_items"] = []

                    filtered_items["unmapped_items"].append({
                        "item_id": item_id,
                        "stock_level": stock_level,
                        "numeric_stock_level": int(stock_level) if isinstance(stock_level, (int, str)) and str(stock_level).isdigit() else 0,
                        "stock_status": "available" if isinstance(stock_level, (int, str)) and str(stock_level).isdigit() and int(stock_level) > 0 else stock_level,
                        "variant_info": {
                            "price": 0,
                            "available": False,
                            "options": {}
                        }
                    })

        # Build detailed product information (only for products that match the type filter)
        products_with_items = []

        # Instead of iterating through supplier_products, iterate through filtered_items
        for product_id, product_items in filtered_items.items():
            # Skip unmapped_items key
            if product_id == "unmapped_items":
                continue

            # Only process products that are in our filtered product_details_map
            if product_id in product_details_map:
                product_info = product_details_map.get(product_id)

                # Only include products that have items after filtering
                if product_items:
                    # Calculate product-level stock summary
                    product_stock_summary = {
                        "total_items": len(product_items),
                        "available_items": len([item for item in product_items if item["stock_status"] == "available"]),
                        "out_of_stock_items": len([item for item in product_items if item["stock_status"] == "out_of_stock"]),
                        "discontinued_items": len([item for item in product_items if item["stock_status"] == "discontinued"]),
                        "total_stock": sum(item["numeric_stock_level"] for item in product_items)
                    }

                    products_with_items.append({
                        "product_id": product_id,
                        "product_name": product_info["name"],
                        "product_category": product_info["category"],
                        "stock_summary": product_stock_summary,
                        "items": product_items
                    })

        # Add unmapped items if any exist
        unmapped_items = filtered_items.get("unmapped_items", [])

        result = {
            "status": "success",
            "products_with_items": products_with_items
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_items_per_supplier",
                "description": "Get products and items for a specific supplier with optional stock filtering and product type filtering. Maps each item to its corresponding product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier identifier (e.g., '#SUP0001')"
                        },
                        "stock_available": {
                            "type": "boolean",
                            "description": "Optional stock filter: true = only items with stock, false = only out_of_stock/discontinued items, null/undefined = all items"
                        },
                        "product_type": {
                            "oneOf": [
                                {"type": "string"},
                                {
                                    "type": "array",
                                    "items": {"type": "string"}
                                }
                            ],
                            "description": "Optional product type(s) to filter by. Can be a single string (e.g., 'headphones') or list of strings (e.g., ['smartphone', 'laptop']). Matches product names containing these terms."
                        }
                    },
                    "required": ["supplier_id"]
                }
            }
        }
