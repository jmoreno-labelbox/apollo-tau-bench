from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSupplierDetails(Tool):
    """Obtains complete details for a supplier using their ID."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None) -> str:
        suppliers = data.get("supplier_master", {}).values()
        for supplier in suppliers.values():
            if supplier.get("supplier_id") == supplier_id:
                payload = supplier
                out = json.dumps(payload)
                return out
        payload = {"error": "Supplier not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupplierDetails",
                "description": "Retrieves the full record for a supplier by their id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The id of the supplier.",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }
