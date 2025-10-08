from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class FindWarehouseByName(Tool):
    """Locates a warehouse's ID using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_name: str = None) -> str:
        warehouses = data.get("warehouses", [])
        for warehouse in warehouses:
            if warehouse.get("warehouse_name") == warehouse_name:
                payload = {"warehouse_id": warehouse.get("warehouse_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": "Warehouse not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindWarehouseByName",
                "description": "Finds a warehouse's ID by its full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_name": {
                            "type": "string",
                            "description": "The full name of the warehouse.",
                        }
                    },
                    "required": ["warehouse_name"],
                },
            },
        }
