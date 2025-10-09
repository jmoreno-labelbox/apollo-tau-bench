from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetProductBySku(Tool):
    """Utility for retrieving product information using SKU."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str) -> str:
        """Run the tool using the specified parameters."""
        products = data.get("product_master", [])
        for product in products:
            if product.get("sku") == sku:
                payload = product
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Product with SKU {sku} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetProductBySku",
                "description": "Retrieves detailed information about a specific product using its SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The Stock Keeping Unit (SKU) of the product to find.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }
