from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAdsByAdsetID(Tool):
    """Fetches all ads contained in a particular ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        ads = [ad for ad in data.get("ads", {}).values() if ad.get("adset_id") == adset_id]
        payload = {"ads": ads}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsByAdsetId",
                "description": "Retrieves a list of all ads that belong to a specific ad set ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }
