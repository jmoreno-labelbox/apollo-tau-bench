# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalcRoas(Tool):
    """Compute ROAS (revenue/spend) for an adset on a date."""
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, date) -> str:
        aid, date = adset_id, date
        for i in data.get("f_insights", []):
            if i.get("adset_id") == aid and i.get("date") == date:
                s, r = i.get("spend", 0), i.get("revenue", 0)
                return json.dumps({"adset_id": aid, "roas": round(r / s, 2) if s > 0 else 0})
        return json.dumps({"error": "No data to calc ROAS"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calc_roas",
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
