# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCampaignByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name) -> str:
        err = _require(kwargs, ["name"])
        if err: return _fail(err)
        rows = _assert_table(data, "campaigns")
        for r in rows:
            if r.get("name") == name:
                return json.dumps(r)
        return _fail("campaign_not_found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_campaign_by_name", "description": "Find a campaign by exact name.",
                             "parameters": {"type": "object", "properties": {"name": {"type": "string"}},
                                            "required": ["name"]}}}
