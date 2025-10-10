# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDailyBudgetForAdSet(Tool):
    """Retrieves the daily budget for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], adset_id) -> str:
        adsets = list(data.get("adsets", {}).values())
        
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                return json.dumps({"daily_budget": adset.get('daily_budget')})
        
        return json.dumps({"error": f"Ad set with ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_daily_budget_for_adset",
                "description": "Retrieves the daily budget for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }
