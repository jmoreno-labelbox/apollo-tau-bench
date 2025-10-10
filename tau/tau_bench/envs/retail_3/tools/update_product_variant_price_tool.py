# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateProductVariantPriceTool(Tool):
    """
    Update the price of an existing product variant in products.json.

    Behavior:
    - Validates that the provided product_id exists in products.json.
    - Validates that the provided item_id exists within product['variants'].
    - Overwrites the 'price' field with the new positive numeric value.
    - Does NOT create new products or variants; strictly updates an existing variant's price.

    Input (kwargs):
        product_id (str, required)
        item_id (str, required)
        new_price (float, required, > 0)

    Output:
        JSON string with {"product_id","item_id","old_price","new_price"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_id = kwargs.get("product_id")
        item_id = kwargs.get("item_id")
        new_price = kwargs.get("new_price")

        # Validação básica
        if not product_id or not item_id or new_price is None:
            return json.dumps({"error": "product_id, item_id and new_price are required"}, indent=2)
        try:
            price_val = float(new_price)
            if price_val <= 0:
                return json.dumps({"error": "new_price must be a positive number"}, indent=2)
        except Exception:
            return json.dumps({"error": "new_price must be numeric"}, indent=2)

        products = list(data.get("products", {}).values())
        product = next((p for p in products if p.get("product_id") == product_id), None)
        if not product:
            return json.dumps(
                {"error": f"product_id '{product_id}' not found in products"}, indent=2
            )

        variants = product.get("variants") or {}
        variant = variants.get(item_id)
        if not variant:
            return json.dumps(
                {"error": f"item_id '{item_id}' not found under product_id '{product_id}'"},
                indent=2,
            )

        old_price = variant.get("price")
        variant["price"] = price_val
        product["variants"][item_id] = variant  # redundante, mas mantém simetria

        return json.dumps(
            {
                "product_id": product_id,
                "item_id": item_id,
                "old_price": old_price,
                "new_price": price_val,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_product_variant_price",
                "description": "Update the 'price' field of an existing product variant in products.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "new_price": {"type": "number", "minimum": 0},
                    },
                    "required": ["product_id", "item_id", "new_price"],
                },
            },
        }
