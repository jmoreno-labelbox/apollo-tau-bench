# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyPlanAllocations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["plan_id", "timestamp", "request_id"])
        if err:
            return _fail(err)

        plan_id   = str(kwargs["plan_id"])
        timestamp = str(kwargs["timestamp"])
        request_id = str(kwargs["request_id"])

        # Tables
        plans_tbl   = _assert_table(data, "plans")           # frozen plan envelopes
        adsets_tbl  = _assert_table(data, "adsets")

        # Load plan
        plan = next((p for p in plans_tbl if str(p.get("plan_id")) == plan_id), None)
        if not plan:
            return _fail(f"plan_not_found:{plan_id}")

        # Policy snapshot (with safe defaults)
        policy = plan.get("policy_snapshot", {}) or {}
        min_alloc = float(policy.get("min_budget_allocation", 0.0))
        unit = float(policy.get("budget_rounding_unit", 1.0))

        # Utility: rounding to unit (symmetric nearest)
        def round_to_unit(x: float, u: float) -> float:
            if u <= 0:
                return float(x)
            return round(float(x) / u) * u

        # Index plan strategies by adset_id for quick lookup
        plan_strat_by_id: Dict[str, Dict[str, Any]] = {}
        for s in plan.get("strategies", []) or []:
            aid = str(s.get("adset_id"))
            if aid:
                plan_strat_by_id[aid] = s

        # Track results
        changed_ids: List[str] = []
        noop_ids: List[str] = []
        noop_details: List[Dict[str, str]] = []

        # Apply per allocation
        for alloc in plan.get("allocations", []) or []:
            aid = str(alloc.get("adset_id"))
            if not aid:
                # Skip silently if malformed row (keeps backward-compat)
                continue

            # Find current adset
            ad = next((a for a in adsets_tbl if str(a.get("adset_id")) == aid), None)
            if not ad:
                # If adset is missing, we cannot apply; treat as NOOP with a stable reason
                noop_ids.append(aid)
                noop_details.append({"adset_id": aid, "reason": "already_in_target_state"})
                continue

            # Planned vs current budget (rounded)
            planned_budget_raw = float(alloc.get("budget", ad.get("daily_budget", 0.0)))
            planned_budget = round_to_unit(planned_budget_raw, unit)
            current_budget = round_to_unit(float(ad.get("daily_budget", 0.0)), unit)

            # Planned vs current strategy
            ps = plan_strat_by_id.get(aid, {})
            planned_strategy = str(ps.get("bid_strategy", ad.get("bid_strategy")))
            planned_bid_amount = ps.get("bid_amount", ad.get("bid_amount"))
            # Normalize planned_bid_amount to float or None
            planned_bid_amount = float(planned_bid_amount) if planned_bid_amount is not None else None

            current_strategy = str(ad.get("bid_strategy"))
            current_bid_amount = ad.get("bid_amount")
            current_bid_amount = float(current_bid_amount) if current_bid_amount is not None else None

            # Guardrail: below min allocation → NOOP
            if planned_budget < min_alloc:
                noop_ids.append(aid)
                noop_details.append({"adset_id": aid, "reason": "below_min_budget_allocation"})
                continue

            # Determine if anything changes (respect rounding)
            budget_change = (planned_budget != current_budget)
            if planned_strategy == "lowest_cost":
                strategy_change = (current_strategy != "lowest_cost")
            else:
                # cost_cap or other strategies that include a bid amount
                strategy_change = not (
                    current_strategy == planned_strategy and current_bid_amount == planned_bid_amount
                )

            if not budget_change and not strategy_change:
                # Nothing to do
                noop_ids.append(aid)
                noop_details.append({"adset_id": aid, "reason": "already_in_target_state"})
                continue

            # Apply changes
            if budget_change:
                ad["daily_budget"] = planned_budget
            if strategy_change:
                ad["bid_strategy"] = planned_strategy
                # Only store bid_amount for cost_cap (or when planned provides one)
                if planned_strategy == "cost_cap":
                    ad["bid_amount"] = planned_bid_amount
                else:
                    ad["bid_amount"] = None

            # Touch metadata
            ad["updated_at"] = timestamp
            ad["rev"] = _i(ad.get("rev"), 0) + 1

            changed_ids.append(aid)

        # Deterministic sorting by adset_id (numeric if possible)
        def _sort_key(x: str) -> Tuple[int, str]:
            try:
                return (0, int(x))
            except Exception:
                return (1, x)

        changed_ids_sorted = sorted(set(changed_ids), key=_sort_key)
        noop_ids_sorted = sorted(set(noop_ids), key=_sort_key)
        noop_details_sorted = sorted(
            [{"adset_id": nd["adset_id"], "reason": nd["reason"]} for nd in noop_details],
            key=lambda d: _sort_key(d["adset_id"])
        )

        result = {
            "plan_id": plan_id,
            "applied_adsets": changed_ids_sorted,
            "applied_adsets_count": len(changed_ids_sorted),
            "noops_skipped": noop_ids_sorted,          # legacy field (kept)
            "noops_details": noop_details_sorted,      # NEW: explicit reasons
            "timestamp": timestamp,
            "request_id": request_id,
        }
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "apply_plan_allocations",
            "description": "Apply a frozen allocation plan to adsets; returns applied adsets, NOOPs (with reasons), and audit metadata.",
            "parameters": {"type": "object",
                "properties": {
                    "plan_id": {"type": "string"},
                    "timestamp": {"type": "string"},
                    "request_id": {"type": "string"}
                },
                "required": ["plan_id", "timestamp", "request_id"]
            }
        }}
