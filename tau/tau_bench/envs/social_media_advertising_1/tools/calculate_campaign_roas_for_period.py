# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateCampaignROASForPeriod(Tool):
    """Calculates ROAS for a campaign over a period."""

    @staticmethod
    def invoke(data: Dict[str, Any], campaign_id, end_date, start_date) -> str:
        
        adsets = list(data.get("adsets", {}).values())
        campaign_adsets = [adset for adset in adsets if adset.get("campaign_id") == campaign_id]
        adset_ids = [adset.get("adset_id") for adset in campaign_adsets]
        
        insights = list(data.get("f_insights", {}).values())
        total_revenue = 0
        total_spend = 0
        
        for insight in insights:
            if insight.get("adset_id") in adset_ids and start_date <= insight.get("date") <= end_date:
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
                "name": "calculate_campaign_roas_for_period",
                "description": "Calculates ROAS for a campaign over a period.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {
                            "type": "string",
                            "description": "The campaign ID.",
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
                    "required": ["campaign_id", "start_date", "end_date"],
                },
            },
        }
