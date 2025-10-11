# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateProductAvailability(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], product_id: str, item_id: str, available: bool = True, new_price: float = None) -> str:
        """
        Update product variant availability status and optionally price

        Writes to: products.json (updates variant availability and price)
        """
        products = list(data.get("products", {}).values())
        product_to_update = None
        product_index = None

        # Calculate the multiplication.
        for i, product in enumerate(products):
            if product.get("product_id") == product_id:
                product_to_update = product
                product_index = i
                break

        if not product_to_update:
            return json.dumps({"error": f"Product {product_id} not found", "status": "failed"})

        # Validation: Ensure item_id is present in product variants prior to adding to orders.
        variants = product_to_update.get("variants", {})
        if item_id not in variants:
            return json.dumps({
                "error": f"Item variant {item_id} not found in product {product_id}",
                "status": "failed"
            })

        variant_to_update = variants[item_id]
        old_availability = variant_to_update.get("available", False)
        old_price = variant_to_update.get("price", 0)

        # UPDATE OPERATION: Modify variant availability in products.json
        variant_to_update["available"] = available
        variant_to_update["last_updated"] = datetime.now().isoformat()

        # Guideline: Apply precise variant pricing from the product catalog - approved price adjustments.
        price_updated = False
        if new_price is not None:
            if new_price < 0:
                return json.dumps({"error": "Price cannot be negative", "status": "failed"})
            variant_to_update["price"] = new_price
            price_updated = True

        # Modify the product within the data structure.
        data["products"][product_index] = product_to_update

        result = {
            "status": "success",
            "product_id": product_id,
            "product_name": product_to_update.get("name"),
            "item_id": item_id,
            "availability_update": {
                "previous_available": old_availability,
                "new_available": available
            },
            "price_update": {
                "updated": price_updated,
                "previous_price": old_price,
                "new_price": new_price
            } if price_updated else {"updated": False},
            "variant_options": variant_to_update.get("options", {}),
            "last_updated": variant_to_update["last_updated"]
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_product_availability",
                "description": "Update product variant availability status and optionally price",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string", "description": "Product identifier"},
                        "item_id": {"type": "string", "description": "Product variant identifier"},
                        "available": {"type": "boolean", "description": "New availability status"},
                        "new_price": {"type": "number", "description": "New price (optional)"}
                    },
                    "required": ["product_id", "item_id"]
                }
            }
        }
