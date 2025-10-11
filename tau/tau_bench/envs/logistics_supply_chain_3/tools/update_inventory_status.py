# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInventoryStatus(Tool):
    """Updates the stock status for a specific inventory ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], inventory_id, new_status) -> str:
        inventory_items = list(data.get("inventory", {}).values())

        if not inventory_id or not new_status:
            return json.dumps({"error": "Inventory ID and new status are required."})

        for item in inventory_items:
            if item.get("inventory_id") == inventory_id:
                item["stock_status"] = new_status
                # During quarantine, render quantity inaccessible.
                if new_status.lower() == "quarantined":
                    item["quantity_available"] = 0
                return json.dumps(
                    {
                        "status": "success",
                        "inventory_id": inventory_id,
                        "new_stock_status": item["stock_status"],
                    }
                )
        return json.dumps({"error": "Inventory ID not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_status",
                "description": "Updates the stock status of a specific inventory item (e.g., to 'In Stock', 'Quarantined'). If status is set to 'Quarantined', it also sets the available quantity to 0.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "The unique ID of the inventory record to update (e.g., 'INV-0001').",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new stock status to set.",
                        },
                    },
                    "required": ["inventory_id", "new_status"],
                },
            },
        }
