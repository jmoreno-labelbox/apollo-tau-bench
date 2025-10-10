# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAdsetBudget(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        nb = float(kwargs.get("new_budget"))
        for a in list(data.get("adsets", {}).values()):
            if a.get("adset_id") == aid:
                a["daily_budget"] = nb
                a["updated_at"] = kwargs.get("updated_at")
                return json.dumps(a)
        return json.dumps({"error": f"adset {aid} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "update_adset_budget", "description": "Updates an ad set budget.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"},
                                                                             "new_budget": {"type": "number"},
                                                                             "updated_at": {"type": "string"}},
                                            "required": ["adset_id", "new_budget", "updated_at"]}}}
