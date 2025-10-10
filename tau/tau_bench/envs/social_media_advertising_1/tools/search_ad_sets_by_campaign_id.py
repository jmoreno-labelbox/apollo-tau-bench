# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchAdSetsByCampaignId(Tool):
    """Searches for ad sets belonging to a specific campaign."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_id = kwargs.get("campaign_id")
        adsets = list(data.get("adsets", {}).values())
        matching_adsets = []
        
        for adset in adsets:
            if adset.get("campaign_id") == campaign_id:
                matching_adsets.append(adset.get("adset_id"))
        
        return json.dumps({"adset_ids": matching_adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_adsets_by_campaign_id",
                "description": "Searches for ad sets belonging to a specific campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The campaign ID to search for ad sets.",
                        }
                    },
                    "required": ["campaign_id"],
                },
            },
        }
