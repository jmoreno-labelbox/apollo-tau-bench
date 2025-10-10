# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSupplierById(Tool):
    """Get supplier details from suppliers.json by supplier_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str) -> str:
        suppliers = data.get("suppliers", [])
        for supplier in suppliers:
            if supplier.get("supplier_id") == supplier_id:
                return json.dumps(supplier)
        return json.dumps({"error": "Supplier not found", "supplier_id": supplier_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_supplier_by_id",
                "description": "Get supplier details using the supplier ID from suppliers.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "Supplier ID (e.g., '#SUP0001')."}
                    },
                    "required": ["supplier_id"]
                }
            }
        }
