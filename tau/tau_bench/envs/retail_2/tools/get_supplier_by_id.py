from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSupplierById(Tool):
    """Retrieve supplier information from suppliers.json using supplier_id."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str) -> str:
        suppliers = data.get("suppliers", {}).values()
        for supplier in suppliers.values():
            if supplier.get("supplier_id") == supplier_id:
                payload = supplier
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
                "name": "GetSupplierById",
                "description": "Get supplier details using the supplier ID from suppliers.json.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier ID (e.g., '#SUP0001').",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }
