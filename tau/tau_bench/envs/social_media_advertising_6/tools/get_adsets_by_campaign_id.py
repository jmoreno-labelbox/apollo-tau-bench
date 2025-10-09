from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class GetAdsetsByCampaignID(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str) -> str:
        err = _require({"campaign_id": campaign_id}, ["campaign_id"])
        if err:
            return _fail(err)
        rows = _assert_table(data, "adsets")
        payload = [r for r in rows.values() if str(r.get("campaign_id")) == str(campaign_id)]
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAdsetsByCampaignId",
                "description": "List adsets by campaign_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }
