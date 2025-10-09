from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class GetCampaignByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str) -> str:
        err = _require({"name": name}, ["name"])
        if err:
            return _fail(err)
        rows = _assert_table(data, "campaigns")
        for r in rows:
            if r.get("name") == name:
                payload = r
                out = json.dumps(payload)
                return out
        return _fail("campaign_not_found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCampaignByName",
                "description": "Find a campaign by exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
