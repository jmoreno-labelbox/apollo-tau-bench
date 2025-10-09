from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchAdsByCreativeType(Tool):
    """Looks for ads that feature a particular creative type."""

    @staticmethod
    def invoke(data: dict[str, Any], creative_type: str = None) -> str:
        ads = data.get("ads", [])
        matching_ads = []

        for ad in ads:
            if ad.get("creative_type") == creative_type:
                matching_ads.append(ad.get("ad_id"))
        payload = {"ad_ids": matching_ads}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchAdsByCreativeType",
                "description": "Searches for ads with a specific creative type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "creative_type": {
                            "type": "string",
                            "description": "The creative type to search for (e.g., image, video, carousel).",
                        }
                    },
                    "required": ["creative_type"],
                },
            },
        }
