from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class find_items(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: str = None,
        sku: str = None,
        store_id: str = None,
        status: str = None,
        last_stock_count: str = None,
        location: str = None
    ) -> str:
        inventory = data.get("inventory", [])

        # These columns will match precisely with the provided value
        exact_match_cols = ["id", "sku", "store_id", "status", "last_stock_count"]
        exact_match_values = {
            "id": id,
            "sku": sku,
            "store_id": store_id,
            "status": status,
            "last_stock_count": last_stock_count
        }

        # These columns will match as long as the database field has the provided value
        approximate_match_cols = ["location"]
        approximate_match_values = {
            "location": location
        }

        matches = []
        for item in inventory:
            # Include in the return list if all provided criteria match
            if all(
                [
                    exact_match_values[k] == item[k]
                    for k in exact_match_values.keys()
                    if exact_match_values[k] is not None
                ]
            ) and all(
                [
                    approximate_match_values[k].lower() in item[k].lower()
                    for k in approximate_match_values.keys()
                    if approximate_match_values[k] is not None
                ]
            ):
                matches.append(item)
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindItems",
                "description": "Finds items matching the sent criteria. Returns an empty list if there are none",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "The inventory id of the item. Will do an exact match",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The store id of the item. Will do an exact match",
                        },
                        "status": {
                            "type": "string",
                            "description": "status of the employee. Will do an exact match",
                        },
                        "sku": {
                            "type": "string",
                            "description": "The sku of the item. Will do an exact match",
                        },
                        "last_stock_count": {
                            "type": "string",
                            "description": "The last stock count of the item. Will do an exact match",
                        },
                        "location": {
                            "type": "string",
                            "description": "The shelf loaction of the item. Will do an approximate match",
                        },
                    },
                },
            },
        }
