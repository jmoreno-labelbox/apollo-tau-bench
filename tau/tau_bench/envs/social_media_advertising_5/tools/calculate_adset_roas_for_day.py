from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any

class CalculateAdsetRoasForDay(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None) -> str:
        aid = adset_id
        d = date
        for i in data.get("f_insights", []):
            if i.get("adset_id") == aid and i.get("date") == d:
                spend = i.get("spend", 0)
                revenue = i.get("revenue", 0)
                roas = round(revenue / spend, 2) if spend > 0 else 0
                payload = {"adset_id": aid, "date": d, "roas": roas}
                out = json.dumps(payload)
                return out
        payload = {"error": "roas_not_available"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateAdsetRoasForDay",
                "description": "Computes ROAS for one day.",
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
