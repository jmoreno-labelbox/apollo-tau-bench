# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDailyInsightsForAdset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, date) -> str:
        aid = adset_id
        d = date
        for i in list(data.get("f_insights", {}).values()):
            if i.get("adset_id") == aid and i.get("date") == d:
                return json.dumps(i)
        return json.dumps({"error": "insights_not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_daily_insights_for_adset",
                                                 "description": "Gets insights for one ad set on a date.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"},
                                                                               "date": {"type": "string"}},
                                                                "required": ["adset_id", "date"]}}}
