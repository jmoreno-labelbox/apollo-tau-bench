# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateROASForAdSetForPeriod(Tool):
    """Calculates ROAS for a specific ad set over a period."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        start_date = kwargs.get("start_date")
        end_date = kwargs.get("end_date")
        insights = list(data.get("f_insights", {}).values())
        total_revenue = 0
        total_spend = 0
        
        for insight in insights:
            if insight.get("adset_id") == adset_id and start_date <= insight.get("date") <= end_date:
                total_revenue += insight.get("revenue", 0)
                total_spend += insight.get("spend", 0)
        
        if total_spend == 0:
            return json.dumps({"error": "No spend found for the period."})
        
        roas = total_revenue / total_spend
        return json.dumps({"roas": roas})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_adset_roas_for_period",
                "description": "Calculates ROAS for a specific ad set over a period.",
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
