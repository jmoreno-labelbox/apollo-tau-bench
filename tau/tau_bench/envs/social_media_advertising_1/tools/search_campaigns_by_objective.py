# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchCampaignsByObjective(Tool):
    """Searches for campaigns with a specific objective."""

    @staticmethod
    def invoke(data: Dict[str, Any], objective) -> str:
        campaigns = list(data.get("campaigns", {}).values())
        matching_campaigns = []
        
        for campaign in campaigns:
            if campaign.get("objective") == objective:
                matching_campaigns.append(campaign.get("campaign_id"))
        
        return json.dumps({"campaign_ids": matching_campaigns})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_campaigns_by_objective",
                "description": "Searches for campaigns with a specific objective.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "objective": {
                            "type": "string",
                            "description": "The objective to search for (e.g., Sales, Awareness, Traffic).",
                        }
                    },
                    "required": ["objective"],
                },
            },
        }
