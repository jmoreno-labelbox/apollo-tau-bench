# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdsByAdsetID(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        rows = [r for r in list(data.get("ads", {}).values()) if r.get("adset_id") == aid]
        return json.dumps({"ads": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_ads_by_adset_id", "description": "Lists ads by ad set.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"}},
                                                                "required": ["adset_id"]}}}
