from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CalculateROASForAdSetForDay(Tool):
    """Computes ROAS for a specific ad set on a particular day."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None) -> str:
        insights = data.get("f_insights", [])

        for insight in insights:
            if insight.get("adset_id") == adset_id and insight.get("date") == date:
                revenue = insight.get("revenue", 0)
                spend = insight.get("spend", 0)
                if spend == 0:
                    payload = {"error": "Spend is zero, cannot calculate ROAS."}
                    out = json.dumps(payload)
                    return out
                roas = revenue / spend
                payload = {"roas": roas}
                out = json.dumps(payload)
                return out
        payload = {"error": f"No insights found for ad set {adset_id} on date {date}."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateAdsetRoasForDay",
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
                        },
                    },
                    "required": ["adset_id", "date"],
                },
            },
        }
