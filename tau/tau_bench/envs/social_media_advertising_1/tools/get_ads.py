# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAds(Tool):
    """Retrieves all ad IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ads = list(data.get("ads", {}).values())
        ids_ = []
        for i in ads:
            ids_ += [i.get("ad_id")]
        return json.dumps({"ad_ids": ids_})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_ads",
                "description": "Retrieves all ad IDs.",
                "parameters": {},
            },
        }
