# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class find_products(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        products = list(data.get("products", {}).values())

        # These columns will correspond precisely to the provided value.
        exact_match_cols = [
            "sku",
            "category",
            "is_discountable",
            "supplier_id",
            "brand",
            "barcode",
            "status",
            "expiry_date",
        ]
        exact_match_values = {k: kwargs.get(k) for k in exact_match_cols}

        # The columns will align as long as the database field includes the provided value.
        approximate_match_cols = ["name", "description", "created_at", "updated_at"]
        approximate_match_values = {k: kwargs.get(k) for k in approximate_match_cols}

        matches = []
        for product in products:
            # If all specified criteria are satisfied, include it in the return list.
            if all(
                [
                    exact_match_values[k] == product[k]
                    for k in exact_match_values.keys()
                    if exact_match_values[k] is not None
                ]
            ) and all(
                [
                    approximate_match_values[k].lower() in product[k].lower()
                    for k in approximate_match_values.keys()
                    if approximate_match_values[k] is not None
                ]
            ):
                matches.append(product)

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_products",
                "description": "Finds products matching the sent criteria. Returns an empty list if there are none",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The sku of the item. Will do an exact match",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category of the item. Will do an exact match",
                        },
                        "is_discountable": {
                            "type": "boolean",
                            "description": "If the product can be discounted. Will do an exact match",
                        },
                        "supplier_id": {
                            "type": "string",
                            "description": "The supplier_id of the product. Will do an exact match",
                        },
                        "brand": {
                            "type": "string",
                            "description": "The brand of the item. Will do an exact match",
                        },
                        "barcode": {
                            "type": "string",
                            "description": "The barcode of the product. Will do an exact match",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the product. Will do an exact match",
                        },
                        "expiry_date": {
                            "type": "string",
                            "description": "The expiry_date of the product. Will do an exact match",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the product. Will do a approximate match",
                        },
                        "description": {
                            "type": "string",
                            "description": "The description of the product. Will do a approximate match",
                        },
                        "created_at": {
                            "type": "string",
                            "description": "The timestamp the product was created at. Will do a approximate match",
                        },
                        "updated_at": {
                            "type": "string",
                            "description": "The timestamp the product was last updated. Will do a approximate match",
                        },
                    },
                },
            },
        }
