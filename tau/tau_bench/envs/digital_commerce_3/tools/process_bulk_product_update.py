# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import FIXED_NOW, _find_one








def _idstr(v):
    """Coerce numeric IDs to strings; leave None/strings unchanged."""
    return str(v) if isinstance(v, int) else v

def _find_one(lst: List[Dict[str, Any]], key: str, value: Any) -> Dict[str, Any] | None:
    for x in lst or []:
        if x.get(key) == value:
            return x
    return None

def _error(msg: str) -> str:
    return json.dumps({"error": msg})

class ProcessBulkProductUpdate(Tool):
    """Process bulk updates to product catalog with validation."""

    @staticmethod
    def invoke(
        data: Dict[str, Any], update_type: Any, product_ids: Any, update_data: Any = {}
    ) -> str:
        update_type = f"{update_type}"
        product_ids = [_idstr(x) for x in (product_ids or [])]
        update_data = update_data or {}

        if not update_type or not product_ids:
            return _error("update_type and product_ids are required.")
        
        if not "list_price" in update_data and not "price" in update_data:
            return _error("list_price or price must be provided in update_data.")

        products = list(data.get("products", {}).values())
        updated_count = 0

        not_found = []

        for pid in product_ids:
            product = _find_one(products, "product_id", pid)
            if product:
                if update_type == "price" and ("list_price" in update_data or "price" in update_data):
                    product["list_price"] = update_data["list_price"]
                product["last_modified"] = FIXED_NOW
                updated_count += 1
            else:
                not_found.append(pid)

        return json.dumps(
            {
                "update_type": update_type,
                "successfully_updated_count": updated_count,
                "product_ids_not_found": not_found,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_bulk_product_update",
                "description": "Process bulk updates to product catalog with validation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "update_type": {"type": "string", "enum": ["price"]},
                        "product_ids": {"type": "array", "items": {"type": "string"}},
                        "update_data": {"type": "object", "properties": {
                            "list_price": {"type": "number", "description": "Optional. New list price for the product."},
                        }},
                    },
                    "required": ["update_type", "product_ids"],
                },
            },
        }