# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindInventoryBySku(Tool):
    """Finds all inventory records for a given SKU across all warehouses."""

    @staticmethod
    def invoke(data: Dict[str, Any], sku) -> str:
        inventory_items = list(data.get("inventory", {}).values())
        found_records = []
        for item in inventory_items:
            if item.get("sku") == sku:
                found_records.append(
                    {
                        "inventory_id": item.get("inventory_id"),
                        "warehouse_id": item.get("warehouse_id"),
                        "warehouse_name": item.get("warehouse_name"),
                        "quantity_on_hand": item.get("quantity_on_hand"),
                        "quantity_available": item.get("quantity_available"),
                        "quantity_allocated": item.get("quantity_allocated"),
                        "quantity_inbound": item.get("quantity_inbound"),
                        "unit_cost": item.get("unit_cost"),
                        "lot_number": item.get("lot_number"),
                        "expiration_date": item.get("expiration_date"),
                        "unit_dimensions_cm": item.get("unit_dimensions_cm"),
                    }
                )
        if found_records:
            return json.dumps(found_records)
        return json.dumps({"error": "No inventory records found for that SKU"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_inventory_by_sku",
                "description": "Finds all inventory records for a given SKU, returning a list of locations and quantities.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product to search for.",
                        }
                    },
                    "required": ["sku"],
                },
            },
        }
