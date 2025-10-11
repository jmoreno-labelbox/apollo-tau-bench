# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadCampaign(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], campaign_id) -> str:
        cid = campaign_id
        c = next((x for x in list(data.get("campaigns", {}).values()) if x.get("campaign_id") == cid), None)
        if not c:
            return json.dumps({"error": f"campaign_id {cid} not found"}, indent=2)
        return json.dumps(c, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "read_campaign",
                "description": "Fetch a campaign row by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "integer"}},
                    "required": ["campaign_id"],
                },
            },
        }
