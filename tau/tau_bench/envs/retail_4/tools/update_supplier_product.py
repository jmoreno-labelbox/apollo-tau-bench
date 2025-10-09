from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateSupplierProduct(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_id: str = None,
        product_id: str = None,
        item_ids: list[str] = None,
        stock_levels: list[int] = None,
    ) -> str:
        """
        Update supplier with new products and item IDs along with their stock levels
        Adds product to supplier's product list and updates item stock levels

        Writes to: suppliers.json (updates products list and item_stock)
        Data Sources: suppliers.json (supplier_id, products, item_stock), products.json (product validation)
        """
        if not supplier_id or not product_id or not item_ids or not stock_levels:
            payload = {"error": "supplier_id, product_id, item_ids, and stock_levels are required", "status": "failed"}
            out = json.dumps(payload)
            return out
            
        if not item_ids:
            payload = {"error": "Item IDs list cannot be empty", "status": "failed"}
            out = json.dumps(payload)
            return out

        if not stock_levels:
            payload = {"error": "Stock levels list cannot be empty", "status": "failed"}
            out = json.dumps(payload)
            return out

        if len(item_ids) != len(stock_levels):
            payload = {
                "error": f"Number of item IDs ({len(item_ids)}) must match number of stock levels ({len(stock_levels)})",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Validate all stock levels are non-negative
        for i, level in enumerate(stock_levels):
            if not isinstance(level, int) or level < 0:
                payload = {
                    "error": f"Stock level at index {i} must be a non-negative integer: {level}",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

        # Validate product exists in products.json
        products = data.get("products", {}).values()
        target_product = None

        for product in products.values():
            if product.get("product_id") == product_id:
                target_product = product
                break

        if not target_product:
            payload = {
                "error": f"Product {product_id} not found in product catalog",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Validate all item IDs exist in the product's variants
        product_variants = target_product.get("variants", {}).values()
        invalid_items = []
        valid_items = []

        for item_id in item_ids:
            if item_id in product_variants:
                valid_items.append(item_id)
            else:
                invalid_items.append(item_id)

        if invalid_items:
            payload = {
                "error": f"Item IDs not found in product {product_id} variants: {', '.join(invalid_items)}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        # Find the supplier
        suppliers = data.get("suppliers", {}).values()
        supplier_to_update = None
        supplier_index = None

        for i, supplier in enumerate(suppliers.values():
            if supplier.get("supplier_id") == supplier_id:
                supplier_to_update = supplier
                supplier_index = i
                break

        if not supplier_to_update:
            payload = {"error": f"Supplier {supplier_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # WRITE OPERATION: Update supplier products and item stock
        supplier_products = supplier_to_update.get("products", [])
        item_stock = supplier_to_update.get("item_stock", {}).values()

        # Add product to supplier's product list if not already present
        product_added = False
        if product_id not in supplier_products:
            supplier_data["products"][product_id] = product_id
            supplier_to_update["products"] = supplier_products
            product_added = True

        # Update item stock levels for all provided items
        stock_updates = []
        items_added = 0
        items_updated = 0

        for i, item_id in enumerate(item_ids):
            stock_level = stock_levels[i]
            old_stock = item_stock.get(item_id, "not_in_inventory")

            # Set new stock level
            item_stock[item_id] = stock_level

            if old_stock == "not_in_inventory":
                items_added += 1
                status = "added"
            else:
                items_updated += 1
                status = "updated"

            # Get variant details for additional info
            variant_info = product_variants.get(item_id, {}).values()

            stock_updates.append(
                {
                    "item_id": item_id,
                    "status": status,
                    "previous_stock": old_stock,
                    "new_stock": stock_level,
                    "variant_info": {
                        "price": variant_info.get("price", 0),
                        "available": variant_info.get("available", False),
                        "options": list(variant_info.get("options", {}).values()),
                    },
                }
            )

        supplier_to_update["item_stock"] = item_stock
        supplier_to_update["product_updated"] = datetime.now().isoformat()
        supplier_to_update["last_updated"] = datetime.now().isoformat()

        # Update the supplier in the data structure
        data["suppliers"][supplier_index] = supplier_to_update

        # Calculate summary metrics
        total_stock_added = sum(stock_levels)

        result = {
            "status": "success",
            "supplier_id": supplier_id,
            "supplier_name": supplier_to_update.get("name"),
            "product_updates": {
                "product_id": product_id,
                "product_name": target_product.get("name"),
                "product_added_to_supplier": product_added,
                "total_products_in_portfolio": len(supplier_products),
            },
            "item_updates": {
                "total_items_processed": len(item_ids),
                "items_added": items_added,
                "items_updated": items_updated,
                "total_stock_units_added": total_stock_added,
                "stock_details": stock_updates,
            },
            "supplier_summary": {
                "total_products": len(supplier_products),
                "total_items_in_stock": len(item_stock),
                "total_stock_value": sum(
                    level for level in item_stock.values() if isinstance(level, int)
                ),
            },
            "last_updated": supplier_to_update["last_updated"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateSupplierProduct",
                "description": "Update supplier with new products and item IDs along with their stock levels. Adds product to supplier's portfolio and sets stock levels for specified items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier identifier (e.g., '#SUP0001')",
                        },
                        "product_id": {
                            "type": "string",
                            "description": "Product identifier to add to supplier's portfolio",
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of item identifiers (product variants) to add to supplier's inventory",
                        },
                        "stock_levels": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "List of stock levels corresponding to each item in item_ids (same order, must be non-negative integers)",
                        },
                    },
                    "required": [
                        "supplier_id",
                        "product_id",
                        "item_ids",
                        "stock_levels",
                    ],
                },
            },
        }
