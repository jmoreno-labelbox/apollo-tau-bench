# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RotateAdCreative(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        to_act = kwargs.get("ad_id_to_activate")
        to_pause = kwargs.get("ad_id_to_pause")
        ok_a = False
        ok_p = False
        for ad in list(data.get("ads", {}).values()):
            if ad.get("ad_id") == to_act:
                ad["status"] = "active"
                ok_a = True
            if ad.get("ad_id") == to_pause:
                ad["status"] = "paused"
                ok_p = True
        if ok_a and ok_p:
            return json.dumps({"status": "success"})
        return json.dumps({"error": "ids_not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "rotate_ad_creative", "description": "Activates one ad and pauses another.",
                             "parameters": {"type": "object", "properties": {"ad_id_to_activate": {"type": "string"},
                                                                             "ad_id_to_pause": {"type": "string"}},
                                            "required": ["ad_id_to_activate", "ad_id_to_pause"]}}}
