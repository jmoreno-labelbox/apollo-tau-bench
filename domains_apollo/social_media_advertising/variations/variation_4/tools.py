import json
from datetime import datetime
from typing import Any

from domains.dto import Tool

#==============================================================================
#1. Tools for Planning & Policy
#==============================================================================


class GetPlanForDate(Tool):
    """Fetches the complete frozen plan for a given date."""

    @staticmethod
    def invoke(data: dict[str, Any], date: str = None) -> str:
        report_date = date
        for plan in data.get("plans", []):
            if plan.get("date") == report_date:
                payload = plan
                out = json.dumps(payload)
                return out
        payload = {"error": f"Plan for date '{report_date}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPlanForDate",
                "description": "Retrieves the entire frozen plan for a specific date, including total budget and all ad set allocations.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "The date of the plan in YYYY-MM-DD format.",
                        }
                    },
                    "required": ["date"],
                },
            },
        }


class GetAdsetAllocationFromPlan(Tool):
    """Obtains the allocation of a specific ad set from a plan."""

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, adset_id: str = None) -> str:
        for plan in data.get("plans", []):
            if plan.get("plan_id") == plan_id:
                for allocation in plan.get("allocations", []):
                    if allocation.get("adset_id") == adset_id:
                        payload = allocation
                        out = json.dumps(payload)
                        return out
        payload = {
                "error": f"Allocation for ad set '{adset_id}' not found in plan '{plan_id}'."
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetAllocationFromPlan",
                "description": "Gets the planned budget, bid, and creative strategy for a single ad set from a specific plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The ID of the plan (e.g., 'plan_2025-08-13').",
                        },
                        "adset_id": {
                            "type": "string",
                            "description": "The ID of the ad set to look up.",
                        },
                    },
                    "required": ["plan_id", "adset_id"],
                },
            },
        }


class GetPolicyParameter(Tool):
    """Fetches the value associated with a specific business rule."""

    @staticmethod
    def invoke(data: dict[str, Any], param_name: str = None) -> str:
        for param in data.get("policy_params", []):
            if param.get("param_name") == param_name:
                payload = param
                out = json.dumps(payload)
                return out
        payload = {"error": f"Policy parameter '{param_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyParameter",
                "description": "Retrieves the value of a specific business rule, like 'max_bid_amount'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "param_name": {
                            "type": "string",
                            "description": "The name of the policy parameter to retrieve.",
                        }
                    },
                    "required": ["param_name"],
                },
            },
        }


#==============================================================================
#2. Tools for Campaign Management
#==============================================================================


class GetCampaignByName(Tool):
    """Obtains the details of a campaign using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        for campaign in data.get("campaigns", []):
            if campaign.get("name") == name:
                payload = campaign
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign '{name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCampaignByName",
                "description": "Find a specific campaign by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of the campaign.",
                        }
                    },
                    "required": ["name"],
                },
            },
        }


class CreateCampaign(Tool):
    """Initiates a new advertising campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, objective: str = None) -> str:
        campaigns = data.get("campaigns", [])
        new_id = max((int(c["campaign_id"]) for c in campaigns), default=0) + 1
        new_campaign = {
            "campaign_id": str(new_id),
            "name": name,
            "objective": objective,
            "created_date": "2025-08-15",
            "status": "paused",
        }
        campaigns.append(new_campaign)
        data["campaigns"] = campaigns
        payload = new_campaign
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCampaign",
                "description": "Creates a new advertising campaign. New campaigns always start with a 'paused' status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "objective": {"type": "string"},
                    },
                    "required": ["name", "objective"],
                },
            },
        }


class UpdateCampaignStatus(Tool):
    """Modifies the status of a campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, status: str = None) -> str:
        for campaign in data.get("campaigns", []):
            if campaign.get("campaign_id") == campaign_id:
                campaign["status"] = status
                payload = campaign
                out = json.dumps(payload)
                return out
        payload = {"error": f"Campaign ID '{campaign_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCampaignStatus",
                "description": "Updates the status of a campaign (e.g., 'active', 'paused', 'archived').",
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
    """Fetches all ad sets associated with a particular campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None) -> str:
        adsets = [
            adset
            for adset in data.get("adsets", [])
            if adset.get("campaign_id") == campaign_id
        ]
        payload = {"adsets": adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetsByCampaignId",
                "description": "Retrieves a list of all ad sets that belong to a specific campaign ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"campaign_id": {"type": "string"}},
                    "required": ["campaign_id"],
                },
            },
        }


#==============================================================================
#3. Tools for Ad Set & Ad Management
#==============================================================================


class GetAdsetDetailsByID(Tool):
    """Obtains the details for an individual ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        for adset in data.get("adsets", []):
            if adset.get("adset_id") == adset_id:
                payload = adset
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetDetailsById",
                "description": "Retrieves the full details for a single ad set using its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }


class CreateAdset(Tool):
    """Initiates a new ad set inside a campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, name: str = None, category: str = None, 
               daily_budget: float = None, bid_strategy: str = None, bid_amount: float = None,
               request_id: Any = None,
               status: Any = None,
               ) -> str:
        adsets = data.get("adsets", [])
        new_id = max((int(a["adset_id"]) for a in adsets), default=100) + 1
        new_adset = {
            "adset_id": str(new_id),
            "campaign_id": campaign_id,
            "name": name,
            "category": category,
            "daily_budget": daily_budget,
            "bid_strategy": bid_strategy,
            "bid_amount": bid_amount,
            "status": "paused",
            "updated_at": "2025-08-15T00:00:00Z",
        }
        adsets.append(new_adset)
        data["adsets"] = adsets
        payload = new_adset
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAdset",
                "description": "Creates a new ad set within a specified campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "name": {"type": "string"},
                        "category": {"type": "string"},
                        "daily_budget": {"type": "number"},
                        "bid_strategy": {"type": "string"},
                        "bid_amount": {"type": "number"},
                    },
                    "required": [
                        "campaign_id",
                        "name",
                        "category",
                        "daily_budget",
                        "bid_strategy",
                    ],
                },
            },
        }


class UpdateAdsetBudget(Tool):
    """Modifies the daily budget for an ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, new_budget: float = None) -> str:
        for adset in data.get("adsets", []):
            if adset.get("adset_id") == adset_id:
                adset["daily_budget"] = new_budget
                payload = adset
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdsetBudget",
                "description": "Updates the daily budget for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_budget": {"type": "number"},
                    },
                    "required": ["adset_id", "new_budget"],
                },
            },
        }


class UpdateAdsetBidStrategy(Tool):
    """Alters the bid strategy of an ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, bid_strategy: str = None, bid_amount: float = None) -> str:
        for adset in data.get("adsets", []):
            if adset.get("adset_id") == adset_id:
                adset["bid_strategy"] = bid_strategy
                adset["bid_amount"] = bid_amount
                payload = adset
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdsetBidStrategy",
                "description": "Updates the bidding strategy and bid amount for a given ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "bid_strategy": {"type": "string"},
                        "bid_amount": {"type": "number"},
                    },
                    "required": ["adset_id", "bid_strategy"],
                },
            },
        }


class GetAdsByAdsetID(Tool):
    """Fetches all ads contained in a particular ad set."""

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
                "name": "GetAdsByAdsetId",
                "description": "Retrieves a list of all ads that belong to a specific ad set ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }


class CreateAd(Tool):
    """Initiates a new ad creative."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, name: str = None, creative_type: str = None, status: str = None, request_id: str = None) -> str:
        ads = data.get("ads", [])
        new_id = max((int(a["ad_id"]) for a in ads), default=1100) + 1
        new_ad = {
            "ad_id": str(new_id),
            "adset_id": adset_id,
            "name": name,
            "creative_type": creative_type,
            "status": status if status is not None else "paused",
            "start_date": "2025-08-15",
            "end_date": None,
        }
        ads.append(new_ad)
        data["ads"] = ads
        payload = new_ad
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAd",
                "description": "Creates a new ad within a specified ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "name": {"type": "string"},
                        "creative_type": {"type": "string"},
                    },
                    "required": ["adset_id", "name", "creative_type"],
                },
            },
        }


class UpdateAdStatus(Tool):
    """Modifies the status of a single ad."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str = None, status: str = None, request_id: Any = None,
    timestamp: Any = None,
    ) -> str:
        for ad in data.get("ads", []):
            if ad.get("ad_id") == ad_id:
                ad["status"] = status
                payload = ad
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad ID '{ad_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdStatus",
                "description": "Updates the status of a single ad (e.g., 'active', 'paused').",
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
    """Suspends one ad while enabling another."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id_to_activate: str = None, ad_id_to_pause: str = None, timestamp: Any = None) -> str:
        ad_to_activate, ad_to_pause = ad_id_to_activate, ad_id_to_pause
        activated, paused = False, False
        for ad in data.get("ads", []):
            if ad.get("ad_id") == ad_to_activate:
                ad["status"], activated = "active", True
            if ad.get("ad_id") == ad_to_pause:
                ad["status"], paused = "paused", True
        if activated and paused:
            payload = {"status": "success"}
            out = json.dumps(payload)
            return out
        payload = {"error": "One or both ad IDs not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RotateAdCreative",
                "description": "Activates one ad and pauses another, effectively rotating the active creative.",
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


#==============================================================================
#4. Tools for Performance & Analytics
#==============================================================================


class GetDailyInsightsForAdset(Tool):
    """Fetches performance metrics related to an ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None) -> str:
        for insight in data.get("f_insights", []):
            if (
                insight.get("adset_id") == adset_id
                and insight.get("date") == date
            ):
                payload = insight
                out = json.dumps(payload)
                return out
        payload = {"error": "Insights not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDailyInsightsForAdset",
                "description": "Retrieves performance insights (spend, clicks, revenue) for one ad set on a specific date.",
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
    """Computes Return On Ad Spend for an ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, date: str = None) -> str:
        for insight in data.get("f_insights", []):
            if (
                insight.get("adset_id") == adset_id
                and insight.get("date") == date
            ):
                spend, revenue = insight.get("spend", 0), insight.get("revenue", 0)
                roas = round(revenue / spend, 2) if spend > 0 else 0
                payload = {"adset_id": adset_id, "roas": roas}
                out = json.dumps(payload)
                return out
        payload = {"error": "Could not calculate ROAS, insights not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateAdsetRoasForDay",
                "description": "Calculates the Return On Ad Spend (Revenue / Spend) for an ad set on a specific date.",
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
    """Computes total expenditure for an ad set across a range."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, start_date: str = None, end_date: str = None) -> str:
        start, end = (
            datetime.strptime(start_date, "%Y-%m-%d").date(),
            datetime.strptime(end_date, "%Y-%m-%d").date(),
        )
        total_spend = sum(
            i.get("spend", 0)
            for i in data.get("f_insights", [])
            if i.get("adset_id") == adset_id
            and start <= datetime.strptime(i["date"], "%Y-%m-%d").date() <= end
        )
        payload = {
                "adset_id": adset_id,
                "start_date": start_date,
                "end_date": end_date,
                "total_spend": round(total_spend, 2),
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
                "description": "Calculates the total ad spend for a single ad set over an inclusive date range.",
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
    """Fetches weekly sales data for a category."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, start_date: str = None) -> str:
        for record in data.get("f_sales", []):
            if (
                record.get("category") == category
                and record.get("start_date") == start_date
            ):
                payload = record
                out = json.dumps(payload)
                return out
        payload = {"error": "Sales data not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWeeklySalesByCategory",
                "description": "Retrieves the units sold and revenue for a product category for a specific week.",
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
    """Obtains user engagement statistics for a category."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, report_date: str = None,
    date: Any = None,
    ) -> str:
        for record in data.get("f_viewership", []):
            if record.get("category") == category and record.get("date") == report_date:
                payload = record
                out = json.dumps(payload)
                return out
        payload = {"error": "Viewership data not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetViewershipForCategory",
                "description": "Retrieves user session and engagement data for a category on a specific date.",
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
    """Finds the price of a product on a given date."""

    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None, query_date: str = None, date: Any = None) -> str:
        for entry in data.get("f_price", []):
            if (
                entry.get("product_id") == product_id
                and entry.get("date") == query_date
            ):
                payload = entry
                out = json.dumps(payload)
                return out
        payload = {"error": "Price not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductPriceOnDate",
                "description": "Retrieves the price of a specific product on a given date.",
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
    """Identifies ad sets that fall below a specific ROAS threshold."""

    @staticmethod
    def invoke(data: dict[str, Any], roas_threshold: float = None, date: str = None) -> str:
        adsets = []
        for i in data.get("f_insights", []):
            if i.get("date") == date:
                spend, revenue = i.get("spend", 0), i.get("revenue", 0)
                roas = (revenue / spend) if spend > 0 else 0
                if spend > 0 and roas < roas_threshold:
                    adsets.append({"adset_id": i["adset_id"], "roas": round(roas, 2)})
        payload = {"underperforming_adsets": adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindUnderperformingAdsets",
                "description": "Finds all ad sets with a ROAS below a specified threshold for a given day.",
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


#==============================================================================
#5. Tools for Auditing & Logging
#==============================================================================


class GetAutomationRunHistory(Tool):
    """Fetches the history of automation runs for review and monitoring."""

    @staticmethod
    def invoke(data: dict[str, Any], run_type: str = None, status: str = None, limit: int = 10) -> str:
        runs = data.get("automation_runs", [])

        # Apply filter based on run type if provided
        if run_type:
            runs = [r for r in runs if r.get("run_type") == run_type]

        # Apply filter based on status if provided
        if status:
            runs = [r for r in runs if r.get("status") == status]

        # Order by started_at (latest first) and restrict results
        runs.sort(key=lambda x: x.get("started_at", ""), reverse=True)
        runs = runs[:limit]

        # Compute summary statistics
        total_runs = len(runs)
        success_count = len([r for r in runs if r.get("status") == "completed"])
        failure_count = len([r for r in runs if r.get("status") == "failed"])
        success_rate = (
            round((success_count / total_runs * 100), 2) if total_runs > 0 else 0
        )

        result = {
            "summary": {
                "total_runs": total_runs,
                "success_count": success_count,
                "failure_count": failure_count,
                "success_rate_percent": success_rate,
            },
            "runs": runs,
        }
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAutomationRunHistory",
                "description": "Retrieves automation run history with filtering and summary statistics for monitoring and analysis.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_type": {
                            "type": "string",
                            "description": "Filter by specific automation type (e.g., 'plan_freeze', 'budget_apply').",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by run status (e.g., 'completed', 'failed', 'started').",
                        },
                        "limit": {
                            "type": "number",
                            "description": "Maximum number of runs to return (default: 10).",
                        },
                    },
                    "required": [],
                },
            },
        }


class GetLastSuccessfulRun(Tool):
    """Determines the last successful completion time of a job type."""

    @staticmethod
    def invoke(data: dict[str, Any], run_type: str = None) -> str:
        successful_runs = [
            r
            for r in data.get("automation_runs", [])
            if r.get("run_type") == run_type and r.get("status") == "completed"
        ]
        if not successful_runs:
            payload = {"error": f"No successful run found for type '{run_type}'."}
            out = json.dumps(payload)
            return out
        last_run = max(successful_runs, key=lambda x: x["ended_at"])
        payload = last_run
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLastSuccessfulRun",
                "description": "Reads the automation log to find when a specific job type last completed successfully.",
                "parameters": {
                    "type": "object",
                    "properties": {"run_type": {"type": "string"}},
                    "required": ["run_type"],
                },
            },
        }


class LogBudgetChange(Tool):
    """Records an entry in the budget change log."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, old_budget: float = None, new_budget: float = None, reason: str = None) -> str:
        changes = data.get("budget_changes", [])
        new_id = f"BC-{max((int(c['change_id'][3:]) for c in changes), default=0) + 1}"
        new_log = {
            "change_id": new_id,
            "adset_id": adset_id,
            "old_budget": old_budget,
            "new_budget": new_budget,
            "changed_at": "2025-08-15T01:00:00Z",
            "reason": reason,
        }
        changes.append(new_log)
        data["budget_changes"] = changes
        payload = new_log
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogBudgetChange",
                "description": "Writes an audit log entry for an ad set budget change.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "old_budget": {"type": "number"},
                        "new_budget": {"type": "number"},
                        "reason": {"type": "string"},
                    },
                    "required": ["adset_id", "old_budget", "new_budget", "reason"],
                },
            },
        }


class LogStrategyChange(Tool):
    """Records an entry in the bid strategy change log."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str = None,
        old_strategy: str = None,
        new_strategy: str = None,
        old_bid: float = None,
        new_bid: float = None,
        reason: str = None
,
    change_id: Any = None,
    ) -> str:
        changes = data.get("strategy_changes", [])
        new_id = f"SC-{max((int(c['change_id'][3:]) for c in changes), default=0) + 1}"
        new_log = {
            "change_id": new_id,
            "adset_id": adset_id,
            "old_strategy": old_strategy,
            "new_strategy": new_strategy,
            "old_bid": old_bid,
            "new_bid": new_bid,
            "changed_at": "2025-08-15T02:00:00Z",
            "reason": reason,
        }
        changes.append(new_log)
        data["strategy_changes"] = changes
        payload = new_log
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogStrategyChange",
                "description": "Writes an audit log entry for an ad set bid strategy change.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "old_strategy": {"type": "string"},
                        "new_strategy": {"type": "string"},
                        "old_bid": {"type": "number"},
                        "new_bid": {"type": "number"},
                        "reason": {"type": "string"},
                    },
                    "required": [
                        "adset_id",
                        "old_strategy",
                        "new_strategy",
                        "old_bid",
                        "new_bid",
                        "reason",
                    ],
                },
            },
        }


class LogCreativeRotation(Tool):
    """Records an entry in the creative rotation log."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str = None,
        old_ad_id: str = None,
        new_ad_id: str = None,
        rationale: str = None, change_id: Any = None) -> str:
        rotations = data.get("creative_rotations", [])
        new_id = (
            f"CR-{max((int(c['rotation_id'][3:]) for c in rotations), default=0) + 1}"
        )
        new_log = {
            "rotation_id": new_id,
            "adset_id": adset_id,
            "old_ad_id": old_ad_id,
            "new_ad_id": new_ad_id,
            "rotated_at": "2025-08-15T03:00:00Z",
            "rationale": rationale,
        }
        rotations.append(new_log)
        data["creative_rotations"] = rotations
        payload = new_log
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogCreativeRotation",
                "description": "Writes an audit log entry for an ad creative rotation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "old_ad_id": {"type": "string"},
                        "new_ad_id": {"type": "string"},
                        "rationale": {"type": "string"},
                    },
                    "required": ["adset_id", "old_ad_id", "new_ad_id", "rationale"],
                },
            },
        }


#==============================================================================
#6. Tools for Data Lookup
#==============================================================================


class GetAdsetsByCategory(Tool):
    """Identifies ad sets aimed at a particular product category."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None) -> str:
        adsets = [
            adset
            for adset in data.get("adsets", [])
            if adset.get("category") == category
        ]
        payload = {"adsets": adsets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetsByCategory",
                "description": "Retrieves a list of ad sets that are targeting a specific product category.",
                "parameters": {
                    "type": "object",
                    "properties": {"category": {"type": "string"}},
                    "required": ["category"],
                },
            },
        }


#==============================================================================
#Complete list of all 28 tools accessible to the agent
#==============================================================================

TOOLS = [
    #Planning & Policy
    GetPlanForDate(),
    GetAdsetAllocationFromPlan(),
    GetPolicyParameter(),
    #Campaign Management
    GetCampaignByName(),
    CreateCampaign(),
    UpdateCampaignStatus(),
    GetAdsetsByCampaignID(),
    #Ad Set & Ad Management
    GetAdsetDetailsByID(),
    CreateAdset(),
    UpdateAdsetBudget(),
    UpdateAdsetBidStrategy(),
    GetAdsByAdsetID(),
    CreateAd(),
    UpdateAdStatus(),
    RotateAdCreative(),
    #Performance & Analytics
    GetDailyInsightsForAdset(),
    CalculateAdsetRoasForDay(),
    GetAdsetSpendForDateRange(),
    GetWeeklySalesByCategory(),
    GetViewershipForCategory(),
    GetProductPriceOnDate(),
    FindUnderperformingAdsets(),
    #Auditing & Logging
    GetAutomationRunHistory(),
    GetLastSuccessfulRun(),
    LogBudgetChange(),
    LogStrategyChange(),
    LogCreativeRotation(),
    #Data Lookups
    GetAdsetsByCategory(),
]
