from domains.dto import Tool
from typing import Any, Dict, List
import json

# def _find_row_by_value(db, field, value):
#     # Returns the first row in the database where the specified field matches the value.
#     for row in db:
#         if row.get(field) == value:
#             return row
#     return None

# Returns True if any row matches the filter conditions.
# Filters can be a combination of lists (OR condition) and/or a dictionarys (AND condition).
def _match(rows, filters):
    # Make the row values a list if not for uniform handling
    if not isinstance(rows, list):
        rows = [rows]

    if isinstance(filters, list):
        # OR condition for lists; return true if any match
        return any(_match(rows, single_filter) for single_filter in filters)

    elif isinstance(filters, dict):
        for filter_key, filter_value in filters.items():
            # AND condition for dictionaries; any filter can return false
            # Only if none return false does it pass and return true
            if not any(_match(row.get(filter_key), filter_value) for row in rows):
                return False

    else:
        if filters not in rows:
            return False
    return True

# Updates valued in a database row based on the update parameters.
# If the value is a list, and the update value is not a list, it will append the update value to the list.
# Otherwise, it will replace the value.
def _apply_update(row, update_params):
    for key, value in update_params.items():
        if isinstance(value, dict) and isinstance(row.get(key), dict):
            _apply_update(row[key], value)
        elif isinstance(row.get(key), list) and not isinstance(value, list):
                row[key].append(value)
        else:
            row[key] = value
    return row


def _apply_delete(db, delete_params):
    # If db is a dictionary, it will return None if the delete_params match the row, or the row otherwise (which may be modified at a lower level)

    # If db is a list, we need to iterate through each row
    if isinstance(db, list):
        # If delete_params is a dictionary, we go a step deeper
        if isinstance(delete_params, dict):
            new_db = []
            for row in db:
                new_row = _apply_delete(row, delete_params)
                if new_row is not None:
                    new_db.append(new_row)
            return new_db
        elif isinstance(delete_params, list):
            # If delete_params is a list, we remove each item from the db
            for item in delete_params:
                db.remove(item)
        else:
            # If delete_params is a single value, we remove it from the db
            if delete_params in db:
                db.remove(delete_params)
    elif isinstance(db, dict):
        if isinstance(delete_params, dict):
            # If delete_params is a dictionary, we go a step deeper
            for key, value in delete_params.items():
                if key in db.keys():
                    if db[key] == value:
                        return None  # Will remove the whole row from the level above
                    else:
                        new_row = _apply_delete(db[key], value)
                        if new_row is None:
                            return None
                        else:
                            db[key] = new_row
    return db

# def _filter_db(db, filter_params):
#     # Returns all rows in the database that match the filter parameters.
#     # Where filter_params is a dictionary of field names and their filter values.
#     # Row must match all of the filter fields to be included.
#     # For each field in filter_params, the row's value (or one of them if there are multiple) must match one of the possible filter values.
#     def match(row):
#         for filter, filter_values in filter_params.items():
#             if not isinstance(filter_values, list):
#                 filter_values = [filter_values]
#             if not isinstance(row.get(filter), list):
#                 row_values = [row.get(filter)]
#             if not any(row_value in filter_values for row_value in row_values):
#                 return False
#         return True
#     return [row for row in db if match(row)]

# class GetUsersInfoByParam(Tool): # READ
#     @staticmethod
#     def invoke(data: Dict[str, Any], filter_params: Dict[str, Any], info_items: List[str] = None) -> str:
#         db = data.get("users", [])
#         filtered_db = _filter_db(db, filter_params)
#         if info_items is None:
#             return json.dumps(filtered_db)
#         return json.dumps([{info_item: row.get(info_item) for info_item in info_items} for row in filtered_db])

#     @staticmethod
#     def get_info() -> Dict[str, Any]:
#         return {
#             "type": "function",
#             "function": {
#                 "name": "users_info_by_param",
#                 "description": "Filter users by parameters and return specified fields.",
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "filter_params": {"type": "object", "description": "Dictionary of ways to filter items in the database. To pass the filter an item must match one of the possible given values for all the filtering paramets"},
#                         "info_items": {"type": "list", "items": {"type": "string"}, "description": "A list of all the keys of the infomation that should be returned by the function for the filtered database entries."}
#                     },
#                     "required": ["filter_params"]
#                 }
#             }
#         }


# Generic function to filter the database based on the provided filter parameters.
class GetInfoFromDB(Tool): # READ
    @staticmethod
    def invoke(data: Dict[str, Any], database_name:str, filter_params: Dict[str, Any], required_fields: List[str] = None) -> str:
        db = data.get(database_name, [])

        filtered_db = [row for row in db if _match(row, filter_params)]
        if not filtered_db:
            return json.dumps({"error": "No entries found matching the filter parameters."})

        # If no specific fields are requested, return the full filtered database.
        if required_fields is None:
            return json.dumps(filtered_db)

        # Otherwise, return only the specified fields.
        return json.dumps([{required_field: row.get(required_field) for required_field in required_fields} for row in filtered_db])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_info_from_db",
                "description": "Filter users by parameters and return specified fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "database_name": {
                            "type": "string",
                            "description": "The name of the database to filter. This should match the key in the data dictionary."
                        },
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary/List of ways to filter items in the database. Dictionaries are AND conditions, lists are OR conditions."
                        },
                        "required_fields": {
                            "type": "list",
                            "items": {"type": "string"},
                            "description": "A list of all the keys of the infomation that should be returned by the function for the filtered database entries."
                        }
                    },
                    "required": ["filter_params"]
                }
            }
        }

class UpdateDB(Tool): # WRITE
    @staticmethod
    # For values in a list, it will just append the new value to the list.
    # To change or remove a value in a list, you must use pass the entire list as you want it to be, and it will replace the old list.
    def invoke(data: Dict[str, Any], database_name:str, filter_params: Dict[str, Any], update_params: Dict[str, Any]) -> str:
        db = data.get(database_name, [])
        filtered_db = [row for row in db if _match(row, filter_params)]
        for row in filtered_db:
            _apply_update(row, update_params)
        return json.dumps(filtered_db)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_db",
                "description": "Edit entries in the database based on filter parameters and update parameters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "database_name": {
                            "type": "string",
                            "description": "The name of the database to edit. This should match the key in the data dictionary."
                        },
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary/List of ways to filter items in the database. Dictionaries are AND conditions, lists are OR conditions."
                        },
                        "update_params": {
                            "type": "object",
                            "description": "Dictionary of fields to update and their new values."
                        }
                    },
                    "required": ["filter_params", "update_params"]
                }
            }
        }

# Lists
# users: order ids
# tracking: item ids
# suppliers: product ids
# orders: item ids
# couriers: coverage areas
# couriers: tracking ids

# Lists of Dictionaries
# orders: fulfillments -> probably only will need adding to, done with UpdateDB
# orders: payment history -> add to using UpdateDB, edit using specific function.

class UpdatePaymentHistory(Tool): # WRITE
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, transaction_type: str, payment_info_to_update: Dict[str, Any]) -> str:
        db = data.get("orders", [])
        order = [row for row in db if row["order_id"] == order_id]

        if len(order) > 1:
            return json.dumps({"error":f"More than one order found with id: {order_id}"})
        if not order:
            return json.dumps({"error":f"Order with id: {order_id} not found"})
        order = order[0]

        payment_history = order["payment_history"]
        for payment in payment_history:
            if payment["transaction_type"] == transaction_type:
                for key, value in payment_info_to_update.items():
                    payment[key] = value
                return json.dumps(payment_history)
        return json.dumps({"error":f"No payment of transaction type {transaction_type} found. Use UpdateDB tool to add payments"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_payment_history",
                "description": "Update values in an orders payment history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to update."},
                        "transaction_type": {"type": "string", "description": "The type of transaction to update."},
                        "payment_info_to_update": {
                            "type": "object",
                            "description": "A dictionary containing payment information to update."
                        }
                    },
                    "required": ["order_id", "transaction_type", "payment_info_to_update"]
                }
            }
        }

class DeleteFromDB(Tool): # WRITE
    @staticmethod
    def invoke(data: Dict[str, Any], database_name:str, filter_params: Dict[str, Any], delete_params: Dict[str, Any]) -> str:
        db = data.get(database_name, [])
        filtered_db = [row for row in db if _match(row, filter_params)]
        filtered_db = _apply_delete(filtered_db, delete_params)
        return json.dumps(filtered_db)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_from_db",
                "description": "Delete entries from the database based on filter parameters and delete parameters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "database_name": {
                            "type": "string",
                            "description": "The name of the database to delete from. This should match the key in the data dictionary."
                        },
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary/List of ways to filter items in the database. Dictionaries are AND conditions, lists are OR conditions."
                        },
                        "delete_params": {
                            "type": "object",
                            "description": "Dictionary of fields to delete and their values."
                        }
                    },
                    "required": ["database_name","filter_params", "delete_params"]
                }
            }
        }


class GetUserIdFromFullNameAndZip(Tool): # READ
    @staticmethod
    def invoke(data: Dict[str, Any], first_name: str, last_name: str, zip: str) -> str:
        db = data.get("users", [])
        filter_params = {
            "name": {
                "first_name": first_name,
                "last_name": last_name
            },
            "address": {
                "zip": zip
            }
        }
        user = [row for row in db if _match(row, filter_params)]
        if len(user) > 1:
            return json.dumps({"error": "Multiple users found"})
        return json.dumps(user[0]["user_id"]) if user else json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_id_from_full_name_and_zip",
                "description": "Retrieve user information by user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {"type": "string", "description": "The user's first name."},
                        "last_name": {"type": "string", "description": "The user's last name."},
                        "zip": {"type": "string", "description": "The user's zip code."}
                    },
                    "required": ["first_name", "last_name", "zip"]
                    }
                }
            }

class GetUserIdFromEmail(Tool): # READ
    @staticmethod
    def invoke(data: Dict[str, Any], email: str) -> str:
        db = data.get("users", [])
        filter_params = {
            "email": email
        }

        user = [row for row in db if _match(row, filter_params)]
        if len(user) > 1:
            return json.dumps({"error": "Multiple users found"})
        return json.dumps(user[0]["user_id"]) if user else json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_id_from_email",
                "description": "Retrieve user information by email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {"type": "string", "description": "The user's email address."},
                    },
                    "required": ["email"]
                }
            }
        }

# functions that will get info from multiple databases
# Create order

class CreateOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, item_ids: List[str], payment_method_id: str) -> str:
        users = data["users"]
        orders = data["orders"]
        products = data["products"]

        items = []

        for product in products:
            for item_id, item in product["variants"].items():
                if item_id in item_ids:
                    item_info = {
                        "item_id": item_id,
                        "product_id": product["product_id"],
                        "name": product["name"],
                        "price": item["price"],
                        "options": item["options"],
                    }
                    items.append(item_info)

        # Check if the user exists
        user = [row for row in users if row["user_id"] == user_id]
        if len(user) > 1:
            return json.dumps({"error": "Multiple users found"})
        if len(user) == 0:
            return json.dumps({"error": "User not found"})
        user = user[0]

        # Check if the payment method exists
        if payment_method_id not in user["payment_methods"]:
            return json.dumps({"error": "Payment method not found"})

        # Calculate the total price of the items
        total_price = 0
        for item in items:
            total_price += item["price"]

        # Check if the payment method is a gift card and has enough balance
        payment_method = user["payment_methods"][payment_method_id]
        if payment_method["source"] == "gift_card":
            if payment_method["balance"] < total_price:
                return json.dumps({"error": "insufficient gift card balance to pay for the order"})
            else:
                payment_method["balance"] -= total_price
                payment_method["balance"] = round(payment_method["balance"], 2)

        payment = {
            "transaction_type": "payment",
            "amount": total_price,
            "payment_method_id": payment_method_id,
        }

        # Create a new order
        order_id = f"#W{len(orders) + 1:07d}"
        order = {
            "order_id": order_id,
            "user_id": user_id,
            "items": items,
            "address": user.get("address", {}),
            "fulfilments": [],
            "status": "pending",
            "payment_history": [payment],
            "timestamp": "2025-07-15T03:35:22.797102" # Fixed timestamp for determinism
        }

        # Add the order to the user's orders and the global orders list
        orders.append(order)
        user.setdefault("orders", []).append(order_id)

        return json.dumps(order)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_order",
                "description": "Create a new order for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user id, such as 'sara_doe_496'.",
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {
                                "type": "string",
                            },
                            "description": (
                                "The item ids to be included in the order."
                            ),
                        },
                        "payment_method_id": {
                            "type": "string",
                            "description": (
                                "The payment method id to pay for the order, such as 'gift_card_0000000' or 'credit_card_0000000'. "
                                "These can be looked up from the user details."
                            ),
                        },
                    },
                    "required": ["user_id", "items", "payment_method_id"],
                },
            },
        }

class CreateBulkOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, item_ids: List[Dict[str, Any]], payment_method_id: str) -> str:
        users = data["users"]
        orders = data["orders"]
        products = data["products"]

        items = []

        for product in products:
            for item_id, item in product["variants"].items():
                if item_id in item_ids.keys():
                    item_info = {
                        "item_id": item_id,
                        "product_id": product["product_id"],
                        "name": product["name"],
                        "price": item["price"],
                        "options": item["options"],
                    }
                    for _ in range(item_ids[item_id]):  # Add the item multiple times based on the quantity
                        items.append(item_info)

        # Check if the user exists
        user = [row for row in users if row["user_id"] == user_id]
        if len(user) > 1:
            return json.dumps({"error": "Multiple users found"})
        if len(user) == 0:
            return json.dumps({"error": "User not found"})
        user = user[0]

        # Check if the payment method exists
        if payment_method_id not in user["payment_methods"]:
            return json.dumps({"error": "Payment method not found"})

        # Calculate the total price of the items
        total_price = 0
        for item in items:
            total_price += item["price"]

        # Check if the payment method is a gift card and has enough balance
        payment_method = user["payment_methods"][payment_method_id]
        if payment_method["source"] == "gift_card":
            if payment_method["balance"] < total_price:
                return json.dumps({"error": "insufficient gift card balance to pay for the order"})
            else:
                payment_method["balance"] -= total_price
                payment_method["balance"] = round(payment_method["balance"], 2)

        payment = {
            "transaction_type": "payment",
            "amount": total_price,
            "payment_method_id": payment_method_id,
        }

        # Create a new order
        order_id = f"#W{len(orders) + 1:07d}"
        order = {
            "order_id": order_id,
            "user_id": user_id,
            "items": items,
            "address": user.get("address", {}),
            "fulfilments": [],
            "status": "pending",
            "payment_history": [payment],
            "timestamp": "2025-07-15T03:35:22.797102" # Fixed timestamp for determinism
        }

        # Add the order to the user's orders and the global orders list
        orders.append(order)
        user.setdefault("orders", []).append(order_id)

        return json.dumps(order)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_bulk_order",
                "description": "Create a new order for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user id, such as 'sara_doe_496'.",
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {
                                "type": "dictionary",
                                "keys": {
                                    "item_id": {"type": "string", "description": "The item id, such as 'item_0001'."},
                                },
                                "values": {
                                    "quantity": {"type": "integer", "description": "The quantity of the item to be included in the order."}
                                }
                            },
                            "description": (
                                "The item ids to be included in the order."
                            ),
                        },
                        "payment_method_id": {
                            "type": "string",
                            "description": (
                                "The payment method id to pay for the order, such as 'gift_card_0000000' or 'credit_card_0000000'. "
                                "These can be looked up from the user details."
                            ),
                        },
                    },
                    "required": ["user_id", "items", "payment_method_id"],
                },
            },
        }

# Create tracking
class CreateTracking(Tool): # WRITE
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, item_ids: List[str], courier_id: str, delivery_option: str) -> str:
        orders = data["orders"]
        order = [row for row in orders if row["order_id"] == order_id]

        couriers = data["couriers"]
        # Check if the delivery carrier exists
        courier_id_list = [row["courier_id"] for row in couriers]
        if courier_id not in courier_id_list:
            return json.dumps({"error": "Delivery carrier not found. It must be the id of a courier from the couriers database."})

        if len(order) > 1:
            return json.dumps({"error": "Multiple orders found"})
        if not order:
            return json.dumps({"error": "Order not found"})
        order = order[0]

        tracking_id = f"TRK{len(data['tracking']) + 1:07d}"

        # Add to the order db
        fulfillment = {
            "tracking_id": [tracking_id],
            "item_ids": item_ids
        }
        order.setdefault("fulfillments", []).append(fulfillment)

        # Add to the tracking db
        tracking_dict = {}
        tracking_dict["tracking_id"] = [tracking_id]
        tracking_dict["item_ids"] = item_ids
        tracking_dict["order_id"] = order_id
        tracking_dict["address"] = order.get("address", {})
        tracking_dict["delivery_carrier"] = courier_id
        tracking_dict["delivery_options"] = delivery_option
        tracking_dict["tracking_history"] = {"received": "2025-01-30T10:26:19.115651"}
        data["tracking"].append(tracking_dict)

        courier = [row for row in couriers if row["courier_id"] == courier_id]
        courier[0]["tracking_ids"].append(tracking_id)

        return json.dumps(tracking_dict)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_tracking",
                "description": "Create a new tracking entry for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to create tracking for."},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "List of item IDs associated with the tracking."},
                        "courier_id": {"type": "string", "description": "The delivery carrier for the tracking."},
                        "delivery_options": {"type": "string", "description": "Delivery options for the tracking."}
                    },
                    "required": ["order_id", "item_ids"]
                }
            }
        }

# Create supply order
class CreateSupplyOrder(Tool): # WRITE
    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str, item_id: str, quantity: int, unit_cost: float) -> str:
        suppliers = data["suppliers"]
        supply_orders = data["supply_orders"]
        products = data["products"]

        product = [row for row in products if item_id in row["variants"].keys()]
        if not product:
            return json.dumps({"error": "Product not found"})
        product = product[0]

        # Check if the supplier exists
        supplier = [row for row in suppliers if row["supplier_id"] == supplier_id]
        if len(supplier) > 1:
            return json.dumps({"error": "Multiple suppliers found"})
        if not supplier:
            return json.dumps({"error": "Supplier not found"})
        supplier = supplier[0]

        # Create a new supply order
        supply_order_id = f"#SO{len(supply_orders) + 1:04d}"
        total_cost = round(unit_cost * quantity, 2)
        supply_order = {
            "supply_order_id": supply_order_id,
            "supplier_id": supplier_id,
            "product_id": product["product_id"],
            "item_id": item_id,
            "quantity": quantity,
            "status": "pending",
            "order_date": "2024-10-26T00:01:34.394073",  # Fixed timestamp for determinism
            "unit_cost": unit_cost,
            "total_cost": total_cost
        }

        # Add the supply order to the database
        supply_orders.append(supply_order)

        return json.dumps(supply_order)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_supply_order",
                "description": "Create a new supply order for a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "The ID of the supplier to create the supply order for."},
                        "item_id": {"type": "string", "description": "The item ID to be ordered."},
                        "quantity": {"type": "integer", "description": "The quantity of the item to be ordered."},
                        "unit_cost": {"type": "number", "description": "The unit cost of the item."}
                    },
                    "required": ["supplier_id", "item_id", "quantity", "unit_cost"]
                }
            }
        }

class GetItemInfoFromId(Tool): # READ
    @staticmethod
    def invoke(data: Dict[str, Any], item_id: str) -> str:
        products = data.get("products", [])
        for product in products:
            if item_id in product["variants"]:
                return json.dumps(product["variants"][item_id])
        return json.dumps({"error": "Item not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_item_info_from_id",
                "description": "Retrieve item information by item ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string", "description": "The ID of the item to retrieve information for."}
                    },
                    "required": ["item_id"]
                }
            }
        }

class ProcessItemExchange(Tool): # WRITE
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, item_ids: list[str], new_item_ids: list[str], payment_method_id: str) -> str:
        orders = data["orders"]
        order = [row for row in orders if row["order_id"] == order_id]


        if len(order) > 1:
            return json.dumps({"error": "Multiple orders found"})
        if not order:
            return json.dumps({"error": "Order not found"})
        order = order[0]

        # Check if the item exists in the order
        items = order.get("items", [])

        removed_price = 0.0
        for item in items:
            if item["item_id"] in item_ids:
                removed_price += item["price"]

        for item in items:
            if item["item_id"] in item_ids:
                items.remove(item)

        products = data["products"]

        added_price = 0.0
        for product in products:
            for item_id, item in product["variants"].items():
                if item_id in new_item_ids:
                    item_info = {
                        "item_id": item_id,
                        "product_id": product["product_id"],
                        "name": product["name"],
                        "price": item["price"],
                        "options": item["options"],
                    }
                    added_price += item["price"]
                    items.append(item_info)

        exchange_cost = added_price - removed_price

        # Check if the gift card has enough balance
        user_id = order["user_id"]
        users = data["users"]
        user = [row for row in users if row["user_id"] == user_id]
        if len(user) > 1:
            return json.dumps({"error": "Multiple users found"})
        if not user:
            return json.dumps({"error": "User not found"})
        user = user[0]

        payment_method = user["payment_methods"].get(payment_method_id)
        if not payment_method:
            return json.dumps({"error": "Payment method not found"})

        if payment_method_id[:9] == "gift_card":
            if payment_method["balance"] < exchange_cost:
                return json.dumps({"error": "Insufficient gift card balance to pay for the exchange"})

            payment_method["balance"] -= exchange_cost
            payment_method["balance"] = round(payment_method["balance"], 2)

        payment_info = {
            "transaction_type": "exchange_payment" if exchange_cost > 0 else "exchange_refund",
            "amount": abs(exchange_cost),
            "payment_method_id": payment_method_id,
        }
        order["payment_history"].append(payment_info)



        return json.dumps(payment_info)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_item_exchange",
                "description": "Process an item exchange for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to process the exchange for."},
                        "item_id": {"type": "string", "description": "The ID of the item to be exchanged."},
                        "reason": {"type": "string", "description": "The reason for the exchange."}
                    },
                    "required": ["order_id", "item_id", "reason"]
                }
            }
        }

class ProcessItemReturn(Tool): # WRITE
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, item_ids: list[str], payment_method_id: str) -> str:
        orders = data["orders"]
        order = [row for row in orders if row["order_id"] == order_id]

        if len(order) > 1:
            return json.dumps({"error": "Multiple orders found"})
        if not order:
            return json.dumps({"error": "Order not found"})
        order = order[0]

        # Check if the item exists in the order
        items = order.get("items", [])

        refund_amount = 0.0
        for item in items:
            if item["item_id"] in item_ids:
                refund_amount += item["price"]

        for item in items:
            if item["item_id"] in item_ids:
                items.remove(item)

        # Check if the gift card has enough balance
        user_id = order["user_id"]
        users = data["users"]
        user = [row for row in users if row["user_id"] == user_id]
        if len(user) > 1:
            return json.dumps({"error": "Multiple users found"})
        if not user:
            return json.dumps({"error": "User not found"})
        user = user[0]

        payment_method = user["payment_methods"].get(payment_method_id)
        if not payment_method:
            return json.dumps({"error": "Payment method not found"})

        if payment_method["source"] == "gift_card":
            payment_method["balance"] += refund_amount
            payment_method["balance"] = round(payment_method["balance"], 2)

        # Add a return entry to the payment history
        payment_info = {
            "transaction_type": "return",
            "amount": refund_amount,
            "payment_method_id": payment_method_id,
        }
        order["payment_history"].append(payment_info)

        return json.dumps(payment_info)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_item_return",
                "description": "Process an item return for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "The ID of the order to process the return for."},
                        "item_ids": {"type": "array", "items": {"type": "string"}, "description": "List of item IDs to be returned."},
                        "payment_method_id": {"type": "string", "description": "The payment method ID to refund the return amount."}
                    },
                    "required": ["order_id", "item_ids", "payment_method_id"]
                }
            }
        }

class AddPaymentMethod(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, payment_method_source: str, last_four: str = None, brand: str = None, balance: int = None) -> str:
        users = data["users"]
        # Check if the user exists
        user = [row for row in users if row["user_id"] == user_id]
        if len(user) > 1:
            return json.dumps({"error": "Multiple users found"})
        if len(user) == 0:
            return json.dumps({"error": "User not found"})
        user = user[0]

        payment_method = {}
        payment_method["source"] = payment_method_source
        if payment_method_source == "gift_card":
            payment_method["balance"] = balance if balance is not None else 0
            payment_method["id"] = f"gift_card_{user_id[-4:]}"
        elif payment_method_source == "credit_card":
            if brand is not None:
                payment_method["brand"] = brand
            else:
                return json.dumps({"error": "brand is required for credit card"})
            if last_four is not None:
                payment_method["last_four"] = last_four
            else:
                return json.dumps({"error": "last four digits are required for credit card"})
            payment_method["id"] = f"credit_card_{user_id[-4:]}"
        elif payment_method_source == "paypal":
            payment_method["id"] = f"paypal_{user_id[-4:]}"
        else:
            return json.dumps({"error": "unsupported payment method source"})

        # Add the new payment method
        user["payment_methods"][payment_method["id"]] = payment_method
        return json.dumps(user)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_payment_method",
                "description": "Add a new payment method for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user id, such as 'sara_doe_496'.",
                        },
                        "payment_method_source": {
                            "type": "string",
                            "description": "The payment method to be added, including id, source (e.g., gift_card or credit_card), and balance if applicable."
                        },
                        "last_four": {
                            "type": "string",
                            "description": "The last four digits of the credit card (required if source is credit card)."
                        },
                        "brand": {
                            "type": "string",
                            "description": "The brand of the credit card, such as visa or mastercard (required if source is credit card)."
                        },
                        "balance": {
                            "type": "integer",
                            "description": "The balance of the gift card, if not present the balance is set to 0."
                        },

                    },
                    "required": ["user_id", "payment_method_source"],
                },
            },
        }

class AddMoneyToGiftCard(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, gift_card_id: str, payment_method_id: str, amount: float) -> str:
        users = data["users"]
        # Check if the user exists
        user = [row for row in users if row["user_id"] == user_id]
        if len(user) > 1:
            return json.dumps({"error": "Multiple users found"})
        if len(user) == 0:
            return json.dumps({"error": "User not found"})
        user = user[0]
        # Check if the gift card exists
        if gift_card_id not in user["payment_methods"]:
            return json.dumps({"error": "gift card not found"})

        # Check if the payment method exists
        if payment_method_id not in user["payment_methods"]:
            return json.dumps({"error": "payment method not found"})

        # Add money to the gift card
        user["payment_methods"][gift_card_id]["balance"] += amount
        user["payment_methods"][gift_card_id]["balance"] = round(user["payment_methods"][gift_card_id]["balance"], 2)

        return json.dumps(user)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_money_to_gift_card",
                "description": "Add money to a user's gift card.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user id, such as 'sara_doe_496'.",
                        },
                        "gift_card_id": {
                            "type": "string",
                            "description": "The gift card id, such as 'gift_card_0000'.",
                        },
                        "payment_method_id": {
                            "type": "string",
                            "description": "The payment method id to pay for the gift card, such as 'credit_card_0000'.",
                        },
                        "amount": {
                            "type": "number",
                            "description": "The amount of money to add to the gift card.",
                        },
                    },
                    "required": ["user_id", "amount"],
                },
            },
        }


TOOLS = [
    GetInfoFromDB(),
    UpdateDB(),
    UpdatePaymentHistory(),
    DeleteFromDB(),
    GetUserIdFromFullNameAndZip(),
    GetUserIdFromEmail(),
    CreateOrder(),
    CreateBulkOrder(),
    CreateTracking(),
    CreateSupplyOrder(),
    ProcessItemExchange(),
    ProcessItemReturn(),
    AddPaymentMethod(),
    AddMoneyToGiftCard(),
]
