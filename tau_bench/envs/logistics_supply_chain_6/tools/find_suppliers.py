from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindSuppliers(Tool):
    """Utility for locating suppliers based on the types of products they provide."""

    @staticmethod
    def invoke(data: dict[str, Any], product_categories: list, supplier_master: list = None) -> str:
        """Run the tool using the specified parameters."""
        suppliers = supplier_master if supplier_master is not None else []
        results = [
            supplier
            for supplier in suppliers
            if set(product_categories).issubset(supplier.get("product_categories", []))
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindSuppliers",
                "description": "Finds suppliers that provide products in a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_categories": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "The product categories to search for (e.g., 'Electronics', 'Apparel').",
                        }
                    },
                    "required": ["product_categories"],
                },
            },
        }
