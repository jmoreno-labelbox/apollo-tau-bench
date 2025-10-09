from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateVariantAvailability(Tool):
    """Modify the 'available' status of a variant."""

    @staticmethod
    def invoke(
        data: dict[str, Any], product_id: str, item_id: str, available: bool
    ) -> str:
        products = data.get("products", [])
        for product in products:
            if product.get("product_id") == product_id:
                variants = product.get("variants", {})
                if item_id in variants:
                    variants[item_id]["available"] = available
                    payload = {
                        "status": "success",
                        "product_id": product_id,
                        "item_id": item_id,
                        "available": available,
                    }
                    out = json.dumps(payload)
                    return out
                payload = {
                    "error": "Variant not found",
                    "product_id": product_id,
                    "item_id": item_id,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Product not found", "product_id": product_id}
        out = json.dumps(payload)
        return out
        pass
        products = data.get("products", [])
        for product in products:
            if product.get("product_id") == product_id:
                variants = product.get("variants", {})
                if item_id in variants:
                    variants[item_id]["available"] = available
                    payload = {
                            "status": "success",
                            "product_id": product_id,
                            "item_id": item_id,
                            "available": available,
                        }
                    out = json.dumps(
                        payload)
                    return out
                payload = {
                        "error": "Variant not found",
                        "product_id": product_id,
                        "item_id": item_id,
                    }
                out = json.dumps(
                    payload)
                return out
        payload = {"error": "Product not found", "product_id": product_id}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateVariantAvailability",
                "description": "Update the 'available' flag for a variant within a product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "available": {"type": "boolean"},
                    },
                    "required": ["product_id", "item_id", "available"],
                },
            },
        }
