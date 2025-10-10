# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchAdSetsByStatus(Tool):
    """Searches for ad sets with a specific status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        adsets = data.get("adsets", [])
        matching_adsets = []
        
        for adset in adsets:
            if adset.get("status") == status:
                matching_adsets.append(adset.get("adset_id"))
        
        return json.dumps({"adset_ids": matching_adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_adsets_by_status",
                "description": "Searches for ad sets with a specific status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status to search for (e.g., active, paused).",
                        }
                    },
                    "required": ["status"],
                },
            },
        }
