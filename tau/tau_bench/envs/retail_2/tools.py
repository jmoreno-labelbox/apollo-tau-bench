import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


class FindUserIdByNameZip(Tool):
    """Locate a user_id using first name, last name, and ZIP code."""

    @staticmethod
    def invoke(data: dict[str, Any], first_name: str, last_name: str, zip: str) -> str:
        users = data.get("users", {}).values()
        for user in users.values():
            if (
                user.get("name", {}).values().get("first_name") == first_name
                and user.get("name", {}).values().get("last_name") == last_name
                and user.get("address", {}).values().get("zip") == zip
            ):
                payload = {"user_id": user.get("user_id")}
                out = json.dumps(payload)
                return out
        payload = {
                "error": "User not found",
                "first_name": first_name,
                "last_name": last_name,
                "zip": zip,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindUserIdByNameZip",
                "description": "Find user_id from users.json by first name, last name, and ZIP code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                        "zip": {"type": "string"},
                    },
                    "required": ["first_name", "last_name", "zip"],
                },
            },
        }


class GetUserDetails(Tool):
    """Obtain complete user information from users.json using user_id."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        users = data.get("users", {}).values()
        for user in users.values():
            if user.get("user_id") == user_id:
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found", "user_id": user_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserDetails",
                "description": "Get user details from users.json by user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class GetUserOrders(Tool):
    """Fetch the list of order IDs associated with a specific user_id."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        users = data.get("users", {}).values()
        for user in users.values():
            if user.get("user_id") == user_id:
                payload = {"orders": user.get("orders", [])}
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found", "user_id": user_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserOrders",
                "description": "Get order IDs linked to a given user_id from users.json.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class UpdateUserAddress(Tool):
    """Modify the user's address in users.json using user_id."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, address: dict[str, Any]) -> str:
        users = data.get("users", {}).values()
        for user in users.values():
            if user.get("user_id") == user_id:
                user["address"] = address
                payload = {"status": "success", "user_id": user_id, "address": address}
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found", "user_id": user_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserAddress",
                "description": "Update a user's address in users.json by user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "address": {
                            "type": "object",
                            "description": "Full address object with address1, address2, city, country, state, zip",
                        },
                    },
                    "required": ["user_id", "address"],
                },
            },
        }


class GetUserPaymentMethods(Tool):
    """Enumerate all payment options for a specified user_id."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        users = data.get("users", {}).values()
        for user in users.values():
            if user.get("user_id") == user_id:
                payload = {"payment_methods": user.get("payment_methods", {}).values()}
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found", "user_id": user_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserPaymentMethods",
                "description": "Retrieve payment methods for a given user_id from users.json.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


#------------------------
#Tools related to Orders (5)
#------------------------


class GetOrderDetails(Tool):
    """Retrieve complete order information from orders.json using order_id."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        orders = data.get("orders", {}).values()
        for order in orders.values():
            if order.get("order_id") == order_id:
                payload = order
                out = json.dumps(payload)
                return out
        payload = {"error": "Order not found", "order_id": order_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrderDetails",
                "description": "Get order details from orders.json by order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class GetOrderStatus(Tool):
    """Provide solely the status of an order."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        orders = data.get("orders", {}).values()
        for order in orders.values():
            if order.get("order_id") == order_id:
                payload = {"order_id": order_id, "status": order.get("status")}
                out = json.dumps(payload)
                return out
        payload = {"error": "Order not found", "order_id": order_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrderStatus",
                "description": "Return the order status by order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


class UpdateOrderStatus(Tool):
    """Alter the status of an order in a predictable manner."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str, status: str) -> str:
        orders = data.get("orders", {}).values()
        for order in orders.values():
            if order.get("order_id") == order_id:
                order["status"] = status
                payload = {"status": "success", "order_id": order_id, "new_status": status}
                out = json.dumps(payload)
                return out
        payload = {"error": "Order not found", "order_id": order_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOrderStatus",
                "description": "Update order status (e.g., pending, delivered, cancelled) by order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["order_id", "status"],
                },
            },
        }


class AddOrderFulfillment(Tool):
    """Insert a fulfillment entry containing tracking IDs for designated item IDs."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        tracking_ids: list[str],
        item_ids: list[str]
    ) -> str:
        orders = data.get("orders", {}).values()
        for order in orders.values():
            if order.get("order_id") == order_id:
                fulfillments = order.get("fulfillments", [])
                fulfillments.append({"tracking_id": tracking_ids, "item_ids": item_ids})
                order["fulfillments"] = fulfillments
                payload = {
                    "status": "success",
                    "order_id": order_id,
                    "fulfillments": order["fulfillments"],
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Order not found", "order_id": order_id}
        out = json.dumps(payload)
        return out
        pass
        orders = data.get("orders", {}).values()
        for order in orders.values():
            if order.get("order_id") == order_id:
                fulfillments = order.get("fulfillments", [])
                fulfillments.append({"tracking_id": tracking_ids, "item_ids": item_ids})
                order["fulfillments"] = fulfillments
                payload = {
                        "status": "success",
                        "order_id": order_id,
                        "fulfillments": order["fulfillments"],
                    }
                out = json.dumps(
                    payload)
                return out
        payload = {"error": "Order not found", "order_id": order_id}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddOrderFulfillment",
                "description": "Add fulfillment with tracking IDs and covered item IDs to an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "tracking_ids": {"type": "array", "items": {"type": "string"}},
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["order_id", "tracking_ids", "item_ids"],
                },
            },
        }


class GetOrderPaymentHistory(Tool):
    """Provide payment transaction details for an order."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        orders = data.get("orders", {}).values()
        for order in orders.values():
            if order.get("order_id") == order_id:
                payload = {
                    "order_id": order_id,
                    "payment_history": order.get("payment_history", []),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Order not found", "order_id": order_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrderPaymentHistory",
                "description": "Get the payment_history array for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


#------------------------
#Tools related to Products (5)
#------------------------


class GetProductDetails(Tool):
    """Obtain product information from products.json using product_id."""

    @staticmethod
    def invoke(data: dict[str, Any], product_id: str) -> str:
        products = data.get("products", {}).values()
        for product in products.values():
            if product.get("product_id") == product_id:
                payload = product
                out = json.dumps(payload)
                return out
        payload = {"error": "Product not found", "product_id": product_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductDetails",
                "description": "Get product details by product_id from products.json.",
                "parameters": {
                    "type": "object",
                    "properties": {"product_id": {"type": "string"}},
                    "required": ["product_id"],
                },
            },
        }


class GetVariantDetails(Tool):
    """Fetch a variant (using item_id) from products.json."""

    @staticmethod
    def invoke(data: dict[str, Any], item_id: str) -> str:
        products = data.get("products", {}).values()
        for product in products.values():
            variants = product.get("variants", {}).values()
            var = variants.get(item_id)
            if var:
                result = {"product_id": product.get("product_id"), "variant": var}
                payload = result
                out = json.dumps(payload)
                return out
        payload = {"error": "Variant not found", "item_id": item_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetVariantDetails",
                "description": "Get variant details by item_id from products.json.",
                "parameters": {
                    "type": "object",
                    "properties": {"item_id": {"type": "string"}},
                    "required": ["item_id"],
                },
            },
        }


class ListAvailableVariants(Tool):
    """Enumerate the variants available for a product."""

    @staticmethod
    def invoke(data: dict[str, Any], product_id: str) -> str:
        products = data.get("products", {}).values()
        for product in products.values():
            if product.get("product_id") == product_id:
                variants = product.get("variants", {}).values()
                available = [v for v in variants.values() if v.get("available") is True]
                payload = {"product_id": product_id, "available_variants": available}
                out = json.dumps(payload)
                return out
        payload = {"error": "Product not found", "product_id": product_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAvailableVariants",
                "description": "List variants with available=true for a given product_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"product_id": {"type": "string"}},
                    "required": ["product_id"],
                },
            },
        }


class UpdateVariantAvailability(Tool):
    """Modify the 'available' status of a variant."""

    @staticmethod
    def invoke(
        data: dict[str, Any], product_id: str, item_id: str, available: bool
    ) -> str:
        products = data.get("products", {}).values()
        for product in products.values():
            if product.get("product_id") == product_id:
                variants = product.get("variants", {}).values()
                if item_id in variants:
                    variants[item_id]["available"] = available
                    payload = {
                        "status": "success",
                        "product_id": product_id,
                        "item_id": item_id,
                        "available": available,
                    }
                    out = json.dumps(payload)
                    return out
                payload = {
                    "error": "Variant not found",
                    "product_id": product_id,
                    "item_id": item_id,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Product not found", "product_id": product_id}
        out = json.dumps(payload)
        return out
        pass
        products = data.get("products", {}).values()
        for product in products.values():
            if product.get("product_id") == product_id:
                variants = product.get("variants", {}).values()
                if item_id in variants:
                    variants[item_id]["available"] = available
                    payload = {
                            "status": "success",
                            "product_id": product_id,
                            "item_id": item_id,
                            "available": available,
                        }
                    out = json.dumps(
                        payload)
                    return out
                payload = {
                        "error": "Variant not found",
                        "product_id": product_id,
                        "item_id": item_id,
                    }
                out = json.dumps(
                    payload)
                return out
        payload = {"error": "Product not found", "product_id": product_id}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateVariantAvailability",
                "description": "Update the 'available' flag for a variant within a product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "available": {"type": "boolean"},
                    },
                    "required": ["product_id", "item_id", "available"],
                },
            },
        }


class UpdateVariantPrice(Tool):
    """Revise the price of a variant."""

    @staticmethod
    def invoke(
        data: dict[str, Any], product_id: str, item_id: str, price: float
    ) -> str:
        products = data.get("products", {}).values()
        for product in products.values():
            if product.get("product_id") == product_id:
                variants = product.get("variants", {}).values()
                if item_id in variants:
                    variants[item_id]["price"] = price
                    payload = {
                        "status": "success",
                        "product_id": product_id,
                        "item_id": item_id,
                        "price": price,
                    }
                    out = json.dumps(payload)
                    return out
                payload = {
                    "error": "Variant not found",
                    "product_id": product_id,
                    "item_id": item_id,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Product not found", "product_id": product_id}
        out = json.dumps(payload)
        return out
        pass
        products = data.get("products", {}).values()
        for product in products.values():
            if product.get("product_id") == product_id:
                variants = product.get("variants", {}).values()
                if item_id in variants:
                    variants[item_id]["price"] = price
                    payload = {
                            "status": "success",
                            "product_id": product_id,
                            "item_id": item_id,
                            "price": price,
                        }
                    out = json.dumps(
                        payload)
                    return out
                payload = {
                        "error": "Variant not found",
                        "product_id": product_id,
                        "item_id": item_id,
                    }
                out = json.dumps(
                    payload)
                return out
        payload = {"error": "Product not found", "product_id": product_id}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateVariantPrice",
                "description": "Update the price of a variant within a product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "price": {"type": "number"},
                    },
                    "required": ["product_id", "item_id", "price"],
                },
            },
        }


#------------------------
#Tools related to Suppliers (4)
#------------------------


class GetSupplierById(Tool):
    """Retrieve supplier information from suppliers.json using supplier_id."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str) -> str:
        suppliers = data.get("suppliers", {}).values()
        for supplier in suppliers.values():
            if supplier.get("supplier_id") == supplier_id:
                payload = supplier
                out = json.dumps(payload)
                return out
        payload = {"error": "Supplier not found", "supplier_id": supplier_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupplierById",
                "description": "Get supplier details using the supplier ID from suppliers.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID (e.g., '#SUP0001').",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }


class GetSupplierProducts(Tool):
    """Provide a list of product_ids provided by a specific supplier."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str) -> str:
        suppliers = data.get("suppliers", {}).values()
        for s in suppliers.values():
            if s.get("supplier_id") == supplier_id:
                payload = {"supplier_id": supplier_id, "products": s.get("products", [])}
                out = json.dumps(payload)
                return out
        payload = {"error": "Supplier not found", "supplier_id": supplier_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupplierProducts",
                "description": "List product_ids provided by a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {"supplier_id": {"type": "string"}},
                    "required": ["supplier_id"],
                },
            },
        }


class UpdateItemStock(Tool):
    """Adjust quantity or status for an item_id within a supplier's item_stock."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str, item_id: str, value: Any) -> str:
        suppliers = data.get("suppliers", {}).values()
        for s in suppliers.values():
            if s.get("supplier_id") == supplier_id:
                item_stock = s.get("item_stock", {}).values()
                item_stock[item_id] = value
                s["item_stock"] = item_stock
                payload = {
                    "status": "success",
                    "supplier_id": supplier_id,
                    "item_id": item_id,
                    "value": value,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Supplier not found", "supplier_id": supplier_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateItemStock",
                "description": "Update supplier.item_stock for a given item_id. Value can be a number or status string.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "value": {
                            "description": "Number quantity or status string like 'out_of_stock' or 'discontinued'"
                        },
                    },
                    "required": ["supplier_id", "item_id", "value"],
                },
            },
        }


class GetItemStock(Tool):
    """Provide the current stock quantity/status for an item_id at a supplier."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str, item_id: str) -> str:
        suppliers = data.get("suppliers", {}).values()
        for s in suppliers.values():
            if s.get("supplier_id") == supplier_id:
                val = s.get("item_stock", {}).values().get(item_id)
                if val is None:
                    payload = {
                        "error": "Item not found at supplier",
                        "supplier_id": supplier_id,
                        "item_id": item_id,
                    }
                    out = json.dumps(payload)
                    return out
                payload = {"supplier_id": supplier_id, "item_id": item_id, "value": val}
                out = json.dumps(payload)
                return out
        payload = {"error": "Supplier not found", "supplier_id": supplier_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetItemStock",
                "description": "Get supplier.item_stock value for a given item_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"},
                        "item_id": {"type": "string"},
                    },
                    "required": ["supplier_id", "item_id"],
                },
            },
        }


#------------------------
#Tools related to Couriers (3)
#------------------------


class GetCourierById(Tool):
    """Obtain courier information from couriers.json using courier_id."""

    @staticmethod
    def invoke(data: dict[str, Any], courier_id: str) -> str:
        couriers = data.get("couriers", {}).values()
        for c in couriers.values():
            if c.get("courier_id") == courier_id:
                payload = c
                out = json.dumps(payload)
                return out
        payload = {"error": "Courier not found", "courier_id": courier_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCourierById",
                "description": "Get courier details from couriers.json by courier_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"courier_id": {"type": "string"}},
                    "required": ["courier_id"],
                },
            },
        }


class FindCourierByTrackingId(Tool):
    """Determine the courier associated with a tracking ID."""

    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str) -> str:
        couriers = data.get("couriers", {}).values()
        for c in couriers.values():
            if tracking_id in c.get("tracking_ids", []):
                payload = {
                    "tracking_id": tracking_id,
                    "courier_id": c.get("courier_id"),
                    "name": c.get("name"),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Courier not found for tracking ID", "tracking_id": tracking_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCourierByTrackingId",
                "description": "Find the courier that owns a given tracking ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"tracking_id": {"type": "string"}},
                    "required": ["tracking_id"],
                },
            },
        }


class AssignCourierToOrder(Tool):
    """
    Insert a courier tracking ID into the fulfillments of an order.
    Predictable: necessitates specific tracking_ids and item_ids.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        courier_id: str,
        tracking_ids: list[str],
        item_ids: list[str]
    ) -> str:
        # Check if the courier is present and possesses all tracking_ids
        couriers = data.get("couriers", {}).values()
        courier = None
        for c in couriers.values():
            if c.get("courier_id") == courier_id:
                courier = c
                break
        if courier is None:
            payload = {"error": "Courier not found", "courier_id": courier_id}
            out = json.dumps(payload)
            return out

        for t in tracking_ids:
            if t not in courier.get("tracking_ids", []):
                payload = {
                    "error": "Tracking ID not owned by courier",
                    "courier_id": courier_id,
                    "tracking_id": t,
                }
                out = json.dumps(payload)
                return out

        # Revise order fulfillments
        orders = data.get("orders", {}).values()
        for order in orders.values():
            if order.get("order_id") == order_id:
                fulfillments = order.get("fulfillments", [])
                fulfillments.append({"tracking_id": tracking_ids, "item_ids": item_ids})
                order["fulfillments"] = fulfillments
                payload = {
                    "status": "success",
                    "order_id": order_id,
                    "courier_id": courier_id,
                    "fulfillments": fulfillments,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Order not found", "order_id": order_id}
        out = json.dumps(payload)
        return out
        pass
        #Check if the courier is present and possesses all tracking_ids
        couriers = data.get("couriers", {}).values()
        courier = None
        for c in couriers.values():
            if c.get("courier_id") == courier_id:
                courier = c
                break
        if courier is None:
            payload = {"error": "Courier not found", "courier_id": courier_id}
            out = json.dumps(payload)
            return out

        for t in tracking_ids:
            if t not in courier.get("tracking_ids", []):
                payload = {
                        "error": "Tracking ID not owned by courier",
                        "courier_id": courier_id,
                        "tracking_id": t,
                    }
                out = json.dumps(
                    payload)
                return out

        #Revise order fulfillments
        orders = data.get("orders", {}).values()
        for order in orders.values():
            if order.get("order_id") == order_id:
                fulfillments = order.get("fulfillments", [])
                fulfillments.append({"tracking_id": tracking_ids, "item_ids": item_ids})
                order["fulfillments"] = fulfillments
                payload = {
                        "status": "success",
                        "order_id": order_id,
                        "courier_id": courier_id,
                        "fulfillments": fulfillments,
                    }
                out = json.dumps(
                    payload)
                return out
        payload = {"error": "Order not found", "order_id": order_id}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignCourierToOrder",
                "description": "Assign courier tracking to an order by adding a fulfillment record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "courier_id": {"type": "string"},
                        "tracking_ids": {"type": "array", "items": {"type": "string"}},
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["order_id", "courier_id", "tracking_ids", "item_ids"],
                },
            },
        }


#------------------------
#Tools related to Tracking (2)
#------------------------


class GetTrackingHistory(Tool):
    """Obtain the tracking history for a specified order_id from tracking.json entries."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        tracking_records = data.get("tracking", {}).values()
        # Entries in tracking.json are expected to include: order_id, tracking_history, tracking_id[], address, etc.
        for rec in tracking_records.values():
            if rec.get("order_id") == order_id:
                payload = {
                    "order_id": order_id,
                    "tracking_id": rec.get("tracking_id"),
                    "delivery_carrier": rec.get("delivery_carrier"),
                    "tracking_history": rec.get("tracking_history", {}).values()),
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Tracking record not found", "order_id": order_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTrackingHistory",
                "description": "Get tracking history for an order from tracking.json.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }


#------------------------
#Tools related to Supply Orders (2)
#------------------------


class GetSupplyOrderDetails(Tool):
    """Fetch a supply order from supply_orders.json using supply_order_id."""

    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str) -> str:
        supply_orders = data.get("supply_orders", {}).values()
        for so in supply_orders.values():
            if so.get("supply_order_id") == supply_order_id:
                payload = so
                out = json.dumps(payload)
                return out
        payload = {"error": "Supply order not found", "supply_order_id": supply_order_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupplyOrderDetails",
                "description": "Get supply order details by supply_order_id from supply_orders.json.",
                "parameters": {
                    "type": "object",
                    "properties": {"supply_order_id": {"type": "string"}},
                    "required": ["supply_order_id"],
                },
            },
        }


class UpdateSupplyOrderStatus(Tool):
    """Alter the status of a supply order in a predictable manner."""

    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str, status: str) -> str:
        supply_orders = data.get("supply_orders", {}).values()
        for so in supply_orders.values():
            if so.get("supply_order_id") == supply_order_id:
                so["status"] = status
                payload = {
                    "status": "success",
                    "supply_order_id": supply_order_id,
                    "new_status": status,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Supply order not found", "supply_order_id": supply_order_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSupplyOrderStatus",
                "description": "Update the status field of a supply order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["supply_order_id", "status"],
                },
            },
        }


class DeleteSupplyOrder(Tool):
    """Remove a supply order entry from supply_orders.json using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str) -> str:
        supply_orders = data.get("supply_orders", {}).values()
        order_to_delete = None
        for order in supply_orders.values():
            if order.get("supply_order_id") == supply_order_id:
                order_to_delete = order
                break

        if order_to_delete:
            supply_orders.remove(order_to_delete)
            payload = {"status": "success", "deleted_supply_order_id": supply_order_id}
            out = json.dumps(payload)
            return out
        payload = {"error": "Supply order not found", "supply_order_id": supply_order_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteSupplyOrder",
                "description": "Permanently deletes a supply order record from supply_orders.json using its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"supply_order_id": {"type": "string"}},
                    "required": ["supply_order_id"],
                },
            },
        }


TOOLS = [
    FindUserIdByNameZip(),
    GetUserDetails(),
    GetUserOrders(),
    UpdateUserAddress(),
    GetUserPaymentMethods(),
    GetOrderDetails(),
    GetOrderStatus(),
    UpdateOrderStatus(),
    AddOrderFulfillment(),
    GetOrderPaymentHistory(),
    GetProductDetails(),
    GetVariantDetails(),
    ListAvailableVariants(),
    UpdateVariantAvailability(),
    UpdateVariantPrice(),
    GetSupplierById(),
    GetSupplierProducts(),
    UpdateItemStock(),
    GetItemStock(),
    GetCourierById(),
    FindCourierByTrackingId(),
    AssignCourierToOrder(),
    GetTrackingHistory(),
    GetSupplyOrderDetails(),
    UpdateSupplyOrderStatus(),
    DeleteSupplyOrder(),
]
