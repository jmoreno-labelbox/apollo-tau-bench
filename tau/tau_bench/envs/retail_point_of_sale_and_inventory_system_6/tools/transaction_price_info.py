from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
