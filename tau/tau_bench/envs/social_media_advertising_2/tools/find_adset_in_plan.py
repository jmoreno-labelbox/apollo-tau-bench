# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindAdsetInPlan(Tool):
    """Return allocation info for one ad set from a specific plan."""

    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, plan_id) -> str:
        for plan in list(data.get("plans", {}).values()):
            if plan.get("plan_id") == plan_id:
                for a in plan.get("allocations", []):
                    if a.get("adset_id") == adset_id:
                        return json.dumps(a)
        return json.dumps({"error": f"Adset {adset_id} not in plan {plan_id}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_adset_in_plan",
                "description": "Return allocation info for a single ad set from a plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "adset_id": {"type": "string"},
                    },
                    "required": ["plan_id", "adset_id"],
                },
            },
        }
