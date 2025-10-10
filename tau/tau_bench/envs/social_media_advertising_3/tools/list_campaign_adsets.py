# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCampaignAdsets(Tool):
    """List all ad sets under a campaign."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("campaign_id")
        adsets = [a for a in data.get("adsets", []) if a.get("campaign_id") == cid]
        return json.dumps({"adsets": adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_campaign_adsets",
                "description": "List all ad sets under a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }
