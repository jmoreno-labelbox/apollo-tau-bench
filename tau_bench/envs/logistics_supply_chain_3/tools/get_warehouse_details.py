from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class GetWarehouseDetails(Tool):
    """Obtains complete details for a warehouse using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str = None) -> str:
        warehouses = data.get("warehouses", [])
        for warehouse in warehouses:
            if warehouse.get("warehouse_id") == warehouse_id:
                payload = warehouse
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
                "name": "GetWarehouseDetails",
                "description": "Retrieves the full record for a warehouse by its exact ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse (e.g., 'WH-01').",
                        }
                    },
                    "required": ["warehouse_id"],
                },
            },
        }
