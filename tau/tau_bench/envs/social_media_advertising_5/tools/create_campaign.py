# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCampaign(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], created_date, name, objective) -> str:
        campaigns = list(data.get("campaigns", {}).values())
        nid = max((int(c["campaign_id"]) for c in campaigns), default=0) + 1
        rec = {"campaign_id": str(nid), "name": name, "objective": objective,
               "created_date": created_date, "status": "paused"}
        campaigns.append(rec)
        data["campaigns"] = campaigns
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_campaign",
                                                 "description": "Creates a paused campaign with a provided created_date.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"name": {"type": "string"},
                                                                               "objective": {"type": "string"},
                                                                               "created_date": {"type": "string"}},
                                                                "required": ["name", "objective", "created_date"]}}}
