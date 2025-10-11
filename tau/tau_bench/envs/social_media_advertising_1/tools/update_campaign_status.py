# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCampaignStatus(Tool):
    """Updates the status of a campaign."""

    @staticmethod
    def invoke(data: Dict[str, Any], campaign_id, new_status) -> str:
        
        campaigns = list(data.get("campaigns", {}).values())
        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                old_status = campaign['status']
                campaign['status'] = new_status
                return json.dumps({
                    "status": "success",
                    "message": f"Campaign status updated from '{old_status}' to '{new_status}'"
                })

        return json.dumps({"error": f"Campaign {campaign_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_campaign_status",
                "description": "Updates the status of a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "new_status": {"type": "string"}
                    },
                    "required": ["campaign_id", "new_status"]
                }
            }
        }
