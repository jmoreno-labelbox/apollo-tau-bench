# Sierra copyright notice.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_profit_margins(Tool):
    @staticmethod
    def get_detailed_item_price(data, **kwargs):
        sku = kwargs.get("sku")
        barcode = kwargs.get("barcode")

        if (sku is None) and (barcode is None):
            return json.dumps({"error": "sku or barcode must be sent"}, indent=2)

        products = list(data.get("products", {}).values())

        for product in products:
            if ((sku is not None) and (product["sku"] == sku)) or (
                (barcode is not None) and (product["barcode"] == barcode)
            ):
                # Retrieve the SKU if a barcode was utilized.
                sku = product["sku"]

                # Apply the discount rate for discountable products; otherwise, assign 0.
                discount_rate = (
                    product["discount_rate"] if product["is_discountable"] else 0.0
                )

                # Compute the amount of the discount.
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
        products = list(data.get("products", {}).values())

        sku_list = kwargs.get("sku_list")
        if isinstance(sku_list, str):
            sku_list = json.loads(sku_list)
        ignore_discounts = kwargs.get("ignore_discounts", True)

        if sku_list is None:
            return json.dumps({"error": "sku_list must be sent"}, indent=2)

        out = []
        for sku in sku_list:
            # Retrieve the pricing details for the item.
            line_item_info = get_profit_margins.get_detailed_item_price(data, sku=sku)
            line_item_info = json.loads(line_item_info)

            # Extract values
            sku = line_item_info["sku"]
            unit_price = line_item_info["unit_price"]
            unit_tax_rate = line_item_info["tax_rate"]
            discount_rate = line_item_info["discount_rate"]
            cost = line_item_info["cost"]

            # Compute totals for each line item.
            # TODO: enhance discount implementation to handle various discount types.
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
                            "type": "boolean",
                            "description": "OPTIONAL. To calculate profits on the discounted total or not. Defaults to True",
                        },
                    },
                },
            },
        }
