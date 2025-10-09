import ast
import json
from datetime import datetime
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


def _as_list_literal(v: str) -> list[str]:
    pass
    try:
        x = ast.literal_eval(v)
        return list(x) if isinstance(x, (list, tuple)) else []
    except Exception:
        return []


class GetPlanForDate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], date: str = None) -> str:
        d = date
        for p in data.get("plans", {}).values():
            if p.get("date") == d:
                payload = p
                out = json.dumps(payload)
                return out
        payload = {"error": f"plan for {d} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPlanForDate",
                "description": "Retrieves a frozen plan by date.",
                "parameters": {
                    "type": "object",
                    "properties": {"date": {"type": "string"}},
                    "required": ["date"],
                },
            },
        }


class GetAdsetAllocationFromPlan(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, adset_id: str = None) -> str:
        for p in data.get("plans", {}).values():
            if p.get("plan_id") == plan_id:
                for a in p.get("allocations", []):
                    if a.get("adset_id") == adset_id:
                        payload = a
                        out = json.dumps(payload)
                        return out
        payload = {"error": f"allocation for {adset_id} not in {plan_id}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetAllocationFromPlan",
                "description": "Gets one ad set allocation from a plan.",
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


class GetPolicyParameter(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], param_name: str = None) -> str:
        n = param_name
        for r in data.get("policy_params", {}).values():
            if r.get("param_name") == n:
                payload = r
                out = json.dumps(payload)
                return out
        payload = {"error": f"policy {n} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyParameter",
                "description": "Gets a single policy parameter.",
                "parameters": {
                    "type": "object",
                    "properties": {"param_name": {"type": "string"}},
                    "required": ["param_name"],
                },
            },
        }


class ListCanonicalBidStrategies(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        for r in data.get("policy_params", {}).values():
            if r.get("param_name") == "canonical_bid_strategies":
                payload = _as_list_literal(r.get("param_value", "[]"))
                out = json.dumps(payload)
                return out
        payload = []
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListCanonicalBidStrategies",
                "description": "Lists allowed bid strategies from policy.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class ListCanonicalCreativeTypes(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        for r in data.get("policy_params", {}).values():
            if r.get("param_name") == "canonical_creative_types":
                payload = _as_list_literal(r.get("param_value", "[]"))
                out = json.dumps(payload)
                return out
        payload = []
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListCanonicalCreativeTypes",
                "description": "Lists allowed creative types from policy.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class ValidateAllocationsAgainstPolicy(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], total_budget: float, allocations: list = None) -> str:
        if allocations is None:
            allocations = []
        params = {
            p["param_name"]: p["param_value"] for p in data.get("policy_params", {}).values()
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
                        "allocations": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["total_budget", "allocations"],
                },
            },
        }


class GetCampaignByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        for c in data.get("campaigns", {}).values():
            if c.get("name") == name:
                payload = c
                out = json.dumps(payload)
                return out
        payload = {"error": f"campaign {name} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCampaignByName",
                "description": "Retrieves a campaign by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class CreateCampaign(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, objective: str = None, created_date: str = None) -> str:
        campaigns = data.get("campaigns", {}).values()
        nid = max((int(c["campaign_id"]) for c in campaigns.values()), default=0) + 1
        rec = {
            "campaign_id": str(nid),
            "name": name,
            "objective": objective,
            "created_date": created_date,
            "status": "paused",
        }
        data["campaigns"][campaign_id] = rec
        data["campaigns"] = campaigns
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createCampaign",
                "description": "Creates a paused campaign with a provided created_date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "objective": {"type": "string"},
                        "created_date": {"type": "string"},
                    },
                    "required": ["name", "objective", "created_date"],
                },
            },
        }


class UpdateCampaignStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, status: str = None) -> str:
        cid = campaign_id
        st = status
        for c in data.get("campaigns", {}).values():
            if c.get("campaign_id") == cid:
                c["status"] = st
                payload = c
                out = json.dumps(payload)
                return out
        payload = {"error": f"campaign {cid} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCampaignStatus",
                "description": "Updates campaign status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["campaign_id", "status"],
                },
            },
        }


class GetAdsetsByCampaignID(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        rows = [r for r in data.get("adsets", {}).values() if r.get("campaign_id") == campaign_id]
        payload = {"adsets": rows}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetsByCampaignId",
                "description": "Lists ad sets for a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }


class GetAdsetDetailsByID(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        aid = adset_id
        for a in data.get("adsets", {}).values():
            if a.get("adset_id") == aid:
                payload = a
                out = json.dumps(payload)
                return out
        payload = {"error": f"adset {aid} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetDetailsById",
                "description": "Gets one ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }


class CreateAdset(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        campaign_id: str = None,
        name: str = None,
        category: str = None,
        daily_budget: float = None,
        bid_strategy: str = None,
        bid_amount: float = None,
        updated_at: str = None
,
    request_id: Any = None,
    status: Any = None,
    ) -> str:
        adsets = data.get("adsets", {}).values()
        nid = max((int(a["adset_id"]) for a in adsets.values()), default=100) + 1
        rec = {
            "adset_id": str(nid),
            "campaign_id": campaign_id,
            "name": name,
            "category": category,
            "daily_budget": daily_budget,
            "bid_strategy": bid_strategy,
            "bid_amount": bid_amount,
            "status": "paused",
            "updated_at": updated_at,
        }
        data["adsets"][adset_id] = rec
        data["adsets"] = adsets
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createAdset",
                "description": "Creates a paused ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "name": {"type": "string"},
                        "category": {"type": "string"},
                        "daily_budget": {"type": "number"},
                        "bid_strategy": {"type": "string"},
                        "bid_amount": {"type": "number"},
                        "updated_at": {"type": "string"},
                    },
                    "required": [
                        "campaign_id",
                        "name",
                        "category",
                        "daily_budget",
                        "bid_strategy",
                        "updated_at",
                    ],
                },
            },
        }


class UpdateAdsetBudget(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str, new_budget: float, updated_at: str) -> str:
        aid = adset_id
        nb = float(new_budget)
        for a in data.get("adsets", {}).values():
            if a.get("adset_id") == aid:
                a["daily_budget"] = nb
                a["updated_at"] = updated_at
                payload = a
                out = json.dumps(payload)
                return out
        payload = {"error": f"adset {aid} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdsetBudget",
                "description": "Updates an ad set budget.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_budget": {"type": "number"},
                        "updated_at": {"type": "string"},
                    },
                    "required": ["adset_id", "new_budget", "updated_at"],
                },
            },
        }


class UpdateAdsetBidStrategy(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, bid_strategy: str = None, bid_amount: float = None, updated_at: str = None) -> str:
        aid = adset_id
        bs = bid_strategy
        ba = bid_amount
        for a in data.get("adsets", {}).values():
            if a.get("adset_id") == aid:
                a["bid_strategy"] = bs
                a["bid_amount"] = ba
                a["updated_at"] = updated_at
                payload = a
                out = json.dumps(payload)
                return out
        payload = {"error": f"adset {aid} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdsetBidStrategy",
                "description": "Updates bid strategy and bid amount.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "bid_strategy": {"type": "string"},
                        "bid_amount": {"type": ["number", "null"]},
                        "updated_at": {"type": "string"},
                    },
                    "required": ["adset_id", "bid_strategy", "updated_at"],
                },
            },
        }


class GetAdsByAdsetID(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        rows = [r for r in data.get("ads", {}).values() if r.get("adset_id") == adset_id]
        payload = {"ads": rows}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsByAdsetId",
                "description": "Lists ads by ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }


class CreateAd(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, name: str = None, creative_type: str = None, start_date: str = None) -> str:
        ads = data.get("ads", {}).values()
        nid = max((int(a["ad_id"]) for a in ads.values()), default=1100) + 1
        rec = {
            "ad_id": str(nid),
            "adset_id": adset_id,
            "name": name,
            "creative_type": creative_type,
            "status": "paused",
            "start_date": start_date,
            "end_date": None,
        }
        data["ads"][ad_id] = rec
        data["ads"] = ads
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAd",
                "description": "Creates a paused ad in an ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "name": {"type": "string"},
                        "creative_type": {"type": "string"},
                        "start_date": {"type": "string"},
                    },
                    "required": ["adset_id", "name", "creative_type", "start_date"],
                },
            },
        }


class UpdateAdStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str = None, status: str = None, request_id: Any = None,
    timestamp: Any = None,
    ) -> str:
        for ad in data.get("ads", {}).values():
            if ad.get("ad_id") == ad_id:
                ad["status"] = status
                payload = ad
                out = json.dumps(payload)
                return out
        payload = {"error": f"ad {ad_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateAdStatus",
                "description": "Updates ad status.",
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


class RotateAdCreative(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ad_id_to_activate: str = None, ad_id_to_pause: str = None, timestamp: Any = None) -> str:
        to_act = ad_id_to_activate
        to_pause = ad_id_to_pause
        ok_a = False
        ok_p = False
        for ad in data.get("ads", {}).values():
            if ad.get("ad_id") == to_act:
                ad["status"] = "active"
                ok_a = True
            if ad.get("ad_id") == to_pause:
                ad["status"] = "paused"
                ok_p = True
        if ok_a and ok_p:
            payload = {"status": "success"}
            out = json.dumps(payload)
            return out
        payload = {"error": "ids_not_found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RotateAdCreative",
                "description": "Activates one ad and pauses another.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id_to_activate": {"type": "string"},
                        "ad_id_to_pause": {"type": "string"},
                    },
                    "required": ["ad_id_to_activate", "ad_id_to_pause"],
                },
            },
        }


class GetDailyInsightsForAdset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None) -> str:
        for i in data.get("f_insights", {}).values():
            if i.get("adset_id") == adset_id and i.get("date") == date:
                payload = i
                out = json.dumps(payload)
                return out
        payload = {"error": "insights_not_found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDailyInsightsForAdset",
                "description": "Gets insights for one ad set on a date.",
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


class CalculateAdsetRoasForDay(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None) -> str:
        aid = adset_id
        d = date
        for i in data.get("f_insights", {}).values():
            if i.get("adset_id") == aid and i.get("date") == d:
                spend = i.get("spend", 0)
                revenue = i.get("revenue", 0)
                roas = round(revenue / spend, 2) if spend > 0 else 0
                payload = {"adset_id": aid, "date": d, "roas": roas}
                out = json.dumps(payload)
                return out
        payload = {"error": "roas_not_available"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateAdsetRoasForDay",
                "description": "Computes ROAS for one day.",
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


class ComputeCtrForAdsetDay(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None) -> str:
        for i in data.get("f_insights", {}).values():
            if i.get("adset_id") == adset_id and i.get("date") == date:
                imp = i.get("impressions", 0)
                clk = i.get("clicks", 0)
                ctr = round(clk / imp, 4) if imp > 0 else 0
                payload = {"adset_id": adset_id, "date": date, "ctr": ctr}
                out = json.dumps(payload)
                return out
        payload = {"error": "ctr_not_available"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeCtrForAdsetDay",
                "description": "Computes CTR for one day.",
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


class GetAdsetSpendForDateRange(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, start_date: str = None, end_date: str = None) -> str:
        aid = adset_id
        s = start_date
        e = end_date
        sd = datetime.strptime(s, "%Y-%m-%d").date()
        ed = datetime.strptime(e, "%Y-%m-%d").date()
        tot = 0.0
        for i in data.get("f_insights", {}).values():
            if i.get("adset_id") == aid:
                idate = datetime.strptime(i.get("date"), "%Y-%m-%d").date()
                if sd <= idate <= ed:
                    tot += float(i.get("spend", 0))
        payload = {
                "adset_id": aid,
                "start_date": s,
                "end_date": e,
                "total_spend": round(tot, 2),
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetSpendForDateRange",
                "description": "Sums spend for a date range.",
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


class GetWeeklySalesByCategory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, start_date: str = None) -> str:
        cat = category
        start = start_date
        for r in data.get("f_sales", {}).values():
            if r.get("category") == cat and r.get("start_date") == start:
                payload = r
                out = json.dumps(payload)
                return out
        payload = {"error": "sales_not_found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWeeklySalesByCategory",
                "description": "Gets weekly sales for a category.",
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


class GetViewershipForCategory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, date: str = None) -> str:
        cat = category
        d = date
        for r in data.get("f_viewership", {}).values():
            if r.get("category") == cat and r.get("date") == d:
                payload = r
                out = json.dumps(payload)
                return out
        payload = {"error": "viewership_not_found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetViewershipForCategory",
                "description": "Gets viewership for a category on a date.",
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


class GetProductPriceOnDate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None, date: str = None) -> str:
        pid = product_id
        d = date
        for r in data.get("f_price", {}).values():
            if r.get("product_id") == pid and r.get("date") == d:
                payload = r
                out = json.dumps(payload)
                return out
        payload = {"error": "price_not_found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductPriceOnDate",
                "description": "Gets product price on a date.",
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
    @staticmethod
    def invoke(data: dict[str, Any], roas_threshold: float, date: str) -> str:
        out = []
        for i in data.get("f_insights", {}).values():
            if i.get("date") == date:
                spend = i.get("spend", 0)
                revenue = i.get("revenue", 0)
                roas = (revenue / spend) if spend > 0 else 0
                if spend > 0 and roas < roas_threshold:
                    out.append({"adset_id": i.get("adset_id"), "roas": round(roas, 2)})
        payload = {"underperforming_adsets": out}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindUnderperformingAdsets",
                "description": "Finds ad sets below a ROAS threshold for a day.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "roas_threshold": {"type": "number"},
                        "date": {"type": "string"},
                    },
                    "required": ["roas_threshold", "date"],
                },
            },
        }


class CreateAutomationRun(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        run_id: str = None,
        run_type: str = None,
        started_at: str = None,
        ended_at: str = None,
        status: str = None,
        input_ref: str = None,
        errors_json: str = None
    ) -> str:
        rec = {
            "run_id": run_id,
            "run_type": run_type,
            "started_at": started_at,
            "ended_at": ended_at,
            "status": status,
            "input_ref": input_ref,
            "errors_json": errors_json,
        }
        table = data.setdefault("automation_runs", {})
        key = f"{len(table)}"
        table[key] = rec
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAutomationRun",
                "description": "Creates an automation run record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "run_type": {"type": "string"},
                        "started_at": {"type": "string"},
                        "ended_at": {"type": "string"},
                        "status": {"type": "string"},
                        "input_ref": {"type": "string"},
                        "errors_json": {"type": "string"},
                    },
                    "required": [
                        "run_id",
                        "run_type",
                        "started_at",
                        "ended_at",
                        "status",
                        "input_ref",
                        "errors_json",
                    ],
                },
            },
        }


class GetAutomationRunHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_type: str = None, status: str = None, limit: int = 10) -> str:
        runs = data.get("automation_runs", {}).values()
        if run_type:
            runs = [r for r in runs.values() if r.get("run_type") == run_type]
        if status:
            runs = [r for r in runs.values() if r.get("status") == status]
        runs.sort(key=lambda x: x.get("started_at", ""), reverse=True)
        runs = runs[:limit]
        total = len(runs)
        succ = len([r for r in runs.values() if r.get("status") == "completed"])
        fail = len([r for r in runs.values() if r.get("status") == "failed"])
        rate = round((succ / total * 100), 2) if total > 0 else 0
        payload = {
                "summary": {
                    "total_runs": total,
                    "success_count": succ,
                    "failure_count": fail,
                    "success_rate_percent": rate,
                },
                "runs": runs,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAutomationRunHistory",
                "description": "Gets automation runs with summary.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_type": {"type": "string"},
                        "status": {"type": "string"},
                        "limit": {"type": "number"},
                    },
                    "required": [],
                },
            },
        }


class UpdateAutomationRunEnd(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None, status: str = None, ended_at: str = None) -> str:
        for r in data.get("automation_runs", {}).values():
            if r.get("run_id") == run_id:
                r["status"] = status
                r["ended_at"] = ended_at
                payload = r
                out = json.dumps(payload)
                return out
        payload = {"error": f"run {run_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAutomationRunEnd",
                "description": "Sets final status and end time for a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "status": {"type": "string"},
                        "ended_at": {"type": "string"},
                    },
                    "required": ["run_id", "status", "ended_at"],
                },
            },
        }


class GetLastSuccessfulRun(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_type: str = None) -> str:
        runs = [
            r
            for r in data.get("automation_runs", {}).values()
            if r.get("run_type") == run_type and r.get("status") == "completed"
        ]
        if not runs:
            payload = {"error": f"no successful run for {run_type}"}
            out = json.dumps(payload)
            return out
        last = max(runs, key=lambda x: x.get("ended_at", ""))
        payload = last
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLastSuccessfulRun",
                "description": "Gets most recent successful run of a type.",
                "parameters": {
                    "type": "object",
                    "properties": {"run_type": {"type": "string"}},
                    "required": ["run_type"],
                },
            },
        }


class LogBudgetChange(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        adset_id: str = None, 
        old_budget: float = None, 
        new_budget: float = None, 
        changed_at: str = None, 
        reason: str = None
    ) -> str:
        rows = data.get("budget_changes", {}).values()
        nid = f"BC-{max((int(r['change_id'][3:]) for r in rows.values()), default=0) + 1}"
        rec = {
            "change_id": nid,
            "adset_id": adset_id,
            "old_budget": old_budget,
            "new_budget": new_budget,
            "changed_at": changed_at,
            "reason": reason,
        }
        data["creative_rotations"][rec["creative_rotation_id"]] = rec
        data["budget_changes"] = rows
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogBudgetChange",
                "description": "Appends a budget change log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "old_budget": {"type": "number"},
                        "new_budget": {"type": "number"},
                        "changed_at": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": [
                        "adset_id",
                        "old_budget",
                        "new_budget",
                        "changed_at",
                        "reason",
                    ],
                },
            },
        }


class LogStrategyChange(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str = None,
        old_strategy: str = None,
        new_strategy: str = None,
        old_bid: float = None,
        new_bid: float = None,
        changed_at: str = None,
        reason: str = None
,
    change_id: Any = None,
    ) -> str:
        rows = data.get("strategy_changes", {}).values()
        nid = f"SC-{max((int(r['change_id'][3:]) for r in rows.values()), default=0) + 1}"
        rec = {
            "change_id": nid,
            "adset_id": adset_id,
            "old_strategy": old_strategy,
            "new_strategy": new_strategy,
            "old_bid": old_bid,
            "new_bid": new_bid,
            "changed_at": changed_at,
            "reason": reason,
        }
        data["creative_rotations"][rec["creative_rotation_id"]] = rec
        data["strategy_changes"] = rows
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogStrategyChange",
                "description": "Appends a strategy change log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "old_strategy": {"type": "string"},
                        "new_strategy": {"type": "string"},
                        "old_bid": {"type": ["number", "null"]},
                        "new_bid": {"type": ["number", "null"]},
                        "changed_at": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": [
                        "adset_id",
                        "old_strategy",
                        "new_strategy",
                        "old_bid",
                        "new_bid",
                        "changed_at",
                        "reason",
                    ],
                },
            },
        }


class LogCreativeRotation(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str = None,
        old_ad_id: str = None,
        new_ad_id: str = None,
        rotated_at: str = None,
        rationale: str = None, change_id: Any = None) -> str:
        rows = data.get("creative_rotations", {}).values()
        nid = f"CR-{max((int(r['rotation_id'][3:]) for r in rows.values()), default=0) + 1}"
        rec = {
            "rotation_id": nid,
            "adset_id": adset_id,
            "old_ad_id": old_ad_id,
            "new_ad_id": new_ad_id,
            "rotated_at": rotated_at,
            "rationale": rationale,
        }
        data["creative_rotations"][rec["creative_rotation_id"]] = rec
        data["creative_rotations"] = rows
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogCreativeRotation",
                "description": "Appends a creative rotation log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "old_ad_id": {"type": "string"},
                        "new_ad_id": {"type": "string"},
                        "rotated_at": {"type": "string"},
                        "rationale": {"type": "string"},
                    },
                    "required": [
                        "adset_id",
                        "old_ad_id",
                        "new_ad_id",
                        "rotated_at",
                        "rationale",
                    ],
                },
            },
        }


class GetProductByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_name: str = None) -> str:
        n = product_name
        for p in data.get("dim_product", {}).values():
            if p.get("name") == n:
                payload = p
                out = json.dumps(payload)
                return out
        payload = {"error": f"product {n} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getProductByName",
                "description": "Looks up a product by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"product_name": {"type": "string"}},
                    "required": ["product_name"],
                },
            },
        }


class GetAdsetsByCategory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], category: str = None) -> str:
        rows = [r for r in data.get("adsets", {}).values() if r.get("category") == category]
        payload = {"adsets": rows}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAdsetsByCategory",
                "description": "Lists ad sets by category.",
                "parameters": {
                    "type": "object",
                    "properties": {"category": {"type": "string"}},
                    "required": ["category"],
                },
            },
        }


class CreatePlan(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        plan_id: str = None,
        date: str = None,
        total_budget: float = None,
        author: str = None,
        created_at: str = None,
        checksum: str = None,
        allocations: list = None
    ) -> str:
        if allocations is None:
            allocations = []
        rec = {
            "plan_id": plan_id,
            "date": date,
            "total_budget": total_budget,
            "author": author,
            "created_at": created_at,
            "checksum": checksum,
            "allocations": allocations,
        }
        table = data.setdefault("plans", {})
        key = f"{len(table)}"
        table[key] = rec
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePlan",
                "description": "Creates a plan with allocations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "date": {"type": "string"},
                        "total_budget": {"type": "number"},
                        "author": {"type": "string"},
                        "created_at": {"type": "string"},
                        "checksum": {"type": "string"},
                        "allocations": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": [
                        "plan_id",
                        "date",
                        "total_budget",
                        "author",
                        "created_at",
                        "checksum",
                        "allocations",
                    ],
                },
            },
        }


TOOLS = [
    GetPlanForDate(),
    GetAdsetAllocationFromPlan(),
    GetPolicyParameter(),
    ListCanonicalBidStrategies(),
    ListCanonicalCreativeTypes(),
    ValidateAllocationsAgainstPolicy(),
    GetCampaignByName(),
    CreateCampaign(),
    UpdateCampaignStatus(),
    GetAdsetsByCampaignID(),
    GetAdsetDetailsByID(),
    CreateAdset(),
    UpdateAdsetBudget(),
    UpdateAdsetBidStrategy(),
    GetAdsByAdsetID(),
    CreateAd(),
    UpdateAdStatus(),
    RotateAdCreative(),
    GetDailyInsightsForAdset(),
    CalculateAdsetRoasForDay(),
    ComputeCtrForAdsetDay(),
    GetAdsetSpendForDateRange(),
    GetWeeklySalesByCategory(),
    GetViewershipForCategory(),
    GetProductPriceOnDate(),
    FindUnderperformingAdsets(),
    CreateAutomationRun(),
    GetAutomationRunHistory(),
    UpdateAutomationRunEnd(),
    GetLastSuccessfulRun(),
    LogBudgetChange(),
    LogStrategyChange(),
    LogCreativeRotation(),
    GetProductByName(),
    GetAdsetsByCategory(),
    CreatePlan(),
]
