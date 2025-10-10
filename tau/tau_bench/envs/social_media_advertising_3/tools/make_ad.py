# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MakeAd(Tool):
    """Create a new ad in an adset."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ads = list(data.get("ads", {}).values())
        new_id = str(max((int(a["ad_id"]) for a in ads), default=1000) + 1)
        ad = {
            "ad_id": new_id,
            "adset_id": kwargs.get("adset_id"),
            "name": kwargs.get("name"),
            "format": kwargs.get("format"),
            "status": "paused",
        }
        ads.append(ad)
        data["ads"] = ads
        return json.dumps(ad)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "make_ad",
                "description": "Create a new ad in a given adset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "name": {"type": "string"},
                        "format": {"type": "string"},
                    },
                    "required": ["adset_id", "name", "format"],
                },
            },
        }
