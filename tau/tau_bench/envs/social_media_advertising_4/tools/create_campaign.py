# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCampaign(Tool):
    """Creates a new advertising campaign."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaigns = list(data.get('campaigns', {}).values())
        new_id = max((int(c['campaign_id']) for c in campaigns), default=0) + 1
        new_campaign = {"campaign_id": str(new_id), "name": kwargs.get("name"), "objective": kwargs.get("objective"), "created_date": "2025-08-15", "status": "paused"}
        campaigns.append(new_campaign)
        data['campaigns'] = campaigns
        return json.dumps(new_campaign)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_campaign", "description": "Creates a new advertising campaign. New campaigns always start with a 'paused' status.", "parameters": {"type": "object", "properties": {"name": {"type": "string"}, "objective": {"type": "string"}}, "required": ["name", "objective"]}}}
