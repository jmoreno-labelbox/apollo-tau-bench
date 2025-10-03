import json
import os
from typing import Any

from domains.dto import Tool

#Note: DATA_DIR and load_json are not utilized by the invoke methods anymore,
#which represents the appropriate architecture. They remain here for potential use,
#utilized by other sections of the framework that are not included.
DATA_DIR = os.path.join(os.path.dirname(__file__), "../../data")


def generate_unique_id() -> str:
    pass
    #Deterministic ID according to specifications
    return "fd520c73"


def get_current_timestamp() -> str:
    pass
    #Deterministic timestamp in line with specifications
    return "2025-08-12T12:00:00.000000"


class SearchProductsByCategory(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        category: str,
        available_only: bool = True,
        max_price: float = None,
        min_price: float = None,
        min_stock: int = 1,
        max_stock: int = None
    ) -> str:
        if not category:
            payload = {"error": "category is required"}
            out = json.dumps(payload)
            return out

        # Check the validity of stock range
        if min_stock is not None and max_stock is not None and min_stock > max_stock:
            payload = {"error": "min_stock cannot be greater than max_stock"}
            out = json.dumps(payload)
            return out

        products = data["products"]
        suppliers = data["suppliers"]
        results = []

        # Establish a mapping from item_id to stock level for fast retrieval
        item_stock_map = {}
        for supplier in suppliers:
            for item_id, stock in supplier.get("item_stock", {}).items():
                # Take into account only numeric stock levels
                if isinstance(stock, (int, float)) and stock >= 0:
                    item_stock_map[item_id] = stock

        for product in products:
            if category.lower() in product["name"].lower():
                for variant_id, variant in product["variants"].items():
                    if available_only and not variant.get("available", False):
                        continue
                    if max_price and variant["price"] > max_price:
                        continue
                    if min_price and variant["price"] < min_price:
                        continue

                    # Verify stock levels when stock filters are available
                    item_id = variant.get("item_id", variant_id)
                    stock_level = item_stock_map.get(item_id, 0)

                    if min_stock is not None and stock_level < min_stock:
                        continue
                    if max_stock is not None and stock_level > max_stock:
                        continue

                    results.append(
                        {
                            "product_id": product["product_id"],
                            "name": product["name"],
                            "item_id": variant.get("item_id", variant_id),
                            "price": variant["price"],
                            "stock_level": stock_level,
                            "options": variant["options"],
                            "available": variant["available"],
                        }
                    )

        results.sort(key=lambda x: x["price"])
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchProductsByCategory",
                "description": "Search for products by category name with optional price, availability, and stock filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "Product category to search for",
                        },
                        "available_only": {
                            "type": "boolean",
                            "description": "Only return available products",
                            "default": True,
                        },
                        "max_price": {
                            "type": "number",
                            "description": "Maximum price filter",
                        },
                        "min_price": {
                            "type": "number",
                            "description": "Minimum price filter",
                        },
                        "min_stock": {
                            "type": "integer",
                            "description": "Minimum stock level filter",
                        },
                        "max_stock": {
                            "type": "integer",
                            "description": "Maximum stock level filter",
                        },
                    },
                    "required": ["category"],
                },
            },
        }


class GetOrderDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None) -> str:
        if not order_id:
            payload = {"error": "order_id is required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        order = next((o for o in orders if o["order_id"] == order_id), None)

        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOrderDetails",
                "description": "Retrieve complete details for a specific order by order ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order ID to look up",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }


class GetUserOrders(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, status: str = None, limit: int = 10) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        user_orders = []

        for order in orders:
            if order["user_id"] == user_id:
                if status and order["status"] != status:
                    continue
                user_orders.append(
                    {
                        "order_id": order["order_id"],
                        "status": order["status"],
                        "items": order["items"],
                        "total_amount": sum(item["price"] for item in order["items"]),
                    }
                )

        user_orders.sort(key=lambda x: x["order_id"], reverse=True)
        payload = user_orders[:limit]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUserOrders",
                "description": "Get all orders for a specific user with optional status filtering.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User ID to get orders for",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by order status",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of orders to return",
                            "default": 10,
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }


class UpdateOrderStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, new_status: str = None) -> str:
        if not order_id or not new_status:
            payload = {"error": "order_id and new_status are required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        order = next((o for o in orders if o["order_id"] == order_id), None)

        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out

        old_status = order["status"]
        order["status"] = new_status
        payload = {
                "success": True,
                "order_id": order_id,
                "old_status": old_status,
                "new_status": new_status,
                "updated_at": get_current_timestamp(),
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
                "name": "updateOrderStatus",
                "description": "Update the status of an existing order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order ID to update",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status for the order",
                        },
                    },
                    "required": ["order_id", "new_status"],
                },
            },
        }


class CheckProductAvailability(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_id: str = None, product_id: str = None) -> str:
        if not item_id and not product_id:
            payload = {"error": "Either item_id or product_id is required"}
            out = json.dumps(payload)
            return out

        products = data["products"]

        if item_id:
            for product in products:
                for variant_id, variant in product["variants"].items():
                    if variant["item_id"] == item_id:
                        payload = {
                                "item_id": item_id,
                                "product_name": product["name"],
                                "available": variant["available"],
                                "price": variant["price"],
                                "options": variant["options"],
                            }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
            payload = {"error": "Item not found"}
            out = json.dumps(payload)
            return out

        if product_id:
            product = next((p for p in products if p["product_id"] == product_id), None)
            if not product:
                payload = {"error": "Product not found"}
                out = json.dumps(payload)
                return out

            available_variants = []
            for variant_id, variant in product["variants"].items():
                if variant["available"]:
                    available_variants.append(
                        {
                            "item_id": variant["item_id"],
                            "price": variant["price"],
                            "options": variant["options"],
                        }
                    )
            payload = {
                    "product_id": product_id,
                    "product_name": product["name"],
                    "available_variants": available_variants,
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
                "name": "checkProductAvailability",
                "description": "Check availability of a specific product variant or all variants of a product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {
                            "type": "string",
                            "description": "Specific item ID to check",
                        },
                        "product_id": {
                            "type": "string",
                            "description": "Product ID to check all variants",
                        },
                    },
                },
            },
        }


class GetTrackingInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str = None, order_id: str = None) -> str:
        if not tracking_id and not order_id:
            payload = {"error": "Either tracking_id or order_id is required"}
            out = json.dumps(payload)
            return out

        tracking_data = data["tracking"]

        if tracking_id:
            tracking_info = next(
                (t for t in tracking_data if tracking_id in t["tracking_id"]), None
            )
        else:
            tracking_info = next(
                (t for t in tracking_data if t["order_id"] == order_id), None
            )

        if not tracking_info:
            payload = {"error": "Tracking information not found"}
            out = json.dumps(payload)
            return out
        payload = tracking_info
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTrackingInfo",
                "description": "Get tracking information for an order by tracking ID or order ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {
                            "type": "string",
                            "description": "Tracking ID to look up",
                        },
                        "order_id": {
                            "type": "string",
                            "description": "Order ID to get tracking for",
                        },
                    },
                },
            },
        }


class GetSupplierInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, product_id: str = None) -> str:
        if not supplier_id and not product_id:
            payload = {"error": "Either supplier_id or product_id is required"}
            out = json.dumps(payload)
            return out

        suppliers = data["suppliers"]

        if supplier_id:
            supplier = next(
                (s for s in suppliers if s["supplier_id"] == supplier_id), None
            )
            if not supplier:
                payload = {"error": "Supplier not found"}
                out = json.dumps(payload)
                return out
            payload = supplier
            out = json.dumps(payload, indent=2)
            return out

        if product_id:
            suppliers_for_product = []
            for supplier in suppliers:
                if product_id in supplier["products"]:
                    suppliers_for_product.append(
                        {
                            "supplier_id": supplier["supplier_id"],
                            "name": supplier["name"],
                            "contact_info": supplier["contact_info"],
                        }
                    )
            payload = suppliers_for_product
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getSupplierInfo",
                "description": "Get supplier information by supplier ID or find suppliers for a specific product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID to look up",
                        },
                        "product_id": {
                            "type": "string",
                            "description": "Product ID to find suppliers for",
                        },
                    },
                },
            },
        }


class GetStockLevels(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, item_id: str = None, low_stock_threshold: int = 50) -> str:
        suppliers = data["suppliers"]

        if supplier_id:
            supplier = next(
                (s for s in suppliers if s["supplier_id"] == supplier_id), None
            )
            if not supplier:
                payload = {"error": "Supplier not found"}
                out = json.dumps(payload)
                return out

            if item_id:
                stock_level = supplier["item_stock"].get(item_id, "not_found")
                payload = {
                        "supplier_id": supplier_id,
                        "item_id": item_id,
                        "stock_level": stock_level,
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            low_stock_items = []
            for item, stock in supplier["item_stock"].items():
                if (isinstance(stock, int) and stock < low_stock_threshold) or (
                    isinstance(stock, str) and stock == "out_of_stock"
                ):
                    low_stock_items.append({"item_id": item, "stock_level": stock})
            payload = {
                    "supplier_id": supplier_id,
                    "low_stock_items": low_stock_items,
                    "threshold": low_stock_threshold,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Retrieve low stock information from all suppliers
        all_low_stock = []
        for supplier in suppliers:
            for item, stock in supplier["item_stock"].items():
                if (isinstance(stock, int) and stock < low_stock_threshold) or (
                    isinstance(stock, str) and stock == "out_of_stock"
                ):
                    all_low_stock.append(
                        {
                            "supplier_id": supplier["supplier_id"],
                            "supplier_name": supplier["name"],
                            "item_id": item,
                            "stock_level": stock,
                        }
                    )
        payload = all_low_stock
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getStockLevels",
                "description": "Get stock levels for items, with options to filter by supplier or check low stock items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID to check stock for",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "Specific item ID to check stock for",
                        },
                        "low_stock_threshold": {
                            "type": "integer",
                            "description": "Threshold below which items are considered low stock",
                            "default": 50,
                        },
                    },
                },
            },
        }


class CreateSupplyOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, product_id: str = None, item_id: str = None, quantity: int = None, unit_cost: float = None) -> str:
        if not all([supplier_id, product_id, item_id, quantity, unit_cost]):
            payload = {
                    "error": "supplier_id, product_id, item_id, quantity, and unit_cost are required"
                }
            out = json.dumps(
                payload)
            return out

        supply_orders = data["supply_orders"]

        supply_order_id = f"#SO{generate_unique_id()}-{item_id}"
        total_cost = quantity * unit_cost

        new_order = {
            "supply_order_id": supply_order_id,
            "supplier_id": supplier_id,
            "product_id": product_id,
            "item_id": item_id,
            "quantity": quantity,
            "status": "pending",
            "order_date": get_current_timestamp(),
            "unit_cost": unit_cost,
            "total_cost": total_cost,
        }

        supply_orders.append(new_order)
        payload = {
                "success": True,
                "supply_order_id": supply_order_id,
                "total_cost": total_cost,
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
                "name": "createSupplyOrder",
                "description": "Create a new supply order to restock inventory from a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID to order from",
                        },
                        "product_id": {
                            "type": "string",
                            "description": "Product ID to order",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "Specific item variant ID",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "Quantity to order",
                        },
                        "unit_cost": {"type": "number", "description": "Cost per unit"},
                    },
                    "required": [
                        "supplier_id",
                        "product_id",
                        "item_id",
                        "quantity",
                        "unit_cost",
                    ],
                },
            },
        }


class GetCourierInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], courier_id: str = None, tracking_id: str = None, coverage_area: str = None) -> str:
        couriers = data["couriers"]

        if courier_id:
            courier = next((c for c in couriers if c["courier_id"] == courier_id), None)
            if not courier:
                payload = {"error": "Courier not found"}
                out = json.dumps(payload)
                return out
            payload = courier
            out = json.dumps(payload, indent=2)
            return out

        if tracking_id:
            courier = next(
                (c for c in couriers if tracking_id in c["tracking_ids"]), None
            )
            if not courier:
                payload = {"error": "Courier not found for tracking ID"}
                out = json.dumps(payload)
                return out
            payload = {
                    "courier_id": courier["courier_id"],
                    "name": courier["name"],
                    "contact_info": courier["contact_info"],
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if coverage_area:
            matching_couriers = []
            for courier in couriers:
                if coverage_area in courier["coverage_area"]:
                    matching_couriers.append(
                        {
                            "courier_id": courier["courier_id"],
                            "name": courier["name"],
                            "coverage_area": courier["coverage_area"],
                        }
                    )
            payload = matching_couriers
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "courier_id, tracking_id, or coverage_area is required"}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCourierInfo",
                "description": "Get courier information by courier ID, tracking ID, or coverage area.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "courier_id": {
                            "type": "string",
                            "description": "Courier ID to look up",
                        },
                        "tracking_id": {
                            "type": "string",
                            "description": "Tracking ID to find courier",
                        },
                        "coverage_area": {
                            "type": "string",
                            "description": "Geographic area to find couriers for",
                        },
                    },
                },
            },
        }


class SearchUsers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], email: str = None, name: str = None, user_id: str = None) -> str:
        if not any([email, name, user_id]):
            payload = {"error": "email, name, or user_id is required"}
            out = json.dumps(payload)
            return out

        users = data["users"]

        if user_id:
            user = next((u for u in users if u["user_id"] == user_id), None)
            if not user:
                payload = {"error": "User not found"}
                out = json.dumps(payload)
                return out
            payload = user
            out = json.dumps(payload, indent=2)
            return out

        matching_users = []
        for user in users:
            if email and email.lower() in user["email"].lower():
                matching_users.append(user)
            elif name:
                full_name = (
                    f"{user['name']['first_name']} {user['name']['last_name']}".lower()
                )
                if name.lower() in full_name:
                    matching_users.append(user)
        payload = matching_users
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchUsers",
                "description": "Search for users by email, name, or user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "Email address to search for",
                        },
                        "name": {
                            "type": "string",
                            "description": "Name to search for (partial match)",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "Specific user ID to look up",
                        },
                    },
                },
            },
        }


class ProcessReturn(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, item_ids: list = None, reason: str = None) -> str:
        if not all([order_id, item_ids, reason]):
            payload = {"error": "order_id, item_ids, and reason are required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        suppliers = data["suppliers"]
        products = data["products"]
        order = next((o for o in orders if o["order_id"] == order_id), None)

        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out

        if order["status"] not in ["delivered", "completed", "processed"]:
            payload = {
                    "error": f'Returns not allowed for orders with status: {order["status"]}'
                }
            out = json.dumps(
                payload)
            return out

        return_items = []
        refund_amount = 0.0

        for item_to_return_id in item_ids:
            item_in_order = next(
                (i for i in order["items"] if i["item_id"] == item_to_return_id), None
            )
            if item_in_order:
                return_items.append(item_in_order)
                refund_amount += item_in_order["price"]

                #Replenish inventory
                product_for_item = next(
                    (
                        p
                        for p in products
                        if p["product_id"] == item_in_order["product_id"]
                    ),
                    None,
                )
                if product_for_item:
                    supplier_for_product = next(
                        (
                            s
                            for s in suppliers
                            if s["supplier_id"] == product_for_item["supplier_id"]
                        ),
                        None,
                    )
                    if (
                        supplier_for_product
                        and item_to_return_id in supplier_for_product["item_stock"]
                    ):
                        current_stock = supplier_for_product["item_stock"][
                            item_to_return_id
                        ]
                        if isinstance(current_stock, int):
                            supplier_for_product["item_stock"][item_to_return_id] = (
                                current_stock + 1
                            )  #Presuming the quantity is 1

        if not return_items:
            payload = {"error": "No matching items found in order for return"}
            out = json.dumps(payload)
            return out

        #Record the refund transaction
        refund_transaction = {
            "transaction_type": "refund",
            "amount": -refund_amount,
            "reason": reason,
            "timestamp": get_current_timestamp(),
        }
        if "payment_history" not in order:
            order["payment_history"] = []
        order["payment_history"].append(refund_transaction)

        #Modify order status to indicate return
        order["status"] = (
            "partially_returned"
            if len(order["items"]) > len(return_items)
            else "returned"
        )
        payload = {
                "success": True,
                "order_id": order_id,
                "returned_items_count": len(return_items),
                "refund_amount": refund_amount,
                "new_order_status": order["status"],
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
                "name": "processReturn",
                "description": "Process a return for specific items from an order, logs the refund, and restock inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order ID to process return for",
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of item IDs to return",
                        },
                        "reason": {
                            "type": "string",
                            "description": "Reason for return",
                        },
                    },
                    "required": ["order_id", "item_ids", "reason"],
                },
            },
        }


class UpdateInventory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, item_id: str = None, new_stock: int = None, adjustment: int = None) -> str:
        if not supplier_id or not item_id:
            payload = {"error": "supplier_id and item_id are required"}
            out = json.dumps(payload)
            return out

        if new_stock is None and adjustment is None:
            payload = {"error": "Either new_stock or adjustment is required"}
            out = json.dumps(payload)
            return out

        suppliers = data["suppliers"]
        supplier = next((s for s in suppliers if s["supplier_id"] == supplier_id), None)

        if not supplier:
            payload = {"error": "Supplier not found"}
            out = json.dumps(payload)
            return out

        current_stock = supplier["item_stock"].get(item_id)

        if isinstance(current_stock, str) and current_stock == "discontinued":
            payload = {"error": f"Cannot update stock for item with status: {current_stock}"}
            out = json.dumps(payload)
            return out

        if new_stock is not None:
            supplier["item_stock"][item_id] = new_stock
            updated_stock = new_stock
        else:
            if not isinstance(current_stock, int):
                # Manage situations where stock is non-numeric, such as None or absent
                current_stock = 0
            updated_stock = max(0, current_stock + adjustment)
            supplier["item_stock"][item_id] = updated_stock

        payload = {
            "success": True,
            "supplier_id": supplier_id,
            "item_id": item_id,
            "previous_stock": current_stock,
            "updated_stock": updated_stock,
            "updated_at": get_current_timestamp(),
        }
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateInventory",
                "description": "Update inventory stock levels for a specific item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID managing the inventory",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "Item ID to update stock for",
                        },
                        "new_stock": {
                            "type": "integer",
                            "description": "Set to this exact stock level",
                        },
                        "adjustment": {
                            "type": "integer",
                            "description": "Adjust current stock by this amount (positive or negative)",
                        },
                    },
                    "required": ["supplier_id", "item_id"],
                },
            },
        }


class GetOrdersByStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], status: str, limit: int = 20, start_date: str = None, end_date: str = None) -> str:
        if not status:
            payload = {"error": "status is required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        filtered_orders = []

        for order in orders:
            if order["status"] != status:
                continue

            # Date filtering is complicated without appropriate datetime objects, deferring for now as in the original

            order_summary = {
                "order_id": order["order_id"],
                "user_id": order["user_id"],
                "status": order["status"],
                "item_count": len(order["items"]),
                "total_amount": sum(item["price"] for item in order["items"]),
                "tracking_ids": [
                    f["tracking_id"][0]
                    for f in order.get("fulfillments", [])
                    if f.get("tracking_id")
                ],
            }
            filtered_orders.append(order_summary)

        filtered_orders.sort(key=lambda x: x["order_id"], reverse=True)
        payload = filtered_orders[:limit]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOrdersByStatus",
                "description": "Get all orders with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Order status to filter by",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of orders to return",
                            "default": 20,
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date for filtering (ISO format, not fully implemented)",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date for filtering (ISO format, not fully implemented)",
                        },
                    },
                    "required": ["status"],
                },
            },
        }


class GetPendingSupplyOrders(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None) -> str:
        supply_orders = data["supply_orders"]
        pending_orders = []

        for order in supply_orders:
            if order["status"] == "pending":
                if supplier_id and order["supplier_id"] != supplier_id:
                    continue
                pending_orders.append(order)
        payload = pending_orders
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPendingSupplyOrders",
                "description": "Get all pending supply orders, optionally filtered by supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Optional supplier ID to filter by",
                        }
                    },
                },
            },
        }


class UpdateSupplyOrderStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str = None, new_status: str = None) -> str:
        if not supply_order_id or not new_status:
            payload = {"error": "supply_order_id and new_status are required"}
            out = json.dumps(payload)
            return out

        supply_orders = data["supply_orders"]
        order = next(
            (o for o in supply_orders if o["supply_order_id"] == supply_order_id), None
        )

        if not order:
            payload = {"error": "Supply order not found"}
            out = json.dumps(payload)
            return out

        old_status = order["status"]
        order["status"] = new_status

        # Update inventory if the order is finalized
        if new_status == "completed":
            suppliers = data["suppliers"]
            supplier = next(
                (s for s in suppliers if s["supplier_id"] == order["supplier_id"]), None
            )

            if supplier and order["item_id"] in supplier["item_stock"]:
                current_stock = supplier["item_stock"][order["item_id"]]
                if isinstance(current_stock, int):
                    supplier["item_stock"][order["item_id"]] = (
                        current_stock + order["quantity"]
                    )
        payload = {
            "success": True,
            "supply_order_id": supply_order_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_at": get_current_timestamp(),
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
                "name": "updateSupplyOrderStatus",
                "description": "Update the status of a supply order. Automatically updates inventory when marked as completed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {
                            "type": "string",
                            "description": "Supply order ID to update",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status for the supply order",
                        },
                    },
                    "required": ["supply_order_id", "new_status"],
                },
            },
        }


class GetTopSellingProducts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], limit: int = 10, category: str = None) -> str:
        orders = data["orders"]
        product_sales = {}

        for order in orders:
            if order["status"] in ["delivered", "completed", "processed"]:
                for item in order["items"]:
                    product_id = item["product_id"]
                    product_name = item["name"]

                    if category and category.lower() not in product_name.lower():
                        continue

                    if product_id not in product_sales:
                        product_sales[product_id] = {
                            "product_id": product_id,
                            "name": product_name,
                            "total_sold": 0,
                            "revenue": 0,
                        }

                    product_sales[product_id]["total_sold"] += 1
                    product_sales[product_id]["revenue"] += item["price"]

        sorted_products = sorted(
            product_sales.values(), key=lambda x: x["total_sold"], reverse=True
        )
        payload = sorted_products[:limit]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTopSellingProducts",
                "description": "Get top selling products based on completed orders.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "limit": {
                            "type": "integer",
                            "description": "Number of top products to return",
                            "default": 10,
                        },
                        "category": {
                            "type": "string",
                            "description": "Filter by product category",
                        },
                    },
                },
            },
        }


class UpdateTrackingStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tracking_id: str = None, status: str = None) -> str:
        if not tracking_id or not status:
            payload = {"error": "tracking_id and status are required"}
            out = json.dumps(payload)
            return out

        tracking_data = data["tracking"]
        tracking_info = next(
            (t for t in tracking_data if tracking_id in t["tracking_id"]), None
        )

        if not tracking_info:
            payload = {"error": "Tracking information not found"}
            out = json.dumps(payload)
            return out

        if "tracking_history" not in tracking_info:
            tracking_info["tracking_history"] = {}

        tracking_info["tracking_history"][status] = get_current_timestamp()
        payload = {
                "success": True,
                "tracking_id": tracking_id,
                "new_status": status,
                "updated_at": get_current_timestamp(),
                "tracking_history": tracking_info["tracking_history"],
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
                "name": "updateTrackingStatus",
                "description": "Update the tracking status of a shipment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tracking_id": {
                            "type": "string",
                            "description": "Tracking ID to update",
                        },
                        "status": {
                            "type": "string",
                            "description": "New tracking status (e.g., in_transit, delivered)",
                        },
                    },
                    "required": ["tracking_id", "status"],
                },
            },
        }


class GetRevenueSummary(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], group_by: str = "total") -> str:
        orders = data["orders"]
        revenue_data = {"total_revenue": 0.0, "order_count": 0}

        if group_by == "product":
            revenue_data["by_product"] = {}
        elif group_by == "user":
            revenue_data["by_user"] = {}

        for order in orders:
            if order["status"] in ["delivered", "completed", "processed"]:
                order_total = sum(item["price"] for item in order["items"])
                revenue_data["total_revenue"] += order_total
                revenue_data["order_count"] += 1

                if group_by == "product":
                    for item in order["items"]:
                        product_name = item["name"]
                        if product_name not in revenue_data["by_product"]:
                            revenue_data["by_product"][product_name] = 0.0
                        revenue_data["by_product"][product_name] += item["price"]

                elif group_by == "user":
                    user_id = order["user_id"]
                    if user_id not in revenue_data["by_user"]:
                        revenue_data["by_user"][user_id] = 0.0
                    revenue_data["by_user"][user_id] += order_total

        revenue_data["average_order_value"] = revenue_data["total_revenue"] / max(
            1, revenue_data["order_count"]
        )
        payload = revenue_data
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getRevenueSummary",
                "description": "Get revenue summary with optional grouping by product or user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "group_by": {
                            "type": "string",
                            "description": "Group results by: total, product, or user",
                            "default": "total",
                        }
                    },
                },
            },
        }


class GetUserRevenueSummary(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        revenue_data = {"user_id": user_id, "total_revenue": 0.0, "order_count": 0}

        for order in orders:
            if order["user_id"] == user_id and order["status"] in [
                "delivered",
                "completed",
                "processed",
            ]:
                order_total = sum(item["price"] for item in order["items"])
                revenue_data["total_revenue"] += order_total
                revenue_data["order_count"] += 1

        revenue_data["average_order_value"] = revenue_data["total_revenue"] / max(
            1, revenue_data["order_count"]
        )
        payload = revenue_data
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUserRevenueSummary",
                "description": "Get revenue summary for a specific user including total revenue, order count, and order details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User ID to get revenue summary for",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class ValidateOrderItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_ids: list[str] = None, quantities: list[int] = None) -> str:
        if not item_ids:
            payload = {"error": "item_ids is required"}
            out = json.dumps(payload)
            return out

        if quantities and len(quantities) != len(item_ids):
            payload = {"error": "quantities list must match item_ids length"}
            out = json.dumps(payload)
            return out

        products = data["products"]
        suppliers = data["suppliers"]
        validation_results = []

        for i, item_id in enumerate(item_ids):
            quantity = quantities[i] if quantities else 1
            product_variant, product_name, product = None, None, None

            for p in products:
                if item_id in p["variants"]:
                    product_variant = p["variants"][item_id]
                    product_name = p["name"]
                    product = p
                    break

            if not product_variant:
                validation_results.append(
                    {"item_id": item_id, "valid": False, "error": "Item not found"}
                )
                continue

            if not product_variant["available"]:
                validation_results.append(
                    {"item_id": item_id, "valid": False, "error": "Item not available"}
                )
                continue

            supplier = next(
                (s for s in suppliers if s["supplier_id"] == product["supplier_id"]),
                None,
            )
            stock = supplier["item_stock"].get(item_id) if supplier else None
            sufficient_stock = isinstance(stock, int) and stock >= quantity

            validation_results.append(
                {
                    "item_id": item_id,
                    "product_name": product_name,
                    "price": product_variant["price"],
                    "requested_quantity": quantity,
                    "valid": True,
                    "sufficient_stock": sufficient_stock,
                    "options": product_variant["options"],
                }
            )
        payload = validation_results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validateOrderItems",
                "description": "Validate if items are available for ordering and check stock levels.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of item IDs to validate",
                        },
                        "quantities": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Corresponding quantities for each item",
                        },
                    },
                    "required": ["item_ids"],
                },
            },
        }


class GetDeliveryEstimate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], destination_country: str, delivery_option: str = "standard") -> str:
        if not destination_country:
            payload = {"error": "destination_country is required"}
            out = json.dumps(payload)
            return out

        couriers = data["couriers"]

        available_couriers = [
            c for c in couriers if destination_country in c["coverage_area"]
        ]

        if not available_couriers:
            payload = {"error": f"No delivery available to {destination_country}"}
            out = json.dumps(
                payload)
            return out

        delivery_estimates = {
            "express": {"min_days": 1, "max_days": 3, "cost_multiplier": 2.5},
            "standard": {"min_days": 3, "max_days": 7, "cost_multiplier": 1.0},
            "economy": {"min_days": 7, "max_days": 14, "cost_multiplier": 0.7},
        }

        estimate = delivery_estimates.get(
            delivery_option, delivery_estimates["standard"]
        )
        payload = {
                "destination_country": destination_country,
                "delivery_option": delivery_option,
                "estimated_days": f"{estimate['min_days']}-{estimate['max_days']}",
                "available_couriers": len(available_couriers),
                "cost_multiplier": estimate["cost_multiplier"],
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
                "name": "getDeliveryEstimate",
                "description": "Get delivery time estimates and available couriers for a destination.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_country": {
                            "type": "string",
                            "description": "Country to deliver to",
                        },
                        "delivery_option": {
                            "type": "string",
                            "description": "Delivery speed option",
                            "enum": ["express", "standard", "economy"],
                            "default": "standard",
                        },
                    },
                    "required": ["destination_country"],
                },
            },
        }


class AnalyzeCustomerPurchaseHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        user_orders = [o for o in orders if o["user_id"] == user_id]
        # and o['status'] is among ['delivered', 'completed', 'processed']

        total_spent = 0.0
        categories = {}
        most_expensive_item = None
        max_price = 0.0

        for order in user_orders:
            for item in order["items"]:
                total_spent += item["price"]
                category = item["name"]
                categories[category] = categories.get(category, 0) + 1

                if item["price"] > max_price:
                    max_price = item["price"]
                    most_expensive_item = item

        preferred_category = max(categories, key=categories.get) if categories else None
        payload = {
            "user_id": user_id,
            "total_orders": len(user_orders),
            "total_spent": total_spent,
            "average_order_value": total_spent / max(len(user_orders), 1),
            "preferred_category": preferred_category,
            "most_expensive_item": most_expensive_item,
            "category_breakdown": categories,
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
                "name": "analyzeCustomerPurchaseHistory",
                "description": "Analyze a customer's purchase history to understand buying patterns and preferences.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User ID to analyze",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class CreateRecommendations(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, preferred_category: str = None, max_price: int = 1000) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload)
            return out

        products = data["products"]
        recommendations = []

        for product in products:
            if (
                not preferred_category
                or preferred_category.lower() in product["name"].lower()
            ):
                for variant_id, variant in product["variants"].items():
                    if variant["available"] and variant["price"] <= max_price:
                        recommendations.append(
                            {
                                "product_id": product["product_id"],
                                "name": product["name"],
                                "item_id": variant["item_id"],
                                "price": variant["price"],
                                "options": variant["options"],
                            }
                        )

        recommendations.sort(key=lambda x: x["price"])
        payload = {
                "user_id": user_id,
                "recommendations": recommendations[:5],
                "based_on_category": preferred_category,
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
                "name": "createRecommendations",
                "description": "Create product recommendations for a user based on their preferences.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User ID to create recommendations for",
                        },
                        "preferred_category": {
                            "type": "string",
                            "description": "Preferred product category",
                        },
                        "max_price": {
                            "type": "number",
                            "description": "Maximum price for recommendations",
                            "default": 1000,
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }


class BulkOrderProcessing(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_ids: list[str] = None, new_status: str = None) -> str:
        if not order_ids or not new_status:
            payload = {"error": "order_ids and new_status are required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        updated_orders = []

        for order_id in order_ids:
            order = next((o for o in orders if o["order_id"] == order_id), None)
            if order:
                old_status = order["status"]
                order["status"] = new_status
                updated_orders.append(
                    {
                        "order_id": order_id,
                        "old_status": old_status,
                        "new_status": new_status,
                    }
                )
        payload = {
                "success": True,
                "updated_orders": updated_orders,
                "total_updated": len(updated_orders),
                "updated_at": get_current_timestamp(),
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
                "name": "bulkOrderProcessing",
                "description": "Update the status of multiple orders at once.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of order IDs to update",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status for all orders",
                        },
                    },
                    "required": ["order_ids", "new_status"],
                },
            },
        }


class InventoryAlert(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], threshold: int = 10, category_filter: str = None) -> str:
        suppliers = data["suppliers"]
        products = data["products"]
        critical_items = []

        for supplier in suppliers:
            for item_id, stock in supplier["item_stock"].items():
                if isinstance(stock, int) and stock <= threshold:
                    product_name = "Unknown"
                    for product in products:
                        if item_id in product["variants"]:
                            product_name = product["name"]
                            break

                    if (
                        category_filter
                        and category_filter.lower() not in product_name.lower()
                    ):
                        continue

                    critical_items.append(
                        {
                            "item_id": item_id,
                            "product_name": product_name,
                            "supplier_id": supplier["supplier_id"],
                            "supplier_name": supplier["name"],
                            "current_stock": stock,
                            "threshold": threshold,
                        }
                    )
        payload = {
                "critical_items": critical_items,
                "total_critical": len(critical_items),
                "threshold_used": threshold,
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
                "name": "inventoryAlert",
                "description": "Generate alerts for items that are critically low in stock.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "threshold": {
                            "type": "integer",
                            "description": "Stock threshold for critical alert",
                            "default": 10,
                        },
                        "category_filter": {
                            "type": "string",
                            "description": "Filter alerts by product category",
                        },
                    },
                },
            },
        }


class CreatePromotionalCampaign(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], campaign_name: str = None, target_category: str = None, discount_percentage: int = 10) -> str:
        if not campaign_name or not target_category:
            payload = {"error": "campaign_name and target_category are required"}
            out = json.dumps(
                payload)
            return out

        if "active_campaigns" not in data:
            data["active_campaigns"] = []

        campaign_id = f"CAMP_{generate_unique_id()}"

        new_campaign = {
            "campaign_id": campaign_id,
            "campaign_name": campaign_name,
            "target_category": target_category,
            "discount_percentage": discount_percentage,
            "created_at": get_current_timestamp(),
        }

        data["active_campaigns"].append(new_campaign)
        payload = {
                "success": True,
                "campaign_id": campaign_id,
                "message": f"Campaign '{campaign_name}' created and is now active.",
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
                "name": "createPromotionalCampaign",
                "description": "Create and save a promotional campaign for specific product categories.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_name": {
                            "type": "string",
                            "description": "Name of the promotional campaign",
                        },
                        "target_category": {
                            "type": "string",
                            "description": "Product category to target",
                        },
                        "discount_percentage": {
                            "type": "number",
                            "description": "Discount percentage",
                            "default": 10,
                        },
                    },
                    "required": ["campaign_name", "target_category"],
                },
            },
        }


#--- NEW DETAILED WRITE TOOLS ---


class UpdateUserAddress(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, address: str = None) -> str:
        if not user_id or not address:
            payload = {"error": "user_id and address are required"}
            out = json.dumps(payload)
            return out

        user = next((u for u in data["users"] if u["user_id"] == user_id), None)
        if not user:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out

        user["address"] = address
        payload = {"success": True, "user_id": user_id, "message": "Address updated."}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateUserAddress",
                "description": "Update a user's primary shipping address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user to update.",
                        },
                        "address": {
                            "type": "object",
                            "description": "A complete address object.",
                        },
                    },
                    "required": ["user_id", "address"],
                },
            },
        }


class AddPaymentMethodToUser(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, payment_method: dict = None) -> str:
        if not user_id or not payment_method:
            payload = {"error": "user_id and payment_method are required"}
            out = json.dumps(payload)
            return out

        user = next((u for u in data["users"] if u["user_id"] == user_id), None)
        if not user:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out

        method_id = f"{payment_method.get('source', 'card')}_{generate_unique_id()}"
        payment_method["id"] = method_id
        user["payment_methods"][method_id] = payment_method
        payload = {"success": True, "payment_method_id": method_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addPaymentMethodToUser",
                "description": "Add a new payment method to a user's profile.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        },
                        "payment_method": {
                            "type": "object",
                            "description": "Object containing payment details like source, brand, last_four.",
                        },
                    },
                    "required": ["user_id", "payment_method"],
                },
            },
        }


class CancelOrderItem(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, item_id: str = None) -> str:
        if not order_id or not item_id:
            payload = {"error": "order_id and item_id are required"}
            out = json.dumps(payload)
            return out

        order = next((o for o in data["orders"] if o["order_id"] == order_id), None)
        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out

        if order["status"] not in ["pending", "processing", "processed"]:
            payload = {
                    "error": f"Cannot cancel items from an order with status '{order['status']}'"
                }
            out = json.dumps(
                payload)
            return out

        #Identify the item for cancellation and compute the refund amount
        cancelled_item = next(
            (item for item in order["items"] if item["item_id"] == item_id), None
        )
        if not cancelled_item:
            payload = {"error": f"Item {item_id} not found in order {order_id}"}
            out = json.dumps(
                payload)
            return out

        refund_amount = cancelled_item["price"]

        #Eliminate the item from the order
        len(order["items"])
        order["items"] = [item for item in order["items"] if item["item_id"] != item_id]

        if not order["items"]:
            order["status"] = "cancelled"

        #Verify if gift card payments were made for this order and process the refund
        user = next(
            (u for u in data["users"] if u["user_id"] == order["user_id"]), None
        )
        gift_card_refund_processed = False

        if user and "payment_history" in order:
            #Search for gift card payments within the payment history
            for payment in order["payment_history"]:
                if payment.get("transaction_type") in [
                    "payment",
                    "partial_payment",
                ] and payment.get("payment_method_id", "").startswith("gift_card"):

                    payment_method_id = payment["payment_method_id"]
                    if payment_method_id in user["payment_methods"]:
                        #Reinstate the refund amount to the gift card balance
                        gift_card = user["payment_methods"][payment_method_id]
                        current_balance = gift_card.get("balance", 0)
                        gift_card["balance"] = current_balance + refund_amount
                        gift_card_refund_processed = True

                        #Record the refund in the payment history
                        order["payment_history"].append(
                            {
                                "transaction_type": "refund",
                                "amount": -refund_amount,
                                "payment_method_id": payment_method_id,
                                "reason": f"Item cancellation: {item_id}",
                                "timestamp": get_current_timestamp(),
                            }
                        )
                        break

        #If no gift card payment is detected, still document the refund in the payment history
        if not gift_card_refund_processed:
            if "payment_history" not in order:
                order["payment_history"] = []
            order["payment_history"].append(
                {
                    "transaction_type": "refund",
                    "amount": -refund_amount,
                    "reason": f"Item cancellation: {item_id}",
                    "timestamp": get_current_timestamp(),
                }
            )
        payload = {
                "success": True,
                "order_id": order_id,
                "new_status": order["status"],
                "refund_amount": refund_amount,
                "gift_card_refund_processed": gift_card_refund_processed,
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
                "name": "cancelOrderItem",
                "description": "Remove a specific item from a pending or processing order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to modify.",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "The ID of the item to remove.",
                        },
                    },
                    "required": ["order_id", "item_id"],
                },
            },
        }


class UpdateOrderItemPrice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, item_id: str = None, new_price: float = None) -> str:
        if not all([order_id, item_id, new_price]):
            payload = {"error": "order_id, item_id, and new_price are required"}
            out = json.dumps(
                payload)
            return out

        order = next((o for o in data["orders"] if o["order_id"] == order_id), None)
        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out

        if order["status"] != "pending":
            payload = {"error": "Can only update prices on pending orders."}
            out = json.dumps(payload)
            return out

        item_to_update = next(
            (item for item in order["items"] if item["item_id"] == item_id), None
        )
        if not item_to_update:
            payload = {"error": f"Item {item_id} not in order."}
            out = json.dumps(payload)
            return out

        item_to_update["price"] = new_price
        payload = {
                "success": True,
                "order_id": order_id,
                "item_id": item_id,
                "new_price": new_price,
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
                "name": "updateOrderItemPrice",
                "description": "Manually update the price of an item in a pending order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "new_price": {"type": "number"},
                    },
                    "required": ["order_id", "item_id", "new_price"],
                },
            },
        }


#--- NEW SEPARATED WRITE TOOLS ---


class CreatePendingOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, item_details: list[dict[str, Any]] = None) -> str:
        if not user_id or not item_details:
            payload = {"error": "user_id and item_details are required"}
            out = json.dumps(payload)
            return out

        user = next((u for u in data["users"] if u["user_id"] == user_id), None)
        if not user:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out

        order_items, total_amount = [], 0.0
        order_string = ""
        for detail in item_details:
            item_id, quantity = detail["item_id"], detail.get("quantity", 1)
            found_item = None
            for p in data["products"]:
                if item_id in p["variants"]:
                    variant = p["variants"][item_id]
                    if variant["available"]:
                        price = variant["price"] * quantity
                        found_item = {
                            "name": p["name"],
                            "product_id": p["product_id"],
                            "item_id": item_id,
                            "price": price,
                            "options": variant["options"],
                        }
                        total_amount += price
                        order_string += f"{item_id}"
                    break
            if not found_item:
                payload = {"error": f"Item {item_id} is not available"}
                out = json.dumps(payload)
                return out
            order_items.append(found_item)

        order_id = f"#W{generate_unique_id()}_{order_string}"
        new_order = {
            "order_id": order_id,
            "user_id": user_id,
            "address": None,
            "items": order_items,
            "fulfillments": [],
            "status": "pending",
            "payment_history": [],
            "timestamp": get_current_timestamp(),
        }

        existing_order_index = next(
            (i for i, o in enumerate(data["orders"]) if o["order_id"] == order_id), None
        )
        if existing_order_index is not None:
            data["orders"][existing_order_index] = new_order
        else:
            data["orders"].append(new_order)
        payload = {"success": True, "order_id": order_id, "total_amount": total_amount}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createPendingOrder",
                "description": 'Creates a new order with a "pending" status without payment or shipping.',
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "item_details": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "item_id": {"type": "string"},
                                    "quantity": {"type": "integer"},
                                },
                            },
                        },
                    },
                    "required": ["user_id", "item_details"],
                },
            },
        }


class ApplyPaymentToOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, payment_method_id: str = None, shipping_address: str = None) -> str:
        if not all([order_id, payment_method_id, shipping_address]):
            payload = {
                    "error": "order_id, payment_method_id, and shipping_address are required"
                }
            out = json.dumps(
                payload)
            return out

        order = next((o for o in data["orders"] if o["order_id"] == order_id), None)
        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out
        if order["status"] != "pending":
            payload = {"error": f'Order status is not pending, but {order["status"]}'}
            out = json.dumps(
                payload)
            return out

        user = next(
            (u for u in data["users"] if u["user_id"] == order["user_id"]), None
        )
        if not user or payment_method_id not in user["payment_methods"]:
            payload = {"error": "Invalid payment method for user"}
            out = json.dumps(payload)
            return out

        total_amount = sum(item["price"] for item in order["items"])

        #Process gift card payments independently
        if payment_method_id.startswith("gift_card"):
            #Retrieve details of the gift card payment method
            gift_card = user["payment_methods"][payment_method_id]
            gift_card_balance = gift_card.get("balance", 0)

            if gift_card_balance >= total_amount:
                #Adequate balance - subtract the amount and proceed as usual
                gift_card["balance"] = gift_card_balance - total_amount
                order["payment_history"].append(
                    {
                        "transaction_type": "payment",
                        "amount": total_amount,
                        "payment_method_id": payment_method_id,
                        "timestamp": get_current_timestamp(),
                    }
                )
                order["address"] = shipping_address
                order["status"] = "processing"
                payload = {"success": True, "order_id": order_id, "new_status": "processing"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            else:
                #Insufficient balance - utilize the entire available balance and maintain the order in pending status
                if gift_card_balance > 0:
                    order["payment_history"].append(
                        {
                            "transaction_type": "partial_payment",
                            "amount": gift_card_balance,
                            "payment_method_id": payment_method_id,
                            "timestamp": get_current_timestamp(),
                        }
                    )
                    order["address"] = shipping_address
                    order["status"] = "pending"
                    gift_card["balance"] = 0
                payload = {
                        "success": False,
                        "reason": "Insufficient gift card balance",
                        "order_id": order_id,
                        "status": "pending",
                        "remaining_amount": total_amount - gift_card_balance,
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        else:
            #Standard payment method handling
            order["payment_history"].append(
                {
                    "transaction_type": "payment",
                    "amount": total_amount,
                    "payment_method_id": payment_method_id,
                    "timestamp": get_current_timestamp(),
                }
            )
            order["address"] = shipping_address
            order["status"] = "processing"
            payload = {"success": True, "order_id": order_id, "new_status": "processing"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "applyPaymentToOrder",
                "description": "Applies a payment method and shipping address to a pending order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "payment_method_id": {"type": "string"},
                        "shipping_address": {"type": "object"},
                    },
                    "required": ["order_id", "payment_method_id", "shipping_address"],
                },
            },
        }


class AssignFulfillmentToOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, courier_id: str = None, delivery_options: str = "standard") -> str:
        if not order_id or not courier_id:
            payload = {"error": "order_id and courier_id are required"}
            out = json.dumps(payload)
            return out

        order = next((o for o in data["orders"] if o["order_id"] == order_id), None)
        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out
        if order["status"] != "processing":
            payload = {"error": f'Order status is not processing, but {order["status"]}'}
            out = json.dumps(
                payload)
            return out

        ord_split = order_id.split("_")

        tracking_id = ord_split[1] if len(ord_split) > 1 else f"{generate_unique_id()}"
        item_ids = [item["item_id"] for item in order["items"]]

        fulfillment = {"tracking_id": [tracking_id], "item_ids": item_ids}
        order["fulfillments"].append(fulfillment)

        new_tracking_record = {
            "tracking_id": [tracking_id],
            "item_ids": item_ids,
            "address": order["address"],
            "delivery_carrier": courier_id,
            "delivery_options": delivery_options,
            "order_id": order_id,
            "tracking_history": {"received": get_current_timestamp()},
        }
        data["tracking"].append(new_tracking_record)

        courier = next(
            (c for c in data["couriers"] if c["courier_id"] == courier_id), None
        )
        if courier:
            courier["tracking_ids"].append(tracking_id)

        order["status"] = "processed"
        payload = {
                "success": True,
                "order_id": order_id,
                "tracking_id": tracking_id,
                "new_status": "processed",
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
                "name": "assignFulfillmentToOrder",
                "description": "Assigns a courier and creates tracking for a processed order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "courier_id": {"type": "string"},
                        "delivery_options": {"type": "string"},
                    },
                    "required": ["order_id", "courier_id"],
                },
            },
        }


class AdjustOrderPayment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, payment_method_id: str = None) -> str:
        if not order_id or not payment_method_id:
            payload = {"error": "order_id and payment_method_id are required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        users = data["users"]

        order = next((o for o in orders if o["order_id"] == order_id), None)
        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out

        # Determine the current total of items within the order
        current_total = sum(item["price"] for item in order["items"])

        # Compute the total amount that has been paid so far
        paid_amount = 0.0
        if "payment_history" in order:
            for transaction in order["payment_history"]:
                if (
                    transaction.get("transaction_type") == "payment"
                    or transaction.get("transaction_type") == "partial_payment"
                ):
                    paid_amount += transaction.get("amount", 0.0)
                elif transaction.get("transaction_type") == "refund":
                    paid_amount += transaction.get(
                        "amount", 0.0
                    )  # refund amounts are less than zero
                elif transaction.get("transaction_type") == "charge":
                    paid_amount += transaction.get("amount", 0.0)

        # Determine the difference
        payment_difference = current_total - paid_amount

        # Retrieve the user and verify the payment method
        user = next((u for u in users if u["user_id"] == order["user_id"]), None)
        if not user:
            payload = {"error": "User not found for this order"}
            out = json.dumps(payload)
            return out

        if payment_method_id not in user.get("payment_methods", {}):
            payload = {"error": "Payment method not found for this user"}
            out = json.dumps(payload)
            return out

        # Set up payment_history if it is not already present
        if "payment_history" not in order:
            order["payment_history"] = []

        transaction_type = None
        amount = 0.0
        message = ""

        if (
            abs(payment_difference) < 0.01
        ):  # Practically equal (considering floating point precision)
            message = f"Order total ({current_total:.2f}) matches paid amount ({paid_amount:.2f}). No adjustment needed."
            payload = {
                "success": True,
                "order_id": order_id,
                "current_total": current_total,
                "paid_amount": paid_amount,
                "payment_difference": payment_difference,
                "action": "no_action_needed",
                "message": message,
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        elif payment_difference < 0:  # Amount paid exceeds total, requires a refund
            refund_amount = abs(payment_difference)
            transaction_type = "refund"
            amount = -refund_amount  # Negative indicates a refund
            message = f"Refund of ${refund_amount:.2f} processed to payment method {payment_method_id}"

        else:  # payment_difference is greater than 0, requires additional charge
            charge_amount = payment_difference
            transaction_type = "charge"
            amount = charge_amount  # Positive indicates a need for extra charge
            order["status"] = "processing"
            message = f"Additional charge of ${charge_amount:.2f} processed to payment method {payment_method_id}"

        # Generate the transaction record
        transaction = {
            "transaction_type": transaction_type,
            "amount": amount,
            "payment_method_id": payment_method_id,
            "reason": "Order total adjustment",
            "timestamp": get_current_timestamp(),
        }

        # Include the transaction in the payment history
        order["payment_history"].append(transaction)
        payload = {
            "success": True,
            "order_id": order_id,
            "current_total": current_total,
            "paid_amount": paid_amount,
            "payment_difference": payment_difference,
            "action": transaction_type,
            "transaction_amount": amount,
            "payment_method_id": payment_method_id,
            "message": message,
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
                "name": "adjustOrderPayment",
                "description": "Automatically adjusts payment for an order by comparing current order total with paid amount. Creates refund if overpaid or charges additional amount if underpaid.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "Order ID to adjust payment for",
                        },
                        "payment_method_id": {
                            "type": "string",
                            "description": "Payment method ID to use for refund or additional charge",
                        },
                    },
                    "required": ["order_id", "payment_method_id"],
                },
            },
        }


#Product Create, Read, Update, Delete Tools
class GetProductDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None) -> str:
        if not product_id:
            payload = {"error": "product_id is required"}
            out = json.dumps(payload)
            return out

        products = data["products"]
        product = next((p for p in products if p["product_id"] == product_id), None)

        if not product:
            payload = {"error": f"Product {product_id} not found"}
            out = json.dumps(payload)
            return out
        payload = product
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getProductDetails",
                "description": "Get detailed information about a specific product including all variants.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "Product ID to get details for",
                        }
                    },
                    "required": ["product_id"],
                },
            },
        }


class UpdateProductPrice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None, item_id: str = None, new_price: float = None) -> str:
        if not product_id or not item_id or new_price is None:
            payload = {"error": "product_id, item_id, and new_price are required"}
            out = json.dumps(
                payload)
            return out

        products = data["products"]
        product = next((p for p in products if p["product_id"] == product_id), None)

        if not product:
            payload = {"error": f"Product {product_id} not found"}
            out = json.dumps(payload)
            return out

        if item_id not in product["variants"]:
            payload = {"error": f"Item {item_id} not found in product {product_id}"}
            out = json.dumps(
                payload)
            return out

        old_price = product["variants"][item_id]["price"]
        product["variants"][item_id]["price"] = new_price
        payload = {
                "success": True,
                "product_id": product_id,
                "item_id": item_id,
                "old_price": old_price,
                "new_price": new_price,
                "updated_at": get_current_timestamp(),
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
                "name": "updateProductPrice",
                "description": "Update the price of a specific product variant.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string", "description": "Product ID"},
                        "item_id": {
                            "type": "string",
                            "description": "Variant ID to update price for",
                        },
                        "new_price": {
                            "type": "number",
                            "description": "New price for the variant",
                        },
                    },
                    "required": ["product_id", "item_id", "new_price"],
                },
            },
        }


class ListProductsBySupplier(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None) -> str:
        if not supplier_id:
            payload = {"error": "supplier_id is required"}
            out = json.dumps(payload)
            return out

        products = data["products"]
        supplier_products = [p for p in products if p["supplier_id"] == supplier_id]
        payload = supplier_products
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listProductsBySupplier",
                "description": "Get all products supplied by a specific supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID to get products for",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }


class UpdateSupplierContact(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None, phone: str = None, email: str = None, contact_info: dict = None) -> str:
        if not supplier_id:
            payload = {"error": "supplier_id is required"}
            out = json.dumps(payload)
            return out

        suppliers = data["suppliers"]
        supplier = next((s for s in suppliers if s["supplier_id"] == supplier_id), None)

        if not supplier:
            payload = {"error": f"Supplier {supplier_id} not found"}
            out = json.dumps(payload)
            return out

        if contact_info:
            old_contact = supplier["contact_info"].copy()
            supplier["contact_info"] = contact_info
        else:
            if not phone and not email:
                payload = {"error": "At least one of phone or email is required"}
                out = json.dumps(payload)
                return out
            old_contact = supplier["contact_info"].copy()

            if phone:
                supplier["contact_info"]["phone"] = phone
            if email:
                supplier["contact_info"]["email"] = email
        payload = {
                "success": True,
                "supplier_id": supplier_id,
                "old_contact": old_contact,
                "new_contact": supplier["contact_info"],
                "updated_at": get_current_timestamp(),
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
                "name": "updateSupplierContact",
                "description": "Update contact information for a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID to update",
                        },
                        "phone": {"type": "string", "description": "New phone number"},
                        "email": {"type": "string", "description": "New email address"},
                        "contact_info": {
                            "type": "object",
                            "description": "Complete contact information object",
                            "properties": {
                                "phone": {
                                    "type": "string",
                                    "description": "Phone number",
                                },
                                "email": {
                                    "type": "string",
                                    "description": "Email address",
                                },
                            },
                        },
                    },
                    "required": ["supplier_id"],
                },
            },
        }


class ListAllSuppliers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        suppliers = data["suppliers"]

        # Provide basic supplier information without extensive inventory details
        supplier_list = []
        for supplier in suppliers:
            supplier_list.append(
                {
                    "supplier_id": supplier["supplier_id"],
                    "name": supplier["name"],
                    "contact_info": supplier["contact_info"],
                    "total_products": len(supplier["products"]),
                }
            )
        payload = supplier_list
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listAllSuppliers",
                "description": "Get a list of all suppliers with basic information.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class GetProductByItemId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], item_id: str = None) -> str:
        if not item_id:
            payload = {"error": "item_id is required"}
            out = json.dumps(payload)
            return out

        products = data["products"]

        # Examine all products to identify which one includes this item_id
        for product in products:
            if item_id in product["variants"]:
                product["variants"][item_id]
                payload = {
                    "product_id": product["product_id"],
                    "product_name": product["name"],
                    "supplier_id": product["supplier_id"],
                    "item_id": item_id,
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": f"Item ID {item_id} not found in any product"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getProductByItemId",
                "description": "Find the product ID and details given a specific item ID (variant ID).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {
                            "type": "string",
                            "description": "Item ID (variant ID) to search for",
                        }
                    },
                    "required": ["item_id"],
                },
            },
        }


#Supply Order Create, Read, Update, Delete Tools
class GetSupplyOrderDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str = None) -> str:
        if not supply_order_id:
            payload = {"error": "supply_order_id is required"}
            out = json.dumps(payload)
            return out

        supply_orders = data["supply_orders"]
        order = next(
            (o for o in supply_orders if o["supply_order_id"] == supply_order_id), None
        )

        if not order:
            payload = {"error": f"Supply order {supply_order_id} not found"}
            out = json.dumps(payload)
            return out
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getSupplyOrderDetails",
                "description": "Get detailed information about a specific supply order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {
                            "type": "string",
                            "description": "Supply order ID to get details for",
                        }
                    },
                    "required": ["supply_order_id"],
                },
            },
        }


class ListSupplyOrdersByStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], status: str, supplier_id: str = None, limit: int = 20) -> str:
        if not status:
            payload = {"error": "status is required"}
            out = json.dumps(payload)
            return out

        supply_orders = data["supply_orders"]
        filtered_orders = []

        for order in supply_orders:
            if order["status"] == status:
                if supplier_id and order["supplier_id"] != supplier_id:
                    continue
                filtered_orders.append(order)

        # Arrange by order date, with the latest first
        filtered_orders.sort(key=lambda x: x["order_date"], reverse=True)
        payload = filtered_orders[:limit]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listSupplyOrdersByStatus",
                "description": "Get supply orders filtered by status, optionally by supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Status to filter by (pending, fulfilled, cancelled)",
                        },
                        "supplier_id": {
                            "type": "string",
                            "description": "Optional supplier ID to filter by",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of orders to return",
                            "default": 20,
                        },
                    },
                    "required": ["status"],
                },
            },
        }


class UpdateSupplyOrderQuantity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supply_order_id: str = None, new_quantity: int = None) -> str:
        if not supply_order_id or new_quantity is None:
            payload = {"error": "supply_order_id and new_quantity are required"}
            out = json.dumps(
                payload)
            return out

        if new_quantity < 0:
            payload = {"error": "Quantity cannot be negative"}
            out = json.dumps(payload)
            return out

        supply_orders = data["supply_orders"]
        order = next(
            (o for o in supply_orders if o["supply_order_id"] == supply_order_id), None
        )

        if not order:
            payload = {"error": f"Supply order {supply_order_id} not found"}
            out = json.dumps(payload)
            return out

        if order["status"] not in ["pending"]:
            payload = {
                    "error": f'Cannot update quantity for order with status: {order["status"]}'
                }
            out = json.dumps(
                payload)
            return out

        old_quantity = order["quantity"]
        old_total_cost = order["total_cost"]

        order["quantity"] = new_quantity
        order["total_cost"] = new_quantity * order["unit_cost"]
        payload = {
                "success": True,
                "supply_order_id": supply_order_id,
                "old_quantity": old_quantity,
                "new_quantity": new_quantity,
                "old_total_cost": old_total_cost,
                "new_total_cost": order["total_cost"],
                "updated_at": get_current_timestamp(),
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
                "name": "updateSupplyOrderQuantity",
                "description": "Update the quantity of a pending supply order and recalculate total cost.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supply_order_id": {
                            "type": "string",
                            "description": "Supply order ID to update",
                        },
                        "new_quantity": {
                            "type": "integer",
                            "description": "New quantity for the order",
                        },
                    },
                    "required": ["supply_order_id", "new_quantity"],
                },
            },
        }


#Inter-entity query tools (10% of the tools)
class GetProductSupplierSummary(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None) -> str:
        if not product_id:
            payload = {"error": "product_id is required"}
            out = json.dumps(payload)
            return out

        products = data["products"]
        suppliers = data["suppliers"]
        supply_orders = data["supply_orders"]

        product = next((p for p in products if p["product_id"] == product_id), None)
        if not product:
            payload = {"error": f"Product {product_id} not found"}
            out = json.dumps(payload)
            return out

        supplier = next(
            (s for s in suppliers if s["supplier_id"] == product["supplier_id"]), None
        )

        # Retrieve supply orders associated with this product
        product_supply_orders = [
            o for o in supply_orders if o["product_id"] == product_id
        ]

        # Compute the stock summary
        stock_summary = {}
        if supplier:
            for variant_id in product["variants"].keys():
                stock_level = supplier["item_stock"].get(variant_id, "unknown")
                stock_summary[variant_id] = stock_level
        payload = {
            "product": product,
            "supplier": supplier,
            "stock_summary": stock_summary,
            "total_supply_orders": len(product_supply_orders),
            "recent_supply_orders": product_supply_orders[-5:],  # Most recent 5 orders
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
                "name": "getProductSupplierSummary",
                "description": "Get comprehensive information about a product, its supplier, stock levels, and recent supply orders.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "Product ID to get summary for",
                        }
                    },
                    "required": ["product_id"],
                },
            },
        }


class GetSupplierOrderHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str, limit: int = 10) -> str:
        if not supplier_id:
            payload = {"error": "supplier_id is required"}
            out = json.dumps(payload)
            return out

        suppliers = data["suppliers"]
        supply_orders = data["supply_orders"]
        products = data["products"]

        supplier = next((s for s in suppliers if s["supplier_id"] == supplier_id), None)
        if not supplier:
            payload = {"error": f"Supplier {supplier_id} not found"}
            out = json.dumps(payload)
            return out

        # Retrieve all orders related to this supplier
        supplier_orders = [o for o in supply_orders if o["supplier_id"] == supplier_id]
        supplier_orders.sort(key=lambda x: x["order_date"], reverse=True)

        # Enhance orders by adding product names
        enriched_orders = []
        for order in supplier_orders[:limit]:
            product = next(
                (p for p in products if p["product_id"] == order["product_id"]), None
            )
            enriched_order = order.copy()
            enriched_order["product_name"] = (
                product["name"] if product else "Unknown Product"
            )
            enriched_orders.append(enriched_order)

        # Compute summary statistics
        total_orders = len(supplier_orders)
        total_value = sum(o["total_cost"] for o in supplier_orders)
        pending_orders = len([o for o in supplier_orders if o["status"] == "pending"])
        payload = {
            "supplier": {
                "supplier_id": supplier["supplier_id"],
                "name": supplier["name"],
                "contact_info": supplier["contact_info"],
            },
            "order_summary": {
                "total_orders": total_orders,
                "total_value": total_value,
                "pending_orders": pending_orders,
            },
            "recent_orders": enriched_orders,
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
                "name": "getSupplierOrderHistory",
                "description": "Get order history and summary statistics for a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID to get order history for",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of recent orders to return",
                            "default": 10,
                        },
                    },
                    "required": ["supplier_id"],
                },
            },
        }


TOOLS = [
    #Reading/Computational Tools
    SearchProductsByCategory(),
    GetOrderDetails(),
    GetUserOrders(),
    CheckProductAvailability(),
    GetTrackingInfo(),
    GetSupplierInfo(),
    GetStockLevels(),
    GetOrdersByStatus(),
    GetPendingSupplyOrders(),
    GetTopSellingProducts(),
    GetRevenueSummary(),
    GetUserRevenueSummary(),
    ValidateOrderItems(),
    GetDeliveryEstimate(),
    AnalyzeCustomerPurchaseHistory(),
    CreateRecommendations(),
    InventoryAlert(),
    SearchUsers(),
    GetCourierInfo(),
    GetProductDetails(),
    ListProductsBySupplier(),
    GetProductByItemId(),
    ListAllSuppliers(),
    GetSupplyOrderDetails(),
    ListSupplyOrdersByStatus(),
    GetProductSupplierSummary(),
    GetSupplierOrderHistory(),
    #Writing Tools
    UpdateOrderStatus(),
    CreateSupplyOrder(),
    ProcessReturn(),
    UpdateInventory(),
    UpdateSupplyOrderStatus(),
    UpdateTrackingStatus(),
    BulkOrderProcessing(),
    CreatePromotionalCampaign(),
    UpdateUserAddress(),
    AddPaymentMethodToUser(),
    CancelOrderItem(),
    UpdateOrderItemPrice(),  #Recent
    CreatePendingOrder(),  #Recent (separated)
    ApplyPaymentToOrder(),  #Recent (separated)
    AssignFulfillmentToOrder(),  #Recent (separated)
    AdjustOrderPayment(),  #Recent - manages payment modifications
    #Recent Product/Supplier/Supply Order Writing Tools
    UpdateProductPrice(),
    UpdateSupplierContact(),
    UpdateSupplyOrderQuantity(),
]
