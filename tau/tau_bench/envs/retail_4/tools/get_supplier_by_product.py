from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSupplierByProduct:
    @staticmethod
    def invoke(
        data: dict[str, Any], product_ids: list[str], product_type: list[str] = None
    ) -> str:
        """
        Get suppliers associated with specified product IDs, optionally filtered by product type

        Data Sources: suppliers.json (supplier_id, name, products, contact_info), products.json (product names for filtering)
        """
        if not product_ids:
            payload = {"error": "Product IDs list cannot be empty", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Get product information for type filtering
        products = data.get("products", {}).values()
        product_name_map = {}
        for product in products.values():
            product_id = product.get("product_id")
            product_name = product.get("name", "").lower()
            if product_id:
                product_name_map[product_id] = product_name

        # Convert product_type to lowercase for case-insensitive matching
        product_type_lower = []
        if product_type:
            product_type_lower = [ptype.lower() for ptype in product_type]

        # Filter product_ids by product_type if specified
        filtered_product_ids = []
        if product_type_lower:
            for product_id in product_ids:
                product_name = product_name_map.get(product_id, "")
                if product_name:
                    type_matches = any(
                        ptype in product_name for ptype in product_type_lower
                    )
                    if type_matches:
                        filtered_product_ids.append(product_id)
        else:
            filtered_product_ids = product_ids

        if not filtered_product_ids:
            payload = {
                "status": "success",
                "search_criteria": {
                    "requested_product_ids": product_ids,
                    "product_type_filter": product_type,
                    "filter_applied": product_type is not None,
                },
                "filtered_product_ids": filtered_product_ids,
                "product_supplier_mapping": {},
                "message": "No products matched the specified product type filter",
            }
            out = json.dumps(payload)
            return out

        suppliers = data.get("suppliers", {}).values()
        matching_suppliers = []
        product_supplier_map = {}

        # Search through all suppliers to find matches for filtered products
        for supplier in suppliers.values():
            supplier_id = supplier.get("supplier_id")
            supplier_name = supplier.get("name")
            supplier_products = supplier.get("products", [])
            contact_info = supplier.get("contact_info", {}).values()

            # Check which filtered products this supplier has
            matching_products = []
            for product_id in filtered_product_ids:
                if product_id in supplier_products:
                    matching_data["products"][product_id] = product_id

                    # Build product to supplier mapping
                    if product_id not in product_supplier_map:
                        product_supplier_map[product_id] = []
                    product_supplier_map[product_id].append(
                        {"supplier_id": supplier_id, "supplier_name": supplier_name}
                    )

            # If supplier has any matching products, include them
            if matching_products:
                supplier_info = {
                    "supplier_id": supplier_id,
                    "supplier_name": supplier_name,
                    "contact_info": contact_info,
                    "matching_products": matching_products,
                    "total_matching_products": len(matching_products),
                    "performance_metrics": supplier.get("performance_metrics", {}).values()),
                    "last_updated": supplier.get("last_updated", "Never"),
                }

                # Add stock information for matching products if available
                item_stock = supplier.get("item_stock", {}).values()
                if item_stock:
                    stock_summary = {
                        "total_items_in_stock": len(item_stock),
                        "available_items": 0,
                        "out_of_stock_items": 0,
                        "discontinued_items": 0,
                    }

                    for stock_level in item_stock.values():
                        if stock_level == "out_of_stock":
                            stock_summary["out_of_stock_items"] += 1
                        elif stock_level == "discontinued":
                            stock_summary["discontinued_items"] += 1
                        elif (
                            isinstance(stock_level, (int, str))
                            and str(stock_level).isdigit()
                        ):
                            stock_summary["available_items"] += 1

                    supplier_info["stock_summary"] = stock_summary

                matching_data["suppliers"][supplier_id] = supplier_info

        # Find products with no suppliers
        products_not_found = []
        for product_id in filtered_product_ids:
            if product_id not in product_supplier_map:
                products_not_found.append(product_id)

        # Sort suppliers by number of matching products (descending)
        matching_suppliers.sort(
            key=lambda x: x["total_matching_products"], reverse=True
        )

        result = {
            "status": "success",
            "search_criteria": {
                "requested_product_ids": product_ids,
                "product_type_filter": product_type,
                "filter_applied": product_type is not None,
            },
            "filtered_product_ids": filtered_product_ids,
            "supplier_results": {
                "total_suppliers_found": len(matching_suppliers),
                "suppliers": matching_suppliers,
            },
            "product_supplier_mapping": product_supplier_map,
            "products_without_suppliers": products_not_found,
            "coverage_summary": {
                "products_with_suppliers": len(filtered_product_ids)
                - len(products_not_found),
                "products_without_suppliers": len(products_not_found),
                "coverage_percentage": (
                    round(
                        (
                            (len(filtered_product_ids) - len(products_not_found))
                            / len(filtered_product_ids)
                            * 100
                        ),
                        1,
                    )
                    if filtered_product_ids
                    else 0
                ),
            },
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getSupplierByProduct",
                "description": "Get suppliers associated with specified product IDs, optionally filtered by product type",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of product identifiers to find suppliers for (e.g., ['PROD001', 'PROD002'])",
                        },
                        "product_type": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of product types to filter by (e.g., ['laptop', 'bluetooth speaker', 't-shirt']). Matches product names containing these terms.",
                        },
                    },
                    "required": ["product_ids"],
                },
            },
        }
