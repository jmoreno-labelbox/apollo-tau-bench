from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateInventoryStatus(Tool):
    """Modifies the stock status for a particular inventory ID."""

    @staticmethod
    def invoke(data: dict[str, Any], inventory_id: str = None, new_status: str = None) -> str:
        inventory_items = data.get("inventory", {}).values()

        if not inventory_id or not new_status:
            payload = {"error": "Inventory ID and new status are required."}
            out = json.dumps(payload)
            return out

        for item in inventory_items:
            if item.get("inventory_id") == inventory_id:
                item["stock_status"] = new_status
                if new_status.lower() == "quarantined":
                    item["quantity_available"] = 0
                payload = {
                    "status": "success",
                    "inventory_id": inventory_id,
                    "new_stock_status": item["stock_status"],
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Inventory ID not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInventoryStatus",
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
