# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateROASForAdSetForDay(Tool):
    """Calculates ROAS for a specific ad set on a specific day."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        date = kwargs.get("date")
        insights = data.get("f_insights", [])
        
        for insight in insights:
            if insight.get("adset_id") == adset_id and insight.get("date") == date:
                revenue = insight.get("revenue", 0)
                spend = insight.get("spend", 0)
                if spend == 0:
                    return json.dumps({"error": "Spend is zero, cannot calculate ROAS."})
                roas = revenue / spend
                return json.dumps({"roas": roas})
        
        return json.dumps({"error": f"No insights found for ad set {adset_id} on date {date}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_adset_roas_for_day",
                "description": "Calculates ROAS for a specific ad set on a specific day.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID.",
                        },
                        "date": {
                            "type": "string",
                            "description": "The date in YYYY-MM-DD format.",
                        }
                    },
                    "required": ["adset_id", "date"],
                },
            },
        }
