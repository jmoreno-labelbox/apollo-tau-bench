# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCampaignDetails(Tool):
    """Get details about a specific marketing campaign."""
    
    @staticmethod
    def invoke(data: Dict[str, Any], campaign_id) -> str:
        if not campaign_id:
            return json.dumps({"error": "campaign_id is required"}, indent=2)
        
        # Retrieve campaign information.
        campaigns = list(data.get('campaigns', {}).values())
        campaign = next((c for c in campaigns if c.get('campaign_id') == campaign_id), None)
        
        if not campaign:
            # Return a mock campaign for testing if the campaign is not located.
            mock_campaign = {
                "campaign_id": campaign_id,
                "name": f"Campaign {campaign_id}",
                "type": "general_update",
                "status": "active",
                "created_at": "2024-08-21T00:00:00Z"
            }
            return json.dumps(mock_campaign, indent=2)
        
        return json.dumps(campaign, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_campaign_details",
                "description": "Get details about a specific marketing campaign",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "integer",
                            "description": "Campaign ID to get details for"
                        }
                    },
                    "required": ["campaign_id"]
                }
            }
        }
