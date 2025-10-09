from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetCampaigns(Tool):
    """Fetches all advertising campaigns."""

    @staticmethod
    def invoke(data: dict[str, Any], timestamp: Any = None) -> str:
        campaigns = data.get("campaigns", [])
        ids_ = []
        for i in campaigns:
            ids_ += [i.get("campaign_id")]
        payload = {"campaigns_ids": ids_}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCampaigns",
                "description": "Retrieves all advertising campaign ids.",
                "parameters": {},
            },
        }
