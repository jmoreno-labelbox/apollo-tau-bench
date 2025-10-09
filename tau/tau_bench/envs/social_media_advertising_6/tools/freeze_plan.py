from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FreezePlan(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        plan_id: str,
        date: str,
        created_at: str,
        allocations: list[dict[str, Any]],
        author: str = None,
        checksum: str = None,
        policy_snapshot: dict[str, Any] = None,
        adset_mapping: list[dict[str, Any]] = None,
        strategies: list[dict[str, Any]] = None,
        creatives: list[dict[str, Any]] = None,
        total_budget: float = None
    ) -> str:
        """
        Construct & freeze a budget plan (category- or account-scoped).
        Accepts a subset of adsets (category-scoped) and checks against policy snapshot.
        Saves the complete plan envelope in the `plans` table indexed by `plan_id`.
        """
        pass
        import json
        from decimal import ROUND_HALF_UP, Decimal, InvalidOperation

        #--- assistance functions -------------------------------------------
        def _to_dec(x) -> Decimal:
            pass
            return Decimal(str(x))

        def _require_keys(obj: dict[str, Any], keys: list[str], ctx: str) -> str | None:
            pass
            missing = [k for k in keys if k not in obj]
            return (
                f"missing_required_keys:{ctx}:{','.join(missing)}" if missing else None
            )

        #--- necessary top-level arguments ----------------------------------
        err = _require(locals(), ["plan_id", "date", "created_at", "allocations"])
        if err:
            return _fail(err)

        plan_id: str = str(plan_id)
        created_at: str = str(created_at)  #do not interpret; consider as opaque string
        date: str = str(date)

        #Guidelines / defaults
        rules = data.get("_rules", {}) if isinstance(data, dict) else {}
        default_author = rules.get("default_author", "automation_agent")
        default_checksum = rules.get("default_checksum", "CHK001")

        author = str(author or default_author)
        checksum = str(checksum or default_checksum)

        #Policy snapshot (derived from payload or default rules)
        policy_snapshot = policy_snapshot or {}
        if not isinstance(policy_snapshot, dict):
            return _fail("invalid_policy_snapshot:not_object")

        min_alloc = float(
            policy_snapshot.get(
                "min_budget_allocation", rules.get("min_budget_allocation", 0)
            )
        )
        unit = int(
            policy_snapshot.get(
                "budget_rounding_unit", rules.get("budget_rounding_unit", 10)
            )
        )
        currency = str(policy_snapshot.get("currency", rules.get("currency", "USD")))
        timezone = str(policy_snapshot.get("timezone", rules.get("timezone", "UTC")))

        #adset_mapping: necessary for any adset present in allocations
        adset_mapping = adset_mapping or []
        if not isinstance(adset_mapping, list):
            return _fail("invalid_adset_mapping:not_array")

        #strategies: essential for any adset included in allocations
        strategies = strategies or []
        if not isinstance(strategies, list):
            return _fail("invalid_strategies:not_array")

        #creatives: mandatory for any adset listed in allocations
        creatives = creatives or []
        if not isinstance(creatives, list):
            return _fail("invalid_creatives:not_array")

        #index assistance functions
        mapping_idx = {}
        for i, m in enumerate(adset_mapping):
            if not isinstance(m, dict):
                return _fail(f"invalid_adset_mapping_row:{i}:not_object")
            need = _require_keys(
                m,
                ["adset_id", "category", "campaign_id", "name"],
                f"adset_mapping[{i}]",
            )
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
                    return _fail(
                        f"invalid_strategy_row:{i}:missing_bid_amount_for_cost_cap:{aid}"
                    )
                try:
                    _ = _to_dec(s["bid_amount"])
                except (InvalidOperation, TypeError, ValueError):
                    return _fail(
                        f"invalid_strategy_row:{i}:bid_amount_not_numeric:{aid}"
                    )
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
            #Permit any string; common values include: image, video, carousel
            if not ctype:
                return _fail(f"invalid_creative_row:{i}:empty_creative_type:{aid}")
            creat_idx[aid] = c

        #Check allocations for validity
        if not isinstance(allocations, list) or len(allocations) == 0:
            return _fail("invalid_allocations:empty")

        seen_allocs = set()
        total = Decimal("0")
        normalized_allocs: list[dict[str, Any]] = []

        for i, row in enumerate(allocations):
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
                return _fail(
                    f"invalid_allocation_row:{i}:missing_strategy_for_adset:{aid}"
                )
            if aid not in creat_idx:
                return _fail(
                    f"invalid_allocation_row:{i}:missing_creative_for_adset:{aid}"
                )

            if "budget" not in row:
                return _fail(f"invalid_allocation_row:{i}:missing_budget")

            try:
                bud = _to_dec(row["budget"])
            except (InvalidOperation, TypeError, ValueError):
                return _fail(f"invalid_allocation_row:{i}:budget_not_numeric")

            if float(bud) < min_alloc:
                return _fail(
                    f"invalid_allocation_row:{i}:below_min:{float(bud)}<{min_alloc}"
                )

            #rules for rounding
            if unit == 1:
                if bud != bud.to_integral_value(rounding=ROUND_HALF_UP):
                    return _fail(
                        f"invalid_allocation_row:{i}:must_be_integer_when_unit_1:{str(bud)}"
                    )
            else:
                #verify multiple of unit utilizing Decimal
                if (bud % _to_dec(unit)) != 0:
                    return _fail(
                        f"invalid_allocation_row:{i}:violates_rounding_unit:{unit}:{str(bud)}"
                    )

            total += bud
            normalized_allocs.append({"adset_id": aid, "budget": float(bud)})

        #If total_budget exists, ensure it aligns with the subset sum
        if total_budget is not None:
            try:
                tb = _to_dec(total_budget)
            except (InvalidOperation, TypeError, ValueError):
                return _fail("invalid_total_budget:not_numeric")
            if (tb - total).copy_abs() > Decimal("0.000001"):
                return _fail(
                    f"invalid_total_budget_mismatch:{float(tb)}!={float(total)}"
                )
            total_budget_out = float(tb)
        else:
            #obtain from subset
            total_budget_out = float(total)

        #Construct the final plan entry
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

        #Insert or update in plans table
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
        payload = {
                "ok": True,
                "plan_id": plan_id,
                "status": "frozen",
                "allocations_count": len(normalized_allocs),
                "total_budget": total_budget_out,
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FreezePlan",
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
                                "required": [
                                    "adset_id",
                                    "name",
                                    "category",
                                    "campaign_id",
                                ],
                            },
                        },
                        "strategies": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "adset_id": {"type": "string"},
                                    "bid_strategy": {
                                        "type": "string",
                                        "enum": ["lowest_cost", "cost_cap"],
                                    },
                                    "bid_amount": {"type": "number"},
                                },
                                "required": ["adset_id", "bid_strategy"],
                            },
                        },
                        "creatives": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "adset_id": {"type": "string"},
                                    "creative_type": {"type": "string"},
                                },
                                "required": ["adset_id", "creative_type"],
                            },
                        },
                        "policy_snapshot": {
                            "type": "object",
                            "properties": {
                                "min_budget_allocation": {"type": "number"},
                                "budget_rounding_unit": {"type": "integer"},
                                "currency": {"type": "string"},
                                "timezone": {"type": "string"},
                            },
                        },
                        "allocations": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "adset_id": {"type": "string"},
                                    "budget": {"type": "number"},
                                },
                                "required": ["adset_id", "budget"],
                            },
                        },
                    },
                    "required": ["plan_id", "date", "created_at", "allocations"],
                },
            },
        }
