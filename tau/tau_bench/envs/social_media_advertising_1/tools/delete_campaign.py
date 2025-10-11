# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteCampaign(Tool):
    """Deletes a campaign."""

    @staticmethod
    def invoke(data: Dict[str, Any], campaign_id) -> str:
        if not campaign_id:
            return json.dumps({"error": "campaign_id is a required parameter."})

        campaigns = list(data.get("campaigns", {}).values())
        for campaign in campaigns:
            if campaign.get("campaign_id") == campaign_id:
                data['campaigns'] = [d for d in data['campaigns'] if d['campaign_id'] != campaign_id]
                return json.dumps(
                    {
                        "status": "success",
                        "message": f"Campaign with id {campaign_id} deleted successfully",
                    }
                )

        return json.dumps({"error": f"Campaign with ID '{campaign_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_campaign",
                "description": "Deletes a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The unique ID of the campaign to delete.",
                        },
                    },
                    "required": ["campaign_id"],
                },
            },
        }
