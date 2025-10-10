# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateDailyBudgetForAdSet(Tool):
    """Updates the daily budget for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        new_budget = kwargs.get("new_budget")
        
        adsets = list(data.get("adsets", {}).values())
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                old_budget = adset['daily_budget']
                adset['daily_budget'] = new_budget
                return json.dumps({
                    "status": "success",
                    "message": f"Ad set budget updated from {old_budget} to {new_budget}"
                })

        return json.dumps({"error": f"Ad set {adset_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_daily_budget_for_adset",
                "description": "Updates the daily budget for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_budget": {"type": "number"}
                    },
                    "required": ["adset_id", "new_budget"]
                }
            }
        }
