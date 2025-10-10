# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetAdStatus(Tool):
    """Pause or activate a single ad by ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_id, new_status = kwargs.get("ad_id"), kwargs.get("status")
        for ad in list(data.get("ads", {}).values()):
            if ad.get("ad_id") == ad_id:
                ad["status"] = new_status
                return json.dumps(ad)
        return json.dumps({"error": f"Ad {ad_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_ad_status",
                "description": "Pause or activate a single ad by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["ad_id", "status"],
                },
            },
        }
