# Sierra copyright notice

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSupplierByProduct(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], product_ids: List[str], product_type: List[str] = None) -> str:
        """
        Get suppliers associated with specified product IDs, optionally filtered by product type

        Data Sources: suppliers.json (supplier_id, name, products, contact_info), products.json (product names for filtering)
        """
        if not product_ids:
            return json.dumps({"error": "Product IDs list cannot be empty", "status": "failed"})

        # Retrieve product details for type-based filtering.
        products = list(data.get("products", {}).values())
        product_name_map = {}
        for product in products:
            product_id = product.get("product_id")
            product_name = product.get("name", "").lower()
            if product_id:
                product_name_map[product_id] = product_name

        # Transform product_type to lowercase for uniform matching regardless of case.
        product_type_lower = []
        if product_type:
            product_type_lower = [ptype.lower() for ptype in product_type]

        # Narrow down product_ids based on the specified product_type.
        filtered_product_ids = []
        if product_type_lower:
            for product_id in product_ids:
                product_name = product_name_map.get(product_id, "")
                if product_name:
                    type_matches = any(
                        ptype in product_name
                        for ptype in product_type_lower
                    )
                    if type_matches:
                        filtered_product_ids.append(product_id)
        else:
            filtered_product_ids = product_ids

        if not filtered_product_ids:
            return json.dumps({
                "status": "success",
                "search_criteria": {
                    "requested_product_ids": product_ids,
                    "product_type_filter": product_type,
                    "filter_applied": product_type is not None
                },
                "filtered_product_ids": filtered_product_ids,
                "product_supplier_mapping": {},
                "message": "No products matched the specified product type filter"
            })

        suppliers = data.get("suppliers", [])
        matching_suppliers = []
        product_supplier_map = {}

        # Scan all suppliers to identify matches for the selected products.
        for supplier in suppliers:
            supplier_id = supplier.get("supplier_id")
            supplier_name = supplier.get("name")
            supplier_products = supplier.get("products", [])
            contact_info = supplier.get("contact_info", {})

            # Verify the products that this supplier offers based on the applied filters.
            matching_products = []
            for product_id in filtered_product_ids:
                if product_id in supplier_products:
                    matching_products.append(product_id)

                    # Create a mapping of products to their respective suppliers.
                    if product_id not in product_supplier_map:
                        product_supplier_map[product_id] = []
                    product_supplier_map[product_id].append({
                        "supplier_id": supplier_id,
                        "supplier_name": supplier_name
                    })

            # Incorporate any products from the supplier that match.
            if matching_products:
                supplier_info = {
                    "supplier_id": supplier_id,
                    "supplier_name": supplier_name,
                    "contact_info": contact_info,
                    "matching_products": matching_products,
                    "total_matching_products": len(matching_products),
                    "performance_metrics": supplier.get("performance_metrics", {}),
                    "last_updated": supplier.get("last_updated", "Never")
                }

                # Incorporate stock details for corresponding products if present.
                item_stock = supplier.get("item_stock", {})
                if item_stock:
                    stock_summary = {
                        "total_items_in_stock": len(item_stock),
                        "available_items": 0,
                        "out_of_stock_items": 0,
                        "discontinued_items": 0
                    }

                    for stock_level in item_stock.values():
                        if stock_level == "out_of_stock":
                            stock_summary["out_of_stock_items"] += 1
                        elif stock_level == "discontinued":
                            stock_summary["discontinued_items"] += 1
                        elif isinstance(stock_level, (int, str)) and str(stock_level).isdigit():
                            stock_summary["available_items"] += 1

                    supplier_info["stock_summary"] = stock_summary

                matching_suppliers.append(supplier_info)

        # Identify items that lack associated suppliers.
        products_not_found = []
        for product_id in filtered_product_ids:
            if product_id not in product_supplier_map:
                products_not_found.append(product_id)

        # Order suppliers based on the count of corresponding products (in descending order).
        matching_suppliers.sort(key=lambda x: x["total_matching_products"], reverse=True)

        result = {
            "status": "success",
            "search_criteria": {
                "requested_product_ids": product_ids,
                "product_type_filter": product_type,
                "filter_applied": product_type is not None
            },
            "filtered_product_ids": filtered_product_ids,
            "supplier_results": {
                "total_suppliers_found": len(matching_suppliers),
                "suppliers": matching_suppliers
            },
            "product_supplier_mapping": product_supplier_map,
            "products_without_suppliers": products_not_found,
            "coverage_summary": {
                "products_with_suppliers": len(filtered_product_ids) - len(products_not_found),
                "products_without_suppliers": len(products_not_found),
                "coverage_percentage": round(((len(filtered_product_ids) - len(products_not_found)) / len(filtered_product_ids) * 100), 1) if filtered_product_ids else 0
            }
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_supplier_by_product",
                "description": "Get suppliers associated with specified product IDs, optionally filtered by product type",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of product identifiers to find suppliers for (e.g., ['PROD001', 'PROD002'])"
                        },
                        "product_type": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional list of product types to filter by (e.g., ['laptop', 'bluetooth speaker', 't-shirt']). Matches product names containing these terms."
                        }
                    },
                    "required": ["product_ids"]
                }
            }
        }
