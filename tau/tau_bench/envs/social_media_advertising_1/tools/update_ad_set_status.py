# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAdSetStatus(Tool):
    """Updates the status for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        new_status = kwargs.get("new_status")
        
        adsets = data.get("adsets", [])
        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                old_status = adset['status']
                adset['status'] = new_status
                return json.dumps({
                    "status": "success",
                    "message": f"Ad set status updated from '{old_status}' to '{new_status}'"
                })

        return json.dumps({"error": f"Ad set {adset_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_adset_status",
                "description": "Updates the status for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_status": {"type": "string"}
                    },
                    "required": ["adset_id", "new_status"]
                }
            }
        }
