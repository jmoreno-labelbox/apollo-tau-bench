from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CalculateAdsetRoasForDay(Tool):
    """Computes Return On Ad Spend for an ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None) -> str:
        for insight in data.get("f_insights", {}).values():
            if (
                insight.get("adset_id") == adset_id
                and insight.get("date") == date
            ):
                spend, revenue = insight.get("spend", 0), insight.get("revenue", 0)
                roas = round(revenue / spend, 2) if spend > 0 else 0
                payload = {"adset_id": adset_id, "roas": roas}
                out = json.dumps(payload)
                return out
        payload = {"error": "Could not calculate ROAS, insights not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateAdsetRoasForDay",
                "description": "Calculates the Return On Ad Spend (Revenue / Spend) for an ad set on a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["adset_id", "date"],
                },
            },
        }
