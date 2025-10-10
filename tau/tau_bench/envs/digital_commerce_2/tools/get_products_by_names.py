# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductsByNames(Tool):
    """Fetch multiple products' full details by exact names (batch)."""

    @staticmethod
    def invoke(data: Dict[str, Any], names: Any) -> str:
        names = names
        if not names or not isinstance(names, list):
            return json.dumps(
                {"error": "Missing or invalid 'names'. Expected a list of product names."}, indent=2
            )
        products = list(data.get("products", {}).values())
        results: List[Dict[str, Any]] = []
        for n in names:
            match = next((p for p in products if p.get("name") == n), None)
            results.append(match if match else {"name": n, "error": "Product not found"})
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_products_by_names",
                "description": "Fetch multiple products by their exact names.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "names": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of product names to fetch.",
                        }
                    },
                    "required": ["names"],
                },
            },
        }
