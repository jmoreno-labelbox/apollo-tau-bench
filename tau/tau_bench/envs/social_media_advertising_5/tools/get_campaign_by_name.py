# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCampaignByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        n = kwargs.get("name")
        for c in list(data.get("campaigns", {}).values()):
            if c.get("name") == n:
                return json.dumps(c)
        return json.dumps({"error": f"campaign {n} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_campaign_by_name", "description": "Retrieves a campaign by name.",
                             "parameters": {"type": "object", "properties": {"name": {"type": "string"}},
                                            "required": ["name"]}}}
