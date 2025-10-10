# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInventoryStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory_id = kwargs.get('inventory_id')
        status = kwargs.get('status')
        inventory_items = list(data.get("inventory", {}).values())  # Lista []
        updated_item = None
        for item in inventory_items:
            if item.get("id") == inventory_id:
                item["status"] = status
                updated_item = item
                break
        return json.dumps({"updated_inventory_item": updated_item})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inventory_status",
                "description": "Updates the status of an inventory item (e.g., 'in_stock', 'low_stock', 'out_of_stock', 'critical').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inventory_id": {
                            "type": "string",
                            "description": "Unique identifier of the inventory item to update.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status of the inventory item.",
                        },
                    },
                    "required": ["inventory_id", "status"],
                },
            },
        }
