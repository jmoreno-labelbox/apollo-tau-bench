from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetWarehouseByID(Tool):
    """Utility for obtaining complete details of a warehouse via its ID."""
    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str = None) -> str:
        warehouses = data.get("warehouses", [])
        for warehouse in warehouses:
            if warehouse["warehouse_id"] == warehouse_id:
                payload = warehouse
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Warehouse ID '{warehouse_id}' not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWarehouseById",
                "description": "Retrieve full warehouse details using warehouse ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "Warehouse ID (e.g., 'WH-14')",
                        }
                    },
                    "required": ["warehouse_id"],
                },
            },
        }
