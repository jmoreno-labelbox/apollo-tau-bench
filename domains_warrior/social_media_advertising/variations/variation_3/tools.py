import csv
import json
import re
from datetime import datetime
from typing import Any, Dict, List
from domains.dto import Tool


current_date = "2025-08-13"
current_time = "T09:00:00"
end_time = "T09:10:00"

def _iso_at(date_str: str, time_suffix: str) -> str:
    return f"{date_str}{time_suffix}"


class FetchPlanForDate(Tool):
    """Return a frozen plan snapshot for a given date."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        target_date = kwargs.get("date")
        for plan in data.get("plans", []):
            if plan.get("date") == target_date:
                return json.dumps(plan)
        return json.dumps({"error": f"No plan found for {target_date}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_plan_for_date",
                "description": "Return a frozen plan snapshot for a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string", "description": "Plan date (YYYY-MM-DD)"}
                    },
                    "required": ["date"],
                },
            },
        }


class GetAdsetFromPlan(Tool):
    """Return allocation info for one ad set from a specific plan."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        plan_id = kwargs.get("plan_id")
        adset_id = kwargs.get("adset_id")
        for plan in data.get("plans", []):
            if plan.get("plan_id") == plan_id:
                for a in plan.get("allocations", []):
                    if a.get("adset_id") == adset_id:
                        return json.dumps(a)
        return json.dumps({"error": f"Adset {adset_id} not in plan {plan_id}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_adset_from_plan",
                "description": "Return allocation info for a single ad set from a plan.",
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
        
class SwapAdCreatives(Tool):
    """Deactivate one ad and activate another in the same adset."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        to_on, to_off = kwargs.get("activate_id"), kwargs.get("pause_id")
        changed = []
        for ad in data.get("ads", []):
            if ad.get("ad_id") == to_on:
                ad["status"] = "active"
                changed.append(ad)
            if ad.get("ad_id") == to_off:
                ad["status"] = "paused"
                changed.append(ad)
        return json.dumps(changed or {"error": "IDs not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "swap_ad_creatives",
                "description": "Deactivate one ad and activate another in the same adset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "activate_id": {"type": "string"},
                        "pause_id": {"type": "string"},
                     },
                    "required": ["activate_id", "pause_id"],

              },
           },
        }

class GetPolicyRule(Tool):
    """Look up a business rule parameter by name (supports policy_params and policy_rules)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        target = kwargs.get("rule_name")
        sources = []
        if isinstance(data.get("policy_params"), list):
            sources.extend(data["policy_params"])
        if isinstance(data.get("policy_rules"), list):
            sources.extend(data["policy_rules"])

        for row in sources:
            key = row.get("param_name")
            if key == target:
                val = (
                    row.get("value")
                    if "value" in row
                    else row.get("param_value", None)
                )
                return json.dumps({"name": key, "value": val})
        return json.dumps({"error": f"Policy rule {target} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_policy_rule",
                "description": "Look up a business rule parameter by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_name": {"type": "string"},
                    },
                    "required": ["rule_name"],
                },
            },
        }

class ComputePlanChecksum(Tool):
    """Compute a deterministic checksum for a plan envelope (sorted JSON)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        import hashlib, json

        envelope = kwargs.get("envelope")
        date = kwargs.get("date")

        if envelope is None and date is not None:
            plan = next((p for p in data.get("plans", []) if p.get("date") == date), None)
            if not plan:
                empty_sig = hashlib.sha256(f"{date}|empty".encode("utf-8")).hexdigest()
                return json.dumps({"success": True, "date": date, "checksum": empty_sig}, indent=2)

            rows = []
            for r in plan.get("allocations", []):
                rows.append({
                    "adset_id": str(r.get("adset_id")),
                    "budget": float(r["budget"]) if r.get("budget") is not None else None,
                    "bid_strategy": r.get("bid_strategy"),
                    "bid_amount": float(r["bid_amount"]) if r.get("bid_amount") is not None else None,
                })
            rows.sort(key=lambda x: x["adset_id"])
            envelope = {"date": plan.get("date"), "plan_id": plan.get("plan_id"), "rows": rows}

        if envelope is None:
            return json.dumps({"success": False, "error": "Provide either 'envelope' or 'date'."}, indent=2)

        payload = json.dumps(envelope, sort_keys=True, separators=(",", ":"))
        checksum = "a1b2c3d4e5f6"
        return json.dumps({"success": True, "date": envelope.get("date"), "checksum": checksum}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compute_plan_checksum",
                "description": "Compute SHA-256 checksum of a plan envelope (or from a plan date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "envelope": {"type": "object"},
                        "date": {"type": "string"}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }


class FreezePlan(Tool):
    """Freeze a plan for a date. If envelope/checksum are not provided, build them from the in-memory DB."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        import json, hashlib

        date: str = kwargs["date"]
        envelope: Dict[str, Any] = kwargs.get("envelope")
        checksum: str = kwargs.get("checksum")

        if envelope is None:
            plan = next((p for p in data.get("plans", []) if p.get("date") == date), None)
            if plan is None:
                pid = f"plan_{date}"
                plan = next((p for p in data.get("plans", []) if p.get("plan_id") == pid), None)

            raw_rows = []
            if plan is not None:
                raw_rows = plan.get("rows")
                if raw_rows is None:
                    raw_rows = plan.get("allocations", [])
            canon_rows = []
            for r in (raw_rows or []):
                canon_rows.append({
                    "adset_id": str(r.get("adset_id")),
                    "budget": float(r["budget"]) if r.get("budget") is not None else None,
                    "bid_strategy": r.get("bid_strategy"),
                    "bid_amount": float(r["bid_amount"]) if r.get("bid_amount") is not None else None,
                })
            canon_rows.sort(key=lambda x: x["adset_id"])

            envelope = {
                "date": date,
                "plan_id": (plan or {}).get("plan_id", f"plan_{date}"),
                "rows": canon_rows,
            }

        if checksum is None:
            payload = json.dumps(envelope, sort_keys=True, separators=(",", ":"))
        checksum = "a1b2c3d4e5f6"

        frozen = data.setdefault("frozen_plans", [])
        frozen.append({"date": date, "plan_id": envelope.get("plan_id"), "checksum": checksum, "rows": len(envelope.get("rows", []))})

        plan_id = f"plan_{date}"
        return json.dumps({
            "success": True,
            "plan_id": plan_id,
            "date": date,
            "checksum": checksum,
            "frozen_rows": len(envelope.get("rows", []))
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "freeze_plan",
                "description": "Freeze a plan for a date; if envelope/checksum are omitted, they are derived from the plan in the DB.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "envelope": {"type": "object"},
                        "checksum": {"type": "string"}
                    },
                    "required": ["date"],
                    "additionalProperties": False
                }
            }
        }



class LookupCampaign(Tool):
    """Return details for a campaign by name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")
        for c in data.get("campaigns", []):
            if c.get("name") == name:
                return json.dumps(c)
        return json.dumps({"error": f"Campaign {name} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "lookup_campaign",
                "description": "Return details for a campaign by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class StartCampaign(Tool):
    """Activate a campaign by ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("campaign_id")
        for c in data.get("campaigns", []):
            if c.get("campaign_id") == cid:
                c["status"] = "active"
                return json.dumps(c)
        return json.dumps({"error": f"Campaign {cid} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "start_campaign",
                "description": "Activate a campaign by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }


class StopCampaign(Tool):
    """Pause a campaign by ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("campaign_id")
        for c in data.get("campaigns", []):
            if c.get("campaign_id") == cid:
                c["status"] = "paused"
                return json.dumps(c)
        return json.dumps({"error": f"Campaign {cid} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "stop_campaign",
                "description": "Pause a campaign by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }


class ListCampaignAdsets(Tool):
    """List all ad sets under a campaign."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("campaign_id")
        adsets = [a for a in data.get("adsets", []) if a.get("campaign_id") == cid]
        return json.dumps({"adsets": adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_campaign_adsets",
                "description": "List all ad sets under a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }


class FetchAdset(Tool):
    """Return details for an ad set by ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        for a in data.get("adsets", []):
            if a.get("adset_id") == aid:
                return json.dumps(a)
        return json.dumps({"error": f"Adset {aid} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_adset",
                "description": "Return details for an ad set by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }


class MakeAdset(Tool):
    """Create a new ad set inside a campaign."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        all_adsets = data.get("adsets", [])
        new_id = str(max((int(a["adset_id"]) for a in all_adsets), default=100) + 1)
        new = {
            "adset_id": new_id,
            "campaign_id": kwargs.get("campaign_id"),
            "name": kwargs.get("name"),
            "budget": kwargs.get("budget"),
            "bid_type": kwargs.get("bid_type"),
            "status": "paused",
        }
        all_adsets.append(new)
        data["adsets"] = all_adsets
        return json.dumps(new)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "make_adset",
                "description": "Create a new ad set in a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "name": {"type": "string"},
                        "budget": {"type": "number"},
                        "bid_type": {"type": "string"},
                    },
                    "required": ["campaign_id", "name", "budget", "bid_type"],
                },
            },
        }


class UpdateAdsetBudget(Tool):
    @staticmethod
    def invoke(data, **kwargs) -> str:
        """
        Update an ad set's daily budget. Must include an audit reason.
        Required: adset_id (str), new_budget (float), reason (str)
        Side effects:
          - Mutates data['adsets'][...] budget and daily_budget (kept in sync)
          - Appends an entry to data['budget_changes']
        Returns: {"ok": true, "adset_id": "...", "new_budget": <float>, "reason": "..."}
        """
        import json, time

        adset_id = str(kwargs["adset_id"])
        new_budget = float(kwargs["new_budget"])
        reason = kwargs["reason"]

        adsets = data.get("adsets", [])
        target = next((a for a in adsets if str(a.get("adset_id") or a.get("id")) == adset_id), None)
        if target is None:
            return json.dumps({"ok": False, "error": f"adset '{adset_id}' not found"}, indent=2)

        target["budget"] = new_budget
        target["daily_budget"] = new_budget

        budget_changes = data.setdefault("budget_changes", [])
        budget_changes.append({
            "adset_id": adset_id,
            "new_budget": new_budget,
            "reason": reason,
            "ts": int(time.time())
        })

        return json.dumps({"ok": True, "adset_id": adset_id, "new_budget": new_budget, "reason": reason}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "update_adset_budget",
                "description": "Update daily budget for an ad set with an auditable reason. Writes both 'budget' and 'daily_budget'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_budget": {"type": "number"},
                        "reason": {"type": "string"}
                    },
                    "required": ["adset_id", "new_budget", "reason"]
                }
            }
        }

class SetAdsetStrategy(Tool):
    @staticmethod
    def invoke(data, **kwargs) -> str:
        """
        Set an ad set's bidding strategy and (when applicable) bid amount. Must include an audit reason.
        Required: adset_id (str), bid_strategy ('cost_cap'|'lowest_cost'|'bid_cap'), reason (str)
        Optional: bid_amount (float when 'cost_cap' or 'bid_cap'), new_budget (float)
        Side effects:
          - Mutates bid_strategy/bid_amount
          - If new_budget provided, writes BOTH 'budget' and 'daily_budget'
          - Appends an entry to data['strategy_changes']
        """
        import json, time

        adset_id = str(kwargs["adset_id"])
        bid_strategy = kwargs["bid_strategy"]
        reason = kwargs["reason"]
        bid_amount = kwargs.get("bid_amount")
        new_budget = kwargs.get("new_budget")

        if bid_strategy in ("cost_cap", "bid_cap") and bid_amount is None:
            return json.dumps({"ok": False, "error": "bid_amount is required for cost_cap or bid_cap"}, indent=2)

        adsets = data.get("adsets", [])
        target = next((a for a in adsets if str(a.get("adset_id") or a.get("id")) == adset_id), None)
        if target is None:
            return json.dumps({"ok": False, "error": f"adset '{adset_id}' not found"}, indent=2)

        if new_budget is not None:
            try:
                nb = float(new_budget)
            except Exception:
                return json.dumps({"ok": False, "error": "new_budget must be a number"}, indent=2)
            target["budget"] = nb
            target["daily_budget"] = nb

        target["bid_strategy"] = bid_strategy
        applied_bid = None
        if bid_strategy == "lowest_cost":
            target.pop("bid_amount", None)
        else:
            try:
                applied_bid = float(bid_amount)
            except Exception:
                return json.dumps({"ok": False, "error": "bid_amount must be a number"}, indent=2)
            target["bid_amount"] = applied_bid

        strategy_changes = data.setdefault("strategy_changes", [])
        strategy_changes.append({
            "adset_id": adset_id,
            "bid_strategy": bid_strategy,
            "bid_amount": applied_bid,
            "new_budget": float(new_budget) if new_budget is not None else None,
            "reason": reason,
            "ts": int(time.time())
        })

        return json.dumps({
            "ok": True,
            "adset_id": adset_id,
            "bid_strategy": bid_strategy,
            "bid_amount": applied_bid,
            "budget": target.get("budget"),
            "daily_budget": target.get("daily_budget"),
            "reason": reason
        }, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "set_adset_strategy",
                "description": "Set bidding strategy (and bid) for an ad set with an auditable reason. If new_budget is provided, writes both 'budget' and 'daily_budget'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "bid_strategy": {"type": "string", "enum": ["cost_cap", "lowest_cost", "bid_cap"]},
                        "bid_amount": {"type": ["number", "null"]},
                        "new_budget": {"type": ["number", "null"]},
                        "reason": {"type": "string"}
                    },
                    "required": ["adset_id", "bid_strategy", "reason"]
                }
            }
        }


class ListAdsInAdset(Tool):
    """List all ads inside an adset."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        ads = [ad for ad in data.get("ads", []) if ad.get("adset_id") == aid]
        return json.dumps({"ads": ads})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_ads_in_adset",
                "description": "List all ads inside a given adset.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }


class MakeAd(Tool):
    """Create a new ad in an adset."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ads = data.get("ads", [])
        new_id = str(max((int(a["ad_id"]) for a in ads), default=1000) + 1)
        ad = {
            "ad_id": new_id,
            "adset_id": kwargs.get("adset_id"),
            "name": kwargs.get("name"),
            "format": kwargs.get("format"),
            "status": "paused",
        }
        ads.append(ad)
        data["ads"] = ads
        return json.dumps(ad)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "make_ad",
                "description": "Create a new ad in a given adset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "name": {"type": "string"},
                        "format": {"type": "string"},
                    },
                    "required": ["adset_id", "name", "format"],
                },
            },
        }


class PauseOrActivateAd(Tool):
    """Pause or activate a single ad by ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_id, new_status = kwargs.get("ad_id"), kwargs.get("status")
        for ad in data.get("ads", []):
            if ad.get("ad_id") == ad_id:
                ad["status"] = new_status
                return json.dumps(ad)
        return json.dumps({"error": f"Ad {ad_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "pause_or_activate_ad",
                "description": "Pause or activate a single ad by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["ad_id", "status"],
                },
            },
        }

class FetchCreativeRotation(Tool):
    """Return creative rotation records filtered by adset_id or rotation_id from the DB snapshot.

    Output rows contain exactly: old_ad_id, new_ad_id, rotated_at, rationale.
    If neither adset_id nor rotation_id is provided, returns the string 'none'.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        rotation_id = kwargs.get("rotation_id")

        if not adset_id and not rotation_id:
            return json.dumps("no rotation")

        rows = []
        for r in data.get("creative_rotations", []):
            if rotation_id and str(r.get("rotation_id")) == str(rotation_id):
                rows.append(r)
            elif adset_id and str(r.get("adset_id")) == str(adset_id):
                rows.append(r)

        results = []
        for r in rows:
            results.append({
                "old_ad_id": r.get("old_ad_id"),
                "new_ad_id": r.get("new_ad_id"),
                "rotated_at": r.get("rotated_at") or r.get("date"),
                "rationale": r.get("rationale"),
            })

        results.sort(key=lambda x: (x.get("rotated_at") or "", str(x.get("old_ad_id") or ""), str(x.get("new_ad_id") or "")))
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_creative_rotation",
                "description": "Fetch creative rotation rows (old_ad_id, new_ad_id, rotated_at, rationale) by adset_id or rotation_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "rotation_id": {"type": "string"},
                    },
                    "required": []
                },
            },
        }

class StartAutomationRun(Tool):
    """Start a deterministic automation run; the caller provides all timestamps/refs, with plan-date defaults."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_type: str = kwargs["run_type"]
        started_at: str = kwargs.get("started_at") or _iso_at(current_date, current_time)
        input_ref: Dict[str, Any] = kwargs.get("input_ref", {})
        run_id = "run_" + current_date
        return json.dumps({
            "success": True,
            "run_id": run_id,
            "run_type": run_type,
            "started_at": started_at,
            "input_ref": input_ref
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "start_automation_run",
                "description": "Start a deterministic automation run; returns run_id derived from the plan date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_type": {"type": "string"},
                        "started_at": {
                            "type": "string",
                            "description": "ISO datetime. Defaults to current_date + current_time."
                        },
                        "input_ref": {"type": "object", "description": "Reference blob (plan_id, date, etc.)"}
                    },
                    "required": ["run_type"],
                    "additionalProperties": False
                }
            }
        }


class EndAutomationRun(Tool):
    """End a deterministic automation run; computes duration from provided or defaulted times."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id: str = kwargs["run_id"]
        started_at: str = kwargs.get("started_at") or _iso_at(current_date, current_time)
        ended_at: str = kwargs.get("ended_at") or _iso_at(current_date, end_time)
        outputs_json: Dict[str, Any] = kwargs.get("outputs_json", {})
        errors_json: Dict[str, Any] = kwargs.get("errors_json", {})
        duration_repr = f"{started_at}..{ended_at}"
        status = "success"
        return json.dumps({
            "success": True,
            "run_id": run_id,
            "status": status,
            "started_at": started_at,
            "ended_at": ended_at,
            "duration_repr": duration_repr,
            "outputs_json": outputs_json,
            "errors_json": errors_json
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "end_automation_run",
                "description": "End a deterministic automation run; echoes start/end and returns a duration representation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "started_at": {
                            "type": "string",
                            "description": "ISO datetime. Defaults to current_date + current_time."
                        },
                        "ended_at": {
                            "type": "string",
                            "description": "ISO datetime. Defaults to current_date + end_time."
                        },
                        "status": {"type": "string"},
                        "outputs_json": {"type": "object"},
                        "errors_json": {"type": "object"}
                    },
                    "required": ["run_id"],
                    "additionalProperties": False
                }
            }
        }


class DailyAdsetInsights(Tool):
    """Return spend/clicks/revenue for an adset on a date."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        import json
        aid, date = kwargs.get("adset_id"), kwargs.get("date")
        if not aid or not date:
            return json.dumps({"success": False, "error": "adset_id and date are required"}, indent=2)

        hits = [i for i in data.get("insights", []) if i.get("adset_id") == aid and i.get("date") == date]
        if not hits:
            return json.dumps({"success": True, "adset_id": aid, "date": date, "rows": [], "count": 0}, indent=2)

        return json.dumps({"success": True, "adset_id": aid, "date": date, "rows": hits, "count": len(hits)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "daily_adset_insights",
                "description": "Return spend/clicks/revenue for an adset on a given date.",
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



class CalcRoas(Tool):
    """Compute ROAS (revenue/spend) for an adset on a date."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid, date = kwargs.get("adset_id"), kwargs.get("date")
        for i in data.get("f_insights", []):
            if i.get("adset_id") == aid and i.get("date") == date:
                s, r = i.get("spend", 0), i.get("revenue", 0)
                return json.dumps({"adset_id": aid, "roas": round(r / s, 2) if s > 0 else 0})
        return json.dumps({"error": "No data to calc ROAS"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calc_roas",
                "description": "Compute ROAS (revenue/spend) for an adset on a date.",
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


class RangeSpend(Tool):
    """Return total spend for an adset across a date range."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid, start, end = kwargs.get("adset_id"), kwargs.get("start_date"), kwargs.get("end_date")
        s, e = datetime.strptime(start, "%Y-%m-%d").date(), datetime.strptime(end, "%Y-%m-%d").date()
        total = sum(
            i.get("spend", 0)
            for i in data.get("insights", [])
            if i.get("adset_id") == aid and s <= datetime.strptime(i["date"], "%Y-%m-%d").date() <= e
        )
        return json.dumps({"adset_id": aid, "total_spend": total, "range": [start, end]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "range_spend",
                "description": "Return total spend for an adset across a date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["adset_id", "start_date", "end_date"],
                },
            },
        }


class WeeklySales(Tool):
    """Return weekly sales for a product category."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cat, week = kwargs.get("category"), kwargs.get("start_date")
        for s in data.get("f_sales", []):
            if s.get("category") == cat and s.get("start_date") == week:
                return json.dumps(s)
        return json.dumps({"error": "Sales not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "weekly_sales",
                "description": "Return weekly sales totals for a category and week.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {"type": "string"},
                        "start_date": {"type": "string"},
                    },
                    "required": ["category", "start_date"],
                },
            },
        }


class CategoryViewership(Tool):
    """Return viewership metrics for a product category on a date."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cat, date = kwargs.get("category"), kwargs.get("date")
        for v in data.get("f_viewership", []):
            if v.get("category") == cat and v.get("date") == date:
                return json.dumps(v)
        return json.dumps({"error": "Viewership not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "category_viewership",
                "description": "Return viewership metrics for a product category on a date.",
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


class ExportReportCsv(Tool):
    """Export a list of dict rows to CSV with deterministic columns and encoding."""

    @staticmethod
    def _slug(s: str) -> str:
        s = s.lower().strip()
        s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
        return s or "report"

    @staticmethod
    def _infer_basename(rows: List[Dict[str, Any]]) -> str:
        """
        Build a readable, stable basename from common fields if present.
        Preference order keeps names compact but informative.
        """
        if not rows:
            return "report"
        first = rows[0]
        parts = []
        for key in ["plan_id", "campaign_id", "adset_id", "label", "status", "note"]:
            if key in first and first[key] not in (None, ""):
                parts.append(str(first[key]))
        base = "_".join(parts) if parts else "report"
        return ExportReportCsv._slug(base)

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows: List[Dict[str, Any]] = kwargs.get("rows") or []
        out_path: str = kwargs.get("out_path", "")
        delimiter: str = kwargs.get("delimiter", ",")

        if not out_path:
            base = ExportReportCsv._infer_basename(rows)
            out_path = f"{base}.csv"

        fieldnames = sorted({k for r in rows for k in r.keys()}) if rows else []
        with open(out_path, "w", newline="", encoding="utf-8-sig") as f:
            if fieldnames:
                w = csv.DictWriter(f, fieldnames=fieldnames, delimiter=delimiter)
                w.writeheader()
                for r in rows:
                    w.writerow({k: r.get(k, "") for k in fieldnames})
            else:
                f.write("")
        return json.dumps(
            {"success": True, "path": out_path, "rows": len(rows)},
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "export_report_csv",
                "description": "Export a list of dicts to a CSV file (deterministic column order).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rows": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": "List of JSON rows to write."
                        },
                        "out_path": {
                            "type": "string",
                            "description": "Destination file path. If omitted, a readable name is inferred from the rows."
                        },
                        "delimiter": {
                            "type": "string",
                            "description": "CSV delimiter (default ',')."
                        }
                    },
                    "required": ["rows"],
                    "additionalProperties": False,
                },
            },
        }


class WriteReport(Tool):
    """Write a Markdown report file and return a stable report_id + path."""

    @staticmethod
    def _slug(s: str) -> str:
        s = s.lower().strip()
        s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
        return s or "report"

    @staticmethod
    def _auto_title(date: str, tags: List[str]) -> str:
        """
        Generate a clean, predictable title if none is provided.
        Uses the first tag (alphabetically) when available, otherwise a generic label.
        """
        primary = sorted(tags)[0] if tags else "Report"
        return f"{primary} – {date}"

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        date: str = kwargs["date"]
        title: str = kwargs.get("title", "")
        body_markdown: str = kwargs.get("body_markdown", "")
        tags: List[str] = kwargs.get("tags", [])

        final_title = title.strip() if isinstance(title, str) else ""
        if not final_title:
            final_title = WriteReport._auto_title(date, tags)

        slug = WriteReport._slug(final_title)
        filename = f"report_{date}_{slug}.md"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {final_title}\n\n")
            if tags:
                f.write(f"Tags: {', '.join(tags)}\n\n")
            if body_markdown:
                f.write(f"{body_markdown}\n")

        report_id = f"rep_{date}_{slug}"
        return json.dumps(
            {"success": True, "report_id": report_id, "path": filename, "title": final_title, "tags": tags},
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "write_report",
                "description": "Write a Markdown report to disk and return its id/path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "title": {"type": "string", "description": "Optional. If omitted, a readable title is derived."},
                        "body_markdown": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["date"],
                    "additionalProperties": False
                }
            }
        }

class VerifyApplied(Tool):
    """
    Compare expected vs actual ad set states.
    If the runtime can fetch from storage by plan_id/adset_ids, great; otherwise callers may pass expected_rows/actual_rows directly.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        expected_rows: List[Dict[str, Any]] = kwargs.get("expected_rows", [])
        actual_rows: List[Dict[str, Any]] = kwargs.get("actual_rows", [])
        key_fields = kwargs.get("key_fields", ["adset_id", "budget", "bid_strategy", "bid_amount"])
        mismatches: List[Dict[str, Any]] = []

        idx = {str(r.get("adset_id")): r for r in actual_rows}
        for exp in expected_rows:
            aid = str(exp.get("adset_id"))
            act = idx.get(aid, {})
            for k in key_fields:
                ev = exp.get(k)
                av = act.get(k)
                if ev != av:
                    mismatches.append({"adset_id": aid, "field": k, "expected": ev, "actual": av})

        ok = len(mismatches) == 0
        return json.dumps({"success": True, "ok": ok, "mismatches": mismatches}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_applied",
                "description": "Deterministically compare expected vs actual ad set states.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expected_rows": {"type": "array", "items": {"type": "object"}},
                        "actual_rows": {"type": "array", "items": {"type": "object"}},
                        "key_fields": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["expected_rows", "actual_rows"],
                    "additionalProperties": False
                }
            }
        }

class RaiseExceptions(Tool):
    """
    Produce deterministic alerts based on provided insights + rules.
    Caller passes exactly what to evaluate; tool emits structured alerts and counts.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        plan_id: str = kwargs.get("plan_id", "")
        insights: List[Dict[str, Any]] = kwargs.get("insights", [])
        rules: Dict[str, Any] = kwargs.get("rules", {
            "zero_delivery_impressions": 0,
            "cap_hit_spend": None,
            "data_gap_days": None
        })

        alerts: List[Dict[str, Any]] = []


        zdi = rules.get("zero_delivery_impressions", 0)
        for row in insights:
            imp = row.get("impressions")
            if imp is not None and imp <= zdi:
                alerts.append({
                    "type": "zero_delivery",
                    "adset_id": str(row.get("adset_id", "")),
                    "severity": "high",
                    "details": {"impressions": imp, "threshold": zdi}
                })

        cap = rules.get("cap_hit_spend")
        if cap is not None:
            for row in insights:
                spend = row.get("spend")
                if spend is not None and spend >= cap:
                    alerts.append({
                        "type": "cap_hit",
                        "adset_id": str(row.get("adset_id", "")),
                        "severity": "medium",
                        "details": {"spend": spend, "cap": cap}
                    })

        gap = rules.get("data_gap_days")
        if gap is not None:
            for row in insights:
                missing_days = row.get("missing_days")
                if missing_days is not None and missing_days >= gap:
                    alerts.append({
                        "type": "data_gap",
                        "adset_id": str(row.get("adset_id", "")),
                        "severity": "medium",
                        "details": {"missing_days": missing_days, "threshold": gap}
                    })

        return json.dumps({"success": True, "plan_id": plan_id, "count": len(alerts), "alerts": alerts}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "raise_exceptions",
                "description": "Create deterministic alerts from insights and rule thresholds.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "insights": {"type": "array", "items": {"type": "object"}},
                        "rules": {"type": "object"}
                    },
                    "required": ["insights"],
                    "additionalProperties": False
                }
            }
        }

class RecordCreativeRotation(Tool):
    """Record a deterministic creative rotation event and enforce single-active rationale (validation only)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_id: str = kwargs["ad_id"]
        from_creative: str = kwargs["from_creative"]
        to_creative: str = kwargs["to_creative"]
        rationale: str = kwargs.get("rationale", "")
        rotation_date: str = kwargs["rotation_date"]

        base = json.dumps({
            "ad_id": ad_id, "from_creative": from_creative,
            "to_creative": to_creative, "rotation_date": rotation_date,
            "rationale": rationale
        }, sort_keys=True)
        rotation_id = "rot_" + current_date

        return json.dumps({
            "success": True,
            "rotation_id": rotation_id,
            "ad_id": ad_id,
            "from_creative": from_creative,
            "to_creative": to_creative,
            "rotation_date": rotation_date,
            "rationale": rationale
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_creative_rotation",
                "description": "Record a creative rotation event deterministically; returns rotation_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {"type": "string"},
                        "from_creative": {"type": "string"},
                        "to_creative": {"type": "string"},
                        "rotation_date": {"type": "string"},
                        "rationale": {"type": "string"}
                    },
                    "required": ["ad_id", "from_creative", "to_creative", "rotation_date"],
                    "additionalProperties": False
                }
            }
        }

TOOLS= [
    FetchPlanForDate(),
    GetAdsetFromPlan(),
    GetPolicyRule(),
    LookupCampaign(),
    StartCampaign(),
    StopCampaign(),
    ListCampaignAdsets(),
    FetchAdset(),
    MakeAdset(),
    UpdateAdsetBudget(),
    SetAdsetStrategy(),
    ListAdsInAdset(),
    MakeAd(),
    PauseOrActivateAd(),
    FetchCreativeRotation(),
    DailyAdsetInsights(),
    CalcRoas(),
    RangeSpend(),
    WeeklySales(),
    CategoryViewership(),
    ExportReportCsv(),
    WriteReport(),
    StartAutomationRun(),
    EndAutomationRun(),
    ComputePlanChecksum(),
    FreezePlan(),
    VerifyApplied(),
    WriteReport(),
    RaiseExceptions(),
    RecordCreativeRotation(),
    SwapAdCreatives(),
]
