import json
from typing import Any

from tau_bench.envs.tool import Tool


def get_next_order_id(data):
    pass
    orders = data.get("orders", [])
    next_num = len(orders) + 1
    return f"order_{next_num}"


def get_next_case_id(data):
    pass
    cases = data.get("cases", [])
    next_num = len(cases) + 1
    return f"case_{next_num}"


def get_next_offer_id(data):
    pass
    offers = data.get("offers", [])
    next_num = len(offers) + 1
    return f"offer_{next_num}"


def get_next_order_item_id(data):
    pass
    order_items = data.get("order_items", [])
    return len(order_items) + 1


def get_next_cart_id(data):
    pass
    carts = data.get("carts", [])
    next_num = len(carts) + 1
    return f"cart_{next_num}"


def get_next_cart_item_id(data):
    pass
    cart_items = data.get("cart_items", [])
    next_num = len(cart_items) + 1
    return f"item_{next_num}"


def get_next_account_id(data):
    pass
    accounts = data.get("accounts", [])
    next_num = len(accounts) + 1
    return f"acc_{next_num}"


def get_next_contact_id(data):
    pass
    contacts = data.get("contacts", [])
    next_num = len(contacts) + 1
    return f"cont_{next_num}"


from decimal import ROUND_HALF_UP, Decimal

_TWOPLACES = Decimal("0.01")


def _to_number(d: Decimal) -> float:
    pass
    #JSON will display 199.9 rather than 199.90; this is acceptable and predictable
    return float(d)


def _dec(x) -> Decimal:
    pass
    #convert to string to prevent binary float issues (e.g., 19.99)
    return Decimal(str(x))


def _money(x: Decimal) -> Decimal:
    pass
    #consistently round HALF_UP to two decimal places for monetary values
    return x.quantize(_TWOPLACES, rounding=ROUND_HALF_UP)


ID_KEYS = {
    "account_id",
    "contact_id",
    "offer_id",
    "cart_id",
    "order_id",
    "case_id",
    "product_id",
    "pricebook_id",
}
ID_KEYS |= {"cluster_id", "security_group_id", "rule_id", "subnet_group_id"}


def get_current_timestamp() -> str:
    pass
    return "2025-08-10T12:00:00Z"  #according to the current time as per the rules


def _idstr(v):
    pass
    return str(v) if isinstance(v, int) else v


def _norm_ids_in_obj(obj):
    pass
    if isinstance(obj, list):
        return [_norm_ids_in_obj(x) for x in obj]
    if isinstance(obj, dict):
        return {
            k: (_idstr(v) if k in ID_KEYS else _norm_ids_in_obj(v))
            for k, v in obj.items()
        }
    return obj


class GetAccountById(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], account_id: Any) -> str:
        account_id = _idstr(account_id)
        if not account_id:
            payload = {"error": "Missing required field: account_id"}
            out = json.dumps(payload, indent=2)
            return out
        accounts = data.get("accounts", [])
        for account in accounts:
            if account.get("account_id") == account_id:
                payload = account
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No account found with ID {account_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccountById",
                "description": "Fetch a single account's full details by its account_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Exact account ID to retrieve.",
                        }
                    },
                    "required": ["account_id"],
                },
            },
        }


class GetAccountByName(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], name: Any) -> str:
        account_name = name
        if not account_name:
            payload = {"error": "Missing required field: name"}
            out = json.dumps(payload, indent=2)
            return out
        accounts = data.get("accounts", [])
        for account in accounts:
            if account.get("account_name") == account_name:
                payload = account
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No account found with name '{account_name}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccountByName",
                "description": "Fetch a single account's full details by its account_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Exact account name to retrieve.",
                        }
                    },
                    "required": ["name"],
                },
            },
        }


class UpdateStreetAddress(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        account_id: Any,
        new_shipping_street: Any,
        new_billing_street: Any = None,
    ) -> str:
        account_id = _idstr(account_id)
        new_shipping_street = new_shipping_street
        new_billing_street = new_billing_street
        if not account_id or not new_shipping_street:
            payload = {
                "error": "Missing required field: account_id and/or new_shipping_street"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        accounts = data.get("accounts", [])
        for account in accounts:
            if account.get("account_id") == account_id:
                account["shipping_street"] = new_shipping_street
                if new_billing_street:
                    account["billing_street"] = new_billing_street
                payload = account
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No account found with ID {account_id}"}
        out = json.dumps(payload, indent=2)
        return out


    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateStreetAddress",
                "description": "Update the shipping_street of an account by its account_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Exact account ID whose shipping_street will be updated.",
                        },
                        "new_shipping_street": {
                            "type": "string",
                            "description": "New value for shipping_street.",
                        },
                        "new_billing_street": {
                            "type": "string",
                            "description": "New value for shipping_street.",
                        },
                    },
                    "required": ["account_id", "new_shipping_street"],
                },
            },
        }


class GetContactByName(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], first_name: Any = None, last_name: Any = None) -> str:
        if not first_name or not last_name:
            payload = {"error": "Missing required field: first_name and/or last_name"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        contacts = data.get("contacts", [])
        for contact in contacts:
            if (
                contact.get("first_name") == first_name
                and contact.get("last_name") == last_name
            ):
                payload = contact
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No contact found with name '{first_name} {last_name}'"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetContactByName",
                "description": "Fetch a contact's full details by exact first_name and last_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "Exact first name of the contact.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "Exact last name of the contact.",
                        },
                    },
                    "required": ["first_name", "last_name"],
                },
            },
        }


class GetOrdersByContactId(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], contact_id: Any) -> str:
        contact_id = _idstr(contact_id)
        if not contact_id:
            payload = {"error": "Missing required field: contact_id"}
            out = json.dumps(payload, indent=2)
            return out

        orders = data.get("orders", [])
        contact_orders = [o for o in orders if o.get("contact_id") == contact_id]
        payload = contact_orders
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrdersByContactId",
                "description": "Fetch all orders for a given contact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {
                            "type": "string",
                            "description": "Exact contact ID to retrieve orders for.",
                        }
                    },
                    "required": ["contact_id"],
                },
            },
        }


class AddStockQuantities(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], items: list[dict[str, Any]]) -> str:
        if not isinstance(items, list) or not items:
            payload = {
                "error": "Missing or invalid 'items'. Expected list of {product_id, quantity_to_add}."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        products = data.get("products", [])
        results = []
        for it in items:
            pid = it.get("product_id")
            qty = it.get("quantity_to_add")
            if not pid or qty is None:
                payload = {"error": "Each item must include product_id and quantity_to_add"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            prod = next((p for p in products if p.get("product_id") == pid), None)
            if not prod:
                results.append({"product_id": pid, "error": "Product not found"})
                continue

            try:
                prod["stock_quantity"] = int(prod.get("stock_quantity", 0)) + int(qty)
            except (TypeError, ValueError):
                payload = {"error": "quantity_to_add must be an integer"}
                out = json.dumps(
                    payload, indent=2
                )
                return out

            results.append(
                {"product_id": pid, "stock_quantity": prod["stock_quantity"]}
            )
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddStockQuantities",
                "description": "Batch increase stock quantities for multiple products.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "quantity_to_add": {"type": "integer"},
                                },
                                "required": ["product_id", "quantity_to_add"],
                            },
                        }
                    },
                    "required": ["items"],
                },
            },
        }


class GetPriceOfProduct(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], items: list[dict[str, Any]]) -> str:
        if not items or not isinstance(items, list):
            payload = {
                "error": "Missing or invalid 'items'. Expected a list of {product_id, pricebook_id}."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        pricebook_entries = data.get("pricebook_entries", [])
        results = []
        for item in items:
            product_id = item.get("product_id")
            pricebook_id = item.get("pricebook_id")
            if not product_id or not pricebook_id:
                results.append({"error": "Missing product_id or pricebook_id in item"})
                continue
            match = next(
                (
                    e
                    for e in pricebook_entries
                    if e.get("product_id") == product_id
                    and e.get("pricebook_id") == pricebook_id
                ),
                None,
            )
            if match:
                price = _money(_dec(match.get("price")))
                results.append({"product_id": product_id, "price": _to_number(price)})
            else:
                results.append(
                    {
                        "product_id": product_id,
                        "error": f"No price found in pricebook_id '{pricebook_id}'",
                    }
                )
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPriceOfProduct",
                "description": "Fetch the prices of multiple products for given pricebook_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "items": {
                            "type": "array",
                            "description": "List of products with pricebook_ids to fetch prices for.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {
                                        "type": "string",
                                        "description": "Exact product ID to retrieve price for.",
                                    },
                                    "pricebook_id": {
                                        "type": "string",
                                        "description": "Pricebook ID to look in.",
                                    },
                                },
                                "required": ["product_id", "pricebook_id"],
                            },
                        }
                    },
                    "required": ["items"],
                },
            },
        }


class CreateNewOffer(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any], offer_code: Any, discount_type: Any, discount_value: Any
    ) -> str:
        if not all([offer_code, discount_type, discount_value is not None]):
            payload = {
                "error": "Missing required fields: offer_code, discount_type, discount_value"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        offers = data.get("offers", [])
        offer_id = get_next_offer_id(data)
        new_offer = {
            "offer_id": offer_id,
            "offer_code": offer_code,
            "discount_type": discount_type,
            "discount_value": float(discount_value),
            "is_active": True,
        }
        offers.append(new_offer)
        payload = new_offer
        out = json.dumps(payload, indent=2)
        return out
           

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewOffer",
                "description": "Create a new offer and append it to the offers DB.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "offer_code": {
                            "type": "string",
                            "description": "Unique offer_code for the offer (e.g., SUMMER10).",
                        },
                        "discount_type": {
                            "type": "string",
                            "description": "Type of discount: 'PERCENTAGE' or 'FIXED_AMOUNT'.",
                        },
                        "discount_value": {
                            "type": "number",
                            "description": "Value of the discount (percentage or fixed amount).",
                        },
                    },
                    "required": ["offer_code", "discount_type", "discount_value"],
                },
            },
        }


class DeactivateOffer(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], offer_code: Any) -> str:
        if not offer_code:
            payload = {"error": "Missing required field: offer_code"}
            out = json.dumps(payload, indent=2)
            return out
        offers = data.get("offers", [])
        for offer in offers:
            if offer.get("offer_code") == offer_code:
                offer["is_active"] = False
                payload = offer
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No offer found with code '{offer_code}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeactivateOffer",
                "description": "Deactivate an offer by its offer_code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "offer_code": {
                            "type": "string",
                            "description": "Exact offer code to deactivate.",
                        }
                    },
                    "required": ["offer_code"],
                },
            },
        }


class GetOfferDetails(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], offer_id: Any) -> str:
        offer_id = _idstr(offer_id)
        if not offer_id:
            payload = {"error": "Missing required field: offer_id"}
            out = json.dumps(payload, indent=2)
            return out
        offers = data.get("offers", [])
        for offer in offers:
            if offer.get("offer_id") == offer_id:
                payload = offer
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No offer found with ID '{offer_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOfferDetails",
                "description": "Fetch full details of an offer by offer_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "offer_id": {
                            "type": "string",
                            "description": "Exact offer ID to retrieve.",
                        }
                    },
                    "required": ["offer_id"],
                },
            },
        }


class GetCartByContactId(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], contact_id: Any, carts: list = None) -> str:
        contact_id = _idstr(contact_id)
        if not contact_id:
            payload = {"error": "Missing required field: contact_id"}
            out = json.dumps(payload, indent=2)
            return out
        carts = carts or data.get("carts", [])
        for cart in carts:
            if cart.get("contact_id") == contact_id:
                payload = cart
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No cart found for contact_id '{contact_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCartByContactId",
                "description": "Fetch full cart details by contact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {
                            "type": "string",
                            "description": "Exact contact ID to retrieve cart for.",
                        }
                    },
                    "required": ["contact_id"],
                },
            },
        }


class GetAllItemsInCart(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cart_id: Any, cart_items: list[dict[str, Any]] = None) -> str:
        cart_id = _idstr(cart_id)
        if not cart_id:
            payload = {"error": "Missing required field: cart_id"}
            out = json.dumps(payload, indent=2)
            return out
        cart_items = cart_items or []
        items_list = []
        for item in cart_items:
            if item.get("cart_id") == cart_id:
                items_list.append(
                    {
                        "product_id": item.get("product_id"),
                        "quantity": item.get("quantity"),
                    }
                )

        if not items_list:
            payload = {"error": f"No items found for cart_id '{cart_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = items_list
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllItemsInCart",
                "description": "Fetch all items in a cart by cart_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {
                            "type": "string",
                            "description": "Exact cart ID to retrieve items for.",
                        }
                    },
                    "required": ["cart_id"],
                },
            },
        }


class ClearCart(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cart_id: Any) -> str:
        pass
        cart_id = _idstr(cart_id)
        if not cart_id:
            payload = {"error": "Missing required field: cart_id"}
            out = json.dumps(payload, indent=2)
            return out
        cart_items = data.get("cart_items", [])
        removed_count = 0
        for item in list(cart_items):  # duplicate to prevent changes while iterating
            if item.get("cart_id") == cart_id:
                cart_items.remove(item)
                removed_count += 1

        if removed_count == 0:
            payload = {"error": f"No items found for cart_id '{cart_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {
            "message": f"All items removed from cart '{cart_id}'",
            "removed_count": removed_count,
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
                "name": "ClearCart",
                "description": "Remove all items from a given cart.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {
                            "type": "string",
                            "description": "ID of the cart to clear.",
                        }
                    },
                    "required": ["cart_id"],
                },
            },
        }


class GetOrderDetailsById(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any) -> str:
        order_id = _idstr(order_id)
        if not order_id:
            payload = {"error": "Missing required field: order_id"}
            out = json.dumps(payload, indent=2)
            return out
        orders = data.get("orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                payload = order
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No order found with ID '{order_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrderDetailsById",
                "description": "Fetch full order details by order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Exact order ID to retrieve.",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }


class UpdateOrderStatus(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any, new_status: Any) -> str:
        order_id = _idstr(order_id)
        orders = data.get("orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                order["status"] = new_status
                payload = order
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No order found with ID '{order_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOrderStatus",
                "description": "Update the status of an existing order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Exact order ID to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status to set for the order (e.g., Processing, Shipped, Delivered).",
                        },
                    },
                    "required": ["order_id", "new_status"],
                },
            },
        }


class GetAllOrderItemsByOrderId(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], order_id: Any, order_items: list[dict[str, Any]] = None) -> str:
        order_id = _idstr(order_id)
        if not order_id:
            payload = {"error": "Missing required field: order_id"}
            out = json.dumps(payload, indent=2)
            return out
        order_items = order_items or data.get("order_items", [])
        items = [item for item in order_items if item.get("order_id") == order_id]
        payload = items
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllOrderItemsByOrderId",
                "description": "Return all order items for the specified order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Exact order ID whose items should be returned.",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }


class CreateNewCase(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        contact_id: Any,
        account_id: Any,
        subject: Any,
        priority: Any,
        order_id: Any = None,
    ) -> str:
        contact_id = _idstr(contact_id)
        account_id = _idstr(account_id)
        order_id = _idstr(order_id)
        subject = subject
        priority = priority

        #1) Confirm
        if not contact_id or not account_id or not subject or not priority:
            payload = {
                    "error": "Missing required fields: contact_id, account_id, subject, priority"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        cases = data.get("cases", [])
        case_id = get_next_case_id(data)
        new_case = {
            "case_id": case_id,
            "contact_id": contact_id,
            "account_id": account_id,
            "order_id": order_id,
            "subject": subject,
            "status": "New",
            "priority": priority,
        }
        cases.append(new_case)
        payload = new_case
        out = json.dumps(payload, indent=2)
        return out
         

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewCase",
                "description": "Create a new case and append it to the cases DB.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {
                            "type": "string",
                            "description": "Contact ID related to the case.",
                        },
                        "account_id": {
                            "type": "string",
                            "description": "Account ID related to the case.",
                        },
                        "order_id": {
                            "type": ["string", "null"],
                            "description": "Order ID related to the case, if any.",
                        },
                        "subject": {
                            "type": "string",
                            "description": "Subject line for the case.",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Priority level (e.g., Low, Medium, High).",
                        },
                    },
                    "required": ["contact_id", "account_id", "subject", "priority"],
                },
            },
        }


class UpdateCaseStatus(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], case_id: Any, status: Any) -> str:
        if not case_id or not status:
            payload = {"error": "Missing required fields: case_id and/or status"}
            out = json.dumps(payload, indent=2)
            return out
        cases = data.get("cases", [])
        for case in cases:
            if case.get("case_id") == case_id:
                case["status"] = status
                payload = case
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No case found with ID '{case_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCaseStatus",
                "description": "Update the status of an existing case.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_id": {
                            "type": "string",
                            "description": "Exact case ID to update.",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status to set for the case (e.g., New, In Progress, Closed).",
                        },
                    },
                    "required": ["case_id", "status"],
                },
            },
        }


class CalculateSubTotalPrice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], items: list[dict[str, Any]]) -> str:
        if not items or not isinstance(items, list):
            payload = {
                    "error": "Missing or invalid 'items'. Expected a list of {product_id, quantity, price}."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        total = Decimal("0")
        for item in items:
            product_id = item.get("product_id")
            quantity = item.get("quantity")
            price = item.get("price")
            if product_id is None or quantity is None or price is None:
                payload = {"error": "Each item must include product_id, quantity, price"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            try:
                q = int(quantity)
                p = _money(_dec(price))
            except Exception:
                payload = {"error": f"Invalid numeric values for product_id '{product_id}'"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            line = _money(p * Decimal(q))
            total += line

        total = _money(total)
        payload = {"subtotal": _to_number(total)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateSubTotalPrice",
                "description": "Calculate subtotal price from a list of products, their quantities, and prices.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "items": {
                            "type": "array",
                            "description": "List of products with quantity and price.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                    "price": {"type": "number"},
                                },
                                "required": ["product_id", "quantity", "price"],
                            },
                        }
                    },
                    "required": ["items"],
                },
            },
        }


class CalclulateDiscountFlat(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subtotal: Any = None, discount_amount: Any = None) -> str:
        if subtotal is None or discount_amount is None:
            payload = {"error": "Missing required fields: subtotal and/or discount_amount"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        try:
            sub = _money(_dec(subtotal))
            disc = _money(_dec(discount_amount))
        except Exception:
            payload = {"error": "subtotal and discount_amount must be numeric"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        total = _money(max(sub - disc, Decimal("0")))
        payload = {"total": _to_number(total)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateDiscountFlat",
                "description": "Apply a flat discount amount to a subtotal.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subtotal": {
                            "type": "number",
                            "description": "Original subtotal before discount.",
                        },
                        "discount_amount": {
                            "type": "number",
                            "description": "Flat discount amount to subtract.",
                        },
                    },
                    "required": ["subtotal", "discount_amount"],
                },
            },
        }


class CalculateDiscountPercent(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subtotal: Any = None, discount_percent: Any = None) -> str:
        if subtotal is None or discount_percent is None:
            payload = {"error": "Missing required fields: subtotal and/or discount_percent"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        try:
            sub = _money(_dec(subtotal))
            pct = _dec(discount_percent) / Decimal("100")
        except Exception:
            payload = {"error": "subtotal and discount_percent must be numeric"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        disc = _money(sub * pct)
        total = _money(max(sub - disc, Decimal("0")))
        payload = {"discount_amount": _to_number(disc), "total": _to_number(total)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateDiscountPercent",
                "description": "Apply a percentage discount to a subtotal.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subtotal": {
                            "type": "number",
                            "description": "Original subtotal before discount.",
                        },
                        "discount_percent": {
                            "type": "number",
                            "description": "Discount percentage to apply.",
                        },
                    },
                    "required": ["subtotal", "discount_percent"],
                },
            },
        }


class GetProductsByNames(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], names: list[str]) -> str:
        if not names or not isinstance(names, list):
            payload = {
                "error": "Missing or invalid 'names'. Expected a list of product names."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        products = data.get("products", [])
        results: list[dict[str, Any]] = []
        for n in names:
            match = next((p for p in products if p.get("name") == n), None)
            results.append(
                match if match else {"name": n, "error": "Product not found"}
            )
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductsByNames",
                "description": "Fetch multiple products by their exact names.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "names": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of product names to fetch.",
                        }
                    },
                    "required": ["names"],
                },
            },
        }


class AddItemsToCartBatch(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cart_id: Any, items: list[dict[str, Any]]) -> str:
        if not cart_id or not items or not isinstance(items, list):
            payload = {
                "error": "Missing required fields: cart_id and list 'items' with {product_id, quantity}"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        cart_items = data.get("cart_items", [])
        created = []
        next_num = len(cart_items) + 1
        for it in items:
            pid = it.get("product_id")
            qty = it.get("quantity")
            if not pid or qty is None:
                payload = {"error": "Each item must include product_id and quantity"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            rec = {
                "cart_item_id": f"item_{next_num}",
                "cart_id": cart_id,
                "product_id": pid,
                "quantity": int(qty),
            }
            cart_items.append(rec)
            created.append(rec)
            next_num += 1
        payload = created
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddItemsToCartBatch",
                "description": "Add multiple products to a cart in one call.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["product_id", "quantity"],
                            },
                        },
                    },
                    "required": ["cart_id", "items"],
                },
            },
        }


class UpdateItemsInCartBatch(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cart_id: Any, items: list[dict[str, Any]]) -> str:
        if not cart_id or not items or not isinstance(items, list):
            payload = {
                "error": "Missing required fields: cart_id and list 'items' with {product_id, new_quantity}"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        cart_items = data.get("cart_items", [])
        updated = []
        for it in items:
            pid = it.get("product_id")
            new_q = it.get("new_quantity")
            if not pid or new_q is None:
                payload = {"error": "Each item must include product_id and new_quantity"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            for row in cart_items:
                if row.get("cart_id") == cart_id and row.get("product_id") == pid:
                    row["quantity"] = int(new_q)
                    updated.append(row)
                    break
        if not updated:
            payload = {"error": f"No matching items found to update for cart '{cart_id}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = updated
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateItemsInCartBatch",
                "description": "Update quantities for multiple products in a cart.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "new_quantity": {"type": "integer"},
                                },
                                "required": ["product_id", "new_quantity"],
                            },
                        },
                    },
                    "required": ["cart_id", "items"],
                },
            },
        }


class RemoveItemsFromCartBatch(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cart_id: Any, product_ids: list[str]) -> str:
        if not cart_id or not product_ids or not isinstance(product_ids, list):
            payload = {"error": "Missing required fields: cart_id and list 'product_ids'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        cart_items = data.get("cart_items", [])
        before = len(cart_items)
        cart_items[:] = [
            r
            for r in cart_items
            if not (r.get("cart_id") == cart_id and r.get("product_id") in product_ids)
        ]
        removed = before - len(cart_items)
        payload = {
                "removed_count": removed,
                "cart_id": cart_id,
                "removed_product_ids": product_ids,
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
                "name": "RemoveItemsFromCartBatch",
                "description": "Remove multiple products from a cart in one call.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string"},
                        "product_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["cart_id", "product_ids"],
                },
            },
        }


class VerifyOrderFromStock(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], items: list[dict[str, Any]]) -> str:
        if not items or not isinstance(items, list):
            payload = {
                "error": "Missing or invalid 'items'. Expected list of {product_id, required_quantity}."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        products = data.get("products", [])
        results = []
        is_valid = True
        for it in items:
            pid = it.get("product_id")
            req = it.get("required_quantity")
            if not pid or req is None:
                payload = {
                    "error": "Each item must include product_id and required_quantity"
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            match = next((p for p in products if p.get("product_id") == pid), None)
            if not match:
                results.append({"product_id": pid, "error": "Product not found"})
                is_valid = False
                continue
            avail = int(match.get("stock_quantity", 0))
            valid_q = req if req <= avail else avail
            if req > avail:
                is_valid = False
            results.append(
                {
                    "product_id": pid,
                    "required_quantity": req,
                    "available_quantity": avail,
                    "valid_quantity": valid_q,
                }
            )
        payload = {"is_valid": is_valid, "Valid_item_list": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifyOrderFromStock",
                "description": "Validate order quantities against current stock without separate quantity fetch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "required_quantity": {"type": "integer"},
                                },
                                "required": ["product_id", "required_quantity"],
                            },
                        }
                    },
                    "required": ["items"],
                },
            },
        }


class ApplyOfferToSubtotal(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subtotal: Any, offer_code: Any) -> str:
        if subtotal is None or not offer_code:
            payload = {"error": "Missing required fields: subtotal and/or offer_code"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        try:
            sub = _money(_dec(subtotal))
        except Exception:
            payload = {"error": "subtotal must be numeric"}
            out = json.dumps(payload, indent=2)
            return out

        offers = data.get("offers", [])
        match = next((o for o in offers if o.get("offer_code") == offer_code), None)
        if not match:
            payload = {"valid": False, "reason": "Offer not found"}
            out = json.dumps(payload, indent=2)
            return out
        if not match.get("is_active", False):
            payload = {"valid": False, "reason": "Offer is inactive"}
            out = json.dumps(payload, indent=2)
            return out

        dtype = match.get("discount_type")
        dval = _dec(match.get("discount_value", 0))

        if dtype == "PERCENTAGE":
            disc = _money(sub * dval / Decimal("100"))
        elif dtype == "FIXED_AMOUNT":
            disc = _money(dval)
        else:
            payload = {"error": f"Unknown discount_type '{dtype}'"}
            out = json.dumps(payload, indent=2)
            return out

        total = _money(max(sub - disc, Decimal("0")))
        payload = {
                "valid": True,
                "offer": match,
                "subtotal": _to_number(sub),
                "discount_amount": _to_number(disc),
                "total": _to_number(total),
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
                "name": "ApplyOfferToSubtotal",
                "description": "Validate an offer and compute discount+total for a subtotal.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subtotal": {"type": "number"},
                        "offer_code": {"type": "string"},
                    },
                    "required": ["subtotal", "offer_code"],
                },
            },
        }


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
        carts.append(new_cart)
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


#=========================
#AWS UTILITIES (ElastiCache, Security Groups, Subnet Groups)
#=========================


class InventorySecurityGroupRules(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], aws_security_group_rules: list[dict[str, Any]] = None) -> str:
        rules = aws_security_group_rules or []
        payload = {"rule_ids": [r.get("rule_id") for r in rules]}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InventorySecurityGroupRules",
                "description": "List all AWS security group rule IDs.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class GetSecurityGroupRuleById(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], rule_id: Any, aws_security_group_rules: list = None) -> str:
        rule_id = _idstr(rule_id)
        rules = aws_security_group_rules if aws_security_group_rules is not None else []
        for r in rules:
            if r.get("rule_id") == rule_id:
                payload = r
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No security group rule found with ID '{rule_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSecurityGroupRuleById",
                "description": "Fetch a single AWS security group rule by rule_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_id": {
                            "type": "string",
                            "description": "Exact security group rule_id.",
                        }
                    },
                    "required": ["rule_id"],
                },
            },
        }


class AttachSecurityGroupToCacheCluster(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any, security_group_id: Any) -> str:
        cluster_id = _idstr(cluster_id)
        security_group_id = _idstr(security_group_id)
        clusters = data.get("aws_elasticache_clusters", [])
        for c in clusters:
            if c.get("cluster_id") == cluster_id:
                c["security_group_id"] = security_group_id
                payload = c
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No ElastiCache cluster found with ID '{cluster_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "attachSecurityGroupToCacheCluster",
                "description": "Set the security_group_id for an ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "security_group_id": {"type": "string"},
                    },
                    "required": ["cluster_id", "security_group_id"],
                },
            },
        }


class RenameElastiCacheCluster(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any, new_cluster_name: Any) -> str:
        cluster_id = _idstr(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        for c in clusters:
            if c.get("cluster_id") == cluster_id:
                c["cluster_name"] = new_cluster_name
                payload = c
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No ElastiCache cluster found with ID '{cluster_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "renameElasticacheCluster",
                "description": "Rename an ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "new_cluster_name": {"type": "string"},
                    },
                    "required": ["cluster_id", "new_cluster_name"],
                },
            },
        }


class SetElastiCacheClusterStatus(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any, new_status: Any) -> str:
        cluster_id = _idstr(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        for c in clusters:
            if c.get("cluster_id") == cluster_id:
                c["status"] = new_status
                payload = c
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No ElastiCache cluster found with ID '{cluster_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setElasticacheClusterStatus",
                "description": "Set the status field for an ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["cluster_id", "new_status"],
                },
            },
        }


class SetElastiCacheEndpointUrl(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any, endpoint_url: Any) -> str:
        cluster_id = _idstr(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        for c in clusters:
            if c.get("cluster_id") == cluster_id:
                c["endpoint_url"] = endpoint_url
                payload = c
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No ElastiCache cluster found with ID '{cluster_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setElasticacheEndpointUrl",
                "description": "Set or clear the endpoint_url for an ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "endpoint_url": {
                            "type": "string",
                            "description": "Endpoint (or 'NULL' to clear).",
                        },
                    },
                    "required": ["cluster_id", "endpoint_url"],
                },
            },
        }


class SetElastiCacheSubnetGroup(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any, subnet_group_id: Any, aws_subnet_groups: list = None, aws_elasticache_clusters: list = None) -> str:
        cluster_id = _idstr(cluster_id)
        subnet_group_id = _idstr(subnet_group_id)

        # Check if the subnet group is present
        groups = aws_subnet_groups or []
        if not any(g.get("subnet_group_id") == subnet_group_id for g in groups):
            payload = {"error": f"No subnet group found with ID '{subnet_group_id}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        clusters = aws_elasticache_clusters or []
        for c in clusters:
            if c.get("cluster_id") == cluster_id:
                c["subnet_group_id"] = subnet_group_id
                payload = c
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No ElastiCache cluster found with ID '{cluster_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setElasticacheSubnetGroup",
                "description": "Set the subnet_group_id for an ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "subnet_group_id": {"type": "string"},
                    },
                    "required": ["cluster_id", "subnet_group_id"],
                },
            },
        }


class UpdateSubnetGroupDescription(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], subnet_group_id: Any, new_description: Any) -> str:
        subnet_group_id = _idstr(subnet_group_id)
        groups = data.get("aws_subnet_groups", [])
        for g in groups:
            if g.get("subnet_group_id") == subnet_group_id:
                g["description"] = new_description
                payload = g
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No subnet group found with ID '{subnet_group_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSubnetGroupDescription",
                "description": "Set the description field on an AWS subnet group record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subnet_group_id": {"type": "string"},
                        "new_description": {"type": "string"},
                    },
                    "required": ["subnet_group_id", "new_description"],
                },
            },
        }


class SetClusterInstanceTypeNote(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any, note: Any) -> str:
        cluster_id = _idstr(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        for c in clusters:
            if c.get("cluster_id") == cluster_id:
                c["instance_type_note"] = note
                payload = c
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No ElastiCache cluster found with ID '{cluster_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setClusterInstanceTypeNote",
                "description": "Set 'instance_type_note' on an ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "note": {"type": "string"},
                    },
                    "required": ["cluster_id", "note"],
                },
            },
        }


def _next_aws_plan_id(data: dict[str, Any]) -> str:
    pass
    plans = data.setdefault("aws_plans", [])
    return f"ap-{len(plans)+1:04d}"


#---------- Ingress (Security Group regulations) ----------


class CreateIngressChangePlan(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        rule_id: Any,
        target_cidr: Any,
        final_description: Any,
        env_tag: Any,
    ) -> str:
        rule_id = _idstr(rule_id)
        target_cidr = str(target_cidr)
        final_description = str(final_description)
        env_tag = str(env_tag)
        # locate the rule
        rule = None
        for r in data.get("aws_security_group_rules", []):
            if r.get("rule_id") == rule_id:
                rule = r
                break
        if not rule:
            payload = {"error": f"No security group rule found with ID '{rule_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        plan = {
            "plan_id": _next_aws_plan_id(data),
            "type": "ingress",
            "rule_id": rule_id,
            "security_group_id": rule["security_group_id"],
            "port": rule["port"],
            "protocol": rule["protocol"],
            "target_cidr": target_cidr,
            "final_description": final_description,
            "env_tag": env_tag,
            "steps": ["update_rule", "consolidate", "standardize"],
        }
        data.setdefault("aws_plans", []).append(plan)
        payload = {"plan_id": plan["plan_id"], "steps": plan["steps"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
           

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateIngressChangePlan",
                "description": "Create a plan (update, consolidate, standardize) for a rule_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_id": {"type": "string"},
                        "target_cidr": {"type": "string"},
                        "final_description": {"type": "string"},
                        "env_tag": {"type": "string"},
                    },
                    "required": [
                        "rule_id",
                        "target_cidr",
                        "final_description",
                        "env_tag",
                    ],
                },
            },
        }


class ApplyIngressPlanStep(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: Any, step_index: Any) -> str:
        pass
        plan_id = _idstr(plan_id)
        step_index = int(step_index)
        #retrieve plan
        plan = None
        for p in data.get("aws_plans", []):
            if p.get("plan_id") == plan_id and p.get("type") == "ingress":
                plan = p
                break
        if not plan:
            payload = {"error": f"No ingress plan '{plan_id}'"}
            out = json.dumps(payload, indent=2)
            return out
        steps = plan.get("steps", [])
        if step_index < 0 or step_index >= len(steps):
            payload = {"error": f"Invalid step_index {step_index}"}
            out = json.dumps(payload, indent=2)
            return out

        sg_id = plan["security_group_id"]
        rules = data.get("aws_security_group_rules", [])
        step = steps[step_index]

        def _append_tag(desc: str, tag: str) -> str:
            pass
            tag = tag if tag.startswith("[") and tag.endswith("]") else f"[{tag}]"
            if tag in desc:  #prevent duplicates
                return desc
            return f"{desc} {tag}".strip()

        if step == "update_rule":
            #assign source and description to the original rule
            for r in rules:
                if r.get("rule_id") == plan["rule_id"]:
                    r["source_ip"] = plan["target_cidr"]
                    r["description"] = plan["final_description"]
                    payload = r
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Missing rule '{plan['rule_id']}'"}
            out = json.dumps(payload, indent=2)
            return out

        if step == "consolidate":
            #confirm there is precisely one 6379/TCP rule in this Security Group
            keep = None
            removed = []
            remain = []
            for r in rules:
                if r.get("security_group_id") == sg_id and r.get("port") == 6379:
                    if keep is None:
                        keep = r
                    else:
                        removed.append(r)
                        continue
                remain.append(r)
            data["aws_security_group_rules"] = remain + ([keep] if keep else [])
            if keep is None:
                #generate one
                new_rule = {
                    "rule_id": f"sgr-auto-{len(data['aws_security_group_rules'])+1:04d}",
                    "security_group_id": sg_id,
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": plan["target_cidr"],
                    "description": plan["final_description"],
                }
                data["aws_security_group_rules"].append(new_rule)
                payload = {"consolidated_rule": new_rule, "removed": removed}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            else:
                keep["source_ip"] = plan["target_cidr"]
                keep["description"] = plan["final_description"]
                payload = {"consolidated_rule": keep, "removed": removed}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        if step == "standardize":
            #add environment tag to every 6379 rule in this Security Group
            updated = []
            tag = plan["env_tag"]
            for r in rules:
                if r.get("security_group_id") == sg_id and r.get("port") == 6379:
                    before = r.get("description", "")
                    after = _append_tag(before, tag)
                    if after != before:
                        r["description"] = after
                        updated.append(r)
            payload = {"updated": updated, "count": len(updated)}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"Unsupported step '{step}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyIngressPlanStep",
                "description": "Apply a single step by index for a previously created ingress plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "step_index": {"type": "integer"},
                    },
                    "required": ["plan_id", "step_index"],
                },
            },
        }


class GetElastiCacheClusterById(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any) -> str:
        cluster_id = _idstr(cluster_id)
        for c in data.get("aws_elasticache_clusters", []):
            if c.get("cluster_id") == cluster_id:
                payload = c
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No ElastiCache cluster found with ID '{cluster_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getElasticacheClusterById",
                "description": "Fetch an ElastiCache cluster by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"cluster_id": {"type": "string"}},
                    "required": ["cluster_id"],
                },
            },
        }


class CreateClusterChangePlan(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        cluster_id: Any,
        reference_rule_id: Any,
        subnet_group_id: Any,
        new_status: Any,
        new_name: Any,
        note: Any,
        env_tag: Any,
        consolidate_cidr: Any,
        consolidate_desc: Any,
        endpoint_url: Any,
    ) -> str:
        cluster_id = _idstr(cluster_id)
        reference_rule_id = _idstr(reference_rule_id)
        subnet_group_id = _idstr(subnet_group_id)
        # does the cluster exist?
        cluster = None
        for c in data.get("aws_elasticache_clusters", []):
            if c.get("cluster_id") == cluster_id:
                cluster = c
                break
        if not cluster:
            payload = {"error": f"No ElastiCache cluster '{cluster_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        # does the rule exist?
        sg_id = None
        proto = None
        port = None
        for r in data.get("aws_security_group_rules", []):
            if r.get("rule_id") == reference_rule_id:
                sg_id = r.get("security_group_id")
                proto = r.get("protocol")
                port = r.get("port")
                break
        if sg_id is None:
            payload = {"error": f"No security group rule '{reference_rule_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        # is the subnet group present?
        ok = False
        for g in data.get("aws_subnet_groups", []):
            if g.get("subnet_group_id") == subnet_group_id:
                ok = True
                break
        if not ok:
            payload = {"error": f"No subnet group '{subnet_group_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        plan = {
            "plan_id": _next_aws_plan_id(data),
            "type": "cluster",
            "cluster_id": cluster_id,
            "security_group_id": sg_id,
            "subnet_group_id": subnet_group_id,
            "new_status": str(new_status),
            "new_name": str(new_name),
            "note": str(note),
            "env_tag": str(env_tag),
            "consolidate_cidr": str(consolidate_cidr),
            "consolidate_desc": str(consolidate_desc),
            "endpoint_url": str(endpoint_url),
            "steps": [
                "attach_sg",
                "set_subnet",
                "set_status",
                "set_name",
                "set_note",
                "standardize_env_on_sg",
                "consolidate_redis_on_sg",
                "set_endpoint",
            ],
        }
        data.setdefault("aws_plans", []).append(plan)
        payload = {"plan_id": plan["plan_id"], "steps": plan["steps"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
           

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateClusterChangePlan",
                "description": "Create a cluster hardening plan using a reference rule to derive SG.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "reference_rule_id": {"type": "string"},
                        "subnet_group_id": {"type": "string"},
                        "new_status": {"type": "string"},
                        "new_name": {"type": "string"},
                        "note": {"type": "string"},
                        "env_tag": {"type": "string"},
                        "consolidate_cidr": {"type": "string"},
                        "consolidate_desc": {"type": "string"},
                        "endpoint_url": {"type": "string"},
                    },
                    "required": [
                        "cluster_id",
                        "reference_rule_id",
                        "subnet_group_id",
                        "new_status",
                        "new_name",
                        "note",
                        "env_tag",
                        "consolidate_cidr",
                        "consolidate_desc",
                        "endpoint_url",
                    ],
                },
            },
        }


class ApplyClusterPlanStep(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: Any, step_index: Any) -> str:
        pass
        plan_id = _idstr(plan_id)
        step_index = int(step_index)
        # retrieve the plan
        plan = None
        for p in data.get("aws_plans", []):
            if p.get("plan_id") == plan_id and p.get("type") == "cluster":
                plan = p
                break
        if not plan:
            payload = {"error": f"No cluster plan '{plan_id}'"}
            out = json.dumps(payload, indent=2)
            return out
        steps = plan.get("steps", [])
        if step_index < 0 or step_index >= len(steps):
            payload = {"error": f"Invalid step_index {step_index}"}
            out = json.dumps(payload, indent=2)
            return out

        # find the cluster
        cl = None
        for c in data.get("aws_elasticache_clusters", []):
            if c.get("cluster_id") == plan["cluster_id"]:
                cl = c
                break
        if not cl:
            payload = {"error": f"Missing cluster '{plan['cluster_id']}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        step = steps[step_index]
        if step == "attach_sg":
            cl["security_group_id"] = plan["security_group_id"]
            payload = cl
            out = json.dumps(payload, indent=2)
            return out

        if step == "set_subnet":
            cl["subnet_group_id"] = plan["subnet_group_id"]
            payload = cl
            out = json.dumps(payload, indent=2)
            return out

        if step == "set_status":
            cl["status"] = plan["new_status"]
            payload = cl
            out = json.dumps(payload, indent=2)
            return out

        if step == "set_name":
            cl["cluster_name"] = plan["new_name"]
            payload = cl
            out = json.dumps(payload, indent=2)
            return out

        if step == "set_note":
            cl["instance_type_note"] = plan["note"]
            payload = cl
            out = json.dumps(payload, indent=2)
            return out

        if step == "standardize_env_on_sg" or step == "consolidate_redis_on_sg":
            # manage rules for this Security Group
            sg_id = plan["security_group_id"]
            rules = data.get("aws_security_group_rules", [])
            if step == "standardize_env_on_sg":
                tag = plan["env_tag"]
                changed = []
                tag_norm = (
                    tag if tag.startswith("[") and tag.endswith("]") else f"[{tag}]"
                )
                for r in rules:
                    if r.get("security_group_id") == sg_id and r.get("port") == 6379:
                        d = r.get("description", "")
                        if tag_norm not in d:
                            r["description"] = (d + " " + tag_norm).strip()
                            changed.append(r)
                payload = {"updated": changed, "count": len(changed)}
                out = json.dumps(payload, indent=2)
                return out

            if step == "consolidate_redis_on_sg":
                keep = None
                removed = []
                remain = []
                for r in rules:
                    if r.get("security_group_id") == sg_id and r.get("port") == 6379:
                        if keep is None:
                            keep = r
                        else:
                            removed.append(r)
                            continue
                    remain.append(r)
                data["aws_security_group_rules"] = remain + ([keep] if keep else [])
                if keep is None:
                    new_rule = {
                        "rule_id": f"sgr-auto-{len(data['aws_security_group_rules'])+1:04d}",
                        "security_group_id": sg_id,
                        "port": 6379,
                        "protocol": "TCP",
                        "source_ip": plan["consolidate_cidr"],
                        "description": plan["consolidate_desc"],
                    }
                    data["aws_security_group_rules"].append(new_rule)
                    payload = {"consolidated_rule": new_rule, "removed": removed}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                else:
                    keep["source_ip"] = plan["consolidate_cidr"]
                    keep["description"] = plan["consolidate_desc"]
                    payload = {"consolidated_rule": keep, "removed": removed}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out

        if step == "set_endpoint":
            cl["endpoint_url"] = plan["endpoint_url"]
            payload = cl
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"Unsupported step '{step}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyClusterPlanStep",
                "description": "Apply a single step by index for a previously created cluster plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "step_index": {"type": "integer"},
                    },
                    "required": ["plan_id", "step_index"],
                },
            },
        }


TOOLS = [
    GetAccountById(),
    GetAccountByName(),
    UpdateStreetAddress(),
    GetContactByName(),
    GetPriceOfProduct(),
    CreateNewOffer(),
    DeactivateOffer(),
    GetOfferDetails(),
    GetCartByContactId(),
    GetAllItemsInCart(),
    ClearCart(),
    GetOrderDetailsById(),
    UpdateOrderStatus(),
    GetAllOrderItemsByOrderId(),
    CreateNewCase(),
    UpdateCaseStatus(),
    CalculateSubTotalPrice(),
    CalclulateDiscountFlat(),
    CalculateDiscountPercent(),
    GetProductsByNames(),
    AddItemsToCartBatch(),
    UpdateItemsInCartBatch(),
    RemoveItemsFromCartBatch(),
    VerifyOrderFromStock(),
    ApplyOfferToSubtotal(),
    GetOrdersByContactId(),
    AddStockQuantities(),
    InventorySecurityGroupRules(),
    GetSecurityGroupRuleById(),
    AttachSecurityGroupToCacheCluster(),
    RenameElastiCacheCluster(),
    SetElastiCacheClusterStatus(),
    SetElastiCacheEndpointUrl(),
    SetElastiCacheSubnetGroup(),
    SetClusterInstanceTypeNote(),
    UpdateSubnetGroupDescription(),
    CreateIngressChangePlan(),
    ApplyIngressPlanStep(),
    CreateClusterChangePlan(),
    ApplyClusterPlanStep(),
]
