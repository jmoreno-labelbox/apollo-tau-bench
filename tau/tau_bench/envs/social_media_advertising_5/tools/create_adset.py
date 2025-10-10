# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAdset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adsets = data.get("adsets", [])
        nid = max((int(a["adset_id"]) for a in adsets), default=100) + 1
        rec = {"adset_id": str(nid), "campaign_id": kwargs.get("campaign_id"), "name": kwargs.get("name"),
               "category": kwargs.get("category"), "daily_budget": kwargs.get("daily_budget"),
               "bid_strategy": kwargs.get("bid_strategy"), "bid_amount": kwargs.get("bid_amount"), "status": "paused",
               "updated_at": kwargs.get("updated_at")}
        adsets.append(rec)
        data["adsets"] = adsets
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_adset", "description": "Creates a paused ad set.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"campaign_id": {"type": "string"},
                                                                               "name": {"type": "string"},
                                                                               "category": {"type": "string"},
                                                                               "daily_budget": {"type": "number"},
                                                                               "bid_strategy": {"type": "string"},
                                                                               "bid_amount": {"type": "number"},
                                                                               "updated_at": {"type": "string"}},
                                                                "required": ["campaign_id", "name", "category",
                                                                             "daily_budget", "bid_strategy",
                                                                             "updated_at"]}}}
