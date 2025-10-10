# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateCPAForAdSetForPeriod(Tool):
    """Calculates CPA for a specific ad set over a period."""

    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, end_date, start_date) -> str:
        insights = list(data.get("f_insights", {}).values())
        total_spend = 0
        total_purchases = 0
        
        for insight in insights:
            if insight.get("adset_id") == adset_id and start_date <= insight.get("date") <= end_date:
                total_spend += insight.get("spend", 0)
                total_purchases += insight.get("purchases", 0)
        
        if total_purchases == 0:
            return json.dumps({'cpa': 0})
            return json.dumps({"error": "No purchases found for the period."})
        
        cpa = total_spend / total_purchases
        return json.dumps({"cpa": cpa})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_adset_cpa_for_period",
                "description": "Calculates CPA for a specific ad set over a period.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date in YYYY-MM-DD format.",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "End date in YYYY-MM-DD format.",
                        }
                    },
                    "required": ["adset_id", "start_date", "end_date"],
                },
            },
        }
