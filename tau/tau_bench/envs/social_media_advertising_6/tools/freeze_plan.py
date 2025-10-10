# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FreezePlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Compose & freeze a budget plan (category- or account-scoped).
        Accepts a subset of adsets (category-scoped) and validates against policy snapshot.
        Stores the full plan envelope in the `plans` table keyed by `plan_id`.
        """
        import json
        from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

        # --- utility functions ---------------------------------------------------------
        def _to_dec(x) -> Decimal:
            return Decimal(str(x))

        def _require_keys(obj: Dict[str, Any], keys: List[str], ctx: str) -> Optional[str]:
            missing = [k for k in keys if k not in obj]
            return f"missing_required_keys:{ctx}:{','.join(missing)}" if missing else None

        # --- necessary top-level parameters ---------------------------------
        err = _require(kwargs, ["plan_id", "date", "created_at", "allocations"])
        if err:
            return _fail(err)

        plan_id: str = str(kwargs["plan_id"])
        created_at: str = str(kwargs["created_at"])  # avoid parsing; handle as a non-interpreted string
        date: str = str(kwargs["date"])

        # Guidelines / presets
        rules = data.get("_rules", {}) if isinstance(data, dict) else {}
        default_author = rules.get("default_author", "automation_agent")
        default_checksum = rules.get("default_checksum", "CHK001")

        author = str(kwargs.get("author", default_author))
        checksum = str(kwargs.get("checksum", default_checksum))

        # Policy overview (derived from payload or standard from regulations)
        policy_snapshot = kwargs.get("policy_snapshot") or {}
        if not isinstance(policy_snapshot, dict):
            return _fail("invalid_policy_snapshot:not_object")

        min_alloc = float(policy_snapshot.get(
            "min_budget_allocation",
            rules.get("min_budget_allocation", 0)
        ))
        unit = int(policy_snapshot.get(
            "budget_rounding_unit",
            rules.get("budget_rounding_unit", 10)
        ))
        currency = str(policy_snapshot.get(
            "currency",
            rules.get("currency", "USD")
        ))
        timezone = str(policy_snapshot.get(
            "timezone",
            rules.get("timezone", "UTC")
        ))

        # adset_mapping: necessary for all adsets included in allocations
        adset_mapping = kwargs.get("adset_mapping", [])
        if not isinstance(adset_mapping, list):
            return _fail("invalid_adset_mapping:not_array")

        # strategies: necessary for any ad set included in allocations
        strategies = kwargs.get("strategies", [])
        if not isinstance(strategies, list):
            return _fail("invalid_strategies:not_array")

        # creatives: necessary for any ad set present in allocations
        creatives = kwargs.get("creatives", [])
        if not isinstance(creatives, list):
            return _fail("invalid_creatives:not_array")

        # index utilities
        mapping_idx = {}
        for i, m in enumerate(adset_mapping):
            if not isinstance(m, dict):
                return _fail(f"invalid_adset_mapping_row:{i}:not_object")
            need = _require_keys(m, ["adset_id", "category", "campaign_id", "name"], f"adset_mapping[{i}]")
            if need:
                return _fail(need)
            aid = str(m["adset_id"]).strip()
            if not aid:
                return _fail(f"invalid_adset_mapping_row:{i}:empty_adset_id")
            if aid in mapping_idx:
                return _fail(f"invalid_adset_mapping_row:{i}:duplicate_adset_id:{aid}")
            mapping_idx[aid] = m

        strat_idx = {}
        for i, s in enumerate(strategies):
            if not isinstance(s, dict):
                return _fail(f"invalid_strategy_row:{i}:not_object")
            need = _require_keys(s, ["adset_id", "bid_strategy"], f"strategies[{i}]")
            if need:
                return _fail(need)
            aid = str(s["adset_id"]).strip()
            if not aid:
                return _fail(f"invalid_strategy_row:{i}:empty_adset_id")
            if aid in strat_idx:
                return _fail(f"invalid_strategy_row:{i}:duplicate_adset_id:{aid}")
            bs = str(s["bid_strategy"])
            if bs not in ("lowest_cost", "cost_cap"):
                return _fail(f"invalid_strategy_row:{i}:unknown_bid_strategy:{bs}")
            if bs == "cost_cap":
                if "bid_amount" not in s:
                    return _fail(f"invalid_strategy_row:{i}:missing_bid_amount_for_cost_cap:{aid}")
                try:
                    _ = _to_dec(s["bid_amount"])
                except (InvalidOperation, TypeError, ValueError):
                    return _fail(f"invalid_strategy_row:{i}:bid_amount_not_numeric:{aid}")
            strat_idx[aid] = s

        creat_idx = {}
        for i, c in enumerate(creatives):
            if not isinstance(c, dict):
                return _fail(f"invalid_creative_row:{i}:not_object")
            need = _require_keys(c, ["adset_id", "creative_type"], f"creatives[{i}]")
            if need:
                return _fail(need)
            aid = str(c["adset_id"]).strip()
            if not aid:
                return _fail(f"invalid_creative_row:{i}:empty_adset_id")
            if aid in creat_idx:
                return _fail(f"invalid_creative_row:{i}:duplicate_adset_id:{aid}")
            ctype = str(c["creative_type"])
            # Accept any string; common examples include image, video, carousel.
            if not ctype:
                return _fail(f"invalid_creative_row:{i}:empty_creative_type:{aid}")
            creat_idx[aid] = c

        # Verify resource allocations.
        allocs = kwargs.get("allocations", [])
        if not isinstance(allocs, list) or len(allocs) == 0:
            return _fail("invalid_allocations:empty")

        seen_allocs = set()
        total = Decimal("0")
        normalized_allocs: List[Dict[str, Any]] = []

        for i, row in enumerate(allocs):
            if not isinstance(row, dict):
                return _fail(f"invalid_allocation_row:{i}:not_object")

            aid = str(row.get("adset_id", "")).strip()
            if not aid:
                return _fail(f"invalid_allocation_row:{i}:missing_adset_id")
            if aid in seen_allocs:
                return _fail(f"invalid_allocation_row:{i}:duplicate_adset_id:{aid}")
            seen_allocs.add(aid)

            if aid not in mapping_idx:
                return _fail(f"invalid_allocation_row:{i}:adset_not_in_mapping:{aid}")
            if aid not in strat_idx:
                return _fail(f"invalid_allocation_row:{i}:missing_strategy_for_adset:{aid}")
            if aid not in creat_idx:
                return _fail(f"invalid_allocation_row:{i}:missing_creative_for_adset:{aid}")

            if "budget" not in row:
                return _fail(f"invalid_allocation_row:{i}:missing_budget")

            try:
                bud = _to_dec(row["budget"])
            except (InvalidOperation, TypeError, ValueError):
                return _fail(f"invalid_allocation_row:{i}:budget_not_numeric")

            if float(bud) < min_alloc:
                return _fail(f"invalid_allocation_row:{i}:below_min:{float(bud)}<{min_alloc}")

            # rules for rounding
            if unit == 1:
                if bud != bud.to_integral_value(rounding=ROUND_HALF_UP):
                    return _fail(f"invalid_allocation_row:{i}:must_be_integer_when_unit_1:{str(bud)}")
            else:
                # verify unit multiplicity with Decimal
                if (bud % _to_dec(unit)) != 0:
                    return _fail(f"invalid_allocation_row:{i}:violates_rounding_unit:{unit}:{str(bud)}")

            total += bud
            normalized_allocs.append({"adset_id": aid, "budget": float(bud)})

        # If total_budget exists, it must equal the subset sum.
        if "total_budget" in kwargs and kwargs["total_budget"] is not None:
            try:
                tb = _to_dec(kwargs["total_budget"])
            except (InvalidOperation, TypeError, ValueError):
                return _fail("invalid_total_budget:not_numeric")
            if (tb - total).copy_abs() > Decimal("0.000001"):
                return _fail(f"invalid_total_budget_mismatch:{float(tb)}!={float(total)}")
            total_budget_out = float(tb)
        else:
            # obtain from a subset
            total_budget_out = float(total)

        # Create the final plan entry.
        plan_row = {
            "plan_id": plan_id,
            "date": date,
            "created_at": created_at,
            "author": author,
            "checksum": checksum,
            "total_budget": total_budget_out,
            "adset_mapping": adset_mapping,
            "strategies": strategies,
            "creatives": creatives,
            "policy_snapshot": {
                "min_budget_allocation": min_alloc,
                "budget_rounding_unit": unit,
                "currency": currency,
                "timezone": timezone,
            },
            "allocations": normalized_allocs,
            "status": "frozen",
        }

        # Insert or update records in the plans table.
        plans_tbl = _assert_table(data, "plans")
        if not isinstance(plans_tbl, list):
            return _fail("invalid_storage:plans_not_list")

        replaced = False
        for idx, row in enumerate(plans_tbl):
            if isinstance(row, dict) and row.get("plan_id") == plan_id:
                plans_tbl[idx] = plan_row
                replaced = True
                break
        if not replaced:
            plans_tbl.append(plan_row)

        return json.dumps({
            "ok": True,
            "plan_id": plan_id,
            "status": "frozen",
            "allocations_count": len(normalized_allocs),
            "total_budget": total_budget_out
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "freeze_plan",
                "description": "Compose and freeze a budget plan envelope (subset or account-scoped) with policy validation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "date": {"type": "string"},
                        "created_at": {"type": "string"},
                        "author": {"type": "string"},
                        "checksum": {"type": "string"},
                        "total_budget": {"type": "number"},
                        "adset_mapping": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "adset_id": {"type": "string"},
                                    "name": {"type": "string"},
                                    "category": {"type": "string"},
                                    "campaign_id": {"type": "string"},
                                },
                                "required": ["adset_id", "name", "category", "campaign_id"]
                            }
                        },
                        "strategies": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "adset_id": {"type": "string"},
                                    "bid_strategy": {"type": "string", "enum": ["lowest_cost", "cost_cap"]},
                                    "bid_amount": {"type": "number"}
                                },
                                "required": ["adset_id", "bid_strategy"]
                            }
                        },
                        "creatives": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "adset_id": {"type": "string"},
                                    "creative_type": {"type": "string"}
                                },
                                "required": ["adset_id", "creative_type"]
                            }
                        },
                        "policy_snapshot": {
                            "type": "object",
                            "properties": {
                                "min_budget_allocation": {"type": "number"},
                                "budget_rounding_unit": {"type": "integer"},
                                "currency": {"type": "string"},
                                "timezone": {"type": "string"},
                            }
                        },
                        "allocations": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "adset_id": {"type": "string"},
                                    "budget": {"type": "number"}
                                },
                                "required": ["adset_id", "budget"]
                            }
                        }
                    },
                    "required": ["plan_id", "date", "created_at", "allocations"]
                }
            }
        }
