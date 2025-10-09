from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAdsetSpendForDateRange(Tool):
    """Computes total expenditure for an ad set across a range."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, start_date: str = None, end_date: str = None) -> str:
        start, end = (
            datetime.strptime(start_date, "%Y-%m-%d").date(),
            datetime.strptime(end_date, "%Y-%m-%d").date(),
        )
        total_spend = sum(
            i.get("spend", 0)
            for i in data.get("f_insights", {}).values()
            if i.get("adset_id") == adset_id
            and start <= datetime.strptime(i["date"], "%Y-%m-%d").date() <= end
        )
        payload = {
                "adset_id": adset_id,
                "start_date": start_date,
                "end_date": end_date,
                "total_spend": round(total_spend, 2),
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetSpendForDateRange",
                "description": "Calculates the total ad spend for a single ad set over an inclusive date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["adset_id", "start_date", "end_date"],
                },
            },
        }
