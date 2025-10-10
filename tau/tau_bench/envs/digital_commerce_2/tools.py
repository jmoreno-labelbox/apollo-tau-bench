import json
from decimal import ROUND_HALF_UP, Decimal
from typing import Any, Dict, List

from domains.dto import Tool


def get_next_contact_id(data):
    contacts = data.get("contacts", [])
    next_num = len(contacts) + 1
    return f"cont_{next_num}"


def get_next_account_id(data):
    accounts = data.get("accounts", [])
    next_num = len(accounts) + 1
    return f"acc_{next_num}"


def get_next_offer_id(data):
    offers = data.get("offers", [])
    next_num = len(offers) + 1
    return f"offer_{next_num}"


def get_next_cart_id(data):
    carts = data.get("carts", [])
    next_num = len(carts) + 1
    return f"cart_{next_num}"


def get_next_cart_item_id(data):
    cart_items = data.get("cart_items", [])
    next_num = len(cart_items) + 1
    return f"item_{next_num}"


def get_next_order_id(data):
    orders = data.get("orders", [])
    next_num = len(orders) + 1
    return f"order_{next_num}"


def get_next_order_item_id(data):
    order_items = data.get("order_items", [])
    return len(order_items) + 1


def get_next_case_id(data):
    cases = data.get("cases", [])
    next_num = len(cases) + 1
    return f"case_{next_num}"


_TWOPLACES = Decimal("0.01")


def _dec(x) -> Decimal:
    return Decimal(str(x))


def _money(x: Decimal) -> Decimal:
    return x.quantize(_TWOPLACES, rounding=ROUND_HALF_UP)


def _to_number(d: Decimal) -> float:
    return float(d)


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


def _idstr(v):
    return str(v) if isinstance(v, int) else v


def _norm_ids_in_obj(obj):
    if isinstance(obj, list):
        return [_norm_ids_in_obj(x) for x in obj]
    if isinstance(obj, dict):
        return {k: (_idstr(v) if k in ID_KEYS else _norm_ids_in_obj(v)) for k, v in obj.items()}
    return obj


def get_current_timestamp() -> str:
    return "2025-08-10T12:00:00Z"


class GetAccountById(Tool):
    """Fetch an account record by its account_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], account_id: Any) -> str:
        account_id = _idstr(account_id)
        if not account_id:
            return json.dumps({"error": "Missing required field: account_id"}, indent=2)
        accounts = data.get("accounts", [])
        for account in accounts:
            if account.get("account_id") == account_id:
                return json.dumps(account, indent=2)
        return json.dumps({"error": f"No account found with ID {account_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_account_by_id",
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
    """Fetch a company account record by its account_name."""

    @staticmethod
    def invoke(data: Dict[str, Any], name: Any) -> str:
        account_name = name
        if not account_name:
            return json.dumps({"error": "Missing required field: name"}, indent=2)
        accounts = data.get("accounts", [])
        for account in accounts:
            if account.get("account_name") == account_name:
                return json.dumps(account, indent=2)

        return json.dumps({"error": f"No account found with name '{account_name}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_account_by_name",
                "description": "Fetch a single company account's full details by its account_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Exact company account name to retrieve.",
                        }
                    },
                    "required": ["name"],
                },
            },
        }


class UpdateStreetAddress(Tool):
    """Update the shipping_street of an account by its account_id."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        account_id: Any,
        new_shipping_street: Any,
        new_billing_street: Any = None,
    ) -> str:
        account_id = _idstr(account_id)
        new_shipping_street = new_shipping_street
        new_billing_street = new_billing_street
        if not account_id or not new_shipping_street:
            return json.dumps(
                {"error": "Missing required field: account_id and/or new_shipping_street"}, indent=2
            )
        accounts = data.get("accounts", [])
        for account in accounts:
            if account.get("account_id") == account_id:
                account["shipping_street"] = new_shipping_street
                if new_billing_street:
                    account["billing_street"] = new_billing_street
                return json.dumps(account, indent=2)

        return json.dumps({"error": f"No account found with ID {account_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_street_address",
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
    """Fetch a contact by exact first_name and last_name."""

    @staticmethod
    def invoke(data: Dict[str, Any], first_name: Any, last_name: Any) -> str:
        first_name = first_name
        last_name = last_name
        if not first_name or not last_name:
            return json.dumps(
                {"error": "Missing required field: first_name and/or last_name"}, indent=2
            )
        contacts = data.get("contacts", [])
        for contact in contacts:
            if contact.get("first_name") == first_name and contact.get("last_name") == last_name:
                return json.dumps(contact, indent=2)

        return json.dumps(
            {"error": f"No contact found with name '{first_name} {last_name}'"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_contact_by_name",
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
    """Fetch all orders for a given contact_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], contact_id: Any) -> str:
        contact_id = _idstr(contact_id)
        if not contact_id:
            return json.dumps({"error": "Missing required field: contact_id"}, indent=2)

        orders = data.get("orders", [])
        contact_orders = [o for o in orders if o.get("contact_id") == contact_id]
        return json.dumps(contact_orders, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_orders_by_contact_id",
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
    """Batch increase stock quantities for multiple products (returns, cancellations)."""

    @staticmethod
    def invoke(data: Dict[str, Any], items: Any) -> str:
        if not isinstance(items, list) or not items:
            return json.dumps(
                {
                    "error": "Missing or invalid 'items'. Expected list of {product_id, quantity_to_add}."
                },
                indent=2,
            )

        products = data.get("products", [])
        results = []
        for it in items:
            pid = it.get("product_id")
            qty = it.get("quantity_to_add")
            if not pid or qty is None:
                return json.dumps(
                    {"error": "Each item must include product_id and quantity_to_add"}, indent=2
                )

            prod = next((p for p in products if p.get("product_id") == pid), None)
            if not prod:
                results.append({"product_id": pid, "error": "Product not found"})
                continue

            try:
                prod["stock_quantity"] = int(prod.get("stock_quantity", 0)) + int(qty)
            except (TypeError, ValueError):
                return json.dumps({"error": "quantity_to_add must be an integer"}, indent=2)

            results.append({"product_id": pid, "stock_quantity": prod["stock_quantity"]})

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_stock_quantities",
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
    def invoke(data: Dict[str, Any], items: Any) -> str:
        items = items
        if not items or not isinstance(items, list):
            return json.dumps(
                {
                    "error": "Missing or invalid 'items'. Expected a list of {product_id, pricebook_id}."
                },
                indent=2,
            )
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
                    if e.get("product_id") == product_id and e.get("pricebook_id") == pricebook_id
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
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_price_of_product",
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
    """Create a new offer and append it to the offers DB."""

    @staticmethod
    def invoke(
        data: Dict[str, Any], offer_code: Any, discount_type: Any, discount_value: Any
    ) -> str:
        offer_code = offer_code
        discount_type = discount_type
        discount_value = discount_value

        if not all([offer_code, discount_type, discount_value is not None]):
            return json.dumps(
                {"error": "Missing required fields: offer_code, discount_type, discount_value"},
                indent=2,
            )
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
        return json.dumps(new_offer, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_offer",
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
    """Deactivate an offer by its offer_code."""

    @staticmethod
    def invoke(data: Dict[str, Any], offer_code: Any) -> str:
        offer_code = offer_code
        if not offer_code:
            return json.dumps({"error": "Missing required field: offer_code"}, indent=2)
        offers = data.get("offers", [])
        for offer in offers:
            if offer.get("offer_code") == offer_code:
                offer["is_active"] = False
                return json.dumps(offer, indent=2)

        return json.dumps({"error": f"No offer found with code '{offer_code}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deactivate_offer",
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
    """Fetch full details of an offer by offer_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], offer_id: Any) -> str:
        offer_id = _idstr(offer_id)
        if not offer_id:
            return json.dumps({"error": "Missing required field: offer_id"}, indent=2)
        offers = data.get("offers", [])
        for offer in offers:
            if offer.get("offer_id") == offer_id:
                return json.dumps(offer, indent=2)

        return json.dumps({"error": f"No offer found with ID '{offer_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_offer_details",
                "description": "Fetch full details of an offer by offer_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "offer_id": {"type": "string", "description": "Exact offer ID to retrieve."}
                    },
                    "required": ["offer_id"],
                },
            },
        }


class GetCartByContactId(Tool):
    """Fetch full cart details by contact_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], contact_id: Any) -> str:
        contact_id = _idstr(contact_id)
        if not contact_id:
            return json.dumps({"error": "Missing required field: contact_id"}, indent=2)
        carts = data.get("carts", [])
        for cart in carts:
            if cart.get("contact_id") == contact_id:
                return json.dumps(cart, indent=2)

        return json.dumps({"error": f"No cart found for contact_id '{contact_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_cart_by_contact_id",
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
    """Fetch all items in a cart by cart_id in simplified format."""

    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any) -> str:
        cart_id = _idstr(cart_id)
        if not cart_id:
            return json.dumps({"error": "Missing required field: cart_id"}, indent=2)
        cart_items = data.get("cart_items", [])
        items_list = []
        for item in cart_items:
            if item.get("cart_id") == cart_id:
                items_list.append(
                    {"product_id": item.get("product_id"), "quantity": item.get("quantity")}
                )

        if not items_list:
            return json.dumps({"error": f"No items found for cart_id '{cart_id}'"}, indent=2)

        return json.dumps(items_list, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_items_in_cart",
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
    """Remove all items from a given cart."""

    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any) -> str:
        cart_id = _idstr(cart_id)
        if not cart_id:
            return json.dumps({"error": "Missing required field: cart_id"}, indent=2)
        cart_items = data.get("cart_items", [])
        removed_count = 0
        for item in list(cart_items):
            if item.get("cart_id") == cart_id:
                cart_items.remove(item)
                removed_count += 1

        if removed_count == 0:
            return json.dumps({"error": f"No items found for cart_id '{cart_id}'"}, indent=2)

        return json.dumps(
            {"message": f"All items removed from cart '{cart_id}'", "removed_count": removed_count},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "clear_cart",
                "description": "Remove all items from a given cart.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cart_id": {"type": "string", "description": "ID of the cart to clear."}
                    },
                    "required": ["cart_id"],
                },
            },
        }


class GetOrderDetailsById(Tool):
    """Fetch full order details by order_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: Any) -> str:
        order_id = _idstr(order_id)
        if not order_id:
            return json.dumps({"error": "Missing required field: order_id"}, indent=2)
        orders = data.get("orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                return json.dumps(order, indent=2)

        return json.dumps({"error": f"No order found with ID '{order_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_details_by_id",
                "description": "Fetch full order details by order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Exact order ID to retrieve."}
                    },
                    "required": ["order_id"],
                },
            },
        }


class UpdateOrderStatus(Tool):
    """Update the status of an existing order."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: Any, new_status: Any) -> str:
        order_id = _idstr(order_id)
        orders = data.get("orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                order["status"] = new_status
                return json.dumps(order, indent=2)

        return json.dumps({"error": f"No order found with ID '{order_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_order_status",
                "description": "Update the status of an existing order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Exact order ID to update."},
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
    """Return all order_items rows for a given order_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: Any) -> str:
        order_id = _idstr(order_id)
        if not order_id:
            return json.dumps({"error": "Missing required field: order_id"}, indent=2)
        order_items: List[Dict[str, Any]] = data.get("order_items", [])
        items = [item for item in order_items if item.get("order_id") == order_id]
        return json.dumps(items, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_order_items_by_order_id",
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
    """Create a new case and append it to the cases DB."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
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
        if not contact_id or not account_id or not subject or not priority:
            return json.dumps(
                {"error": "Missing required fields: contact_id, account_id, subject, priority"},
                indent=2,
            )
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
        return json.dumps(new_case, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_case",
                "description": "Create a new case and append it to the cases DB. Default status is 'New'.",
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
                        "subject": {"type": "string", "description": "Subject line for the case."},
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
    """Update the status of an existing case."""

    @staticmethod
    def invoke(data: Dict[str, Any], case_id: Any, status: Any) -> str:
        case_id = case_id
        if not case_id or not status:
            return json.dumps({"error": "Missing required fields: case_id and/or status"}, indent=2)
        cases = data.get("cases", [])
        for case in cases:
            if case.get("case_id") == case_id:
                case["status"] = status
                return json.dumps(case, indent=2)

        return json.dumps({"error": f"No case found with ID '{case_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_case_status",
                "description": "Update the status of an existing case.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "case_id": {"type": "string", "description": "Exact case ID to update."},
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
    def invoke(data: Dict[str, Any], items: Any) -> str:
        items: List[Dict[str, Any]] = items
        if not items or not isinstance(items, list):
            return json.dumps(
                {
                    "error": "Missing or invalid 'items'. Expected a list of {product_id, quantity, price}."
                },
                indent=2,
            )

        total = Decimal("0")
        for item in items:
            product_id = item.get("product_id")
            quantity = item.get("quantity")
            price = item.get("price")
            if product_id is None or quantity is None or price is None:
                return json.dumps(
                    {"error": "Each item must include product_id, quantity, price"}, indent=2
                )
            try:
                q = int(quantity)
                p = _money(_dec(price))
            except Exception:
                return json.dumps(
                    {"error": f"Invalid numeric values for product_id '{product_id}'"}, indent=2
                )
            line = _money(p * Decimal(q))
            total += line

        total = _money(total)
        return json.dumps({"subtotal": _to_number(total)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_sub_total_price",
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
    def invoke(data: Dict[str, Any], subtotal: Any, discount_amount: Any) -> str:
        if subtotal is None or discount_amount is None:
            return json.dumps(
                {"error": "Missing required fields: subtotal and/or discount_amount"}, indent=2
            )
        try:
            sub = _money(_dec(subtotal))
            disc = _money(_dec(discount_amount))
        except Exception:
            return json.dumps({"error": "subtotal and discount_amount must be numeric"}, indent=2)
        total = _money(max(sub - disc, Decimal("0")))
        return json.dumps({"total": _to_number(total)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_discount_flat",
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
    def invoke(data: Dict[str, Any], subtotal: Any, discount_percent: Any) -> str:
        if subtotal is None or discount_percent is None:
            return json.dumps(
                {"error": "Missing required fields: subtotal and/or discount_percent"}, indent=2
            )
        try:
            sub = _money(_dec(subtotal))
            pct = _dec(discount_percent) / Decimal("100")
        except Exception:
            return json.dumps({"error": "subtotal and discount_percent must be numeric"}, indent=2)

        disc = _money(sub * pct)
        total = _money(max(sub - disc, Decimal("0")))
        return json.dumps(
            {"discount_amount": _to_number(disc), "total": _to_number(total)}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_discount_percent",
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
    """Fetch multiple products' full details by exact names (batch)."""

    @staticmethod
    def invoke(data: Dict[str, Any], names: Any) -> str:
        names = names
        if not names or not isinstance(names, list):
            return json.dumps(
                {"error": "Missing or invalid 'names'. Expected a list of product names."}, indent=2
            )
        products = data.get("products", [])
        results: List[Dict[str, Any]] = []
        for n in names:
            match = next((p for p in products if p.get("name") == n), None)
            results.append(match if match else {"name": n, "error": "Product not found"})
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_products_by_names",
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
    """Add multiple products to a cart in one call."""

    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any, items: Any) -> str:
        cart_id = cart_id
        items: List[Dict[str, Any]] = items
        if not cart_id or not items or not isinstance(items, list):
            return json.dumps(
                {
                    "error": "Missing required fields: cart_id and list 'items' with {product_id, quantity}"
                },
                indent=2,
            )
        cart_items = data.get("cart_items", [])
        created = []
        next_num = len(cart_items) + 1
        for it in items:
            pid = it.get("product_id")
            qty = it.get("quantity")
            if not pid or qty is None:
                return json.dumps(
                    {"error": "Each item must include product_id and quantity"}, indent=2
                )
            rec = {
                "cart_item_id": f"item_{next_num}",
                "cart_id": cart_id,
                "product_id": pid,
                "quantity": int(qty),
            }
            cart_items.append(rec)
            created.append(rec)
            next_num += 1
        return json.dumps(created, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_items_to_cart_batch",
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
    """Update quantities for multiple products in a cart in one call."""

    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any, items: Any) -> str:
        cart_id = cart_id
        items: List[Dict[str, Any]] = items
        if not cart_id or not items or not isinstance(items, list):
            return json.dumps(
                {
                    "error": "Missing required fields: cart_id and list 'items' with {product_id, new_quantity}"
                },
                indent=2,
            )
        cart_items = data.get("cart_items", [])
        updated = []
        for it in items:
            pid = it.get("product_id")
            new_q = it.get("new_quantity")
            if not pid or new_q is None:
                return json.dumps(
                    {"error": "Each item must include product_id and new_quantity"}, indent=2
                )
            for row in cart_items:
                if row.get("cart_id") == cart_id and row.get("product_id") == pid:
                    row["quantity"] = int(new_q)
                    updated.append(row)
                    break
        if not updated:
            return json.dumps(
                {"error": f"No matching items found to update for cart '{cart_id}'"}, indent=2
            )
        return json.dumps(updated, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_items_in_cart_batch",
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
    """Remove multiple products from a cart in one call."""

    @staticmethod
    def invoke(data: Dict[str, Any], cart_id: Any, product_ids: Any) -> str:
        cart_id = cart_id
        product_ids: List[str] = product_ids
        if not cart_id or not product_ids or not isinstance(product_ids, list):
            return json.dumps(
                {"error": "Missing required fields: cart_id and list 'product_ids'."}, indent=2
            )
        cart_items = data.get("cart_items", [])
        before = len(cart_items)
        cart_items[:] = [
            r
            for r in cart_items
            if not (r.get("cart_id") == cart_id and r.get("product_id") in product_ids)
        ]
        removed = before - len(cart_items)
        return json.dumps(
            {"removed_count": removed, "cart_id": cart_id, "removed_product_ids": product_ids},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_items_from_cart_batch",
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
    """Validate order using live stock, without passing available_quantity explicitly."""

    @staticmethod
    def invoke(data: Dict[str, Any], items: Any) -> str:
        items: List[Dict[str, Any]] = items
        if not items or not isinstance(items, list):
            return json.dumps(
                {
                    "error": "Missing or invalid 'items'. Expected list of {product_id, required_quantity}."
                },
                indent=2,
            )
        products = data.get("products", [])
        results = []
        is_valid = True
        for it in items:
            pid = it.get("product_id")
            req = it.get("required_quantity")
            if not pid or req is None:
                return json.dumps(
                    {"error": "Each item must include product_id and required_quantity"}, indent=2
                )
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
        return json.dumps({"is_valid": is_valid, "Valid_item_list": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_order_from_stock",
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
    def invoke(data: Dict[str, Any], subtotal: Any, offer_code: Any) -> str:
        if subtotal is None or not offer_code:
            return json.dumps(
                {"error": "Missing required fields: subtotal and/or offer_code"}, indent=2
            )
        try:
            sub = _money(_dec(subtotal))
        except Exception:
            return json.dumps({"error": "subtotal must be numeric"}, indent=2)

        offers = data.get("offers", [])
        match = next((o for o in offers if o.get("offer_code") == offer_code), None)
        if not match:
            return json.dumps({"valid": False, "reason": "Offer not found"}, indent=2)
        if not match.get("is_active", False):
            return json.dumps({"valid": False, "reason": "Offer is inactive"}, indent=2)

        dtype = match.get("discount_type")
        dval = _dec(match.get("discount_value", 0))

        if dtype == "PERCENTAGE":
            disc = _money(sub * dval / Decimal("100"))
        elif dtype == "FIXED_AMOUNT":
            disc = _money(dval)
        else:
            return json.dumps({"error": f"Unknown discount_type '{dtype}'"}, indent=2)

        total = _money(max(sub - disc, Decimal("0")))
        return json.dumps(
            {
                "valid": True,
                "offer": match,
                "subtotal": _to_number(sub),
                "discount_amount": _to_number(disc),
                "total": _to_number(total),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_offer_to_subtotal",
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


class InventorySecurityGroupRules(Tool):
    """Return a compact inventory of all security group rule IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        rules = data.get("aws_security_group_rules", [])
        return json.dumps({"rule_ids": [r.get("rule_id") for r in rules]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "inventory_security_group_rules",
                "description": "List all AWS security group rule IDs.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class GetSecurityGroupRuleById(Tool):
    """Fetch a security group rule by rule_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], rule_id: Any) -> str:
        rule_id = _idstr(rule_id)
        rules = data.get("aws_security_group_rules", [])
        for r in rules:
            if r.get("rule_id") == rule_id:
                return json.dumps(r, indent=2)
        return json.dumps({"error": f"No security group rule found with ID '{rule_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_security_group_rule_by_id",
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


class UpdateSubnetGroupDescription(Tool):
    """Replace the description on a subnet group."""

    @staticmethod
    def invoke(data: Dict[str, Any], subnet_group_id: Any, new_description: Any) -> str:
        subnet_group_id = _idstr(subnet_group_id)
        groups = data.get("aws_subnet_groups", [])
        for g in groups:
            if g.get("subnet_group_id") == subnet_group_id:
                g["description"] = new_description
                return json.dumps(g, indent=2)
        return json.dumps({"error": f"No subnet group found with ID '{subnet_group_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_subnet_group_description",
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


def _next_aws_plan_id(data: Dict[str, Any]) -> str:
    plans = data.setdefault("aws_plans", [])
    return f"ap-{len(plans)+1:04d}"


class CreateIngressChangePlan(Tool):
    name = "create_ingress_change_plan"
    description = "Create a deterministic ingress change plan ap-0001 for a given rule."

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        rule_id: Any,
        target_cidr: Any,
        final_description: Any = None,
        env_tag: Any = None,
    ) -> Dict[str, Any]:
        rules = data.get("aws_security_group_rules", [])

        def find_rule(rid):
            if isinstance(rules, dict):
                return rules.get(rid)
            for r in rules:
                if r.get("rule_id") == rid:
                    return r
            return None

        rule = find_rule(rule_id)
        if not rule:
            return {"error": f"Unknown rule_id '{rule_id}'"}
        plan = {
            "plan_id": "ap-0001",
            "type": "ingress",
            "rule_id": rule_id,
            "target_cidr": target_cidr,
            "final_description": final_description,
            "env_tag": env_tag,
            "steps": ["update_rule", "consolidate", "standardize"],
        }
        rule["_pending_ingress_plan"] = plan
        data["_last_ingress_plan_rule_id"] = rule_id
        data["_last_ingress_plan_id"] = "ap-0001"
        return {"plan_id": "ap-0001", "steps": ["update_rule", "consolidate", "standardize"]}

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_ingress_change_plan",
                "description": "Create a plan (update, consolidate, standardize) for a rule_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_id": {"type": "string"},
                        "target_cidr": {"type": "string"},
                        "final_description": {"type": "string"},
                        "env_tag": {"type": "string"},
                    },
                    "required": ["rule_id", "target_cidr"],
                },
            },
        }


class ApplyIngressPlanStep(Tool):
    name = "apply_ingress_plan_step"
    description = "Apply a single step of the most recent ingress plan."

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        plan_id: Any,
        step_index: Any,
    ) -> Dict[str, Any]:
        rules = data.get("aws_security_group_rules", [])

        def find_rule(rid):
            if isinstance(rules, dict):
                return rules.get(rid)
            for r in rules:
                if r.get("rule_id") == rid:
                    return r
            return None

        def remove_rules(ids):
            if isinstance(rules, dict):
                for rid in ids:
                    rules.pop(rid, None)
            else:
                idxs = [i for i, r in enumerate(rules) if r.get("rule_id") in ids]
                for i in sorted(idxs, reverse=True):
                    rules.pop(i)

        last_rule_id = data.get("_last_ingress_plan_rule_id")
        if not last_rule_id:
            return {"error": f"No ingress plan '{plan_id}'"}
        rule = find_rule(last_rule_id)
        if not rule:
            return {"error": f"No ingress plan '{plan_id}'"}
        plan = rule.get("_pending_ingress_plan")
        if not plan or plan.get("plan_id") != plan_id:
            return {"error": f"No ingress plan '{plan_id}'"}
        steps = plan.get("steps", [])
        i = int(step_index)
        if i < 0 or i >= len(steps):
            return {"error": f"Invalid step_index '{step_index}'"}
        action = steps[i]
        if action == "update_rule":
            rule["source_ip"] = plan["target_cidr"]
            rule["description"] = plan["final_description"]
            return {
                "rule_id": rule["rule_id"],
                "security_group_id": rule["security_group_id"],
                "protocol": rule.get("protocol", "TCP"),
                "port": rule.get("port", 6379),
                "source_ip": rule["source_ip"],
                "description": rule["description"],
            }
        if action == "consolidate":
            sg_id = rule["security_group_id"]
            port = rule.get("port", 6379)
            proto = rule.get("protocol", "TCP")
            same = []
            if isinstance(rules, dict):
                same = [
                    r
                    for r in rules.values()
                    if r.get("security_group_id") == sg_id
                    and r.get("port", 6379) == port
                    and r.get("protocol", "TCP") == proto
                ]
            else:
                same = [
                    r
                    for r in rules
                    if r.get("security_group_id") == sg_id
                    and r.get("port", 6379) == port
                    and r.get("protocol", "TCP") == proto
                ]
            keep_id = rule["rule_id"]
            removed = [r["rule_id"] for r in same if r.get("rule_id") != keep_id]
            remove_rules(removed)
            return {
                "consolidated_rule": {
                    "rule_id": rule["rule_id"],
                    "security_group_id": rule["security_group_id"],
                    "protocol": proto,
                    "port": port,
                    "source_ip": rule["source_ip"],
                    "description": rule["description"],
                },
                "removed": removed,
            }
        if action == "standardize":
            tag = plan.get("env_tag")
            updated = []
            if tag:
                if not str(rule.get("description", "")).endswith(f" [{tag}]"):
                    rule["description"] = f"{rule['description']} [{tag}]"
                updated.append(
                    {
                        "rule_id": rule["rule_id"],
                        "security_group_id": rule["security_group_id"],
                        "protocol": rule.get("protocol", "TCP"),
                        "port": rule.get("port", 6379),
                        "source_ip": rule["source_ip"],
                        "description": rule["description"],
                    }
                )
            return {"updated": updated, "count": len(updated)}
        return {"error": f"Unknown step '{action}'"}

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_ingress_plan_step",
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


class CreateClusterChangePlan(Tool):
    name = "create_cluster_change_plan"
    description = "Create a deterministic cluster change plan ap-0001 for a given cluster."

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        cluster_id: Any,
        reference_rule_id: Any,
        subnet_group_id: Any,
        new_status: Any,
        new_name: Any,
        note: Any,
        env_tag: Any = None,
        consolidate_cidr: Any = None,
        consolidate_desc: Any = None,
        endpoint_url: Any = None,
    ) -> str:
        clusters = data.get("aws_clusters", {})
        cluster = clusters.get(cluster_id)
        if not cluster:
            return {"error": f"Unknown cluster_id '{cluster_id}'"}
        plan = {
            "plan_id": "ap-0001",
            "type": "cluster",
            "cluster_id": cluster_id,
            "reference_rule_id": reference_rule_id,
            "subnet_group_id": subnet_group_id,
            "new_status": new_status,
            "new_name": new_name,
            "note": note,
            "env_tag": env_tag,
            "consolidate_cidr": consolidate_cidr,
            "consolidate_desc": consolidate_desc,
            "endpoint_url": endpoint_url,
            "steps": [
                "attach_sg",
                "attach_subnet_group",
                "set_status",
                "set_name",
                "set_note",
                "consolidate_ingress",
                "standardize_env_on_sg",
                "set_endpoint",
            ],
        }
        cluster["_pending_cluster_plan"] = plan
        data["_last_cluster_plan_cluster_id"] = cluster_id
        data["_last_cluster_plan_id"] = "ap-0001"
        return {"plan_id": "ap-0001"}

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_cluster_change_plan",
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
                        "consolidate_cidr",
                        "consolidate_desc",
                        "endpoint_url",
                    ],
                },
            },
        }


class ApplyClusterPlanStep(Tool):
    name = "apply_cluster_plan_step"
    description = "Apply a single step of the most recent cluster plan."

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        plan_id: Any,
        step_index: Any,
    ) -> Dict[str, Any]:
        clusters = data.get("aws_clusters", [])
        rules = data.get("aws_security_group_rules", [])

        def find_cluster(cid):
            if isinstance(clusters, dict):
                return clusters.get(cid)
            for c in clusters:
                if c.get("cluster_id") == cid:
                    return c
            return None

        def find_rule(rid):
            if isinstance(rules, dict):
                return rules.get(rid)
            for r in rules:
                if r.get("rule_id") == rid:
                    return r
            return None

        def iter_rules():
            if isinstance(rules, dict):
                return list(rules.values())
            return list(rules)

        def remove_rules(ids):
            if isinstance(rules, dict):
                for rid in ids:
                    rules.pop(rid, None)
            else:
                idxs = [i for i, r in enumerate(rules) if r.get("rule_id") in ids]
                for i in sorted(idxs, reverse=True):
                    rules.pop(i)

        last_cid = data.get("_last_cluster_plan_cluster_id")
        if not last_cid:
            return {"error": f"No cluster plan '{plan_id}'"}
        cluster = find_cluster(last_cid)
        if not cluster:
            return {"error": f"No cluster plan '{plan_id}'"}
        plan = cluster.get("_pending_cluster_plan")
        if not plan or plan.get("plan_id") != plan_id:
            return {"error": f"No cluster plan '{plan_id}'"}
        i = int(step_index)
        steps = plan.get("steps", [])
        if i < 0 or i >= len(steps):
            return {"error": f"Invalid step_index '{step_index}'"}
        action = steps[i]
        if action == "attach_sg":
            rule = find_rule(plan["reference_rule_id"])
            if rule:
                cluster["security_group_id"] = rule["security_group_id"]
            return {
                "cluster_id": cluster["cluster_id"],
                "security_group_id": cluster.get("security_group_id"),
            }
        if action == "attach_subnet_group":
            cluster["subnet_group_id"] = plan["subnet_group_id"]
            return {
                "cluster_id": cluster["cluster_id"],
                "subnet_group_id": cluster["subnet_group_id"],
            }
        if action == "set_status":
            cluster["status"] = plan["new_status"]
            return {"cluster_id": cluster["cluster_id"], "status": cluster["status"]}
        if action == "set_name":
            cluster["name"] = plan["new_name"]
            return {"cluster_id": cluster["cluster_id"], "name": cluster["name"]}
        if action == "set_note":
            cluster["note"] = plan["note"]
            return {"cluster_id": cluster["cluster_id"], "note": cluster["note"]}
        if action == "consolidate_ingress":
            sg_id = cluster.get("security_group_id")
            port = 6379
            proto = "TCP"
            same = [
                r
                for r in iter_rules()
                if r.get("security_group_id") == sg_id
                and r.get("port", 6379) == port
                and r.get("protocol", "TCP") == proto
            ]
            keep = same[0] if same else None
            removed = [r["rule_id"] for r in same[1:]] if len(same) > 1 else []
            if removed:
                remove_rules(removed)
            if keep:
                if plan.get("consolidate_cidr") is not None:
                    keep["source_ip"] = plan["consolidate_cidr"]
                if plan.get("consolidate_desc") is not None:
                    keep["description"] = plan["consolidate_desc"]
            return {"security_group_id": sg_id, "port": port}
        if action == "standardize_env_on_sg":
            tag = plan.get("env_tag")
            updated = 0
            if tag:
                sg_id = cluster.get("security_group_id")
                for r in iter_rules():
                    if r.get("security_group_id") != sg_id:
                        continue
                    if not str(r.get("description", "")).endswith(f" [{tag}]"):
                        r["description"] = f"{r['description']} [{tag}]"
                        updated += 1
            return {"updated": updated}
        if action == "set_endpoint":
            ep = plan.get("endpoint_url")
            if ep == "NULL":
                cluster["endpoint_url"] = None
            elif ep and ep != "NOCHANGE":
                cluster["endpoint_url"] = ep
            return {
                "cluster_id": cluster["cluster_id"],
                "endpoint_url": cluster.get("endpoint_url"),
            }
        return {"error": f"Unknown step '{action}'"}

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_cluster_plan_step",
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


class SetTraceFlag(Tool):
    """Enable/disable a trace flag for an org (ensure-exists)."""

    @staticmethod
    def invoke(data: Dict[str, Any], org_id: Any, flag_name: Any, is_active: Any) -> str:
        if not org_id or not flag_name or is_active is None:
            return json.dumps(
                {"error": "Missing required fields: org_id, flag_name, is_active"}, indent=2
            )
        flags = data.setdefault("trace_flags", [])
        for flag in flags:
            if flag.get("org_id") == org_id and flag.get("flag_name") == flag_name:
                flag["is_active"] = bool(is_active)
                return json.dumps(flag, indent=2)
        next_id = str(max([int(f.get("flag_id")) for f in flags] + [400]) + 1)
        record = {
            "flag_id": next_id,
            "org_id": org_id,
            "flag_name": flag_name,
            "is_active": bool(is_active),
        }
        flags.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_trace_flag",
                "description": "Ensure a trace flag exists and set its active state for the org.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "flag_name": {"type": "string"},
                        "is_active": {"type": "boolean"},
                    },
                    "required": ["org_id", "flag_name", "is_active"],
                },
            },
        }


class RunCacheJob(Tool):
    """Run a cache job for an org (idempotent). Sets last_run_status='Success' and last_run_time=policy NOW."""

    POLICY_NOW = "2025-08-10T12:00:00Z"

    @staticmethod
    def invoke(data: Dict[str, Any], org_id: Any, job_name: Any) -> str:
        if not org_id or not job_name:
            return json.dumps(
                {"error": "Missing required fields: org_id and/or job_name"}, indent=2
            )
        jobs = data.setdefault("cache_jobs", [])
        for job in jobs:
            if job.get("org_id") == org_id and job.get("job_name") == job_name:
                job["last_run_status"] = "Success"
                job["last_run_time"] = RunCacheJob.POLICY_NOW
                return json.dumps(job, indent=2)
        next_id = str(max([int(j.get("job_id")) for j in jobs] + [300]) + 1)
        record = {
            "job_id": next_id,
            "org_id": org_id,
            "job_name": job_name,
            "last_run_status": "Success",
            "last_run_time": RunCacheJob.POLICY_NOW,
        }
        jobs.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "run_cache_job",
                "description": "Mark a cache job as run for the org (Success at policy NOW); creates job if missing.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "job_name": {"type": "string"},
                    },
                    "required": ["org_id", "job_name"],
                },
            },
        }


class UpsertCustomSetting(Tool):
    """Upsert a custom setting value for an org (ensure-exists)."""

    @staticmethod
    def invoke(data: Dict[str, Any], org_id: Any, setting_name: Any, value: Any) -> str:
        if not org_id or not setting_name:
            return json.dumps(
                {"error": "Missing required fields: org_id and/or setting_name"}, indent=2
            )
        settings = data.setdefault("custom_settings", [])
        for rec in settings:
            if rec.get("org_id") == org_id and rec.get("setting_name") == setting_name:
                rec["value"] = value
                return json.dumps(rec, indent=2)
        next_id = str(max([int(s.get("setting_id")) for s in settings] + [100]) + 1)
        record = {
            "setting_id": next_id,
            "org_id": org_id,
            "setting_name": setting_name,
            "value": value,
        }
        settings.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_custom_setting",
                "description": "Create or update a custom setting (org_id + setting_name) with the provided value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "setting_name": {"type": "string"},
                        "value": {},
                    },
                    "required": ["org_id", "setting_name", "value"],
                },
            },
        }


class BuildBearerForConnectedApp(Tool):
    """Deterministically build an Authorization: Bearer header for an org/client pair (compute-only)."""

    @staticmethod
    def invoke(data: Dict[str, Any], org_id: Any, client_id: Any) -> str:
        if not org_id or not client_id:
            return json.dumps(
                {"error": "Missing required fields: org_id and/or client_id"}, indent=2
            )
        token = f"{org_id}:{client_id}"
        digest = hex(sum(ord(c) for c in token))[2:].rjust(16, "0")[-16:]
        header = f"Bearer {digest}"
        return json.dumps({"authorization_header": header}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "build_bearer_for_connected_app",
                "description": "Return a deterministic Authorization header (Bearer ...) for org_id + client_id (compute-only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "client_id": {"type": "string"},
                    },
                    "required": ["org_id", "client_id"],
                },
            },
        }


class EnsureConnectedApp(Tool):
    """Ensure a connected app exists for an org; create if missing, upsert scopes deterministically."""

    @staticmethod
    def invoke(
        data: Dict[str, Any], org_id: Any, app_name: Any, client_id: Any, oauth_scopes: Any
    ) -> str:
        if not org_id or not app_name or not client_id or oauth_scopes is None:
            return json.dumps(
                {"error": "Missing required fields: org_id, app_name, client_id, oauth_scopes"},
                indent=2,
            )
        if not isinstance(oauth_scopes, list):
            return json.dumps({"error": "oauth_scopes must be a list"}, indent=2)

        apps = data.setdefault("connected_apps", [])
        for app in apps:
            if app.get("org_id") == org_id and app.get("app_name") == app_name:
                merged = sorted(set(app.get("oauth_scopes", []) + oauth_scopes))
                app["client_id"] = client_id
                app["client_secret_stored"] = True
                app["oauth_scopes"] = merged
                return json.dumps(app, indent=2)

        next_id = str(max([int(a.get("app_id")) for a in apps] + [200]) + 1)
        record = {
            "app_id": next_id,
            "org_id": org_id,
            "app_name": app_name,
            "client_id": client_id,
            "client_secret_stored": True,
            "oauth_scopes": sorted(set(oauth_scopes)),
        }
        apps.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ensure_connected_app",
                "description": "Ensure a connected app exists with given client_id and scopes; create if missing; returns the app record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "app_name": {"type": "string"},
                        "client_id": {"type": "string"},
                        "oauth_scopes": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["org_id", "app_name", "client_id", "oauth_scopes"],
                },
            },
        }


class GetConnectedAppByName(Tool):
    """Fetch a connected app by exact app_name within a given org_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], org_id: Any, app_name: Any) -> str:
        if not org_id or not app_name:
            return json.dumps({"error": "Missing required field: org_id and/or app_name"}, indent=2)
        apps = data.get("connected_apps", [])
        for app in apps:
            if app.get("org_id") == org_id and app.get("app_name") == app_name:
                return json.dumps(app, indent=2)
        return json.dumps(
            {"error": f"Connected app not found for org_id={org_id}, app_name={app_name}"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_connected_app_by_name",
                "description": "Resolve a connected app by app_name within the specified org_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "app_name": {"type": "string"},
                    },
                    "required": ["org_id", "app_name"],
                },
            },
        }


class GetOrgByName(Tool):
    """Fetch a Salesforce org by exact org_name (e.g., 'UAT', 'Production')."""

    @staticmethod
    def invoke(data: Dict[str, Any], org_name: Any) -> str:
        if not org_name:
            return json.dumps({"error": "Missing required field: org_name"}, indent=2)
        orgs = data.get("salesforce_orgs", [])
        for org in orgs:
            if org.get("org_name") == org_name:
                return json.dumps(org, indent=2)
        return json.dumps({"error": f"Org not found: {org_name}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_org_by_name",
                "description": "Resolve a Salesforce org by org_name ('UAT', 'Production'). Returns the org record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_name": {"type": "string"},
                    },
                    "required": ["org_name"],
                },
            },
        }


class PriceAndApplyOfferByNames(Tool):
    """
    Price items by product name and pricebook, then apply an offer code.
    Inputs:
      - pricebook_id: str
      - items_by_name: [{ "name": str, "quantity": int }]
      - offer_code: str
    Returns:
      {
        "items": [
          {"product_id": "...", "name": "...", "quantity": int, "unit_price": float, "line_total": float}
        ],
        "subtotal": float,
        "applied_offer_code": str,
        "discount_amount": float,
        "total": float
      }
    """

    @staticmethod
    def invoke(data: Dict[str, Any], pricebook_id: Any, items_by_name: Any, offer_code: Any) -> str:
        def _err(msg):
            return json.dumps({"error": msg}, indent=2)

        if not pricebook_id or not isinstance(items_by_name, list) or not offer_code:
            return _err("Missing required fields: pricebook_id, items_by_name (list), offer_code")

        products = data.get("products", [])
        price_entries = data.get("pricebook_entries", []) or data.get("prices", [])
        offers = data.get("offers", [])

        name_to_product = {p.get("name"): p for p in products if p.get("name")}

        def _price_for(pid, pbid):
            for e in price_entries:
                if e.get("product_id") == pid and str(e.get("pricebook_id")) == str(pbid):
                    return float(e.get("price"))
            return None

        offer_rec = None
        for o in offers:
            if o.get("offer_code") == offer_code or o.get("code") == offer_code:
                offer_rec = o
                break
        if offer_rec is None:
            offer_rec = {
                "offer_code": offer_code,
                "discount_type": "PERCENTAGE",
                "discount_value": 0.0,
            }

        lines = []
        subtotal = 0.0
        for item in items_by_name:
            nm = item.get("name")
            qty = int(item.get("quantity", 0))
            prod = name_to_product.get(nm)
            if not prod:
                return _err(f"Product not found by name: {nm}")
            pid = prod.get("product_id")
            unit_price = _price_for(pid, pricebook_id)
            if unit_price is None:
                return _err(f"Price not found for product_id={pid} in pricebook_id={pricebook_id}")
            line_total = unit_price * qty
            subtotal += line_total
            lines.append(
                {
                    "product_id": pid,
                    "name": nm,
                    "quantity": qty,
                    "unit_price": unit_price,
                    "line_total": line_total,
                }
            )
        discount_amount = 0.0
        dtype = str(offer_rec.get("discount_type", "PERCENTAGE")).upper()
        dval = float(offer_rec.get("discount_value", 0.0))
        if dtype == "PERCENTAGE":
            discount_amount = round(subtotal * (dval / 100.0), 2)
        elif dtype == "FIXED_AMOUNT":
            discount_amount = min(subtotal, dval)
        total = round(subtotal - discount_amount, 2)

        result = {
            "items": lines,
            "subtotal": round(subtotal, 2),
            "applied_offer_code": offer_code,
            "discount_amount": discount_amount,
            "total": total,
        }
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "price_and_apply_offer_by_names",
                "description": "Resolve product names via catalog, price by pricebook, compute subtotal, apply offer, and return totals.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pricebook_id": {"type": "string"},
                        "items_by_name": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                                "required": ["name", "quantity"],
                            },
                        },
                        "offer_code": {"type": "string"},
                    },
                    "required": ["pricebook_id", "items_by_name", "offer_code"],
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
    UpdateSubnetGroupDescription(),
    CreateIngressChangePlan(),
    ApplyIngressPlanStep(),
    CreateClusterChangePlan(),
    ApplyClusterPlanStep(),
    GetOrgByName(),
    GetConnectedAppByName(),
    EnsureConnectedApp(),
    BuildBearerForConnectedApp(),
    UpsertCustomSetting(),
    RunCacheJob(),
    SetTraceFlag(),
    PriceAndApplyOfferByNames(),
]
