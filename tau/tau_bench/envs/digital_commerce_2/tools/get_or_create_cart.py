# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrCreateCart(Tool):
    """Return existing cart for a contact_id, or create a new empty cart if none exists."""

    @staticmethod
    def invoke(data: Dict[str, Any], contact_id: Any) -> str:
        if not contact_id:
            return json.dumps({"error": "Missing required field: contact_id"}, indent=2)
        carts = data.setdefault("carts", [])
        for cart in carts:
            if cart.get("contact_id") == contact_id:
                return json.dumps(cart, indent=2)
        cart_id = get_next_cart_id(data)
        new_cart = {
            "cart_id": cart_id,
            "contact_id": contact_id,
            "last_updated_at": get_current_timestamp(),
        }
        carts.append(new_cart)
        return json.dumps(new_cart, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_or_create_cart",
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
