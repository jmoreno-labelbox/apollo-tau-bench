from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddStockQuantities(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], items: list[dict[str, Any]]) -> str:
        if not isinstance(items, list) or not items:
            payload = {
                "error": "Missing or invalid 'items'. Expected list of {product_id, quantity_to_add}."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        products = data.get("products", {}).values()
        results = []
        for it in items:
            pid = it.get("product_id")
            qty = it.get("quantity_to_add")
            if not pid or qty is None:
                payload = {"error": "Each item must include product_id and quantity_to_add"}
                out = json.dumps(
                    payload, indent=2,
                )
                return out

            prod = next((p for p in products.values() if p.get("product_id") == pid), None)
            if not prod:
                results.append({"product_id": pid, "error": "Product not found"})
                continue

            try:
                prod["stock_quantity"] = int(prod.get("stock_quantity", 0)) + int(qty)
            except (TypeError, ValueError):
                payload = {"error": "quantity_to_add must be an integer"}
                out = json.dumps(
                    payload, indent=2
                )
                return out

            results.append(
                {"product_id": pid, "stock_quantity": prod["stock_quantity"]}
            )
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddStockQuantities",
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
