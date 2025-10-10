# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInventory(Tool):
    """Tool to update inventory record."""

    @staticmethod
    def invoke(data: Dict[str, Any], inventory_id, updates) -> str:
        inventories = list(data.get("inventory", {}).values())

        for inv in inventories:
            if inv["inventory_id"] == inventory_id:
                inv.update(updates)
                return json.dumps({"success": f"inventory {inventory_id} updated"}, indent=2)
        return json.dumps({"error": f"inventory_id {inventory_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory",
                "description": "Update inventory record by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {"type": "string", "description": "The inventory ID to update"},
                        "updates": {"type": "object", "description": "Fields and values to update"}
                    },
                    "required": ["inventory_id", "updates"]
                }
            }
        }
