from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAdsetAllocationFromPlan(Tool):
    """Obtains the allocation of a specific ad set from a plan."""

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, adset_id: str = None) -> str:
        for plan in data.get("plans", []):
            if plan.get("plan_id") == plan_id:
                for allocation in plan.get("allocations", []):
                    if allocation.get("adset_id") == adset_id:
                        payload = allocation
                        out = json.dumps(payload)
                        return out
        payload = {
                "error": f"Allocation for ad set '{adset_id}' not found in plan '{plan_id}'."
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetAllocationFromPlan",
                "description": "Gets the planned budget, bid, and creative strategy for a single ad set from a specific plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The ID of the plan (e.g., 'plan_2025-08-13').",
                        },
                        "adset_id": {
                            "type": "string",
                            "description": "The ID of the ad set to look up.",
                        },
                    },
                    "required": ["plan_id", "adset_id"],
                },
            },
        }
