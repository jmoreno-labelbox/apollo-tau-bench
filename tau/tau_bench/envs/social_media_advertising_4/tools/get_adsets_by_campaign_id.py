# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdsetsByCampaignID(Tool):
    """Retrieves all ad sets belonging to a specific campaign."""
    @staticmethod
    def invoke(data: Dict[str, Any], campaign_id) -> str:
        adsets = [adset for adset in data.get('adsets', []) if adset.get('campaign_id') == campaign_id]
        return json.dumps({"adsets": adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adsets_by_campaign_id", "description": "Retrieves a list of all ad sets that belong to a specific campaign ID.", "parameters": {"type": "object", "properties": {"campaign_id": {"type": "string"}}, "required": ["campaign_id"]}}}
