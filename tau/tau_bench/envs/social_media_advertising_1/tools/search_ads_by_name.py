from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchAdsByName(Tool):
    """Looks for ads whose names include the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        ads = data.get("ads", [])
        matching_ads = []
        
        if not name_query:
            payload = {"ad_ids": []}
            out = json.dumps(payload)
            return out

        for ad in ads:
            if name_query.lower() in ad.get("name", "").lower():
                matching_ads.append(ad.get("ad_id"))
        payload = {"ad_ids": matching_ads}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchAdsByName",
                "description": "Searches for ads with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in ad names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }
