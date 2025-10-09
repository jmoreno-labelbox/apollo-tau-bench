from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAdsetSpendForDateRange(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, start_date: str = None, end_date: str = None) -> str:
        aid = adset_id
        s = start_date
        e = end_date
        sd = datetime.strptime(s, "%Y-%m-%d").date()
        ed = datetime.strptime(e, "%Y-%m-%d").date()
        tot = 0.0
        for i in data.get("f_insights", {}).values():
            if i.get("adset_id") == aid:
                idate = datetime.strptime(i.get("date"), "%Y-%m-%d").date()
                if sd <= idate <= ed:
                    tot += float(i.get("spend", 0))
        payload = {
                "adset_id": aid,
                "start_date": s,
                "end_date": e,
                "total_spend": round(tot, 2),
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
                "description": "Sums spend for a date range.",
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
