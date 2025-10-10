# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdsetsByCampaignID(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("campaign_id")
        rows = [r for r in data.get("adsets", []) if r.get("campaign_id") == cid]
        return json.dumps({"adsets": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_adsets_by_campaign_id", "description": "Lists ad sets for a campaign.",
                             "parameters": {"type": "object", "properties": {"campaign_id": {"type": "string"}},
                                            "required": ["campaign_id"]}}}
