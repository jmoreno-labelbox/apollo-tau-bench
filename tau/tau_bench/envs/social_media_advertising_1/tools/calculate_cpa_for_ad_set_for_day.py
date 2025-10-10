# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateCPAForAdSetForDay(Tool):
    """Calculates CPA for a specific ad set on a specific day."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        date = kwargs.get("date")
        insights = list(data.get("f_insights", {}).values())
        
        for insight in insights:
            if insight.get("adset_id") == adset_id and insight.get("date") == date:
                spend = insight.get("spend", 0)
                purchases = insight.get("purchases", 0)
                if purchases == 0:
                    return json.dumps({"error": "No purchases, cannot calculate CPA."})
                cpa = spend / purchases
                return json.dumps({"cpa": cpa})
        
        return json.dumps({"error": f"No insights found for ad set {adset_id} on date {date}."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_adset_cpa_for_day",
                "description": "Calculates CPA for a specific ad set on a specific day.",
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
