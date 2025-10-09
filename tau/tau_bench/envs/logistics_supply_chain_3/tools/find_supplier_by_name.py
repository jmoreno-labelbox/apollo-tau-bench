from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindSupplierByName(Tool):
    """Locates a supplier's ID and lead time using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_name: str = None) -> str:
        suppliers = data.get("supplier_master", {}).values()
        for supplier in suppliers.values():
            if supplier.get("supplier_name") == supplier_name:
                payload = {
                    "supplier_id": supplier.get("supplier_id"),
                    "standard_lead_time_days": supplier.get("standard_lead_time_days"),
                }
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
                "name": "FindSupplierByName",
                "description": "Finds a supplier's ID and standard lead time by its full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_name": {
                            "type": "string",
                            "description": "The full name of the supplier.",
                        }
                    },
                    "required": ["supplier_name"],
                },
            },
        }
