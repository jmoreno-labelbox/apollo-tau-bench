import copy
import json
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple
from domains.dto import Tool


# ================================================================
# Helpers
# ================================================================
def _next_numeric_suffix(prefix: str, items: List[Dict[str, Any]], key: str) -> str:
    mx = 0
    for it in items:
        s = it.get(key)
        if not isinstance(s, str) or not s.startswith(prefix):
            continue
        try:
            num = int(s[len(prefix):])
            mx = max(mx, num)
        except Exception:
            pass
    return f"{prefix}{mx+1:03d}"

def _ensure_list(data: Dict[str, Any], key: str):
    if key not in data or not isinstance(data[key], list):
        data[key] = []

def _assert_table(data: Dict[str, Any], key: str) -> List[Dict[str, Any]]:
    if key not in data:
        raise ValueError(f"missing_table:{key}")
    tbl = data[key]
    if not isinstance(tbl, list):
        raise ValueError(f"invalid_table:{key}")
    return tbl


def _index(rows: List[Dict[str, Any]], key: str) -> Dict[str, Dict[str, Any]]:
    return {str(r.get(key)): r for r in rows}


def _require(kwargs: Dict[str, Any], names: List[str]) -> Optional[str]:
    for n in names:
        if n not in kwargs:
            return f"missing_arg:{n}"
    return None

def _i(x, default=0):
    try:
        return int(x)
    except (TypeError, ValueError):
        return default

def _fail(msg: str) -> str:
    return json.dumps({"error": msg})


def _next_numeric_id(rows: List[Dict[str, Any]], key: str) -> str:
    mx = 0
    for r in rows:
        v = str(r.get(key))
        if v.isdigit():
            mx = max(mx, int(v))
    return str(mx + 1)


def _append_change(tbl: List[Dict[str, Any]], rec: Dict[str, Any]) -> None:
    tbl.append(rec)


# ================================================================
# 1. Planning & Policy
# ================================================================

class GetPlanForDate(Tool):
    """Return the frozen plan for a given date (exact match on 'date')."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["date"])
        if err: return _fail(err)
        plans = _assert_table(data, "plans")
        for p in plans:
            if p.get("date") == kwargs["date"]:
                return json.dumps(p)
        return _fail("plan_not_found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_plan_for_date", "description": "Get a frozen plan for a given date.",
                             "parameters": {"type": "object", "properties": {
                                 "date": {"type": "string", "description": "The YYYY-MM-DD date of the plan."}},
                                            "required": ["date"]}}}


class GetAdsetAllocationFromPlan(Tool):
    """Return the allocation entry for a given adset_id inside a plan_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["plan_id", "adset_id"])
        if err: return _fail(err)
        plans = _assert_table(data, "plans")
        pid = kwargs["plan_id"]
        aid = str(kwargs["adset_id"])
        for p in plans:
            if p.get("plan_id") == pid:
                for row in p.get("allocations", []):
                    if str(row.get("adset_id")) == aid:
                        return json.dumps(row)
                return _fail("allocation_not_found")
        return _fail("plan_not_found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adset_allocation_from_plan",
                                                 "description": "Get the planned allocation for an adset in a plan.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"plan_id": {"type": "string"},
                                                                               "adset_id": {"type": "string"}},
                                                                "required": ["plan_id", "adset_id"]}}}

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

        # --- helpers ---------------------------------------------------------
        def _to_dec(x) -> Decimal:
            return Decimal(str(x))

        def _require_keys(obj: Dict[str, Any], keys: List[str], ctx: str) -> Optional[str]:
            missing = [k for k in keys if k not in obj]
            return f"missing_required_keys:{ctx}:{','.join(missing)}" if missing else None

        # --- required top-level args -----------------------------------------
        err = _require(kwargs, ["plan_id", "date", "created_at", "allocations"])
        if err:
            return _fail(err)

        plan_id: str = str(kwargs["plan_id"])
        created_at: str = str(kwargs["created_at"])  # do not parse; treat as opaque string
        date: str = str(kwargs["date"])

        # Rules / defaults
        rules = data.get("_rules", {}) if isinstance(data, dict) else {}
        default_author = rules.get("default_author", "automation_agent")
        default_checksum = rules.get("default_checksum", "CHK001")

        author = str(kwargs.get("author", default_author))
        checksum = str(kwargs.get("checksum", default_checksum))

        # Policy snapshot (from payload or default from rules)
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

        # adset_mapping: required for any adset that appears in allocations
        adset_mapping = kwargs.get("adset_mapping", [])
        if not isinstance(adset_mapping, list):
            return _fail("invalid_adset_mapping:not_array")

        # strategies: required for any adset that appears in allocations
        strategies = kwargs.get("strategies", [])
        if not isinstance(strategies, list):
            return _fail("invalid_strategies:not_array")

        # creatives: required for any adset that appears in allocations
        creatives = kwargs.get("creatives", [])
        if not isinstance(creatives, list):
            return _fail("invalid_creatives:not_array")

        # index helpers
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
            # Allow any string; typical values: image, video, carousel
            if not ctype:
                return _fail(f"invalid_creative_row:{i}:empty_creative_type:{aid}")
            creat_idx[aid] = c

        # Validate allocations
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

            # rounding rules
            if unit == 1:
                if bud != bud.to_integral_value(rounding=ROUND_HALF_UP):
                    return _fail(f"invalid_allocation_row:{i}:must_be_integer_when_unit_1:{str(bud)}")
            else:
                # check multiple of unit using Decimal
                if (bud % _to_dec(unit)) != 0:
                    return _fail(f"invalid_allocation_row:{i}:violates_rounding_unit:{unit}:{str(bud)}")

            total += bud
            normalized_allocs.append({"adset_id": aid, "budget": float(bud)})

        # If total_budget is present, require it matches the subset sum
        if "total_budget" in kwargs and kwargs["total_budget"] is not None:
            try:
                tb = _to_dec(kwargs["total_budget"])
            except (InvalidOperation, TypeError, ValueError):
                return _fail("invalid_total_budget:not_numeric")
            if (tb - total).copy_abs() > Decimal("0.000001"):
                return _fail(f"invalid_total_budget_mismatch:{float(tb)}!={float(total)}")
            total_budget_out = float(tb)
        else:
            # derive from subset
            total_budget_out = float(total)

        # Compose final plan row
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

        # Upsert into plans table
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

class VerifyPlanAgainstAdsets(Tool):
    """Compare plan allocations vs current adsets (active only)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["plan_id"])
        if err: return _fail(err)
        plans = _assert_table(data, "plans")
        adsets = _index(_assert_table(data, "adsets"), "adset_id")
        pid = kwargs["plan_id"]
        plan = next((p for p in plans if p.get("plan_id") == pid), None)
        if not plan: return _fail("plan_not_found")
        mismatches: List[Dict[str, Any]] = []
        for spec in plan.get("allocations", []):
            aid = str(spec.get("adset_id"))
            a = adsets.get(aid)
            if not a:
                mismatches.append({"adset_id": aid, "issue": "missing"})
                continue
            if str(a.get("status", "")).lower() != "active":
                continue
            if float(a.get("daily_budget", 0.0)) != float(spec.get("budget", 0.0)):
                mismatches.append({"adset_id": aid, "field": "daily_budget", "expected": float(spec.get("budget", 0.0)),
                                   "actual": float(a.get("daily_budget", 0.0))})
            if spec.get("bid_strategy") is not None and a.get("bid_strategy") != spec.get("bid_strategy"):
                mismatches.append({"adset_id": aid, "field": "bid_strategy", "expected": spec.get("bid_strategy"),
                                   "actual": a.get("bid_strategy")})
            if spec.get("bid_amount") is not None and a.get("bid_amount") != spec.get("bid_amount"):
                mismatches.append({"adset_id": aid, "field": "bid_amount", "expected": spec.get("bid_amount"),
                                   "actual": a.get("bid_amount")})
        return json.dumps({"ok": len(mismatches) == 0, "mismatches": mismatches})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "verify_plan_against_adsets",
                                                 "description": "Compare a plan to current adsets, ignoring paused ones.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"plan_id": {"type": "string"}},
                                                                "required": ["plan_id"]}}}


class UpdatePlanStatus(Tool):
    """Set a plan's status and applied_at timestamp explicitly."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["plan_id", "status", "applied_at"])
        if err: return _fail(err)
        plans = _assert_table(data, "plans")
        row = next((p for p in plans if p.get("plan_id") == kwargs["plan_id"]), None)
        if not row: return _fail("plan_not_found")
        row["status"] = kwargs["status"]
        row["applied_at"] = kwargs["applied_at"]
        return json.dumps({"ok": True, "plan_id": kwargs["plan_id"], "status": kwargs["status"]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_plan_status",
                                                 "description": "Mark plan as applied/aborted with explicit applied_at.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"plan_id": {"type": "string"},
                                                                               "status": {"type": "string"},
                                                                               "applied_at": {"type": "string"}},
                                                                "required": ["plan_id", "status", "applied_at"]}}}


class GetPolicyParameter(Tool):
    """Return a policy parameter by name (exact match on 'param_name')."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["param_name"])
        if err: return _fail(err)
        tbl = _assert_table(data, "policy_params")
        for r in tbl:
            if r.get("param_name") == kwargs["param_name"]:
                return json.dumps({"param_name": r.get("param_name"), "param_value": r.get("param_value")})
        return _fail("param_not_found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_policy_parameter", "description": "Get a value from policy_params by name.",
                             "parameters": {"type": "object", "properties": {"param_name": {"type": "string"}},
                                            "required": ["param_name"]}}}


# ================================================================
# 2. Campaigns
# ================================================================

class GetCampaignByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["name"])
        if err: return _fail(err)
        rows = _assert_table(data, "campaigns")
        for r in rows:
            if r.get("name") == kwargs["name"]:
                return json.dumps(r)
        return _fail("campaign_not_found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_campaign_by_name", "description": "Find a campaign by exact name.",
                             "parameters": {"type": "object", "properties": {"name": {"type": "string"}},
                                            "required": ["name"]}}}


class CreateCampaign(Tool):
    """Create a campaign with explicit created_date and status."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["name", "objective", "created_date", "status"])
        if err: return _fail(err)
        rows = _assert_table(data, "campaigns")
        if any(r.get("name") == kwargs["name"] for r in rows):
            return _fail("name_exists")
        new_id = _next_numeric_id(rows, "campaign_id")
        rec = {"campaign_id": new_id, "name": kwargs["name"], "objective": kwargs["objective"],
               "created_date": kwargs["created_date"], "status": kwargs["status"]}
        rows.append(rec)
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_campaign",
                                                 "description": "Create a campaign (deterministic; explicit created_date).",
                                                 "parameters": {"type": "object",
                                                                "properties": {"name": {"type": "string"},
                                                                               "objective": {"type": "string"},
                                                                               "created_date": {"type": "string"},
                                                                               "status": {"type": "string"}},
                                                                "required": ["name", "objective", "created_date",
                                                                             "status"]}}}


class UpdateCampaignStatus(Tool):
    """Update campaign status with explicit timestamp and request_id (logged in automation_runs)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["campaign_id", "status", "timestamp", "request_id"])
        if err: return _fail(err)
        rows = _assert_table(data, "campaigns")
        row = next((r for r in rows if str(r.get("campaign_id")) == str(kwargs["campaign_id"])), None)
        if not row: return _fail("campaign_not_found")
        row["status"] = kwargs["status"]
        row["updated_at"] = kwargs["timestamp"]
        # optional: log to automation_runs
        runs = _assert_table(data, "automation_runs")
        _append_change(runs, {"run_type": "campaign_status_update", "started_at": kwargs["timestamp"],
                              "ended_at": kwargs["timestamp"], "status": "completed",
                              "input_ref": str(kwargs["campaign_id"]),
                              "outputs_json": {"new_status": kwargs["status"], "request_id": kwargs["request_id"]},
                              "errors_json": None})
        return json.dumps({"ok": True, "campaign_id": str(kwargs["campaign_id"]), "status": kwargs["status"]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_campaign_status",
                                                 "description": "Set campaign status with explicit timestamp.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"campaign_id": {"type": "string"},
                                                                               "status": {"type": "string"},
                                                                               "timestamp": {"type": "string"},
                                                                               "request_id": {"type": "string"}},
                                                                "required": ["campaign_id", "status", "timestamp",
                                                                             "request_id"]}}}


# ================================================================
# 3. Adsets
# ================================================================

class GetAdsetsByCampaignID(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["campaign_id"])
        if err: return _fail(err)
        rows = _assert_table(data, "adsets")
        return json.dumps([r for r in rows if str(r.get("campaign_id")) == str(kwargs["campaign_id"])])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_adsets_by_campaign_id", "description": "List adsets by campaign_id.",
                             "parameters": {"type": "object", "properties": {"campaign_id": {"type": "string"}},
                                            "required": ["campaign_id"]}}}


class GetAdsetDetailsByID(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["adset_id"])
        if err:
            return _fail(err)

        adset_id = str(kwargs["adset_id"])
        adsets_tbl = _assert_table(data, "adsets")
        row = _index(adsets_tbl, "adset_id").get(adset_id)
        if not row:
            return json.dumps({"error": "adset_not_found"})

        # Join ads on adset_id; tolerate missing ads table by returning an empty list
        try:
            ads_tbl = _assert_table(data, "ads")
        except Exception:
            ads_tbl = []

        ads_for_adset = [a for a in ads_tbl if str(a.get("adset_id")) == adset_id]

        # Sort: active first, then by start_date (string-safe), then by name for determinism
        def sort_key(a: Dict[str, Any]) -> Tuple[Any, Any, Any]:
            status = a.get("status", "")
            start_date = a.get("start_date", "")  # keep as string to avoid parse errors
            name = a.get("name", "")
            return (status != "active", str(start_date), str(name))

        ads_for_adset_sorted = sorted(ads_for_adset, key=sort_key)

        enriched = dict(row)
        enriched["ads"] = ads_for_adset_sorted
        return json.dumps(enriched)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_adset_details_by_id",
                "description": "Get a single adset by ID, including its ads.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"]
                }
            }
        }



class CreateAdset(Tool):
    """Create an adset with explicit created_at; requires campaign exists."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["campaign_id", "name", "daily_budget", "bid_strategy", "status", "created_at"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        _assert_table(data, "campaigns")  # ensure table exists
        adsets = _assert_table(data, "adsets")
        new_id = _next_numeric_id(adsets, "adset_id")
        rec = {
            "adset_id": new_id,
            "campaign_id": str(kwargs["campaign_id"]),
            "name": kwargs["name"],
            "daily_budget": float(kwargs["daily_budget"]),
            "bid_strategy": kwargs["bid_strategy"],
            "bid_amount": kwargs.get("bid_amount"),
            "start_date": kwargs.get("start_date"),
            "end_date": kwargs.get("end_date"),
            "status": kwargs["status"],
            "updated_at": kwargs["created_at"],
        }
        adsets.append(rec)
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_adset",
                                                 "description": "Create an adset (deterministic; explicit created_at).",
                                                 "parameters": {"type": "object",
                                                                "properties": {"campaign_id": {"type": "string"},
                                                                               "name": {"type": "string"},
                                                                               "daily_budget": {"type": "number"},
                                                                               "bid_strategy": {"type": "string"},
                                                                               "bid_amount": {
                                                                                   "type": ["number", "null"]},
                                                                               "start_date": {
                                                                                   "type": ["string", "null"]},
                                                                               "end_date": {"type": ["string", "null"]},
                                                                               "status": {"type": "string"},
                                                                               "created_at": {"type": "string"}},
                                                                "required": ["campaign_id", "name", "daily_budget",
                                                                             "bid_strategy", "status", "created_at"]}}}


class UpdateAdsetBudget(Tool):
    """Update daily_budget with explicit timestamp & request_id; logs to budget_changes."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["adset_id", "new_budget", "timestamp", "request_id"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        adsets = _assert_table(data, "adsets")
        row = next((r for r in adsets if str(r.get("adset_id")) == str(kwargs["adset_id"])), None)
        if not row: return _fail("adset_not_found")
        old = float(row.get("daily_budget", 0.0))
        new = float(kwargs["new_budget"])
        if new != old:
            row["daily_budget"] = new
            row["updated_at"] = kwargs["timestamp"]
            _assert_table(data, "budget_changes").append(
                {"adset_id": str(kwargs["adset_id"]), "old_budget": old, "new_budget": new,
                 "changed_at": kwargs["timestamp"], "reason": kwargs.get("reason", "manual"),
                 "request_id": kwargs["request_id"]})
        return json.dumps({"ok": True, "adset_id": str(kwargs["adset_id"]), "old_budget": old, "new_budget": new})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "update_adset_budget", "description": "Write a budget change and log it.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"},
                                                                             "new_budget": {"type": "number"},
                                                                             "timestamp": {"type": "string"},
                                                                             "request_id": {"type": "string"},
                                                                             "reason": {"type": "string"}},
                                            "required": ["adset_id", "new_budget", "timestamp", "request_id"]}}}


class UpdateAdsetBidStrategy(Tool):
    """Update bid_strategy and/or bid_amount; logs to strategy_changes."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["adset_id", "timestamp", "request_id"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        adsets = _assert_table(data, "adsets")
        row = next((r for r in adsets if str(r.get("adset_id")) == str(kwargs["adset_id"])), None)
        if not row: return _fail("adset_not_found")
        changes = []
        if "bid_strategy" in kwargs and kwargs["bid_strategy"] != row.get("bid_strategy"):
            _assert_table(data, "strategy_changes").append(
                {"adset_id": str(kwargs["adset_id"]), "old_bid_strategy": row.get("bid_strategy"),
                 "new_bid_strategy": kwargs["bid_strategy"], "changed_at": kwargs["timestamp"],
                 "request_id": kwargs["request_id"]})
            row["bid_strategy"] = kwargs["bid_strategy"];
            row["updated_at"] = kwargs["timestamp"];
            changes.append("bid_strategy")
        if "bid_amount" in kwargs and kwargs["bid_amount"] != row.get("bid_amount"):
            _assert_table(data, "strategy_changes").append(
                {"adset_id": str(kwargs["adset_id"]), "old_bid_amount": row.get("bid_amount"),
                 "new_bid_amount": kwargs["bid_amount"], "changed_at": kwargs["timestamp"],
                 "request_id": kwargs["request_id"]})
            row["bid_amount"] = kwargs["bid_amount"];
            row["updated_at"] = kwargs["timestamp"];
            changes.append("bid_amount")
        return json.dumps({"ok": True, "adset_id": str(kwargs["adset_id"]), "updated": changes})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_adset_bid_strategy",
                                                 "description": "Update bid strategy/amount with logging.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"},
                                                                               "bid_strategy": {"type": "string"},
                                                                               "bid_amount": {
                                                                                   "type": ["number", "null"]},
                                                                               "timestamp": {"type": "string"},
                                                                               "request_id": {"type": "string"}},
                                                                "required": ["adset_id", "timestamp", "request_id"]}}}


class UpdateAdsetStatus(Tool):
    """Set adset status (active/paused) with explicit timestamp."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["adset_id", "status", "timestamp"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        adsets = _assert_table(data, "adsets")
        row = next((r for r in adsets if str(r.get("adset_id")) == str(kwargs["adset_id"])), None)
        if not row: return _fail("adset_not_found")
        row["status"] = kwargs["status"]
        row["updated_at"] = kwargs["timestamp"]
        return json.dumps({"ok": True, "adset_id": str(kwargs["adset_id"]), "status": kwargs["status"]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_adset_status",
                                                 "description": "Activate/Pause an adset (explicit timestamp).",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"},
                                                                               "status": {"type": "string"},
                                                                               "timestamp": {"type": "string"}},
                                                                "required": ["adset_id", "status", "timestamp"]}}}


# ================================================================
# 4. Ads
# ================================================================

class GetAdsByAdsetID(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["adset_id"])
        if err: return _fail(err)
        rows = _assert_table(data, "ads")
        return json.dumps([r for r in rows if str(r.get("adset_id")) == str(kwargs["adset_id"])])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_ads_by_adset_id", "description": "List ads under an adset.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}},
                                            "required": ["adset_id"]}}}


class CreateAd(Tool):
    """Create an ad record (status must be provided; no implicit now)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["adset_id", "name", "creative_type", "status", "start_date"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        ads = _assert_table(data, "ads")
        new_id = _next_numeric_id(ads, "ad_id")
        rec = {
            "ad_id": new_id,
            "adset_id": str(kwargs["adset_id"]),
            "name": kwargs["name"],
            "creative_type": kwargs["creative_type"],
            "status": kwargs["status"],
            "start_date": kwargs["start_date"],
            "end_date": kwargs.get("end_date"),
        }
        ads.append(rec)
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_ad", "description": "Create an ad under an adset.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"},
                                                                               "name": {"type": "string"},
                                                                               "creative_type": {"type": "string"},
                                                                               "status": {"type": "string"},
                                                                               "start_date": {"type": "string"},
                                                                               "end_date": {
                                                                                   "type": ["string", "null"]}},
                                                                "required": ["adset_id", "name", "creative_type",
                                                                             "status", "start_date"]}}}


class UpdateAdStatus(Tool):
    """Update a single ad's status with explicit end_date if pausing."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["ad_id", "status"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        ads = _assert_table(data, "ads")
        row = next((r for r in ads if str(r.get("ad_id")) == str(kwargs["ad_id"])), None)
        if not row: return _fail("ad_not_found")
        row["status"] = kwargs["status"]
        if kwargs["status"] == "paused" and kwargs.get("end_date"):
            row["end_date"] = kwargs["end_date"]
        return json.dumps({"ok": True, "ad_id": str(kwargs["ad_id"]), "status": kwargs["status"]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "update_ad_status", "description": "Set an ad status (active/paused).",
                             "parameters": {"type": "object",
                                            "properties": {"ad_id": {"type": "string"}, "status": {"type": "string"},
                                                           "end_date": {"type": ["string", "null"]}},
                                            "required": ["ad_id", "status"]}}}



#
# class RotateAdCreative(Tool):
#     """Create a new active ad for the adset and pause all other ads; log to creative_rotations."""
#
#     @staticmethod
#     def invoke(data: Dict[str, Any], **kwargs) -> str:
#         req = ["adset_id", "new_creative_type", "timestamp", "request_id"]
#         err = _require(kwargs, req)
#         if err: return _fail(err)
#         ads = _assert_table(data, "ads")
#         rotations = _assert_table(data, "creative_rotations")
#         adset_id = str(kwargs["adset_id"])
#         rationale = kwargs.get("rationale", "direct_rotation")
#
#         old_active_id = None
#         for a in ads:
#             if str(a.get("adset_id")) == adset_id and a.get("status") == "active":
#                 old_active_id = str(a.get("ad_id"))
#                 break
#
#         #new_id = _next_numeric_id(ads, "ad_id")
#         new_id = kwargs["ad_name"]
#         new_ad = {
#             "ad_id": new_id,
#             "adset_id": adset_id,
#             "name": kwargs.get("ad_name", f"{kwargs['new_creative_type'].title()} Ad"),
#             "creative_type": kwargs["new_creative_type"],
#             "status": "active",
#             "start_date": kwargs["timestamp"].split("T")[0] if "T" in kwargs["timestamp"] else kwargs["timestamp"],
#             "end_date": None,
#         }
#         ads.append(new_ad)
#
#         # Pause all other ads under the same adset
#         for a in ads:
#             if str(a.get("adset_id")) == adset_id and str(a.get("ad_id")) != new_id:
#                 a["status"] = "paused"
#
#         rotations.append({
#             "adset_id": adset_id,
#             "old_active_id": old_active_id,
#             "new_active_id": new_id,
#             "old_type": None,
#             "new_type": kwargs["new_creative_type"],
#             "changed_at": kwargs["timestamp"],
#             "rationale": rationale,
#             "request_id": kwargs["request_id"],
#         })
#
#         active_now = [a for a in ads if str(a.get("adset_id")) == adset_id and a.get("status") == "active"]
#         return json.dumps({"adset_id": adset_id, "new_active_id": new_id, "new_type": kwargs["new_creative_type"],
#                            "active_count": len(active_now), "rationale": rationale})
#
# ================================================================
# 5. Creative Rotation (patched to comply with rules.py)
# ================================================================
# ================================================================
# rotate_ad_creative (per-request rotation_id + proper audit + field names)
# ================================================================
class RotateAdCreative(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["adset_id", "new_creative_type", "timestamp", "request_id"])
        if err:
            return _fail(err)

        ads = _assert_table(data, "ads")
        rotations = _assert_table(data, "creative_rotations")
        adsets_tbl = _assert_table(data, "adsets")

        adset_id = str(kwargs["adset_id"])
        new_type = str(kwargs["new_creative_type"])
        ts = str(kwargs["timestamp"])
        request_id = str(kwargs["request_id"])
        rationale = kwargs.get("rationale", "direct_rotation")
        ad_name = kwargs.get("ad_name", f"{new_type.title()} Ad")

        # --- Find current active ad (if any)
        old_active = next((a for a in ads if str(a.get("adset_id")) == adset_id and a.get("status") == "active"), None)
        old_ad_id = str(old_active.get("ad_id")) if old_active else None
        old_type = str(old_active.get("creative_type")) if old_active else None

        # --- Deterministic new ad_id: auto_{adset_id}_{YYYYMMDD}_{seq}
        date_part = ts.split("T")[0] if "T" in ts else ts  # YYYY-MM-DD
        yyyymmdd = date_part.replace("-", "")
        prefix = f"auto_{adset_id}_{yyyymmdd}_"
        max_seq = 0
        for a in ads:
            if str(a.get("adset_id")) != adset_id:
                continue
            ad_id_val = str(a.get("ad_id"))
            if ad_id_val.startswith(prefix):
                suf = ad_id_val[len(prefix):]
                if suf.isdigit():
                    max_seq = max(max_seq, int(suf))
        new_ad_id = f"{prefix}{max_seq + 1}"

        # --- Create new active ad (exact ad_name)
        new_ad = {
            "ad_id": new_ad_id,
            "adset_id": adset_id,
            "name": ad_name,
            "creative_type": new_type,
            "status": "active",
            "start_date": date_part,
            "end_date": None,
        }
        ads.append(new_ad)

        # --- Enforce single-active: pause all others
        for a in ads:
            if str(a.get("adset_id")) == adset_id and str(a.get("ad_id")) != new_ad_id:
                a["status"] = "paused"

        # --- Touch adset metadata
        for aset in adsets_tbl:
            if str(aset.get("adset_id")) == adset_id:
                aset["updated_at"] = ts
                aset["rev"] = _i(aset.get("rev"), 0) + 1
                break

        # --- rotation_id per request_id (CR-<n>), unique & deterministic within the run
        n = 0
        for r in rotations:
            if str(r.get("request_id")) == request_id:
                rid = str(r.get("rotation_id", "")).replace("CR-", "")
                if rid.isdigit():
                    n = max(n, int(rid))
        rotation_id = f"CR-{n + 1}"

        # --- Append audit row
        rotations.append({
            "rotation_id": rotation_id,
            "adset_id": adset_id,
            "old_ad_id": old_ad_id,
            "new_ad_id": new_ad_id,  # field name per policy
            "old_type": old_type,
            "new_type": new_type,
            "rotated_at": ts,
            "rationale": rationale,
            "request_id": request_id,
        })

        # --- Return audit-focused payload
        active_now = [a for a in ads if str(a.get("adset_id")) == adset_id and a.get("status") == "active"]
        return json.dumps({
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
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "rotate_ad_creative",
            "description": "Rotate creative: create a new active ad (deterministic ad_id), pause others, update adset metadata, and log a creative_rotations row with rotation_id per request.",
            "parameters": {"type": "object",
                "properties": {
                    "adset_id": {"type": "string"},
                    "new_creative_type": {"type": "string"},
                    "ad_name": {"type": "string"},
                    "timestamp": {"type": "string"},
                    "request_id": {"type": "string"},
                    "rationale": {"type": "string"}
                },
                "required": ["adset_id", "new_creative_type", "timestamp", "request_id"]
            }
        }}



class GetCreativeRotationHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        rows = _assert_table(data, "creative_rotations")
        out = [r for r in rows if (aid is None or str(r.get("adset_id")) == str(aid))]
        return json.dumps(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_creative_rotation_history",
                                                 "description": "List rotation logs (optionally by adset).",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"}}}}}


# ================================================================
# 6. Bulk Apply (Budgets & Strategies)
# ================================================================

# class ApplyPlanAllocations(Tool):
#     """
#     Applies a frozen plan to the adsets table, skipping NO-OPs and returning only
#     the adsets that actually changed. Compares material fields only:
#       - daily_budget (after rounding to policy_snapshot.budget_rounding_unit)
#       - bid_strategy
#       - bid_amount (ONLY when bid_strategy == "cost_cap")
#     Required kwargs: plan_id, timestamp, request_id
#     Returns JSON:
#       {
#         "plan_id": <str>,
#         "applied_adsets": [<adset_id str>, ...],     # only mutated rows
#         "applied_adsets_count": <int>,
#         "noops_skipped": [<adset_id str>, ...],      # processed but unchanged
#         "timestamp": <ISO8601 str>,
#         "request_id": <str>
#       }
#     """
#     @staticmethod
#     def invoke(data: Dict[str, Any], **kwargs) -> str:
#         # 1) Validate args
#         err = _require(kwargs, ["plan_id", "timestamp", "request_id"])
#         if err:
#             return _fail(err)
#
#         plan_id = kwargs["plan_id"]
#         timestamp = kwargs["timestamp"]
#         request_id = kwargs["request_id"]
#
#         # 2) Load the plan (support historical/table naming variance)
#         plan = None
#         for table_name in ("plans", "plan_freezes"):
#             try:
#                 tbl = _assert_table(data, table_name)
#                 plan = _index(tbl, "plan_id").get(plan_id)
#                 if plan:
#                     break
#             except Exception:
#                 continue
#         if not plan:
#             return _fail(f"plan_id {plan_id} not found")
#
#         # 3) Pull required context
#         try:
#             adsets_tbl = _assert_table(data, "adsets")
#         except Exception as e:
#             return _fail(f"adsets table missing: {e}")
#
#         adsets_idx = _index(adsets_tbl, "adset_id")
#
#         policy = (plan.get("policy_snapshot") or {})
#         unit = policy.get("budget_rounding_unit", 1)
#         try:
#             unit = int(unit) if float(unit).is_integer() else float(unit)
#         except Exception:
#             unit = 1  # safe fallback
#
#         # Index strategies by adset_id for quick lookup
#         strategies_list = plan.get("strategies") or []
#         strategies = {str(s.get("adset_id")): s for s in strategies_list if "adset_id" in s}
#
#         def _round_budget(x: Any, u: Any) -> float:
#             # Nearest multiple rounding; robust to strings/ints/floats
#             try:
#                 fx = float(x)
#             except Exception:
#                 fx = 0.0
#             try:
#                 fu = float(u)
#                 if fu == 0:
#                     fu = 1.0
#             except Exception:
#                 fu = 1.0
#             return round(fx / fu) * fu
#
#         def _as_float_or_none(x: Any) -> Optional[float]:
#             try:
#                 return float(x) if x is not None else None
#             except (TypeError, ValueError):
#                 return None
#
#         changed_ids: List[str] = []
#         noop_ids: List[str] = []
#
#         # 4) Iterate allocations and apply only material changes
#         for alloc in (plan.get("allocations") or []):
#             if "adset_id" not in alloc or "budget" not in alloc:
#                 return _fail("invalid_allocation_row")
#
#             aid = str(alloc["adset_id"])
#             adset = adsets_idx.get(aid)
#             if not adset:
#                 return _fail(f"adset_id {aid} missing from DB")
#
#             # Target values from the plan envelope
#             target_budget = _round_budget(alloc.get("budget"), unit)
#
#             strat_row = strategies.get(aid, {})
#             target_strategy = (str(strat_row.get("bid_strategy", adset.get("bid_strategy") or "")).lower()
#                                or adset.get("bid_strategy"))
#             target_bid_amount = strat_row.get("bid_amount") if target_strategy == "cost_cap" else None
#             target_bid_amount = _as_float_or_none(target_bid_amount)
#
#             # Current values (normalized)
#             curr_budget = _round_budget(adset.get("daily_budget", 0.0), unit)
#             curr_strategy = str(adset.get("bid_strategy", "")).lower()
#             curr_bid_amount = _as_float_or_none(adset.get("bid_amount")) if curr_strategy == "cost_cap" else None
#
#             # Compare material fields
#             same_budget = (curr_budget == target_budget)
#             same_strategy = (curr_strategy == target_strategy)
#
#             if target_strategy == "cost_cap":
#                 # If plan omitted bid_amount, compare against current (allows true NO-OP)
#                 cmp_target_bid = target_bid_amount if target_bid_amount is not None else curr_bid_amount
#                 same_bid = (curr_bid_amount == cmp_target_bid)
#             else:
#                 same_bid = True  # bid_amount irrelevant for lowest_cost
#
#             # NO-OP: skip writing and do not count
#             if same_budget and same_strategy and same_bid:
#                 noop_ids.append(aid)
#                 continue
#
#             # Apply changes (material-only)
#             adset["daily_budget"] = float(target_budget)
#             adset["bid_strategy"] = target_strategy
#
#             if target_strategy == "cost_cap":
#                 # Preserve current bid if plan omitted it; if still None, that's an error
#                 if target_bid_amount is None and curr_bid_amount is not None:
#                     target_bid_amount = curr_bid_amount
#                 if target_bid_amount is None:
#                     return _fail(f"missing_bid_amount_for_cost_cap: adset_id {aid}")
#                 adset["bid_amount"] = float(target_bid_amount)
#             else:
#                 # lowest_cost: ensure stale bid_amount is removed
#                 adset.pop("bid_amount", None)
#
#             # Optionally bump an updated_at field if your schema uses it
#             # adset["updated_at"] = timestamp
#
#             changed_ids.append(aid)
#
#         # 5) Deterministic ordering of results
#         def _as_int(s: str) -> int:
#             try:
#                 return int(s)
#             except Exception:
#                 return 10**9  # push non-numeric to the end deterministically
#
#         changed_ids_sorted = sorted(changed_ids, key=_as_int)
#         noop_ids_sorted = sorted(noop_ids, key=_as_int)
#
#         result = {
#             "plan_id": plan_id,
#             "applied_adsets": changed_ids_sorted,  # <- always present
#             "applied_adsets_count": len(changed_ids_sorted),
#             "noops_skipped": noop_ids_sorted,  # optional but nice to have
#             "timestamp": timestamp,
#             "request_id": request_id,
#         }
#         return json.dumps(result)
#
#     @staticmethod
#     def get_info() -> Dict[str, Any]:
#         return {
#             "type": "function",
#             "function": {
#                 "name": "apply_plan_allocations",
#                 "description": "Apply a frozen plan to adsets, skipping no-ops and returning only mutated adsets.",
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "plan_id": {"type": "string"},
#                         "timestamp": {"type": "string"},
#                         "request_id": {"type": "string"},
#                     },
#                     "required": ["plan_id", "timestamp", "request_id"],
#                 },
#             },
#         }

# ================================================================
# apply_plan_allocations — with explicit NOOP reasons
#   - Keeps legacy 'noops_skipped': [adset_id, ...]
#   - Adds 'noops_details': [{"adset_id": "...", "reason": "..."}]
#   - Reasons enumerated (deterministic):
#       * "already_in_target_state" (respecting rounding rules)
#       * "below_min_budget_allocation"
# ================================================================
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


# ================================================================
# 7. Facts & Analytics
# ================================================================

class GetDailyInsightsForAdset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["adset_id", "date"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        rows = _assert_table(data, "f_insights")
        out = [r for r in rows if str(r.get("adset_id")) == str(kwargs["adset_id"]) and r.get("date") == kwargs["date"]]
        return json.dumps(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_daily_insights_for_adset",
                                                 "description": "Read f_insights for a specific day & adset.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"},
                                                                               "date": {"type": "string"}},
                                                                "required": ["adset_id", "date"]}}}


class GetViewershipForCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["category", "date"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        rows = _assert_table(data, "f_viewership")
        out = [r for r in rows if r.get("category") == kwargs["category"] and r.get("date") == kwargs["date"]]
        return json.dumps(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_viewership_for_category",
                                                 "description": "Read f_viewership for a category/date.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"category": {"type": "string"},
                                                                               "date": {"type": "string"}},
                                                                "required": ["category", "date"]}}}


class GetSalesByCategoryRange(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["category", "start_date", "end_date"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        rows = _assert_table(data, "f_sales")
        out = [r for r in rows if
               r.get("category") == kwargs["category"] and r.get("start_date") == kwargs["start_date"] and r.get(
                   "end_date") == kwargs["end_date"]]
        return json.dumps(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_sales_by_category_range",
                                                 "description": "Read f_sales summary for a category & range.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"category": {"type": "string"},
                                                                               "start_date": {"type": "string"},
                                                                               "end_date": {"type": "string"}},
                                                                "required": ["category", "start_date", "end_date"]}}}


class GetProductPriceOnDate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["product_id", "date"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        rows = _assert_table(data, "f_price")
        out = next((r for r in rows if
                    str(r.get("product_id")) == str(kwargs["product_id"]) and r.get("date") == kwargs["date"]), None)
        return json.dumps(out or {"error": "price_not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_product_price_on_date",
                                                 "description": "Read f_price for a product on a date.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"product_id": {"type": "string"},
                                                                               "date": {"type": "string"}},
                                                                "required": ["product_id", "date"]}}}


class FindUnderperformingAdsets(Tool):
    """Find adsets below a ROAS threshold for a given day (joins f_insights with adsets)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["date", "min_roas"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        ins = _assert_table(data, "f_insights")
        adsets = _index(_assert_table(data, "adsets"), "adset_id")
        th = float(kwargs["min_roas"])
        out = []
        for r in ins:
            if r.get("date") != kwargs["date"]:
                continue
            aid = str(r.get("adset_id"))
            spend = float(r.get("spend", 0.0));
            rev = float(r.get("revenue", 0.0))
            roas = (rev / spend) if spend > 0 else 0.0
            if roas < th:
                a = adsets.get(aid, {})
                out.append({"adset_id": aid, "roas": roas, "spend": spend, "revenue": rev, "status": a.get("status")})
        return json.dumps(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_underperforming_adsets",
                                                 "description": "Find adsets with ROAS below threshold on a date.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"date": {"type": "string"},
                                                                               "min_roas": {"type": "number"}},
                                                                "required": ["date", "min_roas"]}}}


# ================================================================
# 8. Automation / Logs
# ================================================================

class RecordAutomationRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        _ensure_list(data, "automation_runs")
        row = dict(kwargs)
        # try:
        #     t0 = datetime.fromisoformat(row["started_at"].replace("Z","+00:00"))
        #     t1 = datetime.fromisoformat(row["ended_at"].replace("Z","+00:00"))
        #     row["duration_ms"] = int((t1 - t0).total_seconds()*1000)
        # except Exception:
        #     row["duration_ms"] = None
        data["automation_runs"].append(row)
        return json.dumps(row)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "record_automation_run", "description": "Append an automation run log entry.",
                             "parameters": {"type": "object", "properties": {"run_type": {"type": "string"},
                                                                             "started_at": {"type": "string"},
                                                                             "ended_at": {"type": "string"},
                                                                             "status": {"type": "string"},
                                                                             "input_ref": {"type": "string"},
                                                                             "outputs_json": {"type": "object"},
                                                                             "errors_json": {
                                                                                 "type": ["object", "null"]}},
                                            "required": ["run_type", "started_at", "ended_at", "status", "input_ref",
                                                         "outputs_json"]}}}


class GetAutomationRunHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # optional filters by type
        rtype = kwargs.get("run_type")
        runs = _assert_table(data, "automation_runs")
        out = [r for r in runs if (rtype is None or r.get("run_type") == rtype)]
        return json.dumps(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_automation_run_history",
                                                 "description": "Read automation_runs (optionally filter by run_type).",
                                                 "parameters": {"type": "object",
                                                                "properties": {"run_type": {"type": "string"}}}}}



class InsertEntity(Tool):
    """Generic deterministic insert into supported tables (ads, adsets)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["table", "row", "timestamp", "request_id"])
        if err:
            return _fail(err)

        table = str(kwargs["table"])
        row = kwargs["row"]
        ts = str(kwargs["timestamp"])

        tbl = _assert_table(data, table)

        # Do NOT coerce row fields. Just append exactly what caller passed.
        # Optional: if the domain wants updated_at defaults, only set if missing.
        if table == "adsets" and "updated_at" not in row:
            row = {**row, "updated_at": ts}

        # Append verbatim and echo back
        tbl.append(copy.deepcopy(row))
        return json.dumps(row)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "insert_entity",
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
    """Rotate creatives per plan or explicit targets: add a new ad, pause worst active, activate new;
    update adset metadata; and log a deterministic rotation row.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Require deterministic fields; user must provide plan_id OR targets
        err = _require(kwargs, ["request_id", "timestamp", "rationale"])
        if err:
            return json.dumps({"error": err})
        if "plan_id" not in kwargs and "targets" not in kwargs:
            return json.dumps({"error": "missing_arg: plan_id_or_targets"})

        _ensure_list(data, "ads")
        _ensure_list(data, "adsets")
        _ensure_list(data, "creative_rotations")
        _ensure_list(data, "f_insights")
        _ensure_list(data, "plans")  # for plan_id path

        ts = kwargs["timestamp"]
        rationale = kwargs["rationale"]

        # ---- Build targets -------------------------------------------------
        # Option A: from plan_id (allocations[*].creative_type)
        targets: List[Dict[str, Any]] = []
        if "plan_id" in kwargs:
            pid = kwargs["plan_id"]
            plan = next((p for p in data["plans"] if str(p.get("plan_id")) == str(pid)), None)
            if not plan:
                return json.dumps({"error": f"missing_plan:{pid}"})
            for row in plan.get("allocations", []):
                ct = row.get("creative_type")
                if ct:
                    targets.append({
                        "adset_id": str(row.get("adset_id")),
                        "creative_type": ct,
                        "ad_name": row.get("ad_name")
                    })
        # Option B: explicit targets array
        if "targets" in kwargs and kwargs["targets"]:
            # normalize & merge (plan targets first, explicit targets can override)
            explicit: List[Dict[str, Any]] = kwargs["targets"]
            by_id = {t["adset_id"]: t for t in targets if t.get("adset_id")}
            for t in explicit:
                aid = str(t.get("adset_id"))
                if not aid or "creative_type" not in t:
                    return json.dumps({"error": "invalid_target: require adset_id and creative_type"})
                by_id[aid] = {
                    "adset_id": aid,
                    "creative_type": t["creative_type"],
                    "ad_name": t.get("ad_name")
                }
            targets = list(by_id.values())

        if not targets:
            # Nothing to do; deterministic no-op
            return json.dumps({
                "plan_id": kwargs.get("plan_id"),
                "request_id": kwargs["request_id"],
                "updated_adsets": [],
                "rotations": []
            })

        # ---- Helpers -------------------------------------------------------
        ads_by_adset: Dict[str, List[Dict[str, Any]]] = {}
        for a in data["ads"]:
            ads_by_adset.setdefault(str(a.get("adset_id")), []).append(a)

        def _worst_active(adset_id: str) -> Optional[str]:
            actives = [a for a in ads_by_adset.get(adset_id, []) if a.get("status") == "active"]
            if not actives:
                return None
            # Compute naive CPA = spend / purchases from f_insights (if available)
            cpa_by_ad: Dict[str, float] = {}
            for row in data.get("f_insights", []):
                if str(row.get("adset_id")) == adset_id:
                    ad_id = str(row.get("ad_id"))
                    spend = float(row.get("spend", 0.0) or 0.0)
                    purchases = float(row.get("purchases", 0.0) or 0.0)
                    cpa_by_ad[ad_id] = (spend / purchases) if purchases > 0 else float("inf")
            actives.sort(key=lambda x: cpa_by_ad.get(str(x.get("ad_id")), float("inf")), reverse=True)
            return str(actives[0].get("ad_id"))

        def _next_ad_id() -> str:
            mx = 0
            for a in data["ads"]:
                try:
                    mx = max(mx, int(str(a.get("ad_id"))))
                except Exception:
                    continue
            return str(mx + 1)

        def _next_rotation_id() -> str:
            mx = 0
            for r in data["creative_rotations"]:
                rid = str(r.get("rotation_id", "")).replace("CR-", "")
                if rid.isdigit():
                    mx = max(mx, int(rid))
            return f"CR-{mx + 1}"

        # ---- Apply per-adset ----------------------------------------------
        updated: List[str] = []
        rotations_written: List[str] = []

        for spec in targets:
            adset_id = str(spec["adset_id"])
            want_type = spec["creative_type"]

            current_active = [a for a in ads_by_adset.get(adset_id, []) if a.get("status") == "active"]
            current_type = current_active[0].get("creative_type") if current_active else None

            # If already correct and single active, skip
            if current_type == want_type and len(current_active) == 1:
                continue

            old_active_id = _worst_active(adset_id)

            # Create new active ad
            new_id = _next_ad_id()
            new_ad = {
                "ad_id": new_id,
                "adset_id": adset_id,
                "name": spec.get("ad_name", f"{adset_id}-{want_type}-auto"),
                "creative_type": want_type,
                "status": "active",
                "start_date": ts.split("T")[0],
                "end_date": None,
            }
            data["ads"].append(new_ad)
            ads_by_adset.setdefault(adset_id, []).append(new_ad)

            # Pause previous worst active (if any)
            if old_active_id:
                for a in data["ads"]:
                    if str(a.get("ad_id")) == old_active_id:
                        a["status"] = "paused"

            # Touch adset metadata deterministically
            for aset in data["adsets"]:
                if str(aset.get("adset_id")) == adset_id:
                    aset["updated_at"] = ts
                    aset["rev"] = _i(aset.get("rev"), 0) + 1
                    break

            # Rotation log row (strict schema)
            rot_id = _next_rotation_id()
            data["creative_rotations"].append({
                "rotation_id": rot_id,
                "adset_id": adset_id,
                "old_ad_id": old_active_id,
                "new_ad_id": new_id,
                "old_type": current_type,
                "new_type": want_type,
                "rotated_at": ts,
                "rationale": rationale,
                "request_id": kwargs["request_id"],
            })

            updated.append(adset_id)
            rotations_written.append(rot_id)

        return json.dumps({
            "plan_id": kwargs.get("plan_id"),
            "request_id": kwargs["request_id"],
            "updated_adsets": updated,
            "rotations": rotations_written
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_creatives",
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
                                "required": ["adset_id", "creative_type"]
                            }
                        },
                        "request_id": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "rationale": {"type": "string"},
                    },
                    "required": ["request_id", "timestamp", "rationale"]
                },
            },
        }

# ================================================================
# 9. Registry (function names are snake_case like v4)
# ================================================================

TOOLS = [
    # Planning & Policy
    GetPlanForDate(),
    GetAdsetAllocationFromPlan(),
    FreezePlan(),
    VerifyPlanAgainstAdsets(),
    UpdatePlanStatus(),
    GetPolicyParameter(),

    # Campaigns
    GetCampaignByName(),
    CreateCampaign(),
    UpdateCampaignStatus(),

    # Adsets
    GetAdsetsByCampaignID(),
    GetAdsetDetailsByID(),
    CreateAdset(),
    UpdateAdsetBudget(),
    UpdateAdsetBidStrategy(),
    UpdateAdsetStatus(),

    # Ads
    GetAdsByAdsetID(),
    CreateAd(),
    UpdateAdStatus(),

    # Creative Rotation
    RotateAdCreative(),
    GetCreativeRotationHistory(),

    # Bulk Apply
    ApplyPlanAllocations(),

    # Facts & Analytics
    GetDailyInsightsForAdset(),
    GetViewershipForCategory(),
    GetSalesByCategoryRange(),
    GetProductPriceOnDate(),
    FindUnderperformingAdsets(),

    # Automation
    RecordAutomationRun(),
    GetAutomationRunHistory(),

    InsertEntity(),
    ApplyCreatives(),
]


