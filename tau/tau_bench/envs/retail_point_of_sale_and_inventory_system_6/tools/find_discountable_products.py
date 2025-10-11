# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class find_discountable_products(Tool):
    """
    Tool to search for all products that can be discounted
    """

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id) -> str:

        products = list(data.get("products", {}).values())

        out = []

        for product in products:
            # Include only products from the specified supplier if supplier_id is provided.
            if (supplier_id is None) or (product["supplier_id"] == supplier_id):
                # Select products eligible for discounts and include them in the return list.
                if product["is_discountable"]:
                    out.append(product["name"])

        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_discountable_products",
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
