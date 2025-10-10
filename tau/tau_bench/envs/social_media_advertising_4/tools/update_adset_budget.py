# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAdsetBudget(Tool):
    """Updates the daily budget of an ad set."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        new_budget = kwargs.get("new_budget")
        for adset in data.get('adsets', []):
            if adset.get('adset_id') == adset_id:
                adset['daily_budget'] = new_budget
                return json.dumps(adset)
        return json.dumps({"error": f"Ad set ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_adset_budget", "description": "Updates the daily budget for a specific ad set.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "new_budget": {"type": "number"}}, "required": ["adset_id", "new_budget"]}}}
