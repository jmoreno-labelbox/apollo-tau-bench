from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class ComputeRoas(Tool):
    """Calculate ROAS (revenue/spend) for an ad set on a specific date."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None) -> str:
        aid, date = adset_id, date
        for i in data.get("f_insights", []):
            if i.get("adset_id") == aid and i.get("date") == date:
                s, r = i.get("spend", 0), i.get("revenue", 0)
                payload = {"adset_id": aid, "roas": round(r / s, 2) if s > 0 else 0}
                out = json.dumps(payload)
                return out
        payload = {"error": "No data to calc ROAS"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeRoas",
                "description": "Compute ROAS (revenue/spend) for an adset on a date.",
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
