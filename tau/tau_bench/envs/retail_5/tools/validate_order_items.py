from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class ValidateOrderItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_ids: list[str] = None, quantities: list[int] = None) -> str:
        if not item_ids:
            payload = {"error": "item_ids is required"}
            out = json.dumps(payload)
            return out

        if quantities and len(quantities) != len(item_ids):
            payload = {"error": "quantities list must match item_ids length"}
            out = json.dumps(payload)
            return out

        products = data["products"]
        suppliers = data["suppliers"]
        validation_results = []

        for i, item_id in enumerate(item_ids):
            quantity = quantities[i] if quantities else 1
            product_variant, product_name, product = None, None, None

            for p in products.values():
                if item_id in p["variants"]:
                    product_variant = p["variants"][item_id]
                    product_name = p["name"]
                    product = p
                    break

            if not product_variant:
                validation_results.append(
                    {"item_id": item_id, "valid": False, "error": "Item not found"}
                )
                continue

            if not product_variant["available"]:
                validation_results.append(
                    {"item_id": item_id, "valid": False, "error": "Item not available"}
                )
                continue

            supplier = next(
                (s for s in suppliers.values() if s["supplier_id"] == product["supplier_id"]),
                None,
            )
            stock = supplier["item_stock"].get(item_id) if supplier else None
            sufficient_stock = isinstance(stock, int) and stock >= quantity

            validation_results.append(
                {
                    "item_id": item_id,
                    "product_name": product_name,
                    "price": product_variant["price"],
                    "requested_quantity": quantity,
                    "valid": True,
                    "sufficient_stock": sufficient_stock,
                    "options": product_variant["options"],
                }
            )
        payload = validation_results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validateOrderItems",
                "description": "Validate if items are available for ordering and check stock levels.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of item IDs to validate",
                        },
                        "quantities": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Corresponding quantities for each item",
                        },
                    },
                    "required": ["item_ids"],
                },
            },
        }
