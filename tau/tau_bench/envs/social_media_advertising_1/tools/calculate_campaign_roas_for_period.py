from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CalculateCampaignROASForPeriod(Tool):
    """Computes ROAS for a campaign during a specified timeframe."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, start_date: str = None, end_date: str = None) -> str:
        adsets = data.get("adsets", {}).values()
        campaign_adsets = [
            adset for adset in adsets.values() if adset.get("campaign_id") == campaign_id
        ]
        adset_ids = [adset.get("adset_id") for adset in campaign_adsets]

        insights = data.get("f_insights", {}).values()
        total_revenue = 0
        total_spend = 0

        for insight in insights.values():
            if (
                insight.get("adset_id") in adset_ids
                and start_date <= insight.get("date") <= end_date
            ):
                total_revenue += insight.get("revenue", 0)
                total_spend += insight.get("spend", 0)

        if total_spend == 0:
            payload = {"error": "No spend found for the period."}
            out = json.dumps(payload)
            return out

        roas = total_revenue / total_spend
        payload = {"roas": roas}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculateCampaignRoasForPeriod",
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
                        },
                    },
                    "required": ["campaign_id", "start_date", "end_date"],
                },
            },
        }
