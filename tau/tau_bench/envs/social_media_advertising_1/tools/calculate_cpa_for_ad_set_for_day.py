from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CalculateCPAForAdSetForDay(Tool):
    """Computes CPA for a specific ad set on a particular day."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None) -> str:
        insights = data.get("f_insights", [])

        for insight in insights:
            if insight.get("adset_id") == adset_id and insight.get("date") == date:
                spend = insight.get("spend", 0)
                purchases = insight.get("purchases", 0)
                if purchases == 0:
                    payload = {"error": "No purchases, cannot calculate CPA."}
                    out = json.dumps(payload)
                    return out
                cpa = spend / purchases
                payload = {"cpa": cpa}
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
                "name": "calculateAdsetCpaForDay",
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
                        },
                    },
                    "required": ["adset_id", "date"],
                },
            },
        }
