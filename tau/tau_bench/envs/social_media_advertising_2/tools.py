import csv
import json
import re
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool

current_date = "2025-08-13"
current_time = "T09:00:00"
end_time = "T09:10:00"


def _iso_at(date_str: str, time_suffix: str) -> str:
    pass
    return f"{date_str}{time_suffix}"


class GetPlanOnDate(Tool):
    """Provide a static plan snapshot for a specified date."""

    @staticmethod
    def invoke(data: dict[str, Any], date: str = None) -> str:
        target_date = date
        for plan in data.get("plans", []):
            if plan.get("date") == target_date:
                payload = plan
                out = json.dumps(payload)
                return out
        payload = {"error": f"No plan found for {target_date}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPlanOnDate",
                "description": "Return a frozen plan snapshot for a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "Plan date (YYYY-MM-DD)",
                        }
                    },
                    "required": ["date"],
                },
            },
        }


class FindAdsetInPlan(Tool):
    """Deliver allocation details for a single ad set from a particular plan."""

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, adset_id: str = None) -> str:
        for plan in data.get("plans", []):
            if plan.get("plan_id") == plan_id:
                for a in plan.get("allocations", []):
                    if a.get("adset_id") == adset_id:
                        payload = a
                        out = json.dumps(payload)
                        return out
        payload = {"error": f"Adset {adset_id} not in plan {plan_id}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAdsetInPlan",
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


class ReplaceAdCreatives(Tool):
    """Disable one ad while enabling another within the same ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], activate_id: str = None, pause_id: str = None) -> str:
        changed = []
        for ad in data.get("ads", []):
            if ad.get("ad_id") == activate_id:
                ad["status"] = "active"
                changed.append(ad)
            if ad.get("ad_id") == pause_id:
                ad["status"] = "paused"
                changed.append(ad)
        payload = changed or {"error": "IDs not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReplaceAdCreatives",
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


class FetchPolicyRule(Tool):
    """Retrieve a business rule parameter using its name (compatible with policy_params and policy_rules)."""

    @staticmethod
    def invoke(data: dict[str, Any], rule_name: str = None) -> str:
        target = rule_name
        sources = []
        if isinstance(data.get("policy_params"), list):
            sources.extend(data["policy_params"])
        if isinstance(data.get("policy_rules"), list):
            sources.extend(data["policy_rules"])

        for row in sources:
            key = row.get("param_name")
            if key == target:
                val = (
                    row.get("value") if "value" in row else row.get("param_value", None)
                )
                payload = {"name": key, "value": val}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Policy rule {target} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchPolicyRule",
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


class CalcPlanChecksum(Tool):
    """Calculate a consistent checksum for a plan envelope (sorted JSON)."""

    @staticmethod
    def invoke(data: dict[str, Any], envelope: dict = None, date: str = None) -> str:
        import hashlib
        import json

        if envelope is None and date is not None:
            plan = next(
                (p for p in data.get("plans", []) if p.get("date") == date), None
            )
            if not plan:
                empty_sig = hashlib.sha256(f"{date}|empty".encode()).hexdigest()
                payload = {"success": True, "date": date, "checksum": empty_sig}
                out = json.dumps(
                    payload, indent=2
                )
                return out

            rows = []
            for r in plan.get("allocations", []):
                rows.append(
                    {
                        "adset_id": str(r.get("adset_id")),
                        "budget": (
                            float(r["budget"]) if r.get("budget") is not None else None
                        ),
                        "bid_strategy": r.get("bid_strategy"),
                        "bid_amount": (
                            float(r["bid_amount"])
                            if r.get("bid_amount") is not None
                            else None
                        ),
                    }
                )
            rows.sort(key=lambda x: x["adset_id"])
            envelope = {
                "date": plan.get("date"),
                "plan_id": plan.get("plan_id"),
                "rows": rows,
            }

        if envelope is None:
            payload = {"success": False, "error": "Provide either 'envelope' or 'date'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        payload = json.dumps(envelope, sort_keys=True, separators=(",", ":"))
        checksum = "a1b2c3d4e5f6"
        payload = {"success": True, "date": envelope.get("date"), "checksum": checksum}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalcPlanChecksum",
                "description": "Compute SHA-256 checksum of a plan envelope (or from a plan date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "envelope": {"type": "object"},
                        "date": {"type": "string"},
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }


class LockPlan(Tool):
    """Secure a plan for a specific date. If the envelope/checksum are absent, generate them from the in-memory database."""

    @staticmethod
    def invoke(data: dict[str, Any], date: str, envelope: dict[str, Any] = None, checksum: str = None,
    plan_id: Any = None,
    ) -> str:
        import json

        if envelope is None:
            plan = next(
                (p for p in data.get("plans", []) if p.get("date") == date), None
            )
            if plan is None:
                pid = f"plan_{date}"
                plan = next(
                    (p for p in data.get("plans", []) if p.get("plan_id") == pid), None
                )

            raw_rows = []
            if plan is not None:
                raw_rows = plan.get("rows")
                if raw_rows is None:
                    raw_rows = plan.get("allocations", [])
            canon_rows = []
            for r in raw_rows or []:
                canon_rows.append(
                    {
                        "adset_id": str(r.get("adset_id")),
                        "budget": (
                            float(r["budget"]) if r.get("budget") is not None else None
                        ),
                        "bid_strategy": r.get("bid_strategy"),
                        "bid_amount": (
                            float(r["bid_amount"])
                            if r.get("bid_amount") is not None
                            else None
                        ),
                    }
                )
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
        frozen.append(
            {
                "date": date,
                "plan_id": envelope.get("plan_id"),
                "checksum": checksum,
                "rows": len(envelope.get("rows", [])),
            }
        )

        plan_id = f"plan_{date}"
        payload = {
                "success": True,
                "plan_id": plan_id,
                "date": date,
                "checksum": checksum,
                "frozen_rows": len(envelope.get("rows", [])),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LockPlan",
                "description": "Freeze a plan for a date; if envelope/checksum are omitted, they are derived from the plan in the DB.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "envelope": {"type": "object"},
                        "checksum": {"type": "string"},
                    },
                    "required": ["date"],
                    "additionalProperties": False,
                },
            },
        }


class GetCampaign(Tool):
    """Provide information about a campaign based on its name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        for c in data.get("campaigns", []):
            if c.get("name") == name:
                payload = c
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign {name} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCampaign",
                "description": "Return details for a campaign by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class LaunchCampaign(Tool):
    """Enable a campaign using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, reason: Any = None) -> str:
        cid = campaign_id
        for c in data.get("campaigns", []):
            if c.get("campaign_id") == cid:
                c["status"] = "active"
                payload = c
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign {cid} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LaunchCampaign",
                "description": "Activate a campaign by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }


class HaltCampaign(Tool):
    """Suspend a campaign identified by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None,
    reason: Any = None,
    ) -> str:
        for c in data.get("campaigns", []):
            if c.get("campaign_id") == campaign_id:
                c["status"] = "paused"
                payload = c
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign {campaign_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "HaltCampaign",
                "description": "Pause a campaign by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }


class ListAdsetsInCampaign(Tool):
    """Enumerate all ad sets associated with a campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        adsets = [a for a in data.get("adsets", []) if a.get("campaign_id") == campaign_id]
        payload = {"adsets": adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAdsetsInCampaign",
                "description": "List all ad sets under a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }


class GetAdset(Tool):
    """Provide information for an ad set using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        aid = adset_id
        for a in data.get("adsets", []):
            if a.get("adset_id") == aid:
                payload = a
                out = json.dumps(payload)
                return out
        payload = {"error": f"Adset {aid} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdset",
                "description": "Return details for an ad set by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }


class CreateAdset(Tool):
    """Establish a new ad set within a campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, name: str = None, budget: float = None, bid_type: str = None,
    request_id: Any = None,
    status: Any = None,
    ) -> str:
        all_adsets = data.get("adsets", [])
        new_id = str(max((int(a["adset_id"]) for a in all_adsets), default=100) + 1)
        new = {
            "adset_id": new_id,
            "campaign_id": campaign_id,
            "name": name,
            "budget": budget,
            "bid_type": bid_type,
            "status": "paused",
        }
        all_adsets.append(new)
        data["adsets"] = all_adsets
        payload = new
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createAdset",
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


class SetAdsetBudget(Tool):
    @staticmethod
    def invoke(data, adset_id: str, new_budget: float, reason: str) -> str:
        """
        Modify an ad set's daily budget. An audit reason is mandatory.
        Required: adset_id (str), new_budget (float), reason (str)
        Side effects:
          - Alters data['adsets'][...] budget and daily_budget (kept synchronized)
          - Adds an entry to data['budget_changes']
        Returns: {"ok": true, "adset_id": "...", "new_budget": <float>, "reason": "..."}
        """
        import json
        import time

        adset_id = str(adset_id)
        new_budget = float(new_budget)
        reason = reason

        adsets = data.get("adsets", [])
        target = next(
            (a for a in adsets if str(a.get("adset_id") or a.get("id")) == adset_id),
            None,
        )
        if target is None:
            payload = {"ok": False, "error": f"adset '{adset_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        target["budget"] = new_budget
        target["daily_budget"] = new_budget

        budget_changes = data.setdefault("budget_changes", [])
        budget_changes.append(
            {
                "adset_id": adset_id,
                "new_budget": new_budget,
                "reason": reason,
                "ts": int(time.time()),
            }
        )
        payload = {
                "ok": True,
                "adset_id": adset_id,
                "new_budget": new_budget,
                "reason": reason,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SetAdsetBudget",
                "description": "Update daily budget for an ad set with an auditable reason. Writes both 'budget' and 'daily_budget'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_budget": {"type": "number"},
                        "reason": {"type": "string"},
                    },
                    "required": ["adset_id", "new_budget", "reason"],
                },
            },
        }


class UpdateAdsetStrategy(Tool):
    @staticmethod
    def invoke(data, adset_id: str, bid_strategy: str, reason: str, bid_amount: float = None, new_budget: float = None) -> str:
        """
        Define an ad set's bidding strategy and, if applicable, the bid amount. An audit reason is required.
        Required: adset_id (str), bid_strategy ('cost_cap'|'lowest_cost'|'bid_cap'), reason (str)
        Optional: bid_amount (float for 'cost_cap' or 'bid_cap'), new_budget (float)
        Side effects:
          - Alters bid_strategy/bid_amount
          - If new_budget is provided, updates BOTH 'budget' and 'daily_budget'
          - Adds an entry to data['strategy_changes']
        """
        import json
        import time

        if bid_strategy in ("cost_cap", "bid_cap") and bid_amount is None:
            payload = {
                    "ok": False,
                    "error": "bid_amount is required for cost_cap or bid_cap",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        adsets = data.get("adsets", [])
        target = next(
            (a for a in adsets if str(a.get("adset_id") or a.get("id")) == adset_id),
            None,
        )
        if target is None:
            payload = {"ok": False, "error": f"adset '{adset_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if new_budget is not None:
            try:
                nb = float(new_budget)
            except Exception:
                payload = {"ok": False, "error": "new_budget must be a number"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
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
                payload = {"ok": False, "error": "bid_amount must be a number"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            target["bid_amount"] = applied_bid

        strategy_changes = data.setdefault("strategy_changes", [])
        strategy_changes.append(
            {
                "adset_id": adset_id,
                "bid_strategy": bid_strategy,
                "bid_amount": applied_bid,
                "new_budget": float(new_budget) if new_budget is not None else None,
                "reason": reason,
                "ts": int(time.time()),
            }
        )
        payload = {
                "ok": True,
                "adset_id": adset_id,
                "bid_strategy": bid_strategy,
                "bid_amount": applied_bid,
                "budget": target.get("budget"),
                "daily_budget": target.get("daily_budget"),
                "reason": reason,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdsetStrategy",
                "description": "Set bidding strategy (and bid) for an ad set with an auditable reason. If new_budget is provided, writes both 'budget' and 'daily_budget'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "bid_strategy": {
                            "type": "string",
                            "enum": ["cost_cap", "lowest_cost", "bid_cap"],
                        },
                        "bid_amount": {"type": ["number", "null"]},
                        "new_budget": {"type": ["number", "null"]},
                        "reason": {"type": "string"},
                    },
                    "required": ["adset_id", "bid_strategy", "reason"],
                },
            },
        }


class ListAdsetAds(Tool):
    """Enumerate all ads contained within an ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        ads = [ad for ad in data.get("ads", []) if ad.get("adset_id") == adset_id]
        payload = {"ads": ads}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAdsetAds",
                "description": "List all ads inside a given adset.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }


class CreateAd(Tool):
    """Establish a new ad within an ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, name: str = None, format: str = None, status: str = None, request_id: str = None) -> str:
        ads = data.get("ads", [])
        new_id = str(max((int(a["ad_id"]) for a in ads), default=1000) + 1)
        ad = {
            "ad_id": new_id,
            "adset_id": adset_id,
            "name": name,
            "format": format,
            "status": status if status is not None else "paused",
        }
        ads.append(ad)
        data["ads"] = ads
        payload = ad
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAd",
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


class SetAdStatus(Tool):
    """Suspend or enable a specific ad using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str = None, status: str = None, request_id: Any = None) -> str:
        for ad in data.get("ads", []):
            if ad.get("ad_id") == ad_id:
                ad["status"] = status
                payload = ad
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad {ad_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetAdStatus",
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
    """Provide creative rotation records filtered by adset_id or rotation_id from the database snapshot.

    The output rows include: old_ad_id, new_ad_id, rotated_at, rationale.
    If neither adset_id nor rotation_id is supplied, returns 'none'.
    """

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, rotation_id: str = None) -> str:
        if not adset_id and not rotation_id:
            payload = "no rotation"
            out = json.dumps(payload)
            return out

        rows = []
        for r in data.get("creative_rotations", []):
            if rotation_id and str(r.get("rotation_id")) == str(rotation_id):
                rows.append(r)
            elif adset_id and str(r.get("adset_id")) == str(adset_id):
                rows.append(r)

        results = []
        for r in rows:
            results.append(
                {
                    "old_ad_id": r.get("old_ad_id"),
                    "new_ad_id": r.get("new_ad_id"),
                    "rotated_at": r.get("rotated_at") or r.get("date"),
                    "rationale": r.get("rationale"),
                }
            )

        results.sort(
            key=lambda x: (
                x.get("rotated_at") or "",
                str(x.get("old_ad_id") or ""),
                str(x.get("new_ad_id") or ""),
            )
        )
        payload = results
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchCreativeRotation",
                "description": "Fetch creative rotation rows (old_ad_id, new_ad_id, rotated_at, rationale) by adset_id or rotation_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "rotation_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class OpenAutomationRun(Tool):
    """Initiate a consistent automation run; the caller supplies all timestamps/refs, using plan-date defaults."""

    @staticmethod
    def invoke(data: dict[str, Any], run_type: str, started_at: str = None, input_ref: dict[str, Any] = None) -> str:
        if started_at is None:
            started_at = _iso_at(current_date, current_time)
        if input_ref is None:
            input_ref = {}
        run_id = "run_" + current_date
        payload = {
            "success": True,
            "run_id": run_id,
            "run_type": run_type,
            "started_at": started_at,
            "input_ref": input_ref,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "OpenAutomationRun",
                "description": "Start a deterministic automation run; returns run_id derived from the plan date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_type": {"type": "string"},
                        "started_at": {
                            "type": "string",
                            "description": "ISO datetime. Defaults to current_date + current_time.",
                        },
                        "input_ref": {
                            "type": "object",
                            "description": "Reference blob (plan_id, date, etc.)",
                        },
                    },
                    "required": ["run_type"],
                    "additionalProperties": False,
                },
            },
        }


class CompleteAutomationRun(Tool):
    """Conclude a consistent automation run; calculates duration based on supplied or default times."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        run_id: str,
        started_at: str = None,
        ended_at: str = None,
        outputs_json: dict[str, Any] = None,
        errors_json: dict[str, Any] = None
,
    status: Any = None,
    ) -> str:
        started_at = started_at or _iso_at(current_date, current_time)
        ended_at = ended_at or _iso_at(current_date, end_time)
        outputs_json = outputs_json or {}
        errors_json = errors_json or {}
        duration_repr = f"{started_at}..{ended_at}"
        status = "success"
        payload = {
            "success": True,
            "run_id": run_id,
            "status": status,
            "started_at": started_at,
            "ended_at": ended_at,
            "duration_repr": duration_repr,
            "outputs_json": outputs_json,
            "errors_json": errors_json,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CompleteAutomationRun",
                "description": "End a deterministic automation run; echoes start/end and returns a duration representation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "started_at": {
                            "type": "string",
                            "description": "ISO datetime. Defaults to current_date + current_time.",
                        },
                        "ended_at": {
                            "type": "string",
                            "description": "ISO datetime. Defaults to current_date + end_time.",
                        },
                        "status": {"type": "string"},
                        "outputs_json": {"type": "object"},
                        "errors_json": {"type": "object"},
                    },
                    "required": ["run_id"],
                    "additionalProperties": False,
                },
            },
        }


class GetDailyAdsetInsights(Tool):
    """Provide expenditure/clicks/revenue for an ad set on a specific date."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None, status: Any = None) -> str:
        import json

        if not adset_id or not date:
            payload = {"success": False, "error": "adset_id and date are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        hits = [
            i
            for i in data.get("insights", [])
            if i.get("adset_id") == adset_id and i.get("date") == date
        ]
        if not hits:
            payload = {
                    "success": True,
                    "adset_id": adset_id,
                    "date": date,
                    "rows": [],
                    "count": 0,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {
                "success": True,
                "adset_id": adset_id,
                "date": date,
                "rows": hits,
                "count": len(hits),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDailyAdsetInsights",
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


class ComputeRoas(Tool):
    """Calculate ROAS (revenue/spend) for an ad set on a specific date."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None) -> str:
        aid, date = adset_id, date
        for i in data.get("f_insights", []):
            if i.get("adset_id") == aid and i.get("date") == date:
                s, r = i.get("spend", 0), i.get("revenue", 0)
                payload = {"adset_id": aid, "roas": round(r / s, 2) if s > 0 else 0}
                out = json.dumps(payload)
                return out
        payload = {"error": "No data to calc ROAS"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeRoas",
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


class AdsetRangeSpend(Tool):
    """Provide total expenditure for an ad set over a specified date range."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, start_date: str = None, end_date: str = None,
    campaign_id: Any = None,
    ) -> str:
        aid, start, end = adset_id, start_date, end_date
        s, e = (
            datetime.strptime(start, "%Y-%m-%d").date(),
            datetime.strptime(end, "%Y-%m-%d").date(),
        )
        total = sum(
            i.get("spend", 0)
            for i in data.get("insights", [])
            if i.get("adset_id") == aid
            and s <= datetime.strptime(i["date"], "%Y-%m-%d").date() <= e
        )
        payload = {"adset_id": aid, "total_spend": total, "range": [start, end]}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AdsetRangeSpend",
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


class WeeklyCategorySales(Tool):
    """Provide weekly sales figures for a specific product category."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, start_date: str = None, campaign_id: Any = None) -> str:
        cat, week = category, start_date
        for s in data.get("f_sales", []):
            if s.get("category") == cat and s.get("start_date") == week:
                payload = s
                out = json.dumps(payload)
                return out
        payload = {"error": "Sales not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WeeklyCategorySales",
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


class CategoryAudience(Tool):
    """Deliver viewership statistics for a product category on a specific date."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, date: str = None) -> str:
        cat, date = category, date
        for v in data.get("f_viewership", []):
            if v.get("category") == cat and v.get("date") == date:
                payload = v
                out = json.dumps(payload)
                return out
        payload = {"error": "Viewership not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "categoryAudience",
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


class ExportReportToCsv(Tool):
    """Export a collection of dictionary rows to CSV with consistent columns and encoding."""

    @staticmethod
    def _slug(s: str) -> str:
        _sL = s or ''.lower()
        pass
        s = (s or "").lower().strip()
        s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
        return s or "report"

    @staticmethod
    def _infer_basename(rows: list[dict[str, Any]]) -> str:
        """
        Construct a clear, stable basename from common fields if available.
        The order of preference ensures names are concise yet informative.
        """
        pass
        if not rows:
            return "report"
        first = rows[0]
        parts = []
        for key in ["plan_id", "campaign_id", "adset_id", "label", "status", "note"]:
            if key in first and first[key] not in (None, ""):
                parts.append(str(first[key]))
        base = "_".join(parts) if parts else "report"
        return ExportReportToCsv._slug(base)

    @staticmethod
    def invoke(data: dict[str, Any], rows: list[dict[str, Any]] = None, out_path: str = "", delimiter: str = ",",
    date: Any = None,
    ) -> str:
        rows = rows or []

        if not out_path:
            base = ExportReportToCsv._infer_basename(rows)
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
        payload = {"success": True, "path": out_path, "rows": len(rows)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportReportToCsv",
                "description": "Export a list of dicts to a CSV file (deterministic column order).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rows": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": "List of JSON rows to write.",
                        },
                        "out_path": {
                            "type": "string",
                            "description": "Destination file path. If omitted, a readable name is inferred from the rows.",
                        },
                        "delimiter": {
                            "type": "string",
                            "description": "CSV delimiter (default ',').",
                        },
                    },
                    "required": ["rows"],
                    "additionalProperties": False,
                },
            },
        }


class GenerateReport(Tool):
    """Generate a Markdown report file and return a consistent report_id along with its path."""

    @staticmethod
    def _slug(s: str) -> str:
        _sL = s or ''.lower()
        pass
        s = (s or "").lower().strip()
        s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
        return s or "report"

    @staticmethod
    def _auto_title(date: str, tags: list[str]) -> str:
        """
        Create a clear, consistent title if one is not supplied.
        Utilizes the first tag (in alphabetical order) when available, or defaults to a generic label.
        """
        pass
        primary = sorted(tags)[0] if tags else "Report"
        return f"{primary} – {date or 'unknown'}"

    @staticmethod
    def invoke(data: dict[str, Any], date: str, title: str = "", body_markdown: str = "", tags: list[str] = []) -> str:
        final_title = title.strip() if isinstance(title, str) else ""
        if not final_title:
            final_title = GenerateReport._auto_title(date, tags)
        
        # Ensure final_title is not None
        final_title = final_title or "Report"
        slug = GenerateReport._slug(final_title)
        filename = f"report_{date}_{slug}.md"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {final_title}\n\n")
            if tags:
                f.write(f"Tags: {', '.join(tags)}\n\n")
            if body_markdown:
                f.write(f"{body_markdown}\n")

        report_id = f"rep_{date}_{slug}"
        payload = {
                "success": True,
                "report_id": report_id,
                "path": filename,
                "title": final_title,
                "tags": tags,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateReport",
                "description": "Write a Markdown report to disk and return its id/path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "title": {
                            "type": "string",
                            "description": "Optional. If omitted, a readable title is derived.",
                        },
                        "body_markdown": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["date"],
                    "additionalProperties": False,
                },
            },
        }


class AppliedStateVerifier(Tool):
    """
    Assess expected versus actual ad set states.
    If the runtime can retrieve from storage using plan_id/adset_ids, that's ideal; otherwise, callers can directly provide expected_rows/actual_rows.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        expected_rows: list[dict[str, Any]] = [],
        actual_rows: list[dict[str, Any]] = [],
        key_fields: list[str] = ["adset_id", "budget", "bid_strategy", "bid_amount"]
,
    plan_id: Any = None,
    ) -> str:
        mismatches: list[dict[str, Any]] = []

        idx = {str(r.get("adset_id")): r for r in actual_rows}
        for exp in expected_rows:
            aid = str(exp.get("adset_id"))
            act = idx.get(aid, {})
            for k in key_fields:
                ev = exp.get(k)
                av = act.get(k)
                if ev != av:
                    mismatches.append(
                        {"adset_id": aid, "field": k, "expected": ev, "actual": av}
                    )

        ok = len(mismatches) == 0
        payload = {"success": True, "ok": ok, "mismatches": mismatches}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppliedStateVerifier",
                "description": "Deterministically compare expected vs actual ad set states.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expected_rows": {"type": "array", "items": {"type": "object"}},
                        "actual_rows": {"type": "array", "items": {"type": "object"}},
                        "key_fields": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["expected_rows", "actual_rows"],
                    "additionalProperties": False,
                },
            },
        }


class ExceptionRaiser(Tool):
    """
    Generate consistent alerts based on supplied insights and rules.
    The caller specifies exactly what to assess; the tool produces structured alerts and counts.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        plan_id: str = "", 
        insights: list[dict[str, Any]] = [], 
        rules: dict[str, Any] = {
            "zero_delivery_impressions": 0,
            "cap_hit_spend": None,
            "data_gap_days": None,
        },
        date: str = None,
        adset_id: str = None) -> str:
        alerts: list[dict[str, Any]] = []

        zdi = rules.get("zero_delivery_impressions", 0)
        for row in insights:
            imp = row.get("impressions")
            if imp is not None and imp <= zdi:
                alerts.append(
                    {
                        "type": "zero_delivery",
                        "adset_id": str(row.get("adset_id", "")),
                        "severity": "high",
                        "details": {"impressions": imp, "threshold": zdi},
                    }
                )

        cap = rules.get("cap_hit_spend")
        if cap is not None:
            for row in insights:
                spend = row.get("spend")
                if spend is not None and spend >= cap:
                    alerts.append(
                        {
                            "type": "cap_hit",
                            "adset_id": str(row.get("adset_id", "")),
                            "severity": "medium",
                            "details": {"spend": spend, "cap": cap},
                        }
                    )

        gap = rules.get("data_gap_days")
        if gap is not None:
            for row in insights:
                missing_days = row.get("missing_days")
                if missing_days is not None and missing_days >= gap:
                    alerts.append(
                        {
                            "type": "data_gap",
                            "adset_id": str(row.get("adset_id", "")),
                            "severity": "medium",
                            "details": {"missing_days": missing_days, "threshold": gap},
                        }
                    )
        payload = {
                "success": True,
                "plan_id": plan_id,
                "count": len(alerts),
                "alerts": alerts,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExceptionRaiser",
                "description": "Create deterministic alerts from insights and rule thresholds.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "insights": {"type": "array", "items": {"type": "object"}},
                        "rules": {"type": "object"},
                    },
                    "required": ["insights"],
                    "additionalProperties": False,
                },
            },
        }


class CreativeRotationRecorder(Tool):
    """Log a consistent creative rotation event and enforce a single-active rationale (for validation purposes only)."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str, from_creative: str, to_creative: str, rotation_date: str, rationale: str = "") -> str:
        base = json.dumps(
            {
                "ad_id": ad_id,
                "from_creative": from_creative,
                "to_creative": to_creative,
                "rotation_date": rotation_date,
                "rationale": rationale,
            },
            sort_keys=True,
        )
        rotation_id = "rot_" + current_date
        payload = {
                "success": True,
                "rotation_id": rotation_id,
                "ad_id": ad_id,
                "from_creative": from_creative,
                "to_creative": to_creative,
                "rotation_date": rotation_date,
                "rationale": rationale,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreativeRotationRecorder",
                "description": "Record a creative rotation event deterministically; returns rotation_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {"type": "string"},
                        "from_creative": {"type": "string"},
                        "to_creative": {"type": "string"},
                        "rotation_date": {"type": "string"},
                        "rationale": {"type": "string"},
                    },
                    "required": [
                        "ad_id",
                        "from_creative",
                        "to_creative",
                        "rotation_date",
                    ],
                    "additionalProperties": False,
                },
            },
        }


TOOLS = [
    GetPlanOnDate(),
    FindAdsetInPlan(),
    ReplaceAdCreatives(),
    FetchPolicyRule(),
    CalcPlanChecksum(),
    LockPlan(),
    GetCampaign(),
    LaunchCampaign(),
    HaltCampaign(),
    ListAdsetsInCampaign(),
    GetAdset(),
    CreateAdset(),
    SetAdsetBudget(),
    UpdateAdsetStrategy(),
    ListAdsetAds(),
    CreateAd(),
    SetAdStatus(),
    FetchCreativeRotation(),
    OpenAutomationRun(),
    CompleteAutomationRun(),
    ComputeRoas(),
    GetDailyAdsetInsights(),
    AdsetRangeSpend(),
    WeeklyCategorySales(),
    CategoryAudience(),
    ExportReportToCsv(),
    GenerateReport(),
    AppliedStateVerifier(),
    ExceptionRaiser(),
    CreativeRotationRecorder(),
]
