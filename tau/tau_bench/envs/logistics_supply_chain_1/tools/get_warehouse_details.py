from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetWarehouseDetails(Tool):
    """Fetches all information for a specific warehouse using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_name: str = None) -> str:
        if not warehouse_name:
            payload = {"error": "warehouse_name is required."}
            out = json.dumps(payload, indent=2)
            return out
        warehouse = next(
            (
                w
                for w in data.get("warehouses", [])
                if w.get("warehouse_name") == warehouse_name
            ),
            None,
        )
        if not warehouse:
            payload = {"error": f"Warehouse '{warehouse_name}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = warehouse
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWarehouseDetails",
                "description": "Retrieves all details for a specific warehouse by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"warehouse_name": {"type": "string"}},
                    "required": ["warehouse_name"],
                },
            },
        }
