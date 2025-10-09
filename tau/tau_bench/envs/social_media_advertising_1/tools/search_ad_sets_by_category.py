from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchAdSetsByCategory(Tool):
    """Looks for ad sets belonging to a certain category."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None) -> str:
        adsets = data.get("adsets", {}).values()
        matching_adsets = []

        for adset in adsets:
            if adset.get("category") == category:
                matching_adsets.append(adset.get("adset_id"))
        payload = {"adset_ids": matching_adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchAdsetsByCategory",
                "description": "Searches for ad sets with a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to search for (e.g., Electronics, Apparel, Home).",
                        }
                    },
                    "required": ["category"],
                },
            },
        }
