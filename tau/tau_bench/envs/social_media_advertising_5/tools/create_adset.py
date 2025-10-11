# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAdset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], bid_amount, bid_strategy, campaign_id, category, daily_budget, name, updated_at) -> str:
        adsets = list(data.get("adsets", {}).values())
        nid = max((int(a["adset_id"]) for a in adsets), default=100) + 1
        rec = {"adset_id": str(nid), "campaign_id": campaign_id, "name": name,
               "category": category, "daily_budget": daily_budget,
               "bid_strategy": bid_strategy, "bid_amount": bid_amount, "status": "paused",
               "updated_at": updated_at}
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
