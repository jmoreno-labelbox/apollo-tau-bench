from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindInventoryBySku(Tool):
    """Identifies all inventory records for a specified SKU across all warehouses."""

    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None) -> str:
        inventory_items = data.get("inventory", {}).values()
        found_records = []
        for item in inventory_items:
            if item.get("sku") == sku:
                found_records.append(
                    {
                        "inventory_id": item["inventory_id"],
                        "warehouse_id": item["warehouse_id"],
                        "warehouse_name": item["warehouse_name"],
                        "quantity_on_hand": item["quantity_on_hand"],
                        "quantity_available": item["quantity_available"],
                        "quantity_allocated": item["quantity_allocated"],
                        "quantity_inbound": item["quantity_inbound"],
                        "unit_cost": item["unit_cost"],
                        "lot_number": item["lot_number"],
                        "expiration_date": item["expiration_date"],
                        "unit_dimensions_cm": item["unit_dimensions_cm"],
                    }
                )
        if found_records:
            payload = found_records
            out = json.dumps(payload)
            return out
        payload = {"error": "No inventory records found for that SKU"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindInventoryBySku",
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
