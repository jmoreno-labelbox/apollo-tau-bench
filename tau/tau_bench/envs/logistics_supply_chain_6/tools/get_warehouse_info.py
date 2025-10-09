from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetWarehouseInfo(Tool):
    """Utility for retrieving details about a warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str) -> str:
        """Run the tool with the provided parameters."""
        warehouses = data.get("warehouses", [])
        for warehouse in warehouses:
            if warehouse.get("warehouse_id") == warehouse_id:
                payload = warehouse
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Warehouse with ID {warehouse_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetWarehouseInfo",
                "description": "Retrieves detailed information about a specific warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse.",
                        }
                    },
                    "required": ["warehouse_id"],
                },
            },
        }
