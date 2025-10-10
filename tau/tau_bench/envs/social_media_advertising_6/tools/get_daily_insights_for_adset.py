# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDailyInsightsForAdset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["adset_id", "date"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        rows = _assert_table(data, "f_insights")
        out = [r for r in rows if str(r.get("adset_id")) == str(kwargs["adset_id"]) and r.get("date") == kwargs["date"]]
        return json.dumps(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_daily_insights_for_adset",
                                                 "description": "Read f_insights for a specific day & adset.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"},
                                                                               "date": {"type": "string"}},
                                                                "required": ["adset_id", "date"]}}}
