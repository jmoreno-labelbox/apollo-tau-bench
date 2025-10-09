from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetItemStock(Tool):
    """Provide the current stock quantity/status for an item_id at a supplier."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str, item_id: str) -> str:
        suppliers = data.get("suppliers", {}).values()
        for s in suppliers.values():
            if s.get("supplier_id") == supplier_id:
                val = s.get("item_stock", {}).values().get(item_id)
                if val is None:
                    payload = {
                        "error": "Item not found at supplier",
                        "supplier_id": supplier_id,
                        "item_id": item_id,
                    }
                    out = json.dumps(payload)
                    return out
                payload = {"supplier_id": supplier_id, "item_id": item_id, "value": val}
                out = json.dumps(payload)
                return out
        payload = {"error": "Supplier not found", "supplier_id": supplier_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetItemStock",
                "description": "Get supplier.item_stock value for a given item_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string"},
                        "item_id": {"type": "string"},
                    },
                    "required": ["supplier_id", "item_id"],
                },
            },
        }
