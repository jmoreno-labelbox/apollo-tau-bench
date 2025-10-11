# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdsByAdsetID(Tool):
    """Retrieves all ads within a specific ad set."""
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id) -> str:
        ads = [ad for ad in list(data.get('ads', {}).values()) if ad.get('adset_id') == adset_id]
        return json.dumps({"ads": ads})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_ads_by_adset_id", "description": "Retrieves a list of all ads that belong to a specific ad set ID.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}}, "required": ["adset_id"]}}}
