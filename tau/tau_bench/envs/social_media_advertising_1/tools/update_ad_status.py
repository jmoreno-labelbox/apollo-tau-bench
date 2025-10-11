# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAdStatus(Tool):
    """Updates the status for a specific ad."""

    @staticmethod
    def invoke(data: Dict[str, Any], ad_id, new_status) -> str:
        
        ads = list(data.get("ads", {}).values())
        for ad in ads:
            if ad.get("ad_id") == ad_id:
                old_status = ad['status']
                ad['status'] = new_status
                return json.dumps({
                    "status": "success",
                    "message": f"Ad status updated from '{old_status}' to '{new_status}'"
                })

        return json.dumps({"error": f"Ad {ad_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_ad_status",
                "description": "Updates the status for a specific ad.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {"type": "string"},
                        "new_status": {"type": "string"}
                    },
                    "required": ["ad_id", "new_status"]
                }
            }
        }
