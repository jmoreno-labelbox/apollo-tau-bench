from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateProduct(Tool):
    """Utility for modifying product information."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, updates: dict[str, Any] = None) -> str:
        products = data.get("product_master", {}).values()

        for product in products.values():
            if product["sku"] == sku:
                product.update(updates)
                payload = {"success": f"product {sku} updated"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"sku {sku} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProduct",
                "description": "Update product by SKU",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "The SKU to update"},
                        "updates": {
                            "type": "object",
                            "description": "Fields and values to update",
                        },
                    },
                    "required": ["sku", "updates"],
                },
            },
        }
