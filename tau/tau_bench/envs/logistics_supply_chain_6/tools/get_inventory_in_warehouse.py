from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetInventoryInWarehouse(Tool):
    """Utility for retrieving inventory from a particular warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str, sku: str | None = None) -> str:
        """Run the tool with the provided parameters."""
        inventory = data.get("inventory", [])
        results = []
        for item in inventory:
            if item.get("warehouse_id") == warehouse_id:
                if not sku or item.get("sku") == sku:
                    results.append(item)
        if not results:
            payload = {"error": f"No inventory found for warehouse {warehouse_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryInWarehouse",
                "description": "Retrieves all inventory items or a specific SKU's inventory from a single warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse to check.",
                        },
                        "sku": {
                            "type": "string",
                            "description": "Optional: The SKU of a specific product to check.",
                        },
                    },
                    "required": ["warehouse_id"],
                },
            },
        }
