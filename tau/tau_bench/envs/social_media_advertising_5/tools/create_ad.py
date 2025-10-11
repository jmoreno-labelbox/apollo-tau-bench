# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAd(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, creative_type, name, start_date) -> str:
        ads = list(data.get("ads", {}).values())
        nid = max((int(a["ad_id"]) for a in ads), default=1100) + 1
        rec = {"ad_id": str(nid), "adset_id": adset_id, "name": name,
               "creative_type": creative_type, "status": "paused", "start_date": start_date,
               "end_date": None}
        ads.append(rec)
        data["ads"] = ads
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "create_ad", "description": "Creates a paused ad in an ad set.",
                             "parameters": {"type": "object",
                                            "properties": {"adset_id": {"type": "string"}, "name": {"type": "string"},
                                                           "creative_type": {"type": "string"},
                                                           "start_date": {"type": "string"}},
                                            "required": ["adset_id", "name", "creative_type", "start_date"]}}}
