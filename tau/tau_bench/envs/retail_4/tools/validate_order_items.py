from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ValidateOrderItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_list: list[dict[str, Any]], allocate_orders: bool = False) -> str:
        """
        Validate all items in an order before processing
        """
        products = data.get("products", {}).values()
        validated_items = []
        total_order_value = 0.0

        # Rule: Multi-item orders need all items available before confirmation
        for item in item_list:
            item_id = item.get("item_id")
            quantity = item.get("quantity", 1)

            # Rule: Confirm item_id exists in product variants before including in orders
            variant_found = None
            product_found = None

            for product in products.values():
                variants = product.get("variants", {}).values()
                if item_id in variants:
                    variant_found = variants[item_id]
                    product_found = product
                    break

            if not variant_found:
                payload = {
                    "error": f"Item {item_id} not found in catalog",
                    "status": "failed",
                }
                out = json.dumps(payload)
                return out

            # Rule: Check product availability status before allocation - never allocate unavailable items
            if allocate_orders:
                if not variant_found.get("available", False):
                    print(
                        f"Item {item_id} ({product_found.get('name')}) is not available"
                    )
                    payload = {
                        "error": f"Item {item_id} ({product_found.get('name')}) is not available",
                        "status": "failed",
                    }
                    out = json.dumps(payload)
                    return out

            # Rule: Use exact variant pricing from product catalog - no unauthorized price modifications
            unit_price = variant_found.get("price", 0)
            item_total = unit_price * quantity
            total_order_value += item_total

            validated_items.append(
                {
                    "item_id": item_id,
                    "product_name": product_found.get("name"),
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "item_total": item_total,
                    "options": list(variant_found.get("options", {}).values()),
                    "availability": variant_found.get("available", False),
                }
            )

        # Rule: Maintain data integrity: order totals must match sum of item prices
        result = {
            "status": "success",
            "validated_items": validated_items,
            "total_items": len(validated_items),
            "total_order_value": total_order_value,
            "requires_verification": total_order_value > 1000.0,
        }
        payload = result
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateOrderItems",
                "description": "Validate all items in order for availability and pricing before processing",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "item_id": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["item_id", "quantity"],
                            },
                            "description": "List of items to validate",
                        },
                        "allocate_orders": {
                            "type": "boolean",
                            "default": False,
                            "description": "Flag to indicate if items should be allocated for orders",
                        },
                    },
                    "required": ["item_list"],
                },
            },
        }
