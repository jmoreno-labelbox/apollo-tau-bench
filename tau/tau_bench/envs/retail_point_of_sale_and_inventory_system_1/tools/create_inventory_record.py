from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateInventoryRecord(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str = None, store_id: str = None, location: str = None) -> str:
        inventory_list = data.get("inventory", [])

        for item in inventory_list:
            if item.get("sku") == sku and item.get("store_id") == store_id:
                payload = {"status": "exists", "inventory_id": item.get("id")}
                out = json.dumps(payload)
                return out

        max_inv_id_num = 0
        for item in inventory_list:
            inv_id = item.get("id")
            if isinstance(inv_id, str):
                match = re.match(r"INV-(\d+)", inv_id)
                if match:
                    num = int(match.group(1))
                    if num > max_inv_id_num:
                        max_inv_id_num = num

        next_inv_id_num = max_inv_id_num + 1
        new_inv_id = f"INV-{next_inv_id_num:04d}"

        new_record = {
            "id": new_inv_id,
            "sku": sku,
            "store_id": store_id,
            "quantity": 0,
            "reserved_quantity": 0,
            "reorder_level": 10,
            "safety_stock": 5,
            "location": location,
            "status": "out_of_stock",
            "last_stock_count": "2025-07-28",
        }

        inventory_list.append(new_record)
        data["inventory"] = inventory_list
        payload = {"status": "created", "inventory_id": new_inv_id}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInventoryRecord",
                "description": "Creates a new inventory record for a product at a specific store, if one does not already exist.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "The SKU of the product.",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The ID of the store.",
                        },
                        "location": {
                            "type": "string",
                            "description": "A placeholder location for the new inventory record.",
                        },
                    },
                    "required": ["sku", "store_id", "location"],
                },
            },
        }
