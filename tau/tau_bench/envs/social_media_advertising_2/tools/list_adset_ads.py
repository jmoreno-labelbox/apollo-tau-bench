# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAdsetAds(Tool):
    """List all ads inside an adset."""

    @staticmethod
    def invoke(data: Dict[str, Any], adset_id) -> str:
        aid = adset_id
        ads = [ad for ad in list(data.get("ads", {}).values()) if ad.get("adset_id") == aid]
        return json.dumps({"ads": ads})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_adset_ads",
                "description": "List all ads inside a given adset.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }
