from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class UpdateInventory(Tool):
    """Utility for modifying inventory records."""

    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None, updates: dict[str, Any] = None) -> str:
        inventories = data.get("inventory", [])

        for inv in inventories:
            if inv["inventory_id"] == inventory_id:
                inv.update(updates)
                payload = {"success": f"inventory {inventory_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"inventory_id {inventory_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventory",
                "description": "Update inventory record by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "The inventory ID to update",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Fields and values to update",
                        },
                    },
                    "required": ["inventory_id", "updates"],
                },
            },
        }
