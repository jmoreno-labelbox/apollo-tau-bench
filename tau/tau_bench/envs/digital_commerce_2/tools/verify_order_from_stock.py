from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class VerifyOrderFromStock(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], items: list[dict[str, Any]]) -> str:
        if not items or not isinstance(items, list):
            payload = {
                "error": "Missing or invalid 'items'. Expected list of {product_id, required_quantity}."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        products = data.get("products", {}).values()
        results = []
        is_valid = True
        for it in items:
            pid = it.get("product_id")
            req = it.get("required_quantity")
            if not pid or req is None:
                payload = {
                    "error": "Each item must include product_id and required_quantity"
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            match = next((p for p in products.values() if p.get("product_id") == pid), None)
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
        payload = {"is_valid": is_valid, "Valid_item_list": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifyOrderFromStock",
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
