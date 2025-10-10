# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdsetsByCampaignID(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["campaign_id"])
        if err: return _fail(err)
        rows = _assert_table(data, "adsets")
        return json.dumps([r for r in rows if str(r.get("campaign_id")) == str(kwargs["campaign_id"])])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_adsets_by_campaign_id", "description": "List adsets by campaign_id.",
                             "parameters": {"type": "object", "properties": {"campaign_id": {"type": "string"}},
                                            "required": ["campaign_id"]}}}
