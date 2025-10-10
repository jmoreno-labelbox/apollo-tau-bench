# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdsetAllocationFromPlan(Tool):
    """Retrieves a specific ad set's allocation from a plan."""
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, plan_id) -> str:
        for plan in data.get('plans', []):
            if plan.get('plan_id') == plan_id:
                for allocation in plan.get('allocations', []):
                    if allocation.get('adset_id') == adset_id:
                        return json.dumps(allocation)
        return json.dumps({"error": f"Allocation for ad set '{adset_id}' not found in plan '{plan_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adset_allocation_from_plan", "description": "Gets the planned budget, bid, and creative strategy for a single ad set from a specific plan.", "parameters": {"type": "object", "properties": {"plan_id": {"type": "string", "description": "The ID of the plan (e.g., 'plan_2025-08-13')."}, "adset_id": {"type": "string", "description": "The ID of the ad set to look up."}}, "required": ["plan_id", "adset_id"]}}}
