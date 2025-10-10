# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSupplierProducts(Tool):
    """Return list of product_ids supplied by a given supplier."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str) -> str:
        suppliers = data.get("suppliers", [])
        for s in suppliers:
            if s.get("supplier_id") == supplier_id:
                return json.dumps({"supplier_id": supplier_id, "products": s.get("products", [])})
        return json.dumps({"error": "Supplier not found", "supplier_id": supplier_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_supplier_products",
                "description": "List product_ids provided by a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"}
                    },
                    "required": ["supplier_id"]
                }
            }
        }
