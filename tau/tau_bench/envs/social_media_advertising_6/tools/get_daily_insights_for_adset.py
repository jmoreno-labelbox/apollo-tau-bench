from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class GetDailyInsightsForAdset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str, date: str) -> str:
        req = ["adset_id", "date"]
        err = _require({"adset_id": adset_id, "date": date}, req)
        if err:
            return _fail(err)
        rows = _assert_table(data, "f_insights")
        out = [
            r
            for r in rows
            if str(r.get("adset_id")) == str(adset_id)
            and r.get("date") == date
        ]
        payload = out
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDailyInsightsForAdset",
                "description": "Read f_insights for a specific day & adset.",
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
