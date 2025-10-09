from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetOrCreateCartForContact(Tool):
    def invoke(
        data: dict[str, Any],
        carts: list[dict[str, Any]],
        contact_id: Any = None
    ) -> str:
        contact_id = _idstr(contact_id)
        cart = next(
            (c for c in carts if f"{c.get('contact_id')}" == f"{contact_id}"), None
        )
        if not cart:
            new_id = _next_numeric_id(carts, "cart_id")
            cart = {
                "cart_id": new_id,
                "contact_id": contact_id,
                "last_updated_at": "FIXED-TIME",
            }
            carts.append(cart)
        payload = {"cart_id": cart["cart_id"]}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOrCreateCartForContact",
                "description": "Gets existing cart for a contact or creates a new deterministic one.",
                "parameters": {
                    "type": "object",
                    "properties": {"contact_id": {"type": "string"}},
                    "required": ["contact_id"],
                },
            },
        }
