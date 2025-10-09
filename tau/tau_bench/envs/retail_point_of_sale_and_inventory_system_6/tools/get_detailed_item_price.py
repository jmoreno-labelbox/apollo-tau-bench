from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

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
