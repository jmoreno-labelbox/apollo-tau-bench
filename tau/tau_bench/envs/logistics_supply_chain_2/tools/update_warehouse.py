from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class UpdateWarehouse(Tool):
    """Utility for modifying warehouse information."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str = None, updates: dict[str, Any] = None) -> str:
        warehouses = data.get("warehouses", [])

        for warehouse in warehouses:
            if warehouse["warehouse_id"] == warehouse_id:
                warehouse.update(updates)
                payload = {"success": f"warehouse {warehouse_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"warehouse_id {warehouse_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateWarehouse",
                "description": "Update warehouse by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "The warehouse ID to update",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Fields and values to update",
                        },
                    },
                    "required": ["warehouse_id", "updates"],
                },
            },
        }
