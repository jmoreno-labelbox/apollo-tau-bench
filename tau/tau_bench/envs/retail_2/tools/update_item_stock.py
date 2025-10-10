# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateItemStock(Tool):
    """Set quantity or status for an item_id in a supplier's item_stock."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str, item_id: str, value: Any) -> str:
        suppliers = data.get("suppliers", [])
        for s in suppliers:
            if s.get("supplier_id") == supplier_id:
                item_stock = s.get("item_stock", {})
                item_stock[item_id] = value
                s["item_stock"] = item_stock
                return json.dumps({"status": "success", "supplier_id": supplier_id, "item_id": item_id, "value": value})
        return json.dumps({"error": "Supplier not found", "supplier_id": supplier_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_item_stock",
                "description": "Update supplier.item_stock for a given item_id. Value can be a number or status string.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"},
                        "item_id": {"type": "string"},
                        "value": {"description": "Number quantity or status string like 'out_of_stock' or 'discontinued'"}
                    },
                    "required": ["supplier_id", "item_id", "value"]
                }
            }
        }
