# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCampaignByName(Tool):
    """Retrieves a campaign's details by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], name) -> str:
        for campaign in list(list(list(data.get('campaigns', {}).values())) if isinstance(data.get('campaigns'), dict) else data.get('campaigns', [])):
            if campaign.get('name') == name:
                return json.dumps(campaign)
        return json.dumps({"error": f"Campaign '{name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_campaign_by_name", "description": "Find a specific campaign by its exact name.", "parameters": {"type": "object", "properties": {"name": {"type": "string", "description": "The name of the campaign."}}, "required": ["name"]}}}
