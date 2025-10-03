from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any

class ValidateAllocationsAgainstPolicy(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], total_budget: float, allocations: list = None) -> str:
        if allocations is None:
            allocations = []
        params = {
            p["param_name"]: p["param_value"] for p in data.get("policy_params", [])
        }
        min_alloc = float(params.get("min_budget_allocation", "0"))
        max_total = float(params.get("max_daily_budget_total", "1e15"))
        strategies = _as_list_literal(params.get("canonical_bid_strategies", "[]"))
        creatives = _as_list_literal(params.get("canonical_creative_types", "[]"))
        s = 0.0
        issues = []
        for a in allocations:
            b = float(a.get("budget", 0))
            s += b
            bs = a.get("bid_strategy")
            ct = a.get("creative_type")
            if b < min_alloc:
                issues.append(
                    {"adset_id": a.get("adset_id"), "issue": "budget_below_min"}
                )
            if bs not in strategies:
                issues.append(
                    {"adset_id": a.get("adset_id"), "issue": "invalid_strategy"}
                )
            if ct not in creatives:
                issues.append(
                    {"adset_id": a.get("adset_id"), "issue": "invalid_creative"}
                )
            if bs == "lowest_cost" and a.get("bid_amount") is not None:
                issues.append(
                    {
                        "adset_id": a.get("adset_id"),
                        "issue": "lowest_cost_requires_null_bid",
                    }
                )
            if bs in ("cost_cap", "bid_cap") and a.get("bid_amount") is None:
                issues.append(
                    {"adset_id": a.get("adset_id"), "issue": "missing_bid_amount"}
                )
        if abs(s - float(total_budget)) > 1e-6:
            issues.append(
                {
                    "issue": "total_budget_mismatch",
                    "provided": total_budget,
                    "computed": s,
                }
            )
        if s > max_total:
            issues.append(
                {
                    "issue": "total_budget_exceeds_max",
                    "provided": total_budget,
                    "max": max_total,
                }
            )
        payload = {"valid": len(issues) == 0, "issues": issues}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateAllocationsAgainstPolicy",
                "description": "Validates a plan allocation list against policy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "total_budget": {"type": "number"},
                        "allocations": {"type": "array"},
                    },
                    "required": ["total_budget", "allocations"],
                },
            },
        }
