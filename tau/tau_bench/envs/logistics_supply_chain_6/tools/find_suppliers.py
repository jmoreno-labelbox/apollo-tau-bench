# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindSuppliers(Tool):
    """Tool to find suppliers by the category of products they supply."""

    @staticmethod
    def invoke(data: Dict[str, Any], product_categories: List) -> str:
        """Execute the tool with given parameters."""
        suppliers = data.get("supplier_master", [])
        results = [
            supplier for supplier in suppliers
            if set(product_categories).issubset(supplier.get("product_categories", []))
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "find_suppliers",
                "description": "Finds suppliers that provide products in a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_categories": {"type": "array", "items": {"type": "string"}, "description": "The product categories to search for (e.g., 'Electronics', 'Apparel')."}
                    },
                    "required": ["product_categories"],
                },
            },
        }
