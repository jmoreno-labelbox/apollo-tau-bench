from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
                            "type": "string",
                            "description": "A list of items being purchased. This should be a json object with a structure like so: [{'sku' : XXX, 'quantity' : 1}, {'barcode' : YYY, 'quantity' : 2}]",
                        },
                        "commit_transaction": {
                            "type": \"boolean\",
                            "description": "If true, the transaction will be commited and processed. If false, the function will just do a dry run and return the transaction information. Defaults to True",
                        },
                    },
                },
            },
        }
