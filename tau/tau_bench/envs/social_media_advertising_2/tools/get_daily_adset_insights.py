# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDailyAdsetInsights(Tool):
    """Return spend/clicks/revenue for an adset on a date."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        import json
        aid, date = kwargs.get("adset_id"), kwargs.get("date")
        if not aid or not date:
            return json.dumps({"success": False, "error": "adset_id and date are required"}, indent=2)

        hits = [i for i in list(data.get("insights", {}).values()) if i.get("adset_id") == aid and i.get("date") == date]
        if not hits:
            return json.dumps({"success": True, "adset_id": aid, "date": date, "rows": [], "count": 0}, indent=2)

        return json.dumps({"success": True, "adset_id": aid, "date": date, "rows": hits, "count": len(hits)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_daily_adset_insights",
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
