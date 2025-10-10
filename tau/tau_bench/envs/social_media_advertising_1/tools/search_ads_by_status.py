# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchAdsByStatus(Tool):
    """Searches for ads with a specific status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        ads = list(data.get("ads", {}).values())
        matching_ads = []
        
        for ad in ads:
            if ad.get("status") == status:
                matching_ads.append(ad.get("ad_id"))
        
        return json.dumps({"ad_ids": matching_ads})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_ads_by_status",
                "description": "Searches for ads with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status to search for (e.g., active, paused, archived).",
                        }
                    },
                    "required": ["status"],
                },
            },
        }
