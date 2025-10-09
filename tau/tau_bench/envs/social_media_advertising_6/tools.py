import copy
import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def _append_change(tbl: list[dict[str, Any]], rec: dict[str, Any]) -> None:
    pass
    tbl.append(rec)


def _ensure_list(data: dict[str, Any], key: str):
    pass
    if key not in data or not isinstance(data[key], list):
        data[key] = []


def _assert_table(data: dict[str, Any], key: str) -> list[dict[str, Any]]:
    pass
    if key not in data:
        raise ValueError(f"missing_table:{key}")
    tbl = data[key]
    if not isinstance(tbl, list):
        raise ValueError(f"invalid_table:{key}")
    return tbl


def _require(kwargs: dict[str, Any], names: list[str]) -> str | None:
    pass
    for n in names:
        if n not in kwargs:
            return f"missing_arg:{n}"
    return None


def _next_numeric_id(rows: list[dict[str, Any]], key: str) -> str:
    pass
    mx = 0
    for r in rows:
        v = str(r.get(key))
        if v.isdigit():
            mx = max(mx, int(v))
    return str(mx + 1)


#================================================================
#Assistance functions
#================================================================
def _next_numeric_suffix(prefix: str, items: list[dict[str, Any]], key: str) -> str:
    pass
    mx = 0
    for it in items:
        s = it.get(key)
        if not isinstance(s, str) or not s.startswith(prefix):
            continue
        try:
            num = int(s[len(prefix) :])
            mx = max(mx, num)
        except Exception:
            pass
    return f"{prefix}{mx+1:03d}"


def _i(x, default=0):
    pass
    try:
        return int(x)
    except (TypeError, ValueError):
        return default


def _fail(msg: str) -> str:
    pass
    payload = {"error": msg}
    out = json.dumps(payload)
    return out


def _index(rows: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
    pass
    return {str(r.get(key)): r for r in rows}


#================================================================
#1. Strategy & Guidelines
#================================================================


class GetPlanForDate(Tool):
    """Provide the frozen plan for a specified date (exact match on 'date')."""

    @staticmethod
    def invoke(data: dict[str, Any], date: str) -> str:
        err = _require({"date": date}, ["date"])
        if err:
            return _fail(err)
        plans = _assert_table(data, "plans")
        for p in plans:
            if p.get("date") == date:
                payload = p
                out = json.dumps(payload)
                return out
        return _fail("plan_not_found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPlanForDate",
                "description": "Get a frozen plan for a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "The YYYY-MM-DD date of the plan.",
                        }
                    },
                    "required": ["date"],
                },
            },
        }


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
            missing = [k for k in keys.values() if k not in obj]
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
        rules = data.get("_rules", {}).values() if isinstance(data, dict) else {}
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


class UpdatePlanStatus(Tool):
    """Explicitly set a plan's status and applied_at timestamp."""

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str, status: str, applied_at: str) -> str:
        err = _require({"plan_id": plan_id, "status": status, "applied_at": applied_at}, ["plan_id", "status", "applied_at"])
        if err:
            return _fail(err)
        plans = _assert_table(data, "plans")
        row = next((p for p in plans if p.get("plan_id") == plan_id), None)
        if not row:
            return _fail("plan_not_found")
        row["status"] = status
        row["applied_at"] = applied_at
        payload = {"ok": True, "plan_id": plan_id, "status": status}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdatePlanStatus",
                "description": "Mark plan as applied/aborted with explicit applied_at.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "status": {"type": "string"},
                        "applied_at": {"type": "string"},
                    },
                    "required": ["plan_id", "status", "applied_at"],
                },
            },
        }


class GetPolicyParameter(Tool):
    """Provide a policy parameter by name (exact match on 'param_name')."""

    @staticmethod
    def invoke(data: dict[str, Any], param_name: str) -> str:
        err = _require({"param_name": param_name}, ["param_name"])
        if err:
            return _fail(err)
        tbl = _assert_table(data, "policy_params")
        for r in tbl.values():
            if r.get("param_name") == param_name:
                payload = {
                    "param_name": r.get("param_name"),
                    "param_value": r.get("param_value"),
                }
                out = json.dumps(payload)
                return out
        return _fail("param_not_found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyParameter",
                "description": "Get a value from policy_params by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"param_name": {"type": "string"}},
                    "required": ["param_name"],
                },
            },
        }


#================================================================
#2. Marketing Campaigns
#================================================================


class GetCampaignByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str) -> str:
        err = _require({"name": name}, ["name"])
        if err:
            return _fail(err)
        rows = _assert_table(data, "campaigns")
        for r in rows:
            if r.get("name") == name:
                payload = r
                out = json.dumps(payload)
                return out
        return _fail("campaign_not_found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCampaignByName",
                "description": "Find a campaign by exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class CreateCampaign(Tool):
    """Generate a campaign with specified created_date and status."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str, objective: str, created_date: str, status: str) -> str:
        err = _require({"name": name, "objective": objective, "created_date": created_date, "status": status}, ["name", "objective", "created_date", "status"])
        if err:
            return _fail(err)
        rows = _assert_table(data, "campaigns")
        if any(r.get("name") == name for r in rows.values()):
            return _fail("name_exists")
        new_id = _next_numeric_id(rows, "campaign_id")
        rec = {
            "campaign_id": new_id,
            "name": name,
            "objective": objective,
            "created_date": created_date,
            "status": status,
        }
        rows.append(rec)
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createCampaign",
                "description": "Create a campaign (deterministic; explicit created_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "objective": {"type": "string"},
                        "created_date": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["name", "objective", "created_date", "status"],
                },
            },
        }


class UpdateCampaignStatus(Tool):
    """Modify campaign status with specified timestamp and request_id (recorded in automation_runs)."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str, status: str, timestamp: str, request_id: str) -> str:
        err = _require({"campaign_id": campaign_id, "status": status, "timestamp": timestamp, "request_id": request_id}, ["campaign_id", "status", "timestamp", "request_id"])
        if err:
            return _fail(err)
        rows = _assert_table(data, "campaigns")
        row = next(
            (
                r
                for r in rows
                if str(r.get("campaign_id")) == str(campaign_id)
            ),
            None,
        )
        if not row:
            return _fail("campaign_not_found")
        row["status"] = status
        row["updated_at"] = timestamp
        #optional: record in automation_runs
        runs = _assert_table(data, "automation_runs")
        _append_change(
            runs,
            {
                "run_type": "campaign_status_update",
                "started_at": timestamp,
                "ended_at": timestamp,
                "status": "completed",
                "input_ref": str(campaign_id),
                "outputs_json": {
                    "new_status": status,
                    "request_id": request_id,
                },
                "errors_json": None,
            },
        )
        payload = {
                "ok": True,
                "campaign_id": str(campaign_id),
                "status": status,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateCampaignStatus",
                "description": "Set campaign status with explicit timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "status": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["campaign_id", "status", "timestamp", "request_id"],
                },
            },
        }


#================================================================
#3. Advertisement Sets
#================================================================


class GetAdsetsByCampaignID(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str) -> str:
        err = _require({"campaign_id": campaign_id}, ["campaign_id"])
        if err:
            return _fail(err)
        rows = _assert_table(data, "adsets")
        payload = [r for r in rows.values() if str(r.get("campaign_id")) == str(campaign_id)]
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAdsetsByCampaignId",
                "description": "List adsets by campaign_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }


class GetAdsetDetailsByID(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str) -> str:
        err = _require({"adset_id": adset_id}, ["adset_id"])
        if err:
            return _fail(err)

        adset_id = str(adset_id)
        adsets_tbl = _assert_table(data, "adsets")
        row = _index(adsets_tbl, "adset_id").get(adset_id)
        if not row:
            payload = {"error": "adset_not_found"}
            out = json.dumps(payload)
            return out

        # Link ads using adset_id; handle absent ads table by returning an empty list
        try:
            ads_tbl = _assert_table(data, "ads")
        except Exception:
            ads_tbl = []

        ads_for_adset = [a for a in ads_tbl.values() if str(a.get("adset_id")) == adset_id]

        # Order: active first, followed by start_date (string-safe), then by name for consistency
        def sort_key(a: dict[str, Any]) -> tuple[Any, Any, Any]:
            status = a.get("status", "")
            start_date = a.get("start_date", "")  # retain as string to prevent parsing errors
            name = a.get("name", "")
            return (status != "active", str(start_date), str(name))

        ads_for_adset_sorted = sorted(ads_for_adset, key=sort_key)

        enriched = dict(row)
        enriched["ads"] = ads_for_adset_sorted
        payload = enriched
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetDetailsById",
                "description": "Get a single adset by ID, including its ads.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }


class CreateAdset(Tool):
    """Generate an adset with specified created_at; requires campaign to exist."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        campaign_id: str,
        name: str,
        daily_budget: float,
        bid_strategy: str,
        status: str,
        created_at: str,
        bid_amount: float = None,
        start_date: str = None,
        end_date: str = None
,
    request_id: Any = None,
    ) -> str:
        req = [
            "campaign_id",
            "name",
            "daily_budget",
            "bid_strategy",
            "status",
            "created_at",
        ]
        err = _require(locals(), req)
        if err:
            return _fail(err)
        _assert_table(data, "campaigns")  # verify the existence of the table
        adsets = _assert_table(data, "adsets")
        new_id = _next_numeric_id(adsets, "adset_id")
        rec = {
            "adset_id": new_id,
            "campaign_id": str(campaign_id),
            "name": name,
            "daily_budget": float(daily_budget),
            "bid_strategy": bid_strategy,
            "bid_amount": bid_amount,
            "start_date": start_date,
            "end_date": end_date,
            "status": status,
            "updated_at": created_at,
        }
        adsets.append(rec)
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createAdset",
                "description": "Create an adset (deterministic; explicit created_at).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "name": {"type": "string"},
                        "daily_budget": {"type": "number"},
                        "bid_strategy": {"type": "string"},
                        "bid_amount": {"type": ["number", "null"]},
                        "start_date": {"type": ["string", "null"]},
                        "end_date": {"type": ["string", "null"]},
                        "status": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "campaign_id",
                        "name",
                        "daily_budget",
                        "bid_strategy",
                        "status",
                        "created_at",
                    ],
                },
            },
        }


class UpdateAdsetBudget(Tool):
    """Modify daily_budget with specified timestamp & request_id; records in budget_changes."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str,
        new_budget: float,
        timestamp: str,
        request_id: str,
        reason: str = "manual"
    ) -> str:
        req = ["adset_id", "new_budget", "timestamp", "request_id"]
        err = _require(locals(), req)
        if err:
            return _fail(err)
        adsets = _assert_table(data, "adsets")
        row = next(
            (r for r in adsets if str(r.get("adset_id")) == str(adset_id)),
            None,
        )
        if not row:
            return _fail("adset_not_found")
        old = float(row.get("daily_budget", 0.0))
        new = float(new_budget)
        if new != old:
            row["daily_budget"] = new
            row["updated_at"] = timestamp
            _assert_table(data, "budget_changes").append(
                {
                    "adset_id": str(adset_id),
                    "old_budget": old,
                    "new_budget": new,
                    "changed_at": timestamp,
                    "reason": reason,
                    "request_id": request_id,
                }
            )
        payload = {
            "ok": True,
            "adset_id": str(adset_id),
            "old_budget": old,
            "new_budget": new,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateAdsetBudget",
                "description": "Write a budget change and log it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_budget": {"type": "number"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": ["adset_id", "new_budget", "timestamp", "request_id"],
                },
            },
        }


class UpdateAdsetBidStrategy(Tool):
    """Modify bid_strategy and/or bid_amount; records in strategy_changes."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str, timestamp: str, request_id: str, bid_strategy: str = None, bid_amount: float = None) -> str:
        req = ["adset_id", "timestamp", "request_id"]
        err = _require({"adset_id": adset_id, "timestamp": timestamp, "request_id": request_id}, req)
        if err:
            return _fail(err)
        adsets = _assert_table(data, "adsets")
        row = next(
            (r for r in adsets if str(r.get("adset_id")) == str(adset_id)),
            None,
        )
        if not row:
            return _fail("adset_not_found")
        changes = []
        if bid_strategy is not None and bid_strategy != row.get("bid_strategy"):
            _assert_table(data, "strategy_changes").append(
                {
                    "adset_id": str(adset_id),
                    "old_bid_strategy": row.get("bid_strategy"),
                    "new_bid_strategy": bid_strategy,
                    "changed_at": timestamp,
                    "request_id": request_id,
                }
            )
            row["bid_strategy"] = bid_strategy
            row["updated_at"] = timestamp
            changes.append("bid_strategy")
        if bid_amount is not None and bid_amount != row.get("bid_amount"):
            _assert_table(data, "strategy_changes").append(
                {
                    "adset_id": str(adset_id),
                    "old_bid_amount": row.get("bid_amount"),
                    "new_bid_amount": bid_amount,
                    "changed_at": timestamp,
                    "request_id": request_id,
                }
            )
            row["bid_amount"] = bid_amount
            row["updated_at"] = timestamp
            changes.append("bid_amount")
        payload = {"ok": True, "adset_id": str(adset_id), "updated": changes}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateAdsetBidStrategy",
                "description": "Update bid strategy/amount with logging.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "bid_strategy": {"type": "string"},
                        "bid_amount": {"type": ["number", "null"]},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["adset_id", "timestamp", "request_id"],
                },
            },
        }


class UpdateAdsetStatus(Tool):
    """Specify adset status (active/paused) with a defined timestamp."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str, status: str, timestamp: str) -> str:
        req = ["adset_id", "status", "timestamp"]
        err = _require({"adset_id": adset_id, "status": status, "timestamp": timestamp}, req)
        if err:
            return _fail(err)
        adsets = _assert_table(data, "adsets")
        row = next(
            (r for r in adsets if str(r.get("adset_id")) == str(adset_id)),
            None,
        )
        if not row:
            return _fail("adset_not_found")
        row["status"] = status
        row["updated_at"] = timestamp
        payload = {
                "ok": True,
                "adset_id": str(adset_id),
                "status": status,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateAdsetStatus",
                "description": "Activate/Pause an adset (explicit timestamp).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "status": {"type": "string"},
                        "timestamp": {"type": "string"},
                    },
                    "required": ["adset_id", "status", "timestamp"],
                },
            },
        }


#================================================================
#4. Advertisements
#================================================================


class GetAdsByAdsetID(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str) -> str:
        err = _require({"adset_id": adset_id}, ["adset_id"])
        if err:
            return _fail(err)
        rows = _assert_table(data, "ads")
        payload = [r for r in rows.values() if str(r.get("adset_id")) == str(adset_id)]
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsByAdsetId",
                "description": "List ads under an adset.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }


class CreateAd(Tool):
    """Generate an ad record (status must be specified; no implicit now)."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str,
        name: str,
        creative_type: str,
        status: str,
        start_date: str,
        end_date: str = None,
        request_id: str = None
    ) -> str:
        req = ["adset_id", "name", "creative_type", "status", "start_date"]
        err = _require(locals(), req)
        if err:
            return _fail(err)
        ads = _assert_table(data, "ads")
        new_id = _next_numeric_id(ads, "ad_id")
        rec = {
            "ad_id": new_id,
            "adset_id": str(adset_id),
            "name": name,
            "creative_type": creative_type,
            "status": status,
            "start_date": start_date,
            "end_date": end_date,
        }
        data["ads"][ad_id] = rec
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAd",
                "description": "Create an ad under an adset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "name": {"type": "string"},
                        "creative_type": {"type": "string"},
                        "status": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": ["string", "null"]},
                    },
                    "required": [
                        "adset_id",
                        "name",
                        "creative_type",
                        "status",
                        "start_date",
                    ],
                },
            },
        }


class UpdateAdStatus(Tool):
    """Modify a single ad's status with specified end_date if pausing."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str, status: str, end_date: str = None, request_id: Any = None,
    timestamp: Any = None,
    ) -> str:
        req = ["ad_id", "status"]
        err = _require({"ad_id": ad_id, "status": status}, req)
        if err:
            return _fail(err)
        ads = _assert_table(data, "ads")
        row = next(
            (r for r in ads if str(r.get("ad_id")) == str(ad_id)), None
        )
        if not row:
            return _fail("ad_not_found")
        row["status"] = status
        if status == "paused" and end_date:
            row["end_date"] = end_date
        payload = {"ok": True, "ad_id": str(ad_id), "status": status}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdStatus",
                "description": "Set an ad status (active/paused).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {"type": "string"},
                        "status": {"type": "string"},
                        "end_date": {"type": ["string", "null"]},
                    },
                    "required": ["ad_id", "status"],
                },
            },
        }


#
#class RotateAdCreative(Tool):
#Create a new active advertisement for the adset and pause all other ads; log to creative_rotations.
#
#@staticmethod
#def invoke(data: Dict[str, Any], **kwargs, timestamp: Any = None) -> str:
#req = ["adset_id", "new_creative_type", "timestamp", "request_id"]
#err = _require(kwargs, req)
#if err: return _fail(err)
#ads = _assert_table(data, "ads")
#rotations = _assert_table(data, "creative_rotations")
#adset_id = str(kwargs["adset_id"])
#rationale = kwargs.get("rationale", "direct_rotation")
#
#old_active_id = None
#for a in ads:
#if str(a.get("adset_id")) == adset_id and a.get("status") == "active":
#old_active_id = str(a.get("ad_id"))
#break
#
#new_id = _next_numeric_id(ads, "ad_id")
#new_id = kwargs["ad_name"]
#new_ad = {
#"ad_id": new_id,
#"adset_id": adset_id,
#"name": kwargs.get("ad_name", f"{kwargs['new_creative_type'].title()} Ad"),
#"creative_type": kwargs["new_creative_type"],
#"status": "active",
#"start_date": kwargs["timestamp"].split("T")[0] if "T" in kwargs["timestamp"] else kwargs["timestamp"],
#"end_date": None,
#}
#data["ads"][ad_id] = new_ad
#
#Suspend all other ads within the same adset
#for a in ads:
#if str(a.get("adset_id")) == adset_id and str(a.get("ad_id")) != new_id:
#a["status"] = "paused"
#
#rotations.append({
#"adset_id": adset_id,
#"old_active_id": old_active_id,
#"new_active_id": new_id,
#"old_type": None,
#"new_type": kwargs["new_creative_type"],
#"changed_at": kwargs["timestamp"],
#"rationale": rationale,
#"request_id": kwargs["request_id"],
#)
#
#active_now = [a for a in ads.values() if str(a.get("adset_id")) == adset_id and a.get("status") == "active"]
#return json.dumps({"adset_id": adset_id, "new_active_id": new_id, "new_type": kwargs["new_creative_type",
#"active_count": len(active_now), "rationale": rationale})
#
#================================================================
#5. Creative Rotation (modified to adhere to rules.py)
#================================================================
#================================================================
#rotate_ad_creative (per-request rotation_id + appropriate audit + field names)
#================================================================
class RotateAdCreative(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str,
        new_creative_type: str,
        timestamp: str,
        request_id: str,
        rationale: str = "direct_rotation",
        ad_name: str = None
    ) -> str:
        pass
        err = _require(
            {
                "adset_id": adset_id,
                "new_creative_type": new_creative_type,
                "timestamp": timestamp,
                "request_id": request_id
            },
            ["adset_id", "new_creative_type", "timestamp", "request_id"]
        )
        if err:
            return _fail(err)

        ads = _assert_table(data, "ads")
        rotations = _assert_table(data, "creative_rotations")
        adsets_tbl = _assert_table(data, "adsets")

        adset_id = str(adset_id)
        new_type = str(new_creative_type)
        ts = str(timestamp)
        request_id = str(request_id)
        rationale = rationale
        ad_name = ad_name or f"{new_type.title()} Ad"

        #--- Locate current active ad (if available)
        old_active = next(
            (
                a
                for a in ads
                if str(a.get("adset_id")) == adset_id and a.get("status") == "active"
            ),
            None,
        )
        old_ad_id = str(old_active.get("ad_id")) if old_active else None
        old_type = str(old_active.get("creative_type")) if old_active else None

        #--- Deterministic new ad_id: auto_{adset_id}_{YYYYMMDD}_{seq}
        date_part = ts.split("T")[0] if "T" in ts else ts  #YYYY-MM-DD
        yyyymmdd = date_part.replace("-", "")
        prefix = f"auto_{adset_id}_{yyyymmdd}_"
        max_seq = 0
        for a in ads:
            if str(a.get("adset_id")) != adset_id:
                continue
            ad_id_val = str(a.get("ad_id"))
            if ad_id_val.startswith(prefix):
                suf = ad_id_val[len(prefix) :]
                if suf.isdigit():
                    max_seq = max(max_seq, int(suf))
        new_ad_id = f"{prefix}{max_seq + 1}"

        #--- Generate new active ad (specific ad_name)
        new_ad = {
            "ad_id": new_ad_id,
            "adset_id": adset_id,
            "name": ad_name,
            "creative_type": new_type,
            "status": "active",
            "start_date": date_part,
            "end_date": None,
        }
        data["ads"][ad_id] = new_ad

        #--- Ensure single-active: suspend all others
        for a in ads:
            if str(a.get("adset_id")) == adset_id and str(a.get("ad_id")) != new_ad_id:
                a["status"] = "paused"

        #--- Update adset metadata
        for aset in adsets_tbl:
            if str(aset.get("adset_id")) == adset_id:
                aset["updated_at"] = ts
                aset["rev"] = _i(aset.get("rev"), 0) + 1
                break

        #--- rotation_id per request_id (CR-<n>), unique & consistent within the execution
        n = 0
        for r in rotations:
            if str(r.get("request_id")) == request_id:
                rid = str(r.get("rotation_id", "")).replace("CR-", "")
                if rid.isdigit():
                    n = max(n, int(rid))
        rotation_id = f"CR-{n + 1}"

        #--- Add audit entry
        rotations.append(
            {
                "rotation_id": rotation_id,
                "adset_id": adset_id,
                "old_ad_id": old_ad_id,
                "new_ad_id": new_ad_id,  #field name according to policy
                "old_type": old_type,
                "new_type": new_type,
                "rotated_at": ts,
                "rationale": rationale,
                "request_id": request_id,
            }
        )

        #--- Provide audit-centric payload
        active_now = [
            a
            for a in ads
            if str(a.get("adset_id")) == adset_id and a.get("status") == "active"
        ]
        payload = {
                "adset_id": adset_id,
                "rotation_id": rotation_id,
                "old_ad_id": old_ad_id,
                "new_ad_id": new_ad_id,
                "old_type": old_type,
                "new_type": new_type,
                "rotated_at": ts,
                #"active_count": len(active_now),
                "rationale": rationale,
                "request_id": request_id,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RotateAdCreative",
                "description": "Rotate creative: create a new active ad (deterministic ad_id), pause others, update adset metadata, and log a creative_rotations row with rotation_id per request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_creative_type": {"type": "string"},
                        "ad_name": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                        "rationale": {"type": "string"},
                    },
                    "required": [
                        "adset_id",
                        "new_creative_type",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }


class GetCreativeRotationHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        rows = _assert_table(data, "creative_rotations")
        out = [r for r in rows.values() if (adset_id is None or str(r.get("adset_id")) == str(adset_id))]
        payload = out
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCreativeRotationHistory",
                "description": "List rotation logs (optionally by adset).",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                },
            },
        }


#================================================================
#6. Mass Application (Budgets & Strategies)
#================================================================

#class ApplyPlanAllocations(Tool):
#"""
#Implements a frozen plan to the adsets table, bypassing NO-OPs and returning only
#the adsets that have genuinely changed. Only compares significant fields:
#- daily_budget (post rounding to policy_snapshot.budget_rounding_unit)
#- bidding strategy
#- bid_amount (ONLY if bid_strategy == "cost_cap")
#Necessary kwargs: plan_id, timestamp, request_id
#Outputs JSON:
#{
#"plan_id": <str>,
#"applied_adsets": [<adset_id str>, ...],     # only modified rows
#"applied_adsets_count": <int>,
#"noops_skipped": [<adset_id str>, ...],      # processed but not altered
#"timestamp": <ISO8601 str>,
#"request_id": <str>
#}
#"""
#@staticmethod
#def invoke(data: Dict[str, Any], **kwargs) -> str:
#1) Check arguments
#err = _require(kwargs, ["plan_id", "timestamp", "request_id"])
#if err:
#return _fail(err)
#
#plan_id = kwargs["plan_id"]
#timestamp = kwargs["timestamp"]
#request_id = kwargs["request_id"]
#
#2) Retrieve the plan (support historical/table naming variations)
#plan = None
#for table_name in ("plans", "plan_freezes"):
#try:
#tbl = _assert_table(data, table_name)
#plan = _index(tbl, "plan_id").get(plan_id)
#if plan:
#break
#except Exception:
#continue
#if not plan:
#return _fail(f"plan_id {plan_id} not located")
#
#3) Retrieve necessary context
#try:
#adsets_tbl = _assert_table(data, "adsets")
#except Exception as e:
#return _fail(f"adsets table not found: {e}")
#
#adsets_idx = _index(adsets_tbl, "adset_id")
#
#policy = (plan.get("policy_snapshot") or {})
#unit = policy.get("budget_rounding_unit", 1)
#try:
#unit = int(unit) if float(unit).is_integer() else float(unit)
#except Exception:
#unit = 1  # safe default
#
#Organize strategies by adset_id for rapid access
#strategies_list = plan.get("strategies") or []
#strategies = {str(s.get("adset_id")): s for s in strategies_list if "adset_id" in s}
#
#def _round_budget(x: Any, u: Any) -> float:
#Rounding to the nearest multiple; resilient to strings/ints/floats
#try:
#fx = float(x)
#except Exception:
#fx = 0.0
#try:
#fu = float(u)
#if fu == 0:
#fu = 1.0
#except Exception:
#fu = 1.0
#return round(fx / fu) * fu
#
#def _as_float_or_none(x: Any) -> Optional[float]:
#try:
#return float(x) if x is not None else None
#except (TypeError, ValueError):
#return None
#
#changed_ids: List[str] = []
#noop_ids: List[str] = []
#
#4) Loop through allocations and implement only significant changes
#for alloc in (plan.get("allocations") or []):
#if "adset_id" not in alloc or "budget" not in alloc:
#return _fail("invalid_allocation_row")
#
#aid = str(alloc["adset_id"])
#adset = adsets_idx.get(aid)
#if not adset:
#return _fail(f"adset_id {aid} not found in DB")
#
#Target values derived from the plan envelope
#target_budget = _round_budget(alloc.get("budget"), unit)
#
#strat_row = strategies.get(aid, {}).values()
#target_strategy = (str(strat_row.get("bid_strategy", adset.get("bid_strategy") or "")).lower()
#or adset.get("bid_strategy"))
#target_bid_amount = strat_row.get("bid_amount") if target_strategy == "cost_cap" else None
#target_bid_amount = _as_float_or_none(target_bid_amount)
#
#Current values (standardized)
#curr_budget = _round_budget(adset.get("daily_budget", 0.0), unit)
#curr_strategy = str(adset.get("bid_strategy", "")).lower()
#curr_bid_amount = _as_float_or_none(adset.get("bid_amount")) if curr_strategy == "cost_cap" else None
#
#Evaluate significant fields
#same_budget = (curr_budget == target_budget)
#same_strategy = (curr_strategy == target_strategy)
#
#if target_strategy == "cost_cap":
#If plan excluded bid_amount, compare with current (allows genuine NO-OP)
#cmp_target_bid = target_bid_amount if target_bid_amount is not None else curr_bid_amount
#same_bid = (curr_bid_amount == cmp_target_bid)
#otherwise:
#same_bid = True  # bid_amount not applicable for lowest_cost
#
#NO-OP: bypass writing and do not include
#if same_budget and same_strategy and same_bid:
#noop_ids.append(aid)
#continue
#
#Implement changes (significant-only)
#adset["daily_budget"] = float(target_budget)
#adset["bid_strategy"] = target_strategy
#
#if target_strategy == "cost_cap":
#Retain current bid if plan excluded it; if still None, that's an issue
#if target_bid_amount is None and curr_bid_amount is not None:
#target_bid_amount = curr_bid_amount
#if target_bid_amount is None:
#return _fail(f"missing_bid_amount_for_cost_cap: adset_id {aid}")
#adset["bid_amount"] = float(target_bid_amount)
#otherwise:
#lowest_cost: ensure outdated bid_amount is eliminated
#adset.pop("bid_amount", None)
#
#Optionally update an updated_at field if your schema requires it
#adset["updated_at"] = timestamp
#
#changed_ids.append(aid)
#
#5) Consistent ordering of outcomes
#def _as_int(s: str) -> int:
#try:
#return int(s)
#except Exception:
#return 10**9  # push non-numeric to the end in a deterministic manner
#
#changed_ids_sorted = sorted(changed_ids, key=_as_int)
#noop_ids_sorted = sorted(noop_ids, key=_as_int)
#
#result = {
#"plan_id": plan_id,
#"applied_adsets": changed_ids_sorted,  # <- always included
#"applied_adsets_count": len(changed_ids_sorted),
#"noops_skipped": noop_ids_sorted,  # optional but beneficial to include
#"timestamp": timestamp,
#"request_id": request_id,
#}
#return json.dumps(result)
#
#@staticmethod
#def get_info() -> Dict[str, Any]:
#return {
#"type": "function",
#"function": {
#"name": "ApplyPlanAllocations",
#"description": "Implement a frozen plan to adsets, bypassing no-ops and returning only modified adsets.",
#"parameters": {
#"type": "object",
#"properties": {
#"plan_id": {"type": "string"},
#"timestamp": {"type": "string"},
#"request_id": {"type": "string"},
#},
#"required": ["plan_id", "timestamp", "request_id"],
#},
#},
#}


#================================================================
#apply_plan_allocations — with clear NOOP reasons
#- Maintains legacy 'noops_skipped': [adset_id, ...]
#- Introduces 'noops_details': [{"adset_id": "...", "reason": "..."}]
#- Reasons listed (consistent):
#* "already_in_target_state" (adhering to rounding rules)
#* "below_min_budget_allocation"
#================================================================
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
        policy = plan.get("policy_snapshot", {}).values() or {}
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
            ps = plan_strat_by_id.get(aid, {}).values()
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


#================================================================
#7. Data & Analysis
#================================================================


class GetDailyInsightsForAdset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str, date: str) -> str:
        req = ["adset_id", "date"]
        err = _require({"adset_id": adset_id, "date": date}, req)
        if err:
            return _fail(err)
        rows = _assert_table(data, "f_insights")
        out = [
            r
            for r in rows
            if str(r.get("adset_id")) == str(adset_id)
            and r.get("date") == date
        ]
        payload = out
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDailyInsightsForAdset",
                "description": "Read f_insights for a specific day & adset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["adset_id", "date"],
                },
            },
        }


class GetViewershipForCategory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], category: str, date: str) -> str:
        req = ["category", "date"]
        err = _require({"category": category, "date": date}, req)
        if err:
            return _fail(err)
        rows = _assert_table(data, "f_viewership")
        out = [
            r
            for r in rows
            if r.get("category") == category
            and r.get("date") == date
        ]
        payload = out
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetViewershipForCategory",
                "description": "Read f_viewership for a category/date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["category", "date"],
                },
            },
        }


class GetSalesByCategoryRange(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], category: str, start_date: str, end_date: str, date: Any = None) -> str:
        req = ["category", "start_date", "end_date"]
        err = _require({"category": category, "start_date": start_date, "end_date": end_date}, req)
        if err:
            return _fail(err)
        rows = _assert_table(data, "f_sales")
        out = [
            r
            for r in rows
            if r.get("category") == category
            and r.get("start_date") == start_date
            and r.get("end_date") == end_date
        ]
        payload = out
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSalesByCategoryRange",
                "description": "Read f_sales summary for a category & range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["category", "start_date", "end_date"],
                },
            },
        }


class GetProductPriceOnDate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str, date: str) -> str:
        req = ["product_id", "date"]
        err = _require({"product_id": product_id, "date": date}, req)
        if err:
            return _fail(err)
        rows = _assert_table(data, "f_price")
        out = next(
            (
                r
                for r in rows
                if str(r.get("product_id")) == str(product_id)
                and r.get("date") == date
            ),
            None,
        )
        payload = out or {"error": "price_not_found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getProductPriceOnDate",
                "description": "Read f_price for a product on a date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["product_id", "date"],
                },
            },
        }


class FindUnderperformingAdsets(Tool):
    """Locate adsets below a ROAS threshold for a specified day (joins f_insights with adsets)."""

    @staticmethod
    def invoke(data: dict[str, Any], date: str, min_roas: float) -> str:
        req = ["date", "min_roas"]
        err = _require({"date": date, "min_roas": min_roas}, req)
        if err:
            return _fail(err)
        ins = _assert_table(data, "f_insights")
        adsets = _index(_assert_table(data, "adsets"), "adset_id")
        th = float(min_roas)
        out = []
        for r in ins:
            if r.get("date") != date:
                continue
            aid = str(r.get("adset_id"))
            spend = float(r.get("spend", 0.0))
            rev = float(r.get("revenue", 0.0))
            roas = (rev / spend) if spend > 0 else 0.0
            if roas < th:
                a = adsets.get(aid, {}).values()
                out.append(
                    {
                        "adset_id": aid,
                        "roas": roas,
                        "spend": spend,
                        "revenue": rev,
                        "status": a.get("status"),
                    }
                )
        payload = out
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findUnderperformingAdsets",
                "description": "Find adsets with ROAS below threshold on a date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "min_roas": {"type": "number"},
                    },
                    "required": ["date", "min_roas"],
                },
            },
        }


#================================================================
#8. Automation / Log Files
#================================================================


class RecordAutomationRun(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_type: str = None, started_at: str = None, ended_at: str = None, status: str = None, input_ref: str = None, outputs_json: dict = None, errors_json: dict = None, request_id: str = None) -> str:
        pass
        _ensure_list(data, "automation_runs")
        row = {
            "run_type": run_type,
            "started_at": started_at,
            "ended_at": ended_at,
            "status": status,
            "input_ref": input_ref,
            "outputs_json": outputs_json,
            "errors_json": errors_json,
        }
        #try:
        #t0 = datetime.fromisoformat(row["started_at"].replace("Z","+00:00"))
        #t1 = datetime.fromisoformat(row["ended_at"].replace("Z","+00:00"))
        #row["duration_ms"] = int((t1 - t0).total_seconds()*1000)
        #except Exception:
        #row["duration_ms"] = None
        data["automation_runs"].append(row)
        payload = row
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordAutomationRun",
                "description": "Append an automation run log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_type": {"type": "string"},
                        "started_at": {"type": "string"},
                        "ended_at": {"type": "string"},
                        "status": {"type": "string"},
                        "input_ref": {"type": "string"},
                        "outputs_json": {"type": "object"},
                        "errors_json": {"type": ["object", "null"]},
                    },
                    "required": [
                        "run_type",
                        "started_at",
                        "ended_at",
                        "status",
                        "input_ref",
                        "outputs_json",
                    ],
                },
            },
        }


class GetAutomationRunHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_type: str = None) -> str:
        pass
        #optional filters based on type
        runs = _assert_table(data, "automation_runs")
        out = [r for r in runs.values() if (run_type is None or r.get("run_type") == run_type)]
        payload = out
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAutomationRunHistory",
                "description": "Read automation_runs (optionally filter by run_type).",
                "parameters": {
                    "type": "object",
                    "properties": {"run_type": {"type": "string"}},
                },
            },
        }


class InsertEntity(Tool):
    """Generic deterministic insertion into supported tables (ads, adsets)."""

    @staticmethod
    def invoke(data: dict[str, Any], table: str, row: dict, timestamp: str, request_id: str) -> str:
        err = _require({"table": table, "row": row, "timestamp": timestamp, "request_id": request_id}, ["table", "row", "timestamp", "request_id"])
        if err:
            return _fail(err)

        tbl = _assert_table(data, table)

        # Do NOT modify row fields. Simply append exactly what the caller provided.
        # Optional: if the domain requires updated_at defaults, only assign if absent.
        if table == "adsets" and "updated_at" not in row:
            row = {**row, "updated_at": timestamp}

        # Append as is and return
        tbl.append(copy.deepcopy(row))
        payload = row
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertEntity",
                "description": "Insert a new row into a supported table (ads, adsets) with strict validation and deterministic timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "table": {"type": "string", "enum": ["ads", "adsets"]},
                        "row": {"type": "object"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["table", "row", "timestamp", "request_id"],
                },
            },
        }


class ApplyCreatives(Tool):
    """Rotate creatives according to plan or specified targets: add a new ad, suspend least effective active, activate new;
    update adset metadata; and record a deterministic rotation entry.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        request_id: str,
        timestamp: str,
        rationale: str,
        plan_id: str = None,
        targets: list[dict[str, Any]] = None
    ) -> str:
        pass
        # Mandate deterministic fields; user must supply plan_id OR targets
        err = _require({"request_id": request_id, "timestamp": timestamp, "rationale": rationale}, ["request_id", "timestamp", "rationale"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload)
            return out
        if plan_id is None and not targets:
            payload = {"error": "missing_arg: plan_id_or_targets"}
            out = json.dumps(payload)
            return out

        _ensure_list(data, "ads")
        _ensure_list(data, "adsets")
        _ensure_list(data, "creative_rotations")
        _ensure_list(data, "f_insights")
        _ensure_list(data, "plans")  # for plan_id route

        # ---- Construct targets ----------------------------------------------
        # Option A: from plan_id (allocations[*].creative_type)
        targets_list: list[dict[str, Any]] = []
        if plan_id is not None:
            plan = next(
                (p for p in data["plans"].values() if str(p.get("plan_id")) == str(plan_id)), None
            )
            if not plan:
                payload = {"error": f"missing_plan:{plan_id}"}
                out = json.dumps(payload)
                return out
            for row in plan.get("allocations", []):
                ct = row.get("creative_type")
                if ct:
                    targets_list.append(
                        {
                            "adset_id": str(row.get("adset_id")),
                            "creative_type": ct,
                            "ad_name": row.get("ad_name"),
                        }
                    )
        # Option B: defined targets array
        if targets:
            # standardize & combine (plan targets first, explicit targets may override)
            explicit: list[dict[str, Any]] = targets
            by_id = {t["adset_id"]: t for t in targets_list if t.get("adset_id")}
            for t in explicit:
                aid = str(t.get("adset_id"))
                if not aid or "creative_type" not in t:
                    payload = {"error": "invalid_target: require adset_id and creative_type"}
                    out = json.dumps(payload)
                    return out
                by_id[aid] = {
                    "adset_id": aid,
                    "creative_type": t["creative_type"],
                    "ad_name": t.get("ad_name"),
                }
            targets_list = list(by_id)

        if not targets_list:
            payload = {
                "plan_id": plan_id,
                "request_id": request_id,
                "updated_adsets": [],
                "rotations": [],
            }
            out = json.dumps(payload)
            return out

        # ---- Assistance Functions ------------------------------------------
        ads_by_adset: dict[str, list[dict[str, Any]]] = {}
        for a in data["ads"].values():
            ads_by_adset.setdefault(str(a.get("adset_id")), []).append(a)

        def _worst_active(adset_id: str) -> str | None:
            pass
            actives = [
                a for a in ads_by_adset.get(adset_id, []) if a.get("status") == "active"
            ]
            if not actives:
                return None
            # Calculate naive CPA = spend / purchases from f_insights (if accessible)
            cpa_by_ad: dict[str, float] = {}
            for row in data.get("f_insights", {}).values():
                if str(row.get("adset_id")) == adset_id:
                    ad_id = str(row.get("ad_id"))
                    spend = float(row.get("spend", 0.0) or 0.0)
                    purchases = float(row.get("purchases", 0.0) or 0.0)
                    cpa_by_ad[ad_id] = (
                        (spend / purchases) if purchases > 0 else float("inf")
                    )
            actives.sort(
                key=lambda x: cpa_by_ad.get(str(x.get("ad_id")), float("inf")),
                reverse=True,
            )
            return str(actives[0].get("ad_id"))

        def _next_ad_id() -> str:
            pass
            mx = 0
            for a in data["ads"].values():
                try:
                    mx = max(mx, int(str(a.get("ad_id"))))
                except Exception:
                    continue
            return str(mx + 1)

        def _next_rotation_id() -> str:
            pass
            mx = 0
            for r in data["creative_rotations"].values():
                rid = str(r.get("rotation_id", "")).replace("CR-", "")
                if rid.isdigit():
                    mx = max(mx, int(rid))
            return f"CR-{mx + 1}"

        # ---- Implement for each adset -------------------------------------
        updated: list[str] = []
        rotations_written: list[str] = []

        for spec in targets_list:
            adset_id = str(spec["adset_id"])
            want_type = spec["creative_type"]

            current_active = [
                a for a in ads_by_adset.get(adset_id, []) if a.get("status") == "active"
            ]
            current_type = (
                current_active[0].get("creative_type") if current_active else None
            )

            # If already accurate and single active, bypass
            if current_type == want_type and len(current_active) == 1:
                continue

            old_active_id = _worst_active(adset_id)

            # Generate new active ad
            new_id = _next_ad_id()
            new_ad = {
                "ad_id": new_id,
                "adset_id": adset_id,
                "name": spec.get("ad_name", f"{adset_id}-{want_type}-auto"),
                "creative_type": want_type,
                "status": "active",
                "start_date": timestamp.split("T")[0],
                "end_date": None,
            }
            data["ads"][ad_id] = new_ad
            ads_by_adset.setdefault(adset_id, []).append(new_ad)

            # Suspend previous least effective active (if any)
            if old_active_id:
                for a in data["ads"].values():
                    if str(a.get("ad_id")) == old_active_id:
                        a["status"] = "paused"

            # Update adset metadata in a deterministic manner
            for aset in data["adsets"].values():
                if str(aset.get("adset_id")) == adset_id:
                    aset["updated_at"] = timestamp
                    aset["rev"] = _i(aset.get("rev"), 0) + 1
                    break

            # Rotation log entry (strict schema)
            rot_id = _next_rotation_id()
            data["creative_rotations"].append(
                {
                    "rotation_id": rot_id,
                    "adset_id": adset_id,
                    "old_ad_id": old_active_id,
                    "new_ad_id": new_id,
                    "old_type": current_type,
                    "new_type": want_type,
                    "rotated_at": timestamp,
                    "rationale": rationale,
                    "request_id": request_id,
                }
            )

            updated.append(adset_id)
            rotations_written.append(rot_id)
        payload = {
            "plan_id": plan_id,
            "request_id": request_id,
            "updated_adsets": updated,
            "rotations": rotations_written,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "applyCreatives",
                "description": "Rotate creatives using either a plan_id (allocations[].creative_type) or an explicit targets list; logs deterministic rotation rows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "targets": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "adset_id": {"type": "string"},
                                    "creative_type": {"type": "string"},
                                    "ad_name": {"type": "string"},
                                },
                                "required": ["adset_id", "creative_type"],
                            },
                        },
                        "request_id": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "rationale": {"type": "string"},
                    },
                    "required": ["request_id", "timestamp", "rationale"],
                },
            },
        }


#================================================================
#9. Registry (function names follow snake_case like v4)
#================================================================

TOOLS = [
    #Strategy & Guidelines
    GetPlanForDate(),
    GetAdsetAllocationFromPlan(),
    FreezePlan(),
    VerifyPlanAgainstAdsets(),
    UpdatePlanStatus(),
    GetPolicyParameter(),
    #Marketing Campaigns
    GetCampaignByName(),
    CreateCampaign(),
    UpdateCampaignStatus(),
    #Advertisement Sets
    GetAdsetsByCampaignID(),
    GetAdsetDetailsByID(),
    CreateAdset(),
    UpdateAdsetBudget(),
    UpdateAdsetBidStrategy(),
    UpdateAdsetStatus(),
    #Advertisements
    GetAdsByAdsetID(),
    CreateAd(),
    UpdateAdStatus(),
    #Creative Rotation
    RotateAdCreative(),
    GetCreativeRotationHistory(),
    #Mass Application
    ApplyPlanAllocations(),
    #Data & Analysis
    GetDailyInsightsForAdset(),
    GetViewershipForCategory(),
    GetSalesByCategoryRange(),
    GetProductPriceOnDate(),
    FindUnderperformingAdsets(),
    #Automation
    RecordAutomationRun(),
    GetAutomationRunHistory(),
    InsertEntity(),
    ApplyCreatives(),
]


def get_tools():
    return TOOLS
