import json
from collections import OrderedDict, defaultdict
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


class FindDiscountableProducts(Tool):
    """Tool for searching all products eligible for discounts"""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None) -> str:
        products = data.get("products", {}).values()

        out = []

        for product in products.values():
            # Include only products from the specified supplier if supplier_id is provided
            if (supplier_id is None) or (product["supplier_id"] == supplier_id):
                # Select discountable products and append them to the return list
                if product["is_discountable"]:
                    out.append(product["name"])
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findDiscountableProducts",
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


class UpdateStockQuantity(Tool):
    """Tool for adjusting the quantity of a specific product, useful after restocks or in cases of missing or damaged inventory"""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        timestamp: str = None,
        store_id: str = None,
        sku: str = None,
        quantity: int = None,
        relative_quantity: int = None
    ) -> str:
        if (
            (store_id is None)
            or (sku is None)
            or ((quantity is None) and (relative_quantity is None))
        ):
            payload = {"error": "store_id, sku, and quantity are required"}
            out = json.dumps(payload)
            return out

        if (quantity is not None) and (quantity < 0):
            payload = {"error": "quantity must be 0 or greater"}
            out = json.dumps(payload)
            return out

        inventory = data.get("inventory", {}).values()

        for item in inventory.values():
            # Item that matches
            if (item["store_id"] == store_id) and (item["sku"] == sku):
                item["quantity"]

                # Revise the quantity
                if quantity is not None:
                    item["quantity"] = quantity
                else:
                    item["quantity"] += int(relative_quantity)

                # Modify the status
                if item["quantity"] <= item["safety_stock"]:
                    item["status"] = "critical"
                elif item["quantity"] <= item["reorder_level"]:
                    item["status"] = "low_stock"
                else:
                    item["status"] = "in_stock"
                payload = {"success": True}
                out = json.dumps(payload)
                return out
        payload = {"error": "No matching product was found at the store"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateStockQuantity",
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
                            "type": "integer",
                            "description": "The quantity to set for the item. Overrides relative_quantity",
                        },
                        "relative_quantity": {
                            "type": "integer",
                            "description": "Will add or remove this much from the current quantity: 5 will add 5 and -2 will remove 2",
                        },
                    },
                },
            },
        }


class CheckLowStockItems(Tool):
    """Tool for reordering items with low stock, capable of ordering for specific stores and items or all at once."""

    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None, sku: str = None) -> str:
        inventory = data.get("inventory", {}).values()

        out = []

        for item in inventory.values():
            # When filtering by store or sku
            if ((store_id is None) or (item["store_id"] == store_id)) and (
                (sku is None) or (item["sku"] == sku)
            ):
                # Verify if the item requires reordering
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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckLowStockItems",
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


class GetDetailedItemPrice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, barcode: str = None) -> str:
        #quantity = data.get("quantity", 1)

        if (sku is None) and (barcode is None):
            payload = {"error": "sku or barcode must be sent"}
            out = json.dumps(payload, indent=2)
            return out

        products = data.get("products", {}).values()

        for product in products.values():
            if ((sku is not None) and (product["sku"] == sku)) or (
                (barcode is not None) and (product["barcode"] == barcode)
            ):
                #Retrieve the sku if a barcode was utilized
                sku = product["sku"]

                #Apply the discount rate for discountable products; otherwise, assign 0
                discount_rate = (
                    product["discount_rate"] if product["is_discountable"] else 0.0
                )

                #Determine the discount value
                #discount = round(product["price"] * discount_rate, 2)

                tax_rate = product["tax_rate"]
                payload = {
                        "sku": sku,
                        "unit_price": product["price"],
                        "discount_rate": discount_rate,
                        "tax_rate": tax_rate,
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": "product not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getDetailedItemPrice",
                "description": "Gets the price infomation for a single transaction line item. Can use either sku or barcode",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "The sku of the item"},
                        "barcode": {
                            "type": "string",
                            "description": "The barcode of the item",
                        },
                        #"quantity": {"type": "integer", "description": "The quantity of the item being bought"}
                    },
                },
            },
        }


class FindCheckOutEmployee(Tool):
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
    def invoke(data: dict[str, Any], store_id: str, ignore_ids: list[str] = None) -> str:
        employees = data.get("employees", {}).values()

        if ignore_ids is None:
            ignore_ids = []
        elif isinstance(ignore_ids, str):
            ignore_ids = json.loads(ignore_ids)

        # Inefficient nested loop, but it should work well given the small number of roles
        for role in FindCheckOutEmployee.priority:
            for employee in employees.values():
                if (
                    (employee["store_id"] == store_id)
                    and (employee["role"] == role)
                    and (employee["employee_id"] not in ignore_ids)
                ):
                    payload = employee
                    out = json.dumps(payload, indent=2)
                    return out
        payload = {"error": "no suitable employee found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCheckOutEmployee",
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


class TransactionPriceInfo(Tool):
    """A tool for generating a price based on provided information, without performing any write operations. To complete the transaction, use make_transaction."""

    #TODO: consolidate logic into a common utility for make_transaction

    @staticmethod
    def get_detailed_line_item_price(data, **kwargs):
        pass
        sku = kwargs.get("sku")
        barcode = kwargs.get("barcode")
        kwargs.get("quantity", 1)

        if (sku is None) and (barcode is None):
            payload = {"error": "sku or barcode must be sent"}
            out = json.dumps(payload, indent=2)
            return out

        products = data.get("products", {}).values()
        promotions = data.get("promotions", {}).values()

        for product in products.values():
            if ((sku is not None) and (product["sku"] == sku)) or (
                (barcode is not None) and (product["barcode"] == barcode)
            ):
                #Obtain the sku if a barcode was applied
                sku = product["sku"]

                #Retrieve the promotional details
                for promotion in promotions.values():
                    if sku in promotion["applicable_skus"]:
                        break

                #Utilize the discount rate for products labeled as discountable; otherwise, set it to 0
                #if use_promotion["type"] is "percentage"
                discount_rate = (
                    product["discount_rate"] if product["is_discountable"] else 0.0
                )

                #Compute the discount amount
                #discount = round(product["price"] * discount_rate, 2)

                tax_rate = product["tax_rate"]
                payload = {
                        "sku": sku,
                        "unit_price": product["price"],
                        "discount_rate": discount_rate,
                        "tax_rate": tax_rate,
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": "product not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def invoke(data: dict[str, Any], timestamp: str = None, line_items: str = None) -> str:
        if isinstance(line_items, str):
            line_items = json.loads(line_items)

        if line_items is None:
            payload = {"error": "item_list must be sent"}
            out = json.dumps(payload)
            return out

        # Items appropriate for a transaction record
        line_items_list = []

        # Maintaining trackers for the total order
        total_amount = 0
        tax_amount = 0
        tax_rate = 0
        discount_total = 0
        for item in line_items:
            sku = item.get("sku")
            barcode = item.get("barcode")
            quantity = item.get("quantity")

            # Retrieve the pricing information for the item
            line_item_info = make_transaction.get_detailed_line_item_price(
                data, sku=sku, barcode=barcode
            )
            line_item_info = json.loads(line_item_info)

            # Extract values
            sku = line_item_info["sku"]
            unit_price = line_item_info["unit_price"]
            unit_tax_rate = line_item_info["tax_rate"]
            discount_rate = line_item_info["discount_rate"]

            # Compute totals for line items
            # TODO: further development needed for discount to accommodate various discount types
            unit_discount = unit_price * discount_rate
            item_sub_total = quantity * (unit_price - unit_discount)
            item_discount = round(quantity * unit_discount, 2)
            item_tax_amount = round(item_sub_total * unit_tax_rate, 2)
            item_final_amount = round(item_sub_total + item_tax_amount, 2)

            # Generate the transaction log for line items
            line_item = {
                "sku": sku,
                "quantity": quantity,
                "unit_price": unit_price,
                "discount": item_discount,
            }
            line_items_list.append(line_item)

            # Revise the cumulative totals
            total_amount += item_final_amount
            tax_amount += item_tax_amount
            discount_total += item_discount
            tax_rate = max(tax_rate, unit_tax_rate)

        # Construct the ultimate transaction log
        total_amount = round(total_amount, 2)
        tax_amount = round(tax_amount, 2)
        discount_total = round(discount_total, 2)
        transaction_row = {
            "total_amount": total_amount,
            "tax_amount": tax_amount,
            "tax_rate": tax_rate,
            "discount_total": discount_total,
            "line_items": line_items_list,
        }
        payload = transaction_row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TransactionPriceInfo",
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
        payload = transaction_row
        out = json.dumps(payload, indent=2)
        return out


class make_transaction(Tool):
    """Tool for managing purchases and refunds, adding records to transactions and updating stock as needed."""

    @staticmethod
    def get_detailed_line_item_price(data, **kwargs):
        pass
        sku = kwargs.get("sku")
        barcode = kwargs.get("barcode")
        kwargs.get("quantity", 1)

        if (sku is None) and (barcode is None):
            payload = {"error": "sku or barcode must be sent"}
            out = json.dumps(payload, indent=2)
            return out

        products = data.get("products", {}).values()
        promotions = data.get("promotions", {}).values()

        for product in products.values():
            if ((sku is not None) and (product["sku"] == sku)) or (
                (barcode is not None) and (product["barcode"] == barcode)
            ):
                #Fetch the sku if a barcode was utilized
                sku = product["sku"]

                #Acquire the promotional information
                for promotion in promotions.values():
                    if sku in promotion["applicable_skus"]:
                        break

                #Apply the discount rate for products identified as discountable; otherwise, set it to 0
                #if use_promotion["type"] equals "percentage"
                discount_rate = (
                    product["discount_rate"] if product["is_discountable"] else 0.0
                )

                #Assess the discount amount
                #discount = round(product["price"] * discount_rate, 2)

                tax_rate = product["tax_rate"]
                payload = {
                        "sku": sku,
                        "unit_price": product["price"],
                        "discount_rate": discount_rate,
                        "tax_rate": tax_rate,
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": "product not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def invoke(
        data: dict[str, Any],
        timestamp: str = None,
        store_id: str = None,
        employee_id: str = None,
        customer_id: str = None,
        line_items: str = None,
        payment_method: str = None,
        status: str = None,
        payment_amount: float = None,
        commit_transaction: bool = True
    ) -> str:
        if isinstance(line_items, str):
            item_list = json.loads(line_items)
        else:
            item_list = line_items

        if (
            (store_id is None)
            or (employee_id is None)
            or (customer_id is None)
            or (item_list is None)
        ):
            payload = {
                "error": "store_id, employee_id, customer_id and item_list must be sent"
            }
            out = json.dumps(payload)
            return out

        transactions = data.get("transactions", {}).values()

        # Items that are appropriate for a transaction record
        line_items = []

        # Tracking the overall order progress
        total_amount = 0
        tax_amount = 0
        tax_rate = 0
        discount_total = 0
        for item in item_list:
            sku = item.get("sku")
            barcode = item.get("barcode")
            quantity = item.get("quantity")

            # Obtain the pricing details for the item
            line_item_info = make_transaction.get_detailed_line_item_price(
                data, sku=sku, barcode=barcode
            )
            line_item_info = json.loads(line_item_info)

            # Extract the values
            sku = line_item_info["sku"]
            unit_price = line_item_info["unit_price"]
            unit_tax_rate = line_item_info["tax_rate"]
            discount_rate = line_item_info["discount_rate"]

            # Determine totals for line items
            # TODO: additional work required for discount to handle various discount types
            unit_discount = unit_price * discount_rate
            item_sub_total = quantity * (unit_price - unit_discount)
            item_discount = round(quantity * unit_discount, 2)
            item_tax_amount = round(item_sub_total * unit_tax_rate, 2)
            item_final_amount = round(item_sub_total + item_tax_amount, 2)

            # Establish the transaction log for line items
            line_item = {
                "sku": sku,
                "quantity": quantity,
                "unit_price": unit_price,
                "discount": item_discount,
            }
            line_items.append(line_item)

            # Adjust the ongoing totals
            total_amount += item_final_amount
            tax_amount += item_tax_amount
            discount_total += item_discount
            tax_rate = max(tax_rate, unit_tax_rate)

        # Verify adequate payment and compute change
        if (status == "completed") and (payment_amount < round(total_amount, 2)):
            if commit_transaction:
                payload = {
                    "error": "Amount paid is insufficient. Order total is: {}".format(
                        total_amount
                    )
                }
                out = json.dumps(payload)
                return out
            else:
                change_given = payment_amount
        else:
            change_given = round(payment_amount - total_amount, 2)

        # Compile the final transaction log

        # Retrieve the most recent transaction id and increase it by one
        transaction_id = (
            max([int(x["transaction_id"].split("-")[1]) for x in transactions.values()]) + 1
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

        # Insert into the database and return the item
        if commit_transaction:
            data["transactions"][transaction_id] = transaction_row
        payload = transaction_row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MakeTransaction",
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
                            "type": "number",
                            "description": "The amount given by the customer",
                        },
                        "status": {
                            "type": "string",
                            "description": "Signifies if the transaction is a purchase or a refund. (completed, refunded)",
                        },
                        "item_list": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string"},
                                    "barcode": {"type": "string"},
                                    "quantity": {"type": "integer"}
                                }
                            },
                            "description": "A list of items being purchased. Each item has either sku or barcode and a quantity.",
                        },
                        "commit_transaction": {
                            "type": "boolean",
                            "description": "If true, the transaction will be commited and processed. If false, the function will just do a dry run and return the transaction information. Defaults to True",
                        },
                    },
                },
            },
        }


class find_transaction(Tool):
    """Searches for and retrieves a transaction. If the transaction_id is known, it returns that specific row. If other parameters are provided, it searches for and returns all transactions that match those parameters."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        transaction_id: str = None,
        store_id: str = None,
        employee_id: str = None,
        customer_id: str = None,
        status: str = None,
        date: str = None
    ) -> str:
        transactions = data.get("transactions", {}).values()

        matches = []
        for transaction in transactions.values():
            # Utilize transaction_id if provided, prioritizing it over other parameters
            if (transaction_id is not None) and (
                transaction["transaction_id"] == transaction_id
            ):
                return transaction

            # If not, include in the matches list if any search parameters align
            else:
                # Retrieve matches
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

                # Assess if the row is a match
                # It must satisfy all provided criteria
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
        payload = matches
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindTransaction",
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
    def invoke(data: dict[str, Any], promotion_id: str = None) -> str:
        if promotion_id is None:
            payload = {"error": "promotion_id must be sent"}
            out = json.dumps(payload)
            return out

        promotions = data.get("promotions", {}).values()
        products = data.get("products", {}).values()

        for promotion in promotions.values():
            # Narrow down to the appropriate promotion
            if promotion["promotion_id"] == promotion_id:
                # Eliminate discounts from the products
                # TODO: investigate the possibility of multiple promotions for each product
                applicable_skus = promotion["applicable_skus"]
                for product in products.values():
                    if product["sku"] in applicable_skus:
                        product["is_discountable"] = False

                # TODO: consider if the row should simply be deleted?
                promotion["status"] = "canceled"
        payload = {"success": "complete"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CancelPromotion",
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
    def invoke(
        data: dict[str, Any],
        name: str,
        type: str,
        discount_value: float,
        description: str,
        applicable_skus: list[str],
        start_date: str,
        end_date: str,
        status: str,
        usage_limit: int
    ) -> str:
        promotion_fields_unpacked = {
            "name": name,
            "type": type,
            "discount_value": discount_value,
            "description": description,
            "applicable_skus": applicable_skus,
            "start_date": start_date,
            "end_date": end_date,
            "status": status,
            "usage_limit": usage_limit,
        }

        # Convert applicable_skus from json to a list if provided as json
        if isinstance(promotion_fields_unpacked["applicable_skus"], str):
            promotion_fields_unpacked["applicable_skus"] = json.loads(
                promotion_fields_unpacked["applicable_skus"]
            )

        promotions = data.get("promotions", {}).values()
        products = data.get("products", {}).values()

        promotion_id = (
            max([int(x["promotion_id"].split("-")[1]) for x in promotions.values()]) + 1
        )

        # TODO: automate status setting based on the start date
        promotion_row = {
            "promotion_id": f"PROMO-{promotion_id:03}",
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

        # Revise the skus
        for product in products.values():
            if product["sku"] in promotion_fields_unpacked["applicable_skus"]:
                product["is_discountable"] = True

                # TODO: will need to manage various discount types
                product["discount_rate"] = (
                    promotion_fields_unpacked["discount_value"] / 100.0
                )
        payload = {"success": "complete"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePromotion",
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
                            "type": "integer",
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
                            "type": "integer",
                            "description": "The number of times the sale can be used.",
                        },
                    },
                },
            },
        }


class find_promotions(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        promotion_id: str = None,
        type: str = None,
        status: str = None,
        name: str = None,
        description: str = None,
        has_sku: str = None
    ) -> str:
        promotions = data.get("promotions", {}).values()

        # If customer id is provided, it will take precedence over all other criteria

        # These columns will match precisely with the provided value
        exact_match_cols = ["type", "status"]
        exact_match_values = {"type": type, "status": status}

        # These columns will match as long as the database field includes the provided value
        approximate_match_cols = ["name", "description"]
        approximate_match_values = {"name": name, "description": description}

        # These columns possess unique matching criteria
        special_match_cols = ["has_sku"]
        special_match_values = {"has_sku": has_sku}

        matches = []
        for promotion in promotions.values():
            # customer_id is prioritized
            if (promotion_id is not None) and (
                promotion["promotion_id"] == promotion_id
            ):
                payload = promotion
                out = json.dumps(payload, indent=2)
                return out

            # Add to the return list if all provided criteria align
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
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindPromotions",
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
    def invoke(
        data: dict[str, Any],
        timestamp: str = None,
        name: str = None,
        phone_number: str = None,
        email: str = None,
        address: str = None,
        birthdate: str = None,
        loyalty_points: int = 0,
        membership_level: str = "basic",
        opt_in_marketing: bool = False,
    ) -> str:
        pass
        customers = data.get("customers", {}).values()

        # A timestamp must be included for database entries

        # These values are required to be sent
        required_cols = ["name", "phone_number", "email", "address", "birthdate"]

        # Default values apply if these are not provided
        optional_cols = ["loyalty_points", "membership_level", "opt_in_marketing"]

        required_values = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "address": address,
            "birthdate": birthdate,
        }
        optional_values = {
            "loyalty_points": loyalty_points,
            "membership_level": membership_level,
            "opt_in_marketing": opt_in_marketing,
        }

        # The function computes these values
        fill_in = {
            "customer_id": "CUST-5{customer_id:03}".format(
                customer_id=max(
                    [int(x["customer_id"].split("-")[1][1:]) for x in customers.values()]
                )
                + 1
            ),
            "created_at": timestamp,
            "updated_at": timestamp,
            "status": "active",
        }

        # Raise an error if any required values are absent
        if any([required_values[k] is None for k in required_values.keys()]):
            payload = {
                "error": "required values not sent: "
                + ", ".join(
                    [k for k in required_values.values() if required_values[k] is None]
                )
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # This indicates the sequence of items in the database
        # Although not essential due to the unordered nature of dictionaries, maintaining the same order can simplify validation
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

        # Arrange the items
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Insert into the database
        customers.append(json.dumps(row_final, indent=2))
        payload = row_final
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCustomer",
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
                            "type": "integer",
                            "description": "OPTIONAL. The number of loyalty points the customer has. This will normally be 0, but sometimes they can start with points as an incentive to create an account.",
                        },
                        "memebership_level": {
                            "type": "string",
                            "description": "OPTIONAL. The membership tier the customer is starting on. This will default to 'basic'.",
                        },
                        "opt_in_marketing": {
                            "type": "boolean",
                            "description": "OPTIONAL. If the customer is opting into marketing. This will default to False",
                        },
                    },
                },
            },
        }


class remove_customer(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str = None) -> str:
        customers = data.get("customers", {}).values()

        if customer_id is None:
            payload = {"error": "customer_id must be sent"}
            out = json.dumps(payload, indent=2)
            return out

        for customer in customers.values():
            if customer["customer_id"] == customer_id:
                del customer
                payload = {"success": f"Removed customer: {customer_id}"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": "No customer found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeCustomer",
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
    def invoke(
        data: dict[str, Any],
        customer_id: str = None,
        phone_number: str = None,
        membership_level: str = None,
        birthdate: str = None,
        opt_in_marketing: bool = None,
        status: str = None,
        name: str = None,
        email: str = None,
        address: str = None,
        birth_month: str = None,
        city: str = None,
    ) -> str:
        customers = data.get("customers", {}).values()

        # If a customer id is provided, it will supersede all other criteria

        # These columns will match exactly with the provided value
        exact_match_cols = [
            "phone_number",
            "membership_level",
            "birthdate",
            "opt_in_marketing",
            "status",
        ]
        exact_match_values = {
            "phone_number": phone_number,
            "membership_level": membership_level,
            "birthdate": birthdate,
            "opt_in_marketing": opt_in_marketing,
            "status": status,
        }

        # These columns will match as long as the database field has the provided value
        approximate_match_cols = ["name", "email", "address"]
        approximate_match_values = {
            "name": name,
            "email": email,
            "address": address,
        }

        # These columns have distinct matching criteria
        special_match_values = {
            "birth_month": birth_month,
            "city": city,
        }

        matches = []
        for customer in customers.values():
            # customer_id is given priority
            if (customer_id is not None) and (customer["customer_id"] == customer_id):
                payload = customer
                out = json.dumps(payload, indent=2)
                return out

            # Include in the return list if all provided criteria match
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
                            (
                                "-{}-".format(special_match_values["birth_month"])
                                in customer["birthdate"]
                            )
                            if special_match_values["birth_month"] is not None
                            else True
                        ),
                        (
                            (
                                special_match_values["city"].lower()
                                == customer["address"].split(",")[1].strip().lower()
                            )
                            if special_match_values["city"] is not None
                            else True
                        ),
                    ]
                )
            ):
                matches.append(customer)
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCustomers",
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
                            "type": "boolean",
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
                            "type": "integer",
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
    def invoke(
        data: dict[str, Any],
        customer_id: str = None,
        timestamp: str = None,
        name: str = None,
        phone_number: str = None,
        email: str = None,
        address: str = None,
        birthdate: str = None,
        membership_level: str = None,
        status: str = None,
        loyalty_points: int = None,
        opt_in_marketing: bool = None
    ) -> str:
        customers = data.get("customers", {}).values()

        # These parameters are essential for updates
        row_id = customer_id
        timestamp = timestamp

        if (row_id is None) or (timestamp is None):
            payload = {"error": "customer_id and timestamp must be sent"}
            out = json.dumps(payload)
            return out

        # These parameters are being submitted for the update
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
        updating_values = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "address": address,
            "birthdate": birthdate,
            "membership_level": membership_level,
            "status": status,
            "loyalty_points": loyalty_points,
            "opt_in_marketing": opt_in_marketing,
        }

        for customer in customers.values():
            if customer["customer_id"] == row_id:
                for col, value in updating_values.items():
                    # Revise any provided values
                    if value is not None:
                        customer[col] = value

                customer["updated_at"] = timestamp
                payload = customer
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "no matching records found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomer",
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
                            "type": "integer",
                            "description": "The number of loyalty points the customer has",
                        },
                        "memebership_level": {
                            "type": "string",
                            "description": "The membership tier of the customer",
                        },
                        "opt_in_marketing": {
                            "type": "boolean",
                            "description": "OPTIONAL. If the customer is opting into marketing",
                        },
                    },
                },
            },
        }


class create_employee(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        timestamp: str,
        name: str = None,
        phone_number: str = None,
        email: str = None,
        role: str = None,
        hire_date: str = None,
        store_id: str = None,
    ) -> str:
        employees = data.get("employees", {}).values()

        # A timestamp is required for database records

        # These values are required to be provided
        required_cols = [
            "name",
            "phone_number",
            "email",
            "role",
            "hire_date",
            "store_id",
        ]

        # Default values will apply if these are not provided
        optional_cols = []

        required_values = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "role": role,
            "hire_date": hire_date,
            "store_id": store_id,
        }
        optional_values = {}

        # The function calculates these values
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

        # Raise an error if any required values are missing
        if any([required_values[k] is None for k in required_values.keys()]):
            payload = {
                "error": "required values not sent: "
                + ", ".join(
                    [k for k in required_values.values() if required_values[k] is None]
                )
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # This represents the order of items in the database
        # While not crucial due to the unordered nature of dictionaries, having items in a consistent order can facilitate validation
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

        # Arrange the items
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Insert into the database
        employees.append(json.dumps(row_final, indent=2))
        payload = row_final
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createEmployee",
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
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        employees = data.get("employees", {}).values()

        if employee_id is None:
            payload = {"error": "employee_id must be sent"}
            out = json.dumps(payload, indent=2)
            return out

        for employee in employees.values():
            if employee["employee_id"] == employee_id:
                del employee
                payload = {"success": f"Removed employee: {employee_id}"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": "No employee found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveEmployee",
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
    def invoke(
        data: dict[str, Any],
        employee_id: str = None,
        phone_number: str = None,
        membership_level: str = None,
        birthdate: str = None,
        opt_in_marketing: bool = None,
        status: str = None,
        role: str = None,
        store_id: str = None,
        name: str = None,
        email: str = None,
        address: str = None,
    ) -> str:
        employees = data.get("employees", {}).values()

        # If a customer id is provided, it will take precedence over all other criteria

        # These columns will match precisely with the provided value
        exact_match_cols = [
            "phone_number",
            "membership_level",
            "birthdate",
            "opt_in_marketing",
            "status",
            "role",
            "store_id",
        ]
        exact_match_values = {
            "phone_number": phone_number,
            "membership_level": membership_level,
            "birthdate": birthdate,
            "opt_in_marketing": opt_in_marketing,
            "status": status,
            "role": role,
            "store_id": store_id,
        }

        # These columns will match as long as the database field includes the provided value
        approximate_match_cols = ["name", "email", "address"]
        approximate_match_values = {
            "name": name,
            "email": email,
            "address": address,
        }

        matches = []
        for employee in employees.values():
            # customer_id is prioritized
            if (employee_id is not None) and (employee["employee_id"] == employee_id):
                payload = employee
                out = json.dumps(payload, indent=2)
                return out

            # Add to the return list if all provided criteria align
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
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindEmployees",
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
    def invoke(
        data: dict[str, Any],
        employee_id: str = None,
        timestamp: str = None,
        name: str = None,
        phone_number: str = None,
        email: str = None,
        hire_date: str = None,
        status: str = None,
        role: str = None
    ) -> str:
        employees = data.get("employees", {}).values()

        # These parameters are essential for updates
        row_id = employee_id
        timestamp = timestamp

        if (row_id is None) or (timestamp is None):
            payload = {"error": "employee_id and timestamp must be sent"}
            out = json.dumps(payload)
            return out

        # These parameters are being submitted for the update
        updatable_cols = [
            "name",
            "phone_number",
            "email",
            "hire_date",
            "status",
            "role",
        ]
        updating_values = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "hire_date": hire_date,
            "status": status,
            "role": role
        }

        for employee in employees.values():
            if employee["employee_id"] == row_id:
                for col, value in updating_values.items():
                    # Revise any provided values
                    if value is not None:
                        employee[col] = value

                employee["updated_at"] = timestamp
                payload = employee
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "no matching records found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmployee",
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
    def invoke(
        data: dict[str, Any],
        sku: str = None,
        store_id: str = None,
        quantity: int = None,
        reserved_quantity: int = None,
        reorder_level: int = None,
        safety_stock: int = None,
        location: str = None,
        timestamp: str = None
    ) -> str:
        inventory = data.get("inventory", {}).values()

        # A timestamp is required for database records

        # These values are required to be sent
        required_cols = [
            "sku",
            "store_id",
            "quantity",
            "reserved_quantity",
            "reorder_level",
            "safety_stock",
            "location",
        ]

        # Default values will apply if these are not provided
        optional_cols = []

        required_values = {
            "sku": sku,
            "store_id": store_id,
            "quantity": quantity,
            "reserved_quantity": reserved_quantity,
            "reorder_level": reorder_level,
            "safety_stock": safety_stock,
            "location": location,
        }
        optional_values = {}

        # The function computes these values
        if required_values["quantity"] > required_values["reorder_level"]:
            status = "in_stock"
        elif required_values["quantity"] > required_values["safety_stock"]:
            status = "low_stock"
        else:
            status = "critical"
        fill_in = {
            "id": "INV-{inv_id:04}".format(
                inv_id=max([int(x["id"].split("-")[1][1:]) for x in inventory.values()]) + 1
            ),
            "created_at": timestamp,
            "updated_at": timestamp,
            "status": status,
            "last_stock_count": timestamp[:10],
        }

        # Raise an error if any required values are absent
        if any([required_values[k] is None for k in required_values.keys()]):
            payload = {
                "error": "required values not sent: "
                + ", ".join([k for k in required_values.values() if required_values[k] is None])
            }
            out = json.dumps(
                payload,
                indent=2,
            )
            return out

        # This indicates the sequence of items in the database
        # Although not essential due to the unordered nature of dictionaries, maintaining the same order can simplify validation
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

        # Arrange the items
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Insert into the database
        inventory.append(json.dumps(row_final, indent=2))
        payload = row_final
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createInventory",
                "description": "Adds a new inventory item to the store. This is for items the store has never stocked before, to update the quantity of an existing item, use UpdateStockQuantity",
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
                            "type": "integer",
                            "description": "The amount that the store starts with",
                        },
                        "reserved_quantity": {
                            "type": "integer",
                            "description": "The amount in reserve",
                        },
                        "reorder_level": {
                            "type": "integer",
                            "description": "The amount to start reordering products",
                        },
                        "safety_stock": {
                            "type": "integer",
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
    def invoke(data: dict[str, Any], inv_id: str = None) -> str:
        inventory = data.get("inventory", {}).values()

        if inv_id is None:
            payload = {"error": "inv_id must be sent"}
            out = json.dumps(payload, indent=2)
            return out

        for item in inventory.values():
            if item["id"] == inv_id:
                del item
                payload = {"success": f"Removed item: {inv_id}"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "No item found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeInventory",
                "description": "Removes an item from the store. This is for completely removing an item, to set to 0, use UpdateStockQuantity",
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
    def invoke(
        data: dict[str, Any],
        id: str = None,
        sku: str = None,
        store_id: str = None,
        status: str = None,
        last_stock_count: str = None,
        location: str = None
    ) -> str:
        inventory = data.get("inventory", {}).values()

        # These columns will match precisely with the provided value
        exact_match_cols = ["id", "sku", "store_id", "status", "last_stock_count"]
        exact_match_values = {
            "id": id,
            "sku": sku,
            "store_id": store_id,
            "status": status,
            "last_stock_count": last_stock_count
        }

        # These columns will match as long as the database field has the provided value
        approximate_match_cols = ["location"]
        approximate_match_values = {
            "location": location
        }

        matches = []
        for item in inventory.values():
            # Include in the return list if all provided criteria match
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
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindItems",
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
    def invoke(
        data: dict[str, Any],
        sku: str,
        name: str,
        category: str,
        price: float,
        description: str,
        supplier_id: int,
        weight_kg: float,
        dimensions_cm: str,
        brand: str,
        cost: float,
        barcode: str,
        tax_rate: float,
        timestamp: str = None,
        is_discountable: bool = False,
        status: str = "active",
        expiry_date: str = None,
        discount_rate: float = 0.0,
    ) -> str:
        products = data.get("products", {}).values()

        # A timestamp must be included for database entries

        # These values are required to be provided
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

        # Default values will apply if these are not provided
        optional_cols = ["is_discountable", "status", "expiry_date", "discount_rate"]

        required_values = {
            "sku": sku,
            "name": name,
            "category": category,
            "price": price,
            "description": description,
            "supplier_id": supplier_id,
            "weight_kg": weight_kg,
            "dimensions_cm": dimensions_cm,
            "brand": brand,
            "cost": cost,
            "barcode": barcode,
            "tax_rate": tax_rate,
        }
        optional_values = {
            "is_discountable": is_discountable,
            "status": status,
            "expiry_date": expiry_date,
            "discount_rate": discount_rate,
        }

        # The function computes these values
        fill_in = {"created_at": timestamp, "updated_at": timestamp}

        # Raise an error if any required values are missing
        if any([required_values[k] is None for k in required_values.keys()]):
            payload = {
                "error": "required values not sent: "
                + ", ".join([k for k in required_values.values() if required_values[k] is None])
            }
            out = json.dumps(
                payload,
                indent=2,
            )
            return out

        # This represents the order of items in the database
        # While not crucial due to the unordered nature of dictionaries, having items in a consistent order can facilitate validation
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

        # Arrange the items
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Insert into the database
        products.append(json.dumps(row_final, indent=2))
        payload = row_final
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateProduct",
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
                            "type": "number",
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
                            "type": "number",
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
                            "type": "number",
                            "description": "The cost the store pays for the product",
                        },
                        "barcode": {
                            "type": "string",
                            "description": "The barcode of the product",
                        },
                        "tax_rate": {
                            "type": "number",
                            "description": "The tax rate of the product",
                        },
                        "is_discountable": {
                            "type": "boolean",
                            "description": "OPTIONAL. If the product has an active discount. Ensure that the promotions table is updated with this information. Defaults to False",
                        },
                        "discount_rate": {
                            "type": "number",
                            "description": "OPTIONAL. The rate the product can be discounted at. Ensure that the promotions table is updated with this information. Defaults to 0",
                        },
                        "expiry_date": {
                            "type": "string",
                            "description": "OPTIONAL. If this product has an expiration. Defaults to None",
                        },
                        "status": {
                            "type": "string",
                            "enum": ["active", "inactive"],
                            "description": "OPTIONAL. Status of the product. Defaults to 'active'",
                        },
                    },
                },
            },
        }


class remove_product(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None) -> str:
        products = data.get("products", {}).values()

        if sku is None:
            payload = {"error": "sku must be sent"}
            out = json.dumps(payload, indent=2)
            return out

        for product in products.values():
            if product["sku"] == sku:
                del product
                payload = {"success": f"Removed product: {sku}"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "No sku found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveProduct",
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
    def invoke(
        data: dict[str, Any],
        sku: str = None,
        category: str = None,
        is_discountable: bool = None,
        supplier_id: int = None,
        brand: str = None,
        barcode: str = None,
        status: str = None,
        expiry_date: str = None,
        name: str = None,
        description: str = None,
        created_at: str = None,
        updated_at: str = None
    ) -> str:
        products = data.get("products", {}).values()

        # These columns will match precisely with the provided value
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
        exact_match_values = {
            "sku": sku,
            "category": category,
            "is_discountable": is_discountable,
            "supplier_id": supplier_id,
            "brand": brand,
            "barcode": barcode,
            "status": status,
            "expiry_date": expiry_date,
        }

        # These columns will match as long as the database field includes the provided value
        approximate_match_cols = ["name", "description", "created_at", "updated_at"]
        approximate_match_values = {
            "name": name,
            "description": description,
            "created_at": created_at,
            "updated_at": updated_at,
        }

        matches = []
        for product in products.values():
            # Add to the return list if all provided criteria align
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
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindProducts",
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
                            "type": "boolean",
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
    def GetDetailedItemPrice(data, **kwargs):
        pass
        sku = kwargs.get("sku")
        barcode = kwargs.get("barcode")

        if (sku is None) and (barcode is None):
            payload = {"error": "sku or barcode must be sent"}
            out = json.dumps(payload, indent=2)
            return out

        products = data.get("products", {}).values()

        for product in products.values():
            if ((sku is not None) and (product["sku"] == sku)) or (
                (barcode is not None) and (product["barcode"] == barcode)
            ):
                #Retrieve the sku if a barcode was utilized
                sku = product["sku"]

                #Apply the discount rate for discountable products; otherwise, assign 0
                discount_rate = (
                    product["discount_rate"] if product["is_discountable"] else 0.0
                )

                #Determine the discount value
                #discount = round(product["price"] * discount_rate, 2)

                tax_rate = product["tax_rate"]
                payload = {
                        "sku": sku,
                        "unit_price": product["price"],
                        "discount_rate": discount_rate,
                        "tax_rate": tax_rate,
                        "cost": product["cost"],
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"error": "product not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def invoke(data: dict[str, Any], sku_list: str = None, ignore_discounts: bool = True) -> str:
        pass
        data.get("products", {}).values()

        if isinstance(sku_list, str):
            sku_list = json.loads(sku_list)

        if sku_list is None:
            payload = {"error": "sku_list must be sent"}
            out = json.dumps(payload, indent=2)
            return out

        out = []
        for sku in sku_list:
            # Retrieve the pricing information for the item
            line_item_info = get_profit_margins.GetDetailedItemPrice(data, sku=sku)
            line_item_info = json.loads(line_item_info)

            # Extract values
            sku = line_item_info["sku"]
            unit_price = line_item_info["unit_price"]
            unit_tax_rate = line_item_info["tax_rate"]
            discount_rate = line_item_info["discount_rate"]
            cost = line_item_info["cost"]

            # Compute totals for line items
            # TODO: further development needed for discount to accommodate various discount types
            unit_discount = unit_price * discount_rate
            item_sub_total = unit_price - unit_discount
            round(unit_discount, 2)
            item_tax_amount = round(item_sub_total * unit_tax_rate, 2)
            round(item_sub_total + item_tax_amount, 2)

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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProfitMargins",
                "description": "Gets the per unit profit margins for items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku_list": {
                            "type": "string",
                            "description": "A json list of the skus to get the profit margins for",
                        },
                        "ignore_discounts": {
                            "type": "boolean",
                            "description": "OPTIONAL. To calculate profits on the discounted total or not. Defaults to True",
                        },
                    },
                },
            },
        }


class get_top_selling_items(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], n_values: int = None, store_id: str = None, payment_method: str = None, customer_id: str = None) -> str:
        transactions = data.get("transactions", {}).values()

        filter_cols = ["store_id", "payment_method", "customer_id"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}
        filter_values = {k: params_dict.get(k) for k in filter_cols if params_dict.get(k) is not None}

        item_tracker = defaultdict(int)
        for transaction in transactions.values():
            # Apply filters based on any provided values
            if all([filter_values[k] == transaction[k] for k in filter_values.keys()]):
                line_items = transaction["line_items"]
                for item in line_items:
                    item_tracker[item["sku"]] += item["quantity"]

        out = OrderedDict()

        # Arrange the values by total and retrieve the top n items
        sort = sorted(item_tracker, key=item_tracker.get, reverse=True)
        if n_values is not None:
            sort = sort[:n_values]
        for sku in sort:
            out[sku] = item_tracker[sku]
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTopSellingItems",
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
    FindDiscountableProducts(),
    UpdateStockQuantity(),
    CheckLowStockItems(),
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
    FindCheckOutEmployee(),
    TransactionPriceInfo(),
    GetDetailedItemPrice(),
]
