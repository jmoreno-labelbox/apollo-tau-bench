# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCampaignStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], campaign_id, status) -> str:
        cid = campaign_id
        st = status
        for c in list(data.get("campaigns", {}).values()):
            if c.get("campaign_id") == cid:
                c["status"] = st
                return json.dumps(c)
        return json.dumps({"error": f"campaign {cid} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "update_campaign_status", "description": "Updates campaign status.",
                             "parameters": {"type": "object", "properties": {"campaign_id": {"type": "string"},
                                                                             "status": {"type": "string"}},
                                            "required": ["campaign_id", "status"]}}}
