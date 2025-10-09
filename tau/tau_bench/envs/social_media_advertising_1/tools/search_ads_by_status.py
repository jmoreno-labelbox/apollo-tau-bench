from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchAdsByStatus(Tool):
    """Looks for ads that have a specific status."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = None) -> str:
        ads = data.get("ads", [])
        matching_ads = []

        for ad in ads:
            if ad.get("status") == status:
                matching_ads.append(ad.get("ad_id"))
        payload = {"ad_ids": matching_ads}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchAdsByStatus",
                "description": "Searches for ads with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status to search for (e.g., active, paused, archived).",
                        }
                    },
                    "required": ["status"],
                },
            },
        }
