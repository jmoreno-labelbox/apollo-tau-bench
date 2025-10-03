from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class SearchCampaignsByStatus(Tool):
    """Looks for campaigns that have a specific status."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = None) -> str:
        campaigns = data.get("campaigns", [])
        matching_campaigns = []

        for campaign in campaigns:
            if campaign.get("status") == status:
                matching_campaigns.append(campaign.get("campaign_id"))
        payload = {"campaign_ids": matching_campaigns}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchCampaignsByStatus",
                "description": "Searches for campaigns with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status to search for (e.g., active, paused, archived).",
                        }
                    },
                    "required": ["status"],
                },
            },
        }
