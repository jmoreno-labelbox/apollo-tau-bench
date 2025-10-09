from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchAdSetsByName(Tool):
    """Looks for ad sets whose names include the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        adsets = data.get("adsets", [])
        matching_adsets = []
        
        if not name_query:
            payload = {"adset_ids": []}
            out = json.dumps(payload)
            return out

        for adset in adsets:
            if name_query.lower() in adset.get("name", "").lower():
                matching_adsets.append(adset.get("adset_id"))
        payload = {"adset_ids": matching_adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchAdsetsByName",
                "description": "Searches for ad sets with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in ad set names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }
