# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdsetSpendForDateRange(Tool):
    """Calculates total spend for an ad set over a range."""
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, end_date, start_date) -> str:
        adset_id, start_str, end_str = adset_id, start_date, end_date
        start, end = datetime.strptime(start_str, "%Y-%m-%d").date(), datetime.strptime(end_str, "%Y-%m-%d").date()
        total_spend = sum(i.get('spend', 0) for i in data.get('f_insights', []) if i.get('adset_id') == adset_id and start <= datetime.strptime(i['date'], "%Y-%m-%d").date() <= end)
        return json.dumps({"adset_id": adset_id, "start_date": start_str, "end_date": end_str, "total_spend": round(total_spend, 2)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adset_spend_for_date_range", "description": "Calculates the total ad spend for a single ad set over an inclusive date range.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "start_date": {"type": "string"}, "end_date": {"type": "string"}}, "required": ["adset_id", "start_date", "end_date"]}}}
