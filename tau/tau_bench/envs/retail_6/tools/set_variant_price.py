from tau_bench.envs.tool import Tool
import json
from typing import Any

class SetVariantPrice(Tool):
    """Assign a specific numeric value as the price for a variant."""

    @staticmethod
    def invoke(data, item_id=None, price=None) -> str:
        if item_id is None or price is None:
            payload = {"error": "item_id and price are required"}
            out = json.dumps(payload, indent=2)
            return out
        prod, variant = _find_product_by_item(data, item_id)
        if not prod:
            payload = {"error": f"item_id {item_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        prod["variants"][item_id]["price"] = float(price)
        payload = {"success": True, "item_id": item_id, "price": float(price)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "setVariantPrice",
                "description": "Set a specific variant price.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"},
                        "price": {"type": "number"},
                    },
                    "required": ["item_id", "price"],
                },
            },
        }
