import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def _apply_delete(db, delete_params):
    pass
    #When db is a dictionary, it returns None if the delete_params correspond to the row, otherwise it returns the row (which could be altered at a deeper level)

    #If db is a list, we must loop through every row
    if isinstance(db, list):
        #If delete_params is a dictionary, we delve further
        if isinstance(delete_params, dict):
            new_db = []
            for row in db:
                new_row = _apply_delete(row, delete_params)
                if new_row is not None:
                    new_db.append(new_row)
            return new_db
        elif isinstance(delete_params, list):
            #If delete_params is a list, we eliminate each item from the db
            for item in delete_params:
                db.remove(item)
        else:
            #If delete_params consists of a single value, we delete it from the db
            if delete_params in db:
                db.remove(delete_params)
    elif isinstance(db, dict):
        if isinstance(delete_params, dict):
            #If delete_params is a dictionary, we explore further
            for key, value in delete_params.items():
                if key in db.keys():
                    if db[key] == value:
                        return None  #This will delete the entire row from the upper level
                    else:
                        new_row = _apply_delete(db[key], value)
                        if new_row is None:
                            return None
                        else:
                            db[key] = new_row
    return db

#def _find_row_by_value(db, field, value):
#Returns the initial row in the database where the given field equals the value.
#for row in db:
#if row.get(field) == value:
#return row
#return None


#Returns True if at least one row satisfies the filter criteria.
#Filters may consist of a mix of lists (OR condition) and/or dictionaries (AND condition).
def _match(rows, filters):
    pass
    #Convert the row values into a list if they are not already for consistent processing
    if not isinstance(rows, list):
        rows = [rows]

    if isinstance(filters, list):
        #OR condition for lists; return true if any of them match
        return any(_match(rows, single_filter) for single_filter in filters.values()

    elif isinstance(filters, dict):
        for filter_key, filter_value in filters.items():
            #AND condition for dictionaries; any filter may yield false
            #It only passes and returns true if none return false
            if not any(_match(row.get(filter_key), filter_value) for row in rows.values()):
                return False

    else:
        if filters not in rows:
            return False
    return True


#Modifies values in a database row according to the update parameters.
#If the value is a list and the update value is not, it will add the update value to the list.
#In other cases, it will substitute the value.
def _apply_update(row, update_params):
    pass
    for key, value in update_params.items():
        if isinstance(value, dict) and isinstance(row.get(key), dict):
            _apply_update(row[key], value)
        elif isinstance(row.get(key), list) and not isinstance(value, list):
            row[key].append(value)
        else:
            row[key] = value
    return row


#def _filter_db(db, filter_params):
#Returns every row in the database that aligns with the filter parameters.
#Where filter_params is a dictionary containing field names and their corresponding filter values.
#A row must satisfy all filter fields to be included.
#For each field in filter_params, the row's value (or one of them if there are several) must correspond to one of the potential filter values.
#def match(row):
#for filter, filter_values in filter_params.items():
#if not isinstance(filter_values, list):
#filter_values = [filter_values]
#if not isinstance(row.get(filter), list):
#row_values = [row.get(filter)]
#if not any(row_value in filter_values for row_value in row_values.values()):
#return False
#return True
#return [row for row in db.values() if match(row)]

#class GetUsersInfoByParam(Tool): # READ
#@staticmethod
#def invoke(data: Dict[str, Any], filter_params: Dict[str, Any], info_items: List[str] = None) -> str:
#db = _convert_db_to_list(data.get("users", {}).values()
#filtered_db = _filter_db(db, filter_params)
#if info_items is None:
#return json.dumps(filtered_db)
#return json.dumps([{info_item: row.get(info_item) for info_item in info_items} for row in filtered_db])

#@staticmethod
#def get_info() -> Dict[str, Any]:
#return {
#"type": "function",
#"function": {
#"name": "usersInfoByParam",
#"description": "Filter users based on parameters and return designated fields.",
#"parameters": {
#"type": "object",
#"properties": {
#"filter_params": {"type": "object", "description": "Dictionary outlining methods to filter items in the database. For an item to pass the filter, it must match one of the possible values for all filtering parameters."},
#"info_items": {"type": "array", "items": {"type": "string"}, "description": "A list of all keys of the information that should be returned by the function for the filtered database entries."}
#},
#"required": ["filter_params"]
#}
#}
#}


#A general function to filter the database according to the specified filter parameters.
class GetInfoFromDB(Tool):  #READ
    @staticmethod
    def invoke(
        data: dict[str, Any],
        database_name: str,
        filter_params: dict[str, Any],
        required_fields: list[str] = None,
    ) -> str:
        pass
        db = _convert_db_to_list(data.get(database_name, {}))

        filtered_db = [row for row in db.values() if _match(row, filter_params)]
        if not filtered_db:
            payload = {"error": "No entries found matching the filter parameters."}
            out = json.dumps(
                payload)
            return out

        #If no specific fields are requested, return the entire filtered database.
        if required_fields is None:
            payload = filtered_db
            out = json.dumps(payload)
            return out
        payload = [
                {
                    required_field: row.get(required_field)
                    for required_field in required_fields
                }
                for row in filtered_db
            ]
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInfoFromDb",
                "description": "Filter users by parameters and return specified fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "database_name": {
                            "type": "string",
                            "description": "The name of the database to filter. This should match the key in the data dictionary.",
                        },
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary/List of ways to filter items in the database. Dictionaries are AND conditions, lists are OR conditions.",
                        },
                        "required_fields": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of all the keys of the infomation that should be returned by the function for the filtered database entries.",
                        },
                    },
                    "required": ["database_name", "filter_params"],
                },
            },
        }


class UpdateDB(Tool):  #WRITE
    @staticmethod
    #For values that are lists, it will simply add the new value to the list.
    #To modify or delete a value in a list, you need to provide the complete list as desired, and it will replace the existing list.
    def invoke(
        data: dict[str, Any],
        database_name: str,
        filter_params: dict[str, Any],
        update_params: dict[str, Any],
    ) -> str:
        pass
        db = _convert_db_to_list(data.get(database_name, {}))
        filtered_db = [row for row in db.values() if _match(row, filter_params)]
        for row in filtered_db:
            _apply_update(row, update_params)
        payload = filtered_db
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateDb",
                "description": "Edit entries in the database based on filter parameters and update parameters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "database_name": {
                            "type": "string",
                            "description": "The name of the database to edit. This should match the key in the data dictionary.",
                        },
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary/List of ways to filter items in the database. Dictionaries are AND conditions, lists are OR conditions.",
                        },
                        "update_params": {
                            "type": "object",
                            "description": "Dictionary of fields to update and their new values.",
                        },
                    },
                    "required": ["database_name", "filter_params", "update_params"],
                },
            },
        }


#Lists
#users: order identifiers
#tracking: item identifiers
#suppliers: product identifiers
#orders: item identifiers
#couriers: service areas
#couriers: tracking identifiers

#Collections of Dictionaries
#orders: fulfillments -> likely will only require additions, managed with UpdateDB
#orders: payment history -> append using UpdateDB, modify with a specific function.


class UpdatePaymentHistory(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        transaction_type: str,
        payment_info_to_update: dict[str, Any],
    ) -> str:
        pass
        db = _convert_db_to_list(data.get("orders", {}).values()
        order = [row for row in db.values() if row["order_id"] == order_id]

        if len(order) > 1:
            payload = {"error": f"More than one order found with id: {order_id}"}
            out = json.dumps(
                payload)
            return out
        if not order:
            payload = {"error": f"Order with id: {order_id} not found"}
            out = json.dumps(payload)
            return out
        order = order[0]

        payment_history = order["payment_history"]
        for payment in payment_history:
            if payment["transaction_type"] == transaction_type:
                for key, value in payment_info_to_update.items():
                    payment[key] = value
                payload = payment_history
                out = json.dumps(payload)
                return out
        payload = {
                "error": f"No payment of transaction type {transaction_type} found. Use UpdateDB tool to add payments"
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdatePaymentHistory",
                "description": "Update values in an orders payment history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to update.",
                        },
                        "transaction_type": {
                            "type": "string",
                            "description": "The type of transaction to update.",
                        },
                        "payment_info_to_update": {
                            "type": "object",
                            "description": "A dictionary containing payment information to update.",
                        },
                    },
                    "required": [
                        "order_id",
                        "transaction_type",
                        "payment_info_to_update",
                    ],
                },
            },
        }


class DeleteFromDB(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        database_name: str,
        filter_params: dict[str, Any],
        delete_params: dict[str, Any],
    ) -> str:
        pass
        db = _convert_db_to_list(data.get(database_name, {}))
        filtered_db = [row for row in db.values() if _match(row, filter_params)]
        filtered_db = _apply_delete(filtered_db, delete_params)
        payload = filtered_db
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteFromDb",
                "description": "Delete entries from the database based on filter parameters and delete parameters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "database_name": {
                            "type": "string",
                            "description": "The name of the database to delete from. This should match the key in the data dictionary.",
                        },
                        "filter_params": {
                            "type": "object",
                            "description": "Dictionary/List of ways to filter items in the database. Dictionaries are AND conditions, lists are OR conditions.",
                        },
                        "delete_params": {
                            "type": "object",
                            "description": "Dictionary of fields to delete and their values.",
                        },
                    },
                    "required": ["database_name", "filter_params", "delete_params"],
                },
            },
        }


class GetUserIdFromFullNameAndZip(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], first_name: str, last_name: str, zip: str) -> str:
        pass
        db = _convert_db_to_list(data.get("users", {}).values()
        filter_params = {
            "name": {"first_name": first_name, "last_name": last_name},
            "address": {"zip": zip},
        }
        user = [row for row in db.values() if _match(row, filter_params)]
        if len(user) > 1:
            payload = {"error": "Multiple users found"}
            out = json.dumps(payload)
            return out
        return (
            json.dumps(user[0]["user_id"])
            if user
            else json.dumps({"error": "User not found"})
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserIdFromFullNameAndZip",
                "description": "Retrieve user information by user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "The user's first name.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "The user's last name.",
                        },
                        "zip": {
                            "type": "string",
                            "description": "The user's zip code.",
                        },
                    },
                    "required": ["first_name", "last_name", "zip"],
                },
            },
        }


class GetUserIdFromEmail(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], email: str) -> str:
        pass
        db = _convert_db_to_list(data.get("users", {}).values()
        filter_params = {"email": email}

        user = [row for row in db.values() if _match(row, filter_params)]
        if len(user) > 1:
            payload = {"error": "Multiple users found"}
            out = json.dumps(payload)
            return out
        return (
            json.dumps(user[0]["user_id"])
            if user
            else json.dumps({"error": "User not found"})
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserIdFromEmail",
                "description": "Retrieve user information by email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "The user's email address.",
                        },
                    },
                    "required": ["email"],
                },
            },
        }


#functions designed to retrieve information from various databases
#Initiate order


class CreateOrder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], user_id: str, item_ids: list[str], payment_method_id: str
    ) -> str:
        pass
        users = data["users"]
        orders = data["orders"]
        products = data["products"]

        items = []

        for product in products.values():
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

        #Verify if the user is present
        user = [row for row in users.values() if row["user_id"] == user_id]
        if len(user) > 1:
            payload = {"error": "Multiple users found"}
            out = json.dumps(payload)
            return out
        if len(user) == 0:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out
        user = user[0]

        #Verify if the payment method is available
        if payment_method_id not in user["payment_methods"]:
            payload = {"error": "Payment method not found"}
            out = json.dumps(payload)
            return out

        #Compute the total cost of the items
        total_price = 0
        for item in items:
            total_price += item["price"]

        #Verify if the payment method is a gift card and has sufficient balance
        payment_method = user["payment_methods"][payment_method_id]
        if payment_method["source"] == "gift_card":
            if payment_method["balance"] < total_price:
                payload = {"error": "insufficient gift card balance to pay for the order"}
                out = json.dumps(
                    payload)
                return out
            else:
                payment_method["balance"] -= total_price
                payment_method["balance"] = round(payment_method["balance"], 2)

        payment = {
            "transaction_type": "payment",
            "amount": total_price,
            "payment_method_id": payment_method_id,
        }

        #Initiate a new order
        order_id = f"#W{len(orders) + 1:07d}"
        order = {
            "order_id": order_id,
            "user_id": user_id,
            "items": items,
            "address": user.get("address", {}).values()),
            "fulfilments": [],
            "status": "pending",
            "payment_history": [payment],
            "timestamp": "2025-07-15T03:35:22.797102",  #Constant timestamp for consistency
        }

        #Include the order in the user's orders and the overall orders list
        data["orders"][order_id] = order
        user.setdefault("orders", []).append(order_id)
        payload = order
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateOrder",
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
    def invoke(
        data: dict[str, Any],
        user_id: str,
        item_ids: dict[str, int],
        payment_method_id: str,
    ) -> str:
        pass
        users = data["users"]
        orders = data["orders"]
        products = data["products"]

        items = []

        for product in products.values():
            for item_id, item in product["variants"].items():
                if item_id in item_ids:
                    item_info = {
                        "item_id": item_id,
                        "product_id": product["product_id"],
                        "name": product["name"],
                        "price": item["price"],
                        "options": item["options"],
                    }
                    for _ in range(
                        item_ids[item_id]
                    ):  #Insert the item several times according to the quantity
                        items.append(item_info)

        #Verify if the user is present
        user = [row for row in users.values() if row["user_id"] == user_id]
        if len(user) > 1:
            payload = {"error": "Multiple users found"}
            out = json.dumps(payload)
            return out
        if len(user) == 0:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out
        user = user[0]

        #Verify if the payment method is available
        if payment_method_id not in user["payment_methods"]:
            payload = {"error": "Payment method not found"}
            out = json.dumps(payload)
            return out

        #Compute the total cost of the items
        total_price = 0
        for item in items:
            total_price += item["price"]

        #Verify if the payment method is a gift card and has sufficient balance
        payment_method = user["payment_methods"][payment_method_id]
        if payment_method["source"] == "gift_card":
            if payment_method["balance"] < total_price:
                payload = {"error": "insufficient gift card balance to pay for the order"}
                out = json.dumps(
                    payload)
                return out
            else:
                payment_method["balance"] -= total_price
                payment_method["balance"] = round(payment_method["balance"], 2)

        payment = {
            "transaction_type": "payment",
            "amount": total_price,
            "payment_method_id": payment_method_id,
        }

        #Initiate a new order
        order_id = f"#W{len(orders) + 1:07d}"
        order = {
            "order_id": order_id,
            "user_id": user_id,
            "items": items,
            "address": user.get("address", {}).values()),
            "fulfilments": [],
            "status": "pending",
            "payment_history": [payment],
            "timestamp": "2025-07-15T03:35:22.797102",  #Constant timestamp for consistency
        }

        #Include the order in the user's orders and the overall orders list
        data["orders"][order_id] = order
        user.setdefault("orders", []).append(order_id)
        payload = order
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateBulkOrder",
                "description": "Create a new order for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user id, such as 'sara_doe_496'.",
                        },
                        "item_ids": {
                            "type": "object",
                            "description": (
                                "A dictionary mapping item IDs to quantities. Keys are item_ids (strings), values are quantities (integers)."
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
                    "required": ["user_id", "item_ids", "payment_method_id"],
                },
            },
        }


#Initiate tracking
class CreateTracking(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        item_ids: list[str],
        courier_id: str,
        delivery_option: str,
    ) -> str:
        pass
        orders = data["orders"]
        order = [row for row in orders.values() if row["order_id"] == order_id]

        couriers = data["couriers"]
        #Verify if the delivery carrier is present
        courier_id_list = [row["courier_id"] for row in couriers.values()]
        if courier_id not in courier_id_list:
            payload = {
                    "error": "Delivery carrier not found. It must be the id of a courier from the couriers database."
                }
            out = json.dumps(
                payload)
            return out

        if len(order) > 1:
            payload = {"error": "Multiple orders found"}
            out = json.dumps(payload)
            return out
        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out
        order = order[0]

        tracking_id = f"TRK{len(data['tracking']) + 1:07d}"

        #Insert into the order database
        fulfillment = {"tracking_id": [tracking_id], "item_ids": item_ids}
        order.setdefault("fulfillments", []).append(fulfillment)

        #Insert into the tracking database
        tracking_dict = {}
        tracking_dict["tracking_id"] = [tracking_id]
        tracking_dict["item_ids"] = item_ids
        tracking_dict["order_id"] = order_id
        tracking_dict["address"] = order.get("address", {}).values()
        tracking_dict["delivery_carrier"] = courier_id
        tracking_dict["delivery_option"] = delivery_option
        tracking_dict["tracking_history"] = {"received": "2025-01-30T10:26:19.115651"}
        data["tracking"][tracking_id] = tracking_dict

        courier = [row for row in couriers.values() if row["courier_id"] == courier_id]
        courier[0]["tracking_ids"].append(tracking_id)
        payload = tracking_dict
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTracking",
                "description": "Create a new tracking entry for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to create tracking for.",
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of item IDs associated with the tracking.",
                        },
                        "courier_id": {
                            "type": "string",
                            "description": "The delivery carrier for the tracking.",
                        },
                        "delivery_option": {
                            "type": "string",
                            "description": "Delivery option for the tracking.",
                        },
                    },
                    "required": ["order_id", "item_ids"],
                },
            },
        }


#Initiate supply order
class CreateSupplyOrder(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_id: str,
        item_id: str,
        quantity: int,
        unit_cost: float,
    ) -> str:
        pass
        suppliers = data["suppliers"]
        supply_orders = data["supply_orders"]
        products = data["products"]

        product = [row for row in products.values() if item_id in row["variants"].keys()]
        if not product:
            payload = {"error": "Product not found"}
            out = json.dumps(payload)
            return out
        product = product[0]

        #Verify if the supplier is present
        supplier = [row for row in suppliers.values() if row["supplier_id"] == supplier_id]
        if len(supplier) > 1:
            payload = {"error": "Multiple suppliers found"}
            out = json.dumps(payload)
            return out
        if not supplier:
            payload = {"error": "Supplier not found"}
            out = json.dumps(payload)
            return out
        supplier = supplier[0]

        #Initiate a new supply order
        supply_order_id = f"#SO{len(supply_orders) + 1:04d}"
        total_cost = round(unit_cost * quantity, 2)
        supply_order = {
            "supply_order_id": supply_order_id,
            "supplier_id": supplier_id,
            "product_id": product["product_id"],
            "item_id": item_id,
            "quantity": quantity,
            "status": "pending",
            "order_date": "2024-10-26T00:01:34.394073",  #Constant timestamp for consistency
            "unit_cost": unit_cost,
            "total_cost": total_cost,
        }

        #Insert the supply order into the database
        data["supply_orders"][supply_order_id] = supply_order
        payload = supply_order
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSupplyOrder",
                "description": "Create a new supply order for a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier to create the supply order for.",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "The item ID to be ordered.",
                        },
                        "quantity": {
                            "type": "integer",
                            "description": "The quantity of the item to be ordered.",
                        },
                        "unit_cost": {
                            "type": "number",
                            "description": "The unit cost of the item.",
                        },
                    },
                    "required": ["supplier_id", "item_id", "quantity", "unit_cost"],
                },
            },
        }


class GetItemInfoFromId(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], item_id: str) -> str:
        pass
        products = data.get("products", {}).values()
        for product in products.values():
            if item_id in product["variants"]:
                payload = product["variants"][item_id]
                out = json.dumps(payload)
                return out
        payload = {"error": "Item not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getItemInfoFromId",
                "description": "Retrieve item information by item ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {
                            "type": "string",
                            "description": "The ID of the item to retrieve information for.",
                        }
                    },
                    "required": ["item_id"],
                },
            },
        }


class ProcessItemExchange(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any],
        order_id: str,
        item_ids: list[str],
        new_item_ids: list[str],
        payment_method_id: str,
    ) -> str:
        pass
        orders = data["orders"]
        order = [row for row in orders.values() if row["order_id"] == order_id]

        if len(order) > 1:
            payload = {"error": "Multiple orders found"}
            out = json.dumps(payload)
            return out
        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out
        order = order[0]

        #Verify if the item is present in the order
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
        for product in products.values():
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

        #Verify if the gift card has sufficient balance
        user_id = order["user_id"]
        users = data["users"]
        user = [row for row in users.values() if row["user_id"] == user_id]
        if len(user) > 1:
            payload = {"error": "Multiple users found"}
            out = json.dumps(payload)
            return out
        if not user:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out
        user = user[0]

        payment_method = user["payment_methods"].get(payment_method_id)
        if not payment_method:
            payload = {"error": "Payment method not found"}
            out = json.dumps(payload)
            return out

        if payment_method_id[:9] == "gift_card":
            if payment_method["balance"] < exchange_cost:
                payload = {"error": "Insufficient gift card balance to pay for the exchange"}
                out = json.dumps(
                    payload)
                return out

            payment_method["balance"] -= exchange_cost
            payment_method["balance"] = round(payment_method["balance"], 2)

        payment_info = {
            "transaction_type": (
                "exchange_payment" if exchange_cost > 0 else "exchange_refund"
            ),
            "amount": abs(exchange_cost),
            "payment_method_id": payment_method_id,
        }
        order["payment_history"].append(payment_info)
        payload = payment_info
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessItemExchange",
                "description": "Process an item exchange for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to process the exchange for.",
                        },
                        "item_id": {
                            "type": "string",
                            "description": "The ID of the item to be exchanged.",
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the exchange.",
                        },
                    },
                    "required": ["order_id", "item_id", "reason"],
                },
            },
        }


class ProcessItemReturn(Tool):  #WRITE
    @staticmethod
    def invoke(
        data: dict[str, Any], order_id: str, item_ids: list[str], payment_method_id: str
    ) -> str:
        pass
        orders = data["orders"]
        order = [row for row in orders.values() if row["order_id"] == order_id]

        if len(order) > 1:
            payload = {"error": "Multiple orders found"}
            out = json.dumps(payload)
            return out
        if not order:
            payload = {"error": "Order not found"}
            out = json.dumps(payload)
            return out
        order = order[0]

        #Verify if the item is present in the order
        items = order.get("items", [])

        refund_amount = 0.0
        for item in items:
            if item["item_id"] in item_ids:
                refund_amount += item["price"]

        for item in items:
            if item["item_id"] in item_ids:
                items.remove(item)

        #Verify if the gift card has sufficient balance
        user_id = order["user_id"]
        users = data["users"]
        user = [row for row in users.values() if row["user_id"] == user_id]
        if len(user) > 1:
            payload = {"error": "Multiple users found"}
            out = json.dumps(payload)
            return out
        if not user:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out
        user = user[0]

        payment_method = user["payment_methods"].get(payment_method_id)
        if not payment_method:
            payload = {"error": "Payment method not found"}
            out = json.dumps(payload)
            return out

        if payment_method["source"] == "gift_card":
            payment_method["balance"] += refund_amount
            payment_method["balance"] = round(payment_method["balance"], 2)

        #Insert a return record into the payment history
        payment_info = {
            "transaction_type": "return",
            "amount": refund_amount,
            "payment_method_id": payment_method_id,
        }
        order["payment_history"].append(payment_info)
        payload = payment_info
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessItemReturn",
                "description": "Process an item return for an order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to process the return for.",
                        },
                        "item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of item IDs to be returned.",
                        },
                        "payment_method_id": {
                            "type": "string",
                            "description": "The payment method ID to refund the return amount.",
                        },
                    },
                    "required": ["order_id", "item_ids", "payment_method_id"],
                },
            },
        }


class AddPaymentMethod(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        payment_method_source: str,
        last_four: str = None,
        brand: str = None,
        balance: int = None,
    ) -> str:
        pass
        users = data["users"]
        #Verify if the user is present
        user = [row for row in users.values() if row["user_id"] == user_id]
        if len(user) > 1:
            payload = {"error": "Multiple users found"}
            out = json.dumps(payload)
            return out
        if len(user) == 0:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out
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
                payload = {"error": "brand is required for credit card"}
                out = json.dumps(payload)
                return out
            if last_four is not None:
                payment_method["last_four"] = last_four
            else:
                payload = {"error": "last four digits are required for credit card"}
                out = json.dumps(
                    payload)
                return out
            payment_method["id"] = f"credit_card_{user_id[-4:]}"
        elif payment_method_source == "paypal":
            payment_method["id"] = f"paypal_{user_id[-4:]}"
        else:
            payload = {"error": "unsupported payment method source"}
            out = json.dumps(payload)
            return out

        #Insert the new payment method
        user["payment_methods"][payment_method["id"]] = payment_method
        payload = user
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddPaymentMethod",
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
                            "description": "The payment method to be added, including id, source (e.g., gift_card or credit_card), and balance if applicable.",
                        },
                        "last_four": {
                            "type": "string",
                            "description": "The last four digits of the credit card (required if source is credit card).",
                        },
                        "brand": {
                            "type": "string",
                            "description": "The brand of the credit card, such as visa or mastercard (required if source is credit card).",
                        },
                        "balance": {
                            "type": "integer",
                            "description": "The balance of the gift card, if not present the balance is set to 0.",
                        },
                    },
                    "required": ["user_id", "payment_method_source"],
                },
            },
        }


class AddMoneyToGiftCard(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str,
        gift_card_id: str,
        payment_method_id: str,
        amount: float,
    ) -> str:
        pass
        users = data["users"]
        #Verify if the user is present
        user = [row for row in users.values() if row["user_id"] == user_id]
        if len(user) > 1:
            payload = {"error": "Multiple users found"}
            out = json.dumps(payload)
            return out
        if len(user) == 0:
            payload = {"error": "User not found"}
            out = json.dumps(payload)
            return out
        user = user[0]
        #Verify if the gift card is present
        if gift_card_id not in user["payment_methods"]:
            payload = {"error": "gift card not found"}
            out = json.dumps(payload)
            return out

        #Verify if the payment method is available
        if payment_method_id not in user["payment_methods"]:
            payload = {"error": "payment method not found"}
            out = json.dumps(payload)
            return out

        #Deposit funds into the gift card
        user["payment_methods"][gift_card_id]["balance"] += amount
        user["payment_methods"][gift_card_id]["balance"] = round(
            user["payment_methods"][gift_card_id]["balance"], 2
        )
        payload = user
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddMoneyToGiftCard",
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
