# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchCampaignsByStatus(Tool):
    """Searches for campaigns with a specific status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        campaigns = list(data.get("campaigns", {}).values())
        matching_campaigns = []
        
        for campaign in campaigns:
            if campaign.get("status") == status:
                matching_campaigns.append(campaign.get("campaign_id"))
        
        return json.dumps({"campaign_ids": matching_campaigns})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_campaigns_by_status",
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
