from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchAdSetsByStatus(Tool):
    """Looks for ad sets that have a specific status."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = None) -> str:
        adsets = data.get("adsets", [])
        matching_adsets = []

        for adset in adsets:
            if adset.get("status") == status:
                matching_adsets.append(adset.get("adset_id"))
        payload = {"adset_ids": matching_adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchAdsetsByStatus",
                "description": "Searches for ad sets with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status to search for (e.g., active, paused).",
                        }
                    },
                    "required": ["status"],
                },
            },
        }
