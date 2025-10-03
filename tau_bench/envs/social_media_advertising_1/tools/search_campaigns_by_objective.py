from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class SearchCampaignsByObjective(Tool):
    """Looks for campaigns that have a particular objective."""

    @staticmethod
    def invoke(data: dict[str, Any], objective: str = None) -> str:
        campaigns = data.get("campaigns", [])
        matching_campaigns = []

        for campaign in campaigns:
            if campaign.get("objective") == objective:
                matching_campaigns.append(campaign.get("campaign_id"))
        payload = {"campaign_ids": matching_campaigns}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchCampaignsByObjective",
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
