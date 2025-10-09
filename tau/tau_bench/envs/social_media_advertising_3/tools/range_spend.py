from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RangeSpend(Tool):
    """Provide the total expenditure for an ad set over a specified date range."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, start_date: str = None, end_date: str = None,
    campaign_id: Any = None,
    ) -> str:
        aid, start, end = adset_id, start_date, end_date
        s, e = (
            datetime.strptime(start, "%Y-%m-%d").date(),
            datetime.strptime(end, "%Y-%m-%d").date(),
        )
        total = sum(
            i.get("spend", 0)
            for i in data.get("insights", {}).values()
            if i.get("adset_id") == aid
            and s <= datetime.strptime(i["date"], "%Y-%m-%d").date() <= e
        )
        payload = {"adset_id": aid, "total_spend": total, "range": [start, end]}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RangeSpend",
                "description": "Return total spend for an adset across a date range.",
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
