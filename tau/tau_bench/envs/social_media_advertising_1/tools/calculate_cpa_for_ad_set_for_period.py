from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CalculateCPAForAdSetForPeriod(Tool):
    """Computes CPA for a specific ad set during a specified timeframe."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, start_date: str = None, end_date: str = None) -> str:
        insights = data.get("f_insights", {}).values()
        total_spend = 0
        total_purchases = 0

        for insight in insights:
            if (
                insight.get("adset_id") == adset_id
                and start_date <= insight.get("date") <= end_date
            ):
                total_spend += insight.get("spend", 0)
                total_purchases += insight.get("purchases", 0)

        if total_purchases == 0:
            payload = {"cpa": 0}
            out = json.dumps(payload)
            return out
            payload = {"error": "No purchases found for the period."}
            out = json.dumps(payload)
            return out

        cpa = total_spend / total_purchases
        payload = {"cpa": cpa}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateAdsetCpaForPeriod",
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
                        },
                    },
                    "required": ["adset_id", "start_date", "end_date"],
                },
            },
        }
