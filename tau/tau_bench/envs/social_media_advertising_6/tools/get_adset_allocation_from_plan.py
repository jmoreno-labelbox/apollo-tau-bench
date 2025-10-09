from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class GetAdsetAllocationFromPlan(Tool):
    """Provide the allocation entry for a specified adset_id within a plan_id."""

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str, adset_id: int) -> str:
        err = _require({"plan_id": plan_id, "adset_id": adset_id}, ["plan_id", "adset_id"])
        if err:
            return _fail(err)
        plans = _assert_table(data, "plans")
        pid = plan_id
        aid = str(adset_id)
        for p in plans:
            if p.get("plan_id") == pid:
                for row in p.get("allocations", []):
                    if str(row.get("adset_id")) == aid:
                        payload = row
                        out = json.dumps(payload)
                        return out
                return _fail("allocation_not_found")
        return _fail("plan_not_found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAdsetAllocationFromPlan",
                "description": "Get the planned allocation for an adset in a plan.",
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
