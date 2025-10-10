# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCampaignStatus(Tool):
    """Changes the status of a campaign."""
    @staticmethod
    def invoke(data: Dict[str, Any], campaign_id, status) -> str:
        new_status = status
        for campaign in list(data.get('campaigns', {}).values()):
            if campaign.get('campaign_id') == campaign_id:
                campaign['status'] = new_status
                return json.dumps(campaign)
        return json.dumps({"error": f"Campaign ID '{campaign_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_campaign_status", "description": "Updates the status of a campaign (e.g., 'active', 'paused', 'archived').", "parameters": {"type": "object", "properties": {"campaign_id": {"type": "string"}, "status": {"type": "string"}}, "required": ["campaign_id", "status"]}}}
