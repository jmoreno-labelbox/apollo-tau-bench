# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCart(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], contact_id: str, created_at: str) -> str:
        carts = data.setdefault("carts", [])
        nums = []
        for c in carts:
            existing = _as_id(c.get("cart_id"))
            if existing is not None and str(existing).isdigit():
                nums.append(int(existing))
        next_id = (max(nums) + 1) if nums else 5001
        cart_id = str(next_id)

        contact_id = _as_id(contact_id)
        if not cart_id or not contact_id or not created_at:
            return _err("cart_id, contact_id, created_at are required.")
        carts = data.setdefault("carts", [])
        if any(_as_id(c.get("cart_id")) == cart_id for c in carts):
            existing = next(c for c in carts if _as_id(c.get("cart_id")) == cart_id)
            return json.dumps(existing, indent=2)
        contacts = data.get("contacts", [])
        contact = next((c for c in contacts if _as_id(c.get("contact_id")) == contact_id), None)
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
        return json.dumps(cart, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_cart",
                "description": "Create a cart for a contact at a deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["contact_id", "created_at"],
                },
            },
        }
