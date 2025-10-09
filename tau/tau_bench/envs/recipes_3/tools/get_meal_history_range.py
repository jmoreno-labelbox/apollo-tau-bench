from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetMealHistoryRange(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], household_id: int, start_date: str, end_date: str
    ) -> str:
        mh = _get_table(data, "meal_history")
        rows = [
            h
            for h in mh
            if h.get("household_id") == household_id
            and start_date <= h.get("plan_date", "") <= end_date
        ]
        payload = {"meal_history": rows}
        out = json.dumps(payload, indent=2)
        return out
        pass
        mh = _get_table(data, "meal_history")
        rows = [
            h
            for h in mh
            if h.get("household_id") == household_id
            and start_date <= h.get("plan_date", "") <= end_date
        ]
        payload = {"meal_history": rows}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMealHistoryRange",
                "description": "Returns meal_history rows for a household in an inclusive date range (ISO yyyy-mm-dd).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["household_id", "start_date", "end_date"],
                },
            },
        }
