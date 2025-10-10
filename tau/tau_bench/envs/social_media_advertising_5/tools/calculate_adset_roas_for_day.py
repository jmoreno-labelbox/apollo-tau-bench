# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateAdsetRoasForDay(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, date) -> str:
        aid = adset_id
        d = date
        for i in list(data.get("f_insights", {}).values()):
            if i.get("adset_id") == aid and i.get("date") == d:
                spend = i.get("spend", 0)
                revenue = i.get("revenue", 0)
                roas = round(revenue / spend, 2) if spend > 0 else 0
                return json.dumps({"adset_id": aid, "date": d, "roas": roas})
        return json.dumps({"error": "roas_not_available"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "calculate_adset_roas_for_day", "description": "Computes ROAS for one day.",
                             "parameters": {"type": "object",
                                            "properties": {"adset_id": {"type": "string"}, "date": {"type": "string"}},
                                            "required": ["adset_id", "date"]}}}
