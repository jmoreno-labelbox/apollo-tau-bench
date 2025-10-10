# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCart(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], contact_id: Any) -> str:
        contact_id = _as_id(contact_id)
        if not contact_id:
            return _err("contact_id required.")

        contacts = data.get("contacts", [])
        contact = next((c for c in contacts if _as_id(c.get("contact_id")) == contact_id), None)
        if not contact:
            return _err("Contact not found.")

        carts = data.get("carts", [])
        numeric_ids = [int(c["cart_id"]) for c in carts if str(c.get("cart_id", "")).isdigit()]
        next_id = str(max(numeric_ids or [0]) + 1)

        cart = {
            "cart_id": next_id,
            "contact_id": contact_id,
            "account_id": contact.get("account_id"),
            "applied_offer_id": None,
            "override_pricebook_id": None,
            "last_updated_at": FIXED_NOW,
        }
        carts.append(cart)
        data["carts"] = carts
        return json.dumps(cart, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_cart",
                "description": "Create a cart for a contact; system auto-assigns the next numeric cart_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {
                            "type": "string",
                            "description": "Existing contact_id.",
                        },
                    },
                    "required": ["contact_id"],
                },
            },
        }
