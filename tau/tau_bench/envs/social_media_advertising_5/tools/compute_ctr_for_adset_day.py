# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeCtrForAdsetDay(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        d = kwargs.get("date")
        for i in data.get("f_insights", []):
            if i.get("adset_id") == aid and i.get("date") == d:
                imp = i.get("impressions", 0)
                clk = i.get("clicks", 0)
                ctr = round(clk / imp, 4) if imp > 0 else 0
                return json.dumps({"adset_id": aid, "date": d, "ctr": ctr})
        return json.dumps({"error": "ctr_not_available"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "compute_ctr_for_adset_day", "description": "Computes CTR for one day.",
                             "parameters": {"type": "object",
                                            "properties": {"adset_id": {"type": "string"}, "date": {"type": "string"}},
                                            "required": ["adset_id", "date"]}}}
