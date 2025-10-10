import json
from collections import OrderedDict, defaultdict
from typing import Any, Dict, List, Optional

from domains.dto import Tool


class find_discountable_products(Tool):
    """
    Tool to search for all products that can be discounted
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get("supplier_id")

        products = data.get("products", [])

        out = []

        for product in products:
            # If supplier_id is sent, only include products from that supplier
            if (supplier_id is None) or (product["supplier_id"] == supplier_id):
                # Filter to discountable products and add to the return list
                if product["is_discountable"]:
                    out.append(product["name"])

        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_discountable_products",
                "description": "Gets the names of products that are considered discountable. If supplier_id is sent, then it will return only products for that supplier, otherwise it will return for all suppliers",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "OPTIONAL. The specific ID of the supplier to focus on.",
                        }
                    },
                },
            },
        }


class update_stock_quantity(Tool):
    """
    Tool to set the quantity of a certain product. This can be used after restocks or to handle cases where inventory is missing or damaged
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        timestamp = kwargs.get("timestamp")
        store_id = kwargs.get("store_id")
        sku = kwargs.get("sku")
        quantity = kwargs.get("quantity")
        relative_quantity = kwargs.get("relative_quantity")

        if (
            (store_id is None)
            or (sku is None)
            or ((quantity is None) and (relative_quantity is None))
        ):
            return json.dumps({"error": "store_id, sku, and quantity are required"})

        if (quantity is not None) and (quantity < 0):
            return json.dumps({"error": "quantity must be 0 or greater"})

        inventory = data.get("inventory", [])

        for item in inventory:
            # Matching item
            if (item["store_id"] == store_id) and (item["sku"] == sku):
                former_quantity = item["quantity"]

                # Update the quantity
                if quantity is not None:
                    item["quantity"] = quantity
                else:
                    item["quantity"] += int(relative_quantity)

                # Update the status
                if item["quantity"] <= item["safety_stock"]:
                    item["status"] = "critical"
                elif item["quantity"] <= item["reorder_level"]:
                    item["status"] = "low_stock"
                else:
                    item["status"] = "in_stock"

                return json.dumps({"success": True})

        return json.dumps({"error": "No matching product was found at the store"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_stock_quantity",
                "description": "Updates the quantity of a product and sets the status based on the quantity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "timestamp for database operations",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The specific ID of the store for the item",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The specific sku for the item",
                        },
                        "quantity": {
                            "type": "int",
                            "description": "The quantity to set for the item. Overrides relative_quantity",
                        },
                        "relative_quantity": {
                            "type": "int",
                            "description": "Will add or remove this much from the current quantity: 5 will add 5 and -2 will remove 2",
                        },
                    },
                },
            },
        }


class check_low_stock_items(Tool):
    """
    Tool that will reorder low stock items. Can order for specific stores and items, or everything all at once.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs.get("store_id")
        sku = kwargs.get("sku")

        inventory = data.get("inventory", [])

        out = []

        for item in inventory:
            # If filtering on store or sku
            if ((store_id is None) or (item["store_id"] == store_id)) and (
                (sku is None) or (item["sku"] == sku)
            ):
                # Check if item needs to be reordered
                if item["status"] in ["low_stock", "critical"]:
                    out.append(
                        {
                            k: item[k]
                            for k in [
                                "store_id",
                                "sku",
                                "status",
                                "safety_stock",
                                "reorder_level",
                                "quantity",
                            ]
                        }
                    )

        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_low_stock_items",
                "description": "Checks if items are low stock and need to be reordered. Returns a list of items that are low stock",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "OPTIONAL. The specific ID of the store to reorder items for. If not sent, every store will be checked.",
                        },
                        "sku": {
                            "type": "string",
                            "description": "OPTIONAL. The specific sku for the item to reorder. If not sent, every item will be checked",
                        },
                    },
                },
            },
        }


class get_detailed_item_price(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = data.get("sku")
        barcode = data.get("barcode")
        # quantity = data.get("quantity", 1)

        if (sku is None) and (barcode is None):
            return json.dumps({"error": "sku or barcode must be sent"}, indent=2)

        products = data.get("products", [])

        for product in products:
            if ((sku is not None) and (product["sku"] == sku)) or (
                (barcode is not None) and (product["barcode"] == barcode)
            ):
                # Get the sku if barcode was used
                sku = product["sku"]

                # Use the discount rate if the product is marked as discountable, otherwise set as 0
                discount_rate = (
                    product["discount_rate"] if product["is_discountable"] else 0.0
                )

                # Calculate the discount amount
                # discount = round(product["price"] * discount_rate, 2)

                tax_rate = product["tax_rate"]

                return json.dumps(
                    {
                        "sku": sku,
                        "unit_price": product["price"],
                        "discount_rate": discount_rate,
                        "tax_rate": tax_rate,
                    },
                    indent=2,
                )

        return json.dumps({"error": "product not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_detailed_item_price",
                "description": "Gets the price infomation for a single transaction line item. Can use either sku or barcode",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "The sku of the item"},
                        "barcode": {
                            "type": "string",
                            "description": "The barcode of the item",
                        },
                        # "quantity": {"type": "int", "description": "The amount of the item being purchased"}
                    },
                },
            },
        }


class find_check_out_employee(Tool):
    priority = [
        "Cashier",
        "Customer Service Rep",
        "Sales Associate",
        "Floor Supervisor",
        "Assistant Manager",
        "Store Manager",
        "Inventory Specialist",
        "Department Manager",
    ]

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employees = data.get("employees", [])

        store_id = kwargs.get("store_id")
        ignore_ids = kwargs.get("ignore_ids", [])
        if isinstance(ignore_ids, str):
            ignore_ids = json.loads(ignore_ids)

        # Inefficient double loop, but should be fine due to low number of roles
        for role in find_check_out_employee.priority:
            for employee in employees:
                if (
                    (employee["store_id"] == store_id)
                    and (employee["role"] == role)
                    and (employee["employee_id"] not in ignore_ids)
                ):
                    return json.dumps(employee, indent=2)

        return json.dumps({"error": "no suitable employee found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_check_out_employee",
                "description": "Gets an employee to process a transaction at a store",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "The store_id to check",
                        },
                        "ignore_ids": {
                            "type": "string",
                            "descrption": "These employee ids will be ignored when searching. Useful if someone is not available",
                        },
                    },
                },
            },
        }


class transaction_price_info(Tool):
    """
    A tool that will create a price from the given information. Does not do any write operations. The finish the transaction, use make_transaction
    """

    # TODO: gather logic into a shared utility for make_transaction

    @staticmethod
    def get_detailed_line_item_price(data, **kwargs):
        sku = kwargs.get("sku")
        barcode = kwargs.get("barcode")
        quantity = kwargs.get("quantity", 1)

        if (sku is None) and (barcode is None):
            return json.dumps({"error": "sku or barcode must be sent"}, indent=2)

        products = data.get("products", [])
        promotions = data.get("promotions", [])

        for product in products:
            if ((sku is not None) and (product["sku"] == sku)) or (
                (barcode is not None) and (product["barcode"] == barcode)
            ):
                # Get the sku if barcode was used
                sku = product["sku"]

                # Get the promotion information
                for promotion in promotions:
                    if sku in promotion["applicable_skus"]:
                        use_promotion = promotion
                        break

                # Use the discount rate if the product is marked as discountable, otherwise set as 0
                # if use_promotion["type"] == "percentage"
                discount_rate = (
                    product["discount_rate"] if product["is_discountable"] else 0.0
                )

                # Calculate the discount amount
                # discount = round(product["price"] * discount_rate, 2)

                tax_rate = product["tax_rate"]

                return json.dumps(
                    {
                        "sku": sku,
                        "unit_price": product["price"],
                        "discount_rate": discount_rate,
                        "tax_rate": tax_rate,
                    },
                    indent=2,
                )

        return json.dumps({"error": "product not found"})

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        timestamp = kwargs.get("timestamp")

        item_list = kwargs.get("line_items")
        if isinstance(item_list, str):
            item_list = json.loads(item_list)

        if item_list is None:
            return json.dumps({"error": "item_list must be sent"})

        # Line items suitable for a transaction record
        line_items = []

        # Running trackers for the overall order
        total_amount = 0
        tax_amount = 0
        tax_rate = 0
        discount_total = 0
        for item in item_list:
            sku = item.get("sku")
            barcode = item.get("barcode")
            quantity = item.get("quantity")

            # Get the price info for the item
            line_item_info = make_transaction.get_detailed_line_item_price(
                data, sku=sku, barcode=barcode
            )
            line_item_info = json.loads(line_item_info)

            # Unpack values
            sku = line_item_info["sku"]
            unit_price = line_item_info["unit_price"]
            unit_tax_rate = line_item_info["tax_rate"]
            discount_rate = line_item_info["discount_rate"]

            # Calculate line item totals
            # TODO: discount needs more work to account for different discount types
            unit_discount = unit_price * discount_rate
            item_sub_total = quantity * (unit_price - unit_discount)
            item_discount = round(quantity * unit_discount, 2)
            item_tax_amount = round(item_sub_total * unit_tax_rate, 2)
            item_final_amount = round(item_sub_total + item_tax_amount, 2)

            # Create the line item transaction log
            line_item = {
                "sku": sku,
                "quantity": quantity,
                "unit_price": unit_price,
                "discount": item_discount,
            }
            line_items.append(line_item)

            # Update the running totals
            total_amount += item_final_amount
            tax_amount += item_tax_amount
            discount_total += item_discount
            tax_rate = max(tax_rate, unit_tax_rate)

        # Build the final transaction log
        total_amount = round(total_amount, 2)
        tax_amount = round(tax_amount, 2)
        discount_total = round(discount_total, 2)
        transaction_row = {
            "total_amount": total_amount,
            "tax_amount": tax_amount,
            "tax_rate": tax_rate,
            "discount_total": discount_total,
            "line_items": line_items,
        }

        return json.dumps(transaction_row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transaction_price_info",
                "description": "Returns price info for communicating to a customer the price of an order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_list": {
                            "type": "string",
                            "description": "A list of items being purchased. This should be a json object with a structure like so: [{'sku' : XXX, 'quantity' : 1}, {'barcode' : YYY, 'quantity' : 2}]",
                        },
                    },
                },
            },
        }

        return json.dumps(transaction_row, indent=2)


class make_transaction(Tool):
    """
    Tool for handling a purchases and refunds. Adds the record to the transactions and updates the stock if necessary
    """

    @staticmethod
    def get_detailed_line_item_price(data, **kwargs):
        sku = kwargs.get("sku")
        barcode = kwargs.get("barcode")
        quantity = kwargs.get("quantity", 1)

        if (sku is None) and (barcode is None):
            return json.dumps({"error": "sku or barcode must be sent"}, indent=2)

        products = data.get("products", [])
        promotions = data.get("promotions", [])

        for product in products:
            if ((sku is not None) and (product["sku"] == sku)) or (
                (barcode is not None) and (product["barcode"] == barcode)
            ):
                # Get the sku if barcode was used
                sku = product["sku"]

                # Get the promotion information
                for promotion in promotions:
                    if sku in promotion["applicable_skus"]:
                        use_promotion = promotion
                        break

                # Use the discount rate if the product is marked as discountable, otherwise set as 0
                # if use_promotion["type"] == "percentage"
                discount_rate = (
                    product["discount_rate"] if product["is_discountable"] else 0.0
                )

                # Calculate the discount amount
                # discount = round(product["price"] * discount_rate, 2)

                tax_rate = product["tax_rate"]

                return json.dumps(
                    {
                        "sku": sku,
                        "unit_price": product["price"],
                        "discount_rate": discount_rate,
                        "tax_rate": tax_rate,
                    },
                    indent=2,
                )

        return json.dumps({"error": "product not found"})

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        timestamp = kwargs.get("timestamp")
        store_id = kwargs.get("store_id")
        employee_id = kwargs.get("employee_id")
        customer_id = kwargs.get("customer_id")
        item_list = kwargs.get("line_items")
        if isinstance(item_list, str):
            item_list = json.loads(item_list)
        payment_method = kwargs.get("payment_method")
        status = kwargs.get("status")
        amount_paid = kwargs.get("payment_amount")
        commit_transaction = kwargs.get("commit_transaction", True)

        if (
            (store_id is None)
            or (employee_id is None)
            or (customer_id is None)
            or (item_list is None)
        ):
            return json.dumps(
                {
                    "error": "store_id, employee_id, customer_id and item_list must be sent"
                }
            )

        transactions = data.get("transactions", [])

        # Line items suitable for a transaction record
        line_items = []

        # Running trackers for the overall order
        total_amount = 0
        tax_amount = 0
        tax_rate = 0
        discount_total = 0
        for item in item_list:
            sku = item.get("sku")
            barcode = item.get("barcode")
            quantity = item.get("quantity")

            # Get the price info for the item
            line_item_info = make_transaction.get_detailed_line_item_price(
                data, sku=sku, barcode=barcode
            )
            line_item_info = json.loads(line_item_info)

            # Unpack values
            sku = line_item_info["sku"]
            unit_price = line_item_info["unit_price"]
            unit_tax_rate = line_item_info["tax_rate"]
            discount_rate = line_item_info["discount_rate"]

            # Calculate line item totals
            # TODO: discount needs more work to account for different discount types
            unit_discount = unit_price * discount_rate
            item_sub_total = quantity * (unit_price - unit_discount)
            item_discount = round(quantity * unit_discount, 2)
            item_tax_amount = round(item_sub_total * unit_tax_rate, 2)
            item_final_amount = round(item_sub_total + item_tax_amount, 2)

            # Create the line item transaction log
            line_item = {
                "sku": sku,
                "quantity": quantity,
                "unit_price": unit_price,
                "discount": item_discount,
            }
            line_items.append(line_item)

            # Update the running totals
            total_amount += item_final_amount
            tax_amount += item_tax_amount
            discount_total += item_discount
            tax_rate = max(tax_rate, unit_tax_rate)

        # Check for sufficent payment and calculate change
        if (status == "completed") and (amount_paid < round(total_amount, 2)):
            if commit_transaction:
                return json.dumps(
                    {
                        "error": "Amount paid is insufficient. Order total is: {}".format(
                            total_amount
                        )
                    }
                )
            else:
                change_given = amount_paid
        else:
            change_given = round(amount_paid - total_amount, 2)

        # Build the final transaction log

        # Get the latest transaction id and increment by one
        transaction_id = (
            max([int(x["transaction_id"].split("-")[1]) for x in transactions]) + 1
        )

        total_amount = round(total_amount, 2)
        tax_amount = round(tax_amount, 2)
        discount_total = round(discount_total, 2)
        transaction_row = {
            "transaction_id": "TNX-{transaction_id:04}".format(
                transaction_id=transaction_id
            ),
            "store_id": store_id,
            "employee_id": employee_id,
            "timestamp": timestamp,
            "total_amount": total_amount,
            "tax_amount": tax_amount,
            "payment_method": payment_method,
            "tax_rate": tax_rate,
            "discount_total": discount_total,
            "change_given": change_given,
            "status": status,
            "customer_id": customer_id,
            "line_items": line_items,
        }
        # transaction_row = json.dumps(transaction_row, indent = 2)

        # Add to the database and return the item
        if commit_transaction:
            transactions.append(transaction_row)

        return json.dumps(transaction_row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "make_transaction",
                "description": "Creates the transaction log for a purchase",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "The current time",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The id of the store where the sale is",
                        },
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee processing the transaction",
                        },
                        "customer_id": {
                            "type": "string",
                            "description": "The id of the customer making the purchase",
                        },
                        "payment_method": {
                            "type": "string",
                            "description": "The payment type used. cash or credit_card",
                        },
                        "payment_amount": {
                            "type": "float",
                            "description": "The amount given by the customer",
                        },
                        "status": {
                            "type": "string",
                            "description": "Signifies if the transaction is a purchase or a refund. (completed, refunded)",
                        },
                        "item_list": {
                            "type": "string",
                            "description": "A list of items being purchased. This should be a json object with a structure like so: [{'sku' : XXX, 'quantity' : 1}, {'barcode' : YYY, 'quantity' : 2}]",
                        },
                        "commit_transaction": {
                            "type": "bool",
                            "description": "If true, the transaction will be commited and processed. If false, the function will just do a dry run and return the transaction information. Defaults to True",
                        },
                    },
                },
            },
        }


class find_transaction(Tool):
    """
    Searches for and returns a transaction. If the transaction_id is known, it will return that exact row. If the other parameters are sent, then it will search for and return all transactions matching those parameters
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        transaction_id = kwargs.get("transaction_id")
        store_id = kwargs.get("store_id")
        employee_id = kwargs.get("employee_id")
        customer_id = kwargs.get("customer_id")
        status = kwargs.get("status")
        date = kwargs.get("date")

        transactions = data.get("transactions", [])

        matches = []
        for transaction in transactions:
            # If transaction_id is sent, then use it over the other parameters
            if (transaction_id is not None) and (
                transaction["transaction_id"] == transaction_id
            ):
                return transaction

            # Otherwise, add to the list of matches if any of the search parameters matches
            else:
                # Get matches
                store_id_match = (store_id is not None) and (
                    transaction["store_id"] == store_id
                )
                employee_id_match = (employee_id is not None) and (
                    transaction["employee_id"] == employee_id
                )
                customer_id_match = (customer_id is not None) and (
                    transaction["customer_id"] == customer_id
                )
                status_match = (status is not None) and (
                    transaction["status"] == status
                )
                date_match = (date is not None) and (
                    transaction["timestamp"][:10] == date
                )

                # Determine if row is a match
                # It should match all criteria that have been sent
                is_match = all(
                    [
                        bool_out
                        for key, bool_out in zip(
                            [store_id, employee_id, customer_id, status, date],
                            [
                                store_id_match,
                                employee_id_match,
                                customer_id_match,
                                status_match,
                                date_match,
                            ],
                        )
                        if key is not None
                    ]
                )

                if is_match:
                    matches.append(json.dumps(transaction))

        return json.dumps(matches)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_transaction",
                "description": "Finds a transaction. Will return 1 row if transaction_id is sent, otherwise it will return rows that match the other parameters",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {
                            "type": "string",
                            "description": "The exact id of the transaction if it is known",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The id of the store where the transaction took place",
                        },
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee that processed the order",
                        },
                        "customer_id": {
                            "type": "string",
                            "description": "The id of the customer that made the transaction",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the order",
                        },
                        "date": {
                            "type": "string",
                            "description": "The date of the order. YYYY-MM-DD",
                        },
                    },
                },
            },
        }


class cancel_promotion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        promotion_id = kwargs.get("promotion_id")

        if promotion_id is None:
            return json.dumps({"error": "promotion_id must be sent"})

        promotions = data.get("promotions", [])
        products = data.get("products", [])

        for promotion in promotions:
            # Filter to the correct promotion
            if promotion["promotion_id"] == promotion_id:
                # Remove discounts from products
                # TODO: check if there can be multiple promotions per product
                applicable_skus = promotion["applicable_skus"]
                for product in products:
                    if product["sku"] in applicable_skus:
                        product["is_discountable"] = False

                # TODO: should the row just be removed?
                promotion["status"] = "canceled"

        return json.dumps({"success": "complete"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_promotion",
                "description": "Cancels a current promotion",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "The id of the promotion to cancel",
                        }
                    },
                },
            },
        }


class create_promotion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        promotion_fields = [
            "name",
            "type",
            "discount_value",
            "description",
            "applicable_skus",
            "start_date",
            "end_date",
            "status",
            "usage_limit",
        ]

        promotion_fields_unpacked = {k: kwargs[k] for k in promotion_fields}

        # If applicable_skus is sent as a json, it needs to be converted to a list
        if isinstance(promotion_fields_unpacked["applicable_skus"], str):
            promotion_fields_unpacked["applicable_skus"] = json.loads(
                promotion_fields_unpacked["applicable_skus"]
            )

        promotions = data.get("promotions", [])
        products = data.get("products", [])

        promotion_id = (
            max([int(x["promotion_id"].split("-")[1]) for x in promotions]) + 1
        )

        # TODO: set status automatically based on start date
        promotion_row = {
            "promotion_id": "PROMO-{promotion_id:03}".format(promotion_id=promotion_id),
            "name": promotion_fields_unpacked["name"],
            "type": promotion_fields_unpacked["type"],
            "discount_value": promotion_fields_unpacked["discount_value"],
            "description": promotion_fields_unpacked["description"],
            "applicable_skus": promotion_fields_unpacked["applicable_skus"],
            "start_date": promotion_fields_unpacked["start_date"],
            "end_date": promotion_fields_unpacked["end_date"],
            "status": promotion_fields_unpacked["status"],
            "usage_limit": promotion_fields_unpacked["usage_limit"],
            "times_used": 0,
        }

        # Update the skus
        for product in products:
            if product["sku"] in promotion_fields_unpacked["applicable_skus"]:
                product["is_discountable"] = True

                # TODO: will need to handle different discount types
                product["discount_rate"] = (
                    promotion_fields_unpacked["discount_value"] / 100.0
                )

        return json.dumps({"success": "complete"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_promotion",
                "description": "Creates a new promotion",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The human readable name for the promotion",
                        },
                        "type": {
                            "type": "string",
                            "description": "The type of promotion. 'fixed_bundle', 'tax_free', 'percentage', 'bogo_percentage'",
                        },
                        "discount_value": {
                            "type": "int",
                            "description": "The discount amount as an integer for percentage and bogo_percentage",
                        },
                        "description": {
                            "type": "string",
                            "description": "A human readable description of the sale",
                        },
                        "applicable_skus": {
                            "type": "string",
                            "description": "A json list containing the skus that the discount applies to",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The date the promotion starts on. YYYY-MM-DD",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The date the promotion ends on. YYYY-MM-DD",
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the promotion. Should be 'active' if the sale is going or 'planned' if it is happening in the future",
                        },
                        "usage_limit": {
                            "type": "int",
                            "description": "The number of times the sale can be used.",
                        },
                    },
                },
            },
        }


class find_promotions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        promotions = data.get("promotions", [])

        # If customer id is sent, then it will override all other criteria
        promotion_id = kwargs.get("promotion_id")

        # These columns will be matched exactly to the value sent
        exact_match_cols = ["type", "status"]
        exact_match_values = {k: kwargs.get(k) for k in exact_match_cols}

        # These columns will be matched as long as the database field contains the sent value
        approximate_match_cols = ["name", "description"]
        approximate_match_values = {k: kwargs.get(k) for k in approximate_match_cols}

        # These columns have special matching criteria
        special_match_cols = ["has_sku"]
        special_match_values = {k: kwargs.get(k) for k in special_match_cols}

        matches = []
        for promotion in promotions:
            # customer_id takes priority
            if (promotion_id is not None) and (
                promotion["promotion_id"] == promotion_id
            ):
                return json.dumps(promotion, indent=2)

            # If all sent criteria match, then add it to the return list
            elif (
                all(
                    [
                        exact_match_values[k] == promotion[k]
                        for k in exact_match_values.keys()
                        if exact_match_values[k] is not None
                    ]
                )
                and all(
                    [
                        approximate_match_values[k].lower() in promotion[k].lower()
                        for k in approximate_match_values.keys()
                        if approximate_match_values[k] is not None
                    ]
                )
                and all(
                    [
                        (
                            special_match_values["has_sku"]
                            in promotion["applicable_skus"]
                            if special_match_values["has_sku"] is not None
                            else True
                        )
                    ]
                )
            ):
                matches.append(promotion)

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_promotions",
                "description": "Finds promotions matching the sent criteria. Returns an empty list if there are none",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {
                            "type": "string",
                            "description": "The id of the promotion to return. If found, the function will return only the promotion matching the promotion_id",
                        },
                        "type": {
                            "type": "string",
                            "description": "type of the promotion. Will do an exact match",
                        },
                        "status": {
                            "type": "string",
                            "description": "status of the promotion. Will do an exact match",
                        },
                        "name": {
                            "type": "string",
                            "description": "name of the promotion. Will do an approximate match",
                        },
                        "description": {
                            "type": "string",
                            "description": "description of the promotion. Will do an approximate match",
                        },
                        "has_sku": {
                            "type": "string",
                            "description": "Will find promotions that apply to the sent sku",
                        },
                    },
                },
            },
        }


class create_customer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customers = data.get("customers", [])

        # Timestamp needs to be sent for database records
        timestamp = kwargs.get("timestamp")

        # These values must be sent
        required_cols = ["name", "phone_number", "email", "address", "birthdate"]

        # These values have defaults if not sent
        optional_cols = ["loyalty_points", "membership_level", "opt_in_marketing"]

        required_values = {k: kwargs.get(k) for k in required_cols}
        optional_values = {
            "loyalty_points": 0,
            "membership_level": "basic",
            "opt_in_marketing": False,
        }
        optional_values.update({k: kwargs[k] for k in optional_cols if k in kwargs})

        # These values are calculated by the function
        fill_in = {
            "customer_id": "CUST-5{customer_id:03}".format(
                customer_id=max(
                    [int(x["customer_id"].split("-")[1][1:]) for x in customers]
                )
                + 1
            ),
            "created_at": timestamp,
            "updated_at": timestamp,
            "status": "active",
        }

        # Throw an error if any of the required values are missing
        if any([required_values[k] is None for k in required_values.keys()]):
            return json.dumps(
                {
                    "error": "required values not sent: "
                    + ", ".join(
                        [k for k in required_values if required_values[k] is None]
                    )
                },
                indent=2,
            )

        # This is the order that the items appear in the database
        # May not be necessary since dictionaries are unordered, but it can make valiation easier if the items appear in the same order everytime
        col_order = [
            "customer_id",
            "name",
            "phone_number",
            "loyalty_points",
            "email",
            "address",
            "membership_level",
            "birthdate",
            "opt_in_marketing",
            "created_at",
            "updated_at",
            "status",
        ]

        # Order the items
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Add to the database
        customers.append(json.dumps(row_final, indent=2))

        # Return the whole row for reference
        return json.dumps(row_final, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_customer",
                "description": "Creates a new customer record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp. Used for database timestamp rows",
                        },
                        "name": {
                            "type": "string",
                            "description": "The customer's name",
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "The customer's phone number",
                        },
                        "email": {
                            "type": "string",
                            "description": "The customer's email",
                        },
                        "address": {
                            "type": "string",
                            "description": "The customer's street address",
                        },
                        "birthdate": {
                            "type": "string",
                            "description": "The customer's birthdate. YYYY-MM-DD",
                        },
                        "loyalty_points": {
                            "type": "int",
                            "description": "OPTIONAL. The number of loyalty points the customer has. This will normally be 0, but sometimes they can start with points as an incentive to create an account.",
                        },
                        "memebership_level": {
                            "type": "string",
                            "description": "OPTIONAL. The membership tier the customer is starting on. This will default to 'basic'.",
                        },
                        "opt_in_marketing": {
                            "type": "bool",
                            "description": "OPTIONAL. If the customer is opting into marketing. This will default to False",
                        },
                    },
                },
            },
        }


class remove_customer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customers = data.get("customers", [])

        customer_id = kwargs.get("customer_id")

        if customer_id is None:
            return json.dumps({"error": "customer_id must be sent"}, indent=2)

        for customer in customers:
            if customer["customer_id"] == customer_id:
                del customer

                return json.dumps(
                    {"success": "Removed customer: {}".format(customer_id)}, indent=2
                )

        return json.dumps({"error": "No customer found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_customer",
                "description": "Removes a customer record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The id of the customer to remove",
                        },
                    },
                },
            },
        }


class find_customers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customers = data.get("customers", [])

        # If customer id is sent, then it will override all other criteria
        customer_id = kwargs.get("customer_id")

        # These columns will be matched exactly to the value sent
        exact_match_cols = [
            "phone_number",
            "membership_level",
            "birthdate",
            "opt_in_marketing",
            "status",
        ]
        exact_match_values = {k: kwargs.get(k) for k in exact_match_cols}

        # These columns will be matched as long as the database field contains the sent value
        approximate_match_cols = ["name", "email", "address"]
        approximate_match_values = {k: kwargs.get(k) for k in approximate_match_cols}

        # These columns have special matching criteria
        special_match_values = {
            "birth_month": kwargs.get("birth_month"),
            "city": kwargs.get("city"),
        }

        matches = []
        for customer in customers:
            # customer_id takes priority
            if (customer_id is not None) and (customer["customer_id"] == customer_id):
                return json.dumps(customer, indent=2)

            # If all sent criteria match, then add it to the return list
            elif (
                all(
                    [
                        exact_match_values[k] == customer[k]
                        for k in exact_match_values.keys()
                        if exact_match_values[k] is not None
                    ]
                )
                and all(
                    [
                        approximate_match_values[k].lower() in customer[k].lower()
                        for k in approximate_match_values.keys()
                        if approximate_match_values[k] is not None
                    ]
                )
                and all(
                    [
                        (
                            "-{}-".format(special_match_values["birth_month"])
                            in customer["birthdate"]
                        )
                        if special_match_values["birth_month"] is not None
                        else True,
                        (
                            special_match_values["city"].lower()
                            == customer["address"].split(",")[1].strip().lower()
                        )
                        if special_match_values["city"] is not None
                        else True,
                    ]
                )
            ):
                matches.append(customer)

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_customers",
                "description": "Finds customer matching the sent criteria. Returns an empty list if there are none",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The id of the customer to return. If found, the function will return only the customer matching the customer_id",
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "phone number of the customer. Will do an exact match",
                        },
                        "membership_level": {
                            "type": "string",
                            "description": "membership level of the customer. Will do an exact match",
                        },
                        "status": {
                            "type": "string",
                            "description": "status of the customer. Will do an exact match",
                        },
                        "birthdate": {
                            "type": "string",
                            "description": "birth date of the customer. Will do an exact match",
                        },
                        "opt_in_marketing": {
                            "type": "bool",
                            "description": "opt in marketing of the customer. Will do an exact match",
                        },
                        "name": {
                            "type": "string",
                            "description": "name of the customer. Will do an approximate match",
                        },
                        "email": {
                            "type": "string",
                            "description": "email of the customer. Will do an approximate match",
                        },
                        "address": {
                            "type": "string",
                            "description": "address of the customer. Will do an approximate match",
                        },
                        "birth_month": {
                            "type": "int",
                            "description": "The month the person was born in. Will ignore year and day when matching to birth month",
                        },
                        "city": {
                            "type": "string",
                            "description": "The city the person lives in. Will ignore other values in the address and only focus on the city",
                        },
                    },
                },
            },
        }


class update_customer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customers = data.get("customers", [])

        # These parameters are mandatory for updates
        row_id = kwargs.get("customer_id")
        timestamp = kwargs.get("timestamp")

        if (row_id is None) or (timestamp is None):
            return json.dumps({"error": "customer_id and timestamp must be sent"})

        # These are the parameters being sent for update
        updatable_cols = [
            "name",
            "phone_number",
            "email",
            "address",
            "birthdate",
            "membership_level",
            "status",
            "loyalty_points",
            "opt_in_marketing",
        ]
        updating_values = {k: kwargs.get(k) for k in updatable_cols}

        for customer in customers:
            if customer["customer_id"] == row_id:
                for col, value in updating_values.items():
                    # Update any sent values
                    if value is not None:
                        customer[col] = value

                customer["updated_at"] = timestamp

                return json.dumps(customer, indent=2)

        return json.dumps({"error": "no matching records found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_customer",
                "description": "Creates a new customer record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp. Used for database timestamp rows",
                        },
                        "customer_id": {
                            "type": "string",
                            "description": "REQUIRED. The id of the customer to update",
                        },
                        "name": {
                            "type": "string",
                            "description": "The customer's name",
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "The customer's phone number",
                        },
                        "email": {
                            "type": "string",
                            "description": "The customer's email",
                        },
                        "address": {
                            "type": "string",
                            "description": "The customer's street address",
                        },
                        "birthdate": {
                            "type": "string",
                            "description": "The customer's birthdate. YYYY-MM-DD",
                        },
                        "loyalty_points": {
                            "type": "int",
                            "description": "The number of loyalty points the customer has",
                        },
                        "memebership_level": {
                            "type": "string",
                            "description": "The membership tier of the customer",
                        },
                        "opt_in_marketing": {
                            "type": "bool",
                            "description": "OPTIONAL. If the customer is opting into marketing",
                        },
                    },
                },
            },
        }


class create_employee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employees = data.get("employees", [])

        # Timestamp needs to be sent for database records
        timestamp = kwargs.get("timestamp")

        # These values must be sent
        required_cols = [
            "name",
            "phone_number",
            "email",
            "role",
            "hire_date",
            "store_id",
        ]

        # These values have defaults if not sent
        optional_cols = []

        required_values = {k: kwargs.get(k) for k in required_cols}
        optional_values = {}
        optional_values.update({k: kwargs[k] for k in optional_cols if k in kwargs})

        # These values are calculated by the function
        fill_in = {
            "employee_id": "EMP-1{employee_id:03}".format(
                employee_id=max(
                    [int(x["employee_id"].split("-")[1][1:]) for x in employees]
                )
                + 1
            ),
            "created_at": timestamp,
            "updated_at": timestamp,
            "status": "active",
        }

        # Throw an error if any of the required values are missing
        if any([required_values[k] is None for k in required_values.keys()]):
            return json.dumps(
                {
                    "error": "required values not sent: "
                    + ", ".join(
                        [k for k in required_values if required_values[k] is None]
                    )
                },
                indent=2,
            )

        # This is the order that the items appear in the database
        # May not be necessary since dictionaries are unordered, but it can make valiation easier if the items appear in the same order everytime
        col_order = [
            "employee_id",
            "name",
            "role",
            "phone_number",
            "email",
            "store_id",
            "hire_date",
            "status",
        ]

        # Order the items
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Add to the database
        employees.append(json.dumps(row_final, indent=2))

        # Return the whole row for reference
        return json.dumps(row_final, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_employee",
                "description": "Creates a new employee record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp. Used for database timestamp rows",
                        },
                        "name": {
                            "type": "string",
                            "description": "The employee's name",
                        },
                        "role": {"type": "string", "description": "The employee's job"},
                        "phone_number": {
                            "type": "string",
                            "description": "The employee's phone number",
                        },
                        "email": {
                            "type": "string",
                            "description": "The employee's email",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The store_id where the employee works",
                        },
                        "hire_date": {
                            "type": "string",
                            "description": "The employee's hiredate. YYYY-MM-DD",
                        },
                    },
                },
            },
        }


class remove_employee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employees = data.get("employees", [])

        employee_id = kwargs.get("employee_id")

        if employee_id is None:
            return json.dumps({"error": "employee_id must be sent"}, indent=2)

        for employee in employees:
            if employee["employee_id"] == employee_id:
                del employee

                return json.dumps(
                    {"success": "Removed employee: {}".format(employee_id)}, indent=2
                )

        return json.dumps({"error": "No employee found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_employee",
                "description": "Removes an employee record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to remove",
                        },
                    },
                },
            },
        }


class find_employees(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employees = data.get("employees", [])

        # If customer id is sent, then it will override all other criteria
        employee_id = kwargs.get("employee_id")

        # These columns will be matched exactly to the value sent
        exact_match_cols = [
            "phone_number",
            "membership_level",
            "birthdate",
            "opt_in_marketing",
            "status",
            "role",
            "store_id",
        ]
        exact_match_values = {k: kwargs.get(k) for k in exact_match_cols}

        # These columns will be matched as long as the database field contains the sent value
        approximate_match_cols = ["name", "email", "address"]
        approximate_match_values = {k: kwargs.get(k) for k in approximate_match_cols}

        matches = []
        for employee in employees:
            # customer_id takes priority
            if (employee_id is not None) and (employee["employee_id"] == employee_id):
                return json.dumps(employee, indent=2)

            # If all sent criteria match, then add it to the return list
            elif all(
                [
                    exact_match_values[k] == employee[k]
                    for k in exact_match_values.keys()
                    if exact_match_values[k] is not None
                ]
            ) and all(
                [
                    approximate_match_values[k].lower() in employee[k].lower()
                    for k in approximate_match_values.keys()
                    if approximate_match_values[k] is not None
                ]
            ):
                matches.append(employee)

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_employees",
                "description": "Finds employees matching the sent criteria. Returns an empty list if there are none",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to return. If found, the function will return only the employee matching the employee_id",
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "phone number of the employee. Will do an exact match",
                        },
                        "status": {
                            "type": "string",
                            "description": "status of the employee. Will do an exact match",
                        },
                        "hire_date": {
                            "type": "string",
                            "description": "hire date of the employee. Will do an exact match",
                        },
                        "role": {
                            "type": "string",
                            "description": "job of the employee. Will do an exact match",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "store id where the employee works. Will do an exact match",
                        },
                        "name": {
                            "type": "string",
                            "description": "name of the employee. Will do an approximate match",
                        },
                        "email": {
                            "type": "string",
                            "description": "email of the employee. Will do an approximate match",
                        },
                    },
                },
            },
        }


class update_employee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employees = data.get("employees", [])

        # These parameters are mandatory for updates
        row_id = kwargs.get("employee_id")
        timestamp = kwargs.get("timestamp")

        if (row_id is None) or (timestamp is None):
            return json.dumps({"error": "employee_id and timestamp must be sent"})

        # These are the parameters being sent for update
        updatable_cols = [
            "name",
            "phone_number",
            "email",
            "hire_date",
            "status",
            "role",
        ]
        updating_values = {k: kwargs.get(k) for k in updatable_cols}

        for employee in employees:
            if employee["employee_id"] == row_id:
                for col, value in updating_values.items():
                    # Update any sent values
                    if value is not None:
                        employee[col] = value

                employee["updated_at"] = timestamp

                return json.dumps(employee, indent=2)

        return json.dumps({"error": "no matching records found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employee",
                "description": "Creates a new employee record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp. Used for database timestamp rows",
                        },
                        "customer_id": {
                            "type": "string",
                            "description": "REQUIRED. The id of the customer to update",
                        },
                        "name": {
                            "type": "string",
                            "description": "The customer's name",
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "The customer's phone number",
                        },
                        "email": {
                            "type": "string",
                            "description": "The customer's email",
                        },
                        "birthdate": {
                            "type": "string",
                            "description": "The customer's birthdate. YYYY-MM-DD",
                        },
                    },
                },
            },
        }


class create_inventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory = data.get("inventory", [])

        # Timestamp needs to be sent for database records
        timestamp = kwargs.get("timestamp")

        # These values must be sent
        required_cols = [
            "sku",
            "store_id",
            "quantity",
            "reserved_quantity",
            "reorder_level",
            "safety_stock",
            "location",
        ]

        # These values have defaults if not sent
        optional_cols = []

        required_values = {k: kwargs.get(k) for k in required_cols}
        optional_values = {}
        optional_values.update({k: kwargs[k] for k in optional_cols if k in kwargs})

        # These values are calculated by the function
        if required_values["quantity"] > required_values["reorder_level"]:
            status = "in_stock"
        elif required_values["quantity"] > required_values["safety_stock"]:
            status = "low_stock"
        else:
            status = "critical"
        fill_in = {
            "id": "INV-{inv_id:04}".format(
                inv_id=max([int(x["id"].split("-")[1][1:]) for x in inventory]) + 1
            ),
            "created_at": timestamp,
            "updated_at": timestamp,
            "status": status,
            "last_stock_count": timestamp[:10],
        }

        # Throw an error if any of the required values are missing
        if any([required_values[k] is None for k in required_values.keys()]):
            return json.dumps(
                {
                    "error": "required values not sent: "
                    + ", ".join(
                        [k for k in required_values if required_values[k] is None]
                    )
                },
                indent=2,
            )

        # This is the order that the items appear in the database
        # May not be necessary since dictionaries are unordered, but it can make valiation easier if the items appear in the same order everytime
        col_order = [
            "id",
            "sku",
            "store_id",
            "quantity",
            "reserved_quantity",
            "reorder_level",
            "safety_stock",
            "location",
            "status",
            "last_stock_count",
            "created_at",
            "updated_at",
        ]

        # Order the items
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Add to the database
        inventory.append(json.dumps(row_final, indent=2))

        # Return the whole row for reference
        return json.dumps(row_final, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_inventory",
                "description": "Adds a new inventory item to the store. This is for items the store has never stocked before, to update the quantity of an existing item, use update_stock_quantity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp. Used for database timestamp rows",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The sku of the item being added",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The id of the store adding the inventory",
                        },
                        "quantity": {
                            "type": "int",
                            "description": "The amount that the store starts with",
                        },
                        "reserved_quantity": {
                            "type": "int",
                            "description": "The amount in reserve",
                        },
                        "reorder_level": {
                            "type": "int",
                            "description": "The amount to start reordering products",
                        },
                        "safety_stock": {
                            "type": "int",
                            "description": "The amount to consider critical stock",
                        },
                        "location": {
                            "type": "string",
                            "description": "The shelf location of the item",
                        },
                    },
                },
            },
        }


class remove_inventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory = data.get("inventory", [])

        inv_id = kwargs.get("inv_id")

        if inv_id is None:
            return json.dumps({"error": "inv_id must be sent"}, indent=2)

        for item in inventory:
            if item["id"] == inv_id:
                del item

                return json.dumps(
                    {"success": "Removed item: {}".format(inv_id)}, indent=2
                )

        return json.dumps({"error": "No item found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_inventory",
                "description": "Removes an item from the store. This is for completely removing an item, to set to 0, use update_stock_quantity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inv_id": {
                            "type": "string",
                            "description": "The id of the item to remove",
                        },
                    },
                },
            },
        }


class find_items(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory = data.get("inventory", [])

        # These columns will be matched exactly to the value sent
        exact_match_cols = ["id", "sku", "store_id", "status", "last_stock_count"]
        exact_match_values = {k: kwargs.get(k) for k in exact_match_cols}

        # These columns will be matched as long as the database field contains the sent value
        approximate_match_cols = ["location"]
        approximate_match_values = {k: kwargs.get(k) for k in approximate_match_cols}

        matches = []
        for item in inventory:
            # If all sent criteria match, then add it to the return list
            if all(
                [
                    exact_match_values[k] == item[k]
                    for k in exact_match_values.keys()
                    if exact_match_values[k] is not None
                ]
            ) and all(
                [
                    approximate_match_values[k].lower() in item[k].lower()
                    for k in approximate_match_values.keys()
                    if approximate_match_values[k] is not None
                ]
            ):
                matches.append(item)

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_items",
                "description": "Finds items matching the sent criteria. Returns an empty list if there are none",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "The inventory id of the item. Will do an exact match",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The store id of the item. Will do an exact match",
                        },
                        "status": {
                            "type": "string",
                            "description": "status of the employee. Will do an exact match",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The sku of the item. Will do an exact match",
                        },
                        "last_stock_count": {
                            "type": "string",
                            "description": "The last stock count of the item. Will do an exact match",
                        },
                        "location": {
                            "type": "string",
                            "description": "The shelf loaction of the item. Will do an approximate match",
                        },
                    },
                },
            },
        }


class create_product(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        products = data.get("products", [])

        # Timestamp needs to be sent for database records
        timestamp = kwargs.get("timestamp")

        # These values must be sent
        required_cols = [
            "sku",
            "name",
            "category",
            "price",
            "description",
            "supplier_id",
            "weight_kg",
            "dimensions_cm",
            "brand",
            "cost",
            "barcode",
            "tax_rate",
        ]

        # These values have defaults if not sent
        optional_cols = ["is_discountable", "status", "expiry_date", "discount_rate"]

        required_values = {k: kwargs.get(k) for k in required_cols}
        optional_values = {
            "is_discountable": False,
            "status": "active",
            "expiry_date": None,
            "discount_rate": 0.0,
        }
        optional_values.update({k: kwargs[k] for k in optional_cols if k in kwargs})

        # These values are calculated by the function
        fill_in = {"created_at": timestamp, "updated_at": timestamp}

        # Throw an error if any of the required values are missing
        if any([required_values[k] is None for k in required_values.keys()]):
            return json.dumps(
                {
                    "error": "required values not sent: "
                    + ", ".join(
                        [k for k in required_values if required_values[k] is None]
                    )
                },
                indent=2,
            )

        # This is the order that the items appear in the database
        # May not be necessary since dictionaries are unordered, but it can make valiation easier if the items appear in the same order everytime
        col_order = [
            "sku",
            "name",
            "category",
            "price",
            "is_discountable",
            "description",
            "supplier_id",
            "weight_kg",
            "dimensions_cm",
            "brand",
            "cost",
            "barcode",
            "tax_rate",
            "discount_rate",
            "status",
            "expiry_date",
            "created_at",
            "updated_at",
        ]

        # Order the items
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Add to the database
        products.append(json.dumps(row_final, indent=2))

        # Return the whole row for reference
        return json.dumps(row_final, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_product",
                "description": "Adds a new product",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp. Used for database timestamp rows",
                        },
                        "name": {
                            "type": "string",
                            "description": "The human readable name of the product",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category of the product. Ex: Electronics",
                        },
                        "price": {
                            "type": "float",
                            "description": "The base price the customer pays",
                        },
                        "description": {
                            "type": "string",
                            "description": "A human readable description of the product",
                        },
                        "supplier_id": {
                            "type": "string",
                            "description": "The supplier id of the supplier that offers the product",
                        },
                        "weight_kg": {
                            "type": "float",
                            "description": "The weight in kilos of the item",
                        },
                        "dimensions_cm": {
                            "type": "string",
                            "description": "The dimensions in cm of the product",
                        },
                        "brand": {
                            "type": "string",
                            "description": "The brand of the product",
                        },
                        "cost": {
                            "type": "string",
                            "description": "The cost the store pays for the product",
                        },
                        "barcode": {
                            "type": "string",
                            "description": "The barcode of the product",
                        },
                        "tax_rate": {
                            "type": "string",
                            "description": "The tax rate of the product",
                        },
                        "is_discountable": {
                            "type": "bool",
                            "description": "OPTIONAL. If the product has an active discount. Ensure that the promotions table is updated with this information. Defaults to False",
                        },
                        "discount_rate": {
                            "type": "float",
                            "description": "OPTIONAL. The rate the product can be discounted at. Ensure that the promotions table is updated with this information. Defaults to 0",
                        },
                        "expiry_date": {
                            "type": "string",
                            "description": "OPTIONAL. If this product has an expiration. Defaults to None",
                        },
                        "status": {
                            "type": "status",
                            "description": "OPTIONAL. Status of the product. Defaults to 'active'",
                        },
                    },
                },
            },
        }


class remove_product(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        products = data.get("products", [])

        sku = kwargs.get("sku")

        if sku is None:
            return json.dumps({"error": "sku must be sent"}, indent=2)

        for product in products:
            if product["sku"] == sku:
                del product

                return json.dumps(
                    {"success": "Removed product: {}".format(sku)}, indent=2
                )

        return json.dumps({"error": "No sku found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_product",
                "description": "Removes a product from the products table. This means that the supplier no longer offers it. Use remove_inventory if it is only being removed from a single store.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The sku of the product to remove",
                        },
                    },
                },
            },
        }


class find_products(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        products = data.get("products", [])

        # These columns will be matched exactly to the value sent
        exact_match_cols = [
            "sku",
            "category",
            "is_discountable",
            "supplier_id",
            "brand",
            "barcode",
            "status",
            "expiry_date",
        ]
        exact_match_values = {k: kwargs.get(k) for k in exact_match_cols}

        # These columns will be matched as long as the database field contains the sent value
        approximate_match_cols = ["name", "description", "created_at", "updated_at"]
        approximate_match_values = {k: kwargs.get(k) for k in approximate_match_cols}

        matches = []
        for product in products:
            # If all sent criteria match, then add it to the return list
            if all(
                [
                    exact_match_values[k] == product[k]
                    for k in exact_match_values.keys()
                    if exact_match_values[k] is not None
                ]
            ) and all(
                [
                    approximate_match_values[k].lower() in product[k].lower()
                    for k in approximate_match_values.keys()
                    if approximate_match_values[k] is not None
                ]
            ):
                matches.append(product)

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_products",
                "description": "Finds products matching the sent criteria. Returns an empty list if there are none",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The sku of the item. Will do an exact match",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category of the item. Will do an exact match",
                        },
                        "is_discountable": {
                            "type": "bool",
                            "description": "If the product can be discounted. Will do an exact match",
                        },
                        "supplier_id": {
                            "type": "string",
                            "description": "The supplier_id of the product. Will do an exact match",
                        },
                        "brand": {
                            "type": "string",
                            "description": "The brand of the item. Will do an exact match",
                        },
                        "barcode": {
                            "type": "string",
                            "description": "The barcode of the product. Will do an exact match",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the product. Will do an exact match",
                        },
                        "expiry_date": {
                            "type": "string",
                            "description": "The expiry_date of the product. Will do an exact match",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the product. Will do a approximate match",
                        },
                        "description": {
                            "type": "string",
                            "description": "The description of the product. Will do a approximate match",
                        },
                        "created_at": {
                            "type": "string",
                            "description": "The timestamp the product was created at. Will do a approximate match",
                        },
                        "updated_at": {
                            "type": "string",
                            "description": "The timestamp the product was last updated. Will do a approximate match",
                        },
                    },
                },
            },
        }


class get_profit_margins(Tool):
    @staticmethod
    def get_detailed_item_price(data, **kwargs):
        sku = kwargs.get("sku")
        barcode = kwargs.get("barcode")

        if (sku is None) and (barcode is None):
            return json.dumps({"error": "sku or barcode must be sent"}, indent=2)

        products = data.get("products", [])

        for product in products:
            if ((sku is not None) and (product["sku"] == sku)) or (
                (barcode is not None) and (product["barcode"] == barcode)
            ):
                # Get the sku if barcode was used
                sku = product["sku"]

                # Use the discount rate if the product is marked as discountable, otherwise set as 0
                discount_rate = (
                    product["discount_rate"] if product["is_discountable"] else 0.0
                )

                # Calculate the discount amount
                # discount = round(product["price"] * discount_rate, 2)

                tax_rate = product["tax_rate"]

                return json.dumps(
                    {
                        "sku": sku,
                        "unit_price": product["price"],
                        "discount_rate": discount_rate,
                        "tax_rate": tax_rate,
                        "cost": product["cost"],
                    },
                    indent=2,
                )

        return json.dumps({"error": "product not found"})

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        products = data.get("products", [])

        sku_list = kwargs.get("sku_list")
        if isinstance(sku_list, str):
            sku_list = json.loads(sku_list)
        ignore_discounts = kwargs.get("ignore_discounts", True)

        if sku_list is None:
            return json.dumps({"error": "sku_list must be sent"}, indent=2)

        out = []
        for sku in sku_list:
            # Get the price info for the item
            line_item_info = get_profit_margins.get_detailed_item_price(data, sku=sku)
            line_item_info = json.loads(line_item_info)

            # Unpack values
            sku = line_item_info["sku"]
            unit_price = line_item_info["unit_price"]
            unit_tax_rate = line_item_info["tax_rate"]
            discount_rate = line_item_info["discount_rate"]
            cost = line_item_info["cost"]

            # Calculate line item totals
            # TODO: discount needs more work to account for different discount types
            unit_discount = unit_price * discount_rate
            item_sub_total = unit_price - unit_discount
            item_discount = round(unit_discount, 2)
            item_tax_amount = round(item_sub_total * unit_tax_rate, 2)
            item_final_amount = round(item_sub_total + item_tax_amount, 2)

            if ignore_discounts:
                revenue = unit_price
            else:
                revenue = item_sub_total

            profit = revenue - cost

            profit_margin = profit / revenue

            profit_margin_percent = (profit / cost) * 100

            out.append(
                {
                    "sku": sku,
                    "profit": profit,
                    "profit_margin": profit_margin,
                    "profit_margin_percent": profit_margin_percent,
                }
            )

        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_profit_margins",
                "description": "Gets the per unit profit margins for items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku_list": {
                            "type": "string",
                            "description": "A json list of the skus to get the profit margins for",
                        },
                        "ignore_discounts": {
                            "type": "bool",
                            "description": "OPTIONAL. To calculate profits on the discounted total or not. Defaults to True",
                        },
                    },
                },
            },
        }


class get_top_selling_items(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        transactions = data.get("transactions", [])

        n_values = kwargs.get("n_values")

        filter_cols = ["store_id", "payment_method", "customer_id"]
        filter_values = {k: kwargs.get(k) for k in filter_cols if k in kwargs}

        item_tracker = defaultdict(int)
        for transaction in transactions:
            # Filter on any sent values
            if all([filter_values[k] == transaction[k] for k in filter_values.keys()]):
                line_items = transaction["line_items"]
                for item in line_items:
                    item_tracker[item["sku"]] += item["quantity"]

        out = OrderedDict()

        # Sort the values by total and get the top n items
        sort = sorted(item_tracker, key=item_tracker.get, reverse=True)
        if n_values is not None:
            sort = sort[:n_values]
        for sku in sorted(item_tracker, key=item_tracker.get, reverse=True)[:n_values]:
            out[sku] = item_tracker[sku]

        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_top_selling_items",
                "description": "Gets top selling items. Can filter values to narrow the scope",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "OPTIONAL. Filters on the store id",
                        },
                        "payment_method": {
                            "type": "string",
                            "description": "OPTIONAL. Filters on the payment method",
                        },
                        "customer_id": {
                            "type": "string",
                            "description": "OPTIONAL. Filters on the customer id",
                        },
                    },
                },
            },
        }


TOOLS = [
    find_discountable_products(),
    update_stock_quantity(),
    check_low_stock_items(),
    make_transaction(),
    find_transaction(),
    cancel_promotion(),
    create_promotion(),
    find_promotions(),
    create_customer(),
    remove_customer(),
    find_customers(),
    update_customer(),
    create_employee(),
    remove_employee(),
    find_employees(),
    update_employee(),
    create_inventory(),
    remove_inventory(),
    find_items(),
    create_product(),
    remove_product(),
    find_products(),
    get_profit_margins(),
    get_top_selling_items(),
    find_check_out_employee(),
    transaction_price_info(),
    get_detailed_item_price()
]
