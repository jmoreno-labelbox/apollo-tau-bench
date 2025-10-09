from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetDailyAdsetInsights(Tool):
    """Provide expenditure/clicks/revenue for an ad set on a specific date."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None, status: Any = None) -> str:
        import json

        if not adset_id or not date:
            payload = {"success": False, "error": "adset_id and date are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        hits = [
            i
            for i in data.get("insights", [])
            if i.get("adset_id") == adset_id and i.get("date") == date
        ]
        if not hits:
            payload = {
                    "success": True,
                    "adset_id": adset_id,
                    "date": date,
                    "rows": [],
                    "count": 0,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {
                "success": True,
                "adset_id": adset_id,
                "date": date,
                "rows": hits,
                "count": len(hits),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDailyAdsetInsights",
                "description": "Return spend/clicks/revenue for an adset on a given date.",
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
