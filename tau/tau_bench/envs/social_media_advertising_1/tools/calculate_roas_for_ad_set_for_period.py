from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class CalculateROASForAdSetForPeriod(Tool):
    """Computes ROAS for a specific ad set during a specified timeframe."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, start_date: str = None, end_date: str = None) -> str:
        insights = data.get("f_insights", [])
        total_revenue = 0
        total_spend = 0

        for insight in insights:
            if (
                insight.get("adset_id") == adset_id
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
                "name": "CalculateAdsetRoasForPeriod",
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
                        },
                    },
                    "required": ["adset_id", "start_date", "end_date"],
                },
            },
        }
