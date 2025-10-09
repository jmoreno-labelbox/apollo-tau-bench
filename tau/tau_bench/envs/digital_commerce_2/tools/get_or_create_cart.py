from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class GetOrCreateCart(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], contact_id: Any) -> str:
        pass
        #1) Confirm
        if not contact_id:
            payload = {"error": "Missing required field: contact_id"}
            out = json.dumps(payload, indent=2)
            return out
        carts = data.setdefault("carts", [])
        for cart in carts:
            if cart.get("contact_id") == contact_id:
                payload = cart
                out = json.dumps(payload, indent=2)
                return out
        cart_id = get_next_cart_id(data)
        new_cart = {
            "cart_id": cart_id,
            "contact_id": contact_id,
            "last_updated_at": get_current_timestamp(),
        }
        data["carts"][new_cart["cart_id"]] = new_cart
        payload = new_cart
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOrCreateCart",
                "description": "Return existing cart for contact_id, or create a new empty cart if none exists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {
                            "type": "string",
                            "description": "The contact_id that owns the cart.",
                        }
                    },
                    "required": ["contact_id"],
                },
            },
        }
