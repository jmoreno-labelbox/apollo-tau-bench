# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddStockQuantities(Tool):
    """Batch increase stock quantities for multiple products (returns, cancellations)."""

    @staticmethod
    def invoke(data: Dict[str, Any], items: Any) -> str:
        if not isinstance(items, list) or not items:
            return json.dumps(
                {
                    "error": "Missing or invalid 'items'. Expected list of {product_id, quantity_to_add}."
                },
                indent=2,
            )

        products = list(data.get("products", {}).values())
        results = []
        for it in items:
            pid = it.get("product_id")
            qty = it.get("quantity_to_add")
            if not pid or qty is None:
                return json.dumps(
                    {"error": "Each item must include product_id and quantity_to_add"}, indent=2
                )

            prod = next((p for p in products if p.get("product_id") == pid), None)
            if not prod:
                results.append({"product_id": pid, "error": "Product not found"})
                continue

            try:
                prod["stock_quantity"] = int(prod.get("stock_quantity", 0)) + int(qty)
            except (TypeError, ValueError):
                return json.dumps({"error": "quantity_to_add must be an integer"}, indent=2)

            results.append({"product_id": pid, "stock_quantity": prod["stock_quantity"]})

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_stock_quantities",
                "description": "Batch increase stock quantities for multiple products.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "quantity_to_add": {"type": "integer"},
                                },
                                "required": ["product_id", "quantity_to_add"],
                            },
                        }
                    },
                    "required": ["items"],
                },
            },
        }
