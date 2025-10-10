import json
from datetime import datetime
from typing import Any, Dict, List

from domains.dto import Tool

class FindUserIdByNameZip(Tool):
    """Find a user_id by first name, last name, and ZIP code."""

    @staticmethod
    def invoke(data: Dict[str, Any], first_name: str, last_name: str, zip: str) -> str:
        users = data.get("users", [])
        for user in users:
            if (user.get("name", {}).get("first_name") == first_name and
                user.get("name", {}).get("last_name") == last_name and
                user.get("address", {}).get("zip") == zip):
                return json.dumps({"user_id": user.get("user_id")})
        return json.dumps({"error": "User not found", "first_name": first_name, "last_name": last_name, "zip": zip})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_user_id_by_name_zip",
                "description": "Find user_id from users.json by first name, last name, and ZIP code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                        "zip": {"type": "string"}
                    },
                    "required": ["first_name", "last_name", "zip"]
                }
            }
        }


class GetUserDetails(Tool):
    """Retrieve full user details from users.json by user_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        users = data.get("users", [])
        for user in users:
            if user.get("user_id") == user_id:
                return json.dumps(user)
        return json.dumps({"error": "User not found", "user_id": user_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_details",
                "description": "Get user details from users.json by user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"}
                    },
                    "required": ["user_id"]
                }
            }
        }


class GetUserOrders(Tool):
    """Get list of order IDs for a given user_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        users = data.get("users", [])
        for user in users:
            if user.get("user_id") == user_id:
                return json.dumps({"orders": user.get("orders", [])})
        return json.dumps({"error": "User not found", "user_id": user_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_orders",
                "description": "Get order IDs linked to a given user_id from users.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"}
                    },
                    "required": ["user_id"]
                }
            }
        }


class UpdateUserAddress(Tool):
    """Update user's address in users.json by user_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, address: Dict[str, Any]) -> str:
        users = data.get("users", [])
        for user in users:
            if user.get("user_id") == user_id:
                user["address"] = address
                return json.dumps({"status": "success", "user_id": user_id, "address": address})
        return json.dumps({"error": "User not found", "user_id": user_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_address",
                "description": "Update a user's address in users.json by user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "address": {"type": "object", "description": "Full address object with address1, address2, city, country, state, zip"}
                    },
                    "required": ["user_id", "address"]
                }
            }
        }


class GetUserPaymentMethods(Tool):
    """List all payment methods for a given user_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        users = data.get("users", [])
        for user in users:
            if user.get("user_id") == user_id:
                return json.dumps({"payment_methods": user.get("payment_methods", {})})
        return json.dumps({"error": "User not found", "user_id": user_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_payment_methods",
                "description": "Retrieve payment methods for a given user_id from users.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"}
                    },
                    "required": ["user_id"]
                }
            }
        }

# ------------------------
# Order-related Tools (5)
# ------------------------

class GetOrderDetails(Tool):
    """Fetch full order details from orders.json by order_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        orders = data.get("orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                return json.dumps(order)
        return json.dumps({"error": "Order not found", "order_id": order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_details",
                "description": "Get order details from orders.json by order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"}
                    },
                    "required": ["order_id"]
                }
            }
        }


class GetOrderStatus(Tool):
    """Return only the status of an order."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        orders = data.get("orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                return json.dumps({"order_id": order_id, "status": order.get("status")})
        return json.dumps({"error": "Order not found", "order_id": order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_status",
                "description": "Return the order status by order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"}
                    },
                    "required": ["order_id"]
                }
            }
        }


class UpdateOrderStatus(Tool):
    """Change the status of an order deterministically."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, status: str) -> str:
        orders = data.get("orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                order["status"] = status
                return json.dumps({"status": "success", "order_id": order_id, "new_status": status})
        return json.dumps({"error": "Order not found", "order_id": order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_order_status",
                "description": "Update order status (e.g., pending, delivered, cancelled) by order_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "status": {"type": "string"}
                    },
                    "required": ["order_id", "status"]
                }
            }
        }


class AddOrderFulfillment(Tool):
    """Add a fulfillment record with tracking IDs for specific item IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, tracking_ids: List[str], item_ids: List[str]) -> str:
        orders = data.get("orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                fulfillments = order.get("fulfillments", [])
                fulfillments.append({
                    "tracking_id": tracking_ids,
                    "item_ids": item_ids
                })
                order["fulfillments"] = fulfillments
                return json.dumps({"status": "success", "order_id": order_id, "fulfillments": order["fulfillments"]})
        return json.dumps({"error": "Order not found", "order_id": order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_order_fulfillment",
                "description": "Add fulfillment with tracking IDs and covered item IDs to an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "tracking_ids": {"type": "array", "items": {"type": "string"}},
                        "item_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["order_id", "tracking_ids", "item_ids"]
                }
            }
        }


class GetOrderPaymentHistory(Tool):
    """Return payment transactions for an order."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        orders = data.get("orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                return json.dumps({"order_id": order_id, "payment_history": order.get("payment_history", [])})
        return json.dumps({"error": "Order not found", "order_id": order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_order_payment_history",
                "description": "Get the payment_history array for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"}
                    },
                    "required": ["order_id"]
                }
            }
        }

# ------------------------
# Product-related Tools (5)
# ------------------------

class GetProductDetails(Tool):
    """Retrieve product details from products.json by product_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], product_id: str) -> str:
        products = data.get("products", [])
        for product in products:
            if product.get("product_id") == product_id:
                return json.dumps(product)
        return json.dumps({"error": "Product not found", "product_id": product_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_details",
                "description": "Get product details by product_id from products.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"}
                    },
                    "required": ["product_id"]
                }
            }
        }


class GetVariantDetails(Tool):
    """Retrieve a variant (by item_id) from products.json."""

    @staticmethod
    def invoke(data: Dict[str, Any], item_id: str) -> str:
        products = data.get("products", [])
        for product in products:
            variants = product.get("variants", {})
            var = variants.get(item_id)
            if var:
                result = {"product_id": product.get("product_id"), "variant": var}
                return json.dumps(result)
        return json.dumps({"error": "Variant not found", "item_id": item_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_variant_details",
                "description": "Get variant details by item_id from products.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"}
                    },
                    "required": ["item_id"]
                }
            }
        }


class ListAvailableVariants(Tool):
    """List available variants for a product."""

    @staticmethod
    def invoke(data: Dict[str, Any], product_id: str) -> str:
        products = data.get("products", [])
        for product in products:
            if product.get("product_id") == product_id:
                variants = product.get("variants", {})
                available = [v for v in variants.values() if v.get("available") is True]
                return json.dumps({"product_id": product_id, "available_variants": available})
        return json.dumps({"error": "Product not found", "product_id": product_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_available_variants",
                "description": "List variants with available=true for a given product_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"}
                    },
                    "required": ["product_id"]
                }
            }
        }


class UpdateVariantAvailability(Tool):
    """Change 'available' status for a variant."""

    @staticmethod
    def invoke(data: Dict[str, Any], product_id: str, item_id: str, available: bool) -> str:
        products = data.get("products", [])
        for product in products:
            if product.get("product_id") == product_id:
                variants = product.get("variants", {})
                if item_id in variants:
                    variants[item_id]["available"] = available
                    return json.dumps({"status": "success", "product_id": product_id, "item_id": item_id, "available": available})
                return json.dumps({"error": "Variant not found", "product_id": product_id, "item_id": item_id})
        return json.dumps({"error": "Product not found", "product_id": product_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_variant_availability",
                "description": "Update the 'available' flag for a variant within a product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "available": {"type": "boolean"}
                    },
                    "required": ["product_id", "item_id", "available"]
                }
            }
        }


class UpdateVariantPrice(Tool):
    """Update price for a variant."""

    @staticmethod
    def invoke(data: Dict[str, Any], product_id: str, item_id: str, price: float) -> str:
        products = data.get("products", [])
        for product in products:
            if product.get("product_id") == product_id:
                variants = product.get("variants", {})
                if item_id in variants:
                    variants[item_id]["price"] = price
                    return json.dumps({"status": "success", "product_id": product_id, "item_id": item_id, "price": price})
                return json.dumps({"error": "Variant not found", "product_id": product_id, "item_id": item_id})
        return json.dumps({"error": "Product not found", "product_id": product_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_variant_price",
                "description": "Update the price of a variant within a product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "price": {"type": "number"}
                    },
                    "required": ["product_id", "item_id", "price"]
                }
            }
        }

# ------------------------
# Supplier-related Tools (4)
# ------------------------

class GetSupplierById(Tool):
    """Get supplier details from suppliers.json by supplier_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str) -> str:
        suppliers = data.get("suppliers", [])
        for supplier in suppliers:
            if supplier.get("supplier_id") == supplier_id:
                return json.dumps(supplier)
        return json.dumps({"error": "Supplier not found", "supplier_id": supplier_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_supplier_by_id",
                "description": "Get supplier details using the supplier ID from suppliers.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "Supplier ID (e.g., '#SUP0001')."}
                    },
                    "required": ["supplier_id"]
                }
            }
        }


class GetSupplierProducts(Tool):
    """Return list of product_ids supplied by a given supplier."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str) -> str:
        suppliers = data.get("suppliers", [])
        for s in suppliers:
            if s.get("supplier_id") == supplier_id:
                return json.dumps({"supplier_id": supplier_id, "products": s.get("products", [])})
        return json.dumps({"error": "Supplier not found", "supplier_id": supplier_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_supplier_products",
                "description": "List product_ids provided by a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"}
                    },
                    "required": ["supplier_id"]
                }
            }
        }


class UpdateItemStock(Tool):
    """Set quantity or status for an item_id in a supplier's item_stock."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str, item_id: str, value: Any) -> str:
        suppliers = data.get("suppliers", [])
        for s in suppliers:
            if s.get("supplier_id") == supplier_id:
                item_stock = s.get("item_stock", {})
                item_stock[item_id] = value
                s["item_stock"] = item_stock
                return json.dumps({"status": "success", "supplier_id": supplier_id, "item_id": item_id, "value": value})
        return json.dumps({"error": "Supplier not found", "supplier_id": supplier_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_item_stock",
                "description": "Update supplier.item_stock for a given item_id. Value can be a number or status string.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "value": {"description": "Number quantity or status string like 'out_of_stock' or 'discontinued'"}
                    },
                    "required": ["supplier_id", "item_id", "value"]
                }
            }
        }


class GetItemStock(Tool):
    """Return current stock quantity/status for an item_id at a supplier."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str, item_id: str) -> str:
        suppliers = data.get("suppliers", [])
        for s in suppliers:
            if s.get("supplier_id") == supplier_id:
                val = s.get("item_stock", {}).get(item_id)
                if val is None:
                    return json.dumps({"error": "Item not found at supplier", "supplier_id": supplier_id, "item_id": item_id})
                return json.dumps({"supplier_id": supplier_id, "item_id": item_id, "value": val})
        return json.dumps({"error": "Supplier not found", "supplier_id": supplier_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_item_stock",
                "description": "Get supplier.item_stock value for a given item_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"},
                        "item_id": {"type": "string"}
                    },
                    "required": ["supplier_id", "item_id"]
                }
            }
        }

# ------------------------
# Courier-related Tools (3)
# ------------------------

class GetCourierById(Tool):
    """Retrieve courier details from couriers.json by courier_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], courier_id: str) -> str:
        couriers = data.get("couriers", [])
        for c in couriers:
            if c.get("courier_id") == courier_id:
                return json.dumps(c)
        return json.dumps({"error": "Courier not found", "courier_id": courier_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_courier_by_id",
                "description": "Get courier details from couriers.json by courier_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "courier_id": {"type": "string"}
                    },
                    "required": ["courier_id"]
                }
            }
        }


class FindCourierByTrackingId(Tool):
    """Identify courier from a tracking ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], tracking_id: str) -> str:
        couriers = data.get("couriers", [])
        for c in couriers:
            if tracking_id in c.get("tracking_ids", []):
                return json.dumps({"tracking_id": tracking_id, "courier_id": c.get("courier_id"), "name": c.get("name")})
        return json.dumps({"error": "Courier not found for tracking ID", "tracking_id": tracking_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_courier_by_tracking_id",
                "description": "Find the courier that owns a given tracking ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {"type": "string"}
                    },
                    "required": ["tracking_id"]
                }
            }
        }


class AssignCourierToOrder(Tool):
    """
    Add a courier tracking ID into an order's fulfillments.
    Deterministic: requires explicit tracking_ids and item_ids.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, courier_id: str, tracking_ids: List[str], item_ids: List[str]) -> str:
        # Verify courier exists and owns all tracking_ids
        couriers = data.get("couriers", [])
        courier = None
        for c in couriers:
            if c.get("courier_id") == courier_id:
                courier = c
                break
        if courier is None:
            return json.dumps({"error": "Courier not found", "courier_id": courier_id})

        for t in tracking_ids:
            if t not in courier.get("tracking_ids", []):
                return json.dumps({"error": "Tracking ID not owned by courier", "courier_id": courier_id, "tracking_id": t})

        # Update order fulfillments
        orders = data.get("orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                fulfillments = order.get("fulfillments", [])
                fulfillments.append({
                    "tracking_id": tracking_ids,
                    "item_ids": item_ids
                })
                order["fulfillments"] = fulfillments
                return json.dumps({
                    "status": "success",
                    "order_id": order_id,
                    "courier_id": courier_id,
                    "fulfillments": fulfillments
                })

        return json.dumps({"error": "Order not found", "order_id": order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_courier_to_order",
                "description": "Assign courier tracking to an order by adding a fulfillment record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "courier_id": {"type": "string"},
                        "tracking_ids": {"type": "array", "items": {"type": "string"}},
                        "item_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["order_id", "courier_id", "tracking_ids", "item_ids"]
                }
            }
        }

# ------------------------
# Tracking-related Tools (2)
# ------------------------

class GetTrackingHistory(Tool):
    """Retrieve tracking history for a given order_id from tracking.json records."""

    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str) -> str:
        tracking_records = data.get("tracking", [])
        # tracking.json entries are assumed to have: order_id, tracking_history, tracking_id[], address, etc.
        for rec in tracking_records:
            if rec.get("order_id") == order_id:
                return json.dumps({
                    "order_id": order_id,
                    "tracking_id": rec.get("tracking_id"),
                    "delivery_carrier": rec.get("delivery_carrier"),
                    "tracking_history": rec.get("tracking_history", {})
                })
        return json.dumps({"error": "Tracking record not found", "order_id": order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_tracking_history",
                "description": "Get tracking history for an order from tracking.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"}
                    },
                    "required": ["order_id"]
                }
            }
        }

# ------------------------
# Supply Order-related Tools (2)
# ------------------------

class GetSupplyOrderDetails(Tool):
    """Retrieve a supply order from supply_orders.json by supply_order_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], supply_order_id: str) -> str:
        supply_orders = data.get("supply_orders", [])
        for so in supply_orders:
            if so.get("supply_order_id") == supply_order_id:
                return json.dumps(so)
        return json.dumps({"error": "Supply order not found", "supply_order_id": supply_order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_supply_order_details",
                "description": "Get supply order details by supply_order_id from supply_orders.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"}
                    },
                    "required": ["supply_order_id"]
                }
            }
        }


class UpdateSupplyOrderStatus(Tool):
    """Change status of a supply order deterministically."""

    @staticmethod
    def invoke(data: Dict[str, Any], supply_order_id: str, status: str) -> str:
        supply_orders = data.get("supply_orders", [])
        for so in supply_orders:
            if so.get("supply_order_id") == supply_order_id:
                so["status"] = status
                return json.dumps({"status": "success", "supply_order_id": supply_order_id, "new_status": status})
        return json.dumps({"error": "Supply order not found", "supply_order_id": supply_order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_supply_order_status",
                "description": "Update the status field of a supply order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"},
                        "status": {"type": "string"}
                    },
                    "required": ["supply_order_id", "status"]
                }
            }
        }

class DeleteSupplyOrder(Tool):
    """Deletes a supply order record from supply_orders.json by its ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], supply_order_id: str) -> str:
        supply_orders = data.get("supply_orders", [])
        order_to_delete = None
        for order in supply_orders:
            if order.get("supply_order_id") == supply_order_id:
                order_to_delete = order
                break

        if order_to_delete:
            supply_orders.remove(order_to_delete)
            return json.dumps({"status": "success", "deleted_supply_order_id": supply_order_id})

        return json.dumps({"error": "Supply order not found", "supply_order_id": supply_order_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_supply_order",
                "description": "Permanently deletes a supply order record from supply_orders.json using its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {"type": "string"}
                    },
                    "required": ["supply_order_id"]
                }
            }
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
    DeleteSupplyOrder()
]
