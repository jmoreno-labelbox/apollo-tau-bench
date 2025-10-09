from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchAdsByAdSet(Tool):
    """Looks for ads that are part of a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        ads = data.get("ads", {}).values()
        matching_ads = []

        for ad in ads.values():
            if ad.get("adset_id") == adset_id:
                matching_ads.append(ad.get("ad_id"))
        payload = {"ad_ids": matching_ads}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchAdsByAdset",
                "description": "Searches for ads belonging to a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID to search for ads.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }
