# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchStoresByName(Tool):
    """Searches for stores with names containing the specified text."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name_query = kwargs.get("name_query")
        if not name_query:
            return json.dumps({"error": "name_query parameter is required."})

        stores = data.get("stores", [])
        
        matching_stores = [
            store for store in stores 
            if name_query.lower() in store.get("store_name", "").lower()
        ]
        
        return json.dumps(matching_stores)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_stores_by_name",
                "description": "Searches for stores with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in store names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }
