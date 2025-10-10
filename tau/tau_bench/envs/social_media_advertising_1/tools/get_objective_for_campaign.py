# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetObjectiveForCampaign(Tool):
    """Retrieves the objective for a specific campaign."""

    @staticmethod
    def invoke(data: Dict[str, Any], campaign_id) -> str:
        campaigns = list(data.get("campaigns", {}).values())
        
        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                return json.dumps({"objective": campaign.get('objective')})
        
        return json.dumps({"error": f"Campaign with ID '{campaign_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_objective_for_campaign",
                "description": "Retrieves the objective for a specific campaign.",
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
