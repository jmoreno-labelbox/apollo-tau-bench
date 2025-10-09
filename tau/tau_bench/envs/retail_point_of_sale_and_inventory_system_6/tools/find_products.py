from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class find_products(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sku: str = None,
        category: str = None,
        is_discountable: bool = None,
        supplier_id: int = None,
        brand: str = None,
        barcode: str = None,
        status: str = None,
        expiry_date: str = None,
        name: str = None,
        description: str = None,
        created_at: str = None,
        updated_at: str = None
    ) -> str:
        products = data.get("products", {}).values()

        # These columns will match precisely with the provided value
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
        exact_match_values = {
            "sku": sku,
            "category": category,
            "is_discountable": is_discountable,
            "supplier_id": supplier_id,
            "brand": brand,
            "barcode": barcode,
            "status": status,
            "expiry_date": expiry_date,
        }

        # These columns will match as long as the database field includes the provided value
        approximate_match_cols = ["name", "description", "created_at", "updated_at"]
        approximate_match_values = {
            "name": name,
            "description": description,
            "created_at": created_at,
            "updated_at": updated_at,
        }

        matches = []
        for product in products.values():
            # Add to the return list if all provided criteria align
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
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindProducts",
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
                            "type": \"boolean\",
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
