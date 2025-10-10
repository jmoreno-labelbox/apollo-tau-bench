# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchCampaignsByName(Tool):
    """Searches for campaigns with names containing the specified text."""

    @staticmethod
    def invoke(data: Dict[str, Any], name_query) -> str:
        campaigns = list(data.get("campaigns", {}).values())
        matching_campaigns = []
        
        for campaign in campaigns:
            if name_query.lower() in campaign.get("name", "").lower():
                matching_campaigns.append(campaign.get("campaign_id"))
        
        return json.dumps({"campaign_ids": matching_campaigns})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_campaigns_by_name",
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
