from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateProductDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str, name: str = None, price: float = None, description: str = None,
    is_discountable: Any = None,
    category: Any = None,
    status: Any = None,
    ) -> str:
        products = data.get("products", [])
        updated_product = None
        for product in products:
            if product.get("sku") == sku:
                if name is not None:
                    product["name"] = name
                if price is not None:
                    product["price"] = price
                if description is not None:
                    product["description"] = description
                updated_product = product
                break
        payload = {"updated_product": updated_product}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProductDetails",
                "description": "Updates various details of an existing product by SKU. Can update 'status', 'is_discountable', 'price', etc.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to update.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The new name of the product.",
                        },
                        "category": {
                            "type": "string",
                            "description": "The new category of the product.",
                        },
                        "price": {
                            "type": "number",
                            "format": "float",
                            "description": "The new price of the product.",
                        },
                        "is_discountable": {
                            "type": "boolean",
                            "description": "New discountability status.",
                        },
                        "description": {
                            "type": "string",
                            "description": "A new description for the product.",
                        },
                        "supplier_id": {
                            "type": "string",
                            "description": "The new supplier ID.",
                        },
                        "weight_kg": {
                            "type": "number",
                            "format": "float",
                            "description": "The new weight in kg.",
                        },
                        "dimensions_cm": {
                            "type": "string",
                            "description": "The new dimensions (LxWxH).",
                        },
                        "brand": {
                            "type": "string",
                            "description": "The new brand of the product.",
                        },
                        "cost": {
                            "type": "number",
                            "format": "float",
                            "description": "The new cost of the product.",
                        },
                        "barcode": {
                            "type": "string",
                            "description": "The new barcode.",
                        },
                        "tax_rate": {
                            "type": "number",
                            "format": "float",
                            "description": "The new tax rate.",
                        },
                        "discount_rate": {
                            "type": "number",
                            "format": "float",
                            "description": "The new default discount rate.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status of the product (e.g., 'active', 'discontinued', 'clearance', 'limited_availability').",
                        },
                        "expiry_date": {
                            "type": ["string", "null"],
                            "format": "date",
                            "description": "The new expiry date (YYYY-MM-DD), or null.",
                        },
                    },
                    "required": ["sku"],
                },
            },
        }
