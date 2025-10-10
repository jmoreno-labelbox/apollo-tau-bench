# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateOrderItems(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], item_list: List[Dict[str, Any]], allocate_orders = False) -> str:
        """
        Validate all items in an order before processing
        """
        products = list(data.get("products", {}).values())
        validated_items = []
        total_order_value = 0.0

        # Requirement: All items in multi-item orders must be in stock prior to confirmation.
        for item in item_list:
            item_id = item.get("item_id")
            quantity = item.get("quantity", 1)

            # Verification: Ensure item_id is present in product variants prior to adding to orders.
            variant_found = None
            product_found = None

            for product in products:
                variants = product.get("variants", {})
                if item_id in variants:
                    variant_found = variants[item_id]
                    product_found = product
                    break

            if not variant_found:
                return json.dumps({
                    "error": f"Item {item_id} not found in catalog",
                    "status": "failed"
                })

            # Condition: Verify product availability prior to allocation - do not allocate items that are not in stock.
            if allocate_orders:
                if not variant_found.get("available", False):
                    print(f"Item {item_id} ({product_found.get('name')}) is not available")
                    return json.dumps({
                        "error": f"Item {item_id} ({product_found.get('name')}) is not available",
                        "status": "failed"
                    })

            # Policy: Apply the precise variant pricing from the product catalog - unauthorized price changes are prohibited.
            unit_price = variant_found.get("price", 0)
            item_total = unit_price * quantity
            total_order_value += item_total

            validated_items.append({
                "item_id": item_id,
                "product_name": product_found.get("name"),
                "quantity": quantity,
                "unit_price": unit_price,
                "item_total": item_total,
                "options": variant_found.get("options", {}),
                "availability": variant_found.get("available", False)
            })

        # Requirement: Ensure data consistency: total order amount should equal the sum of item prices.
        result = {
            "status": "success",
            "validated_items": validated_items,
            "total_items": len(validated_items),
            "total_order_value": total_order_value,
            "requires_verification": total_order_value > 1000.0
        }

        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_order_items",
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
                                    "quantity": {"type": "integer"}
                                },
                                "required": ["item_id", "quantity"]
                            },
                            "description": "List of items to validate",
                            "allocate_orders": {"tuype": "boolean", "default": True, "description": "Flag to indicate if items should be allocated for orders"}
                        }
                    },
                    "required": ["item_list"]
                }
            }
        }
