# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAdStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_id = kwargs.get("ad_id")
        st = kwargs.get("status")
        for ad in list(data.get("ads", {}).values()):
            if ad.get("ad_id") == ad_id:
                ad["status"] = st
                return json.dumps(ad)
        return json.dumps({"error": f"ad {ad_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_ad_status", "description": "Updates ad status.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"ad_id": {"type": "string"},
                                                                               "status": {"type": "string"}},
                                                                "required": ["ad_id", "status"]}}}
