# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAdset(Tool):
    """Creates a new ad set within a campaign."""
    @staticmethod
    def invoke(data: Dict[str, Any], bid_amount, bid_strategy, campaign_id, category, daily_budget, name) -> str:
        adsets = data.get('adsets', [])
        new_id = max((int(a['adset_id']) for a in adsets), default=100) + 1
        new_adset = {"adset_id": str(new_id), "campaign_id": campaign_id, "name": name, "category": category, "daily_budget": daily_budget, "bid_strategy": bid_strategy, "bid_amount": bid_amount, "status": "paused", "updated_at": "2025-08-15T00:00:00Z"}
        adsets.append(new_adset)
        data['adsets'] = adsets
        return json.dumps(new_adset)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_adset", "description": "Creates a new ad set within a specified campaign.", "parameters": {"type": "object", "properties": {"campaign_id": {"type": "string"}, "name": {"type": "string"}, "category": {"type": "string"}, "daily_budget": {"type": "number"}, "bid_strategy": {"type": "string"}, "bid_amount": {"type": "number"}}, "required": ["campaign_id", "name", "category", "daily_budget", "bid_strategy"]}}}
