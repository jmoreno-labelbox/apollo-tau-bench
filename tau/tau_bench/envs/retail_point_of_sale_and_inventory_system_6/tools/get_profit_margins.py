from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
                            "type": \"boolean\",
                            "description": "OPTIONAL. To calculate profits on the discounted total or not. Defaults to True",
                        },
                    },
                },
            },
        }
