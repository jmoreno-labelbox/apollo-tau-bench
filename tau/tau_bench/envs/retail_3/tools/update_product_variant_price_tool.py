from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateProductVariantPriceTool(Tool):
    """
    Modify the price of an existing product variant in products.json.

    Behavior:
    - Confirms that the specified product_id exists in products.json.
    - Confirms that the specified item_id exists within product['variants'].
    - Replaces the 'price' field with the new positive numeric value.
    - Does NOT create new products or variants; strictly updates the price of an existing variant.

    Input (kwargs):
        product_id (str, required)
        item_id (str, required)
        new_price (float, required, > 0)

    Output:
        JSON string with {"product_id","item_id","old_price","new_price"} or {"error": ...}.
    """

    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None, item_id: str = None, new_price: Any = None) -> str:
        # Basic validation
        if not product_id or not item_id or new_price is None:
            payload = {"error": "product_id, item_id and new_price are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        try:
            price_val = float(new_price)
            if price_val <= 0:
                payload = {"error": "new_price must be a positive number"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        except Exception:
            payload = {"error": "new_price must be numeric"}
            out = json.dumps(payload, indent=2)
            return out

        products = data.get("products", [])
        product = next((p for p in products if p.get("product_id") == product_id), None)
        if not product:
            payload = {"error": f"product_id '{product_id}' not found in products"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        variants = product.get("variants") or {}
        variant = variants.get(item_id)
        if not variant:
            payload = {
                    "error": f"item_id '{item_id}' not found under product_id '{product_id}'"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        old_price = variant.get("price")
        variant["price"] = price_val
        product["variants"][item_id] = variant  # redundant, but maintains symmetry
        payload = {
                "product_id": product_id,
                "item_id": item_id,
                "old_price": old_price,
                "new_price": price_val,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProductVariantPrice",
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
