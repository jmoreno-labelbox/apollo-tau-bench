from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class CreateCart(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], cart_id: Any, contact_id: Any, created_at: Any
    ) -> str:
        cart_id = _as_id(cart_id)
        contact_id = _as_id(contact_id)
        if not cart_id or not contact_id or not created_at:
            return _err("cart_id, contact_id, created_at are required.")
        carts = data.setdefault("carts", [])
        if any(_as_id(c.get("cart_id")) == cart_id for c in carts):
            existing = next(c for c in carts if _as_id(c.get("cart_id")) == cart_id)
            payload = existing
            out = json.dumps(payload, indent=2)
            return out
        contacts = data.get("contacts", [])
        contact = next(
            (c for c in contacts if _as_id(c.get("contact_id")) == contact_id), None
        )
        if not contact:
            return _err("Contact not found.")
        cart = {
            "cart_id": cart_id,
            "contact_id": contact_id,
            "account_id": contact.get("account_id"),
            "applied_offer_id": None,
            "override_pricebook_id": None,
            "last_updated_at": created_at,
        }
        carts.append(cart)
        payload = cart
        out = json.dumps(payload, indent=2)
        return out
            

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCart",
                "description": "Create a cart for a contact at a deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "contact_id": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["cart_id", "contact_id", "created_at"],
                },
            },
        }
