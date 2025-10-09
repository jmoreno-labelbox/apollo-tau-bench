from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetInventoryDetails(Tool):
    """Obtains essential inventory information for a particular product at a specific warehouse."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, warehouse_id: str = None) -> str:
        inventory_items = data.get("inventory", [])
        for item in inventory_items:
            if item.get("sku") == sku and item.get("warehouse_id") == warehouse_id:
                payload = {
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
                out = json.dumps(payload)
                return out
        payload = {"error": "Inventory record not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInventoryDetails",
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
