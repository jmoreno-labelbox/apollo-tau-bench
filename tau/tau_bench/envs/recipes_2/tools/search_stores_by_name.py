from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class SearchStoresByName(Tool):
    """Looks for stores whose names include the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        if not name_query:
            payload = {"error": "name_query parameter is required."}
            out = json.dumps(payload)
            return out

        stores = data.get("stores", [])

        matching_stores = [
            store
            for store in stores
            if name_query.lower() in store.get("store_name", "").lower()
        ]
        payload = matching_stores
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchStoresByName",
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
