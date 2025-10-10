# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetNameForCampaign(Tool):
    """Retrieves a specific campaign by ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaign_id = kwargs.get("campaign_id")
        campaigns = list(data.get("campaigns", {}).values())
        
        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                return json.dumps({"name": campaign.get('name')})
        
        return json.dumps({"error": f"Campaign with ID '{campaign_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_name_for_campaign",
                "description": "Retrieves a specific campaign by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The unique ID of the campaign.",
                        }
                    },
                    "required": ["campaign_id"],
                },
            },
        }
