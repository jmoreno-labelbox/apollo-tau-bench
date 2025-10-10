# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateAdsetRoasForDay(Tool):
    """Calculates Return On Ad Spend for an ad set."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id, report_date = kwargs.get("adset_id"), kwargs.get("date")
        for insight in data.get('f_insights', []):
            if insight.get('adset_id') == adset_id and insight.get('date') == report_date:
                spend, revenue = insight.get('spend', 0), insight.get('revenue', 0)
                roas = round(revenue / spend, 2) if spend > 0 else 0
                return json.dumps({"adset_id": adset_id, "roas": roas})
        return json.dumps({"error": "Could not calculate ROAS, insights not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "calculate_adset_roas_for_day", "description": "Calculates the Return On Ad Spend (Revenue / Spend) for an ad set on a specific date.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "date": {"type": "string"}}, "required": ["adset_id", "date"]}}}
