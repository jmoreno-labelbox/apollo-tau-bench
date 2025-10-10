# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class find_items(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inventory = list(data.get("inventory", {}).values())

        # These columns will be matched exactly to the value sent
        exact_match_cols = ["id", "sku", "store_id", "status", "last_stock_count"]
        exact_match_values = {k: kwargs.get(k) for k in exact_match_cols}

        # These columns will be matched as long as the database field contains the sent value
        approximate_match_cols = ["location"]
        approximate_match_values = {k: kwargs.get(k) for k in approximate_match_cols}

        matches = []
        for item in inventory:
            # If all sent criteria match, then add it to the return list
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

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_items",
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
