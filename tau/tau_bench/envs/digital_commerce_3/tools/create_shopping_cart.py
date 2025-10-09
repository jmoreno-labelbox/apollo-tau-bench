from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateShoppingCart(Tool):
    """Establish a new shopping cart for a customer containing several items."""

    @staticmethod
    def invoke(
        data: dict[str, Any], cart_id: Any, contact_id: Any, items: Any = []
    ) -> str:
        cart_id = _idstr(cart_id)
        contact_id = _idstr(contact_id)
        items = _norm_ids_in_obj(items or [])

        if not cart_id or not contact_id:
            return _error("cart_id and contact_id are required.")

        contacts = data.get("contacts", {}).values()
        if not _find_one(list(contacts.values()), "contact_id", contact_id):
            return _error(f"Contact '{contact_id}' not found.")

        carts = data.setdefault("carts", [])
        if _find_one(carts, "cart_id", cart_id):
            return _error(f"Cart '{cart_id}' already exists.")

        cart = {
            "cart_id": cart_id,
            "contact_id": contact_id,
            "last_updated_at": FIXED_NOW,
            "account_id": _find_one(list(contacts.values()), "contact_id", contact_id).get(
                "account_id"
            ),
            "applied_offer_id": None,
        }
        data["carts"][cart["cart_id"]] = cart

        cart_items = data.setdefault("cart_items", [])
        products = data.get("products", {}).values()
        for item in items:
            product_id = item.get("product_id")
            quantity = int(item.get("quantity", 1))
            if not _find_one(list(products.values()), "product_id", product_id):
                return _error(f"Product '{product_id}' not found.")
            cart_item_id = f"{cart_id}:{product_id}"
            cart_items.append(
                {
                    "cart_item_id": cart_item_id,
                    "cart_id": cart_id,
                    "product_id": product_id,
                    "quantity": quantity,
                    "pricebook_entry_id": None,
                }
            )

        _append_audit(
            data,
            "cart_created",
            cart_id,
            {"contact_id": contact_id, "items_count": len(items)},
        )
        payload = cart
        out = json.dumps(payload, indent=2)
        return out
        pass
        cart_id = _idstr(cart_id)
        contact_id = _idstr(contact_id)
        items = _norm_ids_in_obj(items or [])

        if not cart_id or not contact_id:
            return _error("cart_id and contact_id are required.")

        contacts = data.get("contacts", {}).values()
        if not _find_one(list(contacts.values()), "contact_id", contact_id):
            return _error(f"Contact '{contact_id}' not found.")

        carts = data.setdefault("carts", [])
        if _find_one(carts, "cart_id", cart_id):
            return _error(f"Cart '{cart_id}' already exists.")

        cart = {
            "cart_id": cart_id,
            "contact_id": contact_id,
            "last_updated_at": FIXED_NOW,
            "account_id": _find_one(list(contacts.values()), "contact_id", contact_id).get(
                "account_id"
            ),
            "applied_offer_id": None,
        }
        data["carts"][cart["cart_id"]] = cart

        cart_items = data.setdefault("cart_items", [])
        products = data.get("products", {}).values()
        for item in items:
            product_id = item.get("product_id")
            quantity = int(item.get("quantity", 1))
            if not _find_one(list(products.values()), "product_id", product_id):
                return _error(f"Product '{product_id}' not found.")
            cart_item_id = f"{cart_id}:{product_id}"
            cart_items.append(
                {
                    "cart_item_id": cart_item_id,
                    "cart_id": cart_id,
                    "product_id": product_id,
                    "quantity": quantity,
                    "pricebook_entry_id": None,
                }
            )

        _append_audit(
            data,
            "cart_created",
            cart_id,
            {"contact_id": contact_id, "items_count": len(items)},
        )
        payload = cart
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateShoppingCart",
                "description": "Create a new shopping cart for a customer with multiple items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "contact_id": {"type": "string"},
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                            },
                        },
                    },
                    "required": ["cart_id", "contact_id"],
                },
            },
        }
