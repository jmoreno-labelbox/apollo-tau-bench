from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindProducts(Tool):
    """Utility for locating products according to specified criteria."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        category: str | None = None,
        subcategory: str | None = None,
        brand: str | None = None
    ) -> str:
        """Run the tool with the provided parameters."""
        products = data.get("product_master", {}).values()
        results = []
        for product in products.values():
            if (
                (not category or product.get("category") == category)
                and (not subcategory or product.get("subcategory") == subcategory)
                and (not brand or product.get("brand") == brand)
            ):
                results.append(product)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
        """Run the tool with the provided parameters."""
        pass
        products = data.get("product_master", {}).values()
        results = []
        for product in products.values():
            if (
                (not category or product.get("category") == category)
                and (not subcategory or product.get("subcategory") == subcategory)
                and (not brand or product.get("brand") == brand)
            ):
                results.append(product)
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "findProducts",
                "description": "Finds products based on category, subcategory, or brand.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The product category.",
                        },
                        "subcategory": {
                            "type": "string",
                            "description": "The product subcategory.",
                        },
                        "brand": {
                            "type": "string",
                            "description": "The product brand.",
                        },
                    },
                },
            },
        }
