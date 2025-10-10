# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInventoryDetails(Tool):
    """Retrieves key inventory details for a specific product at a specific warehouse."""

    @staticmethod
    def invoke(data: Dict[str, Any], sku, warehouse_id) -> str:
        inventory_items = list(data.get("inventory", {}).values())
        for item in inventory_items:
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                return json.dumps(
                    {
                        "inventory_id": item.get("inventory_id"),
                        "reorder_point": item.get("reorder_point"),
                        "quantity_on_hand": item.get("quantity_on_hand"),
                        "quantity_available": item.get("quantity_available"),
                        "quantity_allocated": item.get("quantity_allocated"),
                        "quantity_inbound": item.get("quantity_inbound"),
                        "unit_cost": item.get("unit_cost"),
                        "unit_weight_kg": item.get("unit_weight_kg"),
                        "lot_number": item.get("lot_number"),
                        "unit_dimensions_cm": item.get("unit_dimensions_cm"),
                    }
                )
        return json.dumps({"error": "Inventory record not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_inventory_details",
                "description": "Retrieves key inventory details for a specific product at a specific warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the warehouse.",
                        },
                    },
                    "required": ["sku", "warehouse_id"],
                },
            },
        }
