# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdsetSpendForDateRange(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, end_date, start_date) -> str:
        aid = adset_id
        s = start_date
        e = end_date
        sd = datetime.strptime(s, "%Y-%m-%d").date()
        ed = datetime.strptime(e, "%Y-%m-%d").date()
        tot = 0.0
        for i in list(data.get("f_insights", {}).values()):
            if i.get("adset_id") == aid:
                idate = datetime.strptime(i.get("date"), "%Y-%m-%d").date()
                if sd <= idate <= ed:
                    tot += float(i.get("spend", 0))
        return json.dumps({"adset_id": aid, "start_date": s, "end_date": e, "total_spend": round(tot, 2)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_adset_spend_for_date_range", "description": "Sums spend for a date range.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"},
                                                                             "start_date": {"type": "string"},
                                                                             "end_date": {"type": "string"}},
                                            "required": ["adset_id", "start_date", "end_date"]}}}
