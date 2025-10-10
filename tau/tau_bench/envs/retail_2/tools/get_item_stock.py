# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetItemStock(Tool):
    """Return current stock quantity/status for an item_id at a supplier."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str, item_id: str) -> str:
        suppliers = data.get("suppliers", [])
        for s in suppliers:
            if s.get("supplier_id") == supplier_id:
                val = s.get("item_stock", {}).get(item_id)
                if val is None:
                    return json.dumps({"error": "Item not found at supplier", "supplier_id": supplier_id, "item_id": item_id})
                return json.dumps({"supplier_id": supplier_id, "item_id": item_id, "value": val})
        return json.dumps({"error": "Supplier not found", "supplier_id": supplier_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_item_stock",
                "description": "Get supplier.item_stock value for a given item_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"},
                        "item_id": {"type": "string"}
                    },
                    "required": ["supplier_id", "item_id"]
                }
            }
        }
