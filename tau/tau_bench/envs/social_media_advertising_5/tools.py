import json
import ast
from datetime import datetime
from typing import Any, Dict, List
from domains.dto import Tool


def _as_list_literal(v: str) -> List[str]:
    try:
        x = ast.literal_eval(v)
        return list(x) if isinstance(x, (list, tuple)) else []
    except Exception:
        return []


class GetPlanForDate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        d = kwargs.get("date")
        for p in data.get("plans", []):
            if p.get("date") == d:
                return json.dumps(p)
        return json.dumps({"error": f"plan for {d} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_plan_for_date", "description": "Retrieves a frozen plan by date.",
                             "parameters": {"type": "object", "properties": {"date": {"type": "string"}},
                                            "required": ["date"]}}}


class GetAdsetAllocationFromPlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        plan_id = kwargs.get("plan_id")
        adset_id = kwargs.get("adset_id")
        for p in data.get("plans", []):
            if p.get("plan_id") == plan_id:
                for a in p.get("allocations", []):
                    if a.get("adset_id") == adset_id:
                        return json.dumps(a)
        return json.dumps({"error": f"allocation for {adset_id} not in {plan_id}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adset_allocation_from_plan",
                                                 "description": "Gets one ad set allocation from a plan.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"plan_id": {"type": "string"},
                                                                               "adset_id": {"type": "string"}},
                                                                "required": ["plan_id", "adset_id"]}}}


class GetPolicyParameter(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        n = kwargs.get("param_name")
        for r in data.get("policy_params", []):
            if r.get("param_name") == n:
                return json.dumps(r)
        return json.dumps({"error": f"policy {n} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_policy_parameter", "description": "Gets a single policy parameter.",
                             "parameters": {"type": "object", "properties": {"param_name": {"type": "string"}},
                                            "required": ["param_name"]}}}


class ListCanonicalBidStrategies(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        for r in data.get("policy_params", []):
            if r.get("param_name") == "canonical_bid_strategies":
                return json.dumps(_as_list_literal(r.get("param_value", "[]")))
        return json.dumps([])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_canonical_bid_strategies",
                                                 "description": "Lists allowed bid strategies from policy.",
                                                 "parameters": {"type": "object", "properties": {}, "required": []}}}


class ListCanonicalCreativeTypes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        for r in data.get("policy_params", []):
            if r.get("param_name") == "canonical_creative_types":
                return json.dumps(_as_list_literal(r.get("param_value", "[]")))
        return json.dumps([])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_canonical_creative_types",
                                                 "description": "Lists allowed creative types from policy.",
                                                 "parameters": {"type": "object", "properties": {}, "required": []}}}


class ValidateAllocationsAgainstPolicy(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        total_budget = float(kwargs.get("total_budget"))
        allocations = kwargs.get("allocations", [])
        params = {p["param_name"]: p["param_value"] for p in data.get("policy_params", [])}
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
                issues.append({"adset_id": a.get("adset_id"), "issue": "budget_below_min"})
            if bs not in strategies:
                issues.append({"adset_id": a.get("adset_id"), "issue": "invalid_strategy"})
            if ct not in creatives:
                issues.append({"adset_id": a.get("adset_id"), "issue": "invalid_creative"})
            if bs == "lowest_cost" and a.get("bid_amount") is not None:
                issues.append({"adset_id": a.get("adset_id"), "issue": "lowest_cost_requires_null_bid"})
            if bs in ("cost_cap", "bid_cap") and a.get("bid_amount") is None:
                issues.append({"adset_id": a.get("adset_id"), "issue": "missing_bid_amount"})
        if abs(s - float(total_budget)) > 1e-6:
            issues.append({"issue": "total_budget_mismatch", "provided": total_budget, "computed": s})
        if s > max_total:
            issues.append({"issue": "total_budget_exceeds_max", "provided": total_budget, "max": max_total})
        return json.dumps({"valid": len(issues) == 0, "issues": issues})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "validate_allocations_against_policy",
                                                 "description": "Validates a plan allocation list against policy.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"total_budget": {"type": "number"},
                                                                               "allocations": {"type": "array"}},
                                                                "required": ["total_budget", "allocations"]}}}


class GetCampaignByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        n = kwargs.get("name")
        for c in data.get("campaigns", []):
            if c.get("name") == n:
                return json.dumps(c)
        return json.dumps({"error": f"campaign {n} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_campaign_by_name", "description": "Retrieves a campaign by name.",
                             "parameters": {"type": "object", "properties": {"name": {"type": "string"}},
                                            "required": ["name"]}}}


class CreateCampaign(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        campaigns = data.get("campaigns", [])
        nid = max((int(c["campaign_id"]) for c in campaigns), default=0) + 1
        rec = {"campaign_id": str(nid), "name": kwargs.get("name"), "objective": kwargs.get("objective"),
               "created_date": kwargs.get("created_date"), "status": "paused"}
        campaigns.append(rec)
        data["campaigns"] = campaigns
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_campaign",
                                                 "description": "Creates a paused campaign with a provided created_date.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"name": {"type": "string"},
                                                                               "objective": {"type": "string"},
                                                                               "created_date": {"type": "string"}},
                                                                "required": ["name", "objective", "created_date"]}}}


class UpdateCampaignStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("campaign_id")
        st = kwargs.get("status")
        for c in data.get("campaigns", []):
            if c.get("campaign_id") == cid:
                c["status"] = st
                return json.dumps(c)
        return json.dumps({"error": f"campaign {cid} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "update_campaign_status", "description": "Updates campaign status.",
                             "parameters": {"type": "object", "properties": {"campaign_id": {"type": "string"},
                                                                             "status": {"type": "string"}},
                                            "required": ["campaign_id", "status"]}}}


class GetAdsetsByCampaignID(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("campaign_id")
        rows = [r for r in data.get("adsets", []) if r.get("campaign_id") == cid]
        return json.dumps({"adsets": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_adsets_by_campaign_id", "description": "Lists ad sets for a campaign.",
                             "parameters": {"type": "object", "properties": {"campaign_id": {"type": "string"}},
                                            "required": ["campaign_id"]}}}


class GetAdsetDetailsByID(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        for a in data.get("adsets", []):
            if a.get("adset_id") == aid:
                return json.dumps(a)
        return json.dumps({"error": f"adset {aid} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adset_details_by_id", "description": "Gets one ad set.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"}},
                                                                "required": ["adset_id"]}}}


class CreateAdset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adsets = data.get("adsets", [])
        nid = max((int(a["adset_id"]) for a in adsets), default=100) + 1
        rec = {"adset_id": str(nid), "campaign_id": kwargs.get("campaign_id"), "name": kwargs.get("name"),
               "category": kwargs.get("category"), "daily_budget": kwargs.get("daily_budget"),
               "bid_strategy": kwargs.get("bid_strategy"), "bid_amount": kwargs.get("bid_amount"), "status": "paused",
               "updated_at": kwargs.get("updated_at")}
        adsets.append(rec)
        data["adsets"] = adsets
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_adset", "description": "Creates a paused ad set.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"campaign_id": {"type": "string"},
                                                                               "name": {"type": "string"},
                                                                               "category": {"type": "string"},
                                                                               "daily_budget": {"type": "number"},
                                                                               "bid_strategy": {"type": "string"},
                                                                               "bid_amount": {"type": "number"},
                                                                               "updated_at": {"type": "string"}},
                                                                "required": ["campaign_id", "name", "category",
                                                                             "daily_budget", "bid_strategy",
                                                                             "updated_at"]}}}


class UpdateAdsetBudget(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        nb = float(kwargs.get("new_budget"))
        for a in data.get("adsets", []):
            if a.get("adset_id") == aid:
                a["daily_budget"] = nb
                a["updated_at"] = kwargs.get("updated_at")
                return json.dumps(a)
        return json.dumps({"error": f"adset {aid} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "update_adset_budget", "description": "Updates an ad set budget.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"},
                                                                             "new_budget": {"type": "number"},
                                                                             "updated_at": {"type": "string"}},
                                            "required": ["adset_id", "new_budget", "updated_at"]}}}


class UpdateAdsetBidStrategy(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        bs = kwargs.get("bid_strategy")
        ba = kwargs.get("bid_amount")
        for a in data.get("adsets", []):
            if a.get("adset_id") == aid:
                a["bid_strategy"] = bs
                a["bid_amount"] = ba
                a["updated_at"] = kwargs.get("updated_at")
                return json.dumps(a)
        return json.dumps({"error": f"adset {aid} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "update_adset_bid_strategy", "description": "Updates bid strategy and bid amount.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"},
                                                                             "bid_strategy": {"type": "string"},
                                                                             "bid_amount": {"type": ["number", "null"]},
                                                                             "updated_at": {"type": "string"}},
                                            "required": ["adset_id", "bid_strategy", "updated_at"]}}}


class GetAdsByAdsetID(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        rows = [r for r in data.get("ads", []) if r.get("adset_id") == aid]
        return json.dumps({"ads": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_ads_by_adset_id", "description": "Lists ads by ad set.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"}},
                                                                "required": ["adset_id"]}}}


class CreateAd(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ads = data.get("ads", [])
        nid = max((int(a["ad_id"]) for a in ads), default=1100) + 1
        rec = {"ad_id": str(nid), "adset_id": kwargs.get("adset_id"), "name": kwargs.get("name"),
               "creative_type": kwargs.get("creative_type"), "status": "paused", "start_date": kwargs.get("start_date"),
               "end_date": None}
        ads.append(rec)
        data["ads"] = ads
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "create_ad", "description": "Creates a paused ad in an ad set.",
                             "parameters": {"type": "object",
                                            "properties": {"adset_id": {"type": "string"}, "name": {"type": "string"},
                                                           "creative_type": {"type": "string"},
                                                           "start_date": {"type": "string"}},
                                            "required": ["adset_id", "name", "creative_type", "start_date"]}}}


class UpdateAdStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_id = kwargs.get("ad_id")
        st = kwargs.get("status")
        for ad in data.get("ads", []):
            if ad.get("ad_id") == ad_id:
                ad["status"] = st
                return json.dumps(ad)
        return json.dumps({"error": f"ad {ad_id} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_ad_status", "description": "Updates ad status.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"ad_id": {"type": "string"},
                                                                               "status": {"type": "string"}},
                                                                "required": ["ad_id", "status"]}}}


class RotateAdCreative(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        to_act = kwargs.get("ad_id_to_activate")
        to_pause = kwargs.get("ad_id_to_pause")
        ok_a = False
        ok_p = False
        for ad in data.get("ads", []):
            if ad.get("ad_id") == to_act:
                ad["status"] = "active"
                ok_a = True
            if ad.get("ad_id") == to_pause:
                ad["status"] = "paused"
                ok_p = True
        if ok_a and ok_p:
            return json.dumps({"status": "success"})
        return json.dumps({"error": "ids_not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "rotate_ad_creative", "description": "Activates one ad and pauses another.",
                             "parameters": {"type": "object", "properties": {"ad_id_to_activate": {"type": "string"},
                                                                             "ad_id_to_pause": {"type": "string"}},
                                            "required": ["ad_id_to_activate", "ad_id_to_pause"]}}}


class GetDailyInsightsForAdset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        d = kwargs.get("date")
        for i in data.get("f_insights", []):
            if i.get("adset_id") == aid and i.get("date") == d:
                return json.dumps(i)
        return json.dumps({"error": "insights_not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_daily_insights_for_adset",
                                                 "description": "Gets insights for one ad set on a date.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"},
                                                                               "date": {"type": "string"}},
                                                                "required": ["adset_id", "date"]}}}


class CalculateAdsetRoasForDay(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        d = kwargs.get("date")
        for i in data.get("f_insights", []):
            if i.get("adset_id") == aid and i.get("date") == d:
                spend = i.get("spend", 0)
                revenue = i.get("revenue", 0)
                roas = round(revenue / spend, 2) if spend > 0 else 0
                return json.dumps({"adset_id": aid, "date": d, "roas": roas})
        return json.dumps({"error": "roas_not_available"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "calculate_adset_roas_for_day", "description": "Computes ROAS for one day.",
                             "parameters": {"type": "object",
                                            "properties": {"adset_id": {"type": "string"}, "date": {"type": "string"}},
                                            "required": ["adset_id", "date"]}}}


class ComputeCtrForAdsetDay(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        d = kwargs.get("date")
        for i in data.get("f_insights", []):
            if i.get("adset_id") == aid and i.get("date") == d:
                imp = i.get("impressions", 0)
                clk = i.get("clicks", 0)
                ctr = round(clk / imp, 4) if imp > 0 else 0
                return json.dumps({"adset_id": aid, "date": d, "ctr": ctr})
        return json.dumps({"error": "ctr_not_available"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "compute_ctr_for_adset_day", "description": "Computes CTR for one day.",
                             "parameters": {"type": "object",
                                            "properties": {"adset_id": {"type": "string"}, "date": {"type": "string"}},
                                            "required": ["adset_id", "date"]}}}


class GetAdsetSpendForDateRange(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("adset_id")
        s = kwargs.get("start_date")
        e = kwargs.get("end_date")
        sd = datetime.strptime(s, "%Y-%m-%d").date()
        ed = datetime.strptime(e, "%Y-%m-%d").date()
        tot = 0.0
        for i in data.get("f_insights", []):
            if i.get("adset_id") == aid:
                idate = datetime.strptime(i.get("date"), "%Y-%m-%d").date()
                if sd <= idate <= ed:
                    tot += float(i.get("spend", 0))
        return json.dumps({"adset_id": aid, "start_date": s, "end_date": e, "total_spend": round(tot, 2)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_adset_spend_for_date_range", "description": "Sums spend for a date range.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"},
                                                                             "start_date": {"type": "string"},
                                                                             "end_date": {"type": "string"}},
                                            "required": ["adset_id", "start_date", "end_date"]}}}


class GetWeeklySalesByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cat = kwargs.get("category")
        start = kwargs.get("start_date")
        for r in data.get("f_sales", []):
            if r.get("category") == cat and r.get("start_date") == start:
                return json.dumps(r)
        return json.dumps({"error": "sales_not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_weekly_sales_by_category", "description": "Gets weekly sales for a category.",
                             "parameters": {"type": "object", "properties": {"category": {"type": "string"},
                                                                             "start_date": {"type": "string"}},
                                            "required": ["category", "start_date"]}}}


class GetViewershipForCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cat = kwargs.get("category")
        d = kwargs.get("date")
        for r in data.get("f_viewership", []):
            if r.get("category") == cat and r.get("date") == d:
                return json.dumps(r)
        return json.dumps({"error": "viewership_not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_viewership_for_category",
                                                 "description": "Gets viewership for a category on a date.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"category": {"type": "string"},
                                                                               "date": {"type": "string"}},
                                                                "required": ["category", "date"]}}}


class GetProductPriceOnDate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pid = kwargs.get("product_id")
        d = kwargs.get("date")
        for r in data.get("f_price", []):
            if r.get("product_id") == pid and r.get("date") == d:
                return json.dumps(r)
        return json.dumps({"error": "price_not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_product_price_on_date", "description": "Gets product price on a date.",
                             "parameters": {"type": "object", "properties": {"product_id": {"type": "string"},
                                                                             "date": {"type": "string"}},
                                            "required": ["product_id", "date"]}}}


class FindUnderperformingAdsets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        th = float(kwargs.get("roas_threshold"))
        d = kwargs.get("date")
        out = []
        for i in data.get("f_insights", []):
            if i.get("date") == d:
                spend = i.get("spend", 0)
                revenue = i.get("revenue", 0)
                roas = (revenue / spend) if spend > 0 else 0
                if spend > 0 and roas < th:
                    out.append({"adset_id": i.get("adset_id"), "roas": round(roas, 2)})
        return json.dumps({"underperforming_adsets": out})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_underperforming_adsets",
                                                 "description": "Finds ad sets below a ROAS threshold for a day.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"roas_threshold": {"type": "number"},
                                                                               "date": {"type": "string"}},
                                                                "required": ["roas_threshold", "date"]}}}


class CreateAutomationRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rec = {"run_id": kwargs.get("run_id"), "run_type": kwargs.get("run_type"),
               "started_at": kwargs.get("started_at"), "ended_at": kwargs.get("ended_at"),
               "status": kwargs.get("status"), "input_ref": kwargs.get("input_ref"),
               "errors_json": kwargs.get("errors_json")}
        data.setdefault("automation_runs", []).append(rec)
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "create_automation_run", "description": "Creates an automation run record.",
                             "parameters": {"type": "object",
                                            "properties": {"run_id": {"type": "string"}, "run_type": {"type": "string"},
                                                           "started_at": {"type": "string"},
                                                           "ended_at": {"type": "string"}, "status": {"type": "string"},
                                                           "input_ref": {"type": "string"},
                                                           "errors_json": {"type": "string"}},
                                            "required": ["run_id", "run_type", "started_at", "ended_at", "status",
                                                         "input_ref", "errors_json"]}}}


class GetAutomationRunHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rtype = kwargs.get("run_type")
        status = kwargs.get("status")
        limit = int(kwargs.get("limit", 10))
        runs = data.get("automation_runs", [])
        if rtype:
            runs = [r for r in runs if r.get("run_type") == rtype]
        if status:
            runs = [r for r in runs if r.get("status") == status]
        runs.sort(key=lambda x: x.get("started_at", ""), reverse=True)
        runs = runs[:limit]
        total = len(runs)
        succ = len([r for r in runs if r.get("status") == "completed"])
        fail = len([r for r in runs if r.get("status") == "failed"])
        rate = round((succ / total * 100), 2) if total > 0 else 0
        return json.dumps({"summary": {"total_runs": total, "success_count": succ, "failure_count": fail,
                                       "success_rate_percent": rate}, "runs": runs})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_automation_run_history", "description": "Gets automation runs with summary.",
                             "parameters": {"type": "object",
                                            "properties": {"run_type": {"type": "string"}, "status": {"type": "string"},
                                                           "limit": {"type": "number"}}, "required": []}}}


class UpdateAutomationRunEnd(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rid = kwargs.get("run_id")
        st = kwargs.get("status")
        ea = kwargs.get("ended_at")
        for r in data.get("automation_runs", []):
            if r.get("run_id") == rid:
                r["status"] = st
                r["ended_at"] = ea
                return json.dumps(r)
        return json.dumps({"error": f"run {rid} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_automation_run_end",
                                                 "description": "Sets final status and end time for a run.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"run_id": {"type": "string"},
                                                                               "status": {"type": "string"},
                                                                               "ended_at": {"type": "string"}},
                                                                "required": ["run_id", "status", "ended_at"]}}}


class GetLastSuccessfulRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rtype = kwargs.get("run_type")
        runs = [r for r in data.get("automation_runs", []) if
                r.get("run_type") == rtype and r.get("status") == "completed"]
        if not runs:
            return json.dumps({"error": f"no successful run for {rtype}"})
        last = max(runs, key=lambda x: x.get("ended_at", ""))
        return json.dumps(last)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_last_successful_run",
                                                 "description": "Gets most recent successful run of a type.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"run_type": {"type": "string"}},
                                                                "required": ["run_type"]}}}


class LogBudgetChange(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = data.get("budget_changes", [])
        nid = f"BC-{max((int(r['change_id'][3:]) for r in rows), default=0) + 1}"
        rec = {"change_id": nid, "adset_id": kwargs.get("adset_id"), "old_budget": kwargs.get("old_budget"),
               "new_budget": kwargs.get("new_budget"), "changed_at": kwargs.get("changed_at"),
               "reason": kwargs.get("reason")}
        rows.append(rec)
        data["budget_changes"] = rows
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "log_budget_change", "description": "Appends a budget change log entry.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"},
                                                                             "old_budget": {"type": "number"},
                                                                             "new_budget": {"type": "number"},
                                                                             "changed_at": {"type": "string"},
                                                                             "reason": {"type": "string"}},
                                            "required": ["adset_id", "old_budget", "new_budget", "changed_at",
                                                         "reason"]}}}


class LogStrategyChange(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = data.get("strategy_changes", [])
        nid = f"SC-{max((int(r['change_id'][3:]) for r in rows), default=0) + 1}"
        rec = {"change_id": nid, "adset_id": kwargs.get("adset_id"), "old_strategy": kwargs.get("old_strategy"),
               "new_strategy": kwargs.get("new_strategy"), "old_bid": kwargs.get("old_bid"),
               "new_bid": kwargs.get("new_bid"), "changed_at": kwargs.get("changed_at"), "reason": kwargs.get("reason")}
        rows.append(rec)
        data["strategy_changes"] = rows
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "log_strategy_change", "description": "Appends a strategy change log entry.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"},
                                                                             "old_strategy": {"type": "string"},
                                                                             "new_strategy": {"type": "string"},
                                                                             "old_bid": {"type": ["number", "null"]},
                                                                             "new_bid": {"type": ["number", "null"]},
                                                                             "changed_at": {"type": "string"},
                                                                             "reason": {"type": "string"}},
                                            "required": ["adset_id", "old_strategy", "new_strategy", "old_bid",
                                                         "new_bid", "changed_at", "reason"]}}}


class LogCreativeRotation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = data.get("creative_rotations", [])
        nid = f"CR-{max((int(r['rotation_id'][3:]) for r in rows), default=0) + 1}"
        rec = {"rotation_id": nid, "adset_id": kwargs.get("adset_id"), "old_ad_id": kwargs.get("old_ad_id"),
               "new_ad_id": kwargs.get("new_ad_id"), "rotated_at": kwargs.get("rotated_at"),
               "rationale": kwargs.get("rationale")}
        rows.append(rec)
        data["creative_rotations"] = rows
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "log_creative_rotation", "description": "Appends a creative rotation log entry.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"},
                                                                             "old_ad_id": {"type": "string"},
                                                                             "new_ad_id": {"type": "string"},
                                                                             "rotated_at": {"type": "string"},
                                                                             "rationale": {"type": "string"}},
                                            "required": ["adset_id", "old_ad_id", "new_ad_id", "rotated_at",
                                                         "rationale"]}}}


class GetProductByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        n = kwargs.get("product_name")
        for p in data.get("dim_product", []):
            if p.get("name") == n:
                return json.dumps(p)
        return json.dumps({"error": f"product {n} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_product_by_name", "description": "Looks up a product by name.",
                             "parameters": {"type": "object", "properties": {"product_name": {"type": "string"}},
                                            "required": ["product_name"]}}}


class GetAdsetsByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        c = kwargs.get("category")
        rows = [r for r in data.get("adsets", []) if r.get("category") == c]
        return json.dumps({"adsets": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_adsets_by_category", "description": "Lists ad sets by category.",
                             "parameters": {"type": "object", "properties": {"category": {"type": "string"}},
                                            "required": ["category"]}}}


class CreatePlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rec = {"plan_id": kwargs.get("plan_id"), "date": kwargs.get("date"), "total_budget": kwargs.get("total_budget"),
               "author": kwargs.get("author"), "created_at": kwargs.get("created_at"),
               "checksum": kwargs.get("checksum"), "allocations": kwargs.get("allocations", [])}
        data.setdefault("plans", []).append(rec)
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "create_plan", "description": "Creates a plan with allocations.",
                             "parameters": {"type": "object",
                                            "properties": {"plan_id": {"type": "string"}, "date": {"type": "string"},
                                                           "total_budget": {"type": "number"},
                                                           "author": {"type": "string"},
                                                           "created_at": {"type": "string"},
                                                           "checksum": {"type": "string"},
                                                           "allocations": {"type": "array"}},
                                            "required": ["plan_id", "date", "total_budget", "author", "created_at",
                                                         "checksum", "allocations"]}}}


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
    CreatePlan()
]
