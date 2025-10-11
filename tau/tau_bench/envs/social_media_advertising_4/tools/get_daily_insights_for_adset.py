# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDailyInsightsForAdset(Tool):
    """Retrieves performance metrics for an ad set."""
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, date) -> str:
        adset_id, report_date = adset_id, date
        for insight in data.get('f_insights', []):
            if insight.get('adset_id') == adset_id and insight.get('date') == report_date:
                return json.dumps(insight)
        return json.dumps({"error": "Insights not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_daily_insights_for_adset", "description": "Retrieves performance insights (spend, clicks, revenue) for one ad set on a specific date.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "date": {"type": "string"}}, "required": ["adset_id", "date"]}}}
