from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



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
