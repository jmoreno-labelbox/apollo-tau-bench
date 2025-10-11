# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_detailed_item_price(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        sku = data.get("sku")
        barcode = data.get("barcode")
        # quantity = data.get("quantity", default=1)

        if (sku is None) and (barcode is None):
            return json.dumps({"error": "sku or barcode must be sent"}, indent=2)

        products = list(data.get("products", {}).values())

        for product in products:
            if ((sku is not None) and (product["sku"] == sku)) or (
                (barcode is not None) and (product["barcode"] == barcode)
            ):
                # Retrieve the SKU if a barcode was provided.
                sku = product["sku"]

                # Apply the discount rate when the product is designated as discountable; otherwise, set it to 0.
                discount_rate = (
                    product["discount_rate"] if product["is_discountable"] else 0.0
                )

                # Determine the amount of the discount.
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
                        # "quantity": {"type": "integer", "description": "The number of items being bought"}
                    },
                },
            },
        }
