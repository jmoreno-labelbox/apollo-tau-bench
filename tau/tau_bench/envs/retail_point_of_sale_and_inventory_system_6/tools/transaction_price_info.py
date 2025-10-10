# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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

        products = list(data.get("products", {}).values())
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
