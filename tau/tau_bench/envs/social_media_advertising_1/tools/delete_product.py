from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DeleteProduct(Tool):
    """Removes a product."""

    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None) -> str:
        if not product_id:
            payload = {"error": "product_id is a required parameter."}
            out = json.dumps(payload)
            return out

        products = data.get("dim_product", {}).values()
        for product in products.values():
            if product.get("product_id") == product_id:
                data["dim_product"] = [
                    d for d in data["dim_product"].values() if d["product_id"] != product_id
                ]
                payload = {
                    "status": "success",
                    "message": f"Product with id {product_id} deleted successfully",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Product with ID '{product_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteProduct",
                "description": "Deletes a product.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {
                            "type": "string",
                            "description": "The unique ID of the product to delete.",
                        },
                    },
                    "required": ["product_id"],
                },
            },
        }
