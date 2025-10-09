from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddNewProduct(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        name: str,
        description: str,
        category: str,
        price: float,
        stock_quantity: int
    ) -> str:
        products = data.get("products", {}).values()
        category_prefix = category[:4].upper()
        product_num = (
            len(
                [
                    p
                    for p in products.values() if p.get("category", "").upper() == category.upper()
                ]
            )
            + 1
        )
        sku = f"{category_prefix}-{product_num:04d}"

        new_product = {
            "sku": sku,
            "name": name,
            "description": description,
            "category": category,
            "price": price,
        }

        data["products"][new_product["product_id"]] = new_product
        data["products"] = products
        payload = new_product
        out = json.dumps(payload, indent=2)
        return out
        pass
        products = data.get("products", {}).values()
        category_prefix = category[:4].upper()
        product_num = (
            len(
                [
                    p
                    for p in products.values() if p.get("category", "").upper() == category.upper()
                ]
            )
            + 1
        )
        sku = f"{category_prefix}-{product_num:04d}"

        new_product = {
            "sku": sku,
            "name": name,
            "description": description,
            "category": category,
            "price": price,
        }

        data["products"][new_product["product_id"]] = new_product
        data["products"] = products
        payload = new_product
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddNewProduct",
                "description": "Add a new product to the inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Product name."},
                        "description": {
                            "type": "string",
                            "description": "Product description.",
                        },
                        "category": {
                            "type": "string",
                            "description": "Product category.",
                        },
                        "price": {"type": "number", "description": "Product price."},
                        "stock_quantity": {
                            "type": "integer",
                            "description": "Initial stock quantity.",
                        },
                    },
                    "required": [
                        "name",
                        "description",
                        "category",
                        "price",
                        "stock_quantity",
                    ],
                },
            },
        }
