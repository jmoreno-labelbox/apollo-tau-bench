# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class VerifyOrderFromStock(Tool):
    """Validate order using live stock, without passing available_quantity explicitly."""

    @staticmethod
    def invoke(data: Dict[str, Any], items: Any) -> str:
        items: List[Dict[str, Any]] = items
        if not items or not isinstance(items, list):
            return json.dumps(
                {
                    "error": "Missing or invalid 'items'. Expected list of {product_id, required_quantity}."
                },
                indent=2,
            )
        products = list(data.get("products", {}).values())
        results = []
        is_valid = True
        for it in items:
            pid = it.get("product_id")
            req = it.get("required_quantity")
            if not pid or req is None:
                return json.dumps(
                    {"error": "Each item must include product_id and required_quantity"}, indent=2
                )
            match = next((p for p in products if p.get("product_id") == pid), None)
            if not match:
                results.append({"product_id": pid, "error": "Product not found"})
                is_valid = False
                continue
            avail = int(match.get("stock_quantity", 0))
            valid_q = req if req <= avail else avail
            if req > avail:
                is_valid = False
            results.append(
                {
                    "product_id": pid,
                    "required_quantity": req,
                    "available_quantity": avail,
                    "valid_quantity": valid_q,
                }
            )
        return json.dumps({"is_valid": is_valid, "Valid_item_list": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_order_from_stock",
                "description": "Validate order quantities against current stock without separate quantity fetch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_id": {"type": "string"},
                                    "required_quantity": {"type": "integer"},
                                },
                                "required": ["product_id", "required_quantity"],
                            },
                        }
                    },
                    "required": ["items"],
                },
            },
        }
