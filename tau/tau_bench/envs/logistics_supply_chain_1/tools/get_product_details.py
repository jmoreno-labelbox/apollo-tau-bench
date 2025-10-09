from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetProductDetails(Tool):
    """A utility for fetching all master data related to a specific product by its name."""

    @staticmethod
    def invoke(data: dict[str, Any], product_name: str = None) -> str:
        if not product_name:
            payload = {"error": "product_name is a required argument."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        product_master = data.get("product_master", [])
        product = next(
            (p for p in product_master if p.get("product_name") == product_name), None
        )
        if product:
            payload = product
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"Product '{product_name}' not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductDetails",
                "description": "Retrieves all master data for a specific product by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_name": {
                            "type": "string",
                            "description": "The full, exact name of the product to search for.",
                        }
                    },
                    "required": ["product_name"],
                },
            },
        }
