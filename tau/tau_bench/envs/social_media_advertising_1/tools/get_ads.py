from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAds(Tool):
    """Fetches all IDs of ads."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        ads = data.get("ads", [])
        ids_ = []
        for i in ads:
            ids_ += [i.get("ad_id")]
        payload = {"ad_ids": ids_}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAds",
                "description": "Retrieves all ad IDs.",
                "parameters": {},
            },
        }
