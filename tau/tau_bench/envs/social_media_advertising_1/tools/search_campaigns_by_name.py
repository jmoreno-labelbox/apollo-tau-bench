from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchCampaignsByName(Tool):
    """Looks for campaigns whose names include the specified text."""

    @staticmethod
    def invoke(data: dict[str, Any], name_query: str = None) -> str:
        campaigns = data.get("campaigns", {}).values()
        matching_campaigns = []
        
        if not name_query:
            payload = {"campaign_ids": []}
            out = json.dumps(payload)
            return out

        for campaign in campaigns.values():
            if name_query.lower() in campaign.get("name", "").lower():
                matching_campaigns.append(campaign.get("campaign_id"))
        payload = {"campaign_ids": matching_campaigns}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchCampaignsByName",
                "description": "Searches for campaigns with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in campaign names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }
