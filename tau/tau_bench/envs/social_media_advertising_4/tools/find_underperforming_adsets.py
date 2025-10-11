# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindUnderperformingAdsets(Tool):
    """Finds ad sets below a certain ROAS threshold."""
    @staticmethod
    def invoke(data: Dict[str, Any], date, roas_threshold) -> str:
        threshold, report_date = roas_threshold, date
        adsets = []
        for i in data.get('f_insights', []):
            if i.get('date') == report_date:
                spend, revenue = i.get('spend', 0), i.get('revenue', 0)
                roas = (revenue / spend) if spend > 0 else 0
                if spend > 0 and roas < threshold:
                    adsets.append({"adset_id": i['adset_id'], "roas": round(roas, 2)})
        return json.dumps({"underperforming_adsets": adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_underperforming_adsets", "description": "Finds all ad sets with a ROAS below a specified threshold for a given day.", "parameters": {"type": "object", "properties": {"roas_threshold": {"type": "number"}, "date": {"type": "string"}}, "required": ["roas_threshold", "date"]}}}
