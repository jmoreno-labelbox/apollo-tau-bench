# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetStatusForAdSet(Tool):
    """Retrieves the status for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        adsets = list(data.get("adsets", {}).values())
        
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                return json.dumps({"status": adset.get('status')})
        
        return json.dumps({"error": f"Ad set with ID '{adset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_status_for_adset",
                "description": "Retrieves the status for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }
