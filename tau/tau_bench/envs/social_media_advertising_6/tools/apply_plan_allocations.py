from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class ApplyPlanAllocations(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str, timestamp: str, request_id: str) -> str:
        err = _require({"plan_id": plan_id, "timestamp": timestamp, "request_id": request_id}, ["plan_id", "timestamp", "request_id"])
        if err:
            return _fail(err)

        # Data Tables
        plans_tbl = _assert_table(data, "plans")  # frozen plan packages
        adsets_tbl = _assert_table(data, "adsets")

        # Retrieve plan
        plan = next((p for p in plans_tbl if str(p.get("plan_id")) == plan_id), None)
        if not plan:
            return _fail(f"plan_not_found:{plan_id}")

        # Policy snapshot (with secure defaults)
        policy = plan.get("policy_snapshot", {}) or {}
        min_alloc = float(policy.get("min_budget_allocation", 0.0))
        unit = float(policy.get("budget_rounding_unit", 1.0))

        # Utility: rounding to unit (symmetric nearest)
        def round_to_unit(x: float, u: float) -> float:
            if u is None or u <= 0:
                return float(x)
            return round(float(x) / u) * u

        # Organize plan strategies by adset_id for fast access
        plan_strat_by_id: dict[str, dict[str, Any]] = {}
        for s in plan.get("strategies", []) or []:
            aid = str(s.get("adset_id"))
            if aid:
                plan_strat_by_id[aid] = s

        # Monitor outcomes
        changed_ids: list[str] = []
        noop_ids: list[str] = []
        noop_details: list[dict[str, str]] = []

        # Implement for each allocation
        for alloc in plan.get("allocations", []) or []:
            aid = str(alloc.get("adset_id"))
            if not aid:
                # Silently bypass if row is malformed (maintains backward compatibility)
                continue

            # Locate current adset
            ad = next((a for a in adsets_tbl if str(a.get("adset_id")) == aid), None)
            if not ad:
                # If adset is absent, we cannot implement; consider as NOOP with a consistent reason
                noop_ids.append(aid)
                noop_details.append(
                    {"adset_id": aid, "reason": "already_in_target_state"}
                )
                continue

            # Projected vs current budget (rounded)
            planned_budget_raw = float(alloc.get("budget", ad.get("daily_budget", 0.0)))
            planned_budget = round_to_unit(planned_budget_raw, unit)
            current_budget = round_to_unit(float(ad.get("daily_budget", 0.0)), unit)

            # Projected vs current strategy
            ps = plan_strat_by_id.get(aid, {})
            planned_strategy = str(ps.get("bid_strategy", ad.get("bid_strategy")))
            planned_bid_amount = ps.get("bid_amount", ad.get("bid_amount"))
            # Standardize planned_bid_amount to float or None
            planned_bid_amount = (
                float(planned_bid_amount) if planned_bid_amount is not None else None
            )

            current_strategy = str(ad.get("bid_strategy"))
            current_bid_amount = ad.get("bid_amount")
            current_bid_amount = (
                float(current_bid_amount) if current_bid_amount is not None else None
            )

            # Guardrail: below minimum allocation → NOOP
            if planned_budget < min_alloc:
                noop_ids.append(aid)
                noop_details.append(
                    {"adset_id": aid, "reason": "below_min_budget_allocation"}
                )
                continue

            # Assess if any changes occur (consider rounding)
            budget_change = planned_budget != current_budget
            if planned_strategy == "lowest_cost":
                strategy_change = current_strategy != "lowest_cost"
            else:
                # cost_cap or other strategies that involve a bid amount
                strategy_change = not (
                    current_strategy == planned_strategy
                    and current_bid_amount == planned_bid_amount
                )

            if not budget_change and not strategy_change:
                # No actions required
                noop_ids.append(aid)
                noop_details.append(
                    {"adset_id": aid, "reason": "already_in_target_state"}
                )
                continue

            # Implement modifications
            if budget_change:
                ad["daily_budget"] = planned_budget
            if strategy_change:
                ad["bid_strategy"] = planned_strategy
                # Store bid_amount solely for cost_cap (or when planned specifies one)
                if planned_strategy == "cost_cap":
                    ad["bid_amount"] = planned_bid_amount
                else:
                    ad["bid_amount"] = None

            # Update metadata
            ad["updated_at"] = timestamp
            ad["rev"] = _i(ad.get("rev"), 0) + 1

            changed_ids.append(aid)

        # Consistent sorting by adset_id (numeric if feasible)
        def _sort_key(x: str) -> tuple[int, str]:
            try:
                return (0, int(x))
            except Exception:
                return (1, x)

        changed_ids_sorted = sorted(set(changed_ids), key=_sort_key)
        noop_ids_sorted = sorted(set(noop_ids), key=_sort_key)
        noop_details_sorted = sorted(
            [
                {"adset_id": nd["adset_id"], "reason": nd["reason"]}
                for nd in noop_details
            ],
            key=lambda d: _sort_key(d["adset_id"]),
        )

        result = {
            "plan_id": plan_id,
            "applied_adsets": changed_ids_sorted,
            "applied_adsets_count": len(changed_ids_sorted),
            "noops_skipped": noop_ids_sorted,  # legacy field (retained)
            "noops_details": noop_details_sorted,  # NEW: clear reasons
            "timestamp": timestamp,
            "request_id": request_id,
        }
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyPlanAllocations",
                "description": "Apply a frozen allocation plan to adsets; returns applied adsets, NOOPs (with reasons), and audit metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["plan_id", "timestamp", "request_id"],
                },
            },
        }
