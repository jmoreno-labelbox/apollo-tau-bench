from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ApplyOfferToCart(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], carts: list = None, offers: list = None, cart_id: Any = None, code: Any = None) -> str:
        if carts is None:
            carts = data.get("carts", [])
        if offers is None:
            offers = data.get("offers", [])

        cart_id = _as_id(cart_id)
        if not cart_id or not code:
            return _err("cart_id and code are required.")

        cart = next((c for c in carts if _as_id(c.get("cart_id")) == cart_id), None)
        if not cart:
            return _err("Cart not found.")

        offer = next(
            (
                o
                for o in offers
                if o.get("offer_code") == code and o.get("is_active") is True
            ),
            None,
        )
        if not offer:
            return _err("Offer not found or inactive.")

        cart["applied_offer_id"] = offer.get("offer_id")
        payload = {
            "cart_id": cart_id,
            "applied_offer_id": cart["applied_offer_id"],
            "code": code,
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
                "name": "ApplyOfferToCart",
                "description": "Apply an offer code to a cart (sets applied_offer_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "code": {"type": "string"},
                    },
                    "required": ["cart_id", "code"],
                },
            },
        }
