# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AdsetRangeSpend(Tool):
    """Return total spend for an adset across a date range."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid, start, end = kwargs.get("adset_id"), kwargs.get("start_date"), kwargs.get("end_date")
        s, e = datetime.strptime(start, "%Y-%m-%d").date(), datetime.strptime(end, "%Y-%m-%d").date()
        total = sum(
            i.get("spend", 0)
            for i in data.get("insights", [])
            if i.get("adset_id") == aid and s <= datetime.strptime(i["date"], "%Y-%m-%d").date() <= e
        )
        return json.dumps({"adset_id": aid, "total_spend": total, "range": [start, end]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "adset_range_spend",
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
