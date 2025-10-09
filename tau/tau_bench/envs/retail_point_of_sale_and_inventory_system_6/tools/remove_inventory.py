from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class remove_inventory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], inv_id: str = None) -> str:
        inventory = data.get("inventory", {}).values()

        if inv_id is None:
            payload = {"error": "inv_id must be sent"}
            out = json.dumps(payload, indent=2)
            return out

        for item in inventory.values():
            if item["id"] == inv_id:
                del item
                payload = {"success": f"Removed item: {inv_id}"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "No item found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeInventory",
                "description": "Removes an item from the store. This is for completely removing an item, to set to 0, use UpdateStockQuantity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inv_id": {
                            "type": "string",
                            "description": "The id of the item to remove",
                        },
                    },
                },
            },
        }
