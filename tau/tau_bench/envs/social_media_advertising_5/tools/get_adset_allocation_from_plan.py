# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdsetAllocationFromPlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        plan_id = kwargs.get("plan_id")
        adset_id = kwargs.get("adset_id")
        for p in data.get("plans", []):
            if p.get("plan_id") == plan_id:
                for a in p.get("allocations", []):
                    if a.get("adset_id") == adset_id:
                        return json.dumps(a)
        return json.dumps({"error": f"allocation for {adset_id} not in {plan_id}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adset_allocation_from_plan",
                                                 "description": "Gets one ad set allocation from a plan.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"plan_id": {"type": "string"},
                                                                               "adset_id": {"type": "string"}},
                                                                "required": ["plan_id", "adset_id"]}}}
