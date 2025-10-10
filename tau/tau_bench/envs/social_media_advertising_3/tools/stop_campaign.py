# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class StopCampaign(Tool):
    """Pause a campaign by ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], campaign_id) -> str:
        cid = campaign_id
        for c in list(data.get("campaigns", {}).values()):
            if c.get("campaign_id") == cid:
                c["status"] = "paused"
                return json.dumps(c)
        return json.dumps({"error": f"Campaign {cid} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "stop_campaign",
                "description": "Pause a campaign by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }
