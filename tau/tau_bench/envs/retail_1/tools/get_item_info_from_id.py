from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetItemInfoFromId(Tool):  #READ
    @staticmethod
    def invoke(data: dict[str, Any], item_id: str) -> str:
        pass
        products = data.get("products", [])
        for product in products:
            if item_id in product["variants"]:
                payload = product["variants"][item_id]
                out = json.dumps(payload)
                return out
        payload = {"error": "Item not found"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getItemInfoFromId",
                "description": "Retrieve item information by item ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {
                            "type": "string",
                            "description": "The ID of the item to retrieve information for.",
                        }
                    },
                    "required": ["item_id"],
                },
            },
        }
