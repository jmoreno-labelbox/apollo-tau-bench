from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAdSets(Tool):
    """Fetches all IDs of ad sets."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        adsets = data.get("adsets", [])
        ids_ = []
        for i in adsets:
            ids_ += [i.get("adset_id")]
        payload = {"adset_ids": ids_}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAdsets",
                "description": "Retrieves all ad set IDs.",
                "parameters": {},
            },
        }
