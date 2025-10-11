# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class make_transaction(Tool):
    """
    Tool for handling a purchases and refunds. Adds the record to the transactions and updates the stock if necessary
    """

    @staticmethod
    def get_detailed_line_item_price(data, barcode, sku, quantity = 1):

        if (sku is None) and (barcode is None):
            return json.dumps({"error": "sku or barcode must be sent"}, indent=2)

        products = list(data.get("products", {}).values())
        promotions = data.get("promotions", [])

        for product in products:
            if ((sku is not None) and (product["sku"] == sku)) or (
                (barcode is not None) and (product["barcode"] == barcode)
            ):
                # Retrieve the SKU if a barcode was utilized.
                sku = product["sku"]

                # Retrieve the details of the promotion.
                for promotion in promotions:
                    if sku in promotion["applicable_skus"]:
                        use_promotion = promotion
                        break

                # Apply the discount rate if the product is eligible for discounts; otherwise, assign a value of 0.
                # if use_promotion["type"] == "percent"
                discount_rate = (
                    product["discount_rate"] if product["is_discountable"] else 0.0
                )

                # Compute the discount value.
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
    def invoke(data: Dict[str, Any], customer_id, employee_id, line_items, payment_amount, payment_method, status, store_id, timestamp, commit_transaction = True) -> str:
        item_list = line_items
        if isinstance(item_list, str):
            item_list = json.loads(item_list)
        amount_paid = payment_amount

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

        transactions = list(data.get("transactions", {}).values())

        # Items appropriate for a transaction log
        line_items = []

        # Executing monitors for the total order.
        total_amount = 0
        tax_amount = 0
        tax_rate = 0
        discount_total = 0
        for item in item_list:
            sku = item.get("sku")
            barcode = item.get("barcode")
            quantity = item.get("quantity")

            # Retrieve the pricing details for the item.
            line_item_info = make_transaction.get_detailed_line_item_price(
                data, sku=sku, barcode=barcode
            )
            line_item_info = json.loads(line_item_info)

            # Extract values
            sku = line_item_info["sku"]
            unit_price = line_item_info["unit_price"]
            unit_tax_rate = line_item_info["tax_rate"]
            discount_rate = line_item_info["discount_rate"]

            # Compute totals for each line item.
            # TODO: enhance discount logic to handle various discount types.
            unit_discount = unit_price * discount_rate
            item_sub_total = quantity * (unit_price - unit_discount)
            item_discount = round(quantity * unit_discount, 2)
            item_tax_amount = round(item_sub_total * unit_tax_rate, 2)
            item_final_amount = round(item_sub_total + item_tax_amount, 2)

            # Generate the transaction log for line items.
            line_item = {
                "sku": sku,
                "quantity": quantity,
                "unit_price": unit_price,
                "discount": item_discount,
            }
            line_items.append(line_item)

            # Refresh the cumulative totals.
            total_amount += item_final_amount
            tax_amount += item_tax_amount
            discount_total += item_discount
            tax_rate = max(tax_rate, unit_tax_rate)

        # Verify adequate payment and compute the change.
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

        # Construct the conclusive transaction log.

        # Retrieve the most recent transaction ID and add one to it.
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
        # transaction_row = json.dumps(transaction_row, indent=2)

        # Insert into the database and retrieve the item.
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
                            "type": "boolean",
                            "description": "If true, the transaction will be commited and processed. If false, the function will just do a dry run and return the transaction information. Defaults to True",
                        },
                    },
                },
            },
        }
