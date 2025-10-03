from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class VerifyPlanAgainstAdsets(Tool):
    """Evaluate plan allocations against current adsets (active only)."""

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str) -> str:
        err = _require({"plan_id": plan_id}, ["plan_id"])
        if err:
            return _fail(err)
        plans = _assert_table(data, "plans")
        adsets = _index(_assert_table(data, "adsets"), "adset_id")
        pid = plan_id
        plan = next((p for p in plans if p.get("plan_id") == pid), None)
        if not plan:
            return _fail("plan_not_found")
        mismatches: list[dict[str, Any]] = []
        for spec in plan.get("allocations", []):
            aid = str(spec.get("adset_id"))
            a = adsets.get(aid)
            if not a:
                mismatches.append({"adset_id": aid, "issue": "missing"})
                continue
            status_val = a.get("status", "")
            if status_val is None:
                status_val = ""
            if str(status_val).lower() != "active":
                continue
            if float(a.get("daily_budget", 0.0)) != float(spec.get("budget", 0.0)):
                mismatches.append(
                    {
                        "adset_id": aid,
                        "field": "daily_budget",
                        "expected": float(spec.get("budget", 0.0)),
                        "actual": float(a.get("daily_budget", 0.0)),
                    }
                )
            if spec.get("bid_strategy") is not None and a.get(
                "bid_strategy"
            ) != spec.get("bid_strategy"):
                mismatches.append(
                    {
                        "adset_id": aid,
                        "field": "bid_strategy",
                        "expected": spec.get("bid_strategy"),
                        "actual": a.get("bid_strategy"),
                    }
                )
            if spec.get("bid_amount") is not None and a.get("bid_amount") != spec.get(
                "bid_amount"
            ):
                mismatches.append(
                    {
                        "adset_id": aid,
                        "field": "bid_amount",
                        "expected": spec.get("bid_amount"),
                        "actual": a.get("bid_amount"),
                    }
                )
        payload = {"ok": len(mismatches) == 0, "mismatches": mismatches}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "VerifyPlanAgainstAdsets",
                "description": "Compare a plan to current adsets, ignoring paused ones.",
                "parameters": {
                    "type": "object",
                    "properties": {"plan_id": {"type": "string"}},
                    "required": ["plan_id"],
                },
            },
        }
