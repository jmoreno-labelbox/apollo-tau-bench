# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAdsInAdset(Tool):
    """List all ads inside an adset."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        ads = [ad for ad in list(data.get("ads", {}).values()) if ad.get("adset_id") == aid]
        return json.dumps({"ads": ads})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_ads_in_adset",
                "description": "List all ads inside a given adset.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }
