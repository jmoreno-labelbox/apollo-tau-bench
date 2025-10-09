from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListCampaignAdsets(Tool):
    """Enumerate all ad sets associated with a campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        adsets = [a for a in data.get("adsets", {}).values() if a.get("campaign_id") == campaign_id]
        payload = {"adsets": adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListCampaignAdsets",
                "description": "List all ad sets under a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }
