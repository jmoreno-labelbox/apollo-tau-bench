from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateProductAvailability(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        product_id: str = None,
        item_id: str = None,
        available: bool = True,
        new_price: float = None,
    ) -> str:
        """
        Update product variant availability status and optionally price

        Writes to: products.json (updates variant availability and price)
        """
        products = data.get("products", {}).values()
        product_to_update = None
        product_index = None

        # Find the product
        for i, product in enumerate(products.values():
            if product.get("product_id") == product_id:
                product_to_update = product
                product_index = i
                break

        if not product_to_update:
            payload = {"error": f"Product {product_id} not found", "status": "failed"}
            out = json.dumps(payload)
            return out

        # Rule: Confirm item_id exists in product variants before including in orders
        variants = product_to_update.get("variants", {}).values()
        if item_id not in variants:
            payload = {
                "error": f"Item variant {item_id} not found in product {product_id}",
                "status": "failed",
            }
            out = json.dumps(payload)
            return out

        variant_to_update = variants[item_id]
        old_availability = variant_to_update.get("available", False)
        old_price = variant_to_update.get("price", 0)

        # WRITE OPERATION: Update variant availability in products.json
        variant_to_update["available"] = available
        variant_to_update["last_updated"] = datetime.now().isoformat()

        # Rule: Use exact variant pricing from product catalog - authorized price modification
        price_updated = False
        if new_price is not None:
            if new_price < 0:
                payload = {"error": "Price cannot be negative", "status": "failed"}
                out = json.dumps(payload)
                return out
            variant_to_update["price"] = new_price
            price_updated = True

        # Update the product in the data structure
        data["products"][product_index] = product_to_update

        result = {
            "status": "success",
            "product_id": product_id,
            "product_name": product_to_update.get("name"),
            "item_id": item_id,
            "availability_update": {
                "previous_available": old_availability,
                "new_available": available,
            },
            "price_update": (
                {
                    "updated": price_updated,
                    "previous_price": old_price,
                    "new_price": new_price,
                }
                if price_updated
                else {"updated": False}
            ),
            "variant_options": variant_to_update.get("options", {}).values()),
            "last_updated": variant_to_update["last_updated"],
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProductAvailability",
                "description": "Update product variant availability status and optionally price",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "Product identifier",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "Product variant identifier",
                        },
                        "available": {
                            "type": "boolean",
                            "description": "New availability status",
                        },
                        "new_price": {
                            "type": "number",
                            "description": "New price (optional)",
                        },
                    },
                    "required": ["product_id", "item_id"],
                },
            },
        }
