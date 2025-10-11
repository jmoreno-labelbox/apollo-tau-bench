# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SwapAdCreatives(Tool):
    """Deactivate one ad and activate another in the same adset."""
    @staticmethod
    def invoke(data: Dict[str, Any], activate_id, pause_id) -> str:
        to_on, to_off = activate_id, pause_id
        changed = []
        for ad in list(data.get("ads", {}).values()):
            if ad.get("ad_id") == to_on:
                ad["status"] = "active"
                changed.append(ad)
            if ad.get("ad_id") == to_off:
                ad["status"] = "paused"
                changed.append(ad)
        return json.dumps(changed or {"error": "IDs not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "swap_ad_creatives",
                "description": "Deactivate one ad and activate another in the same adset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "activate_id": {"type": "string"},
                        "pause_id": {"type": "string"},
                     },
                    "required": ["activate_id", "pause_id"],

              },
           },
        }
