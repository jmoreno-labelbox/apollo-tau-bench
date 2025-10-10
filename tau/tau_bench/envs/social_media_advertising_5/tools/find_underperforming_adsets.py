# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindUnderperformingAdsets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        th = float(kwargs.get("roas_threshold"))
        d = kwargs.get("date")
        out = []
        for i in data.get("f_insights", []):
            if i.get("date") == d:
                spend = i.get("spend", 0)
                revenue = i.get("revenue", 0)
                roas = (revenue / spend) if spend > 0 else 0
                if spend > 0 and roas < th:
                    out.append({"adset_id": i.get("adset_id"), "roas": round(roas, 2)})
        return json.dumps({"underperforming_adsets": out})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_underperforming_adsets",
                                                 "description": "Finds ad sets below a ROAS threshold for a day.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"roas_threshold": {"type": "number"},
                                                                               "date": {"type": "string"}},
                                                                "required": ["roas_threshold", "date"]}}}
