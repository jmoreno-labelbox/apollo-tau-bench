from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSupplierProducts(Tool):
    """Provide a list of product_ids provided by a specific supplier."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str) -> str:
        suppliers = data.get("suppliers", {}).values()
        for s in suppliers.values():
            if s.get("supplier_id") == supplier_id:
                payload = {"supplier_id": supplier_id, "products": s.get("products", [])}
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
                "name": "GetSupplierProducts",
                "description": "List product_ids provided by a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {"supplier_id": {"type": "string"}},
                    "required": ["supplier_id"],
                },
            },
        }
