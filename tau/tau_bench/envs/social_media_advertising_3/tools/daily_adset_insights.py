from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class DailyAdsetInsights(Tool):
    """Provide spend/clicks/revenue data for an ad set on a specific date."""

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
                "name": "DailyAdsetInsights",
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
