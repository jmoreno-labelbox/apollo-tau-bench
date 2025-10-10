# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddNewProduct(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name: str, description: str, category: str, price: float, stock_quantity: int) -> str:
        products = list(data.get("products", {}).values())
        category_prefix = category[:4].upper()
        product_num = len([p for p in products if p.get("category", "").upper() == category.upper()]) + 1
        sku = f"{category_prefix}-{product_num:04d}"

        new_product = {
            "sku": sku,
            "name": name,
            "description": description,
            "category": category,
            "price": price
        }

        products.append(new_product)
        data["products"][product_id] = new_product
        return json.dumps(new_product, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_new_product",
                "description": "Add a new product to the inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Product name."},
                        "description": {"type": "string", "description": "Product description."},
                        "category": {"type": "string", "description": "Product category."},
                        "price": {"type": "number", "description": "Product price."},
                        "stock_quantity": {"type": "integer", "description": "Initial stock quantity."}
                    },
                    "required": ["name", "description", "category", "price", "stock_quantity"]
                }
            }
        }
