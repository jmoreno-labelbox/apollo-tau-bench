# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateProductDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku) -> str:
        products = list(data.get("products", {}).values())
        updated_product = None
        for product in products:
            if product.get("sku") == sku:
                for key, value in kwargs.items():
                    if key != 'sku':
                        product[key] = value
                updated_product = product
                break
        return json.dumps({"updated_product": updated_product})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_product_details",
                "description": "Updates various details of an existing product by SKU. Can update 'status', 'is_discountable', 'price', etc.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to update.",
                        },
                        "name": {"type": "string", "description": "The new name of the product."},
                        "category": {"type": "string", "description": "The new category of the product."},
                        "price": {"type": "number", "format": "float", "description": "The new price of the product."},
                        "is_discountable": {"type": "boolean", "description": "New discountability status."},
                        "description": {"type": "string", "description": "A new description for the product."},
                        "supplier_id": {"type": "string", "description": "The new supplier ID."},
                        "weight_kg": {"type": "number", "format": "float", "description": "The new weight in kg."},
                        "dimensions_cm": {"type": "string", "description": "The new dimensions (LxWxH)."},
                        "brand": {"type": "string", "description": "The new brand of the product."},
                        "cost": {"type": "number", "format": "float", "description": "The new cost of the product."},
                        "barcode": {"type": "string", "description": "The new barcode."},
                        "tax_rate": {"type": "number", "format": "float", "description": "The new tax rate."},
                        "discount_rate": {"type": "number", "format": "float", "description": "The new default discount rate."},
                        "status": {"type": "string", "description": "The new status of the product (e.g., 'active', 'discontinued', 'clearance', 'limited_availability')."},
                        "expiry_date": {"type": ["string", "null"], "format": "date", "description": "The new expiry date (YYYY-MM-DD), or null."}                    },
                    "required": ["sku"],
                },
            },
        }
